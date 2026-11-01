"""B15 exact uniform-cube erasure engine.
Conventions: point x in 0..2^n-1, bit j of x is coordinate j; set S is a bitmask;
chi_S(x)=(-1)^popcount(S&x); f(x)=(-1)^t(x); W_S=sum_x f(x)chi_S(x) (integer); fhat=W/2^n;
P_S=W_S^2/4^n. Inf_i=sum_{S contains i} P_S. B_i=H(S_i|S_-i)=H(P)-H(M_i), M_i(T)=P_T+P_{T+i}.
JS_i=H(M_i)-(H(P+)+H(P-))/2 with P+-(T)=(fhat_T +- fhat_{T+i})^2.
Delta_i=H(f)-(H(f|x_i=0)+H(f|x_i=1))/2 computed from restricted truth tables (independent path).
Kstar=4+(5/2)log2 5-(9/2)log2 3 (A082 n<=4 selectable true-erasure constant).
Float values are evidence only; exact_sign_Bi_minus_Kstar is the exact integer comparison."""
import numpy as np, math

LOG2 = np.log2
KSTAR = 4 + 2.5*math.log2(5) - 4.5*math.log2(3)
TWO_OVER_LN2 = 2/math.log(2)

def hadamard(n):
    H = np.array([[1]], dtype=np.int64)
    for _ in range(n):
        H = np.block([[H, H], [H, -H]])
    return H

def ent_rows(P):
    with np.errstate(divide='ignore', invalid='ignore'):
        L = np.where(P > 0, P*np.log2(np.where(P > 0, P, 1.0)), 0.0)
    return -L.sum(axis=1)

def pair_index(n, i):
    idx0 = np.array([S for S in range(1 << n) if not (S >> i) & 1], dtype=np.int64)
    return idx0, idx0 | (1 << i)

def tables_to_pm(tabs, n):
    """tabs: int array of truth-table integers (bit x = t(x)); returns +-1 matrix."""
    x = np.arange(1 << n, dtype=np.int64)
    bits = (tabs[:, None] >> x[None, :]) & 1
    return (1 - 2*bits).astype(np.int64)

def spectra(F, n):
    Hm = hadamard(n)
    W = F @ Hm.T          # W[:,S] = sum_x F[:,x] chi_S(x)  (Hm symmetric)
    return W

def quantities(F, n, want_delta=True):
    """F: (N,2^n) +-1 int matrix. Returns dict of float arrays."""
    N = F.shape[0]; D = 1 << n
    W = spectra(F, n).astype(np.float64)
    P = W*W/(D*D)
    H = ent_rows(P)
    Inf = np.zeros((N, n)); B = np.zeros((N, n)); JS = np.zeros((N, n)); Dl = np.zeros((N, n))
    for i in range(n):
        i0, i1 = pair_index(n, i)
        Inf[:, i] = P[:, i1].sum(axis=1)
        M = P[:, i0] + P[:, i1]
        HM = ent_rows(M)
        B[:, i] = H - HM
        fp = (W[:, i0] + W[:, i1])/D; fm = (W[:, i0] - W[:, i1])/D
        JS[:, i] = HM - 0.5*(ent_rows(fp*fp) + ent_rows(fm*fm))
        if want_delta:
            # independent path: restrict truth table, recompute spectrum on n-1 vars
            x = np.arange(D)
            r0 = x[((x >> i) & 1) == 0]; r1 = r0 | (1 << i)
            H0 = ent_rows((spectra(F[:, r0], n-1).astype(np.float64)/(D//2))**2)
            H1 = ent_rows((spectra(F[:, r1], n-1).astype(np.float64)/(D//2))**2)
            Dl[:, i] = H - 0.5*(H0 + H1)
    I = Inf.sum(axis=1)
    return dict(W=W, P=P, H=H, Inf=Inf, B=B, JS=JS, Delta=Dl, I=I)

def min_ratio(num, Inf, tol=1e-15):
    with np.errstate(divide='ignore', invalid='ignore'):
        R = np.where(Inf > tol, num/np.where(Inf > tol, Inf, 1.0), np.inf)
    return R.min(axis=1), R.argmin(axis=1)

# ---------------- exact arithmetic ----------------
def exact_Bi_parts(Wint, n, i):
    """Return (num, den, L) with 4^n B_i = log2(num/den), 4^n Inf_i = L (integers)."""
    num = 1; den = 1; L = 0
    for T in range(1 << n):
        if (T >> i) & 1: continue
        a = int(Wint[T])**2; b = int(Wint[T | (1 << i)])**2; s = a + b
        if s == 0: continue
        num *= s**s
        if a: den *= a**a
        if b: den *= b**b
        L += b
    return num, den, L

def exact_sign_Bi_minus_Kstar(Wint, n, i):
    """Exact sign of B_i - Kstar*Inf_i.
    B_i > K* Inf_i  <=>  num^2 * 3^(9L) > den^2 * 2^(8L) * 5^(5L)."""
    num, den, L = exact_Bi_parts(Wint, n, i)
    lhs = num*num*3**(9*L); rhs = den*den*2**(8*L)*5**(5*L)
    return (lhs > rhs) - (lhs < rhs)

def exact_sign_Bi_minus_rational(Wint, n, i, p, q):
    """Exact sign of B_i - (p/q) Inf_i:  num^q > den^q * 2^(p L)  (log2 form, 4^n scaling cancels)."""
    num, den, L = exact_Bi_parts(Wint, n, i)
    lhs = num**q; rhs = den**q * 2**(p*L)
    return (lhs > rhs) - (lhs < rhs)
