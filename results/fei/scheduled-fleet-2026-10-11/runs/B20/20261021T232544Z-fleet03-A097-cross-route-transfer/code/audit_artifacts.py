from pathlib import Path
import hashlib,json
RUN=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
p=RUN/'REPORT.md';s=p.read_text(encoding='utf-8')
s=s.replace('The first unpaid line is a repeated/interleaved non-active reset from the now diminished original reserve, or replacing the point source by a generic signed non-point profile.','After the mixed-order strengthening below, the first unpaid line is a dummy-data reset or canonical reset in a retained off-branch from the diminished original reserve, or replacing the point source by a generic signed non-point profile.')
s=s.replace('No shared campaign tree, other agent folder, git state, external system, or brain record is modified.','No shared campaign tree, other agent folder, git state, external system or research brain record is edited; mandatory wake/checklist bookkeeping and recall-tool-managed index activity are separate from the research output.')
p.write_text(s,encoding='utf-8')
(RUN/'out/CHECKPOINT.md').write_text('STATE: stage17 complete locally; A097-MIXED-ACTIVE-CONTROL-RESET-SAME-ANCESTOR@1 saved with analytic proof and15538 exact assertions; full FEI OPEN, new independent review pending.\nNEXT: A096/A094/A086 review; pay dummy-data or off-branch canonical reset using SAME diminished original bank, all old debits and full terminal references retained. No git commit or remote adoption claimed.\n',encoding='utf-8')
protocol=read(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))['required_per_run']
progress=read(RUN/'PROGRESS.json');claims=read(RUN/'CLAIMS.json')
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert all(set(c)==set(protocol['claim_fields']) for c in claims)
assert progress==read(RUN/'PACKET_DELTA.json')
assert claims[1]['statement_sha256']==hashlib.sha256(claims[1]['exact_statement'].encode()).hexdigest()
assert read(RUN/'out/VALIDATION.json')['checks']+read(RUN/'out/MIXED_VALIDATION.json')['checks']==15538
assert s.rstrip().split('\n\n')[-2]=='## Universal bridge'
receipt=read(RUN/'out/PERSISTENCE_RECEIPTS.json');receipt['files']=[]
for f in RUN.rglob('*'):
 if f.is_file() and f.name!='PERSISTENCE_RECEIPTS.json':
  data=f.read_bytes();assert len(data)<20_000_000
  receipt['files'].append({'path':str(f.relative_to(RUN)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(RUN/'out/PERSISTENCE_RECEIPTS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'artifact_audit':'PASS','files':len(receipt['files']),'exact_checks':15538,'full_FEI':'OPEN','new_independent_review':'PENDING','Lean':'NOT_LAUNCHED_MEMORY_GATE'}))
