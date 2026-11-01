import sympy as sp
from dataclasses import dataclass

# Symbolic two-plateau slack identity.
rho, y = sp.symbols("rho y", positive=True)
alpha = 1-rho
lhs = 1-rho*(1+y) + rho*y**2/(2*alpha)
rhs = alpha*(1-rho/2) + rho*(y-alpha)**2/(2*alpha)
assert sp.factor(lhs-rhs) == 0
print("COMPLETE_SQUARE_IDENTITY_PASS")

# Exact finite example X in {1,2,3,5}.
xs = list(map(sp.Rational, [1,2,3,5]))
ps = [sp.Rational(3,5), sp.Rational(3,10), sp.Rational(9,100), sp.Rational(1,100)]
mu = sp.factor(sum(p*x for p,x in zip(ps,xs)))
starts=[]
for j,x0 in enumerate(xs):
    l = sp.Rational(0) if j==0 else xs[j-1]
    S = sum(ps[j:])
    starts.append(sp.factor(sum(ps[i]*xs[i] for i in range(j,len(xs)))/S-l))
assert starts == [sp.Rational(38,25), sp.Rational(13,10), sp.Rational(6,5), sp.Rational(2)]
assert starts[-1] > starts[0] and all(h <= starts[0] for h in starts[1:-1])
print("ONE_MS_RECORD_EXAMPLE", starts)

@dataclass
class Seg:
    l: sp.Rational
    u: sp.Rational
    m: sp.Rational
    c: sp.Rational
    def val(self,a):
        return sp.factor(self.m*a+self.c)

def gittins_segments(xs, ps):
    xs=list(map(sp.Rational,xs)); n=len(xs); segs=[]
    for j in range(n):
        l=sp.Rational(0) if j==0 else xs[j-1]
        u=xs[j]
        S=sum(ps[j:])
        lines=[]
        for k in range(j,n):
            den=sum(ps[j:k+1])
            C=sum(ps[i]*xs[i] for i in range(j,k+1)) + xs[k]*sum(ps[k+1:])
            lines.append((-S/den, sp.factor(C/den)))
        pts={l,u}
        for i in range(len(lines)):
            for h in range(i+1,len(lines)):
                m1,c1=lines[i]; m2,c2=lines[h]
                if m1 != m2:
                    z=sp.factor((c2-c1)/(m1-m2))
                    if l < z < u:
                        pts.add(z)
        pts=sorted(pts)
        for A,B in zip(pts[:-1],pts[1:]):
            mid=(A+B)/2
            m,c=min(lines,key=lambda mc: mc[0]*mid+mc[1])
            if segs and segs[-1].u==A and segs[-1].m==m and segs[-1].c==c:
                segs[-1].u=B
            else:
                segs.append(Seg(A,B,m,c))
    return segs

gsegs=gittins_segments(xs,ps)
# Fresh Gittins rank is below mu; the only strict new record occurs at age 3.
fresh=gsegs[0].val(0)
startsG=[]
for s in gsegs:
    if s.l in xs[:-1] or s.l==0:
        startsG.append((s.l,sp.factor(s.val(s.l))))
record=fresh
record_ages=[]
for a,v in startsG[1:]:
    if v>record:
        record=v
        record_ages.append(a)
assert fresh <= mu
assert record_ages == [sp.Rational(3)]
print("GITTINS_INTERNAL_RECORD_AGES", record_ages)

# Exact high-load response formulas for the two-plateau M-SERPT policy.
rho0=sp.Rational(19,20)
lam=sp.factor(rho0/mu)
b=sp.Rational(3)
tail_mass=sp.factor(sum(p for p,x in zip(ps,xs) if x>b))
p0=1-tail_mass
m=sp.factor(sum(p*min(x,b) for p,x in zip(ps,xs)))
B=sp.factor(sum(p*x for p,x in zip(ps,xs) if x>b))
Vb=sp.factor(sum(p*min(x,b)**2 for p,x in zip(ps,xs)))
V=sp.factor(sum(p*x*x for p,x in zip(ps,xs)))
A=sp.factor(1-lam*m)
alpha0=sp.factor(1-rho0)
Q=sp.factor(p0*lam*Vb/(2*A)+tail_mass*lam*V/(2*A*alpha0))
R=sp.factor(mu+lam*m*B/A)
slack=sp.factor(Q+2*mu-R)
lower=sp.factor(mu*alpha0*(1-rho0/2)/A)
assert mu==sp.Rational(38,25)
assert lam==sp.Rational(5,8)
assert A==sp.Rational(1,16)
assert Q==sp.Rational(649,40)
assert R==sp.Rational(227,100)
assert slack==sp.Rational(3399,200)
assert lower==sp.Rational(399,625)
assert slack >= lower > 0
print("EXACT_EXAMPLE_Q_R_SLACK", Q, R, slack, "LOWER", lower)

# Algebraic Cauchy reduction: the only inequality-specific tail term is B^2 <= r E[X^2 1_tail].
tail_second=sp.factor(sum(p*x*x for p,x in zip(ps,xs) if x>b))
assert sp.factor(tail_mass*tail_second-B**2) >= 0
print("TAIL_CAUCHY_EXAMPLE_PASS", sp.factor(tail_mass*tail_second-B**2))

print("ALL_EXACT_CHECKS_PASS")
