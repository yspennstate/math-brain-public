import math

# Exact heavy-row clique stress, m even >= 130.
m = 130
tau = 1/128
d = 1/(2*m-1)
s = m/(2*m-1)
r2 = 2*m/(2*m-1)
a = (m-1)/(2*m-1)

# Two invariant 2x2 blocks have spectra {1,-r2} and {1,-s}.
eigs_active = [1.0, -r2, 1.0, -s]
max_pair_det = max(2*d, d, d*d)  # all physical diagonals vanish
ell0 = (2*m-1)/(3*m-1)
R_full = ((3*m-1)/(2*m-1))*r2
R_after_peel = s*r2
mixed_bound = 3*2**(4/3)*R_after_peel**(-1/3)

q = math.sqrt(tau+tau*tau)
mu = 1-tau-q
R0 = (1-tau)*mu*mu/4
diffuse_bound = 3*2**(4/3)*R0**(-1/3)

print(f"m={m}")
print(f"tau={tau:.15f}")
print(f"active eigenvalues={eigs_active}")
print(f"remaining leaf eigenvalue={-d:.15f} multiplicity={m-2}")
print(f"max physical pair determinant magnitude={max_pair_det:.15f}")
print(f"strict N3 pair gate={max_pair_det < tau}")
print(f"heavy full-frame leverage={ell0:.15f}")
print(f"full mixed determinant={R_full:.15f}")
print(f"residual mixed determinant after conditioning heavy row={R_after_peel:.15f}")
print(f"residual row leverage={2/m:.15f}")
print(f"one-row-peel density bound={mixed_bound:.15f}")
print(f"universal strict-N3 clique transversality floor R0={R0:.15f}")
print(f"diffuse-clique density bound from R0={diffuse_bound:.15f}")
