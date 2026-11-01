"""C014 exact dyadic interval certificate; Python standard library only.

All elementary operations round outwards using integer arithmetic. Natural
logarithms use the atanh series with an explicit rational remainder bound.
No floating-point value is used to prove an assertion.
"""
from fractions import Fraction as F
from math import isqrt
from itertools import permutations

BITS = 176
UNIT = 1 << BITS
SERIES_TERMS = 68

def flq(x): return x.numerator * UNIT // x.denominator
def ceq(x): return -((-x.numerator * UNIT) // x.denominator)

class IV:
    __slots__=('lo','hi')
    def __init__(self, value=0, upper=None):
        if isinstance(value, IV): self.lo,self.hi=value.lo,value.hi; return
        self.lo=flq(F(value)); self.hi=ceq(F(value if upper is None else upper))
        assert self.lo <= self.hi
    @classmethod
    def raw(cls, lo, hi):
        x=cls.__new__(cls); x.lo=lo; x.hi=hi; assert lo<=hi; return x
    @staticmethod
    def lift(x): return x if isinstance(x,IV) else IV(x)
    def __add__(self,y):
        y=self.lift(y); return self.raw(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self): return self.raw(-self.hi,-self.lo)
    def __sub__(self,y): return self+-self.lift(y)
    def __rsub__(self,y): return self.lift(y)+-self
    def __mul__(self,y):
        y=self.lift(y); a=[self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return self.raw(min(a)//UNIT,-((-max(a))//UNIT))
    __rmul__=__mul__
    def recip(self):
        assert self.lo>0 or self.hi<0, 'division interval includes zero'
        return self.raw(UNIT*UNIT//self.hi,-((-UNIT*UNIT)//self.lo))
    def __truediv__(self,y): return self*self.lift(y).recip()
    def __rtruediv__(self,y): return self.lift(y)*self.recip()
    def square(self):
        a=max(self.lo*self.lo,self.hi*self.hi)
        b=0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        return self.raw(b//UNIT,-((-a)//UNIT))
    def sqrt(self):
        assert self.lo>=0
        lo=isqrt(self.lo*UNIT); hi=isqrt(self.hi*UNIT)
        if hi*hi<self.hi*UNIT:hi+=1
        return self.raw(lo,hi)
    def endpoints(self): return F(self.lo,UNIT),F(self.hi,UNIT)
    def decimal_box(self,places=12):
        scale=10**places; lo=self.lo*scale//UNIT;hi=-((-self.hi*scale)//UNIT)
        return f'[{lo}/{scale}, {hi}/{scale}]'
    def midpoint_float(self):return (self.lo+self.hi)/(2*UNIT)


def log_reduced(y):
    assert F(1)<=y<=F(2)
    t=IV((y-1)/(y+1)); t2=t.square(); power=t; s=IV(0)
    for j in range(SERIES_TERMS):
        s+=power/(2*j+1)
        power*=t2
    # Uniform tail bound for 0 <= t <= 1/3.
    tail=F(2, (2*SERIES_TERMS+1)*3**(2*SERIES_TERMS+1))*F(9,8)
    return 2*s+IV(0,tail)

LOG2=log_reduced(F(2))

def log_fraction(x):
    x=F(x);assert x>0;k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    return k*LOG2+log_reduced(x)


def cmul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def norm2(z):return z[0]*z[0]+z[1]*z[1]

def atom_derivatives(diag,edges,mask):
    # Edges are (K23,K31,K12), each represented by (real,imaginary).
    z0=diag[0]*0
    d=[diag[i]-(0 if mask>>i&1 else 1) for i in range(3)]
    g=[z0 for _ in range(9)];h=[[z0 for _ in range(9)] for _ in range(9)]
    p=d[0]*d[1]*d[2]-sum(d[i]*norm2(edges[i]) for i in range(3))+2*cmul(cmul(edges[0],edges[1]),edges[2])[0]
    for i in range(3):
        j,k=[a for a in range(3) if a!=i]
        g[i]=d[j]*d[k]-norm2(edges[i]);h[i][j]=h[j][i]=d[k];h[i][k]=h[k][i]=d[j]
        prod=cmul(edges[j],edges[k])
        for a in range(2):
            ia=3+2*i+a
            g[ia]=-2*d[i]*edges[i][a]+2*(prod[0] if a==0 else -prod[1])
            h[ia][ia]=-2*d[i];h[i][ia]=h[ia][i]=-2*edges[i][a]
            for other,leftover in [(j,k),(k,j)]:
                for b in range(2):
                    ob=3+2*other+b
                    v=edges[leftover][0] if a+b==0 else (-edges[leftover][1] if a+b==1 else -edges[leftover][0])
                    h[ia][ob]=h[ob][ia]=2*v
    sign=(-1)**(3-mask.bit_count())
    return sign*p,[sign*x for x in g],[[sign*x for x in row] for row in h]

D=[F(43,100),F(41,100),F(13,20)]
R=[F(19,100),F(11,40),F(49,200)]

def probabilities(cosine):
    out=[]
    q=2*R[0]*R[1]*R[2]*cosine
    for mask in range(8):
        d=[D[i]-(0 if mask>>i&1 else 1) for i in range(3)]
        out.append((-1)**(3-mask.bit_count())*(d[0]*d[1]*d[2]-sum(d[i]*R[i]*R[i] for i in range(3))+q))
    return out

def parity_difference(cosine):
    ps=probabilities(cosine);even=odd=F(1)
    for mask,p in enumerate(ps):
        if mask.bit_count()%2:odd*=p
        else:even*=p
    return even-odd


def verify_derivative_formulas():
    # Independent six-permutation determinant evaluation, with exact rational
    # interpolation of all nine gradients and all 45 Hessian coefficients.
    c,s=F(-61,1861),F(1860,1861)
    edges=[(R[0],F(0)),(R[1],F(0)),(R[2]*c,R[2]*s)]
    def direct(diag,ee,mask):
        conj=lambda z:(z[0],-z[1])
        a=[[(diag[0],F(0)),ee[2],conj(ee[1])],
           [conj(ee[2]),(diag[1],F(0)),ee[0]],
           [ee[1],conj(ee[0]),(diag[2],F(0))]]
        for i in range(3):
            if not(mask>>i&1):a[i][i]=(a[i][i][0]-1,F(0))
        total=(F(0),F(0))
        for perm in permutations(range(3)):
            term=(F(1),F(0))
            for i in range(3):term=cmul(term,a[i][perm[i]])
            sign=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
            total=(total[0]+sign*term[0],total[1]+sign*term[1])
        assert total[1]==0
        return (-1)**(3-mask.bit_count())*total[0]
    directions=[]
    for i in range(9):
        x=[F(0)]*9;x[i]=F(1);directions.append(x)
        for j in range(i+1,9):
            x=[F(0)]*9;x[i]=x[j]=F(1);directions.append(x)
    for mask in range(8):
        p,g,h=atom_derivatives(D,edges,mask)
        assert p==direct(D,edges,mask)
        for x in directions:
            def at(t):
                dd=[D[i]+t*x[i] for i in range(3)]
                ee=[(edges[i][0]+t*x[3+2*i],edges[i][1]+t*x[4+2*i]) for i in range(3)]
                return direct(dd,ee,mask)
            second=at(F(1))+at(F(-1))-2*p
            first=(8*(at(F(1,2))-at(F(-1,2)))-(at(F(1))-at(F(-1))))/6
            assert first==sum(g[i]*x[i] for i in range(9))
            assert second==sum(h[i][j]*x[i]*x[j] for i in range(9) for j in range(9))


def log_interval(x):
    # Monotonicity reduces an interval log to two exact rational log bounds.
    lo,hi=x.endpoints();a=log_fraction(lo);b=log_fraction(hi)
    return IV.raw(a.lo,b.hi)


def certify(cosine,sine=None):
    if isinstance(cosine,IV):
        c=cosine;s=(1-c.square()).sqrt() if sine is None else IV(sine)
    else:
        c=IV(cosine);s=IV(sine) if sine is not None else (1-c.square()).sqrt()
    dd=list(map(IV,D));ee=[(IV(R[0]),IV(0)),(IV(R[1]),IV(0)),(R[2]*c,R[2]*s)]
    aa=[atom_derivatives(dd,ee,mask) for mask in range(8)]
    assert all(p.lo>0 for p,g,h in aa)
    fs=[-log_interval(p) for p,g,h in aa]
    tau=sum((-1)**(3-mask.bit_count())*fs[mask] for mask in range(8))
    cs=[fs[7^(1<<i)]-sum(fs[1<<j] for j in range(3) if i!=j)+fs[0] for i in range(3)]
    md=[cs[i]+tau*dd[i] for i in range(3)];me=[(tau*x,tau*y) for x,y in ee]
    delta,grad,hdet=atom_derivatives(md,me,7)
    assert min(x.lo for x in md)>0
    assert all((md[j]*md[k]-norm2(me[i])).lo>0 for i in range(3) for j,k in [[j for j in range(3) if j!=i]])
    assert delta.lo>0
    fi=[[sum(g[i]*g[j]/p for p,g,h in aa) for j in range(9)] for i in range(9)]
    nn=[[fi[i][j]+grad[i]*grad[j]/delta-hdet[i][j] for j in range(9)] for i in range(9)]
    # Interval LDL elimination also certifies positive pivots.
    bb=[row[:] for row in nn]; yy=grad[:]; value=IV(0);pivots=[]
    for i in range(9):
        pivot=bb[i][i];assert pivot.lo>0, (i,pivot.decimal_box())
        pivots.append(pivot)
        value+=yy[i].square()/pivot
        next_y=[yy[j]-bb[j][i]*yy[i]/pivot for j in range(i+1,9)]
        for j in range(i+1,9):
            for k in range(j,9):
                v=bb[j][k]-bb[j][i]*bb[i][k]/pivot
                bb[j][k]=bb[k][j]=v
        for j,v in zip(range(i+1,9),next_y):yy[j]=v
    return value/delta,tau,delta,pivots


def main():
    verify_derivative_formulas()
    print('independent exact determinant interpolation of full atom gradients and Hessians: PASS')
    # Exact affine-in-cosine atom positivity certifies every phase is admissible.
    endpoint_ps=[probabilities(F(-1)),probabilities(F(1))]
    minimum=min(p for row in endpoint_ps for p in row)
    assert minimum>0
    print('BITS',BITS,'SERIES_TERMS',SERIES_TERMS)
    print('minimum atom over every phase =',minimum)
    print('all eight atoms remain positive for every cosine in [-1,1]: PASS')
    results={}
    for name,c,s in [('real_negative',F(-1),F(0)),('quadrature',F(0),F(1)),('real_positive',F(1),F(0)),('witness',F(-61,1861),F(1860,1861))]:
        val,tau,delta,piv=certify(c,s);results[name]=val
        print(name,'cos=',c,'sin=',s,'danger=',val.decimal_box(),'tau=',tau.decimal_box())
        assert val.hi<UNIT
    anchor_max=max(v.hi for name,v in results.items() if name!='witness')
    assert results['witness'].lo>anchor_max
    print('witness minus maximum endpoint/quadrature danger >=',F(results['witness'].lo-anchor_max,UNIT))
    print('strict endpoint/quadrature obstruction: PASS')
    # The phase maximizing entropy is the unique zero of tau. Isolate it by
    # rational bisection of the parity-product polynomial, without logarithms.
    a,b=F(-1),F(1)
    assert parity_difference(a)>0>parity_difference(b)
    for _ in range(104):
        c=(a+b)/2
        if parity_difference(c)>0:a=c
        else:b=c
    assert parity_difference(a)>0>parity_difference(b)
    root=IV(a,b);value,tau,delta,piv=certify(root)
    print('entropy-maximizing cosine in',root.decimal_box(18))
    print('danger throughout isolated entropy-maximizer interval in',value.decimal_box())
    assert results['witness'].lo>value.hi
    print('strict entropy-maximizing-phase obstruction: PASS')
    print('all displayed phase kernels have a negative definite full Hermitian Hessian: PASS')

if __name__=='__main__':main()
