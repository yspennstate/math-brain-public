"""Sequential exact certificates. One process, no worker pool."""
import json
import time
from pathlib import Path
from escape import poisson_bounds

cases = [
    ('m2_p08', ['4/5']*2, 8),
    ('m2_p09', ['9/10']*2, 8),
    ('m2_p09_p08', ['9/10','4/5'], 8),
    ('m2_p08_p09', ['4/5','9/10'], 8),
    ('m3_p07', ['7/10']*3, 80),
    ('m3_p075', ['3/4']*3, 80),
    ('m3_p08', ['4/5']*3, 96),
    ('m3_p09', ['9/10']*3, 96),
    ('m3_p23over30', ['23/30']*3, 80),
    ('m4_p075', ['3/4']*4, 96),
]

for name, params, K in cases:
    path = Path('data') / f'cert_{name}.json'
    if path.exists():
        print('exists', name, flush=True)
        continue
    start = time.monotonic()
    value = poisson_bounds(params, K, 90, exact=True)
    value['seconds'] = time.monotonic()-start
    path.write_text(json.dumps(value, indent=2)+'\n')
    print(name, value['lower'][:48], value['upper'][:48],
          'width', value['width'][:14], 'seconds', round(value['seconds'], 2), flush=True)
