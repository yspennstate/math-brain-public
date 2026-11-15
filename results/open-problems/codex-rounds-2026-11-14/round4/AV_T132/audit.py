"""Bounded standard-library checks for the T132 moment audit."""
from pathlib import Path
from fractions import Fraction
from math import factorial
import hashlib
import os
import re
import resource
import sys

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
root = Path(__file__).resolve().parent
old = Path('~/codex_op_1114r3/briefs/AV_T132')
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
print('OMP_NUM_THREADS=1; process priority=', os.getpriority(os.PRIO_PROCESS, 0))

verify = (root/'VERIFY.md').read_text()
fence = chr(96)*3
blocks = re.findall(fence+r'latex\n(.*?)\n'+fence, verify, re.S)
theorems = [b for b in blocks if b.startswith(r'\begin{theorem}')]
intros = ['metric-introduction.tex', 'critical-introduction.tex',
          'clock-introduction.tex']
texts = [(root/'sources'/n).read_text() for n in intros]
assert len(theorems) == 4
assert all(any(b in t for t in texts) for b in theorems)
print('All 4 exact main theorem blocks match freshly opened source TeX')
for n in intros + ['moments.tex', '211.md', 'FKCRT.lean']:
    assert (root/'sources'/n).read_bytes() == (old/'sources'/n).read_bytes(), n
assert (root/'sources/bootstrap.tex').read_bytes() == (old/'sources/tree-bootstrap.tex').read_bytes()
print('No source drift in 3 introductions, moments, bootstrap or 2 Lean scope files')

def compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for first in range(total+1):
        for tail in compositions(total-first, slots-1):
            yield (first,) + tail

checked = 0
for k in range(2, 9):
    u = Fraction(k, k-1)
    for m in range(1, 5):
        coefficients = pure = mixed = 0
        for a in compositions(k, m):
            coefficient = factorial(k)
            for ai in a:
                coefficient //= factorial(ai)
            coefficients += coefficient
            support = [ai for ai in a if ai]
            if len(support) == 1:
                pure += coefficient
            else:
                assert all(u*ai <= k for ai in support)
                assert sum(u*ai/k for ai in support) == u
                mixed += coefficient
            checked += 1
        assert coefficients == m**k
        assert pure == m
        assert mixed == m**k-m
print('Exact multinomial/Hölder checks:', checked, 'exponent vectors')

cases = 0
for k in [3, 6, 12]:
    for p in [Fraction(1, 2), Fraction(1, 3), Fraction(2, 5)]:
        if k*p <= 1:
            continue
        eta = (k*p-1)/(k-1)
        assert eta > 0
        assert (1-k*p)/(k-1) == -eta
        assert (k-k*p)/(k-1)-1 == -eta
        for log2_r in [Fraction(j, 3) for j in range(300)]:
            h = log2_r // (k-1)
            pure_log = (1-k*p)*h + eta*log2_r
            mixed_log = (k-k*p)*h-log2_r + eta*log2_r
            assert pure_log <= k*p-1
            assert mixed_log <= 0
        cases += 1
print('Tail exponent and dyadic rounding: exact rational checks in', cases, 'parameter cases')
print('Illustrative k=6, p=1/3: theta=1/5, C=3 (not a value of d_sqrt(2))')

k = 4
for r in [2, 10, 100]:
    prob = Fraction(1, r**k)
    assert prob*r**k == 1
    for m in [1, 2, 4, 8, 16]:
        assert prob*Fraction(r, m)**k == Fraction(1, m**k)
    print('Dependent example: r=', r, 'P(nonzero)=', prob, 'unit kth moment=1')

def stirling_row(k):
    row = [1]
    for n in range(1, k+1):
        nxt = [0]*(n+1)
        for j in range(1, n+1):
            nxt[j] = (row[j-1] if j-1 < len(row) else 0) + (j*row[j] if j < len(row) else 0)
        row = nxt
    return row

row = stirling_row(4)
assert row == [0, 1, 7, 6, 1]
for n in range(12):
    fall = 1
    rhs = 0
    for j in range(1, 5):
        fall *= n-j+1
        rhs += row[j]*fall
    assert rhs == n**4

def poisson_moment(lam):
    return sum(Fraction(row[j])*lam**j for j in range(1, 5))

for exponent in [1, 3, 6]:
    lam = Fraction(1, 10**exponent)
    norm4 = poisson_moment(lam)
    for t in [Fraction(1, 2), Fraction(1, 4), Fraction(1, 8)]:
        assert poisson_moment(lam*t) <= t*norm4
    assert norm4/norm4 == 1
    print('Poisson boundary: lambda=', lam, 'normalized fourth moment=1; P(nonzero)<=lambda')
print('Poisson polynomial [1,7,6,1] checked by recurrence and falling-factorial identity')

report = (root/'REPORT.md').read_text()
assert report.startswith('VERDICT: PARTIAL ')
for document in ['VERIFY.md', 'PROOF.md']:
    for target in re.findall(r'\]\(([^)]+)\)', (root/document).read_text()):
        if '://' in target or target.startswith('#'):
            continue
        assert (root/target.split('#')[0]).exists(), (document, target)
print('Verdict format and local Markdown links pass')
for n in ['bootstrap.tex', 'moments.tex', 'certificates.tex', 'comparison.tex'] + intros:
    path = root/'sources'/n
    print('SHA256', hashlib.sha256(path.read_bytes()).hexdigest(), n)
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
print('Peak resident memory bytes:', rss_bytes)
print('All checks passed. These checks do not verify spatial certificate geometry.')
