import math

Cstar=(16/9)*2**(3/8)
Ctime=2*math.gamma(1/4)*math.cos(math.pi/8)*Cstar
Chub=3*2**(4/3)*Cstar**(2/3)
kappa=(math.sqrt(5)-1)/2
Cfamily=Chub*kappa**(-1/6)
B_eigenvalues=[(1+math.sqrt(5))/2,(1-math.sqrt(5))/2]
total=B_eigenvalues+[1.0,-1.0]

print('Cstar', repr(Cstar))
print('Ctime', repr(Ctime))
print('Chub', repr(Chub))
print('kappa', repr(kappa))
print('Cfamily', repr(Cfamily))
print('B eigenvalues', B_eigenvalues)
print('total large eigenvalue count', sum(abs(x)>=1 for x in total))

assert abs(Cstar-2.3054925416017946)<1e-14
assert abs(Ctime-15.445079149508198)<1e-13
assert abs(Chub-13.192802571602053)<1e-13
assert abs(Cfamily-14.294479188689092)<1e-13
assert sum(abs(x)>=1 for x in total)==3
assert abs(B_eigenvalues[0]*B_eigenvalues[1]+1)<1e-14
print('QFORM_B03_ZERO_HUB_QUARTER_RIESZ_PASS')
