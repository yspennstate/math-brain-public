from pathlib import Path
from fractions import Fraction as F
from math import comb, sqrt, log
import json
from check_patterns import words,expected,enlarged_density

ROOT=Path(__file__).resolve().parent
def sums(w):
    s=0; out=[]
    for x in w:
        s+=1 if x=='1' else -1
        out.append(s)
    return out
def fp(w,h):
    s=sums(w)
    return s[-1]==-h and min([0]+s[:-1])>-h
def g(l,a):
    if a<=0 or a>l or (l-a)%2: return F(0)
    return F(a*comb(l,(l-a)//2),l*2**l)
def main():
    checks=0; pair_checks=0; rows=[]
    for l in range(1,201):
        for a in range(1,l+1):
            if (l-a)%2==0:
                assert a*comb(l,(l-a)//2)<=2**l
                assert g(l,a)<=F(1,l)
    for n in range(1,10):
        W=words(n)
        H=sum((F(1,l) for l in range(1,n)),F(0))
        for h in range(1,n+1):
            if (n-h)%2: continue
            A=[w for w in W if fp(w,h)]
            assert len(A)==h*comb(n,(n-h)//2)//n
            p=F(len(A),2**n)
            overlap_total=F(0)
            max_overlap=F(0)
            for w in A:
                total=F(0); ss=sums(w)
                for l in range(1,n):
                    exact=F(sum(fp(w[l:]+u,h) for u in words(l)),2**l)
                    ballot=g(l,-ss[l-1])
                    assert exact==ballot,(n,h,w,l,exact,ballot)
                    total+=ballot; checks+=1
                    overlap_total+=(n-l)*ballot/len(A)
                assert total<=H
                max_overlap=max(max_overlap,total)
            q=enlarged_density(A)
            EN2=n*p+2*p*overlap_total
            assert EN2<=n*p*(1+2*H)
            assert q>=n*p/(1+2*H)
            row={'n':n,'h':h,'patterns':len(A),'p':str(p),'q':str(q),
                 'max_overlap_sum':str(max_overlap),'harmonic_bound':str(H)}
            if n<=7:
                et=expected(A)
                assert et<=F(2*n-1,n*p)*(1+2*H)
                row['ET']=str(et)
                row['ET_over_n']=float(et/n)
                pair_checks+=1
            rows.append(row)
    # Construct explicit near-square-root negative paths and test overlap growth.
    # An optimal full-path dynamic program is separate below.
    results={'all_assertions_passed':True,'conditional_overlap_cases':checks,
             'exact_mean_cases':pair_checks,'binomial_test_range':200,'small_cases':rows}
    ROOT.joinpath('first_passage_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in results.items() if k!='small_cases'},indent=2))

if __name__=='__main__': main()
