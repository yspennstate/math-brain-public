#!/usr/bin/env python3
"""Independent DTCS referee calculations. Does not read or import src.

Run: OPENBLAS_NUM_THREADS=1 python3 referee_audit.py --n 12000
Outputs referee_results.json and timestamped LOG.md entries.
"""
import argparse
from collections import defaultdict
from datetime import datetime
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial, log
from pathlib import Path
import json
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parent

def log_event(s):
    with (ROOT/'LOG.md').open('a') as f:
        f.write('\n- '+datetime.now().astimezone().isoformat(timespec='seconds')+': '+s+'\n')
    print(s, flush=True)

def tolls(n,i):
    return (n, abs(n-2*i), (n-2*i)**2, 2*min(i,n-i))

def exact(N=24):
    # Raw binomial recursion through fourth order, four separate statistics.
    R=[[[F(0) for n in range(N+1)] for k in range(5)] for s in range(4)]
    for r in R:
        r[0]=[F(1)]*(N+1)
    h=F(0)
    pmfs=[[{0:F(1)}] for s in range(4)]
    for n in range(2,N+1):
        h+=F(1,n-1)
        for i in range(1,n):
            q=F(n,2)*F(1,i*(n-i))/h
            for s,t in enumerate(tolls(n,i)):
                for k in range(1,5):
                    for a in range(k+1):
                        for b in range(k-a+1):
                            c=k-a-b
                            R[s][k][n]+=q*comb(k,a)*comb(k-a,b)*R[s][a][i]*R[s][b][n-i]*t**c
        if n<=10:
            for s in range(4):
                out=defaultdict(F)
                for i in range(1,n):
                    q=F(n,2*i*(n-i))/h
                    t=tolls(n,i)[s]
                    for u,pu in pmfs[s][i-1].items():
                        for v,pv in pmfs[s][n-i-1].items():
                            out[u+v+t]+=q*pu*pv
                assert sum(out.values())==1
                for k in range(1,5):
                    assert sum(p*x**k for x,p in out.items())==R[s][k][n]
                pmfs[s].append(dict(out))
        ej=sum(F(n,2*i*(n-i))/h*min(i,n-i) for i in range(1,n))
        r=n//2
        hr=sum((F(1,j) for j in range(1,r+1)),F(0))
        formula=F(n)/h*(h-hr+(F(1,n) if n%2==0 else 0))
        assert ej==formula
        assert R[0][1][n]-R[1][1][n]==R[3][1][n]
    return R, {str(n):{s:[str(R[j][k][n]) for k in range(1,5)] for j,s in enumerate(('S','C','QC','D'))} for n in (2,3,4,5,10,24)}

def high_precision(N=100):
    # Raw moments; compared with central float moments below.
    mp.mp.dps=60
    out=[]
    for s in range(4):
        R=[[mp.mpf(1) if k==0 else mp.mpf(0) for n in range(N+1)] for k in range(5)]
        h=mp.mpf(0)
        for n in range(2,N+1):
            h+=mp.mpf(1)/(n-1)
            for i in range(1,n):
                q=mp.mpf(n)/(2*h*i*(n-i)); t=tolls(n,i)[s]
                for k in range(1,5):
                    R[k][n]+=q*sum(comb(k,a)*comb(k-a,b)*R[a][i]*R[b][n-i]*t**(k-a-b) for a in range(k+1) for b in range(k-a+1))
        u=R[1][N]
        out.append([u]+[sum(comb(k,j)*(-u)**(k-j)*R[j][N] for j in range(k+1)) for k in range(2,5)])
    return out

def floating(N,rat):
    # Mean, variance, third/fourth CENTRAL moment. Independent of exact raw recursion.
    A=np.zeros((4,4,N+1))
    H=np.zeros(N+1); H[1:]=np.cumsum(1/np.arange(1,N+1,dtype=float))
    checkpoints={24,100,500,2000,4000,8000,N}
    rows={}; diagnostics={}
    z=float(mp.zeta(2)); b=float(mp.euler/mp.zeta(2)+mp.zeta(3)/mp.zeta(2)**2)
    kap=float((2*mp.zeta(3)-mp.zeta(2))/mp.zeta(2)**2)
    a3=float(kap/mp.zeta(2)-2*(6*mp.zeta(4)-3*mp.zeta(3)-mp.mpf('1.5')*mp.zeta(2))/(3*mp.zeta(2)**3))
    for n in range(2,N+1):
        i=np.arange(1,n,dtype=float); j=n-i
        q=n/(2*H[n-1]*i*j)
        T=(np.full(n-1,n),abs(n-2*i),(n-2*i)**2,2*np.minimum(i,j))
        for s,t in enumerate(T):
            a=A[s]; left=a[:,1:n]; right=left[:,::-1]
            mu=left[0]+right[0]+t
            a[0,n]=np.sum(q*mu)
            B=mu-a[0,n]; V=left[1]+right[1]; U=left[2]+right[2]
            a[1,n]=np.sum(q*(V+B**2))
            a[2,n]=np.sum(q*(U+3*B*V+B**3))
            a[3,n]=np.sum(q*(left[3]+right[3]+6*left[1]*right[1]+4*B*U+6*B**2*V+B**4))
        if n<=24:
            for s in range(4):
                u=rat[s][1][n]
                expected=[u]+[sum(F(comb(k,j))*(-u)**(k-j)*rat[s][j][n] for j in range(k+1)) for k in range(2,5)]
                for k,x in enumerate(expected):
                    assert abs(A[s,k,n]-float(x))<=1e-10*max(1,abs(float(x)))
        if n in checkpoints:
            L=log(n)
            rows[str(n)]={s:{'mean':float(A[k,0,n]),'variance':float(A[k,1,n]),'scaled_variance':float(A[k,1,n]/(n**(4 if k==2 else 2)*L**2)), 'skewness':float(A[k,2,n]/A[k,1,n]**1.5),'kurtosis':float(A[k,3,n]/A[k,1,n]**2)} for k,s in enumerate(('S','C','QC','D'))}
            rows[str(n)]['mean_remainders']={'S_over_n':float(A[0,0,n]/n-L**2/(2*z)-b*L),'D_over_n':float(A[3,0,n]/n-2*log(2)/z*L),'QC_over_n2':float(A[2,0,n]/n**2-L)}
            x=i/n; y=1-x; ent=-x*np.log(x)-y*np.log(y)
            # Actual nonrecursive tolls and their separate components.
            di={}
            for s in (0,1):
                a=A[s]; left=a[:,1:n]; right=left[:,::-1]
                B=T[s]+left[0]+right[0]-a[0,n]
                V=left[1]+right[1]; U=left[2]+right[2]
                di[('S','C')[s]]={'B_uniform_error_over_n':float(np.max(abs(B+n*L*ent/z))/n),'V_uniform_error':float(np.max(abs(V-a[1,n]-kap*n*n*L*L*(x*x+y*y-1)))/(n*n*L*L)), 'cubic_terms_scaled':[float(np.sum(q*v)/(n**3*L**3/H[n-1])) for v in (3*B*(V-a[1,n]),B**3)],'quartic_terms_scaled':[float(np.sum(q*v)/(n**4*L**4/H[n-1])) for v in (6*left[1]*right[1],4*B*(U-a[2,n]),6*B*B*V,B**4)]}
            diagnostics[str(n)]=di
            log_event('Float central recursion finished n='+str(n))
    return A,rows,diagnostics

def analytic():
    mp.mp.dps=70
    z=mp.zeta(2)
    def H(x): return -x*mp.log(x)-(1-x)*mp.log(1-x)
    def integral(f): return mp.quad(lambda x:f(x)/(2*x*(1-x)),[0,mp.mpf('.5'),1])
    J={k:integral(lambda x:H(x)**k) for k in range(1,5)}
    J3formula=6*mp.zeta(4)-3*mp.zeta(3)-mp.mpf('1.5')*z
    kap=J[2]/z**2; a3=(3*kap/(2*z)-J[3]/z**3)/mp.mpf('1.5')
    mixed=integral(lambda x:H(x)**2*(x*x+(1-x)**2))
    q4=[kap**2/2,3*a3/z,6*kap*mixed/z**2,J[4]/z**4]
    a4=sum(q4)*6/11
    assert abs(J[3]-J3formula)<mp.mpf('1e-60')
    # Second derivation: extract coefficients of the formal equation (27)
    # without using the individual cubic/quartic toll coefficients above.
    central=[mp.mpf(1),mp.mpf(0)]
    formal_components={}
    for k in range(2,5):
        terms=[]
        for a in range(k+1):
            for bb in range(k-a+1):
                c=k-a-bb
                if a==k or bb==k:
                    continue
                if central[a]==0 or central[bb]==0:
                    continue
                coefficient=comb(k,a)*comb(k-a,bb)*central[a]*central[bb]
                terms.append(coefficient*integral(lambda x:x**a*(1-x)**bb*(-H(x)/z)**c))
        drift=k*central[k-1]
        central.append((drift+sum(terms))/sum(mp.mpf(1)/j for j in range(1,k)))
        formal_components[str(k)]={'drift':str(drift),'integral_terms':[str(v) for v in terms],'moment':str(central[k])}
    for x,y in zip(central[2:],(kap,a3,a4)):
        assert abs(x-y)<mp.mpf('1e-60')
    m=[F(1)]
    for k in range(1,31):
        val=k*m[-1]+sum((F(comb(k,j),2)*m[j]*m[k-j]*F(factorial(2*j-1)*factorial(2*k-2*j-1),factorial(2*k-1)) for j in range(1,k)),F(0))
        m.append(val/sum((F(1,j) for j in range(1,2*k)),F(0)))
        assert 0<=m[-1]<=factorial(k)
    # Laplace equation by quadrature of independently evaluated moment series.
    def phi(s): return sum((-s)**k*mp.mpf(v.numerator)/v.denominator/mp.factorial(k) for k,v in enumerate(m))
    lap={}
    for s in (mp.mpf('.1'),mp.mpf('.3')):
        rhs=integral(lambda x:phi(s*x*x)*phi(s*(1-x)**2)-phi(s))
        lap[str(s)]={'lhs':str(s*phi(s)),'rhs':str(rhs),'residual':str(rhs-s*phi(s)), 'note':'30-term polynomial, not exact transform'}
    return {'J':{str(k):str(v) for k,v in J.items()},'J3_zeta':str(J3formula),'kappa':str(kap),'a3':str(a3),'a4':str(a4),'S_skew':str(a3/kap**mp.mpf('1.5')),'S_kurt':str(a4/kap**2),'cubic_components':[str(3*kap/(2*z)),str(-J[3]/z**3)],'quartic_components':[str(v) for v in q4], 'formal_central_moment_check':formal_components, 'QC_moments':[str(v) for v in m], 'laplace_series_quadrature':lap}

def riemann():
    out={}
    for n in (100,1000,10000,100000,1000000):
        x=np.arange(1,n,dtype=float)/n; y=1-x; L=log(n)
        row={}
        for p,r in ((.1,0),(.5,0),(.9,0),(1.1,1),(2,4),(3,3),(4,4)):
            # Algebraically stable defect of n^p log^r n.
            val=np.sum((1-x**p*(1+np.log(x)/L)**r-y**p*(1+np.log(y)/L)**r)/(2*x*y))/n
            target=float(mp.digamma(p)+mp.euler)
            row[str((p,r))]={'scaled_defect':float(val),'limit':target}
        out[str(n)]=row
    return out

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--n',type=int,default=12000); args=parser.parse_args()
    original=sha256((ROOT/'REPORT_UNDER_REVIEW.md').read_bytes()).hexdigest()
    # src is inspected for metadata only, and never read as computational input.
    src_before={str(p.relative_to(ROOT)):(p.stat().st_size,p.stat().st_mtime_ns) for p in (ROOT/'src').rglob('*') if p.is_file()}
    log_event('Starting fresh exact raw/PMF checks and analytic quadratures; no src code used.')
    rat,summary=exact(); const=analytic(); hp=high_precision()
    log_event('Exact rational raw moments through n=24, PMFs through n=10, and 60-digit raw moments at n=100 complete.')
    A,rows,diagnostics=floating(args.n,rat)
    err=max(abs(float(hp[s][k])-A[s,k,100])/max(1,abs(float(hp[s][k]))) for s in range(4) for k in range(4))
    assert err<1e-10
    assert sha256((ROOT/'REPORT_UNDER_REVIEW.md').read_bytes()).hexdigest()==original
    src_after={str(p.relative_to(ROOT)):(p.stat().st_size,p.stat().st_mtime_ns) for p in (ROOT/'src').rglob('*') if p.is_file()}
    assert src_before==src_after
    result={'original_sha256':original,'source_metadata_unchanged':True,'exact_raw':summary,'constants':const,'high_precision_n100':[[str(x) for x in row] for row in hp],'max_relative_float_vs_mp_n100':err,'float':rows,'toll_diagnostics':diagnostics,'riemann':riemann()}
    (ROOT/'referee_results.json').write_text(json.dumps(result,indent=2)+'\n')
    log_event('Completed all calculations; n=100 float vs 60-digit raw max relative error '+str(err)+'. Original hash and src metadata unchanged.')

if __name__=='__main__': main()
