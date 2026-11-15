"""Exhaustively enumerate edge rankings of K4, and check Lemma 2.1 exactly."""
import itertools
import math
from fractions import Fraction as F
import sympy as sp

n=4
edges=list(itertools.combinations(range(n),2))
tot=math.factorial(len(edges))
counts={k:[0,0,0,{}] for k in range(1,n)}
for order in itertools.permutations(edges):
    ranks={};deg=[0]*n
    for u,v in order:
        deg[u]+=1;deg[v]+=1
        ranks[u,v]=max(deg[u],deg[v])
    for k in counts:
        d=[0]*n
        for (u,v),rank in ranks.items():
            if rank<=k:d[u]+=1;d[v]+=1
        z=d.count(0)
        counts[k][0]+=z
        counts[k][1]+=z*(z-1)
        counts[k][2]+=(z==0)
        h=counts[k][3];h[z]=h.get(z,0)+1
x=sp.symbols('x')
for k,(s,f,z0,h) in counts.items():
    N=n-2;m=n-1
    q=sum(sp.binomial(N,j)*x**j*(1-x)**(N-j) for j in range(k,N+1))
    Q=sp.integrate(q,(x,0,x))
    M=sp.factorial(m)/sp.factorial(m-k-1)/sp.factorial(k)*sp.integrate(Q**k*(1-x)**(m-k-1),(x,0,1)) if m>k else None
    print('n=4 k=',k,'p1=',F(s,tot*n),'p2=',F(f,tot*n*(n-1)),'P(Z=0)=',F(z0,tot),'hist=',h,'auxiliary_M=',M)

# Independent algebraic check using g(x)=x^2: ordered-simplex integration.
m,k=7,3
xs=sp.symbols('x1:4')
for A in [(0,1,2),(0,2),(1,2),(2,)]:
    expr=sp.prod(xs[j]**2 for j in A)*(1-xs[2])**(m-k)
    expr=sp.integrate(expr,(xs[0],0,xs[1]))
    expr=sp.integrate(expr,(xs[1],0,xs[2]))
    lhs=sp.factorial(m)/sp.factorial(m-k)*sp.integrate(expr,(xs[2],0,1))
    d=k-len(A);G=x**3/3
    if d==0:
        rhs=sp.factorial(m)/sp.factorial(m-k-1)/sp.factorial(k)*sp.integrate(G**k*(1-x)**(m-k-1),(x,0,1))
    else:
        rhs=sp.binomial(k-1,d)*sp.factorial(m)/sp.factorial(m-k)/sp.factorial(k-1)*sp.integrate(x**2*G**(k-1-d)*x**d*(1-x)**(m-k),(x,0,1))
    print('Lemma2.1 m=7 k=3 g=x^2 ranks=',tuple(j+1 for j in A),'lhs=',lhs,'rhs=',rhs,'holds=',lhs<=rhs)
