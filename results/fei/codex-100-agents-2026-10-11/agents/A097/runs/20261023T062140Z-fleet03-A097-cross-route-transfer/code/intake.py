from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1];BASE=RUN.parents[3]
camp=Path('math-open-problems/reports/fei-2026-10-11');supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
paths=[camp/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+list((supp/'sources').glob('*.md'))+list((BASE/'context').glob('*.txt'))
paths += [BASE/'BOARD.md',BASE/'claude/B20/STREAM_NOTES.md',BASE/'agents/A097/STATUS.md',BASE/'agents/A097/LEARNED.md']
for who,rid in [('A096','20261023T053800Z-fleet03-A096-live-gap-ledger'),('A079','20261023T034945Z-fleet03-A079-correlated-auxiliaries'),('A050','20261023T042019Z-fleet03-A050-repair-with-scope'),('A098','20261023T024000Z-fleet03-A098-resource-reallocation')]:
 p=BASE/'agents'/who/'runs'/rid
 if not p.exists():continue
 paths += [q for q in p.iterdir() if q.name in ['REPORT.md','CLAIMS.json','PROOF.md','DERIVATION.md']]
records=[]
for p in paths:
 if not p.is_file():records.append({'path':str(p),'status':'MISSING'});continue
 data=p.read_bytes()
 try:txt=data.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:txt=data.decode('cp1252');enc='cp1252 legacy text'
 records.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'encoding':enc,'lines':len(txt.splitlines())})
(RUN/'out/SOURCES.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
spec={'helper_version':'A097-sign-partition-phase-v1','helper_sha256':hashlib.sha256((RUN/'code/check.py').read_bytes()).hexdigest(),'family':'all labeled Boolean seeds on fixed 2-bit pilot /3-bit main; fixed displayed A079 controller; both signs; normalized increasing tail source; explicit balanced phase/parity controls','domain':'pilot16 tables*2 queries*2 signs=64; main256*3*2=1536; six additional sequential transactions from explicit witness plus witness/parity checks','case_count':{'pilot_transactions':64,'main_transactions':1536,'explicit_sequential':6},'symmetry':'none','arithmetic':'Fraction full atoms; direct integer character sums; outward128-bit log enclosures using20 atanh terms and explicit geometric error; no floating signs','memory_estimate_MB':100,'max_runtime_seconds':55,'dimension_escalation':False,'scope':'finite validation supports analytic arbitrary-Boolean proof; not FEI certificate'}
(RUN/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
(RUN/'out/CHECKPOINT.md').write_text('A097 stage19: two-bin signed nonempty phase extension derived; x=Gamma*d^2+E*(cplus^2+cminus^2). Exact validation pending. NEXT: run fixed pilot then main; independently audit full CE ledger and parity nullspace.\n',encoding='utf-8')
print(json.dumps({'sources':len(records),'missing':[r['path'] for r in records if r.get('status')=='MISSING'],'frozen':True}))
