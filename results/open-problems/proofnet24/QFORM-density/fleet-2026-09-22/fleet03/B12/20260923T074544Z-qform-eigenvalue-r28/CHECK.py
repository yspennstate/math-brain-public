import json, math
import numpy as np

rng=np.random.default_rng(20260923074544)

def intersection_construct(H1,H2):
    r=H1.shape[0]
    D=H2-H1
    _,Q=np.linalg.eigh(D)
    u=Q[:,0]; v=Q[:,1]
    a=-H1@u; b=-H2@v
    aQ=Q.T@a; bQ=Q.T@b
    M=np.zeros((r,r))
    for k in range(r):
        M[k,0]=aQ[k]; M[0,k]=aQ[k]
        M[k,1]=bQ[k]; M[1,k]=bQ[k]
    cross=0.5*(aQ[1]+bQ[0])
    M[1,0]=M[0,1]=cross
    Theta=Q@M@Q.T
    return Theta,u,v,abs(aQ[1]-bQ[0])

stats={'intersection_trials':0,'intersection_max_kernel_residual_1':0.0,'intersection_max_kernel_residual_2':0.0,'intersection_max_symmetry_error':0.0,'intersection_max_compatibility_error':0.0}
for r in range(2,7):
    for _ in range(500):
        X=rng.normal(size=(r,r)); H1=(X+X.T)/2
        Y=rng.normal(size=(r,r)); H2=(Y+Y.T)/2
        Th,u,v,comp=intersection_construct(H1,H2)
        stats['intersection_trials']+=1
        stats['intersection_max_kernel_residual_1']=max(stats['intersection_max_kernel_residual_1'],float(np.linalg.norm((Th+H1)@u)))
        stats['intersection_max_kernel_residual_2']=max(stats['intersection_max_kernel_residual_2'],float(np.linalg.norm((Th+H2)@v)))
        stats['intersection_max_symmetry_error']=max(stats['intersection_max_symmetry_error'],float(np.linalg.norm(Th-Th.T,2)))
        stats['intersection_max_compatibility_error']=max(stats['intersection_max_compatibility_error'],float(comp))

anchors=np.array([-2.,0.,2.])
diag=[]
for c in anchors: diag += [c/3,c/3,3.]
A0=np.diag(diag)
V=np.zeros((9,2)); V[[0,3,6],0]=1/np.sqrt(3); V[[1,4,7],1]=1/np.sqrt(3)
cores=[np.array([0,1,2]),np.array([3,4,5]),np.array([6,7,8])]
stats.update({'explicit_trials':0,'V_orthonormality_error':float(np.linalg.norm(V.T@V-np.eye(2),2)),'min_max_unperturbed_core_gap':1e9,'min_max_perturbed_core_gap':1e9,'min_third_largest_eigenvalue':1e9,'explicit_violations':0})
for _ in range(5000):
    X=rng.normal(size=(2,2)); Theta=(X+X.T)/2*(10**rng.uniform(-2,2))
    A=A0+V@Theta@V.T
    gaps=[np.linalg.svd(A[np.ix_(I,I)],compute_uv=False)[-1] for I in cores]
    Y=rng.normal(size=(9,9)); T=(Y+Y.T)/2
    T=T/np.linalg.norm(T,2)*(rng.random()/12)
    Af=A+T
    fgaps=[np.linalg.svd(Af[np.ix_(I,I)],compute_uv=False)[-1] for I in cores]
    eig=np.linalg.eigvalsh(Af)[::-1]
    stats['explicit_trials']+=1
    stats['min_max_unperturbed_core_gap']=min(stats['min_max_unperturbed_core_gap'],float(max(gaps)))
    stats['min_max_perturbed_core_gap']=min(stats['min_max_perturbed_core_gap'],float(max(fgaps)))
    stats['min_third_largest_eigenvalue']=min(stats['min_third_largest_eigenvalue'],float(eig[2]))
    if max(gaps)<1/3-1e-10 or max(fgaps)<1/4-1e-10 or eig[2]<35/12-1e-10:
        stats['explicit_violations']+=1
stats['constants']={'gamma':1/3,'post_tail_gap':1/4,'density_constant_24_sqrt_pi':24*math.sqrt(math.pi),'spectral_target_lower_bound_35_over_12':35/12}
print(json.dumps(stats,indent=2,sort_keys=True))
