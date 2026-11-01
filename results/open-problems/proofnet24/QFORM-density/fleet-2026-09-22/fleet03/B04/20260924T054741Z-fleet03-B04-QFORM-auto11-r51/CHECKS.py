import math
import sympy as sp

B=sp.Matrix([[1,1,1],[1,1,-1],[1,-1,1]])
assert B.det()==-4
assert sp.factor(B.charpoly().as_expr())==(sp.Symbol('lambda')-2)**2*(sp.Symbol('lambda')+1)
for inds in [(0,1),(0,2),(1,2)]:
    assert B.extract(inds,inds).det()==0

Cpair=2+2*math.pi
C3new=6*Cpair
C3old=16*(2**0.25)*math.sqrt(30)
assert abs(C3new-49.69911184307752)<1e-12
assert C3new<C3old
assert abs(C3new/C3old-0.4768815481657328)<1e-12
assert abs(C3new*4**(-1/3)-31.308478586086476)<1e-12
assert abs(C3new*24**(1/3)-143.35704540067675)<1e-12
assert abs(129.924435862525374*288**(1/6)-333.879371828014)<1e-9

# Square small-ball constant: H=2sqrt(2), 3 H^(2/3)=6 exactly.
H=2*math.sqrt(2)
assert abs(3*H**(2/3)-6)<1e-12

# Partner splice coefficient from K_ab^2>(4/75)D2 E4 and r50 constant 3*2^(5/6).
partner=(3*2**(5/6))*(4/75)**(-1/12)
assert abs(partner-6.824377206888847)<1e-12

print('QFORM_B04_R51_TRIPLE_DET_ONE_THIRD_CHECK_PASS')
print('Cpair=',repr(Cpair))
print('C3new=',repr(C3new))
print('C3old=',repr(C3old))
print('ratio=',repr(C3new/C3old))
print('example=',repr(C3new*4**(-1/3)))
print('exact_rank3_caseB=',repr(C3new*24**(1/3)))
print('exact_rank3_caseA=',repr(129.924435862525374*288**(1/6)))
print('partner=',repr(partner))
