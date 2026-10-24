import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESEARCH = Path('~/<private-repo>/06_math_research')
IDS = ['P0189', 'P0390', 'C0100', 'P0031', 'P0242', 'C0011', 'C0070', 'C0105', 'C0153', 'P0025']
out = ROOT / 'evidence'
out.mkdir(exist_ok=True)
records = {p: [] for p in IDS}
source_ids = set()
folders = list(sorted(RESEARCH.glob('probability_1000_intake_*')))
folders += [RESEARCH / 'probability_1000_20h_20260906', Path('~/.codex/worktrees/probability-1000-20h-20260906/06_math_research/probability_1000_20h_20260906')]
folders += [Path('~/Downloads/Probability_1000_20h_20260906')]
for folder in folders:
    for name in ['problems.jsonl', 'attempts.jsonl']:
        path = folder / name
        if not path.is_file():
            continue
        with path.open(encoding='utf-8-sig') as f:
            for line_no, line in enumerate(f, 1):
                if not any('"' + p + '"' in line for p in IDS):
                    continue
                row = json.loads(line)
                pid = row.get('problem_id')
                if pid in records:
                    records[pid].append({'path': path.as_posix(), 'line': line_no, 'record': row})
                    if row.get('source_id'):
                        source_ids.add(row['source_id'])
sources = []
for folder in folders:
    path = folder / 'sources.jsonl'
    if not path.is_file():
        continue
    with path.open(encoding='utf-8-sig') as f:
        for line_no, line in enumerate(f, 1):
            if any(s in line for s in source_ids):
                sources.append({'path': path.as_posix(), 'line': line_no, 'record': json.loads(line)})
for pid, rows in records.items():
    (out / (pid + '_intake.json')).write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(pid, 'matched_rows=', len(rows), 'source_ids=', sorted({r['record'].get('source_id') for r in rows if r['record'].get('source_id')}))
(out / 'source_metadata.json').write_text(json.dumps(sources, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('P0189 records:', json.dumps(records['P0189'], indent=2, ensure_ascii=False))
for source in sources:
    if any(source['record'].get('source_id') == r['record'].get('source_id') for r in records['P0189']):
        print('P0189 source:', json.dumps(source, ensure_ascii=False))
