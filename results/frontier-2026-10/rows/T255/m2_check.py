"""T255 m=2: the exact finite-network covariance chain (chain_blowup.py step) against the exact 1D law of w = tr(PV):
 dw = kap w^3 dt + sqrt(2c w^2 + 4k^2 w^4) dB, kap = g2/(4 tau0^2), c = g2(2-g2), 4k^2 = g2^2/tau0^2,
 scale density s'(y) = (2c + 4k^2 y^2)^(-1/(4 g2)), P(hit K before eps | w0) = int_eps^w0 s' / int_eps^K s'.
usage: python m2_check.py g2 n K eps reps Tmax"""
import sys, numpy as np
from scipy.integrate import quad
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
g2=float(sys.argv[1]); n=int(sys.argv[2]); K=float(sys.argv[3]); eps=float(sys.argv[4]); R=int(sys.argv[5]); Tmax=float(sys.argv[6])
m=2; tau0=1.0; nk=1; lam,gam=np.sqrt(1-g2),np.sqrt(g2); tau=tau0*np.sqrt(n*nk)
rng=np.random.default_rng(int(g2*1000)+n)
rho0=0.2; V=np.broadcast_to((1-rho0)*np.eye(m)+rho0,(R,m,m)).copy()
P=np.eye(m)-0.5; I=np.eye(m); J=np.ones((m,m))/m
w0=np.trace(P@V[0])
state=np.zeros(R,int)  # 0 alive, 1 hit K, -1 hit eps
il=np.tril_indices(m,-1)
def wishart(k,size):
    B=np.zeros((size,m,m))
    for i in range(m): B[:,i,i]=np.sqrt(rng.chisquare(k-i,size))
    B[:,il[0],il[1]]=rng.standard_normal((size,len(il[0])))
    return B@np.swapaxes(B,1,2)
step=0
while (state==0).any() and step<Tmax*n:
    step+=1
    idx=np.nonzero(state==0)[0]; Va=V[idx]; k=len(idx)
    L=np.linalg.cholesky(Va+1e-14*I)
    G1=rng.standard_normal((k,m,nk)); G2=rng.standard_normal((k,m,nk))
    Y=L@G1@np.swapaxes(G2,1,2)@np.swapaxes(L,1,2)
    Zs=Y/tau; Zs=Zs-Zs.max(2,keepdims=True); E=np.exp(Zs); A=I+E/E.sum(2,keepdims=True)-J
    Z=rng.standard_normal((k,m,m)); LT=np.swapaxes(L,1,2); AT=np.swapaxes(A,1,2)
    cross=L@np.swapaxes(Z,1,2)@LT@AT
    GG=Z@np.swapaxes(Z,1,2)+wishart(n-m,k)
    Vn=lam**2*Va+(lam*gam/np.sqrt(n))*(cross+np.swapaxes(cross,1,2))+(g2/n)*(A@L@GG@LT@AT)
    V[idx]=Vn
    w=np.einsum('ij,kij->k',P,Vn)
    state[idx[w>=K]]=1; state[idx[w<=eps]]=-1
c=g2*(2-g2); k4=g2**2/tau0**2
sp=lambda y:(2*c+k4*y*y)**(-1/(4*g2))
th=quad(sp,eps,w0)[0]/quad(sp,eps,K)[0]
thinf=quad(sp,eps,w0)[0]/quad(sp,eps,np.inf)[0] if 1/(2*g2)>1 else 0.0
ph=(state==1).mean(); se=np.sqrt(ph*(1-ph)/R)
print("g2 %.2f n %d K %g eps %g w0 %.2f reps %d: chain P(hit K first) %.4f +- %.4f (unresolved %d) | exact 1D law %.4f | P(explode) %.4f"%(g2,n,K,eps,w0,R,ph,se,(state==0).sum(),th,thinf),flush=True)
