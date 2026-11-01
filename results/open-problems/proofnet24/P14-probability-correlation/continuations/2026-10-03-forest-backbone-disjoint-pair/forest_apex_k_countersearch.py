"""Independent exact countersearch: unrooted forest plus one common-profile apex.

The partition DP keeps original labels and exact integer weights.  Cubic
root diagnosis is exact discriminant; higher degrees use rational Sturm plus
polynomial gcd, so multiple real roots never count as nonreal failures.
"""
from collections import defaultdict
from fractions import Fraction as F
from random import Random
from pathlib import Path
from math import gcd
import json
import numpy as np

OUT=Path(__file__).with_name('forest_apex_k_countersearch_results.json')

def merge(p,u,v):
    a,b=p[u],p[v]
    if a==b:return None
    return tuple(a if t==b else t for t in p)

def coefficients(n,edges,beta):
    state={tuple(range(n)):1}
    for u,v,w in edges:
        out=defaultdict(int)
        for p,z in state.items():
            out[p]+=z
            q=merge(p,u,v)
            if q is not None:out[q]+=w*z
        state=out
    ans=[0]*(sum(bool(x) for x in beta)+1)
    for p,z in state.items():
        sizes=defaultdict(int)
        for i,b in enumerate(beta):sizes[p[i]]+=b
        poly=[1]
        for b in sizes.values():
            if not b:continue
            new=[0]*(len(poly)+1)
            for k,x in enumerate(poly):new[k]+=x;new[k+1]+=b*x
            poly=new
        for k,x in enumerate(poly):ans[k]+=z*x
    while len(ans)>1 and ans[-1]==0:ans.pop()
    return ans

def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p

def rem(a,b):
    a=list(map(F,a));b=list(map(F,b))
    while len(a)>=len(b) and any(a):
        fac=a[-1]/b[-1];d=len(a)-len(b)
        for k,v in enumerate(b):a[k+d]-=fac*v
        trim(a)
    return a

def positive_primitive(p):
    den=1
    for v in p:den=den*v.denominator//gcd(den,v.denominator)
    ints=[v.numerator*(den//v.denominator) for v in p]
    g=0
    for x in ints:g=gcd(g,abs(x))
    return [F(x//g)for x in ints] if g else [F(0)]

def real_roots_with_multiplicity(poly):
    p=list(map(F,poly));total=0
    while len(p)>1:
        seq=[p,[i*p[i]for i in range(1,len(p))]]
        while len(seq[-1])>1:
            q=positive_primitive([-v for v in rem(seq[-2],seq[-1])])
            if not any(q):break
            seq.append(q)
        signpos=[1 if row[-1]>0 else -1 for row in seq]
        signneg=[v*(-1 if (len(row)-1)%2 else 1)for row,v in zip(seq,signpos)]
        changes=lambda sig:sum(x!=y for x,y in zip(sig,sig[1:]))
        total+=changes(signneg)-changes(signpos)
        # Last nonzero Euclidean remainder is gcd; repeat on it to count
        # repeated roots with their full multiplicity.
        last=seq[-1]
        if len(last)==1:break
        if any(rem(seq[-2],last)):raise AssertionError('not gcd')
        p=last
    return total

def diagnostic(c):
    d=len(c)-1
    if d==3:
        e,cc,b,a=c
        discr=b*b*cc*cc-4*a*cc**3-4*b**3*e-27*a*a*e*e+18*a*b*cc*e
        return (d if discr>=0 else 1),{'cubic_discriminant':str(discr)}
    roots=np.roots(np.array(c[::-1],dtype=float))
    imag=max(abs(x.imag)for x in roots) if roots.size else 0
    # Exact certification for every degree <=6 and every floating alert.
    if d<=6 or imag>1e-7*max(1,max(abs(x.real)for x in roots)):
        count=real_roots_with_multiplicity(c)
        return count,{'exact_real_roots_counting_multiplicity':count,'float_max_imag':imag}
    return d,{'floating_screen_only':True}

def main():
    rng=Random(61003223)
    report={'status':'EXPLORATION; finite search is not proof','cases':0,'counts':{},'nonreal_counterexample':None,'floating_false_alerts':0,'minimum_cubic_discriminant_normalized':None}
    for n in range(3,11):
        trials=400 if n<=7 else 80 if n==8 else 25
        for trial in range(trials):
            prob=[.22,.4,.6,.85][trial%4]
            edges=[(i,j,rng.choice([1,1,2,3,5,10,30,100,1000])) for i in range(n)for j in range(i+1,n)if rng.random()<prob]
            if len(edges)>20 and n>=8:
                rng.shuffle(edges);edges=edges[:20]
            k=rng.choice([3,3,3,4,min(5,n),n]);k=min(k,n)
            ports=rng.sample(range(n),k)
            beta=[0]*n
            for i in ports:beta[i]=1 if trial%3 else rng.choice([1,2,3,10,100])
            c=coefficients(n,edges,beta)
            count,diag=diagnostic(c);degree=len(c)-1
            report['cases']+=1;report['counts'][str(n)]=report['counts'].get(str(n),0)+1
            if 'float_max_imag' in diag and diag['float_max_imag']>1e-5 and count==degree:report['floating_false_alerts']+=1
            if count<degree:
                report['status']='EXACT NONREAL COUNTEREXAMPLE'
                report['nonreal_counterexample']={'n':n,'edges':edges,'profile':beta,'coefficients_ascending':list(map(str,c)),'degree':degree,**diag}
                OUT.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True);return
            if trial%100==0:OUT.write_text(json.dumps(report,indent=2)+'\n')
        print('completed',n,trials,flush=True);OUT.write_text(json.dumps(report,indent=2)+'\n')
    print('No exact counterexample in',report['cases'],'cases.',flush=True)

if __name__=='__main__':main()
