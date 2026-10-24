from pathlib import Path
import json

for agent in ('w562', 'w563'):
    p = Path('~/brain_workers') / agent / 'STATUS.md'
    print(agent, p.read_text(encoding='utf-8')[:2000] if p.exists() else 'NO_STATUS')
p = Path('~/math-research-brain')
print('CANONICAL_ROOT_NAMES', [x.name for x in p.iterdir() if x.name.lower() not in ('tests','.git','.venv')][:35])
for filename in ('README.md','pyproject.toml'):
    file = p / filename
    if file.exists():
        lines = file.read_text(encoding='utf-8').splitlines()
        for index, line in enumerate(lines):
            if any(term in line.lower() for term in ('sqlite','store','canonical','recall')):
                print(filename, index+1, line[:250])
                if index > 160:
                    break
path = Path('sources/openai_formalization.yaml')
lines = path.read_text(encoding='utf-8').splitlines()
print('FORMAL_CATALOGUE_MATCHES', [(i+1,s) for i,s in enumerate(lines) if 'BenjaminiSchramm' in s or 'CayleyPercolation' in s or 'Nonuniqueness-of-percolation' in s])
