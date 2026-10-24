"""Run the explicitly requested recall and narrow peer coordination, bounded."""
from pathlib import Path
import subprocess
import os
import json
from datetime import datetime, timezone

ROOT = Path('~')
JOB = ROOT / 'brain_workers/w523'
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')

def run(args, timeout=60):
    try:
        result = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', timeout=timeout, env=env)
        return {'command': args, 'returncode': result.returncode, 'stdout': result.stdout[:16000], 'stderr': result.stderr[:2000]}
    except subprocess.TimeoutExpired as e:
        return {'command': args, 'timeout_seconds': timeout, 'stdout': str(e.stdout or '')[:16000]}

receipt = run(['python', '-X', 'utf8', str(ROOT / '.claude/dreaming/brain.py'), 'recall', 'P0297 Liouville quantum gravity exact Hausdorff dimension proof mistakes'], timeout=60)
(JOB / 'SCAR_RECALL.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False), encoding='utf-8')
print('RECALL', json.dumps(receipt, ensure_ascii=False))
memory = ROOT / '.claude/projects/<project>/memory'
names = run(['rg', '--files', str(memory), '-g', '*perceptron_proof_open_gaps_fleet_2026_07_12*', '-g', '*liouville*', '-g', '*lqg*'])
print('SCAR_FILENAMES', names['stdout'])
for p in memory.glob('perceptron_proof_open_gaps_fleet_2026_07_12*.md'):
    print('REQUIRED_SCAR', p.name, p.read_text(encoding='utf-8')[:8500])
comm = str(ROOT / '<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py')
read = run(['python', '-X', 'utf8', comm, 'read', '--as', 'w523', '--max', '8'])
print('TEAM_READ', json.dumps(read, ensure_ascii=False))
claim = 'P0297 w523 independently claims the critical-boundary and circularity audit of the thick-point ratio (2-alpha^2/2)/(xi*(Q-alpha)); primary sources read, paired proof not read. Artifact: ~/brain_workers/w523/INDEPENDENT.md. Please keep other lanes on LFPP crossing/metric arguments.'
receipts = [read]
for who in ['w522', 'w524']:
    sent = run(['python', '-X', 'utf8', comm, 'say', '--as', 'w523', '--to', who, '--kind', 'claim', claim])
    receipts.append(sent)
    print('CLAIM', who, json.dumps(sent, ensure_ascii=False))
(JOB / 'COORDINATION_RECEIPTS.json').write_text(json.dumps(receipts, indent=2, ensure_ascii=False), encoding='utf-8')
print('EXACT_INTAKE_RECORD')
path = ROOT / '<private-repo>/06_math_research/probability_1000_intake_F_20260908/raw/dedup_index.json'
data = json.loads(path.read_text(encoding='utf-8-sig'))
def find(obj, trail='$'):
    if isinstance(obj, dict):
        if 'P0297' in obj:
            print(trail + '.P0297', json.dumps(obj['P0297'], ensure_ascii=False)[:7000])
        if any(v == 'P0297' for v in obj.values() if isinstance(v, str)):
            print(trail, json.dumps(obj, ensure_ascii=False)[:7000])
        for k, v in obj.items():
            if isinstance(v, (list, dict)):
                find(v, trail + '.' + str(k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, (dict, list)):
                find(v, f'{trail}[{i}]')
find(data)
