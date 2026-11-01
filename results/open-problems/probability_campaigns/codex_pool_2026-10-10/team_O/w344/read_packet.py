import json
import pathlib

ROOT = pathlib.Path('~')
HERE = pathlib.Path(__file__).resolve().parent
IDS = ['P0341', 'C0039', 'P0023', 'P0177', 'C0004', 'C0063', 'C0087', 'C0139', 'P0018', 'P0047']
DIRS = [ROOT / 'Downloads/Probability_1000_20h_20260906', ROOT / '<private-repo>/06_math_research/probability_1000_intake_claude_20260907']
selected = []
source_ids = set()
for directory in DIRS:
    for filename in ('problems.jsonl', 'attempts.jsonl'):
        path = directory / filename
        if not path.is_file():
            continue
        for line_no, line in enumerate(path.open(encoding='utf-8-sig'), 1):
            row = json.loads(line)
            pid = row.get('problem_id', row.get('id'))
            if pid not in IDS:
                continue
            record = {'path': str(path), 'line': line_no, 'record': row}
            selected.append(record)
            source_ids.add(row.get('source_id', ''))
            if directory == DIRS[0]:
                print(json.dumps(record, ensure_ascii=False))
sources = []
for directory in DIRS:
    path = directory / 'sources.jsonl'
    for line_no, line in enumerate(path.open(encoding='utf-8-sig'), 1):
        row = json.loads(line)
        if row.get('source_id', row.get('id')) in source_ids:
            record = {'path': str(path), 'line': line_no, 'record': row}
            sources.append(record)
            print(json.dumps(record, ensure_ascii=False))
(HERE / 'packet_sources.json').write_text(json.dumps({'records': selected, 'sources': sources}, indent=2, ensure_ascii=False), encoding='utf-8')
