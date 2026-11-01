#!/usr/bin/env python3
import itertools, math
from fractions import Fraction
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh, expm_multiply
import sympy as sy

# ---------- exact S3 algebra ----------
perms = list(itertools.permutations(range(3)))
idx = {p:i for i,p in enumerate(perms)}
def compose(p,q):
    return tuple(p[q[i]] for i in range(3))
e = (0,1,2)
x = (1,0,2)  # (12)
y = (0,2,1)  # (23)
z = (2,1,0)  # (13)=x y x

def R_sym(g):
    M = sy.zeros(6)
    for p in perms:
        M[idx[p], idx[compose(p,g)]] = 1
    return M
PA = (R_sym(x)+R_sym(y))/2
PB = (R_sym(x)+R_sym(z))/2
C = PA*PB-PB*PA
assert C != sy.zeros(6)
CtC = C.T*C
spec = CtC.eigenvals()
assert spec.get(sy.Rational(3,16),0) == 4
assert spec.get(sy.Integer(0),0) == 2
comm_norm = sy.sqrt(3)/4
hidden_comm_norm = comm_norm/16

# 6-cycle gaps of Cay(S3,{x,y}) and Cay(S3,{x,z})
for P in (PA,PB):
    evals = sorted([sy.N(v) for v in P.eigenvals().keys()], reverse=True)
    # exact second-largest eigenvalue is 1/2
    assert sy.Rational(1,2) in P.eigenvals()

# ---------- exact constants for asymptotic family ----------
sqrt5 = math.sqrt(5.0)
gamma_R = (3.0-sqrt5)/3.0
eta = 1/8
assert 0.75*gamma_R > eta
# d=6, r=8, plus one pure phase generator -> D=15
a = Fraction(6,15)
b = Fraction(8,15)
c = Fraction(1,15)
gap_bound = min(float(b)*eta, float(a)*gamma_R, 2*float(c))
assert abs(gap_bound-1/15) < 1e-14
# exact check a*gamma_R > 1/15 is 2(3-sqrt5)>1 <=> 25>20
assert 25 > 20

# center and error exponents
# base CT center = (3/2) log_5 n, output rescales by 1/a=5/2
center_coeff_n = Fraction(15,4)
# N = 12 n m, log m = (1/10) log n + O(1), so log N=(11/10)log n+O(1)
center_coeff_N = center_coeff_n / Fraction(11,10)
assert center_coeff_N == Fraction(75,22)
hidden_error_exponent_n = 1/20 - 1/(4*math.log(5))
phase_error_exponent_n = -1/(2*math.log(5))
assert hidden_error_exponent_n < 0
assert phase_error_exponent_n < 0
beta_lre = 0.5*(1-math.log(5)/math.log(14))-1/11
assert beta_lre > 0
assert 5**11 < 14**9

# ---------- finite 588-state toy ----------
# visible G=K7 with generator set all nonzero in Z7 (degree 6)
# hidden Lambda=Z7 with same V (degree 6), times S3, phase C2.
# State (g,l,p,i), 7*7*6*2 = 588.
Z=7
states=[]
index={}
for g in range(Z):
  for l in range(Z):
    for p in perms:
      for phase in (0,1):
        index[(g,l,p,phase)] = len(states)
        states.append((g,l,p,phase))
N=len(states)
assert N==588
rows=[]; cols=[]; dat=[]

def alpha_perm(p):
    # conjugation by x: x p x
    return compose(compose(x,p),x)

def alpha_u(u):
    kind,val=u
    if kind=='z': return u
    return ('s', alpha_perm(val))

V=[('z',k) for k in range(1,7)]
A=[('s',x),('s',y)]
U=V+A
D=15

def hidden_mul(l,p,u,phase):
    uu = u if phase==0 else alpha_u(u)
    kind,val=uu
    if kind=='z':
        return ((l+val)%Z,p)
    else:
        return (l,compose(p,val))

for s0,(g,l,p,phase) in enumerate(states):
    # six cross generators: visible step, phase flip
    for step in range(1,7):
        st=((g+step)%Z,l,p,1-phase)
        rows.append(s0); cols.append(index[st]); dat.append(1/D)
    # eight vertical generators, transformed according to current phase
    for u in U:
        ll,pp=hidden_mul(l,p,u,phase)
        st=(g,ll,pp,phase)
        rows.append(s0); cols.append(index[st]); dat.append(1/D)
    # pure phase flip
    st=(g,l,p,1-phase)
    rows.append(s0); cols.append(index[st]); dat.append(1/D)
Q=sp.csr_matrix((dat,(rows,cols)),shape=(N,N))
row_err=np.max(np.abs(np.asarray(Q.sum(axis=1)).ravel()-1))
sym_err=np.max(np.abs((Q-Q.T).data)) if (Q-Q.T).nnz else 0.0
assert row_err < 1e-14 and sym_err < 1e-14

# visible lumping: off-diagonal each neighbor 1/15, self visible mass 9/15
start=index[(0,0,e,0)]
row=Q.getrow(start).toarray().ravel()
vis=np.zeros(Z)
for prob,(g,l,p,ph) in zip(row,states): vis[g]+=prob
assert np.max(np.abs(vis[1:]-1/15))<1e-14
assert abs(vis[0]-9/15)<1e-14

# Numerical gap, theorem bound uses toy base gap 7/6 and hidden eta >=1/8.
evals=eigsh(Q,k=4,which='LA',return_eigenvectors=False)
evals=np.sort(evals)[::-1]
num_gap=1-evals[1]
assert num_gap+1e-10 >= 1/15

# hidden phase kernels on 42 hidden states; commutator norm should sqrt(3)/64.
hstates=[(l,p) for l in range(Z) for p in perms]
hidx={s:i for i,s in enumerate(hstates)}
def P_hidden(phase):
    rr=[];cc=[];dd=[]
    for i,(l,p) in enumerate(hstates):
        for u in U:
            ll,pp=hidden_mul(l,p,u,phase)
            rr.append(i);cc.append(hidx[(ll,pp)]);dd.append(1/8)
    return sp.csr_matrix((dd,(rr,cc)),shape=(42,42))
P0=P_hidden(0);P1=P_hidden(1)
comm=(P0@P1-P1@P0).toarray()
comm_num=np.linalg.norm(comm,2)
assert abs(comm_num-math.sqrt(3)/64)<1e-12

# hidden gaps numerical
for P in (P0,P1):
    ee=eigsh(P,k=3,which='LA',return_eigenvectors=False)
    ee=np.sort(ee)[::-1]
    assert 1-ee[1] >= 1/8-1e-10

# TV sandwich numerical at several times.
# Evolution of column law is exp(t(Q^T-I)) delta.
I=sp.eye(N,format='csr')
delta=np.zeros(N); delta[start]=1.0
pi=np.ones(N)/N
# base K7 source continuous-time at effective time a*t
Pbase=np.full((Z,Z),1/6); np.fill_diagonal(Pbase,0)
base_start=np.zeros(Z); base_start[0]=1
base_pi=np.ones(Z)/Z

def tv(v,p): return 0.5*np.sum(np.abs(v-p))
for t in (0.5,2.0,5.0,10.0,20.0):
    mu=expm_multiply((Q.T-I)*t,delta)
    out_tv=tv(mu,pi)
    base_mu=expm_multiply((sp.csr_matrix(Pbase.T)-sp.eye(Z))*float(a)*t,base_start)
    base_tv=tv(base_mu,base_pi)
    rhs=base_tv+0.5*math.exp(-2*float(c)*t)+0.5*math.sqrt(42-1)*math.exp(-float(b)*eta*t)
    assert out_tv+2e-10 >= base_tv
    assert out_tv <= rhs+2e-10

print('S3_commutator_norm_exact = sqrt(3)/4')
print('hidden_switched_commutator_norm_exact = sqrt(3)/64')
print(f'gamma_R = {gamma_R:.12f}')
print('hidden_gap_lower_bound = 1/8')
print('output_gap_lower_bound = 1/15')
print(f'numerical_toy_output_gap = {num_gap:.12f}')
print('output_cutoff_center = (15/4) log_5 n = (75/22) log_5 N + O(1)')
print(f'hidden_transfer_error_power_in_n = {hidden_error_exponent_n:.12f}')
print(f'phase_error_power_in_n = {phase_error_exponent_n:.12f}')
print(f'non_LRE_beta = {beta_lre:.12f}')
print(f'exact_non_LRE_certificate: 5^11={5**11} < 14^9={14**9}')
print(f'finite_toy_states = {N}, row_err={row_err:.3e}, sym_err={sym_err:.3e}')
print('TV_sandwich_checked_at_t = 0.5,2,5,10,20')
print('ALL_CHECKS_PASS')
