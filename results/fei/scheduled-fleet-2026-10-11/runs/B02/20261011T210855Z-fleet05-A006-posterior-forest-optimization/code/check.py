"""Frozen exact checks for A006 sunflower posterior, standard library only."""
from fractions import Fraction as F
from itertools import combinations, permutations
from collections import deque
from math import factorial, comb
from pathlib import Path
from hashlib import sha256
import json
import time

BASE = Path(__file__).resolve().parents[1]
start = time.perf_counter()
checks = 0

def check(ok):
    global checks
    checks += 1
    assert ok

def subsets(m):
    for mask in range(1, 1 << m):
        yield tuple(i+1 for i in range(m) if mask >> i & 1)

def queue(m, a, roots, selected, children):
    """Reconstruct sequential trace, conditional root probability and each draw."""
    odds = F(1, 4*m)
    D = (1+odds)**m-1
    q = odds**len(roots)/D
    work = deque(sorted(roots))
    trace, visited, output = [], set(), set()
    while work:
        gate = work.popleft()
        check(gate not in visited)
        visited.add(gate)
        B = tuple(sorted(selected[gate]))
        s, c = len(B), len(children.get(gate, ()))
        check(set(B) <= {0, gate} and s in (1,2))
        q /= s*(s+1)
        if s == 1:
            q *= (1 if B == (0,) else a)/(1+a)
        q /= (c+1)*(c+2)
        q /= comb(s+c-1, c)
        edges = children.get(gate, ())
        check(tuple(j for j,_ in edges) == tuple(sorted(j for j,_ in edges)))
        for j, child in edges:
            check(j in B and j in {0,child})
            q /= m  # The conditioned forest generator chooses each gate with lambda=1/m.
            work.append(child)
        trace.append((gate, B, edges))
        output.update(B)
    check(visited == set(selected))
    check(sum(map(len,selected.values())) == len(output))
    return (tuple(sorted(roots)),tuple(trace)), tuple(sorted(output)), q

spectra = []
for m in range(1,9):
    n, N = m+1, 1 << (m+1)
    table = [1 if (x&1 and x>>1) else -1 for x in range(N)]
    # Direct character sums, independent of the symbolic expansion in REPORT.md.
    coeff = []
    for S in range(N):
        # x_i=+1 for bit 1: chi_S(x)=(-1)^(|S|-popcount(S&x)).
        numerator = sum(y * (-1 if ((S.bit_count()-(S&x).bit_count())&1) else 1)
                        for x,y in enumerate(table))
        coeff.append(F(numerator,N))
    p = [c*c for c in coeff]
    check(sum(p) == 1)
    check(coeff[0] == -F(1,1<<m))
    check(coeff[1] == 1-F(1,1<<m))
    check(all(p[S] == F(1,4**m) for S in range(2,N)))
    I = sum((p[S]*S.bit_count() for S in range(N)),F(0))
    edge_I = F(sum(table[x] != table[x ^ (1<<i)] for x in range(N) for i in range(n)), N)
    check(I == edge_I == 1+F(m-1,1<<m))
    check(1-p[0] == 1-F(1,4**m))
    spectra.append({'m':m,'I':str(I),'variance':str(1-p[0]),'inputs':N})

check(F(2,5)**5 < F(1,64) < F(1,2)**5)
trace_results = []
for m in range(1,7):
    for a in (F(2,5), F(1,2)):
        D = (1+F(1,4*m))**m-1
        check(0 < D < F(1,3))
        keys = set()
        total = F(0)
        def add(roots,selected,children,wanted):
            global total
            key,A,q = queue(m,a,roots,selected,children)
            check(A == wanted)
            check(key not in keys)
            keys.add(key)
            total += q
            return q
        singleton = sum((add((r,),{r:(0,)},{},(0,)) for r in range(1,m+1)),F(0))
        check(singleton == 1/(16*(1+a)*D))
        for T in subsets(m):
            t = len(T)
            private = add(T,{r:(r,) for r in T},{},T)
            check(private == (a/(16*m*(1+a)))**t/D)
            star = F(0)
            for root in T:
                for order in permutations(tuple(r for r in T if r != root)):
                    selected = {r:((0,r) if r == root else (r,)) for r in T}
                    children = {root:tuple((0,r) for r in order)}
                    star += add((root,),selected,children,(0,)+T)
            expected = F(factorial(t),24*t*t*(t+1)*m**t)/D*(a/(4*(1+a)))**(t-1)
            check(star == expected)
            # Remaining forests: common coordinate assigned to an unused private gate.
            outside = F(0)
            for root in range(1,m+1):
                if root in T:
                    continue
                for order in permutations(T):
                    selected = {r:(r,) for r in T}
                    selected[root] = (0,)
                    outside += add((root,),selected,{root:tuple((0,r) for r in order)},(0,)+T)
            outside_expected = F((m-t)*factorial(t),8*m**(t+1)*(t+1)*(t+2))/(D*(1+a))*(a/(4*(1+a)))**t
            check(outside == outside_expected)
            check(star+outside == expected+outside_expected)
        check(total <= 1)
        trace_results.append({'m':m,'auxiliary_a':str(a),'distinct_runs':len(keys),'total_conditioned_mass':str(total)})

# Rational steps used in the all-m proof, not numerical logarithm comparisons.
check(F(32,3) < 16)
check(80 < 2**7 and 20 < 2**5 and 24 < 2**5)
for m in range(1,13):
    check(sum(comb(m,t)*t for t in range(1,m+1)) == m*2**(m-1))
    check(F(m*m+9*m+5,2**m) <= F(15,2))
    check(F(5*m*m+11*m+4,5*2**m) <= F(23,10))
    if m >= 2:
        check(2*(5*m*m+11*m+4)-(5*(m+1)**2+11*(m+1)+4) >= 0)

result = {'status':'PASS','assertions':checks,'arithmetic':'integers and fractions.Fraction',
          'truth_tables':spectra,'trace_checks':trace_results,
          'actual_theta':'a=2^(-6/5), bracketed by (2/5,1/2); endpoint queue arithmetic is auxiliary, analytic formulas apply to actual a',
          'all_m_certificate':'REPORT.md analytic inequalities; finite checks do not establish the all-m theorem',
          'elapsed_seconds':time.perf_counter()-start,'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
check(result['elapsed_seconds'] < 60)
(BASE/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'assertions':checks,'elapsed_seconds':result['elapsed_seconds'],'output':str(BASE/'out'/'CHECK.json')},indent=2))
