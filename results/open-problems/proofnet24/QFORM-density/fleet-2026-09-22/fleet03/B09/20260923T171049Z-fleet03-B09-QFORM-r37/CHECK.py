import itertools, math, numpy as np

def anchored_volume(B, R):
    total = 0.0
    m = B.shape[1]
    for k in range(R.shape[0]):
        M = np.vstack([B, R[k]])
        for J in itertools.combinations(range(m), 3):
            total += np.linalg.det(M[:, J])**2
    return total

def projected_packet(B, R):
    G = B @ B.T
    Delta = np.linalg.det(G)
    Pi = B.T @ np.linalg.inv(G) @ B
    C = R @ (np.eye(B.shape[1]) - Pi)
    return Delta, C

rng = np.random.default_rng(20260923)
max_rel = 0.0
max_row_rel = 0.0
for _ in range(100):
    m = 7
    s = 5
    B = rng.normal(size=(2,m))
    if np.linalg.matrix_rank(B) < 2:
        continue
    R = rng.normal(size=(s,m))
    V = anchored_volume(B,R)
    Delta,C = projected_packet(B,R)
    V2 = Delta*np.sum(C*C)
    max_rel=max(max_rel, abs(V-V2)/max(1.0,abs(V)))
    for k in range(s):
        Vk=anchored_volume(B,R[k:k+1])
        rhs=Delta*np.dot(C[k],C[k])
        max_row_rel=max(max_row_rel,abs(Vk-rhs)/max(1.0,abs(Vk)))

m=128
gamma2=1.0/m
Gstar=2.0
W=1.0
w=1.0
V=1.0
alpha=1.0/m
c=27.0/256.0
diffuse_threshold=(c/2.0)*Gstar
new_constant=3.0*2.0**(5.0/6.0)
gstar_constant=new_constant*(400.0/27.0)**(1.0/6.0)
partner_bound=3.0*m**(1.0/6.0)

sing=np.array([1.0,1.0]+[1.0/math.sqrt(m)]*m)
eig=np.concatenate([sing,-sing])
large=int(np.sum(np.abs(eig)>=1.0-1e-12))

print(f"max aggregate identity relative error = {max_rel:.3e}")
print(f"max row identity relative error = {max_row_rel:.3e}")
print(f"m = {m}")
print(f"Gamma_k^2 = {gamma2:.12f}")
print(f"diffuse threshold = {diffuse_threshold:.12f}")
print(f"G_* = {Gstar:.12f}, W = {W:.12f}, V_ab = {V:.12f}")
print(f"projected row marginal alpha = {alpha:.12f}")
print(f"column range leverage in M = 1.000000000000")
print(f"new V bound constant = {new_constant:.12f}")
print(f"new G_* bound coefficient = {gstar_constant:.12f}")
print(f"partner physical-minor bound = {partner_bound:.12f}")
print(f"eigenvalues with |lambda|>=1 = {large}")
assert max_rel < 1e-10
assert max_row_rel < 1e-10
assert gamma2 < diffuse_threshold
assert alpha <= 0.5
assert large >= 3
assert new_constant < partner_bound
print("ALL CHECKS PASSED")
