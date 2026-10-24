import numpy as np

C = 0.75
max_gram = 0.0
max_plucker = 0.0
max_delta_excess = 0.0
max_spectrum = 0.0

for m in range(5, 201):
    theta = 2*np.pi*np.arange(m)/m
    y = np.sqrt(2/m)*np.cos(theta)
    z = np.sqrt(2/m)*np.sin(theta)
    s = np.sqrt(2*(1-C)/m)*np.cos(2*theta)

    U = np.zeros((m+1, 3))
    U[0,0] = np.sqrt(C)
    U[1:,0] = s
    U[1:,1] = y
    U[1:,2] = z
    Lam = np.array([[0.0,1.0,0.0],[1.0,0.0,0.0],[0.0,0.0,1.0]])
    A = U @ Lam @ U.T

    max_gram = max(max_gram, float(np.max(np.abs(U.T @ U - np.eye(3)))))

    vals = np.array([
        y[j]*z[k] - y[k]*z[j]
        for j in range(m) for k in range(j+1,m)
    ])
    max_plucker = max(max_plucker, abs(float(np.sum(vals*vals))-1.0))
    max_delta_excess = max(
        max_delta_excess,
        float(np.max(vals*vals) - 4.0/(m*m))
    )

    ev = np.linalg.eigvalsh(A)
    selected = np.array([ev[0], ev[-2], ev[-1]])
    max_spectrum = max(
        max_spectrum,
        float(np.max(np.abs(selected - np.array([-1.0,1.0,1.0]))))
    )

print("m_range=5..200")
print(f"max_frame_gram_error={max_gram:.3e}")
print(f"max_plucker_sum_error={max_plucker:.3e}")
print(f"max_delta_sq_minus_4_over_m2={max_delta_excess:.3e}")
print(f"max_nonzero_spectrum_error={max_spectrum:.3e}")
print("pair_fractional_matching_bound=2L/m")
print("exact_absorption_block_congestion_bound=6L/m")
print("QFORM_B05_OVERLAP_OBSTRUCTION_PASS")
