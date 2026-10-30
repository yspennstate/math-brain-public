import math


def bound(a,b):
    a=abs(a); b=abs(b)
    if b <= 4*a:
        return (2+math.log(4*a/b))/a
    return 4/math.sqrt(a*b)

C = 2 + math.log(4)
gap = 3*math.sqrt(2)-C
assert C < 3.5
assert 3.5 < 3*math.sqrt(2)
for a in (1.0,2.0,7.0):
    left=(2+math.log(4*a/(4*a)))/a
    right=4/math.sqrt(a*4*a)
    assert abs(left-right) < 1e-12
mx=(0.0,None)
for i in range(500):
    a=1+9*i/499
    for j in range(500):
        b=1+9*j/499
        z=bound(a,b)
        if z>mx[0]:
            mx=(z,(a,b))
assert mx[0] <= C + 1e-12
print('PASS QFORM-NULLPAIR-SQUARE-SHARPENED')
print('C =',C)
print('3sqrt2-C =',gap)
print('target_grid_max =',mx)
