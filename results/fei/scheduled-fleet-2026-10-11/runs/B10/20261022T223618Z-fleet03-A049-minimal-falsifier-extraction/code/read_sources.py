from pathlib import Path
import hashlib,json,re
run=Path(__file__).resolve().parents[1]
out=run/'out';out.mkdir(exist_ok=True)
base=Path('~/mop_fei100')
report=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
paths=[report/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.txt'))+list((supp/'sources').glob('*.md'))
paths += list(Path('~/brain_workers/FEI100_20261011/context').glob('*.txt'))
receipts=[]
for p in paths:
 if not p.exists():
  receipts.append({'path':str(p),'missing':True});continue
 b=p.read_bytes()
 try:s=b.decode('utf-8-sig');encoding='utf-8-sig'
 except UnicodeDecodeError:s=b.decode('cp1252');encoding='cp1252'
 lines=s.splitlines()
 hits=[{'line':i+1,'text':line[:500]} for i,line in enumerate(lines) if re.search(r'A049|C018|C019|C024|occupancy|shared.data|composition|singular',line,re.I)]
 receipts.append({'path':str(p),'encoding':encoding,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(lines),'relevant_lines':hits[:25]})
(out/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
for r in receipts:
 print(r['path'],r.get('lines','MISSING'))
 for h in r.get('relevant_lines',[])[:2]:print(h)
