# Audit of agent B's next-order term under reshuffling with momentum (T354, NOTE section of 04:1x, push 12aff637)

Auditor agent A, 20 Oct 2026 04:2x. Claim, eps = 0, fixed n and beta1, d = 1 - beta2 -> 0:

    x*/x0 = 1 + d (K - (3/4) T H/(K B2 B3)) + O(d^2),   H = (1/n) sum_p (1 - beta1^(p+1)) h(p),
    h(p) = 1 - 3p/(n-1) + 2p(p-1)/((n-1)(n-2)).

Verdict: CONFIRMED (H re-derived by hand and checked by exact enumeration). One table entry in the NOTE is mislabelled; see the end.

## H by hand

At x = 0 and beta2 = 1 (both corrections are O(d^3) in the solve), the quadratic term is (d/B2)^2 E[m (sum_j Z_(k-j))^2], with
m = (1 - beta1) sum_i beta1^i b_(k-i). Permutations of different epochs are independent, and E b = E Z = 0 at a single slot, so
E[b_s Z_t Z_u] vanishes unless s, t, u lie in one epoch. If s is in a full earlier epoch, the sum over t, u in that epoch is
E[b_s (sum Z)^2] = 0, because a full epoch sums Z to zero. That leaves momentum lags i <= p in the current epoch, with t, u over its
p + 1 past slots. The three-slot moments of a uniform permutation, from sum b = sum Z = 0, are:

    same slot: T;   b_s Z_s Z_t or b_s Z_t Z_t (t != s): -T/(n-1);   s, t, u distinct: 2T/((n-1)(n-2)).

The counts, with i fixed, are 1, 2p + p and p(p-1). The bracket is T h(p), the same for every i <= p, and the momentum weights of
those lags sum to 1 - beta1^(p+1). Averaging over p gives E = T H. The solve
x (1 - d K) = d K B3/(2 B2) - (3/8)(d/B2)^2 T H then gives the stated bracket.

## Exact enumeration (rr_mom_H_check.py, rr_mom_H_check_run1.txt)

n = 6, random b with mean 0. Every permutation of the current epoch, crossed with every permutation of one full earlier epoch
(518,400 pairs per p), at beta1 = 0, 0.5, 0.7 and 0.9: E/T equals H to 12 digits (0.166666666667, 0.069791666667, 0.030939000000,
0.004219666667), with and without the earlier epoch, which contributes nothing.

## The coefficients

Test model (n 10, B2 9, B3 72, T 4608), with K -> K0: H = 0.166667, 0.129495, 0.094488, 0.008737 and the limit coefficient
-1.277778, -1.044874, -0.814764, -0.156625 at beta1 = 0, 0.3, 0.5, 0.9. The 0.5 and 0.9 values match the NOTE.
The NOTE's beta1 0.3 row lists -1.0413 "(K-form)". That is the bracket at finite d, not the limit. The limit is -1.044874, and the
exact roots in the same row (-1.04283 at 0.9995, -1.04081 at 0.999) extrapolate linearly to -1.04485, which agrees with it. The row's
"gap -2.90" is measured from the finite-d value, so it is not comparable with the -0.7 and 6.2 of the other rows.

## Not covered

- eps > 0 under reshuffling (the NOTE says it is not done).
- The O(d^2) remainder is not bounded here; the flat gaps in the NOTE's table are its evidence.
