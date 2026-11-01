"""Send the authorized narrow lemma-boundary notice, without starting agents."""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
helper = '~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
body = ('w414 narrow C0017 lane is saved and submitted: boundary chamber domains with closure+boundary Hausdorff, area and unmarked kernel convergence, fixed Euclidean corner marks, series corridor crossing <=2^-k and conformal marked-preimage separation <=8/n. Please keep other triad computations disjoint from these series-cut and prime-end-collapse lemmas. Packet ~/brain_workers/w414/REVIEW_PACKET.md; resource clm-f4591e77ed; referee w416. Author auxiliary proofs only; parent not solved and novelty UNKNOWN.')
for peer in ('w408', 'w411', 'w417'):
    command = [sys.executable, '-X', 'utf8', helper, 'send', '--agent', 'w414',
               '--to', peer, '--topic', 'C0017-lemma-boundaries', '--kind', 'message', '--body', body]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError:
        output = result.stdout[:2000]
    receipt = {'recorded_at': datetime.now(timezone.utc).isoformat(), 'to': peer,
               'exit_code': result.returncode, 'result': output, 'stderr': result.stderr[:1000]}
    with (ROOT / 'LANE_NOTIFICATIONS.jsonl').open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(receipt) + '\n')
    print(json.dumps(receipt), flush=True)
