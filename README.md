# Batocera 家庭游戏机精选指南

面向 **Intel Celeron N4100＋UHD 600＋4 GB 内存＋Batocera** 的家庭电视游戏机精选库。大作之外，同样重视本地合作、双人对战、经典休闲和适合慢节奏游玩的作品。

**阅读全文：[batocera_rom_guide.md](batocera_rom_guide.md)**

## 指南内容

- 覆盖 18 个平台：DOS、Win95／98、MAME、FBNeo、NES／FC、PCE、MD、GB、GG、SNES／SFC、N64、PS1、GBC、Dreamcast、WS／WSC、GBA、NDS、PSP。
- 当前共 **927 个条目、994 款官方游戏**；合集按独立商品展开计数，地区别名不重复。
- 每款作品列出完整商品名、中文译名、出版日期、出版商、预留空间、品类及内容与历史备注。
- 汇总平台位数、发布时间、厂商、硬件特点、推荐模拟器和特别配置。
- 同一基础作品原则上只保留一个平台版本，并记录版本取舍理由。
- 设有品类源流、系列专题和平台回链，以及中文化版本与精选非官方改版清单。
- DOS 使用 DOSBox 路线；Windows 95／98 游戏使用 Batocera Wine，并逐款标明安装判断、字体要求与验收边界。

这份清单依据平台支持、保守性能范围、作品质量与家庭游玩价值筛选，**不是逐款实机测试承诺**。PS2、PS3、PS4、GameCube、Wii 和 Xbox 等超出本机保守性能范围的平台不予收录。

## 容量结论

| 项目 | 预留空间 |
|---|---:|
| 官方游戏库 | 243.64 GiB |
| 中文化与精选改版额外预算 | 16 GiB |
| 全量游戏与改版预算 | 259.64 GiB |
| 现有双盘首装方案 | 202.64 GiB |

容量是安装预算，不是实测 ROM 总量。系统、BIOS、Wine prefix、字体、存档、刮削、缓存和空闲空间需要另算；因此不建议把全量库直接塞入 256＋64 GB 双盘。指南提供了首装、候补、外部备份和 512 GB SSD 升级方案。

## 项目文件

- `batocera_rom_guide.md`：生成后的完整指南，也是主要阅读入口。
- `batocera_rom_guide_source.md`：早期整理底稿。
- `finalize_guide.py`：条目整合、版本取舍、专题与汇总生成。
- `guide_*.py`：平台数据、备注、DOS／Windows 精选和版本规则。
- `audit_guide.py`：重新生成指南并执行完整性与防回归审计。
- `dos_comprehensive_list.csv`：DOS 候选作品核对资料。

维护内容时请修改相应数据或生成脚本，**不要只手改生成后的 `batocera_rom_guide.md`**，以免下次生成时丢失修订。

## 重新生成与审计

需要 Python 3：

```bash
# 只重新生成指南
python finalize_guide.py

# 重新生成并执行完整审计
python audit_guide.py
```

审计会检查平台与条目数量、必填字段、重复商品、Markdown 表格、内部链接、系列归类、跨平台版本取舍、Windows 运行标记及容量汇总，并生成 `audit_report.txt`。当前结果为 **0 错误、0 警告**。

## 内容与版权边界

本仓库只包含文档、候选资料及生成和审计脚本，**不包含 ROM、BIOS、游戏镜像或受版权保护的游戏资源**。指南中的外部项目与兼容性资料由其各自作者维护；实际安装和验收应以所用 Batocera、模拟器、Wine runner 及合法游戏版本为准。
