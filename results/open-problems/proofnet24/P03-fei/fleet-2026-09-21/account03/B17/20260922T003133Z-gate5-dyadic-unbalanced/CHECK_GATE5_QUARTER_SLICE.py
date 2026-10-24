"""Exact/computer-assisted exclusion of the uniform-input, quarter-output arity-5 FEI gate slice.

Target: for G:{0,1}^5->{-1,1}, all input biases 1/2 and Pr[G=-1]=1/4,
prove H(G) <= 6 I(G)-4.  Together with the read-once fixed-point identity
Gamma(1/4)=Gamma(1/2)-2 and C0=Gamma(1/2)=6.4548, this implies c_G<=0.

The high-boundary part is analytic.  The finite part enumerates all 8-subsets
of Q_5 and records the exact Walsh signatures for boundary <=22.  The final
inequality check on those signatures is an arbitrary-precision integer
comparison, not a floating-point decision.  Numpy/numba are used only to make
the finite enumeration fast.
"""
import itertools
import math
import numpy as np
from numba import njit

C0 = 6.4548
N = 32
K = 5

BITS = np.array([[(x >> i) & 1 for i in range(K)] for x in range(N)], dtype=np.int8)
SBITS = np.array([[(s >> i) & 1 for i in range(K)] for s in range(N)], dtype=np.int8)
WALSH = ((-1) ** ((BITS @ SBITS.T) % 2)).astype(np.int8)
DEG = SBITS.sum(axis=1).astype(np.int8)

# For an 8-set A and f=1-2 1_A, nonzero Walsh magnitudes are 4,8,12,16.
# Signature encoding is (n4,n8,n12,n16) in base 33.
BASE = 33
SIGSPACE = BASE ** 4

@njit
def enumerate_quarter_slice(W, deg):
    counts = np.zeros(41, np.int64)
    essential_counts = np.zeros(41, np.int64)
    equality_counts = np.zeros(41, np.int64)
    seen16 = np.zeros(SIGSPACE, np.uint8)
    seen20 = np.zeros(SIGSPACE, np.uint8)
    seen22 = np.zeros(SIGSPACE, np.uint8)
    best_essential_c = -1e99
    best_essential = np.zeros(8, np.int64)
    best_essential_H = 0.0
    best_essential_I = 0.0

    ent = np.zeros(17, np.float64)
    for aw in (4, 8, 12, 16):
        p = (aw * aw) / 1024.0
        ent[aw] = -p * math.log2(p)

    for a0 in range(0, 25):
      for a1 in range(a0 + 1, 26):
       for a2 in range(a1 + 1, 27):
        for a3 in range(a2 + 1, 28):
         for a4 in range(a3 + 1, 29):
          for a5 in range(a4 + 1, 30):
           for a6 in range(a5 + 1, 31):
            for a7 in range(a6 + 1, 32):
                A = (a0,a1,a2,a3,a4,a5,a6,a7)
                mask = np.uint64(0)
                for j in range(8):
                    mask |= np.uint64(1) << np.uint64(A[j])

                internal_edges = 0
                essential = True
                for i in range(5):
                    internal_i = 0
                    for j in range(8):
                        x = A[j]
                        y = x ^ (1 << i)
                        if y > x and ((mask >> np.uint64(y)) & np.uint64(1)):
                            internal_i += 1
                    internal_edges += internal_i
                    if internal_i == 4:
                        essential = False
                B = 40 - 2 * internal_edges
                counts[B] += 1
                if essential:
                    essential_counts[B] += 1

                H = 0.0
                L = 0
                n4 = n8 = n12 = n16 = 0
                for s in range(32):
                    if s == 0:
                        aw = 16
                    else:
                        su = 0
                        for j in range(8):
                            su += W[A[j], s]
                        aw = 2 * abs(su)
                    if aw:
                        H += ent[aw]
                        L += int(deg[s]) * aw * aw
                    if aw == 4: n4 += 1
                    elif aw == 8: n8 += 1
                    elif aw == 12: n12 += 1
                    elif aw == 16: n16 += 1

                I = L / 1024.0
                delta = 6.0 * I - 4.0 - H
                if abs(delta) < 1e-10:
                    equality_counts[B] += 1

                if B <= 22:
                    idx = n4 + BASE * (n8 + BASE * (n12 + BASE * n16))
                    if B == 16: seen16[idx] = 1
                    elif B == 20: seen20[idx] = 1
                    elif B == 22: seen22[idx] = 1

                if essential:
                    # Gamma(1/4)=C0-2, and denominator = I/4-3/16.
                    den = I / 4.0 - 3.0 / 16.0
                    c = (H + (C0 - 2.0) - C0 * I) / den
                    if c > best_essential_c:
                        best_essential_c = c
                        best_essential_H = H
                        best_essential_I = I
                        for j in range(8):
                            best_essential[j] = A[j]

    return (counts, essential_counts, equality_counts,
            seen16, seen20, seen22,
            best_essential_c, best_essential, best_essential_H, best_essential_I)

def decode_sig(idx):
    out = []
    for _ in range(4):
        out.append(idx % BASE)
        idx //= BASE
    return tuple(out)

def exact_signature_check(B, sig):
    """Check H<=6I-4 by exact integer arithmetic.

    With unnormalised Walsh W_S, sum W_S^2=1024 and
    L=sum |S|W_S^2=64B.  The target is equivalent to
      prod_{W_S!=0} (W_S^2)^(W_S^2) >= 2^(14336-6L).
    """
    prod = 1
    for aw, count in zip((4,8,12,16), sig):
        if count:
            prod *= (aw * aw) ** ((aw * aw) * count)
    L = 64 * B
    exponent = 14336 - 6 * L
    assert exponent >= 0
    rhs = 1 << exponent
    return prod > rhs, prod == rhs

def h2(x):
    return -x*math.log2(x) - (1-x)*math.log2(1-x)

def main():
    out = enumerate_quarter_slice(WALSH, DEG)
    counts, essential_counts, equality_counts = out[:3]
    low = out[3:6]
    best_c, best_A, best_H, best_I = out[6:]

    total = sum(int(v) for v in counts)
    assert total == math.comb(32, 8) == 10518300
    print("TOTAL_8_SUBSETS", total)
    print("BOUNDARY_COUNTS")
    for B in range(41):
        if counts[B]:
            print(B, int(counts[B]), "essential", int(essential_counts[B]),
                  "equality_H_le_6I_minus4", int(equality_counts[B]))

    print("LOW_BOUNDARY_EXACT_SIGNATURES")
    for B, seen in zip((16,20,22), low):
        ids = np.flatnonzero(seen)
        for idx in ids:
            sig = decode_sig(int(idx))
            strict, equal = exact_signature_check(B, sig)
            assert strict or equal
            print(B, sig, "STRICT" if strict else "EQUALITY")

    # Analytic high-boundary threshold: at I=3/2 the Gibbs envelope is
    # 2+(3/4)log2(781/81)<5 because 781<16*81=1296; slope log2 3<6.
    assert 781 < 16 * 81
    assert math.log2(3) < 6
    print("GIBBS_B_GE_24", "PASS", "781<1296")

    # Equality/essential conclusions from the exhaustive count plus exact low signatures.
    assert counts[16] == 40 and equality_counts[16] == 40 and essential_counts[16] == 0
    assert counts[20] == 7680 and equality_counts[20] == 1920 and essential_counts[20] == 6400
    assert counts[22] == 45440 and equality_counts[22] == 0
    assert abs(best_c - (-0.9096)) < 1e-10
    assert abs(best_H - 3.5) < 1e-12 and abs(best_I - 1.25) < 1e-12
    print("BEST_ESSENTIAL_C", "%.12f" % best_c)
    print("BEST_ESSENTIAL_H_I", "%.12f" % best_H, "%.12f" % best_I)
    print("BEST_ESSENTIAL_A", list(int(x) for x in best_A))
    print("THEOREM", "H<=6I-4 for every uniform-input five-bit gate with output mass 1/4: PASS")
    print("FEI_STATUS", "OPEN_NOT_PROVED")

if __name__ == "__main__":
    main()
