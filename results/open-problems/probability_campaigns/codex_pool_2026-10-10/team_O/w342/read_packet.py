"""Read only the ten named rows and their prior attempts from the original intake."""
import json
from pathlib import Path

root = Path('~/Downloads/Probability_1000_20h_20260906')
if '--sources' in __import__('sys').argv:
    wanted_sources = {'grimmett_2022_selected','randomstrasse_2025_v1','lyons_peres_20260819','schramm_2006_v2','queues_ross_second_2022'}
    for line in (root/'sources.jsonl').open(encoding='utf-8-sig'):
        row = json.loads(line)
        if row.get('source_id') in wanted_sources:
            print(json.dumps(row,ensure_ascii=False))
    raise SystemExit(0)
wanted = {'P0289', 'P0001', 'P0133', 'P0015', 'P0044'}
source_ids = set()
for name in ('problems.jsonl', 'attempts.jsonl'):
    with (root/name).open(encoding='utf-8-sig') as handle:
        for line in handle:
            row = json.loads(line)
            if row.get('problem_id', row.get('id')) in wanted:
                print(name, json.dumps(row, ensure_ascii=False))
                source_ids.add(row.get('source_id'))
with (root/'sources.jsonl').open(encoding='utf-8-sig') as handle:
    for line in handle:
        row = json.loads(line)
        if row.get('source_id') in source_ids:
            print('sources.jsonl', json.dumps(row, ensure_ascii=False))
