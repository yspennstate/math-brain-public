from fractions import Fraction as F

# Rigorous rational interval arithmetic; no floating-point sign is used.
class I:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self,o):
        o=asI(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-asI(o))
    def __rsub__(self,o): return asI(o)-self
    def __mul__(self,o):
        o=asI(o); xs=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]; return I(min(xs),max(xs))
    __rmul__=__mul__
    def recip(self):
        assert not (self.lo <= 0 <= self.hi)
        return I(min(F(1,self.lo),F(1,self.hi)),max(F(1,self.lo),F(1,self.hi)))
    def __truediv__(self,o): return self*asI(o).recip()
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        if n==0:return I(1)
        vals=[self.lo**n,self.hi**n]
        if n%2==0 and self.lo<0<self.hi: vals.append(F(0))
        return I(min(vals),max(vals))
    def __repr__(self): return f'[{self.lo}, {self.hi}]'
def asI(x): return x if isinstance(x,I) else I(x)

def log_near1_interval(y, N=50):
    # y rational in [1,2]. atanh series z=(y-1)/(y+1).
    assert F(1) <= y <= F(2)
    z=(y-1)/(y+1)
    s=F(0)
    for n in range(N+1): s += z**(2*n+1)/F(2*n+1)
    partial=2*s
    # positive remainder bound for z>=0
    rem=2*z**(2*N+3)/(F(2*N+3)*(1-z*z))
    return I(partial, partial+rem)

def log2_interval(N=50): return log_near1_interval(F(2),N)

def log_rat_interval(x,N=50):
    assert x>0
    k=0; y=F(x)
    while y>=2:
        y/=2; k+=1
    while y<1:
        y*=2; k-=1
    return log_near1_interval(y,N)+k*log2_interval(N)

# Strict positive contraction K with eigenvalues 49/50,1/200,1/200:
# K_ii=33/100, K_ij=13/40.
a=F(49,50); b=F(1,200)
p0=F(39601,2000000); p1=F(646949,2000000); p12=F(6501,2000000); p123=F(49,2000000)
assert p0+3*p1+3*p12+p123 == 1
rc=F(10569001,6501)
rt=F(274751769501,335042626769501)
assert rc == p1*p1/(p0*p12)
assert rt == p0*p12**3/(p1**3*p123)
c=log_rat_interval(rc)
tau=log_rat_interval(rt)
# M=c I + tau K, so eigenvalues along (1,1,1) and its orthogonal plane.
ma=c+tau*a; mb=c+tau*b
d=ma*mb*mb
assert d.lo>0
# Explicit frozen statistic R(S), depending only on n=|S|.
r0=I(0)
r1=c*c/d
r2=(2*c*c+tau*c)/d
r3=(3*c*c+3*tau*c+tau*tau)/d
mean=p0*r0+3*p1*r1+3*p12*r2+p123*r3
second=p0*r0*r0+3*p1*r1*r1+3*p12*r2*r2+p123*r3*r3
var=second-mean*mean
Q=d*var
assert Q.lo > F(3,2), Q
print('PASS')
print('claim=P11-LYONS-DUALVAR-UNIVERSAL-01 DISPROVED')
print('K_diag=33/100 K_offdiag=13/40 eigenvalues=49/50,1/200,1/200')
print('Q_lower_decimal=',format(float(Q.lo),'.15g'))
print('Q_upper_decimal=',format(float(Q.hi),'.15g'))
print('threshold=3/2')
