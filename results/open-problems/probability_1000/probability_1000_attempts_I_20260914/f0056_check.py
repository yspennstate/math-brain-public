# Numerical sanity check of Theorem (a) [w_1>0 => Thm 18.7 holds for m/n->0] on the weight sequence w_k=1 (uniform weak compositions)
# and of Theorem (b) [w=(1,0,1,1,...) parity failure].  Exact rational/float arithmetic via log-gamma.
from mpmath import mp, mpf, loggamma, exp, log, binomial, findroot
mp.dps = 30
def logC(a,b):
    return loggamma(a+1)-loggamma(b+1)-loggamma(a-b+1)
def uniform_compositions(m,n):
    # w_k = 1: Z(m,n) = C(m+n-1, n-1). P(Y1=k) = Z(m-k,n-1)/Z(m,n) = C(m-k+n-2,n-2)/C(m+n-1,n-1)
    # tilt: xi geometric, P(xi=k)=(1-t)t^k, mean t/(1-t)=m/n -> t = m/(m+n)
    t = mpf(m)/(m+n)
    pk = lambda k: (1-t)*t**k
    # E N_{>=2} = n P(Y1>=2); E N(N-1) = n(n-1) P(Y1>=2, Y2>=2) = n(n-1) sum_{k1,k2>=2} Z(m-k1-k2, n-2)/Z(m,n)
    logZ = lambda mm,nn: logC(mm+nn-1, nn-1) if mm>=0 else None
    Zmn = logZ(m,n)
    EN = n*sum(exp(logZ(m-k,n-1)-Zmn) for k in range(2,m+1))
    # E N(N-1): sum over s=k1+k2>=4 of (#pairs k1,k2>=2 with sum s = s-3) * Z(m-s,n-2)/Z(m,n)
    EN2 = n*(n-1)*sum((s-3)*exp(logZ(m-s,n-2)-Zmn) for s in range(4,m+1))
    alpha = n*sum(pk(k) for k in range(2,m+1)) + n*t**(m+1)  # n P(xi>=2) = n t^2
    return EN, EN2, alpha, n*t**2
for (m,n) in [(100,10**4),(300,10**5),(1000,10**6),(50,10**3)]:
    EN,EN2,alpha,a2 = uniform_compositions(m,n)
    print("w_k=1: m=%d n=%d: E N[2,inf)=%.5f  E N(N-1)=%.5f  Poisson alpha=nP(xi>=2)=%.5f alpha^2=%.5f" % (m,n,float(EN),float(EN2),float(a2),float(a2)**2))
# parity example: w0=1,w1=0,wk=1 (k>=2). Y(1)>=3 a.s. for odd m. Tilted: Phi(t)=1+t^2/(1-t); check nP(xi>=3) for n=k^4, m=2k+1
def parity(k):
    n=k**4; m=2*k+1; mu=mpf(m)/n
    Phi=lambda t: 1+t**2/(1-t)
    Psi=lambda t: t*(2*t-t**2)/((1-t)**2*Phi(t))
    tau=findroot(lambda t: Psi(t)-mu, mpf(k)**-1.5)
    p3 = (tau**3/(1-tau))/Phi(tau)
    return tau*k**1.5, n*p3
for k in [10,100,1000]:
    r=parity(k); print("parity k=%d: tau*k^1.5=%.5f nP(xi>=3)=%.5f"%(k,float(r[0]),float(r[1])))
