"""Three coherent two-site blocks with bridges on different scales; diagnostics only."""
import json,time
from pathlib import Path
import numpy as np
from search_hessian import basis,curvature

def main():
    rng=np.random.default_rng(761709);E=basis(6);best=1e100;records=[];accepted=0;rejected=0;start=time.time()
    for k in range(3000):
        K=np.zeros((6,6),complex)
        for b in range(3):
            Z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));U=np.linalg.qr(Z)[0]
            w=rng.uniform(.12,.88,2);K[2*b:2*b+2,2*b:2*b+2]=(U*w)@U.conj().T
        exponents=rng.permutation([1,2,3]);eps=rng.uniform(.02,.2)
        for (i,j),power in zip([(0,1),(0,2),(1,2)],exponents):
            Z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));Z*=eps**power/np.linalg.norm(Z)
            K[2*i:2*i+2,2*j:2*j+2]=Z;K[2*j:2*j+2,2*i:2*i+2]=Z.conj().T
        spectrum=np.linalg.eigvalsh(K)
        if spectrum[0]<=1e-4 or spectrum[-1]>=1-1e-4:rejected+=1;continue
        Q,p=curvature(K,E);w,V=np.linalg.eigh(Q);val=float(w[0]);accepted+=1
        if val<best:
            best=val;A=np.einsum('a,aij->ij',V[:,0],E)
            records.append(dict(k=k,epsilon=eps,exponents=exponents.tolist(),min_curvature=val,K_real=K.real.tolist(),K_imag=K.imag.tolist(),A_real=A.real.tolist(),A_imag=A.imag.tolist(),kernel_eigenvalues=spectrum.tolist()))
            Path('multiscale_search.json').write_text(json.dumps(dict(accepted=accepted,rejected=rejected,records=records,elapsed=time.time()-start),indent=2))
        if k%500==0:print(json.dumps(dict(k=k,best=best)),flush=True)
    Path('multiscale_search.json').write_text(json.dumps(dict(accepted=accepted,rejected=rejected,records=records,elapsed=time.time()-start),indent=2))
    print(json.dumps(dict(accepted=accepted,rejected=rejected,best=best,elapsed=time.time()-start)),flush=True)

if __name__=='__main__':main()
