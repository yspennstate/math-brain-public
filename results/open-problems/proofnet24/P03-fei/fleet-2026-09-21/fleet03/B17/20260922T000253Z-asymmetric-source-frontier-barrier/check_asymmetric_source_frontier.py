#!/usr/bin/env python3
"""Targeted checker for the B17 asymmetric slab-plus-outlier FEI adversary.

This is not an exhaustive FEI search.  It checks the exact closed formulas against
truth-table definitions on small parameter pairs, then evaluates the analytic
family at larger parameters to expose the source-frontier coefficient barrier.
"""
from __future__ import annotations
from fractions import Fraction
import json, math


def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x) - (1-x)*math.log2(1-x)


def phi(x: float) -> float:
    return 0.0 if x <= 0.0 else x*math.log2(1.0/x)


def formulas(r: int, k: int) -> dict:
    q = 2.0**(-r)
    delta = 2.0**(-k)
    eps = q*delta
    j_minus = 2*q*(1-delta)
    j_plus = 2*q*(1+delta)
    j_tail = 2*q*delta
    J = j_minus + (r-1)*j_plus + k*j_tail

    Dminus = 0.5*(k*delta/(1-delta) + math.log2(1-delta))
    Dplus = 0.5*((k-2)*delta/(1+delta) + math.log2(1+delta))
    defect = j_minus*Dminus + (r-1)*j_plus*Dplus

    w0 = (1-2*q-2*eps)**2
    wplus = 4*(q+eps)**2
    wminus = 4*(q-eps)**2
    wsmall = 4*eps**2
    H = (phi(w0)
         +(2**(r-1)-1)*phi(wplus)
         +(2**(r-1))*phi(wminus)
         +(2**r)*(2**k-1)*phi(wsmall))

    B_source = H - h2(j_tail)
    I_source = J - j_tail

    m = 2**(r-1)
    M0 = w0 + (m-1)*wplus
    c0 = 0.0
    if w0:
        c0 += w0*math.log2(M0/w0)
    if wplus:
        c0 += (m-1)*wplus*math.log2(M0/wplus)
    M1 = m*wminus
    My = (2**r)*(2**k-1)*wsmall
    B_gate = c0 + (M1+My)*(r-1)
    I_gate = (r-1)*j_plus

    R_gate = 4*k*q*delta
    crossing_fraction_lb = 1.0 - R_gate/(2*j_minus)

    return {
        "r": r, "k": k, "q": q, "delta": delta,
        "j_minus": j_minus, "j_plus": j_plus, "j_tail": j_tail,
        "J": J, "global_defect": defect,
        "Delta_minus": Dminus, "Delta_plus": Dplus,
        "H": H,
        "source_B": B_source, "source_I": I_source,
        "source_B_over_J": B_source/J,
        "source_rate": B_source/I_source,
        "defect_over_J": defect/J,
        "gate_B": B_gate, "gate_I": I_gate,
        "gate_rate": B_gate/I_gate,
        "gate_crossing_fraction_lb": crossing_fraction_lb,
    }


def table_value(idx: int, r: int, k: int) -> int:
    z = idx & ((1<<r)-1)
    y = (idx >> r) & ((1<<k)-1)
    return -1 if (z == 0 or (z == 1 and y == 0)) else 1


def derivative_row(r: int, k: int, i: int):
    n = r+k
    others = [j for j in range(n) if j != i]
    vals=[]
    for u in range(1<<(n-1)):
        a=0
        for b,j in enumerate(others):
            if (u>>b)&1:
                a |= 1<<j
        b=a | (1<<i)
        vals.append((table_value(a,r,k)-table_value(b,r,k))//2)
    return vals


def exact_j_d(r: int, k: int, i: int):
    n=r+k
    g=derivative_row(r,k,i)
    m=len(g)
    j=Fraction(sum(v!=0 for v in g),m)
    d=Fraction(0,1)
    for t in range(n-1):
        s=0
        for u in range(1<<(n-2)):
            low = ((u >> t) << (t+1)) | (u & ((1<<t)-1))
            high = low | (1<<t)
            diff = g[low]-g[high]
            s += diff*diff
        d += Fraction(s,4*(1<<(n-2)))
    return j,d


def verify_small() -> list[dict]:
    rows=[]
    for r,k in [(3,4),(4,4),(4,5)]:
        F=formulas(r,k)
        q=Fraction(1,1<<r); delta=Fraction(1,1<<k)
        targets=[0, 1 if r>1 else 0, r]
        exact=[]
        for i in targets:
            j,d=exact_j_d(r,k,i)
            if i==0:
                jf=2*q*(1-delta)
                df=j*(Fraction(r-1,2)+Fraction(k,2)*delta/(1-delta))
            elif i<r:
                jf=2*q*(1+delta)
                df=j*(Fraction(r-1,2)+Fraction(k-2,2)*delta/(1+delta))
            else:
                jf=2*q*delta
                df=j*Fraction(r+k-1,2)
            assert j==jf, (r,k,i,j,jf)
            assert d==df, (r,k,i,d,df)
            exact.append({"coord":i,"j":str(j),"d":str(d)})
        rows.append({"r":r,"k":k,"exact_rows":exact,
                     "source_rate":F["source_rate"],
                     "gate_rate":F["gate_rate"]})
    return rows


def main():
    small=verify_small()
    large=[]
    for r,k in [(8,10),(8,24),(12,24),(16,24),(24,32),(32,40)]:
        large.append(formulas(r,k))
    out={
        "status":"PASS",
        "small_exact_formula_checks":small,
        "asymptotic_samples":[{
            "r":x["r"],"k":x["k"],
            "source_B_over_J":x["source_B_over_J"],
            "source_rate":x["source_rate"],
            "defect_over_J":x["defect_over_J"],
            "Delta_minus":x["Delta_minus"],
            "Delta_plus":x["Delta_plus"],
            "gate_rate":x["gate_rate"],
            "gate_crossing_fraction_lb":x["gate_crossing_fraction_lb"],
        } for x in large],
        "interpretation": {
            "source_frontier_barrier":"source B/J tends to 4 while global defect/J tends to 0",
            "promoted_gate_replacement":"gate-block Shannon rate tends to 3 and crossing fraction tends to 1"
        }
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
