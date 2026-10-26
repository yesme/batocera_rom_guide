from pathlib import Path
from dataclasses import dataclass
import re, importlib.util, difflib
ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('rg',ROOT/'rebuild_guide.py')
rg=importlib.util.module_from_spec(spec); spec.loader.exec_module(rg)
Entry=rg.Entry
entries=rg.entries
from guide_dos import DOS_GAMES, DOS_GENRES, DOS_SERIES, DOS_COUNTS
from guide_windows import WINDOWS_GAMES, WINDOWS_GENRES, WINDOWS_SERIES, WINDOWS_COUNTS, WINDOWS_RUNTIME

# 只保留适合家庭电视与 N4100 保守性能范围的正式作品。
drop_old={
('NES / FC','打鸭子'),('GBA','火影忍者系列'),('N64','宝可梦皮卡丘'),('GB / GBC','Kirby’s Dream Land 1 / 2'),
('PSP','侠盗猎车手：自由城故事'),('PSP','铁拳6'),('PSP','湾岸午夜俱乐部'),('PSP','火爆狂飙：传奇'),
('PSP','高达VS高达NEXT PLUS'),('PSP','真三国无双：联合突袭'),('PSP','刺客信条：血统'),
('PSP','荣誉勋章：英雄'),('PSP','抵抗：惩罚'),('PSP','合金装备：和平行者'),('PSP','最终幻想零式Type-0'),
('PSP','战神：奥林匹斯之链'),('PSP','战神：斯巴达之魂'),('PSP','火影忍者：疾风传终极觉醒3'),
('Dreamcast','死亡之屋2'),('Dreamcast','Carrier'),('Dreamcast','NBA 2K / NFL 2K系列'),
('PS1','龙珠Final Bout'),('PS1','同级生2/下级生/To Heart'),
}
arcade_drop={'三国战纪七星转生','西游释厄传2','Sonic the Fighters','Virtua Fighter 1','Virtua Fighter 2','Daytona USA','Sega Rally','Virtua Cop 1/2','Space Gun','beatmania IIDX','DDR',"pop'n music",'GITADORA','Taiko no Tatsujin'}
entries=[e for e in entries if (e.platform,e.old) not in drop_old and not (e.platform=='街机（FBNeo / MAME）' and e.old in arcade_drop)]

# 修正机器可辨识的残缺名称、历史发行主体和错误归属。
fix={
'Journey to Silius':('Journey to Silius','Sunsoft'),
'Shantae':('Shantae','Capcom'),
'Tales of Phantasia':('Tales of Phantasia','Namco'),
'EarthBound / Mother 2':('EarthBound / Mother 2','Nintendo'),
'Killer Instinct':('Killer Instinct','Nintendo'),
'Banjo-Kazooie':('Banjo-Kazooie','Nintendo'),
'Banjo-Tooie':('Banjo-Tooie','Nintendo'),
'Conker\'s Bad Fur Day':("Conker's Bad Fur Day",'Rare'),
'The Lost Vikings':('The Lost Vikings','Interplay'),
'Harvest Moon':('Harvest Moon','Natsume'),
'Harvest Moon GB':('Harvest Moon GB','Natsume'),
'Harvest Moon: Friends of Mineral Town':('Harvest Moon: Friends of Mineral Town','Natsume'),
'Harvest Moon: Grand Bazaar':('Harvest Moon: Grand Bazaar','Marvelous'),
'Grandia':('Grandia','Sony Computer Entertainment'),
'Grandia II':('Grandia II','Ubisoft'),
'Lunar: Silver Star Story Complete':('Lunar: Silver Star Story Complete','Kadokawa Shoten / Working Designs'),
'Lunar 2: Eternal Blue Complete':('Lunar 2: Eternal Blue Complete','Kadokawa Shoten / Working Designs'),
'Wild Arms 1':('Wild Arms','Sony Computer Entertainment'),
'Wild Arms 2':('Wild Arms 2nd Ignition','Sony Computer Entertainment'),
'Medal of Honor':('Medal of Honor','Electronic Arts'),
'Medal of Honor: Underground':('Medal of Honor: Underground','Electronic Arts'),
'1942':('1942','Capcom'),'1943':('1943: The Battle of Midway','Capcom'),
'1080° Snowboarding':('1080° Snowboarding','Nintendo'),
'Snowboarding':('1080° Snowboarding','Nintendo'),
'Special Champion Edition':("Street Fighter II': Special Champion Edition",'Capcom'),
'Alpha 2':('Street Fighter Alpha 2','Capcom'),
'Innocent Sin':('Persona 2: Innocent Sin','Atlus'),
'Eternal Punishment':('Persona 2: Eternal Punishment','Atlus'),
'if...':('Shin Megami Tensei if...','Atlus'),
'Persona 1':('Revelations: Persona','Atlus'),
'PaRappa':('PaRappa the Rapper','Sony Computer Entertainment'),
'DDR/beatmania/':('Dance Dance Revolution / beatmania','Konami'),
}
for e in entries:
    if e.en in fix:e.en,e.pub=fix[e.en]
    if e.pub=='见商品版本':
        e.pub={'Memories Off / Clannad / Steins;Gate / Higurashi / Fate/Extra':'5pb. / CyberFront / Imageepoch / Capcom'}.get(e.en,e.pub)
    if e.pub=='Square Enix' and re.search(r'Final Fantasy|Dragon Quest|Parasite Eve',e.en):
        if e.platform in {'NES / FC','SNES / SFC','PS1'}:e.pub='Enix' if 'Dragon Quest' in e.en else 'Square'
    if e.platform=='PS1' and e.en.startswith('Final Fantasy'):e.pub='Square'

# 旧稿中仍需精确到完整商品名的条目。
old_names={
'三国战纪正宗Plus':('Knights of Valour Plus','三国战纪：正宗 Plus'),
'西游释厄传Super':('Oriental Legend Super','西游释厄传 Super'),
'D&D毁灭之塔':('Dungeons & Dragons: Tower of Doom','龙与地下城：毁灭之塔'),
'D&D暗影之谜':('Dungeons & Dragons: Shadow over Mystara','龙与地下城：暗黑秘影'),
'AVP异形VS铁血战士':('Alien vs. Predator','异形大战铁血战士'),
'饿狼传说Real Bout':('Real Bout Fatal Fury','饿狼传说 Real Bout'),
'饿狼传说RB Special':('Real Bout Fatal Fury Special','饿狼传说 Real Bout Special'),
'世界英雄Perfect':('World Heroes Perfect','世界英雄 Perfect'),
'街头霸王2 Hyper Fighting':('Street Fighter II: Hyper Fighting','街头霸王 II：Hyper Fighting'),
'街头霸王2 Super Turbo':('Super Street Fighter II Turbo','超级街头霸王 II Turbo'),
'少年街霸Alpha 1':('Street Fighter Alpha: Warriors’ Dreams','少年街霸 Alpha'),
'少年街霸Alpha 2':('Street Fighter Alpha 2','少年街霸 Alpha 2'),
'少年街霸Alpha 3':('Street Fighter Alpha 3','少年街霸 Alpha 3'),
'街头霸王III New Generation':('Street Fighter III: New Generation','街头霸王 III：新世代'),
'街头霸王III 2nd Impact':('Street Fighter III: 2nd Impact','街头霸王 III：二度冲击'),
'街头霸王III 三度冲击':('Street Fighter III: 3rd Strike','街头霸王 III：三度冲击'),
'恶魔战士Vampire Savior':('Vampire Savior: The Lord of Vampire','恶魔战士：吸血鬼救世主'),
'X-Men vs SF':('X-Men vs. Street Fighter','X 战警对街头霸王'),
'MVC1':('Marvel vs. Capcom: Clash of Super Heroes','漫威对卡普空：超级英雄冲突'),
'MVC2':('Marvel vs. Capcom 2: New Age of Heroes','漫威对卡普空 2：英雄新纪元'),
'JOJO的奇妙冒险':('JoJo’s Bizarre Adventure: Heritage for the Future','JOJO 的奇妙冒险：未来遗产'),
'打击者1945 II':('Strikers 1945 II','打击者 1945 II'),
'打击者1945 III':('Strikers 1945 III / Strikers 1999','打击者 1945 III'),
'飞翔鲛Same!Same!Same!':('Fire Shark / Same! Same! Same!','飞翔鲛'),
'OutZone':('Out Zone','异域战将'),
'Xexex':('Xexex / Orius','Xexex'),
'忍者神龟Turtles in Time':('Teenage Mutant Ninja Turtles: Turtles in Time','忍者神龟：时空之战'),
'X-Men（6人版）':('X-Men (Arcade)','X 战警（街机）'),
'Gradius I/II/III/Gaiden':('Gradius / Gradius II / Gradius III / Gradius Gaiden','宇宙巡航机 I／II／III／外传'),
'Parodius全系':('Parodius Da! / Sexy Parodius / Gokujou Parodius!','疯狂大射击系列'),
'TwinBee全系':('TwinBee / Detana!! TwinBee / Pop’n TwinBee','兵蜂系列'),
'泡泡龙+Rainbow Islands':('Bubble Bobble / Rainbow Islands','泡泡龙／彩虹岛'),
'Darius I/II/外传/Gaiden':('Darius / Darius II / Darius Gaiden','太空战斗机 I／II／外传'),
'Ninja Warriors':('The Ninja Warriors','忍者战士'),
'Puzzle Bobble 1-4':('Puzzle Bobble / Puzzle Bobble 2 / 3 / 4','泡泡龙解谜 1／2／3／4'),
'OutRun':('Out Run','OutRun'),
'After Burner':('After Burner II','冲破火网 II'),
'Joe & Mac':('Joe & Mac: Caveman Ninja','乔与麦克：原始人忍者'),
'Dark Seal':('Dark Seal / Gate of Doom','暗黑封印'),
'真女神转生1':('Shin Megami Tensei','真·女神转生'),
'真女神转生2':('Shin Megami Tensei II','真·女神转生 II'),
'真女神转生if...':('Shin Megami Tensei if...','真·女神转生 if…'),
'塞尔达传说：时空之章':('The Legend of Zelda: Oracle of Ages','塞尔达传说：时空之章'),
'塞尔达传说：大地之章':('The Legend of Zelda: Oracle of Seasons','塞尔达传说：大地之章'),
'源平讨魔伝':('Genpei Touma Den','源平讨魔传'),
'スーパー桃太郎電鉄':('Super Momotarou Dentetsu','超级桃太郎电铁'),
'Cosmo Fantasy':('Cosmic Fantasy 2','宇宙幻想 2'),
'Valis 1-4':('Valis: The Fantasm Soldier / Valis II / III / IV','梦幻战士 1／2／3／4'),
'Bomberman \'93/\'94':("Bomberman '93 / '94",'炸弹人 ’93／’94'),
'Neutopia 1':('Neutopia','新乌托邦'),
'Neutopia 2':('Neutopia II','新乌托邦 II'),
'Dungeon Explorer 1':('Dungeon Explorer','迷宫探险家'),
'Dungeon Explorer 2':('Dungeon Explorer II','迷宫探险家 II'),
'Download 1&2':('Download / Download 2','Download 1／2'),
'Original Generation 1':('Super Robot Taisen: Original Generation','超级机器人大战 OG'),
'Original Generation 2':('Super Robot Taisen: Original Generation 2','超级机器人大战 OG2'),
'Wild Arms 1':('Wild Arms','荒野兵器'),
'Wild Arms 2':('Wild Arms 2nd Ignition','荒野兵器 2'),
'1080° Snowboarding':('1080° Snowboarding','1080° 滑雪'),
'Sega GT':('Sega GT','世嘉 GT'),
}
for e in entries:
    if e.old in old_names:e.en,e.zh=old_names[e.old]

# 将掌机和街机按实际核心／硬件拆开。
gbc_old={'塞尔达传说：织梦岛DX','瓦力欧乐园3','宝可梦金/银/水晶','宝可梦卡片GB','Game & Watch Gallery系列','Shantae','Metal Gear Ghost Babel','Dragon Warrior Monsters 1','Dragon Warrior Monsters 2','塞尔达传说：时空之章','塞尔达传说：大地之章'}
mame_old={'泡泡龙+Rainbow Islands','奇奇怪界','电梯大战1/2','Chase HQ','太空侵略者','Darius I/II/外传/Gaiden','Ninja Warriors','Rastan','Metal Black','兽王记','太空哈利','Fantasy Zone','OutRun','After Burner','Super Monaco GP','Hang-On','Thunder Blade','Pac-Man / Ms. Pac-Man','Donkey Kong / Donkey Kong Jr.','Galaga / Galaxian','Dig Dug'}
for e in entries:
    if e.platform=='GB / GBC' and (e.old in gbc_old or e.en in {'Wario Land II','Super Mario Bros. Deluxe','Survival Kids','Star Ocean: Blue Sphere','Mega Man Xtreme'}):e.platform='GBC'
    elif e.platform=='GB / GBC':e.platform='GB'
    if e.platform=='街机（FBNeo / MAME）':e.platform='MAME' if e.old in mame_old else 'FBNeo'

# 去掉同平台同商品的重复行，保留内容较完整的一行。
uniq=[]; seen=set()
for e in entries:
    key=(e.platform,re.sub(r'[^a-z0-9]','',e.en.lower()))
    if key in seen:continue
    seen.add(key);uniq.append(e)
entries=uniq

# 查漏补缺：经典休闲、合作、GG 与 WS／WSC 代表作。
def add(p,en,zh,pub,size,year,note,series=''):
    e=Entry(p,en,en,zh,pub,size,year,note,series)
    entries.append(e);return e
add('MAME','Snow Bros.: Nick & Tom','雪人兄弟','Toaplan','4MB','1990','固定单屏中把敌人滚成雪球并推动连锁撞击，双人可协作也可争抢得分。它是街机时代合家欢动作的代表，规则直观但隐藏道具与高分路线很有深度。','雪人兄弟')
add('FBNeo','Puyo Puyo Tsu','噗哟噗哟通','Compile / Sega','8MB','1994','四连消除与向对手发送干扰块构成对战核心，加入相杀规则后攻防逆转更鲜明。它确立了噗哟系列长期沿用的连锁对战范式，适合家庭双人对局。','噗哟噗哟')
add('FBNeo','Magical Drop III','魔法气泡 III','Data East','30MB','1997','从底部抓取并回投同色球，连续消除可压迫对手；角色差异和快节奏让它区别于普通落块游戏。街机版保留了 Data East 益智对战特有的紧张感。','魔法气泡')
add('GB','Kirby’s Dream Land','星之卡比','Nintendo','1MB','1992','卡比吸入敌人、鼓起身体飞行，但首作还没有后来标志性的复制能力。短小关卡与可调节难度让它成为 GB 早期适合新手的动作游戏。','星之卡比')
add('GB','Kirby’s Dream Land 2','星之卡比 2','Nintendo','2MB','1995','复制能力与三位动物伙伴组合，同一能力会随伙伴改变形态。隐藏彩虹水滴和真结局鼓励探索，是黑白 GB 后期内容很扎实的一作。','星之卡比')
add('GB','Qix','Qix 领土分割','Nintendo','0.5MB','1990','在空白区域画线封地，同时躲避沿边和场内移动的敌人；风险越高，单次圈地收益越大。任天堂掌机版把 Taito 的抽象街机规则带进便携短局。')
add('GB','Mole Mania','摩尔庄园','Nintendo','1MB','1996','鼹鼠在地面与地下两层之间推球开路，障碍位置需要在两层共同规划。宫本茂参与制作的这款后期 GB 益智动作游戏常被忽略，但关卡完成度很高。')
add('GBC','The Legend of Zelda: Oracle of Seasons / Oracle of Ages','塞尔达传说：大地之章／时空之章','Nintendo','8MB','2001','双作分别围绕四季变化和过去／现在切换，大地偏动作、时空偏谜题；通关密码可联动另一作并开启完整结局。它们是互补冒险而非红蓝式版本差异。','塞尔达传说')
# 删除被合集的独立 Oracle 行，避免重复占位。
entries=[e for e in entries if e.old not in {'塞尔达传说：时空之章','塞尔达传说：大地之章'}]
add('GBC','Mega Man Xtreme 2','洛克人 X2：灵魂消除者','Capcom','8MB','2001','结合 X 与 Zero 两条可操作路线，Boss 和关卡借用早期 X 系列元素并重新编排。相比首作内容更完整，也延续掌机 Xtreme 支线。','洛克人')
add('GBC','Mario Tennis','马力欧网球（GBC）','Nintendo','8MB','2000','除即时网球外还有 RPG 式校园成长、训练和赛事，属性培养会直接影响击球能力。GBC 版可与 N64 版联动，不是简单缩小移植。','马力欧')
add('GG','Sonic the Hedgehog','刺猬索尼克（GG）','Sega','1MB','1991','针对小屏重新安排关卡和视野，保留金环与高速动作但并非 MD 版的逐关移植。掌机版混沌翡翠获取方式也不同。','索尼克')
add('GG','Sonic the Hedgehog 2','刺猬索尼克 2（GG）','Sega','2MB','1992','GG／MS 版由 Aspect 制作，关卡、Boss 和取得翡翠的方式与 MD 版不同，难度更偏严格跳跃。应按独立掌机作品收藏。','索尼克')
add('GG','Sonic Chaos','索尼克与塔尔斯：混沌','Sega','2MB','1993','索尼克与塔尔斯具备不同动作，塔尔斯可飞行，关卡因此有两套路线思路。GG 原创章节比移植作更能体现掌机节奏。','索尼克')
add('GG','Sonic the Hedgehog: Triple Trouble','索尼克与塔尔斯 2：三重麻烦','Sega','4MB','1994','索尼克与塔尔斯各有专属能力，纳克鲁斯与宝藏猎人方古共同参与争夺翡翠。关卡和道具围绕 GG 原创设计。','索尼克')
add('GG','Shinobi II: The Silent Fury','超级忍 II：沉默之怒','Sega','2MB','1992','乔·武藏可使用五种忍者能力与多名同伴技能，关卡允许一定探索而非纯直线推进。它常被视为 GG 动作游戏的代表作。','超级忍')
add('GG','Castle of Illusion Starring Mickey Mouse','米奇妙妙屋：幻影城堡','Sega','2MB','1991','以投掷和踩击穿越童话关卡，GG 版对 MD 原作进行独立改编，操作温和、画面清晰，适合家庭短局。','米奇妙境')
add('GG','Land of Illusion Starring Mickey Mouse','米奇妙境：幻影大陆','Sega','4MB','1992','加入地图连接、能力道具和较丰富的互动，结构比前作更接近小型动作冒险。唐老鸭等迪士尼角色也参与剧情。','米奇妙境')
add('GG','Shining Force Gaiden','光明力量外传','Sega','2MB','1992','以网格回合战斗和角色成长延续光明力量体系，是 GG 独占掌机篇章。较短战役仍保留队伍配置和地形判断。','光明与梦幻模拟战')
add('GG','Shining Force: The Sword of Hajya','光明力量外传 II：邪神之剑','Sega','2MB','1993','延续 GG 外传的战斗系统并增加双主角部队会合结构。它不是 MD《光明力量 II》的移植。','光明与梦幻模拟战')
add('GG','Shining Force Gaiden: Final Conflict','光明力量外传：最终冲突','Sega','4MB','1995','把 GG 外传故事与 MD 初代角色联系起来，保留探索、队伍培养和战棋战斗。日文文本是主要门槛。','光明与梦幻模拟战')
add('GG','Defenders of Oasis','绿洲守护者','Sega','2MB','1992','以一千零一夜风格的王国冒险为背景，采用小队回合制和自动战斗辅助。它是 GG 少见且完成度较高的原创 JRPG。')
add('GG','GG Aleste','GG 亚雷斯','Compile','2MB','1991','纵版射击使用可蓄力升级的主武器与多种副武器，敌弹速度和视野针对 GG 调整。Compile 的 Aleste 血脉使其成为掌机射击精品。','Aleste')
add('GG','Power Strike II','力量打击 II','Compile','2MB','1993','高速纵版射击强调武器升级和贴近敌弹的风险回报，画面与敌群密度在 GG 上突出。它与 GG Aleste 同属 Compile 掌机射击高峰。','Aleste')
add('GG','Wonder Boy: The Dragon’s Trap','神奇男孩 III：龙之陷阱','Sega','2MB','1989','主角受诅咒后在多种动物形态间变身，能力用于返回旧区域开路。GG 版保留非线性结构，是早期“能力锁探索”的代表。','神奇男孩')
add('GG','Columns','宝石方块','Sega','1MB','1990','下落的三颗宝石可循环换序，横、竖、斜三颗同色即可消除。规则简单，连续消除与高度管理构成长期挑战，也是 GG 早期代表作。')
add('GG','Puyo Puyo Tsu','噗哟噗哟通（GG）','Compile / Sega','2MB','1994','保留四连消除、连锁与对战干扰规则，掌机屏幕让局面更易掌握。它是经典休闲对战的 GG 版本。','噗哟噗哟')
add('GG','Tails Adventure','塔尔斯大冒险','Sega','4MB','1995','塔尔斯以飞行、道具和炸弹探索相互连接的海岛区域，速度不快，重点是能力解锁与路线发现。它区别于索尼克本篇的高速关卡。','索尼克')
add('WS / WSC','Gunpey','Gunpey 线条接龙','Bandai','1MB','1999','在竖排棋盘上上下交换线段，把折线接通左右边界即可消除。以作曲家横井军平命名的原创规则是 WS 首发阵容中最具代表性的益智作品。')
add('WS / WSC','Klonoa: Moonlight Museum','风之少年：月光博物馆','Namco','2MB','1999','风弹抓敌、投掷与二段跳被用于单屏机关解谜，是系列首款掌机作品，也为后来 GBA《梦之帝国》奠定方向。','风之少年')
add('WS / WSC','Mr. Driller','钻地先生','Namco','2MB','1999','向下钻穿彩色方块，连接的大块会坍塌，同时必须管理氧气。得分、路线和生存压力使短局非常紧凑。','钻地先生')
add('WS / WSC','Judgement Silversword: Rebirth Edition','审判银剑：重生版','Qute / M-Kai','2MB','2001','高密度纵版射击使用贴身刀击与远程射击两套手段，关卡和 Boss 节奏在 WS 小屏上仍很清楚。它源自独立开发，是 WSC 射击名作。')
add('WS / WSC','Pocket Fighter','口袋战士','Capcom','4MB','2000','将街霸与恶魔战士角色 Q 版化，宝石强化招式、连锁操作相对简化。WSC 版保留了轻松对战与角色幽默。','街头霸王')
add('WS / WSC','Buffers Evolution','Buffers Evolution','Bandai','2MB','1999','操纵可变形的生命体在场地中占领区域、吞噬对手，规则结合动作与抽象策略。它是 WS 原创阵容中很有实验气质的一作。')
add('WS / WSC','Makaimura for WonderSwan','魔界村 for WonderSwan','Capcom','4MB','1999','采用横屏与竖屏两类关卡，保留高难度跳跃、铠甲破损和武器选择。内容为掌机原创，不是旧作的简单合集。','魔界村')
add('WS / WSC','Digimon: Battle Spirit','数码宝贝：战斗精神','Bandai','4MB','1999','数码兽在平台场地中交战，通过攻击收集数据球并积累进化条件。操作直观，适合本地对战的轻量格斗。','数码宝贝')
add('WS / WSC','One Piece: Grand Battle! Swan Colosseum','海贼王：天鹅斗技场','Bandai','4MB','2000','在横向小场地进行角色对战，结合援助和简单连段。它属于早期海贼王掌机格斗，画面与角色动画利用 WSC 特色。','海贼王')
add('WS / WSC','Riviera: Yakusoku no Chi Riviera','约束之地：利维艾拉','Bandai','4MB','2002','以选择推进场景、有限行动点和回合制战斗构成冒险，资源取舍会影响探索结果。WSC 原版是 Sting 该系列的起点，日文阅读门槛较高。','Dept. Heaven')
add('WS / WSC','Final Fantasy I / II / IV','最终幻想 I／II／IV（WS／WSC）','Square','8MB','2000–2002','WS／WSC 分别重制早期最终幻想，改进画面、界面与部分平衡；其中 IV 为 WSC 版本。此行是三个独立商品的收藏组，日文版文本门槛较高。','最终幻想')
add('WS / WSC','Front Mission','前线任务（WSC）','Square','4MB','2002','把 SFC 初代机甲战棋带到 WSC，保留部件损坏、武器射程与阵营战争。画面针对掌机重绘，日文菜单和剧情需要一定阅读基础。','前线任务')
add('NES / FC','Galaxian','小蜜蜂（FC 版）','Namco','0.5MB','1984','外星机群在编队中轮番俯冲，玩家要判断离队轨迹并抓住反击间隙。FC 版把 1979 年街机《Galaxian》的固定射击规则带进家庭，它才是中文通常所称的“小蜜蜂”，不要与续作《Galaga》混名。')
add('NES / FC','Galaga','大蜜蜂（FC 版）','Namco','0.5MB','1985','在《Galaxian》的俯冲攻击上加入 Boss 捕获、救回双机火力与挑战关，风险回报比前作更丰富。FC 版于 1985 年发行，中文常称“大蜜蜂”；与街机原版及《Galaxian》都分开计数。')
add('NES / FC','Fire Emblem: Shadow Dragon and the Blade of Light','火焰之纹章：暗黑龙与光之剑','Nintendo','1MB','1990','马尔斯复国战争把单位职业、武器耐久和永久阵亡结合，是系列首作。界面与移动节奏古老，保留它是为了理解整个战棋谱系。','火焰之纹章')
add('NES / FC','Dai-2-Ji Super Robot Taisen','第 2 次超级机器人大战','Banpresto','1MB','1991','高达、魔神与盖塔等机体进入网格战棋，精神指令和改造开始形成系列基本循环。它在中文圈的中文化传播尤其广。','超级机器人大战')
add('SNES / SFC','Dragon Quest III: The Seeds of Salvation','勇者斗恶龙 III：传说的开始（SFC 重制版）','Enix','8MB','1996','以 SFC 音画重制 FC 第三作，保留转职、昼夜与广阔世界，并调整界面和平衡。它不是 GBA 游戏，也与 NDS 没有对应原生移植。','勇者斗恶龙')
add('GBA','Mother 3','地球冒险 3','Nintendo','32MB','2006','以章节切换多名角色视角，回合战斗可随音乐节拍追加连击。只在日本正式发行，中文化让其亲情、社区与失落主题更易被理解。','MOTHER')
add('GB','Seiken Densetsu: Final Fantasy Gaiden / Final Fantasy Adventure','圣剑传说：最终幻想外传','Square','1MB','1991','以即时武器攻击、场景解谜和角色成长展开冒险，是圣剑传说的 GB 起点。海外曾挂 Final Fantasy Adventure 名称，但不属于最终幻想正传。','圣剑传说')
add('GBA','Sword of Mana','新约圣剑传说','Square Enix','16MB','2003','重新诠释 GB 初代，以男女双视角、昼夜和武器锻造扩展动作 RPG。它是 GBA 重制，不应与 SFC《圣剑传说 2》混为一作。','圣剑传说')
add('PS1','Legend of Mana','圣剑传说：玛娜传奇','Square','700MB','1999','以地图放置 Artifact 生成地区，事件、宠物、锻造和家园系统形成非线性冒险。它强调世界构筑与氛围，不是圣剑 3 的直接续作。','圣剑传说')
add('PS1','SaGa Frontier','浪漫沙加：开拓者','Square','700MB','1997','七名主角拥有各自目标和自由剧本，闪悟、种族成长与非线性探索体现沙加式系统实验。完成度带有鲜明取舍。','沙加')
add('PS1','SaGa Frontier 2','浪漫沙加：开拓者 2','Square','500MB','1999','以世代传承和多段历史事件组织故事，战斗引入连携与角色成长，手绘水彩画面独特。系统与初代自由剧本路线不同。','沙加')
add('SNES / SFC','Treasure of the Rudra','鲁多拉秘宝','Square','8MB','1996','以自由组合言灵创造魔法，词根与后缀会改变效果、属性和消耗。Square 的 SFC 后期 RPG 以这套文字系统著称。')
# 用户追加候选逐款落实；无对应街机版或非本机平台者不硬凑。
add('MAME','Puyo Puyo Sun','噗哟噗哟 SUN','Compile / Sega','64MB','1996','在连锁对战上加入太阳噗哟，消除它们可向对手发送更强干扰。街机原版使用 ST-V，归入 MAME 而非假设所有版本都属于 FBNeo。','噗哟噗哟')
add('MD / Genesis','VS Puyo Puyo SUN / Futari de Puyo Puyo SUN','双人噗哟噗哟 SUN','Sega','4MB','2022','Mega Drive Mini 2 新增的官方双人移植，保留 SUN 规则并加入 Fusion Sun／Fading Sun 变体。它不是 1996 年旧卡带，也不含完整单人剧情模式。','噗哟噗哟')
add('PSP','Me & My Katamari','块魂：我与我的块魂','Namco','2GB','2005','推动黏球卷起物件并逐步扩大可收集尺度，以动物委托和岛屿界面组织任务。它是系列首款掌机作，十字键与按键模拟双摇杆需要适应；1× 渲染下仍需实测物件密集场景。','块魂')
add('PS1','Theme Hospital','主题医院','Electronic Arts','400MB','1998','规划诊疗室、培训员工并处理夸张病症，在排队、设备维护、声誉和利润间取舍。Bullfrog 的经营幽默来自扎实系统；PS1 手柄操作不如 PC 鼠标，但慢节奏适合电视游玩。','Theme 经营模拟')
add('GBA','Tomato Adventure','番茄酱王国大冒险','Nintendo','16MB','2002','主角为营救女友进入番茄酱王国，战斗用“ gimmick ”玩具和按键小游戏取代普通指令。AlphaDream 后来把动作指令思路带入马力欧与路易吉 RPG；它与斯塔菲无关。')
add('GBA','Densetsu no Stafy','传说的斯塔菲','Nintendo','8MB','2002','海星王子斯塔菲以旋转、游泳和水下机动穿越海洋关卡，帮助沿途角色并收集宝箱。TOSE 与任天堂把平台动作做得温和亲切，首作原定 GBC 后转向 GBA。','传说的斯塔菲')
add('GBA','Densetsu no Stafy 2','传说的斯塔菲 2','Nintendo','16MB','2003','延续海洋动作与角色委托，加入更多变身、载具和斯塔菲的家人相关剧情。关卡目标比单纯抵达终点更丰富，日语阅读会影响部分委托理解。','传说的斯塔菲')
add('GBA','Densetsu no Stafy 3','传说的斯塔菲 3','Nintendo','16MB','2004','第三部 GBA 作加入妹妹斯塔碧，并以双角色能力和更丰富的关卡互动扩展海洋冒险。它是 GBA 三部曲的完成篇，不是 NDS 海外版《The Legendary Starfy》。','传说的斯塔菲')
add('NDS','Densetsu no Stafy 4','传说的斯塔菲 4','Nintendo','64MB','2006','把海洋平台动作扩展到双屏，斯塔菲与斯塔碧的能力、变身和触摸操作共同参与关卡。它是系列第四作，日版剧情与委托需要一定阅读。','传说的斯塔菲')
add('NDS','The Legendary Starfy','传说的斯塔菲：对决！达伊尔海贼团','Nintendo','128MB','2008','系列第五作，也是当年唯一正式推出英文版的斯塔菲游戏；海底探索、变身和伙伴协力延续轻快节奏。不能把英文标题误当成 GBA 初代。','传说的斯塔菲')
# 基连野望按正式商品拆分，装甲将军并无街机原版。
entries=[e for e in entries if e.en!='Mobile Suit Gundam: Gihren’s Greed and related PlayStation titles']
add('PS1','Mobile Suit Gundam: Gihren’s Greed','机动战士高达：基连的野望——吉翁独立战争记','Bandai','700MB','1998','围绕一年战争配置将领、预算、生产与机体开发，在战略地图上推进联邦或吉翁战役。动画事件和 IF 路线把高达编年史变成可改写的战争推演，日文信息量较大。','基连的野望')
add('PS1','Mobile Suit Gundam: Gihren’s Greed – Blood of Zeon','机动战士高达：基连的野望——吉翁的系谱','Bandai','900MB','2000','加入停战与条约、机体改造和更多 OVA 角色，并把战线延伸至 Z 高达相关势力。它扩展的不只是剧本，也包括政治与军工系统；PS1 与 DC 版分开识别。','基连的野望')
add('PSP','Mobile Suit Gundam: Gihren’s Greed – Axis no Kyoui V','机动战士高达：基连的野望——阿克西斯的威胁 V','Bandai Namco Games','2GB','2009','V 版扩充无印《阿克西斯的威胁》的机体、角色与势力，战役横跨一年战争至后续宇宙世纪冲突。静态事件与回合战略适合低负载设置，但大规模战场和日文菜单仍需实测。','基连的野望')
add('PS1','Brigandine: The Legend of Forsena','幻想大陆战记：弗鲁塞那传说','Hearty Robin / Atlus','700MB','1998','选择国家经营符文骑士与召唤魔物，在大陆据点争夺和小队六角格战斗间循环。多国视角、职业转职与魔物编成带来重玩价值，北美版由 Atlus 发行。','幻想大陆战记')
add('PS1','Brigandine: Grand Edition','幻想大陆战记：Grand Edition','Hearty Robin','900MB','2000','官方扩展版让艾斯加雷斯帝国正式可玩，新增最多六人轮玩、事件配音、职业和魔物，并调整战斗规则。仅在日本发行；它不是玩家“威力加强版”，也不等于网络联机。','幻想大陆战记')
add('PS1','Gradius Gaiden','宇宙巡航机外传','Konami','600MB','1996','PS1 原创外传提供四种力量槽配置与双机合作，关卡和大型 Boss 专为家用机设计。它不是街机 Gradius IV，也不应混入 FBNeo 合集。','宇宙巡航机与兵蜂')
# DOSBox 管理 DOS 与轻量 Win3.x；Win95／98 游戏另走 Batocera Wine。
for en,zh,pub,size,year,note,series,category,subgenre in DOS_GAMES:
    if category!='射击':add('DOS',en,zh,pub,size,year,note,series)
for en,zh,pub,size,year,note,series,category,subgenre in WINDOWS_GAMES:
    if category not in {'射击','射击（STG）','动作射击'}:add('Win95 / Win98',en,zh,pub,size,year,note,series)
# 低评价凑数及不属于 FBNeo 的 Atomiswave 条目不保留。
entries=[e for e in entries if e.en not in {'Burning Fight','Blue Stinger','Sega GT','Sonic Spinball','Sonic 3D Blast','Knights of Valour: The Seven Spirits','Capcom vs SNK 1','Capcom vs SNK 2'}]
# SFC 只有 Der Langrisser（MD 初代的重制），没有另一张 Langrisser II 卡带。
entries=[e for e in entries if not (e.platform=='SNES / SFC' and e.en=='Langrisser II / Der Langrisser')]
for e in entries:
    if e.platform=='SNES / SFC' and e.en=='Trials of Mana / Seiken Densetsu 3':e.year='1995'
    if e.platform=='FBNeo' and e.en=='Gradius / Gradius II / Gradius III / Gradius Gaiden':
        e.en='Gradius / Gradius II / Gradius III';e.zh='宇宙巡航机 I／II／III';e.note='三部街机编号作依次扩展力量槽、武器组和高密度关卡，体现从固定配置到多武器选择的演进。PS1 原创《Gradius Gaiden》另有独立条目，不再混作街机 ROM。'
    if e.platform=='FBNeo' and e.en=='TwinBee / Detana!! TwinBee / Pop’n TwinBee':
        e.en='TwinBee / Detana!! TwinBee';e.zh='兵蜂／出击！！兵蜂';e.note='初代以打铃铛变色强化和双人合作为核心，Detana 加入蓄力、角色演出与更完整关卡。SFC 家用原创《Pop’n TwinBee》保留在 SNES 表，不在这里重复占位。'
    if e.platform=='FBNeo' and e.en=='Golden Axe (Arcade) / Golden Axe: The Revenge of Death Adder':
        e.en='Golden Axe (Arcade)';e.zh='战斧（街机）';e.note='以魔法储量、骑乘生物、投技和双人合作建立战斧的街机规则。它不是 MD II／III；同平台独立条目《The Revenge of Death Adder》也不重复塞进本合集。'
    if e.platform=='MD / Genesis' and e.en=='Langrisser II / Der Langrisser':
        e.en='Langrisser II';e.zh='梦幻模拟战 II';e.year='1994';e.note='艾尔文与光辉后裔的战争延续兵种、指挥官范围和转职系统，关卡规模与角色阵容较初代扩大。此条只收 MD 原版；《Der Langrisser》是 SFC 对 MD 初代的多路线重制，不是本作的移植。'
    if e.platform=='MD / Genesis' and e.en=='Advanced Daisenryaku':
        e.en='Advanced Daisenryaku: Deutsch Dengeki Sakusen';e.zh='高级大战略：德意志电击作战';e.note='SystemSoft 开发、Sega 于 1991 年发行的 MD 战略游戏，以二战欧洲战场、武器单位、燃料弹药和补给为核心。它承继电脑《大战略》系列，但没有对应 DOS 原版可再复制一条；也不是与 MD 版互为重制的另一款游戏。'
    if e.en=='装甲勇士Armored Warriors':e.en='Armored Warriors';e.zh='装甲勇士'
    if e.platform=='FBNeo' and e.en in {'Raiden','Raiden II'}:e.pub='Seibu Kaihatsu'
    if e.platform=='PSP' and e.en=='Ys I & II Chronicles':e.year='2009'
    if e.en=='Lumines':
        e.en='Lumines: Puzzle Fusion';e.zh='音乐方块';e.pub='Bandai / Ubisoft';e.year='2004'
    if e.en=='Lumines II':e.zh='音乐方块 II';e.pub='Q Entertainment / Buena Vista Games'
    if e.en=='Double Dragon III: The Sacred Stones':e.note='三国圣石与环球旅程把拳脚清版扩展为队伍换人，但节奏和判定评价不如 II。仅作为系列完整性例外保留，家庭首次游玩优先二代。'

# 自动从 libretro 元数据核对年份；模糊匹配仅接受高相似候选，之后还有人工规则。
files={
'NES / FC':['Nintendo - Nintendo Entertainment System','Nintendo - Family Computer Disk System'],'GB':['Nintendo - Game Boy'],'GBC':['Nintendo - Game Boy Color'],
'MD / Genesis':['Sega - Mega Drive - Genesis'],'SNES / SFC':['Nintendo - Super Nintendo Entertainment System'],'N64':['Nintendo - Nintendo 64'],
'PCE (PC Engine / TurboGrafx-16)':['NEC - PC Engine - TurboGrafx 16'],'GBA':['Nintendo - Game Boy Advance'],'NDS':['Nintendo - Nintendo DS'],
'GG':['Sega - Game Gear'],'WS / WSC':['Bandai - WonderSwan','Bandai - WonderSwan Color'],'PSP':['Sony - PlayStation Portable']}
def norm(s):
    s=re.sub(r'\s*\([^)]*\)','',s);s=re.sub(r',\s+(The|A|An)$','',s,flags=re.I)
    s=s.replace('&','and').replace('’',"'").replace('–','-')
    return re.sub(r'[^a-z0-9]+','',s.lower())
idx={}
for p,fs in files.items():
    d={}
    for f in fs:
        fp=ROOT/'libretro-database/metadat/releaseyear'/f'{f}.dat'
        if not fp.exists():continue
        for n,y in re.findall(r'comment "([^"]+)"\s+releaseyear "(\d{4})"',fp.read_text(errors='ignore')):d.setdefault(norm(n),set()).add(y)
    idx[p]=d
# MAME 的名称、年份和制造方。
mame={}
for block in re.findall(r'game \((.*?)\n\)',(ROOT/'libretro-database/metadat/mame/MAME.dat').read_text(errors='ignore'),re.S):
    n=re.search(r'name "([^"]+)"',block);y=re.search(r'year "(\d{4})"',block);d=re.search(r'developer "([^"]+)"',block)
    if n and y:mame.setdefault(norm(n.group(1)),set()).add((y.group(1),d.group(1) if d else ''))
for e in entries:
    if e.year:continue
    d=mame if e.platform in {'MAME','FBNeo'} else idx.get(e.platform,{})
    candidates=[e.en]+re.split(r' / ',e.en)
    found=None
    for c in candidates:
        vals=d.get(norm(c))
        if vals:
            found=sorted(vals)[0];break
    if not found and d and len(e.en)>5:
        key=norm(e.en); matches=difflib.get_close_matches(key,list(d),n=1,cutoff=.94)
        if matches:found=sorted(d[matches[0]])[0]
    if found:
        e.year=found[0] if isinstance(found,tuple) else found

# 数据库不能可靠覆盖的版本、合集和光盘游戏，按具体版本核定。
Y={
'Super Mario Bros. 2 (USA)':'1988','Dragon Quest II: Luminaries of the Legendary Line':'1987','Dragon Quest III: The Seeds of Salvation':'1988','Dragon Quest IV: Chapters of the Chosen':'1990',
'1942':'1984','1943: The Battle of Midway':'1987','Feng Shen Bang: Fu Mo San Jian Xia':'1995','Duck Hunt':'1984',
'The Legend of Zelda: Link’s Awakening':'1993','The Legend of Zelda: Link’s Awakening DX':'1998','Pokémon Red / Green / Blue / Yellow':'1996–1998','Pokémon Gold / Silver / Crystal':'1999–2000',
'The Legend of Zelda: Oracle of Seasons / Oracle of Ages':'2001','Final Fantasy Legend II / SaGa 2: Hihou Densetsu':'1990','Final Fantasy Legend III / SaGa 3: Jikuu no Hasha':'1991',
'Game & Watch Gallery 1–3':'1997–1999','Kirby’s Dream Land 1 / 2':'1992–1995','Shining Force II: Ancient Sealing':'1993','Raiden Trad':'1991',
'Final Fantasy IV':'1991','Final Fantasy V':'1992','Final Fantasy VI':'1994','Dragon Quest V: Hand of the Heavenly Bride':'1992','Dragon Quest VI: Realms of Revelation':'1995',
'Tactics Ogre: Let Us Cling Together':'1995','Tales of Phantasia':'1995','EarthBound / Mother 2':'1994','Shin Megami Tensei I / II':'1992–1994',
'Street Fighter Alpha 2':'1996','The Legend of Zelda: Ocarina of Time':'1998','The Legend of Zelda: Majora’s Mask':'2000','1080° Snowboarding':'1998',
'Ys Book I & II':'1989','Ys III: Wanderers from Ys':'1991','Ys IV: The Dawn of Ys':'1993','Tengai Makyou II: Manji Maru':'1992','Tengai Makyou: Fuun Kabuki Den':'1993',
'Bomberman \'93 / \'94':'1992–1993','Valis: The Fantasm Soldier / Valis II / III / IV':'1986–1993','Ginga Fukei Densetsu Sapphire':'1995',
'Gyakuten Saiban / Phoenix Wright: Ace Attorney':'2001','Gyakuten Saiban 2 / Phoenix Wright: Ace Attorney – Justice for All':'2002','Gyakuten Saiban 3 / Phoenix Wright: Ace Attorney – Trials and Tribulations':'2004',
'Phoenix Wright: Ace Attorney / Justice for All / Trials and Tribulations (DS)':'2005–2007','Dragon Quest IV: Chapters of the Chosen (NDS)':'2007',
'Romance of the Three Kingdoms VII':'2000','Daisenryaku: Master Combat':'1998','Medal of Honor':'1999','Medal of Honor: Underground':'2000',
'Final Fantasy VII':'1997','Final Fantasy VIII':'1999','Final Fantasy IX':'2000','Final Fantasy Tactics':'1997','Parasite Eve':'1998','Parasite Eve II':'1999',
'Vagrant Story':'2000','Xenogears':'1998','Front Mission 3':'1999','Tactics Ogre: Let Us Cling Together (PlayStation)':'1997',
'Silent Hill':'1999','Dino Crisis':'1999','Dino Crisis 2':'2000','Valkyrie Profile':'1999','Grandia':'1997','Suikoden':'1995','Suikoden II':'1998','Chrono Cross':'1999',
'Star Ocean: The Second Story':'1998','The Legend of Dragoon':'1999','Tales of Destiny':'1997','Tales of Eternia':'2000','Brave Fencer Musashi':'1998',
'Lunar: Silver Star Story Complete':'1996','Lunar 2: Eternal Blue Complete':'1998','Wild Arms':'1996','Wild Arms 2nd Ignition':'1999','Popolocrois Monogatari':'1996','Clock Tower: The First Fear':'1995',
'Crash Bandicoot 1 / 2: Cortex Strikes Back / 3: Warped':'1996–1998','Spyro the Dragon 1 / 2: Ripto’s Rage! / 3: Year of the Dragon':'1998–2000',
'Tekken 3':'1997','R4: Ridge Racer Type 4':'1998','Gran Turismo':'1997','Gran Turismo 2':'1999','Tomb Raider I / II / III':'1996–1998','Syphon Filter':'1999',
'Ape Escape':'1999','PaRappa the Rapper':'1996','Vib-Ribbon':'1999','Winning Eleven / Pro Evolution Soccer (PlayStation)':'1995–2002','Dance Dance Revolution / beatmania':'1998–1999',
'Castlevania Chronicles':'1999','Revelations: Persona':'1996','Persona 2: Innocent Sin':'1999','Persona 2: Eternal Punishment':'2000','Shin Megami Tensei':'1992','Shin Megami Tensei II':'1994','Shin Megami Tensei if...':'1994',
'Digimon World':'1999','Digimon World 2':'2000','Digimon World 3 / 2003':'2002','Mobile Suit Gundam: Gihren’s Greed and related PlayStation titles':'1998–2000','Tokimeki Memorial 1 / 2':'1994–1999',
'Front Mission Alternative':'1997','Vandal Hearts':'1996','Panzer Front':'1999','Sid Meier’s Civilization':'1999',
'Shenmue':'1999','Shenmue II':'2001','Dead or Alive 2':'2000','Soulcalibur':'1999','Street Fighter III: Double Impact':'1999','Crazy Taxi':'2000','Resident Evil – Code: Veronica':'2000','Ikaruga':'2002','Jet Set Radio':'2000','Sonic Adventure':'1998','Sonic Adventure 2':'2001','Power Stone':'1999','Power Stone 2':'2000',
'Marvel vs. Capcom: Clash of Super Heroes':'1999','Marvel vs. Capcom 2: New Age of Heroes':'2000','Capcom vs. SNK: Millennium Fight 2000':'2000','Capcom vs. SNK 2: Mark of the Millennium 2001':'2001','Guilty Gear X':'2000','Virtua Fighter 3tb':'1999',
'Sakura Wars 3: Is Paris Burning?':'2001','Sakura Wars 4: Fall in Love, Maidens':'2002','Phantasy Star Online':'2000','Grandia II':'2000','Sega Rally 2':'1999','Daytona USA 2001':'2001','Rez':'2001','Space Channel 5: Part 2':'2002','The Typing of the Dead':'2001','Toy Commander':'1999','Hydro Thunder':'1999','Blue Stinger':'1999','Bangai-O':'1999','Sega GT':'2000','Crazy Taxi 2':'2001','Skies of Arcadia':'2000','Street Fighter III: 3rd Strike':'2000','Virtua Tennis / Virtua Tennis 2':'2000–2001','Metropolis Street Racer':'2000','ChuChu Rocket!':'1999','Project Justice':'2000','Samba de Amigo':'2000',
'Monster Hunter Portable 3rd':'2010','Monster Hunter Freedom Unite / Monster Hunter Portable 2nd G':'2008','The Legend of Heroes: Trails in the Sky FC':'2006','The Legend of Heroes: Trails in the Sky SC':'2007','The Legend of Heroes: Trails in the Sky the 3rd':'2008','The Legend of Heroes: Zero no Kiseki':'2010','The Legend of Heroes: Ao no Kiseki':'2011','Nayuta no Kiseki / The Legend of Nayuta: Boundless Trails':'2012','The Legend of Heroes II: Prophecy of the Moonlight Witch / III: White Witch / IV: A Tear of Vermillion / V: Cagesong of the Ocean':'2004–2006',
'Crisis Core: Final Fantasy VII':'2007','The 3rd Birthday':'2010','Shin Megami Tensei: Persona 3 Portable':'2009','Ridge Racer':'2004','Hatsune Miku: Project DIVA':'2009','Hatsune Miku: Project DIVA 2nd':'2010','Hatsune Miku: Project DIVA Extend':'2011','Super Robot Taisen A Portable':'2008','Final Fantasy Tactics: The War of the Lions':'2007','Ys I & II Chronicles':'2009','Ys: The Oath in Felghana':'2005','Ys Seven':'2009','Valkyria Chronicles II':'2010','Valkyria Chronicles III':'2011','Disgaea: Afternoon of Darkness':'2006','Kingdom Hearts: Birth by Sleep':'2010','LocoRoco':'2006','Patapon':'2007','Lumines':'2004','Everybody’s Golf / Hot Shots Golf':'2004','DJMax Portable 1 / 2 / Clazziquai / Black Square':'2006–2008','Taiko no Tatsujin Portable':'2005','Silent Hill: Origins':'2007','Silent Hill: Shattered Memories':'2009','Memories Off / Clannad / Steins;Gate / Higurashi / Fate/Extra':'2008–2011','Dissidia Final Fantasy':'2008','Hatsune Miku: Project DIVA 2nd':'2010','Grand Theft Auto: Chinatown Wars':'2009','Tekken: Dark Resurrection':'2006','Wipeout Pure':'2005','Jeanne d’Arc':'2006','Castlevania: The Dracula X Chronicles':'2007','Daxter':'2006','LittleBigPlanet':'2009','Lumines II':'2006',
}
Y.update({
'Nakahara no Hasha: Sangoku Shouseiden':'1988','The Goonies':'1986','The Legend of Kage':'1985','Wario Land: Super Mario Land 3':'1994','Metal Gear Solid: Ghost Babel':'2000','Castlevania II: Belmont’s Revenge':'1991','Castlevania Legends':'1997','Ninja Gaiden Shadow':'1991','Double Dragon II':'1991','Teenage Mutant Ninja Turtles: Fall of the Foot Clan':'1990','Dragon Ball Z: Goku Hishouden / Goku Gekitouden':'1994–1995','聖闘士セイントパラダイス 最強の戦士たち / Saint Paradise: Saikyou no Senshitachi':'1992','Dr. Mario':'1990','Yoshi':'1991',
'Sonic the Hedgehog 3 & Knuckles':'1994','Altered Beast':'1988','Nobunaga’s Ambition: Zenkokuban':'1986','Advanced Daisenryaku':'1991','Thunder Force IV: Lightening Force':'1992','The Revenge of Shinobi':'1989',"Street Fighter II': Special Champion Edition":'1993','Shinobi III':'1993','Phantasy Star IV: The End of the Millennium':'1993','Beyond Oasis / The Story of Thor':'1994',
'Fire Emblem: Mystery of the Emblem':'1994','Fire Emblem: Genealogy of the Holy War':'1996','Langrisser':'1991','Langrisser II / Der Langrisser':'1994–1995','Front Mission: Gun Hazard':'1996','Nobunaga’s Ambition: Bushou Fuuunroku':'1990','Nobunaga’s Ambition: Haouden':'1992','Nobunaga’s Ambition: Tenshouki':'1993','Street Fighter II Turbo: Hyper Fighting':'1993','Star Fox 2':'2017','Street Fighter Alpha 2':'1996','Parodius Da!':'1992','Disney’s Aladdin':'1993','Disney’s The Lion King':'1994','The Lost Vikings':'1992',
'Sin and Punishment: Successor of the Earth':'2000','Wave Race 64':'1996','Mario Party 1 / 2 / 3':'1998–2000','Tengai Makyou: Ziria':'1989','Gate of Thunder':'1992','Lords of Thunder':'1993','Dungeon Explorer II':'1993','Cho Aniki':'1992','Cosmic Fantasy 2':'1991','Cotton':'1993','Xevious':'1990','Tokimeki Memorial':'1994','Genpei Touma Den':'1990',
'Fire Emblem: The Binding Blade':'2002','Fire Emblem: The Blazing Blade':'2003','Super Mario World: Super Mario Advance 2':'2001','Yoshi’s Island: Super Mario Advance 3':'2002','Mega Man Battle Network 3: Blue / White':'2002',
'Ace Attorney Investigations: Miles Edgeworth':'2009','Gyakuten Kenji 2 / Ace Attorney Investigations 2':'2011','Ghost Trick: Phantom Detective':'2010','Professor Layton and the Last Specter':'2008','Fire Emblem: Shadow Dragon':'2008','Fire Emblem: New Mystery of the Emblem':'2010','Super Robot Taisen W':'2007','Super Robot Taisen K':'2009','Super Robot Taisen L':'2010','Rhythm Heaven / Rhythm Tengoku Gold':'2008','Etrian Odyssey':'2007','Etrian Odyssey II: Heroes of Lagaard':'2008','999: Nine Hours, Nine Persons, Nine Doors':'2009','Inazuma Eleven':'2008','Inazuma Eleven 2: Kyoui no Shinryakusha – Fire / Blizzard':'2009','Kingdom Hearts 358/2 Days':'2009','Digimon World Dawn / Dusk':'2006','Rune Factory: A Fantasy Harvest Moon':'2006','Rune Factory 2: A Fantasy Harvest Moon':'2007','Harvest Moon: Grand Bazaar':'2008','Yoshi’s Island DS':'2006','Mega Man ZX':'2006','Mega Man ZX Advent':'2007','Mega Man Star Force: Pegasus / Leo / Dragon':'2006','Golden Sun: Dark Dawn':'2010','Final Fantasy III (Nintendo DS)':'2006','Final Fantasy IV (Nintendo DS)':'2007','SaGa 2: Hihou Densetsu – Goddess of Destiny':'2009','Final Fantasy Crystal Chronicles: Echoes of Time':'2009','Dragon Quest Monsters: Joker':'2006','Dragon Quest Monsters: Joker 2':'2010','Pokémon Mystery Dungeon: Blue Rescue Team':'2005','Pokémon Mystery Dungeon: Explorers of Time':'2007','Pokémon Mystery Dungeon: Explorers of Darkness':'2007','Pokémon Mystery Dungeon: Explorers of Sky':'2009','Pokémon Ranger':'2006','Daigasso! Band Brothers':'2004','Brain Age: Train Your Brain in Minutes a Day!':'2005','Nintendogs':'2005','Cooking Mama':'2006',
'Samurai Shodown II':'1993','Samurai Shodown':'1993','Samurai Shodown III: Blades of Blood':'1995','Samurai Shodown IV: Amakusa’s Revenge':'1996','Samurai Shodown V':'2003','The Last Blade':'1997','The Last Blade 2':'1998','Fatal Fury: King of Fighters':'1991','Fatal Fury 2':'1992','Fatal Fury 3: Road to the Final Victory':'1995','Real Bout Fatal Fury':'1995','Real Bout Fatal Fury Special':'1997','Art of Fighting':'1992','Art of Fighting 2':'1994','Kizuna Encounter: Super Tag Battle / Fu’un Super Combo':'1996','Savage Reign':'1995','Galaxy Fight':'1995','Kizuna Encounter':'1996','Neo Turf Masters':'1996','Street Fighter III: 2nd Impact':'1997','JoJo’s Bizarre Adventure: Heritage for the Future':'1999','Capcom vs SNK 1':'2000','Capcom vs SNK 2':'2001','Gunbird 1':'1994','Sol Divide':'1997','Truxton':'1988','Mars Matrix':'2000','Double Dragon 1 / 2 / 3 (Arcade)':'1987–1990','Joe & Mac: Caveman Ninja':'1991',
'Resident Evil':'1996','Resident Evil 2':'1998','Resident Evil 3: Nemesis':'1999','Metal Gear Solid':'1998','Romance of the Three Kingdoms V':'1995','Romance of the Three Kingdoms VI':'1998','Nobunaga’s Ambition: Shouseiroku':'1997','Nobunaga’s Ambition: Reppuuden':'1998','Super Robot Taisen Alpha':'2000','Super Robot Taisen Alpha Gaiden':'2001','Dai-2-Ji Super Robot Taisen (PlayStation)':'1999','Panzer General':'1996','Allied General':'1997'
})
# 少量混合标题按原稿键强制使用完整商品名。
for e in entries:
    if e.old=='街头霸王2 Special Champion Edition':e.en="Street Fighter II': Special Champion Edition";e.zh='街头霸王 II：冠军加强版'
    if e.old=='街头霸王Alpha 2':e.en='Street Fighter Alpha 2';e.zh='少年街霸 Alpha 2'
    if 'The Story of Thor' in e.old:e.en='Beyond Oasis / The Story of Thor';e.zh='光之继承者'
    if e.old=='火枪英雄 Gunstar Heroes':e.en='Gunstar Heroes';e.zh='火枪英雄'
    if e.old=='蚯蚓战士 Earthworm Jim 1':e.en='Earthworm Jim';e.zh='蚯蚓战士'
    if e.old=='蚯蚓战士 Earthworm Jim 2':e.en='Earthworm Jim 2';e.zh='蚯蚓战士 2'
    if e.old=='实况足球WEP系列':e.en='World Soccer Winning Eleven 2002';e.zh='实况足球：胜利十一人 2002';e.year='2002'
    if e.old=='DDR/beatmania/太鼓达人':e.en='Dance Dance Revolution';e.zh='劲舞革命';e.year='1999'
# NDS／PS1 同名重制与系列年代表。
for e in entries:
    if not e.year:e.year=Y.get(e.en,'')
    if not e.year and e.platform=='NDS':
        e.year=Y.get(e.en,'')
    if not e.year and re.search(r'Knights of Valour|Oriental Legend',e.en):e.year='1999–2003'
    if not e.year and re.search(r'Metal Slug 1 / 2 / X / 3 / 4 / 5',e.en):e.year='1996–2003'
    if not e.year and e.en in {'Pac-Man / Ms. Pac-Man','Donkey Kong / Donkey Kong Jr.','Galaga / Galaxian'}:e.year={'Pac-Man / Ms. Pac-Man':'1980–1982','Donkey Kong / Donkey Kong Jr.':'1981–1982','Galaga / Galaxian':'1979–1981'}[e.en]
    if not e.year and e.en=='Street Fighter II: Champion Edition':e.year='1992'

# 发行方兜底只使用已核定的明确值。
for e in entries:
    if e.pub in {'','—','见商品版本'}:
        e.pub={'Memories Off / Clannad / Steins;Gate / Higurashi / Fate/Extra':'5pb. / CyberFront / Imageepoch / Capcom'}.get(e.en,'')

# 每作一个主品类和一个细分品类。
def genre(e):
    s=e.en
    manual_genres={
        'Tengai Makyou II: Manji Maru':('角色扮演','回合／迷宫／叙事 RPG'),
        'Tony Hawk’s Pro Skater 2':('竞速／体育','体育与运动'),
        'Dragon Ball: Advanced Adventure':('格斗／清版动作','清版动作与合作'),
    }
    if s in manual_genres:return manual_genres[s]
    # 精确覆盖优先于宽泛正则，避免 Sapphire 被当射击、Mario RPG 被当平台动作。
    overrides=[
        (r'Pokémon Ruby / Sapphire|Super Mario RPG: Legend of the Seven Stars|Paper Mario|Mario & Luigi:.*|Mega Man Battle Network.*|Mega Man Star Force:.*|The Legend of Heroes II: Prophecy of the Moonlight Witch.*|Tengai Makyou: Ziria|Tengai Makyou: Fuun Kabuki Den|Skies of Arcadia|Live A Live|Saint Seiya: Ougon Densetsu|Dragon Ball Z: Goku Hishouden / Goku Gekitouden','角色扮演','回合／迷宫／叙事 RPG'),
        (r'Pokémon Trading Card Game|聖闘士セイントパラダイス 最強の戦士たち / Saint Paradise: Saikyou no Senshitachi','战略／战棋','卡牌与策略对战'),
        (r'Pokémon Stadium(?: 2)?','战略／战棋','大战略与军团'),
        (r'Pokémon Snap','模拟／音乐／派对','经营与生活模拟'),
        (r'Dissidia Final Fantasy|Yie Ar Kung-Fu|Martial Masters|The Killing Blade|Red Earth / War-Zard|Nekketsu Kakutou Densetsu','格斗／清版动作','一对一与场地格斗'),
        (r'Jeanne d’Arc|Bahamut Lagoon|Sakura Wars [34].*|Advance Wars.*|Military Madness','战略／战棋','网格战术'),
        (r'Front Mission Alternative','战略／战棋','即时军事模拟'),
        (r'Metal Max.*|Metal Saga.*','角色扮演','回合／迷宫／叙事 RPG'),
        (r'Phantasy Star Online|Crystalis|Wonder Boy in Monster World|Soul Blazer|Illusion of Gaia|E\.V\.O\.: Search for Eden|Neutopia(?: II)?|Crisis Core: Final Fantasy VII|The 3rd Birthday|Nayuta no Kiseki.*|Final Fantasy Crystal Chronicles: Echoes of Time|Pokémon Ranger|The World Ends with You|Ys: The Oath in Felghana|Brave Fencer Musashi|Front Mission: Gun Hazard|Uncharted Waters: New Horizons / Daikoukai Jidai II|Dark Seal / Gate of Doom','角色扮演','动作 RPG'),
        (r'1942|1943: The Battle of Midway|Cho Aniki|Thunder Blade|Blazing Star','射击（STG）','横纵卷轴射击'),
        (r'Nakahara no Hasha: Sangoku Shouseiden','战略／战棋','大战略与军团'),
        (r'Shadow of the Ninja|Takahashi Meijin no Bouken Jima IV|Doraemon|Hokuto no Ken|Kid Dracula.*|Teenage Mutant Ninja Turtles: Fall of the Foot Clan|Valis:.*|Banjo-Kazooie|Banjo-Tooie|Conker\'s Bad Fur Day|Mischief Makers|Ape Escape','平台动作','横版／单屏／3D 平台'),
        (r'Teenage Mutant Ninja Turtles','平台动作','横版／单屏／3D 平台'),
        (r'Teenage Mutant Ninja Turtles III: The Manhattan Project|Nekketsu Kouha Kunio-kun.*|River City Ransom.*|Alien vs\. Predator|The Ninja Warriors|Genpei Touma Den','格斗／清版动作','清版动作与合作'),
        (r'Nintendo World Cup.*|Downtown Nekketsu Koushinkyoku.*|Excitebike|Tony Hawk’s Pro Skater|Super Punch-Out!!','竞速／体育','体育与运动'),
        (r'Lode Runner|Yoshi|Wario’s Woods|The Lost Vikings','益智／休闲','规则解谜与短局'),
        (r'Pilotwings','模拟／音乐／派对','经营与生活模拟'),
        (r'Zombies Ate My Neighbors|KiKi KaiKai','动作射击','跑射与动作射击'),
        (r'Star Wars: Rogue Squadron|Star Wars: Shadows of the Empire','动作射击','第一／第三人称射击'),
        (r'Alien Crush|Devil\'s Crush','模拟／音乐／派对','生活模拟与派对'),
        (r'Super Momotarou Dentetsu','模拟／音乐／派对','生活模拟与派对'),
        (r'Chase HQ|Crazy Taxi(?: 2)?|Metropolis Street Racer|Gran Turismo(?: 2)?','竞速／体育','竞速与驾驶'),
        (r'Osu! Tatakae! Ouendan / Elite Beat Agents|Taiko no Tatsujin Portable','模拟／音乐／派对','音乐与节奏'),
        (r'The Typing of the Dead','模拟／音乐／派对','输入与生活模拟'),
        (r'Scorched Earth|Worms','战略／战棋','炮术与回合对抗'),
    ]
    for pattern,category,subgenre in overrides:
        if re.fullmatch(pattern,s,re.I):return category,subgenre
    if e.platform=='DOS' and s in DOS_GENRES:return DOS_GENRES[s]
    if e.platform=='Win95 / Win98' and s in WINDOWS_GENRES:return WINDOWS_GENRES[s]
    if re.search(r'Tetris|Puyo|Puzzle|Columns|Dr\. Mario|Panel de Pon|Picross|Lemmings|Magical Drop|Gunpey|Qix|ChuChu|Mr\. Driller|Buffers|Mole Mania|Twinkle Star Sprites|Professor Layton|Brain Age|WarioWare|Cooking Mama|Lumines|Katamari',s,re.I):return ('益智／休闲','落块与消除' if re.search(r'Tetris|Puyo|Puzzle Bobble|Columns|Dr\. Mario|Panel|Magical Drop|Lumines',s,re.I) else '规则解谜与短局')
    if re.search(r'Fire Emblem|Tactics Ogre|Ogre Battle|Advance Wars|Romance of the Three Kingdoms|Sangokushi|Nobunaga|Langrisser|Shining Force|Super Robot|Front Mission(?!: Gun Hazard)|Disgaea|Valkyria Chronicles|Panzer|Allied General|Brigandine|Gihren|Military Madness|Civilization|Daisen|Vandal Hearts|Final Fantasy Tactics',s,re.I):return ('战略／战棋','即时军事模拟' if 'Panzer Front' in s else ('网格战术' if re.search(r'Fire Emblem|Tactics|Langrisser|Shining Force|Super Robot|Front Mission|Disgaea|Valkyria|Vandal|Brigandine',s,re.I) else '大战略与军团'))
    if re.search(r'Mario Kart|F-ZERO|Ridge Racer|Gran Turismo|Rally|Out Run|Daytona|Hang-On|Wave Race|Snowboarding|Hydro Thunder|Burnout|Midnight Club|Wipeout|Crash Team Racing|Road Rash|Super Monaco|Rock n\' Roll Racing|Top Gear|Golf|Tennis|NBA|NFL|Captain Tsubasa|Inazuma Eleven|Neo Turf Masters|Winning Eleven|Super Dodge Ball|Street Basket|Windjammers|Fishing',s,re.I):return ('竞速／体育','竞速与驾驶' if re.search(r'Kart|F-ZERO|Racer|Racing|Rally|Out Run|Daytona|Hang-On|Wave Race|Hydro|Wipeout|Monaco|Top Gear|Midnight|Burnout',s,re.I) else '体育与运动')
    if re.search(r'Rhythm|Project DIVA|DJMax|Dance Dance|beatmania|PaRappa|Vib-Ribbon|Space Channel|Samba|Patapon|Band Brothers|Nintendogs|Animal Crossing|Harvest Moon|Rune Factory|SimCity|Theme Hospital|Tokimeki|Memories Off|Clannad|Steins;Gate|Higurashi|Fate/Extra|Mario Party|Game & Watch|Super Monkey Ball',s,re.I):return ('模拟／音乐／派对','音乐与节奏' if re.search(r'Rhythm|DIVA|DJMax|Dance|beatmania|PaRappa|Vib|Channel|Samba|Patapon|Band',s,re.I) else ('经营与生活模拟' if re.search(r'Theme|SimCity|Harvest|Rune|Nintendogs|Animal',s,re.I) else '生活模拟与派对'))
    if re.search(r'Street Fighter|King of Fighters|Samurai Shodown|Last Blade|Fatal Fury|Art of Fighting|World Heroes|Kizuna|Savage Reign|Galaxy Fight|Tekken|Mortal Kombat|Killer Instinct|Darkstalkers|Vampire|JoJo|Marvel|Capcom vs|Guilty Gear|Dead or Alive|Soulcalibur|Power Stone|Virtua Fighter|Pocket Fighter|Battle Spirit|Grand Battle|Yuu Yuu Hakusho|Supersonic Warriors|Ninja Council|Rival Schools|Project Justice|Slam Masters|Smash Bros|Windjammers',s,re.I):return ('格斗／清版动作','一对一与场地格斗')
    if re.search(r'Final Fight|Double Dragon|Streets of Rage|Bare Knuckle|Golden Axe|Cadillacs|Captain Commando|Knights of the Round|Punisher|Battle Circuit|Armored Warriors|Dungeons & Dragons|Three Wonders|King of Dragons|Magic Sword|Sengoku 3|Guardians|Denjin Makai|Night Slashers|Knights of Valour|Oriental Legend|Warriors of Fate|Tenchi wo Kurau II|X-Men \(Arcade\)|Simpsons|Sunset Riders|Violent Storm|Mystic Warriors|Turtles in Time|Teenage Mutant Ninja Turtles II|Burning Fight|Dungeon Explorer|Splatterhouse|Vigilante|Altered Beast',s,re.I):return ('格斗／清版动作','清版动作与合作')
    if re.search(r'Gradius|R-Type|Raiden|Strikers|Gunbird|Truxton|Vimana|Garegga|Darius|Thunder Force|Xevious|Galaga|Galaxian|Space Invaders|Fantasy Zone|After Burner|Space Harrier|Gunhed|Blazing Lazers|Cotton|Magical Chase|Download|Dead Moon|Image Fight|Out Zone|Twin Cobra|Fire Shark|Batsugun|DoDonPachi|ESP Ra\.De|Espgaluda|Progear|Tiger Heli|Sengoku Blade|Sol Divide|Dragon Blaze|Mars Matrix|Giga Wing|Xexex|Parodius|TwinBee|Life Force|Salamander|Gate of Thunder|Lords of Thunder|Spriggan|Sapphire|Aleste|Power Strike|Metal Black|In the Hunt|U\.N\. Squadron|Axelay|Star Fox|Sin and Punishment|Bangai-O|Ikaruga|Rez|Silversword|Space Gun|House of the Dead',s,re.I):
        sub='弹幕射击' if re.search(r'DoDonPachi|ESP Ra\.De|Espgaluda|Progear|Batsugun|Garegga|Mars Matrix|Giga Wing|Ikaruga|Judgement Silversword',s,re.I) else ('固定屏幕与轨道射击' if re.search(r'Galaga|Galaxian|Space Invaders|After Burner|Space Harrier|Star Fox|Sin and Punishment|Rez',s,re.I) else '横纵卷轴射击')
        return ('射击（STG）',sub)
    if re.search(r'Contra|Super C|Metal Slug|Gunstar|Alien Soldier|Midnight Resistance|Heavy Barrel|Jackal|Rush’n Attack|Journey to Silius|Battle City|Metal Gear(?! Solid: Ghost Babel)|GoldenEye|Perfect Dark|Turok|Medal of Honor|Syphon Filter|Resistance|Gundam vs|Cannon Fodder',s,re.I):
        return ('动作射击','第一／第三人称射击' if re.search(r'GoldenEye|Perfect Dark|Turok|Medal of Honor|Syphon Filter|Resistance',s,re.I) else '跑射与动作射击')
    if re.search(r'Final Fantasy|Dragon Quest|Dragon Warrior|Pokémon(?!.*Puzzle)|Golden Sun|Chrono|Mother|EarthBound|Shin Megami|Persona|Suikoden|Grandia|Star Ocean|Tales of|Breath of Fire|Lufia|SaGa|Mana|Terranigma|Soul Blazer|Illusion of Gaia|Bahamut Lagoon|Robotrek|Arcana|E\.V\.O\.|Xenogears|Vagrant Story|Valkyrie Profile|Legend of Dragoon|Lunar|Wild Arms|Popolocrois|Metal Max|Metal Saga|Phantasy Star(?! Online)|Shining Soul|Baldur’s Gate|Kingdom Hearts|Etrian Odyssey|Rune Factory|Riviera|Defenders of Oasis|Blue Sphere|Monster Hunter|Trails in the Sky|Kiseki|Nayuta|Ys |Digimon World|Inazuma Eleven|Dragon Ball: Daimaou|Feng Shen|Destiny of an Emperor|Shokatsu Koumei|Crystalis|Neutopia|Beyond Oasis|Landstalker|Wonder Boy in Monster World|Cosmic Fantasy|Parasite Eve|The 3rd Birthday|Jeanne d’Arc|Crisis Core|Tomato Adventure|Treasure of the Rudra',s,re.I):return ('角色扮演','动作 RPG' if re.search(r'Mana|Seiken Densetsu|Ys |Kingdom Hearts|Monster Hunter|Shining Soul|Baldur|Metal Max|Star Ocean|Tales of|Terranigma|Beyond Oasis|Landstalker',s,re.I) else '回合／迷宫／叙事 RPG')
    if re.search(r'Mario(?!.*Kart)|Donkey Kong|Yoshi|Wario|Kirby|Sonic|Mega Man|Castlevania|Metroid|Ninja Gaiden|Adventure Island|Bonk|Crash|Spyro|Klonoa|Rayman|Ristar|Vectorman|Earthworm Jim|Aladdin|Lion King|Shinobi|Strider|Rocket Knight|Dynamite Headdy|Ristar|Ghouls|Ghosts|Makaimura|Gimmick|Batman|DuckTales|Chip ’n Dale|Joe & Mac|Karnov|Rastan|Legendary Axe|ActRaiser|Prince of Persia|Another World|Shantae|Astro Boy|Ninja Five-O|Gunstar Super Heroes|LocoRoco|Daxter|LittleBigPlanet|Comix Zone|Wonder Boy: The Dragon|Tails Adventure|Shinobi II|Illusion Starring|Illusion|ToeJam|Ecco|Balloon Fight|Ice Climber|Circus Charlie|The Legend of Kage|Ninja JaJaMaru|Saiyuuki World|Goonies|Blaster Master|Bubble Bobble|Rainbow Islands|Snow Bros|Parasol Stars|Mario Bros\.|Pac-Man|Dig Dug|Frogger|Bomberman|Stafy|Starfy',s,re.I):return ('平台动作','探索型动作' if re.search(r'Metroid|Symphony of the Night|Aria of Sorrow|Harmony of Dissonance|Circle of the Moon|Dawn of Sorrow|Portrait of Ruin|Order of Ecclesia|Dragon’s Trap|Shantae|Amazing Mirror',s,re.I) else '横版／单屏／3D 平台')
    return ('动作冒险','生存恐怖与潜行' if re.search(r'Resident Evil|Silent Hill|Dino Crisis|Metal Gear|Clock Tower',s,re.I) else '探索／解谜／文字冒险')

# 系列只按真实 IP 关系，尤其不把 FFT 塞进皇家骑士团。
def series_for(e):
    s=e.en
    if e.platform=='DOS' and s in DOS_SERIES:return DOS_SERIES[s]
    if e.platform=='Win95 / Win98' and s in WINDOWS_SERIES:return WINDOWS_SERIES[s]
    if re.search(r'Seiken Densetsu|Secret of Mana|Trials of Mana|Sword of Mana|Legend of Mana',s,re.I):return '圣剑传说'
    if re.search(r'The Final Fantasy Legend|Final Fantasy Legend II|Final Fantasy Legend III',s,re.I):return '沙加'
    if re.search(r'Mother|EarthBound',s,re.I):return 'MOTHER'
    if re.search(r'Bahamut Lagoon',s,re.I):return '圣龙传说'
    if re.search(r'Dragon Ball',s,re.I):return '龙珠'
    if re.search(r'Kizuna Encounter|Savage Reign',s,re.I):return '风云默示录'
    if re.search(r'Daisenryaku|Panzer General|Allied General',s,re.I):return '大战略与装甲将军'
    if re.search(r'Gihren',s,re.I):return '基连的野望'
    if re.search(r'Brigandine',s,re.I):return '幻想大陆战记'
    if re.search(r'Nakahara no Hasha|Haou no Tairiku',s,re.I):return '三国志与三国题材'
    if re.search(r'Densetsu no Stafy|The Legendary Starfy',s,re.I):return '传说的斯塔菲'
    if re.search(r'Katamari',s,re.I):return '块魂'
    if re.search(r'Lumines',s,re.I):return '音乐方块'
    if re.search(r'Theme Hospital',s,re.I):return 'Theme 经营模拟'
    if re.search(r'Final Fantasy|Crisis Core|Dissidia',s,re.I):return '最终幻想'
    if re.search(r'Tactics Ogre|Ogre Battle',s,re.I):return '皇家骑士团'
    for name,pat in rg.series_rules:
        if name in {'最终幻想','皇家骑士团','光明力量'}:continue
        if re.search(pat,s,re.I):return name
    extra=[('泡泡龙与彩虹岛',r'Bubble Bobble|Rainbow Islands|Parasol Stars'),('炸弹人',r'Bomberman'),('风之少年',r'Klonoa'),('魔界村',r'Ghouls|Ghosts|Makaimura'),('钻地先生',r'Mr\. Driller'),('俄罗斯方块',r'Tetris'),('噗哟噗哟',r'Puyo Puyo'),('神奇男孩',r'Wonder Boy'),('米奇妙境',r'Illusion'),(' Aleste',r'Aleste|Power Strike'),('樱花大战',r'Sakura Wars'),('大盗五右卫门',r'Goemon|Mystical Ninja'),('忍者神龟',r'Teenage Mutant Ninja'),('热血系列',r'Nekketsu|River City|Super Dodge Ball|Nintendo World Cup'),('梦幻战士',r'Valis'),('雷曼',r'Rayman')]
    for name,pat in extra:
        if re.search(pat,s,re.I):return name.strip()
    return ''
custom_notes={id(e):e.note for e in entries if e.note}
for e in entries:
    e.series=series_for(e)
    e.category,e.subgenre=genre(e)
    e.note=custom_notes.get(id(e)) or rg.make_note(e).replace('|','／').replace('\n',' ')
    if e.platform=='Win95 / Win98':
        level,runtime_note=WINDOWS_RUNTIME[e.en]
        e.note+=f' 【Wine 安装判断：{level}】{runtime_note}'
    if id(e) not in custom_notes and (e.old in old_names or e.en in Y or e.platform in {'GG','WS / WSC'}):
        if e.note.startswith('本作保留了该平台') or e.note==rg.series_note.get(e.series,''):e.note=''

# 为通用系列注追加作品定位，避免只有系列背景没有本作信息。
def detail(e):
    s=e.en
    if re.search(r'The King of Fighters (\d+)',s):
        y=re.search(r'(\d+)',s).group(1)
        specific={'94':'系列首作确立三人组队与跨国队伍编排，以 Rugal 为最终对手。','95':'引入自由组队与八神庵，草薙京与八神的对抗开始成为长期主线。','96':'重做移动、紧急回避与跳跃系统，神乐千鹤和高尼茨推动大蛇篇。','97':'大蛇篇收束，指令速度和简易操作使它在街机厅传播极广。','98':'无剧情的梦幻对战合集，平衡与角色阵容成熟，是长期比赛常用版本。','99':'开启 NESTS 篇并加入援护系统，K′ 取代旧主角位置。','2000':'延续 NESTS 篇与援护机制，库拉等角色加入，队伍构筑更依赖援护选择。','2001':'可在出战与援护间分配四人名额，队伍编成自由但平衡评价分化。','2002':'回归无剧情三人梦幻战与 ABC 连招系统，角色多、对战节奏直接。','2003':'采用可换人三对三与多路线 Boss，开启 Ash 篇，也是 Atomiswave 之前最后一部编号作。'}
        return specific.get(y,'三人组队对战，角色阵容与系统围绕该届规则展开。')
    if re.search(r'Samurai Shodown',s):
        if ' II' in s:return '加入武器破坏技与更完整角色阵容，以重击威慑、弹刀和距离控制成为系列最流行的一作。'
        if 'III' in s:return '分为修罗与罗刹两种战斗风格，整体色调和人物路线更阴沉，系统也明显转向连段。'
        if 'IV' in s:return '加入连斩与自裁等机制，天草四郎时贞再次成为核心，节奏和演出区别于 II。'
        if ' V' in s:return '加入剑气槽与一撃必杀相关机制，阵容加入新角色，在旧 2D 体系中调整攻防资源。'
        return '系列首作以刀剑重击、武器脱手和道具投掷区别于拳脚格斗，节奏更强调读招。'
    m=re.search(r'Mega Man (\d+)$',s)
    if m:return f'元祖第 {m.group(1)} 作延续 Boss 武器克制与选关，关卡机关、蓄力和辅助能力随代际逐步调整；可与同平台其他编号作比较关卡节奏。'
    if re.search(r'Final Fantasy Tactics Advance',s):return '以伊瓦利斯学校社团为切口，法则牌会限制战斗中的行动，职业任务和地域占领构成养成。作为最终幻想战略版的掌机分支，它把网格战斗、职业培养与较轻盈的校园异世界叙事结合起来。'
    if re.search(r'Final Fantasy Tactics: The War of the Lions',s):return 'PSP 版重制 FFT，加入动画过场、新职业与角色，并调整多人内容；政治群像和网格职业战仍是核心，载入与战斗速度需注意。'
    if re.search(r'Final Fantasy Tactics$',s):return rg.notes_exact['Final Fantasy Tactics']
    if re.search(r'Final Fantasy I / II / IV',s):return 'WSC／WS 重制早期最终幻想，改良画面、界面与部分平衡；三作是独立商品，I／II 偏系列源头，IV 则有完整 ATB 群像剧。'
    if re.search(r'Pokémon (Red|Gold|Ruby|FireRed|HeartGold|Black|Platinum)',s):return rg.notes_exact.get(s,e.note)
    return ''
from guide_notes import N2
from guide_deep_notes import DEEP
version_notes={
('Win95 / Win98','Rayman 2: The Great Escape'):'Rayman 为解救世界收集能量、恢复伙伴并对抗机械海盗，3D 关卡把跳跃、攀爬、飞行与轻解谜结合。PC 版与 Dreamcast／N64／PS1 版本在关卡和画面上有差异；保持原始低画质和手柄输入，不把其他平台备注套用到 Windows 版。',
('NES / FC','Dragon Quest IV: Chapters of the Chosen'):'各章先讲述不同伙伴的命运，最后汇入勇者一行，章节结构让群像塑造格外鲜明。此条是 FC 原版，受硬件限制的界面与遇敌节奏不同于 NDS 重制，不存在对应的 GBA 移植。',
('NES / FC','Tetris'):'旋转四格方块、堆叠并消除整行，速度提升后空间规划越来越紧张。此条是 FC 版本，应与任天堂 GB 捆绑版分开识别；它不以联机或便携传播史为卖点，核心价值仍是这套极简规则。',
('GB','The Legend of Zelda: Link’s Awakening'):'林克在谜样岛屿收集乐器、穿越迷宫，离岛设定与结局带有淡淡忧伤。此条是 GB 单色原版；DX 的色彩和隐藏迷宫留在 GBC 条目，不把两版混成一个镜像。',
('SNES / SFC','Langrisser'):'《Der Langrisser》以 SFC 重制 MD 初代，保留指挥官、兵种克制与转职，并扩展多阵营路线和角色演出。它不是《Langrisser II》，也不应沿用只介绍 MD 初代的备注。',
('PS1','Resident Evil 2'):'里昂与克莱尔的双路线从警局扩展到地下设施，资源管理、固定镜头和解谜延续初代。PS1 原版以双光盘呈现两条起始路线，是后续 N64 高压缩移植与各类重制之前的基准版本。',
('GBC','Mario Tennis'):'除即时网球外还有 RPG 式校园成长、训练和赛事，属性培养会直接影响击球能力。GBC 版可与 N64 版联动，但自身拥有完整成长模式，不是家用版的简单缩小移植。',
('PSP','Grand Theft Auto: Chinatown Wars'):'以俯视角呈现自由城帮派任务、驾驶和毒品交易经济，保留系列开放城市结构。PSP 版没有 NDS 的触屏交互，改用普通按键并调整画面表现，不能沿用 NDS 的操作说明。',
('FBNeo','Street Fighter Alpha 2'):'以 Alpha Counter、Custom Combo 和更鲜明角色阵容发展少年街霸，街机原版在动画、输入与对战节奏上是版本基准。SFC 移植的载入和画面妥协不写入本条。',
('PS1','Tokimeki Memorial 1 / 2'):'初代以学习、社团、约会和角色评价建立恋爱模拟循环，二代扩大人物关系、事件与毕业前经营。这里按两部独立 PS1 商品收藏，不把 PCE 初代或单作备注当成整个合集的内容。',
}
for e in entries:
    if e.en in N2:e.note=N2[e.en]
    d=detail(e)
    if d:e.note=d
    if e.en in DEEP:e.note=DEEP[e.en]
    if (e.platform,e.en) in version_notes:e.note=version_notes[(e.platform,e.en)]
    if e.platform=='SNES / SFC' and e.en=='Langrisser':e.en='Der Langrisser';e.year='1995'
    if not e.note:
        base=rg.series_note.get(e.series,'')
        e.note=(base+' ' if base else '')+f'本作《{e.zh}》在{e.subgenre}中有独立的关卡、角色或系统配置；表列的是 {e.platform} 正式版本，应与其他平台同名移植或重制分开识别。'
    e.note=e.note.strip()

# 稳定 ID 在所有删改后重新分配；只有两款以上真实成员才设系列专题。
platforms=['DOS','Win95 / Win98','MAME','FBNeo','NES / FC','PCE (PC Engine / TurboGrafx-16)','MD / Genesis','GB','GG','SNES / SFC','N64','PS1','GBC','Dreamcast','WS / WSC','GBA','NDS','PSP']
short={'MAME':'MAME','FBNeo':'FBNEO','GBA':'GBA','GBC':'GBC','GB':'GB','GG':'GG','WS / WSC':'WS','NES / FC':'NES','SNES / SFC':'SNES','MD / Genesis':'MD','PCE (PC Engine / TurboGrafx-16)':'PCE','PS1':'PS1','N64':'N64','PSP':'PSP','Dreamcast':'DC','NDS':'NDS','DOS':'DOS','Win95 / Win98':'WIN9X'}
for p in platforms:
    for i,e in enumerate([x for x in entries if x.platform==p],1):e.eid=f'{short[p]}-{i:03d}'
series_counts={s:sum(e.series==s for e in entries) for s in {e.series for e in entries if e.series}}
series_order=[]
for e in entries:
    if e.series and series_counts[e.series]>=2 and e.series not in series_order:series_order.append(e.series)
series_id={s:f'series-{i:02d}' for i,s in enumerate(series_order,1)}
# 系列子组。
for e in entries:
    if e.series=='最终幻想':e.subgroup='战略版' if 'Tactics' in e.en else ('VII 衍生' if 'Crisis Core' in e.en else '正传与重制')
    elif e.series=='马力欧':
        e.subgroup='卡丁车' if 'Kart' in e.en else ('派对' if 'Party' in e.en else ('体育' if re.search(r'Golf|Tennis',e.en) else ('瓦力欧' if 'Wario' in e.en else ('咚奇刚' if 'Donkey Kong' in e.en else ('耀西' if 'Yoshi' in e.en else ('角色扮演' if re.search(r'Paper Mario|Mario & Luigi|Super Mario RPG',e.en) else '平台动作'))))))
    elif e.series=='宝可梦':e.subgroup='不可思议迷宫' if 'Mystery Dungeon' in e.en else ('护林员' if 'Ranger' in e.en else ('家用机与益智衍生' if re.search(r'Stadium|Snap|Puzzle|Trading Card|Hey You',e.en) else '正统角色扮演'))
    elif e.series=='三国志与三国题材':e.subgroup='英杰传与曹操传' if re.search(r'Eiketsuden|Sousouden|英傑傳|孔明傳|曹操伝|曹操傳',e.en) else ('Namco《三国志》' if re.search(r'Nakahara no Hasha|Haou no Tairiku|^Sangokushi$',e.en) else ('光荣《三国志》' if re.search(r'Romance|Sangokushi',e.en) else ('吞食天地' if re.search(r'Tenchi wo Kurau|Destiny of an Emperor',e.en) else ('三国战纪' if 'Knights of Valour' in e.en else '其他三国题材'))))
    elif e.series=='洛克人':e.subgroup='EXE／网络对战' if 'Battle Network' in e.en else ('Zero' if 'Zero' in e.en else ('ZX 与流星' if re.search(r'ZX|Star Force',e.en) else ('X' if 'Mega Man X' in e.en else '元祖与世界')))
    elif e.series=='光明与梦幻模拟战':e.subgroup='梦幻模拟战' if 'Langrisser' in e.en else '光明系列'
    elif e.series=='女神转生与女神异闻录':e.subgroup='Persona' if 'Persona' in e.en else '真·女神转生'
    else:e.subgroup='主系列'

platform_intro={
'MAME':'早期 Namco、Taito、Nintendo、Sega 等 2D 街机。与 FBNeo 分目录管理，ROM set 必须匹配 Batocera 当前核心；这里不列后期 PC 基板与光枪依赖作品。',
'FBNeo':'CPS、Neo Geo、PGM、Toaplan 等成熟 2D 街机内容，重点是合作、对战、射击与休闲短局。NAOMI 不混放这里，Model 2／3 和后期音游也不为凑数收录。',
'GBA':'32 位掌机的动作、RPG、战棋与原创短局作品；Advance 复刻与原创续篇分开写，未把民间改版或不存在的主机移植混入。',
'GBC':'彩色专用或以彩色体验为主的作品，包含 GBC 原创、双版本联动和掌机衍生；黑白 GB 原作留在下一章。',
'GB':'黑白 Game Boy 正式作品，兼顾早期便携史、经典休闲和可反复游玩的动作／RPG。',
'GG':'Sega Game Gear 精选，优先原创掌机篇章、Compile 射击和经典休闲，不用普通移植作填满平台。',
'WS / WSC':'WonderSwan 与 WonderSwan Color 合并展示，备注注明彩色版或日文门槛；以 Gunpey、风之少年与原创射击等真正体现平台价值的作品为主。',
'NES / FC':'8 位家用机与 Famicom 正式作品，中文俗称只作辅助识别，商品原名和实际发行主体为准。',
'SNES / SFC':'16 位任天堂平台，覆盖平台动作、JRPG、战棋、射击和合作游戏；特殊芯片作品按核心兼容情况逐一测试。',
'MD / Genesis':'Mega Drive 与 Genesis 是同一硬件的地区名。保留《Raiden Trad》《R-Type》等正式移植，也突出 Sonic、Treasure 和战棋传统。',
'PCE (PC Engine / TurboGrafx-16)':'HuCard、CD‑ROM²／Super CD 与 Arcade Card 作品并列；光盘容量按预留空间估算，收藏时还需对应系统卡。',
'PS1':'以原生分辨率运行，兼顾类型史、家庭对战与中文圈经典；多盘游戏需维护 M3U，重型画面增强不纳入默认建议。',
'N64':'保留第一方、Rare、本地多人和类型代表，不承诺高负载游戏在 N4100 上全场景稳定；Expansion Pak 与图形插件需逐作核对。',
'PSP':'删除对 N4100 负担过高的重型 3D 动作与开放世界，以 2D、静态场景 RPG、战棋和原创休闲为主；仍按实机场景验证。',
'Dreamcast':'以 Flycast 原生分辨率、较成熟 2D 移植与 DC 特色游戏为主；重型 3D 只保留高代表作，不把“可启动”写成“全程稳定”。',
'NDS':'以双屏、触控、RPG、文字冒险和本地家庭短局为主，注意触控与麦克风在游戏中的必要性。',
'DOS':'IBM PC 兼容环境的 DOS 精品，并保留《文明 II》这类可在 DOSBox‑X＋Windows 3.x 运行的轻量作品。中文战棋、国产三剑、经营、点击冒险与即时战略均有覆盖；射击作优先采用主机／街机版本，Win95／98 专用作品转由下一平台的 Wine 管理。鼠标、键盘和手柄映射逐作写明。',
'Win95 / Win98':'Windows 95／98 时代的低配置精品经 Batocera 官方 windows 系统与内置 Wine runner 运行，并不虚拟完整 Win95。以中文 RPG、战棋、欧美角色扮演、策略经营和点击冒险为主，辅以轻量平台动作与竞速；不收第一／第三人称射击、FPS 或 STG。每作独立 Wine prefix，DirectDraw 优先试 cnc-ddraw，早期 3D 保持原始低画质，默认不开 DXVK。备注中的“优先安装／固定版本后安装／低画质专项验收”是公开资料形成的安装优先级，不是本机实测认证：N4100 的四核低功耗 CPU、12 EU 的 UHD 600 与 4 GB 共享内存决定了老游戏的主要风险是兼容、早期 3D、视频和字库，而非仅看当年最低配置。'}

# 输出。
out=['# Batocera 家庭游戏机精选指南','',
'> 适用配置：Intel Celeron N4100＋UHD 600＋4 GB 内存＋Batocera。定位是电视上的家庭游戏机，因此本地合作、双人对战、经典休闲与大作同样占位置。','',
'本清单只覆盖 **DOS、Win95／98、MAME、FBNeo、NES／FC、PCE、MD、GB、GG、SNES／SFC、N64、PS1、GBC、Dreamcast、WS／WSC、GBA、NDS、PSP**。筛选依据是平台支持、保守性能范围、作品质量与家庭游玩价值，并非逐款实机测试承诺；合集行是收藏组，不等于一个 ROM。','',
'## 总目录','',
'- [使用规则与硬件边界](#使用规则与硬件边界)','- [平台、硬件、模拟器与容量汇总](#平台硬件模拟器与容量汇总)','- [存储、目录与镜像管理](#存储目录与镜像管理)','- [各平台精选清单](#各平台精选清单)']
for p in platforms:out.append(f'  - [{p}](#platform-{short[p].lower()})')
out+=['- [游戏方式专题：品类源流与代表作](#游戏方式专题品类源流与代表作)','- [游戏内容专题：系列与平台回链](#游戏内容专题系列与平台回链)','- [中文化版本与精选非官方改版](#中文化版本与精选非官方改版)','- [三层查漏补缺结果](#三层查漏补缺结果)','- [摄像头与麦克风验证附录](#摄像头与麦克风验证附录)','',
'---','','## 使用规则与硬件边界','',
'1. **名字分两列。** 完整商品名采用英文、日文或中文原文，中文译名只辅助识别；同一游戏的地区版、复刻和重制不互相冒充。','2. **日期采用首发年份或合集年份范围。** 合集行明确标注范围，避免把不同作品伪装成一个日期；发行商采用该版本的主要历史发行主体，不用今天的公司名倒填。','3. **容量是预留预算，不是实测 ROM 大小。** CHD、CSO、音轨、多盘与地区版都会改变占用，安装后以实际文件为准。','4. **不保留差作凑数。** 只有系列史或版本比较确有必要的旧作才作为严格例外，并在备注说明；外设依赖、后期高负载街机和低评价移植不占位置。','5. **不纳入 Xbox、PS2、PS3、PS4、GameCube、Wii。** Batocera 虽提供 xemu 的 Xbox 入口，但 N4100＋UHD 600＋4 GB 不适合作为稳定可玩的 Xbox 库，因此这里明确不设 Xbox 章节。','6. **合法备份。** 只使用自己合法拥有的游戏与 BIOS，不提供下载，不把 hack、民间改版或虚构商品当正式发行作。','',
'---','']
from guide_sections import platform_overview, mod_sections, stg_history, hardware_input_appendix
out += platform_overview()
out += ['## 存储、目录与镜像管理','',
'### 存储分工','',
'| 位置 | 内容 | 原则 |','|---|---|---|','| eMMC 独立 ext4 分区 | DOS／Win3.x、MAME、FBNeo、NES、PCE HuCard、MD、GB、GG、SNES、N64、GBC、WS／WSC、GBA 游戏 | 小体积顺序读取，目录级软链接，不做 mergerfs |','| SSD `/userdata` | Win95／98、PS1、Dreamcast、NDS、PSP，以及全部存档、配置、缓存与刮削 | Windows 游戏、Wine prefix、大镜像和写入集中，避免挤占 eMMC |','',
'```bash','mkdir -p /mnt/emmc/roms/{dos,mame,fbneo,nes,pcengine,megadrive,gb,gg,snes,n64,gbc,wswan,wswanc,gba}','# 先确认目标路径不存在；不要覆盖已有实体目录','ln -s /mnt/emmc/roms/dos /userdata/roms/dos','ln -s /mnt/emmc/roms/mame /userdata/roms/mame','ln -s /mnt/emmc/roms/fbneo /userdata/roms/fbneo','ln -s /mnt/emmc/roms/nes /userdata/roms/nes','ln -s /mnt/emmc/roms/pcengine /userdata/roms/pcengine','ln -s /mnt/emmc/roms/megadrive /userdata/roms/megadrive','ln -s /mnt/emmc/roms/gb /userdata/roms/gb','ln -s /mnt/emmc/roms/gg /userdata/roms/gg','ln -s /mnt/emmc/roms/snes /userdata/roms/snes','ln -s /mnt/emmc/roms/n64 /userdata/roms/n64','ln -s /mnt/emmc/roms/gbc /userdata/roms/gbc','ln -s /mnt/emmc/roms/wswan /userdata/roms/wswan','ln -s /mnt/emmc/roms/wswanc /userdata/roms/wswanc','ln -s /mnt/emmc/roms/gba /userdata/roms/gba','```','',
'先用 `blkid`、`lsblk` 核对实际设备并手工验证挂载，不要照抄设备名。PCE CD 镜像虽属 PCE 平台，也放在 SSD；存档和配置始终留在 `/userdata`。','',
'- **DOS／Win3.x 每作独立目录。** 实体文件放 eMMC `/mnt/emmc/roms/dos/<游戏名>.pc/`，经 `/userdata/roms/dos` 软链接访问；保留各自程序、音轨与启动配置，存档和模拟器配置仍由系统写入 `/userdata`。DOS 原版先用 DOSBox Pure，启动菜单或 Pad2Key 不顺时再试独立 DOSBox。DOS 游戏一般不需 BIOS。轻量 Win3.x 游戏则使用自己合法拥有的 Windows 3.x 和 Batocera 官方支持的 DOSBox‑X，共用已配置的环境，逐作核对 WinG、CD 与声音；Win95／98 游戏不走此路线。',
'- **Win95／98 使用 Batocera 的 windows 系统。** 已安装游戏放 SSD `/userdata/roms/windows/`，安装介质放 `/userdata/roms/windows_installers/`；支持 `.pc`、`.exe`、`.wine`、`.wsquashfs`、`.wtgz`，无需 BIOS，也不需安装完整 Windows。每作独立 `.wine` prefix，`autorun.cmd` 用 LF 换行并明确 `DIR`、`CMD`，再用 `SAVEDIR`／`SAVEFILES` 把存档映射到 `/userdata/saves/windows/<游戏>/`。老安装器不能在 Wine 中完成时，先在另一台兼容机器安装，再复制完整安装目录。`/userdata` 用 ext4 或 btrfs，不把 Wine 库放在 FAT、NTFS 或 NAS。',
'- **Runner 以本机 Batocera 版本为准。** Batocera 41 起已由停止维护的旧 Wine-GE 8-26 转向 Wine-TKG，后续版本仍会继续更新，因此不把某个 runner 名称写成永久前提。先查系统信息与 `/usr/wine/` 下实际安装版本；确有单作版本需求时，把兼容 runner 放到 `/userdata/system/wine/custom/` 的独立目录并为该作单独选择。4 GB 内存同时供 Batocera、Wine 与共享显存使用，不并行安装多个大型组件，也不把他人的高配测试当本机性能证明。',
'- **DirectDraw 优先使用 cnc-ddraw。** 将官方发布包中的 `ddraw.dll`、配置程序与所需文件放到游戏 EXE 同目录，游戏自身先设全屏并关闭自带窗口模式；在 Wine 中运行一次 `cnc-ddraw config.exe`，或把 `ddraw` 覆盖为 `native,builtin`。`autorun.cmd` 也可针对该作写 `ENV=WINEDLLOVERRIDES=ddraw=n,b`。N4100 先用 OpenGL 渲染，异常时试 GDI；速度过快再调 `maxgameticks=60`，不要默认开高成本缩放 shader。**它只处理 DirectDraw／软件渲染，不支持 Direct3D 或 Glide**，这三类不能靠替换 `ddraw.dll` 通用修复。DDrawCompat 官方不支持 Wine，不作为 Batocera 方案；cnc-ddraw、GOG 自带渲染器和其他 wrapper 不叠加。',
'- **Wine 配置按游戏隔离。** DirectDraw 和早期 Direct3D 默认关闭 DXVK，以 WineD3D／OpenGL 与原始低分辨率起步；只有确有收益的较新 DirectX 游戏才单独试 DXVK。老中文游戏按实际编码补字体并设置 `LANG`，日区旧作还需检查 `LC_ALL` 与 Shift-JIS 文件名，不把整套字库覆盖到所有 prefix。Batocera 的高级选项通常只在首次启动生效；修改后先备份存档，再重建该作的可写层或 prefix。小型且写入多的游戏可用 `.wtgz`，大型且主要只写存档的游戏可用 `.wsquashfs`。《文明 III》的黑色地形问题在 Wine 10.13 上游有修复记录，但不代表外交界面、声音和后续兼容层回归都已解决，须保留该作的专项验收。',
'- **街机按 ROM set 管理。** MAME 放 `/userdata/roms/mame`，FBNeo 放 `/userdata/roms/fbneo`；ZIP 不随意改名或解压，Neo Geo、PGM 等依赖文件随匹配 ROM set 配置。','- **BIOS 以本机检查为准。** 用 Batocera 的 BIOS 检查、`batocera-systems` 和当前版本文档确认，不用旧网络清单替代。','- **光盘与便携镜像。** PCE CD、PS1 可用 CHD，多盘配 M3U；Dreamcast 按核心选 CHD 或 GDI，转换前保留原镜像。PSP 以 ISO 作兼容基线，CSO 是否合适按游戏测试。','- **家庭游玩先测操作。** 核对多手柄分配、存档、双人画面与热键；触控、陀螺仪、阳光传感器和专用外设作品会在备注中说明。DOS／Windows 经营、RTS 与点击冒险优先实体鼠标，Pad2Key 只是可用性补偿。','',
'官方依据：[Batocera Arcade Guide](https://wiki.batocera.org/arcade)、[Advanced arcade emulation](https://wiki.batocera.org/advanced_arcade)、[Add games/BIOS files](https://wiki.batocera.org/add_games_bios)、[Batocera DOS 系统说明](https://wiki.batocera.org/systems:dos)、[DOSBox‑X 的 Windows 3.1x 指南](https://dosbox-x.com/wiki/Guide%3AInstalling-Windows-3.1x)、[Batocera Windows（Wine）系统说明](https://wiki.batocera.org/systems:windows)、[Batocera Changelog](https://batocera.org/changelog)、[cnc-ddraw 官方说明](https://github.com/FunkyFr3sh/cnc-ddraw)、[DDrawCompat 官方说明](https://github.com/narzoul/DDrawCompat)、[《文明 III》Wine／Proton 问题记录](https://github.com/ValveSoftware/Proton/issues/315)、[Dungeon Keeper II 技术资料](https://www.pcgamingwiki.com/wiki/Dungeon_Keeper_2)、[Need for Speed III 技术资料](https://www.pcgamingwiki.com/wiki/Need_for_Speed_III:_Hot_Pursuit)、[The Sims 技术资料](https://www.pcgamingwiki.com/wiki/The_Sims)、[Intel N4100 官方规格](https://www.intel.com/content/www/us/en/products/sku/128983/intel-celeron-processor-n4100-4m-cache-up-to-2-40-ghz/specifications.html)、[Xbox 系统说明](https://wiki.batocera.org/systems:xbox)。','',
'---','','## 各平台精选清单','']
for p in platforms:
    es=[e for e in entries if e.platform==p]
    out += [f'### {p}','',f'<a id="platform-{short[p].lower()}"></a>','',platform_intro[p],'',
    '| 条目 | 完整商品名（英文／日文／原文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |','|---|---|---|---:|---|---:|---|---|']
    for e in es:
        note=e.note
        if e.series in series_id:
            note+=f' [系列专题](#{series_id[e.series]})。'
        elif e.series:
            background=rg.series_note.get(e.series,'').strip()
            if background and background not in note:
                note+=f' 系列背景：{background}'
        out.append(f'| <a id="{e.eid.lower()}"></a>{e.eid} | {e.en.replace("|","／")} | {e.zh.replace("|","／")} | {e.year} | {e.pub} | {e.size} | {e.category}／{e.subgenre} | {note.strip()} |')
    out+=['','---','']

# 十大品类，包含历史、细分与真实条目链接；STG 与动作射击并列。
genre_defs=[
('平台动作','从街机单屏《Donkey Kong》、FC 卷轴《Super Mario Bros.》到 16 位高速动作与 3D 收集，核心始终是移动手感、空间判断和关卡节奏。PC 的《Claw》《Jazz Jackrabbit 2》与主机传统并行，随后共同进入 3D 收集时代。细分包括单屏动作、横版卷轴、跑跳解谜、3D 平台，以及靠能力回环打开地图的“银河城”。',['Super Mario Bros.','Sonic the Hedgehog 2','Super Metroid','Castlevania: Symphony of the Night','Shantae','Klonoa: Door to Phantomile','Captain Claw','Jazz Jackrabbit 2','Rayman 2: The Great Escape']),
('动作冒险','这一大类把动作操作放进探索、解谜或叙事空间。塞尔达的迷宫道具、生存恐怖的资源压力、点击冒险的物品逻辑、视觉小说的调查指证都属于不同分支；它们共享“如何理解并穿过这个空间”，但不共享同一种战斗。DOS／Windows 的 SCUMM 与手绘点击冒险是其中不可缺的一支。',['The Legend of Zelda: A Link to the Past','Metal Gear Solid','Resident Evil','Ghost Trick: Phantom Detective','The Secret of Monkey Island','The Curse of Monkey Island','Grim Fandango','Broken Sword: The Shadow of the Templars']),
('射击（STG）','STG 是 Shoot ’em up 的常用缩写，中文通常称“射击游戏”；弹幕射击只是其中后来形成的细分，并不涵盖全部 STG。本章从《Space Invaders》《Galaxian》的固定屏幕，经《Gradius》《沙罗曼蛇》的横纵卷轴，到 Cave 的高密度弹幕梳理源流；《魂斗罗》这类以人物跑跳和射击并重的作品另列“动作射击”。',['Space Invaders','Galaxian','Life Force / Salamander','Gradius','R-Type','Ikaruga']),
('动作射击','这一品类以角色直接移动、跑跳、载具或第一／第三人称视角为主，射击服务于动作空间，而不是单纯沿卷轴闪避敌弹。FC《魂斗罗》《Super C》是跑射代表，《GoldenEye 007》等则属于第一人称路线；它们与 STG 并列，避免把所有带枪的游戏混为一类。',['Contra','Super C','Metal Slug 1 / 2 / X / 3 / 4 / 5','Gunstar Heroes','GoldenEye 007']),
('格斗／清版动作','清版动作由《双截龙》《快打旋风》把街头推进、投技与多人合作定型；一对一格斗则由《Street Fighter II》确立帧数、距离和角色博弈。3D 场地格斗与派对乱斗进一步扩大分支，但本地对战始终是核心。',['Street Fighter II: The World Warrior','The King of Fighters 98','Streets of Rage 2 / Bare Knuckle II','Cadillacs and Dinosaurs','Soulcalibur','Power Stone 2']),
('角色扮演','家用 JRPG 从《Dragon Quest》《Final Fantasy》的清晰回合制出发，逐渐分化出 ATB、职业构筑、动作战斗与怪物养成；PC 的《Ultima》《Fallout》《Baldur’s Gate》则突出世界模拟、选择后果和小队构筑，中文 DOS／Windows 又形成仙侠武侠与历史叙事传统。此处把战棋单列；塞尔达等没有数值成长主轴的作品归动作冒险。',['Dragon Quest III: The Seeds of Salvation','Final Fantasy VI','Chrono Trigger','Pokémon Emerald','Fallout','Planescape: Torment',"Baldur's Gate II: Shadows of Amn",'Diablo II','軒轅劍參外傳：天之痕']),
('战略／战棋','光荣历史模拟把内政、外交与战争连成宏观循环；火焰之纹章、皇家骑士团和曹操传聚焦网格、单位与角色成长。PC 还发展出文明式 4X、英雄无敌的探索＋六角格战斗，以及 C&C、帝国时代式即时战略；不同节奏共享资源与决策，却不应混成同一种“战棋”。',['Fire Emblem: Genealogy of the Holy War','Tactics Ogre: Let Us Cling Together','Advance Wars','三國志曹操伝 / Sangokushi Sousouden','Sangokushi VII / 三國志VII','Heroes of Might and Magic III: The Restoration of Erathia','Age of Empires II: The Age of Kings',"Sid Meier's Civilization III",'Jagged Alliance 2']),
('竞速／体育','竞速从街机计时、伪 3D 路带发展到卡丁车道具、拟真调校与高速反重力；体育则在规则还原和电视节奏之间取舍。PC《Need for Speed III》把警匪追逐变成核心，足球 RPG、马力欧体育和滑板目标模式进一步说明这一大类不只模拟真实赛事。',['Super Mario Kart','R4: Ridge Racer Type 4','F-ZERO X','Tony Hawk’s Pro Skater 2','Captain Tsubasa','Neo Turf Masters','Need for Speed III: Hot Pursuit']),
('益智／休闲','俄罗斯方块、泡泡龙解谜、噗哟噗哟与宝石方块证明经典休闲并非附属：短规则能产生长期精通，本地对战又能直接服务家庭场景。PC《Lemmings》以鼠标分配技能，扩展了路线规划与逻辑解谜。细分包括落块消除、物理解谜、路线规划、绘图逻辑与短局动作益智。',['Tetris','Puzzle Bobble / Puzzle Bobble 2 / 3 / 4','Puyo Puyo Tsu','Columns','Gunpey','Lemmings']),
('模拟／音乐／派对','生活模拟重视日程与关系，经营模拟重视资源循环，音乐游戏把输入映射到节拍，派对和微游戏则降低旁观与轮换门槛。PC 从《SimCity》《Theme Hospital》到《The Sims》《大富翁》形成完整经营与家庭轮玩传统；专用控制器会改变体验，因此本指南优先保留普通手柄或鼠标仍能成立的作品。',['Harvest Moon','Animal Crossing: Wild World','Rhythm Heaven / Rhythm Tengoku Gold','Mario Party 1 / 2 / 3','SimCity 2000','Theme Hospital','The Sims','大富翁 4','明星志願 2'])]
out+=['## 游戏方式专题：品类源流与代表作','','本章按每个条目的主要玩法归类，细分方向写在平台表的“品类”列。DOS／Windows 与主机作品采用同一分类；代表系列链接回游戏内容专题，代表条目链接回平台，跨类型作品只设一个主品类，避免重复计数。','']
for gi,(g,history,reps) in enumerate(genre_defs,1):
    out += [f'### {g}','',history,'']
    if g=='射击（STG）':out += stg_history(entries)+['']
    linked=[]
    for title in reps:
        e=next((x for x in entries if x.en==title),None)
        if e:linked.append(f'[{e.zh}](#{e.eid.lower()})')
    sers=[]
    for e in entries:
        if e.category==g and e.series and e.series not in sers:sers.append(e.series)
    slinks=[f'[{s}](#{series_id[s]})' for s in sers[:8] if s in series_id]
    out+=['代表作：'+'、'.join(linked)+'。','相关系列：'+'、'.join(slinks)+'。','']
    subs=[]
    for e in entries:
        if e.category==g and e.subgenre not in subs:subs.append(e.subgenre)
    out+=['本库细分：'+'、'.join(subs)+'。','']
out+=['---','']

# 系列专题：只呈现至少两个真实成员，全部回链。
series_intro={'最终幻想':'正传、重制与战略版分组。FFT／FFTA 属于本专题“战略版”，与皇家骑士团没有系列隶属关系。','皇家骑士团':'只收 Ogre Battle／Tactics Ogre 体系，军团制与网格战棋分开理解，不混入 FFT。','圣剑传说':'Square 的 2D 黄金期脉络在这里按系列保留：GB《最终幻想外传》建立即时战斗与成长，SFC《圣剑传说 2》加入多人与环形菜单，《圣剑传说 3》扩展多主角和转职，PS1《玛娜传奇》转向地图放置与世界构筑；GBA《新约》则重新诠释 GB 初代。它虽从最终幻想外传起步，却不属于最终幻想正传。','沙加':'Square 的 2D 黄金期在沙加系列中体现为持续系统实验：GB 三部曲以种族、耐久和非常规成长起步，SFC《浪漫沙加》发展自由剧本、闪悟与世代传承，PS1《开拓者》两作分别探索多主角自由剧情和世代连携。GB 海外旧名含 Final Fantasy，但不属于最终幻想正传；NDS《沙加 2》重制另按平台识别。','马力欧':'按平台动作、卡丁车、派对、体育、RPG、瓦力欧、咚奇刚与耀西拆分。','宝可梦':'按正统 RPG、不可思议迷宫、护林员及家用机衍生拆分；Metal Max／重装机兵不属于本专题。','三国志与三国题材':'按发行体系与玩法拆分为 Namco《中原之霸者／霸王的大陆》、光荣《三国志》、英杰传／曹操传、Capcom《吞食天地》与 IGS《三国战纪》，避免同题材混成同系列。DOS《英杰传》《孔明传》与 Windows《曹操传》《三国志 VII／VIII》直接并列到 PC 条目，和 FC、主机、街机版本互相回链。','英雄无敌':'DOS《Heroes of Might and Magic》建立英雄探索、城镇建设与六角格战斗的循环，DOS 二代加入兵种升级与双路线战役，Windows 三代扩大阵营、魔法和地图事件。三款作品跨 DOS／Win95／98 连续收藏，但不能与只有名称相近的《魔法门》RPG 正传混成同一专题。','光明与梦幻模拟战':'光明与 Langrisser 拆为两个子系列；Saturn《光明力量 III》不属于本机清单。','女神转生与女神异闻录':'本传与 Persona 分列，保留关联但不混用序号。','洛克人':'元祖／世界、X、Zero、EXE、ZX 与流星分组。','逆转裁判':'正传、逆转检事与同作者的《幽灵诡计》分开识别。'}
out+=['## 游戏内容专题：系列与平台回链','','按作品世界观、题材与真实系列组织；仅两个及以上真实成员设立专题，单款作品不单列“系列”。DOS、Windows、主机和掌机版本使用同一专题并互相回链，单款背景已经并回平台表备注。','']
for s in series_order:
    es=sorted((e for e in entries if e.series==s),key=lambda e:platforms.index(e.platform))
    intro=series_intro.get(s,rg.series_note.get(s,f'围绕《{es[0].zh}》等真实同一系列作品整理，按平台回到对应版本。'))
    out += [f'### {s}','',f'<a id="{series_id[s]}"></a>','',intro+'','']
    groups=[]
    for e in es:
        if e.subgroup not in groups:groups.append(e.subgroup)
    for g in groups:
        if len(groups)>1:out += [f'#### {g}','']
        out += ['| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |','|---|---|---|---:|---|']
        for e in es:
            if e.subgroup==g:out.append(f'| {e.en} | {e.zh} | {short[e.platform]} | {e.year} | [{e.eid}](#{e.eid.lower()}) |')
        out+=['']
    out+=['---','']
mod_out,hack_count=mod_sections(entries,short,platforms)
out += mod_out

out+=['## 三层查漏补缺结果','',
'三层查漏都已落实到上方表格，而不是另留候选清单。榜单用于发现作品，系列用于核对版本和支线，品类用于检查玩法盲区；质量、外设与 N4100 负担再做最后筛选。','',
'| 查漏路径 | 已实际补入或纠正的内容 |','|---|---|',
'| ① 榜单与精品／著名／特色作品 | 补入 Metroid、Super Castlevania IV、Ninja Five-O、The World Ends with You、Tony Hawk、Skies of Arcadia、Shining Force、GG Aleste、Judgement Silversword 等；PS1／PSP 不再只偏 RPG |',
'| ② 从重要系列反查缺作 | 拆清马力欧、宝可梦、三国、洛克人、最终幻想、光明／梦幻模拟战、女神转生子系列；补蓝宝石／红宝石、赤救助队、Wario Land II、Oracle 联动、GBC 与 WS 篇章 |',
'| ③ 从品类与细分反查主题和作品 | 补 Snow Bros.、Bubble Bobble、Puzzle Bobble、Puyo Puyo Tsu、Columns、Gunpey、Magical Drop III、Qix、Mole Mania；补 GG 光明力量外传与 WS 风之少年，避免类型章只有大作 |','',
'核对来源：[IGN 任天堂百佳](https://www.ign.com/articles/the-100-best-nintendo-games-of-all-time)、[Nintendo Life SNES 50](https://www.nintendolife.com/guides/50-best-super-nintendo-snes-games-of-all-time)、[GBA 50](https://www.nintendolife.com/guides/50-best-game-boy-advance-games-of-all-time)、[NDS 50](https://www.nintendolife.com/guides/50-best-nintendo-ds-games-of-all-time)、[GBC 50](https://www.nintendolife.com/guides/50-best-game-boy-color-gbc-games-of-all-time)、[Metacritic PS1](https://www.metacritic.com/browse/game/ps1/)、[Metacritic PSP](https://www.metacritic.com/browse/game/psp/)、[Time Extension MD](https://www.timeextension.com/guides/best-sega-genesis-mega-drive-games-of-all-time)、[Time Extension GG](https://www.timeextension.com/guides/best-sega-game-gear-games-of-all-time)、[MobyGames WSC](https://www.mobygames.com/platform/wonderswan-color/)。','',
'---','','## 容量汇总与运行核对','']
def mb(size):
    try:
        return float(re.findall(r'[\d.]+',size)[0])*(1024 if 'GB' in size.upper() else 1)
    except:return 0
game_counts={
'Pokémon Red / Green / Blue / Yellow':4,'Pokémon Gold / Silver / Crystal':3,'Dragon Warrior Monsters 2: Cobi’s Journey / Tara’s Adventure':2,'Dragon Ball Z: Goku Hishouden / Goku Gekitouden':2,'Game & Watch Gallery 1–3':3,'Shin Megami Tensei I / II':2,'Mario Party 1 / 2 / 3':3,"Bomberman '93 / '94":2,'Valis: The Fantasm Soldier / Valis II / III / IV':4,'Download / Download 2':2,
'Pokémon FireRed / LeafGreen':2,'Mega Man Battle Network 3: Blue / White':2,'Pokémon Ruby / Sapphire':2,'Pokémon HeartGold / SoulSilver':2,'Pokémon Black / White':2,'Pokémon Black 2 / White 2':2,'Phoenix Wright: Ace Attorney / Justice for All / Trials and Tribulations (DS)':3,'Inazuma Eleven 2: Kyoui no Shinryakusha – Fire / Blizzard':2,'Digimon World Dawn / Dusk':2,'Mega Man Star Force: Pegasus / Leo / Dragon':3,'Osu! Tatakae! Ouendan / Elite Beat Agents':2,
'Gradius / Gradius II / Gradius III':3,'Parodius Da! / Sexy Parodius / Gokujou Parodius!':3,'TwinBee / Detana!! TwinBee':2,'Puzzle Bobble / Puzzle Bobble 2 / 3 / 4':4,'Golden Axe (Arcade)':1,'Double Dragon 1 / 2 / 3 (Arcade)':3,'Metal Slug 1 / 2 / X / 3 / 4 / 5':6,'Bubble Bobble / Rainbow Islands':2,'Elevator Action / Elevator Action Returns':2,'Darius / Darius II / Darius Gaiden':3,'Pac-Man / Ms. Pac-Man':2,'Donkey Kong / Donkey Kong Jr.':2,'Galaga / Galaxian':2,
'Virtua Tennis / Virtua Tennis 2':2,'The Legend of Heroes II: Prophecy of the Moonlight Witch / III: White Witch / IV: A Tear of Vermillion / V: Cagesong of the Ocean':4,'DJMax Portable 1 / 2 / Clazziquai / Black Square':4,'Memories Off / Clannad / Steins;Gate / Higurashi / Fate/Extra':5,'Crash Bandicoot 1 / 2: Cortex Strikes Back / 3: Warped':3,'Spyro the Dragon 1 / 2: Ripto’s Rage! / 3: Year of the Dragon':3,'Tomb Raider I / II / III':3,'Tokimeki Memorial 1 / 2':2,'The Legend of Zelda: Oracle of Seasons / Oracle of Ages':2,'Final Fantasy I / II / IV':3,
'Super Mario All-Stars':4,'Ys Book I & II':2,'Final Fantasy I & II: Dawn of Souls':2,'Three Wonders':3,'Street Fighter III: Double Impact':2,'Ys I & II Chronicles':2,'Castlevania: The Dracula X Chronicles':3,'Langrisser II / Der Langrisser':2,
}
game_counts.update(DOS_COUNTS)
game_counts.update(WINDOWS_COUNTS)
def gc(e):return game_counts.get(e.en,1)
game_total=sum(gc(e) for e in entries)
new_hack_count=15
variant_mb=16*1024
maker_columns=['Nintendo','Sega','Sony','NEC／Hudson','Bandai','多厂商／PC']
def maker_cells(p):
    cells=['']*len(maker_columns)
    if p in {'NES / FC','GB','SNES / SFC','N64','GBC','GBA','NDS'}:cells[0]='Nintendo'
    elif p in {'MD / Genesis','GG','Dreamcast'}:cells[1]='Sega'
    elif p in {'PS1','PSP'}:cells[2]='Sony'
    elif p=='PCE (PC Engine / TurboGrafx-16)':cells[3]='NEC／Hudson Soft'
    elif p=='WS / WSC':cells[4]='Bandai'
    else:cells[5]='IBM／Microsoft 等' if p in {'DOS','Win95 / Win98'} else '多厂商'
    return cells
out+=['平台章大体按首发年代排列；Win95／98 紧随 DOS 以区分两种运行环境，N64 与 PS1 依 eMMC／SSD 存储建议对调。出品方矩阵中，空白表示该平台不属于该厂家。','',
'| 平台 | 条目数 | 游戏数（合集展开） | 表内预留空间 | Nintendo | Sega | Sony | NEC／Hudson | Bandai | 多厂商／PC | 建议位置 |','|---|---:|---:|---:|---|---|---|---|---|---|']
total=0
for p in platforms:
    es=[e for e in entries if e.platform==p];v=sum(mb(e.size) for e in es);total+=v
    makers=' | '.join(maker_cells(p))
    out.append(f'| {p} | {len(es)} | {sum(gc(e) for e in es)} | {v/1024:.2f} GB | {makers} | {"SSD" if p in {"Win95 / Win98","PS1","PSP","Dreamcast","NDS"} else "eMMC"} |')
out+=[f'| **官方库合计** | **{len(entries)}** | **{game_total}** | **{total/1024:.2f} GB** |  |  |  |  |  |  | 另留系统、BIOS、刮削与存档 |','',
'#### 游戏总数与总容量','',
f'- **官方游戏总数：{game_total} 个平台版本。** 合集已展开，地区别名不重复；同一游戏跨平台各算一个可玩版本。Game & Watch 等合集按独立商品计数，不把内含迷你游戏再拆成数十款。',f'- **原创改版内容：{new_hack_count} 款。** 仅统计含全新战役、地区或主要地图的改版；纯汉化、平衡调整和便利增强不重复增加游戏数。','- **官方库预留：'+f'{total/1024:.2f} GB。** 中文化与精选改版若与原版全部并存，另建议预留 16 GB；**合计预算 {(total+variant_mb)/1024:.2f} GB**，系统、BIOS、刮削和存档另算。','',
'> 容量是安装预算，不是实测文件总量；合集拆分、CHD／CSO、多盘与保留多个地区版都会改变占用。','',
'### 实机核对顺序','',
'1. DOS：逐作检查可执行文件、声音、鼠标、存档与退出方式；中文游戏保留字库和安装目录，CD 游戏连音轨一起验证，不能只确认进入标题画面。','2. Win95／98：逐作验证安装目录、Wine prefix、字体、过场、鼠标与存档；DirectDraw 黑屏／花屏优先核对 cnc-ddraw 的 DLL 覆盖和全屏设置，Direct3D 则保持低分辨率并单独选渲染路径。','3. MAME、FBNeo：先验证 ROM set、BIOS、双人手柄，再检查高分采样与声音；不要跨核心随意搬 ZIP。','4. NES、PCE、MD、GB、GG、SNES：先开存档与特殊芯片游戏，检查 RTC、传感器和地区刷新率。','5. N64：按游戏选择插件与 1× 渲染，核对 Expansion Pak，并测试最繁忙的战斗／竞速场景。','6. PS1、GBC、Dreamcast、WS／WSC、GBA、NDS、PSP：依次检查多盘与记忆卡、GBC 存档、Dreamcast 重负载场景、WS 横竖持机、GBA 的 RTC／传感器、NDS 双屏触控、PSP 原生设置下的繁忙场景；不只看标题画面。','',
'']
out += hardware_input_appendix()
# 当前版直接合并硬件与容量内容，不保留旧章节或历史修订入口。
cap_start=out.index('## 容量汇总与运行核对')
cap_end=out.index('## 摄像头与麦克风验证附录')
capacity=out[cap_start:cap_end]
del out[cap_start:cap_end]
capacity[0]='### 容量、出品方与存储汇总'
capacity+=['---','']
insert_at=out.index('## 存储、目录与镜像管理')
out[insert_at:insert_at]=capacity
(ROOT/'batocera_rom_guide.md').write_text('\n'.join(out)+'\n')
print('entries',len(entries),'lines',len(out),'bytes',(ROOT/'batocera_rom_guide.md').stat().st_size)
for p in platforms:print(short[p],sum(e.platform==p for e in entries))
print('missing_year',sum(not e.year for e in entries),'missing_pub',sum(not e.pub for e in entries),'generic',sum(e.note.startswith('本作《') for e in entries))
for e in entries:
    if not e.year or not e.pub:print('MISSING',e.platform,e.eid,e.en,e.year,e.pub)
