"""Independent quadrature from one-edge/two-edge rejection probabilities.

No use of q_n, X, or the covariance formula in PAPER.tex. Integrate scores
u<v of two root edges, conditioning only on their shared non-root edge.
"""
import json
import math
import numpy as np
from scipy.special import betainc, roots_legendre

def low(m,h,x):
    if h < 0: return np.zeros_like(x)
    if h >= m: return np.ones_like(x)
    return betainc(m-h,h+1,1-x)

def high(m,h,x):
    if h <= 0: return np.ones_like(x)
    if h > m: return np.zeros_like(x)
    return betainc(h,m-h+1,x)

def moments(n,k,order=192):
    s=math.sqrt(k*(n-k)/n)
    p=k/n
    # Normal scale, with generous tails; for fixed small complements use
    # a larger asymmetric range in y=n(1-u).
    if n-1-k <= 5:
        a=max(0,1-(80+4*(n-1-k))/n)
        b=1.
    else:
        a=max(0,p-16*s/n)
        b=min(1,p+16*s/n)
    t,w=roots_legendre(order)
    v=a+(b-a)*(t+1)/2
    wv=w*(b-a)/2
    f=low(n-2,k-1,v)
    eh=(n-1)*np.dot(wv,f*high(n-2,k,v))
    u=a+(v[:,None]-a)*(t[None,:]+1)/2
    wu=(v[:,None]-a)*w[None,:]/2
    ar=high(n-3,k,u)
    br=high(n-3,k-1,u)
    av=high(n-3,k,v)[:,None]
    bv=high(n-3,k-1,v)[:,None]
    vv=v[:,None]
    kernel=u*br*bv+(vv-u)*ar*bv+(1-vv)*ar*av
    inner=np.sum(wu*kernel,axis=1)
    f2=2*(n-1)*(n-2)*np.dot(wv,low(n-3,k-2,v)*inner)
    return float(eh),float(eh+f2-eh*eh)

def main():
    exact=json.load(open('referee_exact.json'))
    for n,k in ((12,4),(12,8),(40,20),(80,30),(80,78)):
        e,v=moments(n,k,256)
        from fractions import Fraction
        target=exact[f'{n},{k}']
        err=max(abs(e-float(Fraction(target['eh']))),abs(v-float(Fraction(target['var']))))
        print(f'exact cross-check n={n} k={k} max_error={err:.3g}')
        assert err<2e-10
    cases = [(n,n//2) for n in (1000,10000,100000,1000000)]
    cases += [(n,n//10) for n in (1000,10000,100000,1000000)]
    cases += [(n,math.isqrt(n)) for n in (100,10000,1000000,100000000)]
    cases += [(n,k) for n in (1000,10000,20000) for k in (n//4,n//2,math.isqrt(n),n-2,n-3,n-6)]
    out={}
    for n,k in dict.fromkeys(cases):
        e,v=moments(n,k,192)
        e2,v2=moments(n,k,320)
        s=math.sqrt(k*(n-k)/n)
        diff=max(abs(e-e2)/s,abs(v-v2)/(s*s))
        print(f'n={n} k={k} EH={e2:.12f} VH={v2:.12f} EH/s={e2/s:.9f} VH/s2={v2/s**2:.9f} order_difference={diff:.3g}')
        out[f'{n},{k}']=dict(eh=e2,var=v2,order_difference=diff)
    json.dump(out,open('referee_numeric.json','w'),indent=2)

if __name__=='__main__': main()
