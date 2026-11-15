"""Exact box Bernstein arithmetic. Discovery lives in discover.py, not here.

All signs returned by this module use Python integers and Fraction. NumPy's
object arrays only arrange exact integer additions/multiplications.
"""
import sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import comb, lcm, prod
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE / 'STRAT10'))
from zero_face import construct
from centered_bounds import translate


@lru_cache(None)
def data():
    rr, t, V, R, M, delta, Q, tau, D, edges, P, num = construct()
    q = rr.gens[-1]
    z = rr.gens[5]
    polys = {
        'orientation': t*t-1-z*z,
        'order12': V[1][0]-V[0][0],
        'order23': V[2][0]-V[1][0],
        'x3bound': V[2][0]+1,
    }
    for i in range(5):
        polys['row'+str(i)] = 4*t-R[i][i]
    for (i,j), g in edges.items():
        if (i,j) != (3,4):
            polys['g'+str(i)+str(j)] = g
    polys.update(spectral00=5*t-M[0][0], spectral11=5*t-M[1][1],
                 connected=25*t*t-5*t*tau+delta, rank=delta,
                 ratio=529*delta-60*tau*tau)
    # Residual endpoint scale a>14/25. With X=(14/25)D-tau,
    # X>=0 implies H-X^2>0. When the box has X<0 anywhere this
    # conditional constraint is omitted, rather than assumed globally.
    X = 14*D-25*tau
    H = tau*tau-4*delta
    polys['scale14'] = 625*H-X*X
    polys['scale_guard'] = X
    def dic(p):
        out = {}
        for mon,c in p.terms():
            assert not mon[-1] and c.denominator == 1
            out[mon[:6]] = int(c)
        return out
    target = dic(num.subs(q,0))
    assert all(c % 8 == 0 for c in target.values())
    target = {m:c//8 for m,c in target.items()}
    return target, {key:dic(p) for key,p in polys.items()}


def degree(poly):
    return tuple(max((m[i] for m in poly), default=0) for i in range(6))


def normal(poly, box):
    """Integer numerator of P(center+halfwidth*y), with positive denominator."""
    if not poly:
        return {}, 1
    c = [(a+b)/2 for a,b in box]
    h = [(b-a)/2 for a,b in box]
    s = lcm(*(x.denominator for x in c+h))
    tr, d = translate(poly, [int(x*s) for x in c], s)
    powers = [[int(x*s)**k for k in range(max(degree(poly))+1)] for x in h]
    out = {}
    for m,a in tr.items():
        v = a*prod(powers[i][k] for i,k in enumerate(m))
        if v:
            out[m] = v
    return out, s**d


@lru_cache(None)
def conversion(n):
    """Integer matrix for y^k -> Bernstein_n((y+1)/2)."""
    s = lcm(*(comb(n,j) for j in range(n+1)))
    a = []
    for i in range(n+1):
        row = []
        for k in range(n+1):
            val = sum(F(comb(k,j)*2**j*(-1)**(k-j)*comb(i,j),comb(n,j))
                      for j in range(min(i,k)+1))
            assert (val*s).denominator == 1
            row.append(int(val*s))
        a.append(row)
    return s, tuple(map(tuple,a))


def controls(normalized, degrees, exact=True):
    """Return tensor controls and their common positive integer denominator."""
    a = np.zeros(tuple(n+1 for n in degrees), dtype=object if exact else float)
    for m,c in normalized.items():
        a[m] = c if exact else float(c)
    denom = 1
    for axis,n in enumerate(degrees):
        s, rows = conversion(n)
        mat = np.array(rows, dtype=object if exact else float)
        if not exact:
            mat /= s
        else:
            denom *= s
        a = np.moveaxis(np.tensordot(mat, a, axes=(1,axis)), 0, axis)
    return a, denom


def bernstein_min(poly, box, degrees=None):
    degrees = degree(poly) if degrees is None else tuple(degrees)
    assert all(x<=y for x,y in zip(degree(poly),degrees))
    tr,denom = normal(poly,box)
    # Every coefficient of y^k in any elevated Bernstein basis has |b|<=1:
    # it is the average of products of k numbers in {-1,1} (blossoming).
    # This fast sufficient check still proves every tensor coefficient.
    c0 = tr.get((0,)*6,0)
    simple = c0-sum(abs(c) for m,c in tr.items() if any(m))
    if simple > 0:
        return F(simple,denom), 'absolute-envelope'
    a, scale = controls(tr,degrees)
    return F(int(a.min()),denom*scale), 'full-tensor'


def active_constraints(box):
    target, gs = data()
    out = {k:p for k,p in gs.items() if k not in ('scale14','scale_guard')}
    tr,denom = normal(gs['scale_guard'],box)
    lo = tr.get((0,)*6,0)-sum(abs(v) for m,v in tr.items() if any(m))
    if lo >= 0:
        out['scale14'] = gs['scale14']
    return out


def residual(box, kind, weights):
    target, _ = data()
    gs = active_constraints(box)
    assert kind in ('exclusion','positivity')
    weights = {k:F(v) for k,v in weights.items()}
    assert all(v>=0 for v in weights.values())
    terms = []
    for key,v in weights.items():
        names = key.split('*')
        assert len(names) in (1,2) and all(k in gs for k in names)
        p = gs[names[0]]
        if len(names) == 2:
            p = multiply(p,gs[names[1]])
        terms.append((p,v))
    scale = lcm(*(v.denominator for p,v in terms)) if terms else 1
    out = {m:c*scale for m,c in target.items()} if kind=='positivity' else {}
    for p,v in terms:
        k = int(v*scale)
        for m,c in p.items():
            out[m] = out.get(m,0)-k*c
    # Both kinds are checked as a strictly POSITIVE polynomial:
    # -sum lambda*g for exclusion, T-sum lambda*g for positivity.
    return {m:c for m,c in out.items() if c}, scale


def multiply(a,b):
    out = {}
    for m,c in a.items():
        for n,d in b.items():
            key = tuple(x+y for x,y in zip(m,n))
            out[key] = out.get(key,0)+c*d
    return {m:c for m,c in out.items() if c}


def verify_certificate(record):
    box = [tuple(map(F,x)) for x in record['box']]
    assert len(box)==6 and all(a<b for a,b in box)
    p,scale = residual(box,record['kind'],record['lambda'])
    lo,method = bernstein_min(p,box,record.get('bernstein_degrees'))
    assert lo>0, (record['kind'],record.get('node'),lo)
    return lo/scale,method


def volume(box):
    return prod(F(b)-F(a) for a,b in box)
