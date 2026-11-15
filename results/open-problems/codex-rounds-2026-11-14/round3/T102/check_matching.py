#!/usr/bin/env python3
"""Exact independent Dirichlet checks; Python standard library, one process."""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json
import os
import resource
import signal
import time

ROOT = Path(__file__).resolve().parent
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
START = time.monotonic()


def eliminate(a, b):
    """Forward elimination and back substitution, exact rational arithmetic."""
    n = len(b)
    a = [[F(x) for x in row] for row in a]
    b = list(map(F, b))
    for j in range(n):
        k = next(k for k in range(j, n) if a[k][j])
        a[j], a[k], b[j], b[k] = a[k], a[j], b[k], b[j]
        for i in range(j + 1, n):
            if not a[i][j]:
                continue
            w = a[i][j] / a[j][j]
            for k in range(j, n):
                a[i][k] -= w * a[j][k]
            b[i] -= w * b[j]
    x = [F(0)] * n
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i+1, n))) / a[i][i]
    return x


def vertices(edges):
    return {u for u,v,r in edges} | {v for u,v,r in edges}


def components(edges, extra=()):
    vs = vertices(edges) | set(extra)
    adj = {v:set() for v in vs}
    for u,v,r in edges:
        adj[u].add(v); adj[v].add(u)
    out = []
    while vs:
        comp = {next(iter(vs))}
        todo = list(comp)
        while todo:
            v = todo.pop()
            for u in adj[v] - comp:
                comp.add(u); todo.append(u)
        out.append(comp); vs -= comp
    return out


def energy(edges, f):
    return sum((r*x*x for (u,v,r),x in zip(edges,f)), F(0))


def divergence(edges, f, boundary):
    d = {v:F(0) for v in boundary}
    for (u,v,r),x in zip(edges,f):
        if u in d: d[u] += x
        if v in d: d[v] -= x
    return d


def unit_voltage(edges, left, right):
    """Fix each left vertex at 1, each right at 0; solve harmonic interior."""
    left, right = set(left), set(right)
    assert left.isdisjoint(right)
    vs = vertices(edges) | left | right
    fixed = {v:F(v in left) for v in left | right}
    for comp in components(edges, vs):
        if comp.isdisjoint(fixed):
            fixed[next(iter(comp))] = F(0)
    free = sorted(vs - fixed.keys())
    idx = {v:i for i,v in enumerate(free)}
    a = [[F(0) for _ in free] for _ in free]
    b = [F(0) for _ in free]
    for u,v,r in edges:
        c = 1/F(r)
        for s,t in ((u,v),(v,u)):
            if s in idx:
                a[idx[s]][idx[s]] += c
                if t in idx: a[idx[s]][idx[t]] -= c
                else: b[idx[s]] += c*fixed[t]
    potential = dict(fixed)
    potential.update(zip(free, eliminate(a,b)))
    f = [(potential[u]-potential[v])/r for u,v,r in edges]
    total = sum(divergence(edges,f,left).values())
    assert total > 0
    f = [x/total for x in f]
    assert energy(edges,f) == 1/total
    return 1/total, f


def dipole(edges,u,v):
    if u == v: return F(0), [F(0)]*len(edges)
    return unit_voltage(edges,[u],[v])


def diameter(edges, boundary):
    return max((dipole(edges,u,v)[0] for u,v in combinations(boundary,2)), default=F(0))


def pair_check(a,b,s):
    ra,fa = unit_voltage(a,['x'],s)
    rb,fb = unit_voltage(b,s,['y'])
    qa = {v:-x for v,x in divergence(a,fa,s).items()}
    qb = divergence(b,fb,s)
    assert min(qa.values()) >= 0 and min(qb.values()) >= 0
    assert sum(qa.values()) == sum(qb.values()) == 1
    tv = sum(abs(qa[v]-qb[v]) for v in s)/2
    da,db = diameter(a,s),diameter(b,s)
    bound = (da*db/(da+db) if da+db else F(0))*tv*tv
    whole,f = unit_voltage(a+b,['x'],['y'])
    d = whole-ra-rb
    assert 0 <= d <= bound
    # Orthogonal projection check, independent of the explicit bound.
    eta_a = [x-y for x,y in zip(f[:len(a)],fa)]
    eta_b = [x-y for x,y in zip(f[len(a):],fb)]
    assert d == energy(a,eta_a)+energy(b,eta_b)
    assert sum(r*x*y for (u,v,r),x,y in zip(a,fa,eta_a)) == 0
    assert sum(r*x*y for (u,v,r),x,y in zip(b,fb,eta_b)) == 0
    return ra,rb,whole,d,bound


# Recheck all 255 assignments from the earlier report, with Dirichlet solves.
s = ['u','v','w']
pairs = list(combinations(s,2))
count = positive = 0
for lm,rm,ch in product(range(1,8),range(1,8),product(range(3),repeat=3)):
    a = [('x',v,F(1)) for i,v in enumerate(s) if lm >> i & 1]
    b = [(v,'y',F(1)) for i,v in enumerate(s) if rm >> i & 1]
    a += [(u,v,F(1)) for (u,v),c in zip(pairs,ch) if c == 1]
    b += [(u,v,F(1)) for (u,v),c in zip(pairs,ch) if c == 2]
    if len(components(a,['x']+s)) != 1 or len(components(b,s+['y'])) != 1:
        continue
    *_,d,bound = pair_check(a,b,s)
    count += 1; positive += int(d>0)
assert (count,positive) == (255,210)

# Earlier cycle example, reduced exactly to weighted path edges.
cycle_rows = []
for length in [1,2,3,4,8,16,32]:
    a = [('x','u',F(1)),('x','v',F(length))]
    b = [('u','y',F(length)),('v','y',F(1))]
    ra,rb,r,d,bound = pair_check(a,b,['u','v'])
    assert ra == rb == F(length,length+1)
    assert r == F(length+1,2)
    assert d == bound == F((length-1)**2,2*(length+1))
    cycle_rows.append({'L':length,'D':str(d),'bound':str(bound)})

# Nonuniform resistances, three-vertex interface, including non-proportional
# trace forms. Enumerate 3^6 choices of terminal-edge resistances on two stars.
weighted_count = 0
strict_count = 0
for rs in product([F(1),F(2),F(5)], repeat=6):
    a = [('x',v,r) for v,r in zip(s,rs[:3])]
    b = [(v,'y',r) for v,r in zip(s,rs[3:])]
    *_,d,bound = pair_check(a,b,s)
    weighted_count += 1
    strict_count += int(0 < d < bound)
assert weighted_count == 729


def layers_check(pieces,boundaries):
    theta = [unit_voltage(e,l,r) for e,l,r in zip(pieces,boundaries,boundaries[1:])]
    all_edges = [edge for piece in pieces for edge in piece]
    r, full = unit_voltage(all_edges,boundaries[0],boundaries[-1])
    scalar = sum(x[0] for x in theta)
    correction = F(0)
    offset = 0
    for edges,(ri,fi) in zip(pieces,theta):
        eta = [x-y for x,y in zip(full[offset:offset+len(edges)],fi)]
        offset += len(edges)
        assert sum(re*x*y for (u,v,re),x,y in zip(edges,fi,eta)) == 0
        correction += energy(edges,eta)
    assert r == scalar+correction
    bound_sum = F(0)
    details = []
    for i in range(len(pieces)-1):
        si = boundaries[i+1]
        q = {v:-x for v,x in divergence(pieces[i],theta[i][1],si).items()}
        p = divergence(pieces[i+1],theta[i+1][1],si)
        tv = sum(abs(q[v]-p[v]) for v in si)/2
        a,b = diameter(pieces[i],si),diameter(pieces[i+1],si)
        term = a*b/(a+b)*tv*tv if a+b else F(0)
        details.append((a,b,tv,term))
        bound_sum += term
    assert 0 <= correction <= 2*bound_sum
    return r,scalar,correction,bound_sum,details


sharp_rows = []
for length in [1,2,4,8,16,32,64,128,256,512,1024]:
    k = length**2
    pieces = [[('x','u',F(1)),('x','v',F(k))],
              [('u','p',F(1)),('v','q',F(1)),('p','q',F(length))],
              [('p','y',F(k)),('q','y',F(1))]]
    boundaries = [['x'],['u','v'],['p','q'],['y']]
    r,scalar,d,bnd,details = layers_check(pieces,boundaries)
    tv = F(k-1,2*(k+1))
    expected = tv*tv*(F((k+1)*(length+2),k+length+3)
                     +F((k+1)*length,k+length+1))
    assert bnd == expected
    assert details[0][:3] == (k+1,length+2,tv)
    assert details[1][:3] == (length,k+1,tv)
    assert scalar == 2*F(k,k+1)+F(1,2)
    lower = 1/(F(1,length)+F(2,k))
    assert lower <= r <= length+3
    # A separate two-variable energy minimization of the entire network.
    # Let a be current x->v, and b be current p->y. Other currents:
    # x->u->p: 1-a; v->q: a; p->q: 1-a-b; q->y: 1-b.
    # E=2(1-a)^2+(k+1)a^2+k*b^2+(1-b)^2+L(1-a-b)^2.
    aa,bb = eliminate([[k+3+length,length],[length,k+1+length]],
                      [2+length,1+length])
    second = 2*(1-aa)**2+(k+1)*aa**2+k*bb**2+(1-bb)**2+length*(1-aa-bb)**2
    assert r == second
    sharp_rows.append({'L':length,'K':k,'R':str(r),'D':str(d),'sum_terms':str(bnd),
                       'D_over_sum':str(d/bnd) if bnd else None,
                       'D_over_sum_decimal':float(d/bnd) if bnd else None})
assert F(sharp_rows[-1]['D_over_sum']) > F(199,100)

# Multi-layer enumeration: unit links form connected strips; unequal boundary
# resistances and crossing patterns test both correction signs.
multilayer_count = 0
for weights in product([1,3],repeat=6):
    for flip in [False,True]:
        u,v = ('q','p') if flip else ('p','q')
        pieces = [[('x','u',F(weights[0])),('x','v',F(weights[1]))],
                  [('u',u,F(weights[2])),('v',v,F(weights[3])),('u','v',F(2))],
                  [('p','y',F(weights[4])),('q','y',F(weights[5]))]]
        layers_check(pieces,[['x'],['u','v'],['p','q'],['y']])
        multilayer_count += 1

# Disconnected layer from the earlier report: repair on the connected outside
# pieces only. This avoids pretending the middle resistance diameter is finite.
pieces = [[('x','u',F(1)),('x','v',F(1))],
          [('u','p',F(1)),('v','q',F(3))],
          [('p','y',F(1)),('q','y',F(1))]]
rr,ff = unit_voltage(sum(pieces,[]),['x'],['y'])
assert rr == F(15,8)
# Scalar sum=1/2+3/4+1/2=7/4. Each mismatch TV=1/4;
# repair both in outside layers with diameter 2. No layer has two repairs.
one_sided_bound = 2*F(1,4)**2+2*F(1,4)**2
assert rr-F(7,4) == F(1,8) <= one_sided_bound == F(1,4)

# A wired-diameter substitution is invalid already in the old cycle:
# the interface collapses to one vertex, giving diameter zero but D>0.
assert F((4-1)**2,2*(4+1)) == F(9,10) > 0

summary = {'earlier_family_cases':count,'earlier_positive_corrections':positive,
           'earlier_cycles':cycle_rows,'weighted_star_cases':weighted_count,
           'weighted_strict_inequalities':strict_count,
           'multilayer_strip_cases':multilayer_count,'sharpness_family':sharp_rows,
           'disconnected_full_R':str(rr),'disconnected_D':str(rr-F(7,4)),
           'disconnected_one_sided_bound':str(one_sided_bound),
           'effective_nice':os.getpriority(os.PRIO_PROCESS,0),
           'OMP_NUM_THREADS':os.environ['OMP_NUM_THREADS'],
           'peak_RSS_bytes_macOS':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
           'elapsed_seconds':round(time.monotonic()-START,4),
           'result':'all exact checks passed'}
assert summary['peak_RSS_bytes_macOS'] < 1024**3
(ROOT/'matching_results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
