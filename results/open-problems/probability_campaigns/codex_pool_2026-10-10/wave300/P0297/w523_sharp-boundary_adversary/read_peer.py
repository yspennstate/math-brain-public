"""Read the paired proof only after the independent artifact is on disk."""
from pathlib import Path
import json

ROOT = Path('~')
JOB = ROOT / 'brain_workers/w523'
assert (JOB / 'INDEPENDENT.md').exists()
peer = ROOT / 'brain_workers/w522'
for name in ['STATEMENT_FOR_ADVERSARY.md', 'ATTEMPT.md', 'CLAIMS.jsonl', 'REVIEW_PACKET.md', 'SOURCE_STATUS.json', 'EXISTING_P0297_CARDS.json']:
    p = peer / name
    print('FILE', p)
    if p.exists():
        print(p.read_text(encoding='utf-8')[:16000])
for name in ['README.md']:
    p = ROOT / 'primary_directive/hooks1000' / name
    print('HOOK_SCHEMA', p)
    if p.exists():
        lines=p.read_text(encoding='utf-8').splitlines()
        hits=[i for i,x in enumerate(lines) if any(s in x.lower() for s in ['schema', 'fire', 'silent', 'jsonl'])]
        for i in sorted({j for hit in hits for j in range(max(0,hit-3), min(len(lines),hit+13))}):
            print(f'{i+1}: {lines[i]}')
for folder in ['w515','w518','w525']:
    p=ROOT / 'brain_workers' / folder / 'STATUS.md'
    print('OTHER_LANE_STATUS',folder)
    if p.exists():
        print(p.read_text(encoding='utf-8')[:2400])
data=json.loads((JOB/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
data['paired_proof_read']=True
data['independent_derivation_preceded_paired_proof']=True
data['independent_artifact']='INDEPENDENT.md'
(JOB/'SOURCE_STATUS.json').write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding='utf-8')
