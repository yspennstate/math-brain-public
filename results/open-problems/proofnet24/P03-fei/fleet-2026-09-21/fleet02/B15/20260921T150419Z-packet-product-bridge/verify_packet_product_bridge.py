#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
import json, math

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a

def v2(z):
    z = abs(z)
    if z == 0:
        raise ValueError("v2(0)")
    return (z & -z).bit_length()-1

def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def bridge(vals):
    Np = len(vals)
    n = Np.bit_length()-1
    W = fwht(vals)
    den = 1 << n
    mu = [Fraction(w*w, den*den) for w in W]
    js = [sum(mu[s] for s in range(Np) if (s>>i)&1) for i in range(n)]

    groups = defaultdict(list)
    for s,w in enumerate(W):
        if w:
            groups[abs(w)].append(s)

    packets = []
    p = []
    N = []
    R = 0.0
    D = 0.0
    for mag,A in sorted(groups.items()):
        eps = [0]*Np
        for s in A:
            eps[s] = 1 if W[s] > 0 else -1
        V = fwht(eps)
        r = min(v2(x) for x in V if x)
        pa = sum(mu[s] for s in A)
        ba = Fraction(mag*(1<<r), den)
        Na = Fraction(len(A), 4**r)
        packets.append((A,r,pa,Na))
        p.append(pa); N.append(Na)
        R += float(pa)*r
        D += float(pa)*math.log2(1/float(ba))

    nu = []
    for s in range(Np):
        z = Fraction(1)
        for i,j in enumerate(js):
            z *= j if ((s>>i)&1) else (1-j)
        nu.append(z)

    beta = [sum(nu[s] for s in A) for A,_,_,_ in packets]
    Z = sum(math.sqrt(float(Na*be)) for Na,be in zip(N,beta))
    m = [math.sqrt(float(Na*be))/Z for Na,be in zip(N,beta)]

    KLm = sum(float(pa)*math.log2(float(pa)/ma) for pa,ma in zip(p,m))
    Cin = 0.0
    for (A,_,pa,_),be in zip(packets,beta):
        ua = Fraction(1,len(A))
        inner = 0.0
        for s in A:
            cond = nu[s]/be
            inner += float(ua)*math.log2(float(ua/cond))
        Cin += float(pa)*inner

    Sh = sum(h2(float(j)) for j in js)
    lhs = 4*D
    rhs = Sh - 2*R + 2*math.log2(Z) - 2*KLm - Cin
    return abs(lhs-rhs)

def one_point_summary(n):
    vals = [-1] + [1]*((1<<n)-1)
    Np = 1<<n
    W = fwht(vals)
    den = 1<<n
    mu = [Fraction(w*w, den*den) for w in W]
    j = sum(mu[s] for s in range(Np) if s&1)
    beta0 = (1-j)**n
    beta1 = 1-beta0
    Z = math.sqrt(float(beta0)) + math.sqrt(float((Np-1)*beta1))
    p0 = mu[0]
    p1 = 1-p0
    m0 = math.sqrt(float(beta0))/Z
    m1 = math.sqrt(float((Np-1)*beta1))/Z
    KLm = float(p0)*math.log2(float(p0)/m0)+float(p1)*math.log2(float(p1)/m1)
    I = n*float(j)
    return {"n":n,"I":I,"log2_Z":math.log2(Z),"KL_bridge":KLm,
            "difference":math.log2(Z)-KLm}

def main():
    per_n = {}
    total = 0
    max_residual = 0.0
    for n in range(1,5):
        Np = 1<<n
        worst = 0.0
        for mask in range(1<<Np):
            vals = [1 if (mask>>x)&1 else -1 for x in range(Np)]
            e = bridge(vals)
            worst = max(worst,e)
        per_n[str(n)] = {"functions":1<<Np,"max_abs_residual_bits":worst}
        total += 1<<Np
        max_residual = max(max_residual,worst)
    out = {
        "scope":"all Boolean truth tables through n=4; floating sanity check only",
        "functions":total,
        "per_dimension":per_n,
        "max_abs_residual_bits":max_residual,
        "one_point_defect":[one_point_summary(n) for n in range(3,11)]
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
