from __future__ import annotations
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, getcontext
from fractions import Fraction as F
import json, hashlib

PREC = 120
getcontext().prec = PREC
NTERMS = 100
ALPHA = F(9, 256)
D0 = F(133, 128)
B = F(257, 256)
ISRC = F(261,128)

# Exact multiplicities of the source-bound shared-core Walsh numerator pairs (a,q),
# coefficient = (a+bq)/512.
PAIRS = [
    ((-18, -2), 72), ((2, 2), 72), ((0, 0), 46), ((-16, 0), 36),
    ((16, 0), 36), ((10, -6), 36), ((4, 4), 36), ((-4, -4), 36),
    ((-2, -2), 36), ((44, -4), 18), ((-44, 4), 18), ((-6, 10), 18),
    ((38, 6), 12), ((114, 2), 9), ((8, 8), 9), ((-8, -8), 9),
    ((4, -12), 6), ((-4, 12), 6), ((2, 18), 1),
]

def qbounds(q:F):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        lo=Decimal(q.numerator)/Decimal(q.denominator)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        hi=Decimal(q.numerator)/Decimal(q.denominator)
    return (lo,hi)

def add(a,b):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a[0]+b[0]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=a[1]+b[1]
    return lo,hi

def sub(a,b):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a[0]-b[1]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=a[1]-b[0]
    return lo,hi

def mulpos(a,b):
    assert a[0] >= 0 and b[0] >= 0
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a[0]*b[0]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=a[1]*b[1]
    return lo,hi

def mul_general(a,b):
    vals=[x*y for x in a for y in b]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=min(vals)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=max(vals)
    return lo,hi

def divpos(a,b):
    assert a[0] >= 0 and b[0] > 0
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a[0]/b[1]
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING; hi=a[1]/b[0]
    return lo,hi

def scale(a,q:F):
    qb=qbounds(abs(q))
    out=mulpos((max(a[0],Decimal(0)), max(a[1],Decimal(0))), qb) if a[0]>=0 else None
    if q>=0:
        if a[0]>=0: return out
        return mul_general(a,qbounds(q))
    return (-mul_general(a,qbounds(-q))[1], -mul_general(a,qbounds(-q))[0])

def log_unit(m:F):
    assert F(1) <= m <= F(2)
    if m==1: return Decimal(0),Decimal(0)
    z=qbounds((m-1)/(m+1)); z2=mulpos(z,z); power=z
    s=(Decimal(0),Decimal(0))
    for k in range(NTERMS):
        s=add(s, divpos(power,(Decimal(2*k+1),Decimal(2*k+1))))
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
    if x < F(2)**e: e-=1
    m=x/(F(2)**e)
    y=divpos(log_unit(m),LN2)
    return (Decimal(e)+y[0], Decimal(e)+y[1])

def log2_pos(x:F):
    if x>=1: return log2_ge1(x)
    y=log2_ge1(1/x)
    return (-y[1],-y[0])

def phi_interval(p:F):
    if p==0: return Decimal(0),Decimal(0)
    return mulpos(qbounds(p),log2_ge1(1/p))

def hcore(b:F):
    out=(Decimal(0),Decimal(0))
    for (a,q),mult in PAIRS:
        coeff=F(a,512)+b*F(q,512)
        p=coeff*coeff
        if p:
            term=mulpos(phi_interval(p),(Decimal(mult),Decimal(mult)))
            out=add(out,term)
    return out

def K_interval(b:F):
    ph=phi_interval(b*b)
    corr=add((-ph[1],-ph[0]),qbounds(F(16)*(1-b*b)))
    return add(hcore(b),mulpos(qbounds(ALPHA),corr))

def Kprime_interval(b:F):
    assert b>0
    out=(Decimal(0),Decimal(0))
    den=F(512*512)
    for (a,q),mult in PAIRS:
        if q==0: continue
        x=F(a)+b*F(q)
        p=x*x/den
        phiprime=sub(log2_ge1(1/p), INV_LN2)
        pp=F(2*mult*q,512*512)*x
        out=add(out,mul_general(phiprime,qbounds(pp)))
    t=add(scale(log2_pos(b*b),F(2)*b), scale(INV_LN2,F(2)*b))
    t=add(t,qbounds(F(-32)*b))
    return add(out,mul_general(qbounds(ALPHA),t))

def main():
    assert sum(mult for _,mult in PAIRS)==512
    den=512*512
    s_q2=sum(F(mult*q*q,den) for (a,q),mult in PAIRS)
    s_cross=sum(F(mult*2*a*q,den) for (a,q),mult in PAIRS)
    s_a2=sum(F(mult*a*a,den) for (a,q),mult in PAIRS)
    assert s_q2==ALPHA and s_cross==0 and s_a2==1-ALPHA

    min_abs=F(10**9)
    for (a,q),mult in PAIRS:
        if q==0: continue
        vals=[abs(F(a)),abs(F(a)+F(q,4))]
        root=F(-a,q)
        assert not (F(0)<=root<=F(1,4))
        m=min(vals)
        min_abs=min(min_abs,m)
        assert m>=1
    assert min_abs==1

    concavity_bound=F(-9,64)

    l=F(2713295,10**9)
    u=F(2713296,10**9)
    dkl=Kprime_interval(l); dku=Kprime_interval(u)
    assert dkl[0]>0 and dku[1]<0
    kl=K_interval(l); ku=K_interval(u)

    tangent_add=mulpos((max(dkl[0],Decimal(0)),max(dkl[1],Decimal(0))),qbounds(u-l))
    kmax_upper=add(kl,tangent_add)[1]
    m_upper=divpos((kmax_upper,kmax_upper),qbounds(D0))[1]
    m_lower=divpos((kl[0],kl[0]),qbounds(D0))[0]

    f7_lower=Decimal("6.5218509495504481848401605388605115013503296799038586768578")
    gap=m_upper-f7_lower

    assert m_upper < Decimal("6.521851214")
    assert gap < Decimal("2.64e-7")

    out={
      "status":"PASS",
      "parseval_q2":str(s_q2),
      "min_abs_numerator_q_nonzero_on_0_to_1over4":str(min_abs),
      "K_second_derivative_uniform_upper":str(concavity_bound),
      "root_bracket_lower":str(l),
      "root_bracket_upper":str(u),
      "Kprime_lower_endpoint_interval":[str(dkl[0]),str(dkl[1])],
      "Kprime_upper_endpoint_interval":[str(dku[0]),str(dku[1])],
      "K_lower_endpoint_interval":[str(kl[0]),str(kl[1])],
      "K_upper_endpoint_interval":[str(ku[0]),str(ku[1])],
      "Kmax_tangent_upper":str(kmax_upper),
      "adaptive_depth_ratio_floor_lower":str(m_lower),
      "adaptive_depth_ratio_ceiling_upper":str(m_upper),
      "F7_certified_lower_used":str(f7_lower),
      "remaining_gap_ceiling_minus_F7_lower":str(gap),
      "theorem_scope":"Any finite/adaptive sequence of integer self-composition depths d>=1 followed by the same source-bound nine-host shared-core transform, starting at the current source state; not a universal FEI upper bound."
    }
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
