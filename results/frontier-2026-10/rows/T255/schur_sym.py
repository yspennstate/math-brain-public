# TRUE transverse exponent: drift of log( tr Schur(V) / V00 ) per |W|^2 at the corner, w = 0, transverse block s*T, s -> 0
import sympy as sp, sys
g2,s=sp.symbols('g2 s',positive=True)
def run(m,general):
    P=sp.eye(m)-sp.ones(m,m)/m
    T=sp.zeros(m-1,m-1); syms=[]
    for i in range(m-1):
        for j in range(i+1):
            if general or i==j:
                t=sp.Symbol('t%d%d'%(i,j)); syms.append(t); T[i,j]=t
    L=sp.zeros(m,m); L[0,0]=1
    for i in range(m-1):
        for j in range(m-1): L[i+1,j+1]=s*T[i,j]
    V=L*L.T; W=P*V*P; trW=W.trace(); D=sp.Matrix([W[i,i]-trW/m for i in range(m)]); v=sp.Matrix([V[i,i] for i in range(m)])
    nW2=sum(W[i,j]**2 for i in range(m) for j in range(m))
    b=g2*(V*nW2/m**2+(v*(V*D).T+(V*D)*v.T)/(2*m)); k=g2/m
    a=V[0,0]; l=sum(V[i,i] for i in range(1,m))   # at w=0: Schur = V_perp, tr Schur = l
    # F = log(sum_i V_ii - sum_i V_i0^2/V00) - log V00 ; at w=0: grad = (1/l) on V_ii(i>=1), -1/a on V00; Hessian nonzero:
    #   d2/dV00^2 (-log V00) = 1/a^2 ; d2/dV_i0^2 of (-V_i0^2/V00)/l = -2/(a l) (each i>=1, symmetric entry counted once)
    #   d2/dV_ii^2 log l = -1/l^2 (all pairs i,j>=1)
    drift=sum(b[i,i] for i in range(1,m))/l-b[0,0]/a; ito=0
    for i in range(m):
        for j in range(m):
            N=sp.zeros(m,m); N[i,j]=1; Xn=L*N*L.T*P*V; E=k*(Xn+Xn.T)
            el=sum(E[r,r] for r in range(1,m))
            ito+= -el**2/l**2 + E[0,0]**2/a**2 - 2*sum(E[r,0]**2 for r in range(1,m))/(a*l)
    d=drift+ito/2
    lim=sp.simplify(sp.limit(sp.together(d/nW2),s,0))
    free=all(sp.simplify(sp.diff(lim,t))==0 for t in syms)
    return sp.factor(lim),free
for m in range(3,int(sys.argv[1])+1):
    e,free=run(m,m<=4)
    print("m",m,"mu_S =",e,"| shape-free:",free,flush=True)
