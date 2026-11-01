# Pointwise probe: J_q(a, d) = phi(a^2 + d^2) - (1-q) phi((a - t d)^2) - q phi((a + d/t)^2), t = sqrt(q/(1-q)), is the
# Jensen gap of the biased restriction for one pair (T, T + v). Is J_q(a, d) - d^2 log2(1/sigma^2) <= K d^2 for all
# admissible a, d (restricted coefficients of +-1 functions: |a - t d| <= 1, |a + d/t| <= 1), sigma^2 = 4q(1-q)?
import math, numpy as np
def phi(p): return np.where(p > 1e-300, -p * np.log2(np.where(p > 1e-300, p, 1)), 0.0)
worst = (-1e9, None)
for q in np.concatenate([np.logspace(-6, np.log10(0.5), 60), 1 - np.logspace(-6, np.log10(0.5), 60)]):
    t = math.sqrt(q / (1 - q)); sig2 = 4 * q * (1 - q)
    # parametrise by the two restricted coefficients u = a - t d, w = a + d/t in [-1, 1]
    u = np.linspace(-1, 1, 801)[:, None]; w = np.linspace(-1, 1, 801)[None, :]
    d = (w - u) * t / (1 + t * t) * (1 / t) * t      # solve: w - u = d (t + 1/t)  =>  d = (w - u) / (t + 1/t)
    d = (w - u) / (t + 1 / t); a = u + t * d
    J = phi(a * a + d * d) - (1 - q) * phi(u * u) - q * phi(w * w)
    with np.errstate(divide='ignore', invalid='ignore'):
        r = np.where(d * d > 1e-14, (J - d * d * math.log2(1 / sig2)) / (d * d), -1e9)
    i = np.unravel_index(np.argmax(r), r.shape)
    if r[i] > worst[0]: worst = (float(r[i]), (float(q), float(a[i]), float(d[i])))
print('sup of (J_q - d^2 log2(1/sigma^2)) / d^2 over the grid: %.4f at q=%.3g a=%.4f d=%.4g' % (worst[0], *worst[1]))
