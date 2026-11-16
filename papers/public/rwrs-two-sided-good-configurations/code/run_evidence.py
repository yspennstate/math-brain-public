"""Save exact conditional probabilities and TV gaps as rows are completed."""
import csv
from fractions import Fraction
from pathlib import Path
import os
import resource
import time
from rwrs_exact import conditional, self_check


def record(m, n, kind):
    out = []
    for t in range(-m, m+1):
        if t == 0:
            out.append(None)
        elif abs(t) <= n or kind == 'black':
            out.append(1)
        elif kind == 'white_tails':
            out.append(0)
        elif kind == 'period4_tails':
            out.append(int((abs(t)-n-1) % 4 >= 2))
        elif kind == 'opposite_tails':
            out.append(int(t < 0))
        elif kind == 'period2_tails':
            out.append((abs(t)-n) % 2)
        else:
            raise ValueError(kind)
    return out


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 10
    checks = self_check()
    start = time.monotonic()
    peak = 0
    path = Path('data/finite_windows.csv')
    fields = ['p','n','m','extension','base_black_probability','extension_black_probability',
              'tv_gap','tv_gap_decimal','peak_states','seconds']
    rows = 0
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for p in map(Fraction, ['1/2','3/4','39/50','79/100','4/5','81/100','41/50','17/20','97/100','199/200']):
            for n in (2,4,6):
                for m in sorted(set([n, n+2, n+4, n+8, n+12, n+20, n+28])):
                    now = time.monotonic()
                    base, bp = conditional(record(m,n,'black'),p)
                    for kind in ('white_tails','period4_tails','opposite_tails','period2_tails'):
                        other, op = conditional(record(m,n,kind),p)
                        gap = abs(base-other)
                        peak = max(peak,bp,op)
                        writer.writerow(dict(p=str(p),n=n,m=m,extension=kind,
                            base_black_probability=str(base),extension_black_probability=str(other),
                            tv_gap=str(gap),tv_gap_decimal=f'{float(gap):.12g}',
                            peak_states=max(bp,op),seconds=f'{time.monotonic()-now:.6f}'))
                        rows += 1
                        f.flush()
            print(f'p={p}: {rows} rows; peak states {peak}', flush=True)
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    Path('data/computation_summary.txt').write_text(
        f'exact_self_checks={checks}\nrows={rows}\npeak_dp_states={peak}\n'
        f'elapsed_seconds={time.monotonic()-start:.6f}\nmacos_peak_rss_bytes={rss}\n'
        f'nice={os.getpriority(os.PRIO_PROCESS,0)}\nthreads=1\n'
        'arithmetic=integer path weights, fractions.Fraction conditional probabilities\n')


if __name__ == '__main__':
    main()
