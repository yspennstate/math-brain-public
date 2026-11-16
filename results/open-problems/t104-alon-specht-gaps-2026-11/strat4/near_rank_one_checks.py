"""Numerical checks of the proven perturbation bounds; not their proof."""
import numpy as np,json
from stratum import *
rng=np.random.default_rng(891213)
maxcoef=np.zeros(3);worst=1e9
for k in range(20000):
 U=frame(rng.uniform(-np.pi,np.pi,5));A,B,C,d,e,f,h,*_=moments(U)
 P=2/9*(A+C-.2)+4/3-14*A/3-4*C+8*d*d/3+2*e*e/3+2*d*f
 R=2/9*(B+C-.2)+4/3-14*B/3-4*C+8*h*h/3+2*f*f/3+2*h*e
 Q=2/9*(A+B+2*C-.4)-4*C/3+10*(e*e+f*f)/3+2*d*f+2*h*e
 maxcoef=np.maximum(maxcoef,abs(np.array([P,Q,R])))
 r=10**rng.uniform(-10,np.log10(1/3000));a=tmax(r,U)*rng.uniform(.001,1);b=a*r
 a0=2*a/(2+11*b)
 T=lambda aa,bb:np.dot(closed(aa,bb,U),[1,1,1,-1])
 assert T(a0,0)>=a0/81-2e-15
 assert abs(T(a,b)-T(a0,0))<=34*b+2e-15
 worst=min(worst,T(a,b)/a)
 assert T(a,b)>=2*a/2025-2e-15
print(json.dumps({'samples':20000,'max_absolute_quadratic_coefficients':maxcoef.tolist(),'minimum_T_over_a':worst,'proved_region':'0<b/a<=1/3000'},indent=2))
