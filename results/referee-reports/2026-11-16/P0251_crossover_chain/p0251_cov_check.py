# exact Cov(g(m(k)), g(m(k'))) for a uniform perfect matching, g in {0,1}^K (extreme points suffice: cov is
# bilinear-quadratic in g, so check 0/1 and also random [0,1] vectors)
import numpy as np
def cov(K,g,k=0,kp=1):
    G=g.sum(); H=G-g[k]-g[kp]; rest=np.delete(g,[k,kp])
    e2=g[k]*g[kp]/(K-1)+(H*H-(rest**2).sum())/((K-1)*(K-3))
    return e2-(G-g[k])*(G-g[kp])/(K-1)**2
worst=0
for K in (8,10,16,32,64,128,512,2048):
    m=0
    for n in range(K+1):
        for gk in (0,1):
            for gkp in (0,1):
                if gk+gkp>n or n-gk-gkp>K-2: continue
                g=np.zeros(K); g[0]=gk; g[1]=gkp; g[2:2+n-gk-gkp]=1
                m=max(m,abs(cov(K,g))*(K-3))
    rng=np.random.default_rng(K)
    for _ in range(2000): m=max(m,abs(cov(K,rng.random(K)))*(K-3))
    worst=max(worst,m); print(K,"max |cov|*(K-3) =",round(m,4))
# brute-force check of the formula at K=8 by enumerating all matchings
import itertools
def matchings(s):
    if not s: yield []; return
    a=s[0]
    for i in range(1,len(s)):
        for r in matchings(s[1:i]+s[i+1:]): yield [(a,s[i])]+r
K=8; g=np.random.default_rng(1).random(K); vals=[]
for M in matchings(list(range(K))):
    p={}; [p.update({a:b,b:a}) for a,b in M]; vals.append((g[p[0]],g[p[1]]))
v=np.array(vals); print("K=8 brute cov",np.cov(v.T,bias=True)[0,1],"formula",cov(K,g))
