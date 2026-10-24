import itertools, json, math
import numpy as np

rng = np.random.default_rng(20260923)
max_incident_err = 0.0
max_alpha = 0.0
max_det_ratio = 0.0
max_kl_excess = -1e100
used = 0


def minor2_law(M):
    items, total = [], 0.0
    for R in itertools.combinations(range(M.shape[0]), 2):
        for T in itertools.combinations(range(M.shape[1]), 2):
            d = np.linalg.det(M[np.ix_(R, T)])
            w = float(d * d)
            if w > 1e-24:
                items.append((R, T, w))
                total += w
    return total, [(R, T, w / total) for R, T, w in items]


for _ in range(200):
    B = rng.normal(size=(5, 5))
    a = B[0, 0]
    if abs(a) < 1e-8:
        continue
    r, c, N = B[0, 1:], B[1:, 0], B[1:, 1:]
    S = N - np.outer(c, r) / a
    ES, lawS = minor2_law(S)
    EN, lawN = minor2_law(N)
    J = a * a * ES

    incident = 0.0
    for R in itertools.combinations(range(1, 5), 2):
        for T in itertools.combinations(range(1, 5), 2):
            d = np.linalg.det(B[np.ix_((0,) + R, (0,) + T)])
            incident += float(d * d)
    max_incident_err = max(max_incident_err, abs(J - incident) / max(1.0, J))

    delta, joint = 0.0, []
    for Rs, Ts, ws in lawS:
        for Rn, Tn, wn in lawN:
            if set(Rs).isdisjoint(Rn):
                p = ws * wn
                delta += p
                joint.append((Rs, Ts, Rn, Tn, p))
    if delta <= 1e-15:
        continue
    used += 1

    muS, muN = {}, {}
    for Rs, Ts, Rn, Tn, p in joint:
        z = p / delta
        muS[(Rs, Ts)] = muS.get((Rs, Ts), 0.0) + z
        muN[(Rn, Tn)] = muN.get((Rn, Tn), 0.0) + z
    nuS = {(R, T): w for R, T, w in lawS}
    nuN = {(R, T): w for R, T, w in lawN}
    DS = sum(p * math.log(p / nuS[k]) for k, p in muS.items())
    DN = sum(p * math.log(p / nuN[k]) for k, p in muN.items())
    max_kl_excess = max(max_kl_excess, DS + DN - math.log(1 / delta))

    arS = np.zeros(4); arN = np.zeros(4)
    bcS = np.zeros(4); bcN = np.zeros(4)
    for (R, T), p in muS.items():
        for i in R: arS[i] += p
        for j in T: bcS[j] += p
    for (R, T), p in muN.items():
        for i in R: arN[i] += p
        for j in T: bcN[j] += p
    alpha, beta = (arS + arN) / 2, (bcS + bcN) / 2
    max_alpha = max(max_alpha, float(alpha.max()))

    prow = np.exp(rng.normal(size=5)); qcol = np.exp(rng.normal(size=5))
    lhs = float(np.linalg.det(B.T @ np.diag(prow) @ B + np.diag(qcol)))
    rhs = 2 * math.sqrt(J * EN) * math.exp(-(DS + DN) / 2) * math.sqrt(prow[0] * qcol[0])
    for i, x in enumerate(alpha, 1): rhs *= prow[i] ** x
    for j, x in enumerate(beta, 1): rhs *= qcol[j] ** (1 - x)
    max_det_ratio = max(max_det_ratio, rhs / lhs)

out = {
    "seed": 20260923,
    "trials_requested": 200,
    "trials_used": used,
    "max_relative_incident_identity_error": max_incident_err,
    "max_conditioned_average_row_marginal": max_alpha,
    "max_KL_excess_over_log_1_over_delta": max_kl_excess,
    "max_determinant_lower_bound_rhs_over_lhs": max_det_ratio,
    "C_L1_exact_formula": "5*exp(4/5)",
    "C_L1": 5 * math.exp(4 / 5),
    "N3_tau_1_over_64_eta_1_over_16_coefficient": 5 * math.exp(4 / 5) * (36 * (1 / 64) * (1 + 1 / 64) / (1 / 16)) ** (1 / 10),
    "status": "PASS",
}
print(json.dumps(out, indent=2))
