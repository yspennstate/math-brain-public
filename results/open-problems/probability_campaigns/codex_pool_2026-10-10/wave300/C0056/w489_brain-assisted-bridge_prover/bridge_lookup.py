"""Bounded, read-only lookup of a few exported mathematical cards, never a store load."""
from pathlib import Path
import json
import subprocess
import time

BASE = Path(__file__).resolve().parent
EXPORT = Path('~/math-brain-build/export/population/nodes.jsonl')
QUERIES = {
    'spectral_averaging': 'spectral averaging|Simon.Wolff',
    'poisson_bridge': 'Stieltjes inversion|Poisson.*absolut|absolut.*Poisson',
    'anderson': 'Anderson model|Bethe lattice',
    'measure_bridge': 'Radon.Nikodym theorem|Lebesgue decomposition theorem',
}

def main():
    output = {'source': str(EXPORT), 'mode': 'read-only export lookup', 'max_rows_per_query': 4, 'queries': []}
    for name, pattern in QUERIES.items():
        command = ['rg', '--no-heading', '-i', '-m', '4', '-e', pattern, str(EXPORT)]
        start = time.perf_counter()
        record = {'name': name, 'pattern': pattern, 'command': command, 'rows': []}
        try:
            run = subprocess.run(command, capture_output=True, encoding='utf-8', errors='replace', timeout=45)
            record['exit_code'] = run.returncode
            record['stderr'] = run.stderr[:1000]
            if run.returncode in (0, 1):
                record['rows'] = [json.loads(line) for line in run.stdout.splitlines() if line.strip()]
            else:
                record['failure'] = 'rg failed'
        except subprocess.TimeoutExpired:
            record['failure'] = 'deadline 45 seconds'
        record['seconds'] = round(time.perf_counter() - start, 6)
        record['count'] = len(record['rows'])
        output['queries'].append(record)
        (BASE / 'BRAIN_RETRIEVAL.json').write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')
        print(json.dumps(record, ensure_ascii=False), flush=True)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
