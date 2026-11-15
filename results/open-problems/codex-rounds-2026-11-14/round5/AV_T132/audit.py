"""Bounded standard-library checks for the interior-lifting audit."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import os
import re
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
root = Path(__file__).resolve().parent
started = time.monotonic()
print('OMP_NUM_THREADS=1; process priority=', os.getpriority(os.PRIO_PROCESS, 0))

def heights(word):
    l = [0]
    r = [0]
    for dx, dy in word:
        l.append(l[-1]+dx)
        r.append(r[-1]+dy)
    return l, r

def l_stack_partition(l, a, b):
    parent = list(range(len(l)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        parent[find(i)] = find(j)
    stack = []
    for i in range(a, b):
        step = l[i+1]-l[i]
        if step == 0:
            union(i, i+1)
        elif step == 1:
            stack.append(i)
        elif step == -1:
            if stack:
                union(stack.pop(), i+1)
        else:
            raise AssertionError('not an axial walk')
    return [find(i) for i in range(a, b+1)]

def l_minimum_pairs(l, a, b):
    pairs = set()
    for i in range(a, b+1):
        minimum = l[i]
        for j in range(i, b+1):
            minimum = min(minimum, l[j])
            if l[i] == l[j] == minimum:
                pairs.add((i, j))
    return pairs

def r_stack_matches(r, a, b):
    stack = []
    matches = set()
    for v in range(a+1, b+1):
        step = r[v]-r[v-1]
        if step == 1:
            stack.append(v)
        elif step == -1:
            if stack:
                matches.add((stack.pop(), v))
        else:
            assert step == 0
    return matches

def r_minimum_matches(r, a, b):
    matches = set()
    for u in range(a+1, b+1):
        if r[u]-r[u-1] != 1:
            continue
        minimum = r[u]
        for v in range(u+1, b+1):
            if r[v]-r[v-1] == -1 and r[u-1] == r[v] < minimum:
                matches.add((u, v))
            minimum = min(minimum, r[v])
    return matches

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
walks = intervals = zero_pairs = matches_checked = 0
for length in range(1, 8):
    for word in product(directions, repeat=length):
        l, r = heights(word)
        full_lp = l_minimum_pairs(l, 0, length)
        full_rm = r_minimum_matches(r, 0, length)
        assert full_rm == r_stack_matches(r, 0, length)
        for a in range(length+1):
            for b in range(a, length+1):
                internal_lp = l_minimum_pairs(l, a, b)
                assert internal_lp == {(i, j) for i, j in full_lp if a <= i <= j <= b}
                labels = l_stack_partition(l, a, b)
                stack_pairs = {(i, j) for i in range(a, b+1) for j in range(i, b+1)
                               if labels[i-a] == labels[j-a]}
                assert internal_lp == stack_pairs
                internal_rm = r_stack_matches(r, a, b)
                assert internal_rm == r_minimum_matches(r, a, b)
                assert internal_rm == {(u, v) for u, v in full_rm if a < u < v <= b}
                intervals += 1
                zero_pairs += len(internal_lp)
                matches_checked += len(internal_rm)
        walks += 1
print('Exhaustive axial walks of lengths 1..7:', walks)
print('All subintervals including singleton intervals:', intervals)
print('First-coordinate equivalence pairs checked:', zero_pairs)
print('Internal vertical match occurrences checked:', matches_checked)
assert walks == sum(4**n for n in range(1, 8))
assert intervals == sum(4**n*(n+1)*(n+2)//2 for n in range(1, 8))

word = ((0, 1), (1, 0), (0, -1))
l, r = heights(word)
assert r_stack_matches(r, 0, 3) == {(1, 3)}
assert r_stack_matches(r, 0, 2) == set()
assert 0 <= 1-1 <= 2 and 0 <= 3-1 <= 2
print('Boundary trap: representatives 0,2 are internal but step ending at 3 is outside')

# Independent rational recheck of the earlier tail-bound exponents.
cases = 0
for k in range(2, 13):
    for p in (Fraction(1, 3), Fraction(2, 5), Fraction(1, 2), Fraction(3, 4)):
        if k*p <= 1:
            continue
        theta = (k*p-1)/(k-1)
        for log2_r in (Fraction(i, 5) for i in range(200)):
            log2_m = log2_r // (k-1)
            assert (1-k*p)*log2_m + theta*log2_r <= k*p-1
            assert (k-k*p)*log2_m-log2_r+theta*log2_r <= 0
        assert (1-k*p)/(k-1) == (k-k*p)/(k-1)-1 == -theta
        cases += 1
print('Earlier tail estimate: exact rational exponent/rounding checks in', cases, 'cases')

verify = (root/'VERIFY.md').read_text()
fence = chr(96)*3
theorems = [s for s in re.findall(fence+r'latex\n(.*?)\n'+fence, verify, re.S)
            if s.startswith(r'\begin{theorem}')]
intros = ['metric-introduction', 'critical-introduction', 'clock-introduction']
assert len(theorems) == 4
texts = [(root/'sources'/(n+'-fresh.tex')).read_text() for n in intros]
assert all(any(t in s for s in texts) for t in theorems)
print('All four exact main theorem quotations agree with freshly opened TeX')
for name in intros+['background', 'certificates']:
    source = root/'sources'/(name+'.tex')
    assert source.read_bytes() == (root/'sources'/(name+'-fresh.tex')).read_bytes()
    print('SHA256', hashlib.sha256(source.read_bytes()).hexdigest(), name+'.tex')
for name in ['PROOF.md', 'VERIFY.md']:
    document = (root/name).read_text()
    assert not any(ord(c) < 32 and c != '\n' for c in document), name
    for target in re.findall(r'\]\(([^)]+)\)', document):
        if '://' in target or target.startswith('#'):
            continue
        assert (root/target.split('#')[0]).exists(), (name, target)
report = (root/'REPORT.md').read_text()
assert report.startswith('VERDICT: PARTIAL ')
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss*1024
assert rss_bytes < 1024**3
print('Peak resident memory bytes:', rss_bytes)
print('Elapsed seconds:', round(time.monotonic()-started, 3))
print('All checks passed; continuum construction and upper-certificate closure are not verified.')
