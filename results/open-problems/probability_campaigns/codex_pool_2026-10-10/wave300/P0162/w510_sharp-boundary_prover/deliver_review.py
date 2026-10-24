"""Use an existing team to deliver a named-peer review through supported routing."""
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys

root=Path(__file__).resolve().parent
db="~/.agents/coordination/agent_mesh.sqlite3"
body="Complete w510 proof packet: ~/brain_workers/w510/REVIEW_PACKET.md. C001-C004 prove sharp affine constant 4 and reject two stronger bridges; full FEI unproved. Initial 182 exact checks passed; corrected commit gate denied repeat. Please audit independently; delivery and experimental PASS are not mathematical keeps."
receipt={"to":"w512","body":body,"initial_direct_delivery":"failed: recipient unregistered","state":"prepared, not delivered"}
try:
    conn=sqlite3.connect("file:"+db+"?mode=ro",uri=True,timeout=2)
    rows=conn.execute("SELECT DISTINCT c.name FROM campaigns c JOIN agents a ON a.campaign_id=c.campaign_id WHERE c.status='active' AND a.agent_id IN (?,?,?,?) LIMIT 4",("w510","w511","w512","w330")).fetchall()
    conn.close()
    receipt["existing_teams"]=teams=[row[0] for row in rows]
    if teams:
        cmd=[sys.executable,"-X","utf8","~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py","say","--as","w510","--team",teams[0],"--to","w512","--kind","review",body]
        completed=subprocess.run(cmd,capture_output=True,text=True,encoding="utf-8",errors="replace",env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1"))
        receipt.update(exit_code=completed.returncode,stdout=completed.stdout,stderr=completed.stderr,state="delivered via supported named-peer routing" if completed.returncode==0 else "prepared, routing failed")
    else:
        # team_comm already implements re-registration of a parked, existing worker
        # before direct delivery. Reuse that helper without creating a team or AI.
        peer_folder=Path("~/brain_workers/w512")
        if not peer_folder.is_dir():
            receipt["reason"]="Named peer folder absent; no new worker created"
        else:
            sys.dont_write_bytecode=True
            sys.path.insert(0,"~/<private-repo>/12_cognitive_architecture/agent_mesh")
            import team_comm
            mesh=team_comm.mesh()
            team_comm.ensure(mesh,"w510")
            team_comm.ensure(mesh,"w512")
            sent=mesh.send("w510","w512","p0162-boundary",body+" Paired adversary packet: ~/brain_workers/w511/REVIEW_PACKET.md.",kind="request")
            team_comm.ring("w512")
            receipt.update(state="delivered via existing-worker registration helper",delivery_result=sent,registration_scope="existing named peer metadata only; no AI process or team started")
except Exception as exc:
    receipt["reason"]=type(exc).__name__+": "+str(exc)
(root/"REVIEW_DELIVERY.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps(receipt))
