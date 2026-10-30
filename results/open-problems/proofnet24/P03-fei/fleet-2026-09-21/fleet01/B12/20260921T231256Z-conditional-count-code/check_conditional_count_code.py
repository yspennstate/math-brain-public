#!/usr/bin/env python3
import math, random
from collections import defaultdict

LOG2E = math.log2(math.e)
C_COUNT = 17.0/16.0 * (2.0 + LOG2E)
C_INTERNAL = 2.0*LOG2E + 1.0/16.0
C_TOTAL = C_COUNT + C_INTERNAL


def H(ps):
    return -sum(p*math.log2(p) for p in ps if p > 0.0)


def conditional_entropy(joint):
    pt = defaultdict(float)
    by_t = defaultdict(list)
    for (x,t), p in joint.items():
        pt[t] += p
        by_t[t].append((x,p))
    ans = 0.0
    for t, items in by_t.items():
        z = pt[t]
        ans += z * H([p/z for _,p in items if p > 0])
    return ans


def component_count_bound(joint, n, comps):
    # Universal inequality H(Y|T) <= H(N|T) + sum_C(E_C-Q_C).
    hy_t = conditional_entropy(joint)
    p_i = [sum(p for (s,t),p in joint.items() if i in s) for i in range(n)]
    n_joint = defaultdict(float)
    for (s,t),p in joint.items():
        counts = tuple(sum(i in s for i in C) for C in comps)
        n_joint[(counts,t)] += p
    hn_t = conditional_entropy(n_joint)
    internal = 0.0
    for C in comps:
        P = sum(p_i[i] for i in C)
        if P > 0:
            internal += P*H([p_i[i]/P for i in C])
        for (s,t),p in joint.items():
            k = sum(i in s for i in C)
            internal -= p*math.lgamma(k+1.0)/math.log(2.0)
    return hy_t, hn_t + internal


def random_joint(n, nt, rng):
    subs = [tuple(i for i in range(n) if (mask>>i)&1) for mask in range(1<<n)]
    raw = [rng.expovariate(1.0) for _ in range(nt*len(subs))]
    z = sum(raw)
    joint = {}
    q = 0
    for t in range(nt):
        for s in subs:
            joint[(s,t)] = raw[q]/z
            q += 1
    return joint


def ideal_component(m):
    # Exact-Palm ideal with p_i=2^{-m}, r=m+1.
    r=m+1
    P=r*(2.0**(-m))
    probs=[]
    for k in range(1,r+1):
        lam=math.comb(m,k-1)/(2.0**m)
        probs.append(P*lam/k)
    p0=1.0-sum(probs)
    return P, H([p0]+probs)


def main():
    rng=random.Random(20260921)
    worst_slack=1e9
    tests=0
    for n in (2,3,4,5):
        cut=max(1,n//2)
        comps=(tuple(range(cut)),tuple(range(cut,n)))
        if not comps[1]:
            comps=(tuple(range(n)),)
        for _ in range(500):
            joint=random_joint(n, 3, rng)
            lhs,rhs=component_count_bound(joint,n,comps)
            slack=rhs-lhs
            worst_slack=min(worst_slack,slack)
            if slack < -1e-10:
                raise AssertionError((n,lhs,rhs,slack))
            tests += 1

    cmax=(-1.0,None)
    idealmax=(-1.0,None)
    for m in range(1,201):
        r=m+1
        cm=17.0/(8.0*r)*(m+LOG2E+math.log2(r))
        if cm>cmax[0]: cmax=(cm,m)
        P,hn=ideal_component(m)
        ratio=hn/P
        if ratio>idealmax[0]: idealmax=(ratio,m)
    if abs(cmax[0]-C_COUNT)>1e-12 or cmax[1]!=1:
        raise AssertionError((cmax,C_COUNT))

    print(f"random_joint_component_count_checks={tests}")
    print(f"minimum_rhs_minus_lhs={worst_slack:.16e}")
    print(f"c_count={C_COUNT:.15f} attained_bound_at_m={cmax[1]}")
    print(f"c_internal={C_INTERNAL:.15f}")
    print(f"c_total={C_TOTAL:.15f}")
    print(f"max_ideal_HN_over_P_through_m200={idealmax[0]:.15f} at_m={idealmax[1]}")

if __name__=='__main__':
    main()
