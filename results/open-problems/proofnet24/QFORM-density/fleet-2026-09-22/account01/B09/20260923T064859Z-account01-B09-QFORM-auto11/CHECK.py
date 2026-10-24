import math
import numpy as np

eta = 1/16
c_eta = (1-eta)/math.sqrt(6)
C = 2**(11/4)
assert abs(c_eta - 0.3827327723098716) < 1e-14
assert C / math.sqrt(c_eta*(1/8)) < 30.756
assert C / math.sqrt(c_eta*(1/8)/math.sqrt(2)) < 36.576
assert C / (4**0.25) < 4.757

A = np.array([[1.,1.,0.],[1.,1.,2.],[0.,2.,1.]])
ev = np.linalg.eigvalsh(A)
expected = np.array([1-math.sqrt(5),1.,1+math.sqrt(5)])
assert np.max(np.abs(ev-expected)) < 1e-12
assert np.min(np.abs(ev)) >= 1-1e-12

a,b,d = A[0,0],A[0,1],A[1,1]
assert abs(a*d-b*b) < 1e-14
u = A[0,2:]
v = A[1,2:]
g = a*v-b*u
assert abs(float(g@g)-4.0) < 1e-14
z = np.array([-b,a,0.])
assert np.max(np.abs(A@z - np.array([0.,0.,2.]))) < 1e-14
print('CHECK_PASS', ev, c_eta, C/math.sqrt(2))
