"""Small exact checks; no simulation is treated as a proof."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for tail in compositions(n-j, k-1):
                yield (j,) + tail

def polynomial(m, theta, u):
    k=len(u); value=F(0); grad=[F(0)]*k; hess=[[F(0)]*k for _ in u]
    for a in compositions(m,k):
        c=F(factorial(m), __import__('math').prod(factorial(n) for n in a))
        for t,n in zip(theta,a): c*=t**(n*n)
        def monomial(beta):
            ans=c
            for x,n in zip(u,beta): ans*=x**n
            return ans
        value+=monomial(a)
        for i in range(k):
            if a[i]:
                b=list(a); b[i]-=1; grad[i]+=a[i]*monomial(b)
            for j in range(k):
                mult=a[i]*(a[j]-(i==j))
                if mult>0:
                    b=list(a); b[i]-=1; b[j]-=1; hess[i][j]+=mult*monomial(b)
    return value,grad,hess

count=0
transport_cases=0
for k in (2,3):
    for m in range(2,7 if k==2 else 5):
        theta=[64]*k
        for i in reversed(range(k-1)): theta[i]=3*max(theta[j]**(2*m-1) for j in range(i+1,k))
        points=list(compositions(3,k))+[(F(1,3),)*k, (F(0),)*k]
        for u in points:
            P,g,H=polynomial(m,theta,u)
            assert P>=sum(u)**m
            for i in range(k):
                for j in range(i+1,k):
                    assert g[i]>=3*g[j]
                    assert H[i][j]**2*(theta[i]*theta[j])**2<=H[i][i]*H[j][j]
            # R has all ones on/below its diagonal: solve R^T lambda=g.
            lam=[F(0)]*k
            for i in reversed(range(k)):
                lam[i]=g[i]-sum(lam[j] for j in range(i+1,k))
                assert 0<=lam[i]<=g[i]
            # nu_i=1, b_i=(-1)^i, so the parabolicity margin is mu=1.
            for v in [tuple(1 for _ in range(k)),tuple((-1)**i for i in range(k)),tuple(i-1 for i in range(k))]:
                energy=sum(H[i][i]*v[i]**2 for i in range(k))
                Q=-F(1,2)*energy
                for i in range(k):
                    for j in range(i+1,k):
                        Q+=(-2+(-1)**(i+j))*H[i][j]*v[i]*v[j]
                assert Q<=-F(1,4)*energy
                transport_cases+=1
            count+=1
Path('polynomial_checks.json').write_text(json.dumps({'exact_rational_cases':count,'transport_quadratic_cases':transport_cases,'result':'all passed','checked':'gradient hierarchy; normalized mixed Hessian bound; lower polynomial bound; triangular dual cone; transport absorption; boundary and origin'},indent=2),encoding='utf-8')
print('Exact rational checks passed:',count,flush=True)
