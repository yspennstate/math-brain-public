from __future__ import annotations
import itertools, math
import numpy as np
from scipy.linalg import expm

# ---------- asymptotic degree-20 family constants ----------
d = 6
s = 14
D = d+s
alpha = 1/10
sqrt5 = math.sqrt(5.0)
gamma_base = 1 - sqrt5/3
# Hidden skew graph K=C6 x Lambda has gap >= min((6/7)gamma_Lambda, 2/7).
gamma_hidden = min((6/7)*gamma_base, 2/7)
a = d/D
b = s/D
gamma_output_lb = min(a*gamma_base, b*gamma_hidden)
center_factor = D/(d-2)  # times log_{d-1} n
mix_decay_power = b*gamma_hidden*center_factor/math.log(d-1) - alpha/2
rho = math.log(d-1)/math.log(D-1)
beta_nonlre = 0.5*(1-rho) - alpha/(1+alpha)

print('ASYMPTOTIC_CONSTANTS')
print(f'd={d} s={s} D={D} alpha={alpha:.12f}')
print(f'gamma_base_lb={gamma_base:.15f}')
print(f'gamma_hidden_lb={gamma_hidden:.15f}')
print(f'gamma_output_lb={gamma_output_lb:.15f}')
print(f'center_factor_log5_n={center_factor:.15f}')
print(f'center_factor_log5_N_asymptotic={center_factor/(1+alpha):.15f}')
print(f'hidden_error_decay_power_in_n={mix_decay_power:.15f}')
print(f'nonLRE_beta_in_N={beta_nonlre:.15f}')
print(f'exact_nonLRE_integer_check: 5^11={5**11} < 19^9={19**9} -> {5**11 < 19**9}')
assert abs(gamma_hidden - (6-2*sqrt5)/7) < 1e-14
assert abs(gamma_output_lb - (3-sqrt5)/10) < 1e-14
assert abs(center_factor - 5.0) < 1e-15
assert mix_decay_power > 0.0
assert beta_nonlre > 0.0
assert 5**11 < 19**9

# ---------- finite noncommuting semidirect sanity toy ----------
# Base Gamma = V_4 = {0,1,2,3} under xor; S={1,2,3}; Aut preserving S is S_3.
base = list(range(4))
Sbase = [1,2,3]

def bxor(x,y): return x ^ y

# permutations of labels 1,2,3 represented by tuple (p(1),p(2),p(3))
perms = list(itertools.permutations((1,2,3)))
idp = (1,2,3)
def pcomp(p,q):
    # p after q
    return tuple(p[q[i]-1] for i in range(3))
def pinv(p):
    out=[0,0,0]
    for i,v in enumerate(p, start=1): out[v-1]=i
    return tuple(out)
def pact(p,g):
    return 0 if g==0 else p[g-1]

tau = (2,1,3)              # transposition (12)
r = (2,3,1)                # 3-cycle 1->2->3->1
rinv = pinv(r)

# Hidden K=S3 x C3.
K = [(p,c) for p in perms for c in range(3)]
def kmul(k,l): return (pcomp(k[0],l[0]), (k[1]+l[1])%3)
def kinv(k): return (pinv(k[0]), (-k[1])%3)
Kid=(idp,0)
# Symmetric, connected, and cross tau does not commute with r.
sigma = (1,3,2)            # transposition (23), not normalized by tau inside this T
T = [(r,0),(rinv,0),(sigma,1),(sigma,2)]
assert {kinv(t) for t in T} == set(T)

def rho(k,g): return pact(k[0],g)

def hmul(x,y):
    g,k=x; h,l=y
    return (bxor(g, rho(k,h)), kmul(k,l))
def hinv(x):
    g,k=x
    ki=kinv(k)
    return (rho(ki,g), ki)  # V4 has -g=g

cross=[(u,(tau,0)) for u in Sbase]
vert=[(0,t) for t in T]
Sigma=cross+vert
assert len(Sigma)==len(set(Sigma))
assert {hinv(x) for x in Sigma}==set(Sigma)

H=[(g,k) for g in base for k in K]
idx={x:i for i,x in enumerate(H)}
Kidx={k:i for i,k in enumerate(K)}
N=len(H)
P_H=np.zeros((N,N))
for x in H:
    i=idx[x]
    for z in Sigma:
        P_H[i,idx[hmul(x,z)]] += 1/len(Sigma)
assert np.max(np.abs(P_H.sum(axis=1)-1))<1e-14
assert np.max(np.abs(P_H-P_H.T))<1e-14

P_G=np.zeros((4,4))
for g in base:
    for u in Sbase:
        P_G[g,bxor(g,u)] += 1/3

P_F=np.zeros((len(K),len(K)))
for k in K:
    for t in T:
        P_F[Kidx[k],Kidx[kmul(k,t)]] += 1/len(T)
assert np.max(np.abs(P_F-P_F.T))<1e-14

def gap(P):
    vals=np.linalg.eigvalsh(P)
    vals=np.sort(vals)[::-1]
    return 1-vals[1], vals

gG,_=gap(P_G)
gF,_=gap(P_F)
gH,_=gap(P_H)
a_t=len(cross)/len(Sigma)
b_t=len(vert)/len(Sigma)
print('\nFINITE_TOY')
print(f'|Gamma|={len(base)} |K|={len(K)} |H|={N} d={len(cross)} s={len(vert)}')
print(f'a={a_t:.15f} b={b_t:.15f}')
print(f'gap_base={gG:.15f} gap_hidden={gF:.15f} gap_output={gH:.15f}')
print(f'gap_theorem_lb={min(a_t*gG,b_t*gF):.15f}')
assert gH + 1e-12 >= min(a_t*gG,b_t*gF)

# Exact lumping check: total probability from (g,k) to base h equals a P_G[g,h] plus hold b at h=g.
max_lump=0.0
for x in H:
    g,k=x; i=idx[x]
    for h in base:
        got=sum(P_H[i,idx[(h,l)]] for l in K)
        want=a_t*P_G[g,h] + (b_t if h==g else 0.0)
        max_lump=max(max_lump,abs(got-want))
print(f'max_one_step_base_lumping_error={max_lump:.3e}')
assert max_lump < 1e-14

# Hidden cross permutation and vertical kernel genuinely fail to commute.
Rtau=np.zeros_like(P_F)
for k in K:
    Rtau[Kidx[k],Kidx[kmul(k,(tau,0))]]=1.0
comm=np.max(np.abs(Rtau@P_F-P_F@Rtau))
print(f'hidden_cross_vertical_commutator_max={comm:.15f}')
assert comm > 1e-8

# Continuous-time TV sandwich from identity start.
def ct_row(P,t,i=0):
    return expm(t*(P-np.eye(P.shape[0])))[i]
def tv(mu):
    return 0.5*np.sum(np.abs(mu-1/len(mu)))
startH=idx[(0,Kid)]
for t in [0.25,0.75,1.5,3.0,6.0,12.0,20.0]:
    dH=tv(ct_row(P_H,t,startH))
    dG=tv(ct_row(P_G,a_t*t,0))
    err=0.5*math.sqrt(len(K)-1)*math.exp(-b_t*gF*t)
    oklo=dH+2e-11>=dG
    okup=dH<=dG+err+2e-11
    print(f't={t:4.2f} dG(a t)={dG:.12f} dH(t)={dH:.12f} err={err:.12f} lower={oklo} upper={okup}')
    assert oklo and okup

print('ALL_CHECKS_PASS')
