"""Recheck all saved LP results with an explicit one-thread HiGHS scheduler.

RA columns are retained: their NumPy operations and BLAS were already serial.
"""
import csv
import json
from pathlib import Path
import resource
import time
from numerics import laws, occupation_lp


def main():
    catalogue = {law.name: law for law in laws()}
    start = time.monotonic()
    total = 0
    for path in sorted(Path('data').glob('results_*.csv')):
        with path.open() as f:
            rows = list(csv.DictReader(f))
        for row in rows:
            result = occupation_lp(catalogue[row['law']], int(row['n']), int(row['bins']))
            assert row['lp_status'] == result['lp_status'], (row, result)
            row.update(result)
            total += 1
        with path.open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print(path, len(rows), flush=True)
    record = dict(cases=total, status_changes=0,
                  seconds=time.monotonic()-start, highs_threads=1,
                  peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    Path('data/lp_thread_validation.json').write_text(json.dumps(record, indent=2)+'\n')
    print(record)


if __name__ == '__main__':
    main()
