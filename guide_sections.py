def platform_overview():
    rows=[
    ('DOS／Win3.x','16／32 位 x86 PC 环境','1981／1992','IBM／Microsoft 等','键盘鼠标、VGA、声卡、CD‑ROM 与中文 PC 游戏传统','DOS 用 DOSBox Pure；轻量 Win3.x 用 DOSBox‑X','DOSBox Pure 可用 .zip／.dosz；复杂安装与独立配置用 .pc；Win3.x 需自备系统并配置显示、声音与 WinG；经营和 RTS 用鼠标；Win95／98 游戏转下一平台'),
    ('Win95／98（Wine）','16／32 位 x86 Windows 程序','1995／1998','Microsoft（兼容层由 Wine 提供）','DirectDraw、早期 Direct3D、中文 RPG、策略与经营经典','Batocera 内置 Wine runner（版本随系统更新）','每作独立 .wine prefix；DirectDraw 优先试 cnc-ddraw；DXVK 默认关闭；原始低分辨率；不虚拟完整 Win95，不收射击游戏'),
    ('MAME','多种 8／16／32 位街机','1970 年代末起','多厂商','早期迷宫、单屏、Taito／Namco／Sega 硬件','MAME（当前 Batocera 核心）','ROM set 必须与核心匹配；ZIP 不改名、不解压；BIOS／CHD 依赖完整'),
    ('FBNeo','多种 16／32 位 2D 街机','1980 年代末起','Capcom／SNK／IGS 等','CPS、Neo Geo、PGM、Toaplan 等','FinalBurn Neo（libretro）','Neo Geo／PGM BIOS 随匹配 ROM set；NAOMI 不放入此目录'),
    ('NES／FC','8 位','1983','Nintendo','家用卷轴动作与早期 JRPG，含 FDS','Mesen／Nestopia／FCEUmm','FDS 需 disksys.rom；核对 Mapper、地区制式与汉化改版 Mapper'),
    ('PCE','8 位 CPU＋16 位图形','1987','NEC／Hudson Soft','HuCard 与 CD‑ROM²，射击和 CD 音画突出','Beetle PCE Fast／Beetle PCE','CD 需对应 syscard BIOS；Arcade Card 游戏单独验证；CHD 保留音轨'),
    ('MD／Genesis','16 位','1988','Sega','高速 2D、FM 音源、街机风格','Genesis Plus GX','六键手柄用于街霸等；Sonic 3 & Knuckles 用锁合镜像；核对地区'),
    ('GB','8 位','1989','Nintendo','单色便携，长续航与经典短局','Gambatte／SameBoy','用 GB 调色板，不把 GBC 专用卡误放入 GB；联机按核心支持'),
    ('GG','8 位','1990','Sega','Master System 相近架构的彩色掌机','Genesis Plus GX／Gearsystem','小屏视野与原版一致；整数缩放，不要误用 MD ROM'),
    ('SNES／SFC','16 位','1990','Nintendo','Mode 7、丰富音源、特殊增强芯片','Snes9x（轻量优先）／bsnes','特殊芯片逐作核对；Star Fox 2 用正式发行版；高画质 bsnes 更耗资源'),
    ('N64','64 位','1996','Nintendo','3D 平台与四人本地对战，部分用 Expansion Pak','Mupen64Plus‑Next','按游戏选 GLideN64／Rice；Expansion Pak 游戏核对内存；重负载场景测帧'),
    ('PS1','32 位','1994','Sony','CD 光盘、预渲染背景与早期 3D','x86_64 优先 DuckStation；PCSX‑ReARMed 仅作后备','原生分辨率起步；多盘 M3U；记忆卡与 BIOS 校验，不开高负载增强'),
    ('GBC','8 位','1998','Nintendo','彩色掌机，兼容部分 GB 黑卡','Gambatte／SameBoy','GBC 与 GB 分目录；双版本联动密码属于游戏内功能'),
    ('Dreamcast','32 位','1998','Sega','GD‑ROM、NAOMI 同源、2D 格斗与 3D 原创','Flycast','原生分辨率起步；DC 与 NAOMI 分开；核对 GDI／CHD、区域和 VGA 选项'),
    ('WS／WSC','16 位','1999／2000','Bandai','横竖双持、低功耗、原创益智与掌机衍生','Beetle Cygne／Beetle Wswan','Gunpey 等按游戏旋转画面与按键；WS、WSC 目录可分开'),
    ('GBA','32 位','2001','Nintendo','ARM 掌机，2D 动作与 RPG 丰富','mGBA（libretro）','默认即可；核对 RTC、存档类型；Boktai 与转转瓦力欧需传感器映射'),
    ('NDS','双 32 位 ARM','2004','Nintendo','双屏、触控、麦克风与本地无线','melonDS（软件渲染优先）','配置竖屏／横屏布局与触控；存档类型、麦克风按游戏检查，不开高倍率'),
    ('PSP','32 位','2004','Sony','宽屏便携、UMD、2D 与大型 3D 并存','PPSSPP','1× 渲染、保留缓冲渲染；ISO 为兼容基线；逐作验证，不用统一跳帧掩盖卡顿'),
    ]
    out=['## 平台、硬件、模拟器与容量汇总','','本表、下方容量矩阵与“各平台精选清单”使用完全相同的平台顺序。核心名称是 Batocera 常见选项，实际可用项随安装版本变化；先用轻量核心和原生设置，再针对单作调整，不为所有游戏套同一个“优化配置”。','',
    '| 平台 | 位数／架构 | 发布时间 | 发布商 | 主要特点 | 对应模拟器／核心 | 特别配置 |','|---|---|---:|---|---|---|---|']
    out += ['| '+' | '.join(r)+' |' for r in rows]
    return out+['']

def mod_sections(entries,short,platforms,entry_link):
    labels={'DOS':'DOS','Win95／98':'Win95 / Win98','MAME':'MAME','FBNeo':'FBNeo','NES／FC':'NES / FC','PCE':'PCE (PC Engine / TurboGrafx-16)','MD':'MD / Genesis','GB':'GB','GG':'GG','SNES／SFC':'SNES / SFC','N64':'N64','PS1':'PS1','GBC':'GBC','Dreamcast':'Dreamcast','WS／WSC':'WS / WSC','GBA':'GBA','NDS':'NDS','PSP':'PSP'}
    def ordered(rows):
        return sorted(rows,key=lambda r:platforms.index(labels[r[0]]))
    def link(title):
        e=next((x for x in entries if x.en==title),None)
        return entry_link(e,e.zh) if e else title
    trans=[
    ('NES／FC','Dragon Quest I–II','早期中文化＋后续修正','FC 的 DQ 前两作文本和菜单量较大，不同卡带时期译名差异明显；优先选修复乱码与存档问题的版本。III／IV 已在保留平台采用重制版。'),
    ('NES／FC','Metal Max','先锋卡通中文化＋doubledr 等修正','中文化是它在中文圈形成口碑的重要原因；修正版改善旧版文本与兼容，仍应保留日版原作作对照。'),
    ('NES／FC','Tenchi wo Kurau I／II','早期中文化＋后续修正','武将、阵型与剧情都依赖文本，诸葛孔明传尤其需要完整中文化；不要把玩家改编剧情当官方原作。'),
    ('NES／FC','Fire Emblem Gaiden','民间汉化','外传的武器、职业和角色对话需要准确译名；其系统与正统序号作不同，初代已在 NDS 保留重制版。'),
    ('NES／FC','Nakahara no Hasha／Haou no Tairiku','早期中文化＋后续修正','中原之霸者与霸王的大陆是 Namco 系统，中文菜单让它们成为 FC 策略启蒙；不要套用光荣《三国志》发行信息。'),
    ('NES／FC','Captain Tsubasa II: Super Striker','民间汉化＋修复','必杀技、球员与剧情文本量大，中文化明显提升可玩性；修正重点应是死机、字库和赛程显示。'),
    ('MD','Langrisser II','民间汉化','兵种、转职与指挥范围需要清楚文本；初代已在 SFC 采用《Der Langrisser》，本行只对应 MD 二代。'),
    ('MD','Shining Force I／II','民间汉化','角色对话、转职和道具说明是主要阅读点；GG 外传不是这两作的镜像版本。'),
    ('MD','Phantasy Star IV','民间汉化＋修正','剧情和组队技说明适合完整中文体验，选择修复字体与文本溢出的版本。'),
    ('MD','Beyond Oasis／Landstalker','民间汉化','两款动作 RPG 都依赖道具和谜题提示，中文能降低等距视角与精灵谜题之外的额外门槛。'),
    ('SNES／SFC','Chrono Trigger／Final Fantasy VI','民间汉化','两部 Square RPG 都有成熟中文化需求；魔石、协力技等术语应保持一致，不把后续复刻追加内容误写入 SFC 原版。'),
    ('SNES／SFC','Dragon Quest III','民间汉化','SFC 的 III 是重制；IV／V／VI 已采用 NDS 版本，字库和存档应按实际保留平台分别验证。'),
    ('SNES／SFC','Der Langrisser','民间汉化','多阵营路线、兵种、转职与指挥范围需要准确文本；本行对应 SFC 初代重制，不与 MD 二代混底本。'),
    ('SNES／SFC','Fire Emblem: Genealogy of the Holy War／Thracia 776','民间汉化','血统、配对、俘虏和疲劳等机制需要精确说明；两作属于同一世界的不同时段。'),
    ('SNES／SFC','Tactics Ogre: Let Us Cling Together','民间汉化','阵营、法律和职业文本量大；SFC 原版与 PSP《命运之轮》不是同一重制版本。'),
    ('SNES／SFC','Terranigma／Bahamut Lagoon／Live A Live','民间汉化','三款未正式海外发行的作品各以复兴世界、龙与群像、分时代章节见长，中文能补足其最重要的叙事价值。'),
    ('GBA','Pokémon Emerald／FireRed／LeafGreen','民间汉化','中文便于理解特性、技能和剧情；“386”“全神兽”等同时改数据的作品应改归改版，不冒充纯汉化。'),
    ('GBA','Golden Sun／The Lost Age','民间汉化','精神力、精灵与召唤术语较多，两部连续故事适合统一译名。'),
    ('GBA','Castlevania: Circle of the Moon／Harmony of Dissonance／Aria of Sorrow','民间汉化','DSS、法术书与魂系统的说明各不相同；三作都应保留原日版作版本对照。'),
    ('GBA','Mother 3','民间汉化','原版仅在日本正式发行，汉化使章节叙事和节奏战斗更易理解；声音连击需要实际听节拍。'),
    ('NDS','Pokémon Platinum／HeartGold／SoulSilver／Black／White／Black 2／White 2','民间汉化','神奥、城都与合众作品均可按世代整理中文版本；纯汉化与提高难度、改图鉴的改版分目录。'),
    ('NDS','Dragon Quest IV／V／VI／IX','民间汉化','章节、人生旅程、双世界与多人任务分别依赖大量文本；NDS 版不是 GBA 移植。'),
    ('NDS','Phoenix Wright: Ace Attorney 1–3','民间汉化','法庭指证要求精确文本，优先选修复错字、证物描述和存档的版本；三部曲与 NDS 底本一一对应。'),
    ('NDS','Ghost Trick／Ace Attorney Investigations 2','民间汉化','逆转检事 2 未正式海外发行，中文化尤其重要；幽灵诡计的线索链要求准确译文。'),
    ('NDS','999／Professor Layton 系列','民间汉化','数字根、谜题提示和多结局文本是核心，不适合只靠图片攻略跳过语言。'),
    ('PS1','Final Fantasy VII／VIII／IX／Tactics','民间汉化','魔晶石、Junction、职业与政治叙事均需统一术语；多盘版必须让汉化镜像与 M3U 盘序一致。'),
    ('PS1','Xenogears／Chrono Cross／Vagrant Story','民间汉化','三部作品的世界观和系统文本密度高，中文更适合理解机甲设定、平行世界与武器构筑。'),
    ('PS1','Suikoden II／Valkyrie Profile','民间汉化','108 星招募和英灵章节都含易遗漏条件，中文可降低理解成本，但仍需保留原版镜像作校验。'),
    ('PS1','Metal Gear Solid／Persona 2: Innocent Sin','民间汉化',' codec 与潜行提示、传言系统和人物关系都高度依赖文本；Innocent Sin 的 PS1 日版与后续移植分开。'),
    ('PSP','Trails in the Sky FC／SC／Zero／Ao','民间汉化','轨迹系列 NPC 文本和连续剧情量很大，建议按 FC→SC→Zero→Ao 顺序，并分游戏备份存档。'),
    ('PSP','Persona 3 Portable／Valkyria Chronicles III','民间汉化','P3P 的日程社群与战场女武神 3 的部队任务都需要文本；后者未正式海外发行。'),
    ('PSP','Ys: The Oath in Felghana／Ys Seven／Monster Hunter Portable 3rd','民间汉化','装备、技能、怪物与任务说明适合中文；动作本身不需要等汉化，但完整体验会明显受益。'),
    ]
    hacks=[
    ('Win95／98','三国志姜维传','三國志曹操伝 / Sangokushi Sousouden','非官方全新剧情与战役','以姜维为主角扩展后三国故事，包含独立人物、战役和大量新文本，是曹操传引擎的高完成度中文同人改版，不是光荣官方续作。按所选发布包说明使用匹配底本，在独立 Wine prefix 中运行，不与曹操传原版共用存档；同样优先保留完整动画、字体与 cnc-ddraw 配置。'),
    ('NES／FC','Super Mario Bros. 3Mix','Super Mario Bros. 3','全新关卡／跨作机制','融合多部马力欧元素与新地图，完成度高；先通原版再玩，部分改版 Mapper 需在 Mesen／FCEUmm 验证。'),
    ('NES／FC','Super Mario Unlimited','Super Mario Bros.','全新关卡／难度重构','基于初代引擎设计新世界，强调隐藏路线与跳跃技巧，不是官方 Lost Levels。'),
    ('NES／FC','Yanshan 90 Tank / Tank 1990（烟山 90 坦克）','Battle City','新关卡／规则扩展','烟山软件基于 FC《Battle City》制作的经典修改版，加入新手枪与船、消草、敌人拾取道具及更多关卡／难度组合，并支持双人借命。它不是 Namco 官方续作；同名合卡与后续二改很多，应固定一个说明清楚的版本，用 Mesen 验证选关、道具和双人，A–N 等模式不重复算游戏数。'),
    ('NES／FC','Rockman 4: Minus Infinity','Mega Man 4','系统增强／全新关卡','重做武器、Boss 与关卡并加入惊喜演出，质量很高但难度硬核；适合熟悉元祖系列的玩家。'),
    ('SNES／SFC','The Second Reality Project Reloaded','Super Mario World','全新关卡','大型新关卡包，重做地图、图形与音乐，保留 SMW 手感；与原版分存档。'),
    ('SNES／SFC','The Legend of Zelda: Parallel Worlds','The Legend of Zelda: A Link to the Past','全新地图／难度重构','重排世界和迷宫，路线与解谜几乎全新，难度高于原作；不是官方续作。'),
    ('SNES／SFC','Super Metroid: Redesign Axeil Edition','Super Metroid','地图重构／难度调整','扩大并重塑泽贝斯探索，Axeil 版调整原作改版的严苛处；适合熟悉原版地图与技巧者。'),
    ('SNES／SFC','Final Fantasy VI: Brave New World','Final Fantasy VI','平衡与养成重构','重做角色、 Esper 与敌方数据，强化人物构筑差异；不是“简单加强”，需要重新理解系统。'),
    ('GBA','Pokémon Unbound','Pokémon FireRed','全新地区与剧情／系统增强','完整原创地区、任务与较新世代机制，难度选项友好；这是大型改版，不是官方正统地区。'),
    ('GBA','Pokémon Radical Red','Pokémon FireRed','图鉴与难度重构','以后代机制、技能和高强度对战见长，默认难度偏硬核；家庭首次游玩不建议替代原版。'),
    ('GBA','Pokémon Emerald Rogue','Pokémon Emerald','规则重构／随机关卡','把道馆旅程改成连续路线选择与随机构筑，重玩性来自 Roguelike 循环，不是绿宝石剧情汉化。'),
    ('GBA','Pokémon Team Rocket Edition','Pokémon FireRed','剧情改写／系统增强','从火箭队视角重讲关都并改动养成与任务，适合已熟悉原版剧情者。'),
    ('GBA','Fire Emblem: Vision Quest','Fire Emblem: The Sacred Stones','全新战役','利用 GBA 火纹引擎制作原创地图、角色与剧情，应作为独立同人战役管理。'),
    ('NDS','Pokémon Renegade Platinum','Pokémon Platinum','图鉴与平衡增强','保留神奥主线，扩展可用宝可梦并调整训练家与便利功能，是较接近“增强原作”的路线。'),
    ('NDS','Pokémon Sacred Gold／Storm Silver','Pokémon HeartGold / SoulSilver','图鉴与难度增强','扩展城都／关都可获得内容并提高训练家强度；两个改版对应两个原版底本。'),
    ('NDS','Pokémon Blaze Black 2／Volt White 2','Pokémon Black 2 / White 2','图鉴与难度增强','保留 BW2 主线并调整图鉴、队伍与难度；不要与第一代 Blaze Black／Volt White 混底本。'),
    ('MD','Sonic 3 Complete','Sonic the Hedgehog 3 & Knuckles','修复与可选增强','整合锁合内容并提供多项可选调整，目标是更完整的 Sonic 3 体验；选项不宜误当原始官方设置。'),
    ('MD','Sonic Megamix','Sonic the Hedgehog','全新关卡／系统融合','汇集多角色、音乐与重做关卡，风格接近大型同人合集；不同版本完成状态不同，固定一个成熟版本收藏。'),
    ('N64','Super Mario 64: Star Road','Super Mario 64','全新关卡','以新场景和新星星路线重制收集体验，规模接近完整同人续篇；图形插件与存档需单独验证。'),
    ('N64','Super Mario 64: Last Impact','Super Mario 64','全新关卡／新机制','加入新能力、机关和大型关卡，技术改动较多；N4100 上用兼容插件逐场景测试。'),
    ('PS1','Final Fantasy Tactics: Valeria','Final Fantasy Tactics','职业与平衡重构','调整职业、装备、敌人和难度，让冷门技能更有用；适合已理解原版 FFT 的玩家。'),
    ]
    trans=ordered(trans);hacks=ordered(hacks)
    out=['## 中文化版本与精选非官方改版','',
    '这一章与官方商品清单分开管理。**中文化不视为新游戏；改版也不冒充官方发行。** 文件建议按 `平台／原版`、`平台／汉化`、`平台／改版` 分开，各自保留补丁说明、底本版本和独立存档。只把补丁应用于自己合法备份的原版，不提供 ROM 或下载地址。','',
    '### 中文化版本：优先保留哪些','',
    '“早期中文化”包括当年港台或大陆厂商推出、但未必获得原权利人正式授权的版本；它们是中文游戏传播史的一部分，不等于官方中文版。译者、修订者与 CRC 以所选补丁说明为准，不用一个模糊的“汉化版”覆盖所有修订。','',
    '| 平台 | 原作／范围 | 中文化性质 | 选择与使用建议 |','|---|---|---|---|']
    for p,t,k,n in trans:out.append(f'| {p} | {t} | {k} | {n} |')
    out+=['','### 精选非官方改版：增强、重构与全新内容','',
    '这里的“威力加强版”按玩家修改版处理；光荣等厂商正式发行的 Power‑Up Kit／威力加强版仍是官方商品，不放进下表。纯无敌、无限金钱、简单换皮和粗暴提高数值不占位置。','',
    '| 平台 | 改版名称 | 对应原作 | 类型 | 内容、难度与兼容说明 |','|---|---|---|---|---|']
    for p,h,b,k,n in hacks:out.append(f'| {p} | {h} | {link(b)} | {k} | {n} |')
    out+=['','### 改版安装与家庭游玩规则','',
    '1. 先读补丁要求的地区、Rev、Header 与 CRC，底本不对不要硬打；IPS／BPS／xdelta 不混用。Windows 改版则核对发布包对应的原版版本和文件结构，不把不同整合包逐文件混拷。','2. 原版、汉化、改版使用不同目录与存档名，先开新档再验证旧档；不要把兼容未证实的改版直接覆盖家庭共用存档。','3. 模拟器优先沿用原作核心；若改版修改 Mapper、容量或图形方式，再逐作切换核心。Windows 改版使用独立 Wine prefix，保留自己的字体、DLL 覆盖和 cnc-ddraw 配置。Rockman 4 MI、N64 大型改版尤其需要实际场景验证。','4. 难度标签必须保留：Radical Red、Parallel Worlds、Rockman 4 MI 等面向熟练玩家，不能替代家庭首次游玩的原版。','',
    '> 版本统计：上表共收录 '+str(len(trans))+' 组中文化建议、'+str(len(hacks))+' 款精选改版。中文化与增强版不重复计算原作总数；含全新战役／地图的改版另作改版内容统计。','',
    '改版选择参考：[CBR 的 ROM hack 类型综述](https://www.cbr.com/best-rom-hacks-better-than-original/) 与 [Rockman 4: Minus Infinity 评测](https://www.romhacking.net/reviews/5674/)；FC 中文化传播参考 [重装机兵与 FC 中文 RPG 史料](https://k.sina.cn/article_1403377667_53a5d80300100pilc.html?from=game)。','','---','']
    return out,len(hacks)

def stg_history(entries,entry_link):
    def link(title):
        e=next((x for x in entries if x.en==title),None)
        if not e:e=next((x for x in entries if x.en.startswith(title)),None)
        return entry_link(e,e.zh) if e else title
    out=['**STG 机制时间线。** 这条脉络按机制而不是“厂商名气”排列。Toaplan 强化关卡记忆、武器和节奏；彩京把角色、蓄力攻击与近战风险结合起来；Cave 则把敌弹密度、连锁、得分和 Hyper 等系统推到新层次。“擦弹”并非所有 Cave 作品的统一核心：《怒首领蜂》重点是连锁与弹幕，《大往生》还要理解 Hyper 的资源收益。','',
    '| 年代 | 厂商／流派 | 条目回链 | 在进化史中的位置 |','|---:|---|---|---|']
    timeline=[
    ('1985','Toaplan','Tiger Heli','早期纵版空战，以炸弹和固定关卡节奏建立记忆型射击。'),
    ('1987','Irem','R-Type','蓄力炮与 Force 装置改变站位，关卡解谜性显著增强。'),
    ('1988','Toaplan','Truxton','高速敌群、武器升级与严苛关卡延续传统硬派路线。'),
    ('1990','Seibu Kaihatsu','Raiden','双色武器、双人协作和易懂节奏让雷电成为街机厅常青树。'),
    ('1993','Toaplan','Batsugun','角色与火力成长、密集弹幕已显露后来 Cave 风格的先声。'),
    ('1994–1999','彩京 Psikyo','Gunbird 1','武装飞鸟、Strikers 与战国系列把角色射击和蓄力攻击发展成稳定体系。'),
    ('1996','彩京 Psikyo','Sengoku Blade','横版角色射击，近战与蓄力让风险站位比单纯躲弹更重要。'),
    ('1996','Raizing／8ing','Battle Garegga','动态难度与得分资源相互牵制，高手路线和首次通关几乎是两种玩法。'),
    ('1997','Cave','DoDonPachi','连锁击破、蜂道具与高密度弹幕结合，确立 Cave 的代表性得分语言。'),
    ('1998','Cave','ESP Ra.De.','角色灵力与穿透攻击加入得分决策，弹幕不仅是生存压力也是资源。'),
    ('1999','彩京 Psikyo','Strikers 1945 III','以现代喷气机、蓄力攻击和变形 Boss 延续 1945 系列。'),
    ('2000','彩京 Psikyo','Dragon Blaze','龙的分离与召回改变攻击位置，是彩京机制创新的典型。'),
    ('2001','Cave／Capcom','Progear','横向弹幕、宝石与连击构成另一条 Cave 路线，画面和音乐风格鲜明。'),
    ('2002','Cave','DoDonPachi Dai-Ou-Jou','Hyper 同时增强火力与风险，资源管理进入背板和得分核心。'),
    ('2003','Cave','Espgaluda','觉醒系统改变敌弹与得分规则，进一步强化攻防转换。'),
    ]
    for year,maker,title,note in timeline:out.append(f'| {year} | {maker} | {link(title)} | {note} |')
    out+=['','补充交叉索引：彩京另见 '+link('Strikers 1945')+'，Toaplan 另见 '+link('Fire Shark')+' 与 '+link('Out Zone')+'；Treasure 的 '+link('Ikaruga')+' 以黑白极性吸收敌弹，不属于 Cave，却构成理解弹幕规则创新的必要对照。']
    return out

def hardware_input_appendix():
    return ['## 摄像头与麦克风验证附录','',
    '机器带有摄像头和麦克风，只说明物理设备存在；能否用于游戏必须经过 **Linux 驱动 → Batocera 设备识别 → 模拟器核心接口** 三层。任何一层缺失，都不能把外设游戏写成可玩。此附录是现场验证流程，不是对当前机器已经兼容的承诺。','',
    '### 1．先确认操作系统是否看见设备','',
    '在 Batocera 的 SSH 终端执行；不同镜像未必安装全部命令，缺少命令时以设备节点和系统日志交叉判断，不要为了测试盲目覆盖系统配置。','',
    '```bash','lsusb','v4l2-ctl --list-devices','ls -l /dev/video*','arecord -l','cat /proc/asound/cards','```','',
    '- 普通 **UVC 摄像头**通常应出现 `/dev/video0` 一类节点；`v4l2-ctl` 能列出格式，说明驱动层更进一步。','- **ALSA** 应列出录音设备，随后还要测试实际采样、音量与噪声；只有播放声卡不等于麦克风可用。','- USB 复合设备可能分别出现视频和音频节点。若设备未被识别，先换 USB 口并排除供电、转接器和隐私开关，再核对具体芯片与当前 Batocera 内核。','',
    '### 2．再确认模拟器是否提供输入接口','',
    '**系统识别不等于核心能调用。** RetroArch、libretro 核心和独立模拟器的摄像头／麦克风能力并不一致，同一核心不同 Batocera 版本也可能变化。先在当前界面查找 Microphone、Camera、Device Input 等选项，再用游戏内实际输入验证；不要只看“设备已连接”。','',
    '| 场景 | 本指南的处理 | 验证边界 |','|---|---|---|',
    '| NDS《Nintendogs》《Brain Age》 | 保留，但麦克风不是全库统一前提 | 若当前 melonDS 提供真实麦克风输入，选择对应采集设备；若只有噪声／吹气模拟，只适合接受吹气的环节，不能保证连续语音识别 |',
    '| NDS 触控与双屏 | 先用鼠标或映射手柄验证 | 与麦克风分开测试；双屏显示正常不代表语音链路正常 |',
    '| N64《Hey You, Pikachu!》 | 不收录 | 原作需要 VRU 专用硬件与语音识别链路，内置普通麦克风不能据此承诺完整可玩 |',
    '| DSi 摄像头游戏 | 不纳入普通 NDS 清单 | DSi 是不同硬件与核心支持范围，不能把 DSi 功能套到 NDS |',
    '| 其他平台摄像头游戏 | 当前不设专门游戏库 | 本清单没有必须依赖摄像头的作品；只有核心明确支持且实测通过后才另行增加 |','',
    '### 3．建议的现场测试顺序','',
    '1. 先确认 `/dev/video*` 与 ALSA 采集设备，再在系统层做一次短录音／图像测试；失败就停在驱动层排查。','2. 在 melonDS 中检查输入选项，分别测试持续语音、短促吹气和无输入三种状态，排除环境噪声造成的假成功。','3. 用《Nintendogs》的语音呼唤和《Brain Age》的语音环节验证游戏内结果，并记录 Batocera 版本、核心版本和设备名。','4. 测试结果只写入该设备的个人配置；本指南仍保持“普通手柄即可运行大部分作品”的保守基线。','','---','']
