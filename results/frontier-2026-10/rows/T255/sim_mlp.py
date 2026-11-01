"""T255 sections 13-14 check by direct simulation (agent Q, 17 Oct). Euler-Maruyama on the full m x m Corollary 4.3 SDE
(attention drift and noise of gen.py, c-noise, MLP drift b_res and MLP noise sqrt(2 g2) L dH L^T), R paths in a batch, adaptive
step dt = h/(1+w)^2 with w = tr(PV)... per path. A path explodes when tr V > BIG; for m = 2 it is decided non-exploding when
w < SMALL (from there the Feller probability of explosion is negligible). usage: m g2 Delta R h T seed V0(diag,offdiag)"""
import sys, time, numpy as np
WALL=float(sys.argv[10]) if len(sys.argv)>10 else 1e9; t_wall=time.time()   # optional wall budget (s): stop and report what is decided
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
m=int(sys.argv[1]); g2=float(sys.argv[2]); DEL=float(sys.argv[3]); R=int(sys.argv[4]); h=float(sys.argv[5]); T=float(sys.argv[6])
rng=np.random.default_rng(int(sys.argv[7])); d0=float(sys.argv[8]); o0=float(sys.argv[9]); tau0=1.0
BIG=1e5; SMALL=1e-5; P=np.eye(m)-1.0/m; c=g2*(2-g2); k=g2/(m*tau0)
V=np.tile(np.full((m,m),o0)+np.eye(m)*(d0-o0),(R,1,1)); t=np.zeros(R); state=np.zeros(R,int)  # 0 live, 1 explode, 2 decided no
def drift(V):
    W=P@V@P; nW=np.einsum('rij,rij->r',W,W); D=np.einsum('rii->ri',W)-np.einsum('rii->r',W)[:,None]/m
    v=np.einsum('rii->ri',V); VD=np.einsum('rij,rj->ri',V,D)
    B=g2/tau0**2*(V*nW[:,None,None]/m**2+(v[:,:,None]*VD[:,None,:]+VD[:,:,None]*v[:,None,:])/(2*m))
    s=np.sqrt(np.einsum('rii->ri',V)); r=np.clip(V/(s[:,:,None]*s[:,None,:]),-1,1)
    nu=DEL/(2*np.pi)*(np.sqrt(1-r*r)-r*np.arccos(r)); nu[:,np.arange(m),np.arange(m)]=0
    return B+g2*nu*s[:,:,None]*s[:,None,:]
step=0
while True:
    live=np.where(state==0)[0]
    if live.size==0 or step>2_000_000 or time.time()-t_wall>WALL: break
    if step%2000==0: print(f'step {step} live {live.size} exploded {(state==1).sum()} decided-no {(state==2).sum()} t_med {np.median(t[live]):.2f}', flush=True)
    Vl=V[live]; w=np.einsum('ij,rji->r',P,Vl)
    dt=np.minimum(h/(1+w)**2, T-t[live]+1e-12); sq=np.sqrt(dt)[:,None,None]
    ev0,U0=np.linalg.eigh(Vl); L=U0*np.sqrt(np.maximum(ev0,0))[:,None,:]   # any square root: GOE and iid noise are O-invariant
    G1=rng.standard_normal((live.size,m,m)); H1=(G1+np.swapaxes(G1,1,2))/np.sqrt(2)
    G2=rng.standard_normal((live.size,m,m)); H2=(G2+np.swapaxes(G2,1,2))/np.sqrt(2)
    N=rng.standard_normal((live.size,m,m)); LT=np.swapaxes(L,1,2)
    X=L@N@LT@P@Vl
    dV=drift(Vl)*dt[:,None,None]+sq*((np.sqrt(c)*L@H1@LT)+np.sqrt(2*g2)*(L@H2@LT)+k*(X+np.swapaxes(X,1,2)))
    Vn=Vl+dV; Vn=(Vn+np.swapaxes(Vn,1,2))/2
    ev,U=np.linalg.eigh(Vn); bad=ev[:,0]<=0
    if bad.any(): ev[bad]=np.maximum(ev[bad],1e-14*ev[bad,-1:]); Vn[bad]=(U[bad]*ev[bad][:,None,:])@np.swapaxes(U[bad],1,2)
    V[live]=Vn; t[live]+=dt
    tr=np.einsum('rii->r',Vn); wn=np.einsum('ij,rji->r',P,Vn)
    state[live[tr>BIG]]=1
    if m==2: state[live[(tr<=BIG)&(wn<SMALL)]]=2
    state[live[(state[live]==0)&(t[live]>=T)]]=3
    step+=1
n1=(state==1).sum(); n3=(state==3).sum()+(state==0).sum(); p=n1/R
print(f'm {m} g2 {g2} Delta {DEL} R {R} h {h} T {T}: exploded {n1} ({p:.4f} +- {np.sqrt(p*(1-p)/R):.4f}), decided-no {(state==2).sum()}, undecided at T {n3}, steps {step}')
