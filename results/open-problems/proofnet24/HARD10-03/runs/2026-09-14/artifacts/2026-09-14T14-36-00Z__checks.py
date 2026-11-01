"""HARD10-03 sanity checks. The proofs are in the report."""
import math

def reciprocal_from_p(p):
    return sum(pk/(i+1) for i,pk in enumerate(p))

def reciprocal_from_cdf(p):
    F=s=0.0
    for m,pk in enumerate(p,start=1):
        F += pk
        s += F/(m*(m+1))
    s += F/(len(p)+1)
    return s

for p in ([1.0],[0.2,0.3,0.5],[0.01,0.09,0.2,0.3,0.4]):
    assert abs(reciprocal_from_p(p)-reciprocal_from_cdf(p))<1e-12
print('summation-by-parts reciprocal identity: PASSED')

for a in [0.2,0.1,0.03,0.01,0.003]:
    M=int(math.floor(1/a)); p=[]; prev=0.0
    for m in range(1,M+2):
        cur=min(1.0,a*m); p.append(cur-prev); prev=cur
        if cur>=1.0: break
    val=reciprocal_from_p(p)
    bound=a*(1+math.log(2/a))
    print(f'a={a:g} extremal E[1/L]={val:.8g} bound={bound:.8g}')
    assert val<=bound+1e-12
print('CDF-envelope inverse-length bound: PASSED')

def interaction_envelope(d,beta,K):
    first=beta**(-d/2)*sum(r**(-d/2) for r in range(1,K+1))
    jumps=beta**(1-d/2)*sum((K-r)*r**(-d/2) for r in range(1,K))
    return first+jumps

for beta in [10**2,10**3,10**4,10**5,10**6]:
    K=max(1,int(beta**0.4)); b=interaction_envelope(3,beta,K); scale=K/math.sqrt(beta)
    print(f'beta={beta:7d} K={K:4d} envelope={b:.6g} K/sqrt(beta)={scale:.6g} ratio={b/scale:.5g}')
print('interaction-envelope scaling check: COMPLETED')
