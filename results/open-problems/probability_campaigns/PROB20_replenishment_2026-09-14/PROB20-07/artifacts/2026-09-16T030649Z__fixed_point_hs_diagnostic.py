import numpy as np
from scipy.optimize import minimize, root

SEED = 20260916
RNG = np.random.default_rng(SEED)
a = 1.0/12.0
b = 3.0/4.0
pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]

def W(Q, x):
    y = np.zeros(3)
    for r,(i,j) in enumerate(pairs):
        y += (x[i]*x[j]*(1.0 if i == j else 2.0))*Q[r]
    return y

def V(Q, x):
    return a*np.ones(3) + b*W(Q,x)

def Rmat(Q, x):
    R = np.zeros((3,3))
    for j in range(3):
        for i in range(3):
            r = pairs.index((min(i,j),max(i,j)))
            R[j] += x[i]*Q[r]
    return R

def Tmat(Q,x):
    return a*np.ones((3,3)) + b*Rmat(Q,x)

def fixed_point(Q):
    def f(z):
        x = np.array([z[0],z[1],1.0-z[0]-z[1]])
        return V(Q,x)[:2]-x[:2]
    guesses = [np.array([1/3,1/3])]
    guesses += [RNG.dirichlet(np.ones(3))[:2] for _ in range(4)]
    for g in guesses:
        rr = root(f,g)
        if rr.success:
            x = np.array([rr.x[0],rr.x[1],1.0-rr.x.sum()])
            if np.min(x) >= a-1e-8 and np.max(np.abs(V(Q,x)-x)) < 1e-7:
                return x
    return None

def unpack(z):
    Q = z[:18].reshape(6,3)
    x = np.array([z[18],z[19],1.0-z[18]-z[19]])
    return Q,x

def constraints_eq(z):
    Q,x = unpack(z)
    return np.r_[Q.sum(axis=1)-1.0,(V(Q,x)-x)[:2]]

def hs_nontriv(Q,x):
    T = Tmat(Q,x)
    return sum(x[j]*T[j,k]**2/x[k] for j in range(3) for k in range(3))-1.0

def objective(z):
    Q,x = unpack(z)
    return -hs_nontriv(Q,x)

bounds = [(0.0,1.0)]*18 + [(a,1-2*a),(a,1-2*a)]
constraints = [
    {'type':'eq','fun':constraints_eq},
    {'type':'ineq','fun':lambda z: 1.0-a-z[18]-z[19]},
]

best = None
for _ in range(24):
    Q0 = RNG.dirichlet(0.4*np.ones(3),size=6)
    x0 = fixed_point(Q0)
    if x0 is None:
        continue
    z0 = np.r_[Q0.ravel(),x0[:2]]
    res = minimize(objective,z0,method='SLSQP',bounds=bounds,constraints=constraints,
                   options={'maxiter':1400,'ftol':1e-11,'disp':False})
    if res.success and (best is None or res.fun < best.fun):
        best = res

if best is None:
    raise RuntimeError('No successful constrained optimization run')
Q,x = unpack(best.x)
T = Tmat(Q,x)
print('seed',SEED)
print('successful_best_hs',-best.fun)
print('x',repr(x))
print('det_T',np.linalg.det(T))
print('tangent_complex_or_real_eigs',2.0*np.linalg.eigvals(T)[1:])
print('Q_rows')
print(Q)
print('DIAGNOSTIC ONLY: SLSQP is not a universal certificate')
