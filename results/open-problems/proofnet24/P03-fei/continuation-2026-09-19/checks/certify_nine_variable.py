"""Direct rational-interval certificate: every actual shift and admissible quotient.
Run with Python 3.10+; standard library only. No sampling or floating acceptance.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
from exact_drift_certificate import IV, fwht, psi, row_potential, log2_iv, show

def entropy(w):
    N=len(w)
    counts=Counter(a*a for a in w if a)
    return sum((-c*F(a,N*N)*log2_iv(F(a,N*N)) for a,c in counts.items()),IV.point(0))

def physical(f):
    N=len(f); n=N.bit_length()-1
    inf=[F(sum(f[x]!=f[x^(1<<i)] for x in range(N)),N) for i in range(n)]
    j=[min(a,1-a) for a in inf]
    t=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for k in range(i):
            t[i][k]=t[k][i]=F(sum(f[x]*f[x^(1<<i)]*f[x^(1<<k)]*f[x^(1<<i)^(1<<k)]<0 for x in range(N)),4*N)
    return j,t

def main():
    n=9; N=1<<n
    f=tuple((-1)**((x&1)*(((x>>1).bit_count()*((x>>1).bit_count()-1)//2)&1)) for x in range(N))
    w=fwht(f); H=entropy(w); j,t=physical(f); P,L,_=row_potential(j,t)
    EH=IV.point(0); EQP=IV.point(0);EQL=IV.point(0)
    E_best=IV.point(0);quotients=0
    for z in range(N):
        g=tuple(f[x]*f[x^z] for x in range(N));wg=fwht(g)
        EH+=entropy(wg);jj,tt=physical(g);pg,lg,_=row_potential(jj,tt)
        gains=[]
        for i in range(n):
            if not z&(1<<i):continue
            quotients+=1
            q=tuple(y for x,y in enumerate(g) if not x&(1<<i));wq=fwht(q)
            assert Counter(F(a*a,N*N) for a in wg if a)==Counter(F(a*a,(N//2)**2) for a in wq if a)
            jq,tq=physical(q);rem=[k for k in range(n) if k!=i]
            assert jq==[jj[k] for k in rem]
            assert tq==[[tt[k][l] for l in rem] for k in rem]
            pq,lq,_=row_potential(jq,tq)
            gains.append(4*(pg-pq)+2*(lg-lq))
        best=IV(max((a.lo for a in gains),default=F(0)),max((a.hi for a in gains),default=F(0)))
        E_best+=best; EQP+=pg;EQL+=lg
    D=2*H-EH/N
    best_rhs=4*(2*P-EQP/N)+2*(2*L-EQL/N)+E_best/N
    residual=D-best_rhs
    assert residual.lo>F(174606321217,10**12)
    assert residual.hi<F(174606321220,10**12)
    result={'status':'PASS','full_FEI_proved':False,'claim':'D_cross > 4 Delta_Q P + 2 Delta_Q L for every admissible single-coordinate quotient rule',
            'variables':n,'shifts_checked':N,'admissible_quotients_checked':quotients,
            'H_bits':show(H),'J':str(sum(j)),'D_cross':show(D),'best_possible_rhs':show(best_rhs),
            'positive_residual':show(residual),'acceptance':'exact rational interval arithmetic; displayed decimals are not used for acceptance'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
