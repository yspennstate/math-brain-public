#!/usr/bin/env python3
from fractions import Fraction
from math import factorial
from itertools import product
from collections import Counter, defaultdict

CHECKS = 0

def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

def connected_mapping_count(n):
    if n == 1:
        return 1
    s = 0
    for k in range(1, n):
        s += factorial(n) // factorial(n-k) * n**(n-k-1)
    s += factorial(n-1)
    return s

def weak_components(f):
    n = len(f)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a,b):
        a,b = find(a),find(b)
        if a != b:
            parent[b] = a
    for i,j in enumerate(f):
        union(i,j)
    d = defaultdict(list)
    for i in range(n):
        d[find(i)].append(i)
    return list(d.values())

def restricted_partition(comps, b):
    ans = []
    for c in comps:
        s = tuple(sorted(x for x in c if x < b))
        if s:
            ans.append(s)
    return tuple(sorted(ans))

def poly_mul(a,b,N):
    out = [Fraction(0) for _ in range(N+1)]
    for i,x in enumerate(a):
        if not x:
            continue
        for j,y in enumerate(b):
            if i+j > N:
                break
            if y:
                out[i+j] += x*y
    return out

def poly_pow(a,p,N):
    out = [Fraction(1)] + [Fraction(0)]*N
    for _ in range(p):
        out = poly_mul(out,a,N)
    return out

def deriv(a,r):
    out = a[:]
    for _ in range(r):
        out = [out[i]*i for i in range(1,len(out))]
    return out

def C_series(N):
    return [Fraction(0)] + [
        Fraction(connected_mapping_count(n), factorial(n))
        for n in range(1,N+1)
    ]

def denominator_count(N,r):
    C = C_series(N)
    P = poly_pow(C,r,N)
    val = Fraction(factorial(N), factorial(r))*P[N]
    ok(val.denominator == 1, f"denominator integrality N={N},r={r}")
    return val.numerator

def visible_count_formula(N,r,pi):
    b = sum(len(B) for B in pi)
    q = len(pi)
    if q > r:
        return 0
    C = C_series(N)
    P = [Fraction(1)] + [Fraction(0)]*N
    for B in pi:
        P = poly_mul(P, deriv(C,len(B)), N)
    R = poly_pow(C,r-q,N)
    R = [x/Fraction(factorial(r-q),1) for x in R]
    P = poly_mul(P,R,N)
    val = Fraction(factorial(N-b),1) * P[N-b]
    ok(val.denominator == 1, f"visible integrality N={N},r={r},pi={pi}")
    return val.numerator

def pi_from_sizes(sizes):
    ans=[]
    a=0
    for s in sizes:
        ans.append(tuple(range(a,a+s)))
        a += s
    return tuple(ans)

def p_exact(N,r,sizes):
    return Fraction(
        visible_count_formula(N,r,pi_from_sizes(sizes)),
        denominator_count(N,r)
    )

def beta(i,j):
    return Fraction(factorial(i-1)*factorial(j-1), factorial(i+j-1))

# 1. Exhaustive finite mapping checks N<=7.
enum_den = {}
enum_vis = {}
enum_shapes = {}
for N in range(1,8):
    connected = 0
    per_r_den = Counter()
    per_r_vis = defaultdict(Counter)
    per_r_shapes = defaultdict(Counter)
    b = min(4,N)
    for f in product(range(N), repeat=N):
        comps = weak_components(f)
        r = len(comps)
        if r == 1:
            connected += 1
        per_r_den[r] += 1
        per_r_vis[r][restricted_partition(comps,b)] += 1
        per_r_shapes[r][tuple(sorted((len(c) for c in comps), reverse=True))] += 1
    ok(connected == connected_mapping_count(N), f"connected count N={N}")
    for r in range(1,N+1):
        ok(per_r_den[r] == denominator_count(N,r), f"denominator N={N},r={r}")
        if r <= 4:
            for pi,count in per_r_vis[r].items():
                ok(count == visible_count_formula(N,r,pi),
                   f"visible EGF N={N},r={r},pi={pi}")
    enum_den[N]=per_r_den
    enum_vis[N]=per_r_vis
    enum_shapes[N]=per_r_shapes

# 2. C036 full-root degree is exactly four for N>=4.
for N in range(4,8):
    den = enum_den[N][4]
    deg4 = sum(v for shape,v in enum_shapes[N][4].items() if len(shape)==4)
    ok(deg4 == den, f"root degree 4 N={N}")

# Exact small root-shape witnesses.
ok(Fraction(enum_shapes[6][4][(3,1,1,1)], enum_den[6][4]) == Fraction(68,149),
   "N=6 shape 3,1,1,1")
ok(Fraction(enum_shapes[6][4][(2,2,1,1)], enum_den[6][4]) == Fraction(81,149),
   "N=6 shape 2,2,1,1")

# 3. Pair-separation lower bound and activation legitimacy for r=4.
for N in range(4,41):
    lower = Fraction(3*(2*N-4), N*(N-1))
    ok(lower > Fraction(1,N), f"pair lower bound N={N}")
    lam_upper = 1/lower
    delta = Fraction(1,N*N)
    ok(delta*lam_upper < 1, f"activation bound N={N}")

# 4. Exact normalized generator values and finite trends from fixed-r theorem.
trend = []
for r in (2,3,4,5):
    for N in (20,50,100):
        p11 = p_exact(N,r,(1,1))
        lam = 1/p11
        q12 = lam*p_exact(N,r,(1,2))
        q22 = lam*p_exact(N,r,(2,2))
        q111 = lam*p_exact(N,r,(1,1,1)) if r >= 3 else Fraction(0)
        ok(p11 > 0, f"p11 positive r={r},N={N}")
        trend.append((r,N,float(lam),float(q12),float(q22),float(q111)))

# 5. Exact CTCS targets.
ok(beta(1,1)==1, "B11")
ok(beta(1,2)==Fraction(1,2), "B12")
ok(beta(2,2)==Fraction(1,6), "B22")

print(f"EXACT_CHECKS={CHECKS}")
print("C036_ROOT_DEGREE=4_FOR_N=4..7")
print("C036_N6_SHAPES: P(3,1,1,1)=68/149; P(2,2,1,1)=81/149")
print("FIXED_R_TREND columns: r N lambda q12 q22 q111")
for row in trend:
    print("%d %d %.12f %.12f %.12f %.12f" % row)
print("CTCS_TARGETS q12=0.5 q22=0.166666666667 q111=0")
print("ALL_EXACT_CHECKS_PASS")
