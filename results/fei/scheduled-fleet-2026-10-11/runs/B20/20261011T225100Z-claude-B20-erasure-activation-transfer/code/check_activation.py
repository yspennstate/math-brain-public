# B20 check: exact activation formula for the erasure functional B, tensor additivity of B,
# and the bias-erasure bound sum_i phi(h0^2, hi^2) <= (2/(sqrt(e) ln 2)) I(h).
# Masses are exact Fractions; entropies are floats (evidence for identities proved in REPORT.md).
import itertools, math, json, sys
from fractions import Fraction as Fr

def walsh(tt, n):
    # tt: list of +-1 of length 2^n, index bit j = coordinate j (bit=1 means x_j=-1 convention irrelevant)
    a = list(tt)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    N = len(a)
    return [Fr(v, N) for v in a]  # fhat indexed by subset mask

def phi(a, b):
    a = float(a); b = float(b)
    s = a + b
    t = 0.0
    if a > 0: t += a*math.log2(s/a)
    if b > 0: t += b*math.log2(s/b)
    return t

def Bfun(fh, n):
    tot = 0.0
    for i in range(n):
        bit = 1 << i
        for S in range(1 << n):
            if S & bit: continue
            tot += phi(fh[S]**2, fh[S|bit]**2)
    return tot

def Infl(tt, n):
    N = 1 << n
    tot = Fr(0)
    for i in range(n):
        bit = 1 << i
        cnt = sum(1 for x in range(N) if tt[x] != tt[x ^ bit])
        tot += Fr(cnt, N)
    return tot

def activate(tt, n, k):
    # F(x,y) = tt(x) if y = all-zero-bits (the single active point), else +1. y bits are coordinates n..n+k-1
    N = 1 << (n+k)
    out = []
    for z in range(N):
        x = z & ((1 << n) - 1); y = z >> n
        out.append(tt[x] if y == 0 else 1)
    return out

def tensor(t1, n1, t2, n2):
    return [t1[z & ((1<<n1)-1)] * t2[z >> n1] for z in range(1 << (n1+n2))]

CONST = 2/(math.sqrt(math.e)*math.log(2))
res = {"formula_cases":0, "formula_maxerr":0.0, "infl_exact_cases":0, "infl_failures":0,
       "lower_bound_cases":0, "lower_bound_failures":0, "min_lower_slack":None,
       "tensor_cases":0, "tensor_maxerr":0.0, "phi_bound_cases":0, "phi_bound_failures":0,
       "phi_bound_max_ratio":0.0, "yratio_samples":[]}

def formula(fh, n, k):
    d = Fr(1, 1 << k); c = 1 - fh[0]
    Bf = Bfun(fh, n)
    sf = sum(phi(fh[0]**2, fh[1<<i]**2) for i in range(n))
    sg = sum(phi(c**2, fh[1<<i]**2) for i in range(n))
    s0 = sum(phi((1-d*c)**2, d*d*fh[1<<i]**2) for i in range(n))
    df = float(d)
    xpart = float(d - d*d)*(Bf - sf + sg) + float(d*d)*(Bf - sf) + s0
    ypart = k*(float(d*(1-fh[0]**2)) + float((d-2*d*d)*c*c) + phi((1-d*c)**2, d*d*c*c))
    return xpart + ypart

for n in (1, 2, 3):
    for bits in itertools.product((1, -1), repeat=1 << n):
        tt = list(bits); fh = walsh(tt, n); If = Infl(tt, n)
        for k in (1, 2, 3):
            F = activate(tt, n, k); FH = walsh(F, n+k)
            BF = Bfun(FH, n+k); pred = formula(fh, n, k)
            err = abs(BF - pred); res["formula_cases"] += 1
            res["formula_maxerr"] = max(res["formula_maxerr"], err)
            IF = Infl(F, n+k); d = Fr(1, 1 << k); c = 1 - fh[0]
            res["infl_exact_cases"] += 1
            if IF != d*(If + k*c): res["infl_failures"] += 1
            lb = float(d)*(Bfun(fh, n) - CONST*float(If))
            slack = BF - lb; res["lower_bound_cases"] += 1
            if slack < -1e-12: res["lower_bound_failures"] += 1
            res["min_lower_slack"] = slack if res["min_lower_slack"] is None else min(res["min_lower_slack"], slack)

# tensor additivity on n1,n2 <= 2
for n1 in (1, 2):
    for n2 in (1, 2):
        for b1 in itertools.product((1, -1), repeat=1 << n1):
            for b2 in itertools.product((1, -1), repeat=1 << n2):
                T = tensor(list(b1), n1, list(b2), n2)
                lhs = Bfun(walsh(T, n1+n2), n1+n2)
                rhs = Bfun(walsh(list(b1), n1), n1) + Bfun(walsh(list(b2), n2), n2)
                res["tensor_cases"] += 1
                res["tensor_maxerr"] = max(res["tensor_maxerr"], abs(lhs-rhs))

# phi bound over all Boolean functions on n <= 4
for n in (1, 2, 3, 4):
    for bits in itertools.product((1, -1), repeat=1 << n):
        tt = list(bits); fh = walsh(tt, n); If = Infl(tt, n)
        s = sum(phi(fh[0]**2, fh[1<<i]**2) for i in range(n))
        res["phi_bound_cases"] += 1
        if If > 0:
            r = s/float(If); res["phi_bound_max_ratio"] = max(res["phi_bound_max_ratio"], r)
            if s > CONST*float(If) + 1e-12: res["phi_bound_failures"] += 1
        elif s > 1e-15: res["phi_bound_failures"] += 1

# y-part ratio for the point defect (f = -1 constant, n=1 dummy) as k grows (formula only, exact masses)
for k in (2, 4, 8, 16, 32):
    fh = [Fr(-1), Fr(0)]
    d = Fr(1, 1 << k); c = 2
    ypart = k*(float(d*(1-fh[0]**2)) + float((d-2*d*d)*c*c) + phi((1-d*c)**2, d*d*c*c))
    res["yratio_samples"].append([k, ypart/float(d*k*c)])
res["const_2_over_sqrt_e_ln2"] = CONST
json.dump(res, sys.stdout, indent=1)
