from pathlib import Path
import json,hashlib,datetime
import exact as E
from exact import F
r=Path(__file__).resolve().parents[1]
# Additional physical negative control, not just an arbitrary probability law.
g=(-1,1,1,1);R=(F(1,2),F(1,6),F(1,6),F(1,6))
p=E.spectrum(g)[0];child=E.child(g,0,0);q=E.spectrum(child)[0]
old=E.marginal(E.calibrate(R,p),0);raw=E.marginal(R,0);fresh=E.calibrate(raw,q)
assert p==F(1,4) and q==0
assert old!=fresh and E.calibrate(old,q)==fresh
control=dict(status='PASS',source_truth_table=g,physical_child=child,source_reference=list(map(str,R)),source_true_vacuum=str(p),child_true_vacuum=str(q),intermediate_calibrated_marginal=list(map(str,old)),final_calibrated_original_marginal=list(map(str,fresh)),conclusion='Omitting final calibration fails on an actual Boolean point-defect-to-dictator restriction; applying it gives exact equality.')
(r/'out/PHYSICAL_NEGATIVE_CONTROL.json').write_text(json.dumps(control,indent=2),encoding='utf-8')
# Do not confuse the stale first-setup output with the later blocked admission.
formal=json.loads((r/'out/FORMAL_RECEIPT.json').read_text(encoding='utf-8'))
assert formal['status']=='NOT_ATTEMPTED_MEMORY_ADMISSION' and formal['exit_code']==1
formal.update(prepared_source='code/Calibration.lean',prepared_source_sha256=hashlib.sha256((r/'code/Calibration.lean').read_bytes()).hexdigest(),previous_setup_output='out/LEAN.txt',compiler_launched_on_latest_attempt=False)
(r/'out/FORMAL_RECEIPT.json').write_text(json.dumps(formal,indent=2),encoding='utf-8')
p=r/'REPORT.md';s=p.read_text(encoding='utf-8')
s=s.replace('The first formal setup was rejected before any compiler launch because the --stmt receipt omitted generated imports/newlines. The byte-exact --file correction and fresh memory admission are preserved; its narrow real-algebra target returns SETUP_UNVERIFIED. No full theorem is claimed Lean-checked.','The first formal setup was rejected before compiler launch because the --stmt receipt omitted generated imports/newlines. A byte-exact --file correction is prepared, but fresh memok returns1 and blocks submission. out/LEAN.txt records the FIRST rejection; out/FORMAL_RECEIPT.json records the LATEST memory hold. No compiler is launched on the retry and no Lean certificate is claimed.')
s=s.replace('Ommiting final calibration','Omitting final calibration')
s=s.replace('Omitting final calibration is an executed negative control and fails equality.','Omitting final calibration is an executed negative control and fails equality. The supplementary out/PHYSICAL_NEGATIVE_CONTROL.json repeats this control on an actual two-bit point-defect-to-dictator restriction.')
p.write_text(s,encoding='utf-8')
with (r.parents[1]/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+datetime.datetime.now(datetime.timezone.utc).isoformat()+': Final formal receipt reconciliation: initial hash setup rejection launched no compiler; fresh retry blocked by memok exit1 BEFORE submission. Old LEAN.txt is not latest admission state. Prepared byte-exact Lean source retained; no formal certificate. Added actual Boolean point-defect/dictator omission control, exact PASS.\n')
progress=json.loads((r/'PROGRESS.json').read_text(encoding='utf-8'))
progress['source_artifacts']+=['out/PHYSICAL_NEGATIVE_CONTROL.json','code/Calibration.lean']
progress['blockers'].append('Narrow formal check not verified: first setup rejected, fresh retry held by memory admission; analytic proof has no Lean certificate.')
for name in ('PROGRESS.json','PACKET_DELTA.json'):(r/name).write_text(json.dumps(progress,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
rows=[]
for p in r.rglob('*'):
 if p.is_file() and p.name!='RECEIPTS.json':
  b=p.read_bytes();assert len(b)<20000000;rows.append(dict(path=str(p.relative_to(r)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
(r/'out/RECEIPTS.json').write_text(json.dumps(dict(files=rows,remote_mirror_verified=False),indent=2),encoding='utf-8')
for row in rows:assert hashlib.sha256((r/row['path']).read_bytes()).hexdigest()==row['sha256']
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
print('FINAL READBACK PASS:',len(rows),'files; physical omission control PASS; formal retry NOT_STARTED_MEMORY_HOLD; local artifacts complete; full FEI OPEN.')
