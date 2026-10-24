from fractions import Fraction as F
import itertools, functools

class I:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=asI(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asI(o))
    def __rsub__(self,o): return asI(o)-self
    def __mul__(self,o):
        o=asI(o)
        v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError((self.lo,self.hi))
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,o): return self*asI(o).inv()
    def __rtruediv__(self,o): return asI(o)/self
    def sq(self):
        if self.lo>=0: return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0: return I(self.hi*self.hi,self.lo*self.lo)
        return I(0,max(self.lo*self.lo,self.hi*self.hi))

def asI(x): return x if isinstance(x,I) else I(x)
def H(vals): return 1/sum((1/z for z in vals),F(0))

def Tcorner(L,P,y2,y3):
    vals={2:y2,3:y3}; ans=[]
    for k in (2,3):
        total=F(0)
        for types in itertools.product((2,3),repeat=k):
            prob=F(1)
            for r in types:
                prob *= P if r==3 else 1-P
            total += prob*H([vals[r] for r in types])
        ans.append(1+L*total)
    return ans[0],ans[1]

def ceil_grid(x,Q):
    return F((x.numerator*Q+x.denominator-1)//x.denominator,Q)

@functools.lru_cache(maxsize=None)
def corner_supersolution(L,P,niter=30,Q=10**9):
    D=1-L*(3-P)/6
    assert D>0
    M=1/D
    y2=1+L*M/2; y3=1+L*M/3
    for _ in range(niter):
        t2,t3=Tcorner(L,P,y2,y3)
        assert t2<=y2 and t3<=y3
        z2=ceil_grid(t2,Q); z3=ceil_grid(t3,Q)
        if z2>y2: z2=y2
        if z3>y3: z3=y3
        assert t2<=z2<=y2 and t3<=z3<=y3
        y2,y3=z2,z3
    t2,t3=Tcorner(L,P,y2,y3)
    assert t2<=y2 and t3<=y3 and y2>=y3
    return y2,y3

def bound_box(a,b,c,d,niter=30,Q=10**9):
    y2,y3=corner_supersolution(b,c,niter,Q)
    d2,d3=1/y2,1/y3
    L=I(a,b); P=I(c,d); w2,w3=1-P,P

    def K(base,j):
        if j==1:
            return base*w2/(base+d2).sq()+base*w3/(base+d3).sq()
        assert j==2
        return (base*w2*w2/(base+2*d2).sq()
                +2*base*w2*w3/(base+d2+d3).sq()
                +base*w3*w3/(base+2*d3).sq())

    rho=(1-P)*2*K(L,1)+P*3*K(L,2)
    if rho.hi>=1:
        return None,rho

    A=(1-P)*6*(3-L)/(L+6).sq()+P*(3-L)/9
    eta=A/(1-rho)

    a0=L-1
    assert a0.lo>0
    u=(3-L)/3
    Dmax=(9-L)/3
    Delta=Dmax*(2*eta/a0.sq()+2*u/(a0*a0*a0))

    theta0=3*c/(4-c)
    assert theta0*theta0+4*theta0-2>0
    g0=theta0*(1-theta0)/(2+theta0)
    product=L*g0*Delta
    return product,rho

def certify(rect,q,rho_q,maxdepth=24):
    a,b,c,d=map(F,rect)
    stack=[(a,b,c,d,0)]
    visited=accepted=0; max_depth=0
    worst_product=F(-10**6); worst_rho=F(-10**6)
    while stack:
        a,b,c,d,depth=stack.pop()
        visited+=1; max_depth=max(max_depth,depth)
        product,rho=bound_box(a,b,c,d)
        good=(product is not None and product.hi<q and rho.hi<rho_q)
        if good:
            accepted+=1
            worst_product=max(worst_product,product.hi)
            worst_rho=max(worst_rho,rho.hi)
            continue
        assert depth<maxdepth,("uncertified",a,b,c,d,depth,
                               None if product is None else product.hi,rho.hi)
        if depth%2==0:
            m=(a+b)/2
            stack.append((a,m,c,d,depth+1)); stack.append((m,b,c,d,depth+1))
        else:
            m=(c+d)/2
            stack.append((a,b,c,m,depth+1)); stack.append((a,b,m,d,depth+1))
    return visited,accepted,max_depth,worst_product,worst_rho

# New strip only; the predecessor already proves p>=3/4 through lambda=107/50.
rect=(F(107,50),F(12,5),F(3,4),F(1))
q=F(999,1000); rho_q=F(49,50)
v,a,dep,wp,wr=certify(rect,q,rho_q)
margin=F(4)*(1-q)/(F(3)+F(12,5))**2
assert margin==F(1,7290)

# Exact obstruction to the false stronger claim Delta<=0 at p=1.
# For the deterministic 3-ary tree B=(3-lambda)/3 and c3/c2=6/(9-lambda),
# hence Delta=(log(c3/c2))'=1/(9-lambda)>0. Check at lambda=12/5.
lam=F(12,5)
Delta_regular=1/(9-lam)
assert Delta_regular==F(5,33)>0

# Exact obstruction to a uniform q-contraction: for the same deterministic tree,
# the log-elasticity recursion discount is 1-B=lambda/3 -> 1 as lambda ->3.
assert F(299,100)/3 > F(99,100)

print("BRANCH_GAP_LOGDERIVATIVE_CHECK")
print("RECT_PASS lambda=[107/50,12/5] p=[3/4,1]")
print("visited=%d accepted=%d max_depth=%d"%(v,a,dep))
print("product_upper<999/1000")
print("rho_upper<49/50")
print("worst_product_upper_float=%.15f"%float(wp))
print("worst_rho_upper_float=%.15f"%float(wr))
print("derivative_margin=1/7290")
print("truncation_bound=E[B_N-B]<=(49/50)^N")
print("NEGATION_OBSTRUCTION_PASS regular3_Delta_at_12_5=5/33>0")
print("Q_CONTRACTION_OBSTRUCTION_PASS regular3_discount_at_2_99>99/100")
print("ROUNDING_GRID=1e-9 TYPE_VECTOR_ITERATIONS=30")
print("ALL_EXACT_CHECKS_PASS")
