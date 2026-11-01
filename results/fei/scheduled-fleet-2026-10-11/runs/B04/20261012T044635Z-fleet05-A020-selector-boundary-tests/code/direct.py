"""Direct character sums and Fraction logs; no NumPy/butterflies."""
import json,math
from pathlib import Path
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[1]
def log_interval(k):
    e=k.bit_length()-1;r=Q(k,1<<e)
    def s(z):
        p=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(60)),Q(0))
        return p,p+2*z**121/(121*(1-z*z))
    l,h=s((r-1)/(r+1));a,b=s(Q(1,3));return l+e*a,h+e*b
def factor(n):
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def transform(v):return [sum((a*(-1)**((x&t).bit_count()) for x,a in enumerate(v)),Q(0)) for t in range(len(v))]
def entropy_expr(w):
    den=len(w)**2;d={p:Q(e) for p,e in factor(den).items()}
    for c in w:
        assert c.denominator==1
        c=int(c);mass=Q(c*c,den)
        if c:
            for p,e in factor(c*c).items():d[p]=d.get(p,Q(0))-mass*e
    return {p:e for p,e in d.items() if e}
def eval_expr(d):
    lo=hi=Q(0)
    for p,e in d.items():
        l,h=log_interval(p);lo+=e*(l if e>0 else h);hi+=e*(h if e>0 else l)
    return lo,hi
def record(mask,i):
    v=[Q(1-2*((mask>>x)&1)) for x in range(32)];w=transform(v)
    def inject(y):return (y&((1<<i)-1))|((y>>i)<<(i+1))
    g=[v[inject(y)] for y in range(16)];h=[v[inject(y)|(1<<i)] for y in range(16)]
    wg=transform(g);wh=transform(h);D=[(a-b)/2 for a,b in zip(g,h)];wd=transform(D)
    d=sum(a!=b for a,b in zip(g,h))/Q(16)
    energy=sum((wd[t]**2*t.bit_count()/256 for t in range(16)),Q(0))
    physical=sum(((D[y]-D[y^(1<<j)])**2/64 for y in range(16) for j in range(4)),Q(0))
    assert energy==physical
    expr=entropy_expr(w)
    for ww in [wg,wh]:
        for p,e in entropy_expr(ww).items():expr[p]=expr.get(p,Q(0))-e/2
    expr={p:e for p,e in expr.items() if e}
    l,hh=eval_expr(expr);a,b=log_interval(2);blo=3*d+2*energy*a;bhi=3*d+2*energy*b
    ratio=(l/bhi,hh/blo);assert ratio[0]>Q(81,100)
    if mask==474167 and i==0:
        assert expr=={2:Q(-1),3:Q(9,8)}
        assert ratio[0]>Q(17,20)
        # Exact conditional erasure: eight fibers, masses 4/64 and 1/64.
        berasure={5:Q(5,8),2:Q(-1)}
        el,eh=eval_expr(berasure);assert eh<4*d*log_interval(2)[0]
        erasure_record=dict(prime_log_expression_nats={str(p):str(e) for p,e in berasure.items()},ratio_to_influence_formula='5*log2(5)-8',bad_at_K4=False)
    else:erasure_record=None
    result=dict(mask=mask,coordinate=i,negative_inputs=[x for x in range(32) if mask>>x&1],parent_walsh=[int(c) for c in w],branch_masks=[sum((a==-1)<<y for y,a in enumerate(branch)) for branch in [g,h]],branch_walsh=[[int(c) for c in ww] for ww in [wg,wh]],derivative_support={str(y):int(D[y]) for y in range(16) if D[y]},influence=str(d),derivative_energy=str(energy),delta_nats_prime_log_expression={str(p):str(e) for p,e in expr.items()},ratio_interval=[str(q) for q in ratio],ratio_float=float((ratio[0]+ratio[1])/2),margin_against_81_nats_interval=[str(l-Q(81,100)*bhi),str(hh-Q(81,100)*blo)])
    result['exact_erasure']=erasure_record
    return result
if __name__=='__main__':
    masks=[(775,1),(474167,0)]
    if (ROOT/'out'/'census.json').exists():
        r=json.loads((ROOT/'out'/'census.json').read_text())['best_boundary'];masks.append((r['mask'],r['coordinate']))
    out=[record(m,i) for m,i in sorted(set(masks))]
    (ROOT/'out'/'direct_certificates.json').write_text(json.dumps(out,indent=2))
    print(json.dumps([{k:r[k] for k in ['mask','coordinate','branch_masks','derivative_support','influence','derivative_energy','delta_nats_prime_log_expression','ratio_float']} for r in out],indent=2))
