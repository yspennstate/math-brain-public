"""Exact 4-bit obstruction to valuation-depth-filtered KL-credit positivity.

This is NOT a counterexample to FEI.  It checks that the negative information
credit D(mu||nu) from the product-shadow identity is globally nonnegative but
can have a NEGATIVE contribution after filtering packets by valuation depth.

For f=+1 on {1,2,4} subset F_2^4 and -1 elsewhere, the depth-r=2 packet is
the |W|=2 packet.  Its contribution to D(mu||nu), where nu is the product law
with the same spectral marginals, equals

    (3/16) log_2(64/225) < 0.

Thus the account02/B15 valuation-tail inequalities cannot be spent
depth-by-depth by discarding correspondingly filtered KL terms as if each were
nonnegative.  Only the unfiltered total KL has guaranteed sign.
"""
from collections import Counter
from fractions import Fraction
import math

NVAR = 4
N = 1 << NVAR
PLUS = {1,2,4}

def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for s in range(0,len(a),2*h):
            for j in range(s,s+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h *= 2
    return a

def v2(z):
    z=abs(int(z))
    assert z
    return (z & -z).bit_length()-1

def packet_r(indices, W):
    eps=[0]*N
    for S in indices:
        eps[S]=1 if W[S]>0 else -1
    V=fwht(eps)
    return min(v2(z) for z in V if z)

def main():
    f=[1 if x in PLUS else -1 for x in range(N)]
    W=fwht(f)
    groups={}
    for S,w in enumerate(W):
        if w:
            groups.setdefault(abs(w),[]).append(S)
    assert {k:len(v) for k,v in groups.items()} == {10:1,2:12,6:3}

    r={mag:packet_r(inds,W) for mag,inds in groups.items()}
    assert r == {10:0,2:2,6:0}

    masses=[Fraction(w*w,N*N) for w in W]
    q=[]
    for i in range(NVAR):
        q.append(sum(masses[S] for S in range(N) if (S>>i)&1))
    assert q == [Fraction(3,8)]*4

    A2=groups[2]
    level_counts=Counter(S.bit_count() for S in A2)
    assert level_counts == Counter({1:3,2:6,3:3})
    p_each=Fraction(1,64)
    p_packet=12*p_each
    assert p_packet == Fraction(3,16)

    ratio = p_each / (Fraction(3,8)**2 * Fraction(5,8)**2)
    assert ratio == Fraction(64,225)
    assert ratio < 1
    K2 = float(p_packet)*math.log2(float(ratio))
    assert K2 < 0

    direct=0.0
    for S in A2:
        k=S.bit_count()
        nu=float(Fraction(3,8)**k * Fraction(5,8)**(4-k))
        direct += float(p_each)*math.log2(float(p_each)/nu)
    assert abs(direct-K2) < 1e-14

    print("Walsh", W)
    print("packet_sizes", {k:len(v) for k,v in groups.items()})
    print("packet_valuations", r)
    print("spectral_marginals", [str(x) for x in q])
    print("depth2_level_counts", dict(sorted(level_counts.items())))
    print("depth2_mass", p_packet)
    print("depth2_credit_exact", "(3/16)*log2(64/225)")
    print("depth2_credit_decimal", f"{K2:.15f}")
    print("PASS: valuation-depth-filtered KL credit is strictly negative")

if __name__=="__main__":
    main()
