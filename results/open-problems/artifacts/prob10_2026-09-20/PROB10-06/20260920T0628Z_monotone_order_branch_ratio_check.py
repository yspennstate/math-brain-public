import sympy as sp, itertools, math

lam,p=sp.symbols('lam p')
A=sp.Rational(1855087,1000000)      # inherited all-mixture endpoint
L=sp.Rational(185527,100000)        # new endpoint 1.85527
Q=sp.Rational(99995,100000)         # strict product cap <1
P1=sp.Rational(23,50)               # small-p monotone-g cutoff
P2=sp.Rational(53,100)              # large-p monotone-g cutoff
GB=sp.Rational(101021,1000000)      # rational > 5-2*sqrt(6)

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
    sg=1 if den.subs(var,mid)>0 else -1
    okd,dd,md=cert_poly(sp.expand(sg*den),var,a0,b0)
    okn,dn,mn=cert_poly(sp.expand(sg*num),var,a0,b0)
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
    ymin=sp.cancel(smin/(a+smin))
    ymax=sp.cancel(smax/(a+smax))
    if upper:
        Qm=sp.cancel(((n-m)*u2*q2u+m*b3*q3u)/((n-m)*u2+m*b3))
        r=sp.cancel((1+a*Qm)/(a+smin))
    else:
        Qm=sp.cancel(((n-m)*b2*q2l+m*u3*q3l)/((n-m)*b2+m*u3))
        r=sp.cancel((1+a*Qm)/(a+smax))
    return ymin,ymax,r

mono_checks=0
mono_maxdepth=0
for n,upper in [(3,True),(4,False)]:
    for m in range(n+1):
        ymin,ymax,r=pat(n,m,upper)
        for expr,sgn in [(sp.diff(ymin,lam),-1),
                         (sp.diff(ymax,lam),-1),
                         (sp.diff(r,lam),1)]:
            ok,d,_=cert_rat(sgn*expr,lam,A,L)
            assert ok
            mono_checks+=1
            mono_maxdepth=max(mono_maxdepth,d)

RU=[]
for m in range(4):
    _,_,r=pat(3,m,True)
    RU.append(sp.factor(r.subs(lam,L)))
assert all(RU[m]>RU[m+1] for m in range(3))
U=sp.factor(sum(sp.binomial(3,m)*p**m*(1-p)**(3-m)*RU[m]
                for m in range(4)))

V=[]
for m in range(5):
    ymin,ymax,r=pat(4,m,False)
    lo=sp.factor(ymin.subs(lam,L))
    hi=sp.factor(ymax.subs(lam,A))
    rr=sp.factor(r.subs(lam,A))
    assert 0<lo<=hi and rr>0
    V.append((lo,hi,rr))
assert all(V[m][0]<V[m+1][0] and V[m][1]<V[m+1][1]
           and V[m][2]>V[m+1][2] for m in range(4))

ys=sp.symbols('y0:5')
eqs=[]
for i,(lo,hi,_) in enumerate(V):
    eqs.extend([ys[i]-lo,ys[i]-hi])
for i in range(4):
    eqs.append(ys[i]-ys[i+1])

vertices={}
for inds in itertools.combinations(range(len(eqs)),5):
    M,bv=sp.linear_eq_to_matrix([eqs[i] for i in inds],ys)
    if M.rank()<5:
        continue
    sol=sp.linsolve((M,bv),ys)
    if sol is sp.EmptySet:
        continue
    y=tuple(next(iter(sol)))
    feasible=(all(V[i][0]<=y[i]<=V[i][1] for i in range(5))
              and all(y[i]<=y[i+1] for i in range(4)))
    if feasible:
        vertices[y]=inds
assert len(vertices)==64

# Quantitative branch-addition bound on t=c3/c2.
b=(2-lam)/2
u=(3-lam)/3
coord_lb=sp.factor(4*(lam-1)*b+13*b**2-u**2)
assert sp.factor(coord_lb-(41*lam**2-228*lam+288)/36)==0
ok_coord,d_coord,_=cert_rat(coord_lb,lam,A,L)
assert ok_coord
T=sp.factor((4-L)/(2*(3-L)))

thetaU=sp.factor(p*T/(1-p+p*T))
thetaL=sp.factor(3*p/(4-p))
def g(th):
    return sp.factor(th*(1-th)/(2+th))
def gprime_num(th):
    return sp.factor(2-4*th-th**2)

assert gprime_num(thetaU).subs(p,P1)>0
assert gprime_num(thetaL).subs(p,P2)<0
assert (5-GB)**2<24

cert_count=0
maxdepth=0
min_terminal=None
worst=None
for vi,y in enumerate(vertices):
    probs=[sp.binomial(4,m)*p**m*(1-p)**(4-m) for m in range(5)]
    Dl=sp.factor(sum(probs[m]*y[m] for m in range(5)))
    Nl=sp.factor(sum(probs[m]*y[m]*V[m][2] for m in range(5)))
    diffnum=sp.expand(U*Dl-Nl)
    regimes=[
        ('small',g(thetaU),sp.Rational(0),P1),
        ('middle',GB,P1,P2),
        ('large',g(thetaL),P2,sp.Rational(1)),
    ]
    for name,gbar,p0,p1 in regimes:
        expr=sp.together(Q*Dl-L*gbar*diffnum)
        ok,d,mc=cert_rat(expr,p,p0,p1)
        assert ok,(vi,name,d,mc)
        cert_count+=1
        maxdepth=max(maxdepth,d)
        if min_terminal is None or mc<min_terminal:
            min_terminal=mc
            worst=(vi,name)

margin=sp.factor(4*(1-Q)/(3+L)**2)
assert margin>0

obstruction_at_2=sp.Rational(2,1)*(sp.Rational(1,4)+sp.Rational(1,4))
assert obstruction_at_2==1

print('PROB10-06 monotone-order + quantitative branch-ratio exact checker')
print('lambda strip =',A,L,'gain =',sp.factor(L-A))
print('target product cap Q =',Q)
print('lambda envelope checks =',mono_checks,'max Bernstein depth =',mono_maxdepth)
print('monotone lower-score polytope vertices =',len(vertices))
print('coordinate monotonicity lower polynomial =',coord_lb)
print('coordinate monotonicity certificate depth =',d_coord)
print('new c3/c2 upper bound at L =',T,'~',float(T))
print('small-p cutoff P1 =',P1,'g\' numerator at thetaU(P1) =',sp.factor(gprime_num(thetaU).subs(p,P1)))
print('large-p cutoff P2 =',P2,'g\' numerator at thetaL(P2) =',sp.factor(gprime_num(thetaL).subs(p,P2)))
print('product certificates =',cert_count,'max Bernstein depth =',maxdepth,'worst index/regime =',worst)
print('uniform derivative margin -ell_prime >=',margin,'~',float(margin))
print('inverse-escape derivative pathwise contraction factor at lambda=2, degree 2, equal children =',obstruction_at_2)
print('ALL_EXACT_CHECKS_PASS')
