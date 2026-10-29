# linear (c) noise part: its contribution to drift(log trSchur/V00) per unit t at the corner, w=0, s->0 (must be finite)
import sympy as sp
g2,s=sp.symbols('g2 s',positive=True)
for m in (3,4):
    t=[sp.Symbol('t%d'%i,positive=True) for i in range(m-1)]
    L=sp.diag(*([1]+[s*x for x in t])); V=L*L.T; c=g2*(2-g2)
    a=V[0,0]; l=sum(V[i,i] for i in range(1,m)); ito=0
    for i in range(m):
        for j in range(i,m):
            H=sp.zeros(m,m)
            if i==j: H[i,i]=sp.sqrt(2)
            else: H[i,j]=H[j,i]=1
            E=sp.sqrt(c)*L*H*L.T
            el=sum(E[r,r] for r in range(1,m))
            ito+= -el**2/l**2 + E[0,0]**2/a**2 - 2*sum(E[r,0]**2 for r in range(1,m))/(a*l)
    print("m",m,"c-part drift of log(trSchur/V00) per t:",sp.factor(sp.limit(sp.simplify(ito/2),s,0)))
