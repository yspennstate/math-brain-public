from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];(R/'out').mkdir(exist_ok=True)
old=A/'runs/20261023T112901Z-fleet03-A011-representation-existence'
(R/'code/shared.py').write_bytes((old/'code/shared.py').read_bytes())
base=Path('~/brain_workers/FEI100_20261011')
sources=[base/'BOARD.md',base/'claude/B03/STREAM_NOTES.md',old/'DERIVATION.md',old/'CLAIMS.json',base/'agents/A086/runs/20261023T114749Z-fleet03-A086-joint-code-referee/REPORT.md',base/'agents/A094/runs/20261023T131208Z-fleet03-A094-proof-chain-challenger/REPORT.md',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'),old/'code/shared.py']
rows=[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources]
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':rows},indent=2),encoding='utf-8',newline='')
(A/'STATUS.md').write_text('STATE: A011 stage21 ACTIVE: arbitrary physical query-policy extension drafted with same b12/K and full old U, including exposed controls/zero fibers; exact verification pending; FEI OPEN.\nNEXT: Verify cylinder partition identity, actual r0 models and full signed frontiers; A086/A094 reconstruct policy extension.\n',encoding='utf-8',newline='')
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='') as f:f.write('\n\n## 2026-10-23 stage21 checkpoint\nRead current board/lead/status and new A086/A094 context. Drafted arbitrary physical policy extension of v4: multiple hit leaves partition each edit cylinder; reprice unchanged first/second floors at9/8 and5/4, handle exposed new controllers r0 and mass retained on zero fibers. Same b12,K4C0+15,full old U; new margin[(6311/23552)C0+18111/4096]Ig+KsumG. Proof/spec saved before checks. Independent proof review pending; full FEI OPEN.\n')
print('stage21 proof/spec/checkpoint saved; source receipts pinned')
