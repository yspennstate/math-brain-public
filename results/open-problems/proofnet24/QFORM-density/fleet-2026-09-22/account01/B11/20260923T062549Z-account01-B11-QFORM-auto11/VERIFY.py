import math
import numpy as np

C3 = 16*math.sqrt(30)*2**0.25
Cpair = 8*math.sqrt(5)*((1/8)*(math.sqrt(3/8)-1/2))**(-0.25)
Cbank = 2*C3
Cpartner = 32*math.sqrt(30)
assert Cpair < 51.962
assert C3 < 104.217
assert Cbank < 208.434
assert Cpartner < 175.272

H0 = np.array([[0.0,1.0,0.0],[1.0,0.0,0.0],[0.0,0.0,1.0]])
assert np.allclose(np.linalg.eigvalsh(H0), [-1.0,1.0,1.0])
B0 = np.array([[0.0,0.5],[0.5,0.0]])
assert abs(np.linalg.det(B0)+0.25) < 1e-12

# Nontrivial aligned-Schur regression: det(H)=det(B)*sigma.
B = np.array([[0.2,1.1],[1.1,-0.1]])
c = np.array([0.3,-0.4])
sigma = -1.7
d = float(c @ np.linalg.inv(B) @ c + sigma)
H = np.block([[B,c[:,None]],[c[None,:],np.array([[d]])]])
assert abs(np.linalg.det(H)-np.linalg.det(B)*sigma) < 1e-12

print('C3', C3)
print('Cpair', Cpair)
print('Cbank', Cbank)
print('Cpartner', Cpartner)
print('H0_eigenvalues', np.linalg.eigvalsh(H0))
print('aligned_det', np.linalg.det(H))
print('QFORM_B11_THREE_BANK_CHECK_PASS')
