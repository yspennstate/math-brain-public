import itertools
import math
import numpy as np

th = math.pi/8
V = np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
M0 = np.array([[1.0,0.0],[0.0,1.0],[1.0,1.0]])
M = M0 @ V

# physical 2x2 squared minors
rows = list(itertools.combinations(range(3),2))
d2 = []
for S in rows:
    d = np.linalg.det(M[list(S),:])
    d2.append(d*d)
assert max(abs(x-1.0) for x in d2) < 1e-12
Z2 = sum(d2)
assert abs(Z2-3.0) < 1e-12

# exact triangle row-law combinatorics
cnt_empty_2 = 0
cnt_empty_3 = 0
for tup in itertools.product(rows, repeat=2):
    inter = set(tup[0]).intersection(tup[1])
    cnt_empty_2 += (len(inter)==0)
for tup in itertools.product(rows, repeat=3):
    inter = set(tup[0]).intersection(tup[1]).intersection(tup[2])
    cnt_empty_3 += (len(inter)==0)
assert cnt_empty_2 == 0
assert cnt_empty_3 == 6
assert abs(cnt_empty_3/27 - 2/9) < 1e-15
Omega3 = Z2**3 * (2/9)
assert abs(Omega3-6.0) < 1e-12

# singular/eigenvalue certificate
svals = np.linalg.svd(M, compute_uv=False)
assert np.max(np.abs(np.sort(svals)-np.array([1.0,math.sqrt(3)]))) < 1e-12
Axy = np.block([[np.zeros((3,3)), M],[M.T, np.zeros((2,2))]])
A = np.zeros((6,6))
A[0,0] = 1.0
A[1:,1:] = Axy
evals = np.linalg.eigvalsh(A)
expected = np.array([-math.sqrt(3),-1.0,0.0,1.0,1.0,math.sqrt(3)])
assert np.max(np.abs(evals-expected)) < 1e-12

# k=3 constant and final example bound
C3 = 6*(3**0.25)*math.sqrt(math.e)
bound = C3 * (Omega3**(-1/24))
assert abs(C3-13.019035313822702) < 1e-12
assert abs(bound-12.082473081510534) < 1e-12

print({
    "all_M_entries_nonzero": bool(np.all(np.abs(M)>1e-12)),
    "minor_squares": d2,
    "Z2": Z2,
    "delta2_row": cnt_empty_2/9,
    "delta3_row": cnt_empty_3/27,
    "Omega3_row": Omega3,
    "singular_values": svals.tolist(),
    "A_eigenvalues": evals.tolist(),
    "C3": C3,
    "density_bound": bound,
})
