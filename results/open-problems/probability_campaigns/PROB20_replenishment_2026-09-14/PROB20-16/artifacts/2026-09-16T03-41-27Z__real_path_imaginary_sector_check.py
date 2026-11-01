#!/usr/bin/env python3
import itertools, math
import numpy as np

SEED = 20260916
NTEST = 2000
rng = np.random.default_rng(SEED)

def atom_probs(K):
    out = {}
    for bits in itertools.product((0,1), repeat=3):
        Q = K.astype(complex).copy()
        holes = [i for i,b in enumerate(bits) if not b]
        for i in holes:
            Q[i,i] -= 1.0
        out[bits] = float((((-1)**len(holes))*np.linalg.det(Q)).real)
    return out

def strict_random_path():
    for _ in range(100000):
        a,b,c = rng.uniform(0.03,0.97,3)
        x,y = rng.uniform(-0.34,0.34,2)
        K = np.array([[a,x,0.0],[x,b,y],[0.0,y,c]], dtype=float)
        if np.linalg.eigvalsh(K)[0] > 1e-5 and np.linalg.eigvalsh(np.eye(3)-K)[0] > 1e-5:
            return K
    raise RuntimeError("failed to sample strict path")

def lam(ps,i,j,k,s):
    def p(ii,jj):
        bits=[0,0,0]; bits[i]=ii; bits[j]=jj; bits[k]=s
        return ps[tuple(bits)]
    return math.log(p(0,1)*p(1,0)/(p(0,0)*p(1,1)))

def tau(ps):
    return math.log(ps[(0,0,0)]*ps[(1,1,0)]*ps[(1,0,1)]*ps[(0,1,1)]/
                    (ps[(1,0,0)]*ps[(0,1,0)]*ps[(0,0,1)]*ps[(1,1,1)]))

def hessian(K,A,B):
    ps=atom_probs(K)
    ans=0.0
    for bits,p in ps.items():
        Q=K.astype(complex).copy()
        for i,b in enumerate(bits):
            if not b:
                Q[i,i] -= 1.0
        R=np.linalg.inv(Q)
        ta=float(np.trace(R@A).real)
        tb=float(np.trace(R@B).real)
        pab=p*(ta*tb-float(np.trace(R@A@R@B).real))
        ans += -(p*ta)*(p*tb)/p - pab*math.log(p)
    return ans

def imag_basis():
    out=[]
    for i,j in ((0,1),(1,2),(2,0)):
        S=np.zeros((3,3))
        S[i,j]=1.0; S[j,i]=-1.0
        out.append(1j*S)
    return out

E=imag_basis()
max_tau_res=0.0
max_formula_res=0.0
min_bracket=float("inf")
max_imag_eig=-float("inf")
min_schur_margin=float("inf")

for _ in range(NTEST):
    K=strict_random_path()
    ps=atom_probs(K)
    tv=tau(ps)
    L12=[lam(ps,0,1,2,s) for s in (0,1)]
    L23=[lam(ps,1,2,0,s) for s in (0,1)]
    L13=[lam(ps,0,2,1,s) for s in (0,1)]
    max_tau_res=max(max_tau_res,
        abs((L12[1]-L12[0])-tv),
        abs((L23[1]-L23[0])-tv),
        abs((L13[1]-L13[0])-tv))
    a,b,c=np.diag(K); x=K[0,1]; y=K[1,2]
    W12=(1-c)*L12[0]+c*L12[1]
    W23=(1-a)*L23[0]+a*L23[1]
    W13=(1-b)*L13[0]+b*L13[1]
    bracket=W13-tv*tv*(y*y/W12+x*x/W23)
    min_bracket=min(min_bracket,bracket)
    if tv >= 0:
        schur = b - x*x/a - y*y/c
    else:
        schur = (1-b) - x*x/(1-a) - y*y/(1-c)
    min_schur_margin=min(min_schur_margin,schur)

    H=np.array([[hessian(K,E[i],E[j]) for j in range(3)] for i in range(3)])
    Hformula=np.array([
        [-2*W12, 0.0, -2*tv*y],
        [0.0, -2*W23, -2*tv*x],
        [-2*tv*y, -2*tv*x, -2*W13]
    ])
    max_formula_res=max(max_formula_res,float(np.max(np.abs(H-Hformula))))
    max_imag_eig=max(max_imag_eig,float(np.linalg.eigvalsh(H)[-1]))

assert max_tau_res < 1e-10
assert max_formula_res < 1e-9
assert min_bracket > 0.0
assert max_imag_eig < 0.0
assert min_schur_margin > 0.0

print("PROB20-16 REAL-PATH IMAGINARY-SECTOR CHECK PASSED")
print("seed =", SEED)
print("tests =", NTEST)
print("max conditional-interaction identity residual =", repr(max_tau_res))
print("max direct-Hessian/cycle-formula residual =", repr(max_formula_res))
print("minimum completed-square bracket =", repr(min_bracket))
print("maximum imaginary-sector Hessian eigenvalue =", repr(max_imag_eig))
print("minimum relevant Schur-complement margin =", repr(min_schur_margin))
