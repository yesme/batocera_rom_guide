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
for pat in [r'\bTODO\b',r'\[存疑\]',r'\[删除\]',r'\[不存在\]',r'待补',r'本作保留了该平台',r'见商品版本',r'有独立的关卡、角色或系统配置',r'Gradius III / Gradius Gaiden',r'TwinBee / Pop’n TwinBee',r'Golden Axe \(Arcade\) / Golden Axe: The Revenge',r'两个深化专题',r'史克威尔 2D 黄金期',r'本文已直接修正的典型错误']:
    hits=[m.start() for m in re.finditer(pat,text,re.I)]
    check(not hits,f'遗留禁用文本：{pat} × {len(hits)}')

# 合集展开计数和容量。
game_total=sum(gc(e) for e in entries);total=sum(mb(e.size) for e in entries)
check(f'**{len(entries)}** | **{game_total}** | **{total/1024:.2f} GB**' in text,f'汇总与重算不符：{len(entries)}／{game_total}／{total/1024:.2f} GB')
check(round(ns['emmc_total']/1024,2)==25.37 and round(ns['ssd_total']/1024,2)==206.01,'eMMC／SSD 平台容量分算错误')
check(round(ns['windows_priority']/1024,2)==36.37 and round(ns['windows_deferred']/1024,2)==37.50,'Windows 首装／候补容量分算错误')
check(round(ns['first_install_budget']/1024,2)==209.89,'首装总预算不是 209.89 GiB')
check(round((ns['first_ssd_rom']+6*1024)/1024,2)==174.51,'SSD 首装容量不是 174.51 GiB')
for snippet in ['#### 256＋64 GB 双盘容量结论','298.02 GiB','50.64 GiB','310–344 GiB','512 GB SSD＋64 GB eMMC','NDS 固定放 eMMC','不要直接执行 `ln -s`']:
    check(snippet in text,f'双盘容量规划缺失：{snippet}')
expected_counts={'Three Wonders':3,'Super Mario All-Stars':4,'Ys Book I & II':2,'Final Fantasy I & II: Dawn of Souls':2,'Street Fighter III: Double Impact':2,'Ys I & II Chronicles':2,'Castlevania: The Dracula X Chronicles':3,'Gradius / Gradius II / Gradius III':3,'TwinBee / Detana!! TwinBee':2,'Commander Keen in Goodbye, Galaxy!':2,'Galaga / Galaxian':2}
for name,n in expected_counts.items():
    es=[e for e in entries if e.en==name]
    check(len(es)==1 and gc(es[0])==n,f'合集计数错误：{name} 应为 {n}')

# 深度备注应全部使用；同商品跨平台可共享备注，不同商品不能共用整段。
from guide_deep_notes import DEEP
ens={e.en for e in entries}
unused=sorted(set(DEEP)-ens)
check(not unused,'DEEP 未使用键：'+str(unused))
dup_notes=collections.defaultdict(list)
for e in entries:
    norm=re.sub(r'\s+','',e.note)
    dup_notes[norm].append((e.platform,e.en))
for note,products in dup_notes.items():
    if len({en for p,en in products})>1:
        errors.append('不同商品复用整段备注：'+str(products))

# 用户点名补漏、三国、射击、改版和 PC 边界。
required=['Chrono Cross','Tengai Makyou II: Manji Maru','Kingdom Hearts: Birth by Sleep','Dragon Ball: Advanced Adventure','Tony Hawk’s Pro Skater 2','Lumines: Puzzle Fusion','Me & My Katamari','Theme Hospital','Tomato Adventure','Puyo Puyo Sun',"Sid Meier's Civilization II",'三國志英傑傳','三國志孔明傳','Life Force / Salamander','Contra','Super C','Galaxian','Galaga','Nakahara no Hasha: Sangoku Shouseiden','あっぱれ伝 ‐伏龍の章‐ / Appare-den: Fukuryuu no Shou','Farland Story: Tooi Kuni no Monogatari / ファーランドストーリー 遠い国の物語']
for name in required:check(name in ens,f'点名作品缺失：{name}')
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
    'Pokémon Ruby / Sapphire':'角色扮演',
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
check(len(win_entries)==49==len(ns['WINDOWS_GAMES']),f'Windows 条目数应为 49：{len(win_entries)}')
check('Rayman 2: The Great Escape' not in win_ens,'高风险且已有主机版的 Windows Rayman 2 不应收录')
for en,zh,pub,size,year,note,series,category,subgenre in ns['WINDOWS_GAMES']:
    check(en in win_ens,f'Windows 精选缺失：{en}')
for e in win_entries:
    check(e.category not in {'射击','射击（STG）','动作射击'},f'Windows 混入射击游戏：{e.en}')
    check(e.en in ns['WINDOWS_RUNTIME'],f'Windows 缺运行判断：{e.en}')
    if e.en in ns['WINDOWS_RUNTIME']:
        level,runtime_note=ns['WINDOWS_RUNTIME'][e.en]
        check(level in {'优先安装','固定版本后安装','低画质专项验收'},f'Windows 运行级别异常：{e.en}')
        check(f'【Wine 安装判断：{level}】{runtime_note}' in e.note,f'Windows 具体验收备注未落入正文：{e.en}')
for snippet in ['/userdata/roms/windows/','cnc-ddraw','ddraw.dll','native,builtin','WINEDLLOVERRIDES=ddraw=n,b','不支持 Direct3D 或 Glide','DDrawCompat 官方不支持 Wine','DXVK','SAVEDIR','SAVEFILES','Wine-TKG','/usr/wine/','/userdata/system/wine/custom/']:
    check(snippet in text,f'Windows／cnc-ddraw 配置缺失：{snippet}')
check('与 Wine-GE 运行' not in text,'仍把旧 Wine-GE 写成固定运行前提')
check(next(e for e in win_entries if e.en=='Diablo').year=='1996–1997','Diablo 应保留 1996 首发出货／1997 广泛上市的跨年标注')
check(next(e for e in win_entries if e.en=="Sid Meier's Alpha Centauri").year=='1999','Alpha Centauri 年份应为 1999')
castle=next(e for e in win_entries if '幽城' in e.en)
check(castle.en=='天地劫序傳：幽城幻劍錄' and castle.zh=='天地劫序传：幽城幻剑录' and castle.subgenre=='即时／半即时 RPG','幽城幻剑录完整名或战斗分类错误')
civ3=next(e for e in win_entries if e.en=="Sid Meier's Civilization III")
check('Wine ≥10.13' in civ3.note and '回归' in civ3.note,'文明 III 缺 Wine 10.13 门槛与回归风险')
check(civ3.note.count('低画质专项验收')==1,'文明 III 未设专项验收')
for name in ['Dungeon Keeper II','Need for Speed III: Hot Pursuit']:
    e=next(e for e in win_entries if e.en==name)
    check('低画质专项验收' in e.note and '640×480' in e.note,f'早期 3D 游戏缺低分辨率验收：{name}')
check(gc(next(e for e in win_entries if e.en=='StarCraft / StarCraft: Brood War'))==2,'星际争霸合集展开计数不是 2')
homm=[e for e in entries if e.series=='英雄无敌']
check({e.platform for e in homm}=={'DOS','Win95 / Win98'} and len(homm)==3,'英雄无敌未形成 DOS＋Windows 三作专题')
check('### 英雄无敌\n' in text,'英雄无敌专题未生成')
pc_sanguo_groups={
    '三國志英傑傳':'英杰传与曹操传',
    '三國志孔明傳':'英杰传与曹操传',
    '三國志曹操伝 / Sangokushi Sousouden':'英杰传与曹操传',
    'Sangokushi VII / 三國志VII':'光荣《三国志》',
    'Sangokushi VIII / 三國志VIII':'光荣《三国志》',
}
for name,subgroup in pc_sanguo_groups.items():
    e=next((x for x in entries if x.en==name),None)
    check(e and e.series=='三国志与三国题材',f'PC 三国未进入同题材专题：{name}')
    if e:
        check(e.subgroup==subgroup,f'PC 三国子系列归类错误：{name} → {e.subgroup}')
        check(ns['entry_link'](e) in text,f'PC 三国缺专题回链：{name}')
gameplay=text.split('## 游戏方式专题：品类源流与代表作',1)[-1].split('## 游戏内容专题：系列与平台回链',1)[0]
for eid in ['dos-020','win9x-018','win9x-024','win9x-004','win9x-034']:
    e=next((x for x in entries if x.eid.lower()==eid),None)
    check(e and ns['entry_link'](e,e.zh) in gameplay,f'游戏方式专题缺 PC 代表作回链：{eid}')
check('三国志姜维传' in text and ns['new_hack_count']==15,'曹操传精选改版或原创改版计数缺失')

report=[f'entries={len(entries)}',f'games={game_total}',f'capacity_gb={total/1024:.2f}',f'rows={len(rows)}',f'anchors={len(anchors)}',f'heading_anchors={len(heading_anchors)}',f'internal_links={len(links)}',f'errors={len(errors)}',f'warnings={len(warnings)}','']
report += ['ERROR: '+x for x in errors]
report += ['WARNING: '+x for x in warnings]
(ROOT/'audit_report.txt').write_text('\n'.join(report)+'\n')
print('\n'.join(report))
sys.exit(1 if errors else 0)
