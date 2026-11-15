"""Audit Perron/variance constants by two independent Gaussian integrations."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import json,math,pathlib
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_hermitenorm
ROOT=pathlib.Path(__file__).resolve().parents[1]
MEANS=np.array([-.8,.8])
def p(x): return .55+.15*np.tanh(x)
def w(x):
    x=np.asarray(x);w1=.5+.2*np.tanh(x)
    return np.stack([w1,1-w1],axis=-1)

def calculate(method):
    if method=='gauss_hermite_160':
        z,v=roots_hermitenorm(160);v=v/math.sqrt(2*math.pi)
        def expect(i,f): return float(v@f(MEANS[i]+z))
    else:
        def expect(i,f):
            return quad(lambda x:float(f(x))*math.exp(-.5*(x-MEANS[i])**2)/math.sqrt(2*math.pi),-math.inf,math.inf,epsabs=2e-12,epsrel=2e-12)[0]
    c=np.array([expect(i,p) for i in range(2)])
    A=np.array([[c[j]*expect(i,lambda x,j=j:p(x)*w(x)[...,j])/c[i] for j in range(2)] for i in range(2)])
    lam,vec=np.linalg.eig(A);index=int(np.argmax(lam.real));rho=float(lam[index].real);nu=1/rho;M=nu*A
    vals,leftvec=np.linalg.eig(M.T);a=leftvec[:,int(np.argmin(abs(vals-1)))].real
    a=a/a.sum();b=vec[:,index].real;b=b/(a@b)
    assert np.all(a>0) and np.all(b>0)
    def h(x): return nu*(w(x)@(c*b))
    def ell(f): return sum(a[i]*expect(i,lambda x:p(x)*f(x))/c[i] for i in range(2))
    def m(x): return nu*(w(x)@c)
    eh=ell(h);h2=ell(lambda x:h(x)**2)
    spine_count_mean=ell(lambda x:h(x)*m(x))
    spine_count_second=ell(lambda x:h(x)*(m(x)+m(x)**2))
    offvar=spine_count_second-spine_count_mean**2
    # Independent finite-vector factorial-moment summation.
    Q=np.empty((2,2,2))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                Q[i,j,k]=nu**2*c[j]*c[k]*expect(i,lambda x,j=j,k=k:p(x)*w(x)[...,j]*w(x)[...,k])/c[i]
    sigma2=float(np.einsum('i,j,k,ijk',a,b,b,Q))
    assert abs(sigma2-h2)<3e-12 and abs(eh-1)<3e-12
    # Explicit Doeblin constant using the first mixture component.
    hmax=nu*max(c*b)
    minorisation=nu*.3*c[0]*b[0]/hmax
    return {'integration':method,'c':c.tolist(),'nu':nu,'M':M.tolist(),'a':a.tolist(),'b':b.tolist(),
            'h_mean':eh,'sigma2_continuous':h2,'sigma2_finite_factorial':sigma2,
            'Sigma_c':math.sqrt(sigma2)/2,'spine_mean_ordinary_count':spine_count_mean,
            'sigma2_off_spine_mixture':offvar,'incorrect_raw_variance_scale':math.sqrt(offvar)/2,
            'Doeblin_lower_bound':minorisation,'spectral_residual':float(np.max(abs(M@b-b)))}

if __name__=='__main__':
    a=calculate('gauss_hermite_160');b=calculate('adaptive_quad')
    diffs={key:abs(a[key]-b[key]) for key in ('nu','sigma2_continuous','sigma2_finite_factorial','Sigma_c','spine_mean_ordinary_count','sigma2_off_spine_mixture')}
    assert max(diffs.values())<2e-10,diffs
    out={'definition':'q_j=N((-0.8,0.8)_j,1); w_1(a)=0.5+0.2tanh(a); p(a)=0.55+0.15tanh(a); D=Poisson(nu)','runs':[a,b],'absolute_discrepancies':diffs}
    (ROOT/'data/finite_mixture_constants.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
