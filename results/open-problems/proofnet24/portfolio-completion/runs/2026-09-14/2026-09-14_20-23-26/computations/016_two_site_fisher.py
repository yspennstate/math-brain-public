#!/usr/bin/env python3
"""Deterministic checks for agent 016's analytic two-site entropy proof.

This is a consistency check, not a numerical proof.  Atom identities and
derivatives are checked exactly with Fraction; the explicit endpoint minimizer
is checked with ordinary floating-point complex 2-by-2 matrix arithmetic.
There are no randomized searches and no third-party dependencies.
"""

from fractions import Fraction as F
import json
import math
from pathlib import Path


def atoms(k):
    a, b, cr, ci = k
    r = cr * cr + ci * ci
    return ((1-a)*(1-b)-r, a*(1-b)+r, (1-a)*b+r, a*b-r)


def differential(k, d):
    a, b, cr, ci = k
    u, s, vr, vi = d
    dr = 2*(cr*vr + ci*vi)
    delta = u*s-vr*vr-vi*vi
    dp = (-(1-b)*u-(1-a)*s-dr,
          (1-b)*u-a*s+dr,
          -b*u+(1-a)*s+dr,
          b*u+a*s-dr)
    ddp = (2*delta, -2*delta, -2*delta, 2*delta)
    return dp, ddp, delta


def mat(k):
    a, b, cr, ci = map(float, k)
    c = complex(cr, ci)
    return [[complex(a), c], [c.conjugate(), complex(b)]]


def det(a):
    return (a[0][0]*a[1][1]-a[0][1]*a[1][0]).real


def adj(a):
    return [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]]


def add(a, b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]


def scale(a, t):
    return [[t*a[i][j] for j in range(2)] for i in range(2)]


def trace_product(a, b):
    val = sum(a[i][j]*b[j][i] for i in range(2) for j in range(2))
    assert abs(val.imag) < 1e-10
    return val.real


def check(name, k, d):
    p = atoms(k)
    x, y, z, w = p
    assert all(q > 0 for q in p)
    assert 0 < k[0] < 1 and 0 < k[1] < 1
    assert sum(p) == 1
    assert y*z-x*w == k[2]*k[2]+k[3]*k[3]
    dp, ddp, delta = differential(k, d)
    h = F(1, 10000)
    pp = atoms(tuple(ki+h*di for ki, di in zip(k, d)))
    pm = atoms(tuple(ki-h*di for ki, di in zip(k, d)))
    assert tuple((pp[i]-pm[i])/(2*h) for i in range(4)) == dp
    assert tuple((pp[i]-2*p[i]+pm[i])/(h*h) for i in range(4)) == ddp
    assert sum(dp) == 0 and sum(ddp) == 0
    fisher = sum(q*q/pi for q, pi in zip(dp, p))
    endpoint = dp[0]*dp[0]/x+dp[3]*dp[3]/w
    ell = math.log(float(y*z/(x*w)))
    hessian = -float(fisher)+2*float(delta)*ell
    assert hessian <= 1e-10
    t = float(y+z)/(2*math.sqrt(float(x*w)))
    endpoint_minimum = 4*(1+t)
    assert t >= 1-1e-12
    assert ell <= 2*math.log(t)+1e-12
    assert 4*(1+t-math.log(t)) >= 8-1e-12
    if delta > 0:
        assert d[0] > 0
        assert float(endpoint) >= float(delta)*endpoint_minimum-1e-10
        assert hessian <= -8*float(delta)+1e-10

    # Independently construct the analytic minimizer of the two-atom objective.
    km = mat(k)
    identity = [[1+0j, 0j], [0j, 1+0j]]
    complement = add(identity, scale(km, -1))
    a = scale(adj(km), 1/math.sqrt(float(w)))
    b = scale(adj(complement), 1/math.sqrt(float(x)))
    c = add(a, b)
    dc = det(c)
    dstar = scale(adj(c), 1/math.sqrt(dc))
    qa = trace_product(a, dstar)
    qb = trace_product(b, dstar)
    min_value = qa*qa+qb*qb
    assert abs(det(a)-1) < 1e-10
    assert abs(det(b)-1) < 1e-10
    assert abs(dc-(2+float(y+z)/math.sqrt(float(x*w)))) < 1e-10
    assert abs(det(dstar)-1) < 1e-10
    assert abs(qa-qb) < 1e-10
    assert abs(min_value-endpoint_minimum) < 1e-9
    return {
        "name": name,
        "exact_probabilities": list(map(str, p)),
        "exact_first_derivatives": list(map(str, dp)),
        "exact_det_direction": str(delta),
        "exact_fisher": str(fisher),
        "exact_endpoint_fisher": str(endpoint),
        "log_odds": ell,
        "hessian": hessian,
        "endpoint_minimum_at_det_one": endpoint_minimum,
        "constructed_minimizer_error": abs(min_value-endpoint_minimum),
    }


examples = [
    ("uniform_sharp", (F(1,2), F(1,2), F(0), F(0)),
     (F(1), F(1), F(0), F(0))),
    ("symmetric_real", (F(1,2), F(1,2), F(1,4), F(0)),
     (F(1), F(1), F(0), F(0))),
    ("complex_transverse", (F(1,2), F(1,2), F(9,50), F(12,50)),
     (F(5,4), F(5,4), F(-12,20), F(9,20))),
    ("asymmetric_complex", (F(1,3), F(3,5), F(1,10), F(1,5)),
     (F(5,4), F(5,4), F(3,5), F(9,20))),
    ("near_empty", (F(1,100), F(1,50), F(1,200), F(1,400)),
     (F(2), F(1,2), F(0), F(0))),
    ("indefinite_complex", (F(1,3), F(3,5), F(1,10), F(1,5)),
     (F(1), F(-1), F(1,3), F(1,4))),
    ("rank_one_complex", (F(1,3), F(3,5), F(1,10), F(1,5)),
     (F(1), F(1), F(3,5), F(4,5))),
    ("diagonal_pure_transverse", (F(1,2), F(1,2), F(0), F(0)),
     (F(0), F(0), F(0), F(1))),
]

if __name__ == "__main__":
    result = {
        "method": "exact Fraction atom checks and deterministic minimizer checks",
        "random_trials": 0,
        "proof_dependency": "The analytic proof in agents/016.md is independent of this script.",
        "examples": [check(*item) for item in examples],
    }
    target = Path(__file__).with_name("016_two_site_fisher_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
