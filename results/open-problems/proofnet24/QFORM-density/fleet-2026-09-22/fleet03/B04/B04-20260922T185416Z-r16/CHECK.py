import mpmath as mp

mp.mp.dps = 60
z = mp.findroot(lambda z: 4*z*mp.e**(-(z-2)) - 1, 5)
K2 = z + 1/z
K3 = z*z + 3 + 2/z
C3 = K3**(mp.mpf(1)/3)
Cstar = 2**(mp.mpf(5)/3) * C3
Ctwo = 2*K2
Cpivot2 = 4*mp.sqrt(K2)
print('z=', mp.nstr(z, 55))
print('K2=', mp.nstr(K2, 55))
print('K3=', mp.nstr(K3, 55))
print('K3^(1/3)=', mp.nstr(C3, 55))
print('Cstar=', mp.nstr(Cstar, 55))
print('two-bank=', mp.nstr(Ctwo, 55))
print('pivot-two-bank=', mp.nstr(Cpivot2, 55))
assert abs(4*z*mp.e**(-(z-2)) - 1) < mp.mpf('1e-50')
assert Cstar < mp.mpf('9.681')
