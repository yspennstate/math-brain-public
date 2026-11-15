"""Leading Hankel minors with m_30: Khinchin test u_k=(2k+1)m_2k and the
semicircle-mixture test w_k=m_2k/Catalan_k, exact."""
import sys, contextlib, io
from fractions import Fraction as Fr
from math import comb
R = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles/verify"
sys.path.insert(0, R)
with contextlib.redirect_stdout(io.StringIO()):
    from order24_threshold import mT as mT22
mT = dict(mT22)
mT[0] = Fr(1)
mT[24] = Fr(1112571762134554, 75075)
mT[26] = Fr(2032842751996209, 7700)
mT[28] = Fr(1141293103886559392, 225225)
mT[30] = Fr(41741563830607349103, 400400)


def det(M):
    M = [r[:] for r in M]; n = len(M); d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            M[i], M[p] = M[p], M[i]; d = -d
        d *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d


def minors(seq, shift, nmax):
    out = []
    for n in range(1, nmax + 1):
        if 2 * (n - 1) + shift >= len(seq):
            break
        out.append(det([[seq[i + j + shift] for j in range(n)] for i in range(n)]))
    return out


K = 15
assert all(2 * k in mT for k in range(K + 1)), sorted(mT)
u = [(2 * k + 1) * mT[2 * k] for k in range(K + 1)]
w = [mT[2 * k] / (comb(2 * k, k) // (k + 1)) for k in range(K + 1)]
print("u_0..5:", u[:6])
for name, s in (("u", u), ("w", w)):
    for sh in (0, 1):
        ms = minors(s, sh, 8)
        print(f"{name} shift {sh}: {len(ms)} minors, all positive {all(m > 0 for m in ms)}, last {float(ms[-1]):.4e}")
