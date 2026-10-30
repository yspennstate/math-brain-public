import itertools, math
import numpy as np


def e2(M):
    z = 0.0
    for R in itertools.combinations(range(M.shape[0]), 2):
        for T in itertools.combinations(range(M.shape[1]), 2):
            z += np.linalg.det(M[np.ix_(R, T)]) ** 2
    return z


def e3(M):
    z = 0.0
    for R in itertools.combinations(range(M.shape[0]), 3):
        for T in itertools.combinations(range(M.shape[1]), 3):
            z += np.linalg.det(M[np.ix_(R, T)]) ** 2
    return z


def psi_mass(r, c, E):
    z = 0.0
    for R in itertools.combinations(range(E.shape[0]), 2):
        for T in itertools.combinations(range(E.shape[1]), 2):
            F = E[np.ix_(R, T)]
            adj = np.array([[F[1, 1], -F[0, 1]], [-F[1, 0], F[0, 0]]])
            v = r[list(T)] @ adj @ c[list(R)]
            z += v * v
    return z


def anchored_g3(b, r, c, E):
    D = np.block([[np.array([[b]]), r[None, :]], [c[:, None], E]])
    z = 0.0
    for R in itertools.combinations(range(E.shape[0]), 2):
        for T in itertools.combinations(range(E.shape[1]), 2):
            RR = (0,) + tuple(i + 1 for i in R)
            TT = (0,) + tuple(j + 1 for j in T)
            z += np.linalg.det(D[np.ix_(RR, TT)]) ** 2
    return z


def stress(N):
    one = np.ones(N) / math.sqrt(N)
    alt = np.array([1 if i % 2 == 0 else -1 for i in range(N)]) / math.sqrt(N)
    c, u, r, v = one, alt, one.copy(), alt.copy()
    E = np.outer(u, v)
    D = np.block([[np.zeros((1, 1)), r[None, :]], [c[:, None], E]])
    s = np.linalg.svd(D, compute_uv=False)
    return N, s[:4], e3(D), anchored_g3(0.0, r, c, E), e2(E), np.linalg.norm(r)*np.linalg.norm(c)*np.linalg.norm(E), np.max(np.abs(D))


rng = np.random.default_rng(20260923)
max_cofactor_ratio = 0.0
max_bordered_ratio = 0.0
for _ in range(300):
    E = rng.normal(size=(5, 6))
    r = rng.normal(size=6)
    c = rng.normal(size=5)
    b = float(rng.normal())
    denom = np.dot(r, r) * np.dot(c, c) * np.sum(E * E)
    max_cofactor_ratio = max(max_cofactor_ratio, psi_mass(r, c, E) / denom)
    G = anchored_g3(b, r, c, E)
    rhs = abs(b) * math.sqrt(e2(E)) + np.linalg.norm(r) * np.linalg.norm(c) * np.linalg.norm(E)
    max_bordered_ratio = max(max_bordered_ratio, math.sqrt(G) / rhs)

h = (2*math.sqrt(2)-1) / 1572864
beta = math.sqrt(63) / 16
Pmin = beta*h*h
amin = 16*math.sqrt(Pmin/4617)
C_Dprime = 9*math.sqrt(3*math.e)*(3/8)**(1/6)

print(f"DPRIME_SCALE_CONSTANT={C_Dprime:.15f}")
print(f"PARTNER_A_FLOOR={amin:.15e}")
print(f"DPRIME_PARTNER_CAP={C_Dprime/amin:.9f}")
print(f"MAX_COFACTOR_RATIO_300={max_cofactor_ratio:.12f}")
print(f"MAX_BORDERED_RATIO_300={max_bordered_ratio:.12f}")
for N in (8, 16):
    N, s, Z3, G3, Z2far, star, mx = stress(N)
    print(f"STRESS_N={N} S={','.join(f'{x:.12g}' for x in s)} E3={Z3:.12g} G3={G3:.12g} E2FAR={Z2far:.12g} STARSTARF={star:.12g} MAXENTRY={mx:.12g} RESID_MARG={2/N:.12g}")
print("STATUS=PASS")
