import math
import numpy as np

M = math.sqrt(2.0)
Aenv = 2*M + 8*math.log(3.0)
Benv = 4.0
gamma_E = 0.577215664901532860606512090082402431
Cmaj = (6/math.pi)*(2.5 + math.log(4/3) - gamma_E)
baseline = 3*math.sqrt(2.0)
assert Cmaj < baseline
assert abs(Benv - 4.0) < 1e-15

def transfer_modulus(delta):
    assert 0 < delta < 1
    Lam = Aenv + Benv*math.log(1/delta)
    return 4*math.sqrt(delta*Lam) + 4*math.sqrt(2)*Benv*math.sqrt(delta)

# The displayed modulus tends to zero.
assert transfer_modulus(1e-8) < transfer_modulus(1e-4) < transfer_modulus(1e-2)

# Check the exact stress spectrum numerically at representative bank sizes.
for m in (1,2,5,10):
    J = np.ones((m,m))/m
    Z1m = np.zeros((1,m)); Zm1 = np.zeros((m,1)); Zmm = np.zeros((m,m))
    Am = np.block([[np.array([[1.0]]), Z1m, Z1m],
                   [Zm1, J, Zmm],
                   [Zm1, Zmm, -J]])
    eig = np.linalg.eigvalsh(Am)
    nz = eig[np.abs(eig) > 1e-10]
    assert np.allclose(nz, [-1.0,1.0,1.0], atol=1e-12)

print('PASS QFORM-ONE-HEAVY-MAJORITY-EVENTUAL-NOOVERSHOOT-v1')
print('Cmaj=', repr(Cmaj))
print('3sqrt2=', repr(baseline))
print('gap=', repr(baseline-Cmaj))
print('Aenv=', repr(Aenv), 'Benv=', repr(Benv))
for d in (1e-2,1e-4,1e-8):
    print('delta', d, 'transfer_modulus', transfer_modulus(d))
