"""Exact connected regularizations of the previous rational sparse witness."""
import sympy as s
H=s.eye(5)-s.ones(5)/5
W=s.zeros(5)
for i,j,v in [(0,1,s.Rational(110,789)),(0,3,s.Rational(110,789)),(0,2,s.Rational(272,789)),(1,3,s.Rational(99,263))]:
    W[i,j]=W[j,i]=v
L0=s.diag(*[sum(W.row(i)) for i in range(5)])-W
lam0=s.Rational(704,789)
a0=lam0
b0=s.Rational(178,263)
G0=lam0*H-L0
Pi=H-((a0+b0)*G0-G0*G0)/(a0*b0)
assert Pi*Pi==Pi and Pi*G0==s.zeros(5) and s.trace(Pi)==2
for eps in [s.Rational(1,1000),s.Rational(1,1000000)]:
    scale=1-10*eps
    L=scale*L0+5*eps*H
    lam=scale*lam0+5*eps
    a,b=scale*a0,scale*b0
    G=lam*H-L
    assert G==scale*G0 and L*Pi==lam*Pi
    assert min(-L[i,j] for i in range(5) for j in range(i+1,5))==eps
    assert lam-a==5*eps
    X1=2*(lam*s.trace(G)-s.trace(G*G))
    X2=s.Rational(10,3)*sum(Pi[i,j]*G[i,j]**2 for i in range(5) for j in range(5))
    X3=(1-lam)/3*(2*s.trace(G)-s.Rational(10,3)*sum(Pi[i,i]*G[i,i] for i in range(5)))
    Y=2*sum(-L[i,j]*(Pi[i,i]+Pi[j,j]-2*Pi[i,j])*(G[i,i]+G[j,j]-2*G[i,j]) for i in range(5) for j in range(i+1,5))
    T=X1+X2+X3-Y
    quotient=s.factor(T/(X1+X2+X3))
    assert T>=s.Rational(7,45)*(a+b)*(lam-a)>0
    print('PROVED: epsilon =',eps,'exact quotient =',quotient,flush=True)
    print('NUMERICAL: decimal quotient =',s.N(quotient,20),flush=True)
    assert quotient<(s.Rational(381,10000) if eps==s.Rational(1,1000) else s.Rational(203,10000))
