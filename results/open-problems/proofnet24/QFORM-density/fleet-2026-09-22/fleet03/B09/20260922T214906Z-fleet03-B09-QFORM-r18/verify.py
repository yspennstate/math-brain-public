import math
import numpy as np

Cdef = 2**(5/4) * math.sqrt(math.pi) * math.e**(3/4)
stress = Cdef * 2**0.25
print('C_def =', Cdef)
print('stress_bound =', stress)

for delta in [0.2, 0.1, 0.05]:
    R = math.exp(1/(4*delta*delta))
    volume = 4*delta*delta*math.log(R)
    lower = 1/(4*delta)
    print('delta=', delta, 'E_delta_volume=', volume, 'density_lower_bound=', lower)

M = np.array([
    [0.0, 1.0, 0.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 0.5],
])
print('stress_eigenvalues =', np.linalg.eigvalsh(M))

assert Cdef < 8.925
assert stress < 10.614
assert np.allclose(np.linalg.eigvalsh(M), [-1.0, 0.5, 1.0, 1.0])
for delta in [0.2, 0.1, 0.05]:
    R = math.exp(1/(4*delta*delta))
    assert abs(4*delta*delta*math.log(R)-1) < 1e-12
print('all checks passed')
