"""Entry-by-entry check of gen.py's noise covariance against ONE LAYER of the finite shaped-attention network
(the exact covariance chain of chain_blowup.py). n*Cov(V' - V) -> Sigma(V) = sum_j E_j (x) E_j. usage: python cov_check.py m g2 n K"""
import sys, numpy as np
from gen import noise_basis
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
m=int(sys.argv[1]); g2=float(sys.argv[2]); n=int(sys.argv[3]); K=int(sys.argv[4]); nk=1; tau0=1.0
rng=np.random.default_rng(77+m)
A0=rng.standard_normal((m,m)); V=(A0@A0.T/m+0.3*np.eye(m))*(float(sys.argv[5]) if len(sys.argv)>5 else 1.0)
L=np.linalg.cholesky(V); lam=np.sqrt(1-g2); gam=np.sqrt(g2); tau=tau0*np.sqrt(n*nk); I=np.eye(m); J=np.ones((m,m))/m
iu=np.triu_indices(m); il=np.tril_indices(m,-1)
S=np.zeros((len(iu[0]),)*2); mu=np.zeros(len(iu[0])); done=0; CH=20000
while done<K:
    k=min(CH,K-done)
    G1=rng.standard_normal((k,m,nk)); G2=rng.standard_normal((k,m,nk))
    Y=L@G1@np.swapaxes(G2,1,2)@L.T/tau; Y=Y-Y.max(2,keepdims=True); E=np.exp(Y); A=I+E/E.sum(2,keepdims=True)-J
    Z=rng.standard_normal((k,m,m))
    B=np.zeros((k,m,m))
    for i in range(m): B[:,i,i]=np.sqrt(rng.chisquare(n-m-i,k))
    B[:,il[0],il[1]]=rng.standard_normal((k,len(il[0])))
    GG=Z@np.swapaxes(Z,1,2)+B@np.swapaxes(B,1,2)
    cross=L@np.swapaxes(Z,1,2)@L.T@np.swapaxes(A,1,2)
    Vn=lam**2*V+(lam*gam/np.sqrt(n))*(cross+np.swapaxes(cross,1,2))+(g2/n)*(A@L@GG@L.T@np.swapaxes(A,1,2))
    d=(Vn-V)[:,iu[0],iu[1]]*np.sqrt(n)
    mu+=d.sum(0); S+=d.T@d; done+=k
mu/=K; C=S/K-np.outer(mu,mu)
Eb=noise_basis(V,g2,tau0,att=True,lin=True)
Th=np.zeros_like(C)
for Ej in Eb:
    e=Ej[iu]; Th+=np.outer(e,e)
se=np.sqrt((np.diag(C)[:,None]*np.diag(C)[None,:]+C**2)/K)
z=(C-Th)/se
print("m %d g2 %.2f n %d K %d: max |MC - Sigma| / max|Sigma| = %.4f ; max |z| = %.2f ; median |z| = %.2f"%(m,g2,n,K,np.max(abs(C-Th))/np.max(abs(Th)),np.max(abs(z)),np.median(abs(z))))
Tl=np.zeros_like(C)
for Ej in noise_basis(V,g2,tau0,att=False,lin=True):
    e=Ej[iu]; Tl+=np.outer(e,e)
Ta=Th-Tl; za=(C-Tl-Ta)/se
print("   attention part: max|Sigma_att|/max|Sigma| = %.3f ; max |(MC-Sigma_lin) - Sigma_att| / max|Sigma_att| = %.4f ; MC-Sigma_lin vs att corr %.5f"%(np.max(abs(Ta))/np.max(abs(Th)),np.max(abs(C-Tl-Ta))/np.max(abs(Ta)),np.corrcoef((C-Tl).ravel(),Ta.ravel())[0,1]))
print(" diag MC   :",np.round(np.diag(C),4)); print(" diag Sigma:",np.round(np.diag(Th),4))
