import numpy as np, sys
x,w=np.polynomial.hermite_e.hermegauss(120); w=w/w.sum()
X,Y=np.meshgrid(x,x); W=np.outer(w,w)
def E2(f,g,q,c):
    s=np.sqrt(max(1-c*c,0)); u=np.sqrt(q)*X; v=np.sqrt(q)*(c*X+s*Y); return (W*f(u)*g(v)).sum()
th=np.tanh; dth=lambda z:1/np.cosh(z)**2
def run(sw2,sb2,c0,Lmax):
    q=1.0
    for _ in range(2000): q=sw2*(w*th(np.sqrt(q)*x)**2).sum()+sb2
    chi1=sw2*(w*dth(np.sqrt(q)*x)**2).sum()
    chi=lambda c: sw2*E2(dth,dth,q,c)
    h=1e-5; B=(chi(1.0)-chi(1-h))/h
    T=q/(1-chi1)
    c=c0; Td=q; To=q*c; out=[]
    for l in range(1,Lmax+1):
        chic=chi(c)
        cn=(sw2*E2(th,th,q,c)+sb2)/q
        Td=q+chi1*Td; To=q*cn+chic*To; c=cn
        out.append((l,1-c,Td-To))
    # A from tail
    lA,DA,_=out[-1]; A=DA/chi1**lA
    kappa=A*(q+B*T/chi1)
    print(f"sw2={sw2} c0={c0}: q*={q:.5f} chi1={chi1:.5f} A={A:.5f} B={B:.5f} T*={T:.4f} kappa={kappa:.5f}")
    for l,D,E in out:
        if l in (20,40,80,120,160,200,Lmax): print(f"  L={l:4d} E/(L chi^L)={E/(l*chi1**l):.5f}  D/chi^L={D/chi1**l:.5f}")
for sw2 in (1.5,1.2):
    for c0 in (0.0,0.5): run(sw2,0.05,c0,200 if sw2==1.5 else 120)
