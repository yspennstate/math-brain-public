from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]; O=R/'out';O.mkdir(exist_ok=True)
base=Path(r'~\mop_fei100'); camp=base/'reports/fei-2026-10-11'
adv=base/'research_pushes/2026-10-11-full-fei-100-agents'
ctx=Path(r'context')
files=[camp/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [adv/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [p for p in (adv/'sources').iterdir() if p.suffix in ['.txt','.md','.tex']]+list(ctx.glob('*.txt'))
files += list((camp/'runs').rglob('REPORT.md'))
files += [p for p in Path(r'~\.claude\compute').glob('*intervention*') if p.is_file()]
records=[];extracts=[]
for p in files:
 if not p.exists():records.append({'path':str(p),'missing':True});continue
 b=p.read_bytes()
 try:s=b.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:s=b.decode('cp1252');enc='cp1252'
 records.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'encoding':enc})
 lines=s.splitlines(); hits=[(i+1,line[:350]) for i,line in enumerate(lines) if re.search(r'A047|C019|C024|source|spike|Theorem|composition',line,re.I)]
 extracts.append({'path':str(p),'locators':hits[:10]})
(O/'INTAKE.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
(O/'INTAKE_EXTRACTS.json').write_text(json.dumps(extracts,indent=2),encoding='utf-8')
print(json.dumps({'files':len(records),'bytes':sum(x.get('bytes',0) for x in records),'missing':[x['path'] for x in records if x.get('missing')]}))
for x in extracts:
 if 'CURRENT_STATUS' in x['path'] or 'STREAM_NEXT' in x['path'] or '38pp.txt' in x['path'] or '30pp.txt' in x['path']:print(json.dumps(x))
