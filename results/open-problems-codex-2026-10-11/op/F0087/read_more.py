from pathlib import Path
l=Path('dubedat.txt').read_text(encoding='utf8').splitlines()
for a,b in [(6030,6115),(6370,6410),(3700,3790),(940,958)]:
 for i in range(a-1,b):print(f'{i+1}: {l[i]}')
l=Path('kenyon.txt').read_text(encoding='utf8').splitlines()
for i,s in enumerate(l):
 if '2.2'==s or 'ﬂow' in s or 'flow' in s:
  if i<650:
   for j in range(max(0,i-3),min(len(l),i+25)):print(f'{j+1}: {l[j]}')
