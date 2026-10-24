from fractions import Fraction as F
import itertools, functools, sys

class I:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi); assert self.lo<=self.hi
    def __add__(self,o):
        o=asI(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asI(o))
    def __rsub__(self,o): return asI(o)-self
    def __mul__(self,o):
        o=asI(o); vals=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def inv(self):
        assert not (self.lo<=0<=self.hi); return I(1/self.hi,1/self.lo)
    def __truediv__(self,o): return self*asI(o).inv()
    def __rtruediv__(self,o): return asI(o)/self
    def sq(self):
        if self.lo>=0: return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0: return I(self.hi*self.hi,self.lo*self.lo)
        return I(0,max(self.lo*self.lo,self.hi*self.hi))

def asI(x): return x if isinstance(x,I) else I(x)
def H(vals): return 1/sum((1/z for z in vals),F(0))

def Tcorner(L,P,y2,y3):
    vals={2:y2,3:y3}; out=[]
    for k in (2,3):
        s=F(0)
        for types in itertools.product((2,3),repeat=k):
            pr=F(1)
            for r in types: pr*=P if r==3 else 1-P
            s+=pr*H([vals[r] for r in types])
        out.append(1+L*s)
    return out

def ceil_grid(x,Q):
    return F((x.numerator*Q+x.denominator-1)//x.denominator,Q)

@functools.lru_cache(maxsize=None)
def corner_supersolution(L,P,niter=30,Q=10**9):
    D=1-L*(3-P)/6; assert D>0
    M=1/D; y2=1+L*M/2; y3=1+L*M/3
    for _ in range(niter):
        t2,t3=Tcorner(L,P,y2,y3); assert t2<=y2 and t3<=y3
        z2,z3=ceil_grid(t2,Q),ceil_grid(t3,Q)
        if z2>y2: z2=y2
        if z3>y3: z3=y3
        assert t2<=z2<=y2 and t3<=z3<=y3
        y2,y3=z2,z3
    t2,t3=Tcorner(L,P,y2,y3)
    assert t2<=y2 and t3<=y3 and y2>=y3
    return y2,y3

def bound_box(a,b,c,d):
    y2,y3=corner_supersolution(b,c); d2,d3=1/y2,1/y3
    L=I(a,b); P=I(c,d); w2,w3=1-P,P
    def K(base,j):
        if j==1:
            return base*w2/(base+d2).sq()+base*w3/(base+d3).sq()
        return (base*w2*w2/(base+2*d2).sq()
                +2*base*w2*w3/(base+d2+d3).sq()
                +base*w3*w3/(base+2*d3).sq())
    rho=(1-P)*2*K(L,1)+P*3*K(L,2)
    if rho.hi>=1: return None,rho
    A=(1-P)*6*(3-L)/(L+6).sq()+P*(3-L)/9
    eta=A/(1-rho)

    # Uniform sibling-chord constants on the subbox.  The actual alpha=lambda-1
    # is >= a-1; the actual support upper bound u(lambda) is <= U=(3-a)/3;
    # and the actual unconditional mean is >= dbar computed from the lower p endpoint.
    alpha0=a-1; U=(3-a)/3; assert alpha0>0 and U>0
    dbar=(1-c)*d2+c*d3
    def C(r):
        return 1/(alpha0**r)+(dbar/U)*(1/((alpha0+2*U)**r)-1/(alpha0**r))
    C2,C3=C(2),C(3)

    u=(3-L)/3; Dmax=(9-L)/3
    Delta=Dmax*(2*eta*C2+2*u*C3)
    theta0=3*c/(4-c)
    assert theta0*theta0+4*theta0-2>0
    g0=theta0*(1-theta0)/(2+theta0)
    return L*g0*Delta,rho

def certify(rect,q,rhoq,maxdepth=24):
    a,b,c,d=map(F,rect); stack=[(a,b,c,d,0)]
    vis=acc=md=0; wp=F(-100); wr=F(-100)
    while stack:
        a,b,c,d,dep=stack.pop(); vis+=1; md=max(md,dep)
        product,rho=bound_box(a,b,c,d)
        if product is not None and product.hi<q and rho.hi<rhoq:
            acc+=1; wp=max(wp,product.hi); wr=max(wr,rho.hi); continue
        assert dep<maxdepth,(a,b,c,d,dep,None if product is None else product.hi,rho.hi)
        if dep%2==0:
            m=(a+b)/2
            stack.extend([(a,m,c,d,dep+1),(m,b,c,d,dep+1)])
        else:
            m=(c+d)/2
            stack.extend([(a,b,c,m,dep+1),(a,b,m,d,dep+1)])
    return vis,acc,md,wp,wr

def run_A():
    rect=(F(20021,10000),F(12,5),F(18,25),F(1)); q=F(99,100); rq=F(199,200)
    v,a,d,wp,wr=certify(rect,q,rq)
    margin=F(4)*(1-q)/(F(3)+F(12,5))**2
    assert margin==F(1,729)
    print('RECT_A lambda=[20021/10000,12/5] p=[18/25,1]')
    print(f'visited={v} accepted={a} max_depth={d}')
    print('product_upper<99/100')
    print('rho_upper<199/200')
    print(f'worst_product_upper_float={float(wp):.15f}')
    print(f'worst_rho_upper_float={float(wr):.15f}')
    print('derivative_margin=1/729')

def run_B():
    rect=(F(12,5),F(247,100),F(3,4),F(1)); q=F(9999,10000); rq=F(199,200)
    v,a,d,wp,wr=certify(rect,q,rq)
    margin=F(4)*(1-q)/(F(3)+F(247,100))**2
    assert margin==F(4,299209)
    print('RECT_B lambda=[12/5,247/100] p=[3/4,1]')
    print(f'visited={v} accepted={a} max_depth={d}')
    print('product_upper<9999/10000')
    print('rho_upper<199/200')
    print(f'worst_product_upper_float={float(wp):.15f}')
    print(f'worst_rho_upper_float={float(wr):.15f}')
    print('derivative_margin=4/299209')

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in {'A','B'}:
        raise SystemExit('usage: python checker.py A|B')
    (run_A if sys.argv[1]=='A' else run_B)()
    print('TYPE_VECTOR_ITERATIONS=30 ROUNDING_GRID=1e-9')
    print('ALL_EXACT_CHECKS_PASS')
