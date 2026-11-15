"""Independent Arb replay from the displayed C005/C007 equations, no solver imports."""
from pathlib import Path
from hashlib import sha256
from math import factorial
from fractions import Fraction
from time import monotonic
import json
import sys
from flint import arb, ctx

ROOT=Path(__file__).resolve().parent
SOLVER=Path('~/brain_workers/w674/T186/logs')
ctx.prec=512

def Q(j,x):
    term=arb(1); total=term
    for i in range(1,j):
        term=term*x/i; total+=term
    return 1-(-x).exp()*total

def P(j,x): return (-x).exp()*x**j/factorial(j)

def image(c,u,k):
    p,q,s=u; d=(-c*(1-s)).exp()
    a=d*Q(k,c*q); b=d*Q(k-1,c*q)
    return (a,b,b+(1-d)*Q(k-1,c*p))

def upper_step(lo,hi,u,k):
    c=lo.union(hi); p,q,s=u; a=1-s; d=(-c*a).exp()
    qk=Q(k,c*q); qj=Q(k-1,c*q); pj=Q(k-1,c*p)
    derivatives=(d*(q*P(k-1,c*q)-a*qk),
                 d*(q*P(k-2,c*q)-a*qj),
                 d*(q*P(k-2,c*q)-a*(qj-pj))+(1-d)*p*P(k-2,c*p))
    raw=image(c,u,k); ends={}
    result=[]
    for i,der in enumerate(derivatives):
        candidates=[u[i],raw[i].upper()]
        side=1 if der>=0 else 0 if der<=0 else None
        if side is not None:
            if side not in ends: ends[side]=image(hi if side else lo,u,k)
            candidates.append(ends[side][i].upper())
        result.append(min(candidates))
    result[1]=min(result[1],result[2]); result[0]=min(result[0],result[1])
    return result

def main():
    k=int(sys.argv[1]); budget=float(sys.argv[2]) if len(sys.argv)>2 else 100
    source=SOLVER/f't3_zero_JS_k{k}.json'; data=json.loads(source.read_text(encoding='utf-8'))
    scale=int(data['scale']); boxes=sorted(data['done'],key=lambda r:int(r['c_scaled'][0]))
    cutoff=Fraction(data['cutoff'])
    right=0
    for box in boxes:
        a,b=map(int,box['c_scaled']); assert a<=right and b>=a; right=max(right,b)
        u=list(map(int,box['upper_scaled']))
        assert b**(k-1)*u[1]**(k-2)<factorial(k-1)*scale**(2*k-3)
    assert Fraction(right,scale)==cutoff
    out=ROOT/f't186_c007_zero_k{k}_own.json'
    script_hash=sha256(Path(__file__).read_bytes()).hexdigest()
    if out.exists():
        receipt=json.loads(out.read_text(encoding='utf-8'))
        assert receipt['script_sha256']==script_hash
    else:
        receipt={'k':k,'precision':512,'input_sha256':sha256(source.read_bytes()).hexdigest(),'script_sha256':script_hash,'coverage_boxes':len(boxes),'checked':[]}
    assert receipt['input_sha256']==sha256(source.read_bytes()).hexdigest()
    start=monotonic()
    for index in range(len(receipt['checked']),len(boxes)):
        box=boxes[index]; aa,bb=map(int,box['c_scaled']); lo=arb(aa)/scale; hi=arb(bb)/scale
        u=[arb(1),arb(1),arb(1)]
        for iteration in range(1,int(box['iterations'])+102):
            u=upper_step(lo,hi,u,k)
            # Exact dyadic endpoint rational, then exact integer stopping test.
            q=u[1].fmpq(); bq=hi.upper().fmpq()
            if bq**(k-1)*q**(k-2)<factorial(k-1): break
        else: raise ArithmeticError(f'Unfinished box {index}, k={k}; no negative verdict implied')
        receipt['checked'].append({'index':index,'iterations':iteration,'q_upper':str(q),'c_upper':str(bq),'strict_stop':True})
        receipt['complete']=len(receipt['checked'])==len(boxes)
        out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
        if monotonic()-start>budget: break
    print(json.dumps({'k':k,'checked':len(receipt['checked']),'total':len(boxes),'complete':receipt['complete'],'seconds':monotonic()-start}))

if __name__=='__main__': main()
