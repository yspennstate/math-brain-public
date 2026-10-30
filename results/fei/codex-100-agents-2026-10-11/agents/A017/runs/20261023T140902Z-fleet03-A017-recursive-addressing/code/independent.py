"""Direct-character witness audit, unreduced logarithms; no inherited Walsh helper."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json
R=Path(__file__).resolve().parents[1]; O=R/'out'
def entropy(t):
    N=len(t); out={2:F(2*(N.bit_length()-1))}
    for mask in range(N):
        v=abs(sum(a*(-1 if (x&mask).bit_count()%2 else 1) for x,a in enumerate(t)))
        if not v:continue
        z=v; q=2
        while q<=z:
            k=0
            while z%q==0:z//=q;k+=1
            if k:out[q]=out.get(q,F(0))-F(2*v*v*k,N*N)
            q+=1
    return {q:c for q,c in out.items() if c}
@lru_cache(None)
def ln(q):
    x=F(q-1,q+1); term=x; lo=F(0)
    for k in range(256):lo+=2*term/(2*k+1);term*=x*x
    return lo,lo+2*term/(513*(1-x*x))
def floor40(q):return str(F((q*(1<<40)).numerator//(q*(1<<40)).denominator,1<<40))
def main():
    z=json.loads((O/'certificate.json').read_text(encoding='utf-8')); w=z['best']; f=w['truth_table']; a,b=w['full_children']
    assert a==f[::2] and b==f[1::2]
    d=entropy(f)
    for child in (a,b):
        for q,c in entropy(child).items():d[q]=d.get(q,F(0))-c/2
    d={q:c for q,c in d.items() if c}
    assert {str(q):str(c) for q,c in d.items()}==w['delta']
    p=F(sum(x!=y for x,y in zip(a,b)),32); assert p==F(1,8)
    expr=dict(d);expr[2]=expr.get(2,F(0))-4*p
    lo=sum((v*ln(q)[0 if v>=0 else 1] for q,v in expr.items()),F(0))-2*p
    hi=sum((v*ln(q)[1 if v>=0 else 0] for q,v in expr.items()),F(0))-2*p
    assert (lo>0)==(w['verdict']=='EXCEEDS_SAME_K')
    if w['verdict']=='PAID_SAME_K':assert hi<0
    result=dict(status='PASS',method='Direct integer character sums for root and BOTH full children;256-term unreduced rational atanh with geometric error',
      actual_original_influence=str(p),delta={str(q):str(c) for q,c in d.items()},verdict=w['verdict'],
      natural_gap_lower_dyadic=floor40(lo),natural_gap_upper_dyadic=str(F((hi*(1<<40)).numerator//(hi*(1<<40)).denominator+1,1<<40)),
      independent_review=False)
    (O/'witness_certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
