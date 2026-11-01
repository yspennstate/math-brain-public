# Monte Carlo of the transverse exponent at m=3 near e1: Euler in the u-clock, attention noise only; mean of d log Phi / d u
import sys, numpy as np
g2=float(sys.argv[1]); h=float(sys.argv[2]); steps=int(sys.argv[3]); R=int(sys.argv[4]); mode=sys.argv[5]
m=int(sys.argv[6]) if len(sys.argv)>6 else 3; tau0=1.0; k=g2/(m*tau0); P=np.eye(m)-1.0/m; rng=np.random.default_rng(4)
s=1e-3
L0=np.zeros((R,m,m)); L0[:,0,0]=1
if mode=="orth": L0[:,1:,1:]=s*np.eye(m-1)
else: L0[:,1:,:]=s*rng.standard_normal((R,m-1,m))
V=L0@np.swapaxes(L0,1,2)
phi=lambda V:(np.trace(V,axis1=1,axis2=2)-V[:,0,0])/V[:,0,0]
schur=lambda V:(np.trace(V,axis1=1,axis2=2)-V[:,0,0]-np.sum(V[:,1:,0]**2,1)/V[:,0,0])/V[:,0,0]
lp0=np.log(phi(V)); ls0=np.log(schur(V)); u=np.zeros(R); rej=0
for st in range(steps):
    W=P@V@P; trW=np.trace(W,axis1=1,axis2=2); nW2=np.sum(W*W,(1,2)); dt=h/nW2
    D=np.einsum('kii->ki',W)-trW[:,None]/m; v=np.einsum('kii->ki',V); VD=np.einsum('kij,kj->ki',V,D)
    b=g2/tau0**2*(V*(nW2/m**2)[:,None,None]+(v[:,:,None]*VD[:,None,:]+VD[:,:,None]*v[:,None,:])/(2*m))
    L=np.linalg.cholesky(V)
    N=rng.standard_normal((R,m,m))*np.sqrt(dt)[:,None,None]
    X=L@N@np.swapaxes(L,1,2)@P@V
    Vn=V+b*dt[:,None,None]+k*(X+np.swapaxes(X,1,2)); Vn=(Vn+np.swapaxes(Vn,1,2))/2
    try: np.linalg.cholesky(Vn); V=Vn
    except np.linalg.LinAlgError:
        ok=np.linalg.eigvalsh(Vn)[:,0]>0; V[ok]=Vn[ok]; rej+=np.sum(~ok); dt=np.where(ok,dt,0)
    tr=np.trace(V,axis1=1,axis2=2); V=V/tr[:,None,None]   # homogeneous: rescale, ratios unchanged
    u+=nW2*dt/tr**2*tr**2
print("g2 %.2f h %g mode %s: u %.2f | mean dlogPhi/du %+.4f (se %.4f) | mean dlog(trSchur/V11)/du %+.4f (se %.4f) WAS %+.4f | rejected %d"%(g2,h,mode,np.mean(u),np.mean((np.log(phi(V))-lp0)/u),np.std((np.log(phi(V))-lp0)/u)/np.sqrt(R),np.mean((np.log(schur(V))-ls0)/u),np.std((np.log(schur(V))-ls0)/u)/np.sqrt(R),0,rej))
