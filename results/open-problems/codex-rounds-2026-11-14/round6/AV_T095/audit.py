"""Exact checks for the BK/itinerary reduction; stdlib, one thread.

Run: OMP_NUM_THREADS=1 nice -n 15 python3 audit.py
No network, file writes, simulations, external libraries, or Lean build.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from pathlib import Path
import math
import os
import re
import resource
import signal
import time

signal.alarm(60)
ROOT = Path(__file__).resolve().parent


def disjoint(options):
    """Packing by support unions; supports are edge or bit masks."""
    reachable = {0}
    for choices in options:
        reachable = {old | new for old in reachable for new in choices
                     if not old & new}
        if not reachable:
            return False
    return True


def submasks(mask):
    current = mask
    while True:
        yield current
        if current == 0:
            return
        current = (current-1) & mask


def rounding_checks():
    count = 0
    for u in [F(0), F(1, 2), F(3, 4), F(1, 3), F(7, 8),
              F(1, 1009), F(1008, 1009)]:
        previous = F(1)
        for t in range(1, 41):
            rounded = F(math.floor((2**t)*u)+1, 2**t)
            # Evaluate the bit-prefix sum separately from the cell formula.
            prefix = F(0)
            for h in range(1, t+1):
                bit = math.floor(2**h*u)-2*math.floor(2**(h-1)*u)
                prefix += F(bit, 2**h)
            assert rounded == prefix+F(1, 2**t)
            assert u <= rounded <= previous and rounded-u <= F(1, 2**t)
            previous = rounded
            count += 1
    # Alternative expansion 0.011111... represents 1/2 as well.
    for t in range(1, 41):
        prefix = sum((F(1, 2**h) for h in range(2, t+1)), F(0))
        assert prefix+F(1, 2**t) == F(1, 2)
        # With the terminating expansion, equality is approached from above.
        assert F(1, 2)+F(1, 2**t) > F(1, 2)
        count += 1
    print('Upper rounding and dyadic-endpoint checks:', count, 'PASS')


def finite_bk():
    # Four collinear lattice edges. A tuple gives traversal multiplicities.
    # All supports below are intervals, realizable by a finite lattice walk;
    # the multiplicity-two path goes out and back on one edge.
    unit = [tuple(int(j == i) for j in range(4)) for i in range(4)]
    family = [
        [(unit[0], F(2))],
        [(unit[1], F(2))],
        [(unit[0], F(2)), (unit[1], F(2))],
        [((1, 1, 0, 0), F(4))],
        [((0, 1, 1, 0), F(4)), ((0, 0, 1, 1), F(4))],
        [((2, 0, 0, 0), F(4)), ((0, 0, 2, 0), F(4))],
        [(unit[0], F(2)), (unit[0], F(4))],  # labeled same path, two bounds
        [(unit[0], F(8))],                # bit occurrence can exceed edge occurrence
        [((1, 1, 1, 1), F(16))],
        [(unit[2], F(1))],                 # impossible strict cost < 0
        [((0, 0, 0, 0), F(2))],          # certain, zero-edge path
    ]
    lists = [(i,) for i in range(len(family))]
    lists += list(combinations_with_replacement(range(len(family)), 2))
    lists += list(combinations_with_replacement(range(len(family)), 3))
    lists += [(i,)*4 for i in range(len(family))]
    totals = dict(lists=0, configurations=0, packing_comparisons=0,
                  repeated_lists=0, proper_bit_supersets=0)
    for precision in (1, 2):
        bits = 4*precision
        states = 1 << bits
        full = states-1
        # x are complemented bits, making events increasing.
        witnesses = [[None]*states for _ in family]
        truth = [[False]*states for _ in family]
        for x in range(states):
            survival = []
            for edge in range(4):
                prefix = sum(((1-((x >> (edge*precision+h-1)) & 1))*F(1, 2**h)
                              for h in range(1, precision+1)), F(0))
                survival.append(1-prefix-F(1, 2**precision))
            for j, paths in enumerate(family):
                successful = set()
                for multiplicities, C in paths:
                    score = F(1)
                    support = 0
                    for e, m in enumerate(multiplicities):
                        if m:
                            score *= survival[e]**m
                            support |= 1 << e
                    if score > 1/C:       # sum m_e tau_e < log C
                        successful.add(support)
                witnesses[j][x] = successful
                truth[j][x] = bool(successful)
            totals['configurations'] += 1
        # Independent positive certificates from all truth-table subconfigs.
        certs = [[None]*states for _ in family]
        for j in range(len(family)):
            for x in range(states):
                # Minimal positive sets suffice; compute from truth only,
                # without accessing path supports or traversal multiplicities.
                candidates = [s for s in submasks(x) if truth[j][s]]
                minimal = [s for s in candidates
                           if not any(truth[j][s ^ (1 << k)]
                                      for k in range(bits) if s & (1 << k))]
                certs[j][x] = minimal
                for k in range(bits):
                    assert not truth[j][x] or truth[j][x | (1 << k)]
        event_counts = [sum(row) for row in truth]
        for labels in lists:
            direct_count = 0
            bit_count = 0
            for x in range(states):
                direct = disjoint([witnesses[j][x] for j in labels])
                bit = disjoint([certs[j][x] for j in labels])
                assert not direct or bit
                direct_count += direct
                bit_count += bit
                totals['packing_comparisons'] += 1
            rhs = math.prod(event_counts[j] for j in labels)
            denominator = states**(len(labels)-1)
            assert direct_count*denominator <= bit_count*denominator <= rhs
            totals['lists'] += 1
            totals['repeated_lists'] += len(set(labels)) < len(labels)
            totals['proper_bit_supersets'] += bit_count > direct_count
    assert totals['repeated_lists'] > 0
    assert totals['proper_bit_supersets'] > 0
    for key, value in totals.items():
        print('Finite BK '+key+':', value)
    print('Direct edge packing <= bit-certificate occurrence <= product: PASS')


def itinerary_checks():
    count = 0
    for s in (2, 3, 8):
        for L in (1, 3, 16):
            for x0 in range(-2*L, 2*L):
                for dx in range(-2*L, 2*L+1):
                    di = math.floor(F(x0+dx, L))-math.floor(F(x0, L))
                    assert abs(di) <= 2
                    count += 1
            for r0 in (F(-13, 7), F(-1, 7), F(0), F(6, 7), F(37, 7)):
                for dnum in range(-7*(s+1), 7*(s+1)+1):
                    dr = F(dnum, 7)
                    dh = math.floor((r0+dr)/s)-math.floor(r0/s)
                    assert abs(dh) <= 2 <= 3
                    count += 1
    print('Independent floor-index displacement cases:', count, 'PASS')
    count = 0
    for N in range(1, 513):
        t = N//16
        dp = [1]+[0]*t
        # Unbounded occupancy in each position; prefix sums implement
        # dp_new[j] = sum(dp_old[j-k], k=0..j).
        for _ in range(N+1):
            prefix = 0
            new = []
            for x in dp:
                prefix += x
                new.append(prefix)
            dp = new
        assert dp[t] == math.comb(N+t, t) <= 2**(N+t) <= 4**N
        count += 1
    print('Weak compositions: independent DP/binomial checks:', count, 'PASS')
    for N in range(16, 4097):
        minimum_M = math.floor(F(N, 8)-F(1, 4))+1
        assert minimum_M >= N//16
    assert 49*4 == 196
    assert F(196, 800) == F(49, 200) < 1
    # Explicit admissible p = 2^-160. The root is exactly 2^-10.
    assert 16*10 == 160
    assert 400*F(1, 2**10) == F(25, 64) < F(1, 2)
    R = F(196, 2**10)
    assert R == F(49, 256) < F(49, 200)
    for N in range(16, 513):
        assert N//16 >= F(N, 16)-1
        # Check the exponent inequality independently using N=16q+r.
        quotient, remainder = divmod(N, 16)
        assert quotient == N//16 and 0 <= remainder < 16
        assert 160*quotient >= 10*N-160
    tail = sum((R**n for n in range(16, 49)), F(0))
    assert tail+R**49/(1-R) == R**16/(1-R)
    print('Multiplicity thresholds: 4081 PASS; constants 196 and 49/200 PASS')
    print('Floor-exponent and exact geometric-tail identities: PASS')


def document_checks():
    count = 0
    verify = (ROOT/'VERIFY.md').read_text()
    for name in ('source-exponential-introduction.tex',
                 'source-no-bigeodesics-introduction.tex', 'source-qaoa-introduction.tex'):
        text = (ROOT/name).read_text()
        earlier = Path('~/codex_op_1114r5/briefs/AV_T095')/name
        assert text.rstrip() == earlier.read_text().rstrip()
        for block in re.findall(r'\\begin\{theorem\}[\s\S]*?\\end\{theorem\}', text):
            assert block in verify
            count += 1
    assert count == 4
    witness = (ROOT/'source-witnesses.tex').read_text()
    earlier = Path('~/codex_op_1114r5/briefs/AV_T095/source-witnesses.tex')
    assert witness.rstrip() == earlier.read_text().rstrip()
    for label in ('df:wi:continuous-bk', 'df:wi:long-paths'):
        assert label in witness and label in (ROOT/'PROOF.md').read_text()
    for name in ('VERIFY.md', 'PROOF.md'):
        for target in re.findall(r'\]\(([^)]+)\)', (ROOT/name).read_text()):
            if not target.startswith(('http://', 'https://')):
                assert (ROOT/target).exists(), target
    report = (ROOT/'REPORT.md').read_text()
    assert report.startswith('VERDICT: PARTIAL ')
    print('Four exact theorem blocks, preserved sources, links and verdict: PASS')


def main():
    started = time.monotonic()
    assert os.environ.get('OMP_NUM_THREADS') == '1'
    priority = os.getpriority(os.PRIO_PROCESS, 0)
    assert priority >= 15
    print('OMP_NUM_THREADS=1; process nice:', priority)
    rounding_checks()
    finite_bk()
    itinerary_checks()
    document_checks()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert rss < 1024**3
    print('Peak RSS bytes (macOS):', rss)
    print('Elapsed seconds:', round(time.monotonic()-started, 3))


if __name__ == '__main__':
    main()
