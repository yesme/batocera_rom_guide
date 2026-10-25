from pathlib import Path
import re, importlib.util
ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('rg',ROOT/'rebuild_guide.py'); rg=importlib.util.module_from_spec(spec); spec.loader.exec_module(rg)
files={
'NES / FC':['Nintendo - Nintendo Entertainment System','Nintendo - Family Computer Disk System'],
'GB / GBC':['Nintendo - Game Boy','Nintendo - Game Boy Color'],
'MD / Genesis':['Sega - Mega Drive - Genesis'],
'SNES / SFC':['Nintendo - Super Nintendo Entertainment System'],
'N64':['Nintendo - Nintendo 64'],
'PCE (PC Engine / TurboGrafx-16)':['NEC - PC Engine - TurboGrafx 16'],
'GBA':['Nintendo - Game Boy Advance'],
'NDS':['Nintendo - Nintendo DS'],
'GG':['Sega - Game Gear'],
'WS / WSC':['Bandai - WonderSwan','Bandai - WonderSwan Color'],
'PSP':['Sony - PlayStation Portable'],
'街机（FBNeo / MAME）':['MAME'],
}
def norm(s):
 s=re.sub(r'\s*\([^)]*\)','',s)
 s=s.split(' / ')[0]
 s=s.replace('&','and').replace('’',"'").replace('–','-')
 return re.sub(r'[^a-z0-9]+','',s.lower())
idx={}
for p,fs in files.items():
 d={}
 for f in fs:
  fp=ROOT/'libretro-database/metadat/releaseyear'/f'{f}.dat'
  if not fp.exists():continue
  for n,y in re.findall(r'comment "([^"]+)"\s+releaseyear "(\d{4})"',fp.read_text(errors='ignore')):
   d.setdefault(norm(n),set()).add(y)
 idx[p]=d
miss=[]
for e in rg.entries:
 if e.year:continue
 y=idx.get(e.platform,{}).get(norm(e.en))
 if y:e.year=sorted(y)[0]
 else:miss.append(e)
print('matched',len(rg.entries)-len(miss),'missing',len(miss))
for e in miss:print(e.platform,'|',e.old,'|',e.en)
