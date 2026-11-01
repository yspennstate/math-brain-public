import math
import numpy as np
from math import comb, factorial
from scipy.optimize import root

GAMMA = 4.4898
M = 23

# Pure-literal core parameter from Diaz et al.
def root_eq(q):
    return q - (1.0 - math.exp(-1.5 * GAMMA * q * q))
lo, hi = 0.9, 1.0
for _ in range(200):
    mid = (lo + hi) / 2
    if root_eq(lo) * root_eq(mid) <= 0:
        hi = mid
    else:
        lo = mid
q = (lo + hi) / 2
a = 1.5 * GAMMA * q * q

def delta_b(i, j):
    if i < j or j < 1:
        return 0.0
    return math.exp(-2*a + (i+j)*math.log(a) - math.lgamma(i+1) - math.lgamma(j+1)) * (2.0 if i > j else 1.0)

# Summation tail is far below displayed precision by 100 for a~6.72.
lambda_p = 0.0
lambda_n = 0.0
for i in range(1, 100):
    for j in range(1, i+1):
        d = delta_b(i, j)
        lambda_p += i*d
        lambda_n += j*d
gamma_b = (lambda_p + lambda_n) / 3.0

light = []
light_p = 0.0
light_n = 0.0
for i in range(1, M+1):
    for j in range(1, i+1):
        d = delta_b(i, j)
        light.append((i,j,d))
        light_p += i*d
        light_n += j*d
h_ps = lambda_p - light_p
h_ns = lambda_n - light_n

gamma_k = [comb(3,k)*lambda_p**k*lambda_n**(3-k)/(lambda_p+lambda_n)**3*gamma_b for k in range(4)]

def clause_states(K):
    out = []
    for ps in range(4):
        for ns in range(4-ps):
            for pu in range(4-ps-ns):
                nu = 3-ps-ns-pu
                if ps + ns < 1 or ps + pu != K:
                    continue
                ns1 = ns if ps + ns == 1 else 0
                ns2 = 0 if ps + ns == 1 else ns
                zeros = sum(int(x == 0) for x in (ps,ns,pu,nu))
                out.append((ps,ns1,ns2,2.0/factorial(zeros)))
    return out
CSTATES = [clause_states(k) for k in range(4)]

def variable_mean_cov(nu):
    nps,n1,n2 = nu
    mean = np.array([h_ps,0.0,0.0])
    cov = np.zeros((3,3))
    for i,j,d in light:
        weights = [nps**i]
        states = [np.array([float(i),0.0,0.0])]
        for k in range(1,j+1):
            weights.append(comb(j,k)*n1**k*n2**(j-k))
            states.append(np.array([0.0,float(k),float(j-k)]))
        p = np.array(weights,dtype=float)
        p /= p.sum()
        Y = np.stack(states)
        m = (p[:,None]*Y).sum(axis=0)
        mean += d*m
        cov += d*(p[:,None,None]*(Y-m)[:,:,None]*(Y-m)[:,None,:]).sum(axis=0)
    p1 = n1/(n1+n2)
    mean += np.array([0.0,h_ns*p1,h_ns*(1-p1)])
    s = p1*(1-p1)
    hc = np.zeros((3,3))
    hc[1,1] = hc[2,2] = s
    hc[1,2] = hc[2,1] = -s
    cov += h_ns*hc
    return mean,cov

def clause_mean_cov(mu):
    mps,m1,m2 = mu
    mean = np.zeros(3)
    cov = np.zeros((3,3))
    for K in range(4):
        states=[]
        weights=[]
        for ps,ns1,ns2,base in CSTATES[K]:
            states.append(np.array([float(ps),float(ns1),float(ns2)]))
            weights.append(base*mps**ps*m1**ns1*m2**ns2)
        p=np.array(weights,dtype=float)
        p/=p.sum()
        Y=np.stack(states)
        m=(p[:,None]*Y).sum(axis=0)
        mean += gamma_k[K]*m
        cov += gamma_k[K]*(p[:,None,None]*(Y-m)[:,:,None]*(Y-m)[:,None,:]).sum(axis=0)
    return mean,cov

def copy_y(nu,mu):
    nps,n1,n2=nu
    mps,m1,m2=mu
    dp=1+nps*mps
    dn=1+n1*m1+n2*m2
    return np.array([
        lambda_p*nps*mps/dp,
        lambda_n*n1*m1/dn,
        lambda_n*n2*m2/dn,
    ])

def stationarity(logx):
    x=np.exp(logx)
    nu=x[:3]
    mu=x[3:]
    y=copy_y(nu,mu)
    return np.r_[variable_mean_cov(nu)[0]-y, clause_mean_cov(mu)[0]-y]

x0=np.log([1.2782018,0.33277280,0.95336927,1.9972796,0.45029358,0.33794030])
sol=root(stationarity,x0,method='hybr',tol=1e-12)
assert sol.success
x=np.exp(sol.x)
nu=x[:3]
mu=x[3:]
y=copy_y(nu,mu)
vm,SV=variable_mean_cov(nu)
cm,SC=clause_mean_cov(mu)
u,v,w=y
ell_nu=lambda_n-v-w
Hcopy=np.array([
    [1/u+1/(lambda_p-u),0.0,0.0],
    [0.0,1/v+1/ell_nu,1/ell_nu],
    [0.0,1/ell_nu,1/w+1/ell_nu],
])
Hout=Hcopy-np.linalg.inv(SV)-np.linalg.inv(SC)
eigs=np.linalg.eigvalsh(Hout)
minusH=-Hout
minors=[np.linalg.det(minusH[:k,:k]) for k in (1,2,3)]

# Exact finite sanity check for the closed-form variable support oracle.
dirs=[(aa,bb,cc) for aa in range(-2,3) for bb in range(-2,3) for cc in range(-2,3) if (aa,bb,cc)!=(0,0,0)]
block_checks=0
for aa,bb,cc in dirs:
    for i in range(1,M+1):
        for j in range(1,i+1):
            explicit=max([aa*i]+[bb*k+cc*(j-k) for k in range(1,j+1)])
            false_closed=(bb*j if bb>=cc else bb+cc*(j-1))
            closed=max(aa*i,false_closed)
            assert explicit==closed
            block_checks += 1

print('OUTER_COVARIANCE_COMPENSATION_DIAGNOSTIC')
print('NUMERICAL_HESSIAN_DIAGNOSTIC_ONLY_NOT_INTERVAL_ENDPOINT')
print(f'gamma = {GAMMA:.16g}')
print(f'q = {q:.16g}')
print(f'lambda_p = {lambda_p:.16g}')
print(f'lambda_n = {lambda_n:.16g}')
print(f'gamma_b = {gamma_b:.16g}')
print(f'h_ps = {h_ps:.16g}')
print(f'h_ns = {h_ns:.16g}')
print('solved multipliers nu_ps nu_ns1 nu_ns2 mu_ps mu_ns1 mu_ns2 =')
print('  '+' '.join(f'{z:.16g}' for z in x))
print(f'stationarity_residual_inf = {np.linalg.norm(stationarity(sol.x),np.inf):.16g}')
print('copy macrostate u v w =')
print('  '+' '.join(f'{z:.16g}' for z in y))
print('Sigma_V =')
for row in SV: print('  '+' '.join(f'{z:.16g}' for z in row))
print('Sigma_C =')
for row in SC: print('  '+' '.join(f'{z:.16g}' for z in row))
print('H_out = H_copy - inv(Sigma_V) - inv(Sigma_C) =')
for row in Hout: print('  '+' '.join(f'{z:.16g}' for z in row))
print('eig(H_out) = '+' '.join(f'{z:.16g}' for z in eigs))
print('leading_principal_minors(-H_out) = '+' '.join(f'{z:.16g}' for z in minors))
print(f'rounded_local_concavity_margin = {-eigs[-1]:.16g}')
print(f'EXACT_VARIABLE_SUPPORT_BLOCK_CHECKS = {block_checks}')
print(f'CLAUSE_EXTENDED_TYPES = {sum(len(s) for s in CSTATES)}')
print('EXACT_SUPPORT_BLOCK_CHECKS_PASS = True')
print('NUMERICAL_NEGATIVE_DEFINITE_AT_SOLVED_SADDLE =', bool(np.all(eigs<0)))
print('DIAGNOSTIC_COMPLETE = True')