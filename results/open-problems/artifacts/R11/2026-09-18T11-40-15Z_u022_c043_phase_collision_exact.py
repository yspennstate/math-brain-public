from fractions import Fraction
from itertools import combinations

ASSERTIONS = 0

def check(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)

def W(N,s):
    return Fraction(N, 2*s*(N-s))

def x(N,s):
    return Fraction(s,N)

def r(N,s,m):
    z=x(N,s)
    return 1-z**m-(1-z)**m

def r2(N,s):
    z=x(N,s)
    return 2*z*(1-z)

def a(N,s):
    return W(N,s)*r2(N,s)**2

def q(N,i,j):
    total=Fraction(0)
    for s in range(1,N):
        z=x(N,s)
        total += W(N,s)*(z**i*(1-z)**j + z**j*(1-z)**i)
    return total

def qr(N,i,j):
    return sum(((x(N,s)**(i-1))*((1-x(N,s))**(j-1)) for s in range(1,N)), Fraction(0))/N

def c043_channel(N,s,label):
    if s in (1,N-1):
        return 0
    return label

# 1. Exact beta-grid identity and basic rates.
for N in range(3,81):
    for i in range(1,7):
        for j in range(1,7):
            check(q(N,i,j)==qr(N,i,j), f"q-grid N={N} i={i} j={j}")
    check(q(N,1,1)==Fraction(N-1,N), f"q11 N={N}")
    check(q(N,2,2)==Fraction(N*N-1,6*N*N), f"q22 N={N}")

# 2. Exact shared-shock phase mass and all-phase identity.
for N in range(3,121):
    total=Fraction(0)
    for s in range(1,N):
        closed=Fraction(2*s*(N-s),N**3)
        check(a(N,s)==closed, f"a phase N={N} s={s}")
        total += a(N,s)
    check(total==Fraction(N*N-1,3*N*N), f"all shock N={N}")

# 3. Split-probability comparison r_m <= m r_2 and total exit <= m.
for N in range(3,121):
    for m in range(2,10):
        ex=Fraction(0)
        for s in range(1,N):
            rm=r(N,s,m)
            check(rm>=0, f"r>=0 N={N} s={s} m={m}")
            check(rm <= m*r2(N,s), f"r<=mr2 N={N} s={s} m={m}")
            ex += W(N,s)*rm
        check(ex <= m, f"exit<=m N={N} m={m}")

# 4. C043 exact discrepancy: all labels collide only at endpoint phases.
for N in range(4,121):
    D=Fraction(0)
    for s in range(1,N):
        coll = c043_channel(N,s,1)==c043_channel(N,s,2)
        if coll:
            D += a(N,s)
        if s in (1,N-1):
            check(coll, f"endpoint collision N={N} s={s}")
        else:
            check(not coll, f"interior injection N={N} s={s}")
    check(D==Fraction(4*(N-1),N**3), f"C043 D N={N}")
    check(D < Fraction(4,N**2), f"C043 D bound N={N}")

# 5. For every fixed tested prefix, every pair has the same C043 collision mass.
for N in range(6,51):
    k=min(8,N)
    target=Fraction(4*(N-1),N**3)
    for aa,bb in combinations(range(1,k+1),2):
        D=Fraction(0)
        for s in range(1,N):
            if c043_channel(N,s,aa)==c043_channel(N,s,bb):
                D+=a(N,s)
        check(D==target, f"homogeneous D N={N} pair={aa,bb}")

# 6. Exact finite non-equivalence witnesses against C041, C040, C042.
# At N=9, C043 has the same positive direct simultaneous rate on all pair-block states.
N=9
d043=Fraction(4*(N-1),N**3)
q22=q(N,2,2)
d040=Fraction(N*N-1,3*N**3)
d042_collision=Fraction(N*N-1,3*N*N)
check(d043==Fraction(32,729), "C043 N9")
check(q22==Fraction(40,243), "q22 N9")
check(d040==Fraction(80,2187), "C040 N9")
check(d042_collision==Fraction(80,243), "C042 collision N9")
check(d043>0, "C043 positive")
check(d043!=d040 and d043!=d042_collision, "rate distinctions")
check(d043/q22==Fraction(4,15), "C043 invariant ratio")
check(d040/q22==Fraction(2,9), "C040 invariant ratio")
check(d042_collision/q22==2, "C042 invariant ratio")
# C041 ratio is 0, so all four are pair-rate-ratio distinct at this witness.

# 7. Multi-block pair-union bound tested exactly on split probabilities.
for N in range(3,61):
    for s in range(1,N):
        base=r2(N,s)**2
        for m in range(2,7):
            for n in range(2,7):
                check(r(N,s,m)*r(N,s,n) <= m*n*base,
                      f"pair bound N={N} s={s} m={m} n={n}")

print(f"ASSERTIONS={ASSERTIONS}")
print("ALL_EXACT_CHECKS_PASS")
