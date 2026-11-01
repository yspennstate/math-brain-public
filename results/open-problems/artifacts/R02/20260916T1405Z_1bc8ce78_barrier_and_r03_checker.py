#!/usr/bin/env python3
# Exact/symbolic self-check for R02 KLS run 20260916T1405Z_1bc8ce78.
import itertools, math
import sympy as sp

# X002: softmax barrier on the isotropic shifted-exponential product law.
eps,beta,n=sp.symbols('eps beta n', positive=True)
phi=1+sp.log(sp.exp(2*beta*eps)+n-1)/beta
d1=sp.simplify(sp.diff(phi,eps).subs(eps,0))
d2=sp.simplify(sp.diff(phi,eps,2).subs(eps,0))
assert sp.simplify(d1-2/n)==0
assert sp.simplify(d2-4*beta*(n-1)/n**2)==0
gen=sp.simplify(-1+sp.Rational(1,2)*n*d2)
assert sp.simplify(gen-(-1+2*beta*(1-1/n)))==0
L,b=sp.symbols('L b', positive=True)
ratio=sp.simplify((1-L/b)/b)
assert sp.solve(sp.Eq(sp.diff(ratio,b),0),b)==[2*L]
print('X002 PASS', 'D2=',d2, 'generator=',gen, 'opt_beta=',2*L)

# C003: cubic-root barrier z(A), Tr[(A(zI-A)^-1)^3-A(zI-A)^-1]=0.
lam,z=sp.symbols('lam z', positive=True)
q=lam/(z-lam); h=q**3-q
partials=(sp.diff(h,lam).subs({lam:1,z:2}),
          sp.diff(h,z).subs({lam:1,z:2}),
          sp.diff(h,lam,2).subs({lam:1,z:2}),
          sp.diff(h,lam,z).subs({lam:1,z:2}),
          sp.diff(h,z,2).subs({lam:1,z:2}))
assert partials==(4,-2,32,-18,10)
S1,S2,N=sp.symbols('S1 S2 N', positive=True)
zp=2*S1/N; zpp=16*(S2-S1**2/N)/N
ellp=sp.simplify(zp/2); ellpp=sp.simplify(zpp/2-zp**2/4)
assert sp.simplify(ellp-S1/N)==0
assert sp.simplify(ellpp-(8*S2/N-9*S1**2/N**2))==0
print('C003 PASS', 'partials=',partials, 'Dell=',ellp, 'D2ell=',ellpp)

# X003: stationary-filler family; exact symbolic asymptotics.
R=sp.symbols('R', positive=True)
qs=1/sp.sqrt(3); ms=2/(3*sp.sqrt(3)); r=(R**3-R)/ms
lamR=R/(1+R); lams=qs/(1+qs)
def ee(x): return (3*x**2-1)*x*(1+x)
def ss(x): return x*(1+x)
def rr(x): return ss(x)*(1+2*x)
def GG(x): return 6*x*ss(x)**2+(3*x**2-1)*rr(x)
eR=sp.factor(ee(R)); GR=sp.factor(GG(R)); Gs=sp.simplify(GG(qs))
Ito=sp.simplify(2*lamR/eR*(GR*(1-1/r)+Gs-eR)+2*r*lams*Gs/eR)
total=sp.simplify(Ito-lamR)
qv=sp.simplify(4*lamR/r)
assert sp.simplify(sp.limit(Ito/R,R,sp.oo)-8)==0
assert sp.simplify(sp.limit(total/R,R,sp.oo)-8)==0
assert sp.simplify(qv-8*sp.sqrt(3)/(9*(R+1)*(R**2-1)))==0
print('X003 PASS', 'lim_Ito/R=',sp.limit(Ito/R,R,sp.oo), 'lim_total/R=',sp.limit(total/R,R,sp.oo), 'qv=',qv)

# Independent exact audit R03-C227.
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def normal4(cols):
    a=[]
    for i in range(4):
        M=[[cols[c][row] for c in range(3)] for row in range(4) if row!=i]
        a.append(((-1)**i)*det3(M))
    if all(x==0 for x in a): return None
    g=0
    for x in a: g=math.gcd(g,abs(x))
    a=[x//g for x in a]
    for x in a:
        if x:
            if x<0: a=[-y for y in a]
            break
    return tuple(a)
sign4=list(itertools.product([-1,1],repeat=4))
directions=set(); rank3=0; nonzero=0
for inds in itertools.combinations(range(16),3):
    cols=[sign4[i] for i in inds]; a=normal4(cols)
    if a is None: continue
    rank3+=1
    assert all(sum(a[i]*v[i] for i in range(4))==0 for v in cols)
    if all(x!=0 for x in a):
        nonzero+=1
        assert len({abs(x) for x in a})==1
        directions.add(a)
assert len(directions)==8
for a in directions:
    assert sum(sum(a[i]*v[i] for i in range(4))==0 for v in sign4)==6
print('R02-AUDIT-R03-C227-01 PASS', 'rank3=',rank3, 'all_nonzero=',nonzero, 'directions=',len(directions), 'orthogonal=6')
print('ALL CHECKS PASS')
