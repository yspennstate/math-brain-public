"""Small exact checks of the saved sources and conditional reduction.

Run with OMP_NUM_THREADS=1 nice -n 15 python3 audit.py.
No network, third-party modules, simulations, or Lean builds.
"""

from fractions import Fraction as F
from pathlib import Path
import math
import os
import re
import signal

signal.alarm(30)
ROOT = Path(__file__).resolve().parent
OLD = Path('~/codex_op_1114/briefs/AV_T095')


def theorem_blocks(text):
    return re.findall(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', text)


def main():
    print('OMP_NUM_THREADS=' + str(os.environ.get('OMP_NUM_THREADS')))
    print('Process nice value:', os.getpriority(os.PRIO_PROCESS, 0))
    verify = (ROOT / 'VERIFY.md').read_text()
    total = 0
    for name in ('source-exponential-introduction.tex',
                 'source-no-bigeodesics-introduction.tex',
                 'source-qaoa-introduction.tex'):
        current = (ROOT / name).read_text()
        previous = (OLD / name).read_text()
        assert current == previous, name
        blocks = theorem_blocks(current)
        assert blocks, name
        for block in blocks:
            assert block in verify, name
        total += len(blocks)
    assert total == 4
    print('Sources unchanged; all four exact theorem blocks present: PASS')

    # Integer-shape Gamma integrals computed by the elementary identity
    # integral t^(k-1) exp(-beta*t) dt = (k-1)! / beta^k.
    # This uses exact rational arithmetic, not numerical quadrature.
    count = 0
    for k in (1, 2, 3, 7):
        for rate in (F(1, 3), F(1), F(5)):
            for delta in (F(1, 8), F(1, 4), F(1, 2)):
                alpha = 1 - delta
                beta = rate * (2 / alpha - 1)
                factorial = math.factorial(k - 1)
                by_integral = (alpha ** (-2 * k) * rate ** k
                               / factorial * factorial / beta ** k)
                by_formula = (1 - delta ** 2) ** (-k)
                assert by_integral == by_formula
                count += 1
    print('Exact Gamma integral checks:', count, 'PASS')

    cases = 0
    largest = F(0)
    for s in (1, 2, 4):
        n = s ** 3
        for b in (F(-1), F(-3, 4), F(0), F(1, 3), F(1)):
            for phase in (F(0), F(1, 2)):
                vertices = set()
                for x in range(-n, 2 * n + 1):
                    center = b * x + phase
                    for y in range(math.ceil(center - 8 * s),
                                   math.floor(center + 8 * s) + 1):
                        vertices.add((x, y))
                edges = sum(((x + 1, y) in vertices)
                            + ((x, y + 1) in vertices)
                            for x, y in vertices)
                assert edges <= 2 * len(vertices)
                assert edges <= 144 * n * s
                largest = max(largest, F(edges, n * s))
                cases += 1
    print('Explicit internal-edge enumeration:', cases, 'cases PASS')
    print('Largest enumerated M/(ns):', largest, '(bound 144)')

    # Exact tail identity, checked by splitting off a finite block and
    # comparing the claimed remainder. Its all-J proof is in VERIFY.md.
    tail = lambda j: F(2) ** (1 - j) * (j*j + 2*j + 3)
    for j in range(1, 51):
        end = j + 37
        finite = sum(F(h*h, 2**h) for h in range(j, end))
        assert tail(j) == finite + tail(end)
    print('Attachment-tail identities: 50 exact checks PASS')

    lines = (ROOT / 'REPORT.md').read_text().splitlines()
    assert lines[0].startswith('VERDICT: PARTIAL ')
    assert len(lines) == 4
    status = verify.split('## Recommended replacement for “where it stands”\n\n')[1]
    status = status.split('\n\nTask:')[0]
    assert len(re.findall(r'\.(?:\s|$)', status)) == 3
    for target in re.findall(r'\]\(([^)]+)\)', verify):
        if target.startswith(('https://', 'http://')):
            continue
        assert (ROOT / target).exists(), target
    print('Report format, three-sentence status, local links: PASS')


if __name__ == '__main__':
    main()
