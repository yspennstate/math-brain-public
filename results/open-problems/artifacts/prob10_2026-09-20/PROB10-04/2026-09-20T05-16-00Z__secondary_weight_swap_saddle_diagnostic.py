import math
from math import comb, factorial

M=23
# Inputs reproduced by the companion source-saddle diagnostic from the Diaz
# printed rounded multipliers.  This file isolates the new secondary-weight
# optimization; these are diagnostics, not interval-certified constants.
a=6.718433003118395
nu_ps=1.2782018
nu_ns1=0.33277280
nu_ns2=0.95336927
ell_ps=5.856668036248987
ell_ns1=0.5364470029682571
ell_nu=3.580001818526844
Q_safe=4.380711108236127
B_can=0.4578196810673468

def delta_b(i,j):
    if i<j or j<1:
        return 0.0
    base=math.exp(-2*a)*a**(i+j)/(factorial(i)*factorial(j))
    return base*(2.0 if i>j else 1.0)

def Psi_ij(i,j):
    return nu_ps**i + (nu_ns1+nu_ns2)**j - nu_ns2**j

def tval(i,j):
    return delta_b(i,j)*nu_ps**i/Psi_ij(i,j)

def fval(i,j,k):
    return delta_b(i,j)*comb(j,k)*nu_ns1**k*nu_ns2**(j-k)/Psi_ij(i,j)

q=Q_safe/ell_ps
b1=B_can/ell_nu
rows=[]
for K in range(1,M):
    E_hi=sum(fval(k,1,1) for k in range(K+1,M+1))
    dK=b1*(E_hi/ell_ns1)
    J=0.0
    for i in range(1,K+1):
        p=q**i*dK
        J += -tval(i,1)*math.log1p(-p)
    rows.append((J,K,E_hi,dK))

rows.sort(reverse=True)
best=rows[0]
source_margin=-math.log((1.0+1e-7)*0.9999998965)

print("SECONDARY_WEIGHT_SWAP_ROUNDED_SADDLE_DIAGNOSTIC")
print("NOT_AN_INTERVAL_CERTIFICATE_OR_GLOBAL_REOPTIMIZATION")
print(f"best_K = {best[1]}")
print(f"best_J_K = {best[0]:.16g}")
print(f"E_hi_at_best = {best[2]:.16g}")
print(f"dK_at_best = {best[3]:.16g}")
print(f"published_source_log_margin = {source_margin:.16g}")
print(f"best_J_K/source_margin = {best[0]/source_margin:.16g}")
print("TOP_10_THRESHOLDS")
for J,K,E_hi,dK in rows[:10]:
    print(f"  K={K:2d} J={J:.16g} E_hi={E_hi:.16g} dK={dK:.16g}")
print("BEST_K_TERM_BREAKDOWN")
K=best[1]
E_hi=best[2]
dK=best[3]
for i in range(1,K+1):
    tv=tval(i,1)
    p=q**i*dK
    jt=-tv*math.log1p(-p)
    print(f"  i={i:2d} t_i1={tv:.16g} p={p:.16g} Jterm={jt:.16g}")
print("DIAGNOSTIC_COMPLETE = True")
