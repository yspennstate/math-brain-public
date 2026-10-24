import math
import numpy as np

log5 = math.log(5.0)
Istar = 1152/25 + (48/5)*log5 + (144/25)*log5**2 + (32/25)*log5**3
Cstar = Istar/4
Dstar = 4*Cstar**(1/3)
partner = 8*(math.sqrt(5)-1)**(-1/4)

assert abs(Istar - 81.78688343097915) < 1e-12
assert abs(Cstar - 20.44672085774479) < 1e-12
assert abs(Dstar - 10.93791508120834) < 1e-12
assert partner < 7.588

m = 7
r = np.ones(m)/math.sqrt(m)
u = np.ones(m)/math.sqrt(m)
v = np.ones(m)/math.sqrt(m)
A = np.zeros((3*m, 3*m))
A[:m,:m] = np.outer(r,r)
A[m:2*m,2*m:3*m] = np.outer(u,v)
A[2*m:3*m,m:2*m] = np.outer(v,u)
eigs = np.linalg.eigvalsh(A)
nonzero = eigs[np.abs(eigs) > 1e-10]
assert np.allclose(nonzero, [-1,1,1], atol=1e-12)
assert abs(np.max(np.abs(A)) - 1/m) < 1e-12

print(f"Istar={Istar:.15f}")
print(f"Cstar={Cstar:.15f}")
print(f"Dstar={Dstar:.15f}")
print(f"partner={partner:.15f}")
print("nonzero_spectrum_m7=" + repr(nonzero.tolist()))
print(f"max_physical_coefficient_m7={np.max(np.abs(A)):.15f}")
print("STATUS=PASS")
