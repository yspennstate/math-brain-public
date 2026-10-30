from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
HOME=R.parents[1]; TEAM=HOME.parents[1]
def sha(b): return hashlib.sha256(b).hexdigest()
def save(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
canonical=Path('math-open-problems/reports/fei-2026-10-11')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
files=[canonical/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
files+=list(canonical.glob('*.tex'))
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [p for p in (supp/'sources').rglob('*') if p.is_file() and p.suffix in ['.md','.json','.txt','.tex']]
files += list((TEAM/'context').glob('*.txt'))
files += [TEAM/'BOARD.md',TEAM/'claude/B17/STREAM_NOTES.md',HOME/'STATUS.md',HOME/'LEARNED.md',HOME/'WORKLOG.md']
files += [Path('~/brain_workers/PRIMARY_DIRECTIVE.md'),Path('~/<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md')]
pins=[]
for p in files:
 if not p.exists(): pins.append({'source':str(p),'missing':True});continue
 b=p.read_bytes();encoding='utf-8-sig'
 try:s=b.decode(encoding)
 except UnicodeDecodeError:encoding='cp1252';s=b.decode(encoding)
 dest=R/'out/intake'/f'{len(pins):03}_{p.name}'
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
 if p.suffix=='.json':json.loads(s)
 pins.append({'source':str(p),'snapshot':str(dest.relative_to(R)),'sha256':sha(b),'bytes':len(b),'encoding':encoding,'access':'complete machine intake; not a fresh proof audit'})
save(R/'out/INTAKE_PINS.json',pins)
save(R/'out/FROZEN_SPEC.json',{'helper':'A081 query-ledger-audit v1','family':'A094 actual one-edit dictator witness; exact root-bank coefficient algebra; dependency graph mutation fixtures','domain':{'b':'12..64 corroboration; all b>=12 by explicit factorization','graph':'prior A081 exact graph plus new scoped versions'},'case_count':53,'symmetry':'none','arithmetic':'integers and fractions; signs by exact polynomial factorization; no floating logs','memory_estimate_mb':70,'maximum_runtime_seconds':55,'automatic_escalation':False,'heavy_compute':False,'code_version':'source SHA256 recorded after code freeze'})
print(json.dumps({'intake_files':len(pins),'missing':[p['source'] for p in pins if p.get('missing')],'snapshots':'out/intake','frozen_spec':'out/FROZEN_SPEC.json'}))
