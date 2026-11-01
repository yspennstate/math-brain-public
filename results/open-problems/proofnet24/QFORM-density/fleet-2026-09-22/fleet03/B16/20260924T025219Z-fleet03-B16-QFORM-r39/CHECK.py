import math


def det3(cols):
    a, b, c = cols
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - b[0] * (a[1] * c[2] - a[2] * c[1])
        + c[0] * (a[1] * b[2] - a[2] * b[1])
    )

r = 1.0 / math.sqrt(2.0)
c1 = (r, 0.0, r)
c2 = (0.0, r, 0.0)
c3 = (-r, 0.0, r)
c4 = (0.0, r, 0.0)

masses = [
    det3([c1, c2, c3]) ** 2,
    det3([c1, c2, c4]) ** 2,
    det3([c1, c3, c4]) ** 2,
    det3([c2, c3, c4]) ** 2,
]
print("triple_squared_masses=", masses)
assert abs(masses[0] - 0.5) < 1e-12
assert abs(masses[1]) < 1e-12
assert abs(masses[2] - 0.5) < 1e-12
assert abs(masses[3]) < 1e-12

ell = (r, 0.0, -r, 0.0)
v = (0.0, r, 0.0, r)
leverages = [ell[i] ** 2 + v[i] ** 2 for i in range(4)]
print("two_frame_row_leverages=", leverages)
assert max(abs(x - 0.5) for x in leverages) < 1e-12

closure_constant = math.pi / math.sqrt(2.0)
partner_constant = 12.0 / (4.0 ** (1.0 / 3.0))
projection_sharpening = 3.0 * (2.0 ** (2.0 / 3.0))
print("pi_over_sqrt2=", closure_constant)
print("partner_12_times_4_minus_one_third=", partner_constant)
print("projection_cap_2_sharpening=", projection_sharpening)
assert closure_constant < 2.222
assert partner_constant < 7.56
assert projection_sharpening < 4.763

for N in (10, 100, 1000, 10000):
    # Lower bound from the intervals [k*pi+pi/6,k*pi+5*pi/6]
    # in 2*integral |sin w|/w dw.
    lower = sum(2.0 / (3.0 * (k + 1.0)) for k in range(1, N + 1))
    print(f"harmonic_lower_bound_N={N}: {lower:.12f}")

print("STATUS=PASS")
