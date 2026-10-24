import math


def simpson(f, a, b, n):
    if n % 2:
        n += 1
    h = (b-a)/n
    s = f(a)+f(b)
    for i in range(1,n):
        s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3

# Exact Holder-constant collapse, sampled over several c.
for c in [0.5, 0.75, 1.0, 2.0, 10.0, 100.0]:
    K = 1.0 + 1.0/(2.0*c)
    q0 = K/(K-1.0)
    assert math.isclose(q0, 2.0*c+1.0, rel_tol=1e-13, abs_tol=1e-13)
    base_gauss = 12.0*math.pi*c/q0
    base_sinc = 6.0*math.pi/K
    assert math.isclose(base_gauss, base_sinc, rel_tol=1e-13, abs_tol=1e-13)
    holder = math.sqrt(6.0*math.pi/K)/(2.0*math.sqrt(3.0*math.pi*c))
    gaussian = 1.0/math.sqrt(1.0+2.0*c)
    assert math.isclose(holder, gaussian, rel_tol=1e-14, abs_tol=1e-14)

# The leverage threshold: a_i^2 <=4/9 implies q_i=K/a_i^2>=9/4 for all c>=1/2.
for c in [0.5, 1.0, 10.0, 1e6]:
    K = 1.0 + 1.0/(2.0*c)
    q = K/(4.0/9.0)
    assert q > 2.25 or math.isclose(q, 2.25, rel_tol=1e-6, abs_tol=1e-6)

# Numerically verify the final elementary K0-mixture comparison integral.
f = lambda u: 1.0/math.sqrt(1.0+math.cosh(u))
# Tail is exponentially small by u=40.
I = simpson(f, 0.0, 40.0, 200000)
target = math.pi/math.sqrt(2.0)
assert abs(I-target) < 2e-8, (I,target)

print('PASS')
print('integral', format(I,'.15f'))
print('pi/sqrt(2)', format(target,'.15f'))
print('3sqrt(2)', format(3.0*math.sqrt(2.0),'.15f'))
print('scope: algebra/normalization check only; Koenig-Koldobsky sinc inequality is external analytic input')
