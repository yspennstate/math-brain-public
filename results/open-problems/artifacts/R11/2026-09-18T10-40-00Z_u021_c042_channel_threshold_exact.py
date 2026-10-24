from fractions import Fraction
from math import isqrt

checks = 0

def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def w(N, s):
    return Fraction(N, 2*s*(N-s))

def x(N, s):
    return Fraction(s, N)

def p_spec(N, s, i, j):
    xx = x(N, s)
    return xx**i * (1-xx)**j + xx**j * (1-xx)**i

def q(N, i, j):
    return sum((w(N,s)*p_spec(N,s,i,j) for s in range(1,N)), Fraction(0,1))

def q_rhs(N, i, j):
    return Fraction(1,N) * sum(
        (x(N,s)**(i-1) * (1-x(N,s))**(j-1) for s in range(1,N)),
        Fraction(0,1)
    )

def pair_split(N, s):
    xx = x(N,s)
    return 2*xx*(1-xx)

def d_shared(N):
    return sum((w(N,s)*pair_split(N,s)**2 for s in range(1,N)), Fraction(0,1))

def M(N):
    return max(2, isqrt(N))

def channel(N, a):
    return 1 + ((a-1) % M(N))

# Exact harmonic-beta identities and direct shared-shock formula.
for N in range(3,81):
    for i in range(1,6):
        for j in range(1,6):
            check(q(N,i,j) == q_rhs(N,i,j), f"Riemann identity failed N={N} i={i} j={j}")
    check(q(N,1,1) == Fraction(N-1,N), f"q11 failed N={N}")
    check(q(N,2,2) == Fraction(N*N-1, 6*N*N), f"q22 failed N={N}")
    check(d_shared(N) == Fraction(N*N-1, 3*N*N), f"shared rate failed N={N}")
    check(d_shared(N) == 2*q(N,2,2), f"double-count identity failed N={N}")

# Local injectivity for fixed prefixes once M_N is large enough.
for N in range(4,400):
    m = M(N)
    for k in range(1, min(m,12)+1):
        vals = [channel(N,a) for a in range(1,k+1)]
        check(len(set(vals)) == k, f"prefix injectivity failed N={N} k={k}")

# Collision congruence characterization on a large exact finite range.
for N in range(4,100):
    m = M(N)
    for a in range(1,21):
        for b in range(a+1,21):
            check((channel(N,a)==channel(N,b)) == (((b-a) % m)==0),
                  f"collision characterization failed N={N},a={a},b={b}")

# Concrete N=9 finite-law witness.
N=9
check(M(N)==3, "M9")
check(channel(N,1)==channel(N,4), "1 and 4 should collide")
check(channel(N,1)!=channel(N,5), "1 and 5 should not collide")
check(d_shared(N)==Fraction(80,243), f"N=9 direct rate {d_shared(N)}")

print(f"EXACT_CHECKS={checks}")
print(f"M9={M(9)}")
print(f"channel9(1)={channel(9,1)} channel9(4)={channel(9,4)} channel9(5)={channel(9,5)}")
print(f"q9_22={q(9,2,2)}")
print(f"d9_shared={d_shared(9)}")
print("ALL_EXACT_CHECKS_PASS")
