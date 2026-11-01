import json
import os
from pathlib import Path
import subprocess

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
base = Path(__file__).resolve().parent
comm = '~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py'
messages = [
    ['read', '--as', 'w483', '--max', '6'],
    ['say', '--as', 'w483', '--to', 'w484', '--kind', 'handoff-note',
     'C0056 statement FIRST, no route: ~/brain_workers/w483/STATEMENT_TO_ADVERSARY.md . Bourgade section 2.1 p7 has AC and separate periodic-box GOE goals. Uniform-law slice and fixed-g quantifiers explicit. Sept23 2026 public AC claim found; openness UNKNOWN pending independent validation. Attack statement before reading my attempt.'],
    ['say', '--as', 'w483', '--kind', 'claim',
     'C0056 independent boundary claimed: cutoff local spectral-measure L2 criterion, weighted two-eigenvalue concentration, and flat-Walsh-eigenvector Cantor obstruction. Route precommitted before peer proofs: ~/brain_workers/w483/ROUTE_PRECOMMIT.md . L1-L5 saved in ATTEMPT.md; parent NOT PROVED.'],
]
receipts = []
for args in messages:
    try:
        r = subprocess.run(['python','-X','utf8',comm,*args], capture_output=True,
                           text=True, encoding='utf-8', errors='replace', timeout=75)
        receipt = {'args': args, 'returncode': r.returncode,
                   'stdout': r.stdout, 'stderr': r.stderr}
        print(json.dumps(receipt, ensure_ascii=False), flush=True)
    except subprocess.TimeoutExpired:
        receipt = {'args':args, 'status':'timed-out; delivery unconfirmed; do not blindly resend'}
        print(json.dumps(receipt), flush=True)
    receipts.append(receipt)
    (base/'STATEMENT_SEND_RECEIPTS.json').write_text(json.dumps(receipts,indent=2,ensure_ascii=False),encoding='utf-8')
