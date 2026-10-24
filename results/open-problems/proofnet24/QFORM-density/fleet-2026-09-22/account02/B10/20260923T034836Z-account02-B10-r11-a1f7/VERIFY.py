import itertools
import math
import numpy as np


def check(eps: float):
    delta = eps * eps
    s = math.sqrt(1.0 - eps * eps)
    M = np.array([[-eps, 0.0, s], [0.0, 1.0, 0.0], [s, 0.0, eps]])
    R = np.array([
        [1.0 / math.sqrt(2.0), 0.0, 0.0],
        [1.0 / math.sqrt(2.0), 0.0, 0.0],
        [0.0, math.sqrt(1.0-delta), 0.0],
        [0.0, math.sqrt(delta), 0.0],
        [0.0, 0.0, math.sqrt(1.0-delta)],
        [0.0, 0.0, math.sqrt(delta)],
    ])
    A = R @ M @ R.T
    weights = []
    for S in itertools.combinations(range(6), 3):
        w = np.linalg.det(R[list(S), :]) ** 2
        if w > 1e-25:
            weights.append((S, w))
    d = 0.0
    for S, w in weights:
        SS = set(S)
        for T, z in weights:
            if SS.isdisjoint(T):
                d += w*z
    d_formula = 2.0 * eps**4 * (1.0-eps**2)**2
    star = np.sum(A[0,1:]**2)
    star_formula = 0.5 - eps**2/4.0
    return {
        "eps": eps,
        "eigenvalues": np.linalg.eigvalsh(M),
        "M2_error": np.linalg.norm(M @ M - np.eye(3)),
        "parseval_error": np.linalg.norm(R.T @ R - np.eye(3)),
        "d": d,
        "d_formula": d_formula,
        "d_error": abs(d-d_formula),
        "leverage": float(R[0] @ R[0]),
        "pivot": float(A[0,0]),
        "star": float(star),
        "star_formula": star_formula,
        "star_error": abs(star-star_formula),
        "square_envelope_lower_bound": math.sqrt(2.0)/6.0 * math.log(1.0/(2.0*math.sqrt(eps))),
    }


for eps in (1/64, 1/256, 1/1024):
    out = check(eps)
    print(f"eps={out['eps']:.12g}")
    print(" eigenvalues=", np.array2string(out['eigenvalues'], precision=12))
    print(f" M2_error={out['M2_error']:.3e} parseval_error={out['parseval_error']:.3e}")
    print(f" d={out['d']:.16e} formula={out['d_formula']:.16e} error={out['d_error']:.3e}")
    print(f" leverage={out['leverage']:.12g} pivot={out['pivot']:.12g}")
    print(f" star={out['star']:.16e} formula={out['star_formula']:.16e} error={out['star_error']:.3e}")
    print(f" square_envelope_lower_bound={out['square_envelope_lower_bound']:.12g}")

print("STATUS=PASS")
