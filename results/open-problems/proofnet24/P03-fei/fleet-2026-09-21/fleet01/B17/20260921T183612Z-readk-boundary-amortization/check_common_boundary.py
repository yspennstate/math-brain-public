import math
import numpy as np

LN2 = math.log(2.0)
A = 1.0/(2.0*LN2)
C0 = 2.0 + (2.0 + 2.0/math.sqrt(math.e))/LN2

def fwht(vals):
    a = np.asarray(vals, dtype=float).copy()
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            x = a[i:i+h].copy()
            y = a[i+h:i+2*h].copy()
            a[i:i+h] = x+y
            a[i+h:i+2*h] = x-y
        h *= 2
    return a/n

def H(vals):
    p = fwht(vals)**2
    p = p[p > 0.0]
    return float(np.sum(p*np.log2(1.0/p)))

def all_boolean(n):
    N = 1 << n
    for mask in range(1 << N):
        yield np.array([1.0 if ((mask >> j) & 1) else -1.0 for j in range(N)])

def mux(a,b,r,u,v):
    n = 1+r+u+v
    out = np.empty(1 << n)
    for x in range(1 << n):
        z = x & 1
        y = (x >> 1) & ((1 << r)-1)
        uu = (x >> (1+r)) & ((1 << u)-1)
        vv = (x >> (1+r+u)) & ((1 << v)-1)
        ai = y | (uu << r)
        bi = y | (vv << r)
        out[x] = a[ai] if z else b[bi]
    return out

def product(a,b,r,u,v):
    n = r+u+v
    out = np.empty(1 << n)
    for x in range(1 << n):
        y = x & ((1 << r)-1)
        uu = (x >> r) & ((1 << u)-1)
        vv = (x >> (r+u)) & ((1 << v)-1)
        out[x] = a[y | (uu << r)] * b[y | (vv << r)]
    return out

def influence(vals, i):
    n = int(round(math.log2(len(vals))))
    bit = 1 << i
    return sum(vals[x] != vals[x ^ bit] for x in range(1 << n))/(1 << n)

def stats(a,b,r,u,v):
    F = mux(a,b,r,u,v)
    D = product(a,b,r,u,v)
    omega = H(F) - 0.5*(H(a)+H(b))
    q = float(np.mean(D < 0))
    s = min(q,1.0-q)
    IY = sum(influence(D,j) for j in range(r))
    rhs = A*IY + C0*s
    return omega,q,s,IY,rhs

def run_case(r,u,v):
    aa = list(all_boolean(r+u))
    bb = list(all_boolean(r+v))
    violations = 0
    worst = (-1e100, None)
    for ia,a in enumerate(aa):
        for ib,b in enumerate(bb):
            omega,q,s,IY,rhs = stats(a,b,r,u,v)
            if omega > rhs + 1e-10:
                violations += 1
            if s > 1e-15:
                residual = (omega-A*IY)/s
                if residual > worst[0]:
                    worst = (residual,(ia,ib,omega,q,s,IY,rhs))
    return len(aa)*len(bb), violations, worst

print(f"A={A:.15f}")
print(f"C0={C0:.15f}")
print(f"C_read2={C0+1.0/LN2:.15f}")
for case in [(2,0,0),(1,1,1),(2,1,1)]:
    count,viol,worst=run_case(*case)
    print("case",case,"pairs",count,"violations",viol,
          "max_adjusted_residual",f"{worst[0]:.15f}",
          "witness",worst[1])
