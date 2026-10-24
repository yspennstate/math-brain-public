"""Reproducible self-check of X003's exact block formula and quartic term.

This is not a proof of an entropy inequality. Seeded small probes only test
the proposed stronger full-output inequality before further analytic work.
"""
from pathlib import Path
import json
import numpy as np


def atoms(K):
    n = len(K)
    eye = np.eye(n)
    out = np.empty(1 << n)
    for mask in range(1 << n):
        take = np.array([(mask >> j) & 1 for j in range(n)], dtype=bool)
        M = np.where(take[None, :], K, eye - K)
        z = np.linalg.det(M)
        assert abs(z.imag) < 1e-9
        out[mask] = z.real
    assert out.min() > -1e-10
    assert abs(out.sum() - 1) < 1e-8
    return out


def entropy(p):
    p = p[p > 1e-14]
    return float(-p @ np.log(p))


def splitter(K0, K1, t=0.5):
    C = (1-t)*K0+t*K1
    D = t*K0+(1-t)*K1
    E = np.sqrt(t*(1-t))*(K1-K0)
    return np.block([[C,E],[E,D]])


def main():
    K = np.array([[.41,.13+.06j,.04-.03j],
                  [.13-.06j,.54,-.07+.04j],
                  [.04+.03j,-.07-.04j,.36]])
    A = np.array([[.21,.07-.03j,-.05+.02j],
                  [.07+.03j,-.13,.04+.06j],
                  [-.05-.02j,.04-.06j,.09]])
    p = atoms(K)
    n = len(K)
    G = [np.linalg.inv(K-np.diag([not ((s >> i)&1) for i in range(n)]))
         for s in range(1 << n)]
    r = np.array([[-np.trace(g@A@h@A).real for h in G] for g in G])
    coefficient = float(np.sum(p[:,None]*p[None,:]*r*r)/2)
    base = p[:,None]*p[None,:]
    rows = []
    for eps in [.2,.1,.05,.025]:
        B = np.block([[K,eps*A],[eps*A,K]])
        # First register's mask is the low-order index.
        q = atoms(B).reshape((1 << n,1 << n)).T
        formula = np.array([[p[s]*p[t]*np.linalg.det(
            np.eye(n)-eps**2*G[s]@A@G[t]@A).real
            for t in range(1 << n)] for s in range(1 << n)])
        mi = float(np.sum(q*np.log(q/base)))
        rows.append(dict(epsilon=eps,formula_error=float(np.max(abs(formula-q))),
                         mutual_information=mi,mi_over_epsilon4=mi/eps**4))
    # Small bounded probe, used only to distinguish a promising bridge from
    # an immediately false stronger statement.
    rng = np.random.default_rng(20260915003)
    probes = []
    for dim, count in [(2,60),(3,40),(4,12)]:
        worst = (1e9,None)
        for rep in range(count):
            mats=[]
            for _ in range(2):
                Z=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
                U,_=np.linalg.qr(Z)
                vals=rng.uniform(.01,.99,size=dim)
                mats.append((U*vals)@U.conj().T)
            K0,K1=mats
            q=atoms(splitter(K0,K1))
            delta=entropy(q)-entropy(atoms(K0))-entropy(atoms(K1))
            if delta<worst[0]:
                worst=(delta,rep)
        probes.append(dict(dimension=dim,count=count,minimum_full_output_gain=worst[0],index=worst[1]))
    result=dict(quartic_coefficient=coefficient,checks=rows,bounded_probes=probes)
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('check-results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
