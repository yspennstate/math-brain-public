#!/usr/bin/env python3
import math
import numpy as np

E = math.e
C_SCALAR = 128.0 * (2.0 ** (1.0/8.0)) * (E ** (9.0/8.0))
C_PAIR = 3.0 * (400.0 ** (1.0/3.0)) * (2.0 ** (7.0/12.0)) * (E ** (7.0/12.0))

def harmonic_frame(m, h=0.75):
    theta = 2*np.pi*np.arange(m)/m
    residual = np.column_stack([
        np.full(m, math.sqrt((1.0-h)/m)),
        math.sqrt(2.0/m)*np.cos(theta),
        math.sqrt(2.0/m)*np.sin(theta),
    ])
    return np.vstack(([math.sqrt(h), 0.0, 0.0], residual))

M = np.array([[0.0,1.0,0.0],[1.0,0.0,0.0],[0.0,0.0,1.0]])

assert abs(C_SCALAR - 429.9520373799586) < 1e-9
assert abs(C_PAIR - 59.34906259245628) < 1e-9
assert max(C_SCALAR*0.5**(-0.75), C_PAIR*0.5**(-5.0/6.0)) < 724.0
assert max(C_SCALAR*0.25**(-0.75), C_PAIR*0.25**(-5.0/6.0)) < 1217.0

for m in (8,16,32,64,128):
    C = harmonic_frame(m)
    assert np.max(np.abs(C.T@C - np.eye(3))) < 1e-12
    B = C@M@C.T
    ev = np.linalg.eigvalsh(B)
    nz = ev[np.abs(ev) > 1e-9]
    assert len(nz) == 3
    assert np.max(np.abs(np.sort(nz) - np.array([-1.0,1.0,1.0]))) < 1e-10
    alpha = np.max(np.abs(C[1:,1]))
    assert abs(alpha - math.sqrt(2.0/m)) < 1e-12
    assert np.max(np.abs(B[0,1:])) <= math.sqrt(1.5/m) + 1e-12
    assert np.max(np.abs(np.diag(B)[1:])) <= 3.0/m

# Small coefficient perturbation does not control random output error without moments/support.
for epsilon, L in ((1e-2,10.0),(1e-4,100.0),(1e-6,1000.0)):
    R = L/(2.0*epsilon)
    oscillation = epsilon*((R+1.0)**2-R**2)
    assert oscillation >= L

print(f"C_SCALAR={C_SCALAR:.12f}")
print(f"C_PAIR={C_PAIR:.12f}")
print(f"alpha_half_bound={max(C_SCALAR*0.5**(-0.75), C_PAIR*0.5**(-5.0/6.0)):.12f}")
print(f"alpha_quarter_bound={max(C_SCALAR*0.25**(-0.75), C_PAIR*0.25**(-5.0/6.0)):.12f}")
print("harmonic alpha m=128 =", math.sqrt(2.0/128.0))
print("QFORM_RAY_ATOM_COMPILER_CHECK_PASS")
