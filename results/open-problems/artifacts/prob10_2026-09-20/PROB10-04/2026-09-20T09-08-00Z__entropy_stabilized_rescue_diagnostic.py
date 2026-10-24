import mpmath as mp
from math import factorial

mp.mp.dps = 90
D = mp.mpf
gamma = D("4.4898")
M = 23

# Rounded-source diagnostic only. The six multipliers are the decimals printed
# by Diaz et al. and already used by preceding PROB10-04 diagnostics.
mu_ps = D("1.9972796")
mu_ns1 = D("0.45029358")
mu_ns2 = D("0.33794030")
nu_ps = D("1.2782018")
nu_ns1 = D("0.33277280")
nu_ns2 = D("0.95336927")

# Exact finite combinatorial range check for the two clause statistics.
types = []
for ps in range(4):
    for ns in range(4-ps):
        for pu in range(4-ps-ns):
            nu = 3-ps-ns-pu
            if ps+ns < 1:
                continue
            k = ps+pu
            ns1 = ns if ps+ns == 1 else 0
            ns2 = ns if ps+ns >= 2 else 0
            bstat = int(ps == 0 and ns == 1 and nu >= 1)
            qstat = ps if ps+ns >= 2 else 0
            wfac = sum(int(x == 0) for x in (ps,ns,pu,nu))
            types.append((ps,ns,pu,nu,k,ns1,ns2,bstat,qstat,wfac))

B_ranges = []
Q_ranges = []
for k in range(4):
    bs = [t[7] for t in types if t[4] == k]
    qs = [t[8] for t in types if t[4] == k]
    B_ranges.append(max(bs)-min(bs))
    Q_ranges.append(max(qs)-min(qs))
assert B_ranges == [1,1,0,0]
assert Q_ranges == [0,1,2,3]

# Pure-literal core rounded source point.
def root_eq(q):
    return q - (1-mp.exp(-D("1.5")*gamma*q*q))
lo, hi = D("0.9"), D("1")
flo = root_eq(lo)
for _ in range(400):
    mid = (lo+hi)/2
    fm = root_eq(mid)
    if flo*fm <= 0:
        hi = mid
    else:
        lo = mid
        flo = fm
q_core = (lo+hi)/2
b_core = q_core*q_core
a = D("1.5")*gamma*b_core

def delta_b(i,j):
    if i < j or j < 1:
        return D(0)
    base = mp.exp(-2*a)*a**(i+j)/(mp.factorial(i)*mp.factorial(j))
    return base*(2 if i > j else 1)

lambda_p = D(0)
lambda_n = D(0)
for i in range(1,140):
    for j in range(1,i+1):
        dd = delta_b(i,j)
        lambda_p += i*dd
        lambda_n += j*dd
gamma_b = (lambda_p+lambda_n)/3

Psi_p = nu_ps*mu_ps + 1
Psi_n = nu_ns1*mu_ns1 + nu_ns2*mu_ns2 + 1
u = lambda_p*nu_ps*mu_ps/Psi_p
v = lambda_n*nu_ns1*mu_ns1/Psi_n
w = lambda_n*nu_ns2*mu_ns2/Psi_n
N = lambda_n/Psi_n

gamma_k = [
    mp.binomial(3,k)*lambda_p**k*lambda_n**(3-k)/(lambda_p+lambda_n)**3*gamma_b
    for k in range(4)
]

# Gibbs clause distribution and reference B_*, Q_*.
Psi_k = [D(0)]*4
weights = []
for ps,ns,pu,nu,k,ns1,ns2,bstat,qstat,wfac in types:
    wt = D(2)/mp.factorial(wfac) * mu_ps**ps * mu_ns1**ns1 * mu_ns2**ns2
    weights.append(wt)
    Psi_k[k] += wt

Bstar = D(0)
Qstar = D(0)
for t,wt in zip(types,weights):
    ps,ns,pu,nu,k,ns1,ns2,bstat,qstat,wfac = t
    mass = gamma_k[k]*wt/Psi_k[k]
    Bstar += bstat*mass
    Qstar += qstat*mass

# j=1 Gibbs variable blocks and reference E_*.
delta = [delta_b(i,1) for i in range(1,M+1)]
D1 = sum(delta)
Estar = D(0)
for i,di in enumerate(delta,1):
    pfalse = nu_ns1/(nu_ps**i + nu_ns1)
    Estar += di*pfalse

GB = gamma_k[0] + gamma_k[1]
GQ = gamma_k[1] + 4*gamma_k[2] + 9*gamma_k[3]

def A_min(q,E):
    # Fractional-knapsack structure proved analytically in the companion note.
    # Numerically place false mass in i=1,2,... because q^i decreases in i.
    rem = E
    total = sum(di*q**i for i,di in enumerate(delta,1))
    removed = D(0)
    for i,di in enumerate(delta,1):
        take = min(di, rem)
        removed += take*q**i
        rem -= take
        if rem <= D("1e-80"):
            break
    if rem > D("1e-60"):
        raise RuntimeError("E exceeds D1")
    return total-removed

# Simple rational radii for the theorem's four-case dichotomy.
rB = D("0.0016")
rQ = D("0.0006")
rE = D("0.05")

cost_B = (rB*Bstar)**2/GB
cost_Q = (rQ*Qstar)**2/GQ
cost_E = 2*(rE*Estar)**2/D1

q_low = (1-rQ)*Qstar/u
E_high = (1+rE)*Estar
A_low = A_min(q_low,E_high)
rescue_low = ((1-rB)*Bstar * (1-rE)*Estar)/(2*N*v) * A_low
defect_lb = min(cost_B,cost_Q,cost_E,rescue_low)

source_base = (1+D("1e-7"))*D("0.9999998965")
source_log_margin = -mp.log(source_base)
previous_fixed_outer = D("3.5129045422595363e-7")

print("ENTROPY_STABILIZED_RESCUE_DIAGNOSTIC")
print("ROUNDED_SOURCE_MULTIPLIERS_ONLY_NOT_INTERVAL_ENDPOINT")
print("EXACT_CLAUSE_RANGE_CHECKS_PASS =", B_ranges == [1,1,0,0] and Q_ranges == [0,1,2,3])
for name,x in [
    ("gamma_b",gamma_b),("u",u),("v",v),("w",w),("N",N),
    ("Bstar",Bstar),("Qstar",Qstar),("Estar",Estar),("D1",D1),
    ("GB",GB),("GQ",GQ),("q_low",q_low),("E_high",E_high),
    ("A_min_low",A_low),("cost_B",cost_B),("cost_Q",cost_Q),
    ("cost_E",cost_E),("rescue_low",rescue_low),("defect_lb",defect_lb),
    ("source_log_margin",source_log_margin),
    ("defect_over_source_margin",defect_lb/source_log_margin),
    ("defect_over_previous_fixed_outer",defect_lb/previous_fixed_outer),
]:
    print(name, "=", mp.nstr(x,50))

assert defect_lb > D("2.9e-7")
assert defect_lb/source_log_margin > 80
assert defect_lb/previous_fixed_outer > D("0.83")
print("ROUNDED_DIAGNOSTIC_CHECKS_PASS = True")
