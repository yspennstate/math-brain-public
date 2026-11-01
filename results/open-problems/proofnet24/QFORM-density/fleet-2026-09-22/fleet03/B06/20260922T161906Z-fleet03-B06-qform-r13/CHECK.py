import math
import numpy as np

# Fully coupled branch witness from REPORT.md.
A=np.array([[2.0,1.0,-2.0],[1.0,0.5,2.0],[-2.0,2.0,2.0]])
a=A[0,0]
d12=a*A[1,1]-A[0,1]**2
d13=a*A[2,2]-A[0,2]**2
S=A[1:,1:]-np.outer(A[1:,0],A[0,1:])/a
ev=np.linalg.eigvalsh(A)

assert abs(d12)<1e-12 and abs(d13)<1e-12
assert np.max(np.abs(S-np.array([[0.0,3.0],[3.0,0.0]])))<1e-12
assert np.min(np.abs(ev))>1.0

# Constants in Theorem 4.1.
C0=(65*math.e**2)**(1/3)
Cstar=(8/(3**(3/4)))*(65*math.e**2)**(1/4)
Cheavy=Cstar*12**(1/4)
assert C0 < 7.832
assert Cstar < 16.430
assert Cheavy < 30.579

# Exact branch identity for the witness: sum second minors = a tr(A)-(A^2)_ii = 0.
identity=a*np.trace(A)-(A@A)[0,0]
assert abs(identity)<1e-12

print('d12=',d12)
print('d13=',d13)
print('Schur=',S.tolist())
print('eigenvalues=',ev.tolist())
print('identity=',identity)
print('C0=',C0)
print('Cstar=',Cstar)
print('Cheavy=',Cheavy)
print('PASS')
