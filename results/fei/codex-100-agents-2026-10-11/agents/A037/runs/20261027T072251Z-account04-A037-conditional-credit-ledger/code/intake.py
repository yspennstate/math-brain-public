from pathlib import Path
import json, hashlib, re
root=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100')
report=base/'reports/fei-2026-10-11'
sup=base/'research_pushes/2026-10-11-full-fei-100-agents'
files=[report/x for x in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [sup/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md']]
files += list((sup/'sources').glob('*.txt'))
files += list(Path('context').glob('*.txt'))
out=[]
for p in files:
 if not p.exists():
  out.append({'path':str(p),'missing':True});continue
 raw=p.read_bytes()
 try:s=raw.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:s=raw.decode('cp1252');enc='cp1252 (explicit fallback; source bytes unchanged)'
 lines=s.splitlines()
 hits=[(i+1,x[:240]) for i,x in enumerate(lines) if re.search(r'A037|B08|C024|C019|posterior|chain rule|shared.data|8\.6|singular',x,re.I)]
 out.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':enc,'bytes':len(raw),'lines':len(lines),'locators':hits[:14]})
(root/'out').mkdir(exist_ok=True)
(root/'out/INTAKE.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for d in out:
 print(d['path'],d.get('lines','MISSING'))
 for h in d.get('locators',[])[:5]: print(h)
