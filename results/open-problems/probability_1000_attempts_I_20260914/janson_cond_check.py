# Exact checks for the two condensation counterexamples (Janson Problems 18.41 and 18.42).
# Weights are mpmath mpf (unbounded exponent). Z(m,n) = [t^m] (sum_k w_k t^k)^n by truncated convolution.
import sys, math
from mpmath import mp, mpf, exp, log
mp.dps = 25
def Zpoly(wts, m, n):
    # returns list Z[j] = [t^j] (sum_k wts[k] t^k)^n for j<=m ; wts indexed 0..m (zero beyond allowed)
    cur = [mpf(0)]*(m+1); cur[0] = mpf(1)
    base = [wts[k] if k < len(wts) else mpf(0) for k in range(m+1)]
    for _ in range(n):
        new = [mpf(0)]*(m+1)
        for j in range(m+1):
            cj = cur[j]
            if cj == 0: continue
            for k in range(m+1-j):
                bk = base[k]
                if bk != 0: new[j+k] += cj*bk
        cur = new
    return cur
def check_1842(i, lam):
    m = 2**(i+1); n = int(round(m/lam)); D = m//8
    # d_j = j, except j^3 at powers of two; L(y) = sum_{j<y} d_j ; w_y = e^{L(y)}
    L = [mpf(0)]
    for j in range(m):
        d = j**3 if (j>0 and j & (j-1) == 0) else j
        L.append(L[-1] + d)
    w = [exp(x) for x in L]
    Zall = Zpoly(w, m, n)
    wD = [w[k] if k <= D else mpf(0) for k in range(m+1)]
    ZD_n = Zpoly(wD, m, n)          # all boxes <= D
    ZD_n1 = Zpoly(wD, m, n-1)       # n-1 boxes all <= D
    W1 = n*sum(w[y]*ZD_n1[m-y] for y in range(D+1, m+1))
    Wclass = ZD_n[m] + W1
    p = Wclass/Zall[m]
    # best single config weights for reference
    two = L[3*m//4] + L[m//4]; one = L[m]
    print(f"18.42: i={i} m={m} n={n} D={D}: P(Y(2)<=m/8) = {mp.nstr(p,6)}   log-weight two-box {mp.nstr(two,8)} vs one-box {mp.nstr(one,8)}; log(Wclass/Z)={mp.nstr(log(p),6)}")
def check_1841(J, n, cliff=True):
    # dyadic plateau weights: w_k = exp(-g(block(k))), block(k)=floor(log2 k) for k>=1, w_0 = 1 (block -1 -> g=0).
    # g(j) = max(3j, 6J+4 if cliff and j>=J)
    def g(j):
        v = 3*j
        if cliff and j >= J: v = max(v, 6*J+4)
        return v
    maxk = 2**(J+8)
    w = [mpf(1)] + [exp(-g(int(math.floor(math.log2(k))))) for k in range(1, maxk+1)]
    Phi1 = sum(w); nu = sum(k*w[k] for k in range(len(w)))/Phi1
    K = 3*2**(J-1)
    m = int(round(float(nu)*n)) + K
    assert m+1 <= len(w)
    Zall = Zpoly(w, m, n)
    # P(Y(2) >= 2^(J-1)): weight of configs with at least two boxes >= B := 2^(J-1): total minus (all < B) minus (exactly one >= B)
    B = 2**(J-1)
    wB = [w[k] if k < B else mpf(0) for k in range(m+1)]
    Z0 = Zpoly(wB, m, n)[m]
    ZB_n1 = Zpoly(wB, m, n-1)
    W1 = n*sum(w[y]*ZB_n1[m-y] for y in range(B, m+1))
    p2 = 1 - (Z0 + W1)/Zall[m]
    print(f"18.41 cliff={cliff}: J={J} n={n} nu={mp.nstr(nu,5)} m={m} K={K}: P(Y(2) >= 2^(J-1)={B}) = {mp.nstr(p2,6)}; P(no box>=B)={mp.nstr(Z0/Zall[m],4)} P(exactly one)={mp.nstr(W1/Zall[m],4)}")
which = sys.argv[1]
if which == '1842':
    for i in [5,6,7]:
        check_1842(i, 0.5)
else:
    for J in [4,5]:
        for cl in [True, False]:
            check_1841(J, 300 if J==4 else 400, cl)
