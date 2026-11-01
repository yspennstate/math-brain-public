import math
import numpy as np


def stress(k=3.0, eta=0.2, m=100):
    n = 3 + 2*m
    A = np.zeros((n,n))
    u = np.ones(m)/math.sqrt(m)
    v = np.ones(m)/math.sqrt(m)
    A[0,2] = A[2,0] = eta
    A[0,3:3+m] = k*u
    A[3:3+m,0] = k*u
    A[1,3+m:] = k*v
    A[3+m:,1] = k*v
    ev = np.linalg.eigvalsh(A)
    return ev[np.abs(ev)>1e-10], max(eta**2,k*k/m)

nz,maxpair = stress()

e = np.array([1.0,1.0])/math.sqrt(2)
q = np.array([1.0,-1.0])/math.sqrt(2)
w = e.copy()
Ap = np.zeros((6,6))
Ap[0,0] = 1.0
Ap[1,4:6] = e
Ap[4:6,1] = e
Ap[2:4,4:6] = np.outer(w,q)
Ap[4:6,2:4] = np.outer(q,w)

ev_partner = np.linalg.eigvalsh(Ap)

Ao = np.array([
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]], dtype=float)
ev_obstruction = np.linalg.eigvalsh(Ao)

print('C=', 2*math.sqrt(math.pi))
print('stress_nz=', ['%.12g'%x for x in nz])
print('stress_max_abs_2x2_det=', maxpair)
print('partner_ev=', ['%.12g'%x for x in ev_partner])
print('obstruction_ev=', ['%.12g'%x for x in ev_obstruction])

assert np.max(np.abs(np.sort(nz)-np.array([-math.sqrt(9.04),-3,3,math.sqrt(9.04)]))) < 1e-10
assert maxpair == 0.09
assert np.max(np.abs(np.sort(ev_partner)-np.array([-1,-1,0,1,1,1]))) < 1e-10
assert np.max(np.abs(np.sort(ev_obstruction)-np.array([-2,0,0,2]))) < 1e-10
print('STATUS=PASS')
