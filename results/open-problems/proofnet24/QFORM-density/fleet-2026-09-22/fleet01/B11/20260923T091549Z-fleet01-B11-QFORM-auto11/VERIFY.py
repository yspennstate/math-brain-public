import numpy as np, math

rng = np.random.default_rng(20260923)
max_det_err = 0.0
max_mass_err = 0.0
max_global_area_err = 0.0
max_incident_err = 0.0
min_L_over_sg = float("inf")
tests = 0

for signature in ("21", "12"):
    for n in (3, 5, 9, 17):
        for rep in range(12):
            R, _ = np.linalg.qr(rng.normal(size=(n, 3)))
            O, _ = np.linalg.qr(rng.normal(size=(3, 3)))
            if signature == "21":
                vals = np.array([1.0 + rng.random(),
                                 1.0 + rng.random(),
                                -(1.0 + rng.random())])
            else:
                vals = np.array([1.0 + rng.random(),
                                -(1.0 + rng.random()),
                                -(1.0 + rng.random())])
            M = O @ np.diag(vals) @ O.T
            A = R @ M @ R.T
            detM = np.linalg.det(M)
            s = np.min(np.abs(vals))

            gsum = 0.0
            incident = np.zeros(n)

            for i in range(n):
                for j in range(i + 1, n):
                    P = R[[i, j], :]
                    G = P @ P.T
                    g = float(np.linalg.det(G))
                    if g < 0 and g > -1e-12:
                        g = 0.0
                    gsum += g
                    incident[i] += g
                    incident[j] += g
                    if g <= 1e-12:
                        continue

                    B = P @ M @ P.T
                    nvec = np.cross(R[i], R[j])
                    det_rhs = detM * (nvec @ np.linalg.inv(M) @ nvec)
                    max_det_err = max(max_det_err,
                                      abs(np.linalg.det(B) - det_rhs))

                    extension_mass = 0.0
                    for k in range(n):
                        if k in (i, j):
                            continue
                        S = [i, j, k]
                        extension_mass += abs(
                            np.linalg.det(A[np.ix_(S, S)])
                        )
                    max_mass_err = max(
                        max_mass_err,
                        abs(extension_mass - abs(detM) * g)
                    )

                    ev, U = np.linalg.eigh(G)
                    Gmhalf = U @ np.diag(ev**(-0.5)) @ U.T
                    V = P.T @ Gmhalf
                    C = V.T @ M @ V
                    L = np.linalg.norm(B, 2)
                    min_L_over_sg = min(min_L_over_sg, L/(s*g))
                    assert np.linalg.norm(C, 2) + 1e-10 >= s
                    assert L + 1e-10 >= s*g
                    tests += 1

            max_global_area_err = max(max_global_area_err,
                                      abs(gsum - 3.0))
            h = np.sum(R*R, axis=1)
            max_incident_err = max(max_incident_err,
                                   np.max(np.abs(incident - 2*h)))

assert max_det_err < 1e-10
assert max_mass_err < 1e-10
assert max_global_area_err < 1e-10
assert max_incident_err < 1e-10
assert min_L_over_sg >= 1.0 - 1e-10

C_pair = 8*math.sqrt(5)*2**0.25
C_scalar = 128*math.sqrt(2)
C_partner = 32*math.sqrt(30)

print("tested_pairs", tests)
print("max_det_identity_error", f"{max_det_err:.3e}")
print("max_extension_mass_error", f"{max_mass_err:.3e}")
print("max_global_pair_area_error", f"{max_global_area_err:.3e}")
print("max_incident_pair_area_error", f"{max_incident_err:.3e}")
print("min_L_over_sg", f"{min_L_over_sg:.12f}")
print("pair_branch_constant", f"{C_pair:.12f}")
print("area_compiler_constant", f"{C_scalar:.12f}")
print("partner_three_bank_constant", f"{C_partner:.12f}")
print("QFORM_B11_PAIR_AREA_CHECK_PASS")
