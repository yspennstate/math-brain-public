"""One held-task replay, not a general performance benchmark."""
import json
import subprocess
import sys
import time
from pathlib import Path
import p0110_math_route as pilot

root=Path(__file__).resolve().parent
assert pilot.recognizes('P0110 missing bridge')
assert pilot.recognizes('p0110')
assert not pilot.recognizes('P01100')
assert not pilot.recognizes('P0117')
assert pilot.route('P0117')['supported'] is False
assert pilot.route('P0117')['cards']==[]
baseline=json.loads((root/'recall_receipt.json').read_text(encoding='utf-8'))
query=baseline['query']
command=[sys.executable,'-B','-X','utf8',str(root/'p0110_math_route.py'),query,'--output',str(root/'route_output.json')]
started=time.perf_counter()
run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=60)
elapsed=time.perf_counter()-started
(root/'route_stdout.txt').write_text(run.stdout,encoding='utf-8')
assert run.returncode==0,run.stderr
out=json.loads((root/'route_output.json').read_text(encoding='utf-8'))
assert out['read_only'] and out['current_openness']=='UNKNOWN'
assert out['cards'][0]['id']==pilot.TARGET
assert all('assumptions' in c['claim'] for c in out['cards'])
assert all(c['claim']['status']=='unverified' for c in out['cards'])
default_run=subprocess.run(command[:6],capture_output=True,text=True,encoding='utf-8',timeout=60)
assert default_run.returncode==0,default_run.stderr
default_out=json.loads(default_run.stdout)
assert default_out['cards'][2]['claim']['assumptions']==out['cards'][2]['claim']['assumptions']
receipt={'command':command,'gate_id':'w381-local-lemmas-20261010-01','baseline_command':baseline['command'],
 'baseline_exact_target_hits':0,'baseline_displayed_memory_hits':3,'baseline_elapsed_seconds':baseline['elapsed_seconds'],
 'pilot_exact_target_hits':1,'pilot_returned_cards':len(out['cards']),'pilot_route_seconds':out['elapsed_seconds'],
 'pilot_subprocess_seconds':elapsed,'identifier_boundary_checks':4,'unsupported_route_checks':2,
 'retained_complete_hypothesis_cards':True,'default_cli_complete_hypotheses':True,'retained_unverified_statuses':True,'live_default_changed':False,
 'limitations':'One known target, different retrieval substrates, one loaded-machine observation. No claim of a broad recall improvement or controlled speedup.'}
(root/'route_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
