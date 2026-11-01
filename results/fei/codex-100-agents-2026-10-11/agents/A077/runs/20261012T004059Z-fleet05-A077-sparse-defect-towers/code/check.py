from pathlib import Path
from fractions import Fraction as F
from math import comb,isqrt
from functools import lru_cache
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def ck(v):
    global COUNT
    COUNT+=1
    assert v,COUNT
def fwht(a):
    a=a[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return a
@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1);N=32
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    return lo,lo+2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
def log2(x):
    y=x;k=0
    while y<1:y*=2;k-=1
    while y>=2:y/=2;k+=1
    a,b=ln_unit(y);c,d=ln_unit(F(2));den=1<<120
    return F(((F(k)+a/d)*den).__floor__(),den),F(((F(k)+b/c)*den).__ceil__(),den)
def cbin(k):return comb(k,k//2)
def choose(k,t):return comb(k,t) if 0<=t<=k else 0
def binrow(k):
    row=[1]
    for i in range(k):row.append(row[-1]*(k-i)//(i+1))
    return row
def threshold_table(k,t):
    return [1 if t+2*x.bit_count()-k>0 else -1 for x in range(1<<k)]
def threshold_checks():
    cases=0
    for k in range(1,7):
        for t in range(-k-1,k+2,2):
            vals=threshold_table(k,t);w=fwht(vals);N=1<<k
            mu=F(w[0],N)
            infs=[F(sum(vals[x]!=vals[x^(1<<i)] for x in range(N)),N) for i in range(k)]
            ck(all(F(w[1<<i],N)==-infs[i] for i in range(k))) # binary Walsh reverses fair sign
            ck(max(abs(F(z,N)) for z in w[1:])==max(infs))
            ck(1-max(F(z,N)**2 for z in w)==1-max(mu*mu,max(a*a for a in infs)))
            ck(sum(z*z for z in w)==N*N)
            cases+=1
    return cases
def root(n):
    N=n-1;D=N//2;a=F(cbin(N),1<<N);I=n*a
    total_good=0;total_zero=0;states=0;good_states=0;minimum_kappa=F(1)
    rows=[]
    for d in range(D+1):
        m=n-d;k=m-1
        # Conditional pivotal bridge uses N balanced increments, d already revealed.
        good=zero=allmass=second=0
        child_rows=None
        if n>=511:
            br=binrow(k);cum=[0];v=0
            for q in br:v+=q;cum.append(v)
            child_rows=cum
        for h in range(d+1):
            s=2*h-d;weight=comb(d,h)*choose(N-d,N//2-h)
            allmass+=weight;second+=s*s*weight;states+=1
            if s==0:zero+=weight
            if s*s<=m:
                good+=weight;good_states+=1
                if n>=511:
                    kappas=[]
                    for t in [s-1,s+1]:
                        # Number of negative outcomes for sign(t+sum of k fair signs).
                        cut=(k-t)//2
                        negative=child_rows[min(k+1,max(0,cut+1))]
                        munum=(1<<k)-2*negative
                        infnum=choose(k-1,(k-1-t)//2)
                        ck(5*munum*munum<=4*(1<<k)**2)
                        ck(5*infnum*infnum<=4*(1<<(k-1))**2)
                        kap=1-max(F(munum,1<<k)**2,F(infnum,1<<(k-1))**2)
                        kappas.append(kap)
                    minimum_kappa=min(minimum_kappa,*kappas)
        ck(allmass==cbin(N)) # Vandermonde, hence E j = root a
        variance=F(d*(N-d),N-1)
        ck(F(second,allmass)==variance)
        ck(variance<=F(m,2))
        ck(2*good>=allmass)
        # The removed center-state probability is bounded by 2/sqrt(d+1).
        ck(zero*zero*(d+1)<=4*allmass*allmass)
        total_good+=good;total_zero+=zero
        rows.append({'depth':d,'remaining':m,'good_weighted_j':str(F(good,1<<N)),'zero_weighted_j':str(F(zero,1<<N)),'bridge_variance':str(variance)})
    mass=F(total_good,1<<N);removed=F(total_zero,1<<N);noniso=mass-removed
    ck(mass>=I/4)
    if n>=511:ck(minimum_kappa>=F(1,5))
    if n>=511:ck(noniso>=I/8)
    lower=None
    la,ua=log2(a)
    upper=(-ua*F(n-1,n),-la*F(n-1,n))
    if n>=511:
        # sqrt lower rounded down to an integer keeps the certificate rational.
        base=1+F(isqrt(3*n+1),20)
        l,u=log2(base)
        lower={'log_argument':str(base),'log_interval':[str(l),str(u)],'Lambda_over_I_lower':str(F(n+1,4*n)*l),'noniso_Lambda_over_I_lower':str(noniso/I*l)}
        ck(F(n+1,4*n)*l<=upper[1])
    return {'n':n,'I':str(I),'good_mass_over_I':str(mass/I),'removed_mass_over_I':str(removed/I),'noniso_good_mass_over_I':str(noniso/I),'minimum_good_child_kappa':str(minimum_kappa) if n>=511 else None,'state_count':states,'good_state_count':good_states,'certified_lower':lower,'Lambda_over_I_upper_interval':[str(x) for x in upper],'depth_rows':rows}
def main():
    start=time.perf_counter();mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
    ns=[3,5,9,17,33,65] if mode=='pilot' else [3,5,9,17,33,65,129,257,511,513,1025]
    cases=threshold_checks();results=[root(n) for n in ns]
    # Central-binomial upper/lower bounds and their elementary induction.
    for r in range(1,1026):
        c=F(comb(2*r,r),1<<(2*r));ck(c*c<=F(1,3*r+1));ck(c*c>=F(1,4*r))
        ck(F((2*r+1)**2,(2*r+2)**2)<=F(3*r+1,3*r+4))
        ck(F((2*r+1)**2,(2*r+2)**2)>=F(r,r+1))
    result={'helper_version':'A077-majority-bridge-v1','mode':mode,'assertions':COUNT,'root_cases':len(ns),'walsh_threshold_cases':cases,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer/Fraction, outward rational log intervals','rows':results}
    p=ROOT/'out'/f'{mode}.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}));print('saved',p,'sha256',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
