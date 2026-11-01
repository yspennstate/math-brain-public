"""Carry the supervisor's explicit C1 routing instruction to the named integrator."""
import json
import subprocess
import sys
from pathlib import Path

root=Path(__file__).resolve().parent
body=('Claude-4a88bc43 instructed forwarding C1 for a different-model referee KEEP before builder claude-51330238. '
 'Packet ~/brain_workers/w381/REVIEW_PACKET.md; source/page quote PRIMARY_SOURCES.md, Annals Th1.1 PDF3-4 (665-666). '
 'The original theorem lists no separate uniform-curvature hypothesis; matching chi_a=chi_b and xi_a=xi_b remains. '
 'Existing card claim_e090760039c41cb781c56fbb85679625a58a678ff42cfb3ec11a01d8887de6c5. Source clarification only; no KEEP claimed and live node untouched.')
cmd=[sys.executable,'-B','-X','utf8',r'~\<private-repo>\12_cognitive_architecture\agent_mesh\agent_mesh.py','send','--agent','w381','--to','codex-01a12190','--topic','P0110-C1-integrator-review','--kind','message','--body',body,'--idempotency-key','w381-P0110-C1-integrator-20261010-v1']
run=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=60)
receipt={'to':'codex-01a12190','authority':'Supervisor claude-4a88bc43 direct feedback 05:36, same task','returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr}
(root/'source_integrator_handoff.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
raise SystemExit(run.returncode)
