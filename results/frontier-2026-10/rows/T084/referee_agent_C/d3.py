"""D3: per lam-power, the q-power-series coefficients of N/(1-q)^2 are nonnegative.
N = sum_k a_k u^k (a_0 = 0). N/u^2 = a_1/(1-q) + sum_{k>=2} a_k (1-q)^(k-2), so the q^j coefficient is
a_1 + [poly part]_j; for j beyond the poly part it is a_1 (= b_0)."""
import sys, random, itertools
from math import comb
def series_ok_dict(N):
    # N as {(i,j): c} lam^i u^j  -> list of (j, i, coeff) negatives
    deg=max(j for (_,j) in N)
    a1={i:c for (i,j),c in N.items() if j==1}
    poly={}
    for (i,k),c in N.items():
        if k>=2:
            for j in range(k-1):
                poly[(i,j)]=poly.get((i,j),0)+c*comb(k-2,j)*(-1)**j
    neg=[]
    for j in range(max(deg-1,1)):
        lams={i for (i,jj) in poly if jj==j}|set(a1)
        for i in lams:
            v=a1.get(i,0)+poly.get((i,j),0)
            if v<0: neg.append((j,i,v))
    return neg, any(a1.values())
if __name__=='__main__' and sys.argv[1]=='kn':
    import rec
    kind=sys.argv[2]
    for n in range(int(sys.argv[3]),int(sys.argv[4])+1):
        N=rec.Npoly(n,kind)
        D={(i,k):int(c) for k,x in enumerate(N) for i,c in enumerate(x.coeffs()) if c}
        neg,a1=series_ok_dict(D)
        print(kind,n,'neg',len(neg),neg[:2],'a1!=0',a1,flush=True)
if __name__=='__main__' and sys.argv[1]=='rand':
    import brute
    rnd=random.Random(int(sys.argv[2])); T=int(sys.argv[3]); bad=0; seen=0
    for t in range(T):
        n=rnd.randint(4,7); allE=list(itertools.combinations(range(n),2))
        m=rnd.randint(2,min(len(allE),14)); E=rnd.sample(allE,m); e,f=rnd.sample(E,2)
        N=brute.N_of(n,E,e,f)
        if not N: continue
        seen+=1
        neg,_=series_ok_dict(N)
        if neg:
            bad+=1
            if bad<=5: print('FAIL n',n,'E',E,'e',e,'f',f,'neg',neg[:3])
    print('random graphs',T,'nonzero N',seen,'failures',bad)
