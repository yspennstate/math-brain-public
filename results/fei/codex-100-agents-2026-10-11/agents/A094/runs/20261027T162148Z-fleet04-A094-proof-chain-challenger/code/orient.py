from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1]
RUN.joinpath('out').mkdir(exist_ok=True)
BASE=RUN.parents[3]
files=[BASE/'BOARD.md',BASE/'claude/B19/STREAM_NOTES.md',RUN.parents[1]/'STATUS.md',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
files += list((BASE/'agents/A011/runs/20261027T025625Z-fleet04-A011-representation-existence').glob('*.md'))
files += list((BASE/'agents/A011/runs/20261027T025625Z-fleet04-A011-representation-existence').glob('CLAIMS.json'))
receipts=[]
for p in files:
 if p.is_file():
  b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
RUN.joinpath('out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('source receipts',len(receipts))
