"""T255 section 9 local step, checked directly: the generator of Y = a^-q + |w|^2 + M Phi_S^p (full SDE: drift, attention
noise and linear c-noise, exact first and second derivatives) at random points of D = {a > lam1, |w| < delta, Phi_S < delta},
in 50-digit arithmetic. Points are built in coordinates: L = [[sqrt a, 0], [sqrt a w, chol X]], X = a Phi_S S, tr S = 1.
Reports max over samples of LY / (|W|^2 * Y_scale), where Y_scale = a^-q + |w|^2 + M Phi_S^p. usage: m g2 q p delta lam1 M N"""
import sys, random
import mpmath as mp
mp.mp.dps = 50
m=int(sys.argv[1]); g2=mp.mpf(sys.argv[2]); q=mp.mpf(sys.argv[3]); p=mp.mpf(sys.argv[4]); delta=mp.mpf(sys.argv[5])
lam1=mp.mpf(sys.argv[6]); M=mp.mpf(sys.argv[7]); N=int(sys.argv[8]); tau0=mp.mpf(1)
rnd=random.Random(7+m)
I=mp.eye(m); P=I-mp.ones(m,m)/m
k=g2/(m*tau0); c=g2*(2-g2)
def T(A): return A.T
def drift(V):
    W=P*V*P; nW=sum(W[i,j]**2 for i in range(m) for j in range(m))
    trW=sum(W[i,i] for i in range(m)); D=mp.matrix([W[i,i]-trW/m for i in range(m)]); v=mp.matrix([V[i,i] for i in range(m)])
    VD=V*D; O=v*T(VD); return g2/tau0**2*(V*nW/m**2+(O+T(O))/(2*m)), nW
def basis(L,V):
    out=[]
    for i in range(m):
        for j in range(m):
            Nm=mp.zeros(m,m); Nm[i,j]=1; X=L*Nm*T(L)*P*V; out.append(k*(X+T(X)))
    for i in range(m):
        for j in range(i,m):
            H=mp.zeros(m,m)
            if i==j: H[i,i]=mp.sqrt(2)
            else: H[i,j]=H[j,i]=1
            out.append(mp.sqrt(c)*L*H*T(L))
    return out
def pieces(V,a,w,g):
    """first and second directional derivatives of a^-q, |w|^2, Phi^p along E (exact formulas)"""
    x=a*w
    def d(E,second):
        E11=E[0,0]; Ex=mp.matrix([E[i,0] for i in range(1,m)])
        tr=sum(E[i,i] for i in range(1,m)); xEx=sum(x[i]*Ex[i] for i in range(m-1)); xx=sum(xi**2 for xi in x)
        dg=tr-2*xEx/a+xx*E11/a**2
        Dw=Ex/a-x*E11/a**2
        Phi=g/a; DPhi=dg/a-g*E11/a**2
        d1=-q*a**(-q-1)*E11+2*sum(w[i]*Dw[i] for i in range(m-1))+M*p*Phi**(p-1)*DPhi
        if not second: return d1
        ExEx=sum(e**2 for e in Ex)
        d2g=-2*ExEx/a+4*xEx*E11/a**2-2*xx*E11**2/a**3
        D2w=-2*Ex*E11/a**2+2*x*E11**2/a**3
        D2Phi=d2g/a-2*dg*E11/a**2+2*g*E11**2/a**3
        return (q*(q+1)*a**(-q-2)*E11**2+2*sum(e**2 for e in Dw)+2*sum(w[i]*D2w[i] for i in range(m-1))
                +M*(p*(p-1)*Phi**(p-2)*DPhi**2+p*Phi**(p-1)*D2Phi))
    return d
worst=-mp.inf; wpt=None
for s in range(N):
    a=lam1*mp.mpf(10)**(rnd.uniform(0,8))
    wr=mp.matrix([rnd.gauss(0,1) for _ in range(m-1)]); wn=mp.sqrt(sum(t**2 for t in wr))
    w=wr*(delta*mp.mpf(rnd.random())**(1.0/(m-1)) if rnd.random()<0.8 else delta*mp.mpf(10)**(-rnd.uniform(0,8)))/wn
    Phi=delta*mp.mpf(10)**(-rnd.uniform(0,12))
    Bm=mp.matrix(m-1,m-1)
    for i in range(m-1):
        for j in range(i+1): Bm[i,j]=rnd.gauss(0,1) if i!=j else abs(rnd.gauss(0,1))+0.05
    S=Bm*T(Bm); trS=sum(S[i,i] for i in range(m-1)); Cx=Bm*mp.sqrt(a*Phi/trS)
    L=mp.zeros(m,m); L[0,0]=mp.sqrt(a)
    for i in range(m-1):
        L[i+1,0]=mp.sqrt(a)*w[i]
        for j in range(m-1): L[i+1,j+1]=Cx[i,j]
    V=L*T(L); g=a*Phi
    b,nW=drift(V); d=pieces(V,a,w,g)
    LY=d(b,False)+sum(d(E,True) for E in basis(L,V))/2
    Ys=a**(-q)+sum(t**2 for t in w)+M*Phi**p
    r=LY/(nW*Ys)
    if r>worst: worst=r; wpt=(float(mp.log10(a)),float(mp.sqrt(sum(t**2 for t in w))),float(mp.log10(Phi)))
print("m %d g2 %s q %s p %s delta %s lam1 %s M %s N %d: max LY/(|W|^2 Y) = %.4e at (log10 a, |w|, log10 Phi_S) = %s"%(
    m,g2,q,p,delta,lam1,M,N,float(worst),tuple(round(z,3) for z in wpt)),flush=True)
