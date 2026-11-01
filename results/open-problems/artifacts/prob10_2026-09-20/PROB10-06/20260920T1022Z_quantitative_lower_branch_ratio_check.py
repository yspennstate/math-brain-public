from fractions import Fraction as F

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi); assert self.lo<=self.hi
    def __add__(self,o): o=asI(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asI(o))
    def __rsub__(self,o): return asI(o)-self
    def __mul__(self,o):
        o=asI(o); v=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi: raise ZeroDivisionError
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,o): return self*asI(o).inv()
    def __rtruediv__(self,o): return asI(o)/self
    def sq(self):
        if self.lo>=0: return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0: return I(self.hi*self.hi,self.lo*self.lo)
        return I(0,max(self.lo*self.lo,self.hi*self.hi))

def asI(x): return x if isinstance(x,I) else I(x)

def bound_intervals(L,P):
    # inherited type-conditioned inverse-escape derivative bound
    R=6-3*L+L*P
    u=(3-L)/3
    d2=R/(6+L*P)
    d3=R/(6-L+L*P)
    u2=2*(3-L)/(L+6)
    u3=u
    r2=d2/u2; r3=d3/u3
    w2=(1-P)*r2; w3=P*r3; w0=1-w2-w3

    def K(base,j):
        if j==1:
            return w0/base + base*w2/(base+u2).sq() + base*w3/(base+u3).sq()
        return (w0*w0/base
                +2*base*w0*w2/(base+u2).sq()
                +2*base*w0*w3/(base+u3).sq()
                +base*w2*w2/(base+2*u2).sq()
                +2*base*w2*w3/(base+u2+u3).sq()
                +base*w3*w3/(base+2*u3).sq())

    K1=K(L,1); K2=K(L,2)
    rho=(1-P)*2*K1+P*3*K2
    A=(1-P)*6*(3-L)/(L+6).sq()+P*(3-L)/9
    eta=A/(1-rho)
    mu=(1-P)*d2+P*d3
    a=L-1
    Kc=K(a,2)
    D=1/a+2*eta*Kc/mu-3/(9-L)

    # New quantitative lower branch-addition ratio.
    # c3/c2 >= Rlo, proved in the accompanying report.
    Rlo=F(3,4)*(1+a*mu/(3*u*(a+4*u)))
    theta=P*Rlo/(1-P+P*Rlo)
    # On all certified boxes theta>2/3, and g(t)=t(1-t)/(2+t) is decreasing there.
    if theta.lo<=F(2,3):
        raise ArithmeticError('theta lower bound did not clear 2/3')
    gmax=theta.lo*(1-theta.lo)/(2+theta.lo)
    product_hi=L.hi*gmax*D.hi
    return rho,product_hi,Rlo,theta

def certify(box,q,maxdepth=28):
    x0,x1,y0,y1=box
    stack=[(F(x0),F(x1),F(y0),F(y1),0)]
    visited=accepted=0
    worst=F(0); worst_rho=F(0); min_theta=F(10); min_ratio=F(10)
    while stack:
        a,b,c,d,depth=stack.pop(); visited+=1
        try:
            rho,product,Rlo,theta=bound_intervals(I(a,b),I(c,d))
            good=(rho.hi<F(99,100) and product<q)
        except (ZeroDivisionError,ArithmeticError):
            good=False; rho=product=Rlo=theta=None
        if good:
            accepted+=1
            worst=max(worst,product); worst_rho=max(worst_rho,rho.hi)
            min_theta=min(min_theta,theta.lo); min_ratio=min(min_ratio,Rlo.lo)
            continue
        assert depth<maxdepth, (a,b,c,d,depth,rho,product,Rlo,theta)
        if depth%2==0:
            m=(a+b)/2
            stack.append((a,m,c,d,depth+1)); stack.append((m,b,c,d,depth+1))
        else:
            m=(c+d)/2
            stack.append((a,b,c,m,depth+1)); stack.append((a,b,m,d,depth+1))
    return visited,accepted,worst,worst_rho,min_theta,min_ratio

cases=[
    ('A', (F(185527,100000),F(4001,2000),F(47,64),F(1)), F(999,1000)),
    ('B', (F(185527,100000),F(203,100),F(3,4),F(1)), F(49,50)),
    ('C', (F(185527,100000),F(43,20),F(4,5),F(1)), F(97,100)),
]
import sys
want=sys.argv[1] if len(sys.argv)>1 else None
for name,box,q in cases:
    if want and name!=want: continue
    v,a,w,wr,mt,mr=certify(box,q)
    Lmax=box[1]
    margin=4*(1-q)/(3+Lmax)**2
    print(f'{name}_PASS visited={v} accepted={a}')
    print(f'{name}_product_upper<{q} worst_accepted_float={float(w):.15f}')
    print(f'{name}_rho_upper<99/100 worst_accepted_float={float(wr):.15f}')
    print(f'{name}_theta_lower>{mt} min_ratio_lower>{mr}')
    print(f'{name}_derivative_margin={margin} float={float(margin):.15f}')
print('ALL_EXACT_CHECKS_PASS')
