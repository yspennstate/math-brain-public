"""160-decimal-digit AND calculations: counts can differ from 1 by 2^-n."""
import math
import mpmath as mp
from experiment import KS,TS,TH
def and_row(n):
    with mp.workdps(160):
        q=mp.mpf(2)**-n;mu0=(1-2*q)**2;I=2*n*q;V=4*q*(1-q)
        mu=[mu0]+[4*q*q]*n;up=[mp.mpf(1)]+[4*q*mp.mpf(2)**-s for s in range(1,n+1)]
        p=[mp.mpf(1)]+[mp.mpf(2)**(s-n) for s in range(1,n+1)]
        C=[mp.mpf(math.comb(n,s)) for s in range(n+1)]
        def lg(a):return mp.log(a,2)
        def cost(pi):return sum(C[s]*mu[s]*-lg(pi[s]) for s in range(n+1))
        row={'name':f'AND_{n}','n':n,'I':I,'Var':V,'P':cost(p),'A':cost(up),'H':cost(mu),'precision_decimal_digits':160}
        for K in KS:row[f'Sp{K}']=sum(C[s]*mu[s]*(n-s) for s in range(1,n+1) if n-s>K*s)
        def noise(t):
            t=mp.mpf(t)
            return [1-4*q+4*q*q*(2-t)**n]+[4*q*q*t**s*(2-t)**(n-s) for s in range(1,n+1)]
        for t in TS:
            tau=noise(t);row[f'T{t:g}']=sum(C[s]*tau[s]*-lg(p[s]) for s in range(n+1))
            for theta in TH:
                th=mp.mpf(str(theta));row[f'taumom_t{t:g}_th{theta:g}']=lg(sum(C[s]*tau[s]*p[s]**-th for s in range(n+1)))
        for theta in TH:
            th=mp.mpf(str(theta))
            row[f'raw_th{theta:g}']=lg(sum(C[s]*mp.mpf('.5')**s*up[s]*p[s]**-th for s in range(n+1)))
            for a in (2,4):
                M=min(n,int(mp.ceil(a*I)))
                trunc=[sum(math.comb(n-s,k-s)*mu[k] for k in range(s,M+1)) for s in range(n+1)]
                row[f'raw_M{a}I_th{theta:g}']=lg(sum(C[s]*mp.mpf('.5')**s*trunc[s]*p[s]**-th for s in range(n+1)))
        for theta in (1.,.5,.25):
            th=mp.mpf(str(theta))
            for c in (2.,4.,8.):
                W=sum(C[s]*mu[s]*mp.mpf(c)**-s*up[s]**-th for s in range(1,n+1))
                row[f'W_c{c:g}_th{theta:g}']=lg(W);row[f'W_K_c{c:g}_th{theta:g}']=V*lg(W/V)/I
        refs={f'tau{r:g}':noise(r) for r in (.25,.5,.75)}
        refs['mixture3']=[sum(refs[key][s] for key in refs)/3 for s in range(n+1)]
        refs['mixture_uniform']=[sum(math.comb(n-s,k-s)*mu[k]/((k+1)*math.comb(k,s)) for k in range(s,n+1)) for s in range(n+1)]
        Z=sum(C[s]*up[s] for s in range(n+1));refs['markov_normalized']=[u/Z for u in up]
        for name,pi in refs.items():row['ref_'+name]=cost(pi)
        row['markov_logZ']=lg(Z);inf=2*q;row['ref_product']=n*(lg(1+inf)-inf*lg(inf))
        row['parseval_error']=abs(sum(C[s]*mu[s] for s in range(n+1))-1)
        return {key:float(value) if isinstance(value,mp.mpf) else value for key,value in row.items()}
