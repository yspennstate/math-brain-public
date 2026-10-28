from pathlib import Path
import json,hashlib
base=Path('~')
run=Path(__file__).resolve().parents[1]
files=[]
report=base/'mop_fei100/reports/fei-2026-10-11'
for name in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','FEI_100_agent_research_plan.tex']:
 files.append(report/name)
supp=base/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
 files.append(supp/name)
files+=list((supp/'sources').glob('*'))
files+=list((base/'brain_workers/FEI100_20261011/context').glob('*.txt'))
receipts=[]
(run/'out').mkdir(exist_ok=True)
for p in files:
 if not p.is_file():
  print('MISSING',p);continue
 data=p.read_bytes();rec={'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 receipts.append(rec)
 if p.suffix in ['.txt','.tex','.md','.json']:
  try:s=data.decode('utf-8-sig');rec['encoding']='utf-8-sig'
  except UnicodeDecodeError:s=data.decode('cp1252');rec['encoding']='cp1252 (UTF-8 rejected; legacy source encoding)'
  lines=s.splitlines()
  hits=[i for i,l in enumerate(lines) if any(k in l.lower() for k in ['a024','fei+','composition','restriction','odd-face','c019','c024','biased'])]
  selected=set()
  for i in hits[:8]:selected.update(range(max(0,i-1),min(len(lines),i+3)))
  print('\nSOURCE',p,'lines',len(lines))
  for i in sorted(selected):print(f'{i+1}: {lines[i]}')
(run/'out').mkdir(exist_ok=True)
(run/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
