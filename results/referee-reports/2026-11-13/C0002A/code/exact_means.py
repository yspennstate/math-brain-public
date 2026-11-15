"""Exact Gaussian means; continuum integrals from a disk-to-square map.

f'(z)=C/sqrt(1-z^4), C=1/(sqrt(2)*integral_0^1(1-s^4)^(-1/2)ds).
J(s)=int_D r_D^s = pi*C^(s+2)*sum_k ((nu)_k/k!)^2*B(4k+1,s+1),
nu=(s+2)/4. Analytic derivatives give log-radius moments.
"""
import csv
import gc
import json
import time
from pathlib import Path
from dgff import G, diagonal, check_resources, peak_bytes
import numpy as np
from scipy.special import betaln, beta as betafn, gammaln, digamma, polygamma, ndtr

ROOT=Path(__file__).resolve().parents[1]
C=1/(np.sqrt(2)*betafn(.25,.5)/4)
C0=G*(np.euler_gamma+1.5*np.log(2))

def integrals(s, terms=100000):
    nu=(s+2)/4
    k=np.arange(terms,dtype=float)
    logw=(np.log(np.pi)+(s+2)*np.log(C)+
          2*(gammaln(k+nu)-gammaln(nu)-gammaln(k+1))+
          betaln(4*k+1,s+1))
    w=np.exp(logw)
    a=np.log(C)+.5*(digamma(k+nu)-digamma(nu))+digamma(s+1)-digamma(4*k+s+2)
    b=.125*(polygamma(1,k+nu)-polygamma(1,nu))+polygamma(1,s+1)-polygamma(1,4*k+s+2)
    vals=np.array([w.sum(),(w*a).sum(),(w*(a*a+b)).sum()])
    # Leading asymptotic tail plus half the endpoint. Missing terms are
    # O(K^(-s/2-2)*log(K)^j); doubling K checks numerical stability.
    power=s/2+2
    logconst=np.log(np.pi)+(s+2)*np.log(C)+gammaln(s+1)-2*gammaln(nu)-(s+1)*np.log(4)
    da=np.log(C)+digamma(s+1)-.5*digamma(nu)-np.log(4)
    db=polygamma(1,s+1)-.125*polygamma(1,nu)
    for mult,offset in [(1/(power-1),1),(.5,0)]:
        tail=np.exp(logconst+(offset-power)*np.log(terms))*mult
        ta=da-.5*np.log(terms)-(.5/(power-1) if offset else 0)
        tb=db+(.25/(power-1)**2 if offset else 0)
        vals+=tail*np.array([1,ta,ta*ta+tb])
    return vals

def constants(lam, terms=100000):
    beta=2*lam/np.sqrt(G); a=beta*beta/2; cb=1/(beta*np.sqrt(2*np.pi*G))
    j,j1,j2=integrals(a*G,terms)
    i0=np.exp(a*C0)*j
    i1=np.exp(a*C0)*(C0*j+G*j1)
    i2=np.exp(a*C0)*(C0*C0*j+2*C0*G*j1+G*G*j2)
    return dict(m=cb*i0,B=cb/G*(i1/2-beta*beta*i2/2-i0/(beta*beta)),
                weighted_q_mean=i1/i0,weighted_q2_mean=i2/i0)

if __name__=='__main__':
    lambdas=[.2,.4,.6,.8]
    const={str(l):constants(l) for l in lambdas}
    checks={str(l):{k:constants(l,50000)[k]-const[str(l)][k] for k in ['m','B']} for l in lambdas}
    area=integrals(0)[0]
    assert abs(area-1)<1e-8
    (ROOT/'data'/'continuum_constants.json').write_text(json.dumps(dict(
        C=C,c0=C0,area_check=area,constants=const,truncation_difference=checks,
        formula='disk-square map; positive series with leading tail correction'),indent=2)+'\n')
    print('continuum',json.dumps(const),flush=True)
    rows=[]; started=time.monotonic()
    for N in [32,64,128,256,512,1024,2048,4096,8192]:
        check_resources(N)
        L=np.log(N); t=G*L
        sums={l:np.zeros(3) for l in lambdas}
        for _,v in diagonal(N):
            q=v-t
            for lam in lambdas:
                beta=2*lam/np.sqrt(G); cb=1/(beta*np.sqrt(2*np.pi*G))
                w=np.exp(beta*beta*q/2)
                sums[lam]+=np.array([
                    np.sqrt(L)*np.exp(beta*beta*t/2)*ndtr(-beta*t/np.sqrt(v)).sum(),
                    cb*w.sum(),
                    cb/G*(w*(q/2-beta*beta*q*q/2-1/(beta*beta))).sum()])/N**2
        for lam in lambdas:
            ex,ey,bn=sums[lam]; m=const[str(lam)]['m']; B=const[str(lam)]['B']
            rows.append(dict(N=N,**{'lambda':lam},EX=ex,EY=ey,B_N=bn,m=m,B=B,
                             log_bias=L*(ex-m),first_order_remainder=L*L*(ex-m-B/L)))
        with (ROOT/'data'/'exact_means.csv').open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
        gc.collect()
        print(f'exact means N={N}, peak={peak_bytes()/1e9:.3f} GB',flush=True)
    (ROOT/'data'/'metadata_exact.json').write_text(json.dumps(dict(
        seconds=time.monotonic()-started,peak_bytes=peak_bytes(),nice=check_resources(32)['nice'],threads=1),indent=2)+'\n')
