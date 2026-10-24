import math,cmath,json
from pathlib import Path
from scipy.integrate import quad
phase=[]
for m in range(20):
 z=cmath.exp(-1j*math.pi/6)*(1-1j*math.sqrt(3))**(-(3*m+.5))
 rel=abs(z.imag)/abs(z)
 assert rel<1e-12
 phase.append({'m':m,'normalized_imaginary_residual':rel})
t=(math.pi/(6*math.sqrt(3)))**1.5
r=t**(1/3)
# Smooth variable r=|G| avoids the Gamma density singularity at zero.
delta,err=quad(lambda x:-math.sin(math.sqrt(3)/2*x*x-math.pi/6)*math.exp(-x*x/2)/math.sqrt(2*math.pi),0,r,epsabs=1e-13)
norm,ne=quad(lambda x:math.sin(math.sqrt(3)/2*x*x-math.pi/6)*2*math.exp(-x*x/2)/math.sqrt(2*math.pi),0,12,epsabs=1e-12,limit=100)
assert delta>0 and abs(norm)<1e-10
result={'phase_cancellations':phase,'threshold':t,'threshold_probability_discrepancy':delta,'quadrature_error_estimate':err,'mean_h_quadrature':norm,'mean_h_quadrature_error_estimate':ne,'scope':'Scalar moment reduction counterexample only; not an admissible Gaussian vector counterexample.'}
Path('scalar_barrier_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2),flush=True)
