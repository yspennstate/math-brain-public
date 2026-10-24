"""Exact failure of the truncated normalized-resolvent positivity proposal."""
from fractions import Fraction as F
from itertools import product,permutations
from pathlib import Path
import json
from verify_shuffle_obstruction import log_bounds,scale,enclose_decimal

def det_jet(B,T=None):
    n=len(B)
    if T is None:T=[[F(0)]*n for _ in range(n)]
    out=[F(0)]*3
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        c=[F(1),F(0),F(0)]
        for i,j in enumerate(p):
            b=B[i][j];t=T[i][j]
            c=[c[0]*b,c[1]*b+c[0]*t,c[2]*b+c[1]*t]
        out=[a+sign*b for a,b in zip(out,c)]
    # Expansion used u=i*t. For symmetric B/skew T, c1=0 and u²=-t².
    assert out[1]==0
    return out[0],-out[2]

def main():
    Knum=[[313,-199,-36,25],[-199,531,-21,7],[-36,-21,560,-169],[25,7,-169,314]]
    K=[[F(x,1000) for x in row] for row in Knum]
    T=[[0,0,3,4],[0,0,-4,-7],[-3,4,0,0],[-4,7,0,0]]
    IK=[[F(i==j)-K[i][j] for j in range(4)] for i in range(4)]
    leading=[]
    for M in [K,IK]:
        vals=[det_jet([row[:m] for row in M[:m]])[0] for m in range(1,5)]
        assert all(v>0 for v in vals);leading.append(list(map(str,vals)))
    rows=[]
    for bits in product([0,1],repeat=4):
        B=[[K[i][j]-F(i==j)*(1-bits[i]) for j in range(4)] for i in range(4)]
        p,c=det_jet(B,T);sign=(-1)**(4-sum(bits));p*=sign;c*=sign
        q=F(1)
        for i,b in enumerate(bits):q*=K[i][i] if b else 1-K[i][i]
        assert p>0;rows.append((bits,p,c,q))
    assert sum(p for _,p,_,_ in rows)==1 and sum(c for _,_,c,_ in rows)==0
    for i in range(4):assert sum(c for b,_,c,_ in rows if b[i])==0
    cumul=[F(0),F(0)];full=[F(0),F(0)];s=F(1,10)
    for _,p,c,q in rows:
        for target,coefficient,arg in [(cumul,-2*c,1+s*q/p),(full,2*c,p)]:
            lo,hi=scale(coefficient,log_bounds(arg));target[0]+=lo;target[1]+=hi
    assert cumul[1]<-F(1,25)
    assert full[0]>1
    out=dict(status='PASS: cumulative shortcut false; full curvature remains positive',K_numerator=Knum,K_denominator=1000,T=T,leading_minors_K=leading[0],leading_minors_I_minus_K=leading[1],s='1/10',cumulative_interval=enclose_decimal(cumul),cumulative_upper_bound='-1/25',full_negative_entropy_curvature_interval=enclose_decimal(full),full_curvature_lower_bound='1',atom_data=[dict(bits=''.join(map(str,b)),p=str(p),t_squared_coefficient=str(c),product_reference=str(q)) for b,p,c,q in rows])
    Path('cumulative_obstruction_certificate.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='atom_data'},indent=2))

if __name__=='__main__':main()
