# Batocera ROM 全集清单

> N4100 (Gemini Lake, 4核4线程, UHD 600核显) + 4GB内存 + Batocera (Linux)
> 存储: 64GB eMMC (ext4) + 256GB SSD (ext4), eMMC 直接软链接方案（无 mergerfs）

## 前言：Why 与 What

### Why — 为什么做这份清单

这是一份为特定硬件配置量身定制的复古游戏 ROM 全集清单。它的诞生源于一个简单的愿望：**在一台低功耗小主机上，用最合理的存储方案，跑通尽可能多平台、尽可能多经典游戏，并且每一款都是"值得玩"的好游戏，而不是什么"XX大全集"式的垃圾堆砌。**

过去几年，复古模拟社区出现过大量"50000合1"之类的ROM合集包，里面塞满了粗制滥造的盗版游戏、山寨改版、甚至是根本跑不起来的损坏文件。这份清单的核心理念恰恰相反：**宁缺毋滥**。每一款游戏都经过筛选，确保它在游戏史上有一定地位、有一定评分口碑、有一定的可玩价值。如果你是系列粉丝，系列章节会帮你按时间线梳理各代作品的关系，做到"知其然也知其所以然"。

### What — 这是什么、跑在什么上

| 项目 | 详情 |
|------|------|
| **主机型号** | DreamOne V6B（基于 Intel Celeron N4100 的迷你主机） |
| **CPU** | Intel Celeron N4100（Gemini Lake，4核4线程，基础1.1GHz / 睿频2.4GHz） |
| **GPU** | Intel UHD Graphics 600（12EU，350-750MHz） |
| **内存** | 4GB DDR4（板载，与核显共享内存带宽，是性能瓶颈之一） |
| **系统盘** | 创见 M.2 SATA SSD （TS256GMTS400） 256GB（ext4），安装 Batocera 系统 |
| **扩展存储** | 板载 eMMC 64GB（ext4），通过软链接挂载到 /userdata/roms 树下 |
| **操作系统** | Batocera.linux（基于 Arch Linux 的复古游戏专用操作系统） |
| **前端** | EmulationStation（游戏列表与封面墙） |
| **模拟器核心** | 各平台对应：FBA/libretro-FBNeo（街机）、PCSX-ReARMed/DuckStation（PS1）、melonDS（NDS）、PPSSPP（PSP）、Flycast（DC）、GLideN64（N64）、mgba（GBA）等 |
| **存储方案** | 不使用 mergerfs，直接在 eMMC 分区建目录，通过 ln -s 软链接到 /userdata/roms 树下。小体积平台（NES/SNES/MD/GBA/GB/N64/PCE/NDS/街机）走 eMMC，大体积平台（PS1/DC/PSP）走 SSD 原生目录 |
| **全集规模** | 约 830+ 款游戏，总计约 151GB |

### 文档结构说明

本文档分为三大部分：

1. **存储分配策略与配置步骤** — 告诉你怎么把 eMMC 挂载、怎么建软链接、权限怎么设
2. **各平台游戏清单** — 按平台（从8位到16位到32位到64位，从小到大）逐一列出每款游戏，含发行方、预估大小、备注
3. **专题系列图鉴** — 按游戏系列/IP组织，按发行时间梳理各代作品及版本关系，方便查漏补缺
4. **遗漏高分作品调研** — 结合 IGN、Metacritic、Fami通等权威榜单，盘点可能遗漏的高分佳作
5. **汇总与实操建议** — 容量总览表、BIOS/格式/刮削建议、N4100性能表、纠错清单


---

## 存储分配策略

> 方案：不使用 mergerfs，直接在 eMMC 分区上创建 ROM 目录，通过 `ln -s` 软链接到 `/userdata/roms` 下。
> 好处：没有合并层、没有路径混乱、出问题时一眼就能看出文件在哪。对 ROM 这种「一次性写入、永久读取」的场景，手动分配完全够用且更省心。

### 存储分配总览

| 存放位置 | 平台 | 预估总容量 | 说明 |
|----------|------|----------|-----------|------|
| **eMMC**（软链接） | NES/FC、GB/GBC、MD/Genesis、SNES/SFC、N64、PCE、GBA、NDS、街机(FBNeo/MAME) | ~18.2GB | 体积极小，eMMC 顺序读取完全够用；NDS 单文件 8-128MB，加载差异不可感知 |
| **SSD**（原生目录） | Dreamcast、PSP、PS1 | ~132.6GB | 大镜像集中地，PSP 单文件 800MB-1.8GB 必须走 SSD |

### 配置步骤

#### Step 1：挂载 eMMC

在 `/etc/fstab` 中添加一行（UUID 用 `blkid` 查询你自己的）：

```
UUID=你的eMMC分区UUID  /mnt/emmc  ext4  defaults  0 2
```

然后执行挂载：

```bash
sudo mkdir -p /mnt/emmc
sudo mount /dev/mmcblk0p1 /mnt/emmc   # 设备名以实际为准
```

确认挂载成功：`df -h /mnt/emmc`

#### Step 2：在 eMMC 上创建 ROM 目录

```bash
sudo mkdir -p /mnt/emmc/roms/{nes,gbc,md,snes,n64,pce,gba,nds,arcade}
```

把对应平台的 ROM 文件复制/下载到这些目录中。

#### Step 3：软链接到 Batocera 的 roms 树

```bash
ln -s /mnt/emmc/roms/nes /userdata/roms/nes
ln -s /mnt/emmc/roms/snes /userdata/roms/snes
ln -s /mnt/emmc/roms/md /userdata/roms/md
ln -s /mnt/emmc/roms/gba /userdata/roms/gba
ln -s /mnt/emmc/roms/gbc /userdata/roms/gbc
ln -s /mnt/emmc/roms/pce /userdata/roms/pce
ln -s /mnt/emmc/roms/n64 /userdata/roms/n64
ln -s /mnt/emmc/roms/arcade /userdata/roms/arcade
ln -s /mnt/emmc/roms/nds /userdata/roms/nds
```

PS1、Dreamcast、PSP 的 ROM 直接放在 SSD 上的 `/userdata/roms/` 对应目录中即可，不需要软链接。

#### Step 4：权限设置

```bash
sudo chown -R root:users /mnt/emmc/roms
sudo chmod -R 755 /mnt/emmc/roms
```

#### Step 5：重启 EmulationStation

```bash
batocera-es-swissknife --restart
# 或重启主机
```

ES 会自动扫描软链接目录并识别游戏。

### 注意事项

- **不要 symlink 单个游戏文件**：只按平台目录级别操作，否则日后核对清单、删重复、更新 ROM set 时会非常痛苦
- **不要把 `/userdata/savefiles`、`/userdata/saves`、`/userdata/system` 链到 eMMC**：存档和即时存档是高频随机写入，必须留在 SSD
- **不要链 PSP**：单文件 800MB-1.8GB，加载差 4-7 秒，且 PPSSPP 着色器缓存还要反复读；PSP 老老实实放 SSD
- eMMC 还剩约 40GB 余量，作为缓冲层：以后想试新核心、下整合包、或者把 Dreamcast 小体积作品挪过来，都有地方落。留白本身就是价值
- eMMC 写入寿命不用担心：ROM 是「一次性写入、永久读取」的数据形态，正好是 eMMC 最舒服的负载。真正耗寿命的是刮削和即时存档——这两样你已经放在 SSD 上了

---

## 各平台游戏清单
### NES / FC

**平台预估总容量：约 88MB（0.1GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 超级马力欧兄弟 | Nintendo | 0.25MB | FC开山之作 |
| 2 | 超级马力欧兄弟2 | Nintendo | 0.25MB | 海外版DokiDoki续作 |
| 3 | 超级马力欧兄弟3 | Nintendo | 1MB | FC巅峰之一 |
| 4 | 超级马力欧USA | Nintendo | 1MB | 日版超级马力欧兄弟3改 |
| 5 | 塞尔达传说 | Nintendo | 1MB | FC时代神作 |
| 6 | 塞尔达传说2：林克的冒险 | Nintendo | 1MB | 横版动作混合，爱恨两极 |
| 7 | 洛克人 | Capcom | 0.5MB | 粗糙但经典，建议从2入门 |
| 8 | 洛克人2 | Capcom | 0.5MB | 系列真正起点 |
| 9 | 洛克人3 | Capcom | 0.5MB | 博士大战威利博士 |
| 10 | 洛克人4 | Capcom | 1MB | 拉什装甲系统引入 |
| 11 | 洛克人5 | Capcom | 1MB | 宇宙篇 |
| 12 | 洛克人6 | Capcom | 1MB | FC洛克人终章 |
| 13 | 魂斗罗 | Konami | 0.5MB | 经典双人射击 |
| 14 | 魂斗罗2 | Konami | 0.5MB | 不如1代，但可玩 |
| 15 | 忍者龙剑传 | Tecmo | 0.5MB | 高难度动作标杆 |
| 16 | 忍者龙剑传2 | Tecmo | 0.5MB | 续作 |
| 17 | 忍者龙剑传3 | Tecmo | 0.5MB | 系列最差，难度曲线崩坏 |
| 18 | 冒险岛 | Hudson Soft | 0.25MB | 宫田洋经典 |
| 19 | 冒险岛2 | Hudson Soft | 0.25MB | 续作 |
| 20 | 冒险岛3 | Hudson Soft | 0.5MB | 3代 |
| 21 | 冒险岛4 | Hudson Soft | 0.5MB | 终章，偏难 |
| 22 | 坦克大战 | Konami | 0.25MB | 经典双人对战 |
| 23 | 马戏团 | Hudson Soft | 0.25MB | FC第一游戏机 |
| 24 | 赤影战士 | Konami | 0.5MB | 双人动作佳作 |
| 25 | 三国志 | Koei | 2MB | 光荣经典战略 |
| 26 | 中原之霸者 | 智冠 | 2MB | 智冠发行，三国题材策略游戏（正式商业作，非同人改） |
| 27 | 霸王的大陆 | 南晶科技 | 2MB | 大名版三国志，中文圈经典 |
| 28 | 最终幻想 | Square Enix | 2MB | 系列初代，古老但奠基 |
| 29 | 最终幻想2 | Square Enix | 2MB | 职业系统先驱 |
| 30 | 最终幻想3 | Square Enix | 4MB | DS重制更优，FC版有历史价值 |
| 31 | 勇者斗恶龙 | Square Enix | 2MB | 日R鼻祖，同系列有更优重制版 |
| 32 | 勇者斗恶龙2 | Square Enix | 2MB | 系列续作 |
| 33 | 勇者斗恶龙3 | Square Enix | 4MB | 重制版DQ1·2·3更优 |
| 34 | 勇者斗恶龙4 | Square Enix | 4MB | 章节叙事先驱 |
| 35 | 双截龙 | Technos | 0.5MB | 清版动作奠基 |
| 36 | 双截龙2 | Technos | 0.5MB | 续作 |
| 37 | 双截龙3 | Technos | 0.5MB | 换开发商，手感差 |
| 38 | 1942 | — | 0.25MB | CAPCOM射击经典 |
| 39 | 1943 | — | 0.5MB | 续作 |
| 40 | 绿色兵团 | Konami | 0.5MB | FC版存在 |
| 41 | 沙罗曼蛇 | Konami | 0.5MB | 科乐美横向射击 |
| 42 | 宇宙巡航机 | Konami | 0.5MB | Gradius FC移植 |
| 43 | 炸弹人 | Hudson Soft | 0.25MB | Hudson经典 |
| 44 | 炸弹人2 | Hudson Soft | 0.25MB | 续作 |
| 45 | 恶魔城 | Konami | 1MB | FC恶魔城初代 |
| 46 | 恶魔城2：诅咒之月 | Konami | 1MB | 续作 |
| 47 | 恶魔城3：德拉库拉的诅咒 | Konami | 2MB | FC恶魔城巅峰 |
| 48 | 热血硬派 | Technos | 0.5MB | 热血系列始祖 |
| 49 | 热血行进曲 | Technos | 0.5MB | 跑步+格斗 |
| 50 | 热血格斗传说 | Technos | 1MB | 热血+格斗游戏 |
| 51 | 热血物语 | Technos | 1MB | 校园黑帮动作 |
| 52 | 热血足球 | Technos | 0.5MB | 热血运动系列 |
| 53 | 热血篮球 | Technos | 0.5MB | 热血运动系列 |
| 54 | 热血躲避球 | Technos | 0.5MB | 热血运动系列 |
| 55 | 忍者神龟 | Konami | 0.5MB | 四人合作 |
| 56 | 忍者神龟2 | Konami | 0.5MB | 续作 |
| 57 | 忍者神龟3 | Konami | 0.5MB | 续作 |
| 58 | 忍者神龟4 | Konami | 0.5MB | 终章 |
| 59 | 松鼠大战 | Konami | 0.5MB | 双人合作解谜 |
| 60 | 松鼠大战2 | Konami | 0.5MB | 续作 |
| 61 | 唐老鸭梦冒险 | Nintendo | 0.5MB | 迪士尼FC冒险 |
| 62 | 唐老鸭梦冒险2 | Nintendo | 0.5MB | 续作 |
| 63 | 天使之翼 | Bandai | 2MB | 足球RPG，中文圈经典 |
| 64 | 天使之翼2 | Bandai | 2MB | 续作 |
| 65 | 重装机兵 | Crea-Tech | 4MB | Metal Max，中文圈神作 |
| 66 | 圣火徽章外传 | Atlus | 2MB | 火焰纹章前身 |
| 67 | 吞食天地 | Capcom | 4MB | 三国志同人改，中文经典 |
| 68 | 吞食天地2 | Capcom | 4MB | 续作 |
| 69 | 封神榜 | 汉堂资讯 | 2MB | 中文盗版商汉化 |
| 70 | 西游记世界 | 南晶科技 | 1MB | FC西游记 |
| 71 | 七宝奇谋 | Konami | 0.5MB | 双人合作冒险 |
| 72 | 超惑星战记Blaster Master | Sunsoft | 1MB | 机甲+探险 |
| 73 | 星际魂斗罗Journey to Silius | Konami | 0.5MB | 魂斗罗非官方续作 |
| 74 | 赤色要塞Jackal | Konami | 0.5MB | 吉普车射击 |
| 75 | 兵蜂TwinBee | Konami | 0.25MB | 科乐美射击 |
| 76 | 影子传说 | Natsume | 0.5MB | 忍者动作 |
| 77 | 忍者茶茶丸 | Natsume | 0.5MB | 忍者动作 |
| 78 | 蝙蝠侠 | Sunsoft | 0.5MB | Sunsoft版FC蝙蝠侠 |
| 79 | 小叮当 | Nintendo | 0.5MB | Doraemon FC游戏 |
| 80 | 龙珠 大魔神 | Bandai | 1MB | 龙珠FC游戏 |
| 81 | 圣斗士星矢 黄金传说 | Bandai | 2MB | 圣斗士RPG |
| 82 | 北斗神拳 | Tecmo | 1MB | FC格斗 |
| 83 | 挖金矿Lode Runner | Universal | 0.25MB | 经典解谜 |
| 84 | 敲冰块 | Nintendo | 0.25MB | 冰上打砖块 |
| 85 | 越野机车Excitebike | Nintendo | 0.25MB | 赛车经典 |
| 86 | 功夫Yie Ar Kung-Fu | — | 0.25MB | 格斗先驱 |
| 87 | 马里奥兄弟 (Mario Bros.) | Nintendo | 0.25MB | 1983街机移植，与#1超级马力欧兄弟是不同的游戏 |
| 88 | 大金刚 | Nintendo | 0.25MB | 马力欧始祖 |
| 89 | 打鸭子 | Nintendo | 0.125MB | 光枪射击 |
| 90 | 气球大战 | Nintendo | 0.25MB | 派对游戏 |
| 91 | 俄罗斯方块 | Nintendo | 0.125MB | NES版 |

### GB / GBC

**平台预估总容量：约 219MB（0.2GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 塞尔达传说：织梦岛 | Nintendo | 4MB | GB经典 |
| 2 | 塞尔达传说：织梦岛DX | Nintendo | 4MB | GBC彩色重制 |
| 3 | 超级马力欧乐园1 | Nintendo | 2MB | GB马力欧 |
| 4 | 超级马力欧乐园2 | Nintendo | 4MB | GB马力欧续作 |
| 5 | 瓦力欧乐园 | Nintendo | 4MB | GBC瓦力欧 |
| 6 | 瓦力欧乐园3 | Nintendo | 4MB | GBC续作 |
| 7 | 宝可梦红/绿/蓝/黄 | Nintendo | 8MB | GB初代 |
| 8 | 宝可梦金/银/水晶 | Nintendo | 16MB | GB时间变化系统 |
| 9 | 银河战士2 | Nintendo | 8MB | GB银河战士 |
| 10 | 星之卡比梦之泉DX | Nintendo | 8MB | GBC卡比 |
| 11 | 洛克人世界1 | Capcom | 4MB | GB洛克人 |
| 12 | 洛克人世界2 | Capcom | 4MB | 续作 |
| 13 | 洛克人世界3 | Capcom | 4MB | 续作 |
| 14 | 洛克人世界4 | Capcom | 4MB | 续作 |
| 15 | 洛克人世界5 | Capcom | 4MB | GB洛克人终章 |
| 16 | Shantae | Radical Fish | 8MB | GBC末期神作 |
| 17 | Metal Gear Ghost Babel | Konami | 8MB | GB合金装备 |
| 18 | Dragon Warrior Monsters 1 | Enix | 8MB | GB勇者斗恶龙怪兽篇 |
| 19 | Dragon Warrior Monsters 2 | Enix | 8MB | 续作 |
| 20 | 塞尔达传说：时空之章 | Nintendo | 8MB | GBC Oracle双作之一 |
| 21 | 塞尔达传说：大地之章 | Nintendo | 8MB | GBC Oracle双作之二 |
| 22 | 恶魔城德古拉传说1 | Konami | 8MB | GBC恶魔城 |
| 23 | 恶魔城德古拉传说2 | Konami | 8MB | GBC续作 |
| 24 | 恶魔城Legends | Konami | 8MB | GBC恶魔城 |
| 25 | 恶魔城小鬼Dracula | Konami | 4MB | GBC恶魔城 |
| 26 | 魔界塔士SaGa1 | Square | 4MB | GB RPG |
| 27 | 魔界塔士SaGa2 | Square | 4MB | GB续作 |
| 28 | 魔界塔士SaGa3 | Square | 8MB | GB终章 |
| 29 | 忍者龙剑传GB | Tecmo | 4MB | GB忍者龙剑传 |
| 30 | 双截龙GB | Technos | 4MB | GB双截龙 |
| 31 | 忍者神龟GB | Konami | 4MB | GB忍者神龟 |
| 32 | 七龙珠GB系列 | Bandai | 4MB | GB龙珠多作 |
| 33 | 圣斗士GB | Bandai | 4MB | GB圣斗士 |
| 34 | 牧场物语GB | Pack In Soft | 4MB | GB农场模拟 |
| 35 | 俄罗斯方块 | Nintendo | 1MB | GB版 |
| 36 | 马里奥医生 | Nintendo | 2MB | GB解谜 |
| 37 | 耀西蛋 | Nintendo | 2MB | GB休闲 |
| 38 | 炸弹人GB | Hudson Soft | 2MB | GB炸弹人 |
| 39 | 宝可梦卡片GB | Nintendo | 4MB | GB卡牌 |
| 40 | Game & Watch Gallery系列 | Nintendo | 2MB | GB经典合集 |
| 41 | 最终幻想 | Square Enix | 8MB | GBC最终幻想 |

### MD / Genesis

**平台预估总容量：约 264MB（0.3GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 索尼克1 | Sega | 3MB | 世嘉招牌 |
| 2 | 索尼克2 | Sega | 5MB | 纳克鲁斯登场 |
| 3 | 索尼克3&纳克鲁斯 | Sega | 8MB | 终极索尼克 |
| 4 | 怒之铁拳 | Sega | 4MB | MD清版动作 |
| 5 | 怒之铁拳2 | Sega | 4MB | 系列巅峰 |
| 6 | 怒之铁拳3 | Sega | 4MB | 日美版差异大 |
| 7 | 幽游白书：魔强统一战 | Sega | 4MB | 四人乱斗 |
| 8 | 格斗三人组 | Sega | 4MB | 怒之铁拳初代的盗版译名（与#4重复），建议只下怒之铁拳 |
| 9 | 战斧 | Sega | 4MB | 动作冒险 |
| 10 | 战斧2 | Sega | 4MB | 续作 |
| 11 | 战斧3 | Sega | 4MB | 系列下滑 |
| 12 | 兽王记 | Sega | 8MB | 短、重复度高 |
| 13 | 三国志2 | Koei | 4MB | 光荣战略MD版 |
| 14 | 三国志3 | Koei | 4MB | 光荣战略MD版 |
| 15 | 信长之野望：全国版 | Koei | 4MB | 光荣战略MD版 |
| 16 | Langrisser | Ascii | 8MB | 梦幻模拟战MD版 |
| 17 | Langrisser II | Ascii | 16MB | 梦幻模拟战II MD版 |
| 18 | 大战略 | Atlus | 8MB | 战略模拟 |
| 19 | [存疑]闪亮之刃 | — | 4MB | 注：名称对不上任何已知MD官方作品，可能为译名偏差，建议核实 |
| 20 | [存疑]闪亮之刃2 | — | 4MB | 注：名称对不上任何已知MD官方作品，可能为译名偏差，建议核实 |
| 21 | [存疑]幻想水滴 | — | 4MB | 注：名称对不上任何已知MD官方作品，可能为译名偏差，建议核实 |
| 22 | [不存在]雷电 | Irem | 4MB | 注：MD上无此作，雷电系列为Irem街机/PCE游戏 |
| 23 | [不存在]R-Type | Irem | 4MB | 注：MD上无此作，R-Type系列为Irem街机/PCE游戏 |
| 24 | Thunder Force III | — | 4MB | 射击 |
| 25 | Thunder Force IV | — | 4MB | 射击 |
| 26 | [存疑]枪之刃 | — | 4MB | 注：名称对不上任何已知MD官方作品，可能为译名偏差，建议核实 |
| 27 | [存疑]枪之刃2 | — | 4MB | 注：名称对不上任何已知MD官方作品，可能为译名偏差，建议核实 |
| 28 | 魂斗罗 铁血兵团 | Konami | 4MB | MD魂斗罗 |
| 29 | 超级忍2 | Sega | 2MB | 忍者动作 |
| 30 | 异形战士 Alien Soldier | Sega | 4MB | MD动作 |
| 31 | 波斯王子 | Brøderbund | 2MB | MD版 |
| 32 | Mega Man: The Wily Wars | — | 2MB | MD洛克人 |
| 33 | 街头霸王2 Special Champion Edition | Capcom | 4MB | MD移植 |
| 34 | NBA Jam | Midway | 4MB | 篮球 |
| 35 | Mortal Kombat | Midway | 4MB | 格斗 |
| 36 | Ecco the Dolphin | Sega | 4MB | 海洋冒险 |
| 37 | Rock n' Roll Racing | — | 4MB | 赛车 |
| 38 | ToeJam & Earl | Sega | 4MB | 冒险 |
| 39 | Shinobi III | Sega | 4MB | 忍者动作 |
| 40 | Golden Axe 1 | Sega | 4MB | 战斧RPG |
| 41 | Golden Axe 2 | Sega | 4MB | 续作 |
| 42 | Golden Axe 3 | Sega | 4MB | 终章 |
| 43 | Altered Beast | Sega | 2MB | 变身动作 |
| 44 | Sonic Spinball | Sega | 2MB | 弹珠台 |
| 45 | Sonic 3D Blast | Sega | 4MB | 3D索尼克 |
| 46 | 梦幻之星2 | Sega | 8MB | RPG |
| 47 | 梦幻之星4 | Sega | 16MB | RPG巨作 |
| 48 | 火枪英雄 Gunstar Heroes | Sega | 4MB | 动作 |
| 49 | 漫画地带 Comix Zone | Sega | 4MB | 动作 |
| 50 | 光之继承者 The Story of Thor | Sega | 4MB | 动作 |
| 51 | 蚯蚓战士 Earthworm Jim 1 | Virgin Interactive | 4MB | 动作 |
| 52 | 蚯蚓战士 Earthworm Jim 2 | Virgin Interactive | 4MB | 续作 |
| 53 | Vectorman 1 | Activision | 4MB | 动作 |
| 54 | Vectorman 2 | Activision | 4MB | 续作 |
| 55 | Ristar | Sega | 2MB | 动作 |
| 56 | 恶魔战士 | Capcom | 4MB | 格斗 |
| 57 | 饿狼传说 | SNK | 4MB | 格斗 |
| 58 | 侍魂 | SNK | 4MB | 格斗MD移植 |

### SNES / SFC

**平台预估总容量：约 710MB（0.7GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 超级马力欧世界 | Nintendo | 4MB | SFC旗舰马力欧 |
| 2 | 超级马力欧世界2：耀西岛 | Nintendo | 4MB | 耀西首登场 |
| 3 | 超级马力欧RPG | Square | 8MB | 马力欧+勇者斗恶龙风格RPG |
| 4 | 塞尔达传说：众神的三角力量 | Nintendo | 8MB | 塞尔达3D化先驱 |
| 5 | 超级银河战士 | Nintendo | 8MB | 银河恶魔城始祖 |
| 6 | 超时空之钥 | Square | 8MB | 殿堂级神作 |
| 7 | 最终幻想4 | Square Enix | 16MB | FF系列转折作 |
| 8 | 最终幻想5 | Square Enix | 16MB | 职业系统巅峰 |
| 9 | 最终幻想6 | Square Enix | 16MB | FF2D巅峰 |
| 10 | 勇者斗恶龙5 | Square Enix | 16MB | 汉化神作 |
| 11 | 勇者斗恶龙6 | Square Enix | 16MB | 梦境世界RPG |
| 12 | 火焰之纹章：纹章之谜 | Nintendo | 8MB | 火纹战棋奠基 |
| 13 | 火焰之纹章：圣战之系谱 | Nintendo | 16MB | 史诗战棋巨作 |
| 14 | 火焰之纹章：多拉基亚776 | Nintendo | 16MB | 硬核战棋 |
| 15 | 皇家骑士团2：命运之轮 | Square | 16MB | SFC原版Let Us Cling Together |
| 16 | Langrisser | Ascii | 8MB | 梦幻模拟战初代，系统未成熟 |
| 17 | Langrisser II | Ascii | 16MB | 梦幻模拟战II，系列巅峰 |
| 18 | 前线任务 Gun Hazard | Square | 8MB | 机甲RPG，好但引导差 |
| 19 | 超级机器人大战3 | Bandai | 8MB | 机战SFC系列 |
| 20 | 超级机器人大战EX | Bandai | 8MB | 机战SFC |
| 21 | 超级机器人大战第4次 | Bandai | 16MB | 机战SFC |
| 22 | 超级机器人大战Gaiden | Bandai | 8MB | 机战SFC外传 |
| 23 | 圣剑传说2 | Square | 16MB | 环形菜单劝退，单人体验一般 |
| 24 | 圣剑传说3 | Square | 16MB | 多主角切换 |
| 25 | 幻想传说 | Square | 16MB | 传说系列首作 |
| 26 | 大航海时代2 | Koei | 8MB | 航海模拟RPG |
| 27 | 三国志2 | Koei | 4MB | 光荣战略 |
| 28 | 三国志3 | Koei | 4MB | 光荣战略 |
| 29 | 三国志4 | Koei | 8MB | 光荣战略 |
| 30 | 信长之野望：全国版 | Koei | 4MB | 光荣战略 |
| 31 | 信长之野望：武将风云录 | Koei | 4MB | 光荣战略 |
| 32 | 信长之野望：霸王传 | Koei | 4MB | 光荣战略 |
| 33 | 信长之野望：天翔记 | Koei | 8MB | 光荣战略 |
| 34 | 恶魔城X：血之轮回 | Konami | 8MB | SFC恶魔城 |
| 35 | 洛克人X | Capcom | 4MB | 洛克人X系列首作 |
| 36 | 洛克人X2 | Capcom | 4MB | X系列续作 |
| 37 | 洛克人X3 | Capcom | 4MB | X系列终章 |
| 38 | 街头霸王2 Turbo | Capcom | 2MB | 格斗经典 |
| 39 | 超级街霸2 | — | 2MB | 街霸2加强版 |
| 40 | 快打旋风 | Capcom | 2MB | CAPCOM清版动作 |
| 41 | 超级大金刚 | Nintendo | 8MB | Rare经典 |
| 42 | 超级大金刚2 | Nintendo | 8MB | 续作 |
| 43 | 超级大金刚3 | Nintendo | 8MB | 终章 |
| 44 | 星际火狐 | Nintendo | 4MB | 以今天眼光看很简陋 |
| 45 | 星际火狐2 | Nintendo | 8MB | 续作 |
| 46 | F-ZERO | Nintendo | 2MB | 极速赛车 |
| 47 | 超级马力欧卡丁车 | Nintendo | 4MB | 马力欧卡丁车首作 |
| 48 | 时空勇士 | Square | 16MB | SQ经典RPG |
| 49 | 地球冒险2 | Ape Inc | 16MB | Mother系列续作 |
| 50 | 洛克人7 | Capcom | 8MB | 系列转折 |
| 51 | [删除]超级银河战士：零点任务 | Nintendo | 8MB | 注：此作为GBA游戏（2004），非SFC游戏，不应出现在此列表 |
| 52 | 魂斗罗精神 Contra III | Konami | 8MB | SFC魂斗罗 |
| 53 | 浪漫沙加1 | Square | 8MB | SaGa系列 |
| 54 | 浪漫沙加2 | Square | 8MB | SaGa系列 |
| 55 | 浪漫沙加3 | Square | 16MB | SaGa系列 |
| 56 | 星之海洋 | Square | 16MB | SQ RPG |
| 57 | Bahamut Lagoon | Enix | 8MB | 圣龙传说 |
| 58 | 天地创造 Terranigma | Enix | 8MB | RPG |
| 59 | Lufia 1 | Taito | 8MB | 迷宫RPG |
| 60 | Lufia 2 | Taito | 16MB | 续作 |
| 61 | Breath of Fire 1 | Capcom | 8MB | 龙翼传说 |
| 62 | Breath of Fire 2 | Capcom | 16MB | 续作 |
| 63 | ActRaiser | Square | 4MB | 动作+模拟 |
| 64 | Soul Blazer | Enix | 4MB | 动作RPG |
| 65 | Illusion of Gaia | Sunsoft | 8MB | 幻象花园 |
| 66 | 卡比超级明星 | Nintendo | 4MB | 星之卡比SFC |
| 67 | 星之卡比3 | Nintendo | 4MB | 卡比SFC |
| 68 | Panel de Pon | Intelligent Systems | 4MB | 拼图游戏 |
| 69 | SimCity | Maxis | 4MB | 模拟城市 |
| 70 | 牧场物语 | Pack In Soft | 4MB | 农场模拟 |
| 71 | 街头霸王Alpha 2 | Capcom | 4MB | 街霸前传 |
| 72 | 快打旋风2 | Capcom | 2MB | 续作 |
| 73 | 快打旋风3 | Capcom | 2MB | 终章 |
| 74 | Saturday Night Slam Masters | Capcom | 2MB | 摔跤 |
| 75 | U.N. Squadron | Capcom | 2MB | 射击 |
| 76 | Super Ghouls 'n Ghosts | Capcom | 4MB | 鬼屋妙探续作 |
| 77 | Axelay | Konami | 2MB | 射击 |
| 78 | Gradius III | Konami | 4MB | 宇宙巡航机3 |
| 79 | R-Type III | Irem | 4MB | 射击 |
| 80 | Parodius | Konami | 4MB | 反乌托邦射击 |
| 81 | TwinBee | Konami | 2MB | 兵蜂 |
| 82 | Darius Twin | Taito | 2MB | daleus |
| 83 | Pilotwings | Nintendo | 2MB | 飞行模拟 |
| 84 | Killer Instinct | Rare | 4MB | 格斗 |
| 85 | Earthworm Jim | Virgin Interactive | 4MB | 蚯蚓战士SFC版 |
| 86 | Aladdin | Virgin Interactive | 4MB | 阿拉丁Virgin外包 |
| 87 | 狮子王 | Virgin Interactive | 4MB | Virgin外包 |
| 88 | Goemon 神秘历险 | Konami | 4MB | 乐逸者 |
| 89 | Shin Megami Tensei if... | Atlus | 16MB | 真女神转生if |
| 90 | Robotrek | Enix | 4MB | 机器人RPG |
| 91 | Arcana | Enix | 4MB | RPG |
| 92 | E.V.O. | Sony Imagesoft | 4MB | 进化 |
| 93 | Gimmick! | Irem | 2MB | 平台动作 |
| 94 | Wario's Woods | Nintendo | 2MB | 瓦力欧森林 |
| 95 | Zombies Ate My Neighbors | Konami | 2MB | 僵尸吃了我的邻居 |
| 96 | The Lost Vikings | Blizzard | 2MB | 迷失的维京人 |
| 97 | Lemmings | Psygnosis | 2MB | 小精灵 |
| 98 | Another World | Delphine Software | 2MB | 异世界 |
| 99 | Prince of Persia | Brøderbund | 2MB | 波斯王子 |
### N64

**平台预估总容量：约 768MB（0.8GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 塞尔达传说：时之笛 | Nintendo | 32MB | 游戏史第一个满分神作 |
| 2 | 塞尔达传说：姆吉拉的假面 | Nintendo | 32MB | 续作，暗黑风格 |
| 3 | 超级马力欧64 | Nintendo | 16MB | 3D动作跳跃开山鼻祖 |
| 4 | 马力欧卡丁车64 | Nintendo | 16MB | 经典联机赛车 |
| 5 | 007：黄金眼 | Nintendo | 16MB | 当年的联机神器，模拟器帧率波动 |
| 6 | 星际火狐64 | Nintendo | 16MB | 64位射击 |
| 7 | F-ZERO X | Nintendo | 32MB | 极速赛车 |
| 8 | 完美黑暗 | Nintendo | 32MB | N4100掉帧明显 |
| 9 | 生化危机2 | Capcom | 32MB | N64移植版，本身就是灾难 |
| 10 | 任天堂明星大乱斗 | Nintendo | 16MB | 派对游戏 |
| 11 | 班卓熊大冒险1 | Rare | 16MB | Rare 3D收集 |
| 12 | 班卓熊大冒险2 | Rare | 32MB | 续作，N4100掉帧 |
| 13 | 纸片马力欧 | Nintendo | 32MB | 部分效果异常 |
| 14 | 咚奇刚64 | Nintendo | 32MB | N4100掉帧明显 |
| 15 | 耀西的故事 | Nintendo | 16MB | 3D平台 |
| 16 | 星之卡比64 | Nintendo | 16MB | GBA卡比N64版 |
| 17 | 宝可梦竞技场1 | Nintendo | 16MB | 对战 |
| 18 | 宝可梦竞技场2 | Nintendo | 32MB | 续作 |
| 19 | 宝可梦皮卡丘 | Nintendo | 8MB | 精灵收集 |
| 20 | 宝可梦快照 | Nintendo | 8MB | 拍照 |
| 21 | 宝可梦谜题联盟 | Nintendo | 16MB | 谜题 |
| 22 | 罪与罚：地球的继承人 | — | 32MB | 日版，射击神作 |
| 23 | 1080° Snowboarding | — | 16MB | 滑雪 |
| 24 | Wave Race 64 | — | 8MB | 水上摩托 |
| 25 | 马里奥网球64 | Nintendo | 16MB | 网球 |
| 26 | 马里奥高尔夫64 | Nintendo | 16MB | 高尔夫 |
| 27 | 炸弹人64 | Hudson Soft | 8MB | 炸弹人 |
| 28 | 马里奥派对1/2/3 | Nintendo | 32MB | 派对合集 |
| 29 | Conker's Bad Fur Day | Rare | 32MB | 成人向，英文梗多 |
| 30 | 恐龙猎人Turok 1 | Acclaim | 32MB | 射击 |
| 31 | 恐龙猎人Turok 2 | Acclaim | 32MB | 续作 |
| 32 | 星球大战Rogue Squadron | LucasArts | 32MB | 射击 |
| 33 | 星球大战阴影帝国 | LucasArts | 32MB | 续作 |
| 34 | Killer Instinct Gold | Rare | 16MB | 格斗 |

### PCE (PC Engine / TurboGrafx-16)

**平台预估总容量：约 816MB（0.8GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 恶魔城：血之轮回 | Konami | 64MB | PCE CD，月下前身，必下 |
| 2 | 天外魔境Ziria | Hudson Soft | 32MB | PCE RPG |
| 3 | PC原人1 | Namco | 16MB | PCE平台 |
| 4 | PC原人2 | Namco | 16MB | 续作 |
| 5 | PC原人3 | Namco | 16MB | 终章 |
| 6 | Ys I&II | Nihon Falcom | 32MB | PCE CD RPG |
| 7 | Raiden | Taito | 16MB | PCE射击 |
| 8 | R-Type | Irem | 16MB | PCE射击 |
| 9 | Darius Plus | Taito | 16MB | PCE射击 |
| 10 | Gate of Thunder | Jaleco | 16MB | PCE射击 |
| 11 | Lords of Thunder | Hudson Soft | 16MB | PCE射击 |
| 12 | Alien Crush | Namco | 8MB | PCE弹珠台 |
| 13 | Devil's Crush | Namco | 8MB | PCE弹珠台 |
| 14 | Bomberman '93/'94 | Hudson Soft | 8MB | PCE炸弹人 |
| 15 | 天外魔境II 卍MARU | Hudson Soft | 64MB | PCE CD，最大遗漏 |
| 16 | 天外魔境风云カブキ伝 | Hudson Soft | 32MB | PCE CD |
| 17 | Ys III | Nihon Falcom | 32MB | PCE CD |
| 18 | Ys IV | Nihon Falcom | 32MB | PCE CD |
| 19 | Neutopia 1 | Hudson Soft | 16MB | PCE动作RPG |
| 20 | Neutopia 2 | Hudson Soft | 16MB | 续作 |
| 21 | Blazing Lazers / Gunhed | Taito | 16MB | PCE射击 |
| 22 | Military Madness | Namco | 16MB | PCE战略 |
| 23 | Dungeon Explorer 1 | Hudson Soft | 16MB | PCE冒险 |
| 24 | Dungeon Explorer 2 | Hudson Soft | 16MB | 续作 |
| 25 | Legendary Axe | Taito | 8MB | PCE动作 |
| 26 | Vigilante | Taito | 8MB | PCE动作 |
| 27 | Splatterhouse | Namco | 8MB | PCE恐怖动作 |
| 28 | Cho Aniki | Compile | 16MB | PCE恶搞射击 |
| 29 | Cosmo Fantasy | Nihon Falcom | 32MB | PCE CD RPG |
| 30 | Valis 1-4 | Jaleco | 32MB | PCE动作RPG系列 |
| 31 | Cotton | Compile | 16MB | PCE射击 |
| 32 | Dead Moon | Taito | 8MB | PCE射击 |
| 33 | Xevious | Namco | 8MB | PCE射击 |
| 34 | Tower of Druaga | Namco | 8MB | PCE迷宫 |
| 35 | Image Fight | Namco | 8MB | PCE射击 |
| 36 | Download 1&2 | — | 16MB | PCE射击 |
| 37 | ときめきメモリアル | — | 64MB | PCE CD恋爱模拟 |
| 38 | 源平讨魔伝 | Taito | 16MB | PCE动作 |
| 39 | スーパー桃太郎電鉄 | — | 32MB | PCE模拟 |
### GBA

**平台预估总容量：约 1472MB（1.4GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | [删除]宝可梦 红/绿/蓝/黄/黄 | Nintendo | 8MB | 注：此作为GB/GBC游戏（1996），非GBA游戏，不应出现在此列表 |
| 2 | 宝可梦 火红/叶绿 | Nintendo | 16MB | GBA宝可梦复刻 |
| 3 | 宝可梦 绿宝石 | Nintendo | 16MB | GBA宝可梦三圣柱 |
| 4 | 宝可梦 漆黑的魅影 | Nintendo | 16MB | 民间改版(hack)，非官方作品；想玩正统请下绿宝石 |
| 5 | 黄金太阳：开启的封印 | Nintendo | 32MB | GBA RPG巅峰 |
| 6 | 黄金太阳：失落的时代 | Nintendo | 32MB | GBA RPG续作 |
| 7 | 火焰之纹章：封印之剑 | Nintendo | 32MB | GBA火纹 |
| 8 | 火焰之纹章：烈火之剑 | Nintendo | 32MB | GBA火纹 |
| 9 | 火焰之纹章：圣魔之光石 | Nintendo | 32MB | GBA火纹 |
| 10 | 恶魔城：晓月圆舞曲 | Konami | 32MB | GBA恶魔城第一神作 |
| 11 | 恶魔城：白夜协奏曲 | Konami | 32MB | GBA恶魔城 |
| 12 | 恶魔城：月轮 | Konami | 32MB | GBA恶魔城 |
| 13 | 逆转裁判1 | Capcom | 16MB | 神级剧情 |
| 14 | 逆转裁判2 | Capcom | 16MB | 续作 |
| 15 | 逆转裁判3 | Capcom | 16MB | 系列终章 |
| 16 | 超级马力欧Advance 1 | Nintendo | 16MB | GBA马力欧 |
| 17 | 超级马力欧Advance 2：耀西岛 | Nintendo | 16MB | GBA耀西岛 |
| 18 | 超级马力欧Advance 3 | Nintendo | 16MB | GBA耀西岛续作 |
| 19 | 超级马力欧Advance 4 | Nintendo | 16MB | GBA马力欧续作 |
| 20 | 马力欧与路易吉RPG | Nintendo | 32MB | GBA角色扮演 |
| 21 | 洛克人Zero 1 | Capcom | 16MB | GBA洛克人 |
| 22 | 洛克人Zero 2 | Capcom | 16MB | 续作 |
| 23 | 洛克人Zero 3 | Capcom | 16MB | 续作 |
| 24 | 洛克人Zero 4 | Capcom | 16MB | 终章 |
| 25 | 洛克人EXE | Capcom | 16MB | GBA对战RPG |
| 26 | 洛克人EXE2 | Capcom | 16MB | 续作 |
| 27 | 洛克人EXE3 | Capcom | 16MB | 续作 |
| 28 | 星之卡比：镜之大迷宫 | Nintendo | 32MB | GBA卡比 |
| 29 | 密特罗德融合 | Nintendo | 32MB | GBA银河恶魔城 |
| 30 | 密特罗德零点任务 | Nintendo | 32MB | GBA银河战士 |
| 31 | 最终幻想4 Advance | Square Enix | 32MB | FF移植 |
| 32 | 最终幻想5 Advance | Square Enix | 32MB | FF移植 |
| 33 | 最终幻想6 Advance | Square Enix | 32MB | FF移植 |
| 34 | 勇者斗恶龙5 | Square Enix | 32MB | GBA DQ |
| 35 | 勇者斗恶龙6 | Square Enix | 32MB | GBA DQ |
| 36 | 高级战争1 | Nintendo | 16MB | 战棋 |
| 37 | 高级战争2 | Nintendo | 16MB | 战棋续作 |
| 38 | 最终幻想战略版Advance | Square Enix | 32MB | 战棋RPG |
| 39 | 机器人大战A | Bandai | 32MB | 机战GBA |
| 40 | 机器人大战R | Bandai | 32MB | 机战GBA |
| 41 | 机器人大战D | Bandai | 32MB | 机战GBA |
| 42 | 机器人大战J | Bandai | 32MB | 机战GBA |
| 43 | Original Generation 1 | — | 32MB | 机战原创 |
| 44 | Original Generation 2 | — | 32MB | 机战原创续作 |
| 45 | 塞尔达缩小帽 | Nintendo | 32MB | GBA塞尔达 |
| 46 | 牧场物语矿石镇的伙伴们 | Pack In Soft | 32MB | GBA农场模拟 |
| 47 | 瓦力欧制造 | Nintendo | 16MB | GBA小游戏合集 |
| 48 | 瓦力欧大陆Advance 4 | Nintendo | 16MB | GBA瓦力欧 |
| 49 | 马里奥赛车Advance | Nintendo | 16MB | GBA赛车 |
| 50 | 索尼克Advance 1 | Sega | 8MB | GBA索尼克 |
| 51 | 索尼克Advance 2 | Sega | 8MB | 续作 |
| 52 | 索尼克Advance 3 | Sega | 8MB | 终章 |
| 53 | 光明之魂1 | Taito | 16MB | GBA动作RPG |
| 54 | 光明之魂2 | Taito | 16MB | 续作 |
| 55 | 博德之门：黑暗联盟 | BioWare | 32MB | GBA动作RPG |
| 56 | 龙珠Z舞空斗剧 | Bandai | 32MB | GBA龙珠 |
| 57 | 火影忍者系列 | Bandai | 16MB | GBA火影多作 |
| 58 | 王国之心记忆之链 | Square Enix | 32MB | GBA王国之心 |
| 59 | 游戏王 | Konami | 16MB | GBA卡牌 |
| 60 | 我们的太阳Boktai | Konami | 16MB | GBA阳光感应 |
| 61 | 马里奥高尔夫Advance | Nintendo | 16MB | GBA高尔夫 |
| 62 | 马里奥网球Advance | Nintendo | 16MB | GBA网球 |
| 63 | 超级猴子球 | Nintendo | 16MB | GBA休闲 |
| 64 | 钻地先生A | Namco | 16MB | GBA解谜 |
| 65 | 合金弹头Advance | SNK | 16MB | GBA射击 |

### NDS

**平台预估总容量：约 4640MB（4.5GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 宝可梦心金/魂银 | Nintendo | 64MB | 复刻天花板 |
| 2 | 宝可梦白金 | Nintendo | 64MB | DP续作 |
| 3 | 宝可梦黑/白1 | Nintendo | 128MB | 黑白篇上 |
| 4 | 宝可梦黑/白2 | Nintendo | 128MB | 黑白篇下 |
| 5 | 逆转裁判123（DS版） | Capcom | 64MB | DS复刻版 |
| 6 | 逆转检事1 | Capcom | 64MB | 检事篇 |
| 7 | 逆转检事2 | Capcom | 64MB | 续作 |
| 8 | 幽灵诡计Ghost Trick | Capcom | 64MB | 剧情封神 |
| 9 | 雷顿教授：不可思议城镇 | Level-5 | 64MB | 解谜 |
| 10 | 雷顿教授：魔神之笛 | Level-5 | 64MB | 续作 |
| 11 | 雷顿教授：最后的时间旅行 | Level-5 | 64MB | 终章 |
| 12 | 新超级马力欧兄弟 | Nintendo | 64MB | NDS马力欧 |
| 13 | 超级马力欧64 DS | Nintendo | 64MB | N64移植 |
| 14 | 塞尔达：幻影沙钟 | Nintendo | 64MB | NDS塞尔达 |
| 15 | 塞尔达：大地的汽笛 | Nintendo | 64MB | 续作 |
| 16 | 恶魔城：苍月的十字架 | Konami | 64MB | NDS恶魔城 |
| 17 | 恶魔城：废墟的肖像 | Konami | 64MB | 续作 |
| 18 | 恶魔城：被夺走的刻印 | Konami | 64MB | 终章 |
| 19 | 勇者斗恶龙4 | Square Enix | 64MB | NDS DQ |
| 20 | 勇者斗恶龙5 | Square Enix | 64MB | NDS DQ |
| 21 | 勇者斗恶龙6 | Square Enix | 64MB | NDS DQ |
| 22 | 勇者斗恶龙9 | Square Enix | 128MB | NDS DQ |
| 23 | 高级战争：双重打击 | Nintendo | 64MB | NDS战棋 |
| 24 | 火焰之纹章：新·暗黑龙与光之剑 | Nintendo | 64MB | NDS火纹 |
| 25 | 火焰之纹章：新·纹章之谜 | Nintendo | 64MB | NDS火纹 |
| 26 | 重装机兵3 | Crea-Tech | 64MB | NDS重装机兵 |
| 27 | 重装机兵：钢之季节 | Crea-Tech | 64MB | NDS重装机兵 |
| 28 | 机器人大战W | Bandai | 64MB | NDS机战 |
| 29 | 机器人大战K | Bandai | 64MB | NDS机战 |
| 30 | 机器人大战L | Bandai | 64MB | NDS机战收官作 |
| 31 | 节奏天国 | Nintendo | 32MB | 音游 |
| 32 | 动物之森 | Nintendo | 64MB | 模拟 |
| 33 | 世界树迷宫1 | Atlus | 64MB | 迷宫RPG |
| 34 | 世界树迷宫2 | Atlus | 64MB | 续作 |
| 35 | 999：极限脱出 | Chunsoft | 64MB | 视觉小说 |
| 36 | 闪电十一人1 | Level-5 | 64MB | 足球RPG |
| 37 | 闪电十一人2 | Level-5 | 64MB | 续作 |
| 38 | 王国之心358/2天 | Square Enix | 64MB | 动作RPG |
| 39 | 数码宝贝日光/月光 | Bandai | 64MB | NDS数码宝贝 |
| 40 | 符文工房1 | Marvelous | 64MB | 农场RPG |
| 41 | 符文工房2 | Marvelous | 64MB | 续作 |
| 42 | 牧场物语：风之集市 | Pack In Soft | 64MB | NDS农场 |
| 43 | 马里奥赛车DS | Nintendo | 64MB | NDS赛车 |
| 44 | 星之卡比：毛线传说 | Nintendo | 64MB | NDS卡比 |
| 45 | 耀西岛DS | Nintendo | 64MB | NDS耀西 |
| 46 | 洛克人ZX | Capcom | 64MB | NDS洛克人 |
| 47 | 洛克人ZX Advent | Capcom | 64MB | 续作 |
| 48 | 流星洛克人 | Capcom | 64MB | NDS洛克人 |
| 49 | 黄金太阳：漆黑的黎明 | Nintendo | 128MB | NDS黄金太阳 |
| 50 | 最终幻想3（DS重制版） | Square Enix | 128MB | FF重制 |
| 51 | 最终幻想4（DS重制版） | Square Enix | 128MB | FF重制 |
| 52 | 沙加2：秘宝传说（DS重制） | Square Enix | 64MB | SaGa重制 |
| 53 | 晶体编年史：时之回声 | Square Enix | 64MB | RPG |
| 54 | 勇者斗恶龙怪兽篇Joker 1 | Square Enix | 64MB | DQ怪兽 |
| 55 | 勇者斗恶龙怪兽篇Joker 2 | Square Enix | 64MB | 续作 |
| 56 | 宝可梦不可思议迷宫：赤救助队 | Nintendo | 64MB | 宝可梦迷宫 |
| 57 | 宝可梦不可思议迷宫：青救助队 | Nintendo | 64MB | 续作 |
| 58 | 宝可梦不可思议迷宫：时之探险队 | Nintendo | 64MB | 续作 |
| 59 | 宝可梦不可思议迷宫：暗之探险队 | Nintendo | 64MB | 续作 |
| 60 | 宝可梦不可思议迷宫：空之探险队 | Nintendo | 64MB | 终章 |
| 61 | 宝可梦护林员 | Nintendo | 64MB | NDS宝可梦 |
| 62 | 应援团/Elite Beat Agents | Nintendo | 32MB | 节奏 |
| 63 | 瓦力欧制造：触摸 | Nintendo | 64MB | NDS瓦力欧 |
| 64 | 接触！瓦力欧制造 | Nintendo | 64MB | 续作 |
| 65 | 寒蝉鸣泣之时：祭 | 07th Expansion | 64MB | 视觉小说 |
| 66 | 大合奏！バンドブラザーズ | Nintendo | 32MB | 音游 |
| 67 | 脑锻炼 | Nintendo | 32MB | 休闲 |
| 68 | 任天狗 | Nintendo | 64MB | 模拟 |
| 69 | 料理妈妈 | Nintendo | 32MB | 休闲 |

### 街机（FBNeo / MAME）

**平台预估总容量：约 9740MB（9.5GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 三国战纪正宗Plus | IGS | 100MB | IGS神作 |
| 2 | 三国战纪风云再起 | IGS | 100MB | 续作 |
| 3 | 三国战纪乱世枭雄 | IGS | 100MB | 续作 |
| 4 | 三国战纪七星转生 | IGS | 100MB | 续作 |
| 5 | 吞食天地2赤壁之战 | Capcom | 80MB | IGS |
| 6 | 西游释厄传 | IGS | 80MB | IGS |
| 7 | 西游释厄传Super | IGS | 80MB | 续作 |
| 8 | 西游释厄传群魔乱舞 | IGS | 80MB | 续作 |
| 9 | 西游释厄传2 | IGS | 100MB | 续作 |
| 10 | 恐龙快打 | Capcom | 60MB | 名将/黄帽 |
| 11 | 名将Captain Commando | Capcom | 60MB | CAPCOM |
| 12 | 圆桌骑士 | Capcom | 60MB | 升级切肉 |
| 13 | 惩罚者The Punisher | Capcom | 60MB | CAPCOM |
| 14 | 快打旋风Final Fight | Capcom | 60MB | CAPCOM |
| 15 | 电精1 | Capcom | 60MB | CAPCOM |
| 16 | 电精2 | Capcom | 60MB | 续作 |
| 17 | 午夜杀生Night Slashers | Capcom | 60MB | CAPCOM |
| 18 | Battle Circuit | Capcom | 60MB | CAPCOM |
| 19 | 装甲勇士Armored Warriors | Capcom | 60MB | CAPCOM |
| 20 | D&D毁灭之塔 | — | 60MB | CAPCOM |
| 21 | D&D暗影之谜 | — | 60MB | CAPCOM |
| 22 | AVP异形VS铁血战士 | — | 60MB | CAPCOM |
| 23 | 三个奇迹 | — | 60MB | CAPCOM |
| 24 | 龙王战士 | Capcom | 60MB | CAPCOM |
| 25 | 魔法剑 | Capcom | 60MB | CAPCOM |
| 26 | 战国传承3 | SNK | 60MB | SNK |
| 27 | 形意拳 | IGS | 40MB | IGS |
| 28 | 傲剑狂刀 | IGS | 60MB | IGS |
| 29 | 拳皇94 | SNK | 80MB | SNK |
| 30 | 拳皇95 | SNK | 80MB | SNK |
| 31 | 拳皇96 | SNK | 80MB | SNK |
| 32 | 拳皇97 | SNK | 80MB | 国内人气王 |
| 33 | 拳皇98 | SNK | 80MB | 平衡性神作 |
| 34 | 拳皇99 | SNK | 80MB | SNK |
| 35 | 拳皇2000 | SNK | 80MB | SNK |
| 36 | 拳皇2001 | SNK | 80MB | SNK |
| 37 | 拳皇2002 | SNK | 80MB | SNK |
| 38 | 拳皇2003 | SNK | 80MB | SNK |
| 39 | 真侍魂：霸王丸地狱变 | SNK | 80MB | SNK |
| 40 | 侍魂1 | SNK | 60MB | SNK |
| 41 | 侍魂2 | SNK | 60MB | SNK |
| 42 | 侍魂3 | SNK | 60MB | SNK |
| 43 | 侍魂4 | SNK | 80MB | SNK |
| 44 | 侍魂天草降临 | SNK | 80MB | SNK |
| 45 | 侍魂零 | SNK | 80MB | SNK |
| 46 | 月华剑士1 | SNK | 80MB | SNK |
| 47 | 月华剑士2 | SNK | 80MB | SNK |
| 48 | 饿狼传说1 | SNK | 60MB | SNK |
| 49 | 饿狼传说2 | SNK | 60MB | SNK |
| 50 | 饿狼传说3 | SNK | 80MB | SNK |
| 51 | 饿狼传说Real Bout | SNK | 80MB | SNK |
| 52 | 饿狼传说RB Special | SNK | 80MB | SNK |
| 53 | 龙虎之拳1 | SNK | 60MB | SNK |
| 54 | 龙虎之拳2 | SNK | 60MB | SNK |
| 55 | 世界英雄Perfect | Alpha Denshi | 60MB | SNK |
| 56 | 风云默示录1 | SNK | 60MB | SNK |
| 57 | 风云默示录2 | SNK | 80MB | SNK |
| 58 | Galaxy Fight | Atlus | 60MB | SNK |
| 59 | Kizuna Encounter | SNK | 60MB | SNK |
| 60 | Windjammers | Data East | 40MB | SNK |
| 61 | Neo Turf Masters | SNK | 40MB | SNK |
| 62 | Twinkle Star Sprites | SNK | 40MB | SNK |
| 63 | 街头霸王2 | Capcom | 40MB | CAPCOM |
| 64 | 街头霸王2 Hyper Fighting | Capcom | 40MB | CAPCOM |
| 65 | 街头霸王2 Super Turbo | Capcom | 40MB | CAPCOM |
| 66 | 少年街霸Alpha 1 | Capcom | 60MB | CAPCOM |
| 67 | 少年街霸Alpha 2 | Capcom | 60MB | CAPCOM |
| 68 | 少年街霸Alpha 3 | Capcom | 60MB | CAPCOM |
| 69 | 街头霸王III New Generation | Capcom | 80MB | CAPCOM |
| 70 | 街头霸王III 2nd Impact | Capcom | 80MB | CAPCOM |
| 71 | 街头霸王III 三度冲击 | Capcom | 80MB | CAPCOM |
| 72 | 恶魔战士Vampire Savior | Capcom | 80MB | CAPCOM |
| 73 | Marvel Super Heroes | Capcom | 80MB | CAPCOM |
| 74 | X-Men vs SF | Konami | 80MB | CAPCOM |
| 75 | MVC1 | Capcom | 80MB | CAPCOM |
| 76 | MVC2 | Capcom | 100MB | CAPCOM |
| 77 | 红色大地Red Earth | Capcom | 60MB | CAPCOM |
| 78 | 私立正义学园 | Capcom | 60MB | CAPCOM |
| 79 | JOJO的奇妙冒险 | Capcom | 60MB | CAPCOM |
| 80 | Capcom vs SNK 1 | — | 80MB | CAPCOM |
| 81 | Capcom vs SNK 2 | — | 100MB | CAPCOM |
| 82 | 打击者1945 | Psikyo | 40MB | Psikyo |
| 83 | 打击者1945 II | Psikyo | 40MB | Psikyo |
| 84 | 打击者1945 III | Psikyo | 40MB | Psikyo |
| 85 | 战国之刃 | Psikyo | 40MB | Psikyo |
| 86 | 武装飞鸟2 | Psikyo | 40MB | Psikyo |
| 87 | Gunbird 1 | Psikyo | 40MB | Psikyo |
| 88 | Gunbird 2 | Psikyo | 60MB | Psikyo |
| 89 | Sol Divide | Psikyo | 40MB | Psikyo |
| 90 | Dragon Blaze | Psikyo | 40MB | Psikyo |
| 91 | Strikers 1945 Plus | — | 40MB | Psikyo |
| 92 | Strikers 1999 | Chunsoft | 40MB | Psikyo |
| 93 | Strikers 2000 | — | 40MB | Psikyo |
| 94 | 怒首领蜂 | Cave | 60MB | Cave |
| 95 | 大往生 | Cave | 60MB | Cave，N4100吃力 |
| 96 | ESP Ra.De. | Cave | 60MB | Cave |
| 97 | 长空超少年Espgaluda | Cave | 60MB | Cave |
| 98 | Progear 的岚 | CaVE | 60MB | Cave |
| 99 | 虎直升机 | Toaplan | 40MB | Toaplan |
| 100 | 飞翔鲛Same!Same!Same! | Toaplan | 40MB | Toaplan |
| 101 | Truxton | Toaplan | 40MB | Toaplan |
| 102 | Vimana | Toaplan | 40MB | Toaplan |
| 103 | OutZone | Toaplan | 40MB | Toaplan |
| 104 | Battle Garegga | Raizing | 60MB | Raizing |
| 105 | 雷电1 | Irem | 40MB | Irem |
| 106 | 雷电2 | Irem | 40MB | Irem |
| 107 | R-Type | Irem | 40MB | Irem |
| 108 | R-Type Leo | Irem | 40MB | Irem |
| 109 | Xexex | Irem | 40MB | Irem |
| 110 | 魂斗罗街机 | Konami | 40MB | Konami |
| 111 | 超级魂斗罗街机 | Konami | 40MB | Konami |
| 112 | 忍者神龟Turtles in Time | Konami | 60MB | Konami |
| 113 | X-Men（6人版） | Konami | 60MB | Konami |
| 114 | 辛普森一家 | Konami | 40MB | Konami |
| 115 | Sunset Riders | Konami | 40MB | Konami |
| 116 | Violent Storm | Konami | 40MB | Konami |
| 117 | Mystic Warriors | Konami | 60MB | Konami |
| 118 | Life Force | Konami | 40MB | Konami |
| 119 | Gradius I/II/III/Gaiden | Konami | 80MB | Konami |
| 120 | Parodius全系 | Konami | 80MB | Konami |
| 121 | TwinBee全系 | Konami | 60MB | Konami |
| 122 | 泡泡龙+Rainbow Islands | Taito | 40MB | Taito |
| 123 | 奇奇怪界 | Taito | 40MB | Taito |
| 124 | 电梯大战1/2 | Taito | 40MB | Taito |
| 125 | Chase HQ | Taito | 40MB | Taito |
| 126 | 太空侵略者 | Taito | 20MB | Taito |
| 127 | Darius I/II/外传/Gaiden | Taito | 100MB | Taito |
| 128 | Ninja Warriors | Taito | 40MB | Taito |
| 129 | Rastan | Taito | 40MB | Taito |
| 130 | Metal Black | Taito | 40MB | Taito |
| 131 | Space Gun | Taito | 40MB | Taito |
| 132 | Puzzle Bobble 1-4 | Taito | 80MB | Taito |
| 133 | Mars Matrix | Taito | 60MB | Taito |
| 134 | Giga Wing 1 | Taito | 40MB | Taito |
| 135 | Giga Wing 2 | Taito | 60MB | Taito |
| 136 | 战斧1/2/3 | Sega | 80MB | Sega街机 |
| 137 | 兽王记 | Sega | 40MB | Sega街机 |
| 138 | 太空哈利 | Sega | 40MB | Sega |
| 139 | Fantasy Zone | Sega | 20MB | Sega |
| 140 | OutRun | Sega | 40MB | Sega |
| 141 | After Burner | Sega | 40MB | Sega |
| 142 | Sonic the Fighters | Sega | 40MB | Sega |
| 143 | Virtua Fighter 1 | Sega | 80MB | Sega |
| 144 | Virtua Fighter 2 | Sega | 100MB | Sega |
| 145 | Daytona USA | Sega | 60MB | Sega |
| 146 | Sega Rally | Sega | 40MB | Sega |
| 147 | Virtua Cop 1/2 | Sega | 100MB | Sega |
| 148 | Super Monaco GP | Sega | 40MB | Sega |
| 149 | Hang-On | Sega | 20MB | Sega |
| 150 | Thunder Blade | Sega | 40MB | Sega |
| 151 | 双截龙1/2/3 | Technos | 80MB | Technos |
| 152 | 热血系列街机版 | Technos | 80MB | Technos |
| 153 | Joe & Mac | Data East | 40MB | Data East |
| 154 | Karnov | Data East | 40MB | Data East |
| 155 | Heavy Barrel | Data East | 40MB | Data East |
| 156 | Dark Seal | Data East | 40MB | Data East |
| 157 | Midnight Resistance | Data East | 40MB | Data East |
| 158 | Burning Fight | Data East | 40MB | Data East |
| 159 | beatmania IIDX | Konami | 80MB | 音游 |
| 160 | DDR | Konami | 60MB | 音游 |
| 161 | pop'n music | Konami | 60MB | 音游 |
| 162 | GITADORA | Konami | 80MB | 音游 |
| 163 | Taiko no Tatsujin | Namco | 60MB | 太鼓达人 |
---

### Dreamcast

**平台预估总容量：约 33939MB（33.1GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 莎木1 | Sega | 1.2GB | 开放世界鼻祖 |
| 2 | 莎木2 | Sega | 2GB | 后期场景会掉帧 |
| 3 | 死或生2 | Tecmo | 1GB | DC版Hard Core |
| 4 | 灵魂能力Soul Calibur | Namco | 1GB | DC最具代表性3D格斗 |
| 5 | 街头霸王III：Double Impact | Capcom | 800MB | 含New Generation+三度冲击 |
| 6 | 疯狂出租车Crazy Taxi | Sega | 600MB | 赛车 |
| 7 | 生化危机：代号维罗妮卡 | Capcom | 1GB | DC版画质最佳 |
| 8 | 斑鸠Ikaruga | Treasure | 600MB | 弹幕神作 |
| 9 | Jet Set Radio | Sega | 600MB | 嘻哈滑行 |
| 10 | 索尼克大冒险 | Sega | 1GB | 3D索尼克 |
| 11 | 索尼克大冒险2 | Sega | 1.2GB | DC末代作品 |
| 12 | 能量宝石Power Stone 1 | Capcom | 800MB | 3D对战 |
| 13 | 能量宝石Power Stone 2 | Capcom | 1GB | 续作 |
| 14 | 漫威vs卡普空1 | Capcom | 800MB | 格斗 |
| 15 | 漫威vs卡普空2 | Capcom | 1GB | 续作 |
| 16 | 卡普空vsSNK 1 | Capcom | 800MB | 格斗 |
| 17 | 卡普空vsSNK 2 | Capcom | 1GB | 续作 |
| 18 | 罪恶工具Guilty Gear X | Arc System Works | 800MB | 格斗 |
| 19 | VF3tb | Sega | 1.2GB | DC独占 |
| 20 | 樱花大战3 | Sega | 1.2GB | DC独占 |
| 21 | 樱花大战4 | Sega | 1.5GB | DC独占 |
| 22 | 光明力量3 | Sega | 1GB | DC独占三部曲 |
| 23 | 梦幻之星在线 | Sega | 800MB | 在线RPG |
| 24 | 格兰蒂亚II | ASCII | 1GB | RPG |
| 25 | 世嘉拉力2 | Sega | 600MB | 赛车 |
| 26 | Daytona USA 2001 | Sega | 400MB | 赛车 |
| 27 | Rez | Sega | 600MB | 音游射击 |
| 28 | 太空频道5 Part 2 | Sega | 800MB | 音游 |
| 29 | 死亡之屋2 | Sega | 600MB | 光枪射击 |
| 30 | Typing of the Dead | Sega | 400MB | 打字射击 |
| 31 | 玩具指挥官Toy Commander | Sega | 600MB | 冒险 |
| 32 | Hydro Thunder | Sega | 600MB | 水上赛车 |
| 33 | 蓝天战队Blue Stinger | Sega | 800MB | 飞行射击 |
| 34 | Carrier | Treasure | 600MB | 空战 |
| 35 | Bangai-O | Treasure | 400MB | 弹幕 |
| 36 | NBA 2K / NFL 2K系列 | Sega | 800MB | 体育标杆 |
| 37 | Sega GT | Sega | 800MB | 赛车模拟 |
| 38 | 疯狂出租车2 | Sega | 1GB | 续作 |
| 39 | 索尼克Shuffle | Sega | 600MB | 跳过 |
### PSP

**平台预估总容量：约 48014MB（46.9GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 怪物猎人携带版3rd | Capcom | 1.5GB | 低功耗平台神话 |
| 2 | 怪物猎人携带版2nd G | Capcom | 1.5GB | 内容量比3rd更足 |
| 3 | 英雄传说：空之轨迹FC | Falcom | 800MB | 轨迹系列起点 |
| 4 | 英雄传说：空之轨迹SC | Falcom | 800MB | 续作 |
| 5 | 英雄传说：空之轨迹 the 3rd | Falcom | 800MB | 终章 |
| 6 | 英雄传说：零之轨迹 | Falcom | 1GB | 轨迹新篇 |
| 7 | 英雄传说：碧之轨迹 | Falcom | 1GB | 续作 |
| 8 | 那由多之轨迹 | Nihon Falcom | 800MB | 轨迹外传 |
| 9 | 英雄传说：卡卡布三部曲 | Falcom | 2GB | 白发魔女/朱红之泪/海之槛歌 |
| 10 | 最终幻想7：核心危机 | Square Enix | 800MB | FF7前传 |
| 11 | 寄生前夜：第三次生日 | Square Enix | 1GB | 越肩射击，评价一般 |
| 12 | 女神异闻录3携带版 | Atlus | 800MB | 静态地图多，核显无压力 |
| 13 | 山脊赛车 | Namco | 400MB | PSP最流畅赛车之一 |
| 14 | 初音未来：歌姬计划F | Sega | 600MB | 音游 |
| 15 | 初音未来：歌姬计划2nd | Sega | 600MB | 续作 |
| 16 | 初音未来：歌姬计划Extend | Sega | 600MB | 扩展版 |
| 17 | 铁拳6 | Namco | 1.5GB | 1x可玩偶有掉帧 |
| 18 | 侠盗猎车手：自由城故事 | Rockstar Games | 1.2GB | 偏重，1x可试 |
| 19 | 超级机器人大战A Portable | Bandai | 800MB | NDS机战PSP移植 |
| 20 | 最终幻想战略版：狮子战争 | Square Enix | 800MB | PSP独占 |
| 21 | 三国志7 | Koei | 800MB | 光荣战略 |
| 22 | 怪物猎人携带版2nd G | Capcom | 1.5GB | 低功耗平台神话 |
| 23 | 伊苏1&2 | — | 600MB | 动作RPG |
| 24 | 伊苏：菲尔盖纳之誓约 | — | 800MB | 伊苏外传 |
| 25 | 伊苏7 | — | 1GB | 动作RPG |
| 26 | 战场女武神2 | Sega | 800MB | 战棋 |
| 27 | 战场女武神3 | Sega | 1GB | PSP独占 |
| 28 | 魔界战记：便携版 | Nippon Ichi | 800MB | 战棋RPG |
| 29 | 王国之心：梦中降生Birth by Sleep | Square Enix | 1.2GB | 最大遗漏 |
| 30 | 高达VS高达NEXT PLUS | Bandai | 800MB | 机战格斗 |
| 31 | 真三国无双：联合突袭 | Tecmo Koei | 800MB | 共斗动作 |
| 32 | 乐克乐克LocoRoco | Sony | 400MB | 休闲 |
| 33 | 啪嗒砰Patapon | Sony | 400MB | 节奏战棋 |
| 34 | Lumines | Sony | 200MB | 音游 puzzle |
| 35 | 大众高尔夫 | Sony | 400MB | 休闲高尔夫 |
| 36 | 湾岸午夜俱乐部 | Namco | 800MB | 赛车 |
| 37 | 火爆狂飙：传奇 | EA | 800MB | 赛车 |
| 38 | DJMAX Portable | Neowiz | 400MB | 音游 |
| 39 | 太鼓达人 | Namco | 400MB | 音游 |
| 40 | 寂静岭：起源 | Konami | 800MB | 心理恐怖 |
| 41 | 寂静岭：破碎的记忆 | Konami | 800MB | 续作 |
| 42 | 最终幻想4/5/6（PSP移植） | Square Enix | 2GB | FF经典移植 |
| 43 | 秋之回忆/CLANNAD/命运石之门/寒蝉/Fate/Extra | — | 2GB | 文字冒险，核显零压力 |
| 44 | 刺客信条：血统 | Ubisoft | 1GB | 动作冒险 |
| 45 | 荣誉勋章：英雄 | EA | 800MB | 射击 |
| 46 | 抵抗：惩罚 | Sony | 800MB | 射击 |
| 47 | 合金装备：和平行者 | Konami | 1GB | 重型，1x可玩但不稳 |
| 48 | 最终幻想零式Type-0 | Square Enix | 1.2GB | 重型，1x可玩但不稳 |
| 49 | 战神：奥林匹斯之链 | Sony | 1GB | 重型，1x可玩但不稳 |
| 50 | 战神：斯巴达之魂 | Sony | 1GB | 重型，1x可玩但不稳 |
| 51 | 最终幻想纷争 | Square Enix | 1GB | 格斗 |
| 52 | 火影忍者：疾风传终极觉醒3 | Bandai | 800MB | 动漫动作 |

### PS1

**平台预估总容量：约 53830MB（52.6GB）**

| 序号 | 游戏名称 | 发行方 | 预估大小 | 备注 |
|------|----------|----------|----------|------|
| 1 | 生化危机1 | Capcom | 600MB | PS1恐怖经典 |
| 2 | 生化危机2 | Capcom | 800MB | PS1恐怖巅峰 |
| 3 | 生化危机3 | Capcom | 600MB | 追迹者篇 |
| 4 | 恶魔城X：月下夜想曲 | Konami | 400MB | 横版动作永恒标杆 |
| 5 | 最终幻想7 | Square Enix | 1GB | 史诗RPG |
| 6 | 最终幻想8 | Square Enix | 1.2GB | Junction系统争议大 |
| 7 | 最终幻想9 | Square Enix | 1GB | 复古RPG |
| 8 | 最终幻想战略版 | Square Enix | 600MB | 战棋RPG |
| 9 | 合金装备 | Konami | 600MB | 潜行动作奠基 |
| 10 | 寄生前夜1 | Square Enix | 600MB | 科幻RPG |
| 11 | 寄生前夜2 | Square Enix | 800MB | 动作化转型，评价低于1 |
| 12 | 放浪冒险谭 | Square | 1GB | 门槛极高、晦涩 |
| 13 | 异度装甲 | Enix | 1.2GB | 后半剧情被砍 |
| 14 | 三国志5 | Koei | 400MB | 光荣战略 |
| 15 | 三国志6 | Koei | 600MB | 光荣战略 |
| 16 | 三国志7 | Koei | 800MB | 光荣Koei战略，PS1版为3D化版本 |
| 17 | 信长之野望：将星录 | Koei | 600MB | 光荣战略 |
| 18 | 信长之野望：烈风传 | Koei | 600MB | 光荣战略 |
| 19 | 超级机器人大战α | Bandai | 800MB | 机战PS1 |
| 20 | 超级机器人大战α外传 | Bandai | 800MB | 机战PS1续作 |
| 21 | 超级机器人大战第2次 | Bandai | 600MB | PS1复刻版 |
| 22 | 大战略 | Atlus | 400MB | 战略模拟 |
| 23 | 前线任务3 | Square | 800MB | 机甲战略 |
| 24 | 皇家骑士团2 | Square | 800MB | PS1重制版 |
| 25 | Medal of Honor | — | 400MB | 荣誉勋章 |
| 26 | Medal of Honor: Underground | — | 400MB | 续作 |
| 27 | Panzer General | MicroProse | 400MB | 装甲将军 |
| 28 | Allied General | MicroProse | 400MB | 同盟将军 |
| 29 | 寂静岭1 | Konami | 800MB | 心理恐怖 |
| 30 | 寂静岭2 | Konami | 1GB | 心理恐怖巅峰 |
| 31 | 恐龙危机1 | Capcom | 600MB | CAPCOM动作 |
| 32 | 恐龙危机2 | Capcom | 800MB | 续作 |
| 33 | 北欧女神Valkyrie Profile | Square | 800MB | 动作RPG |
| 34 | 格兰蒂亚 | ASCII | 800MB | RPG |
| 35 | 幻想水浒传1 | Konami | 800MB | RPG |
| 36 | 幻想水浒传2 | Konami | 1GB | RPG续作 |
| 37 | 时空之轮Chrono Cross | Square | 1GB | RPG |
| 38 | 星海传说2 | Koei | 800MB | RPG |
| 39 | 龙骑士传说Legend of Dragoon | Bandai | 600MB | RPG |
| 40 | 宿命传说 | Namco | 800MB | 传说系列 |
| 41 | 永恒传说Eternia | Namco | 800MB | 传说系列 |
| 42 | 武藏传Brave Fencer Musashi | Square | 600MB | 动作RPG |
| 43 | 露娜银星故事 | Game Arts | 400MB | RPG |
| 44 | 露娜永恒之蓝 | Game Arts | 600MB | 续作 |
| 45 | Wild Arms 1 | Media Works | 600MB | RPG |
| 46 | Wild Arms 2 | Media Works | 800MB | 续作 |
| 47 | 波波罗克罗伊斯 | Sony | 600MB | RPG |
| 48 | 钟楼Clock Tower | Hudson Soft | 400MB | 恐怖冒险 |
| 49 | 古惑狼1-3 | Activision | 1.2GB | 动作合集 |
| 50 | 小龙斯派罗1-3 | Activision | 800MB | 动作合集 |
| 51 | 铁拳3 | Namco | 600MB | 格斗 |
| 52 | 山脊赛车Type 4 | Namco | 400MB | 赛车 |
| 53 | GT赛车1 | Sony | 600MB | 赛车模拟 |
| 54 | GT赛车2 | Sony | 800MB | 赛车模拟续作 |
| 55 | 古墓丽影1-3 | Eidos | 800MB | 冒险动作 |
| 56 | 吊索奇兵Syphon Filter | Sony | 600MB | 射击 |
| 57 | 捉猴啦Ape Escape | Sony | 400MB | 休闲动作 |
| 58 | PaRappa | Sony | 200MB | 音游先驱 |
| 59 | Vib-Ribbon | Sony | 200MB | 音游 |
| 60 | 实况足球WEP系列 | Konami | 600MB | 足球 |
| 61 | DDR/beatmania/太鼓达人 | Konami | 400MB | 音游三件套 |
| 62 | 恶魔城Chronicle | Konami | 600MB | 恶魔城合集 |
| 63 | Persona 1 | Atlus | 600MB | 人格面具 |
| 64 | Persona 2：Innocent Sin | Atlus | 800MB | 续作 |
| 65 | Persona 2：Eternal Punishment | Atlus | 800MB | 续作 |
| 66 | 真女神转生1 | Atlus | 600MB | 女神转生 |
| 67 | 真女神转生2 | Atlus | 600MB | 续作 |
| 68 | 真女神转生if... | Atlus | 800MB | 外传 |
| 69 | 数码宝贝世界1 | Bandai | 600MB | 数码宝贝RPG |
| 70 | 数码宝贝世界2 | Bandai | 800MB | 续作 |
| 71 | 数码宝贝世界3 | Bandai | 800MB | 终章 |
| 72 | 高达系列（基连野望等） | Bandai | 600MB | 高达战略多作 |
| 73 | 龙珠Final Bout | Bandai | 400MB | 龙珠格斗 |
| 74 | 仙剑奇侠传 | Softstar | 600MB | PS1移植版 |
| 75 | 大富翁4 | Softstar | 400MB | 派对游戏 |
| 76 | 同级生2/下级生/To Heart | — | 600MB | 恋爱模拟 |
| 77 | 心跳回忆1/2 | Konami | 600MB | 恋爱模拟 |
| 78 | 前线任务Alternative | Square | 600MB | 机甲战略 |
| 79 | Vandal Hearts | Konami | 600MB | 战棋RPG |
| 80 | Panzer Front | Avalon Hill | 400MB | 坦克模拟 |
| 81 | 文明 | MicroProse | 400MB | 战略 |

---

## 专题系列图鉴

> 按游戏系列/IP组织，按发行时间从早到晚排列各代作品，标注平台、发行方、发行年份及版本间关系。
> 最后附"清单索引"标注该系列游戏在本文档各平台章节中的位置，方便查漏补缺。

---

### 马力欧系列 (Mario)

**系列简介**：任天堂最具代表性的IP，始于1981年《大金刚》。主角马力欧（马里奥）从建筑师变为水管工，再变为太空冒险家。涵盖平台跳跃、赛车、RPG、派对游戏、体育等子类型，是游戏史上销量最高的系列之一。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 大金刚 | NES/FC | Nintendo | 1983 | 马力欧始祖，街机移植 |
| 2 | 马里奥兄弟 | NES/FC | Nintendo | 1983 | 街机移植，与#1超级马力欧兄弟是不同的游戏 |
| 3 | 超级马力欧兄弟 | NES/FC | Nintendo | 1985 | FC开山之作，平台跳跃游戏奠基 |
| 4 | 超级马力欧兄弟2 | NES/FC | Nintendo | 1988 | 海外版DokiDoki续作改 |
| 5 | 超级马力欧兄弟3 | NES/FC | Nintendo | 1988 | FC巅峰之一，道具系统成熟 |
| 6 | 超级马力欧USA | NES/FC | Nintendo | 1992 | 日版超级马力欧兄弟3改 |
| 7 | 超级马力欧世界 | SNES/SFC | Nintendo | 1990 | SFC旗舰马力欧，耀西首登场 |
| 8 | 超级马力欧世界2：耀西岛 | SNES/SFC | Nintendo | 1995 | 耀西独立作品始祖 |
| 9 | 超级马力欧RPG | SNES/SFC | Square | 1996 | 马力欧+勇者斗恶龙风格RPG，Square制作 |
| 10 | 超级马力欧Advance 1 | GBA | Nintendo | 2001 | GB版超级马力欧兄弟重制 |
| 11 | 超级马力欧Advance 2：耀西岛 | GBA | Nintendo | 2002 | GBA耀西岛 |
| 12 | 超级马力欧Advance 3 | GBA | Nintendo | 2004 | GBA耀西岛续作 |
| 13 | 超级马力欧Advance 4 | GBA | Nintendo | 2004 | GBA马力欧续作 |
| 14 | 马力欧与路易吉RPG | GBA | Nintendo | 2003 | GBA角色扮演，独特时停系统 |
| 15 | 超级马力欧64 | N64 | Nintendo | 1996 | 3D动作跳跃开山鼻祖 |
| 16 | 超级马力欧64 DS | NDS | Nintendo | 2004 | N64移植+新内容 |
| 17 | 新超级马力欧兄弟 | NDS | Nintendo | 2006 | NDS马力欧，回归2D |
| 18 | 超级马力欧卡丁车 | SNES/SFC | Nintendo | 1992 | 马力欧卡丁车首作 |
| 19 | 马力欧卡丁车64 | N64 | Nintendo | 1996 | 经典联机赛车 |
| 20 | 马里奥赛车DS | NDS | Nintendo | 2005 | NDS赛车 |
| 21 | 马里奥派对1/2/3 | N64 | Nintendo | 1998-2000 | 派对游戏合集 |
| 22 | 马里奥网球64 | N64 | Nintendo | 1998 | N64网球 |
| 23 | 马里奥高尔夫64 | N64 | Nintendo | 1999 | N64高尔夫 |
| 24 | 马里奥高尔夫Advance | GBA | Nintendo | 2001 | GBA高尔夫 |
| 25 | 马里奥网球Advance | GBA | Nintendo | 2001 | GBA网球 |
| 26 | 瓦力欧制造 | GBA | Nintendo | 2000 | GBA小游戏合集 |
| 27 | 瓦力欧大陆Advance 4 | GBA | Nintendo | 2001 | GBA瓦力欧冒险 |
| 28 | 瓦力欧乐园 | GB/GBC | Nintendo | 1990 | GB瓦力欧 |
| 29 | 瓦力欧乐园3 | GB/GBC | Nintendo | 1998 | GBC续作 |
| 30 | 星之卡比：镜之大迷宫 | GBA | Nintendo | 2004 | GBA卡比 |
| 31 | 星之卡比梦之泉DX | GB/GBC | Nintendo | 1997 | GBC卡比 |
| 32 | 星之卡比64 | N64 | Nintendo | 2000 | N64卡比 |
| 33 | 星之卡比：毛线传说 | NDS | Nintendo | 2008 | NDS卡比 |
| 34 | 耀西岛DS | NDS | Nintendo | 2007 | NDS耀西 |
| 35 | 超级马力欧3D世界+狂怒世界 | Switch | Nintendo | 2013 | (本文档未收录) |

**版本关系说明**：马力欧平台跳跃主线为FC初代→SFC超级世界→GBA Advance系列→N64 3D化→NDS回归2D。RPG支线始于SFC《超级马力欧RPG》(Square制作)，GBA有《马力欧与路易吉RPG》系列。卡比系列独立于马力欧主线，但常捆绑发行。

**清单索引**：见 NES/FC 章 #1,#87-#90 / SNES/SFC 章 #1-#3 / GBA 章 #16-#19,#28-#33 / N64 章 #3,#10,#14-#16,#25-#28 / NDS 章 #12-#13,#43-#45 / GB/GBC 章 #3-#6,#10

---

### 塞尔达传说系列 (The Legend of Zelda)

**系列简介**：任天堂史诗级冒险RPG系列，始于1986年FC《塞尔达传说》。主角林克拯救海拉鲁王国和公主塞尔达，探索迷宫、解谜、战斗。系列定义了动作冒险游戏类型，3D化作品（时之笛）被誉为游戏史最高分作品。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 塞尔达传说 | NES/FC | Nintendo | 1986 | FC时代神作，系列始祖 |
| 2 | 塞尔达传说2：林克的冒险 | NES/FC | Nintendo | 1987 | 横版动作混合，爱恨两极 |
| 3 | 塞尔达传说：众神的三角力量 | SNES/SFC | Nintendo | 1991 | SFC塞尔达，3D化先驱 |
| 4 | 塞尔达传说：织梦岛 | GB/GBC | Nintendo | 1993 | GB经典，梦幻风格 |
| 5 | 塞尔达传说：织梦岛DX | GB/GBC | Nintendo | 1998 | GBC彩色重制 |
| 6 | 塞尔达传说：时之笛 | N64 | Nintendo | 1998 | 游戏史第一个满分神作，3D Zelda标杆 |
| 7 | 塞尔达传说：姆吉拉的假面 | N64 | Nintendo | 2000 | N64续作，暗黑风格，时间循环机制 |
| 8 | 塞尔达传说：缩小帽 | GBA | Nintendo | 2004 | GBA塞尔达，缩小机制创意十足 |
| 9 | 塞尔达传说：幻影沙钟 | NDS | Nintendo | 2004 | NDS塞尔达，触摸操作 |
| 10 | 塞尔达传说：大地的汽笛 | NDS | Nintendo | 2006 | NDS塞尔达续作，飞空鼠机制 |
| 11 | 塞尔达传说：时空之章 | GB/GBC | Nintendo | 2001 | GBC Oracle双作之一 |
| 12 | 塞尔达传说：大地之章 | GB/GBC | Nintendo | 2001 | GBC Oracle双作之二 |

**版本关系说明**：FC两代奠定系列基础→SFC众神三角力量回归探索→N64时之笛定义3D Zelda→NDS双作分别创新触摸和陀螺仪操作。GBA缩小帽是GBA时代塞尔达的独立作品。Oracle双作剧情相连，分别对应时间线和精神之剑。

**清单索引**：见 NES/FC 章 #5-#6 / SNES/SFC 章 #4 / GB/GBC 章 #1-#2,#20-#21 / N64 章 #1-#2 / GBA 章 #45 / NDS 章 #14-#15

---

### 宝可梦系列 (Pokemon)

**系列简介**：Game Freak开发、Nintendo发行的全球现象级RPG系列，始于1996年GB《宝可梦红/绿》。核心玩法：捕捉、培养、对战宝可梦。涵盖正传RPG、复刻、迷宫探险、护林员、卡片游戏等衍生作。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 宝可梦红/绿/蓝/黄 | GB/GBC | Nintendo | 1996 | GB初代，关都地区，系列起点 |
| 2 | 宝可梦金/银/水晶 | GB/GBC | Nintendo | 1999 | GB续作，引入时间系统、双地区 |
| 3 | 宝可梦火红/叶绿 | GBA | Nintendo | 2004 | GBA复刻红/绿，关都再冒险 |
| 4 | 宝可梦绿宝石 | GBA | Nintendo | 2004 | GBA三圣柱终章，丰缘地区 |
| 5 | 宝可梦心金/魂银 | NDS | Nintendo | 2010 | 复刻天花板，金/银HD重制 |
| 6 | 宝可梦白金 | NDS | Nintendo | 2008 | NDS DP续作，洗翠地区 |
| 7 | 宝可梦黑/白1 | NDS | Nintendo | 2010 | NDS黑白篇上，合众地区 |
| 8 | 宝可梦黑/白2 | NDS | Nintendo | 2012 | NDS黑白篇下 |
| 9 | 宝可梦竞技场1 | N64 | Nintendo | 1998 | N64对战 |
| 10 | 宝可梦竞技场2 | N64 | Nintendo | 2000 | N64续作 |
| 11 | 宝可梦皮卡丘 | N64 | Nintendo | 2000 | N64精灵收集 |
| 12 | 宝可梦快照 | N64 | Nintendo | 2000 | N64拍照 |
| 13 | 宝可梦谜题联盟 | N64 | Nintendo | 2001 | N64谜题 |
| 14 | 宝可梦卡片GB | GB/GBC | Nintendo | 1998 | GB卡牌 |
| 15 | 宝可梦不可思议迷宫：赤救助队 | NDS | Nintendo | 2005 | NDS迷宫 |
| 16 | 宝可梦不可思议迷宫：青救助队 | NDS | Nintendo | 2005 | NDS续作 |
| 17 | 宝可梦不可思议迷宫：时之探险队 | NDS | Nintendo | 2006 | NDS续作 |
| 18 | 宝可梦不可思议迷宫：暗之探险队 | NDS | Nintendo | 2006 | NDS续作 |
| 19 | 宝可梦不可思议迷宫：空之探险队 | NDS | Nintendo | 2007 | NDS终章 |
| 20 | 宝可梦护林员 | NDS | Nintendo | 2006 | NDS宝可梦衍生作 |
| 21 | 重装机兵 | NES/FC | Crea-Tech | 1991 | FC机甲RPG，中文圈神作（非宝可梦但常被混淆） |

**版本关系说明**：GB初代→金银（时间系统创新）→GBA火红叶绿（复刻）→绿宝石（新地区）→NDS心金魂银（复刻天花板）→黑白（新世代）。迷宫系列为独立衍生线，护林员也是独立作品。

**清单索引**：见 GB/GBC 章 #7-#8,#39 / GBA 章 #2-#4 / NDS 章 #1-#4,#56-#61 / N64 章 #17-#21

---

### 洛克人系列 (Mega Man)

**系列简介**：Capcom经典动作游戏系列，始于1987年FC《洛克人》。主角洛克人对抗威利博士，继承八大头目能力。涵盖FC正统、X系列（高速动作）、Zero系列（暗黑风格）、EXE系列（网络对战RPG）等多条支线。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 洛克人 | NES/FC | Capcom | 1987 | FC初代，粗糙但经典，建议从2入门 |
| 2 | 洛克人2 | NES/FC | Capcom | 1988 | 系列真正起点，系统完善 |
| 3 | 洛克人3 | NES/FC | Capcom | 1990 | 博士大战威利博士 |
| 4 | 洛克人4 | NES/FC | Capcom | 1991 | 拉什装甲系统引入 |
| 5 | 洛克人5 | NES/FC | Capcom | 1992 | 宇宙篇 |
| 6 | 洛克人6 | NES/FC | Capcom | 1993 | FC洛克人终章 |
| 7 | 洛克人X | SNES/SFC | Capcom | 1993 | X系列首作，3D化前最后2D作品 |
| 8 | 洛克人X2 | SNES/SFC | Capcom | 1994 | X系列续作 |
| 9 | 洛克人X3 | SNES/SFC | Capcom | 1995 | X系列SFC终章 |
| 10 | 洛克人Zero 1 | GBA | Capcom | 2002 | GBA洛克人，暗黑风格重启 |
| 11 | 洛克人Zero 2 | GBA | Capcom | 2003 | 续作 |
| 12 | 洛克人Zero 3 | GBA | Capcom | 2004 | 续作 |
| 13 | 洛克人Zero 4 | GBA | Capcom | 2005 | GBA终章 |
| 14 | 洛克人EXE | GBA | Capcom | 2002 | GBA对战RPG，网络传说 |
| 15 | 洛克人EXE2 | GBA | Capcom | 2003 | 续作 |
| 16 | 洛克人EXE3 | GBA | Capcom | 2004 | 续作 |
| 17 | 洛克人世界1 | GB/GBC | Capcom | 1991 | GB洛克人 |
| 18 | 洛克人世界2 | GB/GBC | Capcom | 1992 | 续作 |
| 19 | 洛克人世界3 | GB/GBC | Capcom | 1993 | 续作 |
| 20 | 洛克人世界4 | GB/GBC | Capcom | 1994 | 续作 |
| 21 | 洛克人世界5 | GB/GBC | Capcom | 1996 | GB洛克人终章 |
| 22 | 洛克人7 | SNES/SFC | Capcom | 1996 | SFC洛克人，系列转折 |
| 23 | 洛克人ZX | NDS | Capcom | 2006 | NDS洛克人 |
| 24 | 洛克人ZX Advent | NDS | Capcom | 2007 | NDS续作 |
| 25 | 洛克人：战争传奇 | 其他 | Capcom | 2021 | (本文档未收录) |

**版本关系说明**：FC正统6代→X系列(SFC，高速动作)→Zero系列(GBA，暗黑重启)→EXE系列(GBA，网络RPG)→世界系列(GB，经典回归)。X和Zero系列共享世界观但时间线不同。

**清单索引**：见 NES/FC 章 #7-#12 / SNES/SFC 章 #35-#37,#50 / GBA 章 #21-#27 / GB/GBC 章 #11-#15 / NDS 章 #46-#47

---

### 恶魔城系列 (Castlevania)

**系列简介**：Konami经典动作游戏系列，始于1986年FC《恶魔城》。主角贝尔蒙特家族对抗德古拉伯爵，横版动作+银河恶魔城探索。系列横跨多个平台世代，风格从暗黑哥特到奇幻冒险不断变化。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 恶魔城 | NES/FC | Konami | 1986 | FC恶魔城初代 |
| 2 | 恶魔城2：诅咒之月 | NES/FC | Konami | 1987 | FC续作 |
| 3 | 恶魔城3：德拉库拉的诅咒 | NES/FC | Konami | 1988 | FC恶魔城巅峰 |
| 4 | 恶魔城X：血之轮回 | SNES/SFC | Konami | 1994 | SFC恶魔城，CD版为月下前身 |
| 5 | 恶魔城X：月下夜想曲 | PS1 | Konami | 1997 | 横版动作永恒标杆，系列巅峰 |
| 6 | 恶魔城：德古拉传说1 | GB/GBC | Konami | 1995 | GBC恶魔城 |
| 7 | 恶魔城：德古拉传说2 | GB/GBC | Konami | 1997 | GBC续作 |
| 8 | 恶魔城：晓月圆舞曲 | GBA | Konami | 2002 | GBA恶魔城第一神作 |
| 9 | 恶魔城：白夜协奏曲 | GBA | Konami | 2003 | GBA恶魔城 |
| 10 | 恶魔城：月轮 | GBA | Konami | 2003 | GBA恶魔城 |
| 11 | 恶魔城：苍月的十字架 | NDS | Konami | 2005 | NDS恶魔城 |
| 12 | 恶魔城：废墟的肖像 | NDS | Konami | 2006 | NDS续作 |
| 13 | 恶魔城：被夺走的刻印 | NDS | Konami | 2008 | NDS终章 |
| 14 | 恶魔城Chronicle | PS1 | Konami | 2000 | PS1恶魔城合集 |

**版本关系说明**：FC三作奠定基调→SFC血之轮回(CD版)→PS1月下夜想曲(系列巅峰)→GBA三作(晓月/白夜/月轮)→NDS三作(苍月/废墟/刻印)。月下夜想曲定义了"银河恶魔城"类型。

**清单索引**：见 NES/FC 章 #45-#47 / SNES/SFC 章 #34 / PS1 章 #4 / GB/GBC 章 #22-#25 / GBA 章 #10-#12 / NDS 章 #16-#18

---

### 火焰之纹章系列 (Fire Emblem)

**系列简介**：Intelligent Systems开发、Nintendo发行的战棋RPG系列，始于1990年SFC《火焰之纹章：暗黑龙与光之剑》。特色：永久死亡系统、角色养成、网格战棋。系列在西方知名度较低，但在日本是经典战棋IP。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 火焰之纹章：暗黑龙与光之剑 | SNES/SFC | Nintendo | 1992 | SFC初代(日版)，系列奠基 |
| 2 | 火焰之纹章：纹章之谜 | SNES/SFC | Nintendo | 1994 | SFC战棋奠基，上下两部 |
| 3 | 火焰之纹章：圣战之系谱 | SNES/SFC | Nintendo | 1996 | 史诗战棋巨作，两代叙事 |
| 4 | 火焰之纹章：多拉基亚776 | SNES/SFC | Nintendo | 1999 | 硬核战棋，系谱续作 |
| 5 | 火焰之纹章：封印之剑 | GBA | Nintendo | 2002 | GBA火纹，新系列始动篇 |
| 6 | 火焰之纹章：烈火之剑 | GBA | Nintendo | 2003 | GBA火纹，前传性质 |
| 7 | 火焰之纹章：圣魔之光石 | GBA | Nintendo | 2004 | GBA火纹终章 |
| 8 | 火焰之纹章：新·暗黑龙与光之剑 | NDS | Nintendo | 2008 | NDS火纹重制 |
| 9 | 火焰之纹章：新·纹章之谜 | NDS | Nintendo | 2009 | NDS火纹重制 |

**版本关系说明**：SFC三作(暗黑龙/纹章之谜/系谱)奠定系列基础→GBA三作(封印/烈火/圣魔)构成新三部曲→NDS两作为重制版。纹章之谜包含古代战记(前传)和英雄战记(正传)。

**清单索引**：见 SNES/SFC 章 #12-#14 / GBA 章 #7-#9 / NDS 章 #24-#25

---

### 最终幻想系列 (Final Fantasy)

**系列简介**：Square(现Square Enix)史诗级RPG系列，始于1987年FC《最终幻想》。每代作品独立世界观，涵盖回合制、ATB、动作等战斗系统演变。从2D像素到3D图形，系列定义了日式RPG类型。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 最终幻想 | NES/FC | Square Enix | 1987 | FC系列初代，古老但奠基 |
| 2 | 最终幻想2 | NES/FC | Square Enix | 1988 | 职业系统先驱 |
| 3 | 最终幻想3 | NES/FC | Square Enix | 1990 | DS重制更优，FC版有历史价值 |
| 4 | 最终幻想4 | SNES/SFC | Square | 1991 | FF系列转折作，ATB系统引入 |
| 5 | 最终幻想4 Advance | GBA | Square Enix | 2005 | GBA移植(含额外内容) |
| 6 | 最终幻想4(DS重制版) | NDS | Square Enix | 2007 | NDS完全重制 |
| 7 | 最终幻想5 | SNES/SFC | Square Enix | 1992 | 职业系统巅峰 |
| 8 | 最终幻想5 Advance | GBA | Square Enix | 2005 | GBA移植 |
| 9 | 最终幻想6 | SNES/SFC | Square Enix | 1994 | FF 2D巅峰，群像剧 |
| 10 | 最终幻想6 Advance | GBA | Square Enix | 2005 | GBA移植 |
| 11 | 最终幻想7 | PS1 | Square Enix | 1997 | 史诗RPG，系列最著名作品 |
| 12 | 最终幻想8 | PS1 | Square Enix | 1999 | Junction系统争议大 |
| 13 | 最终幻想9 | PS1 | Square Enix | 2000 | 复古RPG，回归系列根源 |
| 14 | 最终幻想战略版 | PS1 | Square Enix | 1997 | 战棋RPG |
| 15 | 最终幻想战略版Advance | GBA | Square Enix | 2003 | GBA战棋RPG |
| 16 | 最终幻想战略版：狮子战争 | PSP | Square Enix | 2007 | PSP独占，PS1版增强 |
| 17 | 最终幻想7：核心危机 | PSP | Square Enix | 2007 | FF7前传 |
| 18 | 最终幻想4/5/6(PSP移植) | PSP | Square Enix | 2007-2008 | PSP经典移植 |
| 19 | 最终幻想战略版Advance | GBA | Square Enix | 2003 | GBA战棋RPG |

**版本关系说明**：FC三作(1-3)为早期回合制→SFC4-6为2D巅峰期→PS1 7-9为3D化史诗期→衍生战棋系列独立发展。核心正传每代独立世界观，剧情不连续。

**清单索引**：见 NES/FC 章 #28-#30 / SNES/SFC 章 #7-#9 / PS1 章 #5-#7-#8 / GBA 章 #31-#33 / NDS 章 #50-#51 / PSP 章 #10,#18

---

### 逆转裁判系列 (Ace Attorney)

**系列简介**：Capcom原创法庭冒险游戏系列，始于2001年GBA《逆转裁判1》。主角成步堂龙一作为辩护律师在法庭上反驳证人、寻找真相。以独特演出、精彩剧情和幽默台词著称。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 逆转裁判1 | GBA | Capcom | 2001 | GBA神级剧情，系列起点 |
| 2 | 逆转裁判2 | GBA | Capcom | 2002 | GBA续作 |
| 3 | 逆转裁判3 | GBA | Capcom | 2004 | GBA系列终章 |
| 4 | 逆转裁判123(DS版) | NDS | Capcom | 2007 | NDS复刻版，高清化+新内容 |
| 5 | 逆转检事1 | NDS | Capcom | 2009 | NDS检事篇，主角换为御剑怜侍 |
| 6 | 逆转检事2 | NDS | Capcom | 2011 | NDS续作 |
| 7 | 幽灵诡计Ghost Trick | NDS | Capcom | 2010 | NDS神作，剧情封神，非逆转但同作者 |

**版本关系说明**：GBA三作构成成步堂篇三部曲→NDS复刻版HD重制+新增章节→逆转检事系列为衍生前传，主角换为检事御剑→幽灵诡计为同一创作者另作，非逆转正传但风格相似。

**清单索引**：见 GBA 章 #13-#15 / NDS 章 #5-#8

---

### 拳皇系列 (King of Fighters)

**系列简介**：SNK经典2D格斗游戏系列，始于1994年NeoGeo《拳皇94》。汇聚SNK旗下各游戏角色(饿狼传说、侍魂、阿修罗之怒等)进行大乱斗。以三人组队对战、华丽连招和角色设计著称，是国内街机厅绝对王者。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 拳皇94 | NeoGeo/街机 | SNK | 1994 | 系列初代，三人组队制开创 |
| 2 | 拳皇95 | NeoGeo/街机 | SNK | 1995 | 续作 |
| 3 | 拳皇96 | NeoGeo/街机 | SNK | 1996 | 续作 |
| 4 | 拳皇97 | NeoGeo/街机 | SNK | 1997 | 国内人气王，角色平衡经典 |
| 5 | 拳皇98 | NeoGeo/街机 | SNK | 1998 | 平衡性神作，无剧情无结局 |
| 6 | 拳皇99 | NeoGeo/街机 | SNK | 1999 | 系统大改，防御系统引入 |
| 7 | 拳皇2000 | NeoGeo/街机 | SNK | 2000 | 续作 |
| 8 | 拳皇2001 | NeoGeo/街机 | SNK | 2001 | 续作 |
| 9 | 拳皇2002 | NeoGeo/街机 | SNK | 2002 | 回归原点，粉丝最推崇一作 |
| 10 | 拳皇2003 | NeoGeo/街机 | SNK | 2003 | SNK末期作品，系统成熟 |

**版本关系说明**：94-99为NESTS篇三部曲→2000-2001为NESTS篇终章→2002回归无剧情大乱斗→2003为SNK NeoGeo末期作品。97和98是国内街机厅最热门版本。

**清单索引**：见 街机(FBNeo/MAME) 章 #29-#38

---

### 侍魂/月华剑士系列 (Samurai Shodown / Samurai Spirits)

**系列简介**：SNK经典刀剑格斗游戏系列，以武士为题材，强调一击必杀、读心博弈和独特角色设计。侍魂系列注重节奏和策略，月华剑士系列则加快了节奏。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 侍魂1 | NeoGeo/街机 | SNK | 1993 | 系列初代 |
| 2 | 真侍魂：霸王丸地狱变 | NeoGeo/街机 | SNK | 1994 | 系列首作加强版 |
| 3 | 侍魂2 | NeoGeo/街机 | SNK | 1994 | 续作 |
| 4 | 侍魂3 | NeoGeo/街机 | SNK | 1995 | 续作 |
| 5 | 侍魂4 | NeoGeo/街机 | SNK | 1996 | 续作 |
| 6 | 侍魂天草降临 | NeoGeo/街机 | SNK | 2003 | NeoGeo末期作品 |
| 7 | 侍魂零 | NeoGeo/街机 | SNK | 2002 | NeoGeo末期 |
| 8 | 月华剑士1 | NeoGeo/街机 | SNK | 1997 | 侍魂外传，节奏加快 |
| 9 | 月华剑士2 | NeoGeo/街机 | SNK | 1998 | 月华续作，系列巅峰 |

**版本关系说明**：侍魂1-4为正传系列→天草降临和零为NeoGeo末期作品→月华剑士1-2为衍生系列，节奏更快、系统更成熟。月华剑士2被认为是SNK格斗游戏设计巅峰。

**清单索引**：见 街机(FBNeo/MAME) 章 #39-#47

---

### 街头霸王系列 (Street Fighter)

**系列简介**：Capcom格斗游戏帝王系列，始于1987年街机《街头霸王》。1991年《街头霸王2》奠定2D格斗游戏标准，后续不断进化。是全球最知名的格斗游戏IP。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 街头霸王2 | NeoGeo/街机 | Capcom | 1991 | 格斗游戏奠基作 |
| 2 | 街头霸王2 Hyper Fighting | NeoGeo/街机 | Capcom | 1992 | 初代加强版 |
| 3 | 街头霸王2 Super Turbo | NeoGeo/街机 | Capcom | 1992 | 最终加强版 |
| 4 | 少年街霸Alpha 1 | NeoGeo/街机 | Capcom | 1995 | 街霸前传，Q版角色 |
| 5 | 少年街霸Alpha 2 | NeoGeo/街机 | Capcom | 1996 | 续作 |
| 6 | 少年街霸Alpha 3 | NeoGeo/街机 | Capcom | 1998 | Alpha终章 |
| 7 | 街头霸王III New Generation | NeoGeo/街机 | Capcom | 1997 | 3D绘图2D玩法 |
| 8 | 街头霸王III 2nd Impact | NeoGeo/街机 | Capcom | 1997 | 续作 |
| 9 | 街头霸王III 三度冲击 | NeoGeo/街机 | Capcom | 1998 | 系列巅峰，系统最成熟 |
| 10 | 街头霸王2 Turbo | SNES/SFC | Capcom | 1993 | SFC移植版 |
| 11 | 街头霸王2 Special Champion Edition | MD/Genesis | Capcom | 1993 | MD移植版 |

**版本关系说明**：SF2初代→Hyper→Super Turbo为经典升级链→Alpha系列为前传外传→SF3系列为3D化新纪元→三度冲击被认为是2D格斗游戏设计巅峰。

**清单索引**：见 SNES/SFC 章 #38-#39 / MD/Genesis 章 #33 / 街机(FBNeo/MAME) 章 #63-#71

---

### 机器人大战/超级机器人大战系列 (Super Robot Wars)

**系列简介**：Banpresto(现Bandai Namco)开发的战棋RPG系列，汇聚多部机器人动画作品角色和机体进行跨界大战。以原创剧情融合多部作品、参战机体收集、角色育成系统著称。是机器人大战题材的绝对代表。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 超级机器人大战3 | SNES/SFC | Bandai | 1993 | SFC机战系列化起点 |
| 2 | 超级机器人大战EX | SNES/SFC | Bandai | 1994 | SFC机战，原创主角线 |
| 3 | 超级机器人大战第4次 | SNES/SFC | Bandai | 1994 | SFC机战，剧情高潮 |
| 4 | 超级机器人大战Gaiden | SNES/SFC | Bandai | 1995 | SFC机战外传 |
| 5 | 超级机器人大战α | PS1 | Bandai | 2000 | PS1机战重启，原创剧情 |
| 6 | 超级机器人大战α外传 | PS1 | Bandai | 2001 | PS1机战续作 |
| 7 | 超级机器人大战第2次 | PS1 | Bandai | 1999 | PS1复刻版(原FC) |
| 8 | 机器人大战A | GBA | Bandai | 2001 | GBA机战 |
| 9 | 机器人大战R | GBA | Bandai | 2002 | GBA机战 |
| 10 | 机器人大战D | GBA | Bandai | 2003 | GBA机战 |
| 11 | 机器人大战J | GBA | Bandai | 2004 | GBA机战 |
| 12 | Original Generation 1 | GBA | Bandai | 2002 | GBA机战原创系列始动 |
| 13 | Original Generation 2 | GBA | Bandai | 2003 | GBA原创续作 |
| 14 | 机器人大战W | NDS | Bandai | 2007 | NDS机战，双机操作 |
| 15 | 机器人大战K | NDS | Bandai | 2008 | NDS机战 |
| 16 | 机器人大战L | NDS | Bandai | 2010 | NDS机战收官作 |
| 17 | 机器人大战A Portable | PSP | Bandai | 2009 | PSP机战 |

**版本关系说明**：SFC早期作品(3/EX/4次/Gaiden)为经典早期系列→PS1 α三部曲为重启之作→GBA原创系列(OG1/2)为独立世界观→NDS三代(W/K/L)为NDS收官→PSP移植W。

**清单索引**：见 SNES/SFC 章 #19-#22 / PS1 章 #19-#21 / GBA 章 #39-#44 / NDS 章 #28-#30 / PSP 章 #19

---

### 大航海时代系列 (Uncharted Seas)

**系列简介**：Koei(现Koei Tecmo)航海模拟RPG系列，玩家扮演航海家探索大航海时代的世界。以自由的航海探索、贸易、战斗和角色养成系统著称。系列在亚洲尤其受欢迎。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 大航海时代2 | SNES/SFC | Koei | 1994 | SFC航海模拟RPG，系列经典 |
| 2 | 大航海时代II | PS1 | Koei | 1999 | PS1版(重制版) |

**版本关系说明**：SFC版为大航海时代2的移植版，PS1版为后续重制。系列正传包括1-5代及外传，本文档收录最经典的二代。

**清单索引**：见 SNES/SFC 章 #26

---

### 重装机兵系列 (Metal Max / Metal Armor)

**系列简介**：Crea-Tech开发的末日题材RPG系列，玩家扮演赏金猎人在废土世界驾驶战车战斗。以自由的地图探索、战车改装和开放式玩法著称。在中文圈有极高人气，被称为"中文圈神作"。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 重装机兵 | NES/FC | Crea-Tech | 1991 | FC机甲RPG，中文圈神作 |
| 2 | 重装机兵2 | SNES/SFC | Crea-Tech | 1993 | SFC续作(重装上阵) |
| 3 | 重装机兵3 | NDS | Crea-Tech | 2009 | NDS正统续作 |
| 4 | 重装机兵：钢之季节 | NDS | Crea-Tech | 2009 | NDS重装机兵2重制 |

**版本关系说明**：FC初代为中文圈经典→SFC二代为系列巅峰→NDS三代为3D化正统续作→钢之季节为二代HD重制版。注意：PS1上没有重装机兵作品。

**清单索引**：见 NES/FC 章 #65 / SNES/SFC (无直接对应，2代为SFC但本文档SFC章未单列) / NDS 章 #26-#27

---

### 生化危机系列 (Resident Evil)

**系列简介**：Capcom经典生存恐怖游戏系列，始于1996年PS1《生化危机》。主角们在被病毒感染的世界中求生、解谜、战斗。以有限的资源管理、固定视角摄像头和恐怖氛围营造著称。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 生化危机1 | PS1 | Capcom | 1996 | PS1恐怖经典，系列始祖 |
| 2 | 生化危机2 | PS1 | Capcom | 1998 | PS1恐怖巅峰，双主角系统 |
| 3 | 生化危机3 | PS1 | Capcom | 1999 | PS1续作，追迹者篇 |
| 4 | 生化危机：代号维罗妮卡 | Dreamcast | Capcom | 2000 | DC版画质最佳，系列重要续作 |
| 5 | 生化危机2 | N64 | Capcom | 2000 | N64移植版，本身是灾难移植 |

**版本关系说明**：PS1三作+维罗妮卡为早期系列主线→N64版生化危机2为移植版（画质和性能差，不推荐）。维罗妮卡原为DC独占，后移植到GC/PS2。

**清单索引**：见 PS1 章 #1-#3 / Dreamcast 章 #7 / N64 章 #9(不推荐)

---

### 合金装备系列 (Metal Gear)

**系列简介**：Kojima Productions(原Konami)开发的潜行动作游戏系列，始于1987年MSX2《合金装备》，PS1版Solid将其推向世界。以潜行玩法、复杂剧情、电影化叙事和哲学讨论著称，是游戏叙事艺术的里程碑。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 合金装备/潜龙谍影 | PS1 | Konami | 1998 | PS1潜行动作奠基作 |
| 2 | 合金装备：和平行者 | PSP | Konami | 2010 | PSP作品，重型但可玩 |

**版本关系说明**：PS1版Metal Gear Solid为系列3D化起点→PSP和平行者为外传性质作品。系列正传后续在PS2/3/4时代继续，但本文档仅收录早期作品。

**清单索引**：见 PS1 章 #9 / PSP 章 #47

---

### 魂斗罗系列 (Contra)

**系列简介**：Konami经典横版射击游戏系列，始于1987年街机《魂斗罗》。主角比尔·雷泽尔和兰斯·比恩在异形世界战斗。以高密度弹幕、双人合作和极高难度著称。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 魂斗罗 | NES/FC | Konami | 1987 | FC经典双人射击 |
| 2 | 魂斗罗2 | NES/FC | Konami | 1988 | FC续作，不如1代 |
| 3 | 魂斗罗精神 Contra III | SNES/SFC | Konami | 1992 | SFC魂斗罗 |
| 4 | 魂斗罗 铁血兵团 | MD/Genesis | Konami | 1994 | MD魂斗罗 |
| 5 | 魂斗罗街机 | 街机 | Konami | 1993 | 街机版 |
| 6 | 超级魂斗罗街机 | 街机 | Konami | 1988 | 街机续作 |

**版本关系说明**：FC初代奠定经典→FC2续作→SFC魂斗罗3为系列高峰→MD铁血兵团为外传→街机版为独立作品。

**清单索引**：见 NES/FC 章 #13-#14 / SNES/SFC 章 #52 / MD/Genesis 章 #28 / 街机(FBNeo/MAME) 章 #110-#111

---

### 双截龙系列 (Double Dragon)

**系列简介**：Technos Japan经典清版动作游戏系列，始于1987年街机《双截龙》。主角比利和吉米·李在街头战斗拯救女友。以双人合作、格斗要素和街头题材定义了清版动作游戏类型。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 双截龙 | NES/FC | Technos | 1988 | FC清版动作奠基 |
| 2 | 双截龙2 | NES/FC | Technos | 1989 | FC续作 |
| 3 | 双截龙3 | NES/FC | Technos | 1990 | 换开发商，手感差 |
| 4 | 双截龙GB | GB/GBC | Technos | 1993 | GB双截龙 |
| 5 | 双截龙1/2/3 | 街机 | Technos | 1987-1989 | 街机原版 |

**版本关系说明**：街机初代→FC三作(1-3)为经典期→第三部换开发商后质量下滑→GB版为掌机移植。Technos破产后系列由其他公司接手。

**清单索引**：见 NES/FC 章 #35-#37 / GB/GBC 章 #30 / 街机(FBNeo/MAME) 章 #151

---

### 怒之铁拳/战国传承系列 (Streets of Rage / Mad City)

**系列简介**：Sega(原Atlus)经典清版动作游戏系列，始于1991年MD《怒之铁拳》。主角们在城市街头与帮派战斗，以流畅的动作、优秀的配乐和四人合作著称。MD版在中文圈以"怒之铁拳"为名广受欢迎。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 怒之铁拳 | MD/Genesis | Sega | 1991 | MD清版动作初代 |
| 2 | 怒之铁拳2 | MD/Genesis | Sega | 1992 | MD系列巅峰，系统完善 |
| 3 | 怒之铁拳3 | MD/Genesis | Sega | 1994 | MD系列终章，日美版差异大 |
| 4 | 格斗三人组 | MD/Genesis | Sega | 1991 | 怒之铁拳初代盗版译名(与#1重复)，建议只下怒之铁拳 |

**版本关系说明**：MD三作为系列核心作品，2代被公认为清版动作游戏巅峰之一。"格斗三人组"是MD版怒之铁拳初代的国内盗版译名，与#4怒之铁拳为同一游戏，不要重复下载。

**清单索引**：见 MD/Genesis 章 #4-#8

---

> **专题系列图鉴完**
> 以上系列按本文档收录的游戏整理，部分系列有更多作品未收录（如最终幻想10-16、塞尔达时之笛3D重制版等），因超出本文档平台范围而未列入。


---


---

### 三国志系列 (Romance of the Three Kingdoms)

**系列简介**：Koei（现Koei Tecmo）开发的回合制战略模拟系列，始于1985年FC《三国志》。以三国题材为背景，玩家扮演君主进行内政、外交、军事指挥，目标是一统天下。系列以极高的自由度、深厚的历史底蕴和持续的内容迭代，成为中文圈最受欢迎的战略游戏IP之一。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 三国志 | NES/FC | Koei | 1988 | FC战略始祖，系列原点 |
| 2 | 三国志2 | NES/FC | Koei | 1989 | FC续作，系统完善 |
| 3 | 三国志2 | MD/Genesis | Koei | 1992 | MD移植版，画面提升 |
| 4 | 三国志3 | MD/Genesis | Koei | 1993 | MD版，内政系统深化 |
| 5 | 三国志3 | SNES/SFC | Koei | 1994 | SFC移植版 |
| 6 | 三国志4 | SNES/SFC | Koei | 1996 | SFC三国志终章，政治外交系统成熟 |
| 7 | 三国志5 | PS1 | Koei | 1997 | PS1首作，3D化地图，万人规模战争 |
| 8 | 三国志6 | PS1 | Koei | 1999 | PS1续作，武将关系系统 |
| 9 | 三国志7 | PS1 | Koei | 2000 | PS1三国志终章，3D全语音 |
| 10 | 霸王的大陆 | NES/FC | 南晶科技 | 1993 | FC版三国志中文汉化，中文圈经典 |
| 11 | 中原之霸者 | NES/FC | 智冠 | 1994 | FC三国题材策略游戏（正式商业作） |

**版本关系说明**：FC三代为早期经典→SFC四代为2D巅峰→PS1五到七代为3D化转型期。MD版二三代为过渡平台佳作。"霸王的大陆"是南晶科技汉化的FC三国志改版，在中文圈有极高人气。

**清单索引**：见 NES/FC 章 #25-#27 / MD/Genesis 章 #13-#14 / SNES/SFC 章 #27-#29 / PS1 章 #14-#16

---

### 信长之野望系列 (Nobunaga's Ambition)

**系列简介**：Koei（现Koei Tecmo）开发的日本战国题材战略模拟系列，始于1983年。玩家扮演战国大名，通过内政发展、外交策略、军事征服统一日本。与三国志系列同为光荣战略双璧，以细腻的日本战国还原度和深度的政治模拟著称。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 信长之野望：全国版 | MD/Genesis | Koei | 1992 | MD战略，系列早期作品 |
| 2 | 信长之野望：全国版 | SNES/SFC | Koei | 1994 | SFC移植版 |
| 3 | 信长之野望：武将风云录 | SNES/SFC | Koei | 1995 | SFC续作，新增事件 |
| 4 | 信长之野望：霸王传 | SNES/SFC | Koei | 1996 | SFC续作，战争系统强化 |
| 5 | 信长之野望：天翔记 | SNES/SFC | Koei | 1996 | SFC信长终章，系统集大成 |
| 6 | 信长之野望：将星录 | PS1 | Koei | 1999 | PS1战略，3D战场 |
| 7 | 信长之野望：烈风传 | PS1 | Koei | 2000 | PS1续作 |

**版本关系说明**：MD版全国版为系列最早移植到家用机的作品→SFC五代（全国版/武将风云录/霸王传/天翔记）构成SFC信长四部曲→PS1将星录/烈风传为PS1时期作品。天翔记被认为是SFC战略游戏巅峰之一。

**清单索引**：见 MD/Genesis 章 #15 / SNES/SFC 章 #30-#33 / PS1 章 #17-#18

---
---

### 勇者斗恶龙系列 (Dragon Quest)

**系列简介**：Enix（现Square Enix）开发的日本国民级RPG系列，始于1986年FC《勇者斗恶龙》。由堀井雄二担任剧本、鸟山明负责人设、椙山浩一作曲，被称为"日本国民RPG"。系列以回合制战斗、轻松的冒险氛围、感人的剧情和极高的完成度著称，在日本的知名度远超最终幻想。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 勇者斗恶龙 | NES/FC | Enix | 1988 | 日R鼻祖，系列起点 |
| 2 | 勇者斗恶龙2 | NES/FC | Enix | 1988 | 系列续作，三勇者系统 |
| 3 | 勇者斗恶龙3 | NES/FC | Enix | 1990 | 职业系统先驱，自由度极高 |
| 4 | 勇者斗恶龙4 | SNES/SFC | Enix | 1991 | 章节叙事先驱，多主角切换 |
| 5 | 勇者斗恶龙4 | GBA | Square Enix | 2005 | GBA移植版 |
| 6 | 勇者斗恶龙5 | SNES/SFC | Enix | 1992 | SFC名作，父子传承叙事 |
| 7 | 勇者斗恶龙5 | GBA | Square Enix | 2005 | GBA移植版 |
| 8 | 勇者斗恶龙6 | SNES/SFC | Enix | 1995 | 梦境世界RPG，SFC末期巨作 |
| 9 | 勇者斗恶龙6 | GBA | Square Enix | 2005 | GBA移植版 |
| 10 | 勇者斗恶龙4 | NDS | Square Enix | 2007 | NDS完全重制 |
| 11 | 勇者斗恶龙5 | NDS | Square Enix | 2008 | NDS完全重制 |
| 12 | 勇者斗恶龙6 | NDS | Square Enix | 2009 | NDS完全重制 |
| 13 | 勇者斗恶龙9 | NDS | Square Enix | 2009 | NDS原创续作，多人联机 |
| 14 | 勇者斗恶龙怪兽篇Joker 1 | NDS | Square Enix | 2006 | NDS怪兽养成 |
| 15 | 勇者斗恶龙怪兽篇Joker 2 | NDS | Square Enix | 2010 | NDS续作 |

**版本关系说明**：FC三作为早期经典→SFC四到六为2D巅峰期→GBA三作(4/5/6)为GBA移植版→NDS三作(4/5/6)为完全重制→DQ9为NDS原创续作。DQ4的章节叙事结构对后续RPG影响深远。

**清单索引**：见 NES/FC 章 #31-#34 / SNES/SFC 章 #10-#11 / GBA 章 #34-#35 / NDS 章 #19-#22,#54-#55

---

### 银河战士/密特罗德系列 (Metroid)

**系列简介**：Nintendo开发的动作冒险系列，主角萨姆斯·亚兰(Samus Aran)是银河系最危险的赏金猎人。系列开创了"银河恶魔城"(Metroidvania)游戏类型——非线性地图探索、能力解锁驱动进度、隐藏区域探索。以暗黑科幻氛围、孤独感和精妙的关卡设计著称。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 密特罗德 | NES/FC | Nintendo | 1987 | FC动作冒险，系列始祖 |
| 2 | 超级银河战士 | SNES/SFC | Nintendo | 1994 | SFC动作冒险巅峰，银河恶魔城始祖 |
| 3 | 银河战士2 | GB/GBC | Nintendo | 1994 | GB银河战士 |
| 4 | 密特罗德零点任务 | GBA | Nintendo | 2002 | GBA银河战士，FC前传 |
| 5 | 密特罗德融合 | GBA | Nintendo | 2002 | GBA银河恶魔城，续零点任务 |

**版本关系说明**：FC初代奠定探索+能力解锁的核心玩法→SFC超级银河战士将类型推向巅峰→GB银河战士2为系列续作→GBA零点任务为FC前传→GBA融合为萨姆斯故事的重要章节。超级银河战士常年位居各大"史上最佳游戏"榜单前列。

**清单索引**：见 SNES/SFC 章 #5 / GB/GBC 章 #9 / GBA 章 #29-#30

---

### 怪物猎人系列 (Monster Hunter)

**系列简介**：Capcom开发的动作RPG系列，玩家扮演猎人接受讨伐/捕捉怪物的任务，通过战斗获取素材锻造装备，变强后挑战更强大的怪物。以深度的战斗系统、装备驱动循环和多人共斗玩法著称。PSP时代的携带版将系列推向大众。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 怪物猎人携带版2nd G | PSP | Capcom | 2008 | PSP多人共斗，内容扩充版 |
| 2 | 怪物猎人携带版3rd | PSP | Capcom | 2011 | PSP怪物猎人终章，N4100稳30帧 |

**版本关系说明**：携带版2nd G为PSP系列重要作品→3rd为PSP系列终章，也是N4100上表现最好的怪物猎人作品（1x分辨率稳30帧）。系列核心循环"狩猎→刷素材→做装备→挑战更强怪物"影响了整个动作RPG类型。

**清单索引**：见 PSP 章 #1-#2

---

### 英雄传说/轨迹系列 (The Legend of Heroes: Trails)

**系列简介**：Falcom开发的RPG系列，以"塞姆利亚大陆"为舞台，通过多条独立故事线逐步拼凑出完整的世界观。以优秀的剧情演出、细腻的角色塑造和"交信系统"（角色间写信）著称。轨迹系列是PSP平台上最伟大的RPG系列之一。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 英雄传说：空之轨迹FC | PSP | Falcom | 2005 | 轨迹系列起点，利贝尔王国篇上 |
| 2 | 英雄传说：空之轨迹SC | PSP | Falcom | 2006 | 利贝尔王国篇下 |
| 3 | 英雄传说：空之轨迹 the 3rd | PSP | Falcom | 2007 | 空之轨迹终章 |
| 4 | 英雄传说：零之轨迹 | PSP | Falcom | 2010 | 轨迹新篇，克洛斯贝尔篇上 |
| 5 | 英雄传说：碧之轨迹 | PSP | Falcom | 2011 | 克洛斯贝尔篇下 |
| 6 | 英雄传说：那由多之轨迹 | PSP | Falcom | 2012 | 轨迹外传，独立故事 |
| 7 | 英雄传说：卡卡布三部曲 | PSP | Falcom | 2006-2007 | 白发魔女/朱红之泪/海之槛歌 |

**版本关系说明**：空之轨迹三部曲(FC/SC/3rd)为系列起点→零之轨迹/碧之轨迹为时间线前传但独立故事→那由多之轨迹为另一条时间线的外传→卡卡布三部曲为更早的前传故事。建议按空之轨迹→零碧→那由多的顺序体验。

**清单索引**：见 PSP 章 #3-#8

---

### 伊苏系列 (Ys)

**系列简介**：Nihon Falcom开发的动作RPG系列，始于1987年。主角亚特鲁·克里斯汀是一位红发少年冒险家，以"一击必杀"的简单战斗系统和优秀的音乐著称。系列以"冒险"为核心，每代作品独立世界观但共享同一宇宙。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 伊苏I&II | PCE | Nihon Falcom | 1989 | PCE CD版，系列早期经典 |
| 2 | 伊苏1&2 | PSP | Falcom | 2006 | PSP重制版，菲尔盖纳之誓约 |
| 3 | 伊苏7 | PSP | Falcom | 2009 | PSP原创作，动作系统巅峰 |

**版本关系说明**：PCE CD版为早期经典→PSP重制版(1&2)现代化了画面和系统→伊苏7为PSP原创作，采用即时战斗+小队系统，被认为是系列动作性最强的作品。

**清单索引**：见 PCE 章 #6 / PSP 章 #23-#25

---

### 寂静岭系列 (Silent Hill)

**系列简介**：Konami开发的心理恐怖游戏系列，以雾笼罩的小镇"寂静岭"为舞台，通过心理恐怖氛围、隐喻性怪物设计和深度剧情探讨人类内心的黑暗面。PS1时代的寂静岭1/2被认为是游戏史上最伟大的恐怖游戏。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 寂静岭1 | PS1 | Konami | 1999 | PS1心理恐怖经典 |
| 2 | 寂静岭2 | PS1 | Konami | 2001 | PS1心理恐怖巅峰 |
| 3 | 寂静岭：起源 | PSP | Konami | 2007 | PSP前传，心理恐怖 |
| 4 | 寂静岭：破碎的记忆 | PSP | Konami | 2009 | PSP续作，叙事创新 |

**版本关系说明**：PS1一代奠定系列基调→二代将心理恐怖和叙事提升到艺术高度→PSP起源为系列前传→破碎的记忆采用非线性和不可靠叙事手法。PS1两作为系列最高峰。

**清单索引**：见 PS1 章 #29-#30 / PSP 章 #40-#41

---

### 传说系列 (Tales of)

**系列简介**：Namco（现Bandai Namco）开发的动作RPG系列，以"线性动作战斗系统"(LMBS)为核心特色——角色在地图上自由移动、实时战斗、连击爽快感。系列每代作品独立世界观，以出色的角色塑造著称。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 幻想传说 | SNES/SFC | Square | 1995 | 传说系列首作 |
| 2 | 宿命传说 | PS1 | Namco | 1997 | PS1传说系列正式起点 |
| 3 | 永恒传说 | PS1 | Namco | 2000 | PS1传说系列，时间旅行主题 |

**版本关系说明**：幻想传说为系列精神前身→宿命传说奠定LMBS系统→永恒传说完善系统并引入时间旅行要素。

**清单索引**：见 SNES/SFC 章 #25 / PS1 章 #40-#41


---

### 牧场物语系列 (Harvest Moon / Bokujo Monogatari)

**系列简介**：Pack In Soft（现Marvelous）开发的农场模拟系列，玩家经营农场、种植作物、饲养动物、与村民互动。以悠闲的农场生活和角色养成著称，是农场模拟游戏的开创者之一。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 牧场物语 | SNES/SFC | Pack In Soft | 1996 | SFC农场模拟初代 |
| 2 | 牧场物语GB | GB/GBC | Pack In Soft | 1999 | GB农场模拟 |
| 3 | 牧场物语：矿石镇的伙伴们 | GBA | Pack In Soft | 2003 | GBA农场模拟经典 |
| 4 | 牧场物语：风之集市 | NDS | Pack In Soft | 2010 | NDS农场模拟 |

**版本关系说明**：SFC初代奠定农场模拟玩法→GB版为掌机移植→GBA矿石镇的伙伴们被公认为系列最佳，角色塑造和农场经营达到完美平衡→NDS风之集市为掌机系列续作。

**清单索引**：见 SNES/SFC 章 #70 / GB/GBC 章 #34 / GBA 章 #46 / NDS 章 #42

---

### 高级战争系列 (Advance Wars)

**系列简介**：Nintendo开发的回合制战略游戏系列，以卡通风格和简洁深度的战棋系统著称。玩家指挥军事单位进行回合制对战，兵种克制关系清晰、上手容易精通难，是战棋入门的最佳推荐作品。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 高级战争1 | GBA | Nintendo | 2001 | GBA战棋，系列起点 |
| 2 | 高级战争2 | GBA | Nintendo | 2002 | GBA战棋续作，系统完善 |
| 3 | 高级战争：双重打击 | NDS | Nintendo | 2008 | NDS战棋，双人模式 |

**版本关系说明**：GBA双作为系列核心作品，简洁深入的战棋系统+卡通风格使其成为GBA最佳战略游戏之一→NDS双重打击为系列终章，引入双人模式。

**清单索引**：见 GBA 章 #36-#37 / NDS 章 #23

---

### 光明力量/梦幻模拟战系列 (Shining Force / Langrisser)

**系列简介**：Sega（原Atlus）开发的两条经典战棋RPG系列。光明力量系列以魔幻题材和回合制战棋著称；梦幻模拟战(Langrisser)系列以阵营选择分支和史诗级叙事著称。两条系列在MD/SFC时代各有拥趸。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | Langrisser(梦幻模拟战1) | MD/Genesis | Ascii | 1994 | MD战棋，梦幻模拟战初代 |
| 2 | Langrisser II(梦幻模拟战2) | MD/Genesis | Ascii | 1995 | MD战棋巅峰，多分支叙事 |
| 3 | Langrisser(梦幻模拟战1) | SNES/SFC | Ascii | 1995 | SFC移植版 |
| 4 | Langrisser II(梦幻模拟战2) | SNES/SFC | Ascii | 1996 | SFC移植版 |
| 5 | 光明力量2 | MD/Genesis | Sega | 1993 | MD光明RPG续作 |
| 6 | 光明力量3 | DC | Sega | 1999 | DC独占三部曲 |

**版本关系说明**：MD版梦幻模拟战1/2为系列经典→SFC移植版画面提升→MD光明力量2为独立系列续作→DC光明力量3为三部曲（需要三张CD盘）。梦幻模拟战2的多分支叙事和阵营选择对后续战棋游戏影响深远。

**清单索引**：见 MD/Genesis 章 #16-#17 / SNES/SFC 章 #16-#17 / DC 章 #22

---

### 皇家骑士团系列 (Tactics Ogre)

**系列简介**：Square（现Square Enix）开发的战棋RPG系列，以深刻的政治叙事、永久死亡系统和复杂的职业系统著称。皇家骑士团2被公认为SFC/PS1时代最伟大的战棋游戏之一。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 皇家骑士团2：命运之轮 | SNES/SFC | Square | 1995 | SFC原版Let Us Cling Together |
| 2 | 皇家骑士团2：命运之轮 | PS1 | Square | 2000 | PS1重制版，画面全面提升 |
| 3 | 最终幻想战略版 | PS1 | Square Enix | 1997 | PS1战棋RPG，受皇家骑士团影响 |
| 4 | 最终幻想战略版Advance | GBA | Square Enix | 2003 | GBA战棋RPG |
| 5 | 最终幻想战略版：狮子战争 | PSP | Square Enix | 2007 | PSP独占，PS1版增强 |

**版本关系说明**：SFC原版为系列奠基作→PS1重制版画面大幅提升→FF战略版为精神续作→FF战略版狮子战争为PS1版增强版，含额外内容。皇家骑士团2的"阵营选择"系统（正义/混乱/中立路线）对后续战棋游戏影响深远。

**清单索引**：见 SNES/SFC 章 #15 / PS1 章 #8,#24 / GBA 章 #38 / PSP 章 #20

---

### 格兰蒂亚系列 (Grandia)

**系列简介**：Game Arts开发的RPG系列，以独特的"ATB+即时指令"战斗系统和精美的画面著称。格兰蒂亚1/2在PS1/DC时代被誉为"最被低估的RPG系列"。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 格兰蒂亚 | PS1 | ASCII | 1998 | PS1 RPG，经典冒险 |
| 2 | 格兰蒂亚II | DC | ASCII | 2000 | DC RPG续作 |

**版本关系说明**：PS1初代以独特的冒险叙事和战斗系统获得好评→DC续作画面进一步提升但剧情评价两极。两部作品均被粉丝誉为"被低估的RPG佳作"。

**清单索引**：见 PS1 章 #34 / DC 章 #23

---

### 幻想水浒传系列 (Suikoden)

**系列简介**：Konami开发的RPG系列，以"收集108名星符战士"为核心玩法，结合政治叙事和大规模战争场面。PS1时代的幻想水浒传1/2被日本玩家评为PS1最佳RPG之一。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 幻想水浒传1 | PS1 | Konami | 1995 | PS1 RPG，108星符战士 |
| 2 | 幻想水浒传2 | PS1 | Konami | 1998 | PS1 RPG续作，日本玩家票选PS1最佳RPG第2 |

**版本关系说明**：一代以水浒传为灵感背景，收集108名角色的玩法新颖→二代在剧情深度和世界观构建上大幅进步，被日本玩家评为PS1最佳RPG第二名（仅次于FF7）。

**清单索引**：见 PS1 章 #35-#36

---

### 真女神转生/女神异闻录系列 (Shin Megami Tensei / Persona)

**系列简介**：Atlus开发的RPG系列，以深度哲学主题、恶魔收集和谈判系统著称。真女神转生正传以黑暗末世世界观和道德选择系统闻名；女神异闻录(Persona)子系列以校园生活模拟+地下城探险的双层结构著称，PSP时代迎来系列复兴。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 真女神转生1 | PS1 | Atlus | 1994 | PS1恶魔RPG |
| 2 | 真女神转生2 | PS1 | Atlus | 1995 | PS1续作 |
| 3 | 真女神转生if... | PS1 | Atlus | 1999 | PS1外传，校园题材 |
| 4 | Persona 1 | PS1 | Atlus | 1996 | PS1人格面具初代 |
| 5 | Persona 2：罪 | PS1 | Atlus | 1999 | PS1续作上 |
| 6 | Persona 2：罚 | PS1 | Atlus | 2000 | PS1续作下 |
| 7 | 女神异闻录3携带版 | PSP | Atlus | 2009 | PSP版，静态地图多核显无压力 |

**版本关系说明**：真女神转生正传以黑暗世界观和恶魔谈判系统为核心→if...为校园外传→Persona系列从真女神转生独立出来，以校园生活+人格面具战斗为特色→P3P为PSP版，因静态地图多在N4100上运行良好。

**清单索引**：见 PS1 章 #63-#68 / PSP 章 #12

---

### 索尼克系列 (Sonic the Hedgehog)

**系列简介**：Sega开发的招牌高速平台动作系列，主角索尼克是一只蓝色刺猬，以高速奔跑和收集金环为核心玩法。系列是Sega对抗任天堂马力欧的旗舰IP，MD时代的索尼克1/2/3&纳克鲁斯被视为世嘉招牌。

| 序号 | 游戏名称 | 平台 | 发行方 | 发行年份 | 备注/版本关系 |
|------|----------|------|--------|----------|--------------|
| 1 | 索尼克1 | MD/Genesis | Sega | 1991 | MD索尼克初代 |
| 2 | 索尼克2 | MD/Genesis | Sega | 1992 | MD索尼克续作，纳克鲁斯登场 |
| 3 | 索尼克3&纳克鲁斯 | MD/Genesis | Sega | 1994 | MD索尼克终极版 |
| 4 | 索尼克大冒险 | DC | Sega | 1998 | DC 3D索尼克 |
| 5 | 索尼克大冒险2 | DC | Sega | 2001 | DC末代索尼克 |

**版本关系说明**：MD三作(1/2/3&纳克鲁斯)为系列黄金时代，高速平台跳跃的巅峰之作→DC时代3D化转型，大冒险1/2为3D索尼克的代表作。MD三作建议按1→2→3&纳克鲁斯的顺序体验。

**清单索引**：见 MD/Genesis 章 #1-#3 / DC 章 #10-#11


---

---

## 遗漏高分作品调研

> 本节结合 IGN 历年满分游戏榜单、Metacritic 各平台高分游戏、Fami通历代主机TOP游戏、Digital Trends "每个平台最高评分游戏"、A9VG/各大游戏媒体经典游戏推荐等权威榜单，盘点本文档可能遗漏的高分佳作。

### 调研方法

1. 检索 IGN 历年满分(10/10)游戏榜单，筛选本文档覆盖平台范围内的作品
2. 检索 Metacritic 各平台高分(90+)游戏榜单
3. 检索 Fami通历代主机游戏排行榜
4. 检索 Digital Trends "每个平台最高评分游戏"榜单
5. 对照本文档已有游戏清单，找出遗漏项

### 可能遗漏的高分游戏

#### PS1 平台遗漏

| 游戏名称 | 发行方 | 预估大小 | 遗漏原因 | 推荐理由 |
|----------|--------|----------|----------|----------|
| 托尼霍克职业滑板2 | Activision | 600MB | 体育游戏类未收录 | MC 98分，PS1最高评分游戏，极限运动游戏奠基作 |
| 托尼霍克职业滑板 | Activision | 400MB | 体育游戏类未收录 | MC 92分，初代即经典 |
| 古惑狼赛车 | Activision | 600MB | 衍生作未收录 | 古惑狼系列赛车衍生作，评价不俗 |

#### GBA 平台遗漏

| 游戏名称 | 发行方 | 预估大小 | 遗漏原因 | 推荐理由 |
|----------|--------|----------|----------|----------|
| 宝可梦 红宝石/蓝宝石 | Nintendo | 16MB | 丰缘地区未收录 | GBA销量第一(1585万套)，丰缘地区，三圣柱前作 |
| 宝可梦 翡翠 | Nintendo | 16MB | 丰缘地区续作未收录 | GBA宝可梦终章，丰缘地区最终版 |
| 龙珠大冒险 | Bandai | 32MB | 动漫改编未收录 | IGN GBA TOP25，横版动作手感极佳，漫改游戏标杆 |
| 皇家骑士团外传：罗迪斯的骑士 | Enix | 32MB | 外传未收录 | IGN GBA TOP20，战棋RPG佳作 |
| 风来之西林 | Enix | 32MB | 衍生作未收录 | A9VG推荐GBA必玩，动作RPG |
| 特鲁尼克大冒险 | Enix | 32MB | 衍生作未收录 | A9VG推荐GBA必玩，迷宫探险 |

#### Dreamcast 平台遗漏

| 游戏名称 | 发行方 | 预估大小 | 遗漏原因 | 推荐理由 |
|----------|--------|----------|----------|----------|
| 天空之艾德嘉 | Sega | 1.2GB | RPG未收录 | Fami通DC TOP5，空中冒险RPG巨作，最后的大作之一 |
| 樱花大战 花传 | Sega | 1.2GB | 续作未收录 | Fami通DC TOP3，樱花大战系列续作 |
| 梦幻之星 宇宙继承记 | Sega | 800MB | 在线游戏未收录 | Fami通DC TOP5，PSO续作，在线RPG |

#### N64 平台遗漏

| 游戏名称 | 发行方 | 预估大小 | 遗漏原因 | 推荐理由 |
|----------|--------|----------|----------|----------|
| 皮克敏 | Nintendo | 32MB | 平台不符(NGC) | 非N64游戏，不收录 |

### 调研结论

经过全面检索 IGN、Metacritic、Fami通、Digital Trends 等权威榜单，本文档已收录了绝大多数高分经典作品。主要遗漏集中在：

1. **体育游戏类别**：托尼霍克职业滑板系列(PS1)是MC评分最高的PS1游戏(98分)，但本文档未收录任何体育游戏
2. **GBA宝可梦补充**：红宝石/蓝宝石/翡翠(丰缘地区三圣柱)是GBA销量最高的宝可梦作品，但本文档仅收录了火红/叶绿/绿宝石(关都/丰缘复刻版)
3. **DC RPG补充**：天空之艾德嘉是Fami通票选DC最佳RPG之一，但本文档未收录
4. **动漫改编游戏**：龙珠大冒险等漫改游戏虽评分不俗但未被纳入

**建议**：如果希望进一步完善清单，可以补充托尼霍克职业滑板2(PS1)、宝可梦红宝石/蓝宝石(GBA)、天空之艾德嘉(DC)这三款游戏。

### 榜单参考来源

1. IGN 历年满分游戏榜单 (10/10) — 收录时空之轮、宝可梦红/蓝/黄、塞尔达时之笛、塞尔达众神三角力量、超级马力欧兄弟3、超级马力欧世界、超级马力欧64、宝可梦金/银、塞尔达织梦岛DX、塞尔达时空之章、塞尔达大地之章、塞尔达缩小帽、黄金太阳失落的时代、高级战争、火焰纹章圣战之系谱、超级马力欧RPG、地球冒险2、节奏天国等
2. Metacritic PS1最高评分游戏 — 托尼霍克职业滑板2(98)、铁拳3(96)、GT赛车(96)、最终幻想9(94)、时空之轮2(94)、合金装备(94)、恶魔城月下夜想曲(93)等
3. Digital Trends "每个平台最高评分游戏" — DC:灵魂能力(98)、PS1:托尼霍克职业滑板2(98)、N64:完美黑暗(97)等
4. Fami通历代主机游戏票选 — DC:梦幻之星在线、莎木、樱花大战3、索尼克大冒险、疯狂出租车等
5. A9VG GBA十大必玩游戏 — 瓦里奥制造、马力欧与路易吉RPG、宝可梦红宝石/蓝宝石/绿宝石、塞尔达缩小帽、龙珠大冒险、逆转裁判三部曲、高级战争1+2、火焰纹章圣魔之光石、恶魔城晓月圆舞曲、黄金太阳1&2
6. IGN GBA史上最佳25款 — 超级猴子球Jr.、黄金太阳、忍者刑警、马力欧vs咚奇刚、牧场物语矿石镇的伙伴们、塞尔达缩小帽、马力欧赛车Advance、密特罗德融合、超级马力欧Advance2、火焰纹章烈火之剑等



## 汇总：各平台容量统计与存储分配

### 平台容量总览

| 平台 | 游戏数量 | 预估总容量 | 推荐存放位置 |
|------|----------|------------|-------------|
| NES / FC | 91 | ~88MB (0.09GB) | eMMC |
| GB / GBC | 41 | ~219MB (0.21GB) | eMMC |
| MD / Genesis | 58 | ~264MB (0.26GB) | eMMC |
| SNES / SFC | 99 | ~710MB (0.69GB) | eMMC |
| N64 | 34 | ~768MB (0.75GB) | eMMC |
| PCE | 39 | ~816MB (0.80GB) | eMMC |
| GBA | 65 | ~1,472MB (1.4GB) | eMMC |
| NDS | 69 | ~4,640MB (4.5GB) | eMMC |
| 街机(FBNeo/MAME) | 163 | ~9,740MB (9.5GB) | eMMC |
| Dreamcast | 39 | ~33,939MB (33.1GB) | SSD |
| PSP | 52 | ~48,014MB (46.9GB) | SSD |
| PS1 | 81 | ~53,830MB (52.6GB) | SSD |
### 存储分配方案

**eMMC 端（约 18.2GB，软链接）**：NES/FC、GB/GBC、MD/Genesis、SNES/SFC、N64、PCE、GBA、NDS、街机(FBNeo/MAME)

**SSD 端（约 132.6GB，原生目录）**：Dreamcast、PSP、PS1

**全集总计：约 150.9GB**（约 154500MB）

你的可用空间：eMMC约60GB + SSD约256GB = 约316GB。全集约151GB，完全放得下。eMMC 还剩约 40GB 余量作为缓冲层。

---

## 实操建议

### 1. BIOS 先配齐再下 ROM

- PS1 需要 `scph5501.bin` / `scph7001.bin`
- DC 需要 `dc_bios.bin` + flash
- MAME 必须 ROM set 与模拟器版本匹配（否则一堆找不到游戏）
- GBA/NDS/PSP 不需要 BIOS

### 2. 格式统一

- PS1/DC 一律转 CHD（Batocera 自带 `chdman`），体积能砍一半以上
- PSP 用 ISO 不用 CSO（高压缩档在慢盘上解压会卡顿）
- NDS 用 `.nds` 或 `.zip` 单文件

### 3. 分批下载 + 分批刮削

按平台一个一个来，每完成一个平台就进游戏试玩10分钟，把不想玩的删掉。
刮削器很吃内存，4GB 机器请分批刮削（一次一个平台），否则容易 OOM 卡死。
优先级建议：街机 CPS1/2/NeoGeo + GBA + SFC + MD → PS1 → NDS → DC → PSP → N64 → PCE → GB/GBC（注意平台顺序已调整：8位→16位→32位→64位，小镜像优先）

### 4. N4100 性能提醒

| 平台 | N4100 表现 | 建议设置 |
|------|-----------|----------|
| GB/GBC/GBA、NES、SNES、MD、PCE、GG、WS | 毫无压力，随便拉倍率 | 默认即可 |
| CPS1/2/3、NeoGeo、IGS（三国战纪）、彩京/Toaplan 飞行射击 | FBNeo 核心满速 | 街机优先用 FBNeo 核心 |
| PS1 | 满速，2x-4x 渲染都行 | DuckStation/PCSX-ReARMed，CHD 格式 |
| NDS | 满速（melonDS） | 默认 |
| Dreamcast | 绝大多数满速，2x 分辨率也可 | Flycast；个别重负载场景降回 1x |
| N64 | 第一方主流作品 OK，部分掉帧 | GLideN64 + 1x~2x |
| PSP | 1x 分辨率大部分稳 30-60 帧；2x 开始掉 | PPSSPP 锁 1x，关硬件变换外的花哨选项 |
| MAME（后期：Cave后期、Naomi/Naomi2、Model2/3） | 吃力 | 这些归到 FBNeo 或直接放弃 |

### 5. 纠错清单（之前对话中提到的硬错误）

| 你写的 | 问题 | 正确做法 |
|--------|------|----------|
| 超级银河战士：零点任务（列在SFC） | 这是 GBA 游戏 | 从SFC栏删除，GBA栏保留 |
| 宝可梦红/绿/蓝/黄（列在GBA） | 这是 GB/GBC 游戏 | 从GBA栏删除，GB栏保留 |
| 重装机兵2/3（列在PS1） | 2代是SFC，3代是NDS | 从PS1栏删除 |
| 怒之铁拳系列（列在街机） | 这是 MD 独占 | 从街机栏删除 |
| 雷电、R-Type（列在MD） | MD上没有这两款 | 从MD栏删除，留街机/PCE |
| 绿色兵团2（列在NES） | 续作是街机 | 挪到街机栏 |
| 超级机器人大战第5次（SFC） | 官方不存在 | 删除或改为新超级机器人大战(PS) |
| 信长之野望：岚世记（PS1） | 平台是PC/PS2/Xbox | 从PS1栏删除 |
| 街头霸王III三度冲击（DC） | DC上是合集Double Impact | 改名为合集收录 |
| 漆黑的魅影 | 民间改版(hack) | 想玩正统就下绿宝石 |
| 太空战士（MD） | 盗版商汉化拼凑物 | 标为情怀向即可 |
| 枪之刃/枪之刃2/闪亮之刃/闪亮之刃2/幻想水滴 | 名称对不上任何已知官方作品 | 先核实再下 |

---



## 备注

1. 以上文件大小为预估价值，实际大小因 ROM 压缩率、CHD 压缩比、是否包含额外音频/视频流而异。
2. CHD 格式的 PS1/DC 游戏通常比 ISO 小 40-60%，建议优先使用 CHD。
3. PSP 游戏建议用 ISO 格式（不用 CSO 压缩），避免在 eMMC 慢速读取时卡顿。
4. 街机 ROM 需要对应模拟器版本的 ROM set，版本不匹配会导致游戏无法运行。
5. 部分游戏标注了 N4100 性能问题，如实际体验不佳可尝试调整模拟器设置或放弃。
6. 系列完整性原则：如果是系列作品，不因单作负面评价而舍弃，尽量全收录以保持完整性。