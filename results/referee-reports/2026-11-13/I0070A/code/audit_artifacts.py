"""Check source provenance, plain-text-only storage, and report structure."""
import hashlib
import json
import os
from pathlib import Path

root = Path(__file__).resolve().parents[1]
failures = []
records = [json.loads(line) for line in (root/'data/source_manifest.jsonl').read_text().splitlines()]
for item in records:
    p = root/'sources'/f"{item['name']}.txt"
    text = p.read_text()
    expected = [f"===== PDF PAGE {i} =====" for i in range(1,item['pages']+1)]
    actual = [line for line in text.splitlines() if line.startswith('===== PDF PAGE ')]
    if actual != expected:
        failures.append(f"page separators: {p.name}")
    if item['url'] not in text.splitlines()[0]:
        failures.append(f"source URL: {p.name}")
    if item['sha256_pdf'] not in text[:600]:
        failures.append(f"source hash: {p.name}")
for p in root.rglob('*'):
    if not p.is_file():
        continue
    if p.suffix.lower() in {'.pdf','.png','.jpg','.jpeg','.tif','.tiff','.webp','.gif'}:
        failures.append(f"forbidden artifact: {p.relative_to(root)}")
    if p.parent == root/'sources' and p.suffix != '.txt':
        failures.append(f"non-text source: {p.name}")
    if p.open('rb').read(5) == b'%PDF':
        failures.append(f"PDF signature: {p.relative_to(root)}")
report = (root/'REPORT.md').read_text()
if report.splitlines()[0] not in {'PROVED','COUNTEREXAMPLE','PARTIAL','NO_PROGRESS','RESOLVED_IN_LITERATURE'}:
    failures.append('invalid status line')
if report.count(r'\[') != report.count(r'\]'):
    failures.append('unbalanced display math')
if r'\$' in report:
    failures.append('escaped closing inline dollar')
display = False
for n,line in enumerate(report.splitlines(),1):
    if line.strip() == r'\[':
        display = True
    if not display and line.count('$') % 2:
        failures.append(f'unbalanced inline math on line {n}')
    if line.strip() == r'\]':
        display = False
result = {
    'status': 'PASS' if not failures else 'FAIL',
    'failures': failures,
    'source_texts': len(records),
    'extracted_pages_including_distinct_versions': sum(x['pages'] for x in records),
    'source_text_bytes': sum(p.stat().st_size for p in (root/'sources').glob('*.txt')),
    'niceness': os.getpriority(os.PRIO_PROCESS,0),
    'report_sha256': hashlib.sha256(report.encode()).hexdigest(),
    'scope': 'Artifact and provenance checks; these do not certify the mathematical proof.'
}
(root/'data/artifact_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if failures:
    raise SystemExit(1)
