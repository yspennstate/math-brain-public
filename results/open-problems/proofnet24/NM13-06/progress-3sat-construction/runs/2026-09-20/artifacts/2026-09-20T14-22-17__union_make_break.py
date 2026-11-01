#!/usr/bin/env python3
"""
NM13-06 T04 diagnostic:
1) exact truth-table check of the flip-variable A/B/C/D normal form and union closure;
2) local-tree majority make/break law under a finite Poisson truncation.

The numerical part uses ordinary IEEE double arithmetic. It is a mechanism diagnostic,
not an interval certificate. K=40 and K=45 are both printed to expose truncation stability.
"""
from math import exp, comb
from itertools import product

def sat(t, x):
    # t_i=1 iff literal i is true under the reference assignment;
    # x_i=1 iff the underlying variable is flipped.
    return any((ti == 0 and xi == 1) or (ti == 1 and xi == 0)
               for ti, xi in zip(t, x))

def exact_truth_checks():
    for t in product((0,1), repeat=3):
        for x in product((0,1), repeat=3):
            direct = any(bool(ti ^ xi) for ti,xi in zip(t,x))
            assert sat(t,x) == direct

    out = {}
    for j in range(4):
        ok = True
        witness = None
        for t in [u for u in product((0,1), repeat=3) if sum(u)==j]:
            sols = [x for x in product((0,1), repeat=3) if sat(t,x)]
            for x in sols:
                for y in sols:
                    z = tuple(max(a,b) for a,b in zip(x,y))
                    if not sat(t,z):
                        ok = False
                        witness = (t,x,y,z)
                        break
                if not ok: break
            if not ok: break
        out[j] = (ok,witness)
    assert out[0][0] and out[1][0]
    assert not out[2][0] and not out[3][0]
    return out

def local(alpha, K):
    mu = 1.5*alpha
    pp = [exp(-mu)]
    for k in range(1,K+1):
        pp.append(pp[-1]*mu/k)

    # Aggregate the (Z,M) law, Z=min(P,N), M=max(P,N).
    EZ = 0.0
    zw = []
    for z in range(1,K+1):
        w = pp[z]*pp[z]
        EZ += z*w
        zw.append((z,z,z*w))
        for m in range(z+1,K+1):
            w = 2.0*pp[z]*pp[m]
            EZ += z*w
            zw.append((z,m,z*w))

    q = EZ/(2.0*mu)
    q2 = q*q

    pmf = {}
    for n in range(K+1):
        pmf[n] = [comb(n,k)*(q2**k)*((1.0-q2)**(n-k)) for k in range(n+1)]

    # False-Palm candidate: A = 1+Bin(Z-1,q^2), B=Bin(M,q^2).
    joint = {}
    for z,m,num in zw:
        wt = num/EZ
        for a0,pa in enumerate(pmf[z-1]):
            A = 1+a0
            for B,pb in enumerate(pmf[m]):
                joint[(A,B)] = joint.get((A,B),0.0) + wt*pa*pb

    bdist = {}
    ddist = {}
    for (A,B),pr in joint.items():
        bdist[B] = bdist.get(B,0.0)+pr
        ddist[B-A] = ddist.get(B-A,0.0)+pr

    def emin(dist, k):
        vals = sorted(dist)
        tails = {}
        tail = 0.0
        for v in reversed(vals):
            tail += dist[v]
            tails[v] = tail
        ans = 0.0
        for v in vals:
            ge = tails[v]
            gt = ge-dist[v]
            ans += v*(ge**k-gt**k)
        return ans

    def selected_moments(dist, key):
        vals = sorted(dist)
        greater = {}
        tail = 0.0
        for v in reversed(vals):
            greater[v] = tail
            tail += dist[v]
        EA = EB = 0.0
        for (A,B),pr in joint.items():
            d = key(A,B)
            peq = dist[d]
            pgt = greater[d]
            # Among 3 iid candidates, labeled item wins minimum with uniform tie-break.
            sel = pgt*pgt + peq*pgt + peq*peq/3.0
            EA += 3.0*pr*sel*A
            EB += 3.0*pr*sel*B
        return EA,EB

    r2 = emin(bdist,2)
    r3 = emin(bdist,3)
    minD = emin(ddist,3)
    EA,EB = selected_moments(ddist, lambda A,B:B-A)
    EA_b,EB_b = selected_moments(bdist, lambda A,B:B)
    pD_nonneg = sum(pr for d,pr in ddist.items() if d >= 0)
    pD_pos = sum(pr for d,pr in ddist.items() if d > 0)

    c = [alpha*comb(3,j)*((1.0-q)**j)*(q**(3-j)) for j in range(4)]
    return dict(q=q,r2=r2,r3=r3,minD=minD,EA=EA,EB=EB,
                minBnet=EB_b-EA_b,
                root_no_strict_decrease=pD_nonneg**3,
                root_all_strict_worsen=pD_pos**3,
                c=c, mass=sum(joint.values()))

def main():
    checks = exact_truth_checks()
    print("EXACT_TRUTH_TABLE_CHECK=PASS")
    for j in range(4):
        ok,w = checks[j]
        print(f"type_j={j} union_closed={ok} witness={w}")

    for alpha in (3.52,3.6,4.4898):
        a40 = local(alpha,40)
        a45 = local(alpha,45)
        keys = ("q","r2","r3","minD","EA","EB","minBnet",
                "root_no_strict_decrease","root_all_strict_worsen")
        stab = max(abs(a40[k]-a45[k]) for k in keys)
        print(f"\nalpha={alpha:.4f} K=45")
        for k in keys:
            print(f"{k}={a45[k]:.15g}")
        print("clause_density_j0_j1_j2_j3=" +
              ",".join(f"{v:.15g}" for v in a45["c"]))
        print(f"joint_mass={a45['mass']:.17g}")
        print(f"max_abs_K40_K45_change={stab:.3e}")
        print(f"makebreak_gain_vs_minB={a45['minBnet']-a45['minD']:.15g}")

    print("\nALL_CHECKS_PASS")

if __name__ == "__main__":
    main()
