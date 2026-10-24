import json
from pathlib import Path

base = Path('~/<private-repo>/06_math_research')
paths = [
    base / 'probability_1000_intake_claude_20260907/problems.jsonl',
    base / 'probability_1000_intake_claude_20260907/attempts.jsonl',
    base / 'prob1000_lean_20260908/RANKED_LIST_2026-09-07_annotated.md',
]
parts = []
for path in paths:
    parts.append(str(path))
    with path.open(encoding='utf-8-sig') as stream:
        for number, line in enumerate(stream, 1):
            if 'C0054' not in line:
                continue
            parts.append(f'LINE {number}:')
            try:
                obj = json.loads(line)
                parts.append(json.dumps(obj, ensure_ascii=False, indent=2)[:18000])
            except json.JSONDecodeError:
                parts.append(line[:9000])
text = '\n'.join(parts)
Path(__file__).with_name('LOCAL_SOURCE_RECORDS.txt').write_text(text, encoding='utf-8')
print(text)
