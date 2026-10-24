#!/usr/bin/env python3
"""Self-checks for B13 tensor-amortized layer-incidence theorem.

No external packages. This checker:
1. computes Walsh spectra of small Boolean functions;
2. verifies the exact B13 entropy decomposition;
3. verifies H/I additivity under disjoint products;
4. checks the universal tensor-power sandwich
   m H(f)-1-2 log2(md) <= R_inc(f^(tensor m)) <= m H(f)
   on direct finite examples;
5. evaluates the explicit AND_2 tensor family from its uniform spectrum
   to illustrate R_inc/(I-tau) -> H/I = 2.
Numerical logarithms are self-checks; theorem proofs are analytic in REPORT.md.
"""
from __future__ import annotations
import math
from collections import defaultdict

TOL = 5e-11

def entropy(ps):
    return sum(-p * math.log2(p) for p in ps if p > 0.0)

def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/n for x in a]

def spectral_metrics(vals):
    N = len(vals)
    n = N.bit_length()-1
    assert 1 << n == N
    a = fwht(vals)
    mu = [x*x for x in a]
    ks = [s.bit_count() for s in range(N)]
    H = entropy(mu)
    I = sum(p*k for p,k in zip(mu,ks))
    tau = sum(p for p,k in zip(mu,ks) if k)
    r = [0.0]*n
    lmass = [defaultdict(float) for _ in range(n)]
    rinc = 0.0

    for s,p in enumerate(mu):
        k = ks[s]
        if not k or p == 0.0:
            continue
        for i in range(n):
            if (s >> i) & 1:
                r[i] += p/k
                lmass[i][k-1] += p/k

    Hmarker = entropy([x/tau for x in r if x > 0.0]) if tau else 0.0
    card = 0.0
    for i in range(n):
        if r[i] > 0.0:
            card += r[i] * entropy([x/r[i] for x in lmass[i].values()])

    for k in range(1,n+1):
        inds = [s for s in range(N) if ks[s] == k and mu[s] > 0.0]
        mass = sum(mu[s] for s in inds)
        if mass == 0.0:
            continue
        q = [mu[s]/mass for s in inds]
        Hs = entropy(q)
        endpoint = [0.0]*n
        for s,w in zip(inds,q):
            for i in range(n):
                if (s >> i) & 1:
                    endpoint[i] += w/k
        Hm = entropy(endpoint)
        rinc += mass * (Hs-Hm)

    hflag = entropy([tau,1.0-tau]) if 0.0 < tau < 1.0 else 0.0
    closure = hflag + tau*Hmarker + card + rinc
    return dict(n=n,H=H,I=I,tau=tau,rinc=rinc,hflag=hflag,
                Hmarker=Hmarker,card=card,closure=closure)

def tensor_vals(a,b):
    return [x*y for x in a for y in b]

def tensor_power(vals,m):
    out=[1]
    for _ in range(m):
        out=tensor_vals(out,vals)
    return out

def assert_close(x,y,msg):
    if abs(x-y) > TOL * max(1.0,abs(x),abs(y)):
        raise AssertionError(f"{msg}: {x} != {y}")

def direct_checks():
    funcs = {
        "AND2": [1,1,1,-1],
        "XOR2": [1,-1,-1,1],
        "MAJ3": [1,1,1,-1,1,-1,-1,-1],
        "DEFECT3": [-1,1,1,1,1,1,1,1],
    }
    checks=0
    rows=[]
    for name,v in funcs.items():
        m=spectral_metrics(v)
        assert_close(m["closure"],m["H"],f"decomposition {name}")
        checks += 1

    # Additivity on all pairs of the small named functions.
    for n1,v1 in funcs.items():
        a=spectral_metrics(v1)
        for n2,v2 in funcs.items():
            b=spectral_metrics(v2)
            c=spectral_metrics(tensor_vals(v1,v2))
            assert_close(c["H"],a["H"]+b["H"],f"H additivity {n1} {n2}")
            assert_close(c["I"],a["I"]+b["I"],f"I additivity {n1} {n2}")
            checks += 2

    # Direct tensor-power sandwich where truth tables remain modest.
    for name in ("AND2","MAJ3","DEFECT3"):
        base=funcs[name]
        bm=spectral_metrics(base)
        d=bm["n"]
        maxm=6 if d==2 else 4
        for power in range(1,maxm+1):
            tp=tensor_power(base,power)
            mm=spectral_metrics(tp)
            assert_close(mm["H"],power*bm["H"],f"tensor H {name} {power}")
            assert_close(mm["I"],power*bm["I"],f"tensor I {name} {power}")
            upper=power*bm["H"]
            lower=upper - 1.0 - 2.0*math.log2(power*d)
            if mm["rinc"] > upper + TOL:
                raise AssertionError(f"upper sandwich {name} {power}")
            if mm["rinc"] + TOL < lower:
                raise AssertionError(f"lower sandwich {name} {power}: {mm['rinc']} < {lower}")
            checks += 4
            rows.append((name,power,mm["rinc"],
                         mm["rinc"]/(mm["I"]-mm["tau"]) if mm["I"]>mm["tau"] else float("nan"),
                         lower,upper))
    return checks,rows

def and2_uniform_tensor_ratio(m):
    # AND2 has uniform squared spectrum on F_2^2. Its m-fold product therefore
    # has uniform squared spectrum on F_2^(2m).
    N=2*m
    rinc=0.0
    for k in range(1,N+1):
        c=math.comb(N,k)
        p=c/(2.0**N)
        rinc += p*(math.log2(c)-math.log2(N))
    tau=1.0-2.0**(-N)
    I=float(m)
    return rinc/(I-tau),rinc

if __name__=="__main__":
    checks,rows=direct_checks()
    print(f"direct_checks={checks}")
    print("direct_tensor_rows=name,m,Rinc,Rinc/(I-tau),lower,upper")
    for row in rows:
        print("%s,%d,%.15g,%.15g,%.15g,%.15g"%row)
    print("AND2_uniform_tensor_asymptotic:")
    for m in (10,20,50,100,200,500):
        ratio,r=and2_uniform_tensor_ratio(m)
        print(f"m={m} Rinc={r:.15g} ratio={ratio:.15g}")
    print("PASS")
