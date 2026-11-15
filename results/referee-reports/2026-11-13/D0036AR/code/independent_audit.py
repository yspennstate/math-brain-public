#!/usr/bin/env python3
"""Independent finite-window canonical correlations and explicit witnesses.
No claim_files code is read or imported. BLAS is restricted before imports.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:
    os.nice(10-os.getpriority(os.PRIO_PROCESS,0))
import csv, json, time, resource, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigh, cholesky, solve_triangular, svdvals
from scipy.integrate import quad
from scipy.signal import fftconvolve
from scipy.special import gammaln
ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic()
CHECKS=[]
def cov_power(beta,k):
    """Fourier coefficient / zero-lag coefficient of |1-e^{it}|**beta."""
    k=np.abs(np.asarray(k,dtype=int))
    result=np.ones(int(np.max(k))+1)
    for j in range(1,len(result)):
        result[j]=result[j-1]*(j-1-beta/2)/(j+beta/2)
    return result[k]
def cov_model(beta,k,kind='power',theta=0.):
    k=np.asarray(k,dtype=int)
    if kind=='twozero':
        def h(j):return (-1.)**j*cov_power(beta,j)
        out=2*h(k)-h(k-1)-h(k+1)
        norm=2-2*float(h(np.array(1)))
        out=out/norm
    elif kind=='ar_difference':
        a=.7
        h=lambda j:a**np.abs(j)
        out=(2*h(k)-h(k-1)-h(k+1))/(2-2*a)
    else:
        out=cov_power(beta,k)
    return out*np.exp(1j*k*theta) if theta else out

def matrices(beta,S,T,kind='power',theta=0.):
    S=np.asarray(S);T=np.asarray(T)
    return (cov_model(beta,S[:,None]-S,kind,theta),
            cov_model(beta,T[:,None]-T,kind,theta),
            cov_model(beta,S[:,None]-T,kind,theta))

def canonical(beta,S,T,kind='power',theta=0.,crosscheck=False):
    A,B,C=matrices(beta,S,T,kind,theta)
    a,b=len(S),len(T); d=a+b
    H=np.zeros((d,d),dtype=C.dtype);D=np.zeros_like(H)
    H[:a,a:]=C;H[a:,:a]=C.conj().T
    D[:a,:a]=A;D[a:,a:]=B
    vals,vec=eigh(H,D,subset_by_index=[d-1,d-1],check_finite=True,driver='gvx')
    rho=float(vals[0]);v=vec[:,0]
    Hv=np.einsum('ij,j->i',H,v);Dv=np.einsum('ij,j->i',D,v)
    residual=np.linalg.norm(Hv-rho*Dv)/(np.linalg.norm(Hv)+np.linalg.norm(Dv)+1e-300)
    min_eig=min(float(eigh(A,subset_by_index=[0,0],eigvals_only=True)[0]),float(eigh(B,subset_by_index=[0,0],eigvals_only=True)[0]))
    if rho>1+1e-5 or rho< -1e-9:raise ArithmeticError((beta,rho,min_eig))
    if crosscheck:
        LA=cholesky(A,lower=True);LB=cholesky(B,lower=True)
        W=solve_triangular(LA,C,lower=True)
        W=solve_triangular(LB,W.conj().T,lower=True).conj().T
        CHECKS.append(dict(check='eigen_vs_cholesky_svd',beta=beta,error=abs(rho-float(svdvals(W)[0]))))
    return rho,residual,min_eig

def supports(W,n,width):
    S=[];T=[];cursor=0;side=0
    while cursor<W:
        block=list(range(cursor,min(W,cursor+width)))
        (S if side==0 else T).extend(block)
        cursor+=width+n-1;side=1-side
    return S,T

def write_csv(name,rows):
    with (ROOT/'data'/name).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)

rows=[]
models=[('power',b) for b in [.2,.5,1.,1.9,2.,2.1,3.,3.9,4.,4.1]]
models += [('twozero',b) for b in [1.,2.,2.1]]+[('ar_difference',2.)]
for kind,beta in models:
    for W in [64,128,256]:
        for n in [1,2,4,8,16]:
            L=(W-n+1)//2
            families=[('blocks',list(range(L)),list(range(L+n-1,2*L+n-1)))]
            families += [(f'runs{width}',*supports(W,n,width)) for width in [1,4,16]]
            for family,S,T in families:
                if not S or not T:continue
                assert min(abs(s-t) for s in S for t in T)>=n
                rho,resid,mineig=canonical(beta,S,T,kind,crosscheck=(W==64 and n==4))
                rows.append(dict(model=kind,beta=beta,window=W,gap=n,family=family,nS=len(S),nT=len(T),rho=rho,residual=resid,min_within_eigenvalue=mineig))
write_csv('canonical_correlations.csv',rows)
# A shifted zero forces the complex Hermitian conventions to be exercised.
S,T=supports(90,3,4)
r0=canonical(.5,S,T)[0];r1=canonical(.5,S,T,theta=.73,crosscheck=True)[0]
CHECKS.append(dict(check='complex_modulation_invariance',beta=.5,error=abs(r0-r1)))
# Independent quadrature of the spectral density checks the recurrence and normalization.
for beta in [.2,.5,1.,1.9,2.,2.1,3.,4.,4.1]:
    normal=quad(lambda t:abs(1-np.exp(1j*t))**beta,0,np.pi,epsabs=1e-11)[0]/np.pi
    for k in [0,1,2,7,20]:
        integral=quad(lambda t:abs(1-np.exp(1j*t))**beta*np.cos(k*t),0,np.pi,epsabs=1e-11)[0]/(np.pi*normal)
        CHECKS.append(dict(check=f'fourier_quadrature_lag{k}',beta=beta,error=abs(integral-float(cov_power(beta,np.array(k))))))
# Equal-block cusp witnesses from a covariance multiplicity sum, and separately
# harmonic variances. No large dense matrix is allocated.
block_rows=[]
V=lambda L:float(np.sum(1/(2*np.arange(1,L+1,dtype=float)-1)))
for L in [32,128,512,2048,8192,32768,131072,524288]:
    variance=V(L)
    for n in [1,2,8,32,128]:
        h=np.arange(n,2*L+n-1,dtype=float)
        weights=L-np.abs(h-(L+n-1))
        cross=float(np.sum(weights/(1-4*h*h)))
        block_rows.append(dict(length=L,gap=n,correlation=abs(cross)/variance,variance=variance))
        if n==1:
            CHECKS.append(dict(check=f'cusp_variance_identity_L{L}',beta=1,error=abs(cross-(V(2*L)-2*variance)/2)))
write_csv('cusp_block_witnesses.csv',block_rows)
# Smooth disjoint test arrays: phi on (0,1), psi on (2,3). Stable O(L log L)
# spectral quadrature with zero-padded FFTs avoids cancellation in tiny norms.
witness_rows=[]
for beta in [.2,.5,1.,1.9,2.,2.1,3.,3.9,4.,4.1]:
    for L in [32,128,512,2048,8192]:
        u=np.arange(1,L)/L
        phi=np.exp(-1/(u*(1-u)))
        phi=phi/phi.max()
        N=4*L
        aa=np.zeros(N);bb=np.zeros(N)
        aa[1:L]=phi;bb[2*L+1:3*L]=phi
        M=64*N
        frequency=2*np.pi*np.fft.fftfreq(M)
        density=np.abs(1-np.exp(1j*frequency))**beta
        FA=np.fft.fft(aa,n=M);FB=np.fft.fft(bb,n=M)
        va=float(np.sum(density*np.abs(FA)**2)/M)
        vb=float(np.sum(density*np.abs(FB)**2)/M)
        spectral_cross=float(np.sum(density*FA*np.conj(FB)).real/M)
        weights=fftconvolve(phi,phi[::-1])
        lags=2*L+np.arange(-(len(phi)-1),len(phi))
        raw_scale=np.exp(gammaln(beta+1)-2*gammaln(beta/2+1))
        cross=float(np.sum(weights*cov_power(beta,lags))*raw_scale)
        witness_rows.append(dict(beta=beta,L=L,gap=L+2,correlation=abs(cross)/np.sqrt(va*vb),variance=va,scaled_variance=va*L**(beta-1),spectral_cross_discrepancy=abs(cross-spectral_cross)))
write_csv('smooth_witnesses.csv',witness_rows)
# Taper far endpoints to remove the extra boundary contribution of flat blocks.
taper_rows=[]
for L in [32,128,512,2048,8192,32768]:
    aa=np.arange(1,L+1,dtype=float)/L
    N=4*L+128;M=1<<(32*N-1).bit_length()
    freq=2*np.pi*np.fft.fftfreq(M)
    density=np.pi/4*np.abs(1-np.exp(1j*freq))
    a=np.zeros(N);a[:L]=aa
    FA=np.fft.fft(a,n=M)
    va=float(np.sum(density*np.abs(FA)**2)/M)
    for gap in [1,2,8,32,128]:
        b=np.zeros(N);b[L+gap-1:2*L+gap-1]=aa[::-1]
        FB=np.fft.fft(b,n=M)
        vb=float(np.sum(density*np.abs(FB)**2)/M)
        cross=float(np.sum(density*FA*np.conj(FB)).real/M)
        taper_rows.append(dict(L=L,gap=gap,correlation=abs(cross)/np.sqrt(va*vb),variance=va,sum_variance=va+vb+2*cross))
write_csv('cusp_taper_witnesses.csv',taper_rows)

# Difference checkerboards have exact correlation cos(pi/(W+1)).
for W in [16,64,128]:
    rho=canonical(2.,list(range(0,W,2)),list(range(1,W,2)))[0]
    CHECKS.append(dict(check=f'difference_checkerboard_W{W}',beta=2.,error=abs(rho-np.cos(np.pi/(W+1)))))
write_csv('checks.csv',CHECKS)
# Maxima only over the named sampled families, never a full supremum.
maxima=[]
for kind,beta in models:
    for W in [64,128,256]:
        item=dict(model=kind,beta=beta,window=W)
        for n in [1,2,4,8,16]:
            item[f'gap{n}']=max(r['rho'] for r in rows if r['model']==kind and r['beta']==beta and r['window']==W and r['gap']==n)
        maxima.append(item)
write_csv('sampled_maxima.csv',maxima)
metadata=dict(nice=os.getpriority(os.PRIO_PROCESS,0),threads={k:os.environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']},numpy=np.__version__,scipy=scipy.__version__,python=platform.python_version(),elapsed_seconds=time.monotonic()-START,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,correlations=len(rows),checks=len(CHECKS),max_check_error=max(c['error'] for c in CHECKS),max_generalized_eigen_residual=max(r['residual'] for r in rows))
(ROOT/'data'/'run_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps(metadata,indent=2))
print('W=256 sampled maxima:')
for r in maxima:
    if r['window']==256:print(r)
