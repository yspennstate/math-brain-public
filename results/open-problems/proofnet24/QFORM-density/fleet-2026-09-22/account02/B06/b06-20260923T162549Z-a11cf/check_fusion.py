import itertools, math
from fractions import Fraction
import numpy as np

def ek_psd(G, k):
    vals = np.linalg.eigvalsh(G)
    total = 0.0
    for inds in itertools.combinations(range(len(vals)), k):
        p = 1.0
        for i in inds:
            p *= vals[i]
        total += p
    return total

def fused_minor_sum(V, M, k):
    r = V.shape[1]
    nI, nJ = M.shape
    z = 0.0
    for S in itertools.combinations(range(nI), r+k):
        for T in itertools.combinations(range(nJ), k):
            B = np.column_stack([V[list(S), :], M[np.ix_(S, T)]])
            z += np.linalg.det(B)**2
    return z

rng = np.random.default_rng(20260923)
max_rel = 0.0
for nI, nJ, r, k in [(7,5,1,1),(8,6,1,2),(9,5,2,1)]:
    Q, _ = np.linalg.qr(rng.normal(size=(nI,r)))
    V = Q[:, :r]
    M = rng.normal(size=(nI,nJ))
    z1 = fused_minor_sum(V,M,k)
    P = np.eye(nI)-V@V.T
    z2 = ek_psd(M.T@P@M,k)
    rel = abs(z1-z2)/max(1.0,abs(z2))
    max_rel=max(max_rel,rel)
assert max_rel < 1e-12

A3 = np.array([[1.0,0.0,0.0],[0.0,0.0,math.sqrt(2.0)],[0.0,math.sqrt(2.0),1.0]])
eigs=np.linalg.eigvalsh(A3)
assert np.max(np.abs(eigs-np.array([-1.0,1.0,2.0]))) < 1e-12

c3=Fraction(11907,16384)
z2_floor=Fraction(31,2048)*c3*c3
diag=4*math.sqrt(math.e)*float(z2_floor)**(-0.25)
rank1=3*(2**(4/3))*math.e**(1/3)*(64/float(c3))**(1/3)
family=6*math.e**(1/3)

print("max_cauchy_binet_relative_error", format(max_rel, ".3e"))
print("target_family_eigenvalues", [round(float(x),12) for x in eigs])
print("partner_Z2_floor", format(float(z2_floor), ".15f"))
print("diagonal_bank_bound", format(diag, ".12f"))
print("rank1_plus_diagonal_bound", format(rank1, ".12f"))
print("diffuse_exact_target_bound", format(family, ".12f"))
