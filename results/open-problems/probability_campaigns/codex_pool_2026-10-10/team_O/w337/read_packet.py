"""Filter the named ledgers by assigned IDs; never read banks or whole exports."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=Path('~/<private-repo>/06_math_research')
IDS=['P0209','P0459','C0130','P0088','P0336','C0022','C0076','C0117','P0009','P0035']
rows=[]
directories=[BASE/d for d in ['probability_1000_intake_claude_20260907','probability_1000_intake_H_20260914','probability_1000_intake_I_20260914']]
directories.append(Path('~/Downloads/Probability_1000_20h_20260906'))
for directory in directories:
    for name in ['problems.jsonl','attempts.jsonl']:
        p=directory/name
        if not p.is_file():
            continue
        with p.open(encoding='utf-8-sig') as f:
            for lineno,line in enumerate(f,1):
                hits=[v for v in IDS if v in line]
                if hits:
                    rows.append({'path':p.as_posix(),'line':lineno,'ids':hits,'record':json.loads(line)})
(ROOT/'evidence').mkdir(exist_ok=True)
(ROOT/'evidence'/'packet_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for row in rows:
    if any(pid.startswith('P') for pid in row['ids']):
        print(json.dumps(row,ensure_ascii=False))
