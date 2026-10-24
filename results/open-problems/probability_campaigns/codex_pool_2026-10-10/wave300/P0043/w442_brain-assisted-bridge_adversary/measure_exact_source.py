"""Refine the broad fallback query using the recovered primary-source title."""
import json
from pathlib import Path
from math_source_fallback import lookup

ROOT = Path(__file__).resolve().parent
result = lookup(Path('~/math-brain-build/local/population/brain.sqlite3'),
                ['critical percolation', 'quasi-transitive'], limit=5)
(ROOT/'EXACT_TARGET_CARDS.json').write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
receipt = json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
receipt['exact_source_fallback'] = {k:v for k,v in result.items() if k!='hits'}
receipt['broad_query_limitation'] = 'percolation AND exponential retrieved FPP and generic decay rows, not the intended critical quasi-transitive source; the exact-source fragments are a different, user-chosen lookup.'
(ROOT/'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))
