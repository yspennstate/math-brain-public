from pathlib import Path
l=Path('dubedat_dimertors_arx.tex').read_text(encoding='utf8').splitlines()
for i,s in enumerate(l):
 if 'For weights' in s or 'partially answering' in s or 'If $s' in s and 'constant' in s:
  print('\n'.join(f'{j+1}: {l[j]}' for j in range(max(0,i-3),min(len(l),i+22))))
