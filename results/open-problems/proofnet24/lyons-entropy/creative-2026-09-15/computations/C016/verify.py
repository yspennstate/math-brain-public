"""Exact algebra and rigorous finite checks for C016; Python standard library only.

Run from any directory: python /absolute/path/to/computations/C016/verify.py
The proof is in agents/C016.md.  Finite checks supplement, not replace, it.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from explore import P, R


def same(a,b):
    a,b=R(a),R(b)
    return (a.a*b.b-b.a*a.b).zero()


def exact_algebra():
    t=R(P([0,1])); v=(1+t)/2; s=t*t; e=1-s; d=9-s
    atoms=[(1-v)**2/2, (1-v*v)/6, v*(2-v)/6, v*v/2]
    du=[-(1-v)**2, (1-v)*(1-3*v)/3, v*(2-3*v)/3, v*v]
    dv=[-(1-v), -v/3, (1-v)/3, v]
    mul=[1,3,3,1]
    fu=sum((n*x*x/p for n,x,p in zip(mul,du,atoms)),R(0))
    fuv=sum((n*x*y/p for n,x,y,p in zip(mul,du,dv,atoms)),R(0))
    fv=sum((n*y*y/p for n,y,p in zip(mul,dv,atoms)),R(0))
    assert same(sum((n*p for n,p in zip(mul,atoms)),R(0)),1)
    assert same(fu,4*(3+3*s+2*s*s)/d)
    assert same(fuv,8*(3+s)/d)
    assert same(fv,16*(3-s)/(e*d))
    assert same(fu*fv-fuv*fuv,64*s*(1+s)/(e*d))
    assert same(4*fuv-2*fu,8*(9+s-2*s*s)/d)
    assert same(fu+fv,4*(15-4*s-s*s-2*s*s*s)/(e*d))
    det_lower=4*s*(144-25*s)/(9*e*d)
    assert same(fu*fv-fuv*fuv-4*169*s*s/(9*e*d),det_lower)
    assert same(det_lower/fu,s*(144-25*s)/(9*e*(3+3*s+2*s*s)))
    eta=s*(144-25*s)/(9*(15-4*s-s*s-2*s*s*s))
    assert same(det_lower/(fu+fv),eta)
    assert same((144-25*s)*(9-s)-72*(15-4*s-s*s-2*s*s*s),
                216-81*s+97*s*s+144*s*s*s)
    return {'symbolic_identities': 11,
            'Fuu': str(fu), 'Fuv': str(fuv), 'Fvv': str(fv),
            'det_F': str(fu*fv-fuv*fuv),
            'Schur_determinant_lower_bound': str(det_lower),
            'eta': str(eta)}


def conditional_variance_check(u,v):
    a,b=u*(1-u),v*(1-v)
    aa=u+2*v-3*u*v; bb=2*u+v-3*u*v
    q=[(1-u)*(1-v)**2,(1-v)*aa,v*bb,u*v*v]
    posterior=[F(0),u*(1-v)/aa,2*u*(1-v)/bb,F(1)]
    w=sum(qn*rn*(1-rn) for qn,rn in zip(q,posterior))
    kap=2*((1-v)/aa+v/bb)
    assert w==a*b*kap
    su=[(z-u)/a for z in posterior]
    sv=[(F(n)-z-2*v)/b for n,z in enumerate(posterior)]
    f00=sum(qn*x*x for qn,x in zip(q,su))
    f01=sum(qn*x*y for qn,x,y in zip(q,su,sv))
    f11=sum(qn*y*y for qn,y in zip(q,sv))
    assert f00==1/a-w/(a*a)
    assert f01==w/(a*b)
    assert f11==2/b-w/(b*b)
    return {'u':str(u),'v':str(v),'E_Var_U_given_N':str(w),
            'Fisher':[[str(f00),str(f01)],[str(f01),str(f11)]]}


# Rational interval arithmetic, rounding outward after every operation.
SCALE=10**40

def down(x): return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x): return -down(-x)
class IV:
    def __init__(self,a=0,b=None):
        if isinstance(a,IV): self.lo,self.hi=a.lo,a.hi; return
        self.lo,self.hi=down(F(a)),up(F(a if b is None else b))
    def __add__(self,x):
        x=IV(x);return IV(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,x): return self+-IV(x)
    def __rsub__(self,x): return IV(x)+-self
    def __mul__(self,x):
        x=IV(x); vals=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]
        return IV(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=IV(x); assert x.lo*x.hi>0
        return self*IV(1/x.hi,1/x.lo)
    def serial(self): return [str(self.lo),str(self.hi)]


def log_unit(x,n=60):
    """Exact bounds for log(x), 1<=x<=2."""
    assert 1<=x<=2
    z=(x-1)/(x+1)
    total=F(0);power=z
    for k in range(n):
        total+=2*power/(2*k+1);power*=z*z
    remainder=2*power/((2*n+1)*(1-z*z))
    return IV(total,total+remainder)
LOG2=log_unit(F(2))
def log_iv(x):
    x=F(x); assert x>0
    if x<1:return -log_iv(1/x)
    n=0
    while x>2:x/=2;n+=1
    return n*LOG2+log_unit(x)


def zero(n=3):return [[F(0) for _ in range(n)] for _ in range(n)]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
                      for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum(a[i][i] for i in range(len(a)))
def det(a):
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det([[a[r][c] for c in range(len(a)) if c!=j]
               for r in range(1,len(a))]) for j in range(len(a)))
def inv(a):
    n=len(a); dd=det(a)
    return [[(-1)**(i+j)*det([[a[r][c] for c in range(n) if c!=i]
             for r in range(n) if r!=j])/dd for j in range(n)] for i in range(n)]


def ldl_positive(matrix):
    """Interval LDL certifies positive definiteness of every enclosed matrix."""
    n=len(matrix);ls=[[IV(0) for _ in range(n)] for _ in range(n)]; ds=[]
    for i in range(n):
        di=matrix[i][i]-sum((ls[i][k]*ls[i][k]*ds[k] for k in range(i)),IV(0))
        assert di.lo>0, (i,di.serial())
        ds.append(di);ls[i][i]=IV(1)
        for j in range(i+1,n):
            ls[j][i]=(matrix[j][i]-sum((ls[j][k]*ls[i][k]*ds[k]
                            for k in range(i)),IV(0)))/di
    return [d.serial() for d in ds]


def full_hessian_check(t):
    """Independent eight-atom construction in all nine real coordinates."""
    K=[[((1+t)/2 if i==j else F(0))-t/6 for j in range(3)] for i in range(3)]
    real=[];imag=[]
    for i in range(3):
        b=zero();b[i][i]=F(1);real.append(b)
    for i,j in combinations(range(3),2):
        b=zero();b[i][j]=b[j][i]=F(1);real.append(b)
        b=zero();b[i][j]=F(1);b[j][i]=F(-1);imag.append(b)
    qr=[[IV(0) for _ in range(6)] for _ in range(6)]
    qi=[[IV(0) for _ in range(3)] for _ in range(3)]
    ps=[]
    for mask in range(8):
        Q=[[K[i][j]-(F(1) if i==j and not(mask&(1<<i)) else F(0))
            for j in range(3)] for i in range(3)]
        p=(-1)**(3-mask.bit_count())*det(Q);assert p>0;ps.append(p)
        r=inv(Q); ar=[mul(r,z) for z in real];ai=[mul(r,z) for z in imag]
        scores=[tr(z) for z in ar];lp=log_iv(p)
        for i in range(6):
            for j in range(6):
                pdd=p*(scores[i]*scores[j]-tr(mul(ar[i],ar[j])))
                qr[i][j]+=p*scores[i]*scores[j]+pdd*lp
        for i in range(3):
            for j in range(3):
                pdd=p*tr(mul(ai[i],ai[j]))
                qi[i][j]+=pdd*lp
    assert sum(ps)==1
    bound=4*t*t/(9-t*t)
    for i,weight in enumerate([1,1,1,2,2,2]):qr[i][i]-=bound*weight
    for i in range(3):qi[i][i]-=2*bound
    return {'t':str(t),'curvature_constant':str(bound),
            'atom_probabilities':list(map(str,ps)),
            'real_sector_LDL_pivots_for_minus_H_minus_bound':ldl_positive(qr),
            'imaginary_sector_LDL_pivots_for_minus_H_minus_bound':ldl_positive(qi)}


def main():
    result={'status':'PASS','exact_algebra':exact_algebra(),
            'general_conditional_variance_checks':[
                conditional_variance_check(u,v) for u,v in
                [(F(1,5),F(2,3)),(F(1,2),F(5,6)),(F(7,8),F(2,9)),(F(3,7),F(3,7))]],
            'rigorous_full_hessian_checks':[
                full_hessian_check(t) for t in [F(1,10),F(1,2),F(4,5),F(-1,2)]]}
    path=Path(__file__).with_name('results.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: eleven rational-function identities; four exact conditional-variance cases;')
    print('four independent all-nine-coordinate Hessian certificates with rational log intervals.')
    print('Saved '+str(path))
if __name__=='__main__':main()
