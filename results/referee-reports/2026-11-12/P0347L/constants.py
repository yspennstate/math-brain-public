"""Limit central moments: cancellation recurrence vs direct formal generator.
Only tiny vectors and a fixed quadrature mesh are allocated (< 2 MB).
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import math,json,time
import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre
mp.mp.dps=55
z=mp.zeta(2)
g=lambda x:(x*mp.log(x)+(1-x)*mp.log1p(-x))/z
A=[mp.mpf(1),mp.mpf(0)]
records=[]
for k in range(2,7):
    terms=[]
    # One canceled linear term, both-daughter cross terms, then c >= 2.
    def integrand(x):
        if x==0 or x==1:return mp.mpf(0)
        y=1-x;v=g(x)
        ans=k*A[k-1]*v*(x**(k-1)+y**(k-1)-1)
        for a in range(2,k-1):
            b=k-a
            if b>=2:ans+=mp.binomial(k,a)*A[a]*A[b]*x**a*y**b
        for a in range(2,k-2):
            b=k-1-a
            if b>=2:ans+=mp.factorial(k)/(mp.factorial(a)*mp.factorial(b))*A[a]*A[b]*x**a*y**b*v
        for c in range(2,k+1):
            for a in range(k-c+1):
                b=k-c-a
                if a==1 or b==1:continue
                ans+=mp.factorial(k)/(mp.factorial(a)*mp.factorial(b)*mp.factorial(c))*A[a]*A[b]*x**a*y**b*v**c
        return ans/(2*x*y)
    val=mp.quad(integrand,[0,mp.mpf('.1'),mp.mpf('.5'),mp.mpf('.9'),1])/mp.harmonic(k-1)
    A.append(val)
    # Independent coefficient extraction from drift + exp(g t) M(xt) M(yt).
    def direct(x):
        if x<=0 or x>=1:return 0.
        y=1-x;v=float(g(mp.mpf(x)));s=0.
        for a in range(k):
            for b in range(k-a):
                c=k-a-b
                if a==1 or b==1:continue
                s+=math.factorial(k)/math.factorial(a)/math.factorial(b)/math.factorial(c)*float(A[a])*float(A[b])*x**a*y**b*v**c
        for a in range(2,k-1):
            b=k-a
            if b>=2:s+=math.comb(k,a)*float(A[a])*float(A[b])*x**a*y**b
        return s/(2*x*y)
    rhs=k*float(A[k-1])+2*quad(direct,0,.5,epsabs=2e-12,epsrel=2e-12,limit=300)[0]
    alt=rhs/float(mp.harmonic(k-1))
    records.append(dict(k=k,a=mp.nstr(val,52),formal_generator_double=alt,difference=abs(alt-float(val))))
    print(k,mp.nstr(val,35), 'difference',abs(alt-float(val)),flush=True)
# A second independent computation uses a vectorized generating polynomial and Gauss-Legendre.
def mesh_constants(nodes,K=24):
    mesh,w=roots_legendre(nodes)
    x=(mesh+1)/2;y=1-x
    w=w/(4*x*y)
    gg=(x*np.log(x)+y*np.log(y))/float(z)
    b=[1.,0.]
    for k in range(2,K+1):
        p=b[k-1]*gg*(x**(k-1)+y**(k-1)-1)
        for a in range(2,k-1):
            d=k-a
            if d>=2:p+=b[a]*b[d]*x**a*y**d
        for a in range(2,k-2):
            d=k-1-a
            if d>=2:p+=b[a]*b[d]*x**a*y**d*gg
        for c in range(2,k+1):
            for a in range(k-c+1):
                d=k-c-a
                if a==1 or d==1:continue
                p+=b[a]*b[d]*x**a*y**d*gg**c/math.factorial(c)
        b.append(float(np.sum(w*p))/sum(1/j for j in range(1,k)))
    return [b[k]*math.factorial(k) for k in range(K+1)]
mesh=mesh_constants(512); mesh2=mesh_constants(1024)
checks={
 'variance_zeta':mp.nstr((2*mp.zeta(3)-z)/z**2,52),
 'third_zeta':mp.nstr(A[2]/z-2*(6*mp.zeta(4)-3*mp.zeta(3)-mp.mpf('1.5')*z)/(3*z**3),52),
 'entropy_integral':mp.nstr(mp.quad(lambda x:-g(x)/(2*x*(1-x)),[0,.5,1]),52),
 'factorial_majorant_constant':1/12+13/24+math.exp(.5)-1-.5,
 'max_mesh_difference_k_le_6':max(abs(mesh2[k]-float(A[k])) for k in range(2,7)),
 'mesh_512_1024_relative_k_le_24':max(abs(mesh[k]-mesh2[k])/max(1,abs(mesh2[k])) for k in range(2,25)),
 'max_abs_a_over_2power_factorial_k_le_24':max(abs(mesh2[k])/(2**k*math.factorial(k)) for k in range(2,25)),
}
json.dump(dict(precision=mp.mp.dps,moments=['1','0']+[mp.nstr(v,52) for v in A[2:]],checks=checks,independent=records,mesh_moments_24=mesh2),open('constants.json','w'),indent=2)
print(json.dumps(checks,indent=2))

assert max(r['difference'] for r in records)<1e-11
assert checks['max_mesh_difference_k_le_6']<1e-9
assert checks['factorial_majorant_constant']<1
assert abs(A[2]-(2*mp.zeta(3)-z)/z**2)<mp.mpf('1e-50')
assert abs(A[3]-(A[2]/z-2*(6*mp.zeta(4)-3*mp.zeta(3)-mp.mpf('1.5')*z)/(3*z**3)))<mp.mpf('1e-50')
