import numpy as np
x,w=np.polynomial.hermite_e.hermegauss(100); w=w/w.sum()
X,Y=np.meshgrid(x,x); W=np.outer(w,w)
th=np.tanh; dth=lambda z:1/np.cosh(z)**2
def E2(f,g,q,c):
    s=np.sqrt(max(1-c*c,0)); u=np.sqrt(q)*X; v=np.sqrt(q)*(c*X+s*Y); return (W*f(u)*g(v)).sum()
def run(sw2,sb2,n,L,seed):
    q=1.0
    for _ in range(2000): q=sw2*(w*th(np.sqrt(q)*x)**2).sum()+sb2
    chi1=sw2*(w*dth(np.sqrt(q)*x)**2).sum(); B=(sw2*E2(dth,dth,q,1.0)-sw2*E2(dth,dth,q,1-1e-5))/1e-5; T=q/(1-chi1)
    rng=np.random.default_rng(seed); V=rng.standard_normal((n,5)); V/=np.linalg.norm(V,axis=1,keepdims=True)
    C=V@V.T; Th=q*C.copy(); np.fill_diagonal(C,1.0)
    for l in range(2,L+1):
        Cn=C.copy(); Chi=np.full_like(C,chi1)
        for i in range(n):
            for j in range(i+1,n):
                c=C[i,j]; Chi[i,j]=Chi[j,i]=sw2*E2(dth,dth,q,c); Cn[i,j]=Cn[j,i]=(sw2*E2(th,th,q,c)+sb2)/q
        Th=q*Cn+Chi*Th; C=Cn
    A=(1-C)/chi1**L
    P=np.eye(n)-np.ones((n,n))/n
    lamA=np.linalg.eigvalsh(P@(-A)@P)[1]   # smallest on 1-perp (index0 is the 1 direction, 0)
    lam=np.linalg.eigvalsh(Th)[0]
    pred=(q+B*T/chi1)*lamA
    print(f"sw2={sw2} n={n} L={L}: lambda_min/(L chi^L)={lam/(L*chi1**L):.5f}  predicted (q*+BT*/chi1)*lmin_perp(-A)={pred:.5f}  ratio={lam/(L*chi1**L)/pred:.4f}")
for L in (60,120,200): run(1.5,0.05,8,L,0)
for L in (40,80,120): run(1.2,0.05,8,L,0)
