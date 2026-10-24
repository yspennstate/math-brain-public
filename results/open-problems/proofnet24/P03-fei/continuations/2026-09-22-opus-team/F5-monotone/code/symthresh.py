"""Exact H and I of the symmetric threshold f = +1 iff #{i: x_i=-1} < k (an LTF), any n.
Level-j coefficient (j>=1) is 2^-(n-1) K_{j-1}(k-1; n-1) (Krawtchouk), from the derivative
D_1 f = indicator of the slice |x'| = k-1.  Exact integers, logs at the end."""
import math, sys
try:
    import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2,3,14,15])
except Exception: pass

def kraw_all(N, i):
    K = [1, N - 2*i]
    for t in range(1, N):
        num = (N - 2*i)*K[t] - (N - t + 1)*K[t-1]
        assert num % (t+1) == 0
        K.append(num//(t+1))
    return K[:N+1]

def sym_HI(n, k):
    """f=+1 iff fewer than k of the x_i are -1; 1<=k<=n."""
    N = n - 1
    K = kraw_all(N, k-1)
    L2 = 2*(n-1)
    H = 0.0; I = 0.0; tot = 0.0
    # level 0
    ptrue = sum(math.comb(n, m) for m in range(k, n+1))  # f=-1 count
    f0 = 1 - 2*ptrue/2**n
    w0 = f0*f0
    if w0 > 0: H -= w0*math.log2(w0)
    tot += w0
    for j in range(1, n+1):
        a = K[j-1]
        if a == 0: continue
        # coefficient = 2^-(n-1) * C(N,k-1) K_{j-1}(k-1) / C(N,j-1)
        lw = 2*(math.log2(abs(a)) + math.log2(math.comb(N, k-1)) - math.log2(math.comb(N, j-1))) - L2   # log2 fhat^2
        # use log domain for C(n,j)*fhat^2
        lW = math.log2(math.comb(n, j)) + lw
        Wj = 2.0**lW
        H += Wj*(-lw)
        I += j*Wj
        tot += Wj
    return H, I, tot, ptrue/2**n

if __name__ == "__main__":
    for n in [int(a) for a in sys.argv[1:]]:
        best = (0, None)
        rows = []
        for k in range(1, n+1):
            H, I, tot, p = sym_HI(n, k)
            r = H/I
            rows.append((k, p, H, I, r, tot))
            if r > best[0]: best = (r, k, p, H, I, tot)
        print("n=%d best H/I=%.6f at k=%d p=%.3e H=%.6g I=%.6g parseval=%.12f" % ((n,)+best))
        sys.stdout.flush()
