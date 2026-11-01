"""Large-n H/I for majority and for the layer-lookup function (exact, symmetric sums)."""
import math, sys, functools
import mpmath as mp
sys.path.insert(0, 'code')
from log_sharp import threshold_coeffs
from layer_lookup import kraw
print = functools.partial(print, flush=True)

def phi(p):
    return mp.mpf(0) if p == 0 else -p * mp.log(p, 2)

def run(n):
    mp.mp.prec = 3 * n + 128
    N = threshold_coeffs(n, (n + 1) // 2)
    w = (n - 1) // 2
    two = mp.mpf(2) ** n
    # Krawtchouk K_w(t; n) for all t via generating function coefficients of (1-u)^t (1+u)^(n-t) at u^w
    K = [kraw(w, t, n) for t in range(n + 1)]
    Hm = Im = HA = IA = mp.mpf(0)
    for t in range(n + 1):
        c = math.comb(n, t)
        pm = (mp.mpf(N[t]) / two) ** 2
        pa = (mp.mpf(N[t] - K[t]) / two) ** 2
        Hm += c * phi(pm); Im += c * t * pm
        HA += c * phi(pa); IA += c * t * pa
    nL = math.comb(n, w)
    Pz = 1 / two ** 2
    Hz = nL * two * phi(Pz)
    Iz = nL * (two / 2 * (n + 2) / 2 * 2) * Pz  # sum_T (|T|+1) = 2^n (n/2 + 1)
    print(f"n={n:5d}: majority H/I = {float(Hm/Im):.4f} (I/sqrt(n) = {float(Im/mp.sqrt(n)):.4f}); "
          f"layer-lookup H/I = {float((HA+Hz)/(IA+Iz)):.4f}")

for n in [int(a) for a in sys.argv[1:]]:
    run(n)
