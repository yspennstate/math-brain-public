import math
import numpy as np

delta = 1.0/16.0
bernstein_fail_bound = 4.0*math.exp(-3.0/(28.0*delta))
assert bernstein_fail_bound < 1.0

m = 32
c = 3.0/4.0
theta = 2.0*np.pi*np.arange(m)/m
z = np.sqrt(2.0/m)*np.column_stack((np.cos(theta), np.sin(theta)))
r0 = np.array([[math.sqrt(c),0.0,0.0]])
res = np.column_stack((
    np.full(m, 1.0/(2.0*math.sqrt(m))),
    z
))
R = np.vstack((r0,res))
M = np.array([[0.0,1.0,0.0],[1.0,0.0,0.0],[0.0,0.0,1.0]])
A = R @ M @ R.T

assert np.max(np.abs(R.T@R - np.eye(3))) < 1e-12
evals = np.linalg.eigvalsh(A)
nz = evals[np.abs(evals)>1e-10]
assert np.max(np.abs(np.sort(nz)-np.array([-1.0,1.0,1.0]))) < 1e-10
assert np.max(np.abs(z.T@z - np.eye(2))) < 1e-12

S = np.arange(0,m,2)
T = np.arange(1,m,2)
GS = z[S].T@z[S]
GT = z[T].T@z[T]
assert np.max(np.abs(GS-0.5*np.eye(2))) < 1e-12
assert np.max(np.abs(GT-0.5*np.eye(2))) < 1e-12

wedge_cross = 0.0
minor_cross = 0.0
minor_all = 0.0
minor_max = 0.0
for i in range(m):
    for j in range(i+1,m):
        d = np.linalg.det(np.vstack((z[i],z[j])))**2
        val = c*d
        minor_all += val
        minor_max = max(minor_max,val)
for i in S:
    for j in T:
        d = np.linalg.det(np.vstack((z[i],z[j])))**2
        wedge_cross += d
        minor_cross += c*d

assert abs(wedge_cross-0.5) < 1e-12
assert abs(minor_all-c) < 1e-12
assert abs(minor_cross-c/2.0) < 1e-12
assert abs(minor_max-3.0/m**2) < 1e-12

print("delta", delta)
print("matrix_bernstein_two_sided_bound", repr(bernstein_fail_bound))
print("max_parseval_error", repr(float(np.max(np.abs(R.T@R-np.eye(3))))))
print("nonzero_spectrum", [float(x) for x in nz])
print("GS_eigs", [float(x) for x in np.linalg.eigvalsh(GS)])
print("GT_eigs", [float(x) for x in np.linalg.eigvalsh(GT)])
print("cross_wedge_energy", repr(wedge_cross))
print("all_principal_minor_mass", repr(minor_all))
print("cross_principal_minor_mass", repr(minor_cross))
print("max_abs_principal_minor", repr(minor_max))
print("theoretical_max_abs_principal_minor", repr(3.0/m**2))
print("QFORM_DIFFUSE_WEDGE_PARTITION_CHECK_PASS")
