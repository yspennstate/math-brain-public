"""T255 m=3 on the invariant set {x2 = x3} (two tokens merged): V = E G E^T, E = [[1,0],[0,1],[0,1]], G 2x2 PSD.
Homogeneous (large-scale) limit, attention noise only, exact drift; L = E chol(G) (3x2), N 2x2 so the noise stays on the set.
usage: python lyapR.py g2 h steps reps"""
import sys, numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
g2=float(sys.argv[1]); h=float(sys.argv[2]); steps=int(sys.argv[3]); R=int(sys.argv[4])
m=3; tau0=1.0; k=g2/(m*tau0)
rng=np.random.default_rng(11+int(100*g2))
P=np.eye(m)-1.0/m; one=np.ones(m); E=np.array([[1.,0],[0,1],[0,1]])
A=rng.standard_normal((R,2,2)); G=A@np.swapaxes(A,1,2)+0.1*np.eye(2)
tr=np.trace(G,axis1=1,axis2=2); G/=tr[:,None,None]; ell=np.log(tr)+np.log(1e3)
uW=np.zeros(R); treal=np.zeros(R)
def V_of(G): return E@G@E.T
V=V_of(G); W=P@V@P; trW=np.trace(W,axis1=1,axis2=2); lt0=np.log(trW)+ell
for st in range(steps):
    V=V_of(G); W=P@V@P; trW=np.trace(W,axis1=1,axis2=2)
    nW=np.sqrt(np.sum(W*W,(1,2))); nV=np.sqrt(np.sum(V*V,(1,2)))
    dt=h/(nW*nV+1e-300)
    D=np.einsum('kii->ki',W)-trW[:,None]/m; v=np.einsum('kii->ki',V); VD=np.einsum('kij,kj->ki',V,D)
    b=g2/tau0**2*(V*(nW**2/m**2)[:,None,None]+(v[:,:,None]*VD[:,None,:]+VD[:,:,None]*v[:,None,:])/(2*m))
    C=np.linalg.cholesky(G+1e-14*np.eye(2)); L=E@C
    N=rng.standard_normal((R,2,2))*np.sqrt(dt)[:,None,None]
    X=L@N@np.swapaxes(L,1,2)@P@V
    dV=b*dt[:,None,None]+k*(X+np.swapaxes(X,1,2))
    # back to G: G11 = V11, G12 = V12 (= V13), G22 = V22 (= V23 = V33); check the set is kept
    if st==0: print("set kept: |dV22-dV33| %.1e |dV22-dV23| %.1e |dV12-dV13| %.1e"%(np.max(abs(dV[:,1,1]-dV[:,2,2])),np.max(abs(dV[:,1,1]-dV[:,1,2])),np.max(abs(dV[:,0,1]-dV[:,0,2]))),flush=True)
    Gn=np.stack([np.stack([V[:,0,0]+dV[:,0,0],V[:,0,1]+dV[:,0,1]],1),np.stack([V[:,0,1]+dV[:,0,1],V[:,1,1]+dV[:,1,1]],1)],1)
    det=Gn[:,0,0]*Gn[:,1,1]-Gn[:,0,1]**2; bad=(det<=0)|(Gn[:,0,0]<=0)
    if bad.any(): Gn[bad]=G[bad]
    trn=np.trace(Gn,axis1=1,axis2=2); G=Gn/trn[:,None,None]
    uW+=nW**2*dt; treal+=dt*np.exp(-2*ell); ell=ell+np.log(trn)
    if (st+1)%(steps//6)==0:
        V=V_of(G); W=P@V@P; trW=np.trace(W,axis1=1,axis2=2); lt=np.log(trW)+ell
        S=V.sum((1,2))/m; corr=G[:,0,1]/np.sqrt(G[:,0,0]*G[:,1,1])
        x=(lt-lt0)/uW
        print("g2 %.2f step %d med uW %.1f | slope log trW/uW q10/50/90 %+.4f %+.4f %+.4f | frac up %.2f | med log(S/trW) %.2f | med corr(x1,x2) %.3f | med t_real %.2e p90 %.2e"%(g2,st+1,np.median(uW),*np.percentile(x,[10,50,90]),np.mean(lt>lt0),np.median(np.log(S/trW)),np.median(corr),np.median(treal),np.percentile(treal,90)),flush=True)
np.savez("lyapR_g%.2f.npz"%g2,dlt=lt-lt0,uW=uW,treal=treal,G=G)
