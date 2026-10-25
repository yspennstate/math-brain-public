"""Exhaustive census of symmetric +-1 matrices, n = 2..7.

Normalisation: every orbit of the diagonal sign-conjugation group D -> DMD
contains EXACTLY ONE matrix with M[0,j] = +1 for all j>=1 (take d_0=1,
d_j = M[0,j]); orbits all have size 2^{n-1}.  So the uniform measure on the
2^{n(n+1)/2 - (n-1)} normalised matrices equals the push-forward of the uniform
measure on all symmetric +-1 matrices, and every event below is invariant under
that group.  Counts are therefore exact probabilities.

Events (all decided EXACTLY on the integer characteristic polynomial):
  PAIR0   : exists i<j with lam_i + lam_j = 0                (Vu Conj 8.5 event)
  PAIRNZ  : exists i<j with lam_i + lam_j = 0 and lam_i != 0
  REP     : exists a repeated eigenvalue                      (Vu Conj 8.4 event)
  REPNZ   : exists a repeated NONZERO eigenvalue
  CORANK2 : corank >= 2
  INTSPEC : spectrum is integral                              (Vu Conj 9.4 event)
Screening is by float eigenvalues; every flagged matrix is then decided exactly,
and the float margin of the non-flagged ones is reported so false negatives can
be ruled out.
"""
import numpy as np, itertools, sys
from fractions import Fraction

# ---------- exact integer polynomial tools ----------
def charpoly_int(M):
    """Faddeev-LeVerrier, exact.  Returns [c_n,...,c_0] for det(xI-M)=sum c_k x^k,
       as a list of Python ints, index k = coefficient of x^k."""
    n = M.shape[0]
    A = np.eye(n, dtype=object)
    Mo = M.astype(object)
    coeffs = [0]*(n+1)
    coeffs[n] = 1
    Mk = np.eye(n, dtype=object)
    c = 1
    for k in range(1, n+1):
        Mk = Mo.dot(Mk)
        tr = sum(Mk[i,i] for i in range(n))
        c = -tr // k if (-tr) % k == 0 else Fraction(-tr, k)
        assert isinstance(c, int) or c.denominator == 1, "Leverrier non-integral"
        c = int(c)
        coeffs[n-k] = c
        Mk = Mk + c*np.eye(n, dtype=object)
    return coeffs   # coeffs[k] multiplies x^k

def poly_trim(p):
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p

def poly_gcd_Q(a, b):
    """gcd over Q of integer coefficient lists (index=power); returns primitive int list."""
    a = poly_trim([Fraction(x) for x in a]); b = poly_trim([Fraction(x) for x in b])
    while len(b) > 1 or b[0] != 0:
        # a mod b
        r = a[:]
        while len(r) >= len(b) and not (len(r)==1 and r[0]==0):
            if r[-1] == 0: r.pop(); continue
            if len(r) < len(b): break
            f = r[-1]/b[-1]; sh = len(r)-len(b)
            for i in range(len(b)):
                r[sh+i] -= f*b[i]
            r = poly_trim(r)
        a, b = b, r
        if len(b)==1 and b[0]==0: break
    # a is the gcd over Q; make primitive integer
    a = poly_trim(a)
    from math import gcd
    dens = 1
    for x in a: dens = dens*x.denominator//gcd(dens, x.denominator)
    ints = [int(x*dens) for x in a]
    g = 0
    for x in ints: g = gcd(g, abs(x))
    if g: ints = [x//g for x in ints]
    return poly_trim(ints)

def poly_deriv(p):
    return poly_trim([k*p[k] for k in range(1, len(p))]) if len(p) > 1 else [0]

def val0(p):
    """multiplicity of the root 0"""
    v = 0
    while v < len(p) and p[v] == 0: v += 1
    return v

def even_odd(p):
    """p(x) = E(x^2) + x*O(x^2); return E, O as coefficient lists in y."""
    E = [p[k] for k in range(0, len(p), 2)]
    O = [p[k] for k in range(1, len(p), 2)]
    return poly_trim(E), poly_trim(O) if O else [0]

def has_pair_sum_zero(p):
    """exists i<j with lam_i+lam_j = 0  (lam real, p monic integer, all roots real)."""
    if val0(p) >= 2: return True, True   # (event, from a double zero)
    E, O = even_odd(p)
    g = poly_gcd_Q(E, O)
    # a common root != 0 of E and O gives a nonzero +-pair
    if len(g) - 1 > val0(g):
        return True, False
    return False, False

def has_repeated(p):
    g = poly_gcd_Q(p, poly_deriv(p))
    if len(g) == 1: return False, False
    nz = (len(g) - 1) > val0(g)
    return True, nz

def integral_spectrum(p, n):
    q = p[:]
    roots = 0
    for m in range(-n, n+1):
        while len(q) > 1:
            # synthetic division by (x-m)
            d = len(q)-1
            new = [0]*d
            carry = q[d]
            for i in range(d-1, -1, -1):
                new[i] = carry
                carry = q[i] + carry*m
            if carry != 0: break
            q = poly_trim(new); roots += 1
    return len(q) == 1

# ---------- enumeration ----------
def run(n, report=True):
    idx = [(i,j) for i in range(n) for j in range(i, n)]
    free = [(i,j) for (i,j) in idx if not (i == 0 and j >= 1)]   # row 0 off-diag pinned to +1
    nf = len(free)
    total = 1 << nf
    CH = 1 << 17
    counts = dict(PAIR0=0, PAIRNZ=0, REP=0, REPNZ=0, CORANK2=0, INTSPEC=0, TEMPLATE=0, TEMPLATE_NZ=0)
    min_nonflag = np.inf
    thr = 1e-7
    base = np.zeros((n,n), dtype=np.int8)
    for start in range(0, total, CH):
        stop = min(start+CH, total)
        m = stop-start
        bits = ((np.arange(start, stop)[:,None] >> np.arange(nf)[None,:]) & 1).astype(np.int8)
        vals = 1 - 2*bits          # 0->+1, 1->-1
        Ms = np.zeros((m,n,n), dtype=np.float64)
        for t,(i,j) in enumerate(free):
            Ms[:,i,j] = vals[:,t]; Ms[:,j,i] = vals[:,t]
        for j in range(1,n):
            Ms[:,0,j] = 1.0; Ms[:,j,0] = 1.0
        ev = np.linalg.eigvalsh(Ms)
        S = ev[:,:,None] + ev[:,None,:]
        iu = np.triu_indices(n,1)
        Spair = np.abs(S[:,iu[0],iu[1]])
        mp = Spair.min(axis=1)
        D = np.abs(ev[:,1:] - ev[:,:-1]).min(axis=1)
        flag = (mp < thr) | (D < thr)
        # integral-spectrum screen
        intflag = (np.abs(ev - np.round(ev)) < 1e-7).all(axis=1)
        allflag = flag | intflag
        nf_mask = ~allflag
        if nf_mask.any():
            min_nonflag = min(min_nonflag, float(min(mp[nf_mask].min(), D[nf_mask].min())))
        for r in np.nonzero(allflag)[0]:
            Mi = np.rint(Ms[r]).astype(np.int64)
            p = charpoly_int(Mi)
            e1, z1 = has_pair_sum_zero(p)
            e2, nz2 = has_repeated(p)
            if e1: counts['PAIR0'] += 1
            if e1 and not (val0(p) >= 2 and not _nonzero_pair(p)): pass
            if _nonzero_pair(p): counts['PAIRNZ'] += 1
            if e2: counts['REP'] += 1
            if e2 and nz2: counts['REPNZ'] += 1
            if val0(p) >= 2: counts['CORANK2'] += 1
            if integral_spectrum(p, n): counts['INTSPEC'] += 1
    return total, counts, min_nonflag

def _nonzero_pair(p):
    E, O = even_odd(p)
    g = poly_gcd_Q(E, O)
    return (len(g) - 1) > val0(g)

if __name__ == '__main__':
    for n in range(2, 7):
        total, c, mnf = run(n)
        print(f"n={n}  normalised matrices={total}")
        for k in ('PAIR0','PAIRNZ','REP','REPNZ','CORANK2','INTSPEC'):
            print(f"   {k:8s} {c[k]:9d}   P = {c[k]/total:.8g}   x 4^n = {c[k]/total*4**n:.4f}")
        print(f"   smallest float margin among UNflagged matrices: {mnf:.3e}")
        sys.stdout.flush()
