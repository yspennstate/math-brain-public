"""Final text audit and persistence readback; no mathematical reruns."""
from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1];OWN=RUN.parents[1]
old='Every sign conclusion uses separated intervals or exact law equality; no numerical tolerance establishes a sign.'
new='Positive-energy signs use separated rigorous intervals; zero-energy cases use the analytic nonpositive-calibration proof, exact zero-mixture law equality and interval identity corroboration. No interval overlapping zero is itself claimed as a certified sign.'
for p in [RUN/'REPORT.md',RUN/'code/finalize.py']:
 t=p.read_text(encoding='utf-8');assert old in t;t=t.replace(old,new);p.write_text(t,encoding='utf-8')
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=(RUN/'DERIVATION.md').read_text(encoding='utf-8');report=(RUN/'REPORT.md').read_text(encoding='utf-8')
claims=read(RUN/'CLAIMS.json');progress=read(RUN/'PROGRESS.json')
protocol=read(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
for c in claims:
 assert set(c)==set(protocol['required_per_run']['claim_fields'])
 assert hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256']
assert claims[0]['statement_sha256'] in proof
assert read(RUN/'PACKET_DELTA.json')==progress
assert report.rstrip().split('\n\n')[-1].startswith('Universal bridge:')
for name in protocol['required_per_run']['report_fields']:assert '# '+name in report
spec=read(RUN/'out/FROZEN_SPEC.json');validation=read(RUN/'out/VALIDATION.json')
assert spec['helper_sha256']==validation['helper_sha256']==sha(RUN/'code/check.py')
aspec=read(RUN/'out/AUDIT_FROZEN_SPEC.json');assert aspec['helper_sha256']==sha(RUN/'code/audit.py')
# Keep NEXT synchronized in the same closing step as the checklist closure.
status=(OWN/'STATUS.md').read_text(encoding='utf-8').splitlines();assert len(status)==2
status[1]='NEXT: A096/A079/A085/A094 review; pay ONE necessary ISOSPECTRAL zero-energy profile conversion from SAME actual unused source/occupancy account, retaining all old debits and BOTH full terminals.'
(OWN/'STATUS.md').write_text('\n'.join(status)+'\n',encoding='utf-8')
paths=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
assert all(p.stat().st_size<20_000_000 for p in paths)
receipt={'status':'SCHEMA_HASH_READBACK_PASS','artifacts':[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths],'rolling':[{'file':p,'sha256':sha(OWN/p)} for p in ['STATUS.md','WORKLOG.md','LEARNED.md']],'remote_mirror':'UNVERIFIED','new_independent_review':'PENDING','final_text_audit':'PASS; zero-energy sign scope explicit','full_FEI':'OPEN'}
(RUN/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for item in read(RUN/'out/PERSISTENCE.json')['artifacts']:assert sha(RUN/item['path'])==item['sha256']
print(json.dumps({'status':'FINAL_READBACK_PASS','artifacts':len(paths),'main_exact_assertions':validation['exact_assertions'],'independent_exact_assertions':read(RUN/'out/INDEPENDENT_AUDIT.json')['exact_assertions'],'new_review':'PENDING','full_FEI':'OPEN','next':status[1]}))
