# Independent check of the run decomposition for the field e = sign (e_y=+1 iff y>=0), f_x = (-1)^x.
# Run j happens in column x_j (parity j), goes G_j ~ Geom(1/2) on {0,1,..} steps in direction (-1)^j, starting at
# height W_{j-1} (W_{-1}=0). Then one horizontal step x_{j+1} = x_j + s(W_j). The origin is visited during run j iff
# x_j = 0 and the run covers height 0; at most once per run. Green(0,0) = sum_j P(x_j=0, run j covers 0).
# DP over the joint law of (x_j, W_{j-1}); geometric convolution by a first-order recursive filter.
import sys, numpy as np
from scipy.signal import lfilter
J = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
X = J + 2; WM = int(12 * np.sqrt(2 * J)) + 20
nx, nw = 2 * X + 1, 2 * WM + 1
w = np.arange(nw) - WM
p = np.zeros((nx, nw)); p[X, WM] = 1.0          # law of (x_0, W_{-1})
green = 0.0; marks = {10, 100, 300, 1000, 2000, 4000, J}
for j in range(J + 1):
    d = 1 if j % 2 == 0 else -1
    if j % 2 == 0:  # run goes up from W_{j-1}: covers 0 iff W_{j-1} <= 0 and G >= -W_{j-1}
        row = p[X]
        term = float(np.sum(row[w <= 0] * 0.5 ** (-w[w <= 0])))
        green += term
    # W_j = W_{j-1} + d*G, G ~ P(G=g) = 2^{-(g+1)}: q[w] = p[w]/2 + q[w-d]/2
    if d == 1:
        q = lfilter([0.5], [1.0, -0.5], p, axis=1)
    else:
        q = lfilter([0.5], [1.0, -0.5], p[:, ::-1], axis=1)[:, ::-1]
    up = q[:, w >= 0].sum(1)  # not needed, kept small
    nxt = np.zeros_like(q)
    pos = (w >= 0)
    nxt[1:, pos] = q[:-1, pos]      # s = +1: x -> x+1
    nxt[:-1, ~pos] = q[1:, ~pos]    # s = -1: x -> x-1
    p = nxt
    if j in marks:
        print(f"runs j={j} green={green:.5f} last_term_scaled j^1.5*term={j**1.5*term if j%2==0 else float('nan'):.4f} mass={p.sum():.9f}", flush=True)
