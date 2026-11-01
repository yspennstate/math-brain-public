"""The certificate potential Gamma_hat(p) = p*G_num(log2(1/p)) + c*p*(1-p), symmetric, from a cert_vi npz.
Shared by the gate-arity program and the diagnostics.  Matches scan_cmin.py / fei_cert*.py exactly."""
import numpy as np, math
LN2 = math.log(2.0)
BSTAR = 8 - 4 / LN2

class Gam:
    def __init__(self, npz, c=0.0):
        d = np.load(npz)
        self.xs = np.asarray(d["xs"], float); self.G = np.asarray(d["G"], float)
        self.K = float(self.xs[-1]); self.C0 = float(d["C"]); self.c = float(c)
        self.sig_t = (self.G[-1] - BSTAR) / self.K
    def Ghat(self, x):
        x = np.asarray(x, float)
        return np.where(x <= self.K, np.interp(np.minimum(x, self.K), self.xs, self.G),
                        self.G[-1] + (x - self.K) * self.sig_t)
    def __call__(self, z):
        z = np.asarray(z, float)
        s = np.minimum(z, 1 - z)
        s = np.clip(s, 1e-300, 0.5)
        return s * self.Ghat(np.log2(1.0 / s)) + self.c * z * (1 - z)
    @property
    def cap(self):   # Gamma(1/2) = the theorem constant
        return 0.5 * self.Ghat(1.0) + self.c * 0.25

def h2(v):
    v = np.clip(np.asarray(v, float), 0.0, 1.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        a = np.where((v > 0) & (v < 1), -v * np.log2(np.maximum(v, 1e-300)), 0.0)
        b = np.where((v > 0) & (v < 1), -(1 - v) * np.log2(np.maximum(1 - v, 1e-300)), 0.0)
    return a + b
