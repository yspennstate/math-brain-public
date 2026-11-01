from pathlib import Path
import time,runpy,json,hashlib
root=Path(__file__).parent
deadline=time.monotonic()+420
while time.monotonic()<deadline:
 log=(root/'lean_check.log').read_text(encoding='utf-8')
 if 'exit_code=' in log or 'Timeout after 3600' in log:
  if not (root/'STATUS.md').read_text(encoding='utf-8').startswith('STATE: DONE'):
   runpy.run_path(str(root/'finalize_results.py'),run_name='__main__')
  manifest=json.loads((root/'final_manifest.json').read_text(encoding='utf-8'))
  for name,digest in manifest['sha256'].items():
   assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest
  for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines():
   r=json.loads(line)
   assert set(['problem_id','claim','status','proof_location','remaining_gap','checks'])<=set(r)
   assert r['problem_id']=='P0170'
  print('Final artifact hashes and all claim schemas checked. STATE: DONE; VERDICT: PARTIAL.',flush=True)
  break
 time.sleep(5)
else:
 print('Existing Lean result still pending after bounded 420-second monitor; no second Lean run started.',flush=True)
