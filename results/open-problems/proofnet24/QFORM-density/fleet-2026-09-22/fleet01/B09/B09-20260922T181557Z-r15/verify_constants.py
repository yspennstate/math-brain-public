import math
import numpy as np

delta0 = 2/(3+math.sqrt(5))
Cdiff = 4*math.sqrt(2*math.e)
Crd = 32*math.sqrt(10)*2**0.25
partner = 11.8757032583/math.sqrt((1/312)*delta0)
diff_target = Cdiff/math.sqrt((1/312)*(delta0/4))
onebank_target = Crd/math.sqrt((1/312)*(delta0/4))
pair_const = 128*(16**0.25)

assert partner < 340
assert diff_target < 534
assert onebank_target < 6879
assert abs(pair_const-256) < 1e-12

rng = np.random.default_rng(20260922)
errs=[]
for _ in range(100):
    mp=int(rng.integers(2,8)); mn=int(rng.integers(2,8))
    p=rng.normal(size=mp); p/=np.linalg.norm(p)
    q=rng.normal(size=mn); q/=np.linalg.norm(q)
    gamma=float(rng.uniform(.1,3))
    H=np.zeros((mp+mn,mp+mn))
    H[:mp,mp:]=gamma*np.outer(p,q)
    H[mp:,:mp]=gamma*np.outer(q,p)
    ev=np.linalg.eigvalsh(H)
    errs.append(max(abs(ev[-1]-gamma),abs(ev[0]+gamma),np.max(np.abs(np.diag(H)))))
maxerr=max(errs)
assert maxerr < 1e-12

print(f"delta0={delta0:.15f}")
print(f"Cdiff={Cdiff:.15f}")
print(f"C_RD={Crd:.15f}")
print(f"partner_target_bound={partner:.15f}")
print(f"diffuse_target_bound={diff_target:.15f}")
print(f"onebank_diffuse_target_bound={onebank_target:.15f}")
print(f"pair_gate_constant={pair_const:.15f}")
print(f"rank2_bipartite_max_numeric_error={maxerr:.3e}")
print("STATUS=PASS")
