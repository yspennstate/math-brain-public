#!/usr/bin/env python3
"""
Exact checker for B16 first-hit two-scale covariance/curvature decomposition.
Standard library only; all comparison arithmetic is Fraction.
"""
from fractions import Fraction
from itertools import permutations
import random
import json

def odd_masks(m):
    return [x for x in range(1,1<<m) if x.bit_count() & 1]

def mean_load(m, coeff):
    mu=[Fraction(0) for _ in range(m)]
    for A,c in coeff.items():
        q=A.bit_count()
        for v in range(m):
            if (A>>v)&1:
                mu[v] += c/Fraction(q)
    return mu

def load(m, coeff, perm):
    rank={v:i for i,v in enumerate(perm)}
    out=[Fraction(0) for _ in range(m)]
    for A,c in coeff.items():
        j=min((v for v in range(m) if (A>>v)&1), key=rank.__getitem__)
        out[j]+=c
    return out

def direct_energy(m, coeff):
    ps=list(permutations(range(m)))
    mu=mean_load(m, coeff)
    tot=Fraction(0)
    for pi in ps:
        x=load(m, coeff, pi)
        tot += sum((x[v]-mu[v])**2 for v in range(m))
    return tot/Fraction(len(ps))

def split_energy(coeff):
    micro=Fraction(0)
    radial=Fraction(0)
    total=Fraction(0)
    for A,cA in coeff.items():
        r=A.bit_count()
        for B,cB in coeff.items():
            s=B.bit_count()
            h=(A&B).bit_count()
            if not h:
                continue
            u=(A|B).bit_count()
            k=Fraction(h,u)-Fraction(h,r*s)
            km=Fraction(h,u)-Fraction(h,r+s-1)
            kr=Fraction(h,r+s-1)-Fraction(h,r*s)
            total += cA*cB*k
            micro += cA*cB*km
            radial += cA*cB*kr
    return total,micro,radial

def curvature_upper_banks(coeff):
    """Pairwise forms of the two Poincare upper banks."""
    micro=Fraction(0)
    radial=Fraction(0)
    for A,cA in coeff.items():
        r=A.bit_count()
        for B,cB in coeff.items():
            s=B.bit_count()
            h=(A&B).bit_count()
            if not h:
                continue
            u=(A|B).bit_count()
            if h >= 2:
                micro += cA*cB*Fraction(h*(h-1), u*(u+1))
            if r >= 2 and s >= 2:
                radial += cA*cB*Fraction(
                    h*(r-1)*(s-1),
                    2*(r+s-2)*(r+s-1)
                )
    return micro,radial

def star_obstruction(d):
    c2=Fraction(d*(d-1),2)
    c3=Fraction(d*(d-1)*(d-2),6)
    radial=Fraction(4,45)*c2*c2
    internal=Fraction(2,15)*c2 + Fraction(3,10)*c3
    ratio=radial/internal if internal else Fraction(0)
    claimed=Fraction(4*d*(d-1),3*(3*d-2)) if d>=2 else Fraction(0)
    assert ratio == claimed
    return radial,internal,ratio

def main():
    rng=random.Random(20260921)
    direct_cases=0
    poincare_cases=0
    min_slack_micro=None
    min_slack_radial=None

    for m in range(1,6):
        masks=odd_masks(m)
        families=[]
        if masks:
            families.append({masks[0]: Fraction(1)})
            families.append({A: Fraction(1 if i%2==0 else -1) for i,A in enumerate(masks[:min(6,len(masks))])})
        for _ in range(12):
            chosen=rng.sample(masks, min(len(masks), 6))
            fam={}
            for A in chosen:
                c=Fraction(rng.randint(-3,3))
                if c:
                    fam[A]=c
            if fam:
                families.append(fam)

        for coeff in families:
            d=direct_energy(m,coeff)
            total,micro,radial=split_energy(coeff)
            assert d == total == micro+radial
            direct_cases += 1
            ubm,ubr=curvature_upper_banks(coeff)
            assert micro <= ubm
            assert radial <= ubr
            sm=ubm-micro
            sr=ubr-radial
            min_slack_micro=sm if min_slack_micro is None else min(min_slack_micro,sm)
            min_slack_radial=sr if min_slack_radial is None else min(min_slack_radial,sr)
            poincare_cases += 1

    r=s=3; h=2; u=4
    K=Fraction(h,u)-Fraction(h,r*s)
    Km=Fraction(h,u)-Fraction(h,r+s-1)
    Kr=Fraction(h,r+s-1)-Fraction(h,r*s)
    assert K == Fraction(5,18)
    assert Km == Fraction(1,10)
    assert Kr == Fraction(8,45)
    assert Km+Kr == K

    c=Fraction(1,8)
    refund_total=2*c*c*K
    refund_micro=2*c*c*Km
    refund_radial=2*c*c*Kr
    assert refund_total == Fraction(5,576)
    assert refund_micro == Fraction(1,320)
    assert refund_radial == Fraction(1,180)
    assert refund_micro+refund_radial == refund_total

    obstruction={}
    prev=None
    for d in range(2,65):
        R,B,q=star_obstruction(d)
        if prev is not None:
            assert q > prev
        prev=q
        obstruction[str(d)]={
            "radial": str(R),
            "internal": str(B),
            "ratio": str(q),
            "ratio_float": float(q),
        }

    out={
        "status":"PASS",
        "direct_first_hit_exact_cases":direct_cases,
        "two_scale_poincare_cases":poincare_cases,
        "minimum_micro_poincare_slack":str(min_slack_micro),
        "minimum_radial_poincare_slack":str(min_slack_radial),
        "q3_overlap2_split":{
            "K_total":str(K),
            "K_micro":str(Km),
            "K_radial":str(Kr),
            "negative_credit_refund_total":str(refund_total),
            "negative_credit_refund_micro":str(refund_micro),
            "negative_credit_refund_radial":str(refund_radial),
        },
        "star_obstruction":{
            "formula_ratio":"4*d*(d-1)/(3*(3*d-2))",
            "asymptotic":"(4/9)d",
            "d_2":obstruction["2"],
            "d_8":obstruction["8"],
            "d_64":obstruction["64"],
        }
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
