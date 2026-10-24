import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
db = Path('~/.agents/coordination/agent_mesh.sqlite3')
conn=sqlite3.connect('file:'+db.as_posix()+'?mode=ro', uri=True, timeout=5)
rows=conn.execute("SELECT a.agent_id,c.name FROM agents a LEFT JOIN campaigns c ON c.campaign_id=a.campaign_id WHERE a.agent_id IN ('w455','w453','w454','w458','claude-4a88bc43')").fetchall()
conn.close()
receipt={'lookup':rows,'deliveries':[]}
team=next((r[1] for r in rows if r[0]=='w455' and r[1]), None)
if not team:
    team=next((r[1] for r in rows if r[0] in ('w453','w454','w458') and r[1]), None)
messages={
 'w453':('claim','C0041 w455 claims source/assumption audit and fixed-box-to-regeneration-range gap; no duplicate proof work requested. My boundary and proof packet: ~/brain_workers/w455/ATTEMPT.md. Send your exact lemma and artifact path for KEEP/FIX/DROP.'),
 'w454':('claim','C0041 w455 claims coordinate spatial regeneration mean identity via delayed renewal generating functions, plus localized time-tail audit. Packet ~/brain_workers/w455/ATTEMPT.md. Please identify your disjoint lemma and exact artifact path.'),
 'w458':('review','Please independently audit w455 L01 (coordinate E_Q Y=1/q) and L02 (quenched box-exit / conditional range bound) in ~/brain_workers/w455/ATTEMPT.md and CLAIMS.jsonl. Parent C0041 remains unsolved; judge each lemma narrowly.')
}
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
if team:
 for peer,(kind,body) in messages.items():
    cmd=[sys.executable,'-X','utf8','~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py','say','--as','w455','--team',team,'--to',peer,'--kind',kind,body]
    try:
        result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=20,env=env)
        receipt['deliveries'].append({'to':peer,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    except subprocess.TimeoutExpired:
        receipt['deliveries'].append({'to':peer,'timed_out':True})
else:
 receipt['delivery_status']='No existing named-peer campaign found; narrow requests saved locally; do not create a campaign or spawn workers.'
(root/'mesh_boundary_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(receipt,ensure_ascii=False))
