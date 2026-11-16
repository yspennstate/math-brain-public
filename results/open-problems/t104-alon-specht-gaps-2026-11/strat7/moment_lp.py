"""NUMERICAL relaxation for discovery of sufficient moment inequalities."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.optimize import linprog

# Affine expressions in nine moment variables and a constant.
A,B,C,d,e,f,h,j,k=np.eye(10)[:9]; one=np.eye(10)[9]
def forms(a,r,N=6):
    b=a*r;s=a+b;lm=(2+s)/4;F=a*(A+C)+b*(B+C)
    K=a*a*A+b*b*B+2*a*b*C-(a*a+b*b)/5*one-a*a*(d+e)-2*a*b*(e+f)-b*b*(f+h)
    R=8/3*a*a*d+8/3*b*b*h+2/3*a*(a+5*b)*e+2/3*b*(b+5*a)*f+2*s*(a*j+b*k)
    T5=(14+2*s)/9*(F-s/5*one)+4/3*(a*a+b*b)*one-14/3*(a*a*A+b*b*B)-4*(a*a+b*b+a*b/3)*C+R
    hh=4/5*one-2/5*s*one+F
    X35=(1-lm)/9*(10*F-2*s*one)
    X3N=(1-lm)/(N-2)**2*((2*(N-1)*(N-4)*lm-4*(N-2))*one+2*N*hh)
    T=T5+(2*N/(N-2)-10/3)*K+X3N-X35
    return T,K,F

def relaxation(a,r,more=True):
    b=a*r;s=a+b;lm=(2+s)/4;T,K,F=forms(a,r)
    con=[]
    def ge(expr):con.append(expr)
    ge(A-7/30*one);ge(B-7/30*one);ge(13/20*one-A);ge(13/20*one-B)
    ge(C);ge(3/10*one-C);ge(A+C-one/4);ge(B+C-one/4)
    ge(4/5*one-A-C);ge(4/5*one-B-C);ge(7/5*one-A-B-2*C);ge(A+B-2*C)
    for z in [d,e,f,h]:ge(z)
    ge(A-one/5-d-e);ge(B-one/5-f-h);ge(C-e-f);ge(K)
    # Cubic moment Gram constraints; t*x + y/t +/- 2z >= 0.
    for t in [1/16,1/8,1/4,1/2,1,2,4,8,16]:
        for sign in [-1,1]:
            ge(t*d+f/t+2*sign*j);ge(t*e+h/t+2*sign*k)
            ge(t*(A-one/5-d-e)+(B-one/5-f-h)/t+2*sign*(C-one/5-j-k))
    ge(A+B+2*C-4/5*one-d-e-f-h-2*j-2*k)
    if more:
        N=a*(d+2*e+f)+b*(e+2*f+h)
        J=a*(d+f+2*j)+b*(e+h+2*k)
        for t in np.linspace(.2,.8,13):
            tangent=2*t*F-s*t*t*one
            ge(N-tangent+lm/5*(2*one-A-B-2*C))
            ge(J-tangent+lm/5*(4*one-A-B-2*C))
        # Separate nonnegative weighted squares u_i^2 u_j^2 and v_i^2 v_j^2.
        for t in np.linspace(.1,.8,15):
            ge(a*d+b*e-(2*t*(a*A+b*C)-s*t*t*one)+lm/5*(one-A))
            ge(a*f+b*h-(2*t*(a*C+b*B)-s*t*t*one)+lm/5*(one-B))
    arr=np.array(con)
    result=linprog(T[:9],A_ub=-arr[:,:9],b_ub=arr[:,9],bounds=[(None,None)]*9,method='highs',options={'threads':1})
    if result.success:return result.fun+T[9],result.x
    return None,None

if __name__=='__main__':
    for r in [0,.05,.1,.2,.4,.6,.8,1]:
        amax=2/(3-r)
        for fraction in [.5,.8,.95,1]:
            a=amax*fraction
            val,x=relaxation(a,r)
            print('NUMERICAL',r,a,val,flush=True)
