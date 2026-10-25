# Batocera 家庭游戏机精选指南

> 适用配置：Intel Celeron N4100＋UHD 600＋4 GB 内存＋Batocera。定位是电视上的家庭游戏机，因此本地合作、双人对战、经典休闲与大作同样占位置。

本清单只覆盖 **MAME、FBNeo、GBA、GBC、GB、GG、WS／WSC、NES／FC、SNES／SFC、MD、PCE、PS1、N64、PSP、Dreamcast、NDS**。筛选依据是平台支持、保守性能范围、作品质量与家庭游玩价值，并非逐款实机测试承诺；合集行是收藏组，不等于一个 ROM。

## 总目录

- [使用规则与硬件边界](#使用规则与硬件边界)
- [平台、硬件与模拟器总览](#平台硬件与模拟器总览)
- [存储、目录与镜像管理](#存储目录与镜像管理)
- [各平台精选清单](#各平台精选清单)
  - [MAME](#platform-mame)
  - [FBNeo](#platform-fbneo)
  - [GBA](#platform-gba)
  - [GBC](#platform-gbc)
  - [GB](#platform-gb)
  - [GG](#platform-gg)
  - [WS / WSC](#platform-ws)
  - [NES / FC](#platform-nes)
  - [SNES / SFC](#platform-snes)
  - [MD / Genesis](#platform-md)
  - [PCE (PC Engine / TurboGrafx-16)](#platform-pce)
  - [PS1](#platform-ps1)
  - [N64](#platform-n64)
  - [PSP](#platform-psp)
  - [Dreamcast](#platform-dc)
  - [NDS](#platform-nds)
- [游戏品类：源流与代表作](#游戏品类源流与代表作)
- [两个深化专题](#两个深化专题)
- [系列专题与平台回链](#系列专题与平台回链)
- [中文化版本与精选非官方改版](#中文化版本与精选非官方改版)
- [三层查漏补缺结果](#三层查漏补缺结果)
- [容量汇总与运行核对](#容量汇总与运行核对)
- [摄像头与麦克风验证附录](#摄像头与麦克风验证附录)

---

## 使用规则与硬件边界

1. **名字分两列。** 完整商品名采用英文或日文，中文译名只辅助识别；同一游戏的地区版、复刻和重制不互相冒充。
2. **日期采用首发年份或合集年份范围。** 合集行明确标注范围，避免把不同作品伪装成一个日期；发行商采用该版本的主要历史发行主体，不用今天的公司名倒填。
3. **容量是预留预算，不是实测 ROM 大小。** CHD、CSO、音轨、多盘与地区版都会改变占用，安装后以实际文件为准。
4. **不保留差作凑数。** 只有系列史或版本比较确有必要的旧作才作为严格例外，并在备注说明；外设依赖、后期高负载街机和低评价移植不占位置。
5. **不纳入 Xbox、PS2、PS3、PS4、GameCube、Wii。** Batocera 虽提供 xemu 的 Xbox 入口，但 N4100＋UHD 600＋4 GB 不适合作为稳定可玩的 Xbox 库，因此这里明确不设 Xbox 章节。
6. **合法备份。** 只使用自己合法拥有的游戏与 BIOS，不提供下载，不把 hack、民间改版或虚构商品当正式发行作。

---

## 平台、硬件与模拟器总览

核心名称是 Batocera 常见选项，实际可用项随安装版本变化；先用轻量核心和原生设置，再针对单作调整，不为所有游戏套同一个“优化配置”。

| 平台 | 位数／架构 | 发布时间 | 发布商 | 主要特点 | 对应模拟器／核心 | 特别配置 |
|---|---|---:|---|---|---|---|
| MAME | 多种 8／16／32 位街机 | 1970 年代末起 | 多厂商 | 早期迷宫、单屏、Taito／Namco／Sega 硬件 | MAME（当前 Batocera 核心） | ROM set 必须与核心匹配；ZIP 不改名、不解压；BIOS／CHD 依赖完整 |
| FBNeo | 多种 16／32 位 2D 街机 | 1980 年代末起 | Capcom／SNK／IGS 等 | CPS、Neo Geo、PGM、Toaplan 等 | FinalBurn Neo（libretro） | Neo Geo／PGM BIOS 随匹配 ROM set；NAOMI 不放入此目录 |
| GBA | 32 位 | 2001 | Nintendo | ARM 掌机，2D 动作与 RPG 丰富 | mGBA（libretro） | 默认即可；核对 RTC、存档类型；Boktai 与转转瓦力欧需传感器映射 |
| GBC | 8 位 | 1998 | Nintendo | 彩色掌机，兼容部分 GB 黑卡 | Gambatte／SameBoy | GBC 与 GB 分目录；双版本联动密码属于游戏内功能 |
| GB | 8 位 | 1989 | Nintendo | 单色便携，长续航与经典短局 | Gambatte／SameBoy | 用 GB 调色板，不把 GBC 专用卡误放入 GB；联机按核心支持 |
| GG | 8 位 | 1990 | Sega | Master System 相近架构的彩色掌机 | Genesis Plus GX／Gearsystem | 小屏视野与原版一致；整数缩放，不要误用 MD ROM |
| WS／WSC | 16 位 | 1999／2000 | Bandai | 横竖双持、低功耗、原创益智与掌机衍生 | Beetle Cygne／Beetle Wswan | Gunpey 等按游戏旋转画面与按键；WS、WSC 目录可分开 |
| NES／FC | 8 位 | 1983 | Nintendo | 家用卷轴动作与早期 JRPG，含 FDS | Mesen／Nestopia／FCEUmm | FDS 需 disksys.rom；核对 Mapper、地区制式与汉化改版 Mapper |
| SNES／SFC | 16 位 | 1990 | Nintendo | Mode 7、丰富音源、特殊增强芯片 | Snes9x（轻量优先）／bsnes | 特殊芯片逐作核对；Star Fox 2 用正式发行版；高画质 bsnes 更耗资源 |
| MD／Genesis | 16 位 | 1988 | Sega | 高速 2D、FM 音源、街机风格 | Genesis Plus GX | 六键手柄用于街霸等；Sonic 3 & Knuckles 用锁合镜像；核对地区 |
| PCE | 8 位 CPU＋16 位图形 | 1987 | NEC／Hudson Soft | HuCard 与 CD‑ROM²，射击和 CD 音画突出 | Beetle PCE Fast／Beetle PCE | CD 需对应 syscard BIOS；Arcade Card 游戏单独验证；CHD 保留音轨 |
| PS1 | 32 位 | 1994 | Sony | CD 光盘、预渲染背景与早期 3D | DuckStation／PCSX‑ReARMed | 原生分辨率起步；多盘 M3U；记忆卡与 BIOS 校验，不开高负载增强 |
| N64 | 64 位 | 1996 | Nintendo | 3D 平台与四人本地对战，部分用 Expansion Pak | Mupen64Plus‑Next | 按游戏选 GLideN64／Rice；Expansion Pak 游戏核对内存；重负载场景测帧 |
| PSP | 32 位 | 2004 | Sony | 宽屏便携、UMD、2D 与大型 3D 并存 | PPSSPP | 1× 渲染、保留缓冲渲染；ISO 为兼容基线；逐作验证，不用统一跳帧掩盖卡顿 |
| Dreamcast | 32 位 | 1998 | Sega | GD‑ROM、NAOMI 同源、2D 格斗与 3D 原创 | Flycast | 原生分辨率起步；DC 与 NAOMI 分开；核对 GDI／CHD、区域和 VGA 选项 |
| NDS | 双 32 位 ARM | 2004 | Nintendo | 双屏、触控、麦克风与本地无线 | melonDS（软件渲染优先） | 配置竖屏／横屏布局与触控；存档类型、麦克风按游戏检查，不开高倍率 |

---

## 存储、目录与镜像管理

### 存储分工

| 位置 | 内容 | 原则 |
|---|---|---|
| eMMC 独立 ext4 分区 | NES、GB、GBC、GBA、GG、WS／WSC、MD、SNES、PCE、N64、FBNeo／MAME 小 ROM | 小体积顺序读取，目录级软链接，不做 mergerfs |
| SSD `/userdata` | PS1、PSP、Dreamcast、PCE CD、NDS，以及全部存档、配置、缓存与刮削 | 大镜像和写入集中，避免挤占 eMMC |

```bash
mkdir -p /mnt/emmc/roms/{nes,gb,gbc,gba,gg,wswan,wswanc,megadrive,snes,n64,pcengine,fbneo,mame}
# 先确认目标路径不存在；不要覆盖已有实体目录
ln -s /mnt/emmc/roms/gb /userdata/roms/gb
ln -s /mnt/emmc/roms/gbc /userdata/roms/gbc
ln -s /mnt/emmc/roms/gg /userdata/roms/gg
ln -s /mnt/emmc/roms/wswan /userdata/roms/wswan
ln -s /mnt/emmc/roms/wswanc /userdata/roms/wswanc
ln -s /mnt/emmc/roms/fbneo /userdata/roms/fbneo
ln -s /mnt/emmc/roms/mame /userdata/roms/mame
```

先用 `blkid`、`lsblk` 核对实际设备并手工验证挂载，不要照抄设备名。其余小平台可按同样方式链接；存档和配置始终留在 `/userdata`。

- **街机按 ROM set 管理。** FBNeo 放 `/userdata/roms/fbneo`，MAME 放 `/userdata/roms/mame`；ZIP 不随意改名或解压，Neo Geo、PGM 等依赖文件随匹配 ROM set 配置。
- **BIOS 以本机检查为准。** 用 Batocera 的 BIOS 检查、`batocera-systems` 和当前版本文档确认，不用旧网络清单替代。
- **PS1／PCE CD 可用 CHD，多盘配 M3U；DC 按核心选 CHD 或 GDI。** 转换前保留原镜像。PSP 以 ISO 作兼容基线，CSO 是否合适按游戏测试。
- **家庭游玩先测操作。** 核对多手柄分配、存档、双人画面与热键；触控、陀螺仪、阳光传感器和专用外设作品会在备注中说明。

官方依据：[Batocera Arcade Guide](https://wiki.batocera.org/arcade)、[Advanced arcade emulation](https://wiki.batocera.org/advanced_arcade)、[Add games/BIOS files](https://wiki.batocera.org/add_games_bios)、[Xbox 系统说明](https://wiki.batocera.org/systems:xbox)。

---

## 各平台精选清单

### MAME

<a id="platform-mame"></a>

早期 Namco、Taito、Nintendo、Sega 等 2D 街机。与 FBNeo 分目录管理，ROM set 必须匹配 Batocera 当前核心；这里不列后期 PC 基板与光枪依赖作品。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="mame-001"></a>MAME-001 | Bubble Bobble / Rainbow Islands | 泡泡龙／彩虹岛 | 1986 | Taito | 40MB | 平台动作／横版／单屏／3D 平台 | 泡泡龙以吐泡封敌并戳破，彩虹岛改用可站立、可攻击的彩虹开路。两款共享角色但玩法不同。 [系列专题](#series-57)。 |
| <a id="mame-002"></a>MAME-002 | KiKi KaiKai | 奇奇怪界 | 1986 | Taito | 40MB | 动作冒险／探索／解谜／文字冒险 | 巫女小夜用御札与驱魔棒对抗妖怪，俯视移动射击与关卡分支结合。Taito 把日本民俗做成了轻松但高难度的街机动作。 |
| <a id="mame-003"></a>MAME-003 | Elevator Action / Elevator Action Returns | 电梯大战1/2 | 1983 | Taito | 40MB | 动作冒险／探索／解谜／文字冒险 | 初代用电梯、门和射击潜入大楼窃取文件；Returns 扩展为三人角色、武器与更复杂关卡。两作相隔多年，体现从单屏谍报到清版射击的演变。 |
| <a id="mame-004"></a>MAME-004 | Chase HQ | Chase HQ | 1988 | Taito | 40MB | 动作冒险／探索／解谜／文字冒险 | 驾驶警车追捕逃逸车辆，在倒计时内追尾撞击并逼停目标。伪 3D 道路、车辆加速和任务节奏让它成为 Taito 追逐竞速代表。 |
| <a id="mame-005"></a>MAME-005 | Space Invaders | 太空侵略者 | 1978 | Taito | 20MB | 射击／卷轴与弹幕射击 | 左右移动炮台，利用掩体抵挡并逐行消灭会加速下降的外星阵列。固定屏幕、逐步提速和 UFO 奖励奠定射击史起点。 |
| <a id="mame-006"></a>MAME-006 | Darius / Darius II / Darius Gaiden | 太空战斗机 I／II／外传 | 1986 | Taito | 100MB | 射击／卷轴与弹幕射击 | 初代以三屏宽视野和分支区域定型，II 改为双屏并扩展路线，Gaiden 加入捕获球与更强得分系统。三者应按独立 ROM 管理。 [系列专题](#series-49)。 |
| <a id="mame-007"></a>MAME-007 | The Ninja Warriors | 忍者战士 | 1987 | Taito | 40MB | 动作冒险／探索／解谜／文字冒险 | 两名机器忍者以近身斩击抵御敌军，攻击时移动受限，站位比连续乱按更重要。街机三屏版以宽阔画面呈现反乌托邦战场。 |
| <a id="mame-008"></a>MAME-008 | Rastan | Rastan | 1987 | Taito | 40MB | 平台动作／横版／单屏／3D 平台 | 野蛮人战士用剑与魔法穿越奇幻关卡，跳台、武器取舍和 Boss 战并重。它是 Taito 早期横版动作代表，后来家用移植各有删改。 |
| <a id="mame-009"></a>MAME-009 | Metal Black | Metal Black | 1991 | Taito | 40MB | 射击／卷轴与弹幕射击 | 以光束和释放 Newalone 能量形成攻防切换，敌我双方都争夺能量。Taito 用暗色科幻与大型生物 Boss 营造独特氛围。 |
| <a id="mame-010"></a>MAME-010 | Altered Beast | 兽王记 | 1988 | Sega | 40MB | 格斗／清版动作／清版动作与合作 | 兽王记通过收集能量球逐步变身为狼人等形态，横向清版节奏直接。它曾是 MD 早期同捆作品，品牌形象意义高于系统复杂度。 |
| <a id="mame-011"></a>MAME-011 | Space Harrier | 太空哈利 | 1985 | Sega | 40MB | 射击／卷轴与弹幕射击 | 在 Super Scaler 伪 3D 棋盘中高速前进，闪避柱体与弹幕并射击大型幻想 Boss。移动反馈和速度感比武器构筑更重要。 |
| <a id="mame-012"></a>MAME-012 | Fantasy Zone | Fantasy Zone | 1986 | Sega | 20MB | 射击／卷轴与弹幕射击 | Opa-Opa 可在左右自由卷轴的平面往返，击毁基地后挑战 Boss，金币可进商店购买引擎和武器。 |
| <a id="mame-013"></a>MAME-013 | Out Run | OutRun | 1986 | Sega | 40MB | 竞速／体育／竞速与驾驶 | 驾驶敞篷车在倒计时内通过检查点，并在岔路选择不同风景与终点。它更像公路驾驶体验，而非圈速拟真。 |
| <a id="mame-014"></a>MAME-014 | After Burner II | 冲破火网 II | 1987 | Sega | 40MB | 射击／卷轴与弹幕射击 | 驾驶 F-14 在高速伪 3D 空战中锁定敌机、发射导弹并调整油门。它是 After Burner 的加速修订版，重点在体感节奏。 |
| <a id="mame-015"></a>MAME-015 | Super Monaco GP | Super Monaco GP | 1989 | Sega | 40MB | 竞速／体育／竞速与驾驶 | 以 F1 街道赛、档位和湿地变化构成计时竞速，街机原版还有不同机台形式。它是赛车，不应套用球类运动备注。 |
| <a id="mame-016"></a>MAME-016 | Hang-On | Hang-On | 1985 | Sega | 20MB | 竞速／体育／竞速与驾驶 | 以 Super Scaler 伪 3D 呈现摩托公路赛，压弯、避让车流与检查点构成短局。它奠定 Sega 体感街机传统。 |
| <a id="mame-017"></a>MAME-017 | Thunder Blade | Thunder Blade | 1987 | Sega | 40MB | 动作冒险／探索／解谜／文字冒险 | 直升机在纵版俯视与第三人称纵深场景间切换，机枪和导弹处理多层目标。Sega 的 Super Scaler 演出是主要特色。 |
| <a id="mame-018"></a>MAME-018 | Pac-Man / Ms. Pac-Man | 吃豆人／吃豆人小姐 | 1980–1982 | Namco / Midway | 2MB | 平台动作／横版／单屏／3D 平台 | 吃豆人以迷宫路线、四鬼不同追踪行为和能量豆反击构成规则；吃豆人小姐加入多迷宫与移动水果。两作共同奠定街机迷宫追逐范式。 |
| <a id="mame-019"></a>MAME-019 | Donkey Kong / Donkey Kong Jr. | 咚奇刚／咚奇刚 Jr. | 1981–1982 | Nintendo | 2MB | 平台动作／横版／单屏／3D 平台 | 初代以爬梯、跨锤和拆铆钉救人为目标，Jr. 则改为藤蔓攀爬与钥匙机关。两作相隔一年，共同确立任天堂早期角色与关卡设计。 [系列专题](#series-01)。 |
| <a id="mame-020"></a>MAME-020 | Galaga / Galaxian | 大蜜蜂／小蜜蜂 | 1979–1981 | Namco | 2MB | 射击／卷轴与弹幕射击 | Galaxian 以编队俯冲革新固定射击，Galaga 再加入 Boss 捕获、双机火力与挑战关。两款是独立商品。 |
| <a id="mame-021"></a>MAME-021 | Dig Dug | 打气人 | 1982 | Namco | 2MB | 平台动作／横版／单屏／3D 平台 | 在地下挖洞，用打气泵让敌人膨胀爆裂，也可诱使落石压敌。地形由玩家改变，风险路线与高分策略相连。 |
| <a id="mame-022"></a>MAME-022 | Snow Bros.: Nick & Tom | 雪人兄弟 | 1990 | Toaplan | 4MB | 平台动作／横版／单屏／3D 平台 | 固定单屏中把敌人滚成雪球并推动连锁撞击，双人可协作也可争抢得分。它是街机时代合家欢动作的代表，规则直观但隐藏道具与高分路线很有深度。 |
| <a id="mame-023"></a>MAME-023 | Puyo Puyo Sun | 噗哟噗哟 SUN | 1996 | Compile / Sega | 64MB | 益智／休闲／落块与消除 | 在连锁对战上加入太阳噗哟，消除它们可向对手发送更强干扰。街机原版使用 ST-V，归入 MAME 而非假设所有版本都属于 FBNeo。 [系列专题](#series-88)。 |

---

### FBNeo

<a id="platform-fbneo"></a>

CPS、Neo Geo、PGM、Toaplan 等成熟 2D 街机内容，重点是合作、对战、射击与休闲短局。NAOMI 不混放这里，Model 2／3 和后期音游也不为凑数收录。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="fbneo-001"></a>FBNEO-001 | Knights of Valour Plus | 三国战纪：正宗 Plus | 1999–2003 | IGS | 100MB | 格斗／清版动作／清版动作与合作 | IGS 将三国武将做成多人清版动作，援军令、道具、分支和隐藏角色形成重复攻略。Plus 是正式修订版本，不与玩家改版混淆。 [系列专题](#series-05)。 |
| <a id="fbneo-002"></a>FBNEO-002 | Knights of Valour: Super Heroes | 三国战纪风云再起 | 1999–2003 | IGS | 100MB | 格斗／清版动作／清版动作与合作 | 在原版阵容与系统上调整角色、招式和宝物流程，强调多人配合与高分路线。它与 Plus、二代及后期七星转生应按基板和 ROM set 分开。 [系列专题](#series-05)。 |
| <a id="fbneo-003"></a>FBNEO-003 | Warriors of Fate / Tenchi wo Kurau II | 吞食天地2赤壁之战 | 1992 | Capcom | 80MB | 格斗／清版动作／清版动作与合作 | 以蜀汉武将骑马与步战推进，武器、马术、抓取和多人合体构成战斗。它是 Capcom 吞食天地 II 街机清版，不是光荣战略游戏。 [系列专题](#series-05)。 |
| <a id="fbneo-004"></a>FBNEO-004 | Oriental Legend | 西游释厄传 | 2007 | IGS | 80MB | 格斗／清版动作／清版动作与合作 | IGS 以西游记为题材制作清版动作，角色法术、道具与合体技支撑多人合作。五行和法宝系统使其区别于普通拳脚街机。 |
| <a id="fbneo-005"></a>FBNEO-005 | Oriental Legend Super | 西游释厄传 Super | 1999–2003 | IGS | 80MB | 格斗／清版动作／清版动作与合作 | 在原版基础上调整角色招式、敌群与宝物系统，让连招和多人配合更突出。它是正式街机修订作，不与玩家魔改混同。 |
| <a id="fbneo-006"></a>FBNEO-006 | Oriental Legend: Qun Mo Luan Wu | 西游释厄传群魔乱舞 | 1999–2003 | IGS | 80MB | 格斗／清版动作／清版动作与合作 | 扩展角色与招式并调整关卡节奏，是西游释厄传后期街机版本。收藏时应与 Oriental Legend 2 分开，后者使用不同硬件。 |
| <a id="fbneo-007"></a>FBNEO-007 | Cadillacs and Dinosaurs | 恐龙快打 | 1993 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 四名角色在恐龙与盗猎者冲突中使用枪械、载具和连段，弹药与多人配合改变战局。Capcom 的改编保留漫画奇想。 |
| <a id="fbneo-008"></a>FBNEO-008 | Captain Commando | 名将Captain Commando | 1991 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 四名未来英雄可使用机械坐骑和协同攻击，在都市与太空场景清版。角色动作差异和 Boss 演出是 CPS 代表作。 |
| <a id="fbneo-009"></a>FBNEO-009 | Knights of the Round | 圆桌骑士 | 1991 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 亚瑟、兰斯洛特与珀西瓦尔以格挡、升级装备和骑马作战，攻防节奏偏刀剑而非纯拳脚。 |
| <a id="fbneo-010"></a>FBNEO-010 | The Punisher | 惩罚者The Punisher | 1993 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 惩罚者与尼克·弗瑞以近战、投掷和有限枪支打击犯罪，双人配合与场景破坏增强漫画感。 |
| <a id="fbneo-011"></a>FBNEO-011 | Final Fight | 快打旋风Final Fight | 1989 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 科迪、哈格与盖以拳脚、投技和武器对抗疯狂齿轮，敌群管理比单人连招更重要。SFC 初版缺双人且阵容不完整，街机版才是合作基准。 [系列专题](#series-43)。 |
| <a id="fbneo-012"></a>FBNEO-012 | Guardians / Denjin Makai II | 电精1 | 1995 | Banpresto | 60MB | 格斗／清版动作／清版动作与合作 | 多名角色拥有丰富连段、投技与特殊攻击，敌我动画夸张。Banpresto 的电神魔鬼 II 以动作深度在清版游戏中突出。 |
| <a id="fbneo-013"></a>FBNEO-013 | Denjin Makai | 电精2 | 1993 | Banpresto | 60MB | 格斗／清版动作／清版动作与合作 | 初代电精以科幻城市、能量攻击和多角色招式展开，和续作 Guardians 的关卡及系统不同。中文圈曾长期使用不同译名。 |
| <a id="fbneo-014"></a>FBNEO-014 | Night Slashers | 午夜杀生Night Slashers | 1994 | Data East | 60MB | 格斗／清版动作／清版动作与合作 | 猎魔角色用拳脚和特殊技对抗僵尸、狼人与吸血鬼，恐怖题材在清版游戏中少见。三名角色拥有不同连段。 |
| <a id="fbneo-015"></a>FBNEO-015 | Battle Circuit | Battle Circuit | 1997 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 赏金猎人四人组以丰富连段、角色升级和 Battle Download 能力攻关，Capcom 后期 CPS II 动作系统较成熟。 |
| <a id="fbneo-016"></a>FBNEO-016 | Armored Warriors | 装甲勇士 | 1994 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 可更换机甲双臂、腿部与武器，击落部件还能为己所用；多人合体和机甲构筑是核心。 |
| <a id="fbneo-017"></a>FBNEO-017 | Dungeons & Dragons: Tower of Doom | 龙与地下城：毁灭之塔 | 1993 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | Capcom 把 D&D 做成清版动作，加入分支路线、商店、法术与角色成长。多人合作和职业差异使它比普通街机闯关更像冒险。 |
| <a id="fbneo-018"></a>FBNEO-018 | Dungeons & Dragons: Shadow over Mystara | 龙与地下城：暗黑秘影 | 1996 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 延续毁灭之塔并增加装备、隐藏路线与更丰富法术，重玩时角色构筑差异明显。它是街机清版与 RPG 融合的高峰。 |
| <a id="fbneo-019"></a>FBNEO-019 | Alien vs. Predator | 异形大战铁血战士 | 1994 | Capcom | 60MB | 动作冒险／探索／解谜／文字冒险 | Capcom 用三人合作清版动作改编电影设定，人类与铁血战士拥有不同武器和连段。异形群与大型 Boss 的动画表现突出。 |
| <a id="fbneo-020"></a>FBNEO-020 | Three Wonders | 三个奇迹 | 1991 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 一张卡带包含横版动作 Midnight Wanderers、射击 Chariot 与益智 Don’t Pull 三种游戏。它本身就是官方多类型合集。 |
| <a id="fbneo-021"></a>FBNEO-021 | The King of Dragons | 龙王战士 | 1991 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 战士、法师、牧师等职业在奇幻关卡升级，装备成长与多人合作让它接近轻量 RPG 清版。 |
| <a id="fbneo-022"></a>FBNEO-022 | Magic Sword: Heroic Fantasy | 魔法剑 | 1990 | Capcom | 60MB | 格斗／清版动作／清版动作与合作 | 勇者与可营救同伴协作攀登龙塔，门锁、分支和伙伴职业改变攻略。Capcom 将清版动作与轻量 RPG 探索结合。 |
| <a id="fbneo-023"></a>FBNEO-023 | Sengoku 3 / Sengoku Denshou 2001 | 战国传承3 | 2001 | SNK | 60MB | 格斗／清版动作／清版动作与合作 | SNK 的战国传承第三作以现代忍者对抗亡灵，角色切换、连击与分身系统让动作更流畅。正式英文名和年份标题需同时识别。 |
| <a id="fbneo-024"></a>FBNEO-024 | Martial Masters | 形意拳 | 2001 | IGS | 40MB | 动作冒险／探索／解谜／文字冒险 | IGS 以清末武林为背景，多名角色拥有不同架势、连段和招式取消。PGM 的动画与对战深度使其兼具闯关和格斗趣味。 |
| <a id="fbneo-025"></a>FBNEO-025 | The Killing Blade | 傲剑狂刀 | 1998 | IGS | 60MB | 动作冒险／探索／解谜／文字冒险 | 以兵器格斗和多名武侠角色为核心，强调连段、怒气与招式派生。IGS 的系统接近格斗游戏，而不是普通清版动作。 |
| <a id="fbneo-026"></a>FBNEO-026 | The King of Fighters 94 | 拳皇94 | 1994 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 系列首作确立三人组队与跨国队伍编排，以 Rugal 为最终对手。 [系列专题](#series-68)。 |
| <a id="fbneo-027"></a>FBNEO-027 | The King of Fighters 95 | 拳皇95 | 1995 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 引入自由组队与八神庵，草薙京与八神的对抗开始成为长期主线。 [系列专题](#series-68)。 |
| <a id="fbneo-028"></a>FBNEO-028 | The King of Fighters 96 | 拳皇96 | 1996 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 重做移动、紧急回避与跳跃系统，神乐千鹤和高尼茨推动大蛇篇。 [系列专题](#series-68)。 |
| <a id="fbneo-029"></a>FBNEO-029 | The King of Fighters 97 | 拳皇97 | 1997 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 大蛇篇收束，指令速度和简易操作使它在街机厅传播极广。 [系列专题](#series-68)。 |
| <a id="fbneo-030"></a>FBNEO-030 | The King of Fighters 98 | 拳皇98 | 1997 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 无剧情的梦幻对战合集，平衡与角色阵容成熟，是长期比赛常用版本。 [系列专题](#series-68)。 |
| <a id="fbneo-031"></a>FBNEO-031 | The King of Fighters 99 | 拳皇99 | 1997 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 开启 NESTS 篇并加入援护系统，K′ 取代旧主角位置。 [系列专题](#series-68)。 |
| <a id="fbneo-032"></a>FBNEO-032 | The King of Fighters 2000 | 拳皇2000 | 2000 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 延续 NESTS 篇与援护机制，库拉等角色加入，队伍构筑更依赖援护选择。 [系列专题](#series-68)。 |
| <a id="fbneo-033"></a>FBNEO-033 | The King of Fighters 2001 | 拳皇2001 | 2001 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 可在出战与援护间分配四人名额，队伍编成自由但平衡评价分化。 [系列专题](#series-68)。 |
| <a id="fbneo-034"></a>FBNEO-034 | The King of Fighters 2002 | 拳皇2002 | 2002 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 回归无剧情三人梦幻战与 ABC 连招系统，角色多、对战节奏直接。 [系列专题](#series-68)。 |
| <a id="fbneo-035"></a>FBNEO-035 | The King of Fighters 2003 | 拳皇2003 | 2003 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 采用可换人三对三与多路线 Boss，开启 Ash 篇，也是 Atomiswave 之前最后一部编号作。 [系列专题](#series-68)。 |
| <a id="fbneo-036"></a>FBNEO-036 | Samurai Shodown II | 真侍魂：霸王丸地狱变 | 1993 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 加入武器破坏技与更完整角色阵容，以重击威慑、弹刀和距离控制成为系列最流行的一作。 [系列专题](#series-34)。 |
| <a id="fbneo-037"></a>FBNEO-037 | Samurai Shodown | 侍魂1 | 1993 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 系列首作以刀剑重击、武器脱手和道具投掷区别于拳脚格斗，节奏更强调读招。 [系列专题](#series-34)。 |
| <a id="fbneo-038"></a>FBNEO-038 | Samurai Shodown III: Blades of Blood | 侍魂3 | 1995 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 以修罗／罗刹两种风格区分动作和连招，整体色调与人物路线更阴沉。它不是二代，不能使用武器破坏技通稿概括。 [系列专题](#series-34)。 |
| <a id="fbneo-039"></a>FBNEO-039 | Samurai Shodown IV: Amakusa’s Revenge | 侍魂4 | 1996 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 加入连斩与自裁等机制，天草四郎时贞再次成为核心，节奏和演出区别于 II。 [系列专题](#series-34)。 |
| <a id="fbneo-040"></a>FBNEO-040 | Samurai Shodown V | 侍魂零 | 2003 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 加入剑气槽与一撃必杀相关机制，阵容加入新角色，在旧 2D 体系中调整攻防资源。 [系列专题](#series-34)。 |
| <a id="fbneo-041"></a>FBNEO-041 | The Last Blade | 月华剑士1 | 1997 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 以幕末剑士、剑质“力／技”和弹反构成刀剑格斗，重击与连段路线随剑质变化。场景和人物命运带有强烈时代悲剧感。 [系列专题](#series-34)。 |
| <a id="fbneo-042"></a>FBNEO-042 | The Last Blade 2 | 月华剑士2 | 1998 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 增加“极”剑质、隐藏角色与更细攻防调整，天野漂等人物推动黄龙与地狱门故事。系统完整度使其成为系列代表作。 [系列专题](#series-34)。 |
| <a id="fbneo-043"></a>FBNEO-043 | Fatal Fury: King of Fighters | 饿狼传说1 | 1991 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 初代以饿狼传说主线、双线和双人合作战役区别于街霸，只有特瑞、安迪、东丈可用于故事。系统后来才全面开放。 [系列专题](#series-33)。 |
| <a id="fbneo-044"></a>FBNEO-044 | Fatal Fury 2 | 饿狼传说2 | 1992 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 双线场地、安迪、东丈与不知火舞等阵容奠定饿狼特色，威力技和线移动形成立体立回。MD 移植与 Neo Geo 原版在画面、速度上不同。 [系列专题](#series-33)。 |
| <a id="fbneo-045"></a>FBNEO-045 | Fatal Fury 3: Road to the Final Victory | 饿狼传说3 | 1995 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 改为三平面与更复杂的线移动，加入新角色和战斗评分。系统实验性较强，Real Bout 随后做了重构。 [系列专题](#series-33)。 |
| <a id="fbneo-046"></a>FBNEO-046 | Real Bout Fatal Fury | 饿狼传说 Real Bout | 1995 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 简化线系统并加入场地边界、Power 管理和更直接连段，吉斯再次成为剧情核心。它是对 Fatal Fury 3 路线的修正。 [系列专题](#series-33)。 |
| <a id="fbneo-047"></a>FBNEO-047 | Real Bout Fatal Fury Special | 饿狼传说 Real Bout Special | 1997 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 扩展角色阵容并引入旧作人物，保留 Real Bout 的高速攻防。它与 Real Bout 2 是不同后续分支。 [系列专题](#series-33)。 |
| <a id="fbneo-048"></a>FBNEO-048 | Art of Fighting | 龙虎之拳1 | 1992 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 以气力槽限制必杀、超必杀与挑衅削气构成攻防，坂崎良与罗伯特拯救百合。双人故事与奖励关体现早期 SNK 特色。 [系列专题](#series-33)。 |
| <a id="fbneo-049"></a>FBNEO-049 | Art of Fighting 2 | 龙虎之拳2 | 1994 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 扩大可选阵容，加入更明确心理战与气力管理，年轻吉斯成为最终挑战。高难度与角色背景后来汇入拳皇。 [系列专题](#series-33)。 |
| <a id="fbneo-050"></a>FBNEO-050 | World Heroes Perfect | 世界英雄 Perfect | 1995 | Alpha Denshi | 60MB | 格斗／清版动作／一对一与场地格斗 | 集结历史人物的时空格斗，取消旧作部分复杂机制并强化连招与英雄技。它是 ADK 世界英雄系列较成熟的一作。 |
| <a id="fbneo-051"></a>FBNEO-051 | Kizuna Encounter: Super Tag Battle / Fu’un Super Combo | 风云默示录1 | 1996 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 两名角色可随时换人，武器格斗与连段围绕标签节奏展开。它是风云默示录续作，不是魂斗罗。 [系列专题](#series-69)。 |
| <a id="fbneo-052"></a>FBNEO-052 | Savage Reign | 风云默示录2 | 1995 | SNK | 80MB | 格斗／清版动作／一对一与场地格斗 | 以两层场地切换、武器与远程攻击构成 SNK 格斗，角色造型夸张。与续作 Kizuna Encounter 的双人组队规则不同。 [系列专题](#series-69)。 |
| <a id="fbneo-053"></a>FBNEO-053 | Galaxy Fight | Galaxy Fight | 1995 | Sunsoft | 60MB | 格斗／清版动作／一对一与场地格斗 | 太阳软早期 3D 多边形场景上的 2D 格斗，场地近乎无边界，强调追击和投射物。其开放式移动在当时很特殊。 |
| <a id="fbneo-054"></a>FBNEO-054 | Kizuna Encounter | Kizuna Encounter | 1996 | SNK | 60MB | 格斗／清版动作／一对一与场地格斗 | 双人标签、武器和场地攻击可随时联动，连段与换人是核心。它是风云默示录的续作，不属于魂斗罗。 [系列专题](#series-69)。 |
| <a id="fbneo-055"></a>FBNEO-055 | Windjammers | Windjammers | 2002 | Data East | 40MB | 竞速／体育／体育与运动 | 以飞盘投掷、弧线球和超级射门在六格场地对战，攻防转换接近格斗与体育结合。Neo Geo 双人对局尤其经典。 |
| <a id="fbneo-056"></a>FBNEO-056 | Neo Turf Masters | Neo Turf Masters | 1996 | SNK | 40MB | 竞速／体育／体育与运动 | 点击式选杆、风向与球场地形结合，击球节奏快而不牺牲策略。它是 Neo Geo 上最受认可的高尔夫作品之一。 |
| <a id="fbneo-057"></a>FBNEO-057 | Twinkle Star Sprites | Twinkle Star Sprites | 1996 | SNK | 40MB | 益智／休闲／规则解谜与短局 | 纵版射击与对战益智结合，连锁击破敌人会向对手发送干扰和 Boss。双人攻防转换比单纯躲弹更重要。 |
| <a id="fbneo-058"></a>FBNEO-058 | Street Fighter II: The World Warrior | 街头霸王2 | 1991 | Capcom | 40MB | 格斗／清版动作／一对一与场地格斗 | 八名角色与四天王构成基础阵容，搓招、对空、距离与连段偶然形成现代格斗语法。它是 1991 年原版，不含冠军版四天王可操作规则。 [系列专题](#series-31)。 |
| <a id="fbneo-059"></a>FBNEO-059 | Street Fighter II: Hyper Fighting | 街头霸王 II：Hyper Fighting | 1992 | Capcom | 40MB | 格斗／清版动作／一对一与场地格斗 | 在冠军版基础上显著提速，开放四天王并调整角色招式。高速立回使其成为街机厅重要版本，但不是加入超级必杀的 Super Turbo。 [系列专题](#series-31)。 |
| <a id="fbneo-060"></a>FBNEO-060 | Super Street Fighter II Turbo | 超级街头霸王 II Turbo | 1994 | Capcom | 40MB | 格斗／清版动作／一对一与场地格斗 | 加入超级必杀槽、受身等调整及隐藏豪鬼，兼顾完整角色阵容和高压立回。它长期是街机比赛与高水平对战代表。 [系列专题](#series-31)。 |
| <a id="fbneo-061"></a>FBNEO-061 | Street Fighter Alpha: Warriors’ Dreams | 少年街霸 Alpha | 1995 | Capcom | 60MB | 格斗／清版动作／一对一与场地格斗 | 以卡通画风和前传阵容重启体系，加入连锁、Alpha Counter 与空中防御。它和 II 的朴素立回不同，超级槽分为多级。 [系列专题](#series-31)。 |
| <a id="fbneo-062"></a>FBNEO-062 | Street Fighter Alpha 2 | 少年街霸 Alpha 2 | 1996 | Capcom | 60MB | 格斗／清版动作／一对一与场地格斗 | 以 Alpha Counter、Custom Combo 和更鲜明角色阵容发展少年街霸，SFC 移植在画面与载入上做了硬件妥协。 [系列专题](#series-31)。 |
| <a id="fbneo-063"></a>FBNEO-063 | Street Fighter Alpha 3 | 少年街霸 Alpha 3 | 1998 | Capcom | 60MB | 格斗／清版动作／一对一与场地格斗 | 以 X／A／V-ISM 区分经典、标准与自定义连段路线，角色阵容与模式大幅扩展。街机版与 PS1 的家用追加内容应按版本比较。 [系列专题](#series-31)。 |
| <a id="fbneo-064"></a>FBNEO-064 | Street Fighter III: New Generation | 街头霸王 III：新世代 | 1997 | Capcom | 80MB | 格斗／清版动作／一对一与场地格斗 | 以几乎全部新角色、Blocking 格挡和 EX 技重塑街霸，亚历克斯与吉尔推动新故事。系统深但首作阵容较小。 [系列专题](#series-31)。 |
| <a id="fbneo-065"></a>FBNEO-065 | Street Fighter III: 2nd Impact | 街头霸王 III：二度冲击 | 1997 | Capcom | 80MB | 格斗／清版动作／一对一与场地格斗 | 增加雨果、Urien 等角色，扩展 EX 技、投技挣脱与奖励关。Blocking 仍是核心，角色与平衡比初代更充实。 [系列专题](#series-31)。 |
| <a id="fbneo-066"></a>FBNEO-066 | Street Fighter III: 3rd Strike | 街头霸王 III：三度冲击 | 2000 | Capcom | 80MB | 格斗／清版动作／一对一与场地格斗 | 加入春丽、真琴等五人，调整判定与音乐美术，Blocking 的时机博弈达到系列高点。街机、DC 与后续移植存在细微差异。 [系列专题](#series-31)。 |
| <a id="fbneo-067"></a>FBNEO-067 | Vampire Savior: The Lord of Vampire | 恶魔战士：吸血鬼救世主 | 1997 | Capcom | 80MB | 格斗／清版动作／一对一与场地格斗 | Dark Force 提供限时角色强化，ES／EX 技与空中连段形成高速恶魔战士对战。角色系统差异很大。 |
| <a id="fbneo-068"></a>FBNEO-068 | Marvel Super Heroes | Marvel Super Heroes | 1995 | Capcom | 80MB | 格斗／清版动作／一对一与场地格斗 | 以漫威角色和六颗无限宝石改变攻防，宝石能力可在战中激活。空中连段与大型角色演出连接后来的 VS 系列。 |
| <a id="fbneo-069"></a>FBNEO-069 | X-Men vs. Street Fighter | X 战警对街头霸王 | 1996 | Capcom | 80MB | 格斗／清版动作／一对一与场地格斗 | 把 X 战警与街霸角色放入双人标签战，空中连段和随时换人形成高速体系。它开启了 Capcom 后续 VS 系列方向。 [系列专题](#series-31)。 |
| <a id="fbneo-070"></a>FBNEO-070 | Marvel vs. Capcom: Clash of Super Heroes | 漫威对卡普空：超级英雄冲突 | 1998 | Capcom | 80MB | 格斗／清版动作／一对一与场地格斗 | 双人标签与援护角色并存，漫威英雄和 Capcom 角色共享空中连段体系。DC 移植是该作的家用版本。 |
| <a id="fbneo-071"></a>FBNEO-071 | Marvel vs. Capcom 2: New Age of Heroes | 漫威对卡普空 2：英雄新纪元 | 2000 | Capcom | 100MB | 格斗／清版动作／一对一与场地格斗 | 三人队伍、三种援护类型和大型角色阵容构成高自由组队。DC 版保留街机核心，是本地多人对战代表。 |
| <a id="fbneo-072"></a>FBNEO-072 | Red Earth / War-Zard | 红色大地Red Earth | 1996 | Capcom | 60MB | 动作冒险／探索／解谜／文字冒险 | Capcom 的 Boss 对战型格斗，玩家角色通过密码保存成长，四名可选角色面对大型敌人。CPS III 画面与 RPG 式成长很独特。 |
| <a id="fbneo-073"></a>FBNEO-073 | Rival Schools: United by Fate | 私立正义学园 | 1997 | Capcom | 60MB | 格斗／清版动作／一对一与场地格斗 | 校园角色以双人队伍、协力技和 3D 场地展开格斗，剧情按学校分组。轻松外表下保留完整立回与连段。 |
| <a id="fbneo-074"></a>FBNEO-074 | JoJo’s Bizarre Adventure: Heritage for the Future | JOJO 的奇妙冒险：未来遗产 | 1999 | Capcom | 60MB | 格斗／清版动作／一对一与场地格斗 | Stand 开关改变招式、防御与资源，角色忠实再现替身能力。CPS III 版以未来遗产篇为基础。 |
| <a id="fbneo-075"></a>FBNEO-075 | Strikers 1945 | 打击者1945 | 1995 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 以二战风格战机、蓄力攻击和金属变形 Boss 构成 Psikyo 纵版射击，奖牌闪烁时机连接高分路线。 |
| <a id="fbneo-076"></a>FBNEO-076 | Strikers 1945 II | 打击者 1945 II | 1997 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 更新机体、蓄力演出和 Boss 形态，节奏更快，奖牌连收与近距离输出让得分风险高于单纯通关。 |
| <a id="fbneo-077"></a>FBNEO-077 | Strikers 1945 III / Strikers 1999 | 打击者 1945 III | 1999 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 改用现代喷气机与更华丽变形 Boss，蓄力技和技术奖励延续 1945 体系。海外标题写 1999，日版编号为 III。 |
| <a id="fbneo-078"></a>FBNEO-078 | Sengoku Blade: Sengoku Ace Episode II / Tengai | 战国之刃 | 1996 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 战国 Ace 续作把横版射击与角色剧情结合，可选人物拥有不同攻击和结局。Psikyo 的敌弹节奏与日式幻想美术突出。 |
| <a id="fbneo-079"></a>FBNEO-079 | Gunbird 2 | 武装飞鸟2 | 1998 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 角色双人组合可发动协力攻击，宝石连锁、蓄力和近距离输出构成高分策略。角色剧情与夸张动画延续彩京风格。 |
| <a id="fbneo-080"></a>FBNEO-080 | Gunbird 1 | Gunbird 1 | 1994 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 魔女、机器人等角色追逐魔镜碎片，蓄力攻击、近战和角色专属火力形成差异。它是彩京角色射击的重要起点。 |
| <a id="fbneo-081"></a>FBNEO-081 | Sol Divide | Sol Divide | 1997 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 横版奇幻射击允许近战魔法与武器攻击，角色升级和道具影响攻略。系统有实验性，保留它是为了呈现 Psikyo 射击的另类分支。 |
| <a id="fbneo-082"></a>FBNEO-082 | Dragon Blaze | Dragon Blaze | 2000 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | 龙骑士可让龙分离进行独立攻击，再召回形成合体火力。这个风险站位机制使它在 Psikyo 纵版射击中很有辨识度。 |
| <a id="fbneo-083"></a>FBNEO-083 | Strikers 1945 Plus | Strikers 1945 Plus | 1999 | Psikyo | 40MB | 射击／卷轴与弹幕射击 | Neo Geo 版本重组系列机体与关卡，并提供适合 MVS 的得分与蓄力规则。它不是 III 的简单地区改名。 |
| <a id="fbneo-084"></a>FBNEO-084 | DoDonPachi | 怒首领蜂 | 1997 | Cave | 60MB | 射击／卷轴与弹幕射击 | 连续击破维持连锁、收集蜂道具并在高密度敌弹中规划路线，Type A／B／C 与射击／激光改变打法。它是 Cave 得分系统的代表。 [系列专题](#series-70)。 |
| <a id="fbneo-085"></a>FBNEO-085 | DoDonPachi Dai-Ou-Jou | 大往生 | 2002 | Cave | 60MB | 射击／卷轴与弹幕射击 | Hyper 强化火力也提升敌弹压力，何时发动成为生存和得分核心。二周目与真 Boss 对背板要求极高，适合从一周目练习。 [系列专题](#series-70)。 |
| <a id="fbneo-086"></a>FBNEO-086 | ESP Ra.De. | ESP Ra.De. | 1998 | Cave | 60MB | 射击／卷轴与弹幕射击 | 角色拥有灵力穿透攻击与特殊得分路线，多路线关卡和大型机械 Boss 结合。它不是单纯以擦弹为唯一机制的作品。 [系列专题](#series-70)。 |
| <a id="fbneo-087"></a>FBNEO-087 | Espgaluda | 长空超少年Espgaluda | 2003 | Cave | 60MB | 射击／卷轴与弹幕射击 | 觉醒系统改变世界与敌弹规则，消耗宝石换取攻防和得分窗口，男女角色性能不同。资源管理比盲目躲弹更重要。 [系列专题](#series-70)。 |
| <a id="fbneo-088"></a>FBNEO-088 | Progear | Progear 的岚 | 2001 | CaVE | 60MB | 射击／卷轴与弹幕射击 | 横向弹幕中切换射击与聚焦，宝石倍率、连击和角色机体决定得分。Capcom 发行、Cave 制作，画面与音乐风格鲜明。 [系列专题](#series-70)。 |
| <a id="fbneo-089"></a>FBNEO-089 | Tiger Heli | 虎直升机 | 1985 | Toaplan | 40MB | 射击／卷轴与弹幕射击 | 直升机纵版射击用炸弹应对密集地面与空中目标，是 Toaplan 早期确立关卡节奏的作品。规则朴素但历史位置重要。 |
| <a id="fbneo-090"></a>FBNEO-090 | Fire Shark / Same! Same! Same! | 飞翔鲛 | 1989 | Toaplan | 40MB | 射击／卷轴与弹幕射击 | 双翼机以散弹、激光和火焰武器推进，蓝色火焰的侧向覆盖改变站位。Toaplan 用长关卡和高难度建立硬派节奏。 |
| <a id="fbneo-091"></a>FBNEO-091 | Truxton | Truxton | 1988 | Toaplan | 40MB | 射击／卷轴与弹幕射击 | 三种颜色武器、骷髅强化与雷鸣炸弹服务高压纵版关卡，死亡后火力损失明显。它是 Toaplan 传统背板射击代表。 |
| <a id="fbneo-092"></a>FBNEO-092 | Vimana | Vimana | 1991 | Toaplan | 40MB | 射击／卷轴与弹幕射击 | 以印度神话风机体、可旋转蓄力射击和副武器应对包围，彩京前身团队的风格已很明显。关卡短促但难度高。 |
| <a id="fbneo-093"></a>FBNEO-093 | Out Zone | 异域战将 | 1990 | Toaplan | 40MB | 射击／卷轴与弹幕射击 | 俯视跑射要求持续前进，主武器可切换方向，副武器与炸弹处理重围。Toaplan 将固定路线与武器资源管理结合。 |
| <a id="fbneo-094"></a>FBNEO-094 | Battle Garegga | Battle Garegga | 1996 | Raizing | 60MB | 射击／卷轴与弹幕射击 | 动态 Rank 会随火力、得分与存活改变敌人强度，奖牌连收和控 rank 相互牵制。生存通关与高分打法几乎两套策略。 |
| <a id="fbneo-095"></a>FBNEO-095 | Raiden | 雷电1 | 1990 | Seibu Kaihatsu | 40MB | 射击／卷轴与弹幕射击 | 双色主武器、导弹与双人协作构成直观纵版射击，节奏重火力路线而非复杂得分。Seibu Kaihatsu 是发行主体，不应写成 Irem。 [系列专题](#series-35)。 |
| <a id="fbneo-096"></a>FBNEO-096 | Raiden II | 雷电2 | 1993 | Seibu Kaihatsu | 40MB | 射击／卷轴与弹幕射击 | 新增紫色等离子鞭与更复杂 Boss，保持双色武器和双人节奏。画面与敌弹升级明显，但仍是传统背板射击。 [系列专题](#series-35)。 |
| <a id="fbneo-097"></a>FBNEO-097 | R-Type | R-Type | 1987 | Irem | 40MB | 射击／卷轴与弹幕射击 | 蓄力波动炮与 Force 装置同时服务正面攻坚、后方防御和特殊站位，关卡强调记忆。街机原版与 MD／PCE 移植各有画面与内容差异。 [系列专题](#series-35)。 |
| <a id="fbneo-098"></a>FBNEO-098 | R-Type Leo | R-Type Leo | 1992 | Irem | 40MB | 射击／卷轴与弹幕射击 | 取消 Force 装置，改用双 Bit 与蓄力突击，节奏比本篇更直接。它是平行分支而非 R-Type III 的街机版。 [系列专题](#series-35)。 |
| <a id="fbneo-099"></a>FBNEO-099 | Xexex / Orius | Xexex | 1991 | Konami | 40MB | 射击／卷轴与弹幕射击 | Konami 以蓄力束与可操纵副武器构成横版射击，背景和大型机械 Boss 展现 16 位街机后期图形能力。 |
| <a id="fbneo-100"></a>FBNEO-100 | Contra (Arcade) | 魂斗罗街机 | 1987 | Konami | 40MB | 射击／跑射与动作射击 | 以纵横卷轴、散弹等武器和双人合作建立系列基础，街机关卡比 FC 更短且演出不同。持续投币与家用有限接关改变难度体验。 [系列专题](#series-04)。 |
| <a id="fbneo-101"></a>FBNEO-101 | Super Contra (Arcade) | 超级魂斗罗街机 | 1988 | Konami | 40MB | 射击／跑射与动作射击 | 增加可升级武器、更密集敌群与俯视图关卡，双人合作仍是核心。它是街机第二作，不是 SFC《Contra III》。 [系列专题](#series-04)。 |
| <a id="fbneo-102"></a>FBNEO-102 | Teenage Mutant Ninja Turtles: Turtles in Time | 忍者神龟：时空之战 | 1991 | Konami | 60MB | 格斗／清版动作／清版动作与合作 | 四名忍者神龟支持合作，投掷敌人向镜头、时间与空间穿越关卡形成特色。街机版与 SFC 移植在内容和画面上不同。 [系列专题](#series-13)。 |
| <a id="fbneo-103"></a>FBNEO-103 | X-Men (Arcade) | X 战警（街机） | 1992 | Konami | 60MB | 格斗／清版动作／清版动作与合作 | 最多六人共享宽阔战场，变种人各自拥有消耗生命的特殊能力。它是授权清版动作中大规模同屏合作的代表。 |
| <a id="fbneo-104"></a>FBNEO-104 | The Simpsons (Arcade) | 辛普森一家 | 1991 | Konami | 40MB | 格斗／清版动作／清版动作与合作 | 辛普森一家四人各有不同武器与合体攻击，关卡穿插 Springfield 场景和动画笑料。家庭合作是主要价值。 |
| <a id="fbneo-105"></a>FBNEO-105 | Sunset Riders | Sunset Riders | 1991 | Konami | 40MB | 格斗／清版动作／清版动作与合作 | 四名牛仔以跑射、滑铲和精准跳跃推进西部关卡，悬赏 Boss 与双人／多人合作形成节奏。 |
| <a id="fbneo-106"></a>FBNEO-106 | Violent Storm | Violent Storm | 1993 | Konami | 40MB | 格斗／清版动作／清版动作与合作 | 三名主角在废墟城市以丰富投技、武器和夸张动画作战，Konami 后期清版动作流畅，场景细节密集。 |
| <a id="fbneo-107"></a>FBNEO-107 | Mystic Warriors | Mystic Warriors | 1993 | Konami | 60MB | 格斗／清版动作／清版动作与合作 | 四名忍者使用不同武器与忍术，关卡横跨现代都市和奇幻场景。Konami 的多人清版节奏与日落骑士相近但动作更华丽。 |
| <a id="fbneo-108"></a>FBNEO-108 | Life Force | Life Force | 1986 | Konami | 40MB | 射击／卷轴与弹幕射击 | 街机版以横纵交替、Option 与有机生物关卡构成沙罗曼蛇体系，海外 Life Force 又调整力量槽规则。需按地区 ROM 识别。 [系列专题](#series-09)。 |
| <a id="fbneo-109"></a>FBNEO-109 | Gradius / Gradius II / Gradius III / Gradius Gaiden | 宇宙巡航机 I／II／III／外传 | 1985 | Konami | 80MB | 射击／卷轴与弹幕射击 | 四作分别代表力量槽定型、武器组扩展、高密度挑战和 PS1 后期原创外传；Gaiden 并非街机编号 IV。街机与家用版本不要混用 ROM。 [系列专题](#series-09)。 |
| <a id="fbneo-110"></a>FBNEO-110 | Parodius Da! / Sexy Parodius / Gokujou Parodius! | 疯狂大射击系列 | 1990 | Konami | 80MB | 射击／卷轴与弹幕射击 | 从初代的 Konami 戏仿到极上的关卡目标与性感帕罗迪乌斯的任务分支，三部都保留射击系统而强化喜剧演出。 [系列专题](#series-09)。 |
| <a id="fbneo-111"></a>FBNEO-111 | TwinBee / Detana!! TwinBee / Pop’n TwinBee | 兵蜂系列 | 1985 | Konami | 60MB | 射击／卷轴与弹幕射击 | 初代确立铃铛强化，Detana 加入蓄力与剧情角色，Pop’n 则是 SFC 家用原创。三作按街机／家用和年份区分。 [系列专题](#series-09)。 |
| <a id="fbneo-112"></a>FBNEO-112 | Puzzle Bobble / Puzzle Bobble 2 / 3 / 4 | 泡泡龙解谜 1／2／3／4 | 1994 | Taito | 80MB | 益智／休闲／落块与消除 | 以固定角度发射彩泡，三颗同色消除并利用悬挂掉落形成大连锁；续作增加对战、角色与新规则。四作分开管理。 |
| <a id="fbneo-113"></a>FBNEO-113 | Mars Matrix | Mars Matrix | 2000 | Capcom | 60MB | 射击／卷轴与弹幕射击 | 自机可吸取敌弹并反弹，连锁与经验等级影响火力和得分。Capcom 的 CPS II 射击以弹幕与反击机制著称。 |
| <a id="fbneo-114"></a>FBNEO-114 | Giga Wing 1 | Giga Wing 1 | 1999 | Capcom | 40MB | 射击／卷轴与弹幕射击 | 反射护盾需要蓄力时机，可在弹幕中创造反攻窗口，奖牌倍率决定高分。它是街机弹幕与打分系统结合的代表。 |
| <a id="fbneo-115"></a>FBNEO-115 | Giga Wing 2 | Giga Wing 2 | 2000 | Capcom | 60MB | 射击／卷轴与弹幕射击 | 在反射系统上加入更明显的 3D 场景与多人机制，分数倍率继续膨胀。DC 另有移植，街机版以 CPS II 为准。 |
| <a id="fbneo-116"></a>FBNEO-116 | Golden Axe (Arcade) / Golden Axe: The Revenge of Death Adder | 战斧1/2/3 | 1989 | Sega | 80MB | 格斗／清版动作／清版动作与合作 | 初代以骑乘与魔法建立合作规则，Death Adder 复仇改用新角色、分支和更华丽演出。两者不是 MD II／III。 [系列专题](#series-27)。 |
| <a id="fbneo-117"></a>FBNEO-117 | Double Dragon 1 / 2 / 3 (Arcade) | 双截龙1/2/3 | 1987–1990 | Technos | 80MB | 格斗／清版动作／清版动作与合作 | 街机初代确立双人清版，二代重做关卡与招式，三代加入商店和更多角色。三作是独立基板商品，家庭优先前 two。 [系列专题](#series-08)。 |
| <a id="fbneo-118"></a>FBNEO-118 | Nekketsu Kouha Kunio-kun / Renegade (Arcade) | 热血系列街机版 | 1986 | Technos | 80MB | 动作冒险／探索／解谜／文字冒险 | 热血硬派街机原作以国夫君街头斗殴开场，海外 Renegade 更换美术与故事。它建立了 Technos 热血系列和双截龙之后的清版方向。 [系列专题](#series-12)。 |
| <a id="fbneo-119"></a>FBNEO-119 | Joe & Mac: Caveman Ninja | 乔与麦克：原始人忍者 | 1991 | Data East | 40MB | 平台动作／横版／单屏／3D 平台 | 原始人用骨头、回旋镖等武器闯关，动作与滑稽动画结合，双人合作是重点。街机版与各家用移植在关卡上有差异。 |
| <a id="fbneo-120"></a>FBNEO-120 | Karnov | Karnov | 1987 | Data East | 40MB | 平台动作／横版／单屏／3D 平台 | Data East 的壮汉 Karnov 以火球和道具挑战横版关卡，难度偏高。这个角色后来多次在 Data East 游戏中客串。 |
| <a id="fbneo-121"></a>FBNEO-121 | Heavy Barrel | Heavy Barrel | 1987 | Data East | 40MB | 射击／跑射与动作射击 | 俯视跑射用方向旋转控制射击，收集钥匙组装终极武器 Heavy Barrel。双人合作与武器时限形成街机节奏。 |
| <a id="fbneo-122"></a>FBNEO-122 | Dark Seal / Gate of Doom | 暗黑封印 | 1990 | Data East | 40MB | 动作冒险／探索／解谜／文字冒险 | 等距动作 RPG 以四名职业角色探索迷宫，法术、道具和升级并存。Data East 的续作 Dark Seal II 又名 Wizard Fire。 |
| <a id="fbneo-123"></a>FBNEO-123 | Midnight Resistance | Midnight Resistance | 1989 | Data East | 40MB | 射击／跑射与动作射击 | 旋转射击方向与角色移动可分开控制，拾取钥匙在关卡间购买武器。它是 Data East 对魂斗罗式跑射的机械化回应。 |
| <a id="fbneo-124"></a>FBNEO-124 | Batsugun | 蝙蝠枪 | 1993 | Toaplan | 20MB | 射击／卷轴与弹幕射击 | 击落敌机积累经验并提升主炮，角色火力、炸弹和双人合作与高密度弹幕结合。Toaplan 晚期作品预示了后来的弹幕风格。 |
| <a id="fbneo-125"></a>FBNEO-125 | Blazing Star | 闪亮之星 | 1998 | Yumekobo / SNK | 60MB | 动作冒险／探索／解谜／文字冒险 | Yumekobo 的纵版射击以蓄力攻击、连击和大型机械场景见长，Neo Geo 画面色彩鲜明。普通通关与高分打法差异明显。 |
| <a id="fbneo-126"></a>FBNEO-126 | Golden Axe: The Revenge of Death Adder | 战斧：死亡蝰蛇的复仇 | 1992 | Sega | 60MB | 格斗／清版动作／清版动作与合作 | 四名新角色各有魔法和连段，关卡分支、坐骑与多人配合大幅扩展。它是街机原创续篇，不是 MD《战斧 III》。 [系列专题](#series-27)。 |
| <a id="fbneo-127"></a>FBNEO-127 | In the Hunt | 海底大战争 | 1993 | Irem | 40MB | 射击／卷轴与弹幕射击 | 驾驶潜艇在水下横版射击，移动缓慢、敌人来自多层深度。Irem 的金属像素细节和双人合作使其独具压迫感。 |
| <a id="fbneo-128"></a>FBNEO-128 | Metal Slug 1 / 2 / X / 3 / 4 / 5 | 合金弹头系列 | 1996–2003 | SNK | 400MB | 射击／跑射与动作射击 | 从初代的越战风幻想跑射，到 X 的二代强化、三代的多路线与变身，再到四五代新角色和系统调整；每作都是独立街机商品。 [系列专题](#series-63)。 |
| <a id="fbneo-129"></a>FBNEO-129 | Street Fighter II: Champion Edition | 街头霸王 II：冠军版 | 1992 | Capcom | 20MB | 格斗／清版动作／一对一与场地格斗 | 首次开放四天王并允许镜像对战，调整部分角色招式与速度。它是 Hyper Fighting 前的竞技版本，不是 Super 的新角色阵容。 [系列专题](#series-31)。 |
| <a id="fbneo-130"></a>FBNEO-130 | Puyo Puyo Tsu | 噗哟噗哟通 | 1994 | Compile / Sega | 8MB | 益智／休闲／落块与消除 | 四连消除与向对手发送干扰块构成对战核心，加入相杀规则后攻防逆转更鲜明。它确立了噗哟系列长期沿用的连锁对战范式，适合家庭双人对局。 [系列专题](#series-88)。 |
| <a id="fbneo-131"></a>FBNEO-131 | Magical Drop III | 魔法气泡 III | 1997 | Data East | 30MB | 益智／休闲／落块与消除 | 从底部抓取并回投同色球，连续消除可压迫对手；角色差异和快节奏让它区别于普通落块游戏。街机版保留了 Data East 益智对战特有的紧张感。 |

---

### GBA

<a id="platform-gba"></a>

32 位掌机的动作、RPG、战棋与原创短局作品；Advance 复刻与原创续篇分开写，未把民间改版或不存在的主机移植混入。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="gba-001"></a>GBA-001 | Pokémon FireRed / LeafGreen | 宝可梦：火红／叶绿 | 2004 | Nintendo | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 以 GBA 画面和第三世代系统重制关都旅程，并加入七之岛与无线适配器支持。它适合比较初代设计与第三世代机制的差异。 [系列专题](#series-21)。 |
| <a id="gba-002"></a>GBA-002 | Pokémon Emerald | 宝可梦：绿宝石 | 2004 | Nintendo | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 整合红蓝宝石的熔岩队与海洋队冲突，并强化对战开拓区。这里的主线是固拉多、盖欧卡与烈空坐，而非原稿误写的“三圣柱”。 [系列专题](#series-21)。 |
| <a id="gba-003"></a>GBA-003 | Golden Sun | 黄金太阳：开启的封印 | 2001 | Nintendo | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 精神力同时用于战斗与场景解谜，精灵召唤和属性搭配构成队伍成长。Camelot 将大地图解谜与传统 JRPG 结合，GBA 音画表现尤其突出。 [系列专题](#series-58)。 |
| <a id="gba-004"></a>GBA-004 | Golden Sun: The Lost Age | 黄金太阳：失落的时代 | 2003 | Nintendo | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 直接延续前作并更换视角，世界规模、精灵组合与航海探索明显扩大。两作合起来才是完整故事，建议按《开启的封印》到《失落的时代》游玩。 [系列专题](#series-58)。 |
| <a id="gba-005"></a>GBA-005 | Fire Emblem: The Binding Blade | 火焰之纹章：封印之剑 | 2002 | Nintendo | 32MB | 战略／战棋／网格战术 | 罗伊在艾雷布大陆组织反抗军，武器耐久与永久阵亡维持传统战棋压力。它是 GBA 首部火纹，主角后来也因《任天堂明星大乱斗》扩大知名度。 [系列专题](#series-15)。 |
| <a id="gba-006"></a>GBA-006 | Fire Emblem: The Blazing Blade | 火焰之纹章：烈火之剑 | 2003 | Nintendo | 32MB | 战略／战棋／网格战术 | 作为《封印之剑》前传，从琳、艾利乌德与赫克托耳的视角补足上一代故事。前期教学与角色支援使它成为许多海外玩家的入坑作。 [系列专题](#series-15)。 |
| <a id="gba-007"></a>GBA-007 | Fire Emblem: The Sacred Stones | 火焰之纹章：圣魔之光石 | 2005 | Nintendo | 32MB | 战略／战棋／网格战术 | 采用独立世界观与双主角路线，并提供地图遭遇战和魔物塔供练级。相较前两作更便于自由培养，战棋压力也更温和。 [系列专题](#series-15)。 |
| <a id="gba-008"></a>GBA-008 | Castlevania: Aria of Sorrow | 恶魔城：晓月圆舞曲 | 2003 | Konami | 32MB | 平台动作／探索型动作 | 来须苍真通过吸收怪物灵魂获得能力，魂收集把探索、战斗与养成连在一起。故事设在 2035 年，是 GBA 三部探索型恶魔城中系统完成度很高的一作。 [系列专题](#series-11)。 |
| <a id="gba-009"></a>GBA-009 | Castlevania: Harmony of Dissonance | 恶魔城：白夜协奏曲 | 2002 | Konami | 32MB | 平台动作／探索型动作 | 祖斯特在表里两座相互关联的城堡间切换，法术书与副武器组合形成不同魔法。画面针对 GBA 屏幕提高亮度，音乐音色则带有鲜明妥协。 [系列专题](#series-11)。 |
| <a id="gba-010"></a>GBA-010 | Castlevania: Circle of the Moon | 恶魔城：月之轮回 | 2001 | Konami | 32MB | 平台动作／探索型动作 | DSS 卡牌两两组合改变武器、属性和技能，动作手感偏传统且难度较高。它由 Konami 神户团队制作，与后续五十岚主导的掌机三部曲在系统路线上不同。 [系列专题](#series-11)。 |
| <a id="gba-011"></a>GBA-011 | Gyakuten Saiban / Phoenix Wright: Ace Attorney | 逆转裁判 | 2001 | Capcom | 16MB | 动作冒险／探索／解谜／文字冒险 | 成步堂在调查与法庭间寻找证词矛盾，以证物“异议”推进案件。GBA 首作没有 NDS 复苏的逆转追加章节和触控科学搜查。 [系列专题](#series-59)。 |
| <a id="gba-012"></a>GBA-012 | Gyakuten Saiban 2 / Phoenix Wright: Ace Attorney – Justice for All | 逆转裁判 2 | 2002 | Capcom | 16MB | 动作冒险／探索／解谜／文字冒险 | 加入心灵枷锁，在调查阶段用证物解开人物秘密；案件继续围绕成步堂与真宵。它是 GBA 原生第二部。 [系列专题](#series-59)。 |
| <a id="gba-013"></a>GBA-013 | Gyakuten Saiban 3 / Phoenix Wright: Ace Attorney – Trials and Tribulations | 逆转裁判 3 | 2004 | Capcom | 16MB | 动作冒险／探索／解谜／文字冒险 | 以多时间线和千寻旧案收束成步堂初期三部曲，法庭攻防与人物关系相互照应。GBA 原版和 NDS 移植文本相同主线。 [系列专题](#series-59)。 |
| <a id="gba-014"></a>GBA-014 | Super Mario Advance | 超级马力欧 Advance（超级马力欧兄弟 2） | 2001 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 重制海外版《Super Mario Bros. 2》的拔菜与投掷玩法，并附街机《Mario Bros.》强化版。角色语音和画面更新明显，不是马力欧世界移植。 [系列专题](#series-01)。 |
| <a id="gba-015"></a>GBA-015 | Super Mario World: Super Mario Advance 2 | 超级马力欧世界：超级马力欧 Advance 2 | 2001 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 把 SFC 马力欧世界带到 GBA，调整存档、路易吉能力与部分界面。披风、耀西和秘密出口仍是主体。 [系列专题](#series-01)。 |
| <a id="gba-016"></a>GBA-016 | Yoshi’s Island: Super Mario Advance 3 | 耀西岛：超级马力欧 Advance 3 | 2002 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 移植耀西岛的背蛋、变身和收集体系，并追加 GBA 专属关卡。画面与声音因掌机硬件有所调整。 [系列专题](#series-01)。 |
| <a id="gba-017"></a>GBA-017 | Super Mario Advance 4: Super Mario Bros. 3 | 超级马力欧 Advance 4：超级马力欧兄弟 3 | 2003 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 以 GBA 重制 FC 三代，保留大地图、变身和世界主题，并支持部分 e-Reader 追加关卡。不是街机 Mario Bros.。 [系列专题](#series-01)。 |
| <a id="gba-018"></a>GBA-018 | Mario & Luigi: Superstar Saga | 马力欧与路易吉 RPG | 2003 | Nintendo | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 兄弟分别由两个按键控制，探索时协作跳跃与锤击，战斗中靠时机强化攻防。豆豆王国的语言和角色幽默开启了长期 RPG 支线。 [系列专题](#series-01)。 |
| <a id="gba-019"></a>GBA-019 | Mega Man Zero | 洛克人 Zero | 2002 | Capcom | 16MB | 平台动作／横版／单屏／3D 平台 | Zero 以剑、枪和盾近身作战，电子精灵提供一次性成长效果，任务评价影响部分能力。高难度与荒野反抗军故事区别于 X 主线。 [系列专题](#series-03)。 |
| <a id="gba-020"></a>GBA-020 | Mega Man Zero 2 | 洛克人 Zero 2 | 2003 | Capcom | 16MB | 平台动作／横版／单屏／3D 平台 | 增加形态切换、EX 技能和链枪，关卡评价与电子精灵养成继续牵制。剧情深化抵抗军与 Neo Arcadia 冲突。 [系列专题](#series-03)。 |
| <a id="gba-021"></a>GBA-021 | Mega Man Zero 3 | 洛克人 Zero 3 | 2004 | Capcom | 16MB | 平台动作／横版／单屏／3D 平台 | 加入反冲杖、身体芯片和更成熟关卡评价，Omega 与 Copy X 把剧情推向系列转折。系统完整度通常被视为四作高峰。 [系列专题](#series-03)。 |
| <a id="gba-022"></a>GBA-022 | Mega Man Zero 4 | 洛克人 Zero 4 | 2005 | Capcom | 16MB | 平台动作／横版／单屏／3D 平台 | 天气系统会改变关卡与 Boss 条件，Zero 可用夺取拳取得敌人武器。故事为 GBA 四部曲收束，难度较前几作更可调。 [系列专题](#series-03)。 |
| <a id="gba-023"></a>GBA-023 | Mega Man Battle Network | 洛克人 EXE | 2001 | Capcom | 16MB | 平台动作／横版／单屏／3D 平台 | 现实网络与网格芯片战斗并行，三行六格场地中移动、选文件夹并即时出牌。它把洛克人变成网络时代动作 RPG。 [系列专题](#series-03)。 |
| <a id="gba-024"></a>GBA-024 | Mega Man Battle Network 2 | 洛克人 EXE 2 | 2002 | Capcom | 16MB | 平台动作／横版／单屏／3D 平台 | 扩充网络区域、芯片码和形态变换，迷宫结构与剧情比初代完整。文件夹构筑仍是战斗效率关键。 [系列专题](#series-03)。 |
| <a id="gba-025"></a>GBA-025 | Mega Man Battle Network 3: Blue / White | 洛克人 EXE 3：蓝／白 | 2002 | Capcom | 16MB | 平台动作／横版／单屏／3D 平台 | 以版本独有芯片、Style Change 和 Navi 培养深化构筑，剧情完成度高。Blue／White 有芯片与部分 Boss 差异，不是地区别名。 [系列专题](#series-03)。 |
| <a id="gba-026"></a>GBA-026 | Kirby & the Amazing Mirror | 星之卡比：镜之大迷宫 | 2004 | Nintendo | 32MB | 平台动作／探索型动作 | 镜之国由相互连接的区域组成，多名卡比可通过手机呼叫协助，能力用于打通分支。它比传统选关更偏自由探索。 [系列专题](#series-20)。 |
| <a id="gba-027"></a>GBA-027 | Metroid Fusion | 密特罗德：融合 | 2002 | Nintendo | 32MB | 平台动作／探索型动作 | 萨姆斯在 BSL 空间站被 X 寄生体威胁，SA-X 会作为高压追逐者反复出现。流程比《超级密特罗德》更线性，但叙事密度和紧迫感明显更强。 [系列专题](#series-18)。 |
| <a id="gba-028"></a>GBA-028 | Metroid: Zero Mission | 密特罗德：零点任务 | 2004 | Nintendo | 32MB | 平台动作／探索型动作 | 以现代地图、存档和动作系统重制 FC 初代，并在原结局后追加零装萨姆斯潜入段落。它不是简单高清化，而是兼顾新玩家与系列史的完整重制。 [系列专题](#series-18)。 |
| <a id="gba-029"></a>GBA-029 | Final Fantasy IV Advance | 最终幻想 IV Advance | 2005 | Square Enix | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 以 ATB、固定角色职业和月之暗面群像剧为主体，GBA 版加入角色重编与追加迷宫。它不是 NDS 的 3D 语音重制。 [系列专题](#series-06)。 |
| <a id="gba-030"></a>GBA-030 | Final Fantasy V Advance | 最终幻想 V Advance | 2006 | Square Enix | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 职业、技能继承与自由编队构成核心，GBA 版追加封印神殿和职业。队伍构筑深度比单纯等级推进更重要。 [系列专题](#series-06)。 |
| <a id="gba-031"></a>GBA-031 | Final Fantasy VI Advance | 最终幻想 VI Advance | 2006 | Square Enix | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 多主角群像、魔石学习和世界崩坏前后结构保持完整，GBA 版增加魔石与龙巢等内容。像素原版与后续像素复刻不是同一版本。 [系列专题](#series-06)。 |
| <a id="gba-032"></a>GBA-032 | Advance Wars | 高级战争 | 2001 | Nintendo | 16MB | 战略／战棋／大战略与军团 | 以兵种克制、地形、产能与指挥官能力构成清晰战棋，战役和挑战地图适合反复优化。它把复杂军事策略压缩成易懂但不浅薄的掌机系统。 [系列专题](#series-60)。 |
| <a id="gba-033"></a>GBA-033 | Advance Wars 2: Black Hole Rising | 高级战争 2：黑洞崛起 | 2003 | Nintendo | 16MB | 战略／战棋／大战略与军团 | 新增黑洞军指挥官与超级 CO 技，并针对前作平衡性调整。整体是“更多内容＋更精细对抗”的续作，而非颠覆系统。 [系列专题](#series-60)。 |
| <a id="gba-034"></a>GBA-034 | Final Fantasy Tactics Advance | 最终幻想战略版 Advance | 2003 | Square Enix | 32MB | 战略／战棋／网格战术 | 以伊瓦利斯学校社团为切口，法则牌会限制战斗中的行动，职业任务和地域占领构成养成。它是最终幻想战略版的掌机分支，不属于皇家骑士团。 [系列专题](#series-06)。 |
| <a id="gba-035"></a>GBA-035 | Super Robot Taisen A | 超级机器人大战 A | 2001 | Bandai | 32MB | 战略／战棋／网格战术 | 以便携短篇战役和护盾、武器系统展开跨作品剧情，原创主角与机体影响路线。PSP 的 A Portable 才是本作重制。 [系列专题](#series-39)。 |
| <a id="gba-036"></a>GBA-036 | Super Robot Taisen R | 超级机器人大战 R | 2002 | Bandai | 32MB | 战略／战棋／网格战术 | 围绕时间移动与装备换装展开，原创机体可通过换装适应战况。GBA 战役节奏紧凑，参战阵容与 A 不同。 [系列专题](#series-39)。 |
| <a id="gba-037"></a>GBA-037 | Super Robot Taisen D | 超级机器人大战 D | 2003 | Bandai | 32MB | 战略／战棋／网格战术 | 以荒废世界和“残骸”相关谜团组织剧情，原创主角与机体拥有鲜明设定。战场地图和双打之外的单队编成仍是主要决策。 [系列专题](#series-39)。 |
| <a id="gba-038"></a>GBA-038 | Super Robot Taisen J | 超级机器人大战 J | 2005 | Bandai | 32MB | 战略／战棋／网格战术 | 取消部分传统小队限制，以新人格主角、伴侣选择和后期强力原创机见长。动画与参战阵容在 GBA 末期作品中较突出。 [系列专题](#series-39)。 |
| <a id="gba-039"></a>GBA-039 | Super Robot Taisen: Original Generation | 超级机器人大战 OG | 2002 | Banpresto | 32MB | 战略／战棋／网格战术 | OG 摆脱授权作品，集中 Banpresto 原创机体与人物，双机小队系统影响站位和攻击。它是理解 OG 世界线的入口。 [系列专题](#series-39)。 |
| <a id="gba-040"></a>GBA-040 | Super Robot Taisen: Original Generation 2 | 超级机器人大战 OG2 | 2005 | Banpresto | 32MB | 战略／战棋／网格战术 | 延续 OG 并扩大机体、角色与剧情线，小队编组仍是战术重点。GBA 两作顺序游玩比单独跳入更容易理解。 [系列专题](#series-39)。 |
| <a id="gba-041"></a>GBA-041 | The Legend of Zelda: The Minish Cap | 塞尔达传说：缩小帽 | 2004 | Nintendo | 32MB | 动作冒险／探索／解谜／文字冒险 | 皮克罗帽子让林克缩小，在普通世界与微型路径间解谜；剑技、分身与碎片拼合扩充探索。由 Capcom 团队参与制作。 [系列专题](#series-02)。 |
| <a id="gba-042"></a>GBA-042 | Harvest Moon: Friends of Mineral Town | 牧场物语：矿石镇的伙伴们 | 2003 | Natsume | 32MB | 模拟／音乐／派对／经营与生活模拟 | 在矿石镇安排农牧、采矿、节庆和恋爱，居民日程与事件让城镇随时间变化。它是 GBA 代表作，不是 Friends 的 NDS 移植。 [系列专题](#series-23)。 |
| <a id="gba-043"></a>GBA-043 | WarioWare, Inc.: Mega Microgame$! | 瓦力欧制造：超迷你游戏 | 2003 | Nintendo | 16MB | 益智／休闲／规则解谜与短局 | 数秒内理解并完成一个微游戏，速度不断提升，规则识别本身就是挑战。它用极短反馈建立派对与单人刷分两种乐趣。 [系列专题](#series-01)。 |
| <a id="gba-044"></a>GBA-044 | Wario Land 4 | 瓦力欧乐园 4 | 2001 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 肩撞与变身用于取得宝石和钥匙，触动终点开关后必须在倒计时内逃回入口。关卡因此形成探索与撤离两段节奏。 [系列专题](#series-01)。 |
| <a id="gba-045"></a>GBA-045 | Mario Kart: Super Circuit | 马力欧卡丁车 Advance | 2001 | Nintendo | 16MB | 竞速／体育／竞速与驾驶 | 拥有 GBA 原创赛道，并可解锁 SFC 全部赛道；金币、轻量漂移和道具延续传统。掌机视野使近身对战尤其紧张。 [系列专题](#series-01)。 |
| <a id="gba-046"></a>GBA-046 | Sonic Advance | 索尼克 Advance | 2001 | Sega | 8MB | 平台动作／横版／单屏／3D 平台 | 索尼克、塔尔斯、纳克鲁斯与爱咪有不同动作，关卡延续高速路线与特殊关。它是 GBA 原创新线，不是 MD 作品移植。 [系列专题](#series-25)。 |
| <a id="gba-047"></a>GBA-047 | Sonic Advance 2 | 索尼克 Advance 2 | 2002 | Sega | 8MB | 平台动作／横版／单屏／3D 平台 | 加入空中动作与更强速度导向，角色解锁和特殊关要求提高。 Cream 的 Chao 攻击降低部分 Boss 难度。 [系列专题](#series-25)。 |
| <a id="gba-048"></a>GBA-048 | Sonic Advance 3 | 索尼克 Advance 3 | 2004 | Sega | 8MB | 平台动作／横版／单屏／3D 平台 | 两名角色组队，搭档会改变动作、能力与路线，队伍选择是主要创新。场景与剧情承接前两作。 [系列专题](#series-25)。 |
| <a id="gba-049"></a>GBA-049 | Shining Soul | 光明之魂 | 2003 | Sega | 16MB | 角色扮演／动作 RPG | 转为俯视即时动作 RPG，以职业、装备掉落和地牢刷取替代光明力量战棋。GBA 联机曾是卖点，单机也能完整推进。 [系列专题](#series-29)。 |
| <a id="gba-050"></a>GBA-050 | Shining Soul II | 光明之魂 II | 2003 | Sega | 16MB | 角色扮演／动作 RPG | 增加职业、技能、道具与地牢变化，角色构筑比初代丰富。它是动作 RPG 续作，不是光明力量 III 的掌机版。 [系列专题](#series-29)。 |
| <a id="gba-051"></a>GBA-051 | Baldur’s Gate: Dark Alliance | 博德之门：黑暗联盟 | 2003 | Destination Software | 32MB | 角色扮演／动作 RPG | 采用俯视即时战斗、装备掉落和本地双人合作，与 PC 版博德之门的队伍暂停战术不同。GBA 移植体量与画面经过压缩。 |
| <a id="gba-052"></a>GBA-052 | Dragon Ball Z: Supersonic Warriors | 龙珠 Z：舞空斗剧 | 2004 | Bandai | 32MB | 格斗／清版动作／一对一与场地格斗 | 以空中高速移动、气力、必杀和队伍换人表现龙珠 Z 战斗，剧情模式含 IF 分支。它是 Arc System Works 的龙珠格斗，与索尼克无关。 [系列专题](#series-16)。 |
| <a id="gba-053"></a>GBA-053 | Kingdom Hearts: Chain of Memories | 王国之心：记忆之链 | 2004 | Square Enix | 32MB | 角色扮演／动作 RPG | 把动作战斗改成卡牌组牌、打断数值与楼层探索，记忆之堡连接一代与二代。它不是梦中降生的掌机版。 [系列专题](#series-61)。 |
| <a id="gba-054"></a>GBA-054 | Yu-Gi-Oh! The Eternal Duelist Soul | 游戏王：永恒决斗者之魂 | 2002 | Konami | 16MB | 动作冒险／探索／解谜／文字冒险 | 以卡牌构筑和规则对战为核心，逐步解锁卡包与对手。它是 GBA 早期较完整的游戏王电子对战作品。 |
| <a id="gba-055"></a>GBA-055 | Boktai: The Sun Is in Your Hand | 我们的太阳 | 2003 | Konami | 16MB | 动作冒险／探索／解谜／文字冒险 | 卡带阳光传感器影响武器充能、场景与战斗，主角用太阳枪对抗不死族。小岛组把真实光照变成核心机制，模拟时需确认传感器映射。 |
| <a id="gba-056"></a>GBA-056 | Mario Golf: Advance Tour | 马力欧高尔夫 Advance Tour | 2004 | Nintendo | 16MB | 竞速／体育／体育与运动 | 在巡回赛之外加入校园成长、经验分配与角色培养，单双人赛对应不同目标。它与 N64／GC 时代联动设计相关，但单机内容完整。 [系列专题](#series-01)。 |
| <a id="gba-057"></a>GBA-057 | Mario Tennis: Power Tour | 马力欧网球 Power Tour | 2005 | Nintendo | 16MB | 竞速／体育／体育与运动 | 以学员成长、训练和赛事串联网球 RPG，力量与旋转属性影响打法。掌机角色培养是它区别于普通街模式移植的重点。 [系列专题](#series-01)。 |
| <a id="gba-058"></a>GBA-058 | Super Monkey Ball Jr. | 超级猴子球 Jr. | 2002 | Sega | 16MB | 模拟／音乐／派对／生活模拟与派对 | 通过倾斜场地引导猴子球到终点，保留家用机核心并缩减内容。关卡要求精细坡度控制，而非直接控制角色跳跃。 |
| <a id="gba-059"></a>GBA-059 | Mr. Driller A: Fushigi na Pacteria | 钻地先生 A | 2002 | Namco | 16MB | 益智／休闲／规则解谜与短局 | 在彩块中向下钻行，管理氧气并避免坍塌，以任务和 Pacteria 培养扩展规则。它是 GBA 原创衍生。 [系列专题](#series-62)。 |
| <a id="gba-060"></a>GBA-060 | Metal Slug Advance | 合金弹头 Advance | 2004 | SNK | 16MB | 射击／跑射与动作射击 | GBA 原创关卡加入卡片收集和生命条，保留手绘跑射、俘虏与载具。它不是街机编号作的简单压缩。 [系列专题](#series-63)。 |
| <a id="gba-061"></a>GBA-061 | Pokémon Ruby / Sapphire | 宝可梦：红宝石／蓝宝石 | 2002 | Nintendo | 16MB | 射击／卷轴与弹幕射击 | 第三世代来到丰缘，加入特性、性格和双打对战，宝可梦构筑由此明显深化。红宝石与蓝宝石是原版双版本，绿宝石是后来的扩展版。 [系列专题](#series-21)。 |
| <a id="gba-062"></a>GBA-062 | Pokémon Mystery Dungeon: Red Rescue Team | 宝可梦不可思议迷宫：赤救助队 | 2005 | Nintendo | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 玩家变成宝可梦，与伙伴组成救助队探索随机迷宫。赤救助队是 GBA 版，青救助队是 NDS 版，两者为同一故事的双版本而非前后续作。 [系列专题](#series-21)。 |
| <a id="gba-063"></a>GBA-063 | Rhythm Tengoku | 节奏天国 | 2006 | Nintendo | 16MB | 模拟／音乐／派对／音乐与节奏 | GBA 首作用极简画面与音乐节拍组织短小游戏，强调听觉和预期节奏。系列后来才因 NDS 续作更广为人知。 |
| <a id="gba-064"></a>GBA-064 | Ninja Five-O | 忍者刑警 | 2003 | Konami | 8MB | 平台动作／横版／单屏／3D 平台 | 忍者以刀、忍术和钩索在房间中救援人质，动作紧凑且路线自由。Konami 发行量小、完成度高，是 GBA 后期动作佳作。 |
| <a id="gba-065"></a>GBA-065 | Klonoa: Empire of Dreams | 风之少年：梦之帝国 | 2001 | Namco | 8MB | 平台动作／横版／单屏／3D 平台 | 用风弹抓敌并投出或二段跳，关卡以机关解谜为主。它是 GBA 原创掌机篇章，与家用机《通往幻界之门》不同。 [系列专题](#series-64)。 |
| <a id="gba-066"></a>GBA-066 | Astro Boy: Omega Factor | 铁臂阿童木：原子心的秘密 | 2003 | Sega | 16MB | 平台动作／横版／单屏／3D 平台 | Treasure 把阿童木的飞行、拳击与光束做成高速清版动作，角色图鉴和能力成长串联手冢宇宙。它是授权改编中少见的系统精品。 |
| <a id="gba-067"></a>GBA-067 | Mario vs. Donkey Kong | 马力欧对咚奇刚 | 2004 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 以迷你马力欧玩具为解谜目标，先搬钥匙再用开关、传送带和敌人引导路线。它是 GBA 益智动作，不是街机 Donkey Kong。 [系列专题](#series-01)。 |
| <a id="gba-068"></a>GBA-068 | Final Fantasy I & II: Dawn of Souls | 最终幻想 I・II：灵魂黎明 | 2004 | Square Enix | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 一张 GBA 卡带收录两部重制，降低初代练级门槛并追加灵魂迷宫。两作仍保留不同职业与熟练度体系。 [系列专题](#series-06)。 |
| <a id="gba-069"></a>GBA-069 | Tactics Ogre: The Knight of Lodis | 皇家骑士团外传：罗迪斯的骑士 | 2001 | Nintendo / Atlus | 16MB | 战略／战棋／网格战术 | 以等距战棋、职业与阵营选择展开外传故事，节奏适合掌机但养成仍很深入。它是 Quest 作品，日本由 Nintendo 发行。 [系列专题](#series-37)。 |
| <a id="gba-070"></a>GBA-070 | Dragon Ball: Advanced Adventure | 龙珠大冒险 | 2004 | Atari / Bandai | 16MB | 动作冒险／探索／解谜／文字冒险 | 以悟空少年篇为主线，横版动作、一对一战斗和飞行关卡交替。隐藏角色与收集内容让它不只是动画关卡复述。 [系列专题](#series-16)。 |
| <a id="gba-071"></a>GBA-071 | Kirby: Nightmare in Dream Land | 星之卡比：梦之泉豪华版 | 2002 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 以 GBA 音画重制 FC 梦之泉，保留复制能力、秘密开关和多人模式，并追加额外玩法。不是 Amazing Mirror 的关卡重排。 [系列专题](#series-20)。 |
| <a id="gba-072"></a>GBA-072 | Gunstar Super Heroes | 超级火枪英雄 | 2005 | Sega | 16MB | 射击／跑射与动作射击 | 重新演绎 MD 火枪英雄的武器与高速动作，双角色路线和 Boss 密集配置延续 Treasure 风格。它不是简单 GBA 移植。 |
| <a id="gba-073"></a>GBA-073 | WarioWare Twisted! | 转转瓦力欧制造 | 2004 | Nintendo | 16MB | 益智／休闲／规则解谜与短局 | 卡带陀螺仪让旋转机体成为操作方式，数秒小游戏围绕转动不断变体。模拟时要配置运动传感器，否则体验不完整。 [系列专题](#series-01)。 |
| <a id="gba-074"></a>GBA-074 | Mother 3 | 地球冒险 3 | 2006 | Nintendo | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 以章节切换多名角色视角，回合战斗可随音乐节拍追加连击。只在日本正式发行，中文化让其亲情、社区与失落主题更易被理解。 [系列专题](#series-44)。 |
| <a id="gba-075"></a>GBA-075 | Sword of Mana | 新约圣剑传说 | 2003 | Square Enix | 16MB | 角色扮演／动作 RPG | 重新诠释 GB 初代，以男女双视角、昼夜和武器锻造扩展动作 RPG。它是 GBA 重制，不应与 SFC《圣剑传说 2》混为一作。 [系列专题](#series-40)。 |
| <a id="gba-076"></a>GBA-076 | Tomato Adventure | 番茄酱王国大冒险 | 2002 | Nintendo | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 主角为营救女友进入番茄酱王国，战斗用“ gimmick ”玩具和按键小游戏取代普通指令。AlphaDream 后来把动作指令思路带入马力欧与路易吉 RPG；它与斯塔菲无关。 |
| <a id="gba-077"></a>GBA-077 | Densetsu no Stafy | 传说的斯塔菲 | 2002 | Nintendo | 8MB | 平台动作／横版／单屏／3D 平台 | 海星王子斯塔菲以旋转、游泳和水下机动穿越海洋关卡，帮助沿途角色并收集宝箱。TOSE 与任天堂把平台动作做得温和亲切，首作原定 GBC 后转向 GBA。 [系列专题](#series-92)。 |
| <a id="gba-078"></a>GBA-078 | Densetsu no Stafy 2 | 传说的斯塔菲 2 | 2003 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 延续海洋动作与角色委托，加入更多变身、载具和斯塔菲的家人相关剧情。关卡目标比单纯抵达终点更丰富，日语阅读会影响部分委托理解。 [系列专题](#series-92)。 |
| <a id="gba-079"></a>GBA-079 | Densetsu no Stafy 3 | 传说的斯塔菲 3 | 2004 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 第三部 GBA 作加入妹妹斯塔碧，并以双角色能力和更丰富的关卡互动扩展海洋冒险。它是 GBA 三部曲的完成篇，不是 NDS 海外版《The Legendary Starfy》。 [系列专题](#series-92)。 |

---

### GBC

<a id="platform-gbc"></a>

彩色专用或以彩色体验为主的作品，包含 GBC 原创、双版本联动和掌机衍生；黑白 GB 原作留在下一章。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="gbc-001"></a>GBC-001 | The Legend of Zelda: Link’s Awakening DX | 塞尔达传说：织梦岛 DX | 1998 | Nintendo | 4MB | 动作冒险／探索／解谜／文字冒险 | 在谜样岛屿收集乐器并探索迷宫，离岛设定与结局赋予故事淡淡忧伤。DX 增加色彩与隐藏迷宫，原版则保留 GB 单色风味。 [系列专题](#series-02)。 |
| <a id="gbc-002"></a>GBC-002 | Wario Land 3 | 瓦力欧乐园 3 | 2000 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 瓦力欧没有传统生命耗尽，敌人更多造成状态变化并反向参与解谜；宝藏和新能力推动非线性探索。 [系列专题](#series-01)。 |
| <a id="gbc-003"></a>GBC-003 | Pokémon Gold / Silver / Crystal | 宝可梦：金／银／水晶 | 1999–2000 | Nintendo | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 城都与关都连成双地区旅程，引入昼夜、星期、孵化和性别等系统。水晶版加入更多动画与水君剧情，是第二世代的扩展版。 [系列专题](#series-21)。 |
| <a id="gbc-004"></a>GBC-004 | Shantae | 桑塔 | 2002 | Capcom | 8MB | 平台动作／探索型动作 | 半精灵桑塔以头发攻击和动物变身探索城镇与迷宫，动画在 GBC 上非常出色。GBA 已发售后才推出使其当年商业表现有限，后来逐步发展为系列。 |
| <a id="gbc-005"></a>GBC-005 | Metal Gear Solid: Ghost Babel | 合金装备：幽灵通天塔 | 2000 | Konami | 8MB | 动作冒险／生存恐怖与潜行 | 以独立世界观呈现掌机潜行任务，并加入大量 VR 挑战。它虽在西方使用 Metal Gear Solid 标题，却不是 PS1 主线移植。 [系列专题](#series-19)。 |
| <a id="gbc-006"></a>GBC-006 | Dragon Warrior Monsters | 勇者斗恶龙怪兽篇 | 2000 | Enix | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 以《勇者斗恶龙 VI》的特瑞为主角，在随机迷宫收服怪物并通过交配继承技能。它开创怪兽篇的掌机养成体系。 [系列专题](#series-07)。 |
| <a id="gbc-007"></a>GBC-007 | Dragon Warrior Monsters 2: Cobi’s Journey / Tara’s Adventure | 勇者斗恶龙怪兽篇 2 | 2001 | Enix | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 双主角版本加入更多怪物、地形钥匙和家族冒险，交配继承仍是队伍构筑核心。Cobi／Tara 是互补商品。 [系列专题](#series-07)。 |
| <a id="gbc-008"></a>GBC-008 | Pokémon Trading Card Game | 宝可梦集换式卡牌 GB | 2000 | Nintendo | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 把实体宝可梦卡牌规则做成牌组构筑、属性克制和道馆挑战，胜负不依赖精灵练级。附赠卡与后续日本限定续作不是同一商品。 [系列专题](#series-21)。 |
| <a id="gbc-009"></a>GBC-009 | Game & Watch Gallery 1–3 | Game & Watch 博物馆 1–3 | 1997–1999 | Nintendo | 2MB | 模拟／音乐／派对／生活模拟与派对 | 每作收录多种 Game & Watch 游戏，并提供原始与现代重绘模式。1–3 横跨 GB／GBC，是观察任天堂早期便携游戏史的合集。 |
| <a id="gbc-010"></a>GBC-010 | Wario Land II | 瓦力欧乐园 2 | 1998 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 以不死身、受击变身与分支关卡改变平台动作逻辑，既有 GB 版也有 GBC 彩色版。 [系列专题](#series-01)。 |
| <a id="gbc-011"></a>GBC-011 | Super Mario Bros. Deluxe | 超级马力欧兄弟 DX | 1999 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | GBC 重制 FC 初代，并加入挑战、隐藏模式与红币收集；小屏视野改变跳跃判断。它不是街机 Mario Bros.。 [系列专题](#series-01)。 |
| <a id="gbc-012"></a>GBC-012 | Survival Kids | 生存少年 | 1999 | Konami | 4MB | 动作冒险／探索／解谜／文字冒险 | 在荒岛收集食物、材料并制作工具，选择会影响路线与结局。它是 Konami 早期掌机生存游戏，也是后来《迷失蔚蓝》的前身。 |
| <a id="gbc-013"></a>GBC-013 | Star Ocean: Blue Sphere | 星之海洋：蔚蓝星球 | 2001 | Enix | 8MB | 角色扮演／动作 RPG | 把星之海洋故事带到 GBC，采用俯视动作战斗与大量角色技能，是系列少见的掌机原创章节。 [系列专题](#series-24)。 |
| <a id="gbc-014"></a>GBC-014 | Mega Man Xtreme | 洛克人 X：电子任务 | 2000 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 把 X 系列动作压缩到 GBC，借用 X1／X2 的 Maverick 并安排数码世界故事。Zero 不可作为常驻主角，续作才扩展双主角。 [系列专题](#series-03)。 |
| <a id="gbc-015"></a>GBC-015 | The Legend of Zelda: Oracle of Seasons / Oracle of Ages | 塞尔达传说：大地之章／时空之章 | 2001 | Nintendo | 8MB | 动作冒险／探索／解谜／文字冒险 | 双作分别围绕四季变化和过去／现在切换，大地偏动作、时空偏谜题；通关密码可联动另一作并开启完整结局。它们是互补冒险而非红蓝式版本差异。 [系列专题](#series-02)。 |
| <a id="gbc-016"></a>GBC-016 | Mega Man Xtreme 2 | 洛克人 X2：灵魂消除者 | 2001 | Capcom | 8MB | 平台动作／横版／单屏／3D 平台 | 结合 X 与 Zero 两条可操作路线，Boss 和关卡借用早期 X 系列元素并重新编排。相比首作内容更完整，也延续掌机 Xtreme 支线。 [系列专题](#series-03)。 |
| <a id="gbc-017"></a>GBC-017 | Mario Tennis | 马力欧网球（GBC） | 2000 | Nintendo | 8MB | 竞速／体育／体育与运动 | Camelot 用旋转球、扣杀和蓄力建立易懂但有深度的网球对战。N64 版还能与 GBC 版联动，是后续家庭体育作品的基础。 [系列专题](#series-01)。 |

---

### GB

<a id="platform-gb"></a>

黑白 Game Boy 正式作品，兼顾早期便携史、经典休闲和可反复游玩的动作／RPG。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="gb-001"></a>GB-001 | The Legend of Zelda: Link’s Awakening | 塞尔达传说：织梦岛 | 1993 | Nintendo | 4MB | 动作冒险／探索／解谜／文字冒险 | 在谜样岛屿收集乐器并探索迷宫，离岛设定与结局赋予故事淡淡忧伤。DX 增加色彩与隐藏迷宫，原版则保留 GB 单色风味。 [系列专题](#series-02)。 |
| <a id="gb-002"></a>GB-002 | Super Mario Land | 超级马力欧乐园 | 1989 | Nintendo | 2MB | 平台动作／横版／单屏／3D 平台 | 在萨拉萨大陆对抗外星人 Tatanga，除跑跳外还有潜艇与飞机射击关。横井军平团队做出不同于 FC 本篇的短小掌机冒险。 [系列专题](#series-01)。 |
| <a id="gb-003"></a>GB-003 | Super Mario Land 2: 6 Golden Coins | 超级马力欧乐园 2：六枚金币 | 1992 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 围绕六枚金币和六大区域展开，地图选关与秘密入口更自由。瓦力欧首次作为最终对手登场，随后才独立成主角。 [系列专题](#series-01)。 |
| <a id="gb-004"></a>GB-004 | Wario Land: Super Mario Land 3 | 瓦力欧乐园：超级马力欧乐园 3 | 1994 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 瓦力欧用肩撞、搬敌和不同帽子变身开路，宝藏数量影响结局住所。它既是马力欧大陆第三作，也是瓦力欧首次担任主角。 [系列专题](#series-01)。 |
| <a id="gb-005"></a>GB-005 | Pokémon Red / Green / Blue / Yellow | 宝可梦：红／绿／蓝／皮卡丘 | 1996–1998 | Nintendo | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 以收集、交换和对战驱动关都旅行，双版本差异鼓励玩家互联。黄版围绕皮卡丘与动画元素调整，红绿蓝则代表 1996 年起家的原始形态。 [系列专题](#series-21)。 |
| <a id="gb-006"></a>GB-006 | Metroid II: Return of Samus | 密特罗德 II：萨姆斯归来 | 1991 | Nintendo | 8MB | 平台动作／探索型动作 | 任务转为在 SR388 星清除各阶段密特罗德，地图随讨伐进度逐步开放。掌机画面限制了视野，却强化了幽闭感；萨姆斯与幼体的剧情也连接《超级密特罗德》。 [系列专题](#series-18)。 |
| <a id="gb-007"></a>GB-007 | Mega Man: Dr. Wily’s Revenge | 洛克人世界：威利博士的反击 | 1991 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | GB 初代混合 FC 一二代的机器人与关卡，并加入威利城新内容。小屏卷轴和跳跃判定使它并非简单 FC 合集。 [系列专题](#series-03)。 |
| <a id="gb-008"></a>GB-008 | Mega Man II | 洛克人世界 II | 1992 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 沿用 GB 掌机化结构，组合 FC 二代与三代元素；难度与音乐评价较特殊，作为系列版本史保留，不建议替代家用机二代入门。 [系列专题](#series-03)。 |
| <a id="gb-009"></a>GB-009 | Mega Man III | 洛克人世界 III | 1992 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 重新编排 FC 三至五代 Boss，并加入滑铲、蓄力与原创最终段落。它比前两部 GB 作更接近完整原创掌机洛克人。 [系列专题](#series-03)。 |
| <a id="gb-010"></a>GB-010 | Mega Man IV | 洛克人世界 IV | 1993 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 引入商店、P 芯片和更完整原创关卡，FC 四代与五代 Boss 分组出现。系统与剧情已明显脱离单纯移植。 [系列专题](#series-03)。 |
| <a id="gb-011"></a>GB-011 | Mega Man V | 洛克人世界 V | 1994 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 以星体机器人和外太空关卡取代直接 reuse FC 阵容，新武器与专属 Boss 让它成为 GB 五作中最完整的一作。 [系列专题](#series-03)。 |
| <a id="gb-012"></a>GB-012 | Castlevania: The Adventure | 恶魔城：德古拉传说 | 1990 | Konami | 8MB | 平台动作／横版／单屏／3D 平台 | 克里斯托弗以火球鞭升级挑战 GB 原创关卡，没有副武器；移动缓慢、视野有限。它是早期掌机作，续作才明显优化节奏。 [系列专题](#series-11)。 |
| <a id="gb-013"></a>GB-013 | Castlevania II: Belmont’s Revenge | 恶魔城：德古拉传说 II | 1991 | Konami | 8MB | 平台动作／横版／单屏／3D 平台 | 加入绳索、四种副武器和初始城堡选择，操作与关卡比 GB 初代成熟。故事延续克里斯托弗父子线。 [系列专题](#series-11)。 |
| <a id="gb-014"></a>GB-014 | Castlevania Legends | 恶魔城：漆黑前奏曲 | 1997 | Konami | 8MB | 平台动作／横版／单屏／3D 平台 | 索尼娅作为女性贝尔蒙特挑战德古拉，灵魂武器提供不同能力。它后来不再被视作正史主线，收藏意义在 GB 独立支线。 [系列专题](#series-11)。 |
| <a id="gb-015"></a>GB-015 | Kid Dracula / Akumajou Special: Boku Dracula-kun | 恶魔城特别篇：我是德古拉 | 1993 | Konami | 4MB | 动作冒险／探索／解谜／文字冒险 | 以 Q 版小吸血鬼、变形法术和轻松关卡重绘恶魔城元素。它偏平台动作与幽默，不是严肃贝尔蒙特正史。 [系列专题](#series-11)。 |
| <a id="gb-016"></a>GB-016 | The Final Fantasy Legend / Makai Toushi SaGa | 魔界塔士 SaGa | 1989 | Square | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 以人、变异人、怪物三种成长和登塔世界构成短而硬的冒险，武器有使用次数。它是沙加首作，海外挂 Final Fantasy 名称但不属 FF 正传。 [系列专题](#series-22)。 |
| <a id="gb-017"></a>GB-017 | Final Fantasy Legend II / SaGa 2: Hihou Densetsu | SaGa 2：秘宝传说 | 1991 | Square | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 以 MAGI 秘宝和多个世界推进，队伍可加入怪物与机器人，成长方式随种族变化。它是沙加 2，剧情与装备耐久都比初代丰富。 [系列专题](#series-22)。 |
| <a id="gb-018"></a>GB-018 | Final Fantasy Legend III / SaGa 3: Jikuu no Hasha | SaGa 3：时空的霸者 | 1993 | Square | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 以过去、现在、未来航行和时间战争展开，角色可在人、兽、机械等形态间转化。系统较前两作更接近传统经验制，但仍属沙加 3。 [系列专题](#series-22)。 |
| <a id="gb-019"></a>GB-019 | Ninja Gaiden Shadow | 忍者龙剑传 GB：摩天楼决战 | 1991 | Tecmo | 4MB | 平台动作／横版／单屏／3D 平台 | 以摩天楼为舞台，使用刀、锁链与忍术推进短关卡。它由 Natsume 相关团队制作，气质接近赤影战士，而非 FC 忍龙直接缩小。 |
| <a id="gb-020"></a>GB-020 | Double Dragon II | 双截龙 II（GB） | 1991 | Technos | 4MB | 格斗／清版动作／清版动作与合作 | GB 版借二代角色与风格制作独立掌机关卡，动作和场景受小屏调整。不要与 FC 同名复仇版直接互换。 [系列专题](#series-08)。 |
| <a id="gb-021"></a>GB-021 | Teenage Mutant Ninja Turtles: Fall of the Foot Clan | 忍者神龟：脚帮的覆灭 | 1990 | Konami | 4MB | 动作冒险／探索／解谜／文字冒险 | GB 首部神龟游戏以短横版关卡、角色切换和救回同伴为核心。画面虽小，仍保留四龟不同武器手感。 [系列专题](#series-13)。 |
| <a id="gb-022"></a>GB-022 | Dragon Ball Z: Goku Hishouden / Goku Gekitouden | 龙珠 Z：悟空飞翔传／激斗传 | 1994–1995 | Bandai | 4MB | 动作冒险／探索／解谜／文字冒险 | 两部 GB 龙珠采用指令与时机输入表现战斗，分别覆盖赛亚人至弗利萨等段落。它们不是普通横版动作移植。 [系列专题](#series-16)。 |
| <a id="gb-023"></a>GB-023 | Saint Seiya: The Sanctuary / Saint Paradise | 圣斗士星矢（GB 合集） | 1990–1992 | Bandai | 4MB | 动作冒险／探索／解谜／文字冒险 | GB 圣斗士作品以十二宫等剧情、指令战斗和角色培养为主，日文菜单是主要门槛。两作应作为独立商品识别。 |
| <a id="gb-024"></a>GB-024 | Harvest Moon GB | 牧场物语 GB | 1997 | Natsume | 4MB | 模拟／音乐／派对／经营与生活模拟 | 把开垦、种植、动物和季节循环压缩到 GB，继承与工具升级提供长期目标。黑白掌机版系统简朴，不与 Mineral Town 混同。 [系列专题](#series-23)。 |
| <a id="gb-025"></a>GB-025 | Tetris | 俄罗斯方块 | 1989 | Nintendo | 1MB | 益智／休闲／落块与消除 | 下落的四格方块需要旋转、堆叠并消除整行，规则极简却有长期竞技深度。任天堂 GB 版随掌机捆绑，使俄罗斯方块成为便携游戏的全球现象。 [系列专题](#series-17)。 |
| <a id="gb-026"></a>GB-026 | Dr. Mario | 马力欧医生 | 1990 | Nintendo | 2MB | 益智／休闲／落块与消除 | 把彩色胶囊与病毒配对消除，玩法更接近连锁规划而非传统落块。它把马力欧角色包装用于益智游戏，并长期衍生多个版本。 [系列专题](#series-01)。 |
| <a id="gb-027"></a>GB-027 | Yoshi | 耀西的蛋 | 1991 | Nintendo | 2MB | 平台动作／横版／单屏／3D 平台 | 在四个落块槽中配对上下怪物，夹住相同怪物可整叠消除。它是有耀西形象的落块益智，不是平台动作或《耀西岛》。 [系列专题](#series-01)。 |
| <a id="gb-028"></a>GB-028 | Bomberman GB | 炸弹人 GB | 1996 | Hudson Soft | 2MB | 平台动作／横版／单屏／3D 平台 | 以掌机原创迷宫和道具推进，支持通过联机外设进行多人对战。不同 GB 型号版本与兼容模式需核对。 [系列专题](#series-10)。 |
| <a id="gb-029"></a>GB-029 | Donkey Kong (Game Boy) | 咚奇刚（GB） | 1994 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 开头重现街机四关，随后扩展为百余个搬钥匙解谜关卡；马力欧可倒立、后空翻和投掷敌人。大量动作后来进入 GBA 的马里奥对大金刚。 [系列专题](#series-01)。 |
| <a id="gb-030"></a>GB-030 | Kirby’s Dream Land | 星之卡比 | 1992 | Nintendo | 1MB | 平台动作／横版／单屏／3D 平台 | 卡比吸入敌人、鼓起身体飞行，但首作还没有后来标志性的复制能力。短小关卡与可调节难度让它成为 GB 早期适合新手的动作游戏。 [系列专题](#series-20)。 |
| <a id="gb-031"></a>GB-031 | Kirby’s Dream Land 2 | 星之卡比 2 | 1995 | Nintendo | 2MB | 平台动作／横版／单屏／3D 平台 | 复制能力与三位动物伙伴组合，同一能力会随伙伴改变形态。隐藏彩虹水滴和真结局鼓励探索，是黑白 GB 后期内容很扎实的一作。 [系列专题](#series-20)。 |
| <a id="gb-032"></a>GB-032 | Qix | Qix 领土分割 | 1990 | Nintendo | 0.5MB | 益智／休闲／规则解谜与短局 | 在空白区域画线封地，同时躲避沿边和场内移动的敌人；风险越高，单次圈地收益越大。任天堂掌机版把 Taito 的抽象街机规则带进便携短局。 |
| <a id="gb-033"></a>GB-033 | Mole Mania | 摩尔庄园 | 1996 | Nintendo | 1MB | 益智／休闲／规则解谜与短局 | 鼹鼠在地面与地下两层之间推球开路，障碍位置需要在两层共同规划。宫本茂参与制作的这款后期 GB 益智动作游戏常被忽略，但关卡完成度很高。 |
| <a id="gb-034"></a>GB-034 | Seiken Densetsu: Final Fantasy Gaiden / Final Fantasy Adventure | 圣剑传说：最终幻想外传 | 1991 | Square | 1MB | 角色扮演／动作 RPG | 以即时武器攻击、场景解谜和可成长角色展开冒险，是圣剑传说的 GB 起点。海外曾挂 Final Fantasy Adventure 名称，但并不属于最终幻想正传。 [系列专题](#series-40)。 |

---

### GG

<a id="platform-gg"></a>

Sega Game Gear 精选，优先原创掌机篇章、Compile 射击和经典休闲，不用普通移植作填满平台。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="gg-001"></a>GG-001 | Sonic the Hedgehog | 刺猬索尼克（GG） | 1991 | Sega | 1MB | 平台动作／横版／单屏／3D 平台 | 针对小屏重新安排关卡和视野，保留金环与高速动作但并非 MD 版的逐关移植。掌机版混沌翡翠获取方式也不同。 [系列专题](#series-25)。 |
| <a id="gg-002"></a>GG-002 | Sonic the Hedgehog 2 | 刺猬索尼克 2（GG） | 1992 | Sega | 2MB | 平台动作／横版／单屏／3D 平台 | GG／MS 版由 Aspect 制作，关卡、Boss 和取得翡翠的方式与 MD 版不同，难度更偏严格跳跃。应按独立掌机作品收藏。 [系列专题](#series-25)。 |
| <a id="gg-003"></a>GG-003 | Sonic Chaos | 索尼克与塔尔斯：混沌 | 1993 | Sega | 2MB | 平台动作／横版／单屏／3D 平台 | 索尼克与塔尔斯具备不同动作，塔尔斯可飞行，关卡因此有两套路线思路。GG 原创章节比移植作更能体现掌机节奏。 [系列专题](#series-25)。 |
| <a id="gg-004"></a>GG-004 | Sonic the Hedgehog: Triple Trouble | 索尼克与塔尔斯 2：三重麻烦 | 1994 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 索尼克与塔尔斯各有专属能力，纳克鲁斯与宝藏猎人方古共同参与争夺翡翠。关卡和道具围绕 GG 原创设计。 [系列专题](#series-25)。 |
| <a id="gg-005"></a>GG-005 | Shinobi II: The Silent Fury | 超级忍 II：沉默之怒 | 1992 | Sega | 2MB | 平台动作／横版／单屏／3D 平台 | 乔·武藏可使用五种忍者能力与多名同伴技能，关卡允许一定探索而非纯直线推进。它常被视为 GG 动作游戏的代表作。 |
| <a id="gg-006"></a>GG-006 | Castle of Illusion Starring Mickey Mouse | 米奇妙妙屋：幻影城堡 | 1991 | Sega | 2MB | 平台动作／横版／单屏／3D 平台 | 以投掷和踩击穿越童话关卡，GG 版对 MD 原作进行独立改编，操作温和、画面清晰，适合家庭短局。 [系列专题](#series-47)。 |
| <a id="gg-007"></a>GG-007 | Land of Illusion Starring Mickey Mouse | 米奇妙境：幻影大陆 | 1992 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 加入地图连接、能力道具和较丰富的互动，结构比前作更接近小型动作冒险。唐老鸭等迪士尼角色也参与剧情。 [系列专题](#series-47)。 |
| <a id="gg-008"></a>GG-008 | Shining Force Gaiden | 光明力量外传 | 1992 | Sega | 2MB | 战略／战棋／网格战术 | 以网格回合战斗和角色成长延续光明力量体系，是 GG 独占掌机篇章。较短战役仍保留队伍配置和地形判断。 [系列专题](#series-29)。 |
| <a id="gg-009"></a>GG-009 | Shining Force: The Sword of Hajya | 光明力量外传 II：邪神之剑 | 1993 | Sega | 2MB | 战略／战棋／网格战术 | 延续 GG 外传的战斗系统并增加双主角部队会合结构。它不是 MD《光明力量 II》的移植。 [系列专题](#series-29)。 |
| <a id="gg-010"></a>GG-010 | Shining Force Gaiden: Final Conflict | 光明力量外传：最终冲突 | 1995 | Sega | 4MB | 战略／战棋／网格战术 | 把 GG 外传故事与 MD 初代角色联系起来，保留探索、队伍培养和战棋战斗。日文文本是主要门槛。 [系列专题](#series-29)。 |
| <a id="gg-011"></a>GG-011 | Defenders of Oasis | 绿洲守护者 | 1992 | Sega | 2MB | 角色扮演／回合／迷宫／叙事 RPG | 以一千零一夜风格的王国冒险为背景，采用小队回合制和自动战斗辅助。它是 GG 少见且完成度较高的原创 JRPG。 |
| <a id="gg-012"></a>GG-012 | GG Aleste | GG 亚雷斯 | 1991 | Compile | 2MB | 射击／卷轴与弹幕射击 | 纵版射击使用可蓄力升级的主武器与多种副武器，敌弹速度和视野针对 GG 调整。Compile 的 Aleste 血脉使其成为掌机射击精品。 [系列专题](#series-89)。 |
| <a id="gg-013"></a>GG-013 | Power Strike II | 力量打击 II | 1993 | Compile | 2MB | 射击／卷轴与弹幕射击 | 高速纵版射击强调武器升级和贴近敌弹的风险回报，画面与敌群密度在 GG 上突出。它与 GG Aleste 同属 Compile 掌机射击高峰。 [系列专题](#series-89)。 |
| <a id="gg-014"></a>GG-014 | Wonder Boy: The Dragon’s Trap | 神奇男孩 III：龙之陷阱 | 1989 | Sega | 2MB | 平台动作／探索型动作 | 主角受诅咒后在多种动物形态间变身，能力用于返回旧区域开路。GG 版保留非线性结构，是早期“能力锁探索”的代表。 [系列专题](#series-36)。 |
| <a id="gg-015"></a>GG-015 | Columns | 宝石方块 | 1990 | Sega | 1MB | 益智／休闲／落块与消除 | 下落的三颗宝石可循环换序，横、竖、斜三颗同色即可消除。规则简单，连续消除与高度管理构成长期挑战，也是 GG 早期代表作。 |
| <a id="gg-016"></a>GG-016 | Puyo Puyo Tsu | 噗哟噗哟通（GG） | 1994 | Compile / Sega | 2MB | 益智／休闲／落块与消除 | 保留四连消除、连锁与对战干扰规则，掌机屏幕让局面更易掌握。它是经典休闲对战的 GG 版本。 [系列专题](#series-88)。 |
| <a id="gg-017"></a>GG-017 | Tails Adventure | 塔尔斯大冒险 | 1995 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 塔尔斯以飞行、道具和炸弹探索相互连接的海岛区域，速度不快，重点是能力解锁与路线发现。它区别于索尼克本篇的高速关卡。 |

---

### WS / WSC

<a id="platform-ws"></a>

WonderSwan 与 WonderSwan Color 合并展示，备注注明彩色版或日文门槛；以 Gunpey、风之少年与原创射击等真正体现平台价值的作品为主。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="ws-001"></a>WS-001 | Gunpey | Gunpey 线条接龙 | 1999 | Bandai | 1MB | 益智／休闲／规则解谜与短局 | 在竖排棋盘上上下交换线段，把折线接通左右边界即可消除。以作曲家横井军平命名的原创规则是 WS 首发阵容中最具代表性的益智作品。 |
| <a id="ws-002"></a>WS-002 | Klonoa: Moonlight Museum | 风之少年：月光博物馆 | 1999 | Namco | 2MB | 平台动作／横版／单屏／3D 平台 | 风弹抓敌、投掷与二段跳被用于单屏机关解谜，是系列首款掌机作品，也为后来 GBA《梦之帝国》奠定方向。 [系列专题](#series-64)。 |
| <a id="ws-003"></a>WS-003 | Mr. Driller | 钻地先生 | 1999 | Namco | 2MB | 益智／休闲／规则解谜与短局 | 向下钻穿彩色方块，连接的大块会坍塌，同时必须管理氧气。得分、路线和生存压力使短局非常紧凑。 [系列专题](#series-62)。 |
| <a id="ws-004"></a>WS-004 | Judgement Silversword: Rebirth Edition | 审判银剑：重生版 | 2001 | Qute / M-Kai | 2MB | 射击／卷轴与弹幕射击 | 高密度纵版射击使用贴身刀击与远程射击两套手段，关卡和 Boss 节奏在 WS 小屏上仍很清楚。它源自独立开发，是 WSC 射击名作。 |
| <a id="ws-005"></a>WS-005 | Pocket Fighter | 口袋战士 | 2000 | Capcom | 4MB | 格斗／清版动作／一对一与场地格斗 | 将街霸与恶魔战士角色 Q 版化，宝石强化招式、连锁操作相对简化。WSC 版保留了轻松对战与角色幽默。 |
| <a id="ws-006"></a>WS-006 | Buffers Evolution | Buffers Evolution | 1999 | Bandai | 2MB | 益智／休闲／规则解谜与短局 | 操纵可变形的生命体在场地中占领区域、吞噬对手，规则结合动作与抽象策略。它是 WS 原创阵容中很有实验气质的一作。 |
| <a id="ws-007"></a>WS-007 | Makaimura for WonderSwan | 魔界村 for WonderSwan | 1999 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 采用横屏与竖屏两类关卡，保留高难度跳跃、铠甲破损和武器选择。内容为掌机原创，不是旧作的简单合集。 [系列专题](#series-48)。 |
| <a id="ws-008"></a>WS-008 | Digimon: Battle Spirit | 数码宝贝：战斗精神 | 1999 | Bandai | 4MB | 格斗／清版动作／一对一与场地格斗 | 数码兽在平台场地中交战，通过攻击收集数据球并积累进化条件。操作直观，适合本地对战的轻量格斗。 [系列专题](#series-67)。 |
| <a id="ws-009"></a>WS-009 | One Piece: Grand Battle! Swan Colosseum | 海贼王：天鹅斗技场 | 2000 | Bandai | 4MB | 格斗／清版动作／一对一与场地格斗 | 在横向小场地进行角色对战，结合援助和简单连段。它属于早期海贼王掌机格斗，画面与角色动画利用 WSC 特色。 |
| <a id="ws-010"></a>WS-010 | Riviera: Yakusoku no Chi Riviera | 约束之地：利维艾拉 | 2002 | Bandai | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 以选择推进场景、有限行动点和回合制战斗构成冒险，资源取舍会影响探索结果。WSC 原版是 Sting 该系列的起点，日文阅读门槛较高。 |
| <a id="ws-011"></a>WS-011 | Final Fantasy I / II / IV | 最终幻想 I／II／IV（WS／WSC） | 2000–2002 | Square | 8MB | 角色扮演／回合／迷宫／叙事 RPG | WSC／WS 重制早期最终幻想，改良画面、界面与部分平衡；三作是独立商品，I／II 偏系列源头，IV 则有完整 ATB 群像剧。 [系列专题](#series-06)。 |
| <a id="ws-012"></a>WS-012 | Front Mission | 前线任务（WSC） | 2002 | Square | 4MB | 战略／战棋／网格战术 | 把 SFC 初代机甲战棋带到 WSC，保留部件损坏、武器射程与阵营战争。画面针对掌机重绘，日文菜单和剧情需要一定阅读基础。 [系列专题](#series-38)。 |

---

### NES / FC

<a id="platform-nes"></a>

8 位家用机与 Famicom 正式作品，中文俗称只作辅助识别，商品原名和实际发行主体为准。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="nes-001"></a>NES-001 | Super Mario Bros. | 超级马力欧兄弟 | 1985 | Nintendo | 0.25MB | 平台动作／横版／单屏／3D 平台 | 横版卷轴平台游戏，以奔跑惯性、踩敌和隐藏通道构成核心节奏。1985 年的家用机版把街机式短关卡整合为连续冒险，奠定了后来 2D 马力欧的基本语法。 [系列专题](#series-01)。 |
| <a id="nes-002"></a>NES-002 | Super Mario Bros. 2 (USA) | 超级马力欧兄弟 2（海外版） | 1988 | Nintendo | 0.25MB | 平台动作／横版／单屏／3D 平台 | 可操纵马力欧、路易吉、桃花公主与奇诺比奥，以拔萝卜、举起并投掷敌人取代传统踩敌。它源自《梦工厂心跳冒险》的角色替换版，1992 年又以《Super Mario USA》回流日本；与日版高难度 2 代不是同一作。 [系列专题](#series-01)。 |
| <a id="nes-003"></a>NES-003 | Super Mario Bros. 3 | 超级马力欧兄弟 3 | 1988 | Nintendo | 1MB | 平台动作／横版／单屏／3D 平台 | 大地图选关、变身道具与世界主题共同扩展了横版动作的结构，狸猫装和多样化 Boss 战尤其经典。它是 FC 后期技术与关卡设计的集大成者，而非普通续作换皮。 [系列专题](#series-01)。 |
| <a id="nes-004"></a>NES-004 | The Legend of Zelda | 塞尔达传说 | 1986 | Nintendo | 1MB | 动作冒险／探索／解谜／文字冒险 | 在开放地图上寻找迷宫、道具与隐藏入口，弱化固定路线并允许玩家自行摸索。电池存档让长期冒险在家用机上成立，也奠定了系列的探索传统。 [系列专题](#series-02)。 |
| <a id="nes-005"></a>NES-005 | Zelda II: The Adventure of Link | 塞尔达传说 2：林克的冒险 | 1987 | Nintendo | 1MB | 动作冒险／探索／解谜／文字冒险 | 把俯视大地图与横版战斗结合，加入经验值、魔法和村镇系统。它与系列其他作品风格差异很大，但经验成长与横版战斗后来仍影响了动作 RPG。 [系列专题](#series-02)。 |
| <a id="nes-006"></a>NES-006 | Mega Man | 洛克人 | 1987 | Capcom | 0.5MB | 平台动作／横版／单屏／3D 平台 | 首作建立八大 Boss 之前的六机器人选关、武器克制与取得能力循环。没有后来的滑铲和蓄力炮，精确跳跃与道具使用更重要。 [系列专题](#series-03)。 |
| <a id="nes-007"></a>NES-007 | Mega Man 2 | 洛克人 2 | 1989 | Capcom | 0.5MB | 平台动作／横版／单屏／3D 平台 | 元祖第 2 作延续 Boss 武器克制与选关，关卡机关、蓄力和辅助能力随代际逐步调整；可与同平台其他编号作比较关卡节奏。 [系列专题](#series-03)。 |
| <a id="nes-008"></a>NES-008 | Mega Man 3 | 洛克人 3 | 1990 | Capcom | 0.5MB | 平台动作／横版／单屏／3D 平台 | 元祖第 3 作延续 Boss 武器克制与选关，关卡机关、蓄力和辅助能力随代际逐步调整；可与同平台其他编号作比较关卡节奏。 [系列专题](#series-03)。 |
| <a id="nes-009"></a>NES-009 | Mega Man 4 | 洛克人 4 | 1992 | Capcom | 1MB | 平台动作／横版／单屏／3D 平台 | 元祖第 4 作延续 Boss 武器克制与选关，关卡机关、蓄力和辅助能力随代际逐步调整；可与同平台其他编号作比较关卡节奏。 [系列专题](#series-03)。 |
| <a id="nes-010"></a>NES-010 | Mega Man 5 | 洛克人 5 | 1992 | Capcom | 1MB | 平台动作／横版／单屏／3D 平台 | 元祖第 5 作延续 Boss 武器克制与选关，关卡机关、蓄力和辅助能力随代际逐步调整；可与同平台其他编号作比较关卡节奏。 [系列专题](#series-03)。 |
| <a id="nes-011"></a>NES-011 | Mega Man 6 | 洛克人 6 | 1994 | Capcom | 1MB | 平台动作／横版／单屏／3D 平台 | 元祖第 6 作延续 Boss 武器克制与选关，关卡机关、蓄力和辅助能力随代际逐步调整；可与同平台其他编号作比较关卡节奏。 [系列专题](#series-03)。 |
| <a id="nes-012"></a>NES-012 | Contra | 魂斗罗 | 1988 | Konami | 0.5MB | 射击／跑射与动作射击 | 以跑射、散弹等武器和双人协作挑战外星敌军，FC 版关卡经过重新设计。30 条命秘籍也使其成为共享卡带时代的文化记忆。 [系列专题](#series-04)。 |
| <a id="nes-013"></a>NES-013 | Super C | 超级魂斗罗 | 1990 | Konami | 0.5MB | 动作冒险／探索／解谜／文字冒险 | 延续双人跑射，并在部分关卡切换俯视角，敌群与 Boss 节奏更紧凑。它常被称作“魂斗罗 2”，但正式海外名是 Super C。 [系列专题](#series-04)。 |
| <a id="nes-014"></a>NES-014 | Ninja Gaiden | 忍者龙剑传 | 1989 | Tecmo | 0.5MB | 平台动作／横版／单屏／3D 平台 | FC 初代以高速跑跳、墙上借力与忍术副武器著称，过场动画在当年很有电影感。终盘难度尤其严苛。 |
| <a id="nes-015"></a>NES-015 | Ninja Gaiden II: The Dark Sword of Chaos | 忍者龙剑传 II：暗黑邪神剑 | 1990 | Tecmo | 0.5MB | 平台动作／横版／单屏／3D 平台 | 加入可复制本体动作的影分身，玩家可借站位让分身攻击高处敌人。黑暗剑与邪神剧情延续电影化过场。 |
| <a id="nes-016"></a>NES-016 | Ninja Gaiden III: The Ancient Ship of Doom | 忍者龙剑传 III：黄泉的方舟 | 1991 | Tecmo | 0.5MB | 平台动作／横版／单屏／3D 平台 | 取消二代影分身，改用新忍术和强化龙剑，角色移动与关卡结构再次调整。美版难度和接关限制与日版不同。 |
| <a id="nes-017"></a>NES-017 | Adventure Island | 高桥名人冒险岛 | 1988 | Hudson Soft | 0.25MB | 平台动作／横版／单屏／3D 平台 | 高桥名人之形象的主角用石斧、滑板和水果体力槽推进，关卡强调持续移动。初代与 Wonder Boy 有开发谱系关系。 |
| <a id="nes-018"></a>NES-018 | Adventure Island II | 高桥名人冒险岛 II | 1991 | Hudson Soft | 0.25MB | 平台动作／横版／单屏／3D 平台 | 加入四种恐龙伙伴和地图选关，能力用于不同地形，水果体力与武器系统延续。它比初代更富探索。 |
| <a id="nes-019"></a>NES-019 | Adventure Island 3 | 高桥名人冒险岛 3 | 1992 | Hudson Soft | 0.5MB | 平台动作／横版／单屏／3D 平台 | 扩充恐龙、道具与分支路线，主角为营救恋人穿越岛屿。库存和伙伴选择让关卡解法更多。 |
| <a id="nes-020"></a>NES-020 | Takahashi Meijin no Bouken Jima IV | 高桥名人冒险岛 IV | 1994 | Hudson Soft | 0.5MB | 动作冒险／探索／解谜／文字冒险 | FC 日本后期原创冒险岛，加入地图、道具与存档密码，结构比早期直线闯关更开放。日版文字不妨碍主要动作流程。 |
| <a id="nes-021"></a>NES-021 | Battle City | 坦克大战 | 1985 | Namco | 0.25MB | 动作冒险／探索／解谜／文字冒险 | 保护基地老鹰并用坦克击毁敌军，可双人合作，也能利用地形与升级改变防线。内置关卡编辑让它在 FC 时代很耐玩。 |
| <a id="nes-022"></a>NES-022 | Circus Charlie | 马戏团 | 1986 | Konami | 0.25MB | 平台动作／横版／单屏／3D 平台 | 以跳火圈、走绳、骑马和空中飞人等短项目组成街机式关卡，是 Konami 的早期作品，不应写成 Hudson。 |
| <a id="nes-023"></a>NES-023 | Shadow of the Ninja | 赤影战士／水上魂斗罗 | 1990 | Natsume | 0.5MB | 动作冒险／探索／解谜／文字冒险 | 两名忍者可用刀与锁镰配合闯关，强调双人合作和武器等级保持。Natsume 的像素、音乐与动作节奏使其成为 FC 后期佳作。 |
| <a id="nes-024"></a>NES-024 | Sangokushi | 三国志 | 1988 | Koei | 2MB | 战略／战棋／大战略与军团 | 以君主治理、外交与战争统一中国，是光荣历史模拟在家用机上的早期形态。菜单和数值较朴素，但奠定了系列基本循环。 [系列专题](#series-05)。 |
| <a id="nes-025"></a>NES-025 | Nakahara no Hasha: Sangoku Shouseiden | 三国志：中原之霸者 | 1988 | Namco | 2MB | 动作冒险／探索／解谜／文字冒险 | Namco 的 FC 三国战略游戏，与光荣《三国志》不是同一系列。武将和即时作战呈现使其在中文玩家中形成独立记忆。 |
| <a id="nes-026"></a>NES-026 | Sangokushi II: Haou no Tairiku | 三国志 II：霸王的大陆 | 1990 | Namco | 2MB | 战略／战棋／大战略与军团 | Namco《中原之霸者》的续作，保留三国君主争霸并深化战场指挥。“南晶科技制作”是常见误传，实际原厂为 Namco。 [系列专题](#series-05)。 |
| <a id="nes-027"></a>NES-027 | Final Fantasy | 最终幻想 | 1987 | Square | 2MB | 角色扮演／回合／迷宫／叙事 RPG | 四光之战士、水晶与职业选择建立系列原点，回合制以整队指令后统一结算。FC 版界面古老，但组队自由度和世界结构仍有历史价值。 [系列专题](#series-06)。 |
| <a id="nes-028"></a>NES-028 | Final Fantasy II | 最终幻想 II | 1988 | Square | 2MB | 角色扮演／回合／迷宫／叙事 RPG | 取消传统等级，武器、魔法与属性随使用成长，剧情更强调战争牺牲和人物轮换。熟练度需要理解，不能用无脑重复行动替代正常养成。 [系列专题](#series-06)。 |
| <a id="nes-029"></a>NES-029 | Final Fantasy III | 最终幻想 III | 1990 | Square | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 引入可切换职业与水晶解锁，后期队伍构筑空间大幅扩大。FC 原版没有 NDS 的 3D 重制演出与职业调整。 [系列专题](#series-06)。 |
| <a id="nes-030"></a>NES-030 | Dragon Quest | 勇者斗恶龙 | 1986 | Enix | 2MB | 角色扮演／回合／迷宫／叙事 RPG | 单主角旅行、回合制战斗和清晰成长曲线把电脑 RPG 转化为家用机可理解的形式。堀井雄二、鸟山明与椙山浩一的组合由此成为系列长期标识。 [系列专题](#series-07)。 |
| <a id="nes-031"></a>NES-031 | Dragon Quest II: Luminaries of the Legendary Line | 勇者斗恶龙 II：恶灵的众神 | 1987 | Enix | 2MB | 角色扮演／回合／迷宫／叙事 RPG | 队伍扩展为三人，地图与航海范围也显著放大，后期难度颇具挑战。它把初代单人冒险推进为真正的小队旅程。 [系列专题](#series-07)。 |
| <a id="nes-032"></a>NES-032 | Dragon Quest III: The Seeds of Salvation | 勇者斗恶龙 III：传说的开始 | 1988 | Enix | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 自由转职、昼夜变化和广阔世界让玩家自行安排成长路线，结局又把故事与初代世界相连。它在日本成为社会现象，也长期是系列最重要的历史节点之一。 [系列专题](#series-07)。 |
| <a id="nes-033"></a>NES-033 | Dragon Quest IV: Chapters of the Chosen | 勇者斗恶龙 IV：被引导的人们 | 1990 | Enix | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 各章先讲述不同伙伴的命运，最后汇入勇者一行，章节结构让群像塑造格外鲜明。NDS 版属于重新制作，并不存在原稿所写的 GBA 移植。 [系列专题](#series-07)。 |
| <a id="nes-034"></a>NES-034 | Double Dragon | 双截龙 | 1988 | Technos | 0.5MB | 格斗／清版动作／清版动作与合作 | FC 移植以模式 A 清版和模式 B 对战组成，经验解锁招式，缺少街机双人同时闯关。它是版本史重要作，但不是街机完全复刻。 [系列专题](#series-08)。 |
| <a id="nes-035"></a>NES-035 | Double Dragon II: The Revenge | 双截龙 II：复仇 | 1990 | Technos | 0.5MB | 格斗／清版动作／清版动作与合作 | 改用左右方向攻击与更流畅招式，关卡和剧情扩展复仇主题。FC 版支持双人合作，通常比初代更适合家庭游玩。 [系列专题](#series-08)。 |
| <a id="nes-036"></a>NES-036 | Double Dragon III: The Sacred Stones | 双截龙 III：圣石 | 1991 | Technos | 0.5MB | 格斗／清版动作／清版动作与合作 | 环球旅程可招募陈与柳生，角色死亡会影响后续可用阵容。节奏与判定评价不如 II，仅作系列完整性例外保留。 [系列专题](#series-08)。 |
| <a id="nes-037"></a>NES-037 | 1942 | 1942 | 1984 | Capcom | 0.25MB | 动作冒险／探索／解谜／文字冒险 | 纵版空战以翻滚回避和双机编队强化火力，舞台围绕太平洋战争抽象化展开。Capcom 的 FC 移植保留了街机基本节奏。 |
| <a id="nes-038"></a>NES-038 | 1943: The Battle of Midway | 1943 | 1988 | Capcom | 0.5MB | 动作冒险／探索／解谜／文字冒险 | 加入能量槽、蓄力攻击与机体升级，生存不再只是一次中弹结束。它让 1942 的简单射击有了资源经营。 |
| <a id="nes-039"></a>NES-039 | Rush’n Attack | 绿色兵团 | 1987 | Konami | 0.5MB | 射击／跑射与动作射击 | 步兵以刺刀近战为主，有限次数的特殊武器用于突破火力点。FC 版双人模式与街机版不同，俗称绿色兵团。 |
| <a id="nes-040"></a>NES-040 | Life Force / Salamander | 沙罗曼蛇 | 1988 | Konami | 0.5MB | 射击／卷轴与弹幕射击 | 横纵关卡交替，采用即时拾取强化而非 Gradius 的力量槽选择；沙罗曼蛇的有机场景突出。FC 与街机版本在系统和双人模式上有差异。 [系列专题](#series-09)。 |
| <a id="nes-041"></a>NES-041 | Gradius | 宇宙巡航机 | 1986 | Konami | 0.5MB | 射击／卷轴与弹幕射击 | 力量槽让玩家自行决定 Speed、Option、Laser 等强化顺序，死亡会损失整套火力。FC 移植保留核心关卡与隐藏密码。 [系列专题](#series-09)。 |
| <a id="nes-042"></a>NES-042 | Bomberman | 炸弹人 | 1985 | Hudson Soft | 0.25MB | 平台动作／横版／单屏／3D 平台 | 在单屏砖墙迷宫放炸弹开路、消灭敌人并寻找出口与道具。FC 初代为单人关卡，系列后来才突出多人对战。 [系列专题](#series-10)。 |
| <a id="nes-043"></a>NES-043 | Bomberman II | 炸弹人 II | 1991 | Hudson Soft | 0.25MB | 平台动作／横版／单屏／3D 平台 | 增加新道具、陷阱和关卡结构，并强化多人方向；爆炸连锁仍会困住自己。它是 FC 正式续作。 [系列专题](#series-10)。 |
| <a id="nes-044"></a>NES-044 | Castlevania | 恶魔城 | 1987 | Konami | 1MB | 平台动作／横版／单屏／3D 平台 | 西蒙以固定节奏挥鞭、副武器和精准跳跃穿越六关，圣水与怀表等资源决定 Boss 难度。它奠定旧式恶魔城的动作约束。 [系列专题](#series-11)。 |
| <a id="nes-045"></a>NES-045 | Castlevania II: Simon’s Quest | 恶魔城 II：西蒙的冒险 | 1988 | Konami | 1MB | 平台动作／横版／单屏／3D 平台 | 改为昼夜循环、村镇提示、经验与开放地图，德古拉遗骸收集取代直线关卡。隐晦谜题需要攻略，中文或注释版本能降低门槛。 [系列专题](#series-11)。 |
| <a id="nes-046"></a>NES-046 | Castlevania III: Dracula’s Curse | 恶魔城 III：德古拉的诅咒 | 1990 | Konami | 2MB | 平台动作／横版／单屏／3D 平台 | 分支路线与赛法、格兰特、阿鲁卡多三名伙伴改变动作和解法。它在 FC 上扩充初代体系，而非月下式自由地图。 [系列专题](#series-11)。 |
| <a id="nes-047"></a>NES-047 | Nekketsu Kouha Kunio-kun | 热血硬派国夫君 | 1987 | Technos | 0.5MB | 动作冒险／探索／解谜／文字冒险 | 国夫君在街头以拳脚与投技推进，是热血系列的 FC 起点。它与 River City Ransom 的开放街区 RPG 结构不同。 [系列专题](#series-12)。 |
| <a id="nes-048"></a>NES-048 | Downtown Nekketsu Koushinkyoku: Soreyuke Daiundoukai | 热血行进曲：前进大运动会 | 1990 | Technos | 0.5MB | 动作冒险／探索／解谜／文字冒险 | 四校队伍在越野、格斗等运动项目中竞争，规则允许攻击干扰。多人轮玩比单人更能体现热血运动会特色。 [系列专题](#series-12)。 |
| <a id="nes-049"></a>NES-049 | Nekketsu Kakutou Densetsu | 热血格斗传说 | 1992 | Technos | 1MB | 动作冒险／探索／解谜／文字冒险 | 热血角色在场地中使用拳脚、武器与机关混战，队伍配合和随机事件增强派对感。它是 FC 后期多人对战佳作。 [系列专题](#series-12)。 |
| <a id="nes-050"></a>NES-050 | River City Ransom / Downtown Nekketsu Monogatari | 热血物语 | 1990 | Technos | 1MB | 动作冒险／探索／解谜／文字冒险 | 在开放街区战斗、购物并提升属性，食物与书籍形成轻量 RPG 成长。双人合作与自由探索使其区别于普通清版。 [系列专题](#series-12)。 |
| <a id="nes-051"></a>NES-051 | Nintendo World Cup / Nekketsu Koukou Dodgeball-bu Soccer-hen | 热血足球 | 1990 | Technos | 0.5MB | 动作冒险／探索／解谜／文字冒险 | 足球规则被简化并加入必杀射门和粗暴身体对抗，热血版与海外 Nintendo World Cup 的呈现不同。 [系列专题](#series-12)。 |
| <a id="nes-052"></a>NES-052 | Nekketsu! Street Basket: Ganbare Dunk Heroes | 热血街头篮球 | 1993 | Technos | 0.5MB | 竞速／体育／体育与运动 | 热血角色以二对二篮球、必杀投篮和场地干扰对战，规则允许直接攻击。它是运动与动作混合的 FC 派对作。 [系列专题](#series-12)。 |
| <a id="nes-053"></a>NES-053 | Super Dodge Ball / Nekketsu Koukou Dodgeball-bu | 热血躲避球 | 1989 | Technos | 0.5MB | 竞速／体育／体育与运动 | 以闪避、接球和必杀投球淘汰对手，场地与队伍各有特色。热血躲避球把体育规则转成直接对战。 [系列专题](#series-12)。 |
| <a id="nes-054"></a>NES-054 | Teenage Mutant Ninja Turtles | 忍者神龟 | 1989 | Konami | 0.5MB | 动作冒险／探索／解谜／文字冒险 | FC 首作在俯视大地图与横版关卡间切换，四龟可随时切换且生命独立。水坝拆弹等关卡以高难度闻名。 [系列专题](#series-13)。 |
| <a id="nes-055"></a>NES-055 | Teenage Mutant Ninja Turtles II: The Arcade Game | 忍者神龟 II：街机移植版 | 1990 | Konami | 0.5MB | 格斗／清版动作／清版动作与合作 | 把街机清版移植到 FC，并追加新关卡与 Boss；受硬件限制同屏人数减少，但合作节奏仍保留。 [系列专题](#series-13)。 |
| <a id="nes-056"></a>NES-056 | Teenage Mutant Ninja Turtles III: The Manhattan Project | 忍者神龟 III：曼哈顿计划 | 1992 | Konami | 0.5MB | 格斗／清版动作／清版动作与合作 | FC 原创清版续作，四龟加入各自特殊技，关卡围绕纽约展开。它不是街机 Turtles in Time 的移植。 [系列专题](#series-13)。 |
| <a id="nes-057"></a>NES-057 | Chip ’n Dale: Rescue Rangers | 松鼠大作战 | 1990 | Capcom | 0.5MB | 平台动作／横版／单屏／3D 平台 | 两只松鼠搬箱子与场景物件攻击，可双人合作也能互相扔掷。关卡短小、操作温和，是 FC 家庭合作代表。 |
| <a id="nes-058"></a>NES-058 | Chip ’n Dale: Rescue Rangers 2 | 松鼠大作战 2 | 1994 | Capcom | 0.5MB | 平台动作／横版／单屏／3D 平台 | 延续搬运与投掷机制，增加更丰富机关和 Boss，流程比前作更完整。FC 后期发行量使其原版较稀缺。 |
| <a id="nes-059"></a>NES-059 | DuckTales | 唐老鸭历险记 | 1989 | Capcom | 0.5MB | 平台动作／横版／单屏／3D 平台 | 史高治用拐杖弹跳攻击与越障，非线性选关和隐藏宝藏鼓励探索。Capcom 的迪士尼改编以音乐和关卡设计著称。 |
| <a id="nes-060"></a>NES-060 | DuckTales 2 | 唐老鸭历险记 2 | 1993 | Capcom | 0.5MB | 平台动作／横版／单屏／3D 平台 | 保留拐杖动作并增加地图、升级和更多剧情段落，体量较小但完成度不错。它是 FC 后期正式续作。 |
| <a id="nes-061"></a>NES-061 | Captain Tsubasa | 天使之翼 | 1988 | Tecmo | 2MB | 竞速／体育／体育与运动 | 以指令选择传球、射门与过人，将足球比赛转为带必杀演出的角色扮演。FC 首作系统较简朴，主要覆盖少年篇。 |
| <a id="nes-062"></a>NES-062 | Captain Tsubasa II: Super Striker | 天使之翼 II：超级射手 | 1990 | Tecmo | 2MB | 竞速／体育／体育与运动 | 扩大球员培养、必杀技与赛程，比赛中的指令和资源管理更完整。大量剧情文本使中文化特别有价值。 |
| <a id="nes-063"></a>NES-063 | Metal Max | 重装机兵 | 1991 | Crea-Tech | 4MB | 角色扮演／动作 RPG | 在核战后废土自由接取赏金、改造战车，也可以随时回归猎人的平凡生活。人车双战斗与开放式目标让它在中文 RPG 玩家中形成独特口碑，与宝可梦毫无系列关系。 [系列专题](#series-14)。 |
| <a id="nes-064"></a>NES-064 | Fire Emblem Gaiden | 火焰之纹章外传 | 1992 | Nintendo | 2MB | 战略／战棋／网格战术 | 采用双主角路线、可探索村镇与地牢，系统和系列其他作品差异较大。它是 1992 年 FC 第二作，后来重制为《回声：另一位英雄王》。 [系列专题](#series-15)。 |
| <a id="nes-065"></a>NES-065 | Tenchi wo Kurau / Destiny of an Emperor | 吞食天地 | 1990 | Capcom | 4MB | 角色扮演／回合／迷宫／叙事 RPG | Capcom 把三国题材做成队伍制 RPG，以兵力代替传统生命并围绕武将招募推进。它是正式商业作品，不是同人改版。 [系列专题](#series-05)。 |
| <a id="nes-066"></a>NES-066 | Tenchi wo Kurau II: Shokatsu Koumei Den | 吞食天地 II：诸葛孔明传 | 1991 | Capcom | 4MB | 格斗／清版动作／清版动作与合作 | 延续 Capcom 三国 RPG，围绕诸葛亮相关剧情扩展队伍与阵形。中文传播广泛，但应与同名街机清版游戏区分。 [系列专题](#series-05)。 |
| <a id="nes-067"></a>NES-067 | Feng Shen Bang: Fu Mo San Jian Xia | 封神榜：伏魔三剑侠 | 1995 | 全崴资讯 | 2MB | 角色扮演／回合／迷宫／叙事 RPG | 全崴资讯原创中文 FC RPG，以哪吒等封神人物组队冒险。它是中文原创商品，不应写成日本游戏的汉化版。 |
| <a id="nes-068"></a>NES-068 | Saiyuuki World | 西游记世界 | 1988 | Jaleco | 1MB | 平台动作／横版／单屏／3D 平台 | Jaleco 的西游记题材横版动作，以武器升级和关卡探索推进。Wonder Boy in Monster Land 的开发谱系与其相近。 |
| <a id="nes-069"></a>NES-069 | The Goonies | 七宝奇谋 | 1986 | Konami | 0.5MB | 平台动作／横版／单屏／3D 平台 | 在相互连通的场景中救队友、找钥匙并解锁门，以解谜路线而非单纯打斗为主。FC 版与街机 PlayChoice 版本不同。 |
| <a id="nes-070"></a>NES-070 | Blaster Master | 超惑星战记 | 1988 | Sunsoft | 1MB | 平台动作／横版／单屏／3D 平台 | 战车横版探索与人物俯视迷宫交替，获得升级后返回旧区域开路。Sunsoft 将两套视角与地图成长紧密结合。 |
| <a id="nes-071"></a>NES-071 | Journey to Silius | 星际魂斗罗／西利乌斯之旅 | 1990 | Sunsoft | 0.5MB | 射击／跑射与动作射击 | Sunsoft 的科幻跑射作品，以多武器和优秀芯片音乐著称。它并非魂斗罗官方续作，“星际魂斗罗”只是中文俗称。 |
| <a id="nes-072"></a>NES-072 | Jackal | 赤色要塞 | 1988 | Konami | 0.5MB | 射击／跑射与动作射击 | 驾驶吉普车营救战俘，机枪与榴弹可分别应对步兵和重火力，双人协作很有特色。车辆移动与射击方向的关系是操作关键。 |
| <a id="nes-073"></a>NES-073 | TwinBee | 兵蜂 | 1986 | Konami | 0.25MB | 射击／卷轴与弹幕射击 | 击落云朵取得铃铛，连续射击改变颜色并触发不同强化，双人可合体或互投。明亮角色和 bells 规则形成 Konami 的可爱射击支线。 [系列专题](#series-09)。 |
| <a id="nes-074"></a>NES-074 | The Legend of Kage | 影子传说 | 1985 | Taito | 0.5MB | 平台动作／横版／单屏／3D 平台 | 忍者可在树林与城郭间高跳，以刀和手里剑迎战敌人。Taito 街机移植的动作轻盈，短循环适合反复挑战。 |
| <a id="nes-075"></a>NES-075 | Ninja JaJaMaru-kun | 忍者茶茶丸 | 1985 | Jaleco | 0.5MB | 平台动作／横版／单屏／3D 平台 | 小忍者用忍具和踩击在单屏关卡清除妖怪，青蛙奖励与移动平台改变路线。Jaleco 的 FC 动作不是体育游戏。 |
| <a id="nes-076"></a>NES-076 | Batman: The Video Game | 蝙蝠侠 | 1990 | Sunsoft | 0.5MB | 平台动作／横版／单屏／3D 平台 | 蝙蝠侠可蹬墙跳并使用三种副武器，敌人位置和节奏要求精确。Sunsoft 的画面与芯片音乐使其成为 FC 动作佳作。 |
| <a id="nes-077"></a>NES-077 | Doraemon | 哆啦 A 梦 | 1986 | Hudson Soft | 0.5MB | 动作冒险／探索／解谜／文字冒险 | Hudson 的哆啦 A 梦 FC 游戏按不同篇章切换动作与冒险规则，道具和角色能力用于关卡。日文菜单不妨碍主要流程。 |
| <a id="nes-078"></a>NES-078 | Dragon Ball: Daimaou Fukkatsu | 龙珠：大魔王复活 | 1988 | Bandai | 1MB | 角色扮演／回合／迷宫／叙事 RPG | 以卡牌数值和移动格推进短笛大魔王篇，战斗采用指令与卡牌组合。它是 Bandai 早期龙珠 RPG，不是格斗游戏。 [系列专题](#series-16)。 |
| <a id="nes-079"></a>NES-079 | Saint Seiya: Ougon Densetsu | 圣斗士星矢：黄金传说 | 1987 | Bandai | 2MB | 动作冒险／探索／解谜／文字冒险 | 围绕黄金十二宫安排角色战斗与剧情选择，小宇宙等数值影响行动。Bandai 的 FC 改编以文字与指令为主。 |
| <a id="nes-080"></a>NES-080 | Hokuto no Ken | 北斗神拳 | 1986 | Toei Animation | 1MB | 动作冒险／探索／解谜／文字冒险 | 以拳四郎横向推进并迎战北斗神拳角色，FC 初代属于早期动作改编。系列后续 FC 作品系统不同，不能统称同一版本。 |
| <a id="nes-081"></a>NES-081 | Lode Runner | 淘金者 | 1984 | Hudson Soft | 0.25MB | 动作冒险／探索／解谜／文字冒险 | 通过挖掘左右地面困住守卫、收集金子并抵达出口，核心是路线规划而非战斗。关卡编辑器延长了作品寿命。 |
| <a id="nes-082"></a>NES-082 | Ice Climber | 敲冰块 | 1985 | Nintendo | 0.25MB | 平台动作／横版／单屏／3D 平台 | 用锤子击碎头顶冰层并逐层登山，跳跃惯性独特。双角色波波与娜娜后来也因大乱斗扩大了认知度。 |
| <a id="nes-083"></a>NES-083 | Excitebike | 越野机车 | 1985 | Nintendo | 0.25MB | 动作冒险／探索／解谜／文字冒险 | 越野摩托需要控制落地姿态与引擎温度，赛道编辑器在 FC 早期很有创意。它展示了简单规则与物理手感结合的魅力。 |
| <a id="nes-084"></a>NES-084 | Yie Ar Kung-Fu | 功夫 | 1985 | Konami | 0.25MB | 动作冒险／探索／解谜／文字冒险 | 在固定场地与不同招式对手进行一对一格斗，是早期对战动作的重要作品，但系统不能直接等同后来的《街霸 II》。 |
| <a id="nes-085"></a>NES-085 | Mario Bros. | 马力欧兄弟 | 1985 | Nintendo | 0.25MB | 平台动作／横版／单屏／3D 平台 | 在固定水管场景从下方撞击地板再踢走敌人，双人可协作也可争抢。它是街机原点，与卷轴 Super Mario Bros. 不同。 [系列专题](#series-01)。 |
| <a id="nes-086"></a>NES-086 | Donkey Kong | 咚奇刚 | 1983 | Nintendo | 0.25MB | 平台动作／横版／单屏／3D 平台 | FC 移植街机爬梯、跨锤和拆铆钉关卡，Jumpman 营救宝琳。它是马力欧角色史起点，不包含 GB 的百关扩展。 [系列专题](#series-01)。 |
| <a id="nes-087"></a>NES-087 | Balloon Fight | 气球大战 | 1985 | Nintendo | 0.25MB | 平台动作／横版／单屏／3D 平台 | 利用拍翼惯性与气球浮力进行空中对战，既可合作也可互相干扰。其物理手感与街机《Joust》有渊源。 |
| <a id="nes-088"></a>NES-088 | Tetris | 俄罗斯方块 | 1988 | Nintendo | 0.125MB | 益智／休闲／落块与消除 | 下落的四格方块需要旋转、堆叠并消除整行，规则极简却有长期竞技深度。任天堂 GB 版随掌机捆绑，使俄罗斯方块成为便携游戏的全球现象。 [系列专题](#series-17)。 |
| <a id="nes-089"></a>NES-089 | Metroid | 密特罗德 | 1986 | Nintendo | 1MB | 平台动作／探索型动作 | 扮演萨姆斯在泽贝斯星非线性探索，靠新能力打开旧区域。它把孤独氛围、地图记忆与能力锁结合起来，是“密特罗德式探索”的源头。 [系列专题](#series-18)。 |
| <a id="nes-090"></a>NES-090 | Super Mario Bros.: The Lost Levels | 超级马力欧兄弟 2（日版） | 1986 | Nintendo | 0.25MB | 平台动作／横版／单屏／3D 平台 | 延续初代引擎但加入毒蘑菇、强风与更苛刻的跳跃，是 1986 年日本原版《超级马力欧兄弟 2》。海外长期未单独发行，后经《Super Mario All-Stars》以“The Lost Levels”广为人知。 [系列专题](#series-01)。 |
| <a id="nes-091"></a>NES-091 | Crystalis | 天神之剑 | 1990 | SNK | 0.5MB | 角色扮演／回合／迷宫／叙事 RPG | 在科幻与奇幻混合的世界以四把元素剑解谜和战斗，蓄力等级影响攻击。SNK 的这款动作 RPG 也常译作天神之剑。 |
| <a id="nes-092"></a>NES-092 | Gimmick! | 吉米克 | 1992 | Sunsoft | 0.5MB | 平台动作／横版／单屏／3D 平台 | 主角 Yumetarō 可生成星星用于攻击和站立，物理轨迹同时服务战斗与解谜。Sunsoft 的音源芯片与物理设计使其成为 FC 后期名作。 |
| <a id="nes-093"></a>NES-093 | Metal Gear | 合金装备 | 1987 | Konami | 0.5MB | 射击／跑射与动作射击 | Snake 潜入 Outer Heaven，以纸箱、无线电、敌人视线和装备选择避开正面冲突。FC 移植与 MSX 原版在地图和 Boss 上差异明显。 [系列专题](#series-19)。 |
| <a id="nes-094"></a>NES-094 | Kirby’s Adventure | 星之卡比：梦之泉物语 | 1993 | Nintendo | 1MB | 平台动作／横版／单屏／3D 平台 | 首次引入复制能力，并通过大地图、小游戏与秘密开关扩展关卡。FC 后期的色彩与动画让它成为卡比体系成型的关键作。 [系列专题](#series-20)。 |
| <a id="nes-095"></a>NES-095 | Fire Emblem: Shadow Dragon and the Blade of Light | 火焰之纹章：暗黑龙与光之剑 | 1990 | Nintendo | 1MB | 战略／战棋／网格战术 | 马尔斯复国战争把单位职业、武器耐久和永久阵亡结合，是系列首作。界面与移动节奏古老，保留它是为了理解整个战棋谱系。 [系列专题](#series-15)。 |
| <a id="nes-096"></a>NES-096 | Dai-2-Ji Super Robot Taisen | 第 2 次超级机器人大战 | 1991 | Banpresto | 1MB | 战略／战棋／网格战术 | 高达、魔神与盖塔等机体进入网格战棋，精神指令和改造开始形成系列基本循环。它在中文圈的中文化传播尤其广。 [系列专题](#series-39)。 |

---

### SNES / SFC

<a id="platform-snes"></a>

16 位任天堂平台，覆盖平台动作、JRPG、战棋、射击和合作游戏；特殊芯片作品按核心兼容情况逐一测试。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="snes-001"></a>SNES-001 | Super Mario World | 超级马力欧世界 | 1991 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 披风飞行、耀西与多出口关卡构成探索主轴，星路与特殊世界奖励反复挑战。它用大地图把 16 位马力欧的关卡网络连成整体。 [系列专题](#series-01)。 |
| <a id="snes-002"></a>SNES-002 | Super Mario World 2: Yoshi’s Island | 超级马力欧世界 2：耀西岛 | 1995 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 耀西背蛋作战并保护婴儿马力欧，受伤后的倒计时取代传统生命条。变身、收集与手绘风格让它成为独立主线而非普通外传。 [系列专题](#series-01)。 |
| <a id="snes-003"></a>SNES-003 | Super Mario RPG: Legend of the Seven Stars | 超级马力欧 RPG：七星传说 | 1996 | Square | 8MB | 平台动作／横版／单屏／3D 平台 | Nintendo 与 Square 合作，把等距探索、动作指令回合战斗和七颗星星旅程结合。时机按键强化攻防，幽默角色也扩展了马力欧世界。 [系列专题](#series-01)。 |
| <a id="snes-004"></a>SNES-004 | The Legend of Zelda: A Link to the Past | 塞尔达传说：众神的三角力量 | 1991 | Nintendo | 8MB | 动作冒险／探索／解谜／文字冒险 | 光明与黑暗两个世界互相映射，玩家利用世界切换改变道路与谜题。它重新整理并固定了“村庄—迷宫—关键道具”的系列结构，是 2D 塞尔达的核心参照。 [系列专题](#series-02)。 |
| <a id="snes-005"></a>SNES-005 | Super Metroid | 超级密特罗德 | 1994 | Nintendo | 8MB | 平台动作／探索型动作 | 以非线性地图、能力回环和环境叙事构成高度统一的探索体验。它没有依赖长对白，却通过场景与结局建立强烈情感，是动作冒险和后续“银河城”设计的重要范本。 [系列专题](#series-18)。 |
| <a id="snes-006"></a>SNES-006 | Chrono Trigger | 超时空之钥 | 1995 | Square | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 穿越时空改变不同年代的事件，战斗在场景内展开并强调双人、三人协力技。鸟山明人设、坂口博信与堀井雄二等阵容以及多结局设计，使其成为 16 位 RPG 的协作高峰。 |
| <a id="snes-007"></a>SNES-007 | Final Fantasy IV | 最终幻想 IV | 1991 | Square | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 以塞西尔从黑骑士到圣骑士的转变推动群像剧，角色会随剧情加入、离队。ATB 让回合指令与等待时间结合，系列由此形成更强的战斗节奏。 [系列专题](#series-06)。 |
| <a id="snes-008"></a>SNES-008 | Final Fantasy V | 最终幻想 V | 1992 | Square | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 职业可自由切换，已学技能又能跨职业装配，构筑空间远大于单纯升级。轻松冒险外壳下是深度很高的系统型 RPG，GBA 版还追加了职业与迷宫。 [系列专题](#series-06)。 |
| <a id="snes-009"></a>SNES-009 | Final Fantasy VI | 最终幻想 VI | 1994 | Square | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 多主角群像围绕魔法复兴与凯夫卡的野心展开，中期世界剧变重新组织探索目标。魔石、角色固有技与宏大配乐共同代表 Square 的 2D 制作高峰。 [系列专题](#series-06)。 |
| <a id="snes-010"></a>SNES-010 | Dragon Quest V: Hand of the Heavenly Bride | 勇者斗恶龙 V：天空的新娘 | 1992 | Enix | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 故事跨越主人公少年、成家与为人父的阶段，怪物收服也与家族主题结合。以人生阶段而非单纯王国危机推动叙事，是它最突出的历史地位。 [系列专题](#series-07)。 |
| <a id="snes-011"></a>SNES-011 | Dragon Quest VI: Realms of Revelation | 勇者斗恶龙 VI：幻之大地 | 1995 | Enix | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 梦与现实两个世界互相折射，失忆与身份追寻贯穿旅程。转职系统与双世界探索体量庞大，NDS 版是较方便的完整体验方式。 [系列专题](#series-07)。 |
| <a id="snes-012"></a>SNES-012 | Fire Emblem: Mystery of the Emblem | 火焰之纹章：纹章之谜 | 1994 | Nintendo | 8MB | 战略／战棋／网格战术 | 第一部重制暗黑龙与光之剑，第二部展开英雄战争，共享马尔斯与阿卡内亚世界。SFC 版系统、地图与 FC 初代不同。 [系列专题](#series-15)。 |
| <a id="snes-013"></a>SNES-013 | Fire Emblem: Genealogy of the Holy War | 火焰之纹章：圣战之系谱 | 1996 | Nintendo | 16MB | 战略／战棋／网格战术 | 横跨父子两代的战争与血统悲剧展开在大型地图上，恋爱配对会影响子代能力。它的史诗结构和继承系统在系列中独树一帜。 [系列专题](#series-15)。 |
| <a id="snes-014"></a>SNES-014 | Fire Emblem: Thracia 776 | 火焰之纹章：多拉基亚 776 | 1999 | Nintendo | 16MB | 战略／战棋／网格战术 | 作为《圣战之系谱》的间章聚焦里夫，加入疲劳、俘虏与营救等更严苛机制。资源紧张与逃生关卡使它以硬核著称。 [系列专题](#series-15)。 |
| <a id="snes-015"></a>SNES-015 | Tactics Ogre: Let Us Cling Together | 皇家骑士团：命运之轮 | 1995 | Square | 16MB | 战略／战棋／网格战术 | 以 WT 决定单位行动顺序，职业、阵营与法律／混沌路线改变战争和同伴命运。SFC 原作与 PSP 命运之轮的系统、画面和追加剧情不同。 [系列专题](#series-37)。 |
| <a id="snes-016"></a>SNES-016 | Langrisser | 梦幻模拟战 | 1991 | Ascii | 8MB | 战略／战棋／网格战术 | 佣兵指挥官带领兵种单位作战，指挥范围、兵种克制和转职决定战线。MD 初代是 Warsong 的日版原作。 [系列专题](#series-29)。 |
| <a id="snes-017"></a>SNES-017 | Langrisser II / Der Langrisser | 梦幻模拟战 II | 1994–1995 | Ascii | 16MB | 战略／战棋／网格战术 | 二代扩展艾尔文与光辉后裔的战争，Der 则重排剧情并提供帝国、黑暗等多路线。两者不是完全相同的剧本版本。 [系列专题](#series-29)。 |
| <a id="snes-018"></a>SNES-018 | Front Mission: Gun Hazard | 前线任务：枪之危机 | 1996 | Square | 8MB | 动作冒险／探索／解谜／文字冒险 | 把前线任务机甲带入横版动作，驾驶员可离机，部件与武器可自由改装。它由 Square 与 Omiya Soft 等合作开发，不是传统网格战棋。 [系列专题](#series-38)。 |
| <a id="snes-019"></a>SNES-019 | Dai-3-Ji Super Robot Taisen | 第 3 次超级机器人大战 | 1993 | Bandai | 8MB | 战略／战棋／网格战术 | 以 DC 战争和跨作品冲突组织战役，机体改造、精神指令与说服系统继续发展。SFC 早期作品界面朴素，却是旧系列剧情的重要节点。 [系列专题](#series-39)。 |
| <a id="snes-020"></a>SNES-020 | Super Robot Taisen EX | 超级机器人大战 EX | 1994 | Bandai | 8MB | 战略／战棋／网格战术 | 以魔装机神相关角色为中心，采用多章节视角与较紧凑战役。它是 SFC 外传式作品，不应与后续完整 OG 编年史混为一谈。 [系列专题](#series-39)。 |
| <a id="snes-021"></a>SNES-021 | Dai-4-Ji Super Robot Taisen | 第 4 次超级机器人大战 | 1995 | Bandai | 16MB | 战略／战棋／网格战术 | 加入原创主人公、生日血型精神和较完整原创路线，是许多旧系列角色的阶段收束。SFC 原版与后来的 F／F Final 不是同一镜像。 [系列专题](#series-39)。 |
| <a id="snes-022"></a>SNES-022 | Super Robot Taisen Gaiden: Masou Kishin – The Lord of Elemental | 超级机器人大战外传：魔装机神 | 1996 | Bandai | 8MB | 战略／战棋／网格战术 | 聚焦拉·基亚斯与魔装机神，弱化跨版权大集结，改为原创世界观和地形魔法战斗。它是 OG 前史的重要源头。 [系列专题](#series-39)。 |
| <a id="snes-023"></a>SNES-023 | Secret of Mana / Seiken Densetsu 2 | 圣剑传说 2 | 1993 | Square | 16MB | 角色扮演／动作 RPG | 环形菜单管理道具与魔法，实时战斗支持多人合作。音乐和世界氛围突出，系统与后来的 Trials of Mana 又有所不同。 [系列专题](#series-40)。 |
| <a id="snes-024"></a>SNES-024 | Trials of Mana / Seiken Densetsu 3 | 圣剑传说 3 | 1995 | Square | 16MB | 角色扮演／动作 RPG | 六名主角决定开场与部分路线，职业转职和多人动作战斗提供重玩价值。SFC 原版长期未正式海外发行，后来才以 Trials of Mana 推出。 [系列专题](#series-40)。 |
| <a id="snes-025"></a>SNES-025 | Tales of Phantasia | 幻想传说 | 1995 | Namco | 16MB | 角色扮演／动作 RPG | 以线性动作战斗、主题曲和大量语音展示 SFC 后期制作规模，是 Namco 传说系列起点，发行方不是 Square。 [系列专题](#series-41)。 |
| <a id="snes-026"></a>SNES-026 | Uncharted Waters: New Horizons / Daikoukai Jidai II | 大航海时代 II | 1994 | Koei | 8MB | 动作冒险／探索／解谜／文字冒险 | 六名主角可从贸易、探险、私掠等路线成名，港口投资、船队配置与发现物交织。开放目标让它成为航海经营代表。 [系列专题](#series-42)。 |
| <a id="snes-027"></a>SNES-027 | Romance of the Three Kingdoms II | 三国志 II | 1992 | Koei | 4MB | 战略／战棋／大战略与军团 | 以君主、领地、武将忠诚与月度指令推进统一战争，战场采用简化军团操作。MD／SFC 移植保留早期光荣宏观战略，和 Namco 霸王的大陆不同。 [系列专题](#series-05)。 |
| <a id="snes-028"></a>SNES-028 | Romance of the Three Kingdoms III: Dragon of Destiny | 三国志 III | 1992 | Koei | 4MB | 战略／战棋／大战略与军团 | 强化武将身份、外交与城市经营，战场加入更丰富地形与部队行动。MD／SFC 的界面略有差别，仍属光荣第三部本传。 [系列专题](#series-05)。 |
| <a id="snes-029"></a>SNES-029 | Romance of the Three Kingdoms IV: Wall of Fire | 三国志 IV | 1995 | Koei | 8MB | 战略／战棋／大战略与军团 | 以六边形战场、武将技能与情报网扩大战争决策，城市建设和人事同样重要。SFC 版是 16 位家用移植，不套用 PS1 后代系统。 [系列专题](#series-05)。 |
| <a id="snes-030"></a>SNES-030 | Nobunaga’s Ambition: Zenkokuban | 信长之野望：全国版 | 1986 | Koei | 4MB | 战略／战棋／大战略与军团 | 早期全国版以大名、城池、军粮与季节指令推进日本统一。系统朴素但已建立光荣历史模拟循环，MD／SFC 为不同移植。 [系列专题](#series-28)。 |
| <a id="snes-031"></a>SNES-031 | Nobunaga’s Ambition: Bushou Fuuunroku | 信长之野望：武将风云录 | 1990 | Koei | 4MB | 战略／战棋／大战略与军团 | 强化武将个体、家宝与人才网络，政治和战役比全国版更具角色感。SFC 版是武将风云录的家用版本。 [系列专题](#series-28)。 |
| <a id="snes-032"></a>SNES-032 | Nobunaga’s Ambition: Haouden | 信长之野望：霸王传 | 1992 | Koei | 4MB | 战略／战棋／大战略与军团 | 采用军团与更鲜明战略地图组织争霸，部队调度和势力决策比个人养成更突出。它与前后各代的系统重心不同。 [系列专题](#series-28)。 |
| <a id="snes-033"></a>SNES-033 | Nobunaga’s Ambition: Tenshouki | 信长之野望：天翔记 | 1993 | Koei | 8MB | 战略／战棋／大战略与军团 | 以城池、军团、官职与多剧本深化全国战略，战斗和人事系统并行。SFC 版属于 16 位原作，不套用 PS 重制信息。 [系列专题](#series-28)。 |
| <a id="snes-034"></a>SNES-034 | Castlevania: Dracula X | 恶魔城 XX | 1995 | Konami | 8MB | 平台动作／横版／单屏／3D 平台 | SFC 的《恶魔城 XX》借用《血之轮回》人物与部分美术，但关卡和系统经过重排，并非 PCE 原版移植。把它单独看待，才能避免与真正的《血之轮回》混淆。 [系列专题](#series-11)。 |
| <a id="snes-035"></a>SNES-035 | Mega Man X | 洛克人 X | 1994 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 冲刺、蹬墙与装甲部件让动作比元祖更流动，击败 Boss 还会影响其他关卡。它开启 X 系列的高速探索路线。 [系列专题](#series-03)。 |
| <a id="snes-036"></a>SNES-036 | Mega Man X2 | 洛克人 X2 | 1995 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 加入反猎人组织与 Zero 部件分支，选择会影响后续剧情；C4 芯片提供线框 3D 效果。冲刺与骑士机车关卡进一步加快速度。 [系列专题](#series-03)。 |
| <a id="snes-037"></a>SNES-037 | Mega Man X3 | 洛克人 X3 | 1996 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 可有限操作 Zero，并加入多套装甲与更复杂关卡事件。容量和敌群负担较高，SFC 版本与光盘移植的音乐、演出不同。 [系列专题](#series-03)。 |
| <a id="snes-038"></a>SNES-038 | Street Fighter II Turbo: Hyper Fighting | 街头霸王 II Turbo | 1993 | Capcom | 2MB | 格斗／清版动作／一对一与场地格斗 | 加速对战并开放四天王，SFC 版在家用机上保留高速规则。角色只有少量调整，重点是节奏而非新增大型系统。 [系列专题](#series-31)。 |
| <a id="snes-039"></a>SNES-039 | Super Street Fighter II: The New Challengers | 超级街头霸王 II | 1994 | Capcom | 2MB | 格斗／清版动作／一对一与场地格斗 | 加入嘉米、飞龙、迪杰与 T. Hawk，并更新场景、音乐和受击演出。它没有 Turbo 的超级必杀与豪鬼，SFC 版与街机速度也有差别。 [系列专题](#series-31)。 |
| <a id="snes-040"></a>SNES-040 | Final Fight | 快打旋风 | 1990 | Capcom | 2MB | 格斗／清版动作／清版动作与合作 | 科迪、哈格与盖以拳脚、投技和武器对抗疯狂齿轮，敌群管理比单人连招更重要。SFC 初版缺双人且阵容不完整，街机版才是合作基准。 [系列专题](#series-43)。 |
| <a id="snes-041"></a>SNES-041 | Donkey Kong Country | 咚奇刚国度 | 1994 | Nintendo | 8MB | 平台动作／横版／单屏／3D 平台 | 咚奇刚与迪迪可随时切换，动物伙伴和桶炮改变关卡路线。预渲染角色与节奏化动作让它成为 SFC 的标志性技术展示。 [系列专题](#series-01)。 |
| <a id="snes-042"></a>SNES-042 | Donkey Kong Country 2: Diddy’s Kong Quest | 咚奇刚国度 2：迪迪刚大冒险 | 1995 | Nintendo | 8MB | 平台动作／横版／单屏／3D 平台 | 迪迪与黛西搭档，头发滑翔扩展空中路线；奖金币与隐藏房鼓励彻底探索。关卡、音乐和难度曲线通常被视为三部曲高峰。 [系列专题](#series-01)。 |
| <a id="snes-043"></a>SNES-043 | Donkey Kong Country 3: Dixie Kong’s Double Trouble! | 咚奇刚国度 3：迪克西刚的双重麻烦 | 1996 | Nintendo | 8MB | 平台动作／横版／单屏／3D 平台 | 黛西与凯迪一轻一重，可互相投掷到达特殊位置。大地图载具、秘密洞穴与熊兄弟任务增强世界探索。 [系列专题](#series-01)。 |
| <a id="snes-044"></a>SNES-044 | Star Fox | 星际火狐 | 1993 | Nintendo | 4MB | 射击／卷轴与弹幕射击 | 利用 Super FX 芯片呈现 3D 多边形空战，路线选择与队员状态影响流程。它在 SFC 上把家用 3D 射击推进一步。 |
| <a id="snes-045"></a>SNES-045 | Star Fox 2 | 星际火狐 2 | 2017 | Nintendo | 8MB | 射击／卷轴与弹幕射击 | 采用更自由的地图、即时战略拦截与双角色切换，完成于 1990 年代但直到 2017 年才随 SNES Classic 正式发行。 |
| <a id="snes-046"></a>SNES-046 | F-ZERO | F-ZERO | 1990 | Nintendo | 2MB | 竞速／体育／竞速与驾驶 | Mode 7 制造高速平面赛道，能量与车体耐久限制激进驾驶。SFC 首作奠定未来竞速与高难度计时传统。 |
| <a id="snes-047"></a>SNES-047 | Super Mario Kart | 超级马力欧卡丁车 | 1992 | Nintendo | 4MB | 竞速／体育／竞速与驾驶 | Mode 7 赛道、金币加速和道具对抗建立卡丁车规则，战斗模式强调本地双人。赛道短而重复游玩价值高，是系列所有后续作品的起点。 [系列专题](#series-01)。 |
| <a id="snes-048"></a>SNES-048 | Live A Live | 时空勇士 | 1994 | Square | 16MB | 动作冒险／探索／解谜／文字冒险 | 多个时代与主角的短篇各自采用不同机制，最终在主线汇合。章节式结构和“同时代多视角”后来在 HD-2D 重制中再次受到关注。 |
| <a id="snes-049"></a>SNES-049 | EarthBound / Mother 2 | 地球冒险 2／MOTHER 2 | 1995 | Nintendo | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 把现代小镇、流行文化与奇异敌人放进回合制 RPG，滚动血条给抢救治疗留下窗口。其幽默与温情使 MOTHER 系列形成独特地位。 [系列专题](#series-44)。 |
| <a id="snes-050"></a>SNES-050 | Mega Man 7 | 洛克人 7 | 1995 | Capcom | 8MB | 平台动作／横版／单屏／3D 平台 | 元祖第 7 作延续 Boss 武器克制与选关，关卡机关、蓄力和辅助能力随代际逐步调整；可与同平台其他编号作比较关卡节奏。 [系列专题](#series-03)。 |
| <a id="snes-051"></a>SNES-051 | Contra III: The Alien Wars | 魂斗罗精神：异形战争 | 1992 | Konami | 8MB | 射击／跑射与动作射击 | 双武器随时切换、炸弹与攀爬动作强化跑射，俯视关卡采用 Mode 7。SFC 原创第三作与街机 Super Contra 不是同一游戏。 [系列专题](#series-04)。 |
| <a id="snes-052"></a>SNES-052 | Romancing SaGa | 浪漫沙加 | 1992 | Square | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 八名主角、自由剧本与事件开放顺序构成非线性冒险，武器耐久、LP 和闪悟让战斗代价鲜明。没有统一等级曲线引导玩家。 [系列专题](#series-22)。 |
| <a id="snes-053"></a>SNES-053 | Romancing SaGa 2 | 浪漫沙加 2 | 1993 | Square | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 皇帝世代继承跨越数百年，技能闪悟、阵型与帝国发展互相影响，敌人强度随进程变化。多代选择会改变可用角色和结局。 [系列专题](#series-22)。 |
| <a id="snes-054"></a>SNES-054 | Romancing SaGa 3 | 浪漫沙加 3 | 1995 | Square | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 八名主角围绕死食与命运之子展开，自由事件、阵型、闪悟和 mass combat 并存。开放结构鼓励多周目而非固定顺序。 [系列专题](#series-22)。 |
| <a id="snes-055"></a>SNES-055 | Star Ocean | 星之海洋 | 1996 | Enix | 16MB | 角色扮演／动作 RPG | SFC 末期以即时战斗、技能、道具创作和星际文明冲突展开，使用特殊芯片与大容量音画。由 tri-Ace 开发、Enix 发行。 [系列专题](#series-24)。 |
| <a id="snes-056"></a>SNES-056 | Bahamut Lagoon | Bahamut Lagoon | 1996 | Square | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 龙与队伍在网格地图上行动，地形和龙的能力影响战斗，剧情以群像与浮空大陆展开。Square 的 SFC 后期作品未在海外正式发行。 [系列专题](#series-45)。 |
| <a id="snes-057"></a>SNES-057 | Terranigma | 天地创造 | 1996 | Enix | 8MB | 角色扮演／动作 RPG | 以动作战斗与复兴世界为主题，从大陆、生命到文明逐步恢复地球。Quintet 的作品与《Soul Blazer》《Illusion of Gaia》常被并置讨论。 |
| <a id="snes-058"></a>SNES-058 | Lufia & the Fortress of Doom | 四狂神战记 | 1993 | Taito | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 传统回合制围绕四狂神与主角一行展开，迷宫包含动作机关。它为续作的系统与人物关系铺路。 |
| <a id="snes-059"></a>SNES-059 | Lufia II: Rise of the Sinistrals | 四狂神战记 II | 1996 | Natsume | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 以古代洞穴的随机遇敌可见化、谜题和 IP 技能强化迷宫，剧情是前作前传。它通常被视为系列完成度最高的一作。 |
| <a id="snes-060"></a>SNES-060 | Breath of Fire | 龙战士 | 1994 | Capcom | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 龙族少年 Ryu 的变身、队伍特殊能力和传统世界探索构成 Capcom JRPG 起点。地图能力与角色切换用于解谜。 [系列专题](#series-46)。 |
| <a id="snes-061"></a>SNES-061 | Breath of Fire II | 龙战士 II | 1995 | Capcom | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 扩大队伍、城镇建设与合体系统，围绕宗教和失忆展开更沉重故事。高随机遇敌率较古老，中文翻译需统一人名。 [系列专题](#series-46)。 |
| <a id="snes-062"></a>SNES-062 | ActRaiser | ActRaiser | 1990 | Enix | 4MB | 平台动作／横版／单屏／3D 平台 | 横版动作关卡与神殿经营模拟交替，通过居民发展重建文明。Quintet 把两种节奏结合成 SFC 早期独特作品。 |
| <a id="snes-063"></a>SNES-063 | Soul Blazer | Soul Blazer | 1992 | Enix | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 主角释放被封印的生命并让村庄逐步恢复，俯视动作与地图变化相连。它是 Quintet 灵魂主题作品的重要起点。 |
| <a id="snes-064"></a>SNES-064 | Illusion of Gaia | Illusion of Gaia | 1994 | Enix | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 以威尔和伙伴的古代遗迹冒险串联现实历史意象，动作简洁但场景叙事突出。它与 Soul Blazer、天地创造常被并置讨论。 [系列专题](#series-47)。 |
| <a id="snes-065"></a>SNES-065 | Kirby Super Star | 星之卡比：超级豪华版 | 1996 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 以多个规则不同的短篇组成合集，含赛跑、银河探索、竞技场与双人助手系统。它不是单一大地图，而是卡比玩法博物馆。 [系列专题](#series-20)。 |
| <a id="snes-066"></a>SNES-066 | Kirby’s Dream Land 3 | 星之卡比 3 | 1997 | Nintendo | 4MB | 平台动作／横版／单屏／3D 平台 | 动物伙伴与复制能力再次组合，隐藏爱心之星需要理解各关特殊条件。粉彩画面与后期 SA-1 表现突出。 [系列专题](#series-20)。 |
| <a id="snes-067"></a>SNES-067 | Panel de Pon | 花仙子方块 | 1995 | Intelligent Systems | 4MB | 益智／休闲／落块与消除 | 左右交换相邻方块，横竖三消会抬升棋盘，主动连锁和同时消除可攻击对手。它是 Puzzle League 的 SFC 原点。 |
| <a id="snes-068"></a>SNES-068 | SimCity | 模拟城市 | 1991 | Maxis | 4MB | 模拟／音乐／派对／经营与生活模拟 | 规划住宅、商业、工业与交通，在预算和居民需求间维持城市增长。SFC 版由 Nintendo 参与调整并加入博士等主机化引导。 |
| <a id="snes-069"></a>SNES-069 | Harvest Moon | 牧场物语 | 1997 | Natsume | 4MB | 模拟／音乐／派对／经营与生活模拟 | 以农场经营、四季作物、牲畜、节庆和村民关系建立长期日常，SFC 首作奠定系列循环。时间分配比单纯追求利润更重要。 [系列专题](#series-23)。 |
| <a id="snes-070"></a>SNES-070 | Street Fighter Alpha 2 | 少年街霸 Alpha 2 | 1996 | Capcom | 4MB | 格斗／清版动作／一对一与场地格斗 | 以 Alpha Counter、Custom Combo 和更鲜明角色阵容发展少年街霸，SFC 移植在画面与载入上做了硬件妥协。 [系列专题](#series-31)。 |
| <a id="snes-071"></a>SNES-071 | Final Fight 2 | 快打旋风 2 | 1993 | Capcom | 2MB | 格斗／清版动作／清版动作与合作 | 卡洛斯、源柳斋与哈格横跨多地营救，SFC 原创续作支持双人。动作较平稳，敌人和角色招式区别于街机初代。 [系列专题](#series-43)。 |
| <a id="snes-072"></a>SNES-072 | Final Fight 3 | 快打旋风 3 | 1995 | Capcom | 2MB | 格斗／清版动作／清版动作与合作 | 加入奔跑、特殊技、武器必杀和分支路线，露西娅与 Dean 等新角色扩大阵容。它是 SFC 后期家用原创第三作。 [系列专题](#series-43)。 |
| <a id="snes-073"></a>SNES-073 | Saturday Night Slam Masters | 摔角霸王 | 1994 | Capcom | 2MB | 格斗／清版动作／一对一与场地格斗 | 把摔角的投技、压制与擂台规则做成街机格斗，支持多人对抗。Capcom 的角色也与 Final Fight 世界有交集。 |
| <a id="snes-074"></a>SNES-074 | U.N. Squadron / Area 88 | 战区 88 | 1991 | Capcom | 2MB | 射击／卷轴与弹幕射击 | 横版射击可在出击前购买机体与武器，飞行员生命和机体选择带来经营感。它改编自漫画战区 88。 |
| <a id="snes-075"></a>SNES-075 | Super Ghouls ’n Ghosts | 超魔界村 | 1991 | Capcom | 4MB | 平台动作／横版／单屏／3D 平台 | 亚瑟以双层跳跃、铠甲与武器挑战高难关卡，二周目才能获得完整结局。SFC 版是系列原创家用篇章。 [系列专题](#series-48)。 |
| <a id="snes-076"></a>SNES-076 | Axelay | 银河风暴 | 1992 | Konami | 2MB | 射击／卷轴与弹幕射击 | 横版与纵版关卡交替，纵版使用独特纵深透视，武器耗尽而非单纯一命清空形成策略。Konami 的 SFC 原创射击美术突出。 |
| <a id="snes-077"></a>SNES-077 | Gradius III | 宇宙巡航机 III | 1990 | Konami | 4MB | 射击／卷轴与弹幕射击 | 武器编辑、多阶段高难度与大型有机／机械关卡强化传统力量槽。SFC 移植有 slowdown，却也有难度与内容调整，非街机逐像素复制。 [系列专题](#series-09)。 |
| <a id="snes-078"></a>SNES-078 | R-Type III: The Third Lightning | 异形战机 III | 1993 | Irem | 4MB | 射击／卷轴与弹幕射击 | 提供三种 Force 与 Hyper 模式，关卡更强调大型机关和高速场景。SFC 原创续作不是 R-Type II 的简单移植。 [系列专题](#series-35)。 |
| <a id="snes-079"></a>SNES-079 | Parodius Da! | 疯狂大射击 | 1992 | Konami | 4MB | 射击／卷轴与弹幕射击 | 把 Gradius 的力量槽和角色换成章鱼、企鹅等荒诞阵容，音乐与场景大量戏仿 Konami。笑料之下仍是完整关卡记忆型射击。 [系列专题](#series-09)。 |
| <a id="snes-080"></a>SNES-080 | Pop’n TwinBee | 出击！兵蜂 | 1993 | Konami | 2MB | 射击／卷轴与弹幕射击 | 保留铃铛强化与双人协力，并加入生命值、近战和更鲜明角色演出。SFC 原创家用作与街机 Detana 不是同一关卡。 [系列专题](#series-09)。 |
| <a id="snes-081"></a>SNES-081 | Darius Twin | 太空战斗机：双子 | 1991 | Taito | 2MB | 射击／卷轴与弹幕射击 | SFC 家用原创以机械海洋生物、区域分支和纵版外星级横向射击为主，支持双人。多屏街机视野不能照搬到单屏版本。 [系列专题](#series-49)。 |
| <a id="snes-082"></a>SNES-082 | Pilotwings | 飞行俱乐部 | 1990 | Nintendo | 2MB | 动作冒险／探索／解谜／文字冒险 | 用轻型飞机、火箭带、跳伞等任务训练飞行技巧，Mode 7 提供立体地形感。它更像飞行挑战合集而非竞速游戏。 |
| <a id="snes-083"></a>SNES-083 | Killer Instinct | 杀手本能 | 1995 | Nintendo | 4MB | 格斗／清版动作／一对一与场地格斗 | 以连段、Combo Breaker 和 Ultra Combo 构成高压攻防，预渲染角色和双人模式是 SFC 家用版本特色。 |
| <a id="snes-084"></a>SNES-084 | Earthworm Jim | 蚯蚓战士 | 1994 | Virgin Interactive | 4MB | 平台动作／横版／单屏／3D 平台 | 蚯蚓战士用头部鞭打、旋转与枪械穿越荒诞关卡，动画风格接近卡通。不同平台版本在音效与关卡上略有差异。 |
| <a id="snes-085"></a>SNES-085 | Disney’s Aladdin | 阿拉丁 | 1993 | Virgin Interactive | 4MB | 平台动作／横版／单屏／3D 平台 | Capcom 的 SFC 版强调跳跃、攀爬与苹果投掷，和 Virgin 的 MD 版由不同团队制作，不是同一游戏简单互移。 |
| <a id="snes-086"></a>SNES-086 | Disney’s The Lion King | 狮子王 | 1994 | Virgin Interactive | 4MB | 平台动作／横版／单屏／3D 平台 | 辛巴从幼年到成年的动作能力随剧情变化，关卡复现电影场景。精准跳跃与鸵鸟、犀牛等段落难度较高。 |
| <a id="snes-087"></a>SNES-087 | The Legend of the Mystical Ninja | 加油五右卫门： Yukihime 救出绘卷 | 1992 | Konami | 4MB | 动作冒险／探索／解谜／文字冒险 | 五右卫门与惠比寿丸在村镇探索和横版关卡间切换，支持双人合作与商店迷你游戏。它是 SFC 五右卫门系列的重要入口。 [系列专题](#series-50)。 |
| <a id="snes-088"></a>SNES-088 | Shin Megami Tensei if... | 真·女神转生 if… | 1994 | Atlus | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 把末世结构缩到被封印的学园，以多名同伴路线、恶魔交涉和阵营分歧展开。校园设定为 Persona 提供先声，但仍属本传。 [系列专题](#series-51)。 |
| <a id="snes-089"></a>SNES-089 | Robotrek | 机器人构筑战记 | 1994 | Enix | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 少年用零件制作和编程机器人，战斗由机器人执行，发明系统替代传统装备购买。Enix 发行、Quintet 参与制作。 |
| <a id="snes-090"></a>SNES-090 | Arcana / Card Master | 卡牌大师 | 1992 | HAL Laboratory | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 以第一人称迷宫探索和卡牌角色战斗构成 JRPG，队伍由人类与精灵卡组成。HAL 的 SFC 早期作品氛围重于复杂系统。 |
| <a id="snes-091"></a>SNES-091 | E.V.O.: Search for Eden | 46 亿年物语 | 1993 | Enix | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 通过进化点改变身体部位，从鱼类逐步跨越地质时代。进化选择直接影响攻击和生存，题材在 SFC RPG 中很独特。 |
| <a id="snes-092"></a>SNES-092 | Wario’s Woods | 瓦力欧的森林 | 1994 | Nintendo | 2MB | 平台动作／横版／单屏／3D 平台 | 奇诺比奥搬运并排列怪物，用同色炸弹消除整组目标。它结合落块与角色行动，和一般只控制方块的益智游戏不同。 [系列专题](#series-01)。 |
| <a id="snes-093"></a>SNES-093 | Zombies Ate My Neighbors | 僵尸邻居 | 1993 | Konami | 2MB | 动作冒险／探索／解谜／文字冒险 | 两名角色在邻居、购物商场等场景救人，以水滴枪和临时武器对抗 B 级片怪物。双人合作与关卡捷径是重点。 |
| <a id="snes-094"></a>SNES-094 | The Lost Vikings | 失落的维京人 | 1992 | Interplay | 2MB | 动作冒险／探索／解谜／文字冒险 | 三名维京人分别擅长战斗、防御和速度，玩家切换角色组合能力解谜。合作闯关与单人切换都可完成。 |
| <a id="snes-095"></a>SNES-095 | Lemmings | Lemmings | 1991 | Psygnosis | 2MB | 益智／休闲／规则解谜与短局 | 给自动前行的小人分配挖掘、搭桥、阻挡等技能，在时限内达到救援比例。难点是路线与资源规划。 |
| <a id="snes-096"></a>SNES-096 | Another World / Out of This World | 另一个世界 | 1993 | Interplay | 2MB | 平台动作／横版／单屏／3D 平台 | 以电影化无对白演出和精确动作解谜讲述异星逃生，检查点支持反复试验。多边形转描视觉影响深远。 |
| <a id="snes-097"></a>SNES-097 | Prince of Persia | 波斯王子 | 1992 | Brøderbund | 2MB | 平台动作／横版／单屏／3D 平台 | 以精确跳跃、机关计时和冷兵器决斗推进地牢逃生，动画采用转描技术呈现真实动作。不同家用版本的关卡与操作细节有差异。 |
| <a id="snes-098"></a>SNES-098 | Super Castlevania IV | 超级恶魔城 IV | 1991 | Konami | 4MB | 平台动作／横版／单屏／3D 平台 | 八方向挥鞭、鞭子悬挂与多方向跳跃操作重塑了西蒙的动作，Mode 7 场景和编曲也突出 16 位机特色。结构上更接近初代的重新演绎，而非 FC 第四作。 [系列专题](#series-11)。 |
| <a id="snes-099"></a>SNES-099 | Metal Max 2 | 重装机兵 2 | 1993 | Data East | 8MB | 角色扮演／动作 RPG | 延续战车改装和赏金首体系，扩大世界并强化伙伴与据点内容。SFC 原作由 Data East 发行，后来也有重制版本；不能误列为 PS1 游戏。 [系列专题](#series-14)。 |
| <a id="snes-100"></a>SNES-100 | Shin Megami Tensei I / II | 真·女神转生 I／II | 1992–1994 | Atlus | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 初代以东京毁灭、法律／混沌阵营和恶魔合体建立现代末世 RPG，二代延续秩序重建后的社会冲突。两作故事相连但独立商品。 [系列专题](#series-51)。 |
| <a id="snes-101"></a>SNES-101 | Super Mario All-Stars | 超级马力欧合集 | 1993 | Nintendo | 8MB | 平台动作／横版／单屏／3D 平台 | 以 16 位音画重制四部 FC 马力欧，并加入存档；海外版收录日本高难度二代的 The Lost Levels。它是版本对照合集，不是全新第五作。 [系列专题](#series-01)。 |
| <a id="snes-102"></a>SNES-102 | Super Punch-Out!! | 超级拳无虚发 | 1994 | Nintendo | 4MB | 动作冒险／探索／解谜／文字冒险 | 观察拳手预备动作、闪避并抓反击窗口，更像节奏与记忆谜题。SFC 版角色夸张，和 FC 初代不是简单移植。 |
| <a id="snes-103"></a>SNES-103 | Ogre Battle: The March of the Black Queen | 皇家骑士团：黑色皇后 | 1993 | Quest / Enix | 8MB | 战略／战棋／大战略与军团 | 编成小队并在战略地图实时进军，单位前后排、声望与阵营影响战局和结局。它是军团制，不是 Tactics Ogre 的逐格回合战。 [系列专题](#series-37)。 |
| <a id="snes-104"></a>SNES-104 | Dragon Quest III: The Seeds of Salvation | 勇者斗恶龙 III：传说的开始（SFC 重制版） | 1996 | Enix | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 以 SFC 音画重制 FC 第三作，保留转职、昼夜与广阔世界，并调整界面和平衡。它不是 GBA 游戏，也与 NDS 没有对应原生移植。 [系列专题](#series-07)。 |
| <a id="snes-105"></a>SNES-105 | Treasure of the Rudra | 鲁多拉秘宝 | 1996 | Square | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 以自由组合言灵创造魔法，词根与后缀会改变效果、属性和消耗。Square 的 SFC 后期 RPG 以这套文字系统著称。 |

---

### MD / Genesis

<a id="platform-md"></a>

Mega Drive 与 Genesis 是同一硬件的地区名。保留《Raiden Trad》《R-Type》等正式移植，也突出 Sonic、Treasure 和战棋传统。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="md-001"></a>MD-001 | Sonic the Hedgehog | 刺猬索尼克 | 1991 | Sega | 3MB | 平台动作／横版／单屏／3D 平台 | 以速度、坡道和环状地形建立不同于马力欧的平台动作，金环同时承担分数与保护。它成为世嘉塑造主机品牌形象的关键作品。 [系列专题](#series-25)。 |
| <a id="md-002"></a>MD-002 | Sonic the Hedgehog 2 | 刺猬索尼克 2 | 1992 | Sega | 5MB | 平台动作／横版／单屏／3D 平台 | 新增塔尔斯与旋转冲刺，关卡分支和高速流动更成熟；纳克鲁斯是在三代才首次登场。双人分屏也扩大了当年的家庭游玩价值。 [系列专题](#series-25)。 |
| <a id="md-003"></a>MD-003 | Sonic the Hedgehog 3 & Knuckles | 索尼克 3 与纳克鲁斯 | 1994 | Sega | 8MB | 平台动作／横版／单屏／3D 平台 | 通过锁合技术把《Sonic 3》与《Sonic & Knuckles》连成大篇幅冒险，三角色路线与大型关卡互补。这是 MD 索尼克内容最完整的形态。 [系列专题](#series-25)。 |
| <a id="md-004"></a>MD-004 | Streets of Rage / Bare Knuckle | 怒之铁拳 | 1991 | Sega | 4MB | 格斗／清版动作／清版动作与合作 | 阿克塞尔、布蕾兹与亚当以拳脚、投技和警察支援清版，古代祐三配乐塑造都市节奏。MD 初代是家庭合作标杆。 [系列专题](#series-26)。 |
| <a id="md-005"></a>MD-005 | Streets of Rage 2 / Bare Knuckle II | 怒之铁拳 2 | 1992 | Sega | 4MB | 格斗／清版动作／清版动作与合作 | 四名角色各有速度、力量与投技差异，敌群配置和关卡节奏明显优于初代。古代佑三的电子配乐与手感共同造就清版动作经典。 [系列专题](#series-26)。 |
| <a id="md-006"></a>MD-006 | Streets of Rage 3 / Bare Knuckle III | 怒之铁拳 3 | 1994 | Sega | 4MB | 格斗／清版动作／清版动作与合作 | 加入奔跑、翻滚、武器必杀与更复杂分支，日版和美版在难度、服装及剧情呈现上不同。应固定地区版本收藏。 [系列专题](#series-26)。 |
| <a id="md-007"></a>MD-007 | Yuu Yuu Hakusho: Makyou Toitsusen | 幽游白书：魔强统一战 | 1994 | Treasure / Sega | 4MB | 格斗／清版动作／一对一与场地格斗 | Treasure 为 MD 制作四人同屏格斗，支持双线场地、连段与多角色对战。它在授权改编中以系统自由度著称。 |
| <a id="md-008"></a>MD-008 | Golden Axe | 战斧 | 1989 | Sega | 4MB | 格斗／清版动作／清版动作与合作 | 三名职业角色以魔法瓶、骑乘生物和投技合作闯关，MD 移植另有追加内容。它是系列家用起点。 [系列专题](#series-27)。 |
| <a id="md-009"></a>MD-009 | Golden Axe II | 战斧 II | 1993 | Sega | 4MB | 格斗／清版动作／清版动作与合作 | 沿用三人清版并调整魔法操作、敌群和关卡，新增场景但系统变化克制。适合喜欢初代合作节奏的玩家。 [系列专题](#series-27)。 |
| <a id="md-010"></a>MD-010 | Golden Axe III | 战斧 III | 1993 | Sega | 4MB | 格斗／清版动作／清版动作与合作 | 增加新角色、分支路线与更丰富连段，日版 MD 原创续作。发行范围较小，角色与手感不同于街机 Death Adder 复仇。 [系列专题](#series-27)。 |
| <a id="md-011"></a>MD-011 | Altered Beast | 兽王记 | 1988 | Sega | 8MB | 格斗／清版动作／清版动作与合作 | 兽王记通过收集能量球逐步变身为狼人等形态，横向清版节奏直接。它曾是 MD 早期同捆作品，品牌形象意义高于系统复杂度。 |
| <a id="md-012"></a>MD-012 | Romance of the Three Kingdoms II | 三国志 II | 1992 | Koei | 4MB | 战略／战棋／大战略与军团 | 以君主、领地、武将忠诚与月度指令推进统一战争，战场采用简化军团操作。MD／SFC 移植保留早期光荣宏观战略，和 Namco 霸王的大陆不同。 [系列专题](#series-05)。 |
| <a id="md-013"></a>MD-013 | Romance of the Three Kingdoms III: Dragon of Destiny | 三国志 III | 1993 | Koei | 4MB | 战略／战棋／大战略与军团 | 强化武将身份、外交与城市经营，战场加入更丰富地形与部队行动。MD／SFC 的界面略有差别，仍属光荣第三部本传。 [系列专题](#series-05)。 |
| <a id="md-014"></a>MD-014 | Nobunaga’s Ambition: Zenkokuban | 信长之野望：全国版 | 1986 | Koei | 4MB | 战略／战棋／大战略与军团 | 早期全国版以大名、城池、军粮与季节指令推进日本统一。系统朴素但已建立光荣历史模拟循环，MD／SFC 为不同移植。 [系列专题](#series-28)。 |
| <a id="md-015"></a>MD-015 | Langrisser | 梦幻模拟战 | 1991 | Ascii | 8MB | 战略／战棋／网格战术 | 佣兵指挥官带领兵种单位作战，指挥范围、兵种克制和转职决定战线。MD 初代是 Warsong 的日版原作。 [系列专题](#series-29)。 |
| <a id="md-016"></a>MD-016 | Langrisser II / Der Langrisser | 梦幻模拟战 II | 1994 | Ascii | 16MB | 战略／战棋／网格战术 | 二代扩展艾尔文与光辉后裔的战争，Der 则重排剧情并提供帝国、黑暗等多路线。两者不是完全相同的剧本版本。 [系列专题](#series-29)。 |
| <a id="md-017"></a>MD-017 | Advanced Daisenryaku | 大战略：德意志电击战 | 1991 | Sega | 8MB | 战略／战棋／大战略与军团 | 以德意志战场为题材，在六角格上管理武器单位、燃料弹药、地形与补给。SystemSoft 开发、Sega 发行 MD 版，是高级大战略早期家用代表。 [系列专题](#series-30)。 |
| <a id="md-018"></a>MD-018 | Thunder Force III | Thunder Force III | 1990 | Technosoft | 4MB | 射击／卷轴与弹幕射击 | 在多个星球间选择攻略顺序，五类武器可随时切换并针对 Boss 调整，高速卷轴与大型机械场景是 Technosoft 的标志。 |
| <a id="md-019"></a>MD-019 | Thunder Force IV: Lightening Force | Thunder Force IV | 1992 | Technosoft | 4MB | 射击／卷轴与弹幕射击 | 多方向纵卷轴关卡、五种常用武器与 later 强化形成高自由射击，Technosoft 以视差和高速画面展示 MD 机能。 |
| <a id="md-020"></a>MD-020 | Contra: Hard Corps | 魂斗罗：铁血兵团 | 1994 | Konami | 4MB | 射击／跑射与动作射击 | 四角色、分支路线和多结局扩大重复游玩价值，滑铲与换武器让动作更灵活。日美版在生命机制等方面差异明显。 [系列专题](#series-04)。 |
| <a id="md-021"></a>MD-021 | The Revenge of Shinobi | 超级忍：复仇 | 1989 | Sega | 2MB | 平台动作／横版／单屏／3D 平台 | 乔·武藏以手里剑、近战和忍术闯关，双重跳跃与Boss时机要求精确。MD 早期版本含多处受版权影响的角色形象。 |
| <a id="md-022"></a>MD-022 | 异形战士 Alien Soldier | 异形战士 Alien Soldier | 1995 | Sega | 4MB | 射击／跑射与动作射击 | 以大量连续 Boss、武器能量与冲刺反击构成高强度动作，Treasure 几乎舍去普通关卡来突出对战设计。 |
| <a id="md-023"></a>MD-023 | Prince of Persia | 波斯王子 | 1993 | Brøderbund | 2MB | 平台动作／横版／单屏／3D 平台 | 以精确跳跃、机关计时和冷兵器决斗推进地牢逃生，动画采用转描技术呈现真实动作。不同家用版本的关卡与操作细节有差异。 |
| <a id="md-024"></a>MD-024 | Mega Man: The Wily Wars | Mega Man: The Wily Wars | 1994 | Capcom | 2MB | 平台动作／横版／单屏／3D 平台 | 以 16 位画面重制元祖洛克人 1–3，并追加原创“威利塔”。它是合集重制，不是单纯把 FC ROM 装进 MD。 [系列专题](#series-03)。 |
| <a id="md-025"></a>MD-025 | Street Fighter II': Special Champion Edition | 街头霸王 II：冠军加强版 | 1993 | Capcom | 4MB | 格斗／清版动作／一对一与场地格斗 | MD 六键手柄可完整发挥拳脚配置，含冠军版与 Hyper Fighting 规则。它是 MD 街霸 II 的正式商品，不是独立新序号。 [系列专题](#series-31)。 |
| <a id="md-026"></a>MD-026 | NBA Jam | NBA Jam | 1994 | Midway | 4MB | 竞速／体育／体育与运动 | 以二对二、夸张扣篮和连续命中“着火”强化街机篮球，规则刻意简化。家庭双人和合作比真实赛季更重要。 |
| <a id="md-027"></a>MD-027 | Mortal Kombat | Mortal Kombat | 1993 | Midway | 4MB | 格斗／清版动作／一对一与场地格斗 | 真人数字化角色、重击与终结技形成鲜明风格，血量、上勾拳和隐藏角色塑造街机话题。它不同于街霸的卡通格斗路线。 |
| <a id="md-028"></a>MD-028 | Ecco the Dolphin | Ecco the Dolphin | 1992 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 海豚在海洋中游泳、声呐交流与解谜，氧气管理贯穿探索。生态氛围和较高难度使其区别于普通卡通动作。 |
| <a id="md-029"></a>MD-029 | Rock n' Roll Racing | Rock n' Roll Racing | 1994 | Interplay | 4MB | 竞速／体育／竞速与驾驶 | 等距赛道中同时驾驶、漂移和发射武器，奖金用于升级车辆，金属乐与解说强化风格。Blizzard 早期代表作。 |
| <a id="md-030"></a>MD-030 | ToeJam & Earl | ToeJam & Earl | 1991 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 两名外星人在随机化的地球层级寻找飞船零件，礼物盒、隐藏斜坡和双人分屏形成探索。它不是体育游戏。 |
| <a id="md-031"></a>MD-031 | Shinobi III | Shinobi III | 1993 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 加入奔跑、蹬墙、骑马与水上关卡，手里剑和近战切换流畅。它被视为 MD 超级忍动作系统最成熟的一作。 |
| <a id="md-032"></a>MD-032 | Phantasy Star II | 梦幻之星 II | 1989 | Sega | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 以队伍制科幻 RPG、迷宫和较沉重剧情推进，是 MD 早期大容量代表作；随机遇敌和难度带有明显时代特征。 [系列专题](#series-32)。 |
| <a id="md-033"></a>MD-033 | Phantasy Star IV: The End of the Millennium | 梦幻之星 IV：千年纪的终结 | 1993 | Sega | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 以漫画格演出、组队技与宏命令加快传统回合制节奏，剧情也回收早期系列线索。它常被视为 MD 最具代表性的 JRPG 之一。 [系列专题](#series-32)。 |
| <a id="md-034"></a>MD-034 | Gunstar Heroes | 火枪英雄 | 1993 | Sega | 4MB | 射击／跑射与动作射击 | 四种武器可两两组合，角色又有投摔、滑铲与蹬墙，Treasure 用密集 Boss 和夸张演出建立风格。双人合作是 MD 原作重点。 |
| <a id="md-035"></a>MD-035 | 漫画地带 Comix Zone | 漫画地带 Comix Zone | 1995 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 主角被吸入自己的漫画，战斗发生在分镜格中，可翻页、撕纸并利用场景。形式与机制紧密结合，但难度较高。 |
| <a id="md-036"></a>MD-036 | Beyond Oasis / The Story of Thor | 光之继承者 | 1994 | Sega | 4MB | 角色扮演／动作 RPG | 阿里以短剑即时战斗，并召唤水、火、影、地精灵解开迷宫机关。古代祐三配乐和 MD 原创动作 RPG 身份突出。 |
| <a id="md-037"></a>MD-037 | Earthworm Jim | 蚯蚓战士 | 1994 | Virgin Interactive | 4MB | 平台动作／横版／单屏／3D 平台 | 蚯蚓战士用头部鞭打、旋转与枪械穿越荒诞关卡，动画风格接近卡通。不同平台版本在音效与关卡上略有差异。 |
| <a id="md-038"></a>MD-038 | Earthworm Jim 2 | 蚯蚓战士 2 | 1995 | Virgin Interactive | 4MB | 平台动作／横版／单屏／3D 平台 | 加入蜗牛背包、枪支与更多变形关卡，动作规则频繁切换。幽默和实验性更强，节奏不同于初代。 |
| <a id="md-039"></a>MD-039 | Vectorman 1 | Vectorman 1 | 1995 | Activision | 4MB | 平台动作／横版／单屏／3D 平台 | 由球体构成的机器人以射击和变形探索预渲染风格关卡，Sega 用它展示 MD 后期图形表现。 |
| <a id="md-040"></a>MD-040 | Vectorman 2 | Vectorman 2 | 1996 | Activision | 4MB | 平台动作／横版／单屏／3D 平台 | 延续射击与变形并加入更多虫形敌人和临时载具，关卡更偏连续动作。它是 MD 后期正式续作。 |
| <a id="md-041"></a>MD-041 | Ristar | Ristar | 1995 | Sega | 2MB | 平台动作／横版／单屏／3D 平台 | 靠伸缩双臂抓握、攀爬与撞击移动，关卡围绕弹性动作设计。它是 Sonic Team 在 MD 后期塑造的另一套平台角色方案。 |
| <a id="md-042"></a>MD-042 | Fatal Fury 2 | 饿狼传说 2 | 1993 | SNK | 4MB | 格斗／清版动作／一对一与场地格斗 | 双线场地、安迪、东丈与不知火舞等阵容奠定饿狼特色，威力技和线移动形成立体立回。MD 移植与 Neo Geo 原版在画面、速度上不同。 [系列专题](#series-33)。 |
| <a id="md-043"></a>MD-043 | Samurai Shodown | 侍魂 | 1994 | SNK | 4MB | 格斗／清版动作／一对一与场地格斗 | 系列首作以刀剑重击、武器脱手和道具投掷区别于拳脚格斗，节奏更强调读招。 [系列专题](#series-34)。 |
| <a id="md-044"></a>MD-044 | Shining Force | 光明力量 | 1992 | Sega | 4MB | 战略／战棋／网格战术 | 探索村镇与网格战役交替，角色升级、转职和永久编队构成冒险。它与 Langrisser 的佣兵军团制不同。 [系列专题](#series-29)。 |
| <a id="md-045"></a>MD-045 | Shining Force II: Ancient Sealing | 光明力量 II：远古封印 | 1993 | Sega | 4MB | 战略／战棋／网格战术 | 自由探索与网格战棋交替，队伍转职、角色收集和大地图冒险更完整。Camelot 的作品不是《光明力量 III》的 DC 版本。 [系列专题](#series-29)。 |
| <a id="md-046"></a>MD-046 | Rocket Knight Adventures | 火箭骑士历险记 | 1993 | Konami | 4MB | 平台动作／横版／单屏／3D 平台 | 负鼠火箭骑士以喷气冲刺改变攻击与移动方向，蓄力时机贯穿关卡。Konami 将角色能力、Boss 与 MD 视差表现结合。 |
| <a id="md-047"></a>MD-047 | Castlevania: Bloodlines | 恶魔城：血族 | 1994 | Konami | 4MB | 平台动作／横版／单屏／3D 平台 | 两位主角分别使用鞭与长枪，关卡横跨欧洲并加入分岔。它与 FC／SFC 作品并列，是 MD 独立原创恶魔城。 [系列专题](#series-11)。 |
| <a id="md-048"></a>MD-048 | Strider | 出击飞龙 | 1990 | Capcom / Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 飞龙以高速斩击、攀爬和滑行穿越关卡，MD 版保留街机核心并调整内容。Capcom 开发、Sega 发行家用移植。 |
| <a id="md-049"></a>MD-049 | Dynamite Headdy | 炸弹头 | 1994 | Sega | 4MB | 平台动作／横版／单屏／3D 平台 | 头部分离后可更换不同能力，关卡以木偶剧和 Boss 演出推进。Treasure 把角色机制与舞台美术紧密结合。 |
| <a id="md-050"></a>MD-050 | Raiden Trad | 雷电传统版 | 1991 | Micronet / Sega | 4MB | 射击／卷轴与弹幕射击 | MD 移植街机初代，保留红色散弹／蓝色激光与导弹组合，画面和双人表现受硬件调整。标题 Trad 不等于续作。 [系列专题](#series-35)。 |
| <a id="md-051"></a>MD-051 | R-Type | 异形战机 | 1991 | Irem / Sega | 4MB | 射击／卷轴与弹幕射击 | 蓄力波动炮与 Force 装置同时服务正面攻坚、后方防御和特殊站位，关卡强调记忆。街机原版与 MD／PCE 移植各有画面与内容差异。 [系列专题](#series-35)。 |
| <a id="md-052"></a>MD-052 | Landstalker: The Treasures of King Nole | 秘境魔宝：皇帝的财宝 | 1992 | Sega | 4MB | 角色扮演／动作 RPG | 采用等距视角与精确跳跃，结合装备、迷宫和城镇解谜。空间判断有学习成本，但关卡构造在 MD 动作 RPG 中很有辨识度。 |
| <a id="md-053"></a>MD-053 | Wonder Boy in Monster World | 神奇男孩：怪物世界 | 1991 | Sega | 4MB | 角色扮演／回合／迷宫／叙事 RPG | 以装备、魔法和伙伴辅助探索相互连接的地区，节奏介于动作平台与 RPG 之间。它属于 Westone 的怪物世界支线。 [系列专题](#series-36)。 |
| <a id="md-054"></a>MD-054 | VS Puyo Puyo SUN / Futari de Puyo Puyo SUN | 双人噗哟噗哟 SUN | 2022 | Sega | 4MB | 益智／休闲／落块与消除 | Mega Drive Mini 2 新增的官方双人移植，保留 SUN 规则并加入 Fusion Sun／Fading Sun 变体。它不是 1996 年旧卡带，也不含完整单人剧情模式。 [系列专题](#series-88)。 |

---

### PCE (PC Engine / TurboGrafx-16)

<a id="platform-pce"></a>

HuCard、CD‑ROM²／Super CD 与 Arcade Card 作品并列；光盘容量按预留空间估算，收藏时还需对应系统卡。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="pce-001"></a>PCE-001 | Akumajou Dracula X: Chi no Rondo / Castlevania: Rondo of Blood | 恶魔城 X：血之轮回 | 1993 | Konami | 64MB | 平台动作／横版／单屏／3D 平台 | 里希特以传统鞭子闯关，可救出人质、发现分支并解锁玛莉亚。PCE CD 的音画演出与多路线关卡使其成为旧式恶魔城高峰，也直接衔接《月下夜想曲》的开场。 [系列专题](#series-11)。 |
| <a id="pce-002"></a>PCE-002 | Tengai Makyou: Ziria | 天外魔境：自来也 | 1989 | Hudson Soft | 32MB | 动作冒险／探索／解谜／文字冒险 | 以火之一族、地狱一族和夸张和风幻想展开，CD 配音、动画与回合战斗结合。它是 PCE CD 早期标志性长篇 RPG。 [系列专题](#series-54)。 |
| <a id="pce-003"></a>PCE-003 | Bonk’s Adventure / PC Genjin | PC 原人 | 1990 | Hudson Soft | 16MB | 平台动作／横版／单屏／3D 平台 | PC 原人以头槌、旋转和食肉强化闯关，动作直接、关卡色彩鲜明。Hudson 的角色是 PCE 品牌形象之一。 |
| <a id="pce-004"></a>PCE-004 | Bonk’s Revenge / PC Genjin 2 | PC 原人 2 | 1991 | Hudson Soft | 16MB | 平台动作／横版／单屏／3D 平台 | 改进头槌控制与关卡节奏，加入更复杂机关和 Boss。PCE 卡带与 CD 音轨版本需按镜像区分。 |
| <a id="pce-005"></a>PCE-005 | Bonk 3: Bonk’s Big Adventure / PC Genjin 3 | PC 原人 3 | 1993 | Hudson Soft | 16MB | 平台动作／横版／单屏／3D 平台 | 加入大小变化与糖果机制，双人合作和更大型关卡扩展系列规则。它是 PCE 第三部主线作品。 |
| <a id="pce-006"></a>PCE-006 | Ys Book I & II | 伊苏 I・II | 1989 | Hudson Soft | 32MB | 角色扮演／动作 RPG | 采用冲撞攻击与较简明的成长结构，PCE CD 版加入配音、动画和重编音乐。它常被视为早期 CD-ROM RPG 音画表现的标志。 [系列专题](#series-55)。 |
| <a id="pce-007"></a>PCE-007 | Raiden | Raiden | 1991 | Hudson Soft | 16MB | 射击／卷轴与弹幕射击 | 双色主武器、导弹与双人协作构成直观纵版射击，节奏重火力路线而非复杂得分。Seibu Kaihatsu 是发行主体，不应写成 Irem。 [系列专题](#series-35)。 |
| <a id="pce-008"></a>PCE-008 | R-Type | R-Type | 1989 | Irem | 16MB | 射击／卷轴与弹幕射击 | 蓄力波动炮与 Force 装置同时服务正面攻坚、后方防御和特殊站位，关卡强调记忆。街机原版与 MD／PCE 移植各有画面与内容差异。 [系列专题](#series-35)。 |
| <a id="pce-009"></a>PCE-009 | Darius Plus | Darius Plus | 1990 | NEC Avenue | 16MB | 射击／卷轴与弹幕射击 | PCE 移植保留区域分支和机械鱼 Boss，单屏重排街机 Darius 的关卡与画面。Plus 与 Super Darius、Darius II 是不同版本。 [系列专题](#series-49)。 |
| <a id="pce-010"></a>PCE-010 | Gate of Thunder | Gate of Thunder | 1992 | Hudson Soft | 16MB | 射击／卷轴与弹幕射击 | 以三种可切换武器、高速敌群和摇滚 CD 音轨构成横版射击。它是 Hudson 的 Thunder 系列，不是 Jaleco 作品。 |
| <a id="pce-011"></a>PCE-011 | Lords of Thunder | Lords of Thunder | 1993 | Hudson Soft | 16MB | 射击／卷轴与弹幕射击 | 把射击舞台转为重金属奇幻，四种铠甲对应不同攻击流派，关卡前可调整装备。CD 音轨是体验核心。 |
| <a id="pce-012"></a>PCE-012 | Alien Crush | Alien Crush | 1988 | Naxat Soft | 8MB | 动作冒险／探索／解谜／文字冒险 | 以生物机械异形为弹珠台主题，挡板、奖励区与 Boss 目标结合。Naxat 的 Crush 系列让视频弹珠有了动作叙事感。 |
| <a id="pce-013"></a>PCE-013 | Devil's Crush | Devil's Crush | 1990 | Naxat Soft | 8MB | 动作冒险／探索／解谜／文字冒险 | 转向恶魔与骷髅主题，台面孔洞和奖励目标更丰富。它与 Alien Crush 共享弹珠机制但桌面布局完全不同。 |
| <a id="pce-014"></a>PCE-014 | Bomberman '93 / '94 | 炸弹人 ’93／’94 | 1992 | Hudson Soft | 8MB | 平台动作／横版／单屏／3D 平台 | PCE 两款以清晰迷宫、道具与最多五人 Multitap 对战见长，’94 增加角色和新场地。家庭多人需先核对端口映射。 [系列专题](#series-10)。 |
| <a id="pce-015"></a>PCE-015 | Tengai Makyou II: Manji Maru | 天外魔境 II：卍丸 | 1992 | Hudson Soft | 64MB | 动作冒险／探索／解谜／文字冒险 | 以万字丸和更庞大的世界推进歌舞伎式群像，场景、配音与动画规模大幅提升。它是 PCE CD 代表作，不是《天外魔境 Ziria》的简单复刻。 [系列专题](#series-54)。 |
| <a id="pce-016"></a>PCE-016 | Tengai Makyou: Fuun Kabuki Den | 天外魔境：风云歌舞伎传 | 1993 | Hudson Soft | 32MB | 动作冒险／探索／解谜／文字冒险 | 以歌舞伎十郎为主角转向更戏谑、自由的支线故事，战斗与音画延续 II 的体系。篇幅较集中，建议在本传后体验。 [系列专题](#series-54)。 |
| <a id="pce-017"></a>PCE-017 | Ys III: Wanderers from Ys | 伊苏 III：来自伊苏的冒险者 | 1991 | Nihon Falcom | 32MB | 角色扮演／动作 RPG | 从俯视冲撞改为横版动作，剑击、魔法与戒指装备推动菲尔盖纳相关故事。PCE CD 版突出配音和音乐，Oath in Felghana 是后来的全面重制。 [系列专题](#series-55)。 |
| <a id="pce-018"></a>PCE-018 | Ys IV: The Dawn of Ys | 伊苏 IV：伊苏的黎明 | 1993 | Nihon Falcom | 32MB | 角色扮演／动作 RPG | PCE CD 原创版本以塞尔塞塔、古代村落和大量配音展开，采用俯视动作。它与 SFC 的 Ys IV 是不同厂商制作的平行版本。 [系列专题](#series-55)。 |
| <a id="pce-019"></a>PCE-019 | Neutopia | 新乌托邦 | 1989 | Hudson Soft | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 以火球剑、迷宫和大地图构成 Hudson 的俯视冒险，主角寻找八枚宝珠。它与塞尔达相似但不是官方移植。 |
| <a id="pce-020"></a>PCE-020 | Neutopia II | 新乌托邦 II | 1991 | Hudson Soft | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 主角外出寻找失踪父亲，加入新道具和更复杂迷宫，沿用剑与魔法俯视探索。它是 PCE 第二作。 |
| <a id="pce-021"></a>PCE-021 | Blazing Lazers / Gunhed | Blazing Lazers / Gunhed | 1989 | Hudson Soft | 16MB | 射击／卷轴与弹幕射击 | 四种主武器与多级强化、辅助模块构成火力构筑，死亡会削弱装备。Compile 的密集敌群和流畅卷轴代表 PCE 早期射击实力。 |
| <a id="pce-022"></a>PCE-022 | Military Madness | Military Madness | 1989 | NEC | 16MB | 战略／战棋／大战略与军团 | 在月球六角格上利用包围提升攻防，工厂占领、地形与单位克制决定战线。Nectaris 的规则简洁但局势计算很深。 |
| <a id="pce-023"></a>PCE-023 | Dungeon Explorer | 迷宫探险家 | 1989 | Hudson Soft | 16MB | 格斗／清版动作／清版动作与合作 | 多名职业角色在俯视地牢合作，以攻击、魔法和钥匙推进，支持多人。它更接近 Gauntlet 式动作 RPG。 |
| <a id="pce-024"></a>PCE-024 | Dungeon Explorer II | 迷宫探险家 II | 1993 | Hudson Soft | 16MB | 格斗／清版动作／清版动作与合作 | 扩大职业、剧情和 CD 音画，继续多人迷宫刷怪与装备成长。它不是 HuCard 初代的简单移植。 |
| <a id="pce-025"></a>PCE-025 | Legendary Axe | Legendary Axe | 1989 | Victor | 8MB | 平台动作／横版／单屏／3D 平台 | 主角用斧与强化道具穿越遗迹，攻击节奏与跳跃位置要求严格。PCE 初代是早期动作代表，续作更换系统。 |
| <a id="pce-026"></a>PCE-026 | Vigilante | Vigilante | 1989 | Taito | 8MB | 格斗／清版动作／清版动作与合作 | 以拳脚和有限双节棍横向营救，属于 Irem 功夫清版谱系。PCE 移植保留短关卡与高压敌群。 |
| <a id="pce-027"></a>PCE-027 | Splatterhouse | Splatterhouse | 1990 | Namco | 8MB | 格斗／清版动作／清版动作与合作 | 恐怖电影风格的横版动作，主角戴面具用肢体与武器击打怪物。血腥演出是特色，PCE 版按地区有内容调整。 |
| <a id="pce-028"></a>PCE-028 | Cho Aniki | Cho Aniki | 1992 | Compile | 16MB | 动作冒险／探索／解谜／文字冒险 | 以肌肉男与荒诞角色构成横版射击，特殊助力和蓄力攻击形成系统。它的历史价值更多在独特美术与亚文化影响。 |
| <a id="pce-029"></a>PCE-029 | Cosmic Fantasy 2 | 宇宙幻想 2 | 1991 | Telenet Japan | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 少年冒险者与伙伴展开科幻幻想 JRPG，CD 动画和配音用于角色演出。它是 PCE CD 早期日式 RPG 的代表之一。 |
| <a id="pce-030"></a>PCE-030 | Valis: The Fantasm Soldier / Valis II / III / IV | 梦幻战士 1／2／3／4 | 1986–1993 | Telenet Japan | 32MB | 动作冒险／探索／解谜／文字冒险 | 女高中生优子持剑变身战斗，各作在横版动作、剧情演出和系统上差异明显。PCE CD 版本重视动画与配音。 [系列专题](#series-56)。 |
| <a id="pce-031"></a>PCE-031 | Cotton | Cotton | 1993 | Hudson Soft | 16MB | 射击／卷轴与弹幕射击 | 小魔女 Cotton 骑扫帚使用水晶魔法与精灵助力，明亮童话角色和恶搞剧情形成“可爱射击”。PCE CD 版另有配音与音轨。 |
| <a id="pce-032"></a>PCE-032 | Dead Moon | Dead Moon | 1992 | Natsume | 8MB | 射击／卷轴与弹幕射击 | 以战机穿越异星机械关卡，拾取不同武器并维持火力，Natsume 的横版节奏强调敌群组合与 Boss 弱点。它是 PCE 原创射击。 |
| <a id="pce-033"></a>PCE-033 | Xevious | Xevious | 1990 | Namco | 8MB | 射击／卷轴与弹幕射击 | Solvalou 以前向子弹打空中目标、以炸弹攻击地面设施，空地双层瞄准构成规则。它是 1982 年街机名作的 PCE 移植。 |
| <a id="pce-034"></a>PCE-034 | Tower of Druaga | Tower of Druaga | 1992 | Namco | 8MB | 动作冒险／探索／解谜／文字冒险 | 在六十层迷宫中寻找隐藏道具与钥匙，很多出现条件极隐晦。它代表早期迷宫攻略与玩家共享秘密的时代。 |
| <a id="pce-035"></a>PCE-035 | Image Fight | Image Fight | 1990 | Irem | 8MB | 射击／卷轴与弹幕射击 | 机体可切换多档速度并配置 Pod，前半模拟战斗成绩会影响后续实战。Irem 把训练关卡和真实战场连成独特结构。 |
| <a id="pce-036"></a>PCE-036 | Download / Download 2 | Download 1／2 | 1990 | NEC Avenue | 16MB | 射击／卷轴与弹幕射击 | 两款 PCE 横版射击以赛博朋克剧情、角色插图和不同武装推进，续作扩展 CD 音画演出。它们是独立商品，不是同一镜像的修订号。 |
| <a id="pce-037"></a>PCE-037 | Tokimeki Memorial | ときめきメモリアル | 1994 | Konami | 64MB | 模拟／音乐／派对／生活模拟与派对 | 安排学习、社团和约会并维持属性与角色关系，角色评价会相互影响。它确立了 1990 年代恋爱模拟的一种主流结构。 |
| <a id="pce-038"></a>PCE-038 | Genpei Touma Den | 源平讨魔传 | 1990 | Namco | 16MB | 动作冒险／探索／解谜／文字冒险 | 以源平合战与亡灵复仇为题材，动作关卡穿插不同视角。Namco 的街机原作与 PCE 版本都具有强烈和式怪谈风格。 |
| <a id="pce-039"></a>PCE-039 | Super Momotarou Dentetsu | 超级桃太郎电铁 | 1989 | Hudson Soft | 32MB | 动作冒险／探索／解谜／文字冒险 | 沿日本铁路掷骰移动、购买车站产业并应对贫穷神，目标是长期资产领先。多人轮玩是桃铁系列最重要的乐趣。 |
| <a id="pce-040"></a>PCE-040 | Seirei Senshi Spriggan | 精灵战记 Spriggan | 1991 | Naxat Soft | 64MB | 射击／卷轴与弹幕射击 | 纵版射击以不同颜色精灵组合武器，元素搭配改变火力。Compile 制作、Naxat 发行，PCE CD 音画表现突出。 |
| <a id="pce-041"></a>PCE-041 | Ginga Fukei Densetsu Sapphire | 银河妇警传说 Sapphire | 1995 | Hudson Soft | 128MB | 射击／卷轴与弹幕射击 | 利用 Arcade Card 展现缩放、伪 3D 与大型 Boss，是 PCE 后期技术展示型射击。收藏和模拟时要确认 Arcade CD 系统支持。 |
| <a id="pce-042"></a>PCE-042 | Parasol Stars: The Story of Bubble Bobble III | 阳伞之星：泡泡龙 III | 1991 | Taito | 8MB | 平台动作／横版／单屏／3D 平台 | 用阳伞接敌、接雨滴并释放水浪，单人屏机关和双人协作延续泡泡龙。它没有彩虹岛的彩虹攻击。 [系列专题](#series-57)。 |
| <a id="pce-043"></a>PCE-043 | Magical Chase | 魔法追击 | 1991 | NEC Avenue | 8MB | 射击／卷轴与弹幕射击 | 小魔女与使魔在童话关卡中射击，可用金币在商店购买强化；受击后的魔法封锁改变节奏。PCE 版因发行量少而在收藏史也有名气。 |
| <a id="pce-044"></a>PCE-044 | Bonk’s Revenge CD / PC Genjin 2 | PC 原人 2（CD 音轨版） | 1993 | Hudson Soft | 64MB | 平台动作／横版／单屏／3D 平台 | PC 原人 2 的 CD 版本在动作内容之外利用 CD 音轨增强表现，与 HuCard 版应按文件和系统要求区分。 |

---

### PS1

<a id="platform-ps1"></a>

以原生分辨率运行，兼顾类型史、家庭对战与中文圈经典；多盘游戏需维护 M3U，重型画面增强不纳入默认建议。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="ps1-001"></a>PS1-001 | Resident Evil | 生化危机 | 1996 | Capcom | 600MB | 动作冒险／生存恐怖与潜行 | 洋馆探索把有限弹药、格子背包、门锁谜题和固定镜头结合，制造持续资源压力。1996 年作品确立了“生存恐怖”这一市场标签。 [系列专题](#series-52)。 |
| <a id="ps1-002"></a>PS1-002 | Resident Evil 2 | 生化危机 2 | 1998 | Capcom | 800MB | 动作冒险／生存恐怖与潜行 | 里昂与克莱尔的双路线从警局扩展到地下设施，资源管理与人偶式镜头延续初代。N64 版以高压缩技术容纳双主角内容，是技术移植亮点，不是“灾难版”。 [系列专题](#series-52)。 |
| <a id="ps1-003"></a>PS1-003 | Resident Evil 3: Nemesis | 生化危机 3：复仇女神 | 1999 | Capcom | 600MB | 动作冒险／生存恐怖与潜行 | 吉尔在被摧毁的浣熊市逃亡，追迹者会跨场景施压，紧急回避与弹药合成改变战斗节奏。流程更偏动作与逃生。 [系列专题](#series-52)。 |
| <a id="ps1-004"></a>PS1-004 | Castlevania: Symphony of the Night | 恶魔城 X：月下夜想曲 | 1997 | Konami | 400MB | 平台动作／探索型动作 | 阿鲁卡多在可反复探索的德古拉城中获取能力、装备与使魔，逆城则大幅扩展后半流程。它把《密特罗德》的探索结构与 RPG 成长结合，直接塑造了“银河城”类型。 [系列专题](#series-11)。 |
| <a id="ps1-005"></a>PS1-005 | Final Fantasy VII | 最终幻想 VII | 1997 | Square | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 克劳德与雪崩的反神罗行动逐渐扩展为星球危机，魔晶石组合允许自由构筑。全 3D 场景、预渲染背景与电影化演出帮助 JRPG 在全球主流市场破圈。 [系列专题](#series-06)。 |
| <a id="ps1-006"></a>PS1-006 | Final Fantasy VIII | 最终幻想 VIII | 1999 | Square | 1.2GB | 角色扮演／回合／迷宫／叙事 RPG | SeeD 学园与佣兵战争背景下，斯考尔和莉诺雅的关系是叙事核心。抽取魔法与 Junction 把数值成长绑定到装备魔法，规则独特也需要较多理解成本。 [系列专题](#series-06)。 |
| <a id="ps1-007"></a>PS1-007 | Final Fantasy IX | 最终幻想 IX | 2000 | Square | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 祖达尔与伙伴的旅程主动回归水晶、职业和童话幻想风格，同时讨论人造生命的自我认同。它是对系列早期传统的总结，而不只是“复古版 FF”。 [系列专题](#series-06)。 |
| <a id="ps1-008"></a>PS1-008 | Final Fantasy Tactics | 最终幻想战略版 | 1997 | Square | 600MB | 战略／战棋／网格战术 | 伊瓦利斯战争通过拉姆萨的视角展开，职业、技能、地形高度与行动顺序形成细密战棋。政治叙事与自由养成使其成为战术 RPG 的长期标杆。 [系列专题](#series-06)。 |
| <a id="ps1-009"></a>PS1-009 | Metal Gear Solid | 合金装备 | 1998 | Konami | 600MB | 射击／跑射与动作射击 | 斯内克潜入影子摩西岛，雷达、噪音与敌人视锥构成潜行核心。大量 codec 对话、电影镜头和打破第四墙的 Boss 战使游戏叙事方式极具辨识度。 [系列专题](#series-19)。 |
| <a id="ps1-010"></a>PS1-010 | Parasite Eve | 寄生前夜 | 1998 | Square | 600MB | 角色扮演／回合／迷宫／叙事 RPG | 在圣诞夜的纽约对抗线粒体异变，战斗在可移动遇敌与 ATB 指令间切换，武器改造与克莱斯勒大厦扩展养成。 [系列专题](#series-75)。 |
| <a id="ps1-011"></a>PS1-011 | Parasite Eve II | 寄生前夜 II | 1999 | Square | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 转向更直接的生存恐怖操作，固定场景、弹药与魔法资源管理更接近生化危机。故事延续阿雅，但玩法变化明显。 [系列专题](#series-75)。 |
| <a id="ps1-012"></a>PS1-012 | Vagrant Story | 放浪冒险谭 | 2000 | Square | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 在雷亚蒙德废墟中探索，武器针对敌种族、部位与属性进行细致构筑。战斗、锻造与连环场景演出风格冷峻，学习门槛也明显高于一般动作 RPG。 |
| <a id="ps1-013"></a>PS1-013 | Xenogears | 异度装甲 | 1998 | Square | 1.2GB | 角色扮演／回合／迷宫／叙事 RPG | 以机甲与肉身两套战斗展开科幻群像，后半大量采用叙事段落呈现庞大设定。它是 Square 制作，不应误写为 Enix；理解其历史也需正视后期制作节奏。 |
| <a id="ps1-014"></a>PS1-014 | Romance of the Three Kingdoms V | 三国志 V | 1995 | Koei | 400MB | 战略／战棋／大战略与军团 | 以名声、武将能力与阵型战术见长，君主战略和战场六角格节奏清楚。PS1 版加入 CD 音画表现，是中文圈常见的经典入门代。 [系列专题](#series-05)。 |
| <a id="ps1-015"></a>PS1-015 | Romance of the Three Kingdoms VI | 三国志 VI | 1998 | Koei | 600MB | 战略／战棋／大战略与军团 | 突出武将个性、理想与事件演出，战场转向更强调部队同时行动和战术选择。它与 V 的回合思路不同，历史剧本是主要重玩动力。 [系列专题](#series-05)。 |
| <a id="ps1-016"></a>PS1-016 | Romance of the Three Kingdoms VII | 三国志 VII | 2000 | Koei | 800MB | 战略／战棋／大战略与军团 | 从君主制扩展到可扮演不同身份武将，个人仕官、交友与势力战争并行。PS1 与 PSP 属同一世代内容，便携版界面与读取需分别验证。 [系列专题](#series-05)。 |
| <a id="ps1-017"></a>PS1-017 | Nobunaga’s Ambition: Shouseiroku | 信长之野望：将星录 | 1997 | Koei | 600MB | 战略／战棋／大战略与军团 | 强调武将身份、城市群和战场指挥，历史事件推动战国局势。PS1 的大地图与读盘节奏适合慢玩。 [系列专题](#series-28)。 |
| <a id="ps1-018"></a>PS1-018 | Nobunaga’s Ambition: Reppuuden | 信长之野望：烈风传 | 1998 | Koei | 600MB | 战略／战棋／大战略与军团 | 加入箱庭式领地建设与更鲜明战役演出，玩家在内政发展和军团作战间循环。烈风传不是吉翁的系谱，二者须分开。 [系列专题](#series-28)。 |
| <a id="ps1-019"></a>PS1-019 | Super Robot Taisen Alpha | 超级机器人大战 α | 2000 | Bandai | 800MB | 战略／战棋／网格战术 | 以更大的地图、剧情规模和原创主角群开启 Alpha 篇章，战斗演出与队伍编成较旧作扩展。PS1 读盘与存档应在长战役中验证。 [系列专题](#series-39)。 |
| <a id="ps1-020"></a>PS1-020 | Super Robot Taisen Alpha Gaiden | 超级机器人大战 α 外传 | 2001 | Bandai | 800MB | 战略／战棋／网格战术 | 延续 Alpha 的部分角色并转入未来世界，引入不同剧情分支与机体改造规则。它是独立外传战役，不是 Alpha 简单加盘。 [系列专题](#series-39)。 |
| <a id="ps1-021"></a>PS1-021 | Dai-2-Ji Super Robot Taisen (PlayStation) | 第 2 次超级机器人大战（PS 重制版） | 1999 | Bandai | 600MB | 战略／战棋／网格战术 | PS1 重制 FC 第二次机战，更新画面、语音和界面，保留早期 DC 战争脉络。它与 FC 汉化原版分开保存。 [系列专题](#series-39)。 |
| <a id="ps1-022"></a>PS1-022 | Daisenryaku: Master Combat | 大战略：玩家精神 | 1998 | Sega | 400MB | 战略／战棋／大战略与军团 | 以现代兵器数据库、六角格和回合战役构成大战略，强调单位性能与补给而非角色养成。PS1 版适合慢节奏推演。 [系列专题](#series-30)。 |
| <a id="ps1-023"></a>PS1-023 | Front Mission 3 | 前线任务 3 | 1999 | Square | 800MB | 战略／战棋／网格战术 | 以 Wanzer 部件、技能、射程和基地网络推进双路线剧情，东南亚战争围绕 MIDAS 展开。双路线让早期选择显著改变战役。 [系列专题](#series-38)。 |
| <a id="ps1-024"></a>PS1-024 | Tactics Ogre: Let Us Cling Together (PlayStation) | 皇家骑士团：命运之轮（PS 移植版） | 1997 | Square | 800MB | 战略／战棋／网格战术 | PS1 移植 SFC 网格战棋，保留法律／混沌／中立的路线与多结局、WT 行动顺序和永久伤亡。读盘、存档与画面表现和 SFC 原版不同。 [系列专题](#series-37)。 |
| <a id="ps1-025"></a>PS1-025 | Medal of Honor | Medal of Honor | 1999 | Electronic Arts | 400MB | 射击／跑射与动作射击 | 以二战秘密任务为舞台，强调目标完成、敌军阵地与有限资源。它是 PS1 早期具有电影化野心的第一人称射击。 |
| <a id="ps1-026"></a>PS1-026 | Medal of Honor: Underground | Medal of Honor: Underground | 2000 | Electronic Arts | 400MB | 射击／跑射与动作射击 | 主角转为抵抗组织成员，任务横跨被占领地区并加入伪装等设计。它延续初代 PS1 二战潜入射击。 |
| <a id="ps1-027"></a>PS1-027 | Panzer General | Panzer General | 1996 | MicroProse | 400MB | 战略／战棋／大战略与军团 | 以二战战役、六角格和部队经验构成核心，战果会影响后续单位与战役路线。它是 SSI／MicroProse 的家用移植，不存在对应街机原版。 [系列专题](#series-30)。 |
| <a id="ps1-028"></a>PS1-028 | Allied General | Allied General | 1997 | MicroProse | 400MB | 战略／战棋／大战略与军团 | 把 Panzer General 体系转向盟军战役，以部队经验、补给和六边形地图组织反攻。它与德军视角前作共享规则但战役内容独立。 [系列专题](#series-30)。 |
| <a id="ps1-029"></a>PS1-029 | Silent Hill | 寂静岭 | 1999 | Konami | 800MB | 动作冒险／生存恐怖与潜行 | 哈里在雾镇寻找雪柔，表里世界、收音机和有限资源构成心理恐怖。固定视角与压抑氛围区别于生化危机的动作节奏。 [系列专题](#series-79)。 |
| <a id="ps1-030"></a>PS1-030 | Dino Crisis | 恐龙危机 | 1999 | Capcom | 600MB | 动作冒险／生存恐怖与潜行 | 在封闭研究设施中面对高攻击性恐龙，弹药与回复资源有限。Capcom 用实时 3D 场景和恐龙制造不同于丧尸的追逐压力。 |
| <a id="ps1-031"></a>PS1-031 | Dino Crisis 2 | 恐龙危机 2 | 2000 | Capcom | 800MB | 动作冒险／生存恐怖与潜行 | 转向更密集的恐龙战斗与连击积分， Regina 和 Dylan 双路线交替。动作比重明显高于初代的生存恐怖。 |
| <a id="ps1-032"></a>PS1-032 | Valkyrie Profile | 北欧女神 | 1999 | Square | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 按章节寻访战魂并安排英灵升天，迷宫采用横版动作，战斗则通过按键连携组织队伍。北欧神话、倒计时与角色结局构成独特结构。 |
| <a id="ps1-033"></a>PS1-033 | Grandia | 格兰蒂亚 | 1997 | Sony Computer Entertainment | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 以可干预行动顺序的战斗条、魔法与技能熟练度形成养成，贾斯汀的冒险强调远行与发现。Game Arts 的叙事节奏和乐观气质使它区别于沉重向 JRPG。 [系列专题](#series-72)。 |
| <a id="ps1-034"></a>PS1-034 | Suikoden | 幻想水浒传 | 1995 | Konami | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 以 108 星宿招募、据点建设、普通回合战与大规模战争交织，角色死亡和招募条件影响结局。它是幻想水浒传首作。 [系列专题](#series-81)。 |
| <a id="ps1-035"></a>PS1-035 | Suikoden II | 幻想水浒传 II | 1998 | Konami | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 围绕少年兵与旧友在战争中的对立展开，108 星宿同伴、据点建设与三种战斗规模并行。人物群像和政治抉择使它在 PS1 RPG 中长期保有口碑。 [系列专题](#series-81)。 |
| <a id="ps1-036"></a>PS1-036 | Chrono Cross | 时空之轮 | 1999 | Square | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 通过平行世界与元素格系统展开新故事，队伍角色众多，和 Chrono Trigger 有主题及剧情联系但不是直接同队续作。 |
| <a id="ps1-037"></a>PS1-037 | Star Ocean: The Second Story | 星之海洋：第二个故事 | 1998 | Enix | 800MB | 角色扮演／动作 RPG | 双主角视角、私人行动、技能与道具创作构成高自由 JRPG，克洛德与蕾娜视角补足人物事件。PS1 原版与后续重制不同。 [系列专题](#series-24)。 |
| <a id="ps1-038"></a>PS1-038 | The Legend of Dragoon | 龙骑士传说 | 1999 | Sony | 600MB | 角色扮演／回合／迷宫／叙事 RPG | 回合战斗加入连续按键的 Addition 连击与龙骑士变身，Sony 的第一方 JRPG 以长篇预渲染演出见长。 |
| <a id="ps1-039"></a>PS1-039 | Tales of Destiny | 宿命传说 | 1997 | Namco | 800MB | 角色扮演／动作 RPG | 以 Linear Motion Battle System 在横线战场即时攻防，剑士斯坦与有意识的剑缔结旅程。PS1 原版与后来 PS2 重制不是同一版本。 [系列专题](#series-41)。 |
| <a id="ps1-040"></a>PS1-040 | Tales of Eternia | 永恒传说 | 2000 | Namco | 800MB | 角色扮演／动作 RPG | 以两条世界、晶灵术和更自由的 LMBS 连携展开，主角一行往返两个文明。PS1 日版与海外 Destiny II 命名应避免混淆。 [系列专题](#series-41)。 |
| <a id="ps1-041"></a>PS1-041 | Brave Fencer Musashi | 武藏传 | 1998 | Square | 600MB | 动作冒险／探索／解谜／文字冒险 | 动作冒险中可用剑吸收敌人技能，食物、休息与昼夜影响流程。Square 将幽默和动作解谜结合。 |
| <a id="ps1-042"></a>PS1-042 | Lunar: Silver Star Story Complete | 露娜：银河之星 | 1996 | Kadokawa Shoten / Working Designs | 400MB | 角色扮演／回合／迷宫／叙事 RPG | 以阿雷斯追求龙大师梦想展开，重制版用动画、配音与可见敌人重述 CD RPG。PS1 版与 Sega CD 原作的地图和战斗有差异。 [系列专题](#series-82)。 |
| <a id="ps1-043"></a>PS1-043 | Lunar 2: Eternal Blue Complete | 露娜 2：永恒之蓝 | 1998 | Kadokawa Shoten / Working Designs | 600MB | 角色扮演／回合／迷宫／叙事 RPG |  Hiro 与 Lucia 的旅程延续露娜世界，动画配音、角色事件和大地图探索扩充前作体系。PS1 重制不是初代附赠剧情。 [系列专题](#series-82)。 |
| <a id="ps1-044"></a>PS1-044 | Wild Arms | 荒野兵器 | 1996 | Sony Computer Entertainment | 600MB | 角色扮演／回合／迷宫／叙事 RPG | 把西部荒野、枪械与幻想遗迹结合，角色工具用于场景解谜，回合战斗强调队伍能力。它是 PS1 首作。 [系列专题](#series-83)。 |
| <a id="ps1-045"></a>PS1-045 | Wild Arms 2nd Ignition | 荒野兵器 2 | 1999 | Sony Computer Entertainment | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 扩大世界与角色群，改变镜头和战斗呈现，以恐怖组织与英雄使命推进。续作系统独立，不是初代加盘。 [系列专题](#series-83)。 |
| <a id="ps1-046"></a>PS1-046 | Popolocrois Monogatari | 波波罗克罗伊斯物语 | 1996 | Sony | 600MB | 角色扮演／回合／迷宫／叙事 RPG | 以童话王国与皮耶特罗王子的旅程为核心，回合战斗和温和人物互动突出。它改编自漫画，PS1 首作是系列游戏起点。 |
| <a id="ps1-047"></a>PS1-047 | Clock Tower: The First Fear | 钟楼 | 1995 | Hudson Soft | 400MB | 动作冒险／生存恐怖与潜行 | 以点选调查、躲藏和剪刀男追逐制造无力感，主角没有常规战斗手段。PS1 版是 SFC 初代的增强移植。 |
| <a id="ps1-048"></a>PS1-048 | Crash Bandicoot 1 / 2: Cortex Strikes Back / 3: Warped | 古惑狼 1／2／3 | 1996–1998 | Sony | 1.2GB | 平台动作／横版／单屏／3D 平台 | 初代以线性纵深跑跳起步，二代加入更多动作与关卡秘密，三代用时间旅行、载具和能力扩展。三作是独立商品。 [系列专题](#series-84)。 |
| <a id="ps1-049"></a>PS1-049 | Spyro the Dragon 1 / 2: Ripto’s Rage! / 3: Year of the Dragon | 小龙斯派罗 1／2／3 | 1998–2000 | Sony | 800MB | 平台动作／横版／单屏／3D 平台 | 初代以喷火、冲撞和龙族营救起步，二代加入技能学习与支线，三代扩展可操作角色。收集和飞行关贯穿三部曲。 [系列专题](#series-85)。 |
| <a id="ps1-050"></a>PS1-050 | Tekken 3 | 铁拳 3 | 1997 | Namco | 600MB | 格斗／清版动作／一对一与场地格斗 | 以侧移、十连与角色差异推进 3D 格斗，队伍、球类与力量模式增加家用内容。PS1 版是街机移植加原创模式。 [系列专题](#series-80)。 |
| <a id="ps1-051"></a>PS1-051 | R4: Ridge Racer Type 4 | 山脊赛车 Type 4 | 1998 | Namco | 400MB | 竞速／体育／竞速与驾驶 | 以车队与赛季叙事串联赛事，漂移手感、车辆设计和爵士电子配乐高度统一。它是 PS1 时代街机赛车美术设计的代表。 [系列专题](#series-76)。 |
| <a id="ps1-052"></a>PS1-052 | Gran Turismo | GT 赛车 | 1997 | Sony | 600MB | 竞速／体育／体育与运动 | 以真实车款、驾照、赛事和调校构成长期收集，PS1 初代把汽车文化带入家用拟真竞速。画面增强不宜牺牲输入与帧率。 [系列专题](#series-86)。 |
| <a id="ps1-053"></a>PS1-053 | Gran Turismo 2 | GT 赛车 2 | 1999 | Sony | 800MB | 竞速／体育／体育与运动 | 扩大车辆、赛事和改装规模，分为 Arcade 与 Simulation 两张盘；M3U 和记忆卡要匹配。车辆物理和轮胎选择比初代更复杂。 [系列专题](#series-86)。 |
| <a id="ps1-054"></a>PS1-054 | Tomb Raider I / II / III | 古墓丽影 1／2／3 | 1996–1998 | Eidos | 800MB | 动作冒险／探索／解谜／文字冒险 | 初代以遗迹空间、跳跃和双枪探索定型，二代加入载具与更多地区，三代强化非线性关卡和全球旅程。三作分盘保存。 [系列专题](#series-87)。 |
| <a id="ps1-055"></a>PS1-055 | Syphon Filter | 虹吸战士 | 1999 | Sony | 600MB | 射击／跑射与动作射击 | 第三人称潜入射击以任务目标、锁定瞄准和多种装备推进，Gabe Logan 的特工故事形成系列。PS1 版操作有时代特征。 |
| <a id="ps1-056"></a>PS1-056 | Ape Escape | 捉猴啦 | 1999 | Sony | 400MB | 动作冒险／探索／解谜／文字冒险 | 用双摇杆分别移动与操作捕猴网、工具，充分发挥 DualShock 结构。它是早期围绕双模拟摇杆设计的主流 3D 游戏之一。 |
| <a id="ps1-057"></a>PS1-057 | PaRappa the Rapper | PaRappa | 1996 | Sony Computer Entertainment | 200MB | 模拟／音乐／派对／音乐与节奏 | 按节奏依次输入指令并模仿说唱，玩家也可偏离节拍争取更高评价。七日式图形与音乐叙事让它成为 PS1 音游符号。 |
| <a id="ps1-058"></a>PS1-058 | Vib-Ribbon | Vib-Ribbon | 1999 | Sony | 200MB | 模拟／音乐／派对／音乐与节奏 | 把音乐分析成极简线条障碍，兔子随节拍跳跃躲避。可读取音乐 CD 生成关卡的创意使其成为独特技术实验。 |
| <a id="ps1-059"></a>PS1-059 | World Soccer Winning Eleven 2002 | 实况足球：胜利十一人 2002 | 2002 | Konami | 600MB | 竞速／体育／体育与运动 | PS1 后期的胜利十一人作品，以短传、跑位和射门节奏延续系列手感，球队数据与平衡相对成熟。它不是把多个年份混装的合集。 |
| <a id="ps1-060"></a>PS1-060 | Dance Dance Revolution | 劲舞革命 | 1999 | Konami | 400MB | 模拟／音乐／派对／音乐与节奏 | 用四方向脚谱配合节拍，PS1 版可用手柄但完整体验需要跳舞垫。它把街机音游带入家庭，外设条件应在收藏时注明。 |
| <a id="ps1-061"></a>PS1-061 | Castlevania Chronicles | 恶魔城年代记 | 1999 | Konami | 600MB | 平台动作／横版／单屏／3D 平台 | 以重绘音画收录 X68000《恶魔城》的 PS1 版本，并提供原始与改编模式。它不是 FC 初代的普通移植，也不是血之轮回。 [系列专题](#series-11)。 |
| <a id="ps1-062"></a>PS1-062 | Revelations: Persona | Persona 1 | 1996 | Atlus | 600MB | 角色扮演／回合／迷宫／叙事 RPG | 以现代校园、人格面具、恶魔交涉和多路线队伍展开，Sebec 与 Snow Queen 路线结构不同。海外版曾修改人物与内容，PSP 重制又另行调整。 [系列专题](#series-51)。 |
| <a id="ps1-063"></a>PS1-063 | Persona 2: Innocent Sin | Persona 2：Innocent Sin | 1999 | Atlus | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 以传言化为现实的珠闲瑠市为舞台，恶魔交涉、合体与队伍关系推进故事。它构成罪与罚双部曲上半部。 [系列专题](#series-51)。 |
| <a id="ps1-064"></a>PS1-064 | Persona 2: Eternal Punishment | Persona 2：Eternal Punishment | 2000 | Atlus | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 承接罪与罚的平行处境，以成年人团队继续调查，系统延续交涉与召唤。英文版发行情况与 Innocent Sin 不同。 [系列专题](#series-51)。 |
| <a id="ps1-065"></a>PS1-065 | Shin Megami Tensei | 真·女神转生 | 1992 | Atlus | 600MB | 角色扮演／回合／迷宫／叙事 RPG | PS1 版沿用 SFC 原作的东京末世、交涉合体与阵营选择，读盘与音画表现不同。不要把它当成 Persona 初代。 [系列专题](#series-51)。 |
| <a id="ps1-066"></a>PS1-066 | Shin Megami Tensei II | 真·女神转生 II | 1994 | Atlus | 600MB | 角色扮演／回合／迷宫／叙事 RPG | 在东京千年王国中追问秩序与救赎，主角记忆、恶魔阵营与多结局相连。PS1 是移植版，并非重新编号的新作。 [系列专题](#series-51)。 |
| <a id="ps1-067"></a>PS1-067 | Shin Megami Tensei if... | 真·女神转生 if… | 1994 | Atlus | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 把末世结构缩到被封印的学园，以多名同伴路线、恶魔交涉和阵营分歧展开。校园设定为 Persona 提供先声，但仍属本传。 [系列专题](#series-51)。 |
| <a id="ps1-068"></a>PS1-068 | Digimon World | 数码宝贝世界 | 1999 | Bandai | 600MB | 角色扮演／回合／迷宫／叙事 RPG | 从被吸入数码世界开始，通过喂食、训练和作息养育伙伴，并招募数码兽重建 File City。养成条件隐晦，死亡与转生是循环的一部分。 [系列专题](#series-67)。 |
| <a id="ps1-069"></a>PS1-069 | Digimon World 2 | 数码宝贝世界 2 | 2000 | Bandai | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 改为驾驶数码坦克探索随机地牢，捕捉、合体与组织队伍构成主要养成。与初代开放城镇养育不同，更偏迷宫 RPG。 [系列专题](#series-67)。 |
| <a id="ps1-070"></a>PS1-070 | Digimon World 3 / 2003 | 数码宝贝世界 3 | 2002 | Bandai | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 以网游式数码世界为舞台，采用队伍回合战斗、进化和卡片等元素；2003 版追加内容。剧情和系统与 World 1／2 不连续。 [系列专题](#series-67)。 |
| <a id="ps1-071"></a>PS1-071 | Tokimeki Memorial 1 / 2 | 心跳回忆 1／2 | 1994–1999 | Konami | 600MB | 模拟／音乐／派对／生活模拟与派对 | 安排学习、社团和约会并维持属性与角色关系，角色评价会相互影响。它确立了 1990 年代恋爱模拟的一种主流结构。 |
| <a id="ps1-072"></a>PS1-072 | Front Mission Alternative | 前线任务 Alternative | 1997 | Square | 600MB | 战略／战棋／网格战术 | 改为即时制小队指挥和不同视角，以非洲冲突、机体编队与武器选择作战。它不是 Front Mission 3 的前传回合战棋。 [系列专题](#series-38)。 |
| <a id="ps1-073"></a>PS1-073 | Vandal Hearts | Vandal Hearts | 1996 | Konami | 600MB | 战略／战棋／网格战术 | 以网格小队、职业转职和高度地形构成战役，角色永久伤亡会影响阵容。PS1 首作偏重固定地图与剧情推进。 |
| <a id="ps1-074"></a>PS1-074 | Panzer Front | Panzer Front | 1999 | JVC / ASCII | 400MB | 战略／战棋／即时军事模拟 | 直接指挥坦克编组进行即时战斗，地形、射界和装甲部位影响交战。它不是 Panzer General 的回合战棋续作。 |
| <a id="ps1-075"></a>PS1-075 | Sid Meier’s Civilization | 文明 | 1999 | MicroProse | 400MB | 战略／战棋／大战略与军团 | 从部落建立城市，研究科技、经营外交并扩张文明，多胜利路径带来超长回合。PS1 版界面为手柄重排。 |
| <a id="ps1-076"></a>PS1-076 | Tony Hawk’s Pro Skater | 托尼·霍克职业滑板 | 1999 | Activision | 400MB | 动作冒险／探索／解谜／文字冒险 | 在两分钟滑行中完成目标、收集字母并追求连招，关卡隐藏路线鼓励反复练习。它奠定了后续滑板游戏的目标循环。 |
| <a id="ps1-077"></a>PS1-077 | Tony Hawk’s Pro Skater 2 | 托尼·霍克职业滑板 2 | 2000 | Activision | 600MB | 动作冒险／探索／解谜／文字冒险 | 以两分钟内完成目标、寻找隐藏物和维持连招为核心，Manual 让地面动作可串入长连段。其关卡目标与得分循环是极限运动游戏的重要节点。 |
| <a id="ps1-078"></a>PS1-078 | Crash Team Racing | 古惑狼赛车 | 1999 | Sony | 400MB | 竞速／体育／竞速与驾驶 | 在卡丁车竞速外加入可控制的漂移蓄力与连续加速，冒险模式还用奖杯和 Boss 串联赛道。它不是简单复制马力欧赛车的衍生作。 [系列专题](#series-84)。 |
| <a id="ps1-079"></a>PS1-079 | Dragon Quest VII: Fragments of the Forgotten Past | 勇者斗恶龙 VII：伊甸的战士们 | 2000 | Enix | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 通过石板恢复消失大陆，各岛屿故事逐步改变现代世界，后期转职系统庞大。PS1 原版流程很长，与 3DS 重制在画面和节奏上不同。 [系列专题](#series-07)。 |
| <a id="ps1-080"></a>PS1-080 | Klonoa: Door to Phantomile | 风之少年：通往幻界之门 | 1997 | Namco | 500MB | 平台动作／横版／单屏／3D 平台 | 在 2.5D 关卡中以风弹抓敌、投掷和二段跳，背景纵深也参与路径与机关。Namco 的童话演出与隐含悲伤使其独具气质。 [系列专题](#series-64)。 |
| <a id="ps1-081"></a>PS1-081 | Rayman | 雷曼 | 1995 | Ubisoft | 400MB | 平台动作／横版／单屏／3D 平台 | 雷曼逐步获得出拳、抓握与滑翔能力，手绘关卡和隐藏笼子构成挑战。PS1 初代以鲜明美术与较高难度著称。 [系列专题](#series-53)。 |
| <a id="ps1-082"></a>PS1-082 | Street Fighter Alpha 3 | 少年街霸 3 | 1998 | Capcom | 600MB | 格斗／清版动作／一对一与场地格斗 | 以 X／A／V-ISM 区分经典、标准与自定义连段路线，角色阵容与模式大幅扩展。街机版与 PS1 的家用追加内容应按版本比较。 [系列专题](#series-31)。 |
| <a id="ps1-083"></a>PS1-083 | Legend of Mana | 圣剑传说：玛娜传奇 | 1999 | Square | 700MB | 角色扮演／动作 RPG | 以地图放置 Artifact 生成地区，事件、宠物、锻造和家园系统形成非线性冒险。它强调世界构筑与氛围，不是圣剑 3 的直接续作。 [系列专题](#series-40)。 |
| <a id="ps1-084"></a>PS1-084 | SaGa Frontier | 浪漫沙加：开拓者 | 1997 | Square | 700MB | 角色扮演／回合／迷宫／叙事 RPG | 七名主角拥有各自目标和自由剧本，闪悟、种族成长与非线性探索体现沙加式系统实验。完成度带有鲜明取舍。 [系列专题](#series-22)。 |
| <a id="ps1-085"></a>PS1-085 | SaGa Frontier 2 | 浪漫沙加：开拓者 2 | 1999 | Square | 500MB | 角色扮演／回合／迷宫／叙事 RPG | 以世代传承和多段历史事件组织故事，战斗引入连携与角色成长，手绘水彩画面独特。系统与初代自由剧本路线不同。 [系列专题](#series-22)。 |
| <a id="ps1-086"></a>PS1-086 | Theme Hospital | 主题医院 | 1998 | Electronic Arts | 400MB | 模拟／音乐／派对／经营与生活模拟 | 规划诊疗室、培训员工并处理夸张病症，在排队、设备维护、声誉和利润间取舍。Bullfrog 的经营幽默来自扎实系统；PS1 手柄操作不如 PC 鼠标，但慢节奏适合电视游玩。 [系列专题](#series-91)。 |
| <a id="ps1-087"></a>PS1-087 | Mobile Suit Gundam: Gihren’s Greed | 机动战士高达：基连的野望——吉翁独立战争记 | 1998 | Bandai | 700MB | 战略／战棋／大战略与军团 | 围绕一年战争配置将领、预算、生产与机体开发，在战略地图上推进联邦或吉翁战役。动画事件和 IF 路线把高达编年史变成可改写的战争推演，日文信息量较大。 [系列专题](#series-93)。 |
| <a id="ps1-088"></a>PS1-088 | Mobile Suit Gundam: Gihren’s Greed – Blood of Zeon | 机动战士高达：基连的野望——吉翁的系谱 | 2000 | Bandai | 900MB | 战略／战棋／大战略与军团 | 加入停战与条约、机体改造和更多 OVA 角色，并把战线延伸至 Z 高达相关势力。它扩展的不只是剧本，也包括政治与军工系统；PS1 与 DC 版分开识别。 [系列专题](#series-93)。 |
| <a id="ps1-089"></a>PS1-089 | Brigandine: The Legend of Forsena | 幻想大陆战记：弗鲁塞那传说 | 1998 | Hearty Robin / Atlus | 700MB | 战略／战棋／网格战术 | 选择国家经营符文骑士与召唤魔物，在大陆据点争夺和小队六角格战斗间循环。多国视角、职业转职与魔物编成带来重玩价值，北美版由 Atlus 发行。 [系列专题](#series-94)。 |
| <a id="ps1-090"></a>PS1-090 | Brigandine: Grand Edition | 幻想大陆战记：Grand Edition | 2000 | Hearty Robin | 900MB | 战略／战棋／网格战术 | 官方扩展版让艾斯加雷斯帝国正式可玩，新增最多六人轮玩、事件配音、职业和魔物，并调整战斗规则。仅在日本发行；它不是玩家“威力加强版”，也不等于网络联机。 [系列专题](#series-94)。 |

---

### N64

<a id="platform-n64"></a>

保留第一方、Rare、本地多人和类型代表，不承诺高负载游戏在 N4100 上全场景稳定；Expansion Pak 与图形插件需逐作核对。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="n64-001"></a>N64-001 | The Legend of Zelda: Ocarina of Time | 塞尔达传说：时之笛 | 1998 | Nintendo | 32MB | 动作冒险／探索／解谜／文字冒险 | 以 Z 注视锁定、情境按键和立体迷宫建立 3D 动作冒险的通用语言，少年与成年林克的时间差也参与解谜。其历史价值不只在评分，而在大量 3D 游戏沿用了这套交互方式。 [系列专题](#series-02)。 |
| <a id="n64-002"></a>N64-002 | The Legend of Zelda: Majora’s Mask | 塞尔达传说：魔吉拉的面具 | 2000 | Nintendo | 32MB | 动作冒险／探索／解谜／文字冒险 | 三天循环让镇民行程、支线与灾难倒计时彼此咬合，面具则改变能力和人际关系。复用《时之笛》引擎却转向压迫与遗憾，是系列最具实验性的作品之一。 [系列专题](#series-02)。 |
| <a id="n64-003"></a>N64-003 | Super Mario 64 | 超级马力欧 64 | 1996 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 在城堡据点中进入画作世界，以非固定顺序收集星星；长跳、三段跳与帽子能力构成立体动作词汇。它奠定了 3D 平台相机的早期范式。 [系列专题](#series-01)。 |
| <a id="n64-004"></a>N64-004 | Mario Kart 64 | 马力欧卡丁车 64 | 1996 | Nintendo | 16MB | 竞速／体育／竞速与驾驶 | 立体赛道与四人分屏成为核心，三重道具和蓝色刺龟壳强化追赶与对战。彩虹路等赛道仍考验贴边和漂移节奏。 [系列专题](#series-01)。 |
| <a id="n64-005"></a>N64-005 | GoldenEye 007 | 007：黄金眼 | 1997 | Nintendo | 16MB | 射击／跑射与动作射击 | 任务目标随难度增加，潜行与射击并存，四人分屏对战尤其影响家用 FPS。它是 Rare 开发的电影改编成功案例。 |
| <a id="n64-006"></a>N64-006 | Star Fox 64 | 星际火狐 64 | 1997 | Nintendo | 16MB | 射击／卷轴与弹幕射击 | 轨道关卡与全范围模式交替，队员求助、分支路线和奖牌增加重玩价值。Rumble Pak 与配音是 N64 时代标志。 |
| <a id="n64-007"></a>N64-007 | F-ZERO X | F-ZERO X | 1998 | Nintendo | 32MB | 竞速／体育／竞速与驾驶 | 以极高速度、30 台赛车同场和能量取舍构建竞速，随机生成赛道模式也延长寿命。N64 的流畅感比画面细节更重要。 |
| <a id="n64-008"></a>N64-008 | Perfect Dark | 完美黑暗 | 2000 | Nintendo | 32MB | 射击／跑射与动作射击 | 继承黄金眼框架并加入外星阴谋、武器副功能和模拟对手，多人内容更丰富。部分模式依赖 Expansion Pak，N4100 上需降低渲染负担。 |
| <a id="n64-009"></a>N64-009 | Resident Evil 2 | 生化危机 2 | 1999 | Capcom | 32MB | 动作冒险／生存恐怖与潜行 | 里昂与克莱尔的双路线从警局扩展到地下设施，资源管理与人偶式镜头延续初代。N64 版以高压缩技术容纳双主角内容，是技术移植亮点，不是“灾难版”。 [系列专题](#series-52)。 |
| <a id="n64-010"></a>N64-010 | Super Smash Bros. | 任天堂明星大乱斗 | 1999 | Nintendo | 16MB | 格斗／清版动作／一对一与场地格斗 | 以击飞率而非传统血条决定胜负，场地边缘与道具改变对战。N64 首作建立任天堂角色 crossover 派对格斗。 |
| <a id="n64-011"></a>N64-011 | Banjo-Kazooie | 班卓熊大冒险 | 1998 | Nintendo | 16MB | 动作冒险／探索／解谜／文字冒险 | 班卓与卡祖笛通过组合动作收集音符和拼图，世界内部探索与能力学习层层开放。Rare 将幽默、音乐和收集型 3D 平台设计结合。 |
| <a id="n64-012"></a>N64-012 | Banjo-Tooie | 班卓熊大冒险 2 | 2000 | Nintendo | 32MB | 动作冒险／探索／解谜／文字冒险 | 扩大世界之间的连接与谜题，班卓和卡祖笛可分离行动，能力组合更复杂。它是 Rare 收集型 3D 平台的后期大型作品。 |
| <a id="n64-013"></a>N64-013 | Paper Mario | 纸片马力欧 | 2001 | Nintendo | 32MB | 平台动作／横版／单屏／3D 平台 | 把角色与场景做成纸片剧场，回合战斗中通过按键时机增强攻防。伙伴能力与徽章构筑使其区别于传统马力欧 RPG。 [系列专题](#series-01)。 |
| <a id="n64-014"></a>N64-014 | Donkey Kong 64 | 咚奇刚 64 | 1999 | Nintendo | 32MB | 平台动作／横版／单屏／3D 平台 | 五名 Kong 各有武器、乐器和能力，在多座大型岛屿分工收集。内容庞大但换角色与回溯频繁，需要 Expansion Pak，宜以重负载场景验证性能。 [系列专题](#series-01)。 |
| <a id="n64-015"></a>N64-015 | Yoshi’s Story | 耀西的故事 | 1998 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 在绘本式舞台吃指定数量水果过关，甜瓜与笑脸花决定高分路线。主线温和，真正的挑战来自全甜瓜、隐藏心和黑色／白色耀西。 [系列专题](#series-01)。 |
| <a id="n64-016"></a>N64-016 | Kirby 64: The Crystal Shards | 星之卡比 64：水晶碎片 | 2000 | Nintendo | 16MB | 平台动作／横版／单屏／3D 平台 | 可把两种能力组合成新能力，水晶碎片决定完整结局。场景为 3D 呈现但主要沿平面移动，节奏温和。 [系列专题](#series-20)。 |
| <a id="n64-017"></a>N64-017 | Pokémon Stadium | 宝可梦竞技场 | 1998 | Nintendo | 16MB | 角色扮演／回合／迷宫／叙事 RPG | 把第一世代队伍带入 3D 对战，含杯赛、道馆城堡与小游戏；Transfer Pak 可导入掌机队伍。没有该外设时仍可玩租借规则，但不等同完整养成。 [系列专题](#series-21)。 |
| <a id="n64-018"></a>N64-018 | Pokémon Stadium 2 | 宝可梦竞技场 2 | 2000 | Nintendo | 32MB | 角色扮演／回合／迷宫／叙事 RPG | 扩展至第二世代，增加城都宝可梦、学院教学与更多杯赛。Transfer Pak 联动是原作特色，单机租借队伍仍有完整对战。 [系列专题](#series-21)。 |
| <a id="n64-019"></a>N64-019 | Pokémon Snap | 宝可梦随乐拍 | 1999 | Nintendo | 8MB | 角色扮演／回合／迷宫／叙事 RPG | 沿固定轨道拍摄宝可梦的自然行为，用道具诱发动作并按构图与瞬间得分。它把收集欲转化为观察与摄影，而非对战。 [系列专题](#series-21)。 |
| <a id="n64-020"></a>N64-020 | Pokémon Puzzle League | 宝可梦方块联盟 | 2000 | Nintendo | 16MB | 益智／休闲／规则解谜与短局 | 以 Panel de Pon 的横向推块、连锁与对战为底，加入宝可梦角色和属性演出。它是益智衍生，不是正统 RPG。 [系列专题](#series-21)。 |
| <a id="n64-021"></a>N64-021 | Sin and Punishment: Successor of the Earth | 罪与罚：地球的继承人 | 2000 | Nintendo | 32MB | 射击／卷轴与弹幕射击 | 在强制前进关卡中移动、瞄准并近战反击，Treasure 将轨道射击与动作操作结合。N64 日本原版后来经数字发行被更多海外玩家认识。 |
| <a id="n64-022"></a>N64-022 | 1080° Snowboarding | 1080° 滑雪 | 1998 | Nintendo | 16MB | 竞速／体育／体育与运动 | 以压板、抓板、旋转和落地平衡构成技巧竞速，赛道分支与计时、特技赛并行。N64 首发期代表体育作。 |
| <a id="n64-023"></a>N64-023 | Wave Race 64 | Wave Race 64 | 1996 | Nintendo | 8MB | 竞速／体育／竞速与驾驶 | 浮标规则、潮汐和动态水面影响摩托艇路线，加速与转向必须随浪调整。水体物理是 N64 技术展示。 |
| <a id="n64-024"></a>N64-024 | Mario Tennis | 马力欧网球 64 | 2000 | Nintendo | 16MB | 竞速／体育／体育与运动 | Camelot 用旋转球、扣杀和蓄力建立易懂但有深度的网球对战。N64 版还能与 GBC 版联动，是后续家庭体育作品的基础。 [系列专题](#series-01)。 |
| <a id="n64-025"></a>N64-025 | Mario Golf | 马力欧高尔夫 64 | 1999 | Nintendo | 16MB | 竞速／体育／体育与运动 | 风向、落点、旋转与力量条共同决定击球，角色属性和球场障碍改变策略。它比纯派对运动更强调稳定技术与球场管理。 [系列专题](#series-01)。 |
| <a id="n64-026"></a>N64-026 | Bomberman 64 | 炸弹人 64 | 1997 | Hudson Soft | 8MB | 平台动作／横版／单屏／3D 平台 | 把炸弹爆炸、搬运与泵大炸弹用于立体关卡解谜和 Boss 战，单人与四人战斗并存。它不是平面迷宫简单 3D 化。 [系列专题](#series-10)。 |
| <a id="n64-027"></a>N64-027 | Mario Party 1 / 2 / 3 | 马力欧派对 1／2／3 | 1998–2000 | Nintendo | 32MB | 模拟／音乐／派对／生活模拟与派对 | 三作都以棋盘掷骰、金币买星和回合末小游戏构成家庭竞赛；二代加入服装主题与更多道具，三代扩展双人棋盘。初代部分高速摇杆小游戏需注意手柄和游玩方式。 [系列专题](#series-01)。 |
| <a id="n64-028"></a>N64-028 | Conker's Bad Fur Day | Conker's Bad Fur Day | 2001 | Rare | 32MB | 动作冒险／探索／解谜／文字冒险 | 以成人讽刺和电影戏仿包装 3D 平台，章节机制变化频繁。Rare 的 N64 后期技术出色，但内容并不适合儿童家庭同玩。 |
| <a id="n64-029"></a>N64-029 | Turok: Dinosaur Hunter | 恐龙猎人 | 1997 | Acclaim | 32MB | 射击／跑射与动作射击 | 在大型遗迹与丛林中使用夸张武器对抗恐龙，探索钥匙和平台跳跃同样重要。N64 版以远景雾效控制性能。 |
| <a id="n64-030"></a>N64-030 | Turok 2: Seeds of Evil | 恐龙猎人 2：邪恶之种 | 1998 | Acclaim | 32MB | 射击／跑射与动作射击 | 扩大关卡与任务目标，加入更复杂武器和敌人，画面负担也更高。N4100 应以低分辨率和重负载场景实测。 |
| <a id="n64-031"></a>N64-031 | Star Wars: Rogue Squadron | 星球大战：侠盗中队 | 1998 | LucasArts | 32MB | 动作冒险／探索／解谜／文字冒险 | 驾驶 X 翼等战機执行电影宇宙任务， medal 与隐藏机种鼓励提高完成度。Factor 5 的 N64 技术表现突出。 |
| <a id="n64-032"></a>N64-032 | Star Wars: Shadows of the Empire | 星球大战：帝国的阴影 | 1996 | LucasArts | 32MB | 动作冒险／探索／解谜／文字冒险 | 在帝国反击战与绝地归来之间展开，包含雪地战机、射击与飞行多种关卡。它代表早期星战跨媒体叙事。 |
| <a id="n64-033"></a>N64-033 | Killer Instinct Gold | Killer Instinct Gold | 1996 | Rare | 16MB | 格斗／清版动作／一对一与场地格斗 | 把 Killer Instinct 2 的角色与连段带到 N64，调整帧率、场景与家用模式。它不是 SFC 初代的简单移植。 |
| <a id="n64-034"></a>N64-034 | Rayman 2: The Great Escape | 雷曼 2：胜利大逃亡 | 1999 | Ubisoft | 16MB | 平台动作／横版／单屏／3D 平台 | 从线性动作转向更完整的 3D 世界，以滑翔、攀爬和收集 Lums 推进。N64 版与其他平台在关卡与画面上有差异。 [系列专题](#series-53)。 |
| <a id="n64-035"></a>N64-035 | Ogre Battle 64: Person of Lordly Caliber | 皇家骑士团 64：王者之风 | 1999 | Nintendo | 40MB | 战略／战棋／大战略与军团 | 以 3D 地图实时调度军团，小队阵形、地形、补给和道德选择共同决定战役。N64 版扩展军团规模，和 SFC 初代剧情、系统不同。 [系列专题](#series-37)。 |
| <a id="n64-036"></a>N64-036 | Mystical Ninja Starring Goemon | 大盗五右卫门：桃山幕府之舞 | 1997 | Konami | 16MB | 动作冒险／探索／解谜／文字冒险 | 五右卫门一行在立体日本风世界中冒险，城镇、地牢与巨大机器人战斗交替。Konami 将幽默和动作 RPG 结合。 [系列专题](#series-50)。 |
| <a id="n64-037"></a>N64-037 | Mischief Makers | 淘气制造者 | 1997 | Nintendo | 8MB | 动作冒险／探索／解谜／文字冒险 | 机器人 Marina 抓取、投掷并摇晃物件，关卡围绕惯性解谜和 Boss 战。Treasure 的 2D 动作在 N64 上独树一帜。 |

---

### PSP

<a id="platform-psp"></a>

删除对 N4100 负担过高的重型 3D 动作与开放世界，以 2D、静态场景 RPG、战棋和原创休闲为主；仍按实机场景验证。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="psp-001"></a>PSP-001 | Monster Hunter Portable 3rd | 怪物猎人携带版 3rd | 2010 | Capcom | 1.5GB | 角色扮演／动作 RPG | 加入结云村、新怪物与随从猫双编制，武器动作进一步调整。PSP 日版未正式海外本地化，内容差异不宜只用“更多／更少”概括。 [系列专题](#series-73)。 |
| <a id="psp-002"></a>PSP-002 | Monster Hunter Freedom Unite / Monster Hunter Portable 2nd G | 怪物猎人携带版 2nd G | 2008 | Capcom | 1.5GB | 角色扮演／动作 RPG | 以武器动作、怪物生态和素材装备构成长期狩猎循环，G 位任务与随从猫扩展内容。英文版名为 Freedom Unite。 [系列专题](#series-73)。 |
| <a id="psp-003"></a>PSP-003 | The Legend of Heroes: Trails in the Sky FC | 英雄传说：空之轨迹 FC | 2006 | Falcom | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 以艾丝蒂尔和约修亚的准游击士旅程铺开利贝尔危机，城镇 NPC 文本随剧情更新。FC 的结尾直接进入 SC，建议按顺序游玩。 [系列专题](#series-74)。 |
| <a id="psp-004"></a>PSP-004 | The Legend of Heroes: Trails in the Sky SC | 英雄传说：空之轨迹 SC | 2007 | Falcom | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 承接 FC 的分离与结社阴谋，扩大全国旅行与战斗系统。它不是可独立理解的外传，而是利贝尔篇下半部。 [系列专题](#series-74)。 |
| <a id="psp-005"></a>PSP-005 | The Legend of Heroes: Trails in the Sky the 3rd | 英雄传说：空之轨迹 the 3rd | 2008 | Falcom | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 以凯文和星杯骑士为主线，通过门与回忆补完空轨人物，迷宫和战斗比重高于 FC／SC。它适合通完前两作后游玩。 [系列专题](#series-74)。 |
| <a id="psp-006"></a>PSP-006 | The Legend of Heroes: Zero no Kiseki | 英雄传说：零之轨迹 | 2010 | Falcom | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 舞台转至克洛斯贝尔，特务支援课以城市案件切入政治结构，组合战技与 Orbment 延续轨迹构筑。故事衔接碧之轨迹。 [系列专题](#series-74)。 |
| <a id="psp-007"></a>PSP-007 | The Legend of Heroes: Ao no Kiseki | 英雄传说：碧之轨迹 | 2011 | Falcom | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 直接收束零轨的克洛斯贝尔危机，扩大势力冲突和角色结局，Burst 等系统强化团战。应从零轨顺序进入。 [系列专题](#series-74)。 |
| <a id="psp-008"></a>PSP-008 | Nayuta no Kiseki / The Legend of Nayuta: Boundless Trails | 那由多之轨迹 | 2012 | Nihon Falcom | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 改用关卡制动作 RPG，剑技、法术、季节变化与装备收集构成循环。虽名为轨迹，但世界观和玩法都独立。 [系列专题](#series-74)。 |
| <a id="psp-009"></a>PSP-009 | The Legend of Heroes II: Prophecy of the Moonlight Witch / III: White Witch / IV: A Tear of Vermillion / V: Cagesong of the Ocean | 英雄传说：卡卡布三部曲 | 2004–2006 | Falcom | 2GB | 动作冒险／探索／解谜／文字冒险 | 此行是 PSP 时代英雄传说旧作移植收藏组，各作以不同主角与大陆展开传统 RPG；具体战斗与剧情不同，安装应按商品拆分而非当作一部轨迹。 [系列专题](#series-74)。 |
| <a id="psp-010"></a>PSP-010 | Crisis Core: Final Fantasy VII | 核心危机：最终幻想 VII | 2007 | Square Enix | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 以扎克斯视角补完 VII 前史，即时战斗结合 DMW 轮盘、魔晶石合成与支线任务。叙事与正传紧密相关，宜在了解 VII 后游玩。 [系列专题](#series-06)。 |
| <a id="psp-011"></a>PSP-011 | The 3rd Birthday | 寄生前夜：第三次生日 | 2010 | Square Enix | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 以 Aya 相关故事和 Overdive 在士兵间转移意识，第三人称射击、掩体与基因强化构成战斗。它是寄生前夜衍生新篇章。 [系列专题](#series-75)。 |
| <a id="psp-012"></a>PSP-012 | Shin Megami Tensei: Persona 3 Portable | 女神异闻录 3 携带版 | 2010 | Atlus | 800MB | 角色扮演／回合／迷宫／叙事 RPG | 在校园日程、社群与塔尔塔罗斯探索间分配时间，PSP 版允许直接操作队友并新增女主角路线。静态场景降低了 3D 负担。 [系列专题](#series-51)。 |
| <a id="psp-013"></a>PSP-013 | Ridge Racer | 山脊赛车 | 2005 | Namco | 400MB | 竞速／体育／竞速与驾驶 | PSP 首发作汇集多条经典赛道，以漂移充能、氮气和世界观巡回构成街机竞速。原生分辨率下优先稳定操控。 [系列专题](#series-76)。 |
| <a id="psp-014"></a>PSP-014 | Hatsune Miku: Project DIVA 2nd | 初音未来：歌姬计划 2nd | 2010 | Sega | 600MB | 模拟／音乐／派对／音乐与节奏 | 增加新曲、双押与长按等谱面变化，角色和房间内容也更丰富。高难谱面输入延迟比画面增强更值得关注。 |
| <a id="psp-015"></a>PSP-015 | Hatsune Miku: Project DIVA Extend | 初音未来：歌姬计划扩展版 | 2011 | Sega | 600MB | 模拟／音乐／派对／音乐与节奏 | 在 2nd 系统上扩展曲目、模块和演出，是内容追加式独立商品。不要把它误称为 2nd 的存档补丁。 |
| <a id="psp-016"></a>PSP-016 | Super Robot Taisen A Portable | 超级机器人大战 A Portable | 2008 | Banpresto | 800MB | 战略／战棋／网格战术 | 重制 GBA《A》，重做战斗动画、界面与部分系统，并加入携带机便利调整。不要误写成 NDS《A》或全新原创续作。 [系列专题](#series-39)。 |
| <a id="psp-017"></a>PSP-017 | Final Fantasy Tactics: The War of the Lions | 最终幻想战略版：狮子战争 | 2007 | Square Enix | 800MB | 战略／战棋／网格战术 | PSP 版重制 FFT，加入动画过场、新职业与角色，并调整多人内容；政治群像和网格职业战仍是核心，载入与战斗速度需注意。 [系列专题](#series-06)。 |
| <a id="psp-018"></a>PSP-018 | Romance of the Three Kingdoms VII | 三国志 VII | 2000 | Koei | 800MB | 战略／战棋／大战略与军团 | 从君主制扩展到可扮演不同身份武将，个人仕官、交友与势力战争并行。PS1 与 PSP 属同一世代内容，便携版界面与读取需分别验证。 [系列专题](#series-05)。 |
| <a id="psp-019"></a>PSP-019 | Ys I & II Chronicles | 伊苏 I・II 编年史 | 2011 | Falcom | 600MB | 角色扮演／动作 RPG | 重制伊苏双子作，以冲撞战斗、双大陆与达兰之塔串联，提供画面和音乐选项。PSP 版不是菲尔盖纳或七代的小队战斗。 [系列专题](#series-55)。 |
| <a id="psp-020"></a>PSP-020 | Ys: The Oath in Felghana | 伊苏：菲尔盖纳的誓约 | 2010 | Falcom | 800MB | 动作冒险／探索／解谜／文字冒险 | 以《伊苏 III》剧情为基础全面重制，改用跳跃、连击与魔法构成高速动作。它不是简单外传，也不等于 PCE 旧版画面升级。 [系列专题](#series-55)。 |
| <a id="psp-021"></a>PSP-021 | Ys Seven | 伊苏 VII | 2010 | Falcom | 1GB | 角色扮演／动作 RPG | 引入三人小队、切换角色与属性克制，告别传统冲撞系统。它是 PSP 时期系列转向小队动作的重要节点。 [系列专题](#series-55)。 |
| <a id="psp-022"></a>PSP-022 | Valkyria Chronicles II | 战场女武神 2 | 2010 | Sega | 800MB | 战略／战棋／网格战术 | 以加利亚军校为舞台，在回合指令与即时移动射击间切换，车辆、兵种转职与同学任务构成养成。PSP 原创续作。 [系列专题](#series-77)。 |
| <a id="psp-023"></a>PSP-023 | Valkyria Chronicles III | 战场女武神 3 | 2010 | Sega | 1GB | 战略／战棋／网格战术 | 转入无名 penal 部队，以特别行动点数、兵种与角色故事扩展战场规则。仅日本正式发行，剧情与一代同时期但视角不同。 [系列专题](#series-77)。 |
| <a id="psp-024"></a>PSP-024 | Disgaea: Afternoon of Darkness | 魔界战记：黄昏的黑暗 | 2007 | Nippon Ichi | 800MB | 战略／战棋／网格战术 | 魔界战棋以等级上限、道具界和地理效果提供深度养成，PSP 版追加内容。幽默叙事与极端数值成长并存。 |
| <a id="psp-025"></a>PSP-025 | Kingdom Hearts: Birth by Sleep | 王国之心：梦中降生 | 2010 | Square Enix | 1.2GB | 角色扮演／动作 RPG | 泰拉、阿库亚与维恩图斯三条路线互补，指令牌组和射击锁构成战斗成长。剧情是本传前史，不是可忽略的小品。 [系列专题](#series-61)。 |
| <a id="psp-026"></a>PSP-026 | LocoRoco | 乐克乐克 | 2006 | Sony | 400MB | 平台动作／横版／单屏／3D 平台 | 通过倾斜场景与分裂／合体引导乐克乐克滚动，重力与歌声构成轻松解谜。原创 PSP 物理操作是其核心。 |
| <a id="psp-027"></a>PSP-027 | Patapon | 啪嗒砰 | 2008 | Sony | 400MB | 模拟／音乐／派对／音乐与节奏 | 用不同鼓点组合指挥眼球小人行军、攻击与防御，节奏输入同时是策略命令。它由 Sony 日本工作室打造，并非传统战棋。 |
| <a id="psp-028"></a>PSP-028 | Lumines: Puzzle Fusion | 音乐方块 | 2004 | Bandai / Ubisoft | 200MB | 益智／休闲／落块与消除 | 四色方块随音乐时间线扫描消除，皮肤会同步改变节拍、视觉与节奏。水口哲也把音乐游戏反馈融入益智规则，是 PSP 早期最具原创性的作品之一。 [系列专题](#series-78)。 |
| <a id="psp-029"></a>PSP-029 | Everybody’s Golf / Hot Shots Golf | 大众高尔夫 | 2005 | Sony | 400MB | 竞速／体育／体育与运动 | 三键挥杆结合风向、地形、旋转和角色成长，规则易懂但球场管理有深度。PSP 首作适合短局。 |
| <a id="psp-030"></a>PSP-030 | DJMax Portable 1 / 2 / Clazziquai / Black Square | DJMax 携带版系列 | 2006–2008 | Neowiz | 400MB | 模拟／音乐／派对／音乐与节奏 | 四作分别以多轨按键、不同曲包和难度体系见长，Clazziquai 偏易接近，Black Square 偏硬核。应按四款独立商品拆分。 |
| <a id="psp-031"></a>PSP-031 | Taiko no Tatsujin Portable | 太鼓达人携带版 | 2005 | Namco | 400MB | 动作冒险／探索／解谜／文字冒险 | 以红面蓝边和连续音符映射按键，普通手柄即可体验基础谱面。专用鼓控并非本清单的可玩前提。 |
| <a id="psp-032"></a>PSP-032 | Silent Hill: Origins | 寂静岭：起源 | 2007 | Konami | 800MB | 动作冒险／生存恐怖与潜行 | 以查维斯寻找过去为前史，镜面切换、临时武器与便携战斗重释寂静岭。PSP 为原生作品，PS2 后来才有移植。 [系列专题](#series-79)。 |
| <a id="psp-033"></a>PSP-033 | Silent Hill: Shattered Memories | 寂静岭：破碎的记忆 | 2009 | Konami | 800MB | 动作冒险／生存恐怖与潜行 | 以哈利寻找女儿为起点重新诠释初代，心理测试会改变人物与场景呈现，追逐段落取代常规战斗。它不是《起源》的续作。 [系列专题](#series-79)。 |
| <a id="psp-034"></a>PSP-034 | Memories Off / Clannad / Steins;Gate / Higurashi / Fate/Extra | 秋之回忆／CLANNAD／命运石之门／寒蝉／Fate/EXTRA（分卷收藏） | 2008 | 5pb. / CyberFront / Imageepoch / Capcom | 2GB | 模拟／音乐／派对／生活模拟与派对 | 此行汇集五类文字／叙事游戏：秋之回忆与 CLANNAD 偏恋爱，命运石之门与寒蝉偏科幻悬疑，Fate/EXTRA 则是迷宫 RPG。实际应拆成独立商品。 |
| <a id="psp-035"></a>PSP-035 | Dissidia Final Fantasy | 最终幻想：纷争 | 2009 | Square Enix | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 把历代角色放入立体场地，以勇气值与 HP 攻击分离资源，兼具格斗和动作 RPG 养成。 [系列专题](#series-06)。 |
| <a id="psp-036"></a>PSP-036 | Hatsune Miku: Project DIVA | 初音未来：歌姬计划 | 2009 | Sega | 700MB | 模拟／音乐／派对／音乐与节奏 | 按飞入的符号与音乐节拍按键，包含初音等 Vocaloid 曲目和编辑模式。PSP 首作不是家用机 F 系列。 |
| <a id="psp-037"></a>PSP-037 | Grand Theft Auto: Chinatown Wars | 侠盗猎车手：唐人街战争 | 2009 | Rockstar Games | 1GB | 动作冒险／探索／解谜／文字冒险 | 采用俯视角与触屏交互，在自由城完成帮派任务、驾驶和小游戏，毒品交易经济是特色。NDS 与 PSP 版本在画面和操作呈现上不同。 |
| <a id="psp-038"></a>PSP-038 | Tekken: Dark Resurrection | 铁拳：暗黑复苏 | 2006 | Bandai Namco | 1GB | 格斗／清版动作／一对一与场地格斗 | 在 Tekken 5 基础上调整平衡并加入 Lili、Dragunov 等角色，PSP 版含幽灵对战与练习内容。原生设置下验证战斗帧率。 [系列专题](#series-80)。 |
| <a id="psp-039"></a>PSP-039 | Wipeout Pure | 反重力赛车：纯粹 | 2005 | Sony | 400MB | 竞速／体育／竞速与驾驶 | 反重力赛车强调高速贴地、武器与加速区，PSP 首发期画面和电子音乐突出。原生分辨率比增强渲染更适合 N4100。 |
| <a id="psp-040"></a>PSP-040 | Jeanne d’Arc | 圣女贞德 | 2006 | Sony | 700MB | 角色扮演／回合／迷宫／叙事 RPG | 以百年战争与奇幻手镯改编历史，网格战斗加入燃烧格子与联合技能。Level-5 的 PSP 原创战棋体量完整。 |
| <a id="psp-041"></a>PSP-041 | Castlevania: The Dracula X Chronicles | 恶魔城 X 历代记 | 2007 | Konami | 800MB | 平台动作／横版／单屏／3D 平台 | 2.5D 重制《血之轮回》，并可解锁 PCE 原版与《月下夜想曲》。一套光盘包含新旧三种体验，适合核对系列版本关系。 [系列专题](#series-11)。 |
| <a id="psp-042"></a>PSP-042 | Daxter | 达斯特 | 2006 | Sony | 900MB | 平台动作／横版／单屏／3D 平台 | 达斯特独自展开冒险，使用喷雾与武器穿越平台关卡，承接 Jak 系列间隙剧情。它是 PSP 较有代表性的 3D 动作移植原创。 |
| <a id="psp-043"></a>PSP-043 | LittleBigPlanet | 小小大星球 | 2009 | Sony | 1GB | 平台动作／横版／单屏／3D 平台 | 横版创造与平台跳跃结合，机关、物理和自制关卡构成核心。PSP 版独立制作，在线内容之外仍有单人关卡。 |
| <a id="psp-044"></a>PSP-044 | Lumines II | 音乐方块 II | 2006 | Q Entertainment / Buena Vista Games | 300MB | 益智／休闲／落块与消除 | 延续音乐时间线消除，并加入更多皮肤、视频背景和模式。规则与一代一致但内容包装更丰富。 [系列专题](#series-78)。 |
| <a id="psp-045"></a>PSP-045 | Me & My Katamari | 块魂：我与我的块魂 | 2005 | Namco | 2GB | 益智／休闲／规则解谜与短局 | 推动黏球卷起物件并逐步扩大可收集尺度，以动物委托和岛屿界面组织任务。它是系列首款掌机作，十字键与按键模拟双摇杆需要适应；1× 渲染下仍需实测物件密集场景。 [系列专题](#series-90)。 |
| <a id="psp-046"></a>PSP-046 | Mobile Suit Gundam: Gihren’s Greed – Axis no Kyoui V | 机动战士高达：基连的野望——阿克西斯的威胁 V | 2009 | Bandai Namco Games | 2GB | 战略／战棋／大战略与军团 | V 版扩充无印《阿克西斯的威胁》的机体、角色与势力，战役横跨一年战争至后续宇宙世纪冲突。静态事件与回合战略适合低负载设置，但大规模战场和日文菜单仍需实测。 [系列专题](#series-93)。 |

---

### Dreamcast

<a id="platform-dc"></a>

以 Flycast 原生分辨率、较成熟 2D 移植与 DC 特色游戏为主；重型 3D 只保留高代表作，不把“可启动”写成“全程稳定”。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="dc-001"></a>DC-001 | Shenmue | 莎木 | 1999 | Sega | 1.2GB | 动作冒险／探索／解谜／文字冒险 | 横须贺日常以时间表、商店、交谈和 QTE 交织，目标是追查父亲遇害。它对持续世界与细节互动的投入影响深远，但慢节奏也需要耐心。 |
| <a id="dc-002"></a>DC-002 | Shenmue II | 莎木 II | 2001 | Sega | 2GB | 动作冒险／探索／解谜／文字冒险 | 从香港到桂林扩展城市调查、打工与格斗，节奏和场景密度不同于初代。DC 版是高负载 3D 游戏，应低分辨率逐段验证。 |
| <a id="dc-003"></a>DC-003 | Dead or Alive 2 | 死或生 2 | 2000 | Tecmo | 1GB | 格斗／清版动作／一对一与场地格斗 | 以反击 Hold、攻击层级和场地边缘危险构成 3D 格斗。DC 版画面优秀，双人策略不是单纯连招竞赛。 |
| <a id="dc-004"></a>DC-004 | Soulcalibur | 灵魂能力 | 1999 | Namco | 1GB | 格斗／清版动作／一对一与场地格斗 | 武器格斗以八向移动、横纵斩与格挡反击构成，DC 版又加入大量任务模式。其街机移植完成度与画面曾长期作为 DC 技术展示。 |
| <a id="dc-005"></a>DC-005 | Street Fighter III: Double Impact | 街头霸王 III：双重冲击（New Generation＋2nd Impact） | 1999 | Capcom | 800MB | 格斗／清版动作／一对一与场地格斗 | 一张 DC 光盘收录 New Generation 与 2nd Impact，适合比较两次系统扩展。它明确不含 3rd Strike，后者应另存。 [系列专题](#series-31)。 |
| <a id="dc-006"></a>DC-006 | Crazy Taxi | 疯狂出租车 | 2000 | Sega | 600MB | 动作冒险／探索／解谜／文字冒险 | 在限时内接送乘客，以跳跃、漂移和高速穿插提高小费并续时。它将开放街区作为得分场，而非拟真驾驶。 |
| <a id="dc-007"></a>DC-007 | Resident Evil – Code: Veronica | 生化危机：代号维罗妮卡 | 2000 | Capcom | 1GB | 动作冒险／生存恐怖与潜行 | 克莱尔与克里斯在孤岛和南极设施双线行动，资源与关键道具跨角色传递。DC 原版以实时 3D 场景区别于 PS1 前作。 [系列专题](#series-52)。 |
| <a id="dc-008"></a>DC-008 | Ikaruga | 斑鸠 | 2002 | Treasure | 600MB | 射击／卷轴与弹幕射击 | 敌弹与自机分黑白两极，同色可吸收、异色才致命，切换属性同时决定生存与得分。Treasure 把弹幕射击变成高度纯粹的规则解谜。 |
| <a id="dc-009"></a>DC-009 | Jet Set Radio | Jet Set Radio | 2000 | Sega | 600MB | 动作冒险／探索／解谜／文字冒险 | 在东京街头滑行、磨轨并喷涂涂鸦，卡通渲染与混搭音乐塑造强烈都市风格。它既是动作游戏，也是 DC 时代世嘉视觉实验的象征。 |
| <a id="dc-010"></a>DC-010 | Sonic Adventure | 索尼克大冒险 | 1998 | Sega | 1GB | 平台动作／横版／单屏／3D 平台 | 以多名角色、不同关卡规则和城市冒险区组成 3D 索尼克，Chao 养成提供长期支线。镜头和控制有时代痕迹，宜原生分辨率验证。 [系列专题](#series-25)。 |
| <a id="dc-011"></a>DC-011 | Sonic Adventure 2 | 索尼克大冒险 2 | 2001 | Sega | 1.2GB | 平台动作／横版／单屏／3D 平台 | 英雄与黑暗双阵营交错，速度、射击与寻宝三类关卡分明，Chao 与双人模式扩展重玩。DC 原版和后来 Battle 版追加内容不同。 [系列专题](#series-25)。 |
| <a id="dc-012"></a>DC-012 | Power Stone | 能量宝石 | 1999 | Capcom | 800MB | 格斗／清版动作／一对一与场地格斗 | 在立体场地拾取武器、移动机关并收集宝石变身，场地互动和多人混战比传统擂台更自由。DC 首作支持双人。 |
| <a id="dc-013"></a>DC-013 | Power Stone 2 | 能量宝石 2 | 2000 | Capcom | 1GB | 格斗／清版动作／一对一与场地格斗 | 四人在可变化场景中拾取武器、机关与能量宝石，变身混战是核心。相比初代更偏派对乱斗。 |
| <a id="dc-014"></a>DC-014 | Marvel vs. Capcom: Clash of Super Heroes | 漫威对卡普空：超级英雄冲突 | 1999 | Capcom | 800MB | 格斗／清版动作／一对一与场地格斗 | 双人标签与援护角色并存，漫威英雄和 Capcom 角色共享空中连段体系。DC 移植是该作的家用版本。 |
| <a id="dc-015"></a>DC-015 | Marvel vs. Capcom 2: New Age of Heroes | 漫威对卡普空 2：英雄新纪元 | 2000 | Capcom | 1GB | 格斗／清版动作／一对一与场地格斗 | 三人队伍、三种援护类型和大型角色阵容构成高自由组队。DC 版保留街机核心，是本地多人对战代表。 |
| <a id="dc-016"></a>DC-016 | Capcom vs. SNK: Millennium Fight 2000 | 卡普空对 SNK：千年之战 2000 | 2000 | Capcom | 800MB | 格斗／清版动作／一对一与场地格斗 | 以 Ratio 分配队伍强度，并在 Capcom／SNK Groove 间选择系统。DC 是 NAOMI 同源移植，不应再放入 FBNeo 街机目录。 |
| <a id="dc-017"></a>DC-017 | Capcom vs. SNK 2: Mark of the Millennium 2001 | 卡普空对 SNK 2：2001 千年印记 | 2001 | Capcom | 1GB | 格斗／清版动作／一对一与场地格斗 | 六种 Groove、自由 Ratio 与大型角色阵容构成高度自由的组队对战。DC 版沿用 NAOMI 体系，不与 CPS 游戏混放。 |
| <a id="dc-018"></a>DC-018 | Guilty Gear X | 罪恶装备 X | 2000 | Arc System Works | 800MB | 格斗／清版动作／一对一与场地格斗 | 以 Roman Cancel、冲刺与空中连段形成高速 2D 格斗，角色风格鲜明。DC 版是 Arc System Works 系列早期家用代表。 |
| <a id="dc-019"></a>DC-019 | Virtua Fighter 3tb | VR 战士 3 组队战 | 1999 | Sega | 1.2GB | 格斗／清版动作／一对一与场地格斗 | 以真实位移、闪避和多边形场景构成立体格斗，Team Battle 模式连续使用不同角色。DC 版对应 Model 3 时代作品。 |
| <a id="dc-020"></a>DC-020 | Sakura Wars 3: Is Paris Burning? | 樱花大战 3：巴黎在燃烧吗 | 2001 | Sega | 1.2GB | 动作冒险／探索／解谜／文字冒险 | 战场转至巴黎，恋爱冒险、日程选择与战棋交替，ARMS 系统强调行动范围。日文文本量较大。 [系列专题](#series-71)。 |
| <a id="dc-021"></a>DC-021 | Sakura Wars 4: Fall in Love, Maidens | 樱花大战 4：恋爱吧少女 | 2002 | Sega | 1.5GB | 动作冒险／探索／解谜／文字冒险 | 让东京与巴黎角色汇合，以较短篇章收束早期系列。它更适合已接触前作的玩家，不宜作为独立入门。 [系列专题](#series-71)。 |
| <a id="dc-022"></a>DC-022 | Phantasy Star Online | 梦幻之星在线 | 2000 | Sega | 800MB | 动作冒险／探索／解谜／文字冒险 | 以实时动作、职业与掉落装备构建大厅组队 RPG，是家用机网络游戏的重要里程碑。离线可体验部分内容，但原官方服务器早已停止。 [系列专题](#series-32)。 |
| <a id="dc-023"></a>DC-023 | Grandia II | 格兰蒂亚 II | 2000 | Ubisoft | 1GB | 角色扮演／回合／迷宫／叙事 RPG | 以即时与回合结合的行动条、打断和站位展开，Ryudo 与 Millenia 的故事较初代更集中。DC 版保留原平台音画。 [系列专题](#series-72)。 |
| <a id="dc-024"></a>DC-024 | Sega Rally 2 | 世嘉拉力锦标赛 2 | 1999 | Sega | 600MB | 竞速／体育／竞速与驾驶 | 泥地、砂石和柏油改变抓地力，车辆调校与赛道记忆同等重要。DC 版含家用拉力内容，需实测高负载场景。 |
| <a id="dc-025"></a>DC-025 | Daytona USA 2001 | Daytona USA 2001 | 2001 | Sega | 400MB | 竞速／体育／竞速与驾驶 | 整合经典 Daytona 赛道与新增内容，漂移、手动挡和多人竞速延续街机手感。它是 DC 版，不是 Model 2 ROM。 |
| <a id="dc-026"></a>DC-026 | Rez | Rez | 2001 | Sega | 600MB | 射击／卷轴与弹幕射击 | 在轨道中锁定目标并释放射击，音效与电子音乐节拍、画面振动同步。它是水口哲也“联觉”设计理念的代表。 |
| <a id="dc-027"></a>DC-027 | Space Channel 5: Part 2 | 太空频道 5：第二章 | 2002 | Sega | 800MB | 模拟／音乐／派对／音乐与节奏 | 按节奏记忆并复现方向与射击指令，以舞蹈对抗外星人。世嘉把音乐游戏、电视秀和复古未来审美结合。 |
| <a id="dc-028"></a>DC-028 | The Typing of the Dead | 死亡打字员 | 2001 | Sega | 400MB | 动作冒险／探索／解谜／文字冒险 | 把《死亡之屋 2》的扳机替换为键盘输入，以打字速度和准确度击杀僵尸。戏谑外表下确实能训练输入。 |
| <a id="dc-029"></a>DC-029 | Toy Commander | 玩具指挥官 | 1999 | Sega | 600MB | 动作冒险／探索／解谜／文字冒险 | 在家居微缩场景中驾驶玩具车辆完成任务，房间成为立体关卡。DC 原创题材强调探索与多人分屏。 |
| <a id="dc-030"></a>DC-030 | Hydro Thunder | 雷霆快艇 | 1999 | Sega | 600MB | 竞速／体育／竞速与驾驶 | 快艇在积水城市中收集加速、飞跃隐藏捷径，水面跳起和推进资源构成风险路线。DC 移植强调街机短局。 |
| <a id="dc-031"></a>DC-031 | Bangai-O | Bangai-O | 1999 | Treasure / Swing! | 400MB | 射击／卷轴与弹幕射击 | 飞行机器人在弹幕中移动，靠近距离释放大量反弹导弹形成风险回报。Treasure 将解谜路线与爆炸得分结合。 |
| <a id="dc-032"></a>DC-032 | Crazy Taxi 2 | 疯狂出租车 2 | 2001 | Sega | 1GB | 动作冒险／探索／解谜／文字冒险 | 增加跳跃与多名乘客等新要素，城市路线和得分技巧延续初代。短局高分适合反复挑战。 |
| <a id="dc-033"></a>DC-033 | Skies of Arcadia | 永恒的阿卡迪亚 | 2000 | Sega | 1.2GB | 动作冒险／探索／解谜／文字冒险 | 空贼维斯一行驾驶飞空艇探索浮空大陆，陆上回合战与舰船炮击战交替。明快探险精神和世界发现在 DC JRPG 中很有代表性。 |
| <a id="dc-034"></a>DC-034 | Street Fighter III: 3rd Strike | 街头霸王 III：三度冲击 | 2000 | Capcom | 700MB | 格斗／清版动作／一对一与场地格斗 | 加入春丽、真琴等五人，调整判定与音乐美术，Blocking 的时机博弈达到系列高点。街机、DC 与后续移植存在细微差异。 [系列专题](#series-31)。 |
| <a id="dc-035"></a>DC-035 | Virtua Tennis / Virtua Tennis 2 | VR 网球／VR 网球 2 | 2000–2001 | Sega | 1.2GB | 竞速／体育／体育与运动 | 以简洁挥拍、跑位和场地类型建立易上手网球，World Circuit 与多人比赛扩充内容。两作分别收藏。 |
| <a id="dc-036"></a>DC-036 | Metropolis Street Racer | 大都会街头赛车 | 2000 | Sega | 700MB | 动作冒险／探索／解谜／文字冒险 | 以 Kudos 同时奖励速度、漂移和驾驶风格，在伦敦、东京与旧金山街道比赛。DC 生涯结构与真实时间设定鲜明。 |
| <a id="dc-037"></a>DC-037 | ChuChu Rocket! | 啾啾火箭队 | 1999 | Sega | 200MB | 益智／休闲／规则解谜与短局 | 在棋盘上放置方向箭头，引导小鼠进入火箭并避开猫，单人谜题与多人抢鼠同样重要。它也是 DC 早期联网代表之一。 |
| <a id="dc-038"></a>DC-038 | Project Justice | 私立正义学园：热血青春日记 2 | 2000 | Capcom | 800MB | 格斗／清版动作／一对一与场地格斗 | 三人队伍可使用协力技与换人，校园角色和夸张必杀构成 3D 格斗。DC 移植包含额外模式。 |
| <a id="dc-039"></a>DC-039 | Samba de Amigo | 桑巴沙锤 | 2000 | Sega | 400MB | 模拟／音乐／派对／音乐与节奏 | 跟随音乐节拍挥动沙锤并定位高低区域，DC 原版体验依赖专用控制器；普通手柄只是替代方案。 |

---

### NDS

<a id="platform-nds"></a>

以双屏、触控、RPG、文字冒险和本地家庭短局为主，注意触控与麦克风在游戏中的必要性。

| 条目 | 完整商品名（英文／日文） | 中文译名 | 出版日期 | 出版商 | 预留空间 | 品类 | 内容·历史备注 |
|---|---|---|---:|---|---:|---|---|
| <a id="nds-001"></a>NDS-001 | Pokémon HeartGold / SoulSilver | 宝可梦：心金／魂银 | 2009 | Nintendo | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 复刻金银并让首位宝可梦跟随行走，计步器与双地区内容增强陪伴感。它是第二世代内容在 NDS 系统上的扩展重制，不是高清重制。 [系列专题](#series-21)。 |
| <a id="nds-002"></a>NDS-002 | Pokémon Platinum | 宝可梦：白金 | 2008 | Nintendo | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 对《珍珠／钻石》的神奥主线、殿堂和战斗设施进行扩展，骑拉帝纳与毁坏的世界成为视觉中心。神奥位于当代地区体系，与后来《传说 阿尔宙斯》的洗翠时代不能混写。 [系列专题](#series-21)。 |
| <a id="nds-003"></a>NDS-003 | Pokémon Black / White | 宝可梦：黑／白 | 2010 | Nintendo | 128MB | 角色扮演／回合／迷宫／叙事 RPG | 合众地区在首轮冒险中只使用全新图鉴，并正面讨论训练家与宝可梦的关系。较完整的角色冲突使它成为系列叙事受关注的一代。 [系列专题](#series-21)。 |
| <a id="nds-004"></a>NDS-004 | Pokémon Black 2 / White 2 | 宝可梦：黑 2／白 2 | 2012 | Nintendo | 128MB | 角色扮演／回合／迷宫／叙事 RPG | 采用两年后、新主角与新地点的直接续篇结构，而非传统第三版。宝可梦世界锦标赛等内容也让旧作角色重新登场。 [系列专题](#series-21)。 |
| <a id="nds-005"></a>NDS-005 | Phoenix Wright: Ace Attorney / Justice for All / Trials and Tribulations (DS) | 逆转裁判 1／2／3（NDS 版） | 2005 | Capcom | 64MB | 动作冒险／探索／解谜／文字冒险 | NDS 分别移植三部曲，首作另加“复苏的逆转”和触控、麦克风采证；后两作主要是双屏便携化。三部是独立商品。 [系列专题](#series-59)。 |
| <a id="nds-006"></a>NDS-006 | Ace Attorney Investigations: Miles Edgeworth | 逆转检事 | 2009 | Capcom | 64MB | 动作冒险／探索／解谜／文字冒险 | 改用御剑现场调查、逻辑整合与对决，不再以传统法庭为唯一舞台。案件围绕走私组织和八咫乌展开。 [系列专题](#series-59)。 |
| <a id="nds-007"></a>NDS-007 | Gyakuten Kenji 2 / Ace Attorney Investigations 2 | 逆转检事 2 | 2011 | Capcom | 64MB | 动作冒险／探索／解谜／文字冒险 | 继续御剑视角，以逻辑象棋突破对方心理防线，并串联监狱、检察审查会与父辈旧案。日本原版未正式海外发行。 [系列专题](#series-59)。 |
| <a id="nds-008"></a>NDS-008 | Ghost Trick: Phantom Detective | 幽灵诡计：幻影侦探 | 2010 | Capcom | 64MB | 动作冒险／探索／解谜／文字冒险 | 主角以幽灵身份附身物件、操纵机关并回溯死者最后四分钟。西塞尔的身世谜题与一连串救援环环相扣，由巧舟打造但不是《逆转裁判》正传。 [系列专题](#series-59)。 |
| <a id="nds-009"></a>NDS-009 | Professor Layton and the Curious Village | 雷顿教授与不可思议的小镇 | 2008 | Level-5 | 64MB | 益智／休闲／规则解谜与短局 | 在谜样小镇与居民对话并解决百余道独立谜题，提示币和动画串联旅程。它是系列首作。 [系列专题](#series-65)。 |
| <a id="nds-010"></a>NDS-010 | Professor Layton and the Last Specter | 雷顿教授与魔神之笛 | 2008 | Level-5 | 64MB | 益智／休闲／规则解谜与短局 | 作为前传讲述雷顿与路克的相识，以雾都巨兽谜团连接城镇调查和谜题。NDS 版还含长期生活模式。 [系列专题](#series-65)。 |
| <a id="nds-011"></a>NDS-011 | Professor Layton and the Unwound Future | 雷顿教授与最后的时间旅行 | 2010 | Level-5 | 64MB | 益智／休闲／规则解谜与短局 | 以未来伦敦、时间旅行和人物遗憾组织谜题与剧情，叙事在系列早期作品中尤其完整。 [系列专题](#series-65)。 |
| <a id="nds-012"></a>NDS-012 | New Super Mario Bros. | 新超级马力欧兄弟 | 2006 | Nintendo | 64MB | 平台动作／横版／单屏／3D 平台 | 以 2.5D 重启横版马力欧，加入巨大蘑菇、迷你蘑菇和蓝龟壳，双屏用于进度与道具。它是 NDS 原创新作。 [系列专题](#series-01)。 |
| <a id="nds-013"></a>NDS-013 | Super Mario 64 DS | 超级马力欧 64 DS | 2005 | Nintendo | 64MB | 平台动作／横版／单屏／3D 平台 | 扩充为耀西、马力欧、路易吉与瓦力欧四角色和 150 颗星，并加入触控小游戏。场景源自 N64，但触控或按键移动与原版模拟摇杆手感不同。 [系列专题](#series-01)。 |
| <a id="nds-014"></a>NDS-014 | The Legend of Zelda: Phantom Hourglass | 塞尔达传说：幻影沙漏 | 2007 | Nintendo | 64MB | 动作冒险／探索／解谜／文字冒险 | 以触控画线移动、回旋镖路线和海图航行推进，海王神殿需反复潜入并受沙漏时间限制。剧情承接风之杖。 [系列专题](#series-02)。 |
| <a id="nds-015"></a>NDS-015 | The Legend of Zelda: Spirit Tracks | 塞尔达传说：大地的汽笛 | 2009 | Nintendo | 64MB | 动作冒险／探索／解谜／文字冒险 | 以铁路调度代替航海，塞尔达公主可附身幻影与林克协作解谜。排汽、轨道敌人和双人机关是主要特色。 [系列专题](#series-02)。 |
| <a id="nds-016"></a>NDS-016 | Castlevania: Dawn of Sorrow | 恶魔城：苍月十字架 | 2005 | Konami | 64MB | 平台动作／探索型动作 | 直接延续苍月的魂系统与故事，地图、武器合成和封印魔法阵构成推进。触屏画封印可用映射或触控，失败后仍要继续战斗。 [系列专题](#series-11)。 |
| <a id="nds-017"></a>NDS-017 | Castlevania: Portrait of Ruin | 恶魔城：迷宫回廊 | 2006 | Konami | 64MB | 平台动作／探索型动作 | 乔纳森与夏洛特可随时切换并协力，画作迷宫让场景离开单一城堡。双人组合技、任务与装备共同扩展探索。 [系列专题](#series-11)。 |
| <a id="nds-018"></a>NDS-018 | Castlevania: Order of Ecclesia | 恶魔城：被夺走的刻印 | 2008 | Konami | 64MB | 平台动作／探索型动作 | 夏诺亚吸收刻印并自由组合双手攻击，村庄救援和支线连接多个外部区域。敌人强度高，刻印构筑比单纯升级更关键。 [系列专题](#series-11)。 |
| <a id="nds-019"></a>NDS-019 | Dragon Quest IV: Chapters of the Chosen | 勇者斗恶龙 IV：被引导的人们 | 1990 | Enix | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 各章先讲述不同伙伴的命运，最后汇入勇者一行，章节结构让群像塑造格外鲜明。NDS 版属于重新制作，并不存在原稿所写的 GBA 移植。 [系列专题](#series-07)。 |
| <a id="nds-020"></a>NDS-020 | Dragon Quest V: Hand of the Heavenly Bride | 勇者斗恶龙 V：天空的新娘 | 1992 | Square Enix | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 故事跨越主人公少年、成家与为人父的阶段，怪物收服也与家族主题结合。以人生阶段而非单纯王国危机推动叙事，是它最突出的历史地位。 [系列专题](#series-07)。 |
| <a id="nds-021"></a>NDS-021 | Dragon Quest VI: Realms of Revelation | 勇者斗恶龙 VI：幻之大地 | 1995 | Square Enix | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 梦与现实两个世界互相折射，失忆与身份追寻贯穿旅程。转职系统与双世界探索体量庞大，NDS 版是较方便的完整体验方式。 [系列专题](#series-07)。 |
| <a id="nds-022"></a>NDS-022 | Dragon Quest IX: Sentinels of the Starry Skies | 勇者斗恶龙 IX：星空的守护者 | 2010 | Square Enix | 128MB | 角色扮演／回合／迷宫／叙事 RPG | 自定义主角与伙伴，以职业、装备、任务和藏宝图迷宫构成长期冒险。曾强调擦肩与多人，离线单人仍有完整主线。 [系列专题](#series-07)。 |
| <a id="nds-023"></a>NDS-023 | Advance Wars: Dual Strike | 高级战争：双重打击 | 2005 | Nintendo | 64MB | 战略／战棋／大战略与军团 | 双屏呈现地图与情报，双战线、双 CO 和 Tag 技让指挥节奏更复杂。兵种数值仍透明，适合回合推演。 [系列专题](#series-60)。 |
| <a id="nds-024"></a>NDS-024 | Fire Emblem: Shadow Dragon | 火焰之纹章：新·暗黑龙与光之剑 | 2008 | Nintendo | 64MB | 战略／战棋／网格战术 | 以 NDS 重制 FC 初代，调整画面、职业与操作，并加入角色条件和外传。永久阵亡仍是核心，新手不应把重制当无死亡模式。 [系列专题](#series-15)。 |
| <a id="nds-025"></a>NDS-025 | Fire Emblem: New Mystery of the Emblem | 火焰之纹章：新·纹章之谜 | 2010 | Nintendo | 64MB | 战略／战棋／网格战术 | 重制 SFC 纹章之谜第二部，加入自定义主角“我的单位”、支援与更多支线。日本正式发行，不是 Shadow Dragon 的同一内容。 [系列专题](#series-15)。 |
| <a id="nds-026"></a>NDS-026 | Metal Max 3 | 重装机兵 3 | 2010 | Kadokawa Games | 64MB | 角色扮演／动作 RPG | 以末日开放世界、赏金任务和深度战车改装延续系列，并加入更具戏剧性的主角设定。NDS 正统序号作由角川 Games 发行。 [系列专题](#series-14)。 |
| <a id="nds-027"></a>NDS-027 | Metal Saga: Hagane no Kisetsu | 重装机兵：钢之季节 | 2006 | Success | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 《钢之季节》延续初代世界观，采用俯视角探索与战车战斗。它是 2006 年 NDS 作品，不是《重装机兵 2》的高清重制。 [系列专题](#series-14)。 |
| <a id="nds-028"></a>NDS-028 | Super Robot Taisen W | 超级机器人大战 W | 2007 | Bandai | 64MB | 战略／战棋／网格战术 | 以双主角家庭、债务和宇宙航行串联多部机器人作品，剧情衔接广受认可。NDS 双屏显示资料，合体与援护仍是战术重点。 [系列专题](#series-39)。 |
| <a id="nds-029"></a>NDS-029 | Super Robot Taisen K | 超级机器人大战 K | 2009 | Bandai | 64MB | 战略／战棋／网格战术 | 采用多作品小队与伙伴系统，原创故事围绕水晶与异世界展开。参战阵容较偏新世代，和 W 的角色线不连续。 [系列专题](#series-39)。 |
| <a id="nds-030"></a>NDS-030 | Super Robot Taisen L | 超级机器人大战 L | 2010 | Bandai | 64MB | 战略／战棋／网格战术 | 以原作合作关卡、伙伴奖励和机体编成组织战役，原创机体强调多形态攻击。它是 NDS 后期独立作品，不是 K 的直接剧情续篇。 [系列专题](#series-39)。 |
| <a id="nds-031"></a>NDS-031 | Rhythm Heaven / Rhythm Tengoku Gold | 节奏天国 | 2008 | Nintendo | 32MB | 模拟／音乐／派对／音乐与节奏 | NDS 续作以点击、滑动和长按完成节奏关卡，判定集中于少数触控动作。横竖持机和按键映射需先配置。 |
| <a id="nds-032"></a>NDS-032 | Animal Crossing: Wild World | 欢迎来到动物森友会 | 2006 | Nintendo | 64MB | 模拟／音乐／派对／经营与生活模拟 | 村庄随真实时钟运行，居民、采集、钓鱼与布置形成无强制终点的日常。NDS 版首次引入在线访问，离线仍有完整生活循环。 |
| <a id="nds-033"></a>NDS-033 | Etrian Odyssey | 世界树迷宫 | 2007 | Atlus | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 玩家用触屏逐格绘制地图，队伍技能与 FOE 位置管理同样重要。它把“地图由玩家完成”变成探索和记忆的一部分。 [系列专题](#series-66)。 |
| <a id="nds-034"></a>NDS-034 | Etrian Odyssey II: Heroes of Lagaard | 世界树迷宫 II：诸王的圣杯 | 2008 | Atlus | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 玩家在下屏自行绘制迷宫地图，以职业、FOE 可见强敌和资源管理深入世界树。二代增加职业与便利调整。 [系列专题](#series-66)。 |
| <a id="nds-035"></a>NDS-035 | 999: Nine Hours, Nine Persons, Nine Doors | 极限脱出：9 小时 9 人 9 扇门 | 2009 | Chunsoft | 64MB | 动作冒险／探索／解谜／文字冒险 | 九人被困于沉船设施，在数字根规则下分组进入房间解谜，逃生与多结局叙事互相嵌套。它是“极限脱出”系列起点。 |
| <a id="nds-036"></a>NDS-036 | Inazuma Eleven | 闪电十一人 | 2008 | Level-5 | 64MB | 竞速／体育／体育与运动 | 足球比赛与 RPG 练级、招募和必杀技结合，触控用于移动与指令。Level-5 由此建立长期跨媒体系列。 |
| <a id="nds-037"></a>NDS-037 | Inazuma Eleven 2: Kyoui no Shinryakusha – Fire / Blizzard | 闪电十一人 2：威胁的侵略者 | 2009 | Level-5 | 64MB | 竞速／体育／体育与运动 | 加入外星球队威胁与更多角色，双版本提供不同对手和收服内容。系统延续首作而非普通体育年货。 |
| <a id="nds-038"></a>NDS-038 | Kingdom Hearts 358/2 Days | 王国之心：358/2 天 | 2009 | Square Enix | 64MB | 角色扮演／动作 RPG | 以洛克萨斯在 XIII 机关的日常任务串联故事，面板系统决定魔法、能力与等级配置。它补充了《王国之心 II》前后的角色背景。 [系列专题](#series-61)。 |
| <a id="nds-039"></a>NDS-039 | Digimon World Dawn / Dusk | 数码宝贝传说：日光／月光 | 2006 | Bandai | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 双版本分别以不同区域、任务和数码兽阵容展开，培育、农场岛与属性搭配决定队伍。它们是同世代互补版本，不是昼／夜两个地区别名。 [系列专题](#series-67)。 |
| <a id="nds-040"></a>NDS-040 | Rune Factory: A Fantasy Harvest Moon | 符文工房：新牧场物语 | 2006 | Marvelous | 64MB | 模拟／音乐／派对／经营与生活模拟 | 在牧场经营外加入迷宫、武器战斗和怪物驯养，角色体力与农事、探索共享。它是系列首作。 [系列专题](#series-23)。 |
| <a id="nds-041"></a>NDS-041 | Rune Factory 2: A Fantasy Harvest Moon | 符文工房 2 | 2007 | Marvelous | 64MB | 模拟／音乐／派对／经营与生活模拟 | 以父子两代和村镇学校扩展生活循环，委托、农作、战斗和怪物培养并存。剧情跨代是主要特色。 [系列专题](#series-23)。 |
| <a id="nds-042"></a>NDS-042 | Harvest Moon: Grand Bazaar | 牧场物语：风之集市 | 2008 | Marvelous | 64MB | 模拟／音乐／派对／经营与生活模拟 | 把农产品加工后带到定期集市销售，风向、跳跃和摊位经营改变牧场节奏。利润不只来自每日出货箱。 [系列专题](#series-23)。 |
| <a id="nds-043"></a>NDS-043 | Mario Kart DS | 马力欧卡丁车 DS | 2005 | Nintendo | 64MB | 竞速／体育／竞速与驾驶 | 加入任务模式和全新／复古赛道组合，双屏显示地图与战况。曾支持网络服务，当前收藏应以本地单机与多人功能为基线。 [系列专题](#series-01)。 |
| <a id="nds-044"></a>NDS-044 | Yoshi’s Island DS | 耀西岛 DS | 2006 | Nintendo | 64MB | 平台动作／横版／单屏／3D 平台 | 婴儿马力欧、桃花公主、大金刚等提供不同能力，巨大耀西蛋用于重型破坏。双屏扩大纵向视野，也要求同时留意两个画面。 [系列专题](#series-01)。 |
| <a id="nds-045"></a>NDS-045 | Mega Man ZX | 洛克人 ZX | 2006 | Capcom | 64MB | 平台动作／横版／单屏／3D 平台 | Model X／Z／H／F／P／L 变身提供不同移动与攻击，地图以相互连通区域组织任务。它把 Zero 的动作与探索型地图结合。 [系列专题](#series-03)。 |
| <a id="nds-046"></a>NDS-046 | Mega Man ZX Advent | 洛克人 ZX Advent | 2007 | Capcom | 64MB | 平台动作／横版／单屏／3D 平台 | 可变身为击败的 Boss 与伪洛克人，能力直接服务地形和战斗；男女主角共享主线。任务与变身数量明显增加。 [系列专题](#series-03)。 |
| <a id="nds-047"></a>NDS-047 | Mega Man Star Force: Pegasus / Leo / Dragon | 流星洛克人：天马／雄狮／天龙 | 2006 | Capcom | 64MB | 平台动作／横版／单屏／3D 平台 | 把网络世界观推进到电波时代，战斗改为洛克人背后视角的三行移动与卡牌。三版本提供不同属性变身和卡片内容。 [系列专题](#series-03)。 |
| <a id="nds-048"></a>NDS-048 | Golden Sun: Dark Dawn | 黄金太阳：漆黑的黎明 | 2010 | Nintendo | 128MB | 角色扮演／回合／迷宫／叙事 RPG | 以初代后代为主角，精神力解谜、精灵收集与召唤延续 GBA 体系。新大陆和角色让故事与前两作相连但可独立识别。 [系列专题](#series-58)。 |
| <a id="nds-049"></a>NDS-049 | Final Fantasy III (Nintendo DS) | 最终幻想 III（NDS 重制版） | 2006 | Square Enix | 128MB | 角色扮演／回合／迷宫／叙事 RPG | 以全 3D 重制 FC 三代，重做角色形象、职业平衡和事件，并调整最终迷宫存档节奏。它与 FC 像素版应分目录。 [系列专题](#series-06)。 |
| <a id="nds-050"></a>NDS-050 | Final Fantasy IV (Nintendo DS) | 最终幻想 IV（NDS 重制版） | 2007 | Square Enix | 128MB | 角色扮演／回合／迷宫／叙事 RPG | 全 3D、配音与增强难度重塑四代，Decant Ability 让离队角色能力可继承。它不是 GBA 的 2D Advance 版。 [系列专题](#series-06)。 |
| <a id="nds-051"></a>NDS-051 | SaGa 2: Hihou Densetsu – Goddess of Destiny | 沙加 2：秘宝传说－命运女神 | 2009 | Square Enix | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 以 3D 和地图探索重制 GB 沙加 2，保留秘宝、种族成长与多世界旅程，并加入连携和剧情调整。不是最终幻想 II 重制。 [系列专题](#series-22)。 |
| <a id="nds-052"></a>NDS-052 | Final Fantasy Crystal Chronicles: Echoes of Time | 最终幻想水晶编年史：时之回声 | 2009 | Square Enix | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 以多人地牢动作、装备与部落职业为核心，NDS 版可与 Wii 同内容联动。单人也能游玩，但家庭电视使用时不把历史联机功能写成当前可用。 [系列专题](#series-06)。 |
| <a id="nds-053"></a>NDS-053 | Dragon Quest Monsters: Joker | 勇者斗恶龙怪兽篇 Joker | 2006 | Square Enix | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 在绿色侦察队大赛中捕捉、合成怪物，以技能树和队伍搭配战斗。它是怪兽篇 3D 化新起点，不是 DQM 旧作移植。 [系列专题](#series-07)。 |
| <a id="nds-054"></a>NDS-054 | Dragon Quest Monsters: Joker 2 | 勇者斗恶龙怪兽篇 Joker 2 | 2010 | Square Enix | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 扩大怪物阵容与合成体系，加入巨型怪物和更强队伍构筑。剧情围绕飞艇失事与岛屿探索，和 Joker 初代分版本。 [系列专题](#series-07)。 |
| <a id="nds-055"></a>NDS-055 | Pokémon Mystery Dungeon: Blue Rescue Team | 宝可梦不可思议迷宫：青救助队 | 2005 | Nintendo | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 与 GBA《赤救助队》共享故事和队伍，NDS 版利用双屏与触控呈现信息。选择版本时应看作介质与操作差异，而不是连续两作。 [系列专题](#series-21)。 |
| <a id="nds-056"></a>NDS-056 | Pokémon Mystery Dungeon: Explorers of Time | 宝可梦不可思议迷宫：时之探险队 | 2007 | Nintendo | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 玩家变成宝可梦，与伙伴加入探险队，在随机迷宫管理招式、饥饿与道具。剧情与时间停止主题突出，和 Darkness 仅有内容差异。 [系列专题](#series-21)。 |
| <a id="nds-057"></a>NDS-057 | Pokémon Mystery Dungeon: Explorers of Darkness | 宝可梦不可思议迷宫：暗之探险队 | 2007 | Nintendo | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 与 Time 共享主线和大部分迷宫，以版本宝可梦及道具差异构成另一商品。收藏时不必为地区别名重复计数。 [系列专题](#series-21)。 |
| <a id="nds-058"></a>NDS-058 | Pokémon Mystery Dungeon: Explorers of Sky | 宝可梦不可思议迷宫：空之探险队 | 2009 | Nintendo | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 在时／暗探险队基础上加入特别章节、宝可梦和便利调整，是内容更完整的扩展版。主线仍是探险队故事，不是正统第四世代复刻。 [系列专题](#series-21)。 |
| <a id="nds-059"></a>NDS-059 | Pokémon Ranger | 宝可梦护林员 | 2006 | Nintendo | 64MB | 角色扮演／回合／迷宫／叙事 RPG | 用触屏连续画圈临时收服宝可梦，以其场地能力清除障碍；强调守护自然而非传统捕获。它是护林员系列首作。 [系列专题](#series-21)。 |
| <a id="nds-060"></a>NDS-060 | Osu! Tatakae! Ouendan / Elite Beat Agents | 押忍！战斗！应援团／节拍特工 | 2006 | Nintendo | 32MB | 动作冒险／探索／解谜／文字冒险 | 用触屏按节拍点击、滑动与旋转，应援团以日本歌曲和漫画剧情呈现，节拍特工则面向海外改编。两作操作同源。 |
| <a id="nds-061"></a>NDS-061 | WarioWare: Touched! | 摸摸瓦力欧制造 | 2005 | Nintendo | 64MB | 益智／休闲／规则解谜与短局 | 微游戏全面改用触摸、拖动与麦克风，身体动作比按键更直接。麦克风只服务特定关卡，普通游戏不应据此假设系统语音功能。 [系列专题](#series-01)。 |
| <a id="nds-062"></a>NDS-062 | Daigasso! Band Brothers | 大合奏！乐团兄弟 | 2004 | Nintendo | 32MB | 模拟／音乐／派对／音乐与节奏 | 用按键演奏乐曲的多个声部，并可编辑音乐，难度随乐器部分变化。NDS 首作强调合奏概念。 |
| <a id="nds-063"></a>NDS-063 | Brain Age: Train Your Brain in Minutes a Day! | 成年人的 DS 脑力锻炼 | 2005 | Nintendo | 32MB | 益智／休闲／规则解谜与短局 | 以计算、记忆与阅读等短练习构成每日训练，利用触控和麦克风。它不是传统剧情游戏，适合家庭轮换短局。 |
| <a id="nds-064"></a>NDS-064 | Nintendogs | 任天狗 | 2005 | Nintendo | 64MB | 模拟／音乐／派对／经营与生活模拟 | 通过触摸、语音和日常照料养育虚拟犬，散步与比赛提供长期目标。NDS 双屏和麦克风直接参与互动。 |
| <a id="nds-065"></a>NDS-065 | Cooking Mama | 料理妈妈 | 2006 | Taito / 505 Games | 32MB | 益智／休闲／规则解谜与短局 | 把切菜、搅拌、煎炒拆成触屏小游戏，按步骤准确度评分。短小流程与直观操作适合家庭轮玩。 |
| <a id="nds-066"></a>NDS-066 | Shin Megami Tensei: Strange Journey | 真·女神转生：奇妙之旅 | 2009 | Atlus | 128MB | 角色扮演／回合／迷宫／叙事 RPG | 调查南极“灭世之地”，恶魔交涉、合体与属性克制维持本传硬核 RPG 结构。科幻军事考察外壳和阵营选择使它区别于校园向 Persona。 [系列专题](#series-51)。 |
| <a id="nds-067"></a>NDS-067 | Okamiden | 大神传：小小太阳 | 2010 | Capcom | 128MB | 动作冒险／探索／解谜／文字冒险 | 以笔神在地图上绘制奇迹，故事围绕小小太阳与伙伴旅行。它在 NDS 上延续《大神》的水墨视觉和解谜，而非简单缩小版移植。 |
| <a id="nds-068"></a>NDS-068 | Final Fantasy Tactics A2: Grimoire of the Rift | 最终幻想战略版 A2：封穴的魔法书 | 2007 | Square Enix | 128MB | 战略／战棋／网格战术 | 回到伊瓦利斯，以任务、法则、职业和地域 auction 组织队伍成长。它是 FFTA 的续作，不是 PS1 FFT 移植，也不属于皇家骑士团。 [系列专题](#series-06)。 |
| <a id="nds-069"></a>NDS-069 | Grand Theft Auto: Chinatown Wars | 侠盗猎车手：唐人街战争 | 2009 | Rockstar Games | 128MB | 动作冒险／探索／解谜／文字冒险 | 采用俯视角与触屏交互，在自由城完成帮派任务、驾驶和小游戏，毒品交易经济是特色。NDS 与 PSP 版本在画面和操作呈现上不同。 |
| <a id="nds-070"></a>NDS-070 | Kirby: Canvas Curse | 触摸！卡比 | 2005 | Nintendo | 64MB | 平台动作／横版／单屏／3D 平台 | 卡比化为球，玩家用触控画彩虹线引导移动、抵挡障碍并触发能力。它是围绕触控重新设计的动作游戏，不是普通平台移植。 [系列专题](#series-20)。 |
| <a id="nds-071"></a>NDS-071 | Kirby: Squeak Squad | 星之卡比：参上！怪盗洛切团 | 2006 | Nintendo | 64MB | 平台动作／横版／单屏／3D 平台 | 以宝箱追逐和鼠盗贼团组织关卡，泡泡宝箱可在下屏储存并组合食物、能力。主线轻松，收集决定完整度。 [系列专题](#series-20)。 |
| <a id="nds-072"></a>NDS-072 | Mario & Luigi: Partners in Time | 马力欧与路易吉 RPG 2×2 | 2005 | Nintendo | 64MB | 平台动作／横版／单屏／3D 平台 | 成年兄弟与婴儿兄弟分屏同行，四个按键分别控制动作和战斗指令。时间旅行让过去与现在的关卡状态相互呼应。 [系列专题](#series-01)。 |
| <a id="nds-073"></a>NDS-073 | Mario & Luigi: Bowser’s Inside Story | 马力欧与路易吉 RPG 3!!! | 2009 | Nintendo | 128MB | 平台动作／横版／单屏／3D 平台 | 兄弟在库巴体内探索，库巴在外部行动，两边状态互相影响；巨大库巴战改变持机方式。动作指令仍是攻防核心。 [系列专题](#series-01)。 |
| <a id="nds-074"></a>NDS-074 | The World Ends with You | 美妙世界 | 2007 | Square Enix | 128MB | 动作冒险／探索／解谜／文字冒险 | 以涩谷文化和死神游戏为舞台，双屏分别控制两名角色，徽章组合决定攻击方式。美术、音乐与系统风格高度统一，是 NDS 原创动作 RPG 的代表。 |
| <a id="nds-075"></a>NDS-075 | Densetsu no Stafy 4 | 传说的斯塔菲 4 | 2006 | Nintendo | 64MB | 平台动作／横版／单屏／3D 平台 | 把海洋平台动作扩展到双屏，斯塔菲与斯塔碧的能力、变身和触摸操作共同参与关卡。它是系列第四作，日版剧情与委托需要一定阅读。 [系列专题](#series-92)。 |
| <a id="nds-076"></a>NDS-076 | The Legendary Starfy | 传说的斯塔菲：对决！达伊尔海贼团 | 2008 | Nintendo | 128MB | 平台动作／横版／单屏／3D 平台 | 系列第五作，也是当年唯一正式推出英文版的斯塔菲游戏；海底探索、变身和伙伴协力延续轻快节奏。不能把英文标题误当成 GBA 初代。 [系列专题](#series-92)。 |

---

## 游戏品类：源流与代表作

本章按每个条目的主要玩法归类，细分方向写在平台表的“品类”列。代表系列链接回专题，代表条目链接回平台；跨类型作品只设一个主品类，避免重复计数。

### 平台动作

从街机单屏《Donkey Kong》、FC 卷轴《Super Mario Bros.》到 16 位高速动作与 3D 收集，核心始终是移动手感、空间判断和关卡节奏。细分包括单屏动作、横版卷轴、跑跳解谜、3D 平台，以及靠能力回环打开地图的“银河城”。

代表作：[超级马力欧兄弟](#nes-001)、[刺猬索尼克 2](#md-002)、[超级密特罗德](#snes-005)、[恶魔城 X：月下夜想曲](#ps1-004)、[桑塔](#gbc-004)、[风之少年：通往幻界之门](#ps1-080)。
相关系列：[马力欧](#series-01)、[洛克人](#series-03)、[炸弹人](#series-10)、[恶魔城](#series-11)、[密特罗德](#series-18)、[星之卡比](#series-20)、[索尼克](#series-25)、[魔界村](#series-48)。

本库细分：横版／单屏／3D 平台、探索型动作。

### 动作冒险

这一大类把动作操作放进探索、解谜或叙事空间。塞尔达的迷宫道具、生存恐怖的资源压力、潜行游戏的视锥与声音、视觉小说的调查指证都属于不同分支；它们共享“如何理解并穿过这个空间”，但不共享同一种战斗。

代表作：[塞尔达传说：众神的三角力量](#snes-004)、[合金装备](#ps1-009)、[生化危机](#ps1-001)、[幽灵诡计：幻影侦探](#nds-008)、[极限脱出：9 小时 9 人 9 扇门](#nds-035)、[古墓丽影 1／2／3](#ps1-054)。
相关系列：[塞尔达传说](#series-02)、[魂斗罗](#series-04)、[热血系列](#series-12)、[忍者神龟](#series-13)、[合金装备](#series-19)、[恶魔城](#series-11)、[龙珠](#series-16)、[前线任务](#series-38)。

本库细分：探索／解谜／文字冒险、生存恐怖与潜行。

### 射击

从固定屏幕的《Space Invaders》到横纵卷轴、弹幕、跑射、轨道射击和第一人称射击，技术演进改变视野，也改变敌弹与空间的关系。高分系统常把风险路线叠加在通关之上，双人协作则是街机与家庭机的重要传统。

代表作：[宇宙巡航机](#nes-041)、[异形战机](#md-051)、[斑鸠](#dc-008)、[火枪英雄](#md-034)、[合金弹头系列](#fbneo-128)、[007：黄金眼](#n64-005)。
相关系列：[魂斗罗](#series-04)、[宇宙巡航机与兵蜂](#series-09)、[合金装备](#series-19)、[雷电与R-Type](#series-35)、[Darius](#series-49)、[合金弹头](#series-63)、[宝可梦](#series-21)、[怒首领蜂与Cave](#series-70)。

本库细分：跑射与动作射击、卷轴与弹幕射击。

### 格斗／清版动作

清版动作由《双截龙》《快打旋风》把街头推进、投技与多人合作定型；一对一格斗则由《Street Fighter II》确立帧数、距离和角色博弈。3D 场地格斗与派对乱斗进一步扩大分支，但本地对战始终是核心。

代表作：[街头霸王2](#fbneo-058)、[拳皇98](#fbneo-030)、[怒之铁拳 2](#md-005)、[恐龙快打](#fbneo-007)、[灵魂能力](#dc-004)、[能量宝石 2](#dc-013)。
相关系列：[双截龙](#series-08)、[忍者神龟](#series-13)、[三国志与三国题材](#series-05)、[怒之铁拳](#series-26)、[战斧](#series-27)、[街头霸王](#series-31)、[饿狼与龙虎之拳](#series-33)、[侍魂与月华剑士](#series-34)。

本库细分：清版动作与合作、一对一与场地格斗。

### 角色扮演

家用 JRPG 从《Dragon Quest》《Final Fantasy》的清晰回合制出发，逐渐分化出 ATB、职业构筑、动作战斗、怪物养成、迷宫绘制与高文本叙事。此处把战棋单列；塞尔达等没有数值成长主轴的作品归动作冒险。

代表作：[勇者斗恶龙 III：传说的开始](#nes-032)、[最终幻想 VI](#snes-009)、[超时空之钥](#snes-006)、[宝可梦：绿宝石](#gba-002)、[幻想水浒传 II](#ps1-035)、[英雄传说：空之轨迹 FC](#psp-003)。
相关系列：[最终幻想](#series-06)、[勇者斗恶龙](#series-07)、[重装机兵](#series-14)、[三国志与三国题材](#series-05)、[龙珠](#series-16)、[宝可梦](#series-21)、[沙加](#series-22)、[星之海洋](#series-24)。

本库细分：回合／迷宫／叙事 RPG、动作 RPG。

### 战略／战棋

光荣历史模拟把内政、外交与战争连成宏观循环；火焰之纹章、皇家骑士团和最终幻想战略版则聚焦网格、单位与角色成长。机器人大战的授权群像、战场女武神的即时移动进一步证明“战棋”并不只有一种节奏。

代表作：[火焰之纹章：圣战之系谱](#snes-013)、[皇家骑士团：命运之轮](#snes-015)、[最终幻想战略版](#ps1-008)、[高级战争](#gba-032)、[三国志 II](#md-012)、[战场女武神 2](#psp-022)。
相关系列：[三国志与三国题材](#series-05)、[火焰之纹章](#series-15)、[信长之野望](#series-28)、[光明与梦幻模拟战](#series-29)、[大战略与装甲将军](#series-30)、[皇家骑士团](#series-37)、[超级机器人大战](#series-39)、[高级战争](#series-60)。

本库细分：大战略与军团、网格战术、即时军事模拟。

### 竞速／体育

竞速从街机计时、伪 3D 路带发展到卡丁车道具、拟真调校与高速反重力；体育则在规则还原和电视节奏之间取舍。足球 RPG、马力欧体育和滑板目标模式说明这一大类的乐趣并不只来自模拟真实赛事。

代表作：[超级马力欧卡丁车](#snes-047)、[山脊赛车 Type 4](#ps1-051)、[F-ZERO X](#n64-007)、[托尼·霍克职业滑板 2](#ps1-077)、[天使之翼](#nes-061)、[Neo Turf Masters](#fbneo-056)。
相关系列：[热血系列](#series-12)、[马力欧](#series-01)、[山脊赛车](#series-76)、[GT赛车](#series-86)、[古惑狼](#series-84)。

本库细分：体育与运动、竞速与驾驶。

### 益智／休闲

俄罗斯方块、泡泡龙解谜、噗哟噗哟与宝石方块证明经典休闲并非附属：短规则能产生长期精通，本地对战又能直接服务家庭场景。细分包括落块消除、物理解谜、路线规划、绘图逻辑与短局动作益智。

代表作：[俄罗斯方块](#nes-088)、[泡泡龙解谜 1／2／3／4](#fbneo-112)、[噗哟噗哟通](#fbneo-130)、[宝石方块](#gg-015)、[Gunpey 线条接龙](#ws-001)、[Lemmings](#snes-095)。
相关系列：[俄罗斯方块](#series-17)、[马力欧](#series-01)、[宝可梦](#series-21)、[钻地先生](#series-62)、[雷顿教授](#series-65)、[音乐方块](#series-78)、[噗哟噗哟](#series-88)、[块魂](#series-90)。

本库细分：落块与消除、规则解谜与短局。

### 模拟／音乐／派对

生活模拟重视日程与关系，经营模拟重视资源循环，音乐游戏把输入映射到节拍，派对和微游戏则降低旁观与轮换门槛。专用控制器会改变体验，因此本指南优先保留普通手柄仍能成立的作品。

代表作：[牧场物语](#snes-069)、[欢迎来到动物森友会](#nds-032)、[节奏天国](#nds-031)、[马力欧派对 1／2／3](#n64-027)、[PaRappa](#ps1-057)、[瓦力欧制造：超迷你游戏](#gba-043)。
相关系列：[牧场物语与符文工房](#series-23)、[马力欧](#series-01)、[Theme 经营模拟](#series-91)。

本库细分：经营与生活模拟、生活模拟与派对、音乐与节奏。

---

## 两个深化专题

### 史克威尔 2D 黄金期：圣剑、沙加与圣龙

这里的“黄金期”指 Square 从 FC／GB 到 SFC，再延伸到 PS1 2D／预渲染制作阶段，不把 Enix 的《勇者斗恶龙》《星之海洋》混入 Square 年表。《圣剑传说》从最终幻想外传独立成动作 RPG；《沙加》不断试验自由剧本、闪悟和非常规成长；《圣龙传说》则把龙、地形与网格战斗结合，是独立作品而不是一个长系列。

| 支线 | 发展脉络与代表作品 |
|---|---|
| 圣剑传说 | [圣剑传说：最终幻想外传](#gb-034) 的 GB 原点 → [圣剑传说 2](#snes-023) 的多人环形菜单 → [圣剑传说 3](#snes-024) 的多主角与转职 → [圣剑传说：玛娜传奇](#ps1-083) 的世界构筑；[新约圣剑传说](#gba-075) 则是对 GB 初代的重新诠释。 |
| 沙加 | [魔界塔士 SaGa](#gb-016) 的 GB 三部曲 → [浪漫沙加](#snes-052) 的 SFC 自由剧本 → [浪漫沙加：开拓者](#ps1-084) 与 [浪漫沙加：开拓者 2](#ps1-085) 的多主角、世代和连携实验。 |
| 圣龙与同期系统探索 | [Bahamut Lagoon](#snes-056) 用龙与地形改变战棋；[鲁多拉秘宝](#snes-105) 用言灵组合魔法；[时空勇士](#snes-048) 以分时代章节汇流，[超时空之钥](#snes-006) 则以时空和协力技代表另一种高峰。 |

版本勾稽：GB《Final Fantasy Adventure》归入圣剑，不归最终幻想正传；《Secret of Mana》是圣剑 2，《Trials of Mana》是圣剑 3；《Bahamut Lagoon》只列一次“圣龙”主题，不虚构续作。

### 街机 STG 进化史：从传统射击到高密度弹幕

这条时间线按机制而不是“厂商名气”排列。Toaplan（东亚企划）强化关卡记忆、武器和节奏；彩京把角色、蓄力攻击与近战风险结合起来；Cave 则把敌弹密度、连锁、得分和 Hyper 等系统推到新层次。**“擦弹”并非所有 Cave 作品的统一核心**：《怒首领蜂》重点是连锁与弹幕，《大往生》还要理解 Hyper 的资源收益。

| 年代 | 厂商／流派 | 条目回链 | 在进化史中的位置 |
|---:|---|---|---|
| 1985 | Toaplan | [虎直升机](#fbneo-089) | 早期纵版空战，以炸弹和固定关卡节奏建立记忆型射击。 |
| 1987 | Irem | [异形战机](#md-051) | 蓄力炮与 Force 装置改变站位，关卡解谜性显著增强。 |
| 1988 | Toaplan | [Truxton](#fbneo-091) | 高速敌群、武器升级与严苛关卡延续传统硬派路线。 |
| 1990 | Seibu Kaihatsu | [Raiden](#pce-007) | 双色武器、双人协作和易懂节奏让雷电成为街机厅常青树。 |
| 1993 | Toaplan | [蝙蝠枪](#fbneo-124) | 角色与火力成长、密集弹幕已显露后来 Cave 风格的先声。 |
| 1994–1999 | 彩京 Psikyo | [Gunbird 1](#fbneo-080) | 武装飞鸟、Strikers 与战国系列把角色射击和蓄力攻击发展成稳定体系。 |
| 1996 | 彩京 Psikyo | [战国之刃](#fbneo-078) | 横版角色射击，近战与蓄力让风险站位比单纯躲弹更重要。 |
| 1996 | Raizing／8ing | [Battle Garegga](#fbneo-094) | 动态难度与得分资源相互牵制，高手路线和首次通关几乎是两种玩法。 |
| 1997 | Cave | [怒首领蜂](#fbneo-084) | 连锁击破、蜂道具与高密度弹幕结合，确立 Cave 的代表性得分语言。 |
| 1998 | Cave | [ESP Ra.De.](#fbneo-086) | 角色灵力与穿透攻击加入得分决策，弹幕不仅是生存压力也是资源。 |
| 1999 | 彩京 Psikyo | [打击者 1945 III](#fbneo-077) | 以现代喷气机、蓄力攻击和变形 Boss 延续 1945 系列。 |
| 2000 | 彩京 Psikyo | [Dragon Blaze](#fbneo-082) | 龙的分离与召回改变攻击位置，是彩京机制创新的典型。 |
| 2001 | Cave／Capcom | [Progear 的岚](#fbneo-088) | 横向弹幕、宝石与连击构成另一条 Cave 路线，画面和音乐风格鲜明。 |
| 2002 | Cave | [大往生](#fbneo-085) | Hyper 同时增强火力与风险，资源管理进入背板和得分核心。 |
| 2003 | Cave | [长空超少年Espgaluda](#fbneo-087) | 觉醒系统改变敌弹与得分规则，进一步强化攻防转换。 |

补充交叉索引：彩京另见 [打击者1945](#fbneo-075)，Toaplan 另见 [飞翔鲛](#fbneo-090) 与 [异域战将](#fbneo-093)；Treasure 的 [斑鸠](#dc-008) 以黑白极性吸收敌弹，不属于 Cave，却构成理解弹幕规则创新的必要对照。

---

## 系列专题与平台回链

### 马力欧

<a id="series-01"></a>

按平台动作、卡丁车、派对、体育、RPG、瓦力欧、咚奇刚与耀西拆分。

#### 平台动作

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Super Mario Bros. | 超级马力欧兄弟 | NES | 1985 | [NES-001](#nes-001) |
| Super Mario Bros. 2 (USA) | 超级马力欧兄弟 2（海外版） | NES | 1988 | [NES-002](#nes-002) |
| Super Mario Bros. 3 | 超级马力欧兄弟 3 | NES | 1988 | [NES-003](#nes-003) |
| Mario Bros. | 马力欧兄弟 | NES | 1985 | [NES-085](#nes-085) |
| Super Mario Bros.: The Lost Levels | 超级马力欧兄弟 2（日版） | NES | 1986 | [NES-090](#nes-090) |
| Super Mario Land | 超级马力欧乐园 | GB | 1989 | [GB-002](#gb-002) |
| Super Mario Land 2: 6 Golden Coins | 超级马力欧乐园 2：六枚金币 | GB | 1992 | [GB-003](#gb-003) |
| Dr. Mario | 马力欧医生 | GB | 1990 | [GB-026](#gb-026) |
| Super Mario Bros. Deluxe | 超级马力欧兄弟 DX | GBC | 1999 | [GBC-011](#gbc-011) |
| Super Mario World | 超级马力欧世界 | SNES | 1991 | [SNES-001](#snes-001) |
| Super Mario All-Stars | 超级马力欧合集 | SNES | 1993 | [SNES-101](#snes-101) |
| Super Mario 64 | 超级马力欧 64 | N64 | 1996 | [N64-003](#n64-003) |
| Super Mario Advance | 超级马力欧 Advance（超级马力欧兄弟 2） | GBA | 2001 | [GBA-014](#gba-014) |
| Super Mario World: Super Mario Advance 2 | 超级马力欧世界：超级马力欧 Advance 2 | GBA | 2001 | [GBA-015](#gba-015) |
| Super Mario Advance 4: Super Mario Bros. 3 | 超级马力欧 Advance 4：超级马力欧兄弟 3 | GBA | 2003 | [GBA-017](#gba-017) |
| New Super Mario Bros. | 新超级马力欧兄弟 | NDS | 2006 | [NDS-012](#nds-012) |
| Super Mario 64 DS | 超级马力欧 64 DS | NDS | 2005 | [NDS-013](#nds-013) |

#### 咚奇刚

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Donkey Kong | 咚奇刚 | NES | 1983 | [NES-086](#nes-086) |
| Donkey Kong (Game Boy) | 咚奇刚（GB） | GB | 1994 | [GB-029](#gb-029) |
| Donkey Kong Country | 咚奇刚国度 | SNES | 1994 | [SNES-041](#snes-041) |
| Donkey Kong Country 2: Diddy’s Kong Quest | 咚奇刚国度 2：迪迪刚大冒险 | SNES | 1995 | [SNES-042](#snes-042) |
| Donkey Kong Country 3: Dixie Kong’s Double Trouble! | 咚奇刚国度 3：迪克西刚的双重麻烦 | SNES | 1996 | [SNES-043](#snes-043) |
| Donkey Kong 64 | 咚奇刚 64 | N64 | 1999 | [N64-014](#n64-014) |
| Mario vs. Donkey Kong | 马力欧对咚奇刚 | GBA | 2004 | [GBA-067](#gba-067) |
| Donkey Kong / Donkey Kong Jr. | 咚奇刚／咚奇刚 Jr. | MAME | 1981–1982 | [MAME-019](#mame-019) |

#### 瓦力欧

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Wario Land: Super Mario Land 3 | 瓦力欧乐园：超级马力欧乐园 3 | GB | 1994 | [GB-004](#gb-004) |
| Wario Land 3 | 瓦力欧乐园 3 | GBC | 2000 | [GBC-002](#gbc-002) |
| Wario Land II | 瓦力欧乐园 2 | GBC | 1998 | [GBC-010](#gbc-010) |
| Wario’s Woods | 瓦力欧的森林 | SNES | 1994 | [SNES-092](#snes-092) |
| WarioWare, Inc.: Mega Microgame$! | 瓦力欧制造：超迷你游戏 | GBA | 2003 | [GBA-043](#gba-043) |
| Wario Land 4 | 瓦力欧乐园 4 | GBA | 2001 | [GBA-044](#gba-044) |
| WarioWare Twisted! | 转转瓦力欧制造 | GBA | 2004 | [GBA-073](#gba-073) |
| WarioWare: Touched! | 摸摸瓦力欧制造 | NDS | 2005 | [NDS-061](#nds-061) |

#### 耀西

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Yoshi | 耀西的蛋 | GB | 1991 | [GB-027](#gb-027) |
| Super Mario World 2: Yoshi’s Island | 超级马力欧世界 2：耀西岛 | SNES | 1995 | [SNES-002](#snes-002) |
| Yoshi’s Story | 耀西的故事 | N64 | 1998 | [N64-015](#n64-015) |
| Yoshi’s Island: Super Mario Advance 3 | 耀西岛：超级马力欧 Advance 3 | GBA | 2002 | [GBA-016](#gba-016) |
| Yoshi’s Island DS | 耀西岛 DS | NDS | 2006 | [NDS-044](#nds-044) |

#### 角色扮演

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Super Mario RPG: Legend of the Seven Stars | 超级马力欧 RPG：七星传说 | SNES | 1996 | [SNES-003](#snes-003) |
| Paper Mario | 纸片马力欧 | N64 | 2001 | [N64-013](#n64-013) |
| Mario & Luigi: Superstar Saga | 马力欧与路易吉 RPG | GBA | 2003 | [GBA-018](#gba-018) |
| Mario & Luigi: Partners in Time | 马力欧与路易吉 RPG 2×2 | NDS | 2005 | [NDS-072](#nds-072) |
| Mario & Luigi: Bowser’s Inside Story | 马力欧与路易吉 RPG 3!!! | NDS | 2009 | [NDS-073](#nds-073) |

#### 卡丁车

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Super Mario Kart | 超级马力欧卡丁车 | SNES | 1992 | [SNES-047](#snes-047) |
| Mario Kart 64 | 马力欧卡丁车 64 | N64 | 1996 | [N64-004](#n64-004) |
| Mario Kart: Super Circuit | 马力欧卡丁车 Advance | GBA | 2001 | [GBA-045](#gba-045) |
| Mario Kart DS | 马力欧卡丁车 DS | NDS | 2005 | [NDS-043](#nds-043) |

#### 体育

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mario Tennis | 马力欧网球 64 | N64 | 2000 | [N64-024](#n64-024) |
| Mario Golf | 马力欧高尔夫 64 | N64 | 1999 | [N64-025](#n64-025) |
| Mario Golf: Advance Tour | 马力欧高尔夫 Advance Tour | GBA | 2004 | [GBA-056](#gba-056) |
| Mario Tennis: Power Tour | 马力欧网球 Power Tour | GBA | 2005 | [GBA-057](#gba-057) |
| Mario Tennis | 马力欧网球（GBC） | GBC | 2000 | [GBC-017](#gbc-017) |

#### 派对

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mario Party 1 / 2 / 3 | 马力欧派对 1／2／3 | N64 | 1998–2000 | [N64-027](#n64-027) |

---

### 塞尔达传说

<a id="series-02"></a>

以迷宫、关键道具、探索与环境谜题构成冒险，地区版本和重制版常在操作与新增迷宫上有差异。它是任天堂动作冒险主线，不是传统数值驱动 RPG。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| The Legend of Zelda | 塞尔达传说 | NES | 1986 | [NES-004](#nes-004) |
| Zelda II: The Adventure of Link | 塞尔达传说 2：林克的冒险 | NES | 1987 | [NES-005](#nes-005) |
| The Legend of Zelda: Link’s Awakening | 塞尔达传说：织梦岛 | GB | 1993 | [GB-001](#gb-001) |
| The Legend of Zelda: Link’s Awakening DX | 塞尔达传说：织梦岛 DX | GBC | 1998 | [GBC-001](#gbc-001) |
| The Legend of Zelda: A Link to the Past | 塞尔达传说：众神的三角力量 | SNES | 1991 | [SNES-004](#snes-004) |
| The Legend of Zelda: Ocarina of Time | 塞尔达传说：时之笛 | N64 | 1998 | [N64-001](#n64-001) |
| The Legend of Zelda: Majora’s Mask | 塞尔达传说：魔吉拉的面具 | N64 | 2000 | [N64-002](#n64-002) |
| The Legend of Zelda: The Minish Cap | 塞尔达传说：缩小帽 | GBA | 2004 | [GBA-041](#gba-041) |
| The Legend of Zelda: Phantom Hourglass | 塞尔达传说：幻影沙漏 | NDS | 2007 | [NDS-014](#nds-014) |
| The Legend of Zelda: Spirit Tracks | 塞尔达传说：大地的汽笛 | NDS | 2009 | [NDS-015](#nds-015) |
| The Legend of Zelda: Oracle of Seasons / Oracle of Ages | 塞尔达传说：大地之章／时空之章 | GBC | 2001 | [GBC-015](#gbc-015) |

---

### 洛克人

<a id="series-03"></a>

元祖／世界、X、Zero、EXE、ZX 与流星分组。

#### 元祖与世界

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mega Man | 洛克人 | NES | 1987 | [NES-006](#nes-006) |
| Mega Man 2 | 洛克人 2 | NES | 1989 | [NES-007](#nes-007) |
| Mega Man 3 | 洛克人 3 | NES | 1990 | [NES-008](#nes-008) |
| Mega Man 4 | 洛克人 4 | NES | 1992 | [NES-009](#nes-009) |
| Mega Man 5 | 洛克人 5 | NES | 1992 | [NES-010](#nes-010) |
| Mega Man 6 | 洛克人 6 | NES | 1994 | [NES-011](#nes-011) |
| Mega Man: Dr. Wily’s Revenge | 洛克人世界：威利博士的反击 | GB | 1991 | [GB-007](#gb-007) |
| Mega Man II | 洛克人世界 II | GB | 1992 | [GB-008](#gb-008) |
| Mega Man III | 洛克人世界 III | GB | 1992 | [GB-009](#gb-009) |
| Mega Man IV | 洛克人世界 IV | GB | 1993 | [GB-010](#gb-010) |
| Mega Man V | 洛克人世界 V | GB | 1994 | [GB-011](#gb-011) |
| Mega Man: The Wily Wars | Mega Man: The Wily Wars | MD | 1994 | [MD-024](#md-024) |
| Mega Man 7 | 洛克人 7 | SNES | 1995 | [SNES-050](#snes-050) |

#### X

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mega Man Xtreme | 洛克人 X：电子任务 | GBC | 2000 | [GBC-014](#gbc-014) |
| Mega Man X | 洛克人 X | SNES | 1994 | [SNES-035](#snes-035) |
| Mega Man X2 | 洛克人 X2 | SNES | 1995 | [SNES-036](#snes-036) |
| Mega Man X3 | 洛克人 X3 | SNES | 1996 | [SNES-037](#snes-037) |
| Mega Man Xtreme 2 | 洛克人 X2：灵魂消除者 | GBC | 2001 | [GBC-016](#gbc-016) |

#### Zero

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mega Man Zero | 洛克人 Zero | GBA | 2002 | [GBA-019](#gba-019) |
| Mega Man Zero 2 | 洛克人 Zero 2 | GBA | 2003 | [GBA-020](#gba-020) |
| Mega Man Zero 3 | 洛克人 Zero 3 | GBA | 2004 | [GBA-021](#gba-021) |
| Mega Man Zero 4 | 洛克人 Zero 4 | GBA | 2005 | [GBA-022](#gba-022) |

#### EXE／网络对战

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mega Man Battle Network | 洛克人 EXE | GBA | 2001 | [GBA-023](#gba-023) |
| Mega Man Battle Network 2 | 洛克人 EXE 2 | GBA | 2002 | [GBA-024](#gba-024) |
| Mega Man Battle Network 3: Blue / White | 洛克人 EXE 3：蓝／白 | GBA | 2002 | [GBA-025](#gba-025) |

#### ZX 与流星

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mega Man ZX | 洛克人 ZX | NDS | 2006 | [NDS-045](#nds-045) |
| Mega Man ZX Advent | 洛克人 ZX Advent | NDS | 2007 | [NDS-046](#nds-046) |
| Mega Man Star Force: Pegasus / Leo / Dragon | 流星洛克人：天马／雄狮／天龙 | NDS | 2006 | [NDS-047](#nds-047) |

---

### 魂斗罗

<a id="series-04"></a>

以跑射、武器拾取和高密度敌人构成动作挑战，双人合作是早期作品的重要记忆。街机、FC、SFC 与 MD 各作关卡并非简单互移。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Contra | 魂斗罗 | NES | 1988 | [NES-012](#nes-012) |
| Super C | 超级魂斗罗 | NES | 1990 | [NES-013](#nes-013) |
| Contra: Hard Corps | 魂斗罗：铁血兵团 | MD | 1994 | [MD-020](#md-020) |
| Contra III: The Alien Wars | 魂斗罗精神：异形战争 | SNES | 1992 | [SNES-051](#snes-051) |
| Contra (Arcade) | 魂斗罗街机 | FBNEO | 1987 | [FBNEO-100](#fbneo-100) |
| Super Contra (Arcade) | 超级魂斗罗街机 | FBNEO | 1988 | [FBNEO-101](#fbneo-101) |

---

### 三国志与三国题材

<a id="series-05"></a>

光荣战略、Capcom《吞食天地》与 IGS《三国战纪》分栏，避免同题材混成同系列。

#### 光荣《三国志》

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Sangokushi | 三国志 | NES | 1988 | [NES-024](#nes-024) |
| Sangokushi II: Haou no Tairiku | 三国志 II：霸王的大陆 | NES | 1990 | [NES-026](#nes-026) |
| Romance of the Three Kingdoms II | 三国志 II | MD | 1992 | [MD-012](#md-012) |
| Romance of the Three Kingdoms III: Dragon of Destiny | 三国志 III | MD | 1993 | [MD-013](#md-013) |
| Romance of the Three Kingdoms II | 三国志 II | SNES | 1992 | [SNES-027](#snes-027) |
| Romance of the Three Kingdoms III: Dragon of Destiny | 三国志 III | SNES | 1992 | [SNES-028](#snes-028) |
| Romance of the Three Kingdoms IV: Wall of Fire | 三国志 IV | SNES | 1995 | [SNES-029](#snes-029) |
| Romance of the Three Kingdoms VII | 三国志 VII | PSP | 2000 | [PSP-018](#psp-018) |
| Romance of the Three Kingdoms V | 三国志 V | PS1 | 1995 | [PS1-014](#ps1-014) |
| Romance of the Three Kingdoms VI | 三国志 VI | PS1 | 1998 | [PS1-015](#ps1-015) |
| Romance of the Three Kingdoms VII | 三国志 VII | PS1 | 2000 | [PS1-016](#ps1-016) |

#### 吞食天地

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Tenchi wo Kurau / Destiny of an Emperor | 吞食天地 | NES | 1990 | [NES-065](#nes-065) |
| Tenchi wo Kurau II: Shokatsu Koumei Den | 吞食天地 II：诸葛孔明传 | NES | 1991 | [NES-066](#nes-066) |
| Warriors of Fate / Tenchi wo Kurau II | 吞食天地2赤壁之战 | FBNEO | 1992 | [FBNEO-003](#fbneo-003) |

#### 三国战纪

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Knights of Valour Plus | 三国战纪：正宗 Plus | FBNEO | 1999–2003 | [FBNEO-001](#fbneo-001) |
| Knights of Valour: Super Heroes | 三国战纪风云再起 | FBNEO | 1999–2003 | [FBNEO-002](#fbneo-002) |

---

### 最终幻想

<a id="series-06"></a>

正传、重制与战略版分组。FFT／FFTA 属于本专题“战略版”，与皇家骑士团没有系列隶属关系。

#### 正传与重制

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Final Fantasy | 最终幻想 | NES | 1987 | [NES-027](#nes-027) |
| Final Fantasy II | 最终幻想 II | NES | 1988 | [NES-028](#nes-028) |
| Final Fantasy III | 最终幻想 III | NES | 1990 | [NES-029](#nes-029) |
| Final Fantasy IV | 最终幻想 IV | SNES | 1991 | [SNES-007](#snes-007) |
| Final Fantasy V | 最终幻想 V | SNES | 1992 | [SNES-008](#snes-008) |
| Final Fantasy VI | 最终幻想 VI | SNES | 1994 | [SNES-009](#snes-009) |
| Final Fantasy IV Advance | 最终幻想 IV Advance | GBA | 2005 | [GBA-029](#gba-029) |
| Final Fantasy V Advance | 最终幻想 V Advance | GBA | 2006 | [GBA-030](#gba-030) |
| Final Fantasy VI Advance | 最终幻想 VI Advance | GBA | 2006 | [GBA-031](#gba-031) |
| Final Fantasy I & II: Dawn of Souls | 最终幻想 I・II：灵魂黎明 | GBA | 2004 | [GBA-068](#gba-068) |
| Final Fantasy III (Nintendo DS) | 最终幻想 III（NDS 重制版） | NDS | 2006 | [NDS-049](#nds-049) |
| Final Fantasy IV (Nintendo DS) | 最终幻想 IV（NDS 重制版） | NDS | 2007 | [NDS-050](#nds-050) |
| Final Fantasy Crystal Chronicles: Echoes of Time | 最终幻想水晶编年史：时之回声 | NDS | 2009 | [NDS-052](#nds-052) |
| Dissidia Final Fantasy | 最终幻想：纷争 | PSP | 2009 | [PSP-035](#psp-035) |
| Final Fantasy VII | 最终幻想 VII | PS1 | 1997 | [PS1-005](#ps1-005) |
| Final Fantasy VIII | 最终幻想 VIII | PS1 | 1999 | [PS1-006](#ps1-006) |
| Final Fantasy IX | 最终幻想 IX | PS1 | 2000 | [PS1-007](#ps1-007) |
| Final Fantasy I / II / IV | 最终幻想 I／II／IV（WS／WSC） | WS | 2000–2002 | [WS-011](#ws-011) |

#### 战略版

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Final Fantasy Tactics Advance | 最终幻想战略版 Advance | GBA | 2003 | [GBA-034](#gba-034) |
| Final Fantasy Tactics A2: Grimoire of the Rift | 最终幻想战略版 A2：封穴的魔法书 | NDS | 2007 | [NDS-068](#nds-068) |
| Final Fantasy Tactics: The War of the Lions | 最终幻想战略版：狮子战争 | PSP | 2007 | [PSP-017](#psp-017) |
| Final Fantasy Tactics | 最终幻想战略版 | PS1 | 1997 | [PS1-008](#ps1-008) |

#### VII 衍生

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Crisis Core: Final Fantasy VII | 核心危机：最终幻想 VII | PSP | 2007 | [PSP-010](#psp-010) |

---

### 勇者斗恶龙

<a id="series-07"></a>

坚持回合制与旅行冒险的基本框架，通过队伍、转职、怪物或章节结构变化主题。NDS 的 IV／V／VI 是重制版，GBA 没有这些序号移植。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Dragon Quest | 勇者斗恶龙 | NES | 1986 | [NES-030](#nes-030) |
| Dragon Quest II: Luminaries of the Legendary Line | 勇者斗恶龙 II：恶灵的众神 | NES | 1987 | [NES-031](#nes-031) |
| Dragon Quest III: The Seeds of Salvation | 勇者斗恶龙 III：传说的开始 | NES | 1988 | [NES-032](#nes-032) |
| Dragon Quest IV: Chapters of the Chosen | 勇者斗恶龙 IV：被引导的人们 | NES | 1990 | [NES-033](#nes-033) |
| Dragon Warrior Monsters | 勇者斗恶龙怪兽篇 | GBC | 2000 | [GBC-006](#gbc-006) |
| Dragon Warrior Monsters 2: Cobi’s Journey / Tara’s Adventure | 勇者斗恶龙怪兽篇 2 | GBC | 2001 | [GBC-007](#gbc-007) |
| Dragon Quest V: Hand of the Heavenly Bride | 勇者斗恶龙 V：天空的新娘 | SNES | 1992 | [SNES-010](#snes-010) |
| Dragon Quest VI: Realms of Revelation | 勇者斗恶龙 VI：幻之大地 | SNES | 1995 | [SNES-011](#snes-011) |
| Dragon Quest IV: Chapters of the Chosen | 勇者斗恶龙 IV：被引导的人们 | NDS | 1990 | [NDS-019](#nds-019) |
| Dragon Quest V: Hand of the Heavenly Bride | 勇者斗恶龙 V：天空的新娘 | NDS | 1992 | [NDS-020](#nds-020) |
| Dragon Quest VI: Realms of Revelation | 勇者斗恶龙 VI：幻之大地 | NDS | 1995 | [NDS-021](#nds-021) |
| Dragon Quest IX: Sentinels of the Starry Skies | 勇者斗恶龙 IX：星空的守护者 | NDS | 2010 | [NDS-022](#nds-022) |
| Dragon Quest Monsters: Joker | 勇者斗恶龙怪兽篇 Joker | NDS | 2006 | [NDS-053](#nds-053) |
| Dragon Quest Monsters: Joker 2 | 勇者斗恶龙怪兽篇 Joker 2 | NDS | 2010 | [NDS-054](#nds-054) |
| Dragon Quest VII: Fragments of the Forgotten Past | 勇者斗恶龙 VII：伊甸的战士们 | PS1 | 2000 | [PS1-079](#ps1-079) |
| Dragon Quest III: The Seeds of Salvation | 勇者斗恶龙 III：传说的开始（SFC 重制版） | SNES | 1996 | [SNES-104](#snes-104) |

---

### 双截龙

<a id="series-08"></a>

李氏兄弟以拳脚、投技和武器清理街头敌人，是清版动作早期代表。FC 初代与街机版在合作和系统上差异明显，二代通常更适合直接入门。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Double Dragon | 双截龙 | NES | 1988 | [NES-034](#nes-034) |
| Double Dragon II: The Revenge | 双截龙 II：复仇 | NES | 1990 | [NES-035](#nes-035) |
| Double Dragon III: The Sacred Stones | 双截龙 III：圣石 | NES | 1991 | [NES-036](#nes-036) |
| Double Dragon II | 双截龙 II（GB） | GB | 1991 | [GB-020](#gb-020) |
| Double Dragon 1 / 2 / 3 (Arcade) | 双截龙1/2/3 | FBNEO | 1987–1990 | [FBNEO-117](#fbneo-117) |

---

### 宇宙巡航机与兵蜂

<a id="series-09"></a>

以卷轴射击、武器升级与关卡记忆为核心，Parodius 和 TwinBee 则以幽默、明亮风格另开支线。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Life Force / Salamander | 沙罗曼蛇 | NES | 1988 | [NES-040](#nes-040) |
| Gradius | 宇宙巡航机 | NES | 1986 | [NES-041](#nes-041) |
| TwinBee | 兵蜂 | NES | 1986 | [NES-073](#nes-073) |
| Gradius III | 宇宙巡航机 III | SNES | 1990 | [SNES-077](#snes-077) |
| Parodius Da! | 疯狂大射击 | SNES | 1992 | [SNES-079](#snes-079) |
| Pop’n TwinBee | 出击！兵蜂 | SNES | 1993 | [SNES-080](#snes-080) |
| Life Force | Life Force | FBNEO | 1986 | [FBNEO-108](#fbneo-108) |
| Gradius / Gradius II / Gradius III / Gradius Gaiden | 宇宙巡航机 I／II／III／外传 | FBNEO | 1985 | [FBNEO-109](#fbneo-109) |
| Parodius Da! / Sexy Parodius / Gokujou Parodius! | 疯狂大射击系列 | FBNEO | 1990 | [FBNEO-110](#fbneo-110) |
| TwinBee / Detana!! TwinBee / Pop’n TwinBee | 兵蜂系列 | FBNEO | 1985 | [FBNEO-111](#fbneo-111) |

---

### 炸弹人

<a id="series-10"></a>

围绕《炸弹人》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Bomberman | 炸弹人 | NES | 1985 | [NES-042](#nes-042) |
| Bomberman II | 炸弹人 II | NES | 1991 | [NES-043](#nes-043) |
| Bomberman GB | 炸弹人 GB | GB | 1996 | [GB-028](#gb-028) |
| Bomberman 64 | 炸弹人 64 | N64 | 1997 | [N64-026](#n64-026) |
| Bomberman '93 / '94 | 炸弹人 ’93／’94 | PCE | 1992 | [PCE-014](#pce-014) |

---

### 恶魔城

<a id="series-11"></a>

从早期线性鞭击闯关到后期地图探索与 RPG 成长，各作分支明显。需特别区分 PCE《血之轮回》、SFC《恶魔城 XX》与 PSP 重制合集。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Castlevania | 恶魔城 | NES | 1987 | [NES-044](#nes-044) |
| Castlevania II: Simon’s Quest | 恶魔城 II：西蒙的冒险 | NES | 1988 | [NES-045](#nes-045) |
| Castlevania III: Dracula’s Curse | 恶魔城 III：德古拉的诅咒 | NES | 1990 | [NES-046](#nes-046) |
| Castlevania: The Adventure | 恶魔城：德古拉传说 | GB | 1990 | [GB-012](#gb-012) |
| Castlevania II: Belmont’s Revenge | 恶魔城：德古拉传说 II | GB | 1991 | [GB-013](#gb-013) |
| Castlevania Legends | 恶魔城：漆黑前奏曲 | GB | 1997 | [GB-014](#gb-014) |
| Kid Dracula / Akumajou Special: Boku Dracula-kun | 恶魔城特别篇：我是德古拉 | GB | 1993 | [GB-015](#gb-015) |
| Castlevania: Bloodlines | 恶魔城：血族 | MD | 1994 | [MD-047](#md-047) |
| Castlevania: Dracula X | 恶魔城 XX | SNES | 1995 | [SNES-034](#snes-034) |
| Super Castlevania IV | 超级恶魔城 IV | SNES | 1991 | [SNES-098](#snes-098) |
| Akumajou Dracula X: Chi no Rondo / Castlevania: Rondo of Blood | 恶魔城 X：血之轮回 | PCE | 1993 | [PCE-001](#pce-001) |
| Castlevania: Aria of Sorrow | 恶魔城：晓月圆舞曲 | GBA | 2003 | [GBA-008](#gba-008) |
| Castlevania: Harmony of Dissonance | 恶魔城：白夜协奏曲 | GBA | 2002 | [GBA-009](#gba-009) |
| Castlevania: Circle of the Moon | 恶魔城：月之轮回 | GBA | 2001 | [GBA-010](#gba-010) |
| Castlevania: Dawn of Sorrow | 恶魔城：苍月十字架 | NDS | 2005 | [NDS-016](#nds-016) |
| Castlevania: Portrait of Ruin | 恶魔城：迷宫回廊 | NDS | 2006 | [NDS-017](#nds-017) |
| Castlevania: Order of Ecclesia | 恶魔城：被夺走的刻印 | NDS | 2008 | [NDS-018](#nds-018) |
| Castlevania: The Dracula X Chronicles | 恶魔城 X 历代记 | PSP | 2007 | [PSP-041](#psp-041) |
| Castlevania: Symphony of the Night | 恶魔城 X：月下夜想曲 | PS1 | 1997 | [PS1-004](#ps1-004) |
| Castlevania Chronicles | 恶魔城年代记 | PS1 | 1999 | [PS1-061](#ps1-061) |

---

### 热血系列

<a id="series-12"></a>

围绕《热血硬派国夫君》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Nekketsu Kouha Kunio-kun | 热血硬派国夫君 | NES | 1987 | [NES-047](#nes-047) |
| Downtown Nekketsu Koushinkyoku: Soreyuke Daiundoukai | 热血行进曲：前进大运动会 | NES | 1990 | [NES-048](#nes-048) |
| Nekketsu Kakutou Densetsu | 热血格斗传说 | NES | 1992 | [NES-049](#nes-049) |
| River City Ransom / Downtown Nekketsu Monogatari | 热血物语 | NES | 1990 | [NES-050](#nes-050) |
| Nintendo World Cup / Nekketsu Koukou Dodgeball-bu Soccer-hen | 热血足球 | NES | 1990 | [NES-051](#nes-051) |
| Nekketsu! Street Basket: Ganbare Dunk Heroes | 热血街头篮球 | NES | 1993 | [NES-052](#nes-052) |
| Super Dodge Ball / Nekketsu Koukou Dodgeball-bu | 热血躲避球 | NES | 1989 | [NES-053](#nes-053) |
| Nekketsu Kouha Kunio-kun / Renegade (Arcade) | 热血系列街机版 | FBNEO | 1986 | [FBNEO-118](#fbneo-118) |

---

### 忍者神龟

<a id="series-13"></a>

围绕《忍者神龟》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Teenage Mutant Ninja Turtles | 忍者神龟 | NES | 1989 | [NES-054](#nes-054) |
| Teenage Mutant Ninja Turtles II: The Arcade Game | 忍者神龟 II：街机移植版 | NES | 1990 | [NES-055](#nes-055) |
| Teenage Mutant Ninja Turtles III: The Manhattan Project | 忍者神龟 III：曼哈顿计划 | NES | 1992 | [NES-056](#nes-056) |
| Teenage Mutant Ninja Turtles: Fall of the Foot Clan | 忍者神龟：脚帮的覆灭 | GB | 1990 | [GB-021](#gb-021) |
| Teenage Mutant Ninja Turtles: Turtles in Time | 忍者神龟：时空之战 | FBNEO | 1991 | [FBNEO-102](#fbneo-102) |

---

### 重装机兵

<a id="series-14"></a>

以废土赏金、战车改装和较高流程自由度为特征，人与战车有独立战斗逻辑。它是独立的 Metal Max／Metal Saga 系列，与宝可梦无关。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Metal Max | 重装机兵 | NES | 1991 | [NES-063](#nes-063) |
| Metal Max 2 | 重装机兵 2 | SNES | 1993 | [SNES-099](#snes-099) |
| Metal Max 3 | 重装机兵 3 | NDS | 2010 | [NDS-026](#nds-026) |
| Metal Saga: Hagane no Kisetsu | 重装机兵：钢之季节 | NDS | 2006 | [NDS-027](#nds-027) |

---

### 火焰之纹章

<a id="series-15"></a>

网格战棋结合武器克制、角色养成和永久阵亡，重制版通常会调整难度与便利功能。不同大陆的故事不要按序号强行串成一条时间线。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Fire Emblem Gaiden | 火焰之纹章外传 | NES | 1992 | [NES-064](#nes-064) |
| Fire Emblem: Mystery of the Emblem | 火焰之纹章：纹章之谜 | SNES | 1994 | [SNES-012](#snes-012) |
| Fire Emblem: Genealogy of the Holy War | 火焰之纹章：圣战之系谱 | SNES | 1996 | [SNES-013](#snes-013) |
| Fire Emblem: Thracia 776 | 火焰之纹章：多拉基亚 776 | SNES | 1999 | [SNES-014](#snes-014) |
| Fire Emblem: The Binding Blade | 火焰之纹章：封印之剑 | GBA | 2002 | [GBA-005](#gba-005) |
| Fire Emblem: The Blazing Blade | 火焰之纹章：烈火之剑 | GBA | 2003 | [GBA-006](#gba-006) |
| Fire Emblem: The Sacred Stones | 火焰之纹章：圣魔之光石 | GBA | 2005 | [GBA-007](#gba-007) |
| Fire Emblem: Shadow Dragon | 火焰之纹章：新·暗黑龙与光之剑 | NDS | 2008 | [NDS-024](#nds-024) |
| Fire Emblem: New Mystery of the Emblem | 火焰之纹章：新·纹章之谜 | NDS | 2010 | [NDS-025](#nds-025) |
| Fire Emblem: Shadow Dragon and the Blade of Light | 火焰之纹章：暗黑龙与光之剑 | NES | 1990 | [NES-095](#nes-095) |

---

### 龙珠

<a id="series-16"></a>

围绕《龙珠：大魔王复活》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Dragon Ball: Daimaou Fukkatsu | 龙珠：大魔王复活 | NES | 1988 | [NES-078](#nes-078) |
| Dragon Ball Z: Goku Hishouden / Goku Gekitouden | 龙珠 Z：悟空飞翔传／激斗传 | GB | 1994–1995 | [GB-022](#gb-022) |
| Dragon Ball Z: Supersonic Warriors | 龙珠 Z：舞空斗剧 | GBA | 2004 | [GBA-052](#gba-052) |
| Dragon Ball: Advanced Adventure | 龙珠大冒险 | GBA | 2004 | [GBA-070](#gba-070) |

---

### 俄罗斯方块

<a id="series-17"></a>

围绕《俄罗斯方块》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Tetris | 俄罗斯方块 | NES | 1988 | [NES-088](#nes-088) |
| Tetris | 俄罗斯方块 | GB | 1989 | [GB-025](#gb-025) |

---

### 密特罗德

<a id="series-18"></a>

以非线性地图、能力锁与科幻孤独感推动探索，掌机作品也在线性叙事和自由探索之间做不同取舍。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Metroid | 密特罗德 | NES | 1986 | [NES-089](#nes-089) |
| Metroid II: Return of Samus | 密特罗德 II：萨姆斯归来 | GB | 1991 | [GB-006](#gb-006) |
| Super Metroid | 超级密特罗德 | SNES | 1994 | [SNES-005](#snes-005) |
| Metroid Fusion | 密特罗德：融合 | GBA | 2002 | [GBA-027](#gba-027) |
| Metroid: Zero Mission | 密特罗德：零点任务 | GBA | 2004 | [GBA-028](#gba-028) |

---

### 合金装备

<a id="series-19"></a>

以视线、声音、雷达与隐蔽路线完成潜入，叙事大量采用电影和通信演出。MSX 起源、GBC 独立故事与 Solid 主线不能混成同一版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Metal Gear | 合金装备 | NES | 1987 | [NES-093](#nes-093) |
| Metal Gear Solid: Ghost Babel | 合金装备：幽灵通天塔 | GBC | 2000 | [GBC-005](#gbc-005) |
| Metal Gear Solid | 合金装备 | PS1 | 1998 | [PS1-009](#ps1-009) |

---

### 星之卡比

<a id="series-20"></a>

以吞噬复制、轻量平台动作和多能力解谜为主，部分作品改用车线、触控或非线性地图实验。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Kirby’s Adventure | 星之卡比：梦之泉物语 | NES | 1993 | [NES-094](#nes-094) |
| Kirby Super Star | 星之卡比：超级豪华版 | SNES | 1996 | [SNES-065](#snes-065) |
| Kirby’s Dream Land 3 | 星之卡比 3 | SNES | 1997 | [SNES-066](#snes-066) |
| Kirby 64: The Crystal Shards | 星之卡比 64：水晶碎片 | N64 | 2000 | [N64-016](#n64-016) |
| Kirby & the Amazing Mirror | 星之卡比：镜之大迷宫 | GBA | 2004 | [GBA-026](#gba-026) |
| Kirby: Nightmare in Dream Land | 星之卡比：梦之泉豪华版 | GBA | 2002 | [GBA-071](#gba-071) |
| Kirby: Canvas Curse | 触摸！卡比 | NDS | 2005 | [NDS-070](#nds-070) |
| Kirby: Squeak Squad | 星之卡比：参上！怪盗洛切团 | NDS | 2006 | [NDS-071](#nds-071) |
| Kirby’s Dream Land | 星之卡比 | GB | 1992 | [GB-030](#gb-030) |
| Kirby’s Dream Land 2 | 星之卡比 2 | GB | 1995 | [GB-031](#gb-031) |

---

### 宝可梦

<a id="series-21"></a>

按正统 RPG、不可思议迷宫、护林员及家用机衍生拆分；Metal Max／重装机兵不属于本专题。

#### 正统角色扮演

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Pokémon Red / Green / Blue / Yellow | 宝可梦：红／绿／蓝／皮卡丘 | GB | 1996–1998 | [GB-005](#gb-005) |
| Pokémon Gold / Silver / Crystal | 宝可梦：金／银／水晶 | GBC | 1999–2000 | [GBC-003](#gbc-003) |
| Pokémon FireRed / LeafGreen | 宝可梦：火红／叶绿 | GBA | 2004 | [GBA-001](#gba-001) |
| Pokémon Emerald | 宝可梦：绿宝石 | GBA | 2004 | [GBA-002](#gba-002) |
| Pokémon Ruby / Sapphire | 宝可梦：红宝石／蓝宝石 | GBA | 2002 | [GBA-061](#gba-061) |
| Pokémon HeartGold / SoulSilver | 宝可梦：心金／魂银 | NDS | 2009 | [NDS-001](#nds-001) |
| Pokémon Platinum | 宝可梦：白金 | NDS | 2008 | [NDS-002](#nds-002) |
| Pokémon Black / White | 宝可梦：黑／白 | NDS | 2010 | [NDS-003](#nds-003) |
| Pokémon Black 2 / White 2 | 宝可梦：黑 2／白 2 | NDS | 2012 | [NDS-004](#nds-004) |

#### 家用机与益智衍生

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Pokémon Trading Card Game | 宝可梦集换式卡牌 GB | GBC | 2000 | [GBC-008](#gbc-008) |
| Pokémon Stadium | 宝可梦竞技场 | N64 | 1998 | [N64-017](#n64-017) |
| Pokémon Stadium 2 | 宝可梦竞技场 2 | N64 | 2000 | [N64-018](#n64-018) |
| Pokémon Snap | 宝可梦随乐拍 | N64 | 1999 | [N64-019](#n64-019) |
| Pokémon Puzzle League | 宝可梦方块联盟 | N64 | 2000 | [N64-020](#n64-020) |

#### 不可思议迷宫

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Pokémon Mystery Dungeon: Red Rescue Team | 宝可梦不可思议迷宫：赤救助队 | GBA | 2005 | [GBA-062](#gba-062) |
| Pokémon Mystery Dungeon: Blue Rescue Team | 宝可梦不可思议迷宫：青救助队 | NDS | 2005 | [NDS-055](#nds-055) |
| Pokémon Mystery Dungeon: Explorers of Time | 宝可梦不可思议迷宫：时之探险队 | NDS | 2007 | [NDS-056](#nds-056) |
| Pokémon Mystery Dungeon: Explorers of Darkness | 宝可梦不可思议迷宫：暗之探险队 | NDS | 2007 | [NDS-057](#nds-057) |
| Pokémon Mystery Dungeon: Explorers of Sky | 宝可梦不可思议迷宫：空之探险队 | NDS | 2009 | [NDS-058](#nds-058) |

#### 护林员

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Pokémon Ranger | 宝可梦护林员 | NDS | 2006 | [NDS-059](#nds-059) |

---

### 沙加

<a id="series-22"></a>

强调自由剧本、闪悟或非常规成长，不采用传统单线等级结构；GB、SFC 与 NDS 重制需按版本区分。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| The Final Fantasy Legend / Makai Toushi SaGa | 魔界塔士 SaGa | GB | 1989 | [GB-016](#gb-016) |
| Final Fantasy Legend II / SaGa 2: Hihou Densetsu | SaGa 2：秘宝传说 | GB | 1991 | [GB-017](#gb-017) |
| Final Fantasy Legend III / SaGa 3: Jikuu no Hasha | SaGa 3：时空的霸者 | GB | 1993 | [GB-018](#gb-018) |
| Romancing SaGa | 浪漫沙加 | SNES | 1992 | [SNES-052](#snes-052) |
| Romancing SaGa 2 | 浪漫沙加 2 | SNES | 1993 | [SNES-053](#snes-053) |
| Romancing SaGa 3 | 浪漫沙加 3 | SNES | 1995 | [SNES-054](#snes-054) |
| SaGa 2: Hihou Densetsu – Goddess of Destiny | 沙加 2：秘宝传说－命运女神 | NDS | 2009 | [NDS-051](#nds-051) |
| SaGa Frontier | 浪漫沙加：开拓者 | PS1 | 1997 | [PS1-084](#ps1-084) |
| SaGa Frontier 2 | 浪漫沙加：开拓者 2 | PS1 | 1999 | [PS1-085](#ps1-085) |

---

### 牧场物语与符文工房

<a id="series-23"></a>

种植、养殖、节庆和人际养成构成慢节奏经营，符文工房再加入迷宫与动作战斗。早期英文 Harvest Moon 与后来品牌变更不能倒套。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Harvest Moon GB | 牧场物语 GB | GB | 1997 | [GB-024](#gb-024) |
| Harvest Moon | 牧场物语 | SNES | 1997 | [SNES-069](#snes-069) |
| Harvest Moon: Friends of Mineral Town | 牧场物语：矿石镇的伙伴们 | GBA | 2003 | [GBA-042](#gba-042) |
| Rune Factory: A Fantasy Harvest Moon | 符文工房：新牧场物语 | NDS | 2006 | [NDS-040](#nds-040) |
| Rune Factory 2: A Fantasy Harvest Moon | 符文工房 2 | NDS | 2007 | [NDS-041](#nds-041) |
| Harvest Moon: Grand Bazaar | 牧场物语：风之集市 | NDS | 2008 | [NDS-042](#nds-042) |

---

### 星之海洋

<a id="series-24"></a>

由 tri-Ace 打造，以即时战斗、技能与科幻文明冲突为特色，早期发行主体是 Enix。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Star Ocean: Blue Sphere | 星之海洋：蔚蓝星球 | GBC | 2001 | [GBC-013](#gbc-013) |
| Star Ocean | 星之海洋 | SNES | 1996 | [SNES-055](#snes-055) |
| Star Ocean: The Second Story | 星之海洋：第二个故事 | PS1 | 1998 | [PS1-037](#ps1-037) |

---

### 索尼克

<a id="series-25"></a>

强调速度、惯性和立体分支路线，MD 2D 与 DC 3D 作品的镜头及关卡逻辑差异明显。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Sonic the Hedgehog | 刺猬索尼克 | MD | 1991 | [MD-001](#md-001) |
| Sonic the Hedgehog 2 | 刺猬索尼克 2 | MD | 1992 | [MD-002](#md-002) |
| Sonic the Hedgehog 3 & Knuckles | 索尼克 3 与纳克鲁斯 | MD | 1994 | [MD-003](#md-003) |
| Sonic Advance | 索尼克 Advance | GBA | 2001 | [GBA-046](#gba-046) |
| Sonic Advance 2 | 索尼克 Advance 2 | GBA | 2002 | [GBA-047](#gba-047) |
| Sonic Advance 3 | 索尼克 Advance 3 | GBA | 2004 | [GBA-048](#gba-048) |
| Sonic Adventure | 索尼克大冒险 | DC | 1998 | [DC-010](#dc-010) |
| Sonic Adventure 2 | 索尼克大冒险 2 | DC | 2001 | [DC-011](#dc-011) |
| Sonic the Hedgehog | 刺猬索尼克（GG） | GG | 1991 | [GG-001](#gg-001) |
| Sonic the Hedgehog 2 | 刺猬索尼克 2（GG） | GG | 1992 | [GG-002](#gg-002) |
| Sonic Chaos | 索尼克与塔尔斯：混沌 | GG | 1993 | [GG-003](#gg-003) |
| Sonic the Hedgehog: Triple Trouble | 索尼克与塔尔斯 2：三重麻烦 | GG | 1994 | [GG-004](#gg-004) |

---

### 怒之铁拳

<a id="series-26"></a>

清版动作结合投技、保险与鲜明角色差异，配乐和都市氛围是系列标志。“格斗三人组”只是初代中文俗称，不应重复收藏。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Streets of Rage / Bare Knuckle | 怒之铁拳 | MD | 1991 | [MD-004](#md-004) |
| Streets of Rage 2 / Bare Knuckle II | 怒之铁拳 2 | MD | 1992 | [MD-005](#md-005) |
| Streets of Rage 3 / Bare Knuckle III | 怒之铁拳 3 | MD | 1994 | [MD-006](#md-006) |

---

### 战斧

<a id="series-27"></a>

以骑乘、魔法瓶与多人合作构成奇幻清版动作，MD 的 II／III 与街机《死亡蝰蛇的复仇》不是同一编号体系。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Golden Axe | 战斧 | MD | 1989 | [MD-008](#md-008) |
| Golden Axe II | 战斧 II | MD | 1993 | [MD-009](#md-009) |
| Golden Axe III | 战斧 III | MD | 1993 | [MD-010](#md-010) |
| Golden Axe (Arcade) / Golden Axe: The Revenge of Death Adder | 战斧1/2/3 | FBNEO | 1989 | [FBNEO-116](#fbneo-116) |
| Golden Axe: The Revenge of Death Adder | 战斧：死亡蝰蛇的复仇 | FBNEO | 1992 | [FBNEO-126](#fbneo-126) |

---

### 信长之野望

<a id="series-28"></a>

以战国大名的内政、外交和军事扩张构成回合制历史模拟，各代在武将扮演与全国策略间改变重心。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Nobunaga’s Ambition: Zenkokuban | 信长之野望：全国版 | MD | 1986 | [MD-014](#md-014) |
| Nobunaga’s Ambition: Zenkokuban | 信长之野望：全国版 | SNES | 1986 | [SNES-030](#snes-030) |
| Nobunaga’s Ambition: Bushou Fuuunroku | 信长之野望：武将风云录 | SNES | 1990 | [SNES-031](#snes-031) |
| Nobunaga’s Ambition: Haouden | 信长之野望：霸王传 | SNES | 1992 | [SNES-032](#snes-032) |
| Nobunaga’s Ambition: Tenshouki | 信长之野望：天翔记 | SNES | 1993 | [SNES-033](#snes-033) |
| Nobunaga’s Ambition: Shouseiroku | 信长之野望：将星录 | PS1 | 1997 | [PS1-017](#ps1-017) |
| Nobunaga’s Ambition: Reppuuden | 信长之野望：烈风传 | PS1 | 1998 | [PS1-018](#ps1-018) |

---

### 光明与梦幻模拟战

<a id="series-29"></a>

光明与 Langrisser 拆为两个子系列；Saturn《光明力量 III》不属于本机清单。

#### 梦幻模拟战

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Langrisser | 梦幻模拟战 | MD | 1991 | [MD-015](#md-015) |
| Langrisser II / Der Langrisser | 梦幻模拟战 II | MD | 1994 | [MD-016](#md-016) |
| Langrisser | 梦幻模拟战 | SNES | 1991 | [SNES-016](#snes-016) |
| Langrisser II / Der Langrisser | 梦幻模拟战 II | SNES | 1994–1995 | [SNES-017](#snes-017) |

#### 光明系列

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Shining Force | 光明力量 | MD | 1992 | [MD-044](#md-044) |
| Shining Force II: Ancient Sealing | 光明力量 II：远古封印 | MD | 1993 | [MD-045](#md-045) |
| Shining Soul | 光明之魂 | GBA | 2003 | [GBA-049](#gba-049) |
| Shining Soul II | 光明之魂 II | GBA | 2003 | [GBA-050](#gba-050) |
| Shining Force Gaiden | 光明力量外传 | GG | 1992 | [GG-008](#gg-008) |
| Shining Force: The Sword of Hajya | 光明力量外传 II：邪神之剑 | GG | 1993 | [GG-009](#gg-009) |
| Shining Force Gaiden: Final Conflict | 光明力量外传：最终冲突 | GG | 1995 | [GG-010](#gg-010) |

---

### 大战略与装甲将军

<a id="series-30"></a>

围绕《大战略：德意志电击战》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Advanced Daisenryaku | 大战略：德意志电击战 | MD | 1991 | [MD-017](#md-017) |
| Daisenryaku: Master Combat | 大战略：玩家精神 | PS1 | 1998 | [PS1-022](#ps1-022) |
| Panzer General | Panzer General | PS1 | 1996 | [PS1-027](#ps1-027) |
| Allied General | Allied General | PS1 | 1997 | [PS1-028](#ps1-028) |

---

### 街头霸王

<a id="series-31"></a>

以拳脚判定、必杀技、对空和资源管理构成格斗基础，II、Alpha、III 的系统与人物阵容各不相同。街机原版和家用移植需分开识别。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Street Fighter II': Special Champion Edition | 街头霸王 II：冠军加强版 | MD | 1993 | [MD-025](#md-025) |
| Street Fighter II Turbo: Hyper Fighting | 街头霸王 II Turbo | SNES | 1993 | [SNES-038](#snes-038) |
| Super Street Fighter II: The New Challengers | 超级街头霸王 II | SNES | 1994 | [SNES-039](#snes-039) |
| Street Fighter Alpha 2 | 少年街霸 Alpha 2 | SNES | 1996 | [SNES-070](#snes-070) |
| Street Fighter II: The World Warrior | 街头霸王2 | FBNEO | 1991 | [FBNEO-058](#fbneo-058) |
| Street Fighter II: Hyper Fighting | 街头霸王 II：Hyper Fighting | FBNEO | 1992 | [FBNEO-059](#fbneo-059) |
| Super Street Fighter II Turbo | 超级街头霸王 II Turbo | FBNEO | 1994 | [FBNEO-060](#fbneo-060) |
| Street Fighter Alpha: Warriors’ Dreams | 少年街霸 Alpha | FBNEO | 1995 | [FBNEO-061](#fbneo-061) |
| Street Fighter Alpha 2 | 少年街霸 Alpha 2 | FBNEO | 1996 | [FBNEO-062](#fbneo-062) |
| Street Fighter Alpha 3 | 少年街霸 Alpha 3 | FBNEO | 1998 | [FBNEO-063](#fbneo-063) |
| Street Fighter III: New Generation | 街头霸王 III：新世代 | FBNEO | 1997 | [FBNEO-064](#fbneo-064) |
| Street Fighter III: 2nd Impact | 街头霸王 III：二度冲击 | FBNEO | 1997 | [FBNEO-065](#fbneo-065) |
| Street Fighter III: 3rd Strike | 街头霸王 III：三度冲击 | FBNEO | 2000 | [FBNEO-066](#fbneo-066) |
| X-Men vs. Street Fighter | X 战警对街头霸王 | FBNEO | 1996 | [FBNEO-069](#fbneo-069) |
| Street Fighter II: Champion Edition | 街头霸王 II：冠军版 | FBNEO | 1992 | [FBNEO-129](#fbneo-129) |
| Street Fighter III: Double Impact | 街头霸王 III：双重冲击（New Generation＋2nd Impact） | DC | 1999 | [DC-005](#dc-005) |
| Street Fighter III: 3rd Strike | 街头霸王 III：三度冲击 | DC | 2000 | [DC-034](#dc-034) |
| Street Fighter Alpha 3 | 少年街霸 3 | PS1 | 1998 | [PS1-082](#ps1-082) |

---

### 梦幻之星

<a id="series-32"></a>

早期以科幻与奇幻混合的 JRPG 世界为特色，Online 则转向联网动作与刷装，二者不是同一玩法延续。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Phantasy Star II | 梦幻之星 II | MD | 1989 | [MD-032](#md-032) |
| Phantasy Star IV: The End of the Millennium | 梦幻之星 IV：千年纪的终结 | MD | 1993 | [MD-033](#md-033) |
| Phantasy Star Online | 梦幻之星在线 | DC | 2000 | [DC-022](#dc-022) |

---

### 饿狼与龙虎之拳

<a id="series-33"></a>

SNK 早期格斗分别以线移动、气力与角色故事建立特色，也共同构成拳皇的角色基础。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Fatal Fury 2 | 饿狼传说 2 | MD | 1993 | [MD-042](#md-042) |
| Fatal Fury: King of Fighters | 饿狼传说1 | FBNEO | 1991 | [FBNEO-043](#fbneo-043) |
| Fatal Fury 2 | 饿狼传说2 | FBNEO | 1992 | [FBNEO-044](#fbneo-044) |
| Fatal Fury 3: Road to the Final Victory | 饿狼传说3 | FBNEO | 1995 | [FBNEO-045](#fbneo-045) |
| Real Bout Fatal Fury | 饿狼传说 Real Bout | FBNEO | 1995 | [FBNEO-046](#fbneo-046) |
| Real Bout Fatal Fury Special | 饿狼传说 Real Bout Special | FBNEO | 1997 | [FBNEO-047](#fbneo-047) |
| Art of Fighting | 龙虎之拳1 | FBNEO | 1992 | [FBNEO-048](#fbneo-048) |
| Art of Fighting 2 | 龙虎之拳2 | FBNEO | 1994 | [FBNEO-049](#fbneo-049) |

---

### 侍魂与月华剑士

<a id="series-34"></a>

刀剑格斗强调距离、重击与读招，侍魂偏一击威慑，月华剑士更强调连段与剑质选择。两个系列共享厂商与时代背景，但不是外传关系。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Samurai Shodown | 侍魂 | MD | 1994 | [MD-043](#md-043) |
| Samurai Shodown II | 真侍魂：霸王丸地狱变 | FBNEO | 1993 | [FBNEO-036](#fbneo-036) |
| Samurai Shodown | 侍魂1 | FBNEO | 1993 | [FBNEO-037](#fbneo-037) |
| Samurai Shodown III: Blades of Blood | 侍魂3 | FBNEO | 1995 | [FBNEO-038](#fbneo-038) |
| Samurai Shodown IV: Amakusa’s Revenge | 侍魂4 | FBNEO | 1996 | [FBNEO-039](#fbneo-039) |
| Samurai Shodown V | 侍魂零 | FBNEO | 2003 | [FBNEO-040](#fbneo-040) |
| The Last Blade | 月华剑士1 | FBNEO | 1997 | [FBNEO-041](#fbneo-041) |
| The Last Blade 2 | 月华剑士2 | FBNEO | 1998 | [FBNEO-042](#fbneo-042) |

---

### 雷电与R-Type

<a id="series-35"></a>

雷电偏重武器颜色与双人快节奏，R-Type 偏重蓄力、Force 装置与严密关卡记忆，两者均有 MD 正式移植。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Raiden Trad | 雷电传统版 | MD | 1991 | [MD-050](#md-050) |
| R-Type | 异形战机 | MD | 1991 | [MD-051](#md-051) |
| R-Type III: The Third Lightning | 异形战机 III | SNES | 1993 | [SNES-078](#snes-078) |
| Raiden | Raiden | PCE | 1991 | [PCE-007](#pce-007) |
| R-Type | R-Type | PCE | 1989 | [PCE-008](#pce-008) |
| Raiden | 雷电1 | FBNEO | 1990 | [FBNEO-095](#fbneo-095) |
| Raiden II | 雷电2 | FBNEO | 1993 | [FBNEO-096](#fbneo-096) |
| R-Type | R-Type | FBNEO | 1987 | [FBNEO-097](#fbneo-097) |
| R-Type Leo | R-Type Leo | FBNEO | 1992 | [FBNEO-098](#fbneo-098) |

---

### 神奇男孩

<a id="series-36"></a>

围绕《神奇男孩：怪物世界》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Wonder Boy in Monster World | 神奇男孩：怪物世界 | MD | 1991 | [MD-053](#md-053) |
| Wonder Boy: The Dragon’s Trap | 神奇男孩 III：龙之陷阱 | GG | 1989 | [GG-014](#gg-014) |

---

### 皇家骑士团

<a id="series-37"></a>

只收 Ogre Battle／Tactics Ogre 体系，军团制与网格战棋分开理解，不混入 FFT。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Tactics Ogre: Let Us Cling Together | 皇家骑士团：命运之轮 | SNES | 1995 | [SNES-015](#snes-015) |
| Ogre Battle: The March of the Black Queen | 皇家骑士团：黑色皇后 | SNES | 1993 | [SNES-103](#snes-103) |
| Ogre Battle 64: Person of Lordly Caliber | 皇家骑士团 64：王者之风 | N64 | 1999 | [N64-035](#n64-035) |
| Tactics Ogre: The Knight of Lodis | 皇家骑士团外传：罗迪斯的骑士 | GBA | 2001 | [GBA-069](#gba-069) |
| Tactics Ogre: Let Us Cling Together (PlayStation) | 皇家骑士团：命运之轮（PS 移植版） | PS1 | 1997 | [PS1-024](#ps1-024) |

---

### 前线任务

<a id="series-38"></a>

聚焦机甲部件、政治军事与战术部署，序号正传多为战棋，Gun Hazard 与 Alternative 则尝试动作或实时方向。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Front Mission: Gun Hazard | 前线任务：枪之危机 | SNES | 1996 | [SNES-018](#snes-018) |
| Front Mission 3 | 前线任务 3 | PS1 | 1999 | [PS1-023](#ps1-023) |
| Front Mission Alternative | 前线任务 Alternative | PS1 | 1997 | [PS1-072](#ps1-072) |
| Front Mission | 前线任务（WSC） | WS | 2002 | [WS-012](#ws-012) |

---

### 超级机器人大战

<a id="series-39"></a>

把机器人动画角色与机体放入战棋关卡，以精神指令、改造和交叉剧情形成特色。A Portable 源自 GBA《A》，不是 NDS 作品移植。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Dai-3-Ji Super Robot Taisen | 第 3 次超级机器人大战 | SNES | 1993 | [SNES-019](#snes-019) |
| Super Robot Taisen EX | 超级机器人大战 EX | SNES | 1994 | [SNES-020](#snes-020) |
| Dai-4-Ji Super Robot Taisen | 第 4 次超级机器人大战 | SNES | 1995 | [SNES-021](#snes-021) |
| Super Robot Taisen Gaiden: Masou Kishin – The Lord of Elemental | 超级机器人大战外传：魔装机神 | SNES | 1996 | [SNES-022](#snes-022) |
| Super Robot Taisen A | 超级机器人大战 A | GBA | 2001 | [GBA-035](#gba-035) |
| Super Robot Taisen R | 超级机器人大战 R | GBA | 2002 | [GBA-036](#gba-036) |
| Super Robot Taisen D | 超级机器人大战 D | GBA | 2003 | [GBA-037](#gba-037) |
| Super Robot Taisen J | 超级机器人大战 J | GBA | 2005 | [GBA-038](#gba-038) |
| Super Robot Taisen: Original Generation | 超级机器人大战 OG | GBA | 2002 | [GBA-039](#gba-039) |
| Super Robot Taisen: Original Generation 2 | 超级机器人大战 OG2 | GBA | 2005 | [GBA-040](#gba-040) |
| Super Robot Taisen W | 超级机器人大战 W | NDS | 2007 | [NDS-028](#nds-028) |
| Super Robot Taisen K | 超级机器人大战 K | NDS | 2009 | [NDS-029](#nds-029) |
| Super Robot Taisen L | 超级机器人大战 L | NDS | 2010 | [NDS-030](#nds-030) |
| Super Robot Taisen A Portable | 超级机器人大战 A Portable | PSP | 2008 | [PSP-016](#psp-016) |
| Super Robot Taisen Alpha | 超级机器人大战 α | PS1 | 2000 | [PS1-019](#ps1-019) |
| Super Robot Taisen Alpha Gaiden | 超级机器人大战 α 外传 | PS1 | 2001 | [PS1-020](#ps1-020) |
| Dai-2-Ji Super Robot Taisen (PlayStation) | 第 2 次超级机器人大战（PS 重制版） | PS1 | 1999 | [PS1-021](#ps1-021) |
| Dai-2-Ji Super Robot Taisen | 第 2 次超级机器人大战 | NES | 1991 | [NES-096](#nes-096) |

---

### 圣剑传说

<a id="series-40"></a>

围绕《圣剑传说 2》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Secret of Mana / Seiken Densetsu 2 | 圣剑传说 2 | SNES | 1993 | [SNES-023](#snes-023) |
| Trials of Mana / Seiken Densetsu 3 | 圣剑传说 3 | SNES | 1995 | [SNES-024](#snes-024) |
| Seiken Densetsu: Final Fantasy Gaiden / Final Fantasy Adventure | 圣剑传说：最终幻想外传 | GB | 1991 | [GB-034](#gb-034) |
| Sword of Mana | 新约圣剑传说 | GBA | 2003 | [GBA-075](#gba-075) |
| Legend of Mana | 圣剑传说：玛娜传奇 | PS1 | 1999 | [PS1-083](#ps1-083) |

---

### 传说系列

<a id="series-41"></a>

以即时线性动作战斗、角色小剧场和独立世界剧情为特点，各作主角与系统通常独立。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Tales of Phantasia | 幻想传说 | SNES | 1995 | [SNES-025](#snes-025) |
| Tales of Destiny | 宿命传说 | PS1 | 1997 | [PS1-039](#ps1-039) |
| Tales of Eternia | 永恒传说 | PS1 | 2000 | [PS1-040](#ps1-040) |

---

### 大航海时代

<a id="series-42"></a>

贸易、航海、发现与人物目标共同构成开放旅程，价值在于自由选择致富和探索路线，而不是固定关卡通关。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Uncharted Waters: New Horizons / Daikoukai Jidai II | 大航海时代 II | SNES | 1994 | [SNES-026](#snes-026) |

---

### 快打旋风

<a id="series-43"></a>

以简洁拳脚、武器与敌群管理奠定 Capcom 清版动作风格，SFC 移植版在合作和角色上曾受硬件限制。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Final Fight | 快打旋风 | SNES | 1990 | [SNES-040](#snes-040) |
| Final Fight 2 | 快打旋风 2 | SNES | 1993 | [SNES-071](#snes-071) |
| Final Fight 3 | 快打旋风 3 | SNES | 1995 | [SNES-072](#snes-072) |
| Final Fight | 快打旋风Final Fight | FBNEO | 1989 | [FBNEO-011](#fbneo-011) |

---

### MOTHER

<a id="series-44"></a>

围绕《地球冒险 2／MOTHER 2》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| EarthBound / Mother 2 | 地球冒险 2／MOTHER 2 | SNES | 1995 | [SNES-049](#snes-049) |
| Mother 3 | 地球冒险 3 | GBA | 2006 | [GBA-074](#gba-074) |

---

### 圣龙传说

<a id="series-45"></a>

围绕《Bahamut Lagoon》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Bahamut Lagoon | Bahamut Lagoon | SNES | 1996 | [SNES-056](#snes-056) |

---

### 龙战士

<a id="series-46"></a>

以龙族变身和传统 JRPG 探索为特色，Capcom 制作，不能写成“龙翼传说”的同一官方译名。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Breath of Fire | 龙战士 | SNES | 1994 | [SNES-060](#snes-060) |
| Breath of Fire II | 龙战士 II | SNES | 1995 | [SNES-061](#snes-061) |

---

### 米奇妙境

<a id="series-47"></a>

围绕《Illusion of Gaia》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Illusion of Gaia | Illusion of Gaia | SNES | 1994 | [SNES-064](#snes-064) |
| Castle of Illusion Starring Mickey Mouse | 米奇妙妙屋：幻影城堡 | GG | 1991 | [GG-006](#gg-006) |
| Land of Illusion Starring Mickey Mouse | 米奇妙境：幻影大陆 | GG | 1992 | [GG-007](#gg-007) |

---

### 魔界村

<a id="series-48"></a>

围绕《超魔界村》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Super Ghouls ’n Ghosts | 超魔界村 | SNES | 1991 | [SNES-075](#snes-075) |
| Makaimura for WonderSwan | 魔界村 for WonderSwan | WS | 1999 | [WS-007](#ws-007) |

---

### Darius

<a id="series-49"></a>

以多屏或宽屏演出、区域分支和机械海洋生物 Boss 著称，不同街机与家用版本不可只按标题互换。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Darius Twin | 太空战斗机：双子 | SNES | 1991 | [SNES-081](#snes-081) |
| Darius Plus | Darius Plus | PCE | 1990 | [PCE-009](#pce-009) |
| Darius / Darius II / Darius Gaiden | 太空战斗机 I／II／外传 | MAME | 1986 | [MAME-006](#mame-006) |

---

### 大盗五右卫门

<a id="series-50"></a>

围绕《加油五右卫门： Yukihime 救出绘卷》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| The Legend of the Mystical Ninja | 加油五右卫门： Yukihime 救出绘卷 | SNES | 1992 | [SNES-087](#snes-087) |
| Mystical Ninja Starring Goemon | 大盗五右卫门：桃山幕府之舞 | N64 | 1997 | [N64-036](#n64-036) |

---

### 女神转生与女神异闻录

<a id="series-51"></a>

本传与 Persona 分列，保留关联但不混用序号。

#### 真·女神转生

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Shin Megami Tensei if... | 真·女神转生 if… | SNES | 1994 | [SNES-088](#snes-088) |
| Shin Megami Tensei I / II | 真·女神转生 I／II | SNES | 1992–1994 | [SNES-100](#snes-100) |
| Shin Megami Tensei: Strange Journey | 真·女神转生：奇妙之旅 | NDS | 2009 | [NDS-066](#nds-066) |
| Shin Megami Tensei | 真·女神转生 | PS1 | 1992 | [PS1-065](#ps1-065) |
| Shin Megami Tensei II | 真·女神转生 II | PS1 | 1994 | [PS1-066](#ps1-066) |
| Shin Megami Tensei if... | 真·女神转生 if… | PS1 | 1994 | [PS1-067](#ps1-067) |

#### Persona

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Shin Megami Tensei: Persona 3 Portable | 女神异闻录 3 携带版 | PSP | 2010 | [PSP-012](#psp-012) |
| Revelations: Persona | Persona 1 | PS1 | 1996 | [PS1-062](#ps1-062) |
| Persona 2: Innocent Sin | Persona 2：Innocent Sin | PS1 | 1999 | [PS1-063](#ps1-063) |
| Persona 2: Eternal Punishment | Persona 2：Eternal Punishment | PS1 | 2000 | [PS1-064](#ps1-064) |

---

### 生化危机

<a id="series-52"></a>

通过有限资源、场景探索与威胁管理制造生存恐怖，后续作品逐步增加动作比重。不同平台移植的压缩和画面差异应具体说明。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Resident Evil 2 | 生化危机 2 | N64 | 1999 | [N64-009](#n64-009) |
| Resident Evil – Code: Veronica | 生化危机：代号维罗妮卡 | DC | 2000 | [DC-007](#dc-007) |
| Resident Evil | 生化危机 | PS1 | 1996 | [PS1-001](#ps1-001) |
| Resident Evil 2 | 生化危机 2 | PS1 | 1998 | [PS1-002](#ps1-002) |
| Resident Evil 3: Nemesis | 生化危机 3：复仇女神 | PS1 | 1999 | [PS1-003](#ps1-003) |

---

### 雷曼

<a id="series-53"></a>

围绕《雷曼 2：胜利大逃亡》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Rayman 2: The Great Escape | 雷曼 2：胜利大逃亡 | N64 | 1999 | [N64-034](#n64-034) |
| Rayman | 雷曼 | PS1 | 1995 | [PS1-081](#ps1-081) |

---

### 天外魔境

<a id="series-54"></a>

以和风幻想、夸张角色与 CD 音画演出构成 RPG／冒险系列，Hudson 与 Red 的呈现是 PCE CD 代表内容。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Tengai Makyou: Ziria | 天外魔境：自来也 | PCE | 1989 | [PCE-002](#pce-002) |
| Tengai Makyou II: Manji Maru | 天外魔境 II：卍丸 | PCE | 1992 | [PCE-015](#pce-015) |
| Tengai Makyou: Fuun Kabuki Den | 天外魔境：风云歌舞伎传 | PCE | 1993 | [PCE-016](#pce-016) |

---

### 伊苏

<a id="series-55"></a>

以高速动作、冲撞或小队战斗和鲜明配乐推动冒险，I・II、菲尔盖纳重制与 VII 的战斗系统并不相同。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Ys Book I & II | 伊苏 I・II | PCE | 1989 | [PCE-006](#pce-006) |
| Ys III: Wanderers from Ys | 伊苏 III：来自伊苏的冒险者 | PCE | 1991 | [PCE-017](#pce-017) |
| Ys IV: The Dawn of Ys | 伊苏 IV：伊苏的黎明 | PCE | 1993 | [PCE-018](#pce-018) |
| Ys I & II Chronicles | 伊苏 I・II 编年史 | PSP | 2011 | [PSP-019](#psp-019) |
| Ys: The Oath in Felghana | 伊苏：菲尔盖纳的誓约 | PSP | 2010 | [PSP-020](#psp-020) |
| Ys Seven | 伊苏 VII | PSP | 2010 | [PSP-021](#psp-021) |

---

### 梦幻战士

<a id="series-56"></a>

围绕《梦幻战士 1／2／3／4》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Valis: The Fantasm Soldier / Valis II / III / IV | 梦幻战士 1／2／3／4 | PCE | 1986–1993 | [PCE-030](#pce-030) |

---

### 泡泡龙与彩虹岛

<a id="series-57"></a>

围绕《阳伞之星：泡泡龙 III》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Parasol Stars: The Story of Bubble Bobble III | 阳伞之星：泡泡龙 III | PCE | 1991 | [PCE-042](#pce-042) |
| Bubble Bobble / Rainbow Islands | 泡泡龙／彩虹岛 | MAME | 1986 | [MAME-001](#mame-001) |

---

### 黄金太阳

<a id="series-58"></a>

以精神力解谜、精灵配置和召唤构成 JRPG 系统，前两作直接接续，NDS《漆黑的黎明》则转向后代故事。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Golden Sun | 黄金太阳：开启的封印 | GBA | 2001 | [GBA-003](#gba-003) |
| Golden Sun: The Lost Age | 黄金太阳：失落的时代 | GBA | 2003 | [GBA-004](#gba-004) |
| Golden Sun: Dark Dawn | 黄金太阳：漆黑的黎明 | NDS | 2010 | [NDS-048](#nds-048) |

---

### 逆转裁判

<a id="series-59"></a>

正传、逆转检事与同作者的《幽灵诡计》分开识别。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Gyakuten Saiban / Phoenix Wright: Ace Attorney | 逆转裁判 | GBA | 2001 | [GBA-011](#gba-011) |
| Gyakuten Saiban 2 / Phoenix Wright: Ace Attorney – Justice for All | 逆转裁判 2 | GBA | 2002 | [GBA-012](#gba-012) |
| Gyakuten Saiban 3 / Phoenix Wright: Ace Attorney – Trials and Tribulations | 逆转裁判 3 | GBA | 2004 | [GBA-013](#gba-013) |
| Phoenix Wright: Ace Attorney / Justice for All / Trials and Tribulations (DS) | 逆转裁判 1／2／3（NDS 版） | NDS | 2005 | [NDS-005](#nds-005) |
| Ace Attorney Investigations: Miles Edgeworth | 逆转检事 | NDS | 2009 | [NDS-006](#nds-006) |
| Gyakuten Kenji 2 / Ace Attorney Investigations 2 | 逆转检事 2 | NDS | 2011 | [NDS-007](#nds-007) |
| Ghost Trick: Phantom Detective | 幽灵诡计：幻影侦探 | NDS | 2010 | [NDS-008](#nds-008) |

---

### 高级战争

<a id="series-60"></a>

以透明兵种数值、地形与指挥官能力形成易读战棋，NDS 双屏与双战线改变指挥方式。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Advance Wars | 高级战争 | GBA | 2001 | [GBA-032](#gba-032) |
| Advance Wars 2: Black Hole Rising | 高级战争 2：黑洞崛起 | GBA | 2003 | [GBA-033](#gba-033) |
| Advance Wars: Dual Strike | 高级战争：双重打击 | NDS | 2005 | [NDS-023](#nds-023) |

---

### 王国之心

<a id="series-61"></a>

将原创角色与迪士尼、Square Enix 世界放入动作 RPG，记忆之链使用卡牌，梦中降生采用三主角视角。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Kingdom Hearts: Chain of Memories | 王国之心：记忆之链 | GBA | 2004 | [GBA-053](#gba-053) |
| Kingdom Hearts 358/2 Days | 王国之心：358/2 天 | NDS | 2009 | [NDS-038](#nds-038) |
| Kingdom Hearts: Birth by Sleep | 王国之心：梦中降生 | PSP | 2010 | [PSP-025](#psp-025) |

---

### 钻地先生

<a id="series-62"></a>

围绕《钻地先生 A》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mr. Driller A: Fushigi na Pacteria | 钻地先生 A | GBA | 2002 | [GBA-059](#gba-059) |
| Mr. Driller | 钻地先生 | WS | 1999 | [WS-003](#ws-003) |

---

### 合金弹头

<a id="series-63"></a>

以手绘像素、夸张动画和跑射 Boss 战见长，Nazca／SNK 的街机系列与 GBA 便携原创版应区分。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Metal Slug Advance | 合金弹头 Advance | GBA | 2004 | [GBA-060](#gba-060) |
| Metal Slug 1 / 2 / X / 3 / 4 / 5 | 合金弹头系列 | FBNEO | 1996–2003 | [FBNEO-128](#fbneo-128) |

---

### 风之少年

<a id="series-64"></a>

围绕《风之少年：梦之帝国》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Klonoa: Empire of Dreams | 风之少年：梦之帝国 | GBA | 2001 | [GBA-065](#gba-065) |
| Klonoa: Door to Phantomile | 风之少年：通往幻界之门 | PS1 | 1997 | [PS1-080](#ps1-080) |
| Klonoa: Moonlight Museum | 风之少年：月光博物馆 | WS | 1999 | [WS-002](#ws-002) |

---

### 雷顿教授

<a id="series-65"></a>

把动画式剧情与大量独立谜题结合，前三部构成初代三部曲，后续作品另有前传关系。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Professor Layton and the Curious Village | 雷顿教授与不可思议的小镇 | NDS | 2008 | [NDS-009](#nds-009) |
| Professor Layton and the Last Specter | 雷顿教授与魔神之笛 | NDS | 2008 | [NDS-010](#nds-010) |
| Professor Layton and the Unwound Future | 雷顿教授与最后的时间旅行 | NDS | 2010 | [NDS-011](#nds-011) |

---

### 世界树迷宫

<a id="series-66"></a>

玩家亲自绘制迷宫地图，并以职业小队应对 FOE 与资源压力，是 NDS 双屏用途最有说服力的 RPG 之一。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Etrian Odyssey | 世界树迷宫 | NDS | 2007 | [NDS-033](#nds-033) |
| Etrian Odyssey II: Heroes of Lagaard | 世界树迷宫 II：诸王的圣杯 | NDS | 2008 | [NDS-034](#nds-034) |

---

### 数码宝贝

<a id="series-67"></a>

围绕数码兽养成、进化和迷宫或世界探索展开，各作系统差异很大，不能仅按序号推断质量。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Digimon World Dawn / Dusk | 数码宝贝传说：日光／月光 | NDS | 2006 | [NDS-039](#nds-039) |
| Digimon World | 数码宝贝世界 | PS1 | 1999 | [PS1-068](#ps1-068) |
| Digimon World 2 | 数码宝贝世界 2 | PS1 | 2000 | [PS1-069](#ps1-069) |
| Digimon World 3 / 2003 | 数码宝贝世界 3 | PS1 | 2002 | [PS1-070](#ps1-070) |
| Digimon: Battle Spirit | 数码宝贝：战斗精神 | WS | 1999 | [WS-008](#ws-008) |

---

### 拳皇

<a id="series-68"></a>

三人组队、角色相性与 SNK 全明星阵容构成对战核心，各年作品会调整系统与队伍规则。97、98、2002 的流行原因不同，不能简单按年份判断优劣。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| The King of Fighters 94 | 拳皇94 | FBNEO | 1994 | [FBNEO-026](#fbneo-026) |
| The King of Fighters 95 | 拳皇95 | FBNEO | 1995 | [FBNEO-027](#fbneo-027) |
| The King of Fighters 96 | 拳皇96 | FBNEO | 1996 | [FBNEO-028](#fbneo-028) |
| The King of Fighters 97 | 拳皇97 | FBNEO | 1997 | [FBNEO-029](#fbneo-029) |
| The King of Fighters 98 | 拳皇98 | FBNEO | 1997 | [FBNEO-030](#fbneo-030) |
| The King of Fighters 99 | 拳皇99 | FBNEO | 1997 | [FBNEO-031](#fbneo-031) |
| The King of Fighters 2000 | 拳皇2000 | FBNEO | 2000 | [FBNEO-032](#fbneo-032) |
| The King of Fighters 2001 | 拳皇2001 | FBNEO | 2001 | [FBNEO-033](#fbneo-033) |
| The King of Fighters 2002 | 拳皇2002 | FBNEO | 2002 | [FBNEO-034](#fbneo-034) |
| The King of Fighters 2003 | 拳皇2003 | FBNEO | 2003 | [FBNEO-035](#fbneo-035) |

---

### 风云默示录

<a id="series-69"></a>

围绕《风云默示录1》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Kizuna Encounter: Super Tag Battle / Fu’un Super Combo | 风云默示录1 | FBNEO | 1996 | [FBNEO-051](#fbneo-051) |
| Savage Reign | 风云默示录2 | FBNEO | 1995 | [FBNEO-052](#fbneo-052) |
| Kizuna Encounter | Kizuna Encounter | FBNEO | 1996 | [FBNEO-054](#fbneo-054) |

---

### 怒首领蜂与Cave

<a id="series-70"></a>

以密集弹幕、连击和打分路线构成射击挑战，通关与高分玩法差异很大；后期基板在 N4100 上需单独测试。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| DoDonPachi | 怒首领蜂 | FBNEO | 1997 | [FBNEO-084](#fbneo-084) |
| DoDonPachi Dai-Ou-Jou | 大往生 | FBNEO | 2002 | [FBNEO-085](#fbneo-085) |
| ESP Ra.De. | ESP Ra.De. | FBNEO | 1998 | [FBNEO-086](#fbneo-086) |
| Espgaluda | 长空超少年Espgaluda | FBNEO | 2003 | [FBNEO-087](#fbneo-087) |
| Progear | Progear 的岚 | FBNEO | 2001 | [FBNEO-088](#fbneo-088) |

---

### 樱花大战

<a id="series-71"></a>

围绕《樱花大战 3：巴黎在燃烧吗》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Sakura Wars 3: Is Paris Burning? | 樱花大战 3：巴黎在燃烧吗 | DC | 2001 | [DC-020](#dc-020) |
| Sakura Wars 4: Fall in Love, Maidens | 樱花大战 4：恋爱吧少女 | DC | 2002 | [DC-021](#dc-021) |

---

### 格兰蒂亚

<a id="series-72"></a>

以行动顺序干预和冒险旅程见长，Game Arts 制作的系列不应把发行商写成 Enix 或 Bandai。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Grandia II | 格兰蒂亚 II | DC | 2000 | [DC-023](#dc-023) |
| Grandia | 格兰蒂亚 | PS1 | 1997 | [PS1-033](#ps1-033) |

---

### 怪物猎人

<a id="series-73"></a>

通过观察怪物动作、武器招式与素材装备循环形成长期挑战，便携共斗是 PSP 时代影响力爆发的重要因素。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Monster Hunter Portable 3rd | 怪物猎人携带版 3rd | PSP | 2010 | [PSP-001](#psp-001) |
| Monster Hunter Freedom Unite / Monster Hunter Portable 2nd G | 怪物猎人携带版 2nd G | PSP | 2008 | [PSP-002](#psp-002) |

---

### 英雄传说与轨迹

<a id="series-74"></a>

重视城镇文本、人物关系与连续世界观，空轨、零碧和那由多应分篇理解；卡卡布三部曲属于更早的英雄传说体系。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| The Legend of Heroes: Trails in the Sky FC | 英雄传说：空之轨迹 FC | PSP | 2006 | [PSP-003](#psp-003) |
| The Legend of Heroes: Trails in the Sky SC | 英雄传说：空之轨迹 SC | PSP | 2007 | [PSP-004](#psp-004) |
| The Legend of Heroes: Trails in the Sky the 3rd | 英雄传说：空之轨迹 the 3rd | PSP | 2008 | [PSP-005](#psp-005) |
| The Legend of Heroes: Zero no Kiseki | 英雄传说：零之轨迹 | PSP | 2010 | [PSP-006](#psp-006) |
| The Legend of Heroes: Ao no Kiseki | 英雄传说：碧之轨迹 | PSP | 2011 | [PSP-007](#psp-007) |
| Nayuta no Kiseki / The Legend of Nayuta: Boundless Trails | 那由多之轨迹 | PSP | 2012 | [PSP-008](#psp-008) |
| The Legend of Heroes II: Prophecy of the Moonlight Witch / III: White Witch / IV: A Tear of Vermillion / V: Cagesong of the Ocean | 英雄传说：卡卡布三部曲 | PSP | 2004–2006 | [PSP-009](#psp-009) |

---

### 寄生前夜

<a id="series-75"></a>

把线粒体科幻、纽约舞台与 RPG 成长结合，续作更偏生存恐怖动作，《第三次生日》则进一步转向射击。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| The 3rd Birthday | 寄生前夜：第三次生日 | PSP | 2010 | [PSP-011](#psp-011) |
| Parasite Eve | 寄生前夜 | PS1 | 1998 | [PS1-010](#ps1-010) |
| Parasite Eve II | 寄生前夜 II | PS1 | 1999 | [PS1-011](#ps1-011) |

---

### 山脊赛车

<a id="series-76"></a>

以易上手的漂移和街机节奏为卖点，Type 4 更以车队叙事、美术与音乐形成独特风格。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Ridge Racer | 山脊赛车 | PSP | 2005 | [PSP-013](#psp-013) |
| R4: Ridge Racer Type 4 | 山脊赛车 Type 4 | PS1 | 1998 | [PS1-051](#ps1-051) |

---

### 战场女武神

<a id="series-77"></a>

在回合部署中即时操纵单位移动与射击，绘本式画面和战场地形是标志，PSP 两作转为学园与更密集任务结构。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Valkyria Chronicles II | 战场女武神 2 | PSP | 2010 | [PSP-022](#psp-022) |
| Valkyria Chronicles III | 战场女武神 3 | PSP | 2010 | [PSP-023](#psp-023) |

---

### 音乐方块

<a id="series-78"></a>

围绕《音乐方块》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Lumines: Puzzle Fusion | 音乐方块 | PSP | 2004 | [PSP-028](#psp-028) |
| Lumines II | 音乐方块 II | PSP | 2006 | [PSP-044](#psp-044) |

---

### 寂静岭

<a id="series-79"></a>

以雾、声音、心理象征与不可靠叙事制造不安，PSP《破碎的记忆》还以心理测试改变呈现，不是《起源》的直接续作。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Silent Hill: Origins | 寂静岭：起源 | PSP | 2007 | [PSP-032](#psp-032) |
| Silent Hill: Shattered Memories | 寂静岭：破碎的记忆 | PSP | 2009 | [PSP-033](#psp-033) |
| Silent Hill | 寂静岭 | PS1 | 1999 | [PS1-029](#ps1-029) |

---

### 铁拳

<a id="series-80"></a>

以四键对应四肢、侧移与浮空连段构成 3D 格斗，家用版通常加入角色与额外模式。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Tekken: Dark Resurrection | 铁拳：暗黑复苏 | PSP | 2006 | [PSP-038](#psp-038) |
| Tekken 3 | 铁拳 3 | PS1 | 1997 | [PS1-050](#ps1-050) |

---

### 幻想水浒传

<a id="series-81"></a>

收集 108 星宿、建设据点并在个人与战争尺度间切换，群像招募是系列最重要的结构。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Suikoden | 幻想水浒传 | PS1 | 1995 | [PS1-034](#ps1-034) |
| Suikoden II | 幻想水浒传 II | PS1 | 1998 | [PS1-035](#ps1-035) |

---

### 露娜

<a id="series-82"></a>

以重视角色演出的传统 JRPG 见长，PS1 Complete 版加入动画和重制内容，与更早 CD 版有版本差异。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Lunar: Silver Star Story Complete | 露娜：银河之星 | PS1 | 1996 | [PS1-042](#ps1-042) |
| Lunar 2: Eternal Blue Complete | 露娜 2：永恒之蓝 | PS1 | 1998 | [PS1-043](#ps1-043) |

---

### 荒野兵器

<a id="series-83"></a>

把西部片意象、枪械与奇幻 JRPG 结合，以角色固有能力解谜和回合战斗推进。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Wild Arms | 荒野兵器 | PS1 | 1996 | [PS1-044](#ps1-044) |
| Wild Arms 2nd Ignition | 荒野兵器 2 | PS1 | 1999 | [PS1-045](#ps1-045) |

---

### 古惑狼

<a id="series-84"></a>

以纵深视角平台跳跃、箱子收集和障碍节奏见长，赛车衍生则采用漂移蓄力竞速。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Crash Bandicoot 1 / 2: Cortex Strikes Back / 3: Warped | 古惑狼 1／2／3 | PS1 | 1996–1998 | [PS1-048](#ps1-048) |
| Crash Team Racing | 古惑狼赛车 | PS1 | 1999 | [PS1-078](#ps1-078) |

---

### 小龙斯派罗

<a id="series-85"></a>

以滑翔、冲撞和火焰探索彩色 3D 关卡，收集宝石与救龙是早期作品主要驱动力。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Spyro the Dragon 1 / 2: Ripto’s Rage! / 3: Year of the Dragon | 小龙斯派罗 1／2／3 | PS1 | 1998–2000 | [PS1-049](#ps1-049) |

---

### GT赛车

<a id="series-86"></a>

以真实车款、驾照挑战、调校和赛事经营建立家用拟真赛车范式，是 Polyphony Digital 的代表系列。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Gran Turismo | GT 赛车 | PS1 | 1997 | [PS1-052](#ps1-052) |
| Gran Turismo 2 | GT 赛车 2 | PS1 | 1999 | [PS1-053](#ps1-053) |

---

### 古墓丽影

<a id="series-87"></a>

以网格化空间、跳跃解谜和遗迹探索构成 3D 动作冒险，早期固定坦克式操作需要适应。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Tomb Raider I / II / III | 古墓丽影 1／2／3 | PS1 | 1996–1998 | [PS1-054](#ps1-054) |

---

### 噗哟噗哟

<a id="series-88"></a>

围绕《噗哟噗哟通》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Puyo Puyo Tsu | 噗哟噗哟通 | FBNEO | 1994 | [FBNEO-130](#fbneo-130) |
| Puyo Puyo Tsu | 噗哟噗哟通（GG） | GG | 1994 | [GG-016](#gg-016) |
| Puyo Puyo Sun | 噗哟噗哟 SUN | MAME | 1996 | [MAME-023](#mame-023) |
| VS Puyo Puyo SUN / Futari de Puyo Puyo SUN | 双人噗哟噗哟 SUN | MD | 2022 | [MD-054](#md-054) |

---

### Aleste

<a id="series-89"></a>

围绕《GG 亚雷斯》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| GG Aleste | GG 亚雷斯 | GG | 1991 | [GG-012](#gg-012) |
| Power Strike II | 力量打击 II | GG | 1993 | [GG-013](#gg-013) |

---

### 块魂

<a id="series-90"></a>

围绕《块魂：我与我的块魂》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Me & My Katamari | 块魂：我与我的块魂 | PSP | 2005 | [PSP-045](#psp-045) |

---

### Theme 经营模拟

<a id="series-91"></a>

围绕《主题医院》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Theme Hospital | 主题医院 | PS1 | 1998 | [PS1-086](#ps1-086) |

---

### 传说的斯塔菲

<a id="series-92"></a>

围绕《传说的斯塔菲》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Densetsu no Stafy | 传说的斯塔菲 | GBA | 2002 | [GBA-077](#gba-077) |
| Densetsu no Stafy 2 | 传说的斯塔菲 2 | GBA | 2003 | [GBA-078](#gba-078) |
| Densetsu no Stafy 3 | 传说的斯塔菲 3 | GBA | 2004 | [GBA-079](#gba-079) |
| Densetsu no Stafy 4 | 传说的斯塔菲 4 | NDS | 2006 | [NDS-075](#nds-075) |
| The Legendary Starfy | 传说的斯塔菲：对决！达伊尔海贼团 | NDS | 2008 | [NDS-076](#nds-076) |

---

### 基连的野望

<a id="series-93"></a>

围绕《机动战士高达：基连的野望——吉翁独立战争记》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Mobile Suit Gundam: Gihren’s Greed | 机动战士高达：基连的野望——吉翁独立战争记 | PS1 | 1998 | [PS1-087](#ps1-087) |
| Mobile Suit Gundam: Gihren’s Greed – Blood of Zeon | 机动战士高达：基连的野望——吉翁的系谱 | PS1 | 2000 | [PS1-088](#ps1-088) |
| Mobile Suit Gundam: Gihren’s Greed – Axis no Kyoui V | 机动战士高达：基连的野望——阿克西斯的威胁 V | PSP | 2009 | [PSP-046](#psp-046) |

---

### 幻想大陆战记

<a id="series-94"></a>

围绕《幻想大陆战记：弗鲁塞那传说》等真实同一系列作品整理，按平台回到对应版本。

| 完整商品名 | 中文译名 | 平台 | 出版日期 | 平台条目 |
|---|---|---|---:|---|
| Brigandine: The Legend of Forsena | 幻想大陆战记：弗鲁塞那传说 | PS1 | 1998 | [PS1-089](#ps1-089) |
| Brigandine: Grand Edition | 幻想大陆战记：Grand Edition | PS1 | 2000 | [PS1-090](#ps1-090) |

---

## 中文化版本与精选非官方改版

这一章与官方商品清单分开管理。**中文化不视为新游戏；改版也不冒充官方发行。** 文件建议按 `平台／原版`、`平台／汉化`、`平台／改版` 分开，各自保留补丁说明、底本版本和独立存档。只把补丁应用于自己合法备份的原版，不提供 ROM 或下载地址。

### 中文化版本：优先保留哪些

“早期中文化”包括当年港台或大陆厂商推出、但未必获得原权利人正式授权的版本；它们是中文游戏传播史的一部分，不等于官方中文版。译者、修订者与 CRC 以所选补丁说明为准，不用一个模糊的“汉化版”覆盖所有修订。

| 平台 | 原作／范围 | 中文化性质 | 选择与使用建议 |
|---|---|---|---|
| NES／FC | Final Fantasy / II / III | 早期中文化＋后续修正 | FC 的《太空战士》等旧译名承载早期传播史；建议保留一个忠实修正版本，法术、道具和存档必须实测。 |
| NES／FC | Dragon Quest I–IV | 早期中文化＋后续修正 | DQ 的文本和菜单量较大，不同卡带时期译名差异明显；III／IV 优先选修复乱码与存档问题的版本。 |
| NES／FC | Metal Max | 先锋卡通中文化＋doubledr 等修正 | 中文化是它在中文圈形成口碑的重要原因；修正版改善旧版文本与兼容，仍应保留日版原作作对照。 |
| NES／FC | Tenchi wo Kurau I／II | 早期中文化＋后续修正 | 武将、阵型与剧情都依赖文本，诸葛孔明传尤其需要完整中文化；不要把玩家改编剧情当官方原作。 |
| NES／FC | Fire Emblem／Fire Emblem Gaiden | 民间汉化 | 初代与外传的武器、职业和角色对话需要准确译名；外传系统与正统序号作不同。 |
| NES／FC | Dai-2-Ji Super Robot Taisen | 民间汉化 | 第二次机战是中文圈早期战棋记忆之一，精神指令与机体名称应统一；它和 PS1 重制版不是同一镜像。 |
| NES／FC | Nakahara no Hasha／Haou no Tairiku | 早期中文化＋后续修正 | 中原之霸者与霸王的大陆是 Namco 系统，中文菜单让它们成为 FC 策略启蒙；不要套用光荣《三国志》发行信息。 |
| NES／FC | Captain Tsubasa II: Super Striker | 民间汉化＋修复 | 必杀技、球员与剧情文本量大，中文化明显提升可玩性；修正重点应是死机、字库和赛程显示。 |
| MD | Langrisser I／II | 民间汉化 | 兵种、转职与指挥范围需要清楚文本，Der Langrisser 的路线选择尤其依赖翻译。 |
| MD | Shining Force I／II | 民间汉化 | 角色对话、转职和道具说明是主要阅读点；GG 外传不是这两作的镜像版本。 |
| MD | Phantasy Star IV | 民间汉化＋修正 | 剧情和组队技说明适合完整中文体验，选择修复字体与文本溢出的版本。 |
| MD | Beyond Oasis／Landstalker | 民间汉化 | 两款动作 RPG 都依赖道具和谜题提示，中文能降低等距视角与精灵谜题之外的额外门槛。 |
| SNES／SFC | Chrono Trigger／Final Fantasy V／VI | 民间汉化 | 三部 Square RPG 都有成熟中文化需求；职业、魔石、协力技等术语应保持一致，不把后续复刻追加内容误写入 SFC 原版。 |
| SNES／SFC | Dragon Quest III／V／VI | 民间汉化 | SFC 的 III 是重制，V／VI 为 16 位原作；与 NDS 重制分版本保存，字库和存档分别验证。 |
| SNES／SFC | Fire Emblem: Genealogy of the Holy War／Thracia 776 | 民间汉化 | 血统、配对、俘虏和疲劳等机制需要精确说明；两作属于同一世界的不同时段。 |
| SNES／SFC | Tactics Ogre: Let Us Cling Together | 民间汉化 | 阵营、法律和职业文本量大；SFC 原版与 PSP《命运之轮》不是同一重制版本。 |
| SNES／SFC | Terranigma／Bahamut Lagoon／Live A Live | 民间汉化 | 三款未正式海外发行的作品各以复兴世界、龙与群像、分时代章节见长，中文能补足其最重要的叙事价值。 |
| GBA | Pokémon Emerald／FireRed／LeafGreen | 民间汉化 | 中文便于理解特性、技能和剧情；“386”“全神兽”等同时改数据的作品应改归改版，不冒充纯汉化。 |
| GBA | Golden Sun／The Lost Age | 民间汉化 | 精神力、精灵与召唤术语较多，两部连续故事适合统一译名。 |
| GBA | Castlevania: Circle of the Moon／Harmony of Dissonance／Aria of Sorrow | 民间汉化 | DSS、法术书与魂系统的说明各不相同；三作都应保留原日版作版本对照。 |
| GBA | Phoenix Wright: Ace Attorney 1–3 | 民间汉化 | 法庭指证要求精确文本，优先选修复错字、证物描述和存档的版本；NDS 版另有章节与操作差异。 |
| GBA | Mother 3 | 民间汉化 | 原版仅在日本正式发行，汉化使章节叙事和节奏战斗更易理解；声音连击需要实际听节拍。 |
| NDS | Pokémon Platinum／HeartGold／SoulSilver／Black／White／Black 2／White 2 | 民间汉化 | 神奥、城都与合众作品均可按世代整理中文版本；纯汉化与提高难度、改图鉴的改版分目录。 |
| NDS | Dragon Quest IV／V／VI／IX | 民间汉化 | 章节、人生旅程、双世界与多人任务分别依赖大量文本；NDS 版不是 GBA 移植。 |
| NDS | Ghost Trick／Ace Attorney Investigations 2 | 民间汉化 | 逆转检事 2 未正式海外发行，中文化尤其重要；幽灵诡计的线索链要求准确译文。 |
| NDS | 999／Professor Layton 系列 | 民间汉化 | 数字根、谜题提示和多结局文本是核心，不适合只靠图片攻略跳过语言。 |
| PS1 | Final Fantasy VII／VIII／IX／Tactics | 民间汉化 | 魔晶石、Junction、职业与政治叙事均需统一术语；多盘版必须让汉化镜像与 M3U 盘序一致。 |
| PS1 | Xenogears／Chrono Cross／Vagrant Story | 民间汉化 | 三部作品的世界观和系统文本密度高，中文更适合理解机甲设定、平行世界与武器构筑。 |
| PS1 | Suikoden II／Valkyrie Profile | 民间汉化 | 108 星招募和英灵章节都含易遗漏条件，中文可降低理解成本，但仍需保留原版镜像作校验。 |
| PS1 | Metal Gear Solid／Persona 2: Innocent Sin | 民间汉化 |  codec 与潜行提示、传言系统和人物关系都高度依赖文本；Innocent Sin 的 PS1 日版与后续移植分开。 |
| PSP | Trails in the Sky FC／SC／Zero／Ao | 民间汉化 | 轨迹系列 NPC 文本和连续剧情量很大，建议按 FC→SC→Zero→Ao 顺序，并分游戏备份存档。 |
| PSP | Persona 3 Portable／Valkyria Chronicles III | 民间汉化 | P3P 的日程社群与战场女武神 3 的部队任务都需要文本；后者未正式海外发行。 |
| PSP | Ys: The Oath in Felghana／Ys Seven／Monster Hunter Portable 3rd | 民间汉化 | 装备、技能、怪物与任务说明适合中文；动作本身不需要等汉化，但完整体验会明显受益。 |

### 精选非官方改版：增强、重构与全新内容

这里的“威力加强版”按玩家修改版处理；光荣等厂商正式发行的 Power‑Up Kit／威力加强版仍是官方商品，不放进下表。纯无敌、无限金钱、简单换皮和粗暴提高数值不占位置。

| 平台 | 改版名称 | 对应原作 | 类型 | 内容、难度与兼容说明 |
|---|---|---|---|---|
| NES／FC | Super Mario Bros. 3Mix | [超级马力欧兄弟 3](#nes-003) | 全新关卡／跨作机制 | 融合多部马力欧元素与新地图，完成度高；先通原版再玩，部分改版 Mapper 需在 Mesen／FCEUmm 验证。 |
| NES／FC | Super Mario Unlimited | [超级马力欧兄弟](#nes-001) | 全新关卡／难度重构 | 基于初代引擎设计新世界，强调隐藏路线与跳跃技巧，不是官方 Lost Levels。 |
| NES／FC | Rockman 4: Minus Infinity | [洛克人 4](#nes-009) | 系统增强／全新关卡 | 重做武器、Boss 与关卡并加入惊喜演出，质量很高但难度硬核；适合熟悉元祖系列的玩家。 |
| SNES／SFC | The Second Reality Project Reloaded | [超级马力欧世界](#snes-001) | 全新关卡 | 大型新关卡包，重做地图、图形与音乐，保留 SMW 手感；与原版分存档。 |
| SNES／SFC | The Legend of Zelda: Parallel Worlds | [塞尔达传说：众神的三角力量](#snes-004) | 全新地图／难度重构 | 重排世界和迷宫，路线与解谜几乎全新，难度高于原作；不是官方续作。 |
| SNES／SFC | Super Metroid: Redesign Axeil Edition | [超级密特罗德](#snes-005) | 地图重构／难度调整 | 扩大并重塑泽贝斯探索，Axeil 版调整原作改版的严苛处；适合熟悉原版地图与技巧者。 |
| SNES／SFC | Final Fantasy VI: Brave New World | [最终幻想 VI](#snes-009) | 平衡与养成重构 | 重做角色、 Esper 与敌方数据，强化人物构筑差异；不是“简单加强”，需要重新理解系统。 |
| GBA | Pokémon Unbound | Pokémon FireRed | 全新地区与剧情／系统增强 | 完整原创地区、任务与较新世代机制，难度选项友好；这是大型改版，不是官方正统地区。 |
| GBA | Pokémon Radical Red | Pokémon FireRed | 图鉴与难度重构 | 以后代机制、技能和高强度对战见长，默认难度偏硬核；家庭首次游玩不建议替代原版。 |
| GBA | Pokémon Emerald Rogue | [宝可梦：绿宝石](#gba-002) | 规则重构／随机关卡 | 把道馆旅程改成连续路线选择与随机构筑，重玩性来自 Roguelike 循环，不是绿宝石剧情汉化。 |
| GBA | Pokémon Team Rocket Edition | Pokémon FireRed | 剧情改写／系统增强 | 从火箭队视角重讲关都并改动养成与任务，适合已熟悉原版剧情者。 |
| GBA | Fire Emblem: Vision Quest | [火焰之纹章：圣魔之光石](#gba-007) | 全新战役 | 利用 GBA 火纹引擎制作原创地图、角色与剧情，应作为独立同人战役管理。 |
| NDS | Pokémon Renegade Platinum | [宝可梦：白金](#nds-002) | 图鉴与平衡增强 | 保留神奥主线，扩展可用宝可梦并调整训练家与便利功能，是较接近“增强原作”的路线。 |
| NDS | Pokémon Sacred Gold／Storm Silver | [宝可梦：心金／魂银](#nds-001) | 图鉴与难度增强 | 扩展城都／关都可获得内容并提高训练家强度；两个改版对应两个原版底本。 |
| NDS | Pokémon Blaze Black 2／Volt White 2 | [宝可梦：黑 2／白 2](#nds-004) | 图鉴与难度增强 | 保留 BW2 主线并调整图鉴、队伍与难度；不要与第一代 Blaze Black／Volt White 混底本。 |
| GBC | Pokémon Crystal Clear | Pokémon Crystal | 开放世界／便利增强 | 把水晶版改造成自由选择起点与路线，保留 GBC 风貌；适合二周目式重玩。 |
| GBC | Pokémon Prism | Pokémon Crystal | 全新地区与剧情 | 在 GBC 引擎上制作新地区、新角色与任务，是大型原创改版，不是官方第三世代作品。 |
| MD | Sonic 3 Complete | [索尼克 3 与纳克鲁斯](#md-003) | 修复与可选增强 | 整合锁合内容并提供多项可选调整，目标是更完整的 Sonic 3 体验；选项不宜误当原始官方设置。 |
| MD | Sonic Megamix | [刺猬索尼克](#md-001) | 全新关卡／系统融合 | 汇集多角色、音乐与重做关卡，风格接近大型同人合集；不同版本完成状态不同，固定一个成熟版本收藏。 |
| N64 | Super Mario 64: Star Road | [超级马力欧 64](#n64-003) | 全新关卡 | 以新场景和新星星路线重制收集体验，规模接近完整同人续篇；图形插件与存档需单独验证。 |
| N64 | Super Mario 64: Last Impact | [超级马力欧 64](#n64-003) | 全新关卡／新机制 | 加入新能力、机关和大型关卡，技术改动较多；N4100 上用兼容插件逐场景测试。 |
| PS1 | Final Fantasy Tactics: Valeria | [最终幻想战略版](#ps1-008) | 职业与平衡重构 | 调整职业、装备、敌人和难度，让冷门技能更有用；适合已理解原版 FFT 的玩家。 |
| PSP | Final Fantasy Tactics: The Lion War | [最终幻想战略版：狮子战争](#psp-017) | 内容与职业增强 | 基于狮子战争追加职业、角色与战斗内容，底本必须是 PSP 版，不能套到 PS1 FFT。 |

### 改版安装与家庭游玩规则

1. 先读补丁要求的地区、Rev、Header 与 CRC，底本不对不要硬打；IPS／BPS／xdelta 不混用。
2. 原版、汉化、改版使用不同目录与存档名，先开新档再验证旧档；不要把兼容未证实的改版直接覆盖家庭共用存档。
3. 模拟器优先沿用原作核心；若改版修改 Mapper、容量或图形方式，再逐作切换核心。Rockman 4 MI、N64 大型改版尤其需要实际场景验证。
4. 难度标签必须保留：Radical Red、Parallel Worlds、Rockman 4 MI 等面向熟练玩家，不能替代家庭首次游玩的原版。

> 版本统计：上表共收录 33 组中文化建议、23 款精选改版。中文化与增强版不重复计算原作总数；含全新战役／地图的改版另作改版内容统计。

改版选择参考：[CBR 的 ROM hack 类型综述](https://www.cbr.com/best-rom-hacks-better-than-original/) 与 [Rockman 4: Minus Infinity 评测](https://www.romhacking.net/reviews/5674/)；FC 中文化传播参考 [重装机兵与 FC 中文 RPG 史料](https://k.sina.cn/article_1403377667_53a5d80300100pilc.html?from=game)。

---

## 三层查漏补缺结果

三层查漏都已落实到上方表格，而不是另留候选清单。榜单用于发现作品，系列用于核对版本和支线，品类用于检查玩法盲区；质量、外设与 N4100 负担再做最后筛选。

| 查漏路径 | 已实际补入或纠正的内容 |
|---|---|
| ① 榜单与精品／著名／特色作品 | 补入 Metroid、Super Castlevania IV、Ninja Five-O、The World Ends with You、Tony Hawk、Skies of Arcadia、Shining Force、GG Aleste、Judgement Silversword 等；PS1／PSP 不再只偏 RPG |
| ② 从重要系列反查缺作 | 拆清马力欧、宝可梦、三国、洛克人、最终幻想、光明／梦幻模拟战、女神转生子系列；补蓝宝石／红宝石、赤救助队、Wario Land II、Oracle 联动、GBC 与 WS 篇章 |
| ③ 从品类与细分反查主题和作品 | 补 Snow Bros.、Bubble Bobble、Puzzle Bobble、Puyo Puyo Tsu、Columns、Gunpey、Magical Drop III、Qix、Mole Mania；补 GG 光明力量外传与 WS 风之少年，避免类型章只有大作 |

核对来源：[IGN 任天堂百佳](https://www.ign.com/articles/the-100-best-nintendo-games-of-all-time)、[Nintendo Life SNES 50](https://www.nintendolife.com/guides/50-best-super-nintendo-snes-games-of-all-time)、[GBA 50](https://www.nintendolife.com/guides/50-best-game-boy-advance-games-of-all-time)、[NDS 50](https://www.nintendolife.com/guides/50-best-nintendo-ds-games-of-all-time)、[GBC 50](https://www.nintendolife.com/guides/50-best-game-boy-color-gbc-games-of-all-time)、[Metacritic PS1](https://www.metacritic.com/browse/game/ps1/)、[Metacritic PSP](https://www.metacritic.com/browse/game/psp/)、[Time Extension MD](https://www.timeextension.com/guides/best-sega-genesis-mega-drive-games-of-all-time)、[Time Extension GG](https://www.timeextension.com/guides/best-sega-game-gear-games-of-all-time)、[MobyGames WSC](https://www.mobygames.com/platform/wonderswan-color/)。

---

## 容量汇总与运行核对

| 平台 | 条目数 | 游戏数（合集展开） | 表内预留空间 | 建议位置 |
|---|---:|---:|---:|---|
| MAME | 23 | 30 | 0.74 GB | eMMC |
| FBNeo | 131 | 149 | 7.91 GB | eMMC |
| GBA | 79 | 82 | 1.64 GB | eMMC |
| GBC | 17 | 23 | 0.11 GB | eMMC |
| GB | 34 | 39 | 0.13 GB | eMMC |
| GG | 17 | 17 | 0.04 GB | eMMC |
| WS / WSC | 12 | 14 | 0.04 GB | eMMC |
| NES / FC | 96 | 96 | 0.09 GB | eMMC |
| SNES / SFC | 105 | 106 | 0.75 GB | eMMC |
| MD / Genesis | 54 | 54 | 0.25 GB | eMMC |
| PCE (PC Engine / TurboGrafx-16) | 44 | 49 | 1.06 GB | eMMC |
| PS1 | 90 | 97 | 58.23 GB | SSD |
| N64 | 37 | 39 | 0.82 GB | eMMC |
| PSP | 46 | 56 | 40.15 GB | SSD |
| Dreamcast | 39 | 40 | 33.18 GB | SSD |
| NDS | 76 | 86 | 5.41 GB | SSD |
| **官方库合计** | **900** | **977** | **150.53 GB** | 另留系统、BIOS、刮削与存档 |

### 游戏总数与总容量

- **官方游戏总数：977 个平台版本。** 合集已展开，地区别名不重复；同一游戏跨平台各算一个可玩版本。Game & Watch 等合集按独立商品计数，不把内含迷你游戏再拆成数十款。
- **原创改版内容：13 款。** 仅统计含全新战役、地区或主要地图的改版；纯汉化、平衡调整和便利增强不重复增加游戏数。
- **官方库预留：150.53 GB。** 中文化与精选改版若与原版全部并存，另建议预留 16 GB；**合计预算 166.53 GB**，系统、BIOS、刮削和存档另算。

> 容量是安装预算，不是实测文件总量；合集拆分、CHD／CSO、多盘与保留多个地区版都会改变占用。

### 实机核对顺序

1. NES、GB／GBC、GBA、GG、WS／WSC、MD、SNES：先开存档与特殊芯片游戏，检查 RTC、传感器和地区刷新率。
2. FBNeo／MAME：先验证 ROM set、BIOS、双人手柄，再检查高分采样与声音；不要跨核心随意搬 ZIP。
3. NDS、PS1：NDS 看双屏与触控，PS1 看记忆卡和多盘；默认原生分辨率。
4. N64、Dreamcast、PSP：按游戏选择插件与 1× 渲染，测最繁忙的战斗／竞速场景，而非只看菜单；本指南不声称这些重型平台全库稳定。

### 本文已直接修正的典型错误

- 海外《Super Mario Bros. 2》与日本《Super Mario USA》是同一游戏的不同地区发行；日版高难度 2 代写为《The Lost Levels》。
- SFC《恶魔城 XX》不等于 PCE《血之轮回》；MD 有《Raiden Trad》《R-Type》正式移植；DC《Street Fighter III: Double Impact》不含 3rd Strike。
- 宝可梦赤救助队在 GBA、青救助队在 NDS；白金是神奥，绿宝石主线是固拉多／盖欧卡／烈空坐。
- 《重装机兵》只属于 Metal Max／Metal Saga；《Final Fantasy Tactics》只属于最终幻想战略版；GB《Final Fantasy Legend》属于沙加，均不再串入其他专题。
- 《番茄酱王国大冒险》与《传说的斯塔菲》是不同作品；Panzer General／Allied General 没有街机原版，Brigandine: Grand Edition 是官方扩展版。
- 《Puyo Puyo Sun》街机原版是 ST-V；MD《VS Puyo Puyo SUN》是 2022 年 Mini 2 的双人新移植，不倒填成 1996 年旧卡带。
- GBA 没有 DQV／DQVI 原生移植；PSP 歌姬计划首作是《Project DIVA》，不是家用机《Project DIVA F》。

## 摄像头与麦克风验证附录

机器带有摄像头和麦克风，只说明物理设备存在；能否用于游戏必须经过 **Linux 驱动 → Batocera 设备识别 → 模拟器核心接口** 三层。任何一层缺失，都不能把外设游戏写成可玩。此附录是现场验证流程，不是对当前机器已经兼容的承诺。

### 1．先确认操作系统是否看见设备

在 Batocera 的 SSH 终端执行；不同镜像未必安装全部命令，缺少命令时以设备节点和系统日志交叉判断，不要为了测试盲目覆盖系统配置。

```bash
lsusb
v4l2-ctl --list-devices
ls -l /dev/video*
arecord -l
cat /proc/asound/cards
```

- 普通 **UVC 摄像头**通常应出现 `/dev/video0` 一类节点；`v4l2-ctl` 能列出格式，说明驱动层更进一步。
- **ALSA** 应列出录音设备，随后还要测试实际采样、音量与噪声；只有播放声卡不等于麦克风可用。
- USB 复合设备可能分别出现视频和音频节点。若设备未被识别，先换 USB 口并排除供电、转接器和隐私开关，再核对具体芯片与当前 Batocera 内核。

### 2．再确认模拟器是否提供输入接口

**系统识别不等于核心能调用。** RetroArch、libretro 核心和独立模拟器的摄像头／麦克风能力并不一致，同一核心不同 Batocera 版本也可能变化。先在当前界面查找 Microphone、Camera、Device Input 等选项，再用游戏内实际输入验证；不要只看“设备已连接”。

| 场景 | 本指南的处理 | 验证边界 |
|---|---|---|
| NDS《Nintendogs》《Brain Age》 | 保留，但麦克风不是全库统一前提 | 若当前 melonDS 提供真实麦克风输入，选择对应采集设备；若只有噪声／吹气模拟，只适合接受吹气的环节，不能保证连续语音识别 |
| NDS 触控与双屏 | 先用鼠标或映射手柄验证 | 与麦克风分开测试；双屏显示正常不代表语音链路正常 |
| N64《Hey You, Pikachu!》 | 不收录 | 原作需要 VRU 专用硬件与语音识别链路，内置普通麦克风不能据此承诺完整可玩 |
| DSi 摄像头游戏 | 不纳入普通 NDS 清单 | DSi 是不同硬件与核心支持范围，不能把 DSi 功能套到 NDS |
| 其他平台摄像头游戏 | 当前不设专门游戏库 | 本清单没有必须依赖摄像头的作品；只有核心明确支持且实测通过后才另行增加 |

### 3．建议的现场测试顺序

1. 先确认 `/dev/video*` 与 ALSA 采集设备，再在系统层做一次短录音／图像测试；失败就停在驱动层排查。
2. 在 melonDS 中检查输入选项，分别测试持续语音、短促吹气和无输入三种状态，排除环境噪声造成的假成功。
3. 用《Nintendogs》的语音呼唤和《Brain Age》的语音环节验证游戏内结果，并记录 Batocera 版本、核心版本和设备名。
4. 测试结果只写入该设备的个人配置；本指南仍保持“普通手柄即可运行大部分作品”的保守基线。

---

