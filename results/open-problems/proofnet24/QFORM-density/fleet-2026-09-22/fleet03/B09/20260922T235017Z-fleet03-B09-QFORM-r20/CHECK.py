import math
import numpy as np

A=np.array([
 [0.,1.,0.,0.,0.],
 [1.,0.,0.,1.,0.],
 [0.,0.,0.,0.,1.],
 [0.,1.,0.,0.,0.],
 [0.,0.,1.,0.,0.],
])
e=np.linalg.eigvalsh(A)
want=np.array([-math.sqrt(2),-1.,0.,1.,math.sqrt(2)])
assert np.allclose(e,want,atol=1e-12), (e,want)
peer_const=3*math.exp(5/6)
sharp_const=3*2**(5/6)
assert peer_const < 6.903
assert sharp_const < 5.346
print('spectrum=',e)
print('3e^(5/6)=',peer_const)
print('3*2^(5/6)=',sharp_const)
print('QFORM_B09_R20_LINEAR_PIVOT_CHECK_PASS')
