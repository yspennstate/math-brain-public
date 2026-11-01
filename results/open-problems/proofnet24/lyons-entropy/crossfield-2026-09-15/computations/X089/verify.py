"""Exact chain identities, a signed-log countercertificate, and moment obstruction."""
import itertools, json
from fractions import Fraction as Q
from pathlib import Path
import sympy as S

HERE=Path(__file__).resolve().parent
checks=0
def check(v):
    global checks
    assert v
    checks+=1

def jets(w,v,acc=None):
    if acc is None: acc=[Q(0)]*len(w)
    out=[]
    for signs in itertools.product([-1,1],repeat=len(w)):
        p0,p1=Q(1),Q(1);d0,d1=Q(0),Q(0);e0,e1=Q(0),Q(0)
        for a,b,c,t in zip(w,v,acc,signs):
            p2=p1+t*a*p0
            d2=d1+t*(a*d0+b*p0)
            e2=e1+t*(a*e0+2*b*d0+c*p0)
            p0,p1,d0,d1,e0,e1=p1,p2,d1,d2,e1,e2
        out.append((p1,d1,e1))
    return out

def log_interval(r,N=40):
    k=0
    while r>2:r/=2;k+=1
    while r<Q(1,2):r*=2;k-=1
    def small(x):
        t=(x-1)/(x+1)
        a=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
        err=2*abs(t)**(2*N+1)/(Q(2*N+1)*(1-t*t))
        return a-err,a+err
    lo,hi=small(r);l2,h2=small(Q(2))
    return (lo+k*l2,hi+k*h2) if k>=0 else (lo+k*h2,hi+k*l2)

def curvature_interval(w,v):
    data=jets(w,v);den=Q(len(data));lo=hi=Q(0)
    for p,d,e in data:
        l,h=log_interval(p);lo+=d*d/p;hi+=d*d/p
        if e>=0:lo+=e*l;hi+=e*h
        else:lo+=e*h;hi+=e*l
    return lo/den,hi/den

# A five-site physically strict strength line with a concave entropy increment.
w=[Q(1,10),Q(11,25),Q(11,25),Q(1,10)]
v=[Q(-3),Q(7),Q(-6),Q(1)]
ratio=w[1]/(1-w[0])+w[2]/(1-w[3])
check(ratio==Q(44,45))
ln,hn=curvature_interval(w,v);lp,hp=curvature_interval(w[:-1],v[:-1])
inc=(ln-hp,hn-lp)
check(inc[1]<0)
check(Q(-1771,1000)<inc[0] and inc[1]<Q(-1770,1000))

# Failure of a stronger reciprocal-moment concavity assertion.
m=7;a=b=Q(1,4);u,vv=Q(-1),Q(1);C=Cp=Cpp=Q(0)
for t,s in itertools.product([-1,1],repeat=2):
    B=1+a*t;Bd=u*t;A=B+b*s;Ad=Bd+vv*s
    f=B**8/A**7;g=8*Bd/B-7*Ad/A;h=-8*(Bd/B)**2+7*(Ad/A)**2
    C+=f/4;Cp+=f*g/4;Cpp+=f*(g*g+h)/4
obstruction=C*Cpp-Q(8,7)*Cp**2
check(obstruction==Q(-1025122761666235553,5991619501228032))

# Independent signed-determinant verification of all atom polynomials and jets.
t=S.symbols('t',real=True);n=6
p=[S.Rational(j,20) for j in [7,9,10,11,12,13]]
dp=[S.Rational(j,100) for j in [2,-3,1,-2,3,-1]]
z=[(S.Integer(a)+S.I*b)/100 for a,b in [(5,1),(7,-2),(6,1),(4,2),(5,-1)]]
dz=[(S.Integer(a)+S.I*b)/100 for a,b in [(1,-1),(-2,1),(2,1),(-1,-2),(1,2)]]
K=S.diag(*[p[i]+t*dp[i] for i in range(n)])
for i in range(n-1):K[i,i+1]=z[i]+t*dz[i];K[i+1,i]=S.conjugate(K[i,i+1])
polys=[]
for bits in itertools.product([0,1],repeat=n):
    eps=[2*b-1 for b in bits]
    d=[K[i,i] if bits[i] else 1-K[i,i] for i in range(n)]
    prev,cur=S.Integer(1),d[0]
    for j in range(1,n):
        nxt=S.expand(d[j]*cur-eps[j-1]*eps[j]*K[j-1,j]*K[j,j-1]*prev)
        prev,cur=cur,nxt
    M=S.zeros(n)
    for j in range(n):M[:,j]=K[:,j] if bits[j] else (S.eye(n)-K)[:,j]
    det=S.Poly(M.det(method='domain-ge'),t)
    rec=S.Poly(cur,t)
    check(det==rec)
    for derivative in [0,1,2]:check(det.diff((0,derivative)).eval(0)==rec.diff((0,derivative)).eval(0))
    polys.append(rec.as_expr())
check(S.expand(sum(polys)-1)==0)

# Balanced recurrence and full perspective second-jet identity, history by history.
w=[Q(1,10),Q(11,25),Q(11,25),Q(1,10)];v=[Q(-3),Q(7),Q(-6),Q(1)]
acc=[b*b/(2*a) for a,b in zip(w,v)]  # actual radial affine-amplitude acceleration
full=jets(w,v,acc);prefix=jets(w[:-1],v[:-1],acc[:-1]);older=jets(w[:-2],v[:-2],acc[:-2])
for idx,(A,Ad,Add) in enumerate(prefix):
    B,Bd,Bdd=older[idx//2];ww,vw,aw=w[-1],v[-1],acc[-1]
    Y=ww*B;Yd=vw*B+ww*Bd;Ydd=aw*B+2*vw*Bd+ww*Bdd;u=Y/A
    for sign in [-1,1]:
        p,dd,ee=full[2*idx+(sign+1)//2]
        check(p==A+sign*Y);check(dd==Ad+sign*Yd);check(ee==Add+sign*Ydd)
    # Rational part of the averaged q log q perspective Hessian.
    direct=((Ad+Yd)**2/(A+Y)+(Ad-Yd)**2/(A-Y))/2-Ad*Ad/A
    square=(Yd-u*Ad)**2/(A*(1-u*u))
    check(direct==square)

result={
 'exact_assertions':checks,
 'chain_size':n,'all_atom_polynomials_and_first_two_jets':'passed',
 'five_path_strength_feasibility_ratio':str(ratio),
 'increment_strength_curvature_interval':[str(inc[0]),str(inc[1])],
 'increment_strength_curvature_approx':float((inc[0]+inc[1])/2),
 'm7_reciprocal_strength_obstruction':str(obstruction),
 'm7_reciprocal_strength_obstruction_approx':float(obstruction),
 'interpretation':'Neither negative certificate is an affine-kernel entropy counterexample.'
}
(HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='increment_strength_curvature_interval'},indent=2))
