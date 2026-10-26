# 同一基础作品的跨平台版本取舍。只处理移植、普通重制、明确增强版和合集重复；
# 续作、平行原创、关卡或系统明显不同的独立改编不在此机械去重。
# keeps／drops 均为 (platform, exact English title)，reason 会写入保留作品备注。
VERSION_CHOICES = []

def choice(name, keeps, drops, reason):
    VERSION_CHOICES.append({'name': name, 'keeps': keeps, 'drops': drops, 'reason': reason})

choice('三国志 V', [('PS1', 'Romance of the Three Kingdoms V')], [('Win95 / Win98', 'Sangokushi V / 三國志V')], '保留 PS1 版：在本机候选中省去 Windows 旧安装器、字库与 Wine prefix 的额外维护，回合操作可用映射手柄完成；Windows 版不再重复收藏。')
choice('三国志 VI', [('PS1', 'Romance of the Three Kingdoms VI')], [('Win95 / Win98', 'Sangokushi VI / 三國志VI')], '保留 PS1 版：完整覆盖六代的同时行动与武将事件，运行链比旧 Windows 版直接；不以 PC 首发身份重复占一份容量。')
choice('三国志 VII', [('PS1', 'Romance of the Three Kingdoms VII')], [('Win95 / Win98', 'Sangokushi VII / 三國志VII'), ('PSP', 'Romance of the Three Kingdoms VII')], '保留 PS1 版：七代的全武将扮演内容完整，负载低于 PSP 路径，也避开 Windows 日区字库与安装器维护；三个平台只留此版。')
choice('三国志 II／III', [('SNES / SFC', 'Romance of the Three Kingdoms II'), ('SNES / SFC', 'Romance of the Three Kingdoms III: Dragon of Destiny')], [('MD / Genesis', 'Romance of the Three Kingdoms II'), ('MD / Genesis', 'Romance of the Three Kingdoms III: Dragon of Destiny')], '保留 SFC 版：同为 16 位光荣移植时优先这一版本，避免 MD 与 SFC 各存一套内容高度重叠的镜像。')
choice('信长之野望 全国版', [('SNES / SFC', 'Nobunaga’s Ambition: Zenkokuban')], [('MD / Genesis', 'Nobunaga’s Ambition: Zenkokuban')], '保留 SFC 版：全国版的战略主体一致，SFC 版在本库中作为单一收藏版本，MD 移植不再并列。')
choice('古大陆物语 I／II 与四个封印', [('DOS', 'Farland Story: Tooi Kuni no Monogatari / ファーランドストーリー 遠い国の物語'), ('DOS', 'Farland Story Denki: Arc Ou no Ensei / ファーランドストーリー 伝記 アーク王の遠征')], [('Win95 / Win98', 'Farland Story: Yottsu no Fuuin / ファーランドストーリー 四つの封印')], '保留 DOS 前两作：系列已有完整中文 DOS 路线；《四个封印》主要重制这两作，若再收 Windows 合集将重复两段战役，还会增加 CD 音轨、字库与 Wine 验收负担。')
choice('仙剑奇侠传初代', [('Win95 / Win98', '新仙劍奇俠傳')], [('DOS', '仙劍奇俠傳')], '保留 Windows《新仙剑奇侠传》：在本机候选中以重制后的音画和完整中文演出覆盖初代旅程，DOS 原作不再另占一份；须先通过 Wine 字库、动画与存档验收。')
choice('Theme Hospital', [('DOS', 'Theme Hospital')], [('PS1', 'Theme Hospital')], '保留 DOS 版：医院经营以鼠标为原生输入，PC 界面和版本完整度更适合本作，DOSBox 负担也低；PS1 手柄移植不重复保留。')
choice('文明初代', [('DOS', "Sid Meier's Civilization")], [('PS1', 'Sid Meier’s Civilization')], '保留 DOS 版：4X 的大量菜单以鼠标操作最直接，DOS 原版能完整呈现初代系统；PS1 手柄重排界面不再另收。')
choice('波斯王子初代', [('DOS', 'Prince of Persia')], [('MD / Genesis', 'Prince of Persia'), ('SNES / SFC', 'Prince of Persia')], '保留 DOS 原版：以最初的转描动画、关卡和计时结构作为版本基准，键盘或映射手柄即可；MD／SFC 的音画与节奏改动不再各存一份。')
choice('Another World', [('DOS', 'Another World / Out of This World')], [('SNES / SFC', 'Another World / Out of This World')], '保留 DOS 版：以电脑原版的电影化动作解谜和检查点结构为基准，避免与 SFC 移植重复；键盘映射即可游玩。')
choice('Lemmings', [('DOS', 'Lemmings')], [('SNES / SFC', 'Lemmings')], '保留 DOS 版：为旅鼠逐个分配技能天然适合鼠标，原版关卡与操作效率优于手柄移植；SFC 版不再重复。')
choice('大航海时代 II', [('DOS', 'Uncharted Waters: New Horizons / Daikoukai Jidai II')], [('SNES / SFC', 'Uncharted Waters: New Horizons / Daikoukai Jidai II')], '保留 DOS 版：航海、交易与大量菜单在 PC 鼠标界面下更顺手，内容基础完整；SFC 同名移植不再重复。')
choice('R-Type 初代', [('FBNeo', 'R-Type')], [('MD / Genesis', 'R-Type'), ('PCE (PC Engine / TurboGrafx-16)', 'R-Type')], '保留街机原版：Force、蓄力炮和关卡节奏均以街机为基准，FBNeo 在 N4100 上负担低；MD 与 PCE 的分关或移植差异不再各存一份。')
choice('雷电初代', [('FBNeo', 'Raiden')], [('MD / Genesis', 'Raiden Trad'), ('PCE (PC Engine / TurboGrafx-16)', 'Raiden')], '保留街机原版：双色武器、双人合作与原版关卡节奏完整，2D 模拟负担低；MD《Raiden Trad》和 PCE 移植不再重复。')
choice('兽王记', [('MAME', 'Altered Beast')], [('MD / Genesis', 'Altered Beast')], '保留街机原版：变身、清版节奏与双人内容以街机为基准；MD 同捆移植虽有历史意义，但不再为同一作品占第二份。')
choice('战斧初代', [('FBNeo', 'Golden Axe (Arcade)')], [('MD / Genesis', 'Golden Axe')], '保留街机原版：魔法、骑乘和合作清版以街机内容为基准；MD 移植不重复，MD 的 II／III 作为独立续作继续保留。')
choice('饿狼传说 2', [('FBNeo', 'Fatal Fury 2')], [('MD / Genesis', 'Fatal Fury 2')], '保留街机原版：角色阵容、双线系统、动画和输入节奏更完整，FBNeo 运行轻松；MD 移植不再重复。')
choice('侍魂初代', [('FBNeo', 'Samurai Shodown')], [('MD / Genesis', 'Samurai Shodown')], '保留街机原版：刀剑重击、缩放与角色动画以 Neo Geo 原版为基准；MD 移植的取舍不再另占一条。')
choice('快打旋风初代', [('FBNeo', 'Final Fight')], [('SNES / SFC', 'Final Fight')], '保留街机原版：角色、关卡与双人合作完整；SFC 移植在合作和内容上有明显限制，因此不重复收藏。')
choice('少年街霸 Alpha 2', [('FBNeo', 'Street Fighter Alpha 2')], [('SNES / SFC', 'Street Fighter Alpha 2')], '保留街机原版：动画、输入与对战节奏没有 16 位家用移植的读取和硬件妥协；SFC 版不再重复。')
choice('噗哟噗哟通', [('FBNeo', 'Puyo Puyo Tsu')], [('GG', 'Puyo Puyo Tsu')], '保留街机版：连锁、相杀与双人对战内容完整，家庭电视端也比 GG 小屏移植更直接；掌机版不再重复。')
choice('噗哟噗哟 SUN', [('MAME', 'Puyo Puyo Sun')], [('MD / Genesis', 'VS Puyo Puyo SUN / Futari de Puyo Puyo SUN')], '保留 ST-V 街机版：包含完整单人内容；MD Mini 2 的 2022 年版本以双人为定位、没有完整单人剧情，因此不再并列。')
choice('魂斗罗初代', [('NES / FC', 'Contra')], [('FBNeo', 'Contra (Arcade)')], '按家庭机定位保留 FC 版：关卡针对家用机重排，也是本清单和中文游玩记忆采用的版本；街机同名作不再重复。')
choice('超级魂斗罗', [('NES / FC', 'Super C')], [('FBNeo', 'Super Contra (Arcade)')], '按家庭机定位保留 FC《Super C》：家用关卡与操作是这里采用的基准，街机《Super Contra》不再另存。')
choice('沙罗曼蛇', [('NES / FC', 'Life Force / Salamander')], [('FBNeo', 'Life Force')], '按家庭机定位保留 FC 版：横纵卷轴、力量槽与双人合作均完整，符合本指南的 FC 经典路线；街机《Life Force》不再重复。')
choice('宇宙巡航机 I–III', [('FBNeo', 'Gradius / Gradius II / Gradius III')], [('NES / FC', 'Gradius'), ('SNES / SFC', 'Gradius III')], '保留 FBNeo 街机 I／II／III 收藏组：力量槽和关卡采用街机基准，FC 初代与 SFC 三代移植不再重复；PS1 原创《Gradius Gaiden》不受影响。')
choice('疯狂大射击', [('FBNeo', 'Parodius Da! / Sexy Parodius / Gokujou Parodius!')], [('SNES / SFC', 'Parodius Da!')], '保留街机收藏组：以《Parodius Da!》原版及后续独立作品覆盖系列脉络，SFC 同名移植不再重复。')
choice('兵蜂早期作品', [('FBNeo', 'TwinBee / Detana!! TwinBee')], [('NES / FC', 'TwinBee')], '保留街机《TwinBee／Detana!! TwinBee》：铃铛强化和双人合作采用原版基准，FC 初代移植不再重复；SFC 原创《Pop’n TwinBee》继续保留。')
choice('双截龙街机三部曲', [('FBNeo', 'Double Dragon 1 / 2 / 3 (Arcade)')], [('NES / FC', 'Double Dragon'), ('NES / FC', 'Double Dragon II: The Revenge'), ('NES / FC', 'Double Dragon III: The Sacred Stones')], '保留街机三部曲：三作以原始清版动作和合作内容收藏，FC 对应作不再重复；GB《Double Dragon II》有独立掌机关卡，仍予保留。')
choice('热血硬派', [('FBNeo', 'Nekketsu Kouha Kunio-kun / Renegade (Arcade)')], [('NES / FC', 'Nekketsu Kouha Kunio-kun')], '保留街机原作：作为热血系列清版动作起点收藏，FC 移植不重复；开放街区的《River City Ransom》等独立作品不受影响。')
choice('街头霸王 II', [('FBNeo', 'Super Street Fighter II Turbo')], [('FBNeo', 'Street Fighter II: The World Warrior'), ('FBNeo', 'Street Fighter II: Hyper Fighting'), ('FBNeo', 'Street Fighter II: Champion Edition'), ('MD / Genesis', "Street Fighter II': Special Champion Edition"), ('SNES / SFC', 'Street Fighter II Turbo: Hyper Fighting'), ('SNES / SFC', 'Super Street Fighter II: The New Challengers')], '只留《Super Street Fighter II Turbo》：在同一基础作品与明确增强版本中，以角色、系统和超级连击最完整的街机版本收束 II 代；旧街机修订及 MD／SFC 移植不再逐版堆放。')
choice('街头霸王 III', [('FBNeo', 'Street Fighter III: 3rd Strike')], [('FBNeo', 'Street Fighter III: New Generation'), ('FBNeo', 'Street Fighter III: 2nd Impact'), ('Dreamcast', 'Street Fighter III: Double Impact'), ('Dreamcast', 'Street Fighter III: 3rd Strike')], '只留街机《3rd Strike》：作为 III 代最终修订覆盖本作阵容与系统，前两代修订和 DC 合集／移植不再重复，亦减轻光盘镜像占用。')
choice('少年街霸 Alpha 3', [('FBNeo', 'Street Fighter Alpha 3')], [('PS1', 'Street Fighter Alpha 3')], '保留街机版：动画帧、输入和节奏不受 PS1 内存与读取条件限制；PS1 虽追加模式，本清单不为同一格斗主体再留一份。')
choice('Marvel vs. Capcom 1', [('FBNeo', 'Marvel vs. Capcom: Clash of Super Heroes')], [('Dreamcast', 'Marvel vs. Capcom: Clash of Super Heroes')], '保留街机版：双人标签、援护和空中连段以 CPS-II 原版为基准，2D 运行负担低；DC 移植不再重复。')
choice('Marvel vs. Capcom 2', [('Dreamcast', 'Marvel vs. Capcom 2: New Age of Heroes')], [('FBNeo', 'Marvel vs. Capcom 2: New Age of Heroes')], '保留 Dreamcast 版：与 NAOMI 同源、适合家庭双人对战，并把 NAOMI 内容统一留在 DC／Flycast 路径；FBNeo 条目不重复。')
choice('生化危机 2', [('PS1', 'Resident Evil 2')], [('N64', 'Resident Evil 2')], '保留 PS1 原版：双路线、双光盘音画与演出采用原始版本，N64 虽是高压缩技术移植，仍需重负载 N64 图形设置，故不重复。')
choice('GTA 唐人街战争', [('NDS', 'Grand Theft Auto: Chinatown Wars')], [('PSP', 'Grand Theft Auto: Chinatown Wars')], '保留 NDS 版：俯视结构、触屏交互和小游戏是作品的原创操作路线，体积与模拟负担也更适合本机；PSP 移植不再重复。')
choice('蚯蚓战士初代', [('MD / Genesis', 'Earthworm Jim')], [('SNES / SFC', 'Earthworm Jim')], '保留 MD 版：以本作首发平台的动画、音效与关卡表现为基准，SFC 移植不再重复；二代是独立续作。')
choice('俄罗斯方块', [('GB', 'Tetris')], [('NES / FC', 'Tetris')], '保留任天堂 GB 版：规则完整、运行轻量，也是系列便携传播与本地联机史上最有代表性的版本；FC 版不再重复。')
choice('小蜜蜂／大蜜蜂', [('MAME', 'Galaga / Galaxian')], [('NES / FC', 'Galaxian'), ('NES / FC', 'Galaga')], '保留 MAME 的《Galaxian／Galaga》原版组合：固定射击规则、俯冲与双机机制均采用街机基准，FC 两项移植不再重复。')
choice('真·女神转生 I／II', [('SNES / SFC', 'Shin Megami Tensei I / II')], [('PS1', 'Shin Megami Tensei'), ('PS1', 'Shin Megami Tensei II')], '保留 SFC 两作：以原始 16 位迷宫、阵营和恶魔交涉系统为版本基准，PS1 对应移植不再重复；SFC 合集行仍展开计两款。')
choice('真·女神转生 if…', [('SNES / SFC', 'Shin Megami Tensei if...')], [('PS1', 'Shin Megami Tensei if...')], '保留 SFC 原版：学园迷宫、守护灵与多路线结构完整，PS1 移植不再另占容量。')
choice('皇家骑士团 2', [('SNES / SFC', 'Tactics Ogre: Let Us Cling Together')], [('PS1', 'Tactics Ogre: Let Us Cling Together (PlayStation)')], '保留 SFC 原版：网格战棋、法律阵营与职业系统完整，避免 PS1 移植的读取与镜像开销；它不与 PSP 另一部重制作品混名。')
choice('伊苏 I＋II', [('PCE (PC Engine / TurboGrafx-16)', 'Ys Book I & II')], [('PSP', 'Ys I & II Chronicles')], '保留 PCE CD《Book I & II》：两作连续冒险、CD 音画与演出是该版本的历史特色；PSP《Chronicles》合集不再重复。')
choice('伊苏 III', [('PSP', 'Ys: The Oath in Felghana')], [('PCE (PC Engine / TurboGrafx-16)', 'Ys III: Wanderers from Ys')], '在本机可运行候选中优先《菲尔盖纳的誓约》：它以完整重制扩展伊苏 III 的动作与关卡，替代 PCE 旧版；但这是 3D PSP 游戏，N4100 仍须以 1× 渲染实测繁忙场景，不能视为已认证。')
choice('恶魔城 血之轮回／月下', [('PCE (PC Engine / TurboGrafx-16)', 'Akumajou Dracula X: Chi no Rondo / Castlevania: Rondo of Blood'), ('PS1', 'Castlevania: Symphony of the Night')], [('PSP', 'Castlevania: The Dracula X Chronicles')], '分别保留 PCE《血之轮回》和 PS1《月下夜想曲》：直接使用两个原生平台版本；PSP《X 历代记》合集再次包含二者并有 3D 负担，不再重复。SFC《Dracula X》是独立改编，仍保留。')
choice('恶魔城初代', [('PS1', 'Castlevania Chronicles')], [('NES / FC', 'Castlevania')], '保留《Castlevania Chronicles》：以原始／改编两种模式覆盖 X68000 初代的再演绎，作为本库旧式初代路线；FC 对应作不再重复，II／III 与其他原创续作不受影响。')
choice('元祖洛克人 1–3', [('NES / FC', 'Mega Man'), ('NES / FC', 'Mega Man 2'), ('NES / FC', 'Mega Man 3')], [('MD / Genesis', 'Mega Man: The Wily Wars')], '保留 FC 元祖 1–3：原版输入、射速与关卡节奏更直接，也避开《Wily Wars》部分版本的输入延迟和卡顿差异；MD 三合集不再重复。')
choice('最终幻想 I／II', [('GBA', 'Final Fantasy I & II: Dawn of Souls')], [('NES / FC', 'Final Fantasy'), ('NES / FC', 'Final Fantasy II')], '保留 GBA《灵魂黎明》：以完整两作、改良界面和附加内容覆盖 I／II，便携平台运行轻量；FC 两个早期版本不再重复。')
choice('最终幻想 III', [('NDS', 'Final Fantasy III (Nintendo DS)')], [('NES / FC', 'Final Fantasy III')], '保留 NDS 重制：以完整 3D 重制、职业与界面调整覆盖第三作，melonDS 软件渲染即可作为保守起点；FC 原版不再重复。')
choice('最终幻想 IV', [('GBA', 'Final Fantasy IV Advance')], [('SNES / SFC', 'Final Fantasy IV'), ('NDS', 'Final Fantasy IV (Nintendo DS)'), ('WS / WSC', 'Final Fantasy I / II / IV')], '保留 GBA《IV Advance》：在 2D 原作路线中兼顾内容与低模拟负担，不再同时收 SFC、NDS 3D 重制及 WSC 收藏组；WS 组的 I／II 也已由 GBA《灵魂黎明》覆盖。')
choice('最终幻想 V', [('GBA', 'Final Fantasy V Advance')], [('SNES / SFC', 'Final Fantasy V')], '保留 GBA《V Advance》：职业系统主体完整并带追加内容，运行轻量；SFC 原版不再重复。')
choice('最终幻想 VI', [('SNES / SFC', 'Final Fantasy VI')], [('GBA', 'Final Fantasy VI Advance')], '特意保留 SFC 原版：以原生音画、演出和输入节奏为基准，也对应精选改版《Brave New World》的底本；GBA 移植不替代此版本。')
choice('最终幻想战略版', [('PS1', 'Final Fantasy Tactics')], [('PSP', 'Final Fantasy Tactics: The War of the Lions')], '保留 PS1 原版：政治群像、职业与网格战斗完整，避开 PSP《狮子战争》的原生法术减速与音质争议，也继续对应 PS1 精选改版底本。')
choice('勇者斗恶龙 III', [('SNES / SFC', 'Dragon Quest III: The Seeds of Salvation')], [('NES / FC', 'Dragon Quest III: The Seeds of Salvation')], '保留 SFC 重制：以改良音画、界面和平衡覆盖第三作的转职与冒险，运行轻量；FC 原版不再重复。')
choice('勇者斗恶龙 IV', [('NDS', 'Dragon Quest IV: Chapters of the Chosen')], [('NES / FC', 'Dragon Quest IV: Chapters of the Chosen')], '在本机可运行版本中优先 NDS 重制：章节群像、界面与便携操作完整，替代 FC 原版；不同地区版本曾有伙伴对话等差异，所选镜像地区须固定，不宣称它是所有玩家唯一公认的最佳版。')
choice('勇者斗恶龙 V', [('NDS', 'Dragon Quest V: Hand of the Heavenly Bride')], [('SNES / SFC', 'Dragon Quest V: Hand of the Heavenly Bride')], '在本机可运行版本中优先 NDS 重制：世代旅程、怪物同伴和界面内容完整，替代 SFC 原版；双屏按普通 RPG 布局即可，不需高倍率。')
choice('勇者斗恶龙 VI', [('NDS', 'Dragon Quest VI: Realms of Revelation')], [('SNES / SFC', 'Dragon Quest VI: Realms of Revelation')], '在本机可运行版本中优先 NDS 重制：双世界、职业与队伍内容集中在一个低体积版本，替代 SFC 原版；美术和怪物招募改动存在口味差异，因此不把此取舍写成绝对优劣。')
choice('塞尔达 织梦岛', [('GBC', 'The Legend of Zelda: Link’s Awakening DX')], [('GB', 'The Legend of Zelda: Link’s Awakening')], '保留 GBC《DX》：在 GB 原作基础上加入彩色呈现和隐藏迷宫，同一冒险只留这个增强版本。')
choice('圣剑传说初代', [('GBA', 'Sword of Mana')], [('GB', 'Seiken Densetsu: Final Fantasy Gaiden / Final Fantasy Adventure')], '保留 GBA《新约圣剑传说》：以双视角、锻造和重制音画覆盖 GB 初代，避免同一冒险的双版本重复；SFC 后续作品仍是独立续作。')
choice('SaGa 2', [('NDS', 'SaGa 2: Hihou Densetsu – Goddess of Destiny')], [('GB', 'Final Fantasy Legend II / SaGa 2: Hihou Densetsu')], '保留 NDS《命运女神》：以完整重制覆盖《SaGa 2》的秘宝旅程与系统，GB 原版不再重复；其余沙加作品不是这一作的重制。')
choice('密特罗德初代', [('GBA', 'Metroid: Zero Mission')], [('NES / FC', 'Metroid')], '保留 GBA《零点任务》：现代地图、存档与动作系统完整重制初代并追加后日谈，替代 FC 原版；GB 二代与 SFC《超级密特罗德》是独立续作。')
choice('星之卡比 梦之泉', [('GBA', 'Kirby: Nightmare in Dream Land')], [('NES / FC', 'Kirby’s Adventure')], '保留 GBA《梦之泉豪华版》：复制能力、秘密开关与重制音画覆盖 FC 同一作品，并保留多人内容；GB 其他卡比和 GBA《镜之大迷宫》均为独立作品。')
choice('宝可梦 第一世代', [('GBA', 'Pokémon FireRed / LeafGreen')], [('GB', 'Pokémon Red / Green / Blue / Yellow')], '保留 GBA《火红／叶绿》：以第三世代系统重制关都旅程，内容与运行负担适合本库；GB 红绿蓝黄收藏组不再重复，火红／叶绿仍展开计两款。')
choice('宝可梦 第二世代', [('NDS', 'Pokémon HeartGold / SoulSilver')], [('GBC', 'Pokémon Gold / Silver / Crystal')], '保留 NDS《心金／魂银》：城都与关都旅程、跟随系统和较完整内容覆盖第二世代，GBC 金银水晶不再重复；依赖水晶底本的改版也同步移除。')
choice('宝可梦 第三世代', [('GBA', 'Pokémon Emerald')], [('GBA', 'Pokémon Ruby / Sapphire')], '保留《绿宝石》：在同一地区与同一世代中采用整合增强版，红／蓝双版不再另占一组；绿宝石仍是改版《Emerald Rogue》的底本。')
choice('宝可梦 赤／青救助队', [('NDS', 'Pokémon Mystery Dungeon: Blue Rescue Team')], [('GBA', 'Pokémon Mystery Dungeon: Red Rescue Team')], '保留 NDS《青救助队》：与 GBA《赤救助队》共享同一救助队主体，双屏与操作呈现更适合本库；不再为 paired version 各留一份。')
choice('宝可梦 时／暗／空探险队', [('NDS', 'Pokémon Mystery Dungeon: Explorers of Sky')], [('NDS', 'Pokémon Mystery Dungeon: Explorers of Time'), ('NDS', 'Pokémon Mystery Dungeon: Explorers of Darkness')], '保留《空之探险队》：作为时／暗的完整增强版，追加章节与内容，同一探险队故事不再同时保存时、暗两个版本。')
choice('火焰之纹章 初代', [('NDS', 'Fire Emblem: Shadow Dragon')], [('NES / FC', 'Fire Emblem: Shadow Dragon and the Blade of Light')], '保留 NDS《新·暗黑龙与光之剑》：重制初代复国战争并改善界面与操作，FC 原版不再重复；《外传》及其他序号作继续独立保留。')
choice('火焰之纹章 纹章之谜', [('NDS', 'Fire Emblem: New Mystery of the Emblem')], [('SNES / SFC', 'Fire Emblem: Mystery of the Emblem')], '保留 NDS《新·纹章之谜》：以重制内容、主角与界面覆盖 SFC 对应作品，SFC 版不再重复；系谱、多拉基亚和 GBA 三作不受影响。')
choice('第 2 次超级机器人大战', [('PS1', 'Dai-2-Ji Super Robot Taisen (PlayStation)')], [('NES / FC', 'Dai-2-Ji Super Robot Taisen')], '保留 PS1 重制：在第二次机战同一战役主体上采用音画与界面更完整的版本，FC 原作不再重复；其他机战序号作均独立。')
choice('超级机器人大战 A', [('PSP', 'Super Robot Taisen A Portable')], [('GBA', 'Super Robot Taisen A')], '保留 PSP《A Portable》：以重制后的演出、语音和界面覆盖 GBA《A》，本机仍需用原生设置实测战斗动画；GBA 版不再重复。')
choice('逆转裁判 1–3', [('NDS', 'Phoenix Wright: Ace Attorney / Justice for All / Trials and Tribulations (DS)')], [('GBA', 'Gyakuten Saiban / Phoenix Wright: Ace Attorney'), ('GBA', 'Gyakuten Saiban 2 / Phoenix Wright: Ace Attorney – Justice for All'), ('GBA', 'Gyakuten Saiban 3 / Phoenix Wright: Ace Attorney – Trials and Tribulations')], '保留 NDS 三部曲：双屏、触控与追加内容覆盖 GBA 三作，法庭文本和证物界面适合中文版本；收藏组仍展开计三款，GBA 对应作不再重复。')
choice('马力欧 NES 原版与复刻', [('NES / FC', 'Super Mario Bros.'), ('NES / FC', 'Super Mario Bros. 2 (USA)'), ('NES / FC', 'Super Mario Bros. 3'), ('NES / FC', 'Super Mario Bros.: The Lost Levels')], [('SNES / SFC', 'Super Mario All-Stars'), ('GBC', 'Super Mario Bros. Deluxe'), ('GBA', 'Super Mario Advance'), ('GBA', 'Super Mario Advance 4: Super Mario Bros. 3')], '保留 FC 原版 SMB、2 USA、3 与日版 2：以原始手感作为家庭动作基准，并对应两款精选改版底本；All-Stars、GBC DX 与 GBA 复刻不再重复，原版与改版分开存档。')
choice('超级马力欧世界', [('SNES / SFC', 'Super Mario World')], [('GBA', 'Super Mario World: Super Mario Advance 2')], '保留 SFC 原版：关卡、手感与音画采用最初版本，也对应精选 SMW 改版底本；GBA《Advance 2》不再重复。')
choice('耀西岛', [('SNES / SFC', 'Super Mario World 2: Yoshi’s Island')], [('GBA', 'Yoshi’s Island: Super Mario Advance 3')], '保留 SFC 原版：Super FX2 绘制风格、关卡和音画以原版为基准，GBA《Advance 3》不再重复；NDS《Yoshi’s Island DS》是独立续作。')
choice('超级马力欧 64', [('N64', 'Super Mario 64')], [('NDS', 'Super Mario 64 DS')], '保留 N64 原版：原生模拟摇杆更贴合 3D 移动，虽不像 DS 版追加角色与星星，却避免触控／十字键替代摇杆的手感差异；N64 大型改版底本也继续使用此版。')
choice('梦幻模拟战初代', [('SNES / SFC', 'Der Langrisser')], [('MD / Genesis', 'Langrisser')], '保留 SFC《Der Langrisser》：重制 MD 初代并扩展多阵营路线与演出，作为初代的单一版本；MD《Langrisser II》是独立续作，继续保留。')
choice('咚奇刚街机初代', [('MAME', 'Donkey Kong / Donkey Kong Jr.')], [('NES / FC', 'Donkey Kong')], '保留 MAME 的《Donkey Kong／Jr.》街机组合：爬梯、跨锤、拆铆钉与藤蔓关卡采用原始版本，FC 初代移植不再重复；GB 版有百余个扩展解谜关卡，仍作为独立作品保留。')
choice('Darius 初代', [('MAME', 'Darius / Darius II / Darius Gaiden')], [('PCE (PC Engine / TurboGrafx-16)', 'Darius Plus')], '保留 MAME 的 Darius 街机收藏组：初代的区域分支和机械鱼 Boss 采用街机基准，PCE《Darius Plus》的单屏重排不再重复；SFC《Darius Twin》是独立续作。')
choice('心跳回忆初代', [('PS1', 'Tokimeki Memorial 1 / 2')], [('PCE (PC Engine / TurboGrafx-16)', 'Tokimeki Memorial')], '保留 PS1 两作收藏组：初代的学习、社团、约会与角色评价和二代续篇集中管理，PCE 初代移植不再重复；两作仍展开计两款并分别维护存档。')

VERSION_DROP = {}
VERSION_REASON = {}
for item in VERSION_CHOICES:
    assert item['keeps'] and item['drops'] and item['reason'], item['name']
    for key in item['drops']:
        assert key not in VERSION_DROP, f'重复删除规则：{key}'
        assert key not in item['keeps'], f'同一规则既保留又删除：{key}'
        VERSION_DROP[key] = item
    for key in item['keeps']:
        assert key not in VERSION_REASON, f'保留条目有冲突说明：{key}'
        VERSION_REASON[key] = item['reason']

assert not (set(VERSION_DROP) & set(VERSION_REASON)), '保留与删除规则存在交叉'
