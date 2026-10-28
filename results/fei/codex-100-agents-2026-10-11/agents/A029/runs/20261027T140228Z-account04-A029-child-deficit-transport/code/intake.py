from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]; agents=r.parents[2]; project=agents.parent
paths=[project/'BOARD.md',project/'claude/B06/STREAM_NOTES.md',agents/'A029/STATUS.md',Path(r'~\AGENTS.md'),Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')]
for a,d in [('A028','20261027T103152Z-account04-A028-stopping-tree-payment'),('A012','20261027T062634Z-account04-A012-sparse-activation-accounting'),('A096','20261027T055827Z-account04-A096-live-gap-ledger'),('A097','20261027T092641Z-account04-A097-cross-route-transfer'),('A029','20261026T213208Z-account04-A029-child-deficit-transport')]:
 p=agents/a/'runs'/d
 for n in ['REPORT.md','DERIVATION.md','PROOF.md','CLAIMS.json']:
  if (p/n).exists():paths.append(p/n)
receipts=[]
for p in paths:
 b=p.read_bytes();s=b.decode('utf-8');receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
prev=agents/'A029/runs/20261026T213208Z-account04-A029-child-deficit-transport/out/SOURCE_RECEIPTS.json'
baseline=json.loads(prev.read_text(encoding='utf-8')); baseline_checks=[]
for o in baseline:
 p=Path(o['path'])
 if p.name in ['BOARD.md','STREAM_NOTES.md','AGENTS.md','DERIVATION.md']:continue
 baseline_checks.append({'path':str(p),'same_bytes_as_prior_intake':hashlib.sha256(p.read_bytes()).hexdigest()==o['sha256']})
(r/'out/SOURCE_RECEIPTS.json').write_text(json.dumps({'current_sources':receipts,'inherited_baseline_receipt':str(prev),'baseline_checks':baseline_checks},indent=2),encoding='utf-8')
state=Path(r'~\.claude\compute\compute_state.json');o=json.loads(state.read_text(encoding='utf-8'));keep={k:o.get(k) for k in ['ts','status','mode','mem_avail_mb','commit_avail_mb','disk_free_gb','reasons']}
(r/'out/COMPUTE_SNAPSHOT.json').write_text(json.dumps(keep,indent=2),encoding='utf-8')
print(json.dumps({'current_sources':len(receipts),'baseline_files_checked':len(baseline_checks),'baseline_unchanged':sum(x['same_bytes_as_prior_intake'] for x in baseline_checks),'compute':keep}))
