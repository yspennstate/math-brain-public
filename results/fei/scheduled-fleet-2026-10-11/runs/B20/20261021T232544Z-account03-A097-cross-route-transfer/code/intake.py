from pathlib import Path
import hashlib,json
RUN=Path(__file__).resolve().parents[1]
base=Path('~/brain_workers/FEI100_20261011')
camp=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
paths=[camp/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md'))+list((base/'context').glob('*.txt'))
paths += [base/'BOARD.md',base/'claude/B20/STREAM_NOTES.md']
paths += [base/'agents/A097/runs/20261014T050248Z-account05-A097-cross-route-transfer'/x for x in ['DERIVATION.md','CLAIMS.json','REPORT.md']]
paths += [base/'agents/A096/runs/20261021T210221Z-account03-A096-live-gap-ledger'/x for x in ['DERIVATION.md','CLAIMS.json','REPORT.md','code/check.py']]
rows=[];extract=[]
for p in paths:
 if not p.exists():rows.append({'path':str(p),'status':'MISSING'});continue
 data=p.read_bytes();txt=data.decode('utf-8',errors='replace')
 rows.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'decoding':'utf-8 with explicit replacement for legacy paper export errors','lines':len(txt.splitlines())})
 if p.suffix=='.json':
  try:json.loads(txt)
  except Exception:pass
 lines=txt.splitlines();hits=[i for i,x in enumerate(lines) if any(k in x.lower() for k in ['a097','c024','c019','normaliz','activation','shared-data','first unsupported'])]
 extract.append('\nSOURCE '+str(p)+'\n'+'\n'.join(f'{i+1}: '+lines[i][:600] for i in hits[:18]))
(RUN/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
(RUN/'out/INTAKE_EXTRACTS.txt').write_text('\n'.join(extract),encoding='utf-8')
print(json.dumps({'sources_read':len(rows),'missing':[x['path'] for x in rows if x.get('status')=='MISSING']}))
