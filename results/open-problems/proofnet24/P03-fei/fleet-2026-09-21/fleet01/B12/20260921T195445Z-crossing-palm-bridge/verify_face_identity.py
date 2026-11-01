from fractions import Fraction
from itertools import combinations


def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for s in range(0, len(a), 2 * h):
            for j in range(s, s + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def direct_face_terms(vals, n, i, j):
    N = 1 << n
    both_pivotal = 0
    for x in range(N):
        di = vals[x] != vals[x ^ (1 << i)]
        dj = vals[x] != vals[x ^ (1 << j)]
        both_pivotal += int(di and dj)

    nonaffine = 0
    affine_parity = 0
    for base in range(N):
        if ((base >> i) & 1) or ((base >> j) & 1):
            continue
        v00 = vals[base]
        v10 = vals[base ^ (1 << i)]
        v01 = vals[base ^ (1 << j)]
        v11 = vals[base ^ (1 << i) ^ (1 << j)]

        if v00 * v10 * v01 * v11 == -1:
            nonaffine += 1
        elif v00 == v11 and v10 == v01 and v00 != v10:
            affine_parity += 1

    outside = 1 << (n - 2)
    return (
        Fraction(both_pivotal, N),
        Fraction(nonaffine, outside),
        Fraction(affine_parity, outside),
    )


def main():
    for n in range(2, 5):
        N = 1 << n
        functions = 1 << (N - 1)  # quotient global output sign by f(0)=+1
        checked_pairs = 0
        for mask in range(functions):
            vals = [1] + [
                -1 if (mask >> k) & 1 else 1 for k in range(N - 1)
            ]
            W = fwht_int(vals)
            denom = N * N
            for i, j in combinations(range(n), 2):
                q_fourier = sum(
                    Fraction(W[s] * W[s], denom)
                    for s in range(N)
                    if ((s >> i) & 1) and ((s >> j) & 1)
                )
                q_physical, c_nonaffine, a_parity = direct_face_terms(
                    vals, n, i, j
                )
                assert q_fourier == q_physical
                assert q_physical == a_parity + c_nonaffine / 4
                assert q_fourier >= c_nonaffine / 4
                checked_pairs += 1
        print(
            f"n={n}: functions_mod_sign={functions}, "
            f"function_pairs_checked={checked_pairs}, PASS"
        )

    print("PASS: q_ij = affine_parity_ij + c_ij/4 exactly through n=4.")
    print("This finite check is only a sanity check; the report gives the dimension-free proof.")


if __name__ == "__main__":
    main()
