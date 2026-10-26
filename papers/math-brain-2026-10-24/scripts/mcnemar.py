"""Recompute Appendix F: exact p values, Holm decisions and planning power.

Counts transcribed from the paper's dated aggregate reports. This does not
regrade unavailable private per-item data. Uses only Python's standard library.
Run with --power to include the slower power and minimum-effect calculations.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, exp, fsum, lgamma, log
import json
import sys

COMPARISONS = [
    ('store100_full_vs_search',10,3), ('store100_full_vs_recall',2,3),
    ('recall1000',462,0), ('solve61',15,4), ('solve54',12,3),
    ('solve_named26',10,1), ('solve_unnamed35',5,3), ('solve61_vs_recall',10,4),
    ('repo80',9,4), ('rank584',27,8), ('rank1070',143,16),
    ('open13_preference',3,8), ('nextcard60',0,3), ('printout60',2,2),
    ('claude988_brain_vs_repo',146,13), ('claude806_both_in_time',3,4),
    ('claude988_brain_vs_model',757,1), ('codex335_brain_vs_repo',6,14),
    ('codex335_brain_vs_model',238,0), ('early300',14,40), ('early110',6,8),
]

def p(b,c):
    d=b+c
    return min(Fraction(1),Fraction(2*sum(comb(d,i) for i in range(min(b,c)+1)),2**d))

@lru_cache(None)
def critical(d):
    total=0
    last=-1
    for k in range(d//2+1):
        total+=comb(d,k)
        if 40*total < 2**d: last=k
        else: break
    return last

def holm(rows):
    ordered=sorted((p(b,c),name) for name,b,c in rows)
    rejected=[]
    for rank,(value,name) in enumerate(ordered):
        if value <= Fraction(1,20*(len(rows)-rank)): rejected.append(name)
        else:break
    return rejected

@lru_cache(None)
def logcombs(n):
    return tuple(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1) for k in range(n+1))

def mass(n,k,q):
    if q==0:return float(k==0)
    if q==1:return float(k==n)
    return exp(logcombs(n)[k]+k*log(q)+(n-k)*log(1-q))

def power(n,psi,theta):
    values=[]
    for d in range(6,n+1):
        w=mass(n,d,psi)
        if w<1e-15:continue
        k=critical(d)
        if k<0:continue
        tail=fsum(mass(d,b,theta)+mass(d,b,1-theta) for b in range(k+1))
        values.append(w*tail)
    return fsum(values)

def main():
    rows=[]
    for name,b,c in COMPARISONS:
        value=p(b,c);k=critical(b+c)
        rows.append({'comparison':name,'wins':b,'losses':c,'p':float(value),
                     'exact_p':str(value),'smallest_significant_split':None if k<0 else [b+c-k,k]})
    result={'comparisons':rows,'holm_all21':holm(COMPARISONS),
            'holm_current19':holm(COMPARISONS[:-2]),
            'exploratory_codex_lookup_p':float(p(4,14))}
    if '--power' in sys.argv:
        grid=[]
        for n in (26,61,100,584,1000):
            for psi in (0.1,0.2,0.3):
                vals={str(t):round(power(n,psi,t),4) for t in (0.6,0.7,0.8,0.9)}
                if power(n,psi,1)<0.8:minimum=None
                else:
                    lo,hi=0.5,1.0
                    for _ in range(18):
                        mid=(lo+hi)/2
                        if power(n,psi,mid)>=0.8:hi=mid
                        else:lo=mid
                    minimum={'theta':round(hi,6),'expected_net_gain':round(n*psi*(2*hi-1),4)}
                grid.append({'n':n,'psi':psi,'power':vals,'minimum_for_power_0_8':minimum})
        result['power_grid']=grid
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
