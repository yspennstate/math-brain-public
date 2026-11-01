from fractions import Fraction as F

def f(k, lam):
    k = F(k)
    return F(1,1)/(k-lam) - F(1,1)/(k*k-lam)

def cert(d, D, L):
    d, D, L = F(d), F(D), F(L)
    H = D-d
    A = L*(f(d,L)-f(D,L))
    if A <= 1:
        delta = d
    else:
        delta = d - H*(A-1)*(A-1)/(4*A)
    margin = 2*delta/(D+L)**2
    return A, delta, margin

cases = [
    # d, D, L, clean_margin_denominator, expected_positive
    (3, 44, F(201,100), 15000, True),
    (3, 45, F(201,100), None, False),
    (3, 28, F(21,10), 4500, True),
    (3, 29, F(21,10), None, False),
    (3, 19, F(11,5), 4100, True),
    (3, 20, F(11,5), None, False),
    (3, 7, F(5,2), 71, True),
    (3, 8, F(5,2), None, False),
    (3, 5, F(27,10), 171, True),
    (3, 6, F(27,10), None, False),
    (2, 13, F(3,2), 3900, True),
    (2, 14, F(3,2), None, False),
]

print("PAIRWISE-GINI EXACT CERTIFICATE")
for d,D,L,N,pos in cases:
    A,delta,margin = cert(d,D,L)
    print(f"d={d} D={D} L={L}")
    print(f"  A={A} ~ {float(A):.15g}")
    print(f"  delta={delta} ~ {float(delta):.15g}")
    print(f"  derivative_margin={margin} ~ {float(margin):.15g}")
    if pos:
        assert delta > 0
        assert margin > 0
        if N is not None:
            assert margin > F(1,N)
            print(f"  clean_bound: margin > 1/{N}")
    else:
        assert delta < 0
        print("  endpoint certificate FAILS (method boundary, not counterexample)")

# Algebraic identity behind endpoint envelopes:
# f_k(lam) = k(k-1)/[(k-lam)(k^2-lam)].
for k in range(2,20):
    for lam in [F(1), F(3,2)]:
        if lam >= k:
            continue
        lhs = f(k,lam)
        rhs = F(k*(k-1),1)/((F(k)-lam)*(F(k*k)-lam))
        assert lhs == rhs

# Pointwise Gini inequality on all integer pairs for the largest main rectangle:
d,D=3,44
for x in range(d,D+1):
    for y in range(d,D+1):
        lhs=F(D-d)*abs(F(x-y))
        rhs=(F(x-d))*(F(D-y))+(F(y-d))*(F(D-x))
        assert lhs <= rhs

print("ALL_EXACT_CHECKS_PASS")
