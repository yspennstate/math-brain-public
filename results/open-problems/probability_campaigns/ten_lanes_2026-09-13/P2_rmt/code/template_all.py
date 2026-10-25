"""All six disjoint-quadruple template types, exact probabilities per configuration."""
import itertools
from fractions import Fraction
def run(n):
    idx=[(a,b) for a in range(n) for b in range(a,n)]
    nf=len(idx); tot=1<<nf
    i,j,k,l=0,1,2,3
    res={}
    for s1 in (+1,-1):
        for s2 in (+1,-1):
            for rel in ('zero','equal'):
                c=cnz=0
                for bits in range(tot):
                    M=[[0]*n for _ in range(n)]
                    for t,(a,b) in enumerate(idx):
                        v=1 if not (bits>>t)&1 else -1
                        M[a][b]=v; M[b][a]=v
                    # e_i + s1 e_j eigenvector: M[m][i] = -s1*M[m][j] for m outside; M[i][i]=M[j][j]
                    ok = all(M[m][i]==-s1*M[m][j] for m in range(n) if m not in (i,j)) and M[i][i]==M[j][j] \
                     and all(M[m][k]==-s2*M[m][l] for m in range(n) if m not in (k,l)) and M[k][k]==M[l][l]
                    if not ok: continue
                    mu = M[i][i]+s1*M[i][j]
                    nu = M[k][k]+s2*M[k][l]
                    hit = (mu+nu==0) if rel=='zero' else (mu==nu)
                    if hit:
                        c+=1
                        if (mu!=0 if rel=='zero' else True) and not (rel=='equal' and mu==0): cnz+=1
                res[(s1,s2,rel)]=(Fraction(c*4**n,tot), Fraction(cnz*4**n,tot))
    return res
for n in [5,6]:
    print(f"--- n={n}   (values are P * 4^n per fixed ordered quadruple (i,j,k,l)=(0,1,2,3))")
    r=run(n)
    for key,(a,b) in sorted(r.items(), key=str):
        s1,s2,rel = key
        t1 = '+' if s1>0 else '-'; t2 = '+' if s2>0 else '-'
        print(f"   e_i{t1}e_j , e_k{t2}e_l   relation={rel:5s}   P*4^n = {a}   (nonzero-eigenvalue part {b})")
