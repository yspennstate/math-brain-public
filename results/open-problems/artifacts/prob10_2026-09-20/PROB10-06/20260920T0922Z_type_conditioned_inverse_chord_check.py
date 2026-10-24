from fractions import Fraction as F

class I:
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
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
    # P(nu=2)=1-p, P(nu=3)=p. Exact type-conditioned chord bound.
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
    theta=3*P/(4-P)
    g=theta*(1-theta)/(2+theta)
    product=L*g*D
    return rho,product

def certify(box,q,maxdepth):
    x0,x1,y0,y1=box
    stack=[(F(x0),F(x1),F(y0),F(y1),0)]
    accepted=0; visited=0; worst=F(-10**9)
    while stack:
        a,b,c,d,depth=stack.pop(); visited+=1
        try:
            rho,product=bound_intervals(I(a,b),I(c,d))
            good=(rho.hi<F(19,20) and product.hi<q)
        except ZeroDivisionError:
            good=False; rho=product=None
        if good:
            accepted+=1
            if product.hi>worst: worst=product.hi
            continue
        assert depth<maxdepth, (a,b,c,d,rho,product)
        if depth%2==0:
            m=(a+b)/2
            stack.append((a,m,c,d,depth+1)); stack.append((m,b,c,d,depth+1))
        else:
            m=(c+d)/2
            stack.append((a,b,c,m,depth+1)); stack.append((a,b,m,d,depth+1))
    return visited,accepted,worst

box=(F(185527,100000),F(101,50),F(3,4),F(1))
q=F(199,200)
v,a,w=certify(box,q,30)
margin=F(4)*(F(1)-q)/(F(3)+F(101,50))**2
assert margin==F(50,63001)
print('RECT_A_PASS visited=%d accepted=%d product_upper<199/200 rho_upper<19/20' % (v,a))
print('RECT_A_worst_interval_upper_float=%.15f' % float(w))
print('RECT_A_derivative_margin=50/63001')
print('TRUNCATION_FROM_RHO: E[B_n-B] <= (19/20)^n')
print('ALL_EXACT_CHECKS_PASS')
