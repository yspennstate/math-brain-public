import math, random

MAX_CROSS = 0.0
MAX_LINEAR = 0.0
for _ in range(20000):
    alpha = random.uniform(0.2, 3.0) * random.choice((-1.0, 1.0))
    beta = random.uniform(0.2, 3.0) * random.choice((-1.0, 1.0))
    delta = random.uniform(0.2, 3.0) * random.choice((-1.0, 1.0))
    a = random.uniform(-3.0, 3.0)
    ell = random.uniform(-3.0, 3.0)
    t = random.uniform(0.5, 100.0)
    c0 = t * alpha / (beta * delta)
    d0 = t * ell / beta
    cross = 2*t*alpha - 2*c0*beta*delta
    linear = t*ell - d0*beta
    MAX_CROSS = max(MAX_CROSS, abs(cross))
    MAX_LINEAR = max(MAX_LINEAR, abs(linear))
    theta1 = t*a - c0*beta*beta
    theta2 = t*(a-alpha*beta/delta)
    assert abs(theta1-theta2) <= 1e-10 * max(1.0, abs(theta1), abs(theta2))

assert MAX_CROSS < 2e-10
assert MAX_LINEAR < 2e-10

def C(gamma):
    return 2.0/(2.0-gamma) * (2.0*math.pi/63.0)**(gamma/2.0)

assert abs(C(1.0)-0.6316109565672897) < 1e-14
assert abs(C(1.5)-0.7098874207331786) < 1e-14

# collar inequality: q>=63/64, |alpha|<=s/64, D>=s^3 gives Delta2>=63 s^2
for _ in range(20000):
    s = 10**random.uniform(-2, 2)
    q = random.uniform(63.0/64.0, 1.0)
    pivot = random.uniform(1e-12, 1.0) * s/64.0
    D = s**3 * random.uniform(1.0, 10.0)
    Delta = q*D/pivot
    assert Delta + 1e-9*s*s >= 63.0*s*s

print(f"max_cross_cancellation_error={MAX_CROSS:.3e}")
print(f"max_linear_cancellation_error={MAX_LINEAR:.3e}")
print(f"C_1={C(1.0):.16f}")
print(f"C_3over2={C(1.5):.16f}")
print("QFORM_B11_R54_NEGMOMENT_PUNCTURE_CHECK_PASS")
