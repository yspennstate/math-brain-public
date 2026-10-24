"""A single bounded measurement on the real read-only store, not a blind bank."""
import json
import sys
from pathlib import Path
from math_source_fallback import lookup

ROOT = Path(__file__).resolve().parent
database = Path('~/math-brain-build/local/population/brain.sqlite3')
results = []
for terms in [['percolation','exponential'], ['anchored','expansion'], ['percolation','sharpness']]:
    result = lookup(database, terms, limit=5)
    results.append(result)
    (ROOT/'TARGETED_CARDS.json').write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))
baseline = json.loads((ROOT/'math_recall_receipt.json').read_text(encoding='utf-8'))
receipt = {'baseline':baseline, 'fallback':[{k:v for k,v in row.items() if k!='hits'} for row in results],
           'interpretation':'Measures bounded source recovery after a ranked-recall timeout; not a ranking-quality or mathematical-proof score.'}
(ROOT/'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
