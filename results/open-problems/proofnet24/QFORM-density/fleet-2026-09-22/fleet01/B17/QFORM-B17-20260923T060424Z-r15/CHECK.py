import math

# Deterministic arithmetic/numerical checker for QFORM-B17 r15.
# The proof itself uses the exact rational certificate; Simpson integration
# below only checks the stated decimal value of the sharper integral bound.

def simpson(f, a, b, n=200000):
    assert n % 2 == 0
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a+i*h)
    return s*h/3

I = simpson(lambda th: 1.0/math.sqrt(math.sin(th)), math.pi/6, math.pi/2)
Cstar = 4*(math.pi/(6*math.sqrt(2)) + 0.5*I)
B0 = 2*math.pi*(1-1/math.sqrt(3)+1/(3*math.sqrt(2)))
target = 3*math.sqrt(2)
rat = 5148/1225
assert Cstar < B0 < rat < target
assert 5148**2 < 18*1225**2

def B(alpha, beta, gamma):
    tau = 0.5*math.sqrt(beta/gamma)
    if tau >= 1:
        return math.sqrt(2)*math.pi/math.sqrt(alpha*beta)
    th0 = math.asin(tau)
    integ = simpson(lambda th: 1.0/math.sqrt(math.sin(th)), th0, math.pi/2, 100000)
    return 4/math.sqrt(alpha) * (
        th0/math.sqrt(2*beta)
        + integ/(2*(beta*gamma)**0.25)
    )

samples = [
    (1,1,1), (1,2,1), (1,1,2), (2,1,1),
    (1,4,1), (1,5,1), (1,1,10), (1,10,1),
]
for p in samples:
    assert B(*p) <= Cstar + 2e-8

print(f'C_sep={Cstar:.15f}')
print(f'elementary_B0={B0:.15f}')
print(f'5148/1225={rat:.15f}')
print(f'3sqrt2={target:.15f}')
print(f'cert_difference={18*1225**2-5148**2}')
for p in samples:
    print(f'B{p}={B(*p):.15f}')
print('PASS')
