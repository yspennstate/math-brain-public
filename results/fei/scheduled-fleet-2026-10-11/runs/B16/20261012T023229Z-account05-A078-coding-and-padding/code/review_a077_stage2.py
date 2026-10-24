from pathlib import Path
from math import comb,isqrt
from fractions import Fraction as F
import time,json
ROOT=Path(__file__).resolve().parents[1];COUNT=0;START=time.perf_counter()
def ck(p):
    global COUNT
    COUNT+=1
    if time.perf_counter()-START>55:raise TimeoutError('frozen55-second review deadline')
    assert p
def main():
    child_cases=0
    for m in range(1,7):
        D=1<<m
        for t in range(1,m+1):
            tab=[1-2*(x.bit_count()>=t) for x in range(D)]
            # Direct character sums, independent from the source FWHT helper.
            w=[sum(tab[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(D)) for s in range(D)]
            inf=2*comb(m-1,t-1)
            ck(max(abs(x) for x in w[1:])==inf)
            child_cases+=1
    for r in range(1,257):
        c=F(comb(2*r,r),1<<(2*r))
        ck(c*c<=F(1,3*r+1));ck(c*c>=F(1,4*r))
        ck((2*r+1)**2*(3*r+4)<=(2*r+2)**2*(3*r+1))
        ck((2*r+1)**2*(r+1)>=(2*r+2)**2*r)
    rows=[]
    for n in [31,63,511]:
        N=n-1;root=comb(N,N//2);L=(n+1)//2
        goodsum=center_sum=0
        for d in range(L):
            m=n-d;good=total=second=center=0
            for j in range(d+1):
                s=d-2*j;h=(N-d+s)//2
                cnt=comb(d,j)*comb(N-d,h)
                total+=cnt;second+=cnt*s*s
                if s*s<=m:good+=cnt
                if s==0:center+=cnt
            ck(total==root)
            ck(second*(N-1)==root*d*(N-d))
            ck(2*second<=root*m)
            ck(2*good>=root)
            ck(center*center*(d+1)<=4*root*root)
            goodsum+=good;center_sum+=center
            if n>=511:
                # Worst allowed child shift, parity-adjusted below sqrt(m)+1.
                k=m-1;t=isqrt(m)+1
                if (k+t)%2==0:t-=1
                mu=sum(comb(k,j) for j in range(k+1) if abs(k-2*j)<t)
                ck(5*mu*mu<=4*(1<<(2*k)))
                # Empty and nonempty squared max both <=4/5.
                ck(5*comb(k-1,(k-1)//2)**2<=4*(1<<(2*(k-1))))
        ck(2*goodsum>=L*root)
        if n>=511:ck(4*(goodsum-center_sum)>=L*root)
        rows.append({'n':n,'first_half_levels':L,'good_bridge_mass_over_root':str(F(goodsum,root)),'center_bridge_mass_over_root':str(F(center_sum,root)),'noniso_good_lower_over_root':str(F(goodsum-center_sum,root))})
    out={'status':'PASS','reviewed_claim':'A077-MAJORITY-SCALAR-LAMBDA-DIVERGENCE','version':1,'verdict':'ACCEPT_AT_STATED_SCOPE','child_tables':child_cases,'assertions':COUNT,'rows':rows,'seconds':time.perf_counter()-START,'arithmetic':'direct integer Walsh, combinatorial bridge counts, rational squared inequalities; analytic proof supplies logarithmic divergence'}
    (ROOT/'out'/'review_a077_stage2.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
