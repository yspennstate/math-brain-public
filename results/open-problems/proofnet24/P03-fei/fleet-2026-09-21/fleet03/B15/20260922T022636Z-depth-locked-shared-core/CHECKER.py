from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN, getcontext
from fractions import Fraction as F

PREC=70
WORK=90
getcontext().prec=PREC
ALPHA=F(9,256)
D0=F(133,128)
PAIRS=[
((-18,-2),72),((2,2),72),((0,0),46),((-16,0),36),((16,0),36),((10,-6),36),
((4,4),36),((-4,-4),36),((-2,-2),36),((44,-4),18),((-44,4),18),((-6,10),18),
((38,6),12),((114,2),9),((8,8),9),((-8,-8),9),((4,-12),6),((-4,12),6),((2,18),1)]
PAD=Decimal('1e-65')
LN2=None

def qiv(q:F):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR
        lo=Decimal(q.numerator)/Decimal(q.denominator)
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING
        hi=Decimal(q.numerator)/Decimal(q.denominator)
    return (lo,hi)

def iv_add(x,y):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR; lo=x[0]+y[0]
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING; hi=x[1]+y[1]
    return lo,hi

def iv_sub(x,y):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR; lo=x[0]-y[1]
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING; hi=x[1]-y[0]
    return lo,hi

def iv_mul(x,y):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR
        lo=min(a*b for a in x for b in y)
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING
        hi=max(a*b for a in x for b in y)
    return lo,hi

def iv_scale(x,q:F):
    return iv_mul(x,qiv(q))

def iv_pow_pos(x,n):
    out=(Decimal(1),Decimal(1));base=x
    while n:
        if n&1: out=iv_mul(out,base)
        base=iv_mul(base,base); n//=2
    return out

def ln_point(x:Decimal):
    assert x>0
    with localcontext() as c:
        c.prec=WORK;c.rounding=ROUND_HALF_EVEN
        y=x.ln()
    # Decimal ln is correctly rounded; pad much more than one WORK-precision ulp.
    return (+(y-PAD), +(y+PAD))

with localcontext() as c:
    c.prec=WORK;c.rounding=ROUND_HALF_EVEN
    _ln2=Decimal(2).ln()
LN2=(+(_ln2-PAD), +(_ln2+PAD))

def div_pos(x,y):
    assert x[0]>=0 and y[0]>0
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR; lo=x[0]/y[1]
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING; hi=x[1]/y[0]
    return lo,hi

def phi_point(x:Decimal):
    if x==0: return (Decimal(0),Decimal(0))
    ln=ln_point(x)
    negln=(-ln[1],-ln[0])
    lg=div_pos(negln,LN2)
    return iv_mul((x,x),lg)

def phi_iv(p):
    # All source masses here are below 1/e, so phi is increasing.
    assert p[0]>=0 and p[1] < Decimal('0.2')
    return (phi_point(p[0])[0],phi_point(p[1])[1])

def square_iv(x):
    lo,hi=x
    if lo<=0<=hi:
        lower=Decimal(0)
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_CEILING
            upper=max(lo*lo,hi*hi)
        return lower,upper
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR
        lower=min(lo*lo,hi*hi)
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING
        upper=max(lo*lo,hi*hi)
    return lower,upper

def hcore_iv(b):
    out=(Decimal(0),Decimal(0))
    for (a,q),mult in PAIRS:
        coeff=iv_add(qiv(F(a,512)),iv_scale(b,F(q,512)))
        p=square_iv(coeff)
        if p[1]==0: continue
        term=phi_iv(p)
        out=iv_add(out,iv_scale(term,F(mult,1)))
    return out

def K_iv(b):
    b2=iv_pow_pos(b,2)
    ph=phi_iv(b2)
    negphi=(-ph[1],-ph[0])
    one_minus=iv_sub((Decimal(1),Decimal(1)),b2)
    bracket=iv_add(negphi,iv_scale(one_minus,F(16,1)))
    return iv_add(hcore_iv(b),iv_scale(bracket,ALPHA))

def main():
    c1=F(14593,65536)
    c_exact=F(57,256)+c1**4/F(256)
    for _ in range(5):
        c_exact=F(57,256)+c_exact**4/F(256)
    c=qiv(c_exact)
    assert c[1] < Decimal('0.25')
    rlo=Decimal('6.5218509495504481848401605388605115013503296799038586768578')-Decimal('1e-58')
    rhi=Decimal('6.5218509495504481848401605388605115013503296832418414558148')+Decimal('1e-58')
    R=(rlo,rhi)
    threshold=iv_scale(R,D0)
    results={}
    for d in range(1,15):
        b=iv_pow_pos(c,d)
        N=iv_sub(K_iv(b),threshold)
        results[d]=N
        if d==4: assert N[0]>0
        else: assert N[1]<0

    N0=iv_sub(K_iv((Decimal(0),Decimal(0))),threshold)
    assert N0[1] < Decimal('-0.000005')
    # For b<=2^-30: |Hcore'|<=185.625 from |q|<=18, |a+bq|<=132,
    # p>=2^-18 for nonzero terms and |phi'(p)|<20.
    # The alpha correction contributes <0.001, so |K'|<186.
    tail_b=Decimal(2) ** Decimal(-30)
    motion=Decimal(186)*tail_b
    assert motion < Decimal('0.0000002')
    assert N0[1]+motion<0
    print("PASS")
    print("c7_upper",c[1])
    for d in range(1,15):
        lo,hi=results[d]
        print(d,lo,hi,"POS" if lo>0 else "NEG")
    print("N0_upper",N0[1])
    print("tail_motion",motion)
    print("all_integer_d_ge_15_negative=True")
    print("unique_positive_integer_depth=4")
    print("full_FEI_status=OPEN")
    print("brain_status=WITHOUT_VERIFIED_BRAIN")
if __name__=="__main__": main()
