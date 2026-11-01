#!/usr/bin/env python3
from fractions import Fraction as F

ASSERTIONS = 0

def check(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)), F(0))

def lam(N,s):
    return F(N, 2*s*(N-s))

def bal(p):
    q = 1-p
    return F(6)*p*p*q*q

def null(p):
    q = 1-p
    return p**4 + q**4

def enum4(p):
    b = F(0); n = F(0); total = F(0)
    q = 1-p
    for mask in range(16):
        r = mask.bit_count()
        prob = (p**r)*(q**(4-r))
        total += prob
        if r == 2:
            b += prob
        if r in (0,4):
            n += prob
    return b,n,total

# Harmonic proposal identities and exact symmetry.
for N in range(2, 201):
    ssum = F(0)
    for s in range(1,N):
        x = lam(N,s)
        ssum += x
        check(x == lam(N,N-s), f"lambda symmetry failed N={N},s={s}")
        check(x == F(1,2)*(F(1,s)+F(1,N-s)), f"partial fraction failed N={N},s={s}")
    check(ssum == harmonic(N-1), f"harmonic total failed N={N}")

# N=4 embedded mark probabilities.
N=4
rates=[lam(N,s) for s in (1,2,3)]
H=sum(rates,F(0))
weights=[r/H for r in rates]
check(rates == [F(2,3),F(1,2),F(2,3)], "N4 rates")
check(weights == [F(4,11),F(3,11),F(4,11)], "N4 weights")
check(sum(weights,F(0)) == 1, "weights total")

# Exact 4-leaf Bernoulli mask checks for all rational biases used.
for p in [F(1,4),F(4,5),F(1,2)]:
    b,n,t = enum4(p)
    check(t == 1, f"mask total {p}")
    check(b == bal(p), f"balanced formula {p}")
    check(n == null(p), f"null formula {p}")
    check(b == bal(1-p), f"balanced complement {p}")
    check(n == null(1-p), f"null complement {p}")

w_in = F(4,11)
w_act = F(7,11)

# State 0: proposal advances to half-turn; active bias 4/5.
A0 = w_in*bal(F(1,4)) + w_act*bal(F(4,5))
N0 = w_in*null(F(1,4)) + w_act*null(F(4,5))
# State 1: proposal advances to zero; active bias 1/2.
A1 = w_in*bal(F(1,4)) + w_act*bal(F(1,2))
N1 = w_in*null(F(1,4)) + w_act*null(F(1,2))

check(A0 == F(3489,20000), "A0")
check(N0 == F(7563,20000), "N0")
check(A1 == F(111,352), "A1")
check(N1 == F(69,352), "N1")
check(0 < N0 < 1 and 0 < N1 < 1, "null masses")

# Solve B0=A0+N0 B1, B1=A1+N1 B0.
B0 = (A0 + N0*A1)/(1-N0*N1)
B1 = A1 + N1*B0
check(B0 == F(2067621,6518153), "B0 exact")
check(B1 == A1 + N1*B0, "B1 recurrence")
check(B0 == A0 + N0*B1, "B0 recurrence")
source = F(3,11)
gap = B0-source
check(gap == F(3189372,71699683), "source gap exact")
check(gap > 0, "source gap positive")

# Exact separation from nearest archived R11 finite witnesses.
archived = {
    "C090": F(3200871,8926643),
    "C091": F(357573111,981185971),
    "C092": F(313435929,882568349),
    "C093": F(259608057,736235773),
}
for name,val in archived.items():
    check(B0 != val, f"C094 equals {name}")
    check((B0-val) != 0, f"C094 difference zero {name}")

# Tent-map elementary exact checks on rational grids.
for M in range(2,101):
    for a in range(M+1):
        u=F(a,M)
        T=2*min(u,1-u)
        check(F(0) <= T <= F(1), f"tent range M={M},a={a}")
        check(T == 2*min(1-u,u), f"tent symmetry M={M},a={a}")
        if a <= M//2:
            check(T == 2*u, f"tent left branch M={M},a={a}")
        if a*2 >= M:
            check(T == 2*(1-u), f"tent right branch M={M},a={a}")

print(f"A0={A0}")
print(f"N0={N0}")
print(f"A1={A1}")
print(f"N1={N1}")
print(f"B0={B0}")
print(f"B1={B1}")
print(f"CTCS4_BALANCED={source}")
print(f"GAP={gap}")
for name,val in archived.items():
    print(f"DIFF_{name}={B0-val}")
print(f"ASSERTIONS={ASSERTIONS}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
