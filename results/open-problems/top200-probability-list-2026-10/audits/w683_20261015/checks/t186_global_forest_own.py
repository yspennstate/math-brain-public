"""Independent exact labelled-parent enumeration and Arb criterion checks."""
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=512
N=5

def add(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,Fraction(0))+v
    return c

def mul(a,b):
    out={}
    for (n,e,r),v in a.items():
        for (nn,ee,rr),w in b.items():
            if n+nn<=N:
                key=(n+nn,e+ee,r+rr); out[key]=out.get(key,Fraction(0))+v*w
    return out

def egf(m):
    one={(0,0,0):Fraction(1)}; x={(1,0,0):Fraction(1)}; A={}
    for _ in range(N):
        children=add(x,A); power=one; new={}
        for j in range(m+1):
            for (n,e,r),v in power.items():
                if n+1<=N:
                    key=(n+1,e+j,r+1); new[key]=new.get(key,Fraction(0))+v/factorial(j)
            power=mul(power,children)
        A=new
    power=one; forest={}; wrong={}
    for j in range(N+1):
        forest=add(forest,{key:v/factorial(j) for key,v in power.items()})
        wrong=add(wrong,power)
        power=mul(power,A)
    return forest,wrong

def enumerate_parent_forests(m):
    out={(0,0,0):1}; cases=0
    for n in range(1,N+1):
        choices=[[-1]+[w for w in range(n) if w!=v] for v in range(n)]
        for parents in product(*choices):
            good=True
            for v in range(n):
                seen=set(); w=v
                while w!=-1:
                    if w in seen: good=False; break
                    seen.add(w); w=parents[w]
                if not good: break
            if not good: continue
            children=[parents.count(v) for v in range(n)]
            if max(children)>m: continue
            required={v for v in range(n) if parents[v]==-1 or children[v]>0}
            edges=sum(p!=-1 for p in parents)
            for mask in range(1<<n):
                if all(mask>>v&1 for v in required):
                    key=(n,edges,mask.bit_count()); out[key]=out.get(key,0)+1; cases+=1
    return out,cases

def ar(q):
    q=Fraction(q); return arb(q.numerator)/q.denominator

def criterion(k,c0,theta,tp,u,R,n0,prefactor):
    c0,theta,tp,u,R=map(Fraction,(c0,theta,tp,u,R)); delta=Fraction(1,10**6); m=k-1
    assert 0<theta<tp<1 and u>1-theta and R>0 and c0>=m/(1-tp)
    assert n0>=k/(tp-theta) and Fraction(k)/(1-tp)<prefactor
    c,t,tt,uu,rr=map(ar,(c0,theta,tp,u,R))
    y=c*(uu+rr); E=sum((y**j/factorial(j) for j in range(m+1)),arb(0))
    A=rr-uu*(-c*(1-tt)).exp()*E
    B=t*uu.log()+t+(1-t)*(1-t).log()-rr-ar(delta)
    assert A>0 and B>0
    margins=[]
    for v in (A,B):
        q=Fraction(str(v.lower().fmpq())); margins.append(str(q))
    expected=[4863729,221578] if k==4 else [6408567,9614657]
    assert all(Fraction(x)>=Fraction(v,10**12) for x,v in zip(margins,expected))
    return {'k':k,'precision':512,'n0':n0,'A_margin_lower':margins[0],'B_minus_delta_lower':margins[1],'prefactor':prefactor,'verdict':'PASS'}

def main():
    results=[]
    for k in (3,4):
        poly,wrong=egf(k-1); direct,cases=enumerate_parent_forests(k-1)
        assert set(poly)==set(direct)
        for (n,e,r),coeff in poly.items(): assert coeff*factorial(n)==direct[n,e,r]
        assert any(wrong.get(key,0)!=value for key,value in poly.items())
        results.append({'k':k,'coefficient_keys':len(direct),'coloured_parent_forests':cases,'degrees_checked':list(range(N+1)),'missing_component_factorial_rejected':True,'verdict':'PASS'})
    criteria=[criterion(4,'11.415','.1','.100001','1.223','.025305',4000000,5),criterion(3,'9.053','.125','.125001','1.315','.042379',3000000,4)]
    proof=Path('~/brain_workers/w674/T186/proofs/C014_C015_global_snapshot_forest.md')
    receipt={'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':sha256(proof.read_bytes()).hexdigest(),'arithmetic':'exact rational symbolic coefficients and 512-bit outward Arb elementary functions','criteria':criteria,'forest_checks':results}
    Path('checks/t186_global_forest_own.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt))
if __name__=='__main__': main()
