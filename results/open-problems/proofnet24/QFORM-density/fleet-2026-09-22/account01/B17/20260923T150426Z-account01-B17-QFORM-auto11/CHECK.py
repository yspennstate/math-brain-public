import sympy as sp
import mpmath as mp

mp.mp.dps = 70

a = sp.Matrix([1,1])/sp.sqrt(2)
b = sp.Matrix([2,1,2])/3
A = sp.zeros(6)
A[0,0] = 1
A[1:3,1:3] = a*a.T
A[3:6,3:6] = -(b*b.T)
assert A**3 == A
assert sp.trace(A) == 1
assert sp.trace(A**2) == 3
assert A.eigenvals() == {sp.Integer(1):2, sp.Integer(0):3, sp.Integer(-1):1}

u = sp.Rational(1,2)
assert sp.simplify(1/sp.sqrt(2) - 1/(2*sp.sqrt(u))) == 0

Kcone = mp.pi*mp.sqrt(2)/3 + 2*mp.quad(lambda x: 1/(mp.sqrt(x)*mp.sqrt(1-x*x)), [mp.mpf('0.5'), 1])
Ksec = mp.pi*(5*mp.sqrt(2)-2)/3 - 2*mp.sqrt(3)*(mp.sqrt(2)-1)
Kpartner = mp.pi/2*(mp.sqrt(2)+mp.power(2, mp.mpf(1)/4))
target = 3*mp.sqrt(2)
assert Kcone < Ksec < target
assert Kcone < Kpartner < target
coarse = (40*mp.sqrt(2)+26)/21
assert Ksec < coarse < target
assert 23*mp.sqrt(2) > 26

print('QFORM_B17_ARBITRARY_HEAVY_UNEQUAL_BANK_SHARPENING_CHECK_PASS')
print('K_cone =', mp.nstr(Kcone, 40))
print('K_sec =', mp.nstr(Ksec, 40))
print('partner_K =', mp.nstr(Kpartner, 40))
print('3sqrt2 =', mp.nstr(target, 40))
print('gap_to_3sqrt2 =', mp.nstr(target-Kcone, 40))
print('improvement_over_partner =', mp.nstr(Kpartner-Kcone, 40))
print('coarse_gap_certificate = (23sqrt2-26)/21 =', mp.nstr((23*mp.sqrt(2)-26)/21, 40))
print('A =')
print(A)
