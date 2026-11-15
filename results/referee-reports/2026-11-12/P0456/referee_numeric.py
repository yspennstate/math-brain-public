"""Independent scaled, high precision integral checks; no author code imported."""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
import math, time
import mpmath as mp
from scipy.integrate import quad
from scipy.special import gammainc, gammaln, betainc

mp.mp.dps = 45

def poisson_ratio(k):
    k = int(k)
    def f(s):
        if not s: return mp.mpf(0)
        F = mp.gammainc(k, 0, s, regularized=True)
        Fp = mp.gammainc(k+1, 0, s, regularized=True)
        q = s*F-k*Fp
        return mp.exp(k*mp.log(q)-s-mp.loggamma(k+1)+k) if q > 0 else mp.mpf(0)
    return mp.quad(f, [0,k/2,k,1.5*k,2*k,3*k,5*k,10*k,mp.inf])

def finite_ratio(n,k,m,N):
    mu=mp.mpf(k)/(N+1)
    logc=sum(mp.log(mp.mpf(m-i)/n) for i in range(k+1))-mp.loggamma(k+1)
    def cdf(jmax,N,x):
        # Complementary binomial CDF, independently evaluated by recurrence.
        term=(1-x)**N
        total=term
        for j in range(1,jmax+1):
            term*=mp.mpf(N-j+1)/j*x/(1-x)
            total+=term
        return 1-total
    def f(s):
        if s==0: return mp.mpf(0)
        x=s/n
        Qn=n*(x*cdf(k-1,N,x)-mu*cdf(k,N+1,x))
        return mp.exp(logc+k*mp.log(Qn)+(m-k-1)*mp.log1p(-x)+k) if Qn>0 else mp.mpf(0)
    hi=min(n-1,20*k+100)
    result=mp.quad(f,[0,k/2,k,1.5*k,2*k,3*k,5*k,hi])
    # Q<=x bounds omitted finite tail. Ignore factor (m)_{k+1}/n^{k+1}<=1.
    rate=mp.mpf(m-k-1)/n
    tail=mp.exp(k)*mp.gammainc(k+1,rate*hi,mp.inf)/mp.factorial(k)/rate**(k+1)
    return result,tail

if __name__=='__main__':
    t=time.monotonic()
    print('mpmath',mp.__version__,'dps',mp.mp.dps,flush=True)
    a=mp.mpf(5)/32;b=1/a
    print('constants a-1-log(a)=',mp.nstr(a-1-mp.log(a),24),
          'b-1-log(b)=',mp.nstr(b-1-mp.log(b),24),
          'gamma=',mp.nstr(mp.log(mp.mpf(2)/3)+mp.mpf(1)/2,24),flush=True)
    for k in [6,8,10,20,25,30]:
        hi=poisson_ratio(k)
        def f(s):
            q=s*gammainc(k,s)-k*gammainc(k+1,s)
            return math.exp(k*math.log(q)-s-gammaln(k+1)+k) if q>0 else 0.
        val,err=quad(f,0,20*k+100,epsabs=2e-12,epsrel=2e-12,points=[k,2*k,3*k],limit=200)
        print('limiting k=%d ratio=%s independent_scipy=%.12f err=%.2g'%(k,mp.nstr(hi,20),val,err),flush=True)
        if k>=20:
            def unscaled(s):
                q=s*gammainc(k,s)-k*gammainc(k+1,s)
                return math.exp(k*math.log(max(q,1e-300))-s-gammaln(k+1))
            wrong,wrong_err=quad(unscaled,0,2*k+60*math.sqrt(k)+60,points=[k,2*k],limit=400)
            print('default_unscaled k=%d ratio=%.12f returned_abs_error=%.3g'%(k,wrong*math.exp(k),wrong_err),flush=True)
    for n,k in [(1000,6),(3000,8),(10000,9),(50000,11),(10000000,16)]:
        for m,N in [(n,n),(n-1,n-2)]:
            val,tail=finite_ratio(n,k,m,N)
            logc=sum(math.log((m-i)/n) for i in range(k+1))-gammaln(k+1)
            def finite_scipy(s):
                x=s/n
                Qn=s*betainc(k,N-k+1,x)-n*k/(N+1)*betainc(k+1,N-k+1,x)
                return math.exp(logc+k*math.log(Qn)+(m-k-1)*math.log1p(-x)+k) if Qn>0 else 0.
            check,err=quad(finite_scipy,0,min(n-1,20*k+100),points=[k,2*k,3*k],epsabs=2e-12,epsrel=2e-12,limit=200)
            print('finite n=%d k=%d m=%d N=%d ratio=%s independent_scipy=%.12f scaled_tail_bound=%s'%(n,k,m,N,mp.nstr(val,18),check,mp.nstr(tail,3)),flush=True)
    print('elapsed_seconds',time.monotonic()-t,flush=True)
