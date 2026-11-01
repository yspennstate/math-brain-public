from decimal import Decimal, getcontext
getcontext().prec = 90

CSTAR = Decimal("6.5218512")
C0 = Decimal("6.4548")
DELTA = CSTAR - C0
RHO = Decimal(1683) / Decimal(35731)
Q = Decimal(1) / Decimal(4096)
LIP = Decimal(8) / Decimal(7)

# Source-exact spine data.
c1 = Decimal(14593) / Decimal(65536)
cstar_lo = Decimal("0.22266585228")
R2_lo = Decimal("6.5218511190811741401649047123071878637276611493668")
R2_hi = Decimal("6.5218511190811741401649047123167742489206633278087")
Tinf_lo = Decimal("6.5218511673423727025654896282010361877746102003501")
Tinf_hi = Decimal("6.5218511673532720920534233991583790594494969981239")

# Arity recurrence n_{t+1}=36 n_t-27, n1=162.
n = 162
ns=[n]
for _ in range(4):
    n=36*n-27
    ns.append(n)
assert ns == [162, 5805, 208953, 7522281, 270802089]

# Tail error propagation. c-map contracts by 1/4096; T has Lipschitz <=8/7.
ec1 = c1-cstar_lo
assert ec1 > 0
tvar2 = LIP*ec1*Q
tvar3 = tvar2*Q
tvar4 = tvar3*Q

e2 = max(abs(Tinf_hi-R2_lo), abs(Tinf_lo-R2_hi))
e3 = RHO*e2 + tvar2
e4 = RHO*e3 + tvar3
E = e4 + tvar4/(Decimal(1)-RHO)

gap = CSTAR-Tinf_hi-E
threshold = DELTA/Decimal(ns[3]-1)
assert gap > 0
assert gap > threshold

# Regression check for binom(k,2) <= n/2*(k-1), 1<=k<=n.
for N in range(2,1000):
    for k in range(1,N+1):
        assert k*(k-1) <= N*(k-1)

print("PASS")
print("Delta =", DELTA)
print("rho =", RHO)
print("arities =", ns)
print("e2 =", e2)
print("e3 =", e3)
print("e4 =", e4)
print("uniform_tail_error_bound_E =", E)
print("stable_candidate_gap_lower_bound_t>=4 =", gap)
print("monotone_pair_threshold_at_n4 =", threshold)
print("gap_over_threshold =", gap/threshold)
