from pathlib import Path
import json

root = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
for name in ('problems.jsonl', 'attempts.jsonl'):
    path = root / name
    print('SOURCE', path)
    with path.open(encoding='utf-8-sig') as handle:
        for line_number, line in enumerate(handle, 1):
            if 'C0056' not in line:
                continue
            row = json.loads(line)
            print('LINE', line_number)
            print(json.dumps(row, ensure_ascii=False, indent=2))
            (Path(__file__).parent / ('C0056_' + name.replace('.jsonl', '.json'))).write_text(json.dumps(row, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

