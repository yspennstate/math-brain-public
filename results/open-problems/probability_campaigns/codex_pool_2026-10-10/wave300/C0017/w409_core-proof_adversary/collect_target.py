"""Read only C0017's cited intake/prior records and save bounded extracts locally."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
RESEARCH = Path('~/<private-repo>/06_math_research')
out = []
intake = RESEARCH / 'probability_1000_intake_claude_20260907'
for name in ('problems.jsonl', 'attempts.jsonl'):
    p = intake / name
    if p.exists():
        for no, line in enumerate(p.open(encoding='utf-8-sig'), 1):
            if 'C0017' in line:
                out.append({'path': str(p), 'line': no, 'record': json.loads(line)})
for name in ('brain_bundle_C004.json', 'brain_bundle_C004a.json', 'brain_bundle_C004b.json'):
    p = intake / name
    if p.exists():
        data = json.loads(p.read_text(encoding='utf-8-sig'))
        for row in data.get('entries', []):
            text = json.dumps(row, ensure_ascii=False)
            if 'C0017' in text or 'conformal invariance of critical bond percolation' in text.lower():
                out.append({'path': str(p), 'record': row})
p = RESEARCH / 'prob1000_lean_20260908/RANKED_LIST_2026-09-07_annotated.md'
if p.exists():
    for no, line in enumerate(p.open(encoding='utf-8-sig'), 1):
        if 'C0017' in line:
            out.append({'path': str(p), 'line': no, 'text': line.rstrip()})
(ROOT / 'target_extracts.json').write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(out, indent=2, ensure_ascii=False))
