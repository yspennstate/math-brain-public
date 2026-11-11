# Exact tail of the height of a random recursive tree against the expected number of deep vertices.
# usage: python root_tail.py N  (N = largest size; sizes reported: 250,500,...,N by doubling)
# Recursion: the subtree of vertex 2 has K vertices, K uniform on 1..n-1, and is a recursive tree of size K; the rest
# is a recursive tree of size n-K, independent.  t_n(h) = P(height > h):
#   t_n(h) = (1/(n-1)) sum_K [ t_K(h-1) (1 - t_{n-K}(h)) + t_{n-K}(h) ].
import sys, math
import numpy as np

N = int(sys.argv[1])
ALPHA = 3.59112147666862
THETA = math.log(ALPHA)
sizes = []
m = 250
while m <= N:
    sizes.append(m)
    m *= 2
HMAX = int(ALPHA * math.log(N)) + 6


def b(n):
    return ALPHA * math.log(n) - math.log(math.log(n)) / (2 * THETA)


# expected profile f_{n,d}, d <= HMAX+1, at the reported sizes
prof = {}
f = np.zeros(HMAX + 2)
f[0] = 1.0
for j in range(1, N):
    f[1:] = f[1:] + f[:-1] / j      # multiply by (1 + z/j)
    if j + 1 in sizes:
        prof[j + 1] = f.copy()

tail = {n: {} for n in sizes}       # tail[n][h] = P(height > h)
t_prev = np.ones(N + 1)             # h = -1: every tree has height > -1
for h in range(0, HMAX + 1):
    t_cur = np.zeros(N + 1)         # t_cur[1] = 0
    s_cur = 0.0                     # sum_{m<n} t_cur[m]
    for n in range(2, N + 1):
        s_cur += t_cur[n - 1]
        # sum_K t_prev[K] * (1 - t_cur[n-K]), K = 1..n-1
        c = float(np.dot(t_prev[1:n], 1.0 - t_cur[n - 1:0:-1]))
        t_cur[n] = (c + s_cur) / (n - 1)
    for n in sizes:
        tail[n][h] = t_cur[n]
    t_prev = t_cur

print('n  k  k-b_n  P(height>=k)  E#(depth>=k)  ratio')
for n in sizes:
    kb = math.ceil(b(n))
    for k in range(kb - 4, kb + 3):
        if k - 1 > HMAX or k > HMAX:
            continue
        p = tail[n][k - 1]
        ey = float(prof[n][k:].sum())
        print('%6d %3d %+6.2f  %.6e  %.6e  %.4f' % (n, k, k - b(n), p, ey, p / ey if ey > 0 else float('nan')))
if len(sys.argv) > 2 and sys.argv[2] == 'law':
    for n in sizes:
        print('law n=%d: P(height>=k), k=1..: %s' % (n, ' '.join('%.5f' % tail[n][k - 1] for k in range(1, HMAX + 1)
                                                                  if tail[n][k - 1] > 5e-6)))
        print('mean height n=%d: %.4f' % (n, sum(tail[n].values())))
