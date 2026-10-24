import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json, math
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import mpmath as mp

rng=np.random.default_rng(10902)
out={'scope':'Finite/algebraic auxiliary checks only; does not certify the stochastic upper-rate theorem.'}

# Exact exponent balancing, including the saturation used for eps>1.
exponents=[]
for e in [F(1,100),F(1,10),F(1,4),F(1,2),F(2,3),F(1)]:
 p=2+e; g=e/(2*(p+1)); b=g/2
 assert e/2-p*g==g and g-b==b and g< F(1,2)
 assert F(1,4)-b>b
 exponents.append({'e':str(e),'gamma':str(g),'beta':str(b)})
out['rational_exponents']=exponents

# Row-rank interlacing for clipped logs and V_eta, including huge rows.
rows=[]
for n in [2,5,12]:
 for eta in [.03,.2,1.]:
  for scale in [1.,1000.]:
   a=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/math.sqrt(2*n)
   b=a.copy(); b[0]=scale*(rng.normal(size=n)+1j*rng.normal(size=n))
   sa=np.linalg.svd(a,compute_uv=False); sb=np.linalg.svd(b,compute_uv=False)
   va=np.mean(eta**2/(sa**2+eta**2)); vb=np.mean(eta**2/(sb**2+eta**2))
   assert abs(va-vb)<=1/n+1e-12
   L=2.
   fa=np.mean(np.minimum(.5*np.log(sa*sa+eta*eta),.5*math.log(L*L+eta*eta)))
   fb=np.mean(np.minimum(.5*np.log(sb*sb+eta*eta),.5*math.log(L*L+eta*eta)))
   cap=.5*math.log((L*L+eta*eta)/(eta*eta))/n
   assert abs(fa-fb)<=cap+1e-12
   rows.append({'n':n,'eta':eta,'scale':scale,'V_change':float(abs(va-vb)),'V_bound':1/n,'log_change':float(abs(fa-fb)),'log_bound':cap})
out['row_replacement_18_cases']=rows

# Complex projection with real Gaussian noise: inspect eigenvalues of Re P,
# then test conditional inverse-distance bounds, with translated centers.
proj=[]
n=16; d=5; v=.5
q,_=np.linalg.qr(rng.normal(size=(n,d))+1j*rng.normal(size=(n,d)))
P=q@q.conj().T
eig=np.linalg.eigvalsh(P.real)
assert eig.min()>-1e-12 and eig.max()<1+1e-12 and abs(eig.sum()-d)<1e-12
samples=rng.normal(size=(12000,n))*math.sqrt(v/n)
for scale in [0.,.2,1.]:
 center=scale*(rng.normal(size=n)+1j*rng.normal(size=n))
 norms=np.sum(abs((samples+center)@P.T)**2,axis=1)
 inv=float(np.mean(1/norms)); bound=n/(v*(d-2))
 assert inv<bound
 proj.append({'center_scale':scale,'inverse_distance_mean':inv,'theoretical_bound':bound})
out['complex_projection_real_noise']={'real_projection_trace':float(eig.sum()),'real_projection_eigen_min':float(eig.min()),'real_projection_eigen_max':float(eig.max()),'samples':12000,'cases':proj}

# Verify dilation derivative trace formulas against high-precision differentiation.
mp.mp.dps=45
n=3; eta=mp.mpf('0.17')
ar=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
ar/=math.sqrt(2*n)
H=mp.matrix(2*n); E=mp.matrix(2*n)
for i in range(n):
 for j in range(n):
  z=mp.mpc(float(ar[i,j].real),float(ar[i,j].imag))
  H[i,n+j]=z; H[n+j,i]=mp.conj(z)
direction=mp.mpc('0.7','-0.4')/mp.sqrt(n)
E[1,n+2]=direction; E[n+2,1]=mp.conj(direction)
I=mp.eye(2*n)
trace=lambda a:sum(a[i,i] for i in range(a.rows))
def f(t): return mp.log(abs(mp.det(H+t*E-1j*eta*I)))/(2*n)
def w(t): return eta*mp.im(trace((H+t*E-1j*eta*I)**-1))/(2*n)
R=(H-1j*eta*I)**-1
der=[]
for k in [1,2,3]:
 exactF=((-1)**(k-1))*mp.factorial(k-1)*mp.re(trace((R*E)**k))/(2*n)
 exactV=eta*((-1)**k)*mp.factorial(k)*mp.im(trace((R*E)**k*R))/(2*n)
 errF=abs(mp.diff(f,0,k)-exactF); errV=abs(mp.diff(w,0,k)-exactV)
 assert errF<mp.mpf('1e-35') and errV<mp.mpf('1e-35')
 der.append({'order':k,'F_residual':str(errF),'V_residual':str(errV)})
out['dilation_derivative_formulas']=der

# The scalar regularization inequality used to avoid a second cutoff.
maxratio=0.
for x in np.logspace(-12,12,1201):
 lhs=math.log1p(float(x)); rhs=(1+math.log1p(float(x)))*x/(1+x)
 assert lhs<=rhs+1e-12*max(1,lhs)
 maxratio=max(maxratio,lhs/rhs)
out['regularization_scalar_1201_cases']={'max_lhs_rhs_ratio':maxratio}
out['memory']='Largest sample array 12000x16; working arrays well below 1 GB. Jobs use one BLAS thread.'
Path('direct_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print('All auxiliary checks passed: exponent identities, 18 row replacements, complex Gaussian projections, six derivative identities, 1201 scalar inequalities.')
