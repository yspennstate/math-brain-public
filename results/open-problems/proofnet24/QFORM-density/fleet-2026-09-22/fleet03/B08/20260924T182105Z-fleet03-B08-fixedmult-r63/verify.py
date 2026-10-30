from fractions import Fraction as F
print(F(9424,244140625))
assert F(40,3)<F(121,9)
J=F(22,7)+F(347,125)
L=F(239,25)
H=1+F(11,3)*(J+2*L)
assert H==F(81208,875)
assert 10*H<929
assert F(400,1)<F(9,2)**4
I=20*(6+F(347,125)+L)+F(1,2)
assert I==F(18361,50) and I<368
k=F(4,625)
W=(1-9*k)*k*k
assert W==F(9424,244140625)
c2=(F(1,64)-F(1,100))**2/F(32,1)
assert c2==F(81,81920000)
print('QFORM_B08_R63_CHECK_PASS')
