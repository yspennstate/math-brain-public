"""Deterministic self-check for the region-2 secant vertex lemma.

This is not the FEI certificate.  It tests the new geometric enclosure on arbitrary
piecewise-linear functions (including nonmonotone ones), and tests the exact
margin identity at high precision.
"""
import json
import math
import numpy as np
import mpmath as mp

SEED = 20260921
rng = np.random.default_rng(SEED)
LN2 = math.log(2.0)


def pl_eval(xs, vals, z):
    return np.interp(z, xs, vals)


def secant(xs, vals, x, lam):
    return (pl_eval(xs, vals, x + lam) - pl_eval(xs, vals, x)) / lam


def vertex_range(xs, vals, x0, x1, l0, l1):
    pts = {(x0,l0),(x0,l1),(x1,l0),(x1,l1)}
    for s in xs:
        if s <= x0 + l0 or s >= x1 + l1:
            continue
        for x in (x0,x1):
            l = s - x
            if l0 <= l <= l1:
                pts.add((x,l))
        for l in (l0,l1):
            x = s - l
            if x0 <= x <= x1:
                pts.add((x,l))
    q = [secant(xs, vals, x, l) for x,l in pts]
    return min(q), max(q)


def run():
    nboxes = 20000
    failures = 0
    ratios = []
    for _ in range(nboxes):
        n = int(rng.integers(8,40))
        dx = rng.uniform(.01,.2,n)
        xs = np.concatenate([[1.0], 1 + np.cumsum(dx)])
        slopes = rng.normal(0,6,n)
        vals = np.empty(n+1)
        vals[0] = rng.normal()
        vals[1:] = vals[0] + np.cumsum(slopes*np.diff(xs))
        i = int(rng.integers(0,n-1))
        a,b = sorted(rng.random(2))
        x0 = xs[i] + a*(xs[i+1]-xs[i])
        x1 = xs[i] + b*(xs[i+1]-xs[i])
        if x1-x0 < 1e-10:
            x1 = (x0+xs[i+1])/2
        lmax = min(.8, xs[-1]-x1-1e-8)
        if lmax <= 1e-5:
            continue
        l0 = float(rng.uniform(1e-5,.7*lmax))
        l1 = float(rng.uniform(max(l0+1e-8,.7*lmax),lmax))
        vlo,vhi = vertex_range(xs,vals,x0,x1,l0,l1)
        dense = [secant(xs,vals,x,l)
                 for x in np.linspace(x0,x1,17)
                 for l in np.linspace(l0,l1,19)]
        if min(dense) < vlo-2e-10 or max(dense) > vhi+2e-10:
            failures += 1
        j0 = max(0,np.searchsorted(xs,x0,side="right")-1)
        j1 = min(n-1,np.searchsorted(xs,x1+l1,side="left"))
        crude = slopes[j0:j1+1]
        w0 = crude.max()-crude.min()
        w1 = vhi-vlo
        if w1 > 1e-12:
            ratios.append(w0/w1)

    mp.mp.dps = 80
    hp_err = mp.mpf("0")
    fp_err = 0.0
    for _ in range(2000):
        x = float(rng.uniform(1,10))
        y = float(rng.uniform(1,40))
        X,Y,c = mp.mpf(str(x)),mp.mpf(str(y)),mp.mpf("0.003")
        p = mp.power(2,-X)
        v = mp.power(2,-Y)
        lam = -mp.log(1-v,2)
        lhs = c*((1-p)-(1-p*mp.power(2,-lam)))/v
        rhs = -c*p
        hp_err = max(hp_err,abs(lhs-rhs))
        pf,vf = 2**(-x),2**(-y)
        lf = -math.log2(1-vf)
        direct = .003*((1-pf)-(1-pf*2**(-lf)))/vf
        fp_err = max(fp_err,abs(direct+.003*pf))

    qprime_min = min(2**(-x)*(1-LN2*(x-1))
                     for x in np.linspace(1,2,10001))
    hprime_max = max((v+math.log1p(-v))/(v*v)
                     for v in np.linspace(1e-6,.5,10001))
    out = {
        "seed": SEED,
        "random_pl_boxes": nboxes,
        "dense_points_per_box": 17*19,
        "vertex_containment_failures": failures,
        "crude_slope_width_over_secant_width_median": float(np.median(ratios)),
        "crude_slope_width_over_secant_width_p90": float(np.quantile(ratios,.9)),
        "margin_identity_high_precision_max_error": mp.nstr(hp_err,8),
        "direct_float_margin_cancellation_max_error": fp_err,
        "min_d_dx_[p(x-1)]_on_[1,2]": qprime_min,
        "max_d_dv_[(1-v)ell(v)]_on_[1e-6,1/2]": hprime_max,
    }
    print(json.dumps(out,indent=2))


if __name__ == "__main__":
    run()
