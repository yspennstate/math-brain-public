import json
from pathlib import Path

root = Path(__file__).resolve().parent
base = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
receipt = {}
for name in ('problems.jsonl', 'attempts.jsonl'):
    selected = []
    with (base / name).open(encoding='utf-8') as stream:
        for lineno, line in enumerate(stream, 1):
            if 'C0052' not in line:
                continue
            row = json.loads(line)
            if row.get('problem_id', row.get('id')) == 'C0052':
                selected.append({'line': lineno, 'record': row})
    receipt[name] = selected
    print(name, json.dumps(selected, ensure_ascii=False))
with (base / 'sources.jsonl').open(encoding='utf-8') as stream:
    for lineno, line in enumerate(stream, 1):
        if 'duminil_copin_ising_potts_2017' in line:
            receipt['primary_source'] = {'line': lineno, 'record': json.loads(line)}
            print('primary_source', line.strip())
            break
(root / 'LOCAL_SOURCE_RECEIPT.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False), encoding='utf-8')
