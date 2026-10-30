from fractions import Fraction as F


def sylvester(k):
    H = [[1]]
    for _ in range(k):
        H = [r + r for r in H] + [r + [-x for x in r] for r in H]
    return H


def det3(B):
    return (B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1])
            - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0])
            + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]))


H = sylvester(4)
assert len(H) == 16
assert all(sum(H[i][a] * H[j][a] for a in range(16)) == (16 if i == j else 0)
           for i in range(16) for j in range(16))

lam = [F(2), F(3), F(-4)] + [F(k, 1000) for k in range(1, 14)]
A = [[sum(F(H[i][a] * H[j][a]) * lam[a] for a in range(16)) / 16
      for j in range(16)] for i in range(16)]
assert all(x != 0 for row in A for x in row)
print("min_abs_entry =", min(abs(x) for row in A for x in row))
print("diagonal_entry =", A[0][0])

t = [F(k * k, 10**6) for k in range(1, 14)]
T1 = sum(t, F(0))
T2 = sum(t[i] * t[j] for i in range(13) for j in range(i + 1, 13))
T3 = sum(t[i] * t[j] * t[k]
         for i in range(13) for j in range(i + 1, 13) for k in range(j + 1, 13))
tail = F(244) * T1 + F(29) * T2 + T3
print("T1,T2,T3 =", T1, T2, T3)
print("third_compound_tail =", tail)
print("eta =", tail / F(576))

# A deliberately local three-row bank for the designated fleet02/B04 exact-rank-three theorem.
S = (3, 11, 15)
T = [j for j in range(16) if j not in S]
M = [[A[i][j] for j in T] for i in S]
MM = [[sum(M[i][k] * M[j][k] for k in range(13)) for j in range(3)] for i in range(3)]
Z = det3(MM)
assert Z > 0
print("partner_E3 =", Z)
print("partner_bound_float =", 6 * float(Z) ** (-1 / 6))
