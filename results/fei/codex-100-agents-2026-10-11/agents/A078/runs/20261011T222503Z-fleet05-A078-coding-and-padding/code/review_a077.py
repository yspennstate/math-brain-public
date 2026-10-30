"""Independent direct Walsh reconstruction, exact symbolic log coefficients."""
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
def transform(t):
    # Direct character sums, independent of A077's compressed spectrum.
    n=len(t)
    return [F(sum(t[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(n)),n) for s in range(n)]
def add_log(dic,r,c):
    if not c:return
    for num,sgn in [(r.numerator,1),(r.denominator,-1)]:
        d=2
        while d*d<=num:
            e=0
            while num%d==0: num//=d;e+=1
            if e:dic[d]+=c*sgn*e
            d+=1
        if num>1:dic[num]+=c*sgn
def cleaned(x):return {k:v for k,v in x.items() if v}
def main():
    start=time.perf_counter();assertions=0;rows=[]
    for m in range(1,9):
        size=1<<m; t=[-1]+[1]*(size-1); a=transform(t)
        alpha=sum(a[s]**2 for s in range(size) if s&1)
        assert alpha==F(2,size);assertions+=1
        masses=[]; qs=[]
        for s in range(0,size,2):
            u,v=a[s]**2,a[s+1]**2
            masses.append(min(u,v));qs.append(u+v)
        M=sum(masses)
        if m==1:
            assert M==0;assertions+=1;continue
        d=F(1,1<<(m-1));q0=(1-d)**2+d*d
        assert M==d and masses==[d*d]*(size//2);assertions+=1
        assert qs==[q0]+[2*d*d]*(size//2-1);assertions+=1
        # Q/M expression as a rational linear combination of log2 primes.
        exact=defaultdict(F)
        for mi,qi in zip(masses,qs):add_log(exact,qi/mi,mi/M)
        formula=defaultdict(F);formula[2]+=1-d+2*d*(m-1);add_log(formula,q0,d)
        assert cleaned(exact)==cleaned(formula);assertions+=1
        # Nonreuse: direct edge disagreement agrees with alpha.
        edges=F(sum(t[x]!=t[x^1] for x in range(size)),size)
        assert alpha==edges;assertions+=1
        rows.append({'m':m,'M':str(M),'q0':str(q0),'Q_over_M_log_coefficients':{str(k):str(v) for k,v in cleaned(exact).items()}})
    for n in range(1,65):
        raw=sum(F(1,1<<(n-m))*F(1,1<<(m-1))*(m-1) for m in range(2,n+1))
        influence=sum(F(1,1<<(n-m))*F(2,1<<m) for m in range(1,n+1))
        assert raw==F(n*(n-1),1<<n);assertions+=1
        assert influence==F(2*n,1<<n);assertions+=1
    out={'reviewed_claim':'A077-MULTISCALE-MINORITY-KL-LEDGER','version':1,'verdict':'ACCEPT_AT_STATED_SCOPE','method':'Independent direct character sums and exact prime-log-vector identity; analytic all-n proof reconstructed in REVIEW_A077.md','assertions':assertions,'direct_walsh_dimensions':[1,8],'compressed_path_dimensions':[1,64],'rows':rows,'seconds':time.perf_counter()-start}
    (ROOT/'out'/'review_a077.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
