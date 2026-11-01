import json
import pathlib

root = pathlib.Path('~/Downloads/Probability_1000_20h_20260906/sources')
for topic in ('beta_splitting_overview', 'lyons_determinantal_2014', 'free_unimodality_journal_2018', 'biskup_dgff_extrema_2020'):
    path = root / topic / 'text.txt'
    with path.open('rb') as file:
        prefix = file.read(600)
    print(json.dumps({'path': str(path), 'bytes': path.stat().st_size, 'first_bytes': prefix.decode('utf-8', errors='replace')}, ensure_ascii=False))
