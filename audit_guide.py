from pathlib import Path
import runpy,re,sys,collections
ROOT=Path(__file__).parent
ns=runpy.run_path(str(ROOT/'finalize_guide.py'))
entries=ns['entries'];platforms=ns['platforms'];short=ns['short'];gc=ns['gc'];mb=ns['mb']
text=(ROOT/'batocera_rom_guide.md').read_text()
errors=[];warnings=[]
def check(ok,msg):
    if not ok:errors.append(msg)

# 数据层完整性。
check(len(platforms)==18,f'平台数不是 18：{len(platforms)}')
for p in platforms:
    es=[e for e in entries if e.platform==p]
    check(bool(es),f'空平台：{p}')
    check(f'### {p}\n' in text,f'缺平台章节：{p}')
ids=[e.eid for e in entries]
check(len(ids)==len(set(ids)),'条目 ID 重复')
seen=collections.Counter((e.platform,e.en) for e in entries)
for k,n in seen.items():
    if n>1:errors.append(f'同平台重复商品：{k} × {n}')
allowed_categories={'平台动作','动作冒险','射击（STG）','动作射击','格斗／清版动作','角色扮演','战略／战棋','竞速／体育','益智／休闲','模拟／音乐／派对'}
for e in entries:
    for field in ('year','pub','size','note','category','subgenre'):
        check(bool(getattr(e,field)),f'{e.eid} 缺 {field}：{e.en}')
    check(e.year==e.year.strip(),f'{e.eid} 年份有空格')
    check(re.search(r'\d{4}',e.year) is not None,f'{e.eid} 年份异常：{e.year}')
    check(e.note==e.note.strip(),f'{e.eid} 备注首尾空格')
    check(e.category in allowed_categories,f'{e.eid} 主品类异常：{e.category}')
    check(e.series not in {'最终幻想'} or not re.search(r'Tactics Ogre|Ogre Battle',e.en),f'皇家骑士团误入最终幻想：{e.en}')
    check(e.series not in {'皇家骑士团'} or not re.search(r'Final Fantasy',e.en),f'最终幻想误入皇家骑士团：{e.en}')
    check(e.series not in {'宝可梦'} or 'Metal Max' not in e.en,f'重装机兵误入宝可梦：{e.en}')

# Markdown 条目行与 Typora 原生标题回链，不使用 HTML 锚点。
rows=[]
for line in text.splitlines():
    m=re.match(r'^\| ([A-Z0-9]+-\d{3}) \|',line)
    if not m:continue
    cells=[c.strip() for c in line.strip().strip('|').split('|')]
    check(len(cells)==8,f'条目列数不是 8：{line[:100]}')
    if len(cells)==8:rows.append((m.group(1).lower(),*cells[1:]))
check(len(rows)==len(entries),f'Markdown 条目行 {len(rows)} != 数据条目 {len(entries)}')
anchors=re.findall(r'<a id="([^"]+)"></a>',text)
check(not anchors,'Typora 原生版仍含 HTML 锚点：'+str(anchors[:10]))
def slug(title):
    title=re.sub(r'[^\w\- ]','',title.strip().lower(),flags=re.UNICODE)
    return re.sub(r' +','-',title)
heading_anchors={slug(h) for h in re.findall(r'^#{1,6} +(.+)$',text,re.M)}
links=re.findall(r'\]\(#([^)]+)\)',text)
missing=sorted(set(links)-heading_anchors)
check(not missing,'失效内部链接：'+str(missing))
series_id=ns['series_id'];series_counts=ns['series_counts']
for e in entries:
    sid=series_id.get(e.series)
    if e.series and series_counts[e.series]>=2:
        check(bool(sid),f'{e.eid} 系列无原生标题 ID：{e.series}')
        if sid:
            row=next((r[7] for r in rows if r[0]==e.eid.lower()),'')
            check(f'[系列专题](#{sid})' in row,f'{e.eid} 缺系列回链')
            check(sid in heading_anchors,f'{e.eid} 系列标题锚点缺失：{sid}')
            check(ns['entry_link'](e) in text,f'{e.eid} 缺平台原生回链')
    else:
        check(not sid,f'单成员系列不应设专题：{e.series}')
        check(f'### {e.series}\n' not in text if e.series else True,f'单成员系列仍有章节：{e.series}')

# 三张平台表顺序一致，厂家矩阵与数据一致。
expected_overview=['DOS／Win3.x','Win95／98（Wine）','MAME','FBNeo','NES／FC','PCE','MD／Genesis','GB','GG','SNES／SFC','N64','PS1','GBC','Dreamcast','WS／WSC','GBA','NDS','PSP']
overview=text.split('## 平台、硬件、模拟器与容量汇总',1)[-1].split('### 容量、出品方与存储汇总',1)[0]
overview_order=[]
for line in overview.splitlines():
    cells=[c.strip() for c in line.strip().strip('|').split('|')]
    if cells and cells[0] in expected_overview:overview_order.append(cells[0])
check(overview_order==expected_overview,f'硬件总览顺序不符：{overview_order}')
capacity=text.split('### 容量、出品方与存储汇总',1)[-1].split('#### 游戏总数与总容量',1)[0]
capacity_lines=capacity.splitlines()
header_i=next((i for i,line in enumerate(capacity_lines) if line.startswith('| 平台 | 条目数 |')),None)
check(header_i is not None,'容量汇总缺表头')
if header_i is not None:
    header_cells=[c.strip() for c in capacity_lines[header_i].strip().strip('|').split('|')]
    divider_cells=[c.strip() for c in capacity_lines[header_i+1].strip().strip('|').split('|')]
    check(len(header_cells)==11 and len(divider_cells)==11,f'容量汇总表头／分隔行列数不符：{len(header_cells)}／{len(divider_cells)}')
    check(all(re.fullmatch(r':?-{3}:?',c) for c in divider_cells),'容量汇总分隔行标记不规范')
capacity_order=[]
for line in capacity_lines:
    cells=[c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells)==11 and cells[0] in platforms:
        p=cells[0];capacity_order.append(p)
        check(cells[4:10]==ns['maker_cells'](p),f'厂家矩阵错误：{p} → {cells[4:10]}')
        expected_storage='SSD' if p in ns['ssd_platforms'] else 'eMMC'
        check(cells[10]==expected_storage,f'存储位置错误：{p} → {cells[10]}')
check(capacity_order==platforms,f'容量表顺序不符：{capacity_order}')
check(text.index('### N64')<text.index('### PS1'),'N64 未排在 PS1 前')
check('## 容量汇总与运行核对' not in text,'容量仍是独立旧章节')

# 禁用占位、模板句、已取消章节和已知错误文本。
for pat in [r'\bTODO\b',r'\[存疑\]',r'\[删除\]',r'\[不存在\]',r'待补',r'本作保留了该平台',r'见商品版本',r'有独立的关卡、角色或系统配置',r'Gradius III / Gradius Gaiden',r'TwinBee / Pop’n TwinBee',r'Golden Axe \(Arcade\) / Golden Axe: The Revenge',r'两个深化专题',r'史克威尔 2D 黄金期',r'本文已直接修正的典型错误',r'三层查漏补缺结果',r'低画质专项验收']:
    hits=[m.start() for m in re.finditer(pat,text,re.I)]
    check(not hits,f'遗留禁用文本：{pat} × {len(hits)}')

# 合集展开计数和容量；关键结论全部由数据重算，不锁定历史总数。
game_total=sum(gc(e) for e in entries);total=sum(mb(e.size) for e in entries)
check(f'**{len(entries)}** | **{game_total}** | **{total/1024:.2f} GB**' in text,f'汇总与重算不符：{len(entries)}／{game_total}／{total/1024:.2f} GB')
check(ns['emmc_total']+ns['ssd_total']==total,'eMMC／SSD 平台容量分算错误')
check(ns['windows_priority']+ns['windows_deferred']==ns['windows_total'],'Windows 首装／候补容量分算错误')
check(ns['first_install_budget']==ns['full_budget']-ns['windows_deferred'],'首装总预算计算错误')
check(ns['first_ssd_rom']==ns['ssd_total']-ns['windows_deferred'],'SSD 首装容量计算错误')
for snippet in ['#### 256＋64 GB 双盘容量结论',f"{ns['full_budget']/1024:.2f} GiB",f"{ns['windows_total']/1024:.2f} GiB",f"{ns['full_budget']/1024+65:.0f}–{ns['full_budget']/1024+97:.0f} GiB",'512 GB SSD＋64 GB eMMC','NDS 固定放 eMMC','不要直接执行 `ln -s`']:
    check(snippet in text,f'双盘容量规划缺失：{snippet}')
expected_counts={'Three Wonders':3,'Ys Book I & II':2,'Final Fantasy I & II: Dawn of Souls':2,'Gradius / Gradius II / Gradius III':3,'TwinBee / Detana!! TwinBee':2,'Commander Keen in Goodbye, Galaxy!':2,'Galaga / Galaxian':2}
for name,n in expected_counts.items():
    es=[e for e in entries if e.en==name]
    check(len(es)==1 and gc(es[0])==n,f'合集计数错误：{name} 应为 {n}')

# 深度备注应全部使用；被版本筛选删除的条目允许留下数据备注，其他未使用键仍报错。
from guide_deep_notes import DEEP
ens={e.en for e in entries}
dropped_ens={en for platform,en in ns['VERSION_DROP']}
unused=sorted(set(DEEP)-ens-dropped_ens)
check(not unused,'DEEP 未使用键：'+str(unused))
dup_notes=collections.defaultdict(list)
for e in entries:
    norm=re.sub(r'\s+','',e.note)
    dup_notes[norm].append((e.platform,e.en))
for note,products in dup_notes.items():
    if len({en for p,en in products})>1:
        errors.append('不同商品复用整段备注：'+str(products))

# 用户点名补漏、三国、射击、改版和 PC 边界。
required=['Chrono Cross','Tengai Makyou II: Manji Maru','Kingdom Hearts: Birth by Sleep','Dragon Ball: Advanced Adventure','Tony Hawk’s Pro Skater 2','Lumines: Puzzle Fusion','Me & My Katamari','Theme Hospital','Tomato Adventure','Puyo Puyo Sun',"Sid Meier's Civilization II",'三國志英傑傳','三國志孔明傳','Life Force / Salamander','Contra','Super C','Galaga / Galaxian','Nakahara no Hasha: Sangoku Shouseiden','あっぱれ伝 ‐伏龍の章‐ / Appare-den: Fukuryuu no Shou','Farland Story: Tooi Kuni no Monogatari / ファーランドストーリー 遠い国の物語','Farland Story Denki: Arc Ou no Ensei / ファーランドストーリー 伝記 アーク王の遠征','Farland Story: Shirogane no Tsubasa / ファーランドストーリー 白銀の翼','Farland Story: Daichi no Kizuna / ファーランドストーリー 大地の絆']
for name in required:check(name in ens,f'点名作品缺失：{name}')
farland=[e for e in entries if e.series=='古大陆物语']
check(len(farland)==4 and all(e.platform=='DOS' for e in farland),'古大陆物语应为 DOS 四作，不重复收 Windows 前两作重制合集')
check(not any('Yottsu no Fuuin' in e.en for e in entries),'四个封印不应与 DOS 前两作重复出现')
sengoku_bishoujo=[e for e in entries if e.series=='战国美少女']
check(len(sengoku_bishoujo)==2 and all(e.platform=='Win95 / Win98' for e in sengoku_bishoujo),'战国美少女应为 Windows 双作专题')
check('### 古大陆物语\n' in text and '### 战国美少女\n' in text,'古大陆物语或战国美少女专题未生成')
chrono_cross=next(e for e in entries if e.en=='Chrono Cross')
check(chrono_cross.zh=='穿越时空／时空之轮 2','Chrono Cross 中文译名与 Chrono Trigger 混淆')
gb_saint_name='聖闘士セイントパラダイス 最強の戦士たち / Saint Paradise: Saikyou no Senshitachi'
check(not any(e.platform=='GB' and e.en=='Saint Seiya: The Sanctuary / Saint Paradise' for e in entries),'GB 圣斗士仍混入 PS2 The Sanctuary 商品名')
gb_saint=next((e for e in entries if e.platform=='GB' and e.en==gb_saint_name),None)
check(gb_saint and gb_saint.year=='1992' and gc(gb_saint)==1,'GB Saint Paradise 应为 1992 年单作')
required_genres={
    'Tengai Makyou II: Manji Maru':'角色扮演',
    'Tony Hawk’s Pro Skater 2':'竞速／体育',
    'Dragon Ball: Advanced Adventure':'格斗／清版动作',
    'Pokémon Emerald':'角色扮演',
    'Super Mario RPG: Legend of the Seven Stars':'角色扮演',
    'Paper Mario':'角色扮演',
    'Dissidia Final Fantasy':'格斗／清版动作',
    'Jeanne d’Arc':'战略／战棋',
    'Bahamut Lagoon':'战略／战棋',
    'Front Mission Alternative':'战略／战棋',
    'Front Mission: Gun Hazard':'角色扮演',
    'Pokémon Trading Card Game':'战略／战棋',
    '聖闘士セイントパラダイス 最強の戦士たち / Saint Paradise: Saikyou no Senshitachi':'战略／战棋',
    'Pokémon Snap':'模拟／音乐／派对',
    'The World Ends with You':'角色扮演',
    'Ys: The Oath in Felghana':'角色扮演',
    'Skies of Arcadia':'角色扮演',
    'Phantasy Star Online':'角色扮演',
    'Crazy Taxi':'竞速／体育',
    'Metropolis Street Racer':'竞速／体育',
    'Gran Turismo':'竞速／体育',
    'Gran Turismo 2':'竞速／体育',
    'Ape Escape':'平台动作',
    'Tony Hawk’s Pro Skater':'竞速／体育',
    'Osu! Tatakae! Ouendan / Elite Beat Agents':'模拟／音乐／派对',
    'Taiko no Tatsujin Portable':'模拟／音乐／派对',
    '1942':'射击（STG）',
    '1943: The Battle of Midway':'射击（STG）',
    'Blazing Star':'射击（STG）',
    'Cho Aniki':'射击（STG）',
    'Nakahara no Hasha: Sangoku Shouseiden':'战略／战棋',
    'Military Madness':'战略／战棋',
    'Advance Wars':'战略／战棋',
    'Live A Live':'角色扮演',
    'Super Punch-Out!!':'竞速／体育',
    'The Lost Vikings':'益智／休闲',
    'Wario’s Woods':'益智／休闲',
    'Lode Runner':'益智／休闲',
    'Yoshi':'益智／休闲',
    'Alien Crush':'模拟／音乐／派对',
    "Devil's Crush":'模拟／音乐／派对',
    'Chase HQ':'竞速／体育',
    'Scorched Earth':'战略／战棋',
    'Worms':'战略／战棋',
}
for name,category in required_genres.items():
    matches=[e for e in entries if e.en==name]
    check(bool(matches),f'品类防回归条目缺失：{name}')
    check(all(e.category==category for e in matches),f'点名作品品类错误：{name} → '+str([(e.platform,e.category) for e in matches]))
for pattern,category in [(r'Metal Max.*','角色扮演'),(r'Mario & Luigi:.*','角色扮演'),(r'Mega Man Battle Network.*','角色扮演'),(r'Mega Man Star Force:.*','角色扮演'),(r'Advance Wars.*','战略／战棋'),(r'Sakura Wars [34].*','战略／战棋'),(r'Crazy Taxi(?: 2)?','竞速／体育'),(r'Banjo-(?:Kazooie|Tooie)','平台动作'),(r'Dragon Ball Z: Goku Hishouden / Goku Gekitouden','角色扮演')]:
    matches=[e for e in entries if re.fullmatch(pattern,e.en,re.I)]
    check(bool(matches),f'品类防回归规则无匹配：{pattern}')
    check(all(e.category==category for e in matches),f'系列品类串扰：{pattern}')
check(next(e for e in entries if e.en=='Gran Turismo').subgenre=='竞速与驾驶','GT 赛车被误归普通体育')
check(next(e for e in entries if e.en=='Front Mission Alternative').subgenre=='即时军事模拟','Front Mission Alternative 未按实时战术归类')
for name in ['Life Force / Salamander','Life Force','Gradius','Galaxian','Galaga']:
    check(all(e.category=='射击（STG）' for e in entries if e.en==name),f'STG 归类错误：{name}')
for name in ['Contra','Super C','Battle City']:
    check(all(e.category=='动作射击' for e in entries if e.en==name),f'动作射击归类错误：{name}')
nakahara=next((e for e in entries if e.en=='Nakahara no Hasha: Sangoku Shouseiden'),None)
check(nakahara and nakahara.series=='三国志与三国题材' and nakahara.subgroup=='Namco《三国志》','中原之霸者未进入 Namco 三国子系列')
check('Yanshan 90 Tank / Tank 1990（烟山 90 坦克）' in text,'烟山 90 坦克未进入改版表')
dos_ens={e.en for e in entries if e.platform=='DOS'}
for forbidden in ['Age of Wonders','明星志願 2','絕代雙驕','阿瑪迪斯戰記','致命武力','戰國美少女','DOOM','DOOM II: Hell on Earth','Wolfenstein 3D','Descent','Tyrian']:
    check(forbidden not in dos_ens,f'不应纳入 DOS 的 Windows／射击／内容项：{forbidden}')
check(any(e.en=='Advanced Daisenryaku: Deutsch Dengeki Sakusen' and e.platform=='MD / Genesis' for e in entries),'高级大战略未保留唯一 MD 版')
check(not any('Daisenryaku' in e.en and e.platform=='DOS' for e in entries),'高级大战略被误收为 DOS 版')
civ2=next((e for e in entries if e.en=="Sid Meier's Civilization II"),None)
check(civ2 and 'DOSBox‑X' in civ2.note and 'Windows 3.x' in civ2.note,'文明 II 缺 DOSBox-X／Win3.x 运行说明')

# Windows 9x 全部来自精选数据，不夹带射击；Wine、cnc-ddraw 与跨平台专题必须真实落入正文。
win_entries=[e for e in entries if e.platform=='Win95 / Win98']
win_ens={e.en for e in win_entries}
check(platforms.index('Win95 / Win98')==platforms.index('DOS')+1,'Win95／98 未紧随 DOS')
check(len(win_entries)==39==len(ns['WINDOWS_GAMES']),f'Windows 条目数应为 39：{len(win_entries)}')
check(set(win_ens)==set(ns['WINDOWS_RUNTIME']),'Windows 商品与运行判断映射不一致')
check('Rayman 2: The Great Escape' not in win_ens,'高风险 Windows Rayman 2 不应收录；其他平台版本不受影响')
for removed in ['Dungeon Keeper II','Need for Speed III: Hot Pursuit','Planescape: Torment','The Sims','Tropico','Grim Fandango','The Longest Journey','Toonstruck','Captain Claw','Jazz Jackrabbit 2','天地劫序傳：幽城幻劍錄']:
    check(removed not in text,f'已移除 Windows 作品仍在正文残留：{removed}')
check('Heroes of Might and Magic III: The Restoration of Erathia' in win_ens,'英雄无敌 III 不应被精简掉')
for en,zh,pub,size,year,note,series,category,subgenre in ns['WINDOWS_GAMES']:
    check(en in win_ens,f'Windows 精选缺失：{en}')
for e in win_entries:
    check(e.category not in {'射击','射击（STG）','动作射击'},f'Windows 混入射击游戏：{e.en}')
    check(e.en in ns['WINDOWS_RUNTIME'],f'Windows 缺运行判断：{e.en}')
    if e.en in ns['WINDOWS_RUNTIME']:
        level,runtime_note=ns['WINDOWS_RUNTIME'][e.en]
        check(level in {'优先安装','固定版本后安装'},f'Windows 运行级别异常：{e.en}')
        check(f'【Wine 安装判断：{level}】{runtime_note}' in e.note,f'Windows 具体验收备注未落入正文：{e.en}')
for snippet in ['/userdata/roms/windows/','cnc-ddraw','ddraw.dll','native,builtin','WINEDLLOVERRIDES=ddraw=n,b','不支持 Direct3D 或 Glide','DDrawCompat 官方不支持 Wine','DXVK','SAVEDIR','SAVEFILES','Wine-TKG','/usr/wine/','/userdata/system/wine/custom/']:
    check(snippet in text,f'Windows／cnc-ddraw 配置缺失：{snippet}')
check('与 Wine-GE 运行' not in text,'仍把旧 Wine-GE 写成固定运行前提')
check(next(e for e in win_entries if e.en=='Diablo').year=='1996–1997','Diablo 应保留 1996 首发出货／1997 广泛上市的跨年标注')
check(next(e for e in win_entries if e.en=="Sid Meier's Alpha Centauri").year=='1999','Alpha Centauri 年份应为 1999')
civ3=next(e for e in win_entries if e.en=="Sid Meier's Civilization III")
check('Wine ≥10.13' in civ3.note and '回归' in civ3.note,'文明 III 缺 Wine 10.13 门槛与回归风险')
check('【Wine 安装判断：固定版本后安装】' in civ3.note,'文明 III 未归入固定版本后安装')
check(gc(next(e for e in win_entries if e.en=='StarCraft / StarCraft: Brood War'))==2,'星际争霸合集展开计数不是 2')
homm=[e for e in entries if e.series=='英雄无敌']
check({e.platform for e in homm}=={'DOS','Win95 / Win98'} and len(homm)==3,'英雄无敌未形成 DOS＋Windows 三作专题')
check('### 英雄无敌\n' in text,'英雄无敌专题未生成')
pc_sanguo_groups={
    '三國志英傑傳':'英杰传与曹操传',
    '三國志孔明傳':'英杰传与曹操传',
    '三國志曹操伝 / Sangokushi Sousouden':'英杰传与曹操传',
    'Sangokushi VIII / 三國志VIII':'光荣《三国志》',
}
for name,subgroup in pc_sanguo_groups.items():
    e=next((x for x in entries if x.en==name),None)
    check(e and e.series=='三国志与三国题材',f'PC 三国未进入同题材专题：{name}')
    if e:
        check(e.subgroup==subgroup,f'PC 三国子系列归类错误：{name} → {e.subgroup}')
        check(ns['entry_link'](e) in text,f'PC 三国缺专题回链：{name}')
for name in ['Romance of the Three Kingdoms V','Romance of the Three Kingdoms VI','Romance of the Three Kingdoms VII']:
    matches=[e for e in entries if e.en==name]
    check(len(matches)==1 and matches[0].platform=='PS1',f'三国志 V／VI／VII 应仅保留 PS1：{name}')
check(not any(e.platform=='Win95 / Win98' and re.fullmatch(r'Sangokushi (V|VI|VII) / .*',e.en) for e in entries),'Windows 三国志 V／VI／VII 仍重复保留')

# 跨平台版本规则逐项闭合：删除项不得出现，保留项恰好一个且写明取舍。
final_keys={(e.platform,e.en) for e in entries}
for key,item in ns['VERSION_DROP'].items():
    check(key not in final_keys,f'跨平台重复版本未删除：{item["name"]} → {key}')
for item in ns['VERSION_CHOICES']:
    for key in item['keeps']:
        matches=[e for e in entries if (e.platform,e.en)==key]
        check(len(matches)==1,f'版本保留项不是恰好一个：{item["name"]} → {key}')
        if matches:check('版本取舍：'+item['reason'] in matches[0].note,f'保留版本缺取舍说明：{key}')
check(not any(name in text for name in ['Pokémon Crystal Clear','Pokémon Prism','Final Fantasy Tactics: The Lion War']),'失去底本的宝可梦／FFT 改版仍残留')
gameplay=text.split('## 游戏方式专题：品类源流与代表作',1)[-1].split('## 游戏内容专题：系列与平台回链',1)[0]
for name in ["Sid Meier's Civilization II",'Heroes of Might and Magic III: The Restoration of Erathia',"Sid Meier's Civilization III",'Icewind Dale','RollerCoaster Tycoon']:
    e=next((x for x in entries if x.en==name),None)
    check(e and ns['entry_link'](e,e.zh) in gameplay,f'游戏方式专题缺 PC 代表作回链：{name}')
for genre,history,reps in ns['genre_defs']:
    for name in reps:
        e=next((x for x in entries if x.en==name),None)
        check(e and ns['entry_link'](e,e.zh) in gameplay,f'品类代表作已失效：{genre} → {name}')
check('三国志姜维传' in text and ns['new_hack_count']==14,'曹操传精选改版或原创改版计数缺失')

report=[f'entries={len(entries)}',f'games={game_total}',f'capacity_gb={total/1024:.2f}',f'rows={len(rows)}',f'anchors={len(anchors)}',f'heading_anchors={len(heading_anchors)}',f'internal_links={len(links)}',f'errors={len(errors)}',f'warnings={len(warnings)}','']
report += ['ERROR: '+x for x in errors]
report += ['WARNING: '+x for x in warnings]
(ROOT/'audit_report.txt').write_text('\n'.join(report)+'\n')
print('\n'.join(report))
sys.exit(1 if errors else 0)
