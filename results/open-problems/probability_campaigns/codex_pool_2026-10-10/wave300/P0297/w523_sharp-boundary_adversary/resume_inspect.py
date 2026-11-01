"""Check named receipts without re-running the finished mathematical experiment."""
from pathlib import Path
import json

ROOT=Path('~')
JOB=Path(__file__).resolve().parent
inbox=ROOT/'math-brain-inbox/w523'
local=(JOB/'bundle_local_001.json').read_bytes()
submitted=inbox/'bundle_001.json'
print('DRAFT_CONTENT_MATCH',submitted.is_file() and submitted.read_bytes()==local)
print('REFEREE_VERDICTS')
path=ROOT/'brain_workers/w524/VERDICTS.jsonl'
for line in path.read_text(encoding='utf-8-sig').splitlines():
    row=json.loads(line)
    print(json.dumps(row,ensure_ascii=False))
print('REFEREE_C3_CONTEXT')
path=ROOT/'brain_workers/w524/REVIEW_PACKET.md'
lines=path.read_text(encoding='utf-8-sig').splitlines()
hits=[i for i,x in enumerate(lines) if any(s in x for s in ['w523','C3','ingest','independent','NEXT:'])]
for i in sorted({j for n in hits for j in range(max(0,n-1),min(len(lines),n+2))}):
    print(f'{i+1}: {lines[i]}')
print('PROGRESS_HELPER_RELEVANT_LINES')
path=ROOT/'primary_directive/pd_progress.py'
lines=path.read_text(encoding='utf-8').splitlines()
hits=[i for i,x in enumerate(lines) if any(s in x for s in ['add_argument','def main','--event','write_text','open(', 'sqlite', 'subprocess', 'TEAM', 'agent_mesh','send('])]
for i in sorted({j for n in hits for j in range(max(0,n-1),min(len(lines),n+3))}):
    print(f'{i+1}: {lines[i]}')
print('NAMED PEER ROUTING')
for name,terms in [('team_comm.py',['DB =','def cmd_say','def ensure']),('agent_mesh.py',['def cmd_send','add_parser("send"','--to','--body','--kind','--agent','--topic'])]:
    path=ROOT/'<private-repo>/12_cognitive_architecture/agent_mesh'/name
    lines=path.read_text(encoding='utf-8').splitlines()
    hits=[i for i,x in enumerate(lines) if any(s in x for s in terms)]
    for i in sorted({j for n in hits[:18] for j in range(max(0,n-1),min(len(lines),n+7))}):
        print(name,f'{i+1}: {lines[i]}')
print('INBOX RECEIPT FILENAMES', [p.name for p in inbox.iterdir() if p.is_file()])
