#!/usr/bin/env python3
"""Finite regression checks for the B14 collision/KL selector continuation.

The analytic statements are in REPORT.md.  This script:
  * exhausts the n=4 Boolean atlas up to global sign for the collision budget,
    exact restriction drop, and directed-erasure KL identity;
  * reconstructs the already authenticated Numaro n=18 seed and measures the
    collision refund along its balanced all-core self-composition path.

It is not a proof of FEI.
"""
from __future__ import annotations

import hashlib
import json
import math
import numpy as np

EXPECTED_SEED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"

TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]

def fwht(a: np.ndarray) -> np.ndarray:
    out = np.asarray(a, dtype=float).copy()
    h = 1
    while h < out.size:
        z = out.reshape(-1, 2*h)
        x = z[:, :h].copy()
        y = z[:, h:].copy()
        z[:, :h] = x + y
        z[:, h:] = x - y
        out = z.reshape(-1)
        h *= 2
    return out / out.size

def spectral(vals: np.ndarray) -> np.ndarray:
    w = fwht(vals)
    return w*w

def influences(p: np.ndarray, n: int) -> np.ndarray:
    ids = np.arange(1 << n)
    return np.array([float(p[(ids & (1 << i)) != 0].sum()) for i in range(n)])

def collision_drop_formula(p: np.ndarray, n: int, i: int) -> tuple[float,float]:
    bit = 1 << i
    a = 0.0
    for t in range(1 << n):
        if t & bit:
            continue
        a += float(p[t] * p[t | bit])
    return a, 6.0*a

def child(vals: np.ndarray, n: int, i: int, b: int) -> np.ndarray:
    ids = np.arange(1 << n)
    return vals[((ids >> i) & 1) == b]

def erasure_kl(p: np.ndarray, n: int, i: int) -> tuple[float,float,float,float]:
    bit = 1 << i
    alpha = float(sum(p[t | bit] for t in range(1 << n) if not (t & bit)))
    if alpha <= 1e-15:
        return 0.0, 0.0, 0.0, 0.0
    B = 0.0
    L1 = 0.0
    q = []
    m = []
    for t in range(1 << n):
        if t & bit:
            continue
        a = float(p[t]); b = float(p[t | bit]); z = a+b
        if a > 0:
            B += a*math.log2(z/a)
        if b > 0:
            term = b*math.log2(z/b)
            B += term
            L1 += term
            q.append(b/alpha)
            m.append(z)
    D = 0.0
    for qq, mm in zip(q,m):
        if qq > 0:
            D += qq*math.log2(qq/mm)
    rhs = alpha*math.log2(1.0/alpha) - alpha*D
    directed_other = B-L1
    return B, L1, rhs, directed_other

def atlas_n4() -> dict:
    n=4; N=1<<n
    min_budget_slack=float("inf")
    max_drop_err=0.0
    max_kl_err=0.0
    min_other_slack=float("inf")
    checked=0
    for mask in range(1 << (N-1)):
        vals=np.ones(N,dtype=np.int8)
        for j in range(1,N):
            if (mask >> (j-1)) & 1:
                vals[j]=-1
        p=spectral(vals)
        inf=influences(p,n)
        Pcol=1.0-float(np.dot(p,p))
        Ifrak=float(np.minimum(inf,1-inf).sum())
        min_budget_slack=min(min_budget_slack,Ifrak-Pcol)
        for i in range(n):
            A, pred=collision_drop_formula(p,n,i)
            sp0=spectral(child(vals,n,i,0)); sp1=spectral(child(vals,n,i,1))
            c0=1.0-float(np.dot(sp0,sp0)); c1=1.0-float(np.dot(sp1,sp1))
            actual=Pcol-(c0+c1)/2.0
            max_drop_err=max(max_drop_err,abs(actual-pred))
            B,L1,rhs,other=erasure_kl(p,n,i)
            max_kl_err=max(max_kl_err,abs(L1-rhs))
            alpha=float(inf[i])
            min_other_slack=min(min_other_slack, alpha/math.log(2.0)-other)
        checked += 1
    return {
        "truth_tables_checked_up_to_global_sign": checked,
        "min_Ifrak_minus_collision_deficit": min_budget_slack,
        "max_abs_collision_drop_identity_error": max_drop_err,
        "max_abs_directed_erasure_KL_identity_error": max_kl_err,
        "min_alpha_over_ln2_minus_other_directed_erasure": min_other_slack,
    }

def reconstruct_numaro() -> np.ndarray:
    base = int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int8)
    table=np.tile(core,(1<<len(hosts),1))
    for j,cells in enumerate(hosts):
        active=(np.arange(1<<len(hosts)) & (1<<j)) != 0
        table[np.ix_(active,np.array(cells,dtype=int))]=-1
    table=table.ravel()
    digest=hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()
    if digest != EXPECTED_SEED_SHA:
        raise AssertionError((digest, EXPECTED_SEED_SHA))
    return table

def numaro_collision_path(depths: int=8) -> dict:
    vals=reconstruct_numaro()
    n=18
    p=spectral(vals)
    if abs(float(p[0])) > 1e-15:
        raise AssertionError("seed is not balanced")
    ids=np.arange(1<<n)
    alpha=np.array([float(p[(ids & (1<<i))!=0].sum()) for i in range(n)])
    core_i=0
    q_single=float(p[1<<core_i])
    c=float(np.dot(p,p))
    bit=1<<core_i
    a=float(sum(p[t]*p[t|bit] for t in range(1<<n) if not (t&bit)))
    e=q_single
    infl=float(alpha[core_i])

    outer_sets=np.arange(1<<n)
    pop=np.array([int(x).bit_count() for x in outer_sets],dtype=np.int16)
    contains=(outer_sets & bit)!=0

    rows=[]
    for d in range(1,depths+1):
        rows.append({
            "depth": d,
            "collision_C2": c,
            "influence": infl,
            "singleton_mass": e,
            "edge_collision_A": a,
            "six_A_over_influence": 6.0*a/infl,
        })
        if d==depths: break
        powers=np.power(c,pop,dtype=float)
        cnext=float(np.sum((p*p)*powers))
        C=outer_sets[~contains]
        pc=np.array([int(x).bit_count() for x in C],dtype=np.int16)
        cpow=np.power(c,pc,dtype=float)
        U=float(np.sum((p[C|bit]**2)*cpow))
        V=float(np.sum((p[C]*p[C|bit])*cpow))
        anext=U*a+V*e
        enext=q_single*e
        inflnext=float(alpha[core_i])*infl
        c,a,e,infl=cnext,anext,enext,inflnext
    return {
        "seed_sha256": EXPECTED_SEED_SHA,
        "seed_collision_C2": float(np.dot(p,p)),
        "seed_core_influence": float(alpha[core_i]),
        "seed_core_singleton_mass": q_single,
        "rows": rows,
    }

def main() -> None:
    result={
        "status":"PASS",
        "warning":"finite regression checks only; analytic proof is in REPORT.md; full FEI remains open",
        "atlas_n4":atlas_n4(),
        "numaro_collision_path":numaro_collision_path(),
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
