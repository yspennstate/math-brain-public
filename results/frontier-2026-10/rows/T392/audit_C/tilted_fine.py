# Cross-check of the tilted-law leakage with a fine log-space trapezoid (quad's absolute tolerance cannot resolve 1e-16).
import numpy as np
from scipy.special import logsumexp
def lq(y, w, m):
    return -(y * y + m * m / 4) / 2 + (1 - w) * np.logaddexp(m * y / 2, -m * y / 2) + w * m * y / 2
for w, m in ((2, 2), (2, 4), (8, 2), (8, 4), (2, 8), (2, 16), (4, 8), (4, 16)):
    y = np.linspace(-30, 40, 7_000_001); h = y[1] - y[0]
    l = lq(y, w, m)
    neg = y < 0
    leak = np.exp(logsumexp(l[neg]) - logsumexp(l))
    C = np.trapezoid(np.exp((1 - w) * np.logaddexp(0, -2 * np.linspace(0, 60, 600001)) + (1 - w) * np.linspace(0, 60, 600001) - (1 - w) * np.log(2) - w * np.linspace(0, 60, 600001)), dx=1e-4)
    asym = (2 / m) * np.exp(-m * m / 8) * C / (2 ** (w - 1) * np.sqrt(2 * np.pi))
    print("tilted w %g m %2g: leak %.4e   asymptotic %.4e  ratio %.4f" % (w, m, leak, asym, leak / asym))
