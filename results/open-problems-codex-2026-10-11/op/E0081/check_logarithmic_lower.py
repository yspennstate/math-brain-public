from pathlib import Path
from fractions import Fraction as F
from math import comb,log,sqrt
import json
import numpy as np
from check_patterns import words
from check_first_passage import fp,g,sums

ROOT=Path(__file__).resolve().parent
def pmf(l): return {2*j-l:F(comb(l,j),2**l) for j in range(l+1)}
def exact_moments(m):
    data={0:(F(1),F(0),F(0))}
    for l in range(1,m+1):
        nxt={}
        for s,(p,b,c) in data.items():
            for t in [s-1,s+1]:
                reward=g(l,-t)
                old=nxt.get(t,(F(0),F(0),F(0)))
                vals=(p/2,(b+reward*p)/2,(c+2*reward*b+reward*reward*p)/2)
                nxt[t]=tuple(x+y for x,y in zip(old,vals))
        data=nxt
    mean=sum(x[1] for x in data.values()); second=sum(x[2] for x in data.values())
    return mean,second-mean*mean

def main():
    smoothing=0; cov_checks=0; prefix_checks=0
    for r in range(1,65):
        masses=[F(comb(r,i),2**r) for i in range(r+1)]
        maximum=max(masses)
        assert maximum*maximum<=F(2,r+1)
        for d in range(1,9):
            tv=sum(abs((masses[i] if i<=r else 0)-(masses[i-d] if 0<=i-d<=r else 0)) for i in range(r+d+1))/2
            assert tv<=d*maximum
            if d==1: assert tv==maximum
            smoothing+=1
    for k in range(2,17):
        pk=pmf(k); muk=sum(p*g(k,-s) for s,p in pk.items())
        for j in range(1,k):
            pj=pmf(j); pr=pmf(k-j)
            muj=sum(p*g(j,-s) for s,p in pj.items())
            cross=sum(p*g(j,-s)*sum(q*g(k,-(s+t)) for t,q in pr.items()) for s,p in pj.items())
            cov=abs(cross-muj*muk)
            assert float(cov)<=2/(sqrt(j)*k**1.5)+1e-14 if j<=k/2 else cov<=F(2,j*k)
            cov_checks+=1
    for n in range(2,9):
        m=n//2
        for h in range(1,n+1):
            if (n-h)%2: continue
            A=[w for w in words(n) if fp(w,h)]
            p=F(len(A),2**n)
            for prefix in words(m):
                count=sum(w.startswith(prefix) for w in A)
                ratio=F(count*2**m,len(A))
                ss=sums(prefix); s=ss[-1]
                formula=g(n-m,h+s)/p if min([0]+ss)>-h else F(0)
                assert ratio==formula,(n,h,prefix,ratio,formula)
                assert ratio<=1/((n-m)*p)
                prefix_checks+=1
    exact=[]
    for m in [4,8,16,32,64]:
        mean,var=exact_moments(m)
        exact.append({'m':m,'mean_exact':str(mean),'variance_exact':str(var),
                      'mean_over_log_m':float(mean)/log(m),'variance_over_log_m':float(var)/log(m)})
    # Deterministic moment recursion, with mass itself giving P(S_l=s).
    p=np.array([1.]); b=np.array([0.]); c=np.array([0.]); numeric=[]
    for l in range(1,8193):
        pp=np.zeros(p.size+2); bb=np.zeros_like(pp); cc=np.zeros_like(pp)
        pp[:-2]+=p/2; pp[2:]+=p/2
        bb[:-2]+=b/2; bb[2:]+=b/2
        cc[:-2]+=c/2; cc[2:]+=c/2
        reward=np.maximum(-np.arange(-l,l+1),0)/l*pp
        cc+=2*reward*bb+reward*reward*pp
        bb+=reward*pp
        p,b,c=pp,bb,cc
        if l in [64,128,256,512,1024,2048,4096,8192]:
            mean=float(b.sum()); var=float(c.sum()-mean*mean)
            if l==64:
                assert abs(mean-float(exact[-1]['mean_exact'].split('/')[0])/float(exact[-1]['mean_exact'].split('/')[1]))<1e-12
            numeric.append({'m':l,'mean':mean,'variance':var,'mean_over_log_m':mean/log(l),'variance_over_log_m':var/log(l)})
    result={'all_assertions_passed':True,'smoothing_checks':smoothing,'covariance_checks':cov_checks,
            'prefix_likelihood_checks':prefix_checks,'exact_moments':exact,'numeric_moments':numeric}
    ROOT.joinpath('logarithmic_lower_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='exact_moments'},indent=2))

if __name__=='__main__': main()
