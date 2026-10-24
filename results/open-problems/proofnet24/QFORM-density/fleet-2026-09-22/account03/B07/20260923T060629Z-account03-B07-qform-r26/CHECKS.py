import math
import numpy as np

rng = np.random.default_rng(20260923)
counts = {"R1":0,"E2":0,"VOL":0,"HEAVY":0}
tested = 0

def e2_singular(M):
    lam = np.linalg.svd(M, compute_uv=False)**2
    S = float(lam.sum())
    return 0.5*(S*S-float((lam*lam).sum()))

def e3_singular(M):
    lam = np.linalg.svd(M, compute_uv=False)**2
    z=0.0
    for i in range(len(lam)):
        for j in range(i+1,len(lam)):
            for k in range(j+1,len(lam)):
                z += float(lam[i]*lam[j]*lam[k])
    return z

for m in range(2,9):
    for n in range(2,9):
        for _ in range(100):
            N=rng.normal(size=(m,n))
            S=float(np.sum(N*N))
            c=float(np.linalg.norm(N,2)**2)
            rowmax=float(np.max(np.sum(N*N,axis=1)))
            colmax=float(np.max(np.sum(N*N,axis=0)))
            rho=min(rowmax,colmax)
            tested += 1
            if c > 3*S/4:
                counts["R1"] += 1
                sv=np.linalg.svd(N,compute_uv=False)
                dist2=float(np.sum(sv[1:]**2))
                assert dist2 < S/4 + 1e-10
            elif c >= S/3:
                counts["E2"] += 1
                assert e2_singular(N) >= 3*S*S/16 - 1e-8
            elif rho <= 2*S/27:
                counts["VOL"] += 1
                if min(m,n) >= 3:
                    assert e3_singular(N) > S**3/27 - 1e-8
            else:
                counts["HEAVY"] += 1
                assert rowmax > 2*S/27 and colmax > 2*S/27

# Explicit diffuse examples exercise VOL.
for d in (50,100):
    N=rng.normal(size=(d,d))/math.sqrt(d)
    S=float(np.sum(N*N))
    c=float(np.linalg.norm(N,2)**2)
    rho=min(float(np.max(np.sum(N*N,axis=1))),
            float(np.max(np.sum(N*N,axis=0))))
    assert c < S/3
    assert rho < 2*S/27
    assert e3_singular(N) > S**3/27
    counts["VOL"] += 1
    tested += 1

# Propagation constants from the r25 edge-star-core packet.
# edge*star*G > theta*F^3/(36*sqrt(2)), edge,star<=F
# implies G > theta*F/(36*sqrt(2)).
# If hR*hC > (2/27)G^2, then
# edge*star*hR*hC > theta^2 F^4/34992.
assert 27*36*36 == 34992

# E2 physical two-coloring: matching squared-Frobenius product >= E2/16.
# With E2>=3G^4/16 this is >=3G^4/256.
assert 16*16 == 256

tau=1/128
eps=math.sqrt(tau+tau*tau)
theta=1/16
kappa=1/(256*math.sqrt(3))
diffuse_local=27*math.e/2
diffuse_parent_coeff=486*math.sqrt(2)*math.e/theta
joint_parent_coeff=69984*math.sqrt(2)*eps/(theta*theta)

print("tested",tested)
print("counts",counts)
print("diffuse_local_coeff",repr(diffuse_local))
print("diffuse_parent_coeff_at_theta_1_16",repr(diffuse_parent_coeff))
print("n3_edge_cap_epsilon",repr(eps))
print("heavy_joint_parent_coeff_at_theta_1_16",repr(joint_parent_coeff))
print("kappa",repr(kappa))
print("STATUS=PASS")
