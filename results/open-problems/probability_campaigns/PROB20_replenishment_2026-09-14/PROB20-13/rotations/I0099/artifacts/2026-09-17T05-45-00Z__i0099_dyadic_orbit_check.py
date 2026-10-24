#!/usr/bin/env python3
"""Exact self-check for I0099 dyadic-degree-two reformulation.

This is a same-track self-check, not an independent audit and not a proof of
the asymptotic Paley clique conjecture.

For every normalized Paley five-clique C containing {0,1} through p<=113:
  * compute t5(C), the common-neighbor count in G_p;
  * compute R1(C), the number of monic irreducible quadratics f over F_p
    for which f(c) is a nonzero square for all c in C;
  * verify R1(C) == 2*t5(C) (mod 4), the congruence proved in the report.
For p<=73 it also checks directly in F_{p^2} that the number of degree-two
base elements x with every x-c square is 2*R1(C).
"""

def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def chi(a,p):
    a %= p
    if a == 0:
        return 0
    r = pow(a,(p-1)//2,p)
    assert r in (1,p-1)
    return 1 if r == 1 else -1

def adj(a,b,p):
    return a != b and chi(a-b,p) == 1

def normalized_five_cliques(p):
    common = [x for x in range(2,p) if adj(x,0,p) and adj(x,1,p)]
    out = []
    L = len(common)
    for i in range(L):
        a = common[i]
        for j in range(i+1,L):
            b = common[j]
            if not adj(a,b,p):
                continue
            for k in range(j+1,L):
                c = common[k]
                if adj(a,c,p) and adj(b,c,p):
                    C = (0,1,a,b,c)
                    assert all(adj(C[u],C[v],p) for u in range(5) for v in range(u+1,5))
                    out.append(C)
    return out

def t5(C,p):
    return sum(
        1 for x in range(p)
        if x not in C and all(adj(x,c,p) for c in C)
    )

def R1(C,p):
    # f(T)=T^2-sT+n is irreducible iff Delta=s^2-4n is nonsquare.
    # For irreducible f, f(c) never vanishes.
    ans = 0
    for s in range(p):
        for n in range(p):
            if chi(s*s-4*n,p) != -1:
                continue
            if all(chi(c*c-s*c+n,p) == 1 for c in C):
                ans += 1
    return ans

def direct_degree_two_good(C,p):
    # F_{p^2}=F_p[u]/(u^2-d), d a fixed nonsquare.
    # For x=a+bu with b!=0, x-c is a square in F_{p^2}
    # iff Norm(x-c)=(a-c)^2-d b^2 is a square in F_p.
    d = next(a for a in range(2,p) if chi(a,p) == -1)
    ans = 0
    for b in range(1,p):
        db2 = (d*b*b) % p
        for a in range(p):
            if all(chi((a-c)*(a-c)-db2,p) == 1 for c in C):
                ans += 1
    return ans

primes = [p for p in range(13,114) if p % 4 == 1 and isprime(p)]
total = 0
for p in primes:
    cliques = normalized_five_cliques(p)
    Rs, Ts = [], []
    for C in cliques:
        r = R1(C,p)
        t = t5(C,p)
        assert r % 4 == (2*t) % 4
        if p <= 73:
            assert direct_degree_two_good(C,p) == 2*r
        Rs.append(r); Ts.append(t)
    total += len(cliques)
    if cliques:
        print("p=%d cliques=%d R1_min=%d R1_max=%d t5_min=%d t5_max=%d congruence=PASS" %
              (p,len(cliques),min(Rs),max(Rs),min(Ts),max(Ts)))
    else:
        print("p=%d cliques=0 congruence=VACUOUS" % p)

assert total == 1004
print("TOTAL_NORMALIZED_FIVE_CLIQUES=%d" % total)
print("DIRECT_Fp2_NORM_CHECK_THROUGH_p=73=PASS")
print("R1_MOD4_EQUALS_2T5_MOD4_THROUGH_p=113=PASS")
print("ALL_I0099_DYADIC_ORBIT_SELF_CHECKS_PASS")
