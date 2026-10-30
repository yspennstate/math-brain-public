"""T250 p = 3 (agent A, 18 Oct 2026): the frame-coupling bound for three inputs. Critical ReLU MLP, W_l iid N(0, 2/n),
three unit inputs in R^3 with pairwise angles (a, b, c) (c near a + b = near-coplanar is the hard case). At depth L the coupling
cost of the output triple against its GP limit is bounded by Bures(G, Cbar)^2 <= ||C^(1/2) D - Cbar^(1/2)||_F^2, G = D C D the
finite-width Gram of the layer-(L-1) post-activations normalised by 2/n, Cbar the arc-cosine iterate (radii 1). Prints
n/L * E Bures^2 (should be bounded in n, L if the p >= 3 route holds), and rho_min = min_l lam_min(Cbar_l)/theta_max_l^2.
argv: n_list L_fracs reps a b c seed"""
import sys, numpy as np
from scipy.linalg import sqrtm
n_list=[int(v) for v in sys.argv[1].split(',')]; fr=[float(v) for v in sys.argv[2].split(',')]; R=int(sys.argv[3])
a,b,c=map(float,sys.argv[4:7]); seed=int(sys.argv[7])
k=lambda t:(np.sin(t)+(np.pi-t)*np.cos(t))/np.pi
F=lambda t:np.arccos(np.clip(k(t),-1,1))
def inputs():
    u1=np.array([1.,0,0]); u2=np.array([np.cos(a),np.sin(a),0])
    # u3 at angle c from u1 and b from u2
    x=np.cos(c); y=(np.cos(b)-np.cos(a)*x)/np.sin(a); z=np.sqrt(max(1-x*x-y*y,0)); return np.stack([u1,u2,np.array([x,y,z])])
U=inputs(); C0=U@U.T
def cbar(L):
    th=np.arccos(np.clip(C0[[0,1,0],[1,2,2]],-1,1)); rho=[]
    for l in range(L):
        th=F(th); C=np.ones((3,3)); C[0,1]=C[1,0]=np.cos(th[0]); C[1,2]=C[2,1]=np.cos(th[1]); C[0,2]=C[2,0]=np.cos(th[2])
        rho.append(np.linalg.eigvalsh(C)[0]/th.max()**2)
    return C,min(rho)
def bures(G,Cb):
    r=sqrtm(Cb); m=sqrtm(r@G@r).real; return max(np.trace(G)+np.trace(Cb)-2*np.trace(m),0)
rng=np.random.default_rng(seed)
for n in n_list:
    for f in fr:
        L=max(1,int(f*n)); Cb,rho=cbar(L)
        B=[]
        for r in range(R):
            H=rng.standard_normal((n,3))@np.linalg.cholesky(C0+1e-15*np.eye(3)).T   # layer-1 preactivations, input norm 1
            for l in range(L-1):
                P=np.maximum(H,0); W=rng.standard_normal((n,n))*np.sqrt(2/n); H=W@P
            P=np.maximum(H,0) if L>1 else None
            G=(2/n)*P.T@P if L>1 else C0
            dg=np.sqrt(np.diag(G)); Cc=G/np.outer(dg,dg)
            B.append((bures(G,Cb),bures(Cc,Cb),np.sum((dg-1)**2)))
        B=np.array(B); m=B.mean(0); se=B.std(0)/np.sqrt(R)
        print(f"n {n:4d} L {L:4d}: n/L*E[Bures^2(G,Cbar)] {n/L*m[0]:.3f}+-{n/L*se[0]:.3f}  correlation part n/L*E[Bures^2(C,Cbar)] {n/L*m[1]:.4f}+-{n/L*se[1]:.4f}  radial n/L*E sum(r-1)^2 {n/L*m[2]:.3f}  rho_min(Cbar) {rho:.4f}",flush=True)
