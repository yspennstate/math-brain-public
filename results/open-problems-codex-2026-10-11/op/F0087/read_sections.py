from pathlib import Path
for fn,ranges in [('dubedat.txt',[(6330,6370),(6110,6330),(700,820),(1470,1565),(3560,3640)]),('kenyon.txt',[(130,270)])]:
 l=Path(fn).read_text(encoding='utf8').splitlines();print('FILE',fn)
 for a,b in ranges:
  for i in range(a-1,min(b,len(l))):print(f'{i+1}: {l[i]}')
