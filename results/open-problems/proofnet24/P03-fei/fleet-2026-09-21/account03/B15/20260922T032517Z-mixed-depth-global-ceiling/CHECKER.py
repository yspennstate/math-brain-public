from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN, getcontext
from fractions import Fraction as F

PREC=80
WORK=110
getcontext().prec=PREC
ALPHA=F(9,256)
D0=F(133,128)
A0=F(57,256)
CMAX=F(57,255)
CMIN=A0
PAIRS=[
((-18,-2),72),((2,2),72),((0,0),46),((-16,0),36),((16,0),36),((10,-6),36),
((4,4),36),((-4,-4),36),((-2,-2),36),((44,-4),18),((-44,4),18),((-6,10),18),
((38,6),12),((114,2),9),((8,8),9),((-8,-8),9),((4,-12),6),((-4,12),6),((2,18),1)]
PAD=Decimal('1e-90')

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
    vals=[a*b for a in x for b in y]
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR; lo=min(vals)
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING; hi=max(vals)
    return lo,hi

def iv_scale(x,q:F): return iv_mul(x,qiv(q))

def iv_pow_pos(x,n):
    out=(Decimal(1),Decimal(1));base=x
    while n:
        if n&1: out=iv_mul(out,base)
        n//=2
        if n: base=iv_mul(base,base)
    return out

def ln_point(x:Decimal):
    assert x>0
    with localcontext() as c:
        c.prec=WORK;c.rounding=ROUND_HALF_EVEN; y=x.ln()
    return +(y-PAD), +(y+PAD)

with localcontext() as c:
    c.prec=WORK;c.rounding=ROUND_HALF_EVEN; z=Decimal(2).ln()
LN2=(+(z-PAD), +(z+PAD))

def div_pos(x,y):
    assert x[0]>=0 and y[0]>0
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR; lo=x[0]/y[1]
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING; hi=x[1]/y[0]
    return lo,hi

def phi_point(x:Decimal):
    if x==0: return Decimal(0),Decimal(0)
    ln=ln_point(x); negln=(-ln[1],-ln[0]); lg=div_pos(negln,LN2)
    return iv_mul((x,x),lg)

def phi_iv_monotone(p):
    assert p[0]>=0 and p[1] < Decimal('0.2')
    return phi_point(p[0])[0], phi_point(p[1])[1]

def square_iv(x):
    lo,hi=x
    if lo<=0<=hi:
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_CEILING; up=max(lo*lo,hi*hi)
        return Decimal(0),up
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR; low=min(lo*lo,hi*hi)
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING; up=max(lo*lo,hi*hi)
    return low,up

def hcore_iv(b):
    out=(Decimal(0),Decimal(0))
    for (a,q),mult in PAIRS:
        coeff=iv_add(qiv(F(a,512)),iv_scale(b,F(q,512)))
        p=square_iv(coeff)
        if p[1]==0: continue
        term=phi_iv_monotone(p)
        out=iv_add(out,iv_scale(term,F(mult)))
    return out

def K_iv(b):
    b2=iv_pow_pos(b,2)
    ph=phi_iv_monotone(b2) if b2[1]>0 else (Decimal(0),Decimal(0))
    negphi=(-ph[1],-ph[0])
    one_minus=iv_sub((Decimal(1),Decimal(1)),b2)
    bracket=iv_add(negphi,iv_scale(one_minus,F(16)))
    return iv_add(hcore_iv(b),iv_scale(bracket,ALPHA))

def log2_inv_iv_pos(x):
    assert x[0]>0
    # -ln(x)/ln2; decreasing in x.
    ln_lo=ln_point(x[0]); ln_hi=ln_point(x[1])
    negln=(-ln_hi[1], -ln_lo[0])
    assert negln[0]>=0
    return div_pos(negln, LN2)

def phi_prime_iv(p):
    # phi'(p)=log2(1/p)-1/ln2, p positive.
    assert p[0]>0
    loginv=log2_inv_iv_pos(p)
    invln2=div_pos((Decimal(1),Decimal(1)),LN2)
    return iv_sub(loginv,invln2)

def Kprime_iv(b):
    # interval for derivative on a positive b interval. Splits coefficient classes where needed.
    out=(Decimal(0),Decimal(0))
    for (a,q),mult in PAIRS:
        if q==0: continue
        coeff=iv_add(qiv(F(a,512)),iv_scale(b,F(q,512)))
        p=square_iv(coeff)
        if p[0]==0:
            # zero class may be identically zero (a=q=0); otherwise shouldn't cross zero on our intervals
            if a==0 and q==0: continue
            raise AssertionError((a,q,b,coeff))
        pp=phi_prime_iv(p)
        dp=iv_scale(coeff,F(2*q,512))
        out=iv_add(out,iv_scale(iv_mul(pp,dp),F(mult)))
    # derivative alpha[-phi(b^2)+16(1-b^2)]: alpha[-2b phi'(b^2)-32b]
    b2=iv_pow_pos(b,2)
    ppb=phi_prime_iv(b2)
    t=iv_add(iv_scale(iv_mul(b,ppb),F(-2)),iv_scale(b,F(-32)))
    return iv_add(out,iv_scale(t,ALPHA))

def target_iv(c,d):
    b=iv_pow_pos(c,d)
    return iv_scale(K_iv(b),F(128,133))

def main():
    cmin=qiv(CMIN); cmax=qiv(CMAX)
    assert cmin[0]>0 and cmax[1]<1
    # invariant: a+c^d/256 stays in [a, a+a/255]=[a,57/255]
    # because c^d <= c <= cmax.
    nxt_max=iv_add(cmin,iv_scale(cmax,F(1,256)))
    assert nxt_max[1] <= cmax[1]

    # Derivative sign of K over b-ranges corresponding to d=1..14.
    best=None; rows=[]
    for d in range(1,15):
        br=(iv_pow_pos(cmin,d)[0],iv_pow_pos(cmax,d)[1])
        kp=Kprime_iv(br)
        if kp[1]<0:
            evalc=cmin; loc='cmin'
        elif kp[0]>0:
            evalc=cmax; loc='cmax'
        else:
            raise AssertionError(('undecided derivative',d,kp))
        t=target_iv(evalc,d)
        rows.append((d,br,kp,loc,t))
        if best is None or t[0]>best[1][1]:
            best=(d,t)
    assert best[0]==4
    M=target_iv(cmax,4)
    # all finite other maxima below M
    for d,br,kp,loc,t in rows:
        if d!=4: assert t[1] < M[0]

    # Analytic d>=15 tail: b<=cmax^15, use old valid uniform |K'|<186 near zero.
    b15=iv_pow_pos(cmax,15)[1]
    assert b15 < Decimal(2) ** Decimal(-30)
    K0=K_iv((Decimal(0),Decimal(0)))
    tailK=(K0[0]-Decimal(186)*b15, K0[1]+Decimal(186)*b15)
    tailT=iv_scale(tailK,F(128,133))
    assert tailT[1] < M[0]

    # F7 predecessor interval, widened as in inherited certificate.
    r7lo=Decimal('6.5218509495504481848401605388605115013503296799038586768578')
    r7hi=Decimal('6.5218509495504481848401605388605115013503296832418414558148')
    assert r7hi < M[0]
    gap=(M[0]-r7hi, M[1]-r7lo)

    # Convex interpolation coefficient lambda = d0/(alpha I^d+B), <=1 for I>=1.
    # Denominator at I=1 is alpha+B = 133/128 exactly.
    assert ALPHA+F(257,256)==D0

    print('PASS')
    print('reachable_c_interval', str(cmin[0]), str(cmax[1]))
    for d,br,kp,loc,t in rows:
        print('d',d,'Kprime',kp[0],kp[1],'max_at',loc,'target_max',t[0],t[1])
    print('global_target_depth',4)
    print('M_lower',M[0])
    print('M_upper',M[1])
    print('tail_b15_upper',b15)
    print('tail_target_upper',tailT[1])
    print('F7_to_M_gap_lower',gap[0])
    print('F7_to_M_gap_upper',gap[1])
    print('mixed_depth_global_ceiling_proved=True')
    print('full_FEI_status=OPEN')
    print('brain_status=WITHOUT_VERIFIED_BRAIN')

if __name__=='__main__': main()
