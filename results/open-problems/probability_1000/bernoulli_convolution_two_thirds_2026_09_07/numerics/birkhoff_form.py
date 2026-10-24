"""I_K is a Birkhoff-sum integral for the x3/2 map. That is the thermodynamic-formalism form.

theta_m(x) = x (3/2)^m / 3 mod 1 satisfies theta_(m+1) = (3/2) theta_m mod 1 - the map T(theta) =
(3/2) theta mod 1, Mahler's map. And 1 + cos(2 pi x (3/2)^m/3) = 1 + cos(2 pi theta_m) = exp(phi(theta_m))
with phi(theta) = log(1 + cos 2 pi theta). So, substituting x = 3 theta (dx = 3 d theta, and x in [1,2]
becomes theta in [1/3, 2/3]),

    I_K = 3 int_(1/3)^(2/3) exp( S_(K+1) phi (theta) ) d theta,   S_n phi = sum_(m<n) phi(T^m theta).

So "is I_K bounded" is "does the Birkhoff sum of log(1+cos) under the x3/2 map have vanishing pressure
on this interval, with a bounded prefactor". Verify the identity numerically.
"""
import numpy as np

def I_direct(K, N=1 << 21):
    x = 1 + (np.arange(N) + 0.5) / N
    P = np.ones(N)
    for m in range(K + 1):
        P *= 1.0 + np.cos(2 * np.pi * x * (1.5 ** m) / 3.0)
    return float(P.mean())

def I_birkhoff(K, N=1 << 21):
    th = (1.0 / 3.0) + (np.arange(N) + 0.5) / N / 3.0     # theta in [1/3, 2/3]
    S = np.zeros(N)
    t = th.copy()
    for m in range(K + 1):
        S += np.log(np.maximum(1.0 + np.cos(2 * np.pi * t), 1e-300))
        t = (1.5 * t) % 1.0
    return float(np.exp(S).mean())          # 3 * int over a length-1/3 interval = the mean

print(f"{'K':>4} {'I_K direct':>14} {'I_K Birkhoff':>15} {'rel diff':>11}")
for K in (6, 8, 10, 12, 14):
    a, b = I_direct(K), I_birkhoff(K)
    print(f"{K:>4} {a:>14.8f} {b:>15.8f} {abs(a-b)/a:>11.2e}")
print()
print("phi has mean -log 2 under Lebesgue:", f"{float(np.log(1+np.cos(2*np.pi*(np.arange(1<<20)+0.5)/(1<<20))).mean()):.6f}", "vs", f"{-np.log(2):.6f}")
