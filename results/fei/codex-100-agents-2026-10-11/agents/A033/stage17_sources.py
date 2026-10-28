from pathlib import Path
import re
r=Path(r'~\brain_workers\FEI100_20261011')
for a in ['A079','A032','A034']:
 ds=sorted((r/'agents'/a/'runs').iterdir())
 print(a,'recent', [d.name for d in ds[-4:]])
 good=[d for d in ds if (d/'REPORT.md').exists()]
 d=good[-1]; print('LATEST',d)
 for n in ['REPORT.md','DERIVATION.md','PROOF.md']:
  p=d/n
  if p.exists(): print(n,p.read_text(encoding='utf-8')[:26000])
base=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents\sources')
for name in ['ROUTE_MAP_CURATED.md','ERASURE_RIGIDITY.md','ONE_BIT_ENDPOINT.md']:
 p=base/name; s=p.read_text(encoding='utf-8'); ls=s.splitlines()
 print('\nSOURCE',name)
 if name=='ROUTE_MAP_CURATED.md': print(s[:23000])
 else:
  hits=[i for i,l in enumerate(ls) if re.search('product|dyadic|prefix|cyclic',l,re.I)]
  keep=set(j for i in hits[:8] for j in range(max(0,i-2),min(len(ls),i+7)))
  print('\n'.join(f'{i+1}: {ls[i]}' for i in sorted(keep)))
print('LEAN CHECKER OPTIONS')
s=Path(r'lean_check.py').read_text(encoding='utf-8')
print('\n'.join(l for l in s.splitlines() if any(t in l for t in ['add_argument','tempfile','write_text','mkdir','subprocess'])))
