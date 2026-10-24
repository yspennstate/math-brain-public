import sympy as sp, itertools, math
lam,p=sp.symbols('lam p')
A=sp.Rational(185527,100000)   # inherited all-mixture endpoint
L=sp.Rational(187,100)         # new moderate-mixture endpoint
P0=sp.Rational(31,200)
P1=sp.Rational(1,4)
Q=sp.Rational(19,20)

def bern_coeffs(poly,var,a0,b0):
    t=sp.symbols('_t')
    q=sp.Poly(sp.expand(poly.subs(var,a0+(b0-a0)*t)),t,domain=sp.QQ)
    n=q.degree(); aa=[q.nth(k) for k in range(n+1)]
    out=[]
    for j in range(n+1):
        s=sp.Rational(0)
        for k in range(j+1):
            s += aa[k]*sp.Rational(math.comb(j,k),math.comb(n,k))
        out.append(s)
    return out

def cert_poly(poly,var,a0,b0,depth=0,maxdepth=20):
    bc=bern_coeffs(poly,var,a0,b0); mc=min(bc)
    if mc>0: return True,depth,mc
    if depth>=maxdepth: return False,depth,mc
    mid=(a0+b0)/2
    ok,d1,m1=cert_poly(poly,var,a0,mid,depth+1,maxdepth)
    if not ok: return False,d1,m1
    ok,d2,m2=cert_poly(poly,var,mid,b0,depth+1,maxdepth)
    return ok,max(d1,d2),min(m1,m2)

def cert_rat(expr,var,a0,b0):
    num,den=sp.cancel(expr).as_numer_denom(); mid=(a0+b0)/2
    s=1 if den.subs(var,mid)>0 else -1
    okd,dd,md=cert_poly(sp.expand(s*den),var,a0,b0)
    if not okd: return False,dd,md
    okn,dn,mn=cert_poly(sp.expand(s*num),var,a0,b0)
    return okn,max(dd,dn),min(md,mn)

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

mono=0; max_mono_depth=0
for n,upper in [(3,True),(4,False)]:
    for m in range(n+1):
        ymin,ymax,r=pat(n,m,upper)
        for expr,sgn in [(sp.diff(ymin,lam),-1),(sp.diff(ymax,lam),-1),(sp.diff(r,lam),1)]:
            ok,d,mc=cert_rat(sgn*expr,lam,A,L)
            assert ok,(n,m,d,mc)
            mono+=1; max_mono_depth=max(max_mono_depth,d)

RU=[]; upper_intervals=[]
for m in range(4):
    ymin,ymax,r=pat(3,m,True)
    lo=sp.factor(ymin.subs(lam,L)); hi=sp.factor(ymax.subs(lam,A)); rr=sp.factor(r.subs(lam,L))
    upper_intervals.append((lo,hi)); RU.append(rr)
assert all(RU[m]>RU[m+1] for m in range(3))
assert max(lo for lo,hi in upper_intervals) <= min(hi for lo,hi in upper_intervals)
U=sp.expand(sum(sp.binomial(3,m)*p**m*(1-p)**(3-m)*RU[m] for m in range(4)))

V=[]
for m in range(5):
    ymin,ymax,r=pat(4,m,False)
    lo=sp.factor(ymin.subs(lam,L)); hi=sp.factor(ymax.subs(lam,A)); rr=sp.factor(r.subs(lam,A))
    V.append((lo,hi,rr))
assert all(V[m][0]<V[m+1][0] and V[m][1]<V[m+1][1] and V[m][2]>V[m+1][2] for m in range(4))
ys=sp.symbols('y0:5'); eqs=[]
for i,(lo,hi,_) in enumerate(V): eqs += [ys[i]-lo,ys[i]-hi]
for i in range(4): eqs.append(ys[i]-ys[i+1])
vertices={}
for inds in itertools.combinations(range(len(eqs)),5):
    M,bv=sp.linear_eq_to_matrix([eqs[i] for i in inds],ys)
    if M.rank()<5: continue
    sol=sp.linsolve((M,bv),ys)
    if sol is sp.EmptySet: continue
    y=tuple(next(iter(sol)))
    if all(V[i][0]<=y[i]<=V[i][1] for i in range(5)) and all(y[i]<=y[i+1] for i in range(4)):
        vertices[y]=inds
assert len(vertices)==64

coord=sp.factor((41*lam**2-228*lam+288)/36)
ok,dc,mc=cert_rat(coord,lam,A,L); assert ok
T=sp.factor((4-L)/(2*(3-L)))
thU=sp.factor(p*T/(1-p+p*T))
g=sp.factor(thU*(1-thU)/(2+thU))
gpnum=sp.factor(2-4*thU-thU**2)
assert gpnum.subs(p,P1)>0

probs=[sp.binomial(4,m)*p**m*(1-p)**(4-m) for m in range(5)]
count=0; maxdepth=0; worst=None; minterm=None
for vi,y in enumerate(vertices):
    D=sp.expand(sum(probs[m]*y[m] for m in range(5)))
    N=sp.expand(sum(probs[m]*y[m]*V[m][2] for m in range(5)))
    expr=sp.factor(Q - L*g*(U-N/D))
    ok,d,mt=cert_rat(expr,p,P0,P1)
    assert ok,(vi,d,mt)
    count+=1; maxdepth=max(maxdepth,d)
    if minterm is None or mt<minterm: minterm=mt; worst=vi

margin=sp.factor(4*(1-Q)/(3+L)**2)
assert margin>0
contract_bound=sp.factor(2*(1-sp.Rational(1,4)/18))
assert contract_bound==sp.Rational(71,36) and contract_bound>1

print('PROB10-06 moderate-p rectangle exact checker')
print('lambda strip =',A,L,'gain over all-mixture endpoint =',sp.factor(L-A))
print('p strip =',P0,P1)
print('product cap Q =',Q)
print('lambda envelope checks =',mono,'max Bernstein depth =',max_mono_depth)
print('upper-order-polytope obstruction: common constant-weight interval =',max(lo for lo,hi in upper_intervals),min(hi for lo,hi in upper_intervals))
print('lower-score vertices =',len(vertices))
print('branch ratio T at L =',T,'~',float(T),'coordinate cert depth =',dc)
print('g-prime numerator at p=1/4 =',sp.factor(gpnum.subs(p,P1)))
print('product certificates =',count,'max depth =',maxdepth,'worst vertex =',worst)
print('uniform new-strip derivative margin >=',margin,'~',float(margin))
print('inverse-moment-only contraction bound at p=1/2, lambda=2 =',contract_bound,'~',float(contract_bound))
print('ALL_EXACT_CHECKS_PASS')
