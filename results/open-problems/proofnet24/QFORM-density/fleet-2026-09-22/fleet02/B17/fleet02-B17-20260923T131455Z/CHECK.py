import math
import numpy as np

K = math.pi/2*(math.sqrt(2)+2**0.25)
target = 3*math.sqrt(2)
assert (11/10)**4 < 2
assert math.pi < 22/7
assert K < target
print(f"K_star={K:.15f}")
print(f"3sqrt2={target:.15f}")
print(f"gap={target-K:.15f}")
print("analytic certificate: pi<22/7 and 2^(-1/4)<10/11 imply K_star<3sqrt2")

for m in (1,2,3,7):
    rng = np.random.default_rng(1700+m)
    a = rng.normal(size=m)
    a /= np.linalg.norm(a)
    A = np.zeros((1+2*m,1+2*m))
    A[0,0] = 1
    A[1:1+m,1:1+m] = np.outer(a,a)
    A[1+m:,1+m:] = -np.outer(a,a)
    ev = np.linalg.eigvalsh(A)
    nz = ev[np.abs(ev)>1e-10]
    assert np.allclose(nz,[-1,1,1],rtol=0,atol=2e-12)
    print(f"m={m}: nonzero spectrum {nz.tolist()}")

print("PASS QFORM-ONE-HEAVY-MAJORITY-ALL-BANKS-BARRIER-v1")
