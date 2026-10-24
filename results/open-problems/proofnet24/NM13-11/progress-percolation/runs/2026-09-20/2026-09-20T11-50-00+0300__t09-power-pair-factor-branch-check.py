from fractions import Fraction

def finite_interval_coefficients(R=5):
    verts = list(range(-R, R+1))
    edges = []
    for i in verts:
        for d in (1,2):
            j = i+d
            if j <= R:
                edges.append((i,j))
    m = len(edges)
    incident = {v: [] for v in verts}
    for ei,(a,b) in enumerate(edges):
        incident[a].append((ei,b))
        incident[b].append((ei,a))
    A = [0]*(m+1)
    for mask in range(1<<m):
        seen = {0}
        stack = [0]
        while stack:
            x = stack.pop()
            for ei,y in incident[x]:
                if ((mask >> ei) & 1) and y not in seen:
                    seen.add(y)
                    stack.append(y)
        A[mask.bit_count()] += len(seen)-1
    return edges, A

edges, A = finite_interval_coefficients(5)
m = len(edges)
assert m == 19
expected_A = [0, 4, 84, 838, 5258, 23130, 75278, 186662, 358566,
              538580, 635614, 590636, 432292, 248424, 111100, 37992,
              9626, 1708, 190, 10]
assert A == expected_A

# Rank-3 doubled-power endpoint: factor Cayley graph uses steps +/-1,+/-2.
p3 = Fraction(47,500)
s3 = 1-p3
mu5 = sum(Fraction(A[k]) * p3**k * s3**(m-k) for k in range(m+1))
mu5_margin = mu5 - Fraction(1,2)
assert mu5_margin > 0
# Three free factors: mean matrix has off-diagonal mu, spectral radius 2 mu.
assert 2*mu5 > 1

# Nonbacktracking lower bound for the degree-15 ambient graph.
# q=2r-1=5, D=15, Q=14, ||A|| <= 3+4 sqrt(5).
sqrt5_ub = Fraction(223607,100000)
sqrt5_square_margin = sqrt5_ub**2 - 5
assert sqrt5_square_margin > 0
z3 = Fraction(10000,941)
assert z3**2 > 14
h3 = z3 + Fraction(14,1)/z3
a3_ub = 3 + 4*sqrt5_ub
root_margin3 = h3-a3_ub
assert root_margin3 > 0
pc3 = p3
pu3 = Fraction(941,10000)
gap3 = pu3-pc3
assert gap3 == Fraction(1,10000)

# Rank-4 arbitrary-two-exponent endpoint.
# In each cyclic factor, E[Z-1] >= 4p+2p^2 using +/-e,+/-f and +/- (e+f).
p4 = Fraction(81,1000)
mu4_lb = 4*p4 + 2*p4*p4
branch4_margin = 3*mu4_lb-1
assert branch4_margin > 0

# q=7, D=19, Q=18, ||A|| <= 3+4 sqrt(7).
sqrt7_ub = Fraction(127,48)
sqrt7_square_margin = sqrt7_ub**2-7
assert sqrt7_square_margin > 0
z4 = Fraction(500,41)
assert z4**2 > 18
h4 = z4 + Fraction(18,1)/z4
a4_ub = 3 + 4*sqrt7_ub
root_margin4 = h4-a4_ub
assert root_margin4 > 0
pc4 = p4
pu4 = Fraction(41,500)
gap4 = pu4-pc4
assert gap4 == Fraction(1,1000)

# For arbitrary two exponent layers and every r>=5, the alternating-factor
# reduced-word tree gives p_c <= 1/[4(r-1)] = 1/[2(q-1)].
# The nonbacktracking root test at z=2(q-1) has margin
# F(q)=2q-4+3/(q-1)-4 sqrt(q), increasing for q>=9.
q0 = Fraction(9,1)
sqrt9 = Fraction(3,1)
F9 = 2*q0-4 + Fraction(3,1)/(q0-1) - 4*sqrt9
assert F9 == Fraction(19,8) and F9 > 0
# derivative lower bound for q>=9:
# F'(q)=2-3/(q-1)^2-2/sqrt(q) >= 2-3/64-2/3.
derivative_lb = Fraction(2,1)-Fraction(3,64)-Fraction(2,3)
assert derivative_lb == Fraction(247,192) and derivative_lb > 0

print("RANK3_DOUBLED_POWER")
print(f"interval_edges={m}")
print(f"A={A}")
print(f"p3={p3}")
print(f"mu5={mu5}")
print(f"mu5_decimal={float(mu5):.15f}")
print(f"mu5_minus_half={mu5_margin}")
print(f"2mu5_minus_1={2*mu5-1}")
print(f"sqrt5_square_margin={sqrt5_square_margin}")
print(f"root_margin3={root_margin3}")
print(f"pc3_strict_lt={pc3}")
print(f"pu3_strict_gt={pu3}")
print(f"gap3_strict_gt={gap3}")

print("RANK4_ARBITRARY_PAIR")
print(f"p4={p4}")
print(f"mu4_lower={mu4_lb}")
print(f"3mu4_minus_1={branch4_margin}")
print(f"sqrt7_square_margin={sqrt7_square_margin}")
print(f"root_margin4={root_margin4}")
print(f"pc4_strict_lt={pc4}")
print(f"pu4_strict_gt={pu4}")
print(f"gap4_strict_gt={gap4}")

print("RANK_GE_5_ARBITRARY_PAIR")
print(f"F9={F9}")
print(f"derivative_lower_bound={derivative_lb}")
print("ALL_EXACT_CHECKS_PASS")
