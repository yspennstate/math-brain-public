from __future__ import annotations
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext
from fractions import Fraction as F

PREC = 100
NTERMS = 55
getcontext().prec = 110

ALPHA = F(9, 256)

# Exact source-bound nine-bit shared-core Walsh numerator classes (A,Q), multiplicity.
PAIRS = [
    ((-18, -2), 72), ((2, 2), 72), ((0, 0), 46), ((-16, 0), 36),
    ((16, 0), 36), ((10, -6), 36), ((4, 4), 36), ((-4, -4), 36),
    ((-2, -2), 36), ((44, -4), 18), ((-44, 4), 18), ((-6, 10), 18),
    ((38, 6), 12), ((114, 2), 9), ((8, 8), 9), ((-8, -8), 9),
    ((4, -12), 6), ((-4, 12), 6), ((2, 18), 1),
]

# Strict source-certified lower bound for K(ell), ell=0.002713295, chosen
# below the rigorous lower endpoint in fleet04/B15's CHECK_OUTPUT.
THRESH = F(67766110260211932590, 10**19)  # 6.7766110260211932590

def qbounds(q: F):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        lo=Decimal(q.numerator)/Decimal(q.denominator)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        hi=Decimal(q.numerator)/Decimal(q.denominator)
    return lo, hi

def add(a,b):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a[0]+b[0]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=a[1]+b[1]
    return lo,hi

def neg(a): return -a[1], -a[0]
def sub(a,b): return add(a,neg(b))

def scale_exact(a,r:F):
    if r==0: return Decimal(0),Decimal(0)
    if r<0: return neg(scale_exact(a,-r))
    rb=qbounds(r); lows=[]; highs=[]
    for x in a:
        for y in rb:
            with localcontext() as c:
                c.prec=PREC; c.rounding=ROUND_FLOOR; lows.append(x*y)
            with localcontext() as c:
                c.prec=PREC; c.rounding=ROUND_CEILING; highs.append(x*y)
    return min(lows),max(highs)

def mulpos(a,b):
    assert a[0]>=0 and b[0]>=0
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a[0]*b[0]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=a[1]*b[1]
    return lo,hi

def divpos(a,b):
    assert a[0]>=0 and b[0]>0
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a[0]/b[1]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=a[1]/b[0]
    return lo,hi

def log_unit(m:F):
    assert F(1)<=m<=F(2)
    if m==1: return Decimal(0),Decimal(0)
    z=qbounds((m-1)/(m+1)); z2=mulpos(z,z); power=z
    s=(Decimal(0),Decimal(0))
    for k in range(NTERMS):
        s=add(s,scale_exact(power,F(1,2*k+1)))
        power=mulpos(power,z2)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        one_minus=Decimal(1)-z2[1]
        lo=Decimal(2)*s[0]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        rem=Decimal(2)*power[1]/(Decimal(2*NTERMS+1)*one_minus)
        hi=Decimal(2)*s[1]+rem
    return lo,hi

LN2=log_unit(F(2))
INV_LN2=divpos((Decimal(1),Decimal(1)),LN2)

def log2_ge1(x:F):
    assert x>=1
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<F(2)**e: e-=1
    m=x/(F(2)**e)
    return add((Decimal(e),Decimal(e)),divpos(log_unit(m),LN2))

def phi_interval(p:F):
    if p==0: return Decimal(0),Decimal(0)
    assert 0<p<=1
    return scale_exact(log2_ge1(1/p),p)

def slope_phi_interval(p:F):
    return sub(log2_ge1(1/p),INV_LN2)

def g_interval(b:F):
    if b==0: return Decimal(16),Decimal(16)
    b2=b*b
    return add(neg(phi_interval(b2)),qbounds(F(16)*(1-b2)))

def gprime_interval(b:F):
    assert b>0
    logb2=neg(log2_ge1(1/(b*b)))
    inside=add(add(logb2,INV_LN2),(Decimal(-16),Decimal(-16)))
    return scale_exact(inside,2*b)

def tangent_upper(center:F,x:F):
    out=(Decimal(0),Decimal(0))
    for (a,q),mult in PAIRS:
        if a==0 and q==0: continue
        p0=(F(a,512)+center*F(q,512))**2
        px=(F(a,512)+x*F(q,512))**2
        assert p0>0 and p0<F(1,4)
        slope=slope_phi_interval(p0)
        assert slope[0]>0
        term=add(phi_interval(p0),scale_exact(slope,px-p0))
        out=add(out,scale_exact(term,F(mult)))
    gt=add(g_interval(center),scale_exact(gprime_interval(center),x-center))
    return add(out,scale_exact(gt,ALPHA))

# These three tangent-majorant rows cover [0.19,1], hence [1/4,1].
CERTS=[
    (F(1,10),F(19,100),F(9,25)),
    (F(1,5),F(9,25),F(13,20)),
    (F(2,5),F(13,20),F(1)),
]

def main():
    assert sum(mult for _,mult in PAIRS)==512
    threshold_lo=qbounds(THRESH)[0]
    previous=F(19,100)
    worst=Decimal("-Infinity")
    worst_gap=None
    worst_row=None
    for row,(center,left,right) in enumerate(CERTS):
        assert left==previous
        for endpoint in (left,right):
            upper=tangent_upper(center,endpoint)[1]
            gap=threshold_lo-upper
            assert gap>0
            if upper>worst:
                worst=upper; worst_gap=gap; worst_row=(row,center,endpoint)
        previous=right
    assert previous==1
    assert F(1,4)>=F(19,100)
    print("PASS")
    print("certified_interval=[0.19,1]")
    print("therefore_interval=[1/4,1]_covered")
    print("strict_threshold_K=" + str(threshold_lo))
    print("worst_tangent_upper=" + str(worst))
    print("worst_gap_to_threshold=" + str(worst_gap))
    print("worst_row=" + str(worst_row))
    print("conclusion=sup_{b in [1/4,1]} K(b) < 6.7766110260211932590")
    print("peer_K_ell_lower_gt=6.7766110260211932590896736474059853605974")
    print("hence_global_K_max_occurs_in_[0,1/4]")
    print("full_FEI_status=OPEN")

if __name__=="__main__":
    main()
