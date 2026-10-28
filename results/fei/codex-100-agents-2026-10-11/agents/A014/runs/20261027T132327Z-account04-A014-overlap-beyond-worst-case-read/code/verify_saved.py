"""Final UTF-8 readback, honest formal status, and persistence receipt check."""
from pathlib import Path
import hashlib
import json

run = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
receipt_path = run / 'out/RECEIPTS.json'
receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
for item in receipt['files']:
    path = run / item['path']
    assert sha(path) == item['sha256'], path
    assert path.stat().st_size == item['bytes'], path
for item in receipt['rolling']:
    assert sha(Path(item['path'])) == item['sha256'], item['path']
formal = json.loads((run / 'out/LEAN.json').read_text(encoding='utf-8-sig'))
assert formal['result']['status'] == 'RUNTIME_UNVERIFIED'
assert not formal['result']['formal_target_verified']
report_path = run / 'REPORT.md'
report = report_path.read_text(encoding='utf-8')
old = 'The contemplated core Lean check has its own memok admission and25s budget; it states ONLY exact scalar constants.'
new = 'The core Lean check passed memok admission but exhausted its25s budget: out/LEAN.json reports RUNTIME_UNVERIFIED and formal_target_verified=false. It states ONLY exact scalar constants, which therefore have no Lean verification receipt.'
if old in report:
    report = report.replace(old, new)
    report = report.replace('The incidence-to-influence factor3 is sharp', 'The strict inequality is for I>0; the constant case is zero<=zero. The incidence-to-influence factor3 is sharp', 1)
    report_path.write_text(report, encoding='utf-8')
assert report.rstrip().split('\n\n')[-1].startswith('C020 whole-set payment')
assert (run / 'PROGRESS.json').read_bytes() == (run / 'PACKET_DELTA.json').read_bytes()
agent = run.parents[1]
assert len((agent / 'STATUS.md').read_text(encoding='utf-8').splitlines()) == 2
receipt['formal_scope'] = 'Scalar only; RUNTIME_UNVERIFIED after 25s; no formal target verified'
receipt['files'] = [dict(path=str(p.relative_to(run)), bytes=p.stat().st_size, sha256=sha(p)) for p in sorted(run.rglob('*')) if p.is_file() and p != receipt_path]
for item in receipt['files']:
    assert item['bytes'] < 20_000_000, item['path']
receipt_path.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
check = json.loads(receipt_path.read_text(encoding='utf-8'))
assert all(sha(run / i['path']) == i['sha256'] for i in check['files'])
print(json.dumps(dict(saved_hashes='PASS', files=len(check['files']), delta='PASS', rolling='PASS', formal='RUNTIME_UNVERIFIED', nonpilot_assertions=27095)))
