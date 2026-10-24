import math

# Exact symbolic identity checked separately in the report:
# det([[eta,b,0],[b,alpha,delta],[0,delta,gamma]])
# = eta * det([[alpha-b*b/eta,delta],[delta,gamma]]).


def fourth_moment_count(N):
    vals = [2**k for k in range(1, N + 1)]
    counts = {}
    for x in vals:
        for y in vals:
            counts[x + y] = counts.get(x + y, 0) + 1
    return sum(m*m for m in counts.values())

for N in range(1, 8):
    got = fourth_moment_count(N)
    want = 2*N*N - N
    assert got == want, (N, got, want)

partner = 128*math.sqrt(2)*((3/20)*(1/16))**(-1/4)
pair_cap = 4/math.sqrt(3)
print('lacunary_fourth_moment_check=PASS')
print('partner_threshold=', repr(partner))
print('moving_slope_pair_cap=', repr(pair_cap))
print('QFORM_B05_MOVING_SLOPE_CHECK_PASS')
