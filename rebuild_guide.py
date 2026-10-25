from pathlib import Path
import re, math
from dataclasses import dataclass

ROOT = Path('/Users/haibara/Documents/Kimi/Workspaces/Botacera_Home')
source = (ROOT/'batocera_rom_guide_source.md').read_text()
platform_heads = ['NES / FC','GB / GBC','MD / Genesis','SNES / SFC','N64','PCE (PC Engine / TurboGrafx-16)','GBA','NDS','街机（FBNeo / MAME）','Dreamcast','PSP','PS1']
short = {'NES / FC':'NES','GB / GBC':'GB','MD / Genesis':'MD','SNES / SFC':'SNES','N64':'N64','PCE (PC Engine / TurboGrafx-16)':'PCE','GBA':'GBA','NDS':'NDS','街机（FBNeo / MAME）':'ARC','Dreamcast':'DC','PSP':'PSP','PS1':'PS1'}

@dataclass
class Entry:
    platform: str
    old: str
    en: str = ''
    zh: str = ''
    pub: str = ''
    size: str = ''
    year: str = ''
    note: str = ''
    series: str = ''
    subgroup: str = ''
    eid: str = ''

# 只删除重复、错平台、非官方改版或无法对应正式商品的条目；正式移植版不因“非独占”删除。
drops = {
'NES / FC': {'超级马力欧USA','忍者神龟4','[存疑]'},
'GB / GBC': {'星之卡比梦之泉DX','最终幻想'},
'MD / Genesis': {'格斗三人组','[存疑]闪亮之刃','[存疑]闪亮之刃2','[存疑]幻想水滴','[不存在]雷电','[不存在]R-Type','[存疑]枪之刃','[存疑]枪之刃2','Golden Axe 1','Golden Axe 2','Golden Axe 3','Altered Beast','恶魔战士'},
'SNES / SFC': {'[删除]超级银河战士：零点任务','Gimmick!'},
'GBA': {'[删除]宝可梦 红/绿/蓝/黄/黄','宝可梦 漆黑的魅影','勇者斗恶龙5','勇者斗恶龙6'},
'NDS': {'星之卡比：毛线传说','宝可梦不可思议迷宫：赤救助队','接触！瓦力欧制造','寒蝉鸣泣之时：祭'},
'街机（FBNeo / MAME）': {'Strikers 1999','Strikers 2000'},
'Dreamcast': {'光明力量3','索尼克Shuffle'},
'PSP': {'怪物猎人携带版2nd G|DUP','初音未来：歌姬计划F','最终幻想4/5/6（PSP移植）'},
'PS1': {'寂静岭2','仙剑奇侠传','大富翁4'},
}

# 精确商品名与常见中文译名。未列出的混合名称会保留英文部分并清理中文前缀。
X = {
'超级马力欧兄弟':('Super Mario Bros.','超级马力欧兄弟'),
'超级马力欧兄弟2':('Super Mario Bros. 2 (USA)','超级马力欧兄弟 2（海外版）'),
'超级马力欧兄弟3':('Super Mario Bros. 3','超级马力欧兄弟 3'),
'塞尔达传说':('The Legend of Zelda','塞尔达传说'),
'塞尔达传说2：林克的冒险':('Zelda II: The Adventure of Link','塞尔达传说 2：林克的冒险'),
'洛克人':('Mega Man','洛克人'),'洛克人2':('Mega Man 2','洛克人 2'),'洛克人3':('Mega Man 3','洛克人 3'),'洛克人4':('Mega Man 4','洛克人 4'),'洛克人5':('Mega Man 5','洛克人 5'),'洛克人6':('Mega Man 6','洛克人 6'),
'魂斗罗':('Contra','魂斗罗'),'魂斗罗2':('Super C','超级魂斗罗'),
'忍者龙剑传':('Ninja Gaiden','忍者龙剑传'),'忍者龙剑传2':('Ninja Gaiden II: The Dark Sword of Chaos','忍者龙剑传 II：暗黑邪神剑'),'忍者龙剑传3':('Ninja Gaiden III: The Ancient Ship of Doom','忍者龙剑传 III：黄泉的方舟'),
'冒险岛':('Adventure Island','高桥名人冒险岛'),'冒险岛2':('Adventure Island II','高桥名人冒险岛 II'),'冒险岛3':('Adventure Island 3','高桥名人冒险岛 3'),'冒险岛4':('Takahashi Meijin no Bouken Jima IV','高桥名人冒险岛 IV'),
'坦克大战':('Battle City','坦克大战'),'马戏团':('Circus Charlie','马戏团'),'赤影战士':('Shadow of the Ninja','赤影战士／水上魂斗罗'),
'三国志':('Sangokushi','三国志'),'中原之霸者':('Nakahara no Hasha: Sangoku Shouseiden','三国志：中原之霸者'),'霸王的大陆':('Sangokushi II: Haou no Tairiku','三国志 II：霸王的大陆'),
'最终幻想':('Final Fantasy','最终幻想'),'最终幻想2':('Final Fantasy II','最终幻想 II'),'最终幻想3':('Final Fantasy III','最终幻想 III'),
'勇者斗恶龙':('Dragon Quest','勇者斗恶龙'),'勇者斗恶龙2':('Dragon Quest II: Luminaries of the Legendary Line','勇者斗恶龙 II：恶灵的众神'),'勇者斗恶龙3':('Dragon Quest III: The Seeds of Salvation','勇者斗恶龙 III：传说的开始'),'勇者斗恶龙4':('Dragon Quest IV: Chapters of the Chosen','勇者斗恶龙 IV：被引导的人们'),
'双截龙':('Double Dragon','双截龙'),'双截龙2':('Double Dragon II: The Revenge','双截龙 II：复仇'),'双截龙3':('Double Dragon III: The Sacred Stones','双截龙 III：圣石'),
'绿色兵团':('Rush’n Attack','绿色兵团'),'沙罗曼蛇':('Life Force / Salamander','沙罗曼蛇'),'宇宙巡航机':('Gradius','宇宙巡航机'),
'炸弹人':('Bomberman','炸弹人'),'炸弹人2':('Bomberman II','炸弹人 II'),
'恶魔城':('Castlevania','恶魔城'),'恶魔城2：诅咒之月':('Castlevania II: Simon’s Quest','恶魔城 II：西蒙的冒险'),'恶魔城3：德拉库拉的诅咒':('Castlevania III: Dracula’s Curse','恶魔城 III：德古拉的诅咒'),
'热血硬派':('Nekketsu Kouha Kunio-kun','热血硬派国夫君'),'热血行进曲':('Downtown Nekketsu Koushinkyoku: Soreyuke Daiundoukai','热血行进曲：前进大运动会'),'热血格斗传说':('Nekketsu Kakutou Densetsu','热血格斗传说'),'热血物语':('River City Ransom / Downtown Nekketsu Monogatari','热血物语'),'热血足球':('Nintendo World Cup / Nekketsu Koukou Dodgeball-bu Soccer-hen','热血足球'),'热血篮球':('Nekketsu! Street Basket: Ganbare Dunk Heroes','热血街头篮球'),'热血躲避球':('Super Dodge Ball / Nekketsu Koukou Dodgeball-bu','热血躲避球'),
'忍者神龟':('Teenage Mutant Ninja Turtles','忍者神龟'),'忍者神龟2':('Teenage Mutant Ninja Turtles II: The Arcade Game','忍者神龟 II：街机移植版'),'忍者神龟3':('Teenage Mutant Ninja Turtles III: The Manhattan Project','忍者神龟 III：曼哈顿计划'),
'松鼠大战':('Chip ’n Dale: Rescue Rangers','松鼠大作战'),'松鼠大战2':('Chip ’n Dale: Rescue Rangers 2','松鼠大作战 2'),
'唐老鸭梦冒险':('DuckTales','唐老鸭历险记'),'唐老鸭梦冒险2':('DuckTales 2','唐老鸭历险记 2'),
'天使之翼':('Captain Tsubasa','天使之翼'),'天使之翼2':('Captain Tsubasa II: Super Striker','天使之翼 II：超级射手'),
'重装机兵':('Metal Max','重装机兵'),'圣火徽章外传':('Fire Emblem Gaiden','火焰之纹章外传'),
'吞食天地':('Tenchi wo Kurau / Destiny of an Emperor','吞食天地'),'吞食天地2':('Tenchi wo Kurau II: Shokatsu Koumei Den','吞食天地 II：诸葛孔明传'),
'封神榜':('Feng Shen Bang: Fu Mo San Jian Xia','封神榜：伏魔三剑侠'),'西游记世界':('Saiyuuki World','西游记世界'),'七宝奇谋':('The Goonies','七宝奇谋'),
'超惑星战记Blaster Master':('Blaster Master','超惑星战记'),'星际魂斗罗Journey to Silius':('Journey to Silius','星际魂斗罗／西利乌斯之旅'),'赤色要塞Jackal':('Jackal','赤色要塞'),'兵蜂TwinBee':('TwinBee','兵蜂'),'影子传说':('The Legend of Kage','影子传说'),'忍者茶茶丸':('Ninja JaJaMaru-kun','忍者茶茶丸'),'蝙蝠侠':('Batman: The Video Game','蝙蝠侠'),'小叮当':('Doraemon','哆啦 A 梦'),'龙珠 大魔神':('Dragon Ball: Daimaou Fukkatsu','龙珠：大魔王复活'),'圣斗士星矢 黄金传说':('Saint Seiya: Ougon Densetsu','圣斗士星矢：黄金传说'),'北斗神拳':('Hokuto no Ken','北斗神拳'),
'挖金矿Lode Runner':('Lode Runner','淘金者'),'敲冰块':('Ice Climber','敲冰块'),'越野机车Excitebike':('Excitebike','越野机车'),'功夫Yie Ar Kung-Fu':('Yie Ar Kung-Fu','功夫'),'马里奥兄弟 (Mario Bros.)':('Mario Bros.','马力欧兄弟'),'大金刚':('Donkey Kong','咚奇刚'),'打鸭子':('Duck Hunt','打鸭子'),'气球大战':('Balloon Fight','气球大战'),'俄罗斯方块':('Tetris','俄罗斯方块'),
'塞尔达传说：织梦岛':('The Legend of Zelda: Link’s Awakening','塞尔达传说：织梦岛'),'塞尔达传说：织梦岛DX':('The Legend of Zelda: Link’s Awakening DX','塞尔达传说：织梦岛 DX'),
'超级马力欧乐园1':('Super Mario Land','超级马力欧乐园'),'超级马力欧乐园2':('Super Mario Land 2: 6 Golden Coins','超级马力欧乐园 2：六枚金币'),'瓦力欧乐园':('Wario Land: Super Mario Land 3','瓦力欧乐园：超级马力欧乐园 3'),'瓦力欧乐园3':('Wario Land 3','瓦力欧乐园 3'),
'宝可梦红/绿/蓝/黄':('Pokémon Red / Green / Blue / Yellow','宝可梦：红／绿／蓝／皮卡丘'),'宝可梦金/银/水晶':('Pokémon Gold / Silver / Crystal','宝可梦：金／银／水晶'),
'银河战士2':('Metroid II: Return of Samus','密特罗德 II：萨姆斯归来'),
'洛克人世界1':('Mega Man: Dr. Wily’s Revenge','洛克人世界：威利博士的反击'),'洛克人世界2':('Mega Man II','洛克人世界 II'),'洛克人世界3':('Mega Man III','洛克人世界 III'),'洛克人世界4':('Mega Man IV','洛克人世界 IV'),'洛克人世界5':('Mega Man V','洛克人世界 V'),
'恶魔城德古拉传说1':('Castlevania: The Adventure','恶魔城：德古拉传说'),'恶魔城德古拉传说2':('Castlevania II: Belmont’s Revenge','恶魔城：德古拉传说 II'),'恶魔城Legends':('Castlevania Legends','恶魔城：漆黑前奏曲'),'恶魔城小鬼Dracula':('Kid Dracula / Akumajou Special: Boku Dracula-kun','恶魔城特别篇：我是德古拉'),
'魔界塔士SaGa1':('The Final Fantasy Legend / Makai Toushi SaGa','魔界塔士 SaGa'),'魔界塔士SaGa2':('Final Fantasy Legend II / SaGa 2: Hihou Densetsu','SaGa 2：秘宝传说'),'魔界塔士SaGa3':('Final Fantasy Legend III / SaGa 3: Jikuu no Hasha','SaGa 3：时空的霸者'),
'忍者龙剑传GB':('Ninja Gaiden Shadow','忍者龙剑传 GB：摩天楼决战'),'双截龙GB':('Double Dragon II','双截龙 II（GB）'),'忍者神龟GB':('Teenage Mutant Ninja Turtles: Fall of the Foot Clan','忍者神龟：脚帮的覆灭'),
'七龙珠GB系列':('Dragon Ball Z: Goku Hishouden / Goku Gekitouden','龙珠 Z：悟空飞翔传／激斗传'),'圣斗士GB':('Saint Seiya: The Sanctuary / Saint Paradise','圣斗士星矢（GB 合集）'),'牧场物语GB':('Harvest Moon GB','牧场物语 GB'),'马里奥医生':('Dr. Mario','马力欧医生'),'耀西蛋':('Yoshi','耀西的蛋'),'炸弹人GB':('Bomberman GB','炸弹人 GB'),'宝可梦卡片GB':('Pokémon Trading Card Game','宝可梦集换式卡牌 GB'),'Game & Watch Gallery系列':('Game & Watch Gallery 1–3','Game & Watch 博物馆 1–3'),
'索尼克1':('Sonic the Hedgehog','刺猬索尼克'),'索尼克2':('Sonic the Hedgehog 2','刺猬索尼克 2'),'索尼克3&纳克鲁斯':('Sonic the Hedgehog 3 & Knuckles','索尼克 3 与纳克鲁斯'),
'怒之铁拳':('Streets of Rage / Bare Knuckle','怒之铁拳'),'怒之铁拳2':('Streets of Rage 2 / Bare Knuckle II','怒之铁拳 2'),'怒之铁拳3':('Streets of Rage 3 / Bare Knuckle III','怒之铁拳 3'),
'幽游白书：魔强统一战':('Yuu Yuu Hakusho: Makyou Toitsusen','幽游白书：魔强统一战'),'战斧':('Golden Axe','战斧'),'战斧2':('Golden Axe II','战斧 II'),'战斧3':('Golden Axe III','战斧 III'),'兽王记':('Altered Beast','兽王记'),
'三国志2':('Romance of the Three Kingdoms II','三国志 II'),'三国志3':('Romance of the Three Kingdoms III: Dragon of Destiny','三国志 III'),'信长之野望：全国版':('Nobunaga’s Ambition: Zenkokuban','信长之野望：全国版'),
'大战略':('Advanced Daisenryaku','大战略：德意志电击战'),'魂斗罗 铁血兵团':('Contra: Hard Corps','魂斗罗：铁血兵团'),'超级忍2':('The Revenge of Shinobi','超级忍：复仇'),'波斯王子':('Prince of Persia','波斯王子'),
'梦幻之星2':('Phantasy Star II','梦幻之星 II'),'梦幻之星4':('Phantasy Star IV: The End of the Millennium','梦幻之星 IV：千年纪的终结'),
'超级马力欧世界':('Super Mario World','超级马力欧世界'),'超级马力欧世界2：耀西岛':('Super Mario World 2: Yoshi’s Island','超级马力欧世界 2：耀西岛'),'超级马力欧RPG':('Super Mario RPG: Legend of the Seven Stars','超级马力欧 RPG：七星传说'),
'塞尔达传说：众神的三角力量':('The Legend of Zelda: A Link to the Past','塞尔达传说：众神的三角力量'),'超级银河战士':('Super Metroid','超级密特罗德'),'超时空之钥':('Chrono Trigger','超时空之钥'),
'最终幻想4':('Final Fantasy IV','最终幻想 IV'),'最终幻想5':('Final Fantasy V','最终幻想 V'),'最终幻想6':('Final Fantasy VI','最终幻想 VI'),'勇者斗恶龙5':('Dragon Quest V: Hand of the Heavenly Bride','勇者斗恶龙 V：天空的新娘'),'勇者斗恶龙6':('Dragon Quest VI: Realms of Revelation','勇者斗恶龙 VI：幻之大地'),
'火焰之纹章：纹章之谜':('Fire Emblem: Mystery of the Emblem','火焰之纹章：纹章之谜'),'火焰之纹章：圣战之系谱':('Fire Emblem: Genealogy of the Holy War','火焰之纹章：圣战之系谱'),'火焰之纹章：多拉基亚776':('Fire Emblem: Thracia 776','火焰之纹章：多拉基亚 776'),
'皇家骑士团2：命运之轮':('Tactics Ogre: Let Us Cling Together','皇家骑士团：命运之轮'),
'前线任务 Gun Hazard':('Front Mission: Gun Hazard','前线任务：枪之危机'),'超级机器人大战3':('Dai-3-Ji Super Robot Taisen','第 3 次超级机器人大战'),'超级机器人大战EX':('Super Robot Taisen EX','超级机器人大战 EX'),'超级机器人大战第4次':('Dai-4-Ji Super Robot Taisen','第 4 次超级机器人大战'),'超级机器人大战Gaiden':('Super Robot Taisen Gaiden: Masou Kishin – The Lord of Elemental','超级机器人大战外传：魔装机神'),
'圣剑传说2':('Secret of Mana / Seiken Densetsu 2','圣剑传说 2'),'圣剑传说3':('Trials of Mana / Seiken Densetsu 3','圣剑传说 3'),'幻想传说':('Tales of Phantasia','幻想传说'),'大航海时代2':('Uncharted Waters: New Horizons / Daikoukai Jidai II','大航海时代 II'),
'三国志4':('Romance of the Three Kingdoms IV: Wall of Fire','三国志 IV'),'信长之野望：武将风云录':('Nobunaga’s Ambition: Bushou Fuuunroku','信长之野望：武将风云录'),'信长之野望：霸王传':('Nobunaga’s Ambition: Haouden','信长之野望：霸王传'),'信长之野望：天翔记':('Nobunaga’s Ambition: Tenshouki','信长之野望：天翔记'),
'恶魔城X：血之轮回':('Castlevania: Dracula X','恶魔城 XX'),'洛克人X':('Mega Man X','洛克人 X'),'洛克人X2':('Mega Man X2','洛克人 X2'),'洛克人X3':('Mega Man X3','洛克人 X3'),'洛克人7':('Mega Man 7','洛克人 7'),
'街头霸王2 Turbo':('Street Fighter II Turbo: Hyper Fighting','街头霸王 II Turbo'),'超级街霸2':('Super Street Fighter II: The New Challengers','超级街头霸王 II'),'快打旋风':('Final Fight','快打旋风'),'快打旋风2':('Final Fight 2','快打旋风 2'),'快打旋风3':('Final Fight 3','快打旋风 3'),
'超级大金刚':('Donkey Kong Country','咚奇刚国度'),'超级大金刚2':('Donkey Kong Country 2: Diddy’s Kong Quest','咚奇刚国度 2：迪迪刚大冒险'),'超级大金刚3':('Donkey Kong Country 3: Dixie Kong’s Double Trouble!','咚奇刚国度 3：迪克西刚的双重麻烦'),
'星际火狐':('Star Fox','星际火狐'),'星际火狐2':('Star Fox 2','星际火狐 2'),'超级马力欧卡丁车':('Super Mario Kart','超级马力欧卡丁车'),'时空勇士':('Live A Live','时空勇士'),'地球冒险2':('EarthBound / Mother 2','地球冒险 2／MOTHER 2'),
'魂斗罗精神 Contra III':('Contra III: The Alien Wars','魂斗罗精神：异形战争'),'浪漫沙加1':('Romancing SaGa','浪漫沙加'),'浪漫沙加2':('Romancing SaGa 2','浪漫沙加 2'),'浪漫沙加3':('Romancing SaGa 3','浪漫沙加 3'),'星之海洋':('Star Ocean','星之海洋'),'天地创造 Terranigma':('Terranigma','天地创造'),'卡比超级明星':('Kirby Super Star','星之卡比：超级豪华版'),'星之卡比3':('Kirby’s Dream Land 3','星之卡比 3'),'牧场物语':('Harvest Moon','牧场物语'),
'塞尔达传说：时之笛':('The Legend of Zelda: Ocarina of Time','塞尔达传说：时之笛'),'塞尔达传说：姆吉拉的假面':('The Legend of Zelda: Majora’s Mask','塞尔达传说：魔吉拉的面具'),'超级马力欧64':('Super Mario 64','超级马力欧 64'),'马力欧卡丁车64':('Mario Kart 64','马力欧卡丁车 64'),'007：黄金眼':('GoldenEye 007','007：黄金眼'),'星际火狐64':('Star Fox 64','星际火狐 64'),'完美黑暗':('Perfect Dark','完美黑暗'),'生化危机2':('Resident Evil 2','生化危机 2'),'任天堂明星大乱斗':('Super Smash Bros.','任天堂明星大乱斗'),'班卓熊大冒险1':('Banjo-Kazooie','班卓熊大冒险'),'班卓熊大冒险2':('Banjo-Tooie','班卓熊大冒险 2'),'纸片马力欧':('Paper Mario','纸片马力欧'),'咚奇刚64':('Donkey Kong 64','咚奇刚 64'),'耀西的故事':('Yoshi’s Story','耀西的故事'),'星之卡比64':('Kirby 64: The Crystal Shards','星之卡比 64：水晶碎片'),
'宝可梦竞技场1':('Pokémon Stadium','宝可梦竞技场'),'宝可梦竞技场2':('Pokémon Stadium 2','宝可梦竞技场 2'),'宝可梦皮卡丘':('Hey You, Pikachu!','皮卡丘，你好！'),'宝可梦快照':('Pokémon Snap','宝可梦随乐拍'),'宝可梦谜题联盟':('Pokémon Puzzle League','宝可梦方块联盟'),'罪与罚：地球的继承人':('Sin and Punishment: Successor of the Earth','罪与罚：地球的继承人'),'马里奥网球64':('Mario Tennis','马力欧网球 64'),'马里奥高尔夫64':('Mario Golf','马力欧高尔夫 64'),'炸弹人64':('Bomberman 64','炸弹人 64'),'马里奥派对1/2/3':('Mario Party 1 / 2 / 3','马力欧派对 1／2／3'),'恐龙猎人Turok 1':('Turok: Dinosaur Hunter','恐龙猎人'),'恐龙猎人Turok 2':('Turok 2: Seeds of Evil','恐龙猎人 2：邪恶之种'),'星球大战Rogue Squadron':('Star Wars: Rogue Squadron','星球大战：侠盗中队'),'星球大战阴影帝国':('Star Wars: Shadows of the Empire','星球大战：帝国的阴影'),
'恶魔城：血之轮回':('Akumajou Dracula X: Chi no Rondo / Castlevania: Rondo of Blood','恶魔城 X：血之轮回'),'天外魔境Ziria':('Tengai Makyou: Ziria','天外魔境：自来也'),'PC原人1':('Bonk’s Adventure / PC Genjin','PC 原人'),'PC原人2':('Bonk’s Revenge / PC Genjin 2','PC 原人 2'),'PC原人3':('Bonk 3: Bonk’s Big Adventure / PC Genjin 3','PC 原人 3'),'Ys I&II':('Ys Book I & II','伊苏 I・II'),'天外魔境II 卍MARU':('Tengai Makyou II: Manji Maru','天外魔境 II：卍丸'),'天外魔境风云カブキ伝':('Tengai Makyou: Fuun Kabuki Den','天外魔境：风云歌舞伎传'),'Ys III':('Ys III: Wanderers from Ys','伊苏 III：来自伊苏的冒险者'),'Ys IV':('Ys IV: The Dawn of Ys','伊苏 IV：伊苏的黎明'),
'宝可梦 火红/叶绿':('Pokémon FireRed / LeafGreen','宝可梦：火红／叶绿'),'宝可梦 绿宝石':('Pokémon Emerald','宝可梦：绿宝石'),'黄金太阳：开启的封印':('Golden Sun','黄金太阳：开启的封印'),'黄金太阳：失落的时代':('Golden Sun: The Lost Age','黄金太阳：失落的时代'),'火焰之纹章：封印之剑':('Fire Emblem: The Binding Blade','火焰之纹章：封印之剑'),'火焰之纹章：烈火之剑':('Fire Emblem: The Blazing Blade','火焰之纹章：烈火之剑'),'火焰之纹章：圣魔之光石':('Fire Emblem: The Sacred Stones','火焰之纹章：圣魔之光石'),
'恶魔城：晓月圆舞曲':('Castlevania: Aria of Sorrow','恶魔城：晓月圆舞曲'),'恶魔城：白夜协奏曲':('Castlevania: Harmony of Dissonance','恶魔城：白夜协奏曲'),'恶魔城：月轮':('Castlevania: Circle of the Moon','恶魔城：月之轮回'),'逆转裁判1':('Gyakuten Saiban / Phoenix Wright: Ace Attorney','逆转裁判'),'逆转裁判2':('Gyakuten Saiban 2 / Phoenix Wright: Ace Attorney – Justice for All','逆转裁判 2'),'逆转裁判3':('Gyakuten Saiban 3 / Phoenix Wright: Ace Attorney – Trials and Tribulations','逆转裁判 3'),
'超级马力欧Advance 1':('Super Mario Advance','超级马力欧 Advance（超级马力欧兄弟 2）'),'超级马力欧Advance 2：耀西岛':('Super Mario World: Super Mario Advance 2','超级马力欧世界：超级马力欧 Advance 2'),'超级马力欧Advance 3':('Yoshi’s Island: Super Mario Advance 3','耀西岛：超级马力欧 Advance 3'),'超级马力欧Advance 4':('Super Mario Advance 4: Super Mario Bros. 3','超级马力欧 Advance 4：超级马力欧兄弟 3'),'马力欧与路易吉RPG':('Mario & Luigi: Superstar Saga','马力欧与路易吉 RPG'),
'洛克人Zero 1':('Mega Man Zero','洛克人 Zero'),'洛克人Zero 2':('Mega Man Zero 2','洛克人 Zero 2'),'洛克人Zero 3':('Mega Man Zero 3','洛克人 Zero 3'),'洛克人Zero 4':('Mega Man Zero 4','洛克人 Zero 4'),'洛克人EXE':('Mega Man Battle Network','洛克人 EXE'),'洛克人EXE2':('Mega Man Battle Network 2','洛克人 EXE 2'),'洛克人EXE3':('Mega Man Battle Network 3: Blue / White','洛克人 EXE 3：蓝／白'),
'星之卡比：镜之大迷宫':('Kirby & the Amazing Mirror','星之卡比：镜之大迷宫'),'密特罗德融合':('Metroid Fusion','密特罗德：融合'),'密特罗德零点任务':('Metroid: Zero Mission','密特罗德：零点任务'),
'最终幻想4 Advance':('Final Fantasy IV Advance','最终幻想 IV Advance'),'最终幻想5 Advance':('Final Fantasy V Advance','最终幻想 V Advance'),'最终幻想6 Advance':('Final Fantasy VI Advance','最终幻想 VI Advance'),'高级战争1':('Advance Wars','高级战争'),'高级战争2':('Advance Wars 2: Black Hole Rising','高级战争 2：黑洞崛起'),'最终幻想战略版Advance':('Final Fantasy Tactics Advance','最终幻想战略版 Advance'),
'机器人大战A':('Super Robot Taisen A','超级机器人大战 A'),'机器人大战R':('Super Robot Taisen R','超级机器人大战 R'),'机器人大战D':('Super Robot Taisen D','超级机器人大战 D'),'机器人大战J':('Super Robot Taisen J','超级机器人大战 J'),'塞尔达缩小帽':('The Legend of Zelda: The Minish Cap','塞尔达传说：缩小帽'),'牧场物语矿石镇的伙伴们':('Harvest Moon: Friends of Mineral Town','牧场物语：矿石镇的伙伴们'),'瓦力欧制造':('WarioWare, Inc.: Mega Microgame$!','瓦力欧制造：超迷你游戏'),'瓦力欧大陆Advance 4':('Wario Land 4','瓦力欧乐园 4'),'马里奥赛车Advance':('Mario Kart: Super Circuit','马力欧卡丁车 Advance'),
'索尼克Advance 1':('Sonic Advance','索尼克 Advance'),'索尼克Advance 2':('Sonic Advance 2','索尼克 Advance 2'),'索尼克Advance 3':('Sonic Advance 3','索尼克 Advance 3'),'光明之魂1':('Shining Soul','光明之魂'),'光明之魂2':('Shining Soul II','光明之魂 II'),'博德之门：黑暗联盟':('Baldur’s Gate: Dark Alliance','博德之门：黑暗联盟'),'龙珠Z舞空斗剧':('Dragon Ball Z: Supersonic Warriors','龙珠 Z：舞空斗剧'),'火影忍者系列':('Naruto: Ninja Council 1 / 2','火影忍者：忍者议会 1／2'),'王国之心记忆之链':('Kingdom Hearts: Chain of Memories','王国之心：记忆之链'),'游戏王':('Yu-Gi-Oh! The Eternal Duelist Soul','游戏王：永恒决斗者之魂'),'我们的太阳Boktai':('Boktai: The Sun Is in Your Hand','我们的太阳'),'马里奥高尔夫Advance':('Mario Golf: Advance Tour','马力欧高尔夫 Advance Tour'),'马里奥网球Advance':('Mario Tennis: Power Tour','马力欧网球 Power Tour'),'超级猴子球':('Super Monkey Ball Jr.','超级猴子球 Jr.'),'钻地先生A':('Mr. Driller A: Fushigi na Pacteria','钻地先生 A'),'合金弹头Advance':('Metal Slug Advance','合金弹头 Advance'),
'宝可梦心金/魂银':('Pokémon HeartGold / SoulSilver','宝可梦：心金／魂银'),'宝可梦白金':('Pokémon Platinum','宝可梦：白金'),'宝可梦黑/白1':('Pokémon Black / White','宝可梦：黑／白'),'宝可梦黑/白2':('Pokémon Black 2 / White 2','宝可梦：黑 2／白 2'),
'逆转裁判123（DS版）':('Phoenix Wright: Ace Attorney / Justice for All / Trials and Tribulations (DS)','逆转裁判 1／2／3（NDS 版）'),'逆转检事1':('Ace Attorney Investigations: Miles Edgeworth','逆转检事'),'逆转检事2':('Gyakuten Kenji 2 / Ace Attorney Investigations 2','逆转检事 2'),'幽灵诡计Ghost Trick':('Ghost Trick: Phantom Detective','幽灵诡计：幻影侦探'),
'雷顿教授：不可思议城镇':('Professor Layton and the Curious Village','雷顿教授与不可思议的小镇'),'雷顿教授：魔神之笛':('Professor Layton and the Last Specter','雷顿教授与魔神之笛'),'雷顿教授：最后的时间旅行':('Professor Layton and the Unwound Future','雷顿教授与最后的时间旅行'),
'新超级马力欧兄弟':('New Super Mario Bros.','新超级马力欧兄弟'),'超级马力欧64 DS':('Super Mario 64 DS','超级马力欧 64 DS'),'塞尔达：幻影沙钟':('The Legend of Zelda: Phantom Hourglass','塞尔达传说：幻影沙漏'),'塞尔达：大地的汽笛':('The Legend of Zelda: Spirit Tracks','塞尔达传说：大地的汽笛'),
'恶魔城：苍月的十字架':('Castlevania: Dawn of Sorrow','恶魔城：苍月十字架'),'恶魔城：废墟的肖像':('Castlevania: Portrait of Ruin','恶魔城：迷宫回廊'),'恶魔城：被夺走的刻印':('Castlevania: Order of Ecclesia','恶魔城：被夺走的刻印'),
'勇者斗恶龙9':('Dragon Quest IX: Sentinels of the Starry Skies','勇者斗恶龙 IX：星空的守护者'),'高级战争：双重打击':('Advance Wars: Dual Strike','高级战争：双重打击'),'火焰之纹章：新·暗黑龙与光之剑':('Fire Emblem: Shadow Dragon','火焰之纹章：新·暗黑龙与光之剑'),'火焰之纹章：新·纹章之谜':('Fire Emblem: New Mystery of the Emblem','火焰之纹章：新·纹章之谜'),
'重装机兵3':('Metal Max 3','重装机兵 3'),'重装机兵：钢之季节':('Metal Saga: Hagane no Kisetsu','重装机兵：钢之季节'),'机器人大战W':('Super Robot Taisen W','超级机器人大战 W'),'机器人大战K':('Super Robot Taisen K','超级机器人大战 K'),'机器人大战L':('Super Robot Taisen L','超级机器人大战 L'),
'节奏天国':('Rhythm Heaven / Rhythm Tengoku Gold','节奏天国'),'动物之森':('Animal Crossing: Wild World','欢迎来到动物森友会'),'世界树迷宫1':('Etrian Odyssey','世界树迷宫'),'世界树迷宫2':('Etrian Odyssey II: Heroes of Lagaard','世界树迷宫 II：诸王的圣杯'),'999：极限脱出':('999: Nine Hours, Nine Persons, Nine Doors','极限脱出：9 小时 9 人 9 扇门'),'闪电十一人1':('Inazuma Eleven','闪电十一人'),'闪电十一人2':('Inazuma Eleven 2: Kyoui no Shinryakusha – Fire / Blizzard','闪电十一人 2：威胁的侵略者'),'王国之心358/2天':('Kingdom Hearts 358/2 Days','王国之心：358/2 天'),'数码宝贝日光/月光':('Digimon World Dawn / Dusk','数码宝贝传说：日光／月光'),'符文工房1':('Rune Factory: A Fantasy Harvest Moon','符文工房：新牧场物语'),'符文工房2':('Rune Factory 2: A Fantasy Harvest Moon','符文工房 2'),'牧场物语：风之集市':('Harvest Moon: Grand Bazaar','牧场物语：风之集市'),'马里奥赛车DS':('Mario Kart DS','马力欧卡丁车 DS'),'耀西岛DS':('Yoshi’s Island DS','耀西岛 DS'),'洛克人ZX':('Mega Man ZX','洛克人 ZX'),'洛克人ZX Advent':('Mega Man ZX Advent','洛克人 ZX Advent'),'流星洛克人':('Mega Man Star Force: Pegasus / Leo / Dragon','流星洛克人：天马／雄狮／天龙'),'黄金太阳：漆黑的黎明':('Golden Sun: Dark Dawn','黄金太阳：漆黑的黎明'),'最终幻想3（DS重制版）':('Final Fantasy III (Nintendo DS)','最终幻想 III（NDS 重制版）'),'最终幻想4（DS重制版）':('Final Fantasy IV (Nintendo DS)','最终幻想 IV（NDS 重制版）'),'沙加2：秘宝传说（DS重制）':('SaGa 2: Hihou Densetsu – Goddess of Destiny','沙加 2：秘宝传说－命运女神'),'晶体编年史：时之回声':('Final Fantasy Crystal Chronicles: Echoes of Time','最终幻想水晶编年史：时之回声'),'勇者斗恶龙怪兽篇Joker 1':('Dragon Quest Monsters: Joker','勇者斗恶龙怪兽篇 Joker'),'勇者斗恶龙怪兽篇Joker 2':('Dragon Quest Monsters: Joker 2','勇者斗恶龙怪兽篇 Joker 2'),
'宝可梦不可思议迷宫：青救助队':('Pokémon Mystery Dungeon: Blue Rescue Team','宝可梦不可思议迷宫：青救助队'),'宝可梦不可思议迷宫：时之探险队':('Pokémon Mystery Dungeon: Explorers of Time','宝可梦不可思议迷宫：时之探险队'),'宝可梦不可思议迷宫：暗之探险队':('Pokémon Mystery Dungeon: Explorers of Darkness','宝可梦不可思议迷宫：暗之探险队'),'宝可梦不可思议迷宫：空之探险队':('Pokémon Mystery Dungeon: Explorers of Sky','宝可梦不可思议迷宫：空之探险队'),'宝可梦护林员':('Pokémon Ranger','宝可梦护林员'),'应援团/Elite Beat Agents':('Osu! Tatakae! Ouendan / Elite Beat Agents','押忍！战斗！应援团／节拍特工'),'瓦力欧制造：触摸':('WarioWare: Touched!','摸摸瓦力欧制造'),'大合奏！バンドブラザーズ':('Daigasso! Band Brothers','大合奏！乐团兄弟'),'脑锻炼':('Brain Age: Train Your Brain in Minutes a Day!','成年人的 DS 脑力锻炼'),'任天狗':('Nintendogs','任天狗'),'料理妈妈':('Cooking Mama','料理妈妈'),
'莎木1':('Shenmue','莎木'),'莎木2':('Shenmue II','莎木 II'),'死或生2':('Dead or Alive 2','死或生 2'),'灵魂能力Soul Calibur':('Soulcalibur','灵魂能力'),'街头霸王III：Double Impact':('Street Fighter III: Double Impact','街头霸王 III：双重冲击（New Generation＋2nd Impact）'),'疯狂出租车Crazy Taxi':('Crazy Taxi','疯狂出租车'),'生化危机：代号维罗妮卡':('Resident Evil – Code: Veronica','生化危机：代号维罗妮卡'),'斑鸠Ikaruga':('Ikaruga','斑鸠'),'索尼克大冒险':('Sonic Adventure','索尼克大冒险'),'索尼克大冒险2':('Sonic Adventure 2','索尼克大冒险 2'),'能量宝石Power Stone 1':('Power Stone','能量宝石'),'能量宝石Power Stone 2':('Power Stone 2','能量宝石 2'),'漫威vs卡普空1':('Marvel vs. Capcom: Clash of Super Heroes','漫威对卡普空：超级英雄冲突'),'漫威vs卡普空2':('Marvel vs. Capcom 2: New Age of Heroes','漫威对卡普空 2：英雄新纪元'),'卡普空vsSNK 1':('Capcom vs. SNK: Millennium Fight 2000','卡普空对 SNK：千年之战 2000'),'卡普空vsSNK 2':('Capcom vs. SNK 2: Mark of the Millennium 2001','卡普空对 SNK 2：2001 千年印记'),'罪恶工具Guilty Gear X':('Guilty Gear X','罪恶装备 X'),'樱花大战3':('Sakura Wars 3: Is Paris Burning?','樱花大战 3：巴黎在燃烧吗'),'樱花大战4':('Sakura Wars 4: Fall in Love, Maidens','樱花大战 4：恋爱吧少女'),'梦幻之星在线':('Phantasy Star Online','梦幻之星在线'),'格兰蒂亚II':('Grandia II','格兰蒂亚 II'),'世嘉拉力2':('Sega Rally 2','世嘉拉力锦标赛 2'),'太空频道5 Part 2':('Space Channel 5: Part 2','太空频道 5：第二章'),'死亡之屋2':('The House of the Dead 2','死亡之屋 2'),'玩具指挥官Toy Commander':('Toy Commander','玩具指挥官'),'蓝天战队Blue Stinger':('Blue Stinger','蓝刺'),'疯狂出租车2':('Crazy Taxi 2','疯狂出租车 2'),
'怪物猎人携带版3rd':('Monster Hunter Portable 3rd','怪物猎人携带版 3rd'),'怪物猎人携带版2nd G':('Monster Hunter Freedom Unite / Monster Hunter Portable 2nd G','怪物猎人携带版 2nd G'),
'英雄传说：空之轨迹FC':('The Legend of Heroes: Trails in the Sky FC','英雄传说：空之轨迹 FC'),'英雄传说：空之轨迹SC':('The Legend of Heroes: Trails in the Sky SC','英雄传说：空之轨迹 SC'),'英雄传说：空之轨迹 the 3rd':('The Legend of Heroes: Trails in the Sky the 3rd','英雄传说：空之轨迹 the 3rd'),'英雄传说：零之轨迹':('The Legend of Heroes: Zero no Kiseki','英雄传说：零之轨迹'),'英雄传说：碧之轨迹':('The Legend of Heroes: Ao no Kiseki','英雄传说：碧之轨迹'),'那由多之轨迹':('Nayuta no Kiseki / The Legend of Nayuta: Boundless Trails','那由多之轨迹'),'英雄传说：卡卡布三部曲':('The Legend of Heroes II: Prophecy of the Moonlight Witch / III: White Witch / IV: A Tear of Vermillion / V: Cagesong of the Ocean','英雄传说：卡卡布三部曲'),
'最终幻想7：核心危机':('Crisis Core: Final Fantasy VII','核心危机：最终幻想 VII'),'寄生前夜：第三次生日':('The 3rd Birthday','寄生前夜：第三次生日'),'女神异闻录3携带版':('Shin Megami Tensei: Persona 3 Portable','女神异闻录 3 携带版'),'山脊赛车':('Ridge Racer','山脊赛车'),'初音未来：歌姬计划2nd':('Hatsune Miku: Project DIVA 2nd','初音未来：歌姬计划 2nd'),'初音未来：歌姬计划Extend':('Hatsune Miku: Project DIVA Extend','初音未来：歌姬计划扩展版'),'铁拳6':('Tekken 6','铁拳 6'),'侠盗猎车手：自由城故事':('Grand Theft Auto: Liberty City Stories','侠盗猎车手：自由城故事'),'超级机器人大战A Portable':('Super Robot Taisen A Portable','超级机器人大战 A Portable'),'最终幻想战略版：狮子战争':('Final Fantasy Tactics: The War of the Lions','最终幻想战略版：狮子战争'),'三国志7':('Romance of the Three Kingdoms VII','三国志 VII'),'伊苏1&2':('Ys I & II Chronicles','伊苏 I・II 编年史'),'伊苏：菲尔盖纳之誓约':('Ys: The Oath in Felghana','伊苏：菲尔盖纳的誓约'),'伊苏7':('Ys Seven','伊苏 VII'),'战场女武神2':('Valkyria Chronicles II','战场女武神 2'),'战场女武神3':('Valkyria Chronicles III','战场女武神 3'),'魔界战记：便携版':('Disgaea: Afternoon of Darkness','魔界战记：黄昏的黑暗'),'王国之心：梦中降生Birth by Sleep':('Kingdom Hearts: Birth by Sleep','王国之心：梦中降生'),'高达VS高达NEXT PLUS':('Mobile Suit Gundam: Gundam vs. Gundam Next Plus','机动战士高达：高达对高达 NEXT PLUS'),'真三国无双：联合突袭':('Dynasty Warriors: Strikeforce','真·三国无双：联合突袭'),'乐克乐克LocoRoco':('LocoRoco','乐克乐克'),'啪嗒砰Patapon':('Patapon','啪嗒砰'),'大众高尔夫':('Everybody’s Golf / Hot Shots Golf','大众高尔夫'),'湾岸午夜俱乐部':('Midnight Club 3: DUB Edition','午夜俱乐部 3：DUB 版'),'火爆狂飙：传奇':('Burnout Legends','火爆狂飙：传奇'),'寂静岭：起源':('Silent Hill: Origins','寂静岭：起源'),'寂静岭：破碎的记忆':('Silent Hill: Shattered Memories','寂静岭：破碎的记忆'),'秋之回忆/CLANNAD/命运石之门/寒蝉/Fate/Extra':('Memories Off / Clannad / Steins;Gate / Higurashi / Fate/Extra','秋之回忆／CLANNAD／命运石之门／寒蝉／Fate/EXTRA（分卷收藏）'),'刺客信条：血统':('Assassin’s Creed: Bloodlines','刺客信条：血统'),'荣誉勋章：英雄':('Medal of Honor: Heroes','荣誉勋章：英雄'),'抵抗：惩罚':('Resistance: Retribution','抵抗：惩罚'),'合金装备：和平行者':('Metal Gear Solid: Peace Walker','合金装备：和平行者'),'最终幻想零式Type-0':('Final Fantasy Type-0','最终幻想：零式'),'战神：奥林匹斯之链':('God of War: Chains of Olympus','战神：奥林匹斯之链'),'战神：斯巴达之魂':('God of War: Ghost of Sparta','战神：斯巴达之魂'),'最终幻想纷争':('Dissidia Final Fantasy','最终幻想：纷争'),'火影忍者：疾风传终极觉醒3':('Naruto Shippuden: Ultimate Ninja Heroes 3','火影忍者疾风传：终极英雄 3'),
'生化危机1':('Resident Evil','生化危机'),'生化危机3':('Resident Evil 3: Nemesis','生化危机 3：复仇女神'),'恶魔城X：月下夜想曲':('Castlevania: Symphony of the Night','恶魔城 X：月下夜想曲'),'最终幻想7':('Final Fantasy VII','最终幻想 VII'),'最终幻想8':('Final Fantasy VIII','最终幻想 VIII'),'最终幻想9':('Final Fantasy IX','最终幻想 IX'),'最终幻想战略版':('Final Fantasy Tactics','最终幻想战略版'),'合金装备':('Metal Gear Solid','合金装备'),'寄生前夜1':('Parasite Eve','寄生前夜'),'寄生前夜2':('Parasite Eve II','寄生前夜 II'),'放浪冒险谭':('Vagrant Story','放浪冒险谭'),'异度装甲':('Xenogears','异度装甲'),'三国志5':('Romance of the Three Kingdoms V','三国志 V'),'三国志6':('Romance of the Three Kingdoms VI','三国志 VI'),'信长之野望：将星录':('Nobunaga’s Ambition: Shouseiroku','信长之野望：将星录'),'信长之野望：烈风传':('Nobunaga’s Ambition: Reppuuden','信长之野望：烈风传'),
'超级机器人大战α':('Super Robot Taisen Alpha','超级机器人大战 α'),'超级机器人大战α外传':('Super Robot Taisen Alpha Gaiden','超级机器人大战 α 外传'),'超级机器人大战第2次':('Dai-2-Ji Super Robot Taisen (PlayStation)','第 2 次超级机器人大战（PS 重制版）'),'前线任务3':('Front Mission 3','前线任务 3'),'皇家骑士团2':('Tactics Ogre: Let Us Cling Together (PlayStation)','皇家骑士团：命运之轮（PS 移植版）'),'寂静岭1':('Silent Hill','寂静岭'),'恐龙危机1':('Dino Crisis','恐龙危机'),'恐龙危机2':('Dino Crisis 2','恐龙危机 2'),'北欧女神Valkyrie Profile':('Valkyrie Profile','北欧女神'),'格兰蒂亚':('Grandia','格兰蒂亚'),'幻想水浒传1':('Suikoden','幻想水浒传'),'幻想水浒传2':('Suikoden II','幻想水浒传 II'),'时空之轮Chrono Cross':('Chrono Cross','时空之轮'),'星海传说2':('Star Ocean: The Second Story','星之海洋：第二个故事'),'龙骑士传说Legend of Dragoon':('The Legend of Dragoon','龙骑士传说'),'宿命传说':('Tales of Destiny','宿命传说'),'永恒传说Eternia':('Tales of Eternia','永恒传说'),'武藏传Brave Fencer Musashi':('Brave Fencer Musashi','武藏传'),'露娜银星故事':('Lunar: Silver Star Story Complete','露娜：银河之星'),'露娜永恒之蓝':('Lunar 2: Eternal Blue Complete','露娜 2：永恒之蓝'),'波波罗克罗伊斯':('Popolocrois Monogatari','波波罗克罗伊斯物语'),'钟楼Clock Tower':('Clock Tower: The First Fear','钟楼'),'古惑狼1-3':('Crash Bandicoot 1 / 2: Cortex Strikes Back / 3: Warped','古惑狼 1／2／3'),'小龙斯派罗1-3':('Spyro the Dragon 1 / 2: Ripto’s Rage! / 3: Year of the Dragon','小龙斯派罗 1／2／3'),'铁拳3':('Tekken 3','铁拳 3'),'山脊赛车Type 4':('R4: Ridge Racer Type 4','山脊赛车 Type 4'),'GT赛车1':('Gran Turismo','GT 赛车'),'GT赛车2':('Gran Turismo 2','GT 赛车 2'),'古墓丽影1-3':('Tomb Raider I / II / III','古墓丽影 1／2／3'),'吊索奇兵Syphon Filter':('Syphon Filter','虹吸战士'),'捉猴啦Ape Escape':('Ape Escape','捉猴啦'),'实况足球WEP系列':('Winning Eleven / Pro Evolution Soccer (PlayStation)','实况足球：胜利十一人系列'),'恶魔城Chronicle':('Castlevania Chronicles','恶魔城年代记'),'数码宝贝世界1':('Digimon World','数码宝贝世界'),'数码宝贝世界2':('Digimon World 2','数码宝贝世界 2'),'数码宝贝世界3':('Digimon World 3 / 2003','数码宝贝世界 3'),'高达系列（基连野望等）':('Mobile Suit Gundam: Gihren’s Greed and related PlayStation titles','机动战士高达：基连的野望等系列'),'龙珠Final Bout':('Dragon Ball GT: Final Bout','龙珠 GT：最终决战'),'同级生2/下级生/To Heart':('Doukyuusei 2 / Kakyuusei / To Heart','同级生 2／下级生／To Heart'),'心跳回忆1/2':('Tokimeki Memorial 1 / 2','心跳回忆 1／2'),'前线任务Alternative':('Front Mission Alternative','前线任务 Alternative'),
}

pubfix = {
'赤影战士':'Natsume','坦克大战':'Namco','马戏团':'Konami','中原之霸者':'Namco','霸王的大陆':'Namco','最终幻想':'Square','最终幻想2':'Square','最终幻想3':'Square','勇者斗恶龙':'Enix','勇者斗恶龙2':'Enix','勇者斗恶龙3':'Enix','勇者斗恶龙4':'Enix','松鼠大战':'Capcom','松鼠大战2':'Capcom','唐老鸭梦冒险':'Capcom','唐老鸭梦冒险2':'Capcom','天使之翼':'Tecmo','天使之翼2':'Tecmo','圣火徽章外传':'Nintendo','吞食天地':'Capcom','吞食天地2':'Capcom','封神榜':'全崴资讯','西游记世界':'Jaleco','影子传说':'Taito','忍者茶茶丸':'Jaleco','小叮当':'Hudson Soft','挖金矿Lode Runner':'Hudson Soft','功夫Yie Ar Kung-Fu':'Konami','龙珠 大魔神':'Bandai','圣斗士星矢 黄金传说':'Bandai','北斗神拳':'Toei Animation',
'瓦力欧乐园':'Nintendo','恶魔城德古拉传说1':'Konami','恶魔城德古拉传说2':'Konami','恶魔城Legends':'Konami','七龙珠GB系列':'Bandai','圣斗士GB':'Bandai',
'大战略':'Sega','Thunder Force III':'Technosoft','Thunder Force IV':'Technosoft','Mega Man: The Wily Wars':'Capcom','Rock n\' Roll Racing':'Interplay','超级街霸2':'Capcom','星之海洋':'Enix','Bahamut Lagoon':'Square','Illusion of Gaia':'Enix','E.V.O.':'Enix','Lufia 1':'Taito','Lufia 2':'Natsume','ActRaiser':'Enix','Soul Blazer':'Enix','Goemon 神秘历险':'Konami','Parodius':'Konami','TwinBee':'Konami','Darius Twin':'Taito','Arcana':'HAL Laboratory','Robotrek':'Enix','Another World':'Interplay','Lemmings':'Psygnosis',
'罪与罚：地球的继承人':'Nintendo','1080° Snowboarding':'Nintendo','Wave Race 64':'Nintendo',
'PC原人1':'Hudson Soft','PC原人2':'Hudson Soft','PC原人3':'Hudson Soft','Ys I&II':'Hudson Soft','Raiden':'Hudson Soft','Darius Plus':'NEC Avenue','Gate of Thunder':'Hudson Soft','Lords of Thunder':'Hudson Soft','Alien Crush':'Naxat Soft','Devil\'s Crush':'Naxat Soft','Blazing Lazers / Gunhed':'Hudson Soft','Military Madness':'NEC','Legendary Axe':'Victor','Cosmo Fantasy':'Telenet Japan','Valis 1-4':'Telenet Japan','Cotton':'Hudson Soft','Dead Moon':'Natsume','Image Fight':'Irem','Download 1&2':'NEC Avenue','ときめきメモリアル':'Konami','源平讨魔伝':'Namco','スーパー桃太郎電鉄':'Hudson Soft',
'光明之魂1':'Sega','光明之魂2':'Sega','博德之门：黑暗联盟':'Destination Software','超级猴子球':'Sega','Original Generation 1':'Banpresto','Original Generation 2':'Banpresto',
'料理妈妈':'Taito / 505 Games','重装机兵：钢之季节':'Success','重装机兵3':'Kadokawa Games',
'吞食天地2赤壁之战':'Capcom','电精1':'Banpresto','电精2':'Banpresto','午夜杀生Night Slashers':'Data East','D&D毁灭之塔':'Capcom','D&D暗影之谜':'Capcom','AVP异形VS铁血战士':'Capcom','三个奇迹':'Capcom','X-Men vs SF':'Capcom','Capcom vs SNK 1':'Capcom','Capcom vs SNK 2':'Capcom','Strikers 1945 Plus':'Psikyo','Xexex':'Konami','Galaxy Fight':'Sunsoft','Mars Matrix':'Capcom','Giga Wing 1':'Capcom','Giga Wing 2':'Capcom','Karnov':'Data East',
'格兰蒂亚II':'Game Arts / Ubisoft','蓝天战队Blue Stinger':'Sega','Carrier':'Jaleco','Bangai-O':'Treasure / Swing!','格兰蒂亚':'Game Arts / Sony','异度装甲':'Square','星海传说2':'Enix','龙骑士传说Legend of Dragoon':'Sony','古惑狼1-3':'Sony','小龙斯派罗1-3':'Sony','Panzer Front':'JVC / ASCII','Persona 1':'Atlus','Persona 2：Innocent Sin':'Atlus','Persona 2：Eternal Punishment':'Atlus',
'超级机器人大战A Portable':'Banpresto','湾岸午夜俱乐部':'Rockstar Games','伊苏1&2':'Falcom','伊苏：菲尔盖纳之誓约':'Falcom','伊苏7':'Falcom','高达VS高达NEXT PLUS':'Bandai Namco','火影忍者：疾风传终极觉醒3':'Bandai Namco',
}

# 榜单补漏与关键平台修正。en, zh, publisher, size, year
adds = {
'NES / FC': [
('Metroid','密特罗德','Nintendo','1MB','1986'),
('Super Mario Bros.: The Lost Levels','超级马力欧兄弟 2（日版）','Nintendo','0.25MB','1986'),
('Crystalis','天神之剑','SNK','0.5MB','1990'),
('Gimmick!','吉米克','Sunsoft','0.5MB','1992'),
('Metal Gear','合金装备','Konami','0.5MB','1987'),
('Kirby’s Adventure','星之卡比：梦之泉物语','Nintendo','1MB','1993'),
],
'GB / GBC': [
('Wario Land II','瓦力欧乐园 2','Nintendo','4MB','1998'),
('Super Mario Bros. Deluxe','超级马力欧兄弟 DX','Nintendo','4MB','1999'),
('Survival Kids','生存少年','Konami','4MB','1999'),
('Star Ocean: Blue Sphere','星之海洋：蔚蓝星球','Enix','8MB','2001'),
('Mega Man Xtreme','洛克人 X：电子任务','Capcom','4MB','2000'),
('Donkey Kong (Game Boy)','咚奇刚（GB）','Nintendo','4MB','1994'),
('Kirby’s Dream Land 1 / 2','星之卡比／星之卡比 2','Nintendo','4MB','1992–1995'),
],
'MD / Genesis': [
('Shining Force','光明力量','Sega','4MB','1992'),
('Shining Force II: Ancient Sealing','光明力量 II：远古封印','Sega','4MB','1993'),
('Rocket Knight Adventures','火箭骑士历险记','Konami','4MB','1993'),
('Castlevania: Bloodlines','恶魔城：血族','Konami','4MB','1994'),
('Strider','出击飞龙','Capcom / Sega','4MB','1990'),
('Dynamite Headdy','炸弹头','Sega','4MB','1994'),
('Raiden Trad','雷电传统版','Micronet / Sega','4MB','1991'),
('R-Type','异形战机','Irem / Sega','4MB','1991'),
('Landstalker: The Treasures of King Nole','秘境魔宝：皇帝的财宝','Sega','4MB','1992'),
('Wonder Boy in Monster World','神奇男孩：怪物世界','Sega','4MB','1991'),
],
'SNES / SFC': [
('Super Castlevania IV','超级恶魔城 IV','Konami','4MB','1991'),
('Metal Max 2','重装机兵 2','Data East','8MB','1993'),
('Shin Megami Tensei I / II','真·女神转生 I／II','Atlus','16MB','1992–1994'),
('Super Mario All-Stars','超级马力欧合集','Nintendo','8MB','1993'),
('Super Punch-Out!!','超级拳无虚发','Nintendo','4MB','1994'),
('Ogre Battle: The March of the Black Queen','皇家骑士团：黑色皇后','Quest / Enix','8MB','1993'),
('Donkey Kong Country Returns (not included)','', '', '', ''),
],
'N64': [
('Rayman 2: The Great Escape','雷曼 2：胜利大逃亡','Ubisoft','16MB','1999'),
('Ogre Battle 64: Person of Lordly Caliber','皇家骑士团 64：王者之风','Nintendo','40MB','1999'),
('Mystical Ninja Starring Goemon','大盗五右卫门：桃山幕府之舞','Konami','16MB','1997'),
('Mischief Makers','淘气制造者','Nintendo','8MB','1997'),
],
'PCE (PC Engine / TurboGrafx-16)': [
('Seirei Senshi Spriggan','精灵战记 Spriggan','Naxat Soft','64MB','1991'),
('Ginga Fukei Densetsu Sapphire','银河妇警传说 Sapphire','Hudson Soft','128MB','1995'),
('Parasol Stars: The Story of Bubble Bobble III','阳伞之星：泡泡龙 III','Taito','8MB','1991'),
('Magical Chase','魔法追击','NEC Avenue','8MB','1991'),
('Bonk’s Revenge CD / PC Genjin 2','PC 原人 2（CD 音轨版）','Hudson Soft','64MB','1993'),
],
'GBA': [
('Pokémon Ruby / Sapphire','宝可梦：红宝石／蓝宝石','Nintendo','16MB','2002'),
('Pokémon Mystery Dungeon: Red Rescue Team','宝可梦不可思议迷宫：赤救助队','Nintendo','32MB','2005'),
('Rhythm Tengoku','节奏天国','Nintendo','16MB','2006'),
('Ninja Five-O','忍者刑警','Konami','8MB','2003'),
('Klonoa: Empire of Dreams','风之少年：梦之帝国','Namco','8MB','2001'),
('Astro Boy: Omega Factor','铁臂阿童木：原子心的秘密','Sega','16MB','2003'),
('Mario vs. Donkey Kong','马力欧对咚奇刚','Nintendo','16MB','2004'),
('Final Fantasy I & II: Dawn of Souls','最终幻想 I・II：灵魂黎明','Square Enix','16MB','2004'),
('Tactics Ogre: The Knight of Lodis','皇家骑士团外传：罗迪斯的骑士','Nintendo / Atlus','16MB','2001'),
('Dragon Ball: Advanced Adventure','龙珠大冒险','Atari / Bandai','16MB','2004'),
('Kirby: Nightmare in Dream Land','星之卡比：梦之泉豪华版','Nintendo','16MB','2002'),
('Gunstar Super Heroes','超级火枪英雄','Sega','16MB','2005'),
('WarioWare Twisted!','转转瓦力欧制造','Nintendo','16MB','2004'),
],
'NDS': [
('Shin Megami Tensei: Strange Journey','真·女神转生：奇妙之旅','Atlus','128MB','2009'),
('Okamiden','大神传：小小太阳','Capcom','128MB','2010'),
('Final Fantasy Tactics A2: Grimoire of the Rift','最终幻想战略版 A2：封穴的魔法书','Square Enix','128MB','2007'),
('Grand Theft Auto: Chinatown Wars','侠盗猎车手：唐人街战争','Rockstar Games','128MB','2009'),
('Kirby: Canvas Curse','触摸！卡比','Nintendo','64MB','2005'),
('Kirby: Squeak Squad','星之卡比：参上！怪盗洛切团','Nintendo','64MB','2006'),
('Mario & Luigi: Partners in Time','马力欧与路易吉 RPG 2×2','Nintendo','64MB','2005'),
('Mario & Luigi: Bowser’s Inside Story','马力欧与路易吉 RPG 3!!!','Nintendo','128MB','2009'),
('The World Ends with You','美妙世界','Square Enix','128MB','2007'),
('Castlevania: The Dracula X Chronicles (not included)','', '', '', ''),
],
'街机（FBNeo / MAME）': [
('Batsugun','蝙蝠枪','Toaplan','20MB','1993'),
('Blazing Star','闪亮之星','Yumekobo / SNK','60MB','1998'),
('Golden Axe: The Revenge of Death Adder','战斧：死亡蝰蛇的复仇','Sega','60MB','1992'),
('In the Hunt','海底大战争','Irem','40MB','1993'),
('Metal Slug 1 / 2 / X / 3 / 4 / 5','合金弹头系列','SNK','400MB','1996–2003'),
('Pac-Man / Ms. Pac-Man','吃豆人／吃豆人小姐','Namco / Midway','2MB','1980–1982'),
('Donkey Kong / Donkey Kong Jr.','咚奇刚／咚奇刚 Jr.','Nintendo','2MB','1981–1982'),
('Galaga / Galaxian','大蜜蜂／小蜜蜂','Namco','2MB','1979–1981'),
('Dig Dug','打气人','Namco','2MB','1982'),
('Street Fighter II: Champion Edition','街头霸王 II：冠军版','Capcom','20MB','1992'),
],
'Dreamcast': [
('Skies of Arcadia','永恒的阿卡迪亚','Sega','1.2GB','2000'),
('Street Fighter III: 3rd Strike','街头霸王 III：三度冲击','Capcom','700MB','2000'),
('Virtua Tennis / Virtua Tennis 2','VR 网球／VR 网球 2','Sega','1.2GB','2000–2001'),
('Metropolis Street Racer','大都会街头赛车','Sega','700MB','2000'),
('ChuChu Rocket!','啾啾火箭队','Sega','200MB','1999'),
('Project Justice','私立正义学园：热血青春日记 2','Capcom','800MB','2000'),
('Samba de Amigo','桑巴沙锤','Sega','400MB','2000'),
],
'PSP': [
('Hatsune Miku: Project DIVA','初音未来：歌姬计划','Sega','700MB','2009'),
('Grand Theft Auto: Chinatown Wars','侠盗猎车手：唐人街战争','Rockstar Games','1GB','2009'),
('Tekken: Dark Resurrection','铁拳：暗黑复苏','Bandai Namco','1GB','2006'),
('Wipeout Pure','反重力赛车：纯粹','Sony','400MB','2005'),
('Jeanne d’Arc','圣女贞德','Sony','700MB','2006'),
('Castlevania: The Dracula X Chronicles','恶魔城 X 历代记','Konami','800MB','2007'),
('Daxter','达斯特','Sony','900MB','2006'),
('LittleBigPlanet','小小大星球','Sony','1GB','2009'),
('Lumines II','音乐方块 II','Q Entertainment','300MB','2006'),
],
'PS1': [
('Tony Hawk’s Pro Skater','托尼·霍克职业滑板','Activision','400MB','1999'),
('Tony Hawk’s Pro Skater 2','托尼·霍克职业滑板 2','Activision','600MB','2000'),
('Crash Team Racing','古惑狼赛车','Sony','400MB','1999'),
('Dragon Quest VII: Fragments of the Forgotten Past','勇者斗恶龙 VII：伊甸的战士们','Enix','1GB','2000'),
('Klonoa: Door to Phantomile','风之少年：通往幻界之门','Namco','500MB','1997'),
('Rayman','雷曼','Ubisoft','400MB','1995'),
('Street Fighter Alpha 3','少年街霸 3','Capcom','600MB','1998'),
('Suikoden Tierkreis (not included)','', '', '', ''),
],
}

# 常见英文/日文原名规范化。
def infer_name(platform, old):
    if old in X:
        return X[old]
    # 去掉原稿的标记，保留完整英文商品名。
    clean = re.sub(r'^\[(?:删除|存疑|不存在)\]', '', old)
    latin = re.findall(r'[A-Za-z][A-Za-z0-9 .&’\'!:+°/–-]*', clean)
    if latin and not re.match(r'^[㐀-鿿]', clean):
        en = max(latin, key=len).strip(' -–')
        fixes = {
            'Langrisser':'Langrisser','Langrisser II':'Langrisser II','Shantae':'Shantae','Metal Gear Ghost Babel':'Metal Gear Solid: Ghost Babel','Dragon Warrior Monsters 1':'Dragon Warrior Monsters','Dragon Warrior Monsters 2':'Dragon Warrior Monsters 2: Cobi’s Journey / Tara’s Adventure',
            'Thunder Force III':'Thunder Force III','Thunder Force IV':'Thunder Force IV: Lightening Force','Mega Man: The Wily Wars':'Mega Man: The Wily Wars','Alien Soldier':'Alien Soldier','Gunstar Heroes':'Gunstar Heroes','Comix Zone':'Comix Zone','The Story of Thor':'Beyond Oasis / The Story of Thor','Earthworm Jim':'Earthworm Jim','Vectorman':'Vectorman','Ristar':'Ristar',
            'Jet Set Radio':'Jet Set Radio','Ikaruga':'Ikaruga','Rez':'Rez','Lumines':'Lumines','Patapon':'Patapon','LocoRoco':'LocoRoco',
        }
        en = fixes.get(en, en)
        return en, clean
    # 剩余的日文、合集和街机简称。
    known = {
        'ときめきメモリアル':'Tokimeki Memorial','大合奏！バンドブラザーズ':'Daigasso! Band Brothers',
        '电精1':'Guardians / Denjin Makai II','电精2':'Denjin Makai','午夜杀生Night Slashers':'Night Slashers',
        '三国战纪正宗Plus':'Knights of Valour Plus','三国战纪风云再起':'Knights of Valour: Super Heroes','三国战纪乱世枭雄':'Knights of Valour: The Seven Spirits','三国战纪七星转生':'Knights of Valour: The Seven Spirits (PGM2)',
        '吞食天地2赤壁之战':'Warriors of Fate / Tenchi wo Kurau II','西游释厄传':'Oriental Legend','西游释厄传Super':'Oriental Legend Super','西游释厄传群魔乱舞':'Oriental Legend: Qun Mo Luan Wu','西游释厄传2':'Oriental Legend 2',
        '恐龙快打':'Cadillacs and Dinosaurs','名将Captain Commando':'Captain Commando','圆桌骑士':'Knights of the Round','惩罚者The Punisher':'The Punisher','快打旋风Final Fight':'Final Fight',
        'D&D毁灭之塔':'Dungeons & Dragons: Tower of Doom','D&D暗影之谜':'Dungeons & Dragons: Shadow over Mystara','AVP异形VS铁血战士':'Alien vs. Predator','三个奇迹':'Three Wonders','龙王战士':'The King of Dragons','魔法剑':'Magic Sword: Heroic Fantasy',
        '战国传承3':'Sengoku 3 / Sengoku Denshou 2001','形意拳':'Martial Masters','傲剑狂刀':'The Killing Blade',
        '真侍魂：霸王丸地狱变':'Samurai Shodown II','侍魂1':'Samurai Shodown','侍魂2':'Samurai Shodown II','侍魂3':'Samurai Shodown III: Blades of Blood','侍魂4':'Samurai Shodown IV: Amakusa’s Revenge','侍魂天草降临':'Samurai Shodown IV: Amakusa’s Revenge','侍魂零':'Samurai Shodown V',
        '月华剑士1':'The Last Blade','月华剑士2':'The Last Blade 2','饿狼传说1':'Fatal Fury: King of Fighters','饿狼传说2':'Fatal Fury 2','饿狼传说3':'Fatal Fury 3: Road to the Final Victory','饿狼传说Real Bout':'Real Bout Fatal Fury','饿狼传说RB Special':'Real Bout Fatal Fury Special','龙虎之拳1':'Art of Fighting','龙虎之拳2':'Art of Fighting 2','世界英雄Perfect':'World Heroes Perfect','风云默示录1':'Kizuna Encounter: Super Tag Battle / Fu’un Super Combo','风云默示录2':'Savage Reign','Galaxy Fight':'Galaxy Fight: Universal Warriors','Kizuna Encounter':'Kizuna Encounter: Super Tag Battle','Windjammers':'Windjammers','Neo Turf Masters':'Neo Turf Masters','Twinkle Star Sprites':'Twinkle Star Sprites',
        '街头霸王2':'Street Fighter II: The World Warrior','街头霸王2 Hyper Fighting':'Street Fighter II: Hyper Fighting','街头霸王2 Super Turbo':'Super Street Fighter II Turbo','少年街霸Alpha 1':'Street Fighter Alpha: Warriors’ Dreams','少年街霸Alpha 2':'Street Fighter Alpha 2','少年街霸Alpha 3':'Street Fighter Alpha 3','街头霸王III New Generation':'Street Fighter III: New Generation','街头霸王III 2nd Impact':'Street Fighter III: 2nd Impact','街头霸王III 三度冲击':'Street Fighter III: 3rd Strike','恶魔战士Vampire Savior':'Vampire Savior: The Lord of Vampire','Marvel Super Heroes':'Marvel Super Heroes','X-Men vs SF':'X-Men vs. Street Fighter','MVC1':'Marvel vs. Capcom: Clash of Super Heroes','MVC2':'Marvel vs. Capcom 2: New Age of Heroes','红色大地Red Earth':'Red Earth / War-Zard','私立正义学园':'Rival Schools: United by Fate','JOJO的奇妙冒险':'JoJo’s Bizarre Adventure: Heritage for the Future','Capcom vs SNK 1':'Capcom vs. SNK: Millennium Fight 2000','Capcom vs SNK 2':'Capcom vs. SNK 2: Mark of the Millennium 2001',
        '打击者1945':'Strikers 1945','打击者1945 II':'Strikers 1945 II','打击者1945 III':'Strikers 1945 III / Strikers 1999','战国之刃':'Sengoku Blade: Sengoku Ace Episode II / Tengai','武装飞鸟2':'Gunbird 2','Sol Divide':'Sol Divide: The Sword of Darkness','Dragon Blaze':'Dragon Blaze','Strikers 1945 Plus':'Strikers 1945 Plus',
        '怒首领蜂':'DoDonPachi','大往生':'DoDonPachi Dai-Ou-Jou','ESP Ra.De.':'ESP Ra.De.','长空超少年Espgaluda':'Espgaluda','Progear 的岚':'Progear no Arashi / Progear','虎直升机':'Tiger Heli','飞翔鲛Same!Same!Same!':'Fire Shark / Same! Same! Same!','Truxton':'Truxton / Tatsujin','Vimana':'Vimana','OutZone':'Out Zone','Battle Garegga':'Battle Garegga','雷电1':'Raiden','雷电2':'Raiden II','R-Type':'R-Type','R-Type Leo':'R-Type Leo','Xexex':'Xexex / Orius','魂斗罗街机':'Contra (Arcade)','超级魂斗罗街机':'Super Contra (Arcade)','忍者神龟Turtles in Time':'Teenage Mutant Ninja Turtles: Turtles in Time','X-Men（6人版）':'X-Men (Arcade)','辛普森一家':'The Simpsons (Arcade)','Sunset Riders':'Sunset Riders','Violent Storm':'Violent Storm','Mystic Warriors':'Mystic Warriors: Wrath of the Ninjas','Life Force':'Life Force / Salamander','Gradius I/II/III/Gaiden':'Gradius I / II / III / Gradius Gaiden','Parodius全系':'Parodius series','TwinBee全系':'TwinBee series','泡泡龙+Rainbow Islands':'Bubble Bobble / Rainbow Islands','奇奇怪界':'KiKi KaiKai','电梯大战1/2':'Elevator Action / Elevator Action Returns','Chase HQ':'Chase H.Q.','太空侵略者':'Space Invaders','Darius I/II/外传/Gaiden':'Darius / Darius II / Darius Gaiden','Ninja Warriors':'The Ninja Warriors','Rastan':'Rastan','Metal Black':'Metal Black','Space Gun':'Space Gun','Puzzle Bobble 1-4':'Puzzle Bobble 1 / 2 / 3 / 4','Mars Matrix':'Mars Matrix: Hyper Solid Shooting','Giga Wing 1':'Giga Wing','Giga Wing 2':'Giga Wing 2',
        '战斧1/2/3':'Golden Axe (Arcade) / Golden Axe: The Revenge of Death Adder','兽王记':'Altered Beast','太空哈利':'Space Harrier','Fantasy Zone':'Fantasy Zone','OutRun':'Out Run','After Burner':'After Burner II','Sonic the Fighters':'Sonic the Fighters','Virtua Fighter 1':'Virtua Fighter','Virtua Fighter 2':'Virtua Fighter 2','Daytona USA':'Daytona USA','Sega Rally':'Sega Rally Championship','Virtua Cop 1/2':'Virtua Cop / Virtua Cop 2','Super Monaco GP':'Super Monaco GP','Hang-On':'Hang-On','Thunder Blade':'Thunder Blade','双截龙1/2/3':'Double Dragon 1 / 2 / 3 (Arcade)','热血系列街机版':'Nekketsu Kouha Kunio-kun / Renegade (Arcade)','Joe & Mac':'Joe & Mac: Caveman Ninja','Heavy Barrel':'Heavy Barrel','Dark Seal':'Dark Seal / Gate of Doom','Midnight Resistance':'Midnight Resistance','Burning Fight':'Burning Fight','beatmania IIDX':'beatmania IIDX','DDR':'Dance Dance Revolution','pop\'n music':'pop’n music','GITADORA':'GuitarFreaks / DrumMania (GITADORA series)','Taiko no Tatsujin':'Taiko no Tatsujin',
        'Medal of Honor':'Medal of Honor','Medal of Honor: Underground':'Medal of Honor: Underground','Panzer General':'Panzer General','Allied General':'Allied General','Panzer Front':'Panzer Front','Vandal Hearts':'Vandal Hearts','Wild Arms 1':'Wild Arms','Wild Arms 2':'Wild Arms 2nd Ignition','PaRappa':'PaRappa the Rapper','Vib-Ribbon':'Vib-Ribbon','DDR/beatmania/太鼓达人':'Dance Dance Revolution / beatmania / Taiko no Tatsujin','Persona 1':'Revelations: Persona','Persona 2：Innocent Sin':'Persona 2: Innocent Sin','Persona 2：Eternal Punishment':'Persona 2: Eternal Punishment','真女神转生1':'Shin Megami Tensei','真女神转生2':'Shin Megami Tensei II','真女神转生if...':'Shin Megami Tensei if...','文明':'Sid Meier’s Civilization',
        'Langrisser':'Langrisser','Langrisser II':'Langrisser II','大战略':'Advanced Daisenryaku',
    }
    if clean in known: return known[clean], clean
    # 系列自动编号。
    pats = [
      (r'^拳皇(\d+)$', lambda m:f'The King of Fighters {m.group(1)}'),
      (r'^宝可梦(.+)$', lambda m:'Pokémon '+m.group(1)),
      (r'^机器人大战(.+)$', lambda m:'Super Robot Taisen '+m.group(1)),
    ]
    for p,f in pats:
        m=re.match(p,clean)
        if m:return f(m),clean
    return clean, clean

# 去掉显然错误、重复或不存在的补充占位。
adds = {p:[a for a in vals if a[0] and 'not included' not in a[0]] for p,vals in adds.items()}

entries=[]
seen_psp_2g=False
for i,p in enumerate(platform_heads):
    start=source.index('### '+p+'\n')
    end=source.find('\n### ',start+5)
    # 下一平台或专题。
    candidates=[source.find('\n### '+q+'\n',start+5) for q in platform_heads[i+1:]]
    candidates += [source.find('\n## 专题系列图鉴',start+5)]
    candidates=[x for x in candidates if x!=-1]
    end=min(candidates) if candidates else len(source)
    block=source[start:end]
    for line in block.splitlines():
        if not re.match(r'^\| \d+ \|',line):continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        old=cells[1]
        dropkey=old
        if p=='PSP' and old=='怪物猎人携带版2nd G':
            if seen_psp_2g: dropkey='怪物猎人携带版2nd G|DUP'
            seen_psp_2g=True
        if dropkey in drops.get(p,set()):continue
        en,zh=infer_name(p,old)
        pub=pubfix.get(old,cells[2] if cells[2] not in {'—',''} else '')
        entries.append(Entry(p,old,en,zh,pub,cells[3]))
    for en,zh,pub,size,year in adds.get(p,[]):
        e=Entry(p,en,en,zh,pub,size,year)
        entries.append(e)

# 修正个别补充条目的残留名称。
for e in entries:
    if e.old=='饿狼传说' and e.platform=='MD / Genesis':e.en='Fatal Fury 2';e.zh='饿狼传说 2'
    if e.old=='侍魂' and e.platform=='MD / Genesis':e.en='Samurai Shodown';e.zh='侍魂'
    if e.old=='VF3tb':e.en='Virtua Fighter 3tb';e.zh='VR 战士 3 组队战'
    if e.old=='Hydro Thunder':e.en='Hydro Thunder';e.zh='雷霆快艇'
    if e.old=='Typing of the Dead':e.en='The Typing of the Dead';e.zh='死亡打字员'
    if e.old=='Sega GT':e.en='Sega GT';e.zh='世嘉 GT'
    if e.old=='NBA 2K / NFL 2K系列':e.en='NBA 2K / NFL 2K series';e.zh='NBA 2K／NFL 2K 系列'
    if e.old=='DJMAX Portable':e.en='DJMax Portable 1 / 2 / Clazziquai / Black Square';e.zh='DJMax 携带版系列'
    if e.old=='太鼓达人':e.en='Taiko no Tatsujin Portable';e.zh='太鼓达人携带版'
    if e.old=='三国志7' and e.platform=='PS1':e.en='Romance of the Three Kingdoms VII';e.zh='三国志 VII'
    if e.old=='大战略' and e.platform=='PS1':e.en='Daisenryaku: Master Combat';e.zh='大战略：玩家精神'
    if e.old=='Shin Megami Tensei if...' and e.platform=='SNES / SFC':e.en='Shin Megami Tensei if...';e.zh='真·女神转生 if…'
    if e.old=='Lufia 1':e.en='Lufia & the Fortress of Doom';e.zh='四狂神战记'
    if e.old=='Lufia 2':e.en='Lufia II: Rise of the Sinistrals';e.zh='四狂神战记 II'
    if e.old=='Breath of Fire 1':e.en='Breath of Fire';e.zh='龙战士'
    if e.old=='Breath of Fire 2':e.en='Breath of Fire II';e.zh='龙战士 II'
    if e.old=='Arcana':e.en='Arcana / Card Master';e.zh='卡牌大师'
    if e.old=='E.V.O.':e.en='E.V.O.: Search for Eden';e.zh='46 亿年物语'
    if e.old=='Panel de Pon':e.en='Panel de Pon';e.zh='花仙子方块'
    if e.old=='Saturday Night Slam Masters':e.en='Saturday Night Slam Masters';e.zh='摔角霸王'
    if e.old=='U.N. Squadron':e.en='U.N. Squadron / Area 88';e.zh='战区 88'
    if e.old=='Super Ghouls \'n Ghosts':e.en='Super Ghouls ’n Ghosts';e.zh='超魔界村'
    if e.old=='Axelay':e.en='Axelay';e.zh='银河风暴'
    if e.old=='Gradius III':e.en='Gradius III';e.zh='宇宙巡航机 III'
    if e.old=='R-Type III':e.en='R-Type III: The Third Lightning';e.zh='异形战机 III'
    if e.old=='Parodius':e.en='Parodius Da!';e.zh='疯狂大射击'
    if e.old=='TwinBee':e.en='Pop’n TwinBee';e.zh='出击！兵蜂'
    if e.old=='Darius Twin':e.en='Darius Twin';e.zh='太空战斗机：双子'
    if e.old=='Pilotwings':e.en='Pilotwings';e.zh='飞行俱乐部'
    if e.old=='Killer Instinct':e.en='Killer Instinct';e.zh='杀手本能'
    if e.old=='Earthworm Jim':e.en='Earthworm Jim';e.zh='蚯蚓战士'
    if e.old=='Aladdin':e.en='Disney’s Aladdin';e.zh='阿拉丁'
    if e.old=='狮子王':e.en='Disney’s The Lion King';e.zh='狮子王'
    if e.old=='Goemon 神秘历险':e.en='The Legend of the Mystical Ninja';e.zh='加油五右卫门： Yukihime 救出绘卷'
    if e.old=='Robotrek':e.en='Robotrek';e.zh='机器人构筑战记'
    if e.old=='SimCity':e.en='SimCity';e.zh='模拟城市'
    if e.old=='Wario\'s Woods':e.en='Wario’s Woods';e.zh='瓦力欧的森林'
    if e.old=='Zombies Ate My Neighbors':e.en='Zombies Ate My Neighbors';e.zh='僵尸邻居'
    if e.old=='The Lost Vikings':e.en='The Lost Vikings';e.zh='失落的维京人'
    if e.old=='Another World':e.en='Another World / Out of This World';e.zh='另一个世界'
    if e.old=='Prince of Persia':e.en='Prince of Persia';e.zh='波斯王子'
    if e.old=='Metal Gear Ghost Babel':e.en='Metal Gear Solid: Ghost Babel';e.zh='合金装备：幽灵通天塔'
    if e.old=='Dragon Warrior Monsters 1':e.en='Dragon Warrior Monsters';e.zh='勇者斗恶龙怪兽篇'
    if e.old=='Dragon Warrior Monsters 2':e.en='Dragon Warrior Monsters 2: Cobi’s Journey / Tara’s Adventure';e.zh='勇者斗恶龙怪兽篇 2'
    if e.old=='Shantae':e.en='Shantae';e.zh='桑塔'
    if e.old=='牧场物语GB':e.en='Harvest Moon GB';e.zh='牧场物语 GB'
    if e.old=='俄罗斯方块':e.en='Tetris';e.zh='俄罗斯方块'
    if e.old=='马里奥医生':e.en='Dr. Mario';e.zh='马力欧医生'
    if e.old=='耀西蛋':e.en='Yoshi';e.zh='耀西的蛋'
    if e.old=='炸弹人GB':e.en='Bomberman GB';e.zh='炸弹人 GB'
    if e.old=='Game & Watch Gallery系列':e.en='Game & Watch Gallery 1–3';e.zh='Game & Watch 博物馆 1–3'
    if e.old=='幽游白书：魔强统一战':e.pub='Treasure / Sega'
    if e.old=='Langrisser':e.en='Langrisser';e.zh='梦幻模拟战'
    if e.old=='Langrisser II':e.en='Langrisser II / Der Langrisser';e.zh='梦幻模拟战 II'
    if e.old=='三国志2' and e.platform=='SNES / SFC':e.en='Romance of the Three Kingdoms II';e.zh='三国志 II'
    if e.old=='三国志3' and e.platform=='SNES / SFC':e.en='Romance of the Three Kingdoms III: Dragon of Destiny';e.zh='三国志 III'
    if e.old=='信长之野望：全国版' and e.platform=='SNES / SFC':e.en='Nobunaga’s Ambition: Zenkokuban';e.zh='信长之野望：全国版'
    if e.old=='勇' : pass
    # 发行方统一历史主体，避免把合并后的公司倒填给早期作品。
    if e.en.startswith('Final Fantasy') and e.year and int(re.sub(r'\D.*','',e.year) or 2000)<2003:e.pub='Square'
    if not e.pub:e.pub='见商品版本'

# 年份与系列归属。
year_exact={
'Super Mario Bros.':'1985','Super Mario Bros. 2 (USA)':'1988','Super Mario Bros. 3':'1988','The Legend of Zelda':'1986','Zelda II: The Adventure of Link':'1987','Metal Max':'1991','Metal Max 2':'1993','Metal Max 3':'2010','Metal Saga: Hagane no Kisetsu':'2006',
'The Legend of Zelda: A Link to the Past':'1991','The Legend of Zelda: Ocarina of Time':'1998','The Legend of Zelda: Majora’s Mask':'2000','The Legend of Zelda: The Minish Cap':'2004','The Legend of Zelda: Phantom Hourglass':'2007','The Legend of Zelda: Spirit Tracks':'2009',
'Super Metroid':'1994','Metroid Fusion':'2002','Metroid: Zero Mission':'2004','Metroid II: Return of Samus':'1991','Metroid':'1986',
'Castlevania: Symphony of the Night':'1997','Akumajou Dracula X: Chi no Rondo / Castlevania: Rondo of Blood':'1993','Castlevania: Aria of Sorrow':'2003','Castlevania: Harmony of Dissonance':'2002','Castlevania: Circle of the Moon':'2001','Castlevania: Dawn of Sorrow':'2005','Castlevania: Portrait of Ruin':'2006','Castlevania: Order of Ecclesia':'2008','Castlevania: Dracula X':'1995','Super Castlevania IV':'1991',
'Pokémon FireRed / LeafGreen':'2004','Pokémon Emerald':'2004','Pokémon HeartGold / SoulSilver':'2009','Pokémon Platinum':'2008','Pokémon Black / White':'2010','Pokémon Black 2 / White 2':'2012',
}
series_rules=[
('马力欧','Mario|Donkey Kong|Yoshi|Wario|Dr\. Mario'),('塞尔达传说','Zelda'),('宝可梦','Pokémon'),('洛克人','Mega Man'),('恶魔城','Castlevania|Akumajou Dracula|Kid Dracula'),('火焰之纹章','Fire Emblem'),('最终幻想','Final Fantasy|Crisis Core|Dissidia'),('逆转裁判','Ace Attorney|Gyakuten|Ghost Trick'),('拳皇','The King of Fighters'),('侍魂与月华剑士','Samurai Shodown|The Last Blade'),('街头霸王','Street Fighter'),('超级机器人大战','Super Robot'),('大航海时代','Uncharted Waters|Daikoukai'),('重装机兵','Metal Max|Metal Saga'),('生化危机','Resident Evil'),('合金装备','Metal Gear'),('魂斗罗','Contra|Super C'),('双截龙','Double Dragon'),('怒之铁拳','Streets of Rage|Bare Knuckle'),('三国志与三国题材','Sangokushi|Romance of the Three Kingdoms|Tenchi wo Kurau|Knights of Valour|Dynasty Warriors'),('信长之野望','Nobunaga'),('勇者斗恶龙','Dragon Quest|Dragon Warrior'),('密特罗德','Metroid'),('怪物猎人','Monster Hunter'),('英雄传说与轨迹','The Legend of Heroes|Nayuta'),('伊苏','^Ys'),('寂静岭','Silent Hill'),('传说系列','Tales of'),('牧场物语与符文工房','Harvest Moon|Rune Factory'),('高级战争','Advance Wars'),('光明与梦幻模拟战','Shining Force|Shining Soul|Langrisser'),('皇家骑士团','Tactics Ogre|Ogre Battle'),('格兰蒂亚','Grandia'),('幻想水浒传','Suikoden'),('女神转生与女神异闻录','Shin Megami Tensei|Persona'),('索尼克','Sonic'),('星之卡比','Kirby'),('雷顿教授','Professor Layton'),('黄金太阳','Golden Sun'),('王国之心','Kingdom Hearts'),('前线任务','Front Mission'),('梦幻之星','Phantasy Star'),('星之海洋','Star Ocean'),('沙加','SaGa'),('龙战士','Breath of Fire'),('露娜','Lunar'),('荒野兵器','Wild Arms'),('战场女武神','Valkyria'),('古惑狼','Crash'),('小龙斯派罗','Spyro'),('古墓丽影','Tomb Raider'),('铁拳','Tekken'),('GT赛车','Gran Turismo'),('山脊赛车','Ridge Racer'),('数码宝贝','Digimon'),('天外魔境','Tengai Makyou'),('怒首领蜂与Cave','DoDonPachi|ESP Ra.De|Espgaluda|Progear'),('合金弹头','Metal Slug'),('饿狼与龙虎之拳','Fatal Fury|Art of Fighting'),('快打旋风','Final Fight'),('战斧','Golden Axe'),('宇宙巡航机与兵蜂','Gradius|Parodius|TwinBee|Life Force|Salamander'),('雷电与R-Type','Raiden|R-Type'),('Darius','Darius'),('世界树迷宫','Etrian Odyssey'),('寄生前夜','Parasite Eve|The 3rd Birthday'),('光明力量','Shining Force'),
]
for e in entries:
    if not e.year:e.year=year_exact.get(e.en,'')
    for s,p in series_rules:
        if re.search(p,e.en,re.I):e.series=s;break
    # 专题中的混杂 IP 拆子系列。
    if e.series=='马力欧':
        if re.search('Mario Kart',e.en,re.I):e.subgroup='卡丁车'
        elif re.search('Mario Party',e.en,re.I):e.subgroup='派对'
        elif re.search('Mario Golf|Mario Tennis',e.en,re.I):e.subgroup='体育'
        elif re.search('Wario',e.en,re.I):e.subgroup='瓦力欧'
        elif re.search('Donkey Kong',e.en,re.I):e.subgroup='咚奇刚'
        elif re.search('Yoshi',e.en,re.I):e.subgroup='耀西'
        elif re.search('Paper Mario|Mario & Luigi|Super Mario RPG',e.en,re.I):e.subgroup='角色扮演'
        else:e.subgroup='平台动作'
    elif e.series=='宝可梦':
        if re.search('Mystery Dungeon',e.en,re.I):e.subgroup='不可思议迷宫'
        elif re.search('Ranger',e.en,re.I):e.subgroup='护林员'
        elif re.search('Stadium|Snap|Puzzle|Trading Card|Hey You',e.en,re.I):e.subgroup='家用机与益智衍生'
        else:e.subgroup='正统角色扮演'
    elif e.series=='三国志与三国题材':
        if re.search('Romance|Sangokushi',e.en,re.I):e.subgroup='光荣《三国志》'
        elif re.search('Tenchi wo Kurau',e.en,re.I):e.subgroup='吞食天地'
        elif re.search('Knights of Valour',e.en,re.I):e.subgroup='三国战纪'
        else:e.subgroup='其他三国题材'
    elif e.series=='洛克人':
        if re.search('Battle Network',e.en,re.I):e.subgroup='EXE／网络对战'
        elif re.search('Zero',e.en,re.I):e.subgroup='Zero'
        elif re.search('ZX|Star Force',e.en,re.I):e.subgroup='ZX 与流星'
        elif re.search('Mega Man X',e.en,re.I):e.subgroup='X'
        else:e.subgroup='元祖与世界'
    elif e.series=='最终幻想':
        if re.search('Tactics',e.en,re.I):e.subgroup='战略版'
        elif re.search('Crisis Core',e.en,re.I):e.subgroup='VII 衍生'
        else:e.subgroup='正传与其他作品'
    elif e.series=='光明与梦幻模拟战':
        e.subgroup='梦幻模拟战' if 'Langrisser' in e.en else '光明系列'
    elif e.series=='女神转生与女神异闻录':
        e.subgroup='Persona' if 'Persona' in e.en else '真·女神转生'
    else:e.subgroup='主系列'

# 内容说明库：优先使用具体作品的玩法与历史地位。
notes_exact={
'Super Mario Bros.':'横版卷轴平台游戏，以奔跑惯性、踩敌和隐藏通道构成核心节奏。1985 年的家用机版把街机式短关卡整合为连续冒险，奠定了后来 2D 马力欧的基本语法。',
'Super Mario Bros. 2 (USA)':'可操纵马力欧、路易吉、桃花公主与奇诺比奥，以拔萝卜、举起并投掷敌人取代传统踩敌。它源自《梦工厂心跳冒险》的角色替换版，1992 年又以《Super Mario USA》回流日本；与日版高难度 2 代不是同一作。',
'Super Mario Bros.: The Lost Levels':'延续初代引擎但加入毒蘑菇、强风与更苛刻的跳跃，是 1986 年日本原版《超级马力欧兄弟 2》。海外长期未单独发行，后经《Super Mario All-Stars》以“The Lost Levels”广为人知。',
'Super Mario Bros. 3':'大地图选关、变身道具与世界主题共同扩展了横版动作的结构，狸猫装和多样化 Boss 战尤其经典。它是 FC 后期技术与关卡设计的集大成者，而非普通续作换皮。',
'The Legend of Zelda':'在开放地图上寻找迷宫、道具与隐藏入口，弱化固定路线并允许玩家自行摸索。电池存档让长期冒险在家用机上成立，也奠定了系列的探索传统。',
'Zelda II: The Adventure of Link':'把俯视大地图与横版战斗结合，加入经验值、魔法和村镇系统。它与系列其他作品风格差异很大，但经验成长与横版战斗后来仍影响了动作 RPG。',
'Metroid':'扮演萨姆斯在泽贝斯星非线性探索，靠新能力打开旧区域。它把孤独氛围、地图记忆与能力锁结合起来，是“密特罗德式探索”的源头。',
'Metroid II: Return of Samus':'任务转为在 SR388 星清除各阶段密特罗德，地图随讨伐进度逐步开放。掌机画面限制了视野，却强化了幽闭感；萨姆斯与幼体的剧情也连接《超级密特罗德》。',
'Super Metroid':'以非线性地图、能力回环和环境叙事构成高度统一的探索体验。它没有依赖长对白，却通过场景与结局建立强烈情感，是动作冒险和后续“银河城”设计的重要范本。',
'Metroid Fusion':'萨姆斯在 BSL 空间站被 X 寄生体威胁，SA-X 会作为高压追逐者反复出现。流程比《超级密特罗德》更线性，但叙事密度和紧迫感明显更强。',
'Metroid: Zero Mission':'以现代地图、存档和动作系统重制 FC 初代，并在原结局后追加零装萨姆斯潜入段落。它不是简单高清化，而是兼顾新玩家与系列史的完整重制。',
'The Legend of Zelda: A Link to the Past':'光明与黑暗两个世界互相映射，玩家利用世界切换改变道路与谜题。它重新整理并固定了“村庄—迷宫—关键道具”的系列结构，是 2D 塞尔达的核心参照。',
'The Legend of Zelda: Ocarina of Time':'以 Z 注视锁定、情境按键和立体迷宫建立 3D 动作冒险的通用语言，少年与成年林克的时间差也参与解谜。其历史价值不只在评分，而在大量 3D 游戏沿用了这套交互方式。',
'The Legend of Zelda: Majora’s Mask':'三天循环让镇民行程、支线与灾难倒计时彼此咬合，面具则改变能力和人际关系。复用《时之笛》引擎却转向压迫与遗憾，是系列最具实验性的作品之一。',
'Castlevania: Symphony of the Night':'阿鲁卡多在可反复探索的德古拉城中获取能力、装备与使魔，逆城则大幅扩展后半流程。它把《密特罗德》的探索结构与 RPG 成长结合，直接塑造了“银河城”类型。',
'Akumajou Dracula X: Chi no Rondo / Castlevania: Rondo of Blood':'里希特以传统鞭子闯关，可救出人质、发现分支并解锁玛莉亚。PCE CD 的音画演出与多路线关卡使其成为旧式恶魔城高峰，也直接衔接《月下夜想曲》的开场。',
'Castlevania: Dracula X':'SFC 的《恶魔城 XX》借用《血之轮回》人物与部分美术，但关卡和系统经过重排，并非 PCE 原版移植。把它单独看待，才能避免与真正的《血之轮回》混淆。',
'Super Castlevania IV':'八方向挥鞭、鞭子悬挂与多方向跳跃操作重塑了西蒙的动作，Mode 7 场景和编曲也突出 16 位机特色。结构上更接近初代的重新演绎，而非 FC 第四作。',
'Castlevania: Aria of Sorrow':'来须苍真通过吸收怪物灵魂获得能力，魂收集把探索、战斗与养成连在一起。故事设在 2035 年，是 GBA 三部探索型恶魔城中系统完成度很高的一作。',
'Castlevania: Harmony of Dissonance':'祖斯特在表里两座相互关联的城堡间切换，法术书与副武器组合形成不同魔法。画面针对 GBA 屏幕提高亮度，音乐音色则带有鲜明妥协。',
'Castlevania: Circle of the Moon':'DSS 卡牌两两组合改变武器、属性和技能，动作手感偏传统且难度较高。它由 Konami 神户团队制作，与后续五十岚主导的掌机三部曲在系统路线上不同。',
'Chrono Trigger':'穿越时空改变不同年代的事件，战斗在场景内展开并强调双人、三人协力技。鸟山明人设、坂口博信与堀井雄二等阵容以及多结局设计，使其成为 16 位 RPG 的协作高峰。',
'Final Fantasy IV':'以塞西尔从黑骑士到圣骑士的转变推动群像剧，角色会随剧情加入、离队。ATB 让回合指令与等待时间结合，系列由此形成更强的战斗节奏。',
'Final Fantasy V':'职业可自由切换，已学技能又能跨职业装配，构筑空间远大于单纯升级。轻松冒险外壳下是深度很高的系统型 RPG，GBA 版还追加了职业与迷宫。',
'Final Fantasy VI':'多主角群像围绕魔法复兴与凯夫卡的野心展开，中期世界剧变重新组织探索目标。魔石、角色固有技与宏大配乐共同代表 Square 的 2D 制作高峰。',
'Final Fantasy VII':'克劳德与雪崩的反神罗行动逐渐扩展为星球危机，魔晶石组合允许自由构筑。全 3D 场景、预渲染背景与电影化演出帮助 JRPG 在全球主流市场破圈。',
'Final Fantasy VIII':'SeeD 学园与佣兵战争背景下，斯考尔和莉诺雅的关系是叙事核心。抽取魔法与 Junction 把数值成长绑定到装备魔法，规则独特也需要较多理解成本。',
'Final Fantasy IX':'祖达尔与伙伴的旅程主动回归水晶、职业和童话幻想风格，同时讨论人造生命的自我认同。它是对系列早期传统的总结，而不只是“复古版 FF”。',
'Final Fantasy Tactics':'伊瓦利斯战争通过拉姆萨的视角展开，职业、技能、地形高度与行动顺序形成细密战棋。政治叙事与自由养成使其成为战术 RPG 的长期标杆。',
'Dragon Quest':'单主角旅行、回合制战斗和清晰成长曲线把电脑 RPG 转化为家用机可理解的形式。堀井雄二、鸟山明与椙山浩一的组合由此成为系列长期标识。',
'Dragon Quest II: Luminaries of the Legendary Line':'队伍扩展为三人，地图与航海范围也显著放大，后期难度颇具挑战。它把初代单人冒险推进为真正的小队旅程。',
'Dragon Quest III: The Seeds of Salvation':'自由转职、昼夜变化和广阔世界让玩家自行安排成长路线，结局又把故事与初代世界相连。它在日本成为社会现象，也长期是系列最重要的历史节点之一。',
'Dragon Quest IV: Chapters of the Chosen':'各章先讲述不同伙伴的命运，最后汇入勇者一行，章节结构让群像塑造格外鲜明。NDS 版属于重新制作，并不存在原稿所写的 GBA 移植。',
'Dragon Quest V: Hand of the Heavenly Bride':'故事跨越主人公少年、成家与为人父的阶段，怪物收服也与家族主题结合。以人生阶段而非单纯王国危机推动叙事，是它最突出的历史地位。',
'Dragon Quest VI: Realms of Revelation':'梦与现实两个世界互相折射，失忆与身份追寻贯穿旅程。转职系统与双世界探索体量庞大，NDS 版是较方便的完整体验方式。',
'Pokémon Red / Green / Blue / Yellow':'以收集、交换和对战驱动关都旅行，双版本差异鼓励玩家互联。黄版围绕皮卡丘与动画元素调整，红绿蓝则代表 1996 年起家的原始形态。',
'Pokémon Gold / Silver / Crystal':'城都与关都连成双地区旅程，引入昼夜、星期、孵化和性别等系统。水晶版加入更多动画与水君剧情，是第二世代的扩展版。',
'Pokémon Ruby / Sapphire':'第三世代来到丰缘，加入特性、性格和双打对战，宝可梦构筑由此明显深化。红宝石与蓝宝石是原版双版本，绿宝石是后来的扩展版。',
'Pokémon Emerald':'整合红蓝宝石的熔岩队与海洋队冲突，并强化对战开拓区。这里的主线是固拉多、盖欧卡与烈空坐，而非原稿误写的“三圣柱”。',
'Pokémon FireRed / LeafGreen':'以 GBA 画面和第三世代系统重制关都旅程，并加入七之岛与无线适配器支持。它适合比较初代设计与第三世代机制的差异。',
'Pokémon HeartGold / SoulSilver':'复刻金银并让首位宝可梦跟随行走，计步器与双地区内容增强陪伴感。它是第二世代内容在 NDS 系统上的扩展重制，不是高清重制。',
'Pokémon Platinum':'对《珍珠／钻石》的神奥主线、殿堂和战斗设施进行扩展，骑拉帝纳与毁坏的世界成为视觉中心。神奥位于当代地区体系，与后来《传说 阿尔宙斯》的洗翠时代不能混写。',
'Pokémon Black / White':'合众地区在首轮冒险中只使用全新图鉴，并正面讨论训练家与宝可梦的关系。较完整的角色冲突使它成为系列叙事受关注的一代。',
'Pokémon Black 2 / White 2':'采用两年后、新主角与新地点的直接续篇结构，而非传统第三版。宝可梦世界锦标赛等内容也让旧作角色重新登场。',
'Pokémon Mystery Dungeon: Red Rescue Team':'玩家变成宝可梦，与伙伴组成救助队探索随机迷宫。赤救助队是 GBA 版，青救助队是 NDS 版，两者为同一故事的双版本而非前后续作。',
'Pokémon Mystery Dungeon: Blue Rescue Team':'与 GBA《赤救助队》共享故事和队伍，NDS 版利用双屏与触控呈现信息。选择版本时应看作介质与操作差异，而不是连续两作。',
'Golden Sun':'精神力同时用于战斗与场景解谜，精灵召唤和属性搭配构成队伍成长。Camelot 将大地图解谜与传统 JRPG 结合，GBA 音画表现尤其突出。',
'Golden Sun: The Lost Age':'直接延续前作并更换视角，世界规模、精灵组合与航海探索明显扩大。两作合起来才是完整故事，建议按《开启的封印》到《失落的时代》游玩。',
'Advance Wars':'以兵种克制、地形、产能与指挥官能力构成清晰战棋，战役和挑战地图适合反复优化。它把复杂军事策略压缩成易懂但不浅薄的掌机系统。',
'Advance Wars 2: Black Hole Rising':'新增黑洞军指挥官与超级 CO 技，并针对前作平衡性调整。整体是“更多内容＋更精细对抗”的续作，而非颠覆系统。',
'Fire Emblem: Genealogy of the Holy War':'横跨父子两代的战争与血统悲剧展开在大型地图上，恋爱配对会影响子代能力。它的史诗结构和继承系统在系列中独树一帜。',
'Fire Emblem: Thracia 776':'作为《圣战之系谱》的间章聚焦里夫，加入疲劳、俘虏与营救等更严苛机制。资源紧张与逃生关卡使它以硬核著称。',
'Fire Emblem: The Binding Blade':'罗伊在艾雷布大陆组织反抗军，武器耐久与永久阵亡维持传统战棋压力。它是 GBA 首部火纹，主角后来也因《任天堂明星大乱斗》扩大知名度。',
'Fire Emblem: The Blazing Blade':'作为《封印之剑》前传，从琳、艾利乌德与赫克托耳的视角补足上一代故事。前期教学与角色支援使它成为许多海外玩家的入坑作。',
'Fire Emblem: The Sacred Stones':'采用独立世界观与双主角路线，并提供地图遭遇战和魔物塔供练级。相较前两作更便于自由培养，战棋压力也更温和。',
'Metal Max':'在核战后废土自由接取赏金、改造战车，也可以随时回归猎人的平凡生活。人车双战斗与开放式目标让它在中文 RPG 玩家中形成独特口碑，与宝可梦毫无系列关系。',
'Metal Max 2':'延续战车改装和赏金首体系，扩大世界并强化伙伴与据点内容。SFC 原作由 Data East 发行，后来也有重制版本；不能误列为 PS1 游戏。',
'Metal Max 3':'以末日开放世界、赏金任务和深度战车改装延续系列，并加入更具戏剧性的主角设定。NDS 正统序号作由角川 Games 发行。',
'Metal Saga: Hagane no Kisetsu':'《钢之季节》延续初代世界观，采用俯视角探索与战车战斗。它是 2006 年 NDS 作品，不是《重装机兵 2》的高清重制。',
'Resident Evil':'洋馆探索把有限弹药、格子背包、门锁谜题和固定镜头结合，制造持续资源压力。1996 年作品确立了“生存恐怖”这一市场标签。',
'Resident Evil 2':'里昂与克莱尔的双路线从警局扩展到地下设施，资源管理与人偶式镜头延续初代。N64 版以高压缩技术容纳双主角内容，是技术移植亮点，不是“灾难版”。',
'Resident Evil 3: Nemesis':'吉尔在被摧毁的浣熊市逃亡，追迹者会跨场景施压，紧急回避与弹药合成改变战斗节奏。流程更偏动作与逃生。',
'Metal Gear Solid':'斯内克潜入影子摩西岛，雷达、噪音与敌人视锥构成潜行核心。大量 codec 对话、电影镜头和打破第四墙的 Boss 战使游戏叙事方式极具辨识度。',
'Metal Gear Solid: Peace Walker':'围绕无国界军队建设基地、招募人员并研发装备，主线与多人共斗任务结合。它是小岛秀夫直接主导的重要正传章节，而非轻量外传。',
'Sonic the Hedgehog':'以速度、坡道和环状地形建立不同于马力欧的平台动作，金环同时承担分数与保护。它成为世嘉塑造主机品牌形象的关键作品。',
'Sonic the Hedgehog 2':'新增塔尔斯与旋转冲刺，关卡分支和高速流动更成熟；纳克鲁斯是在三代才首次登场。双人分屏也扩大了当年的家庭游玩价值。',
'Sonic the Hedgehog 3 & Knuckles':'通过锁合技术把《Sonic 3》与《Sonic & Knuckles》连成大篇幅冒险，三角色路线与大型关卡互补。这是 MD 索尼克内容最完整的形态。',
'Phantasy Star IV: The End of the Millennium':'以漫画格演出、组队技与宏命令加快传统回合制节奏，剧情也回收早期系列线索。它常被视为 MD 最具代表性的 JRPG 之一。',
'Streets of Rage 2 / Bare Knuckle II':'四名角色各有速度、力量与投技差异，敌群配置和关卡节奏明显优于初代。古代佑三的电子配乐与手感共同造就清版动作经典。',
'Gunstar Heroes':'两种射击方式可组合成不同武器，角色又能投摔、滑铲与蹬墙，Treasure 用大量 Boss 和夸张演出建立风格。双人合作是体验重点。',
'Contra: Hard Corps':'四角色、分支路线和多结局扩大重复游玩价值，滑铲与换武器让动作更灵活。日美版在生命机制等方面差异明显。',
'Shin Megami Tensei: Strange Journey':'调查南极“灭世之地”，恶魔交涉、合体与属性克制维持本传硬核 RPG 结构。科幻军事考察外壳和阵营选择使它区别于校园向 Persona。',
'The World Ends with You':'以涩谷文化和死神游戏为舞台，双屏分别控制两名角色，徽章组合决定攻击方式。美术、音乐与系统风格高度统一，是 NDS 原创动作 RPG 的代表。',
'Ghost Trick: Phantom Detective':'主角以幽灵身份附身物件、操纵机关并回溯死者最后四分钟。西塞尔的身世谜题与一连串救援环环相扣，由巧舟打造但不是《逆转裁判》正传。',
'999: Nine Hours, Nine Persons, Nine Doors':'九人被困于沉船设施，在数字根规则下分组进入房间解谜，逃生与多结局叙事互相嵌套。它是“极限脱出”系列起点。',
'Okamiden':'以笔神在地图上绘制奇迹，故事围绕小小太阳与伙伴旅行。它在 NDS 上延续《大神》的水墨视觉和解谜，而非简单缩小版移植。',
'Skies of Arcadia':'空贼维斯一行驾驶飞空艇探索浮空大陆，陆上回合战与舰船炮击战交替。明快探险精神和世界发现在 DC JRPG 中很有代表性。',
'Soulcalibur':'武器格斗以八向移动、横纵斩与格挡反击构成，DC 版又加入大量任务模式。其街机移植完成度与画面曾长期作为 DC 技术展示。',
'Ikaruga':'敌弹与自机分黑白两极，同色可吸收、异色才致命，切换属性同时决定生存与得分。Treasure 把弹幕射击变成高度纯粹的规则解谜。',
'Jet Set Radio':'在东京街头滑行、磨轨并喷涂涂鸦，卡通渲染与混搭音乐塑造强烈都市风格。它既是动作游戏，也是 DC 时代世嘉视觉实验的象征。',
'Shenmue':'横须贺日常以时间表、商店、交谈和 QTE 交织，目标是追查父亲遇害。它对持续世界与细节互动的投入影响深远，但慢节奏也需要耐心。',
'God of War: Chains of Olympus':'以连击、魔法、QTE 与大型 Boss 战呈现希腊神话前传，场景规模在 PSP 上很突出。N4100 建议从 1× 渲染逐段测试，不把“能启动”等同全程稳定。',
'Lumines':'四色方块随音乐时间线扫描消除，皮肤会同步改变节拍、视觉与节奏。水口哲也把音乐游戏反馈融入益智规则，是 PSP 早期最具原创性的作品之一。',
'Castlevania: The Dracula X Chronicles':'2.5D 重制《血之轮回》，并可解锁 PCE 原版与《月下夜想曲》。一套光盘包含新旧三种体验，适合核对系列版本关系。',
'Tony Hawk’s Pro Skater 2':'以两分钟内完成目标、寻找隐藏物和维持连招为核心，Manual 让地面动作可串入长连段。其关卡目标与得分循环是极限运动游戏的重要节点。',
'Crash Team Racing':'在卡丁车竞速外加入可控制的漂移蓄力与连续加速，冒险模式还用奖杯和 Boss 串联赛道。它不是简单复制马力欧赛车的衍生作。',
'Grandia':'以可干预行动顺序的战斗条、魔法与技能熟练度形成养成，贾斯汀的冒险强调远行与发现。Game Arts 的叙事节奏和乐观气质使它区别于沉重向 JRPG。',
'Suikoden II':'围绕少年兵与旧友在战争中的对立展开，108 星宿同伴、据点建设与三种战斗规模并行。人物群像和政治抉择使它在 PS1 RPG 中长期保有口碑。',
'Vagrant Story':'在雷亚蒙德废墟中探索，武器针对敌种族、部位与属性进行细致构筑。战斗、锻造与连环场景演出风格冷峻，学习门槛也明显高于一般动作 RPG。',
'Xenogears':'以机甲与肉身两套战斗展开科幻群像，后半大量采用叙事段落呈现庞大设定。它是 Square 制作，不应误写为 Enix；理解其历史也需正视后期制作节奏。',
'Valkyrie Profile':'按章节寻访战魂并安排英灵升天，迷宫采用横版动作，战斗则通过按键连携组织队伍。北欧神话、倒计时与角色结局构成独特结构。',
}

# 系列级内容与历史，用于没有单独长注的作品；仍给出具体机制而非“神作/续作”。
series_note={
'马力欧':'围绕马力欧宇宙的角色与规则展开，具体作品在平台跳跃、竞速、派对、体育或 RPG 中各有侧重。版本关系应以完整商品名和平台为准，Advance 编号不能按副标题猜。',
'塞尔达传说':'以迷宫、关键道具、探索与环境谜题构成冒险，地区版本和重制版常在操作与新增迷宫上有差异。它是任天堂动作冒险主线，不是传统数值驱动 RPG。',
'宝可梦':'围绕宝可梦收集、培养、交换或衍生玩法展开。正统双版本、扩展版、复刻和迷宫／护林员等支线应分开管理，地区与世代不能混写。',
'洛克人':'以动作关卡、能力获取和 Boss 克制为主要乐趣，元祖、X、Zero、EXE 与 ZX 的系统侧重并不相同。收藏时按子系列分组最不容易混淆。',
'恶魔城':'从早期线性鞭击闯关到后期地图探索与 RPG 成长，各作分支明显。需特别区分 PCE《血之轮回》、SFC《恶魔城 XX》与 PSP 重制合集。',
'火焰之纹章':'网格战棋结合武器克制、角色养成和永久阵亡，重制版通常会调整难度与便利功能。不同大陆的故事不要按序号强行串成一条时间线。',
'最终幻想':'各序号正传通常拥有独立世界，战斗系统与职业／成长规则随作品变化；战略版和 VII 衍生应另列。Square 与 Enix 于 2003 年合并，早期作品发行方不倒写成 Square Enix。',
'逆转裁判':'以调查、证物指证和法庭矛盾追击推动文字冒险，逆转检事改用御剑视角。巧舟的《幽灵诡计》只列同作者相关作品，不并入正传序号。',
'拳皇':'三人组队、角色相性与 SNK 全明星阵容构成对战核心，各年作品会调整系统与队伍规则。97、98、2002 的流行原因不同，不能简单按年份判断优劣。',
'侍魂与月华剑士':'刀剑格斗强调距离、重击与读招，侍魂偏一击威慑，月华剑士更强调连段与剑质选择。两个系列共享厂商与时代背景，但不是外传关系。',
'街头霸王':'以拳脚判定、必杀技、对空和资源管理构成格斗基础，II、Alpha、III 的系统与人物阵容各不相同。街机原版和家用移植需分开识别。',
'超级机器人大战':'把机器人动画角色与机体放入战棋关卡，以精神指令、改造和交叉剧情形成特色。A Portable 源自 GBA《A》，不是 NDS 作品移植。',
'大航海时代':'贸易、航海、发现与人物目标共同构成开放旅程，价值在于自由选择致富和探索路线，而不是固定关卡通关。',
'重装机兵':'以废土赏金、战车改装和较高流程自由度为特征，人与战车有独立战斗逻辑。它是独立的 Metal Max／Metal Saga 系列，与宝可梦无关。',
'生化危机':'通过有限资源、场景探索与威胁管理制造生存恐怖，后续作品逐步增加动作比重。不同平台移植的压缩和画面差异应具体说明。',
'合金装备':'以视线、声音、雷达与隐蔽路线完成潜入，叙事大量采用电影和通信演出。MSX 起源、GBC 独立故事与 Solid 主线不能混成同一版本。',
'魂斗罗':'以跑射、武器拾取和高密度敌人构成动作挑战，双人合作是早期作品的重要记忆。街机、FC、SFC 与 MD 各作关卡并非简单互移。',
'双截龙':'李氏兄弟以拳脚、投技和武器清理街头敌人，是清版动作早期代表。FC 初代与街机版在合作和系统上差异明显，二代通常更适合直接入门。',
'怒之铁拳':'清版动作结合投技、保险与鲜明角色差异，配乐和都市氛围是系列标志。“格斗三人组”只是初代中文俗称，不应重复收藏。',
'三国志与三国题材':'同一历史题材下有光荣君主战略、Capcom 清版动作／RPG 与 IGS 街机清版等不同系列。按子系列和玩法区分，避免把发行方或版本互相套用。',
'信长之野望':'以战国大名的内政、外交和军事扩张构成回合制历史模拟，各代在武将扮演与全国策略间改变重心。',
'勇者斗恶龙':'坚持回合制与旅行冒险的基本框架，通过队伍、转职、怪物或章节结构变化主题。NDS 的 IV／V／VI 是重制版，GBA 没有这些序号移植。',
'密特罗德':'以非线性地图、能力锁与科幻孤独感推动探索，掌机作品也在线性叙事和自由探索之间做不同取舍。',
'怪物猎人':'通过观察怪物动作、武器招式与素材装备循环形成长期挑战，便携共斗是 PSP 时代影响力爆发的重要因素。',
'英雄传说与轨迹':'重视城镇文本、人物关系与连续世界观，空轨、零碧和那由多应分篇理解；卡卡布三部曲属于更早的英雄传说体系。',
'伊苏':'以高速动作、冲撞或小队战斗和鲜明配乐推动冒险，I・II、菲尔盖纳重制与 VII 的战斗系统并不相同。',
'寂静岭':'以雾、声音、心理象征与不可靠叙事制造不安，PSP《破碎的记忆》还以心理测试改变呈现，不是《起源》的直接续作。',
'传说系列':'以即时线性动作战斗、角色小剧场和独立世界剧情为特点，各作主角与系统通常独立。',
'牧场物语与符文工房':'种植、养殖、节庆和人际养成构成慢节奏经营，符文工房再加入迷宫与动作战斗。早期英文 Harvest Moon 与后来品牌变更不能倒套。',
'高级战争':'以透明兵种数值、地形与指挥官能力形成易读战棋，NDS 双屏与双战线改变指挥方式。',
'光明与梦幻模拟战':'光明系列与梦幻模拟战都含奇幻和战略元素，但制作班底、战斗视角与系统不同，必须拆成两个子系列。',
'皇家骑士团':'以战争政治、阵营选择与职业养成为核心，Ogre Battle 的实时军团制与 Tactics Ogre 的网格战棋也不是同一玩法。',
'格兰蒂亚':'以行动顺序干预和冒险旅程见长，Game Arts 制作的系列不应把发行商写成 Enix 或 Bandai。',
'幻想水浒传':'收集 108 星宿、建设据点并在个人与战争尺度间切换，群像招募是系列最重要的结构。',
'女神转生与女神异闻录':'本传偏恶魔交涉、末世与阵营选择，Persona 更强调人物关系和现代生活，两者应作为相关子系列而非同义标题。',
'索尼克':'强调速度、惯性和立体分支路线，MD 2D 与 DC 3D 作品的镜头及关卡逻辑差异明显。',
'星之卡比':'以吞噬复制、轻量平台动作和多能力解谜为主，部分作品改用车线、触控或非线性地图实验。',
'雷顿教授':'把动画式剧情与大量独立谜题结合，前三部构成初代三部曲，后续作品另有前传关系。',
'黄金太阳':'以精神力解谜、精灵配置和召唤构成 JRPG 系统，前两作直接接续，NDS《漆黑的黎明》则转向后代故事。',
'王国之心':'将原创角色与迪士尼、Square Enix 世界放入动作 RPG，记忆之链使用卡牌，梦中降生采用三主角视角。',
'前线任务':'聚焦机甲部件、政治军事与战术部署，序号正传多为战棋，Gun Hazard 与 Alternative 则尝试动作或实时方向。',
'梦幻之星':'早期以科幻与奇幻混合的 JRPG 世界为特色，Online 则转向联网动作与刷装，二者不是同一玩法延续。',
'星之海洋':'由 tri-Ace 打造，以即时战斗、技能与科幻文明冲突为特色，早期发行主体是 Enix。',
'沙加':'强调自由剧本、闪悟或非常规成长，不采用传统单线等级结构；GB、SFC 与 NDS 重制需按版本区分。',
'龙战士':'以龙族变身和传统 JRPG 探索为特色，Capcom 制作，不能写成“龙翼传说”的同一官方译名。',
'露娜':'以重视角色演出的传统 JRPG 见长，PS1 Complete 版加入动画和重制内容，与更早 CD 版有版本差异。',
'荒野兵器':'把西部片意象、枪械与奇幻 JRPG 结合，以角色固有能力解谜和回合战斗推进。',
'战场女武神':'在回合部署中即时操纵单位移动与射击，绘本式画面和战场地形是标志，PSP 两作转为学园与更密集任务结构。',
'古惑狼':'以纵深视角平台跳跃、箱子收集和障碍节奏见长，赛车衍生则采用漂移蓄力竞速。',
'小龙斯派罗':'以滑翔、冲撞和火焰探索彩色 3D 关卡，收集宝石与救龙是早期作品主要驱动力。',
'古墓丽影':'以网格化空间、跳跃解谜和遗迹探索构成 3D 动作冒险，早期固定坦克式操作需要适应。',
'铁拳':'以四键对应四肢、侧移与浮空连段构成 3D 格斗，家用版通常加入角色与额外模式。',
'GT赛车':'以真实车款、驾照挑战、调校和赛事经营建立家用拟真赛车范式，是 Polyphony Digital 的代表系列。',
'山脊赛车':'以易上手的漂移和街机节奏为卖点，Type 4 更以车队叙事、美术与音乐形成独特风格。',
'数码宝贝':'围绕数码兽养成、进化和迷宫或世界探索展开，各作系统差异很大，不能仅按序号推断质量。',
'天外魔境':'以和风幻想、夸张角色与 CD 音画演出构成 RPG／冒险系列，Hudson 与 Red 的呈现是 PCE CD 代表内容。',
'怒首领蜂与Cave':'以密集弹幕、连击和打分路线构成射击挑战，通关与高分玩法差异很大；后期基板在 N4100 上需单独测试。',
'合金弹头':'以手绘像素、夸张动画和跑射 Boss 战见长，Nazca／SNK 的街机系列与 GBA 便携原创版应区分。',
'饿狼与龙虎之拳':'SNK 早期格斗分别以线移动、气力与角色故事建立特色，也共同构成拳皇的角色基础。',
'快打旋风':'以简洁拳脚、武器与敌群管理奠定 Capcom 清版动作风格，SFC 移植版在合作和角色上曾受硬件限制。',
'战斧':'以骑乘、魔法瓶与多人合作构成奇幻清版动作，MD 的 II／III 与街机《死亡蝰蛇的复仇》不是同一编号体系。',
'宇宙巡航机与兵蜂':'以卷轴射击、武器升级与关卡记忆为核心，Parodius 和 TwinBee 则以幽默、明亮风格另开支线。',
'雷电与R-Type':'雷电偏重武器颜色与双人快节奏，R-Type 偏重蓄力、Force 装置与严密关卡记忆，两者均有 MD 正式移植。',
'Darius':'以多屏或宽屏演出、区域分支和机械海洋生物 Boss 著称，不同街机与家用版本不可只按标题互换。',
'世界树迷宫':'玩家亲自绘制迷宫地图，并以职业小队应对 FOE 与资源压力，是 NDS 双屏用途最有说服力的 RPG 之一。',
'寄生前夜':'把线粒体科幻、纽约舞台与 RPG 成长结合，续作更偏生存恐怖动作，《第三次生日》则进一步转向射击。',
}

# 非系列条目的精确短注，保留游戏内容与历史信息。
feature_rules=[
(r'Tetris','下落的四格方块需要旋转、堆叠并消除整行，规则极简却有长期竞技深度。任天堂 GB 版随掌机捆绑，使俄罗斯方块成为便携游戏的全球现象。'),
(r'Dr\. Mario','把彩色胶囊与病毒配对消除，玩法更接近连锁规划而非传统落块。它把马力欧角色包装用于益智游戏，并长期衍生多个版本。'),
(r'Excitebike','越野摩托需要控制落地姿态与引擎温度，赛道编辑器在 FC 早期很有创意。它展示了简单规则与物理手感结合的魅力。'),
(r'Duck Hunt','使用 NES Zapper 射击屏幕中的飞鸭，属于光枪外设游戏；普通手柄无法完整还原原体验。'),
(r'Balloon Fight','利用拍翼惯性与气球浮力进行空中对战，既可合作也可互相干扰。其物理手感与街机《Joust》有渊源。'),
(r'Mario Bros\.','在固定单屏水管场景撞击地板并踢走敌人，是马力欧与路易吉共同登场的早期街机作品，与后来卷轴式《Super Mario Bros.》不同。'),
(r'Donkey Kong$','玩家躲避木桶、跨越平台营救目标， Jumpman 后来发展为马力欧。1981 年街机原作与 FC 移植是角色史和平台动作史的共同起点。'),
(r'Bomberman','在网格迷宫中放置炸弹、打通砖墙并争取道具，爆炸连锁既能杀敌也可能困住自己。多人对战后来成为系列最有影响力的方向。'),
(r'Contra$','以跑射、散弹等武器和双人协作挑战外星敌军，FC 版关卡经过重新设计。30 条命秘籍也使其成为共享卡带时代的文化记忆。'),
(r'Super C$','延续双人跑射，并在部分关卡切换俯视角，敌群与 Boss 节奏更紧凑。它常被称作“魂斗罗 2”，但正式海外名是 Super C。'),
(r'Ninja Gaiden II','加入影分身，让分身复制玩家动作与攻击，关卡仍强调精准跳跃和敌人位置记忆。电影化过场是 FC 三部曲的共同特色。'),
(r'Ninja Gaiden III','增加抓攀与剑光强化，日版和美版在难度、续关等方面存在明显差别。评价不宜简单概括为“系列最差”。'),
(r'Adventure Island','以连续前进、滑板与武器投掷挑战时间槽，手感继承自《Wonder Boy》相关开发脉络。高桥名人的形象是系列识别标志。'),
(r'Battle City','保护基地老鹰并用坦克击毁敌军，可双人合作，也能利用地形与升级改变防线。内置关卡编辑让它在 FC 时代很耐玩。'),
(r'Circus Charlie','以跳火圈、走绳、骑马和空中飞人等短项目组成街机式关卡，是 Konami 的早期作品，不应写成 Hudson。'),
(r'Shadow of the Ninja','两名忍者可用刀与锁镰配合闯关，强调双人合作和武器等级保持。Natsume 的像素、音乐与动作节奏使其成为 FC 后期佳作。'),
(r'Sangokushi$','以君主治理、外交与战争统一中国，是光荣历史模拟在家用机上的早期形态。菜单和数值较朴素，但奠定了系列基本循环。'),
(r'Nakahara no Hasha','Namco 的 FC 三国战略游戏，与光荣《三国志》不是同一系列。武将和即时作战呈现使其在中文玩家中形成独立记忆。'),
(r'Haou no Tairiku','Namco《中原之霸者》的续作，保留三国君主争霸并深化战场指挥。“南晶科技制作”是常见误传，实际原厂为 Namco。'),
(r'Destiny of an Emperor','Capcom 把三国题材做成队伍制 RPG，以兵力代替传统生命并围绕武将招募推进。它是正式商业作品，不是同人改版。'),
(r'Shokatsu Koumei Den','延续 Capcom 三国 RPG，围绕诸葛亮相关剧情扩展队伍与阵形。中文传播广泛，但应与同名街机清版游戏区分。'),
(r'Captain Tsubasa','把足球比赛指令化，射门、过人与门将对抗带有必杀技演出。Tecmo 的改编奠定了“足球 RPG”这一独特体验。'),
(r'Fire Emblem Gaiden','采用双主角路线、可探索村镇与地牢，系统和系列其他作品差异较大。它是 1992 年 FC 第二作，后来重制为《回声：另一位英雄王》。'),
(r'Blaster Master','战车横版探索与人物俯视迷宫交替，获得升级后返回旧区域开路。Sunsoft 将两套视角与地图成长紧密结合。'),
(r'Journey to Silius','Sunsoft 的科幻跑射作品，以多武器和优秀芯片音乐著称。它并非魂斗罗官方续作，“星际魂斗罗”只是中文俗称。'),
(r'Jackal','驾驶吉普车营救战俘，机枪与榴弹可分别应对步兵和重火力，双人协作很有特色。车辆移动与射击方向的关系是操作关键。'),
(r'The Legend of Kage','忍者可在树林与城郭间高跳，以刀和手里剑迎战敌人。Taito 街机移植的动作轻盈，短循环适合反复挑战。'),
(r'Lode Runner','通过挖掘左右地面困住守卫、收集金子并抵达出口，核心是路线规划而非战斗。关卡编辑器延长了作品寿命。'),
(r'Ice Climber','用锤子击碎头顶冰层并逐层登山，跳跃惯性独特。双角色波波与娜娜后来也因大乱斗扩大了认知度。'),
(r'Yie Ar Kung-Fu','在固定场地与不同招式对手进行一对一格斗，是早期对战动作的重要作品，但系统不能直接等同后来的《街霸 II》。'),
(r'Link’s Awakening','在谜样岛屿收集乐器并探索迷宫，离岛设定与结局赋予故事淡淡忧伤。DX 增加色彩与隐藏迷宫，原版则保留 GB 单色风味。'),
(r'Oracle of Seasons','以四季之杖改变环境，偏重战斗和动作谜题；与《时空之章》可通过密码联动，打通真结局与额外内容。'),
(r'Oracle of Ages','以时光竖琴在过去与现在之间切换，偏重场景谜题。它与《大地之章》是互补双作，不是简单版本差异。'),
(r'Shantae$','半精灵桑塔以头发攻击和动物变身探索城镇与迷宫，动画在 GBC 上非常出色。GBA 已发售后才推出使其当年商业表现有限，后来逐步发展为系列。'),
(r'Ghost Babel','以独立世界观呈现掌机潜行任务，并加入大量 VR 挑战。它虽在西方使用 Metal Gear Solid 标题，却不是 PS1 主线移植。'),
(r'Dragon Warrior Monsters','以怪物收服、交配继承与随机迷宫展开，为勇者斗恶龙建立长期怪兽养成支线。'),
(r'Wario Land 3','瓦力欧没有传统生命耗尽，敌人更多造成状态变化并反向参与解谜；宝藏和新能力推动非线性探索。'),
(r'Wario Land II','以不死身、受击变身与分支关卡改变平台动作逻辑，既有 GB 版也有 GBC 彩色版。'),
(r'Super Mario Bros. Deluxe','在 GBC 上重制 FC 初代，并加入挑战、相册等内容；掌机视野较窄，需要适应卷轴显示。'),
(r'Survival Kids','在荒岛收集食物、材料并制作工具，选择会影响路线与结局。它是 Konami 早期掌机生存游戏，也是后来《迷失蔚蓝》的前身。'),
(r'Star Ocean: Blue Sphere','把星之海洋故事带到 GBC，采用俯视动作战斗与大量角色技能，是系列少见的掌机原创章节。'),
(r'Wily Wars','以 16 位画面重制元祖洛克人 1–3，并追加原创“威利塔”。它是合集重制，不是单纯把 FC ROM 装进 MD。'),
(r'Thunder Force IV','多方向纵卷轴关卡、五种常用武器与 later 强化形成高自由射击，Technosoft 以视差和高速画面展示 MD 机能。'),
(r'Alien Soldier','以大量连续 Boss、武器能量与冲刺反击构成高强度动作，Treasure 几乎舍去普通关卡来突出对战设计。'),
(r'Beyond Oasis','以即时动作、精灵召唤与迷宫解谜推进冒险，古代祐三参与作曲。它是 MD 原创动作 RPG，欧版常名 The Story of Thor。'),
(r'Comix Zone','主角被吸入自己的漫画，战斗发生在分镜格中，可翻页、撕纸并利用场景。形式与机制紧密结合，但难度较高。'),
(r'Ristar$','靠伸缩双臂抓握、攀爬与撞击移动，关卡围绕弹性动作设计。它是 Sonic Team 在 MD 后期塑造的另一套平台角色方案。'),
(r'Phantasy Star II','以队伍制科幻 RPG、迷宫和较沉重剧情推进，是 MD 早期大容量代表作；随机遇敌和难度带有明显时代特征。'),
(r'Rocket Knight','负鼠火箭骑士以喷气冲刺改变攻击与移动方向，蓄力时机贯穿关卡。Konami 将角色能力、Boss 与 MD 视差表现结合。'),
(r'Castlevania: Bloodlines','两位主角分别使用鞭与长枪，关卡横跨欧洲并加入分岔。它与 FC／SFC 作品并列，是 MD 独立原创恶魔城。'),
(r'Shining Force II','自由探索与网格战棋交替，队伍转职、角色收集和大地图冒险更完整。Camelot 的作品不是《光明力量 III》的 DC 版本。'),
(r'Landstalker','采用等距视角与精确跳跃，结合装备、迷宫和城镇解谜。空间判断有学习成本，但关卡构造在 MD 动作 RPG 中很有辨识度。'),
(r'Wonder Boy in Monster World','以装备、魔法和伙伴辅助探索相互连接的地区，节奏介于动作平台与 RPG 之间。它属于 Westone 的怪物世界支线。'),
(r'Gun Hazard','把前线任务机甲带入横版动作，驾驶员可离机，部件与武器可自由改装。它由 Square 与 Omiya Soft 等合作开发，不是传统网格战棋。'),
(r'Trials of Mana','六名主角决定开场与部分路线，职业转职和多人动作战斗提供重玩价值。SFC 原版长期未正式海外发行，后来才以 Trials of Mana 推出。'),
(r'Secret of Mana','环形菜单管理道具与魔法，实时战斗支持多人合作。音乐和世界氛围突出，系统与后来的 Trials of Mana 又有所不同。'),
(r'Tales of Phantasia','以线性动作战斗、主题曲和大量语音展示 SFC 后期制作规模，是 Namco 传说系列起点，发行方不是 Square。'),
(r'EarthBound','把现代小镇、流行文化与奇异敌人放进回合制 RPG，滚动血条给抢救治疗留下窗口。其幽默与温情使 MOTHER 系列形成独特地位。'),
(r'Live A Live','多个时代与主角的短篇各自采用不同机制，最终在主线汇合。章节式结构和“同时代多视角”后来在 HD-2D 重制中再次受到关注。'),
(r'Terranigma','以动作战斗与复兴世界为主题，从大陆、生命到文明逐步恢复地球。Quintet 的作品与《Soul Blazer》《Illusion of Gaia》常被并置讨论。'),
(r'F-ZERO X','以极高速度、30 台赛车同场和能量取舍构建竞速，随机生成赛道模式也延长寿命。N64 的流畅感比画面细节更重要。'),
(r'GoldenEye 007','任务目标随难度增加，潜行与射击并存，四人分屏对战尤其影响家用 FPS。它是 Rare 开发的电影改编成功案例。'),
(r'Perfect Dark','继承黄金眼框架并加入外星阴谋、武器副功能和模拟对手，多人内容更丰富。部分模式依赖 Expansion Pak，N4100 上需降低渲染负担。'),
(r'Banjo-Kazooie','班卓与卡祖笛通过组合动作收集音符和拼图，世界内部探索与能力学习层层开放。Rare 将幽默、音乐和收集型 3D 平台设计结合。'),
(r'Paper Mario$','把角色与场景做成纸片剧场，回合战斗中通过按键时机增强攻防。伙伴能力与徽章构筑使其区别于传统马力欧 RPG。'),
(r'Pokémon Snap','沿固定轨道拍摄宝可梦的自然行为，用道具诱发动作并按构图与瞬间得分。它把收集欲转化为观察与摄影，而非对战。'),
(r'Sin and Punishment','在强制前进关卡中移动、瞄准并近战反击，Treasure 将轨道射击与动作操作结合。N64 日本原版后来经数字发行被更多海外玩家认识。'),
(r'Ys Book I & II','采用冲撞攻击与较简明的成长结构，PCE CD 版加入配音、动画和重编音乐。它常被视为早期 CD-ROM RPG 音画表现的标志。'),
(r'Gate of Thunder','以三种可切换武器、高速敌群和摇滚 CD 音轨构成横版射击。它是 Hudson 的 Thunder 系列，不是 Jaleco 作品。'),
(r'Lords of Thunder','把射击舞台转为重金属奇幻，四种铠甲对应不同攻击流派，关卡前可调整装备。CD 音轨是体验核心。'),
(r'Ginga Fukei Densetsu Sapphire','利用 Arcade Card 展现缩放、伪 3D 与大型 Boss，是 PCE 后期技术展示型射击。收藏和模拟时要确认 Arcade CD 系统支持。'),
(r'Neutopia','以俯视迷宫、剑与道具探索构成类塞尔达冒险，Hudson 的系列共有两作。它并非塞尔达官方移植，而是 PCE 自有同类作品。'),
(r'Dungeon Explorer','以多人动作 RPG、职业选择和迷宫刷怪构成合作体验，可看作 PCE 对 Gauntlet 式玩法的扩展。'),
(r'Tokimeki Memorial','安排学习、社团和约会并维持属性与角色关系，角色评价会相互影响。它确立了 1990 年代恋爱模拟的一种主流结构。'),
(r'Rhythm Tengoku','用极简画面和音乐节拍组织一串短小游戏，判定强调听觉而非视觉。GBA 系列首作直到 NDS 续作推出后才更广为人知。'),
(r'Ninja Five-O','忍者以刀、忍术和钩索在房间中救援人质，动作紧凑且路线自由。Konami 发行量小、完成度高，是 GBA 后期动作佳作。'),
(r'Astro Boy: Omega Factor','Treasure 把阿童木的飞行、拳击与光束做成高速清版动作，角色图鉴和能力成长串联手冢宇宙。它是授权改编中少见的系统精品。'),
(r'Klonoa: Empire of Dreams','用风弹抓敌并投出或二段跳，关卡以机关解谜为主。它是 GBA 原创掌机篇章，与家用机《通往幻界之门》不同。'),
(r'Mario vs. Donkey Kong','先直接操纵马力欧解机关，再引导迷你马力欧玩具抵达目标，平台动作与益智规划结合。它开启了长期的“马力欧对咚奇刚”系列。'),
(r'Tactics Ogre: The Knight of Lodis','以等距战棋、职业与阵营选择展开外传故事，节奏适合掌机但养成仍很深入。它是 Quest 作品，日本由 Nintendo 发行。'),
(r'Boktai','卡带阳光传感器影响武器充能、场景与战斗，主角用太阳枪对抗不死族。小岛组把真实光照变成核心机制，模拟时需确认传感器映射。'),
(r'WarioWare Twisted!','卡带陀螺仪让旋转机体成为操作方式，数秒小游戏围绕转动不断变体。模拟时要配置运动传感器，否则体验不完整。'),
(r'Etrian Odyssey$','玩家用触屏逐格绘制地图，队伍技能与 FOE 位置管理同样重要。它把“地图由玩家完成”变成探索和记忆的一部分。'),
(r'Rhythm Heaven$','以触屏滑动、点按和长按配合节奏，关卡围绕不同音乐规则展开。NDS 日版名《节奏天国 Gold》。'),
(r'Professor Layton','在调查场景与人物对话中发现谜题，以提示币和多种题型推动冒险。Level-5 用动画与音乐把短篇益智包装成完整旅程。'),
(r'Rune Factory','在牧场经营外加入武器战斗、怪物驯养与迷宫推进，形成“种田＋动作 RPG”结构。它是牧场物语衍生并逐步独立的系列。'),
(r'Kingdom Hearts 358/2 Days','以洛克萨斯在 XIII 机关的日常任务串联故事，面板系统决定魔法、能力与等级配置。它补充了《王国之心 II》前后的角色背景。'),
(r'Shantae$','半精灵桑塔以头发攻击和动物变身探索城镇与迷宫，动画在 GBC 上非常出色。GBA 已发售后才推出使其当年商业表现有限，后来逐步发展为系列。'),
(r'Grand Theft Auto: Chinatown Wars','采用俯视角与触屏交互，在自由城完成帮派任务、驾驶和小游戏，毒品交易经济是特色。NDS 与 PSP 版本在画面和操作呈现上不同。'),
(r'Soulcalibur$','武器格斗以八向移动、横纵斩与格挡反击构成，DC 版又加入大量任务模式。其街机移植完成度与画面曾长期作为 DC 技术展示。'),
(r'Crazy Taxi$','在限时内接送乘客，以跳跃、漂移和高速穿插提高小费并续时。它将开放街区作为得分场，而非拟真驾驶。'),
(r'Power Stone 2','四人在可变化场景中拾取武器、机关与能量宝石，变身混战是核心。相比初代更偏派对乱斗。'),
(r'Phantasy Star Online$','以实时动作、职业与掉落装备构建大厅组队 RPG，是家用机网络游戏的重要里程碑。离线可体验部分内容，但原官方服务器早已停止。'),
(r'Rez$','在轨道中锁定目标并释放射击，音效与电子音乐节拍、画面振动同步。它是水口哲也“联觉”设计理念的代表。'),
(r'Space Channel 5','按节奏记忆并复现方向与射击指令，以舞蹈对抗外星人。世嘉把音乐游戏、电视秀和复古未来审美结合。'),
(r'The Typing of the Dead','把《死亡之屋 2》的扳机替换为键盘输入，以打字速度和准确度击杀僵尸。戏谑外表下确实能训练输入。'),
(r'ChuChu Rocket!','在棋盘上放置方向箭头，引导小鼠进入火箭并避开猫，单人谜题与多人抢鼠同样重要。它也是 DC 早期联网代表之一。'),
(r'Samba de Amigo','跟随音乐节拍挥动沙锤并定位高低区域，DC 原版体验依赖专用控制器；普通手柄只是替代方案。'),
(r'Monster Hunter Freedom Unite','以武器动作、怪物生态和素材装备构成长期狩猎循环，G 位任务与随从猫扩展内容。英文版名为 Freedom Unite。'),
(r'Monster Hunter Portable 3rd','加入结云村、新怪物与随从猫双编制，武器动作进一步调整。PSP 日版未正式海外本地化，内容差异不宜只用“更多／更少”概括。'),
(r'Trails in the Sky FC','以艾丝蒂尔和约修亚的准游击士旅程铺开利贝尔危机，城镇 NPC 文本随剧情更新。FC 的结尾直接进入 SC，建议按顺序游玩。'),
(r'Trails in the Sky SC','承接 FC 的分离与结社阴谋，扩大全国旅行与战斗系统。它不是可独立理解的外传，而是利贝尔篇下半部。'),
(r'Persona 3 Portable','在校园日程、社群与塔尔塔罗斯探索间分配时间，PSP 版允许直接操作队友并新增女主角路线。静态场景降低了 3D 负担。'),
(r'Ys: The Oath in Felghana','以《伊苏 III》剧情为基础全面重制，改用跳跃、连击与魔法构成高速动作。它不是简单外传，也不等于 PCE 旧版画面升级。'),
(r'Ys Seven','引入三人小队、切换角色与属性克制，告别传统冲撞系统。它是 PSP 时期系列转向小队动作的重要节点。'),
(r'Kingdom Hearts: Birth by Sleep','泰拉、阿库亚与维恩图斯三条路线互补，指令牌组和射击锁构成战斗成长。剧情是本传前史，不是可忽略的小品。'),
(r'Patapon$','用不同鼓点组合指挥眼球小人行军、攻击与防御，节奏输入同时是策略命令。它由 Sony 日本工作室打造，并非传统战棋。'),
(r'LocoRoco$','通过倾斜场景与分裂／合体引导乐克乐克滚动，重力与歌声构成轻松解谜。原创 PSP 物理操作是其核心。'),
(r'Silent Hill: Shattered Memories','以哈利寻找女儿为起点重新诠释初代，心理测试会改变人物与场景呈现，追逐段落取代常规战斗。它不是《起源》的续作。'),
(r'Dissidia Final Fantasy','把历代角色放入立体场地，以勇气值与 HP 攻击分离资源，兼具格斗和动作 RPG 养成。'),
(r'Parasite Eve$','在圣诞夜的纽约对抗线粒体异变，战斗在可移动遇敌与 ATB 指令间切换，武器改造与克莱斯勒大厦扩展养成。'),
(r'Parasite Eve II','转向更直接的生存恐怖操作，固定场景、弹药与魔法资源管理更接近生化危机。故事延续阿雅，但玩法变化明显。'),
(r'Klonoa: Door to Phantomile','在 2.5D 关卡中以风弹抓敌、投掷和二段跳，背景纵深也参与路径与机关。Namco 的童话演出与隐含悲伤使其独具气质。'),
(r'R4: Ridge Racer Type 4','以车队与赛季叙事串联赛事，漂移手感、车辆设计和爵士电子配乐高度统一。它是 PS1 时代街机赛车美术设计的代表。'),
(r'Ape Escape$','用双摇杆分别移动与操作捕猴网、工具，充分发挥 DualShock 结构。它是早期围绕双模拟摇杆设计的主流 3D 游戏之一。'),
(r'PaRappa the Rapper','按节奏依次输入指令并模仿说唱，玩家也可偏离节拍争取更高评价。七日式图形与音乐叙事让它成为 PS1 音游符号。'),
(r'Vib-Ribbon','把音乐分析成极简线条障碍，兔子随节拍跳跃躲避。可读取音乐 CD 生成关卡的创意使其成为独特技术实验。'),
(r'Wild Arms','把西部荒野、枪械与幻想遗迹结合，角色工具用于场景解谜，回合战斗强调队伍能力。续作扩大世界并改变镜头和系统。'),
(r'Clock Tower: The First Fear','以点选调查、躲藏和剪刀男追逐制造无力感，主角没有常规战斗手段。PS1 版是 SFC 初代的增强移植。'),
]

def make_note(e):
    if e.en in notes_exact:return notes_exact[e.en]
    for p,n in feature_rules:
        if re.search(p,e.en,re.I):return n
    if e.series in series_note:return series_note[e.series]
    # 最后才使用类型化说明，仍避免“神作／续作／不错”这类无信息评价。
    if re.search(r'Racing|Racer|Rally|OutRun|Daytona|Hang-On|Wave Race|Snowboarding|Hydro Thunder|Gran Turismo',e.en,re.I):
        return '以赛道记忆、车辆操控与成绩挑战为核心，适合短局反复练习。本作属于该平台竞速库的一部分，具体物理与内容以对应街机或家用版本为准。'
    if re.search(r'Fighter|Fighting|Fury|Kizuna|Samurai|Mortal Kombat|Killer Instinct|Darkstalkers|Vampire|JoJo|Marvel|Capcom vs|Rival Schools|Power Stone',e.en,re.I):
        return '以角色招式、距离判断和对战博弈为核心，单人通关与本地双人是主要玩法。街机原版、家用移植及修订版的角色和平衡可能不同，应按完整标题收藏。'
    if re.search(r'Gradius|R-Type|Raiden|Strikers|Gunbird|Truxton|Vimana|Garegga|Darius|Thunder|Xevious|Galaga|Space Invaders|Fantasy Zone|After Burner|Space Harrier|Gunhed|Blazing Lazers|Cotton|Magical Chase|Download|Dead Moon|Image Fight|Out Zone|Twin Cobra|Fire Shark|Batsugun',e.en,re.I):
        return '卷轴射击以武器选择、关卡记忆和敌弹回避为核心，高分路线往往比单纯通关更复杂。保留它可补足该平台射击史与不同厂商风格的样本。'
    if re.search(r'Puzzle|Bubble|Columns|Lemmings|Picross|Panel de Pon|Driller',e.en,re.I):
        return '以空间判断、连锁或规则规划构成益智玩法，短局之外也有持续优化空间。版本差异主要体现在关卡、模式与联机，而不是剧情。'
    if re.search(r'Panzer|Civilization|Daisenryaku|Military Madness|Vandal Hearts',e.en,re.I):
        return '围绕单位部署、地形、资源与回合决策展开，属于偏系统的战略作品。它保留了早期家用战争模拟的界面与节奏，适合慢节奏研究。'
    if re.search(r'DDR|Dance Dance|beatmania|pop’n|GuitarFreaks|DrumMania|Taiko|DJMax|Project DIVA|GITADORA',e.en,re.I):
        return '以音乐节拍输入、谱面判定和难度进阶为核心。专用控制器能显著改变体验，后期街机版本还需核对 CHD、IO 与性能支持。'
    if re.search(r'Golf|Tennis|NBA|NFL|Jam|Super Monaco|Fishing',e.en,re.I):
        return '将现实运动规则压缩为适合主机的节奏，兼顾单人赛季与本地多人。作品价值主要来自操作、队伍或赛事模式，而非剧情。'
    if re.search(r'Final Fight|Double Dragon|Knights of the Round|Captain Commando|Punisher|Cadillacs|Simpsons|Sunset Riders|Violent Storm|Night Slashers|Golden Axe|King of Dragons|Armored Warriors|Battle Circuit|Dungeon',e.en,re.I):
        return '以横版推进、敌群管理、拾取武器和多人合作为核心，是街机清版动作谱系的一部分。角色性能和关卡机制让重复游玩仍有练习价值。'
    if re.search(r'Prince of Persia',e.en,re.I):
        return '以精确跳跃、机关计时和冷兵器决斗推进地牢逃生，动画采用转描技术呈现真实动作。不同家用版本的关卡与操作细节有差异。'
    return '本作保留了该平台有代表性的关卡、规则或题材，适合用于扩充类型覆盖。备注不以空泛评分代替实际内容；具体地区版和修订版请按商品名与 ROM 信息识别。'

# 标题排序：保留原顺序，补充作品排在该平台末尾。生成稳定 ID。
counts={}
for e in entries:
    counts[e.platform]=counts.get(e.platform,0)+1
    e.eid=f'{short[e.platform]}-{counts[e.platform]:03d}'
    e.note=make_note(e).replace('|','／').replace('\n',' ')

# 平台标题与介绍。
platform_intro={
'NES / FC':'8 位家用机与 Famicom 正式作品。中文俗称很多，表中以商品原名消除“星际魂斗罗”“霸王的大陆”等误归属。',
'GB / GBC':'同时覆盖黑白 GB、彩色 GBC 与双平台黑卡；DX、重制和衍生作品分别标明，不把 GBA 游戏混入。',
'MD / Genesis':'Mega Drive 与 Genesis 为同一硬件的地区名称。保留正式移植版，删除无法对应商品的条目和重复中文别名。',
'SNES / SFC':'16 位任天堂平台。补入《超级恶魔城 IV》《重装机兵 2》等关键缺项，并区分 Square、Enix 与各自作品。',
'N64':'以第一方、Rare 与高完成度第三方作品为主。Expansion Pak 和重负载画面会影响模拟表现，容量为预留预算。',
'PCE (PC Engine / TurboGrafx-16)':'同时包含 HuCard、CD‑ROM²／Super CD 与 Arcade Card 作品；光盘容量不能按卡带大小估算。',
'GBA':'补入红宝石／蓝宝石、节奏天国与 Treasure／Konami 动作佳作；删除不存在的 DQ 移植和民间改版。',
'NDS':'按双屏、触控、RPG、文字冒险等实际体验筛选。赤／青救助队为双版本，其他误平台作品已移除。',
'街机（FBNeo / MAME）':'这是“游戏目录”，不是一个可随意混用的 ROM set。CPS／Neo Geo／PGM 优先 FBNeo，NAOMI、Model 2／3 与后期音游按各自核心和 Batocera 版本处理。',
'Dreamcast':'以 DC 原创与高完成度 NAOMI 移植为主。补入《永恒的阿卡迪亚》，删除 Saturn《光明力量 III》等错平台条目。',
'PSP':'以 1× 渲染可实际尝试的作品为主，重型 3D 游戏须逐段验证。删除重复怪物猎人和不存在的原生 FFV／FFVI 移植。',
'PS1':'兼顾高分榜、类型史与中文圈常用作品。补入托尼·霍克、DQVII、风之少年等，并删除 PS2／PC／Saturn 误项。',
}

def table_for_platform(p, es):
    out=[f'### {p}', '', f'<a id="platform-{short[p].lower()}"></a>', '', platform_intro[p], '',
         '| 条目 | 完整商品名（英文／日文） | 中文译名 | 首发年份 | 发行方／历史发行主体 | 预留空间 | 内容·历史备注 |',
         '|---|---|---|---:|---|---:|---|']
    for e in es:
        year=e.year or '—'
        out.append(f'| <a id="{e.eid.lower()}"></a>{e.eid} | {e.en.replace("|","／")} | {e.zh.replace("|","／")} | {year} | {e.pub} | {e.size} | {e.note} |')
    return out

# 目录与专题。
out=[]
out += ['# Batocera 精选游戏与系列对照指南','',
'> 适用环境：Intel Celeron N4100（Gemini Lake，4 核 4 线程）＋UHD 600＋4 GB 内存＋Batocera。存储采用 SSD 主目录与 eMMC 分平台目录软链接，不使用 mergerfs。','',
'本版是完整修订稿：删除重复、错平台、虚构名称和民间改版，统一完整商品名与中文译名，逐条补写玩法／历史备注，并把专题双向链接到平台条目。这里的“精选”不是声称收录每款好游戏，而是在类型、系列史、中文圈经典与 N4100 可运行性之间做取舍。','',
'## 总目录','',
'- [使用说明与版本规则](#使用说明与版本规则)','- [存储分配与 Batocera 实操](#存储分配与-batocera-实操)','- [各平台精选清单](#各平台精选清单)']
for p in platform_heads:
    out.append(f'  - [{p}](#platform-{short[p].lower()})')
out += ['- [专题系列图鉴](#专题系列图鉴)']
series_order=[]
for e in entries:
    if e.series and e.series not in series_order:series_order.append(e.series)
for s in series_order:
    out.append(f'  - [{s}](#series-{series_order.index(s)+1:02d})')
out += ['- [榜单补漏方法与结论](#榜单补漏方法与结论)','- [容量汇总与性能建议](#容量汇总与性能建议)','',
'---','','## 使用说明与版本规则','',
'1. **一行不一定只有一个 ROM。** 标题中明确写“系列”“1／2／3”的行是合集式收藏建议，数量统计使用“条目”而非伪装成精确游戏数。实际安装时应拆成独立商品，方便刮削、存档与专题链接。','2. **完整商品名优先于中文俗称。** 例如《Journey to Silius》保留“星际魂斗罗”作为中文俗称，但备注明确它不是魂斗罗官方续作；《Super Mario USA》与海外《Super Mario Bros. 2》不再重复占两行。','3. **发行方按历史主体书写。** Square 与 Enix 的早期作品不倒填 Square Enix；开发者与发行商不同的作品在必要处并列。地区版发行方可能不同，因此表列是主要发行主体，不是全部地区版权清单。','4. **首发年份仅在可可靠确认时给出。** 跨地区或多作合集以“—”表示，避免把移植年、合集年和原作年混成一个数字。','5. **预留空间不是 ROM 实测大小。** 它用于容量预算；实际受地区版、修订版、CHD 压缩、光盘音轨和合集拆分影响。文末按表内预算重新求和。','6. **合法性。** 请仅备份自己合法拥有的游戏与 BIOS；本文不提供下载地址，也不把盗版、汉化改版或 hack 当作官方商品。','',
'---','','## 存储分配与 Batocera 实操','',
'### 存储分工','',
'| 位置 | 平台 | 理由 |','|---|---|---|','| eMMC 独立 ext4 分区，目录级软链接 | NES、GB／GBC、MD、SNES、N64、PCE、GBA、NDS、FBNeo／MAME 的小体积 ROM | 以顺序读取为主，容量小；保留 SSD 给光盘镜像与高频写入 |','| SSD 的 `/userdata` | PS1、Dreamcast、PSP，以及全部存档、配置、缓存和刮削数据 | 大镜像与随机写入集中，避免 eMMC 寿命和空间压力 |','',
'### 挂载与软链接','',
'先用 `blkid` 和 `lsblk` 确认设备，不要照抄 `mmcblk0p1`。以下假设 eMMC 数据分区挂载到 `/mnt/emmc`：','',
'```bash','mkdir -p /mnt/emmc/roms/{nes,gbc,megadrive,snes,n64,pcengine,gba,nds,fbneo,mame}','mkdir -p /userdata/roms','# 仅在目标路径不存在或已确认是旧软链接时创建；不要覆盖已有实体目录','ln -s /mnt/emmc/roms/nes /userdata/roms/nes','ln -s /mnt/emmc/roms/gbc /userdata/roms/gbc','ln -s /mnt/emmc/roms/megadrive /userdata/roms/megadrive','ln -s /mnt/emmc/roms/snes /userdata/roms/snes','ln -s /mnt/emmc/roms/n64 /userdata/roms/n64','ln -s /mnt/emmc/roms/pcengine /userdata/roms/pcengine','ln -s /mnt/emmc/roms/gba /userdata/roms/gba','ln -s /mnt/emmc/roms/nds /userdata/roms/nds','ln -s /mnt/emmc/roms/fbneo /userdata/roms/fbneo','ln -s /mnt/emmc/roms/mame /userdata/roms/mame','```','',
'把分区 UUID 写入持久挂载配置前，先手工挂载并验证读写。Batocera 的持久化方式随版本可能变化，应以当前版本文档为准；不要假设在通用 Linux 下使用的 `/etc/fstab` 写法和 root 权限命令都能直接套用。存档与配置留在 `/userdata`，不要软链接到 eMMC。','',
'### 街机、BIOS 与镜像格式','',
'- **街机按核心管理 ROM set。** Batocera 官方将 FBNeo 放在 `/userdata/roms/fbneo`，MAME 放在 `/userdata/roms/mame`；Neo Geo 可单独显示，NAOMI 与 Atomiswave 走 Flycast 对应目录。ZIP 不要改名或解压，版本应与当前 Batocera 附带核心匹配。','- **IGS PGM 需要对应 BIOS／母带。** Neo Geo、PGM 等依赖文件也要随正确 ROM set 配置。 split、non-merged 与 CHD 依赖不能只复制一个表面文件。','- **BIOS 以本机检查为准。** 在系统菜单运行 BIOS 检查，或执行 `batocera-systems`，同时查看 `/usr/share/batocera/datainit/bios/readme.txt`。不要用固定年份的网络清单替代当前版本校验。','- **PS1／PCE CD 可用 CHD，DC 视核心支持选择 CHD 或 GDI。** 多盘游戏同时维护 `.m3u`，保持各盘文件名一致。转换前先保留原镜像，避免错误操作破坏唯一备份。','- **PSP 优先 ISO 作为兼容基线。** CSO 能省空间但增加解压开销；是否在 N4100 上卡顿取决于游戏和压缩级别，不能笼统断言。','- **每批安装后试玩。** 先测启动、声音、存档和重负载场景，再批量刮削。4 GB 内存下逐平台刮削比一次处理全部库更稳妥。','',
'官方依据：[Batocera Arcade Guide](https://wiki.batocera.org/arcade)、[Advanced arcade emulation](https://wiki.batocera.org/advanced_arcade)、[Add games/BIOS files](https://wiki.batocera.org/add_games_bios)。','',
'---','','## 各平台精选清单','']
for p in platform_heads:
    out += table_for_platform(p,[e for e in entries if e.platform==p])+['','---','']

# 专题说明与子系列链接。
series_intro={
'马力欧':'按平台动作、卡丁车、派对、体育、RPG、瓦力欧、咚奇刚与耀西拆分。卡比不再误并入马力欧，GBA Advance 的对应原作也在平台表中写清。',
'宝可梦':'按正统 RPG、迷宫、护林员及家用机衍生拆分。重装机兵已完全移出本专题。',
'三国志与三国题材':'把光荣《三国志》、Capcom《吞食天地》、IGS《三国战纪》和其他三国题材拆开，避免同名不同厂、不同玩法相互串行。',
'光明与梦幻模拟战':'两个相关但不相同的系列分别列示；《光明力量 III》不属于 DC，因此不在清单中。',
'女神转生与女神异闻录':'本传与 Persona 分列，保留世界观的继承关系但不混作同一序号。',
'洛克人':'按元祖／世界、X、Zero、EXE、ZX 与流星分组，避免只按发行年把不同系统揉在一起。',
'最终幻想':'正传与战略版、VII 衍生分开；同一作品的 SFC、GBA、NDS、PSP 版本保留在对应平台并各自回链。',
'逆转裁判':'GBA 原版与 NDS 复刻分行，《逆转检事》是衍生，《幽灵诡计》仅列同作者相关作品。',
}
for idx,s in enumerate(series_order,1):
    es=[e for e in entries if e.series==s]
    out += [f'### {s}', '', f'<a id="series-{idx:02d}"></a>', '',
            series_intro.get(s,series_note.get(s,''))+' 下表每条“平台条目”均链接回上方的完整备注，专题不再维护另一套可能失真的独立序号。','']
    groups=[]
    for e in es:
        if e.subgroup not in groups:groups.append(e.subgroup)
    for g in groups:
        if len(groups)>1:out += [f'#### {g}','']
        out += ['| 完整商品名 | 中文译名 | 平台 | 年份 | 平台条目 |','|---|---|---|---:|---|']
        for e in es:
            if e.subgroup!=g:continue
            out.append(f'| {e.en} | {e.zh} | {short[e.platform]} | {e.year or "—"} | [{e.eid}](#{e.eid.lower()}) |')
        out.append('')
    out += ['---','']

# 榜单调研与修订结论。
out += ['## 榜单补漏方法与结论','',
'本次不是把原稿“遗漏高分作品调研”另留成建议清单，而是把确定应补的作品直接合并进各平台表。检索覆盖 IGN／Nintendo Life 的任天堂历史榜与分平台榜、Metacritic 的 PS1／PSP 高分榜、Dreamcast 与 N64 高分汇总、Time Extension 的 MD 榜、PCE 与街机类型榜，并交叉核对 Batocera 官方文档。评分会随评论数量变化，因此不以单一分数作为唯一入选理由。','',
'| 检索维度 | 实际补入的代表作品 | 处理原则 |','|---|---|---|','| 任天堂与 NES／SNES／GBA／NDS 榜 | Metroid、Super Castlevania IV、Rhythm Tengoku、Ninja Five‑O、Strange Journey、The World Ends with You | 高分之外兼顾平台独占性与类型覆盖 |','| PS1 高分与销量／历史影响 | Tony Hawk’s Pro Skater 1／2、Crash Team Racing、Dragon Quest VII、Klonoa、Rayman | 不只收 RPG，也补体育、竞速和平台动作 |','| PSP 高分与跨榜常客 | Chinatown Wars、Tekken: Dark Resurrection、Wipeout Pure、Jeanne d’Arc、Dracula X Chronicles | 同时考虑 N4100 负担与原创掌机价值 |','| Dreamcast 高分与 DC 特色 | Skies of Arcadia、3rd Strike、Virtua Tennis、Metropolis Street Racer、ChuChu Rocket! | 删除 Saturn／PS2 错平台后再补 |','| MD／PCE／街机类型史 | Shining Force I／II、Rocket Knight、Spriggan、Sapphire、Batsugun、Blazing Star、Metal Slug | 避免榜单只偏 RPG 或格斗，补射击与清版 |','',
'主要检索入口：[IGN 任天堂百佳](https://www.ign.com/articles/the-100-best-nintendo-games-of-all-time)、[Nintendo Life SNES 50](https://www.nintendolife.com/guides/50-best-super-nintendo-snes-games-of-all-time)、[GBA 50](https://www.nintendolife.com/guides/50-best-game-boy-advance-games-of-all-time)、[NDS 50](https://www.nintendolife.com/guides/50-best-nintendo-ds-games-of-all-time)、[GBC 50](https://www.nintendolife.com/guides/50-best-game-boy-color-gbc-games-of-all-time)、[Metacritic PS1](https://www.metacritic.com/browse/game/ps1/)、[Metacritic PSP](https://www.metacritic.com/browse/game/psp/)、[Time Extension MD 榜](https://www.timeextension.com/guides/best-sega-genesis-mega-drive-games-of-all-time)。','',
'“翻榜单”并不意味着无边界收全所有上榜作品：体育年货、依赖已关闭在线服务的内容、明显超出硬件能力的后期 3D 街机，以及只有硬件外设才能成立的游戏，会按实际游玩价值取舍。每一款新增作品已经进入正文，不再保留“可能遗漏”“待补”或 TODO 占位。','',
'---','','## 容量汇总与性能建议','',
'### 按条目预算重算','']

def mb(size):
    try:
        if 'GB' in size.upper():return float(re.findall(r'[\d.]+',size)[0])*1024
        return float(re.findall(r'[\d.]+',size)[0])
    except:return 0
out += ['| 平台 | 条目数（合集行不拆开计数） | 表内预留空间 | 推荐位置 |','|---|---:|---:|---|']
total=0
for p in platform_heads:
    es=[e for e in entries if e.platform==p]
    val=sum(mb(e.size) for e in es);total+=val
    loc='eMMC' if p not in {'Dreamcast','PSP','PS1'} else 'SSD'
    out.append(f'| {p} | {len(es)} | {val/1024:.2f} GB | {loc} |')
out += [f'| **合计** | **{len(entries)}** | **{total/1024:.2f} GB** | 另留系统、BIOS、刮削与存档空间 |','',
'> 合计只是根据每行“预留空间”进行的算术汇总，不代表下载或 CHD 转换后的实测容量。合集行拆分、PCE／街机 CHD、PSP 多盘与额外 DLC 都会改变最终占用。','',
'### N4100 的保守设置','',
'| 平台 | 起始建议 | 验证重点 |','|---|---|---|','| NES／GB／MD／SNES／GBA | 默认核心与整数缩放，逐作开存档 | 特殊芯片、传感器、RTC 与地区刷新率 |','| NDS | melonDS 默认渲染，关闭不必要高倍率 | 双屏布局、触控、麦克风与存档类型 |','| PS1 | DuckStation 或兼容核心，先用原生分辨率 | 多盘切换、纹理抖动、重负载场景与记忆卡 |','| N64 | 原生或低倍率，按游戏选图形插件 | Expansion Pak、帧率、纹理与特定特效，不承诺全库稳定 |','| Dreamcast | Flycast 原生分辨率，必要时降低渲染 | NAOMI 与 DC 分开管理，检查透明排序和重负载场景 |','| PSP | PPSSPP 1×，关闭非必要后期效果 | 《战神》《和平行者》《零式》等逐段测帧，不以菜单帧率代替实战 |','| FBNeo／MAME | 2D 街机优先 FBNeo；其余按硬件和官方支持选核心 | ROM set 版本、BIOS、CHD、专用控制器；Model 2／3 与后期音游另测 |','',
'### 最终核对规则','',
'- 不在正文中保留“删除”“存疑”“不存在”“待核实”等伪条目；已确认错误的项目直接移除。','- 不再保留单独的“纠错清单”来掩盖正文错误；商品名、发行方、平台与版本关系已直接改正。','- 专题全部通过 `#nes-001` 这类稳定锚点回链平台表；平台总目录使用 `platform-*` 锚点，避免中文标题在不同 Markdown 渲染器中的锚点差异。','- 先备份合法镜像与存档，再做格式转换、ROM set 重建或目录迁移。']

(ROOT/'batocera_rom_guide.md').write_text('\n'.join(out)+'\n')
print(f'entries={len(entries)}, lines={len(out)}, bytes={(ROOT/"batocera_rom_guide.md").stat().st_size}')
for p in platform_heads:print(short[p],sum(1 for e in entries if e.platform==p))
