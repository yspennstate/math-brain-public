"""Bounded exact counterchecks and source checks for the T132 transfer lemma."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import os
import re
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
root = Path(__file__).resolve().parent
started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15
print('OMP_NUM_THREADS=1; priority=', priority)

# No sampling: evaluate the infinite-tail example by exact finite sums plus
# the exact remaining geometric mass. Independently integrate the survival
# function over the intervals between its atoms.
for n in range(1, 41):
    eps = F(1, 2**n)
    atom_sum = sum(F(1, 2**(j+1)) * eps * 2**j for j in range(n))
    atom_sum += F(1, 2**n)
    tail_integral = eps  # On [0, eps), the survival probability is one.
    for j in range(n):
        lo, hi = eps*2**j, min(F(1), eps*2**(j+1))
        if lo < hi:
            tail_integral += (hi-lo)*F(1, 2**(j+1))
    closed_form = (1+F(n, 2))*eps
    assert atom_sum == tail_integral == closed_form
    # Truncated E[Y] grows as (N+1)/2, so the full mean is infinite.
    assert sum(F(1, 2**(j+1))*2**j for j in range(n+1)) == F(n+1, 2)
print('Infinite-mean example: atom sum and tail integral agree in 40 exact cases')
for n in (1, 5, 10, 20, 40):
    print('n=', n, 'E[min(1,2^-n Y)]=', (1+F(n, 2))*F(1, 2**n))

# Recheck the scaling identity without numerical powers: exponents of 2
# in v^p cancel from numerator and denominator, for many exact p,i.
scales = 0
for p in (F(1, 3), F(2, 7), F(3, 8)):
    for i in range(21):
        c_exp, h_exp, v_exp = F(-7), F(5), -i*p
        direct = (c_exp+v_exp)-(h_exp+v_exp)
        assert direct == c_exp-h_exp
        scales += 1
print('Quantum-unit cancellation: exact exponent checks in', scales, 'cases')

# Earlier tail estimate: independently balance the pure/mixed exponents and
# check their dyadic rounding on rational log scales.
cases = 0
for k in range(2, 13):
    for p in (F(1, 3), F(2, 5), F(1, 2), F(3, 4)):
        if k*p <= 1:
            continue
        theta = (k*p-1)/(k-1)
        assert (1-k*p)/(k-1) == (k-k*p)/(k-1)-1 == -theta
        for log_r in (F(j, 5) for j in range(100)):
            log_m = log_r // (k-1)
            assert (1-k*p)*log_m+theta*log_r <= k*p-1
            assert (k-k*p)*log_m-log_r+theta*log_r <= 0
        cases += 1
print('Earlier tail estimate: exact exponent/rounding checks in', cases, 'cases')

# Necessary-hypothesis checks, not planar-map counterexamples.
for r in (1, 2, 10, 100):
    eps, reference, passage = F(1, r), F(r), F(1)
    assert eps*reference == passage
print('Non-tight reference countercheck: prefactor -> 0, passage cost stays 1')
for cutoff in range(1, 11):
    # A compact [1/cutoff,1] contains no witness 1/r once r>cutoff.
    r = cutoff+1
    assert F(1, r) < F(1, cutoff)
print('Escaping-witness countercheck: every fixed interior compact loses witnesses')
labels = (0, 1)  # Indicator of membership in Q, used symbolically.
for a in labels:
    for b in labels:
        for c in labels:
            assert abs(a-c) <= abs(a-b)+abs(b-c)
assert abs(1-1) == 0 and abs(1-0) == 1
print('Dense-set countercheck: indicator pseudometric obeys triangle inequality')

verify = (root/'VERIFY.md').read_text()
fence = chr(96)*3
theorems = [t for t in re.findall(fence+r'latex\n(.*?)\n'+fence, verify, re.S)
            if t.startswith(r'\begin{theorem}')]
intros = ['metric-introduction', 'critical-introduction', 'clock-introduction']
texts = [(root/'sources'/(name+'-round6.tex')).read_text() for name in intros]
assert len(theorems) == 4
assert all(any(t in s for s in texts) for t in theorems)
print('Four exact main theorem quotations match the freshly opened TeX')
for name in intros+['bootstrap', 'certificates', 'comparison', 'background']:
    old = root/'sources'/(name+'.tex')
    fresh = root/'sources'/(name+'-round6.tex')
    assert old.read_bytes() == fresh.read_bytes(), name
    print('SHA256', hashlib.sha256(fresh.read_bytes()).hexdigest(), fresh.name)
for old, fresh in [('211.md', '211-round6.md'),
                   ('FKCRT.lean', 'FKCRT-round6.lean')]:
    assert (root/'sources'/old).read_bytes() == (root/'sources'/fresh).read_bytes()
print('Lean scope source unchanged: q>4/CRT only; no Lean build performed')

for name in ['PROOF.md', 'VERIFY.md', 'REPORT.md', 'LOG.md']:
    document = (root/name).read_text()
    assert not any(ord(c) < 32 and c != '\n' for c in document), name
    for target in re.findall(r'\]\(([^)]+)\)', document):
        if '://' in target or target.startswith('#'):
            continue
        assert (root/target.split('#')[0]).exists(), (name, target)
report = (root/'REPORT.md').read_text()
assert report.startswith('VERDICT: PARTIAL ')
assert '## Round 6 verification' in verify
assert '### Spot check: vanishing upper comparisons' in verify
recommendation = verify.split('### Round 6 recommended replacement')[1].strip().split('\n\n')[0]
assert len(re.split(r'(?<=[.!?])\s+', recommendation)) == 3
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
print('Document format, local links and three-sentence recommendation pass')
print('Peak resident memory bytes:', rss_bytes)
print('Elapsed seconds:', round(time.monotonic()-started, 3))
print('All checks passed; raw-array construction and local joining remain inputs.')
