"""Is H (homogenised Phi') >= 0 on the part of the cone where m < T/(n(n-1))?  Float scan over
x = (1, s x k, t x l, -b), k + l = n - 2, the shape of the constrained minimisers.  an agent, 11 Nov 2026."""
import sys

def H(n, T, P, Q, a):
    K = (n * n - 6 * n + 6) * T * T + 2 * n * Q
    Nh = n * (n - 1) * (T * T - Q + 2 * a * P - 2 * a * a * T) + T * T
    Dh = n * Q * T - T ** 3 - n * P * P
    return K * Nh + 2 * (n - 3) * (n * (n - 1) * a * a - T) * Dh

G = 80
for n in [int(v) for v in sys.argv[1:]] or [14, 16, 20, 30, 50]:
    worst = (1e300,)
    cnt = 0
    for ib in range(0, G + 1):
        b = ib / G                      # most negative coordinate is -b, 0 <= b <= 1 = a
        for k in range(0, n - 1):
            l = n - 2 - k
            for i_s in range(0, G + 1):
                s = 1.0 * i_s / G       # value repeated k times (may be negative), in [-b, 1]
                s = -b + (1 + b) * i_s / G
                if l == 0:
                    if abs(1 - b + k * s) > 1e-12: continue
                    t = 0.0
                else:
                    t = -(1 - b + k * s) / l
                if not (-b - 1e-12 <= t <= 1 + 1e-12): continue
                xs = [1.0] + [s] * k + [t] * l + [-b]
                xs.sort(reverse=True)
                T = sum(v * v for v in xs)
                m = max(xs[0] * xs[1], xs[-1] * xs[-2])
                if m >= T / (n * (n - 1)): continue
                P = sum(v ** 3 for v in xs); Q = sum(v ** 4 for v in xs)
                h = H(n, T, P, Q, 1.0) / T ** 4
                cnt += 1
                if h < worst[0]:
                    worst = (h, b, k, s, t, m * n * (n - 1) / T)
    print(n, "points in region", cnt, "min H/T^4", worst, flush=True)
