from sympy import symbols, factor, sqrt
import mpmath as mp

x, c, beta = symbols("x c beta", positive=True)
p = c + 2
a = (c + 1) * (c**2 + c + 2) / (c + 2)**2
b = 2*c*(c + 1) / (c + 2)**2
majorant_gap = factor(
    (a*x**2 + b*x)*(2*x**2 + c) - x**2*(x + c)**2
)
target_gap = c*x*(x - 1)**2*(2*c**2*x + 2*c**2 + 3*c*x + 2*c + 2*x)/(c + 2)**2
assert factor(majorant_gap - target_gap) == 0
assert factor(a + b - (c + 1)**2/(c + 2)) == 0

s = symbols("s", positive=True)
delta = 1 - beta**2*s/2
Rstar = 1/(sqrt(2/s) - beta)
root_poly = factor(delta*Rstar**2 - beta*s*Rstar - s/2)
assert root_poly == 0

print("MAJORANT_FACTOR =", majorant_gap)
print("a_plus_b =", factor(a+b))
print("ROOT_IDENTITY =", root_poly)

mp.mp.dps = 100
for pv in ["2.1", "2.25", "2.5", "2.75", "2.9", "2.99", "2.999"]:
    pnum = mp.mpf(pv)
    snum = pnum - 1
    dnum = (3-pnum)/2
    rstar = 1/(mp.sqrt(2/snum)-1)
    exact_upper = (snum + mp.sqrt(snum*snum + 2*dnum*snum))/(2*dnum)
    err = abs(exact_upper-rstar)
    assert err < mp.mpf("1e-80")
    print(pv, "Rstar=upper=", mp.nstr(rstar, 24),
          "(3-p)Rstar=", mp.nstr((3-pnum)*rstar, 24),
          "identity_err=", mp.nstr(err, 3))
print("CHECK_PASS")
