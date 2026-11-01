#!/usr/bin/env python3
"""B17 FEI harmonic-root hypercontractive checks.

Checks only the finite/numerical claims in REPORT.md. The universal inequalities
in the report are proved analytically; finite checks are not used as proofs.
"""
from __future__ import annotations
import hashlib, json, math
import numpy as np

CROOT = 2 / math.log(2) * (1 + 1/(2*math.e))
EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
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

def fwht(a):
    a=np.array(a,dtype=np.int64,copy=True)
    n=len(a); h=1
    while h<n:
        a=a.reshape(-1,2*h)
        x=a[:,:h].copy(); y=a[:,h:].copy()
        a[:,:h]=x+y; a[:,h:]=x-y
        a=a.reshape(n); h*=2
    return a

def root_data(vals):
    N=len(vals); n=(N.bit_length()-1)
    W=fwht(vals)
    mu=(W.astype(np.float64)/N)**2
    ks=np.fromiter((s.bit_count() for s in range(N)),dtype=np.int16,count=N)
    I=float(np.sum(mu*ks)); V=float(1-mu[0])
    idx=np.arange(N)
    p=[]; v=[]
    for i in range(n):
        bit=((idx>>i)&1).astype(bool)
        p_i=float(np.sum(mu[bit]))
        sel=bit & (ks>0)
        v_i=float(np.sum(mu[sel]/ks[sel]))
        p.append(p_i); v.append(v_i)
    if V>0:
        q=[x/V for x in v if x>0]
        root_ent=V*(-sum(x*math.log2(x) for x in q))
    else:
        root_ent=0.0
    return {"I":I,"V":V,"p":p,"v":v,"root_entropy_weighted":root_ent,
            "root_entropy_over_I":root_ent/I if I else 0.0}

def simple_cap(p):
    if p<=0: return 0.0
    if p>=1: return 1.0
    L=math.log(1/p)
    return min(p, 2*p*(1-p)/L)

def exhaustive_small():
    rows={}
    for n in range(1,5):
        N=1<<n
        max_ratio=0.0
        min_cap_slack=float("inf")
        count=1<<(N-1)  # global negation fixed at x=0
        for mask in range(count):
            vals=np.ones(N,dtype=np.int64)
            for x in range(1,N):
                if (mask>>(x-1))&1: vals[x]=-1
            d=root_data(vals)
            if d["I"]>0:
                max_ratio=max(max_ratio,d["root_entropy_over_I"])
            for p,v in zip(d["p"],d["v"]):
                if p>0:
                    min_cap_slack=min(min_cap_slack,simple_cap(p)-v)
        rows[str(n)]={"functions_mod_global_negation":count,
                      "max_weighted_root_entropy_over_I":max_ratio,
                      "min_simple_cap_minus_v":min_cap_slack if min_cap_slack<float("inf") else None}
    return rows

def make_numaro():
    base=int("".join(SLICES[0]),16)
    masks=[int("".join(row),16)^base for row in SLICES[1:]]
    assert all((m & base)==0 and m.bit_count()==2 for m in masks)
    hosts=[[x for x in range(512) if (m>>x)&1] for m in masks]
    core=np.array([-1 if (base>>x)&1 else 1 for x in range(512)],dtype=np.int64)
    tab=np.tile(core,(1<<len(hosts),1))
    for j,cells in enumerate(hosts):
        mask=(np.arange(1<<len(hosts)) & (1<<j))!=0
        tab[np.ix_(mask,np.array(cells,dtype=int))]=-1
    tab=tab.ravel()
    digest=hashlib.sha256(",".join(map(str,tab)).encode()).hexdigest()
    assert digest==EXPECTED_SHA and int(tab.sum())==0
    return tab

def second_derivative_boundary():
    # f=-1 at 00 and +1 elsewhere.
    f=np.array([-1.0,1.0,1.0,1.0])
    g=f.copy()
    for i in (0,1):
        g=np.array([(g[x]-g[x^(1<<i)])/2 for x in range(4)])
    p=float(np.mean(g*g))
    support=float(np.mean(g!=0))
    q=1.5
    lq2=float(np.mean(np.abs(g)**q)**(2/q))
    naive=p**(2/q)
    quantized=(4*p)**(2/q-1)*p
    return {"D12_values":g.tolist(),"p":p,"support":support,"q":q,
            "Lq_squared":lq2,"naive_p_power":naive,
            "quantization_corrected_bound":quantized,
            "naive_extension_fails":lq2>naive+1e-12,
            "corrected_bound_tight":abs(lq2-quantized)<1e-12}

def main():
    small=exhaustive_small()
    tab=make_numaro()
    nd=root_data(tab)
    ncap=[simple_cap(p)-v for p,v in zip(nd["p"],nd["v"])]
    out={
      "CROOT":CROOT,
      "exhaustive_small":small,
      "numaro":{
        "truth_table_sha256":EXPECTED_SHA,
        "I":nd["I"],
        "V":nd["V"],
        "weighted_root_entropy":nd["root_entropy_weighted"],
        "weighted_root_entropy_over_I":nd["root_entropy_over_I"],
        "min_simple_cap_minus_v":min(ncap),
        "coordinate_p":nd["p"],
        "coordinate_v":nd["v"],
      },
      "second_derivative_boundary":second_derivative_boundary(),
      "all_checks_pass": (
          all(r["min_simple_cap_minus_v"] is None or r["min_simple_cap_minus_v"]>=-1e-12 for r in small.values())
          and nd["root_entropy_weighted"] <= CROOT*nd["I"]+1e-12
          and min(ncap)>=-1e-12
          and second_derivative_boundary()["naive_extension_fails"]
          and second_derivative_boundary()["corrected_bound_tight"]
      )
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
