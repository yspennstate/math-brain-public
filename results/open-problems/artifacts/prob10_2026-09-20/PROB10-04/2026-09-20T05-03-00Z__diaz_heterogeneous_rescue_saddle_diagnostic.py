import math
from math import comb, factorial

gamma = 4.4898
M = 23

# Diaz et al. Appendix B: the pure-literal stopping point gives
# q=sqrt(b)=1-exp(-(3*gamma/2)q^2); take the large positive root.
def root_eq(q):
    return q - (1.0-math.exp(-1.5*gamma*q*q))

lo,hi = 0.9,1.0
for _ in range(200):
    mid=(lo+hi)/2
    if root_eq(lo)*root_eq(mid) <= 0:
        hi=mid
    else:
        lo=mid
q=(lo+hi)/2
b=q*q
a=1.5*gamma*b

def delta_b(i,j):
    if i < j or j < 1:
        return 0.0
    base=math.exp(-2*a)*a**(i+j)/(factorial(i)*factorial(j))
    return base*(2.0 if i>j else 1.0)

lambda_p=lambda_n=0.0
for i in range(1,80):
    for j in range(1,i+1):
        d0=delta_b(i,j)
        lambda_p += i*d0
        lambda_n += j*d0
gamma_b=(lambda_p+lambda_n)/3

# Rounded source saddle multipliers from Diaz et al., Appendix E, p.19.
mu_ps=1.9972796
mu_ns1=0.45029358
mu_ns2=0.33794030
nu_ps=1.2782018
nu_ns1=0.33277280
nu_ns2=0.95336927

Psi_p=nu_ps*mu_ps+1.0
Psi_n=nu_ns1*mu_ns1+nu_ns2*mu_ns2+1.0
ell_ps=lambda_p*nu_ps*mu_ps/Psi_p
ell_pu=lambda_p/Psi_p
ell_ns1=lambda_n*nu_ns1*mu_ns1/Psi_n
ell_ns2=lambda_n*nu_ns2*mu_ns2/Psi_n
ell_nu=lambda_n/Psi_n

gamma_k=[
    comb(3,k)*lambda_p**k*lambda_n**(3-k)/(lambda_p+lambda_n)**3*gamma_b
    for k in range(4)
]

def ns_split(ps,ns):
    if ps+ns == 1:
        return ns,0
    return 0,ns

alphas=[]
Psi_k=[0.0]*4
for ps in range(4):
    for ns in range(4-ps):
        for pu in range(4-ps-ns):
            nu=3-ps-ns-pu
            if ps+ns < 1:
                continue
            p=ps+pu
            ns1,ns2=ns_split(ps,ns)
            w=sum(int(x==0) for x in (ps,ns,pu,nu))
            weight=2.0/factorial(w)*mu_ps**ps*mu_ns1**ns1*mu_ns2**ns2
            alphas.append((ps,ns,pu,nu,p,ns1,ns2,w,weight))
            Psi_k[p]+=weight

c={}
for ps,ns,pu,nu,p,ns1,ns2,w,weight in alphas:
    c[(ps,ns,pu,nu)] = gamma_k[p]*weight/Psi_k[p]

Q_safe=sum(ps*val for (ps,ns,pu,nu),val in c.items() if ps+ns>=2)
B_can=sum(val for (ps,ns,pu,nu),val in c.items()
          if ps==0 and ns==1 and nu>=1)

def Psi_ij(i,j):
    return nu_ps**i + (nu_ns1+nu_ns2)**j - nu_ns2**j

def tval(i,j):
    return delta_b(i,j)*nu_ps**i/Psi_ij(i,j)

def fval(i,j,k):
    return delta_b(i,j)*comb(j,k)*nu_ns1**k*nu_ns2**(j-k)/Psi_ij(i,j)

E1=sum(fval(i,1,1) for i in range(1,M+1))
old_E=fval(1,1,1)

safe_ratio=Q_safe/ell_ps
blocker_ratio=B_can/ell_nu
leaf_ratio=E1/ell_ns1
d_ratio=blocker_ratio*leaf_ratio

terms=[]
J_new=0.0
for i in range(1,M+1):
    for j in range(2,min(i,M)+1):
        tv=tval(i,j)
        p=(safe_ratio**i)*(d_ratio**j)
        jt=-tv*math.log1p(-p)
        J_new += jt
        terms.append((jt,i,j,tv,p))
terms.sort(reverse=True)

# Previous narrow family, evaluated with the same exact NA compiler.
old_Q=c[(1,1,1,0)]
old_B=c[(0,1,1,1)]
old_safe_ratio=old_Q/ell_ps
old_d=(old_B/ell_nu)*(old_E/ell_ns1)
J_old=0.0
for r in range(2,M+1):
    p=(old_safe_ratio**r)*(old_d**r)
    J_old += -tval(r,r)*math.log1p(-p)

source_base=(1.0+1e-7)*0.9999998965
source_log_margin=-math.log(source_base)

print("ROUNDED_SOURCE_SADDLE_DIAGNOSTIC_NOT_A_CERTIFIED_ENDPOINT")
print(f"q = {q:.16g}")
print(f"b = {b:.16g}")
print(f"a = 3*gamma*b/2 = {a:.16g}")
print(f"lambda_p = {lambda_p:.16g}")
print(f"lambda_n = {lambda_n:.16g}")
print(f"gamma_b = {gamma_b:.16g}")
print(f"ell_ps = {ell_ps:.16g}")
print(f"ell_ns1 = {ell_ns1:.16g}")
print(f"ell_nu = {ell_nu:.16g}")
print(f"Q_safe = {Q_safe:.16g}")
print(f"B_can = {B_can:.16g}")
print(f"E1 = sum_i f_(i,1,1) = {E1:.16g}")
print(f"old_E = f_(1,1,1) = {old_E:.16g}")
print(f"E1/old_E = {E1/old_E:.16g}")
print(f"safe_ratio = {safe_ratio:.16g}")
print(f"blocker_ratio = {blocker_ratio:.16g}")
print(f"leaf_ratio = {leaf_ratio:.16g}")
print(f"d_ratio = {d_ratio:.16g}")
print(f"J_old_narrow_NA = {J_old:.16g}")
print(f"J_new_heterogeneous_NA = {J_new:.16g}")
print(f"J_new/J_old = {J_new/J_old:.16g}")
print(f"source_base_from_published_rounded_bound = {source_base:.16g}")
print(f"source_log_margin = {source_log_margin:.16g}")
print(f"J_new/source_log_margin = {J_new/source_log_margin:.16g}")
print("TOP_10_J_TERMS")
for jt,i,j,tv,p in terms[:10]:
    print(f"  i={i:2d} j={j:2d} t={tv:.16g} p={p:.16g} Jterm={jt:.16g}")
print("DIAGNOSTIC_COMPLETE = True")
print("NOTE: multipliers are the rounded decimal values printed by Diaz et al.;")
print("      this diagnostic quantifies the mechanism at that rounded saddle but is")
print("      NOT interval arithmetic, NOT a global reoptimization, and NOT a new alpha endpoint.")
