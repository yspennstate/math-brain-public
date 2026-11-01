"""Named-peer handoffs through the installed team communication tool."""
import json
import os
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parent
tool = "~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py"
team = "P0162-independent-w507"
receipt = {"initial_failure": "Team read: database locked. Direct say: sender had no team.",
           "resolution": "Create a scoped coordination channel for w507 using the installed tool; no agent or runner is spawned.", "steps": []}
env = dict(os.environ)
env["PYTHONDONTWRITEBYTECODE"] = "1"


def call(label, arguments):
    p = subprocess.run([sys.executable, "-B", "-X", "utf8", tool, *arguments], capture_output=True,
                       text=True, encoding="utf-8", errors="replace", cwd=root, env=env)
    record = {"step": label, "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
    receipt["steps"].append(record)
    (root / "PEER_DELIVERY.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record), flush=True)
    return p.returncode == 0


if not call("create-own-coordination-channel", ["new", team, "--as", "w507", "--hours", "3", "--goal",
    "P0162 w507 independent flat-spectrum splice extension; named-peer statement and referee handoff only"]):
    raise SystemExit(1)
if not call("statement-first-to-adversary", ["say", "--as", "w507", "--to", "w508", "--kind", "found",
    "Statement first: P0162 asks one universal finite C with H_2(f)<=C I(f), for every dimension and Boolean f under uniform input. Exact normalized target and primary source: ~/brain_workers/w507/CLAIMS.jsonl first row. Current openness UNKNOWN. Please keep your first adversarial argument independent."]):
    raise SystemExit(1)
if not call("narrow-claim-to-referee", ["say", "--as", "w507", "--to", "w509", "--kind", "claim",
    "Claim L4-L5 only: arbitrary bent base / arbitrary flipped vertex, fixed spectral entropy and exact I(F)=m/2+(m+1-2*s_g(a))/2^m; full-parity twist attains class-max H/I. Canonical witness L1-L3 independently overlaps w505 and is reproduction only. ~/brain_workers/w507/ATTEMPT.md. No full FEI or novelty claim."]):
    raise SystemExit(1)
if not call("complete-packet-to-referee", ["say", "--as", "w507", "--to", "w509", "--kind", "review",
    "Please KEEP/FIX/DROP L4-L5 with independent sign-count and edge-count derivation. Full packet: ~/brain_workers/w507/REVIEW_PACKET.md; source/prior boundary, proof, fresh-gate receipts, CLAIMS and draft brain bundle there. Universal good-coordinate/aggregate charge remains the single gap. Return your verdict artifact path; no global FEI theorem claimed."]):
    raise SystemExit(1)
call("read-after-saved-batch", ["read", "--as", "w507", "--max", "8"])
