# Margin of (C3) in nats: Phi_q(s) = (1-q) X0 ln(X0/M) + q X1 ln(X1/M), X0 = (s - t)^2, X1 = (s + 1/t)^2, M = s^2 + 1,
# t = sqrt(q/(1-q)); claim Phi_q(s) <= 2 + ln(1/(4q(1-q))) for all real s. Print sup_s Phi_q, where it is attained,
# and the margin, for q in (0, 1/2] (the case q > 1/2 is symmetric).
import math, numpy as np
def xlnx_ratio(x, M): return np.where(x > 0, x * np.log(np.where(x > 0, x, 1) / M), 0.0)
s = np.concatenate([-np.logspace(-6, 7, 20001)[::-1], [0.0], np.logspace(-6, 7, 20001)])
for q in (1e-8, 1e-6, 1e-4, 1e-3, 0.01, 0.03, 0.1, 0.2, 0.3, 0.4, 0.45, 0.49, 0.5):
    t = math.sqrt(q / (1 - q)); X0 = (s - t) ** 2; X1 = (s + 1 / t) ** 2; M = s * s + 1
    Phi = (1 - q) * xlnx_ratio(X0, M) + q * xlnx_ratio(X1, M)
    K = 2 + math.log(1 / (4 * q * (1 - q)))
    i = int(np.argmax(Phi))
    print('q=%-8g sup Phi %.5f at s=%-11.4g K %.5f margin %.5f  | Phi(0)=%.4f  Phi(+-inf)->2' % (q, Phi[i], s[i], K, K - Phi[i], (1 - 2 * q) * math.log((1 - q) / q)))
