from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
base=R.parents[3]
for agent in ['A003','A079','A085','A090','A094','A095','A096','A097','A099']:
 runs=sorted((base/'agents'/agent/'runs').glob('*'),reverse=True)
 if runs:
  p=runs[0]/'REPORT.md'
  print(agent,runs[0].name)
  if agent in ['A096','A097','A003'] and p.exists():
   text=p.read_text(encoding='utf-8-sig');print(text[:1900])
