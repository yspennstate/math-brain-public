"""Route the authorized named-peer messages through team_comm only."""
import sqlite3
import subprocess

TEAM = "C0120-w492-w493-w494"
TOOL = "~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py"
with sqlite3.connect("file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro", uri=True) as c:
    exists = c.execute("SELECT 1 FROM campaigns WHERE name=? AND status='active'", (TEAM,)).fetchone()

def run(args):
    r = subprocess.run(["python", "-X", "utf8", TOOL, *args], capture_output=True,
                       text=True, encoding="utf-8", timeout=60)
    print(r.stdout.strip())
    if r.stderr:
        print(r.stderr.strip())
    if r.returncode:
        raise RuntimeError(f"team_comm returned {r.returncode}")

if not exists:
    run(["new", TEAM, "--as", "w493", "--hours", "6", "--goal",
         "C0120 named-triad review only: independent proofs, source scope, exact gaps; no shared proof mutation"])

run(["say", "--as", "w493", "--team", TEAM, "--to", "w492", "--kind", "claim",
     "Disjoint C0120 lane: Gaussian layer-mean variance floor H_n and exact n=2 OU overlap. Independent derivation saved before reading your proof: ~/brain_workers/w493/ATTEMPT.md. Audited L1-L4: scoped KEEP; G1 remains UNPROVED. Full verdicts: w493/AUDIT_VERDICTS.jsonl. No store promotion or served-model receipt."])
run(["say", "--as", "w493", "--team", TEAM, "--to", "w494", "--kind", "review",
     "Please independently check w493 claims 003-005: exact layer-mean variance decomposition, overlap floor H_n, n=2 R(t)=3/2+asin(exp(-t))/pi, and conditional noise-to-variance reduction. ~/brain_workers/w493/ATTEMPT.md and CLAIMS.jsonl; 116 finite checks passed in MEASUREMENTS.json. G1 remains unproved; source-scope correction needs Claude gate; served identity unavailable."])
run(["read", "--as", "w493"])
