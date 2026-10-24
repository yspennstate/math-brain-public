import sympy as sp, itertools, math

lam,p=sp.symbols('lam p')
A=sp.Rational(18539,10000)            # inherited endpoint 1.8539
L=sp.Rational(1855087,1000000)        # new endpoint 1.855087
PS=sp.Rational(449,1000)
GB=sp.Rational(101021,1000000)         # > max g = 5-2sqrt(6)
Q=sp.Rational(999998,1000000)          # target lambda*g(theta)*Delta <= Q < 1


def cert_poly(poly,var,a0,b0,depth=0,maxdepth=20):
    t=sp.symbols('_t')
    q=sp.Poly(sp.expand(poly.subs(var,a0+(b0-a0)*t)),t,domain=sp.QQ)
    n=q.degree()
    aa=[q.nth(k) for k in range(n+1)]
    coeff=[]
    for j in range(n+1):
        s=sp.Rational(0)
        for k in range(j+1):
            s += aa[k]*sp.Rational(math.comb(j,k),math.comb(n,k))
        coeff.append(s)
    mc=min(coeff)
    if mc>0:
        return True,depth,mc
    if depth>=maxdepth:
        return False,depth,mc
    mid=(a0+b0)/2
    ok1,d1,m1=cert_poly(poly,var,a0,mid,depth+1,maxdepth)
    if not ok1:
        return False,d1,m1
    ok2,d2,m2=cert_poly(poly,var,mid,b0,depth+1,maxdepth)
    return ok2,max(d1,d2),min(m1,m2)


def cert_rat(expr,var,a0,b0):
    num,den=sp.together(expr).as_numer_denom()
    mid=(a0+b0)/2
    dv=den.subs(var,mid)
    s=1 if dv>0 else -1
    okd,dd,md=cert_poly(sp.expand(s*den),var,a0,b0)
    okn,dn,mn=cert_poly(sp.expand(s*num),var,a0,b0)
    return okd and okn,max(dd,dn),min(md,mn)


# Consumed type-conditioned escape/elasticity envelopes.
a=lam-1
b2=(2-lam)/2
b3=3*(2-lam)/(6-lam)
u2=2*(3-lam)/(lam+6)
u3=(3-lam)/3
q2u=1/(2-lam)
q3u=4/((2-lam)*(6-lam))
q2l=9/((3-lam)*(lam+6))
q3l=1/(3-lam)


def pat(n,m,upper):
    smin=(n-m)*b2+m*b3
    smax=(n-m)*u2+m*u3
    ymin=sp.cancel(smin/(a+smin))
    ymax=sp.cancel(smax/(a+smax))
    if upper:
        Qm=sp.cancel(((n-m)*u2*q2u+m*b3*q3u)/((n-m)*u2+m*b3))
        r=sp.cancel((1+a*Qm)/(a+smin))
    else:
        Qm=sp.cancel(((n-m)*b2*q2l+m*u3*q3l)/((n-m)*b2+m*u3))
        r=sp.cancel((1+a*Qm)/(a+smax))
    return ymin,ymax,r


# Existing p--theta/g bounds used unchanged.
assert (PS+2)**2 < 6                # PS < sqrt(6)-2
assert (5-GB)**2 < 24               # GB > 5-2sqrt(6) = max g

# Freeze the rational pattern envelopes uniformly on the new lambda strip.
mono_checks=0
mono_maxdepth=0
mono_minbern=None
for n,upper in [(3,True),(4,False)]:
    for m in range(n+1):
        ymin,ymax,r=pat(n,m,upper)
        for name,expr,sgn in [
            ('ymin',sp.diff(ymin,lam),-1),
            ('ymax',sp.diff(ymax,lam),-1),
            ('r',sp.diff(r,lam),1),
        ]:
            ok,d,mc=cert_rat(sgn*expr,lam,A,L)
            assert ok,(n,m,name,d,mc)
            mono_checks += 1
            mono_maxdepth=max(mono_maxdepth,d)
            mono_minbern=mc if mono_minbern is None or mc<mono_minbern else mono_minbern

# Attack A: upper h2/c2 compression.  R_m^U is decreasing in the type-3 count m.
RU=[]
for m in range(4):
    _,_,r=pat(3,m,True)
    RU.append(sp.factor(r.subs(lam,L)))
RU_gaps=[sp.factor(RU[m]-RU[m+1]) for m in range(3)]
assert all(g>0 for g in RU_gaps)

# By the proved stochastic-order lemma in the report, the actual conditional
# escape weights Y_m are nondecreasing in m. Reverse Chebyshev therefore gives
# h2/c2 <= U(p) below.
U=sp.factor(sum(sp.binomial(3,m)*p**m*(1-p)**(3-m)*RU[m]
                for m in range(4)))

# Keep the lower h3/c3 side fully conservative.  Each actual conditional weight
# lies in [lo_m,hi_m], and the lower score is at least RL_m.  A linear-fractional
# function on this box attains its minimum at a vertex, so enumerate all 32.
V=[]
for m in range(5):
    ymin,ymax,r=pat(4,m,False)
    lo=sp.factor(ymin.subs(lam,L))
    hi=sp.factor(ymax.subs(lam,A))
    rr=sp.factor(r.subs(lam,A))
    assert 0<lo<=hi and rr>0
    V.append((lo,hi,rr))

cert_count=0
maxdepth=0
minbern=None
worst=None
for bits in itertools.product([0,1],repeat=5):
    Nl=sp.Rational(0)
    Dl=sp.Rational(0)
    for m,(lo,hi,r) in enumerate(V):
        x=hi if bits[m] else lo
        pr=sp.binomial(4,m)*p**m*(1-p)**(4-m)
        Nl += pr*x*r
        Dl += pr*x
    diff=sp.expand(U*Dl-Nl)

    # p <= PS: theta<=p<sqrt(6)-2, hence g(theta)<=g(p)=p(1-p)/(2+p).
    polyS=sp.expand(Q*(2+p)*Dl - L*p*(1-p)*diff)
    ok,d,mb=cert_poly(polyS,p,sp.Rational(0),PS,maxdepth=20)
    assert ok,('small',bits,d,mb)
    cert_count+=1
    maxdepth=max(maxdepth,d)
    if minbern is None or mb<minbern:
        minbern=mb
        worst=('small',bits)

    # p >= PS: use the rational global majorant GB > max g.
    polyL=sp.expand(Q*Dl - L*GB*diff)
    ok,d,mb=cert_poly(polyL,p,PS,sp.Rational(1),maxdepth=20)
    assert ok,('large',bits,d,mb)
    cert_count+=1
    maxdepth=max(maxdepth,d)
    if mb<minbern:
        minbern=mb
        worst=('large',bits)

# Uniform derivative margin from
# -ell' = 2(2+theta)(1-product)/(2+theta+lambda)^2,
# using 2(2+theta)>=4 and denominator <=(3+L)^2.
margin=sp.factor(4*(1-Q)/(3+L)**2)
assert margin>0

# Attack C falsification: adding a child need not lower the logarithmic
# derivative elasticity R=-B'/B, even inside the exact regular-tree envelope.
LC=sp.Rational(371,200)  # 1.855, inside the certified strip
b_hi=1-LC/3
b_lo=1-LC/2
r_lo=1/(3-LC)
r_hi=1/(2-LC)

def R_vertex(xs,rs):
    S=sum(xs)
    W=sum(x*r for x,r in zip(xs,rs))/S
    return sp.factor((1+LC*W)/(LC+S))

R2=R_vertex([b_hi,b_hi],[r_lo,r_lo])
R3=R_vertex([b_hi,b_hi,b_lo],[r_lo,r_lo,r_hi])
Rgap=sp.factor(R3-R2)
assert Rgap>0

print('PROB10-06 pattern-order bridge exact checker')
print('lambda strip =',A,L,'gain =',sp.factor(L-A))
print('target product Q =',Q)
print('lambda-envelope monotonicity checks =',mono_checks,
      'maxdepth =',mono_maxdepth,'min terminal Bernstein coeff =',mono_minbern)
print('upper score R_m(L) =',RU)
print('upper score decreasing gaps =',RU_gaps)
print('lower-box product certificates =',cert_count,
      'maxdepth =',maxdepth,'worst =',worst)
print('smallest product-certificate terminal Bernstein coeff =',minbern)
print('uniform derivative margin -ell_prime >=',margin,'~',float(margin))
print('Attack-C pathwise derivative-order counterexample at lambda =',LC)
print('R_before =',R2,'~',float(R2))
print('R_after  =',R3,'~',float(R3))
print('R_after-R_before =',Rgap,'~',float(Rgap),'> 0')
print('ALL_EXACT_CHECKS_PASS')
