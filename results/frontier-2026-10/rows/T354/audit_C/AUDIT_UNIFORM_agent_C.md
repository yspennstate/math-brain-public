# T354: the remainder uniform in n, audit 1 (agent C, 20 Oct 2026 07:4x)

Object: agent_B/NOTE.md, section "The remainder, uniform in n" (push 82ce66d6, candidate).
The claim is for random reshuffling with beta1 = 0, eps >= 0 and a_i = 1:

    D(x) sqrt(V) = x - (d K_rr/2)(2 x B2 + B3)/V + E2(x), with |E2| <= C d^2 for all |x| <= rho and all n >= 4,

and hence x* = x0 (1 + O(d)) uniformly in n.

Verdict:
- The conclusion x* = x0 (1 + O(d)) uniformly in n: CONFIRMED, with one line of the argument corrected.
- The bound on E2 as stated: REFUTED. E2 contains (3/8) x E eta^2, which is of order x d, not d^2. The true bound is
  |E2| <= C d (|x| + d). At a zero this is enough, because every zero in |x| <= rho has |x| <= C d, so the conclusion stands.
- The three steps the request asked to break all hold:
  - |E[b eta_c^2]| <= 8 |E[b Z^2]| (d/V)^2. It holds, and in fact the quantity is an exact multiple of E[b Z^2], with |coefficient| <= 6.
  - E[b eta_c^3] = O(d^2). It holds.
  - E S^4 <= 14 (s2^2 A2^2 + m4 A4) for n >= 4. It holds, and 14 is attained at n = 4.
- Steps 1, 2 and 4 were rederived by hand and agree. So do the exactness of E[g eta] and the eta_f decoupling in step 5.

## The E2 bound (uniform_check.py part 3, uniform_check2.py)

The expansion is psi(y) = 1 - eta/2 + (3/8) eta^2 - (5/16) eta^3 + R. With E[g eta^2] = x E eta^2 + E[b eta_c^2], the
eta^2 term contributes (3/8) x E eta^2 to E2. At x = O(1) that is of order d, because E eta^2 is of order d. So the line
"|E2| <= C d^2 for all |x| <= rho" cannot hold.

This was checked with the independent exact solver of the large-n audit, rrm_indep.py, at x = 0.1 and n d = 1:

| n | d | E2 | E2/d^2 | E2/(x d) |
|---|---|---|---|---|
| 100 | 0.01 | 6.114e-4 | 6.11 | 0.611 |
| 200 | 0.005 | 2.439e-4 | 9.75 | 0.488 |
| 400 | 0.0025 | 1.070e-4 | 17.11 | 0.428 |

- E2/d^2 doubles each time d halves.
- A fit gives E2 = 0.365 x d + 2.46 d^2, with residuals under 3.2e-7.
- An independent check: E eta^2 computed exactly from the permutation formula, epoch by epoch, gives (3/8) E eta^2/d =
  0.376, 0.373 and 0.371. That is the fitted 0.365 up to the next order.

The fix is one line.
- Write E2 = x e1(x) + e2(x), with |e1| <= C d and |e2| <= C d^2. Then x e1 = (3/8) x E eta^2 - (5/16) x E eta^3 + ..., and e2
  holds the b terms and E[g R].
- At a zero, x (1 - d K_rr B2/V + e1) = d K_rr B3/(2V) - e2. The bracket is 1 - O(d), so |x*| <= C d. Then x* e1 = O(d^2), and
  the note's displayed equation for x* follows.
- The sign change at x0 +- C' d^2 survives too, since |x| = O(d) there.
- The same correction applies to the eps > 0 version, with p2/2 in place of 3/8 (p2 is psi''(1), a derivative; see
  AUDIT_EPS_agent_C.md).

## E[b eta_c^2] (uniform_check.py part 2, uniform_check2.py (c))

Write Z_k + W, with W = sum_{j=1..p} beta2^j Z_pi(p-j). Each of the three pieces of E[b (Z_k + W)^2] reduces to E[b Z^2] by the
distinct-index sums:
- E[b_i Z_i'] = -E[bZ]/(n-1).
- E[b_i Z_i'^2] = -E[b Z^2]/(n-1).
- For three distinct indices, E[b_i Z_i' Z_i''] = 2 E[b Z^2]/((n-1)(n-2)).

So, exactly,

    E[b (Z_k + W)^2] = c_n(beta2) E[b Z^2],
    c_n = avg_p [1 - (2 sum_j beta2^j + sum_j beta2^(2j))/(n-1) + 2 sum_{j != l} beta2^(j+l)/((n-1)(n-2))], with j, l in 1..p,

and |c_n| <= 1 + 2 + 1 + 2 = 6. The note's pieces 1, 2 and 4 give a total of 7, inside its 8.

The coefficient was checked by brute force over all permutations, with random b and x = 0.2:

| n | beta2 | brute force | formula |
|---|---|---|---|
| 6 | 0.5 | 0.710 | 0.710 |
| 7 | 0.8 | 0.429 | 0.429 |
| 8 | 0.9 | 0.315 | 0.315 |
| 8 | 0.99 | 0.182 | 0.182 |

The ratio is the same for every random draw of b, as the identity requires.

## E[b eta_c^3] = O(d^2)

Condition on pi(p) = i. The other slots are then a uniform permutation of the other n - 1 values, whose sum is -Z_i, not 0.
So W = M + W0, where:
- M = -Z_i sum_j beta2^j/(n-1), with |M| <= max |Z|;
- W0 is a centred permutation sum over n - 1 values.

Then E[(c + W0)^3] = c^3 + 3 c E W0^2 + E W0^3, with c = Z_i + M bounded.
- E W0^2 = O(A2) = O(1/d).
- E W0^3 = O(A3) = O(1/d), by the E S^3 formula at n - 1 >= 3.

So E[b eta_c^3] = (d/V)^3 O(1/d) = O(d^2). The note's sentence leaves out the 3 c E W0^2 piece. That piece is the same order,
so the claim is unaffected.

The brute-force values of d E[b (Z_k + W)^3] (part 2) stay between -2 and 0.24 for n 6 to 8 and beta2 0.5 to 0.99.

## E S^4 and the constant 14 (uniform_check.py part 1)

The note's E S^2, E S^3 and E S^4 were checked against brute force over all permutations, for n 5, 6 and 7 with random a and
z of sum zero. The largest relative difference is 2.6e-13.

Dropping the two negative terms bounds E S^4. What is left has these coefficients:

| term | coefficient | value at n = 4 | for n >= 4 |
|---|---|---|---|
| s2^2 A2^2 | 3 n (n^2-3n+3)/((n-1)(n-2)(n-3)) | 14 | its maximum |
| m4 A4 | n^2 (n+1)/((n-1)(n-2)(n-3)) | 13.33 | its maximum |

Both decrease in n, so the 14 is sharp at n = 4.

The centring step is also right: sum (w - mean)^4 <= 8 (sum w^4 + n mean^4) <= 16 sum w^4, by the power mean.

## Rederived by hand and agreeing

- Step 1: v is a convex combination of the g^2, so y lies in [gamma/V, max g^2/V], and the Taylor remainder of psi is
  C eta^4.
- Step 4: E eta_f^4 = sum E eta_e^4 + 3 sum_{e != f} E eta_e^2 E eta_f^2 <= sum E eta_e^4 + 3 (E eta_f^2)^2. Each sum of A2 is
  at most 1/(1 - beta2^2) <= 1/d, so E eta^4 = O(d^2).
- Step 5: E[g eta] = d K_rr E[bZ]/V exactly. The p-average of 1 - sum_{j<=p} beta2^j/(n-1) is the lag-sum K_rr of the large-n
  audit, and E[bZ] = 2 x B2 + B3. The eta_f cross terms vanish because eta_f is independent of the current epoch and has mean 0.
  The term 3 E[b eta_c] E eta_f^2 is O(d) O(d).

## Not covered

- Uniformity needs a family of multisets along which gamma/V, max |b|, max |Z|, s2 and m4 stay bounded, as in the 9/-1
  model. The note says so in its first paragraph.
- Momentum, which the note also leaves open.
- A second audit.

Files: uniform_check.py, uniform_check.txt, uniform_check2.py, uniform_check2.txt. They use rrm_indep.py from the large-n
audit.
