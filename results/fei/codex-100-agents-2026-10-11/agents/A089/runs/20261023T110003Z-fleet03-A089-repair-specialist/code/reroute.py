from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
def mean(v,w):return sum((a*b for a,b in zip(v,w)),F(0))
def solve(c,u,w):
    need=[max(F(0),b-a) for a,b in zip(c,u)];spare=[max(F(0),a-b) for a,b in zip(c,u)]
    N,P=mean(need,w),mean(spare,w)
    assert P>=N
    f=[n-N/P*s if P else F(0) for n,s in zip(need,spare)]
    return [a+b for a,b in zip(c,f)],f,N
def main():
    start=time.perf_counter();cases=checks=0;regimes={};receipts=[]
    def ck(b):
        nonlocal checks
        assert b;checks+=1
    for w in [(F(1,3),)*3,(F(1,2),F(1,3),F(1,6))]:
        for cc in product(range(3),repeat=3):
            for uu in product(range(3),repeat=3):
                c,u=list(map(F,cc)),list(map(F,uu));a=mean(c,w)
                if a<mean(u,w):continue
                x,f,N=solve(c,u,w);ck(all(v>=z for v,z in zip(x,u)));ck(mean(x,w)==a);ck(mean(f,w)==0);ck(mean([max(z,0) for z in f],w)==N)
                # A piecewise-linear minimum attains a vertex of one of the cells
                # cut out by x_i=u_i or x_i=c_i. Enumerate those vertices directly.
                opts=[]
                for free in range(3):
                    others=[i for i in range(3) if i!=free]
                    for bits in product((0,1),repeat=2):
                        z=[F(0)]*3
                        for i,bit in zip(others,bits):z[i]=c[i] if bit else u[i]
                        z[free]=(a-sum((w[i]*z[i] for i in others),F(0)))/w[free]
                        if all(v>=b for v,b in zip(z,u)):opts.append(mean([max(v-b,0) for v,b in zip(z,c)],w))
                ck(bool(opts));ck(min(opts)==N)
                if a:
                    for owner in (a/3,2*a/3):ck(mean([owner*v/a for v in x],w)==owner)
                else:ck(all(v==0 for v in x))
                ds=[v-b for v,b in zip(x,u)];T=mean(ds,w)
                kernel=[v/T for v in ds] if T else [F(1)]*3
                for label in (F(1),F(-2),T+1):ck(mean([label*k for k in kernel],w)==label)
                ck(all(sum((L*k for L in (F(1),F(-2),T+1)),F(0))==d for k,d in zip(kernel,ds)))
                cases+=1;regime='zero_total' if not T else 'positive_total';regimes[regime]=regimes.get(regime,0)+1
                receipts.append({'w':list(map(str,w)),'c':list(map(str,c)),'u':list(map(str,u)),'x':list(map(str,x)),'minimum_gross':str(N)})
    result={'candidate_cases':1458,'feasible_cases':cases,'checks':checks,'regimes':regimes,'runtime_seconds':time.perf_counter()-start,'cases':receipts}
    (ROOT/'out/REROUTE.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
if __name__=='__main__':main()
