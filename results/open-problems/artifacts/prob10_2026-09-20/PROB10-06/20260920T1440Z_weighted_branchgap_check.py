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
        assert not (self.lo<=0<=self.hi),(self.lo,self.hi)
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

def G(L,z):
    # G(z)=1/((lambda+1/z)(lambda-1+1/z)).
    return z*z/((L*z+1)*((L-1)*z+1))

def box_bound(l0,l1,p0,p1,use_favorable_term=True):
    y2,y3=corner_supersolution(l1,p0)
    d2,d3=1/y2,1/y3
    L=I(l0,l1); P=I(p0,p1); w2,w3=1-P,P
    a=L-1; u=(3-L)/3; Dmax=(9-L)/3

    # Analytic shape conditions used in the proof.
    # u<a makes x/(a+x)^2 increasing/concave on [0,u].
    assert u.hi<a.lo
    # Source f(s)=s/[lambda(lambda+s)(a+s)] is increasing/concave
    # on s in [0,3u] once (3u)^2 <= lambda*a.
    assert (3*u).sq().hi <= (L*a).lo
    # K(x,t)=x/[(x+t)(x+t+1)] decreases in x at t<=2u.
    assert a.sq().lo >= (2*u*(2*u+1)).hi
    # G is increasing and concave for z>=1/(2u):
    # lambda*a*((2lambda-1)z^3+3z^2) >= 1.
    zlo=(1/(2*u)).lo
    assert L.lo*(L.lo-1)*((2*L.lo-1)*zlo**3+3*zlo**2) >= 1

    dbar=w2*d2+w3*d3

    # Reciprocal-Jensen sibling kernels R_1,R_2.
    R1=w2*G(L,y2)+w3*G(L,y3)
    h22=H([y2,y2]); h23=H([y2,y3]); h33=H([y3,y3])
    R2=(w2*w2*G(L,h22)+2*w2*w3*G(L,h23)+w3*w3*G(L,h33))
    rho_s=a*((1-P)*2*R1+P*3*R2)
    if rho_s.hi>=1:
        return None

    # s=E[U/(a+B)] <= mu*C_s.
    C0=((1-P)*2/(L*(L+2*dbar)*(a+2*dbar))
        +P*3/(L*(L+3*dbar)*(a+3*dbar)))
    Cs=C0/(1-rho_s)

    # -J' <= 2 q(s+r), with q<=mu/(a+dbar),
    # r<=mu/(a+dbar)^2.  The optional favorable term comes from
    # Delta=(-J'-d h_2)/c_3 and
    # d h_2 >= a*mu^2/[8(2+u)].
    coeff=2/(a+dbar)*(Cs+1/(a+dbar).sq())
    if use_favorable_term:
        coeff=coeff-a/(8*(2+u))
    assert coeff.lo>=0
    Delta=Dmax*u*coeff

    theta0=3*p0/(4-p0)
    assert theta0*theta0+4*theta0-2>0
    g0=theta0*(1-theta0)/(2+theta0)
    product=L*g0*Delta
    return product,rho_s,Delta

def certify(rect,q,rho_q,maxdepth=28):
    l0,l1,p0,p1=map(F,rect)
    stack=[(l0,l1,p0,p1,0)]
    visited=accepted=max_depth=0
    worst_product=F(-10**6); worst_rho=F(-10**6)
    while stack:
        a,b,c,d,depth=stack.pop()
        visited+=1; max_depth=max(max_depth,depth)
        ans=box_bound(a,b,c,d,True)
        good=(ans is not None and ans[0].hi<q and ans[1].hi<rho_q)
        if good:
            accepted+=1
            worst_product=max(worst_product,ans[0].hi)
            worst_rho=max(worst_rho,ans[1].hi)
            continue
        assert depth<maxdepth,("uncertified",a,b,c,d,depth,ans)
        if depth%2==0:
            m=(a+b)/2
            stack.append((a,m,c,d,depth+1)); stack.append((m,b,c,d,depth+1))
        else:
            m=(c+d)/2
            stack.append((a,b,c,m,depth+1)); stack.append((a,b,m,d,depth+1))
    return visited,accepted,max_depth,worst_product,worst_rho

# Inherited theorem reaches lambda=12/5 for p>=3/4.  Certify only new strip.
rect=(F(12,5),F(2587,1000),F(3,4),F(1))
q=F(999,1000); rho_q=F(99,100)
v,a,dep,wp,wr=certify(rect,q,rho_q)
margin=4*(1-q)/(F(3)+F(2587,1000))**2
assert margin==F(4000,31214569)

# The crude scalar reciprocal supersolution is still legitimate at the
# endpoint: 1-L*(3-P)/6 = 239/8000 >0.
assert 1-F(2587,1000)*(3-F(3,4))/6 == F(239,8000)

# Attack C is quantitatively nonvacuous at the hard corner.  Without the
# favorable -d h_2 term, this proof does not reach the clean 999/1000 product
# margin; retaining the term does.
base=box_bound(F(2587,1000),F(2587,1000),F(3,4),F(3,4),False)
refined=box_bound(F(2587,1000),F(2587,1000),F(3,4),F(3,4),True)
assert base[0].lo > F(999,1000)
assert refined[0].hi < F(999,1000)

print("WEIGHTED_BRANCHGAP_CHECK")
print("RECT_PASS lambda=[12/5,2587/1000] p=[3/4,1]")
print("visited=%d accepted=%d max_depth=%d"%(v,a,dep))
print("speed_product_upper<999/1000")
print("weighted_contraction_rho_s<99/100")
print("worst_product_upper_float=%.15f"%float(wp))
print("worst_rho_s_upper_float=%.15f"%float(wr))
print("derivative_margin=4000/31214569")
print("log_truncation=> E[B_N-B] <= (2587/1400)*(99/100)^N")
print("HARD_CORNER_BASE_PRODUCT_float=%.15f"%float(base[0].lo))
print("HARD_CORNER_REFINED_PRODUCT_float=%.15f"%float(refined[0].hi))
print("TYPE_VECTOR_CORNER_SLACK=239/8000")
print("ROUNDING_GRID=1e-9 TYPE_VECTOR_ITERATIONS=30")
print("ALL_EXACT_CHECKS_PASS")