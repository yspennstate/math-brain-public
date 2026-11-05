"""T390 part 2: independent check of the denoising (noise integrated out) table in
T390_weight_are_asymptotic.md (in the row folder).

Model: clean data 1/2 N(-m,1) + 1/2 N(m,1), weight parameter eta at 0. At noise sigma the smoothed density is the same
mixture with variance tau^2 = 1 + sigma^2, score s(x) = -x/tau^2 + (m/tau^2) tanh(m x/tau^2 + eta).
  g    = d_eta s = (m/tau^2) sech^2(m x/tau^2)
  psi  = s g + g'                       (explicit score-matching gradient of the smoothed model)
  u(x0)= E_z psi(x0 + sigma z)          (= the DSM gradient with the noise integrated out, by Stein's lemma)
  H    = E_{p_sigma} g^2
  V    = E_{p0} u^2      (exact, noise integrated)        V_s = E_{p_sigma} psi^2   (smoothed model alone)
  I    = E_{p0} tanh^2(m x)   (clean ML Fisher information);  I_s = smoothed-model Fisher information
ARE = H^2/(V I). Lower bound H^2/(V_s I) because V <= V_s (total variance). Also prints H^2/(V_s I_s).
By symmetry at eta = 0 every expectation over the mixture equals the expectation over the +m component.
"""
import json
import numpy as np
from scipy.integrate import quad

SQ2PI = np.sqrt(2 * np.pi)


def npdf(x, mu, sd):
    return np.exp(-0.5 * ((x - mu) / sd) ** 2) / (SQ2PI * sd)


def parts(m, sigma):
    t2 = 1.0 + sigma ** 2
    a = m / t2

    def s(x):
        return -x / t2 + a * np.tanh(a * x)

    def g(x):
        return a / np.cosh(a * x) ** 2

    def gp(x):
        return -2 * a * a * np.tanh(a * x) / np.cosh(a * x) ** 2

    def psi(x):
        return s(x) * g(x) + gp(x)

    return t2, a, s, g, psi


def E(f, mu, sd, extra=()):
    pts = sorted({mu, 0.0, *extra})
    lo, hi = min(pts) - 12 * sd, max(pts) + 12 * sd
    v, _ = quad(lambda x: f(x) * npdf(x, mu, sd), lo, hi, points=pts, limit=400, epsabs=0, epsrel=1e-11)
    return v


def are(m, sigma):
    t2, a, s, g, psi = parts(m, sigma)
    tau = np.sqrt(t2)
    w = 1.0 / a  # width of the crossing region
    H = E(lambda x: g(x) ** 2, m, tau, (w, -w))
    Vs = E(lambda x: psi(x) ** 2, m, tau, (w, -w))
    I = E(lambda x: np.tanh(m * x) ** 2, m, 1.0)
    # smoothed Fisher info for eta: d_eta log p_sigma = tanh(a x) at eta=0  -> I_s = E tanh^2(a x)
    Is = E(lambda x: np.tanh(a * x) ** 2, m, tau)
    if sigma == 0:
        V = Vs
    else:
        def u(x0):
            v, _ = quad(lambda x: psi(x) * npdf(x, x0, sigma), x0 - 12 * sigma, x0 + 12 * sigma,
                        points=sorted({0.0, w, -w, x0}) if abs(x0) < 12 * sigma else None,
                        limit=400, epsabs=0, epsrel=1e-10)
            return v
        V = E(lambda x0: u(x0) ** 2, m, 1.0)
    return {"m": m, "sigma": sigma, "H": H, "V": V, "V_s": Vs, "I": I, "I_s": Is,
            "ARE": H * H / (V * I), "lower_HHVsI": H * H / (Vs * I), "HHVsIs": H * H / (Vs * Is)}


SRC = {(3, 0): (0.0072, 0.0072), (3, 1.5): (0.842, 0.182), (3, 3): (0.968, 0.332), (3, 6): (0.916, 0.186),
       (5, 2.5): (0.886, 0.131), (5, 5): (0.991, 0.331), (5, 10): (0.967, 0.187)}

if __name__ == "__main__":
    rows = []
    for (m, sg), (src_are, src_lb) in SRC.items():
        r = are(m, sg)
        r["src_ARE"], r["src_lower"] = src_are, src_lb
        rows.append(r)
        print(f"m={m} sigma={sg}: ARE={r['ARE']:.4f} (src {src_are})  H2/(VsI)={r['lower_HHVsI']:.4f}  "
              f"H2/(VsIs)={r['HHVsIs']:.4f} (src lb {src_lb})")
    json.dump(rows, open("t390_noise_check.json", "w"), indent=1)
