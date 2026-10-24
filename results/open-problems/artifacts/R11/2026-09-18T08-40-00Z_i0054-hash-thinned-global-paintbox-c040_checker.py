from fractions import Fraction

CHECKS = 0

def ck(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError(label)
    CHECKS += 1

def H(n):
    return sum((Fraction(1,k) for k in range(1,n+1)), Fraction())

def w(N,s):
    return Fraction(N, 2*s*(N-s))

def split_prob(N,s,i,j):
    x = Fraction(s,N)
    y = 1-x
    return x**i*y**j + x**j*y**i

def q_direct(N,i,j):
    return sum((w(N,s)*split_prob(N,s,i,j) for s in range(1,N)), Fraction())

def q_riemann(N,i,j):
    return sum((Fraction(1,N)*Fraction(s,N)**(i-1)*Fraction(N-s,N)**(j-1)
                for s in range(1,N)), Fraction())

def q11(N):
    return Fraction(N-1,N)

def q22(N):
    return Fraction(N*N-1, 6*N*N)

def two_pair_double_rate(N,M):
    # one global mark, both two-label blocks hash-eligible and both color-split
    return Fraction(2,M)*q22(N)

for N in range(3,81):
    ck(sum((w(N,s) for s in range(1,N)), Fraction()) == H(N-1),
       f"harmonic-mass N={N}")

    for i in range(1,6):
        for j in range(1,6):
            if i+j <= 8:
                ck(q_direct(N,i,j) == q_riemann(N,i,j),
                   f"beta-riemann identity N={N} i={i} j={j}")

    ck(q_direct(N,1,1) == q11(N), f"q11 N={N}")
    ck(q_direct(N,2,2) == q22(N), f"q22 N={N}")

    # U019 finite core: without hash thinning (M=1), the forbidden
    # simultaneous two-pair rate is exactly twice the desired 2|2 rate.
    d_unthinned = sum(
        (w(N,s)*(2*Fraction(s,N)*(1-Fraction(s,N)))**2
         for s in range(1,N)), Fraction())
    ck(d_unthinned == 2*q22(N), f"unthinned dual obstruction N={N}")

    # C040: M=N channels.  A global mark has rate M*w_s and each
    # disjoint carrier is independently eligible with probability 1/M.
    d_thinned = sum(
        (N*w(N,s)*Fraction(1,N*N)*
         (2*Fraction(s,N)*(1-Fraction(s,N)))**2
         for s in range(1,N)), Fraction())
    ck(d_thinned == two_pair_double_rate(N,N),
       f"thinned double-rate factor N={N}")
    ck(d_thinned == Fraction(N*N-1,3*N**3),
       f"thinned closed form N={N}")

    # Exact row-L1 error in the two-pair state versus independent block clocks.
    q = q11(N)
    d = d_thinned
    actual = [q-d, q-d, d, -(2*q-d)]
    ideal = [q, q, Fraction(0), -2*q]
    row_l1 = sum(abs(a-b) for a,b in zip(actual, ideal))
    ck(row_l1 == 4*d, f"two-pair row-L1 N={N}")

# Exact finite non-equivalence witness at N=4.
ck(q22(4) == Fraction(5,32), "N4 q22 witness")
ck(two_pair_double_rate(4,4) == Fraction(5,64), "N4 simultaneous witness")
ck(two_pair_double_rate(4,1) == Fraction(5,16), "N4 unthinned witness")

print("R11 C040 modular-hash-thinned global paintbox exact self-check")
print(f"CHECKS={CHECKS}")
print("ALL_EXACT_CHECKS_PASS")
print("N=4 q22 =", q22(4))
print("N=4 C040 simultaneous two-pair rate =", two_pair_double_rate(4,4))
print("N=4 unthinned-global simultaneous two-pair rate =", two_pair_double_rate(4,1))
print("General q11(N)=(N-1)/N and q22(N)=(N^2-1)/(6N^2).")
print("General C040 double rate d_N=(N^2-1)/(3N^3)=2 q22(N)/N -> 0.")
print("Unthinned global paintbox has d_N=2 q22(N) -> 1/3, so it cannot converge to CTCS.")
