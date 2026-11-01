import sympy as sp, itertools, math
lam,p=sp.symbols('lam p')
LAM_SPLITS=[(sp.Rational(1851,1000),sp.Rational(18539,10000))]
PS=sp.Rational(449,1000)
GB=sp.Rational(101021,1000000)
Q=sp.Rational(9999,10000)

def bernstein_coeffs(poly,var):
    P=sp.Poly(sp.expand(poly),var,domain=sp.QQ)
    n=P.degree()
    aa=[P.nth(k) for k in range(n+1)]
    out=[]
    for j in range(n+1):
        s=sp.Rational(0)
        for k in range(j+1):
            s += aa[k]*sp.Rational(math.comb(j,k),math.comb(n,k))
        out.append(s)
    return out

def cert_poly(poly,var,a0,b0,depth=0,maxdepth=18):
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
    if mc>0: return True,depth,mc
    if depth>=maxdepth: return False,depth,mc
    mid=(a0+b0)/2
    ok1,d1,m1=cert_poly(poly,var,a0,mid,depth+1,maxdepth)
    if not ok1:return False,d1,m1
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
    ymin=sp.cancel(smin/(a+smin)); ymax=sp.cancel(smax/(a+smax))
    if upper:
        Qm=sp.cancel(((n-m)*u2*q2u+m*b3*q3u)/((n-m)*u2+m*b3))
        r=sp.cancel((1+a*Qm)/(a+smin))
    else:
        Qm=sp.cancel(((n-m)*b2*q2l+m*u3*q3l)/((n-m)*b2+m*u3))
        r=sp.cancel((1+a*Qm)/(a+smax))
    return ymin,ymax,r

# exact p-split and global g bound
assert (PS+2)**2 < 6 # PS < sqrt(6)-2
assert (5-GB)**2 < 24 # GB > 5-2sqrt(6)=max g

allstats=[]
for strip,(A,L) in enumerate(LAM_SPLITS,1):
    # monotonicity
    for n,upper in [(3,True),(4,False)]:
        for m in range(n+1):
            ymin,ymax,r=pat(n,m,upper)
            for name,expr,sgn in [('ymin',sp.diff(ymin,lam),-1),('ymax',sp.diff(ymax,lam),-1),('r',sp.diff(r,lam),1)]:
                ok,d,mc=cert_rat(sgn*expr,lam,A,L)
                assert ok,(strip,n,m,name,d,mc)
    def constants(n,upper):
        z=[]
        for m in range(n+1):
            ymin,ymax,r=pat(n,m,upper)
            lo=sp.factor(ymin.subs(lam,L)); hi=sp.factor(ymax.subs(lam,A))
            rr=sp.factor(r.subs(lam,L if upper else A))
            assert 0<lo<=hi and rr>0
            z.append((lo,hi,rr))
        return z
    U=constants(3,True); V=constants(4,False)
    def corners(n,C):
        arr=[]
        for bits in itertools.product([0,1],repeat=n+1):
            num=sp.Rational(0); den=sp.Rational(0)
            for m,(lo,hi,r) in enumerate(C):
                x=hi if bits[m] else lo
                pr=sp.binomial(n,m)*p**m*(1-p)**(n-m)
                num += pr*x*r; den += pr*x
            arr.append((sp.factor(num),sp.factor(den)))
        return arr
    UC=corners(3,U); VC=corners(4,V)
    cnt=0; maxdepth=0; minbern=None; worst=None
    for i,(Nu,Du) in enumerate(UC):
        for j,(Nl,Dl) in enumerate(VC):
            diff=sp.expand(Nu*Dl-Nl*Du)
            # p <= PS: g(theta)<=g(p)=p(1-p)/(2+p)
            polyS=sp.expand(Q*(2+p)*Du*Dl - L*p*(1-p)*diff)
            ok,d,mb=cert_poly(polyS,p,sp.Rational(0),PS,maxdepth=18)
            assert ok,('small',strip,i,j,d,mb)
            if minbern is None or mb<minbern: minbern=mb; worst=('small',i,j)
            maxdepth=max(maxdepth,d)
            # p >= PS: g(theta)<=GB
            polyL=sp.expand(Q*Du*Dl - L*GB*diff)
            ok,d,mb=cert_poly(polyL,p,PS,sp.Rational(1),maxdepth=18)
            assert ok,('large',strip,i,j,d,mb)
            if mb<minbern: minbern=mb; worst=('large',i,j)
            maxdepth=max(maxdepth,d)
            cnt+=2
    allstats.append((strip,A,L,cnt,maxdepth,minbern,worst))

L=sp.Rational(18539,10000)

# Two backup-route obstruction checks.
# (B) A naive derivative-level copy of the branch-addition 3/4 lower ratio fails.
# For deterministic child escape x=(3-L)/3 (the regular-degree-3 escape value),
# equal logarithmic derivatives q cancel from h3/h2, leaving ((a+3x)/(a+4x))^2.
x=(3-L)/3
aL=L-1
h_ratio=sp.factor(((aL+3*x)/(aL+4*x))**2)
assert h_ratio < sp.Rational(3,4)

# (C) Type-sensitive first-generation B-error contraction still fails centrally.
# At p=449/1000, use type-specific lower escape bounds in the exact 2x2
# Lipschitz matrix for conditional parent types 2 and 3. det(I-M)<0 implies rho(M)>1.
P0=PS
b2L=(2-L)/2
b3L=3*(2-L)/(6-L)
M=sp.zeros(2,2)
for ri,k in enumerate([2,3]):
    for m in range(k+1):
        prob=sp.binomial(k,m)*P0**m*(1-P0)**(k-m)
        S=(k-m)*b2L+m*b3L
        Acoef=L/(L+S)**2
        M[ri,0]+=prob*Acoef*(k-m)
        M[ri,1]+=prob*Acoef*m
det_I_minus_M=sp.factor((sp.eye(2)-M).det())
assert det_I_minus_M < 0

margin=sp.factor(4*(1-Q)/(3+L)**2)
assert margin>0
print('PROB10-06 global coupled p-theta checker')
print('p split =',PS,'; GB =',GB,'; target product <=',Q)
for rec in allstats:
    print('strip',rec[0],rec[1],rec[2],'certificates',rec[3],'maxdepth',rec[4],'worst',rec[6])
    print(' smallest terminal Bernstein coeff =',rec[5])
print('uniform derivative margin -ell_prime >=',margin,'~',float(margin))
print('naive derivative branch-addition obstruction h3/h2 =',h_ratio,'~',float(h_ratio),'< 3/4')
print('type-sensitive truncation obstruction det(I-M) =',det_I_minus_M,'~',float(det_I_minus_M),'< 0')
print('ALL_EXACT_CHECKS_PASS')
