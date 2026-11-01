from fractions import Fraction as F

# Current exact endpoint parameter p=P/Q = 9/10-U_MIV.
p = F(
    231987093666883409713408842559789945917,
    52664345525950501687094998553955322162130,
)
assert F(1,250) < p < F(1,200)

q0 = F(18) - 20*p
qstar = 400*p/F(9)
q1 = F(4057,250)
profile = [
    q0,
    q1,
    F(3083,250),
    F(2239,250),
    F(6221,1000),
    F(1031,250),
    F(2583,1000),
    F(297,200),
    F(18,25),
    qstar,
]

# Inherited non-reflected two-slope Hamiltonian tolerance.
def D(q):
    return (200*p+q)*(40-q)/(110*p+q+81)

ladder_margins = [D(lo) - (hi-lo) for hi,lo in zip(profile,profile[1:])]
assert min(ladder_margins) > 0

# New reflected one-boundary gluing lemma.
# For J<3840, q0 is used on [0,3840), while a high child may cross once
# into the q1 block.  In orientation b>=a, write x=b-a >=0.  The exact
# branch upper bounds are
#   R/Q <= C_R*x - A*J,
#   H/Q <= -C_H*x + d*J,
# because at most J high-interval unit edges lie beyond 3840.
# Thus R>0 forces x>A*J/C_R, and H<=0 follows from d*C_R<=C_H*A.
d = q0-q1
A = F(40)-2*q0            # = 4+40p
C_R = F(38016)-42240*p
C_H = F(38016)+34560*p
reflected_margin = C_H*A - C_R*d
assert 0 < d < 2
assert C_R > 0 and C_H > 0 and A > 0
assert reflected_margin > 0

# The other orientation a>=b is controlled directly by the reflected branch:
#   R/Q <= C_H*(b-a)-A*J <= 0.

# New compact-support staircase: first transition at 3840, then the same
# eight 7681-edge blocks and the same terminal 7680-edge qstar zone.
R0 = 3840
L = 7681
Z = R0 + 8*L + 7680
assert Z == 72968

slopes = profile[1:-1]
ranges = []
start = 0
ranges.append((start,start+R0,q0)); start += R0
for s in slopes:
    ranges.append((start,start+L,s)); start += L
ranges.append((start,start+7680,qstar)); start += 7680
assert start == Z

# Exact handoff domination at the last potentially nonzero old654 state.
J = 18450
psi = F(0)
for a,b,s in ranges:
    n = max(0, min(b,Z)-max(a,J))
    psi += n*s
M = F(6287749069,38880)
handoff_margin = psi-M
assert psi == F(
    1031193430537566654997338277589375324943330739149,
    5266434552595050168709499855395532216213000,
)
assert handoff_margin == F(
    174469540606790832849626539636400507863597542060403,
    5118974385122388763985633859444457314159036000,
)
assert handoff_margin > 0

# Sharpness within the monotone separated-staircase architecture with every
# unit slope <= q0: at reflected state J=0 and action a=b=1, u=v=3840 and
# both branches require a potential drop of exactly 3840*q0.  Hence all of
# the first 3840 unit slopes must equal q0; no downward transition can start
# earlier without using slopes >q0 or a different architecture.
branch0 = F(69120)-76800*p
assert branch0 == 3840*q0

print('I0130_REFLECTED_BOUNDARY_3840_PASS')
print('p=', p)
print('q0=', q0)
print('qstar=', qstar)
print('first_jump_d=', d)
print('reflected_margin=', reflected_margin)
print('min_ladder_margin=', min(ladder_margins))
print('support_cutoff=', Z)
print('psi_18450_over_Q=', psi)
print('old654_envelope_over_Q=', M)
print('handoff_margin_over_Q=', handoff_margin)
print('J0_a=b=1_required_drop_over_Q=', branch0)
print('previous_to_new_support_factor=', F(76807,Z))
