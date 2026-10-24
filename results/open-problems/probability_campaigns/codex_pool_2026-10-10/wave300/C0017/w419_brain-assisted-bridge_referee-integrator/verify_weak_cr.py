"""Deterministic finite-grid check of w418's abstract weak-CR obstruction."""
import json

out = []
for n in (1, 2, 4, 8):
    delta = 1/n
    max_residual = 0.0
    max_average_error = 0.0
    for j in range(1, n+1):
        for k in range(1, n+1):
            z = complex(j*delta, k*delta)
            e, w = (z+delta/2).conjugate(), (z-delta/2).conjugate()
            north, south = z+1j*delta/2, z-1j*delta/2
            max_residual = max(max_residual, abs(e-w+1j*(north-south)))
            max_average_error = max(max_average_error, abs((e+w+north+south)/4-z.real))
    # Along [0,1]^2, integral Re(z) dz equals i by explicit midpoint quadrature.
    path_integral = sum(((k+0.5)*delta)*delta for k in range(n))
    path_integral += sum(1*1j*delta for k in range(n))
    path_integral += sum((1-(k+0.5)*delta)*(-delta) for k in range(n))
    path_integral += sum(0*(-1j*delta) for k in range(n))
    out.append({"n":n,"max_weak_cr_residual":max_residual,"max_average_error":max_average_error,
                "integral_Re_z_dz": [path_integral.real,path_integral.imag]})
assert all(x["max_weak_cr_residual"] < 1e-12 and x["max_average_error"] < 1e-12 for x in out)
assert all(abs(x["integral_Re_z_dz"][1]-1) < 1e-12 for x in out)
print(json.dumps(out))
