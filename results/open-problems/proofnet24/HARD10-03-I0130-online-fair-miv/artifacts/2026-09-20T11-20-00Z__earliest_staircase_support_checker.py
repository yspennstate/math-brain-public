from fractions import Fraction as F

# Inherited source-valid endpoint.
U = F(4716592387968856810867208985600000000000,
      5266434552595050168709499855395532216213)
p = F(9, 10) - U
q0 = F(18, 1) - 20*p
qstar = F(400, 9)*p

# Previously certified old654 envelope at the older parameter p_old.
p_old = F(82051, 18662400)
BASE_MAX = F(3018119553120, 1)
Q_old = 18662400
M = BASE_MAX / Q_old
BASE_SUPPORT = 18450
assert p > p_old
assert F(0) < p < F(9, 10)

def D(q):
    return ((200*p + q)*(40 - q))/(110*p + q + 81)

# Exact tail-to-core ladder inherited from the delayed-staircase theorem.
r = [
    qstar,
    F(18, 25),
    F(297, 200),
    F(2583, 1000),
    F(1031, 250),
    F(6221, 1000),
    F(2239, 250),
    F(3083, 250),
    F(4057, 250),
]
for i in range(8):
    assert r[i+1] - r[i] <= D(r[i])
assert q0 - r[8] <= D(r[8])

# f(q)=q+D(q) is strictly increasing on the relevant range because
# f'(q)=99(9-10p)(10p+11)/(110p+q+81)^2 > 0.
# Thus iterating f gives the largest slope reachable after a fixed number
# of admissible local jumps. Eight jumps are insufficient; nine suffice.
x = qstar
xvals = [x]
for _ in range(9):
    x = x + D(x)
    xvals.append(x)
assert xvals[8] < q0 < xvals[9]

# Earliest transition compatible with the unchanged reflected affine proof.
# For reflected J<3840 and ceil(u)<=3840, the largest queried high state is
# 7679, so all unit edges through index 7678 must retain slope q0.
R = 7679
L = 7681       # strictly exceeds the total comparison span 7680
TAIL = 7680    # exactly the clipping compensation span
E = R + 8*L
Z = E + TAIL
assert E == 69127
assert Z == 76807

# Profile: q0 until R, then r8,...,r1, then qstar for TAIL edges.
segments = [(0, R, q0)]
s = R
for idx in range(8, 0, -1):
    segments.append((s, s + L, r[idx]))
    s += L
segments.append((s, s + TAIL, qstar))
assert s == E and E + TAIL == Z

def psi(j):
    if j >= Z:
        return F(0)
    out = F(0)
    for a, b, slope in segments:
        lo = max(j, a)
        hi = min(Z, b)
        if hi > lo:
            out += (hi - lo)*slope
    return out

# Monotonicity in p gives, for the current p>p_old,
# F0_current(J)/Q_current <= F0_old(J)/Q_old <= M,
# and old support J<=18450 remains a valid support bound.
# Since psi is decreasing, checking the support endpoint suffices.
assert psi(BASE_SUPPORT) > M
margin = psi(BASE_SUPPORT) - M

print('I0130_EARLIEST_STAIRCASE_SUPPORT_PASS')
print('p_minus_pold=', p - p_old)
print('jump_count_minimal=9; intermediate_blocks_minimal=8')
print('R=', R, 'L=', L, 'E=', E, 'tail_edges=', TAIL, 'Z=', Z)
print('old654_M=', M)
print('psi_at_old654_support=', psi(BASE_SUPPORT))
print('domination_margin=', margin)
print('compression_vs_2429036=', F(2429036, Z))
print('compression_vs_240051600=', F(240051600, Z))
