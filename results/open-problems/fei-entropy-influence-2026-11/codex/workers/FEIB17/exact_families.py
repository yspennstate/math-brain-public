import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import math,json
from fractions import Fraction
from audit import h,calc,truth,wht,tree,entropy,info
import numpy as np
from pathlib import Path

def erasure_ratio(m):
    s=2**(m//2);N=2**m;np=(N+s)//2;nm=(N-s)//2
    rr=[(s-1)**2,(s+1)**2]
    val=sum(k*(1+r)*float(h(1/(1+r))) for k,r in zip([np,nm],rr))/N
    # J/delta, using b/a=1/sqrt(r), weighted by (1+r).
    jj=sum(k*(1+r)*(1-float(h((1+2*math.sqrt(r)/(1+r))/2))) for k,r in zip([np,nm],rr))/N
    return val,jj,np,nm,rr
out={};rows=[]
for m in [2,4,6,8,12,16,20]:
    delta=Fraction(1,2**m);alpha=Fraction(1,2)+delta;r=1
    if m<=6:
        while True:
            cr=Fraction(math.comb(r-1,(r-1)//2),2**(r-1))
            if alpha*cr<delta:break
            r+=2
        prev=Fraction(math.comb(r-3,(r-3)//2),2**(r-3)) if r>=3 else None
        dims=m*r+1
    else:cr=prev=None;dims=r=None
    e,j,np_,nm,ratios=erasure_ratio(m)
    rows.append(dict(m=m,r=r,n=dims,delta=str(delta),base_block_influence=str(alpha),majority_single=str(cr),composed_block_influence=str(alpha*cr) if cr else None,previous_block_influence=str(alpha*prev) if prev else None,E_over_delta=e,J_over_delta=j,D_over_delta=e+j,Nplus=np_,Nminus=nm,ratios=ratios))
out['bent_majorities']=rows
other=[]
for m in [2,4,6]:
    d=Fraction(1,2**m);a=Fraction(1,2)-d;r=1
    while a*Fraction(math.comb(r-1,(r-1)//2),2**(r-1))>=d:r+=2
    other.append(dict(m=m,point='all-one bits, every replaced edge pivotal',outer_influence=str(a),least_odd_r=r))
out['bent_alternative_point']=other
# Direct base functions confirm formula, and outer coordinate influences.
out['bent_base_direct']=[]
for m in [2,4,6]:
    ids=np.arange(1<<m);ip=np.zeros(1<<m,dtype=int)
    for j in range(0,m,2):ip^=((ids>>j)&1)*((ids>>(j+1))&1)
    base=1-2*ip;f=np.r_[base,base].astype(float);f[0]=1;f[1<<m]=-1;o=calc(f[None,:])
    out['bent_base_direct'].append(dict(m=m,Inf=o['Inf'][0].tolist(),E_over_delta=float(o['E'][0,m]/o['Inf'][0,m]),J_over_delta=float(o['J'][0,m]/o['Inf'][0,m])))
# AND exact arbitrary dimension and failure of CI^2.
out['and']=[]
for n in [2,4,8,16,32,64,128]:
    # mu0=(1-2^(1-n))^2, every nonempty mass q=4^(1-n).
    d=2.**(1-n);q=d*d;mu0=(1-d)**2;ei=(mu0+q)*float(h(q/(mu0+q)))+(2.**(n-1)-1)*2*q
    I=n*d;out['and'].append(dict(n=n,I=I,Hm=n*ei,Hm_over_I=ei/d,Hm_over_I2=ei/(n*d*d)))
# Greedy largest-influence tree's marginal-entropy proxy on balanced tribes.
out['tribes_greedy_proxy']=[]
for w in range(2,13):
    s=round(math.log(2)*2**w);q=1-2**(-w);prev=0.;previ=0.
    for t in range(1,s+1):
        val=0.;ival=0.
        for l in range(1,w+1):
            delta=2**(-(l-1))*q**(t-1)
            val=float(h(delta))+.5*val+.5*prev
            ival=delta+.5*ival+.5*previ
        prev=val;previ=ival
    I=s*w*2**(-(w-1))*q**(s-1)
    out['tribes_greedy_proxy'].append(dict(w=w,s=s,I=I,proxy=prev,proxy_over_I=prev/I,tree_influence_residual=abs(I-previ)))
# Complex product: exact product-law statistics.
out['complex']=[]
for n,p in [(8,.01),(64,.001),(1024,1e-6)]:
    I=n*p;H=n*float(h(p));G=n*p*math.log2(1/p)
    out['complex'].append(dict(n=n,p=p,I=I,H=H,Hm=H,G=G,H_over_I=H/I,modulus_error=abs(abs(complex(math.sqrt(1-p),math.sqrt(p)))-1)))
Path('exact_families.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
