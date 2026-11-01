"""T255 m>=3: the large-scale (homogeneous) limit of the Thm 4.2 SDE, attention noise only (the linear noise is lower order
at large |V|), drift exact. Scale-free: V renormalised to tr V = 1 each step, log-scale ell tracked; real time dt_real = dt e^{-2 ell}.
Reports the growth of log tr W against its own clock u = int |W|_F^2 dt, the drift of log(S/trW), rho = |r|^2/(trW S/m) (<= 1 by PSD... up to constant),
and sum dt_real (finite and settled = explosion in finite time from that start).
usage: python lyap.py m g2 h steps reps [lin]"""
import sys, numpy as np
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
m=int(sys.argv[1]); g2=float(sys.argv[2]); h=float(sys.argv[3]); steps=int(sys.argv[4]); R=int(sys.argv[5]); lin=False
tau0=1.0; k=g2/(m*tau0); c=g2*(2-g2)
rng=np.random.default_rng(7*m+int(100*g2))
P=np.eye(m)-1.0/m; one=np.ones(m)
eta=float(sys.argv[6]) if len(sys.argv)>6 else 1e-3
A=rng.standard_normal((R,m,m)); V=eta*A@np.swapaxes(A,1,2)/m; V[:,0,0]+=1.0
tr=np.trace(V,axis1=1,axis2=2); V/=tr[:,None,None]; ell=np.log(tr)+np.log(1e3)  # start at scale 1e3
ell0=ell.copy()
uW=np.zeros(R); treal=np.zeros(R); logtrW=np.zeros(R); logS=np.zeros(R)
def stats(V):
    W=P@V@P; trW=np.trace(W,axis1=1,axis2=2); S=np.einsum('i,kij,j->k',one,V,one)/m
    r=np.einsum('ij,kjl,l->ki',P,V,one); rho=np.sum(r*r,1)/(trW*S*m)
    return W,trW,S,rho
W,trW,S,rho=stats(V); lt0=np.log(trW)+ell; ls0=np.log(S)+ell
rec=[]
for st in range(steps):
    W,trW,S,rho=stats(V)
    nW=np.sqrt(np.sum(W*W,(1,2))); nV=np.sqrt(np.sum(V*V,(1,2)))
    dt=h/(nW*nV+1e-300)
    D=np.einsum('kii->ki',W)-trW[:,None]/m; v=np.einsum('kii->ki',V); VD=np.einsum('kij,kj->ki',V,D)
    b=g2/tau0**2*(V*(nW**2/m**2)[:,None,None]+(v[:,:,None]*VD[:,None,:]+VD[:,:,None]*v[:,None,:])/(2*m))
    L=np.linalg.cholesky(V+1e-15*np.eye(m))
    N=rng.standard_normal((R,m,m))*np.sqrt(dt)[:,None,None]
    X=L@N@np.swapaxes(L,1,2)@P@V
    dV=b*dt[:,None,None]+k*(X+np.swapaxes(X,1,2))
    if lin:  # linear noise at the real scale: coefficient is sqrt(c) L H L^T at scale e^ell, i.e. relative e^{-ell}... keep exact
        Hm=rng.standard_normal((R,m,m)); Hm=(Hm+np.swapaxes(Hm,1,2))/np.sqrt(2)*np.sqrt(dt)[:,None,None]
        dV+=np.sqrt(c)*np.exp(-ell)[:,None,None]*(L@Hm@np.swapaxes(L,1,2))*np.exp(0)  # dt here is normalised; see note
    Vn=V+dV; Vn=(Vn+np.swapaxes(Vn,1,2))/2
    ev=np.linalg.eigvalsh(Vn); bad=ev[:,0]<=0
    if bad.any(): Vn[bad]=V[bad]  # reject (rare, h small)
    trn=np.trace(Vn,axis1=1,axis2=2); V=Vn/trn[:,None,None]
    uW+=nW**2*dt; treal+=dt*np.exp(-2*ell); ell=ell+np.log(trn)
    if (st+1)%(steps//10)==0:
        W,trW,S,rho=stats(V)
        lt=np.log(trW)+ell; ls=np.log(S)+ell
        ev=np.linalg.eigvalsh(V); eps=ev[:,-2]/ev[:,-1]
        print('   eps=lam2/lam1 of V: q10/50/90 %.2e %.2e %.2e | frac eps<1e-2 %.2f'%(*np.percentile(eps,[10,50,90]),np.mean(eps<1e-2)),flush=True)
        rec.append((st+1,np.median(uW),np.median((lt-lt0)/uW),np.median((ls-ls0)/uW),np.median(np.log(S/trW)),np.median(rho),np.mean(lt>lt0),np.median(treal),np.percentile(treal,90)))
        print("m %d g2 %.2f step %d med uW %.2f | med slope log trW/uW %+.4f | slope log S/uW %+.4f | med log(S/trW) %.2f | med rho %.3f | frac trW up %.2f | med t_real %.3e p90 %.3e"%((m,g2)+rec[-1]),flush=True)
