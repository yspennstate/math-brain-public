from pathlib import Path
from fractions import Fraction as F
from math import comb,isqrt,sqrt,pi,exp,log
import json
from check_patterns import solve, words, expected
from check_first_passage import fp,g,sums

ROOT=Path(__file__).resolve().parent
def first_hit_distribution(A):
    A=set(A); n=len(next(iter(A)))
    states=sorted({w[:i] for w in A for i in range(n)},key=lambda x:(len(x),x))
    index={w:i for i,w in enumerate(states)}
    matrix=[[F(int(i==j)) for j in range(len(states))] for i in range(len(states))]
    absorbing=[]
    for i,s in enumerate(states):
        for bit in '01':
            t=s+bit
            if len(t)>=n and t[-n:] in A:
                absorbing.append((i,t[-n:]))
            else:
                u=max((x for x in states if t.endswith(x)),key=len)
                matrix[index[u]][i]-=F(1,2)
    b=[F(int(i==index[''])) for i in range(len(states))]
    visits=solve(matrix,b)
    prob={w:F(0) for w in A}
    for i,w in absorbing: prob[w]+=visits[i]/2
    assert all(v>=0 for v in prob.values()) and sum(prob.values())==1
    return prob,sum(visits)

def root_path(n):
    a=[0]
    for l in range(1,n+1):
        r=isqrt(l); a.append(r if r%2==l%2 else r-1)
    assert all(abs(a[l]-a[l-1])==1 for l in range(1,n+1))
    return a

def main():
    rows=[]
    for n in range(1,9):
        for h in range(1,n+1):
            if (n-h)%2: continue
            A=[w for w in words(n) if fp(w,h)]
            dist,et=first_hit_distribution(A)
            p=F(len(A),2**n)
            values={w:1+sum((g(l,-sums(w)[l-1]) for l in range(1,n)),F(0)) for w in A}
            first_mean=sum(dist[w]*values[w] for w in A)
            uniform_mean=sum(values.values())/len(A)
            assert p*et==first_mean,(n,h,p,et,first_mean)
            assert all(prob<=first_mean/len(A) for prob in dist.values())
            assert et==expected(A)
            if h==1: assert first_mean==1 and et==1/p
            rows.append({'n':n,'h':h,'patterns':len(A),'ET':str(et),'p_ET':str(first_mean),
                         'uniform_C':str(uniform_mean),'maximum_C':str(max(values.values()))})
    root_rows=[]
    for h in [4,8,16,32,64,128]:
        n=h*h; a=root_path(n)
        assert a[-1]==h and max(a[:-1])<h
        # Exact binomial numerator / denominator, converted only for output sum.
        c=1+sum(float(g(l,a[l])) for l in range(1,n))
        root_rows.append({'n':n,'h':h,'C_root':c,'C_root_over_log_n':c/log(n)})
    result={'all_assertions_passed':True,'first_hit_distributions_checked':len(rows),
            'small_first_hit_results':rows,'root_path_results':root_rows,
            'root_asymptotic_coefficient':sqrt(2/pi)*exp(-.5)}
    ROOT.joinpath('first_hit_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='small_first_hit_results'},indent=2))

if __name__=='__main__':main()
