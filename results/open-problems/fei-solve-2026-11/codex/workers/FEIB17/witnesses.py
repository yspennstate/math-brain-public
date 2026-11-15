import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,math,json
from scipy.stats import binom
from audit import calc,h
from pathlib import Path
out={'majority_blocks':[],'constants':{}}
for n in [257,1025,4097]:
    delta=binom.pmf((n-1)//2,n-1,.5)
    for k in [1,4,16,64,128]:
        if k>=n:continue
        l=n-1-k;js=np.arange(l+1);ss=l-2*js;target=(k+ss)/2
        q=np.where(np.mod(k+ss,2)==0,binom.pmf(target,k,.5),0);eta=float(np.sum(binom.pmf(js,l,.5)*q*q))
        l2=n-k;j2=np.arange(l2+1);s2=l2-2*j2
        # sum of k signs = 2X-k. Negative total iff X<(k-s)/2.
        cutoff=np.ceil((k-s2)/2)-1;mean=1-2*binom.cdf(cutoff,k,.5);A=float(np.sum(binom.pmf(j2,l2,.5)*(1-mean*mean)))
        out['majority_blocks'].append(dict(n=n,k=k,delta=float(delta),A=A,eta=eta,A_over_delta=float(A/delta),A_over_sqrt_k_delta=float(A/(math.sqrt(k)*delta)),eta_over_delta=float(eta/delta),sqrt_k_eta_over_delta=float(math.sqrt(k)*eta/delta)))
out['constants']=dict(two_over_ln2=2/math.log(2),one_over_ln2=1/math.log(2),three_over_ln2=3/math.log(2),golden_pair_error=math.log2((3+math.sqrt(5))/2)+1/math.log(2),old_pair_error=math.log2(3)+1/math.log(2),first_level_G_constant=2/(math.e*math.log(2)),first_level_Hm_constant=(1+2/math.e)/math.log(2),quadratic_to_linear_constant=81/8)
# A symmetric Boolean spectrum can have comparable consecutive low levels.
from scipy.stats import binom
out['symmetric_adjacent_levels']=[]
for n in [256,1024,4096,16384]:
    t=n//2+round(.25*math.sqrt(n));mean=1-2*binom.sf(t-1,n,.5);alpha=binom.pmf(t-1,n-1,.5)
    out['symmetric_adjacent_levels'].append(dict(n=n,t=t,W0=float(mean*mean),W1=float(n*alpha*alpha),I=float(n*alpha),neighbor_ratio=float((mean/alpha)**2)))
# Check first-level G inequality and sharpened pair error independently on the n<=5 representative file.
from audit import truth,wht
codes=np.array([int(s,16) for s in open('../FEIB11/npn5.txt')],dtype=np.uint64);viol=0.;maxratio=0.
for start in range(0,len(codes),4096):
    f=truth(codes[start:start+4096],5);c=wht(f);mu=c*c;p=mu[:,0,None];q=mu[:,[1,2,4,8,16]];term=(q*np.log2(np.maximum(p+q,1e-300)/np.maximum(q,1e-300))).sum(1);term=np.where(np.isfinite(term),term,0.)
    I=(mu*np.array([j.bit_count() for j in range(32)])).sum(1);viol=max(viol,float((term-out['constants']['first_level_G_constant']*I).max()));maxratio=max(maxratio,float((term/np.maximum(I,1e-300)).max()))
out['first_level_census5']=dict(representatives=len(codes),max_violation=viol,max_G1_over_I=maxratio)
Path('witnesses.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
