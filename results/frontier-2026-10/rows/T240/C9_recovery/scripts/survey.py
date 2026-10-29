import sys; sys.path.insert(0,'.')
import numpy as np, scm_plateau as sp
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
eta=0.5
f=lambda z: sp.rhs(z,eta)
x0=np.array([0.36771969907760643,0.32538554792403124,0.36771969907760643]+[0.4143941508524791]*4)
xs=fsolve(f,x0,xtol=1e-14); print('plateau',xs,'|f|',np.abs(f(xs)).max())
def jac(x,h=1e-7):
    J=np.zeros((7,7))
    for k in range(7):
        d=np.zeros(7);d[k]=h;J[:,k]=(f(x+d)-f(x-d))/(2*h)
    return J
J=jac(xs); w,V=np.linalg.eig(J); o=np.argsort(-w.real); w=w[o]; V=V[:,o]
print('plateau eig',np.round(w,6))
eu=np.real(V[:,0]); eu/=np.linalg.norm(eu); print('e_u',np.round(eu,4))
tp=np.array([1,0,1,1,0,0,1.]); print('teacher |f|',np.abs(f(tp)).max())
wt=np.linalg.eigvals(jac(tp)); print('teacher eig',np.round(np.sort_complex(wt),5))
for sgn in (1,-1):
    sol=solve_ivp(lambda t,y:f(y),(0,3000),xs+sgn*1e-6*eu,method='DOP853',rtol=1e-11,atol=1e-13,dense_output=True)
    for t in (0,200,400,500,600,800,1000,1500,2000,3000):
        y=sol.sol(t); print(sgn,t,np.round(y,5), 'V',round(min(y[0]+y[2]+2-2*y[3]-2*y[6], y[0]+y[2]+2-2*y[4]-2*y[5]),9))
