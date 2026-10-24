#!/usr/bin/env python3
"""
Width-two tribes erasure-selector stress test for FEI.

This is a targeted calculation, not an FEI proof.  It derives and checks the
closed form for B_i/p_i and the exact restriction decrement Delta_i H/p_i for
the symmetric width-two tribes family.
"""
from __future__ import annotations
import json
import math

def h2(t: float) -> float:
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return -t * math.log2(t) - (1.0-t) * math.log2(1.0-t)

def psi(t: float) -> float:
    if t <= 0.0 or t >= 1.0:
        return 0.0
    return h2(t) + 1.0 - h2(0.5 + math.sqrt(t*(1.0-t)))

def fibre_entropy(x: float, y: float) -> float:
    m=x+y
    if m == 0.0:
        return 0.0
    return m*h2(y/m)

def fibre_decrement(x: float, y: float) -> float:
    m=x+y
    if m == 0.0:
        return 0.0
    return m*psi(y/m)

A_B=(10.0/9.0)*h2(0.1)
A_D=(10.0/9.0)*psi(0.1)
C_HOD=6.4547837
CSTAR=2.0/math.log(2.0)
K_HOD=C_HOD-CSTAR

def formula(s: int) -> dict:
    p=0.5*(0.75**(s-1))
    lower_generic=4.5*p - 9.0*p*p
    q_empty=(1.0-3.0*p)**2
    q_single=p*p
    B=p + A_B*lower_generic + fibre_entropy(q_empty,q_single)
    D=2.0*p + A_D*lower_generic + fibre_decrement(q_empty,q_single)
    return {
        "s": s,
        "n": 2*s,
        "p": p,
        "B_over_p": B/p,
        "Delta_over_p": D/p,
        "JS_over_p": (D-B)/p,
    }

def fwht(a):
    a=list(map(float,a))
    h=1
    n=len(a)
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=a[j]; y=a[j+h]
                a[j]=x+y
                a[j+h]=x-y
        h*=2
    return a

def tribes_values(s: int):
    n=2*s
    vals=[]
    for x in range(1<<n):
        out=False
        for b in range(s):
            if ((x>>(2*b))&3)==3:
                out=True
                break
        vals.append(-1.0 if out else 1.0)
    return vals

def brute_one_coordinate(s: int, i: int=0) -> dict:
    n=2*s
    vals=tribes_values(s)
    N=1<<n
    a=[v/N for v in fwht(vals)]
    bit=1<<i
    p=0.0; B=0.0; D=0.0
    for S in range(N):
        if S & bit:
            p += a[S]*a[S]
        else:
            x=a[S]*a[S]
            y=a[S|bit]*a[S|bit]
            B += fibre_entropy(x,y)
            D += fibre_decrement(x,y)
    return {"p":p,"B_over_p":B/p,"Delta_over_p":D/p,"JS_over_p":(D-B)/p}

def tau_for_C(C: float) -> float:
    lo=1e-15; hi=0.5
    for _ in range(120):
        mid=(lo+hi)/2.0
        if psi(mid)/mid > C:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

rows=[]
max_abs_error=0.0
for s in range(2,9):
    f=formula(s)
    b=brute_one_coordinate(s)
    err=max(abs(f[k]-b[k]) for k in ("p","B_over_p","Delta_over_p","JS_over_p"))
    max_abs_error=max(max_abs_error,err)
    f["brute_max_abs_error"]=err
    rows.append(f)

all_formula=[formula(s) for s in range(2,101)]
max_row=max(all_formula,key=lambda r:r["B_over_p"])
r8=formula(8)
tau=tau_for_C(C_HOD)
out={
    "status":"PASS_FOR_STATED_TARGETED_CALCULATION",
    "full_fei_proved":False,
    "family":"width-two tribes",
    "closed_form":{
        "p_s":"(1/2)*(3/4)^(s-1)",
        "A_B":"(10/9)*h2(1/10)",
        "B_i":"p + A_B*(9p/2-9p^2) + F((1-3p)^2,p^2)",
        "F(x,y)":"(x+y) h2(y/(x+y))",
        "A_D":"(10/9)*Psi(1/10)",
        "Delta_i_H":"2p + A_D*(9p/2-9p^2) + G((1-3p)^2,p^2)",
        "G(x,y)":"(x+y) Psi(y/(x+y))",
    },
    "constants":{
        "C_hod_scale":C_HOD,
        "c_star_2_over_ln2":CSTAR,
        "erasure_threshold_C_minus_cstar":K_HOD,
        "tau_C":tau,
    },
    "s8":{
        **r8,
        "p_below_tau":r8["p"]<tau,
        "erasure_threshold_violation":r8["B_over_p"]-K_HOD,
        "direct_payment_slack":C_HOD-r8["Delta_over_p"],
        "universal_JS_surcharge_waste":CSTAR-r8["JS_over_p"],
        "compiler_constant_if_using_B_plus_cstar":r8["B_over_p"]+CSTAR,
        "quadratic_rebate_surcharge":CSTAR*(1.0-r8["p"]/3.0),
        "compiler_constant_with_quadratic_rebate":r8["B_over_p"]+CSTAR*(1.0-r8["p"]/3.0),
        "quadratic_rebate_hod_margin":C_HOD-(r8["B_over_p"]+CSTAR*(1.0-r8["p"]/3.0)),
    },
    "formula_vs_bruteforce_s2_through_s8":rows,
    "max_formula_bruteforce_abs_error":max_abs_error,
    "max_B_over_p_among_s2_through_s100":max_row,
    "quadratic_rebate":{
        "pointwise_statement":"j(t) <= (2/ln2)*(t-t^2/3) for 0<=t<=1/2",
        "marginal_statement":"JS_i <= (2/ln2)*(j_i-j_i^2/3), j_i=min(p_i,1-p_i)",
        "hod_moving_erasure_threshold":"B_i/p_i <= C_hod-2/ln2 + (2/(3ln2))*p_i for p_i<=1/2",
        "minimum_margin_width2_tribes_s5_through_s100":min(
            K_HOD+(CSTAR/3.0)*r["p"]-r["B_over_p"] for r in all_formula if r["s"]>=5
        ),
        "minimum_margin_attained_s":min(
            (r for r in all_formula if r["s"]>=5),
            key=lambda r: K_HOD+(CSTAR/3.0)*r["p"]-r["B_over_p"]
        )["s"],
    },
}
assert max_abs_error < 1e-9
assert r8["p"] < tau
assert r8["B_over_p"] > K_HOD
assert r8["Delta_over_p"] < C_HOD
print(json.dumps(out,indent=2,sort_keys=True))
