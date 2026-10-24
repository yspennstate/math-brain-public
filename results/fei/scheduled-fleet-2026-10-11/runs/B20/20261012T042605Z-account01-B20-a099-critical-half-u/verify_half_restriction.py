#!/usr/bin/env python3
"""Finite diagnostic for B20-A099-CRITICAL-HALF-U-v1.

Enumerates every Boolean truth table through n=4, locates every H/I maximizer,
and checks the retained-terminal lower bound and the constant transfer at the
fixed retention scale t=1/2.  The universal theorem is analytic.
"""
from math import log2, log

TOL = 2e-10


def walsh(vals):
    a = [float(x) for x in vals]
    n = len(a).bit_length()-1
    for j in range(n):
        step = 1 << j
        for base in range(0, len(a), 2*step):
            for k in range(step):
                x, y = a[base+k], a[base+k+step]
                a[base+k], a[base+k+step] = x+y, x-y
    return [x/len(a) for x in a]


def stats(vals):
    n = len(vals).bit_length()-1
    p = [x*x for x in walsh(vals)]
    h = sum(-x*log2(x) for x in p if x > 0)
    influence = sum(mask.bit_count()*p[mask] for mask in range(len(p)))
    pi = p[:]
    for j in range(n):
        for mask in range(len(p)):
            if not ((mask >> j) & 1):
                pi[mask] += pi[mask | (1 << j)]
    u = sum(p[m]*log2(pi[m]/p[m]) for m in range(len(p)) if p[m] > 0)
    var = 1-p[0]
    q = 1-var
    b = q*log2(1/q) if 0 < q < 1 else 0.0
    return h, influence, u, var, b


def restrict(vals, live, z):
    n = len(vals).bit_length()-1
    live_pos = [j for j in range(n) if (live >> j) & 1]
    dead_pos = [j for j in range(n) if not ((live >> j) & 1)]
    out=[]
    for y in range(1 << len(live_pos)):
        x=0
        for k,j in enumerate(live_pos): x |= ((y >> k) & 1) << j
        for k,j in enumerate(dead_pos): x |= ((z >> k) & 1) << j
        out.append(vals[x])
    return out


def half_average(vals, c):
    n = len(vals).bit_length()-1
    eu=ei=ed=ev=eb=0.0
    # At t=1/2 every (live set, assignment) atom has weight 2^{-n}2^{-|dead|}.
    for live in range(1 << n):
        dead = n-live.bit_count()
        w = (0.5**n)/(1 << dead)
        for z in range(1 << dead):
            h,i,u,v,b=stats(restrict(vals,live,z))
            eu += w*u; ei += w*i; ed += w*(c*i-h); ev += w*v; eb += w*b
    return eu,ei,ed,ev,eb


def main():
    total_tables=0
    maximizer_count=0
    checks=0
    for n in range(1,5):
        best=-1.0; maximizers=[]
        for code in range(1 << (1 << n)):
            total_tables += 1
            vals=[1 if (code >> x) & 1 else -1 for x in range(1 << n)]
            h,i,*_=stats(vals)
            if i <= TOL: continue
            r=h/i
            if r > best+TOL: best=r; maximizers=[vals]
            elif abs(r-best)<=TOL: maximizers.append(vals)
        k_req=0.0
        for vals in maximizers:
            maximizer_count += 1
            _,root_i,*_=stats(vals)
            eu,ei,ed,ev,eb=half_average(vals,best)
            assert abs(ei-root_i/2) <= TOL
            assert ed <= root_i/log(2)+TOL
            rhs=(best-2)*root_i/4-ed/2+ev+eb/2
            assert eu+TOL >= rhs
            k=eu/ei if ei>TOL else 0.0
            k_req=max(k_req,k)
            transferred=2+2*k+2/log(2)
            assert best <= transferred+TOL
            checks += 4
        print(f"n={n} c_n={best:.12f} maximizers={len(maximizers)} K_half_required={k_req:.12f}")
    print(f"truth_tables={total_tables}")
    print(f"maximizers={maximizer_count}")
    print(f"assertions={checks}")
    print("status=PASS")


if __name__ == "__main__": main()

