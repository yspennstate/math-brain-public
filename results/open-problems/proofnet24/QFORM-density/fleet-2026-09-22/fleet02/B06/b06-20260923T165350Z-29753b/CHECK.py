import json, math
import numpy as np

rng = np.random.default_rng(20260923)
max_alpha = 0.0
max_transfer = 0.0
max_conditional = 0.0
trials = 500

for _ in range(trials):
    m = int(rng.integers(3, 10))
    n = int(rng.integers(2, 9))
    v = rng.normal(size=m)
    v /= np.linalg.norm(v)
    M = rng.normal(size=(m, n))
    C = (np.eye(m) - np.outer(v, v)) @ M
    Z = float(np.sum(C * C))
    if Z < 1e-12:
        continue

    pair_weight = {}
    incidence = np.zeros(m)
    for p in range(m):
        for q in range(p + 1, m):
            vals = v[p] * M[q, :] - v[q] * M[p, :]
            weights = vals * vals
            pair_weight[(p, q)] = weights
            w = float(weights.sum())
            incidence[p] += w
            incidence[q] += w

    alpha = incidence / Z
    rhs = v * v + np.sum(C * C, axis=1) / Z
    max_alpha = max(max_alpha, float(np.max(np.abs(alpha - rhs))))

    h = int(np.argmax(alpha))
    s2 = 1.0 - v[h] ** 2
    if s2 <= 1e-10:
        continue

    keep = [i for i in range(m) if i != h]
    vp = v[keep] / math.sqrt(s2)
    Mp = M[keep, :]
    Cp = (np.eye(m - 1) - np.outer(vp, vp)) @ Mp
    Zp = float(np.sum(Cp * Cp))
    max_transfer = max(
        max_transfer,
        abs(s2 * Zp - Z * (1.0 - alpha[h])) / max(Z, 1e-15),
    )

    surviving = 0.0
    incidence_cond = np.zeros(m)
    for (p, q), weights in pair_weight.items():
        if h in (p, q):
            continue
        w = float(weights.sum())
        surviving += w
        incidence_cond[p] += w
        incidence_cond[q] += w

    if surviving > 1e-12:
        target = np.delete(incidence_cond / surviving, h)
        incidence_new = np.zeros(m - 1)
        for p in range(m - 1):
            for q in range(p + 1, m - 1):
                vals = vp[p] * Mp[q, :] - vp[q] * Mp[p, :]
                w = float(np.sum(vals * vals))
                incidence_new[p] += w
                incidence_new[q] += w
        alpha_new = incidence_new / Zp
        max_conditional = max(
            max_conditional, float(np.max(np.abs(alpha_new - target)))
        )

m0 = 11907 / 1048576
C_F = 3 * 2 ** (4 / 3) * math.exp(1 / 3)
output = {
    "trials": trials,
    "max_alpha_identity_error": max_alpha,
    "max_transfer_identity_relative_error": max_transfer,
    "max_conditional_marginal_error": max_conditional,
    "partner_r39_x2_floor": m0,
    "fusion_constant_C_F": C_F,
    "paid_branch_constant_if_abs_lambda_ge_1": C_F * 4 ** (1 / 3) * m0 ** (-1 / 3),
    "three_quarters_fused_mass_floor": 0.75 * m0,
}
print(json.dumps(output, indent=2, sort_keys=True))
