# T354 at every n: closed-form reshuffling factor and the law uniform in n(1 - beta2) (agent C, 20 Oct 2026 07:3x)

Object: agent_B/NOTE.md, section "Every n: the reshuffling factor in closed form, and the law uniform in n(1 - beta2)"
(push 17c04a29, candidate). This is audit 1.

Verdict:
- The closed form for K_rr: CONFIRMED, two independent ways.
- The exact roots: CONFIRMED. Every cell of the note's table is reproduced to its printed digits by a solver written without
  reading rr_exact_m.py or rr_exact_m2.py.
- x*/x0 = 1 + d c(n d) + O(d^2) with c bounded: SUPPORTED on 19 roots, n d from 0.1 to 20. The rate at which c -> 1 is a little slower than
  the note says: about 3.5/(n d) at n d = 20, not 3.2 (below).
- The uniform remainder: not audited here. The note has since written it out (push 82ce66d6); it is audited separately in
  AUDIT_UNIFORM_agent_C.md.

## K_rr (kcheck_indep.py, kcheck_indep.txt)

1. Lag sum from first principles.
   - E[g_{k-i} Z_{k-j}] is C when i = j, -C/(n-1) when i != j and the two steps fall in one epoch, and 0 otherwise.
   - With the step's position in its epoch uniform, lags i and i + delta (delta < n) share an epoch for n - delta of the n
     positions, whatever i is.
   - So K = (1-b1)[sum_i (b1 b2)^i - (1/(n-1)) sum_{0 < |i-j| < n} b1^i b2^j (n - |i-j|)/n].
   - Against the note's closed form, over n 2, 3, 10, 37, 100, 400 x beta1 0, .5, .9 x beta2 .9, .99, .999, the largest
     difference is 1.4e-11.
   - At beta1 = 0 the sum is 1 - sum_{j=1}^{n-1} (n-j) beta2^j/(n(n-1)). For n = 2 that is the note's formula exactly, by hand.
2. Monte Carlo of E[m eta]/(d C/V) itself on reshuffled epochs at x = 0 (9 on a tenth of the samples, -1 on the rest):

| n | beta1 | beta2 | K by Monte Carlo | closed form | iid value |
|---|---|---|---|---|---|
| 50 | 0 | .99 | 0.5757 +- 0.0002 | 0.5757 | 1 |
| 500 | 0 | .99 | 0.8422 +- 0.0021 | 0.8410 | 1 |
| 50 | .9 | .99 | 0.3935 +- 0.0007 | 0.3932 | 0.9174 |
| 200 | .5 | .995 | 0.6253 +- 0.0009 | 0.6249 | 0.9950 |

All four are within 0.6 standard errors.

## Exact roots (rrm_indep.py, rrmi_batch.sh, rrmi_out/)

The model is the note's: b = 9 on n/10 samples and -1 on the rest, beta1 = 0, eps = 0, frozen x.

The solver:
- It uses 1/sqrt(v) = (2/sqrt(pi)) int exp(-s^2 v) ds with Gauss-Legendre in s, and v = q + d (A - q) S.
- In the current epoch, the special count among the visited lags is hypergeometric given g_k's type. Given that count, the
  specials are a uniform subset, which is a normalized elementary-symmetric mean built by the convex recursion
  M_h(t) = ((t-h)/t) M_h(t-1) + (h/t) z_t M_{h-1}(t-1).
- Each earlier epoch contributes G(w beta2^L), tabulated on a log grid with a log-scaled recursion so nothing underflows, and
  splined.
- K_rr comes from the lag sum, not from kfactor.py.

Agreement:
- At n = 10 and n = 100 the roots agree with the note's to 4e-10 and 5e-10 relative. That is 5e-8 or less in (x*/x0 - 1)/d.
- 320 nodes and a 4000-point grid (n 500, beta2 .99) give the same root to 1e-12 as 200 and 2400.

(x*/x0 - 1)/d, independent solver (the note's value in brackets where it has one):

| n d | d = 0.01 | d = 0.005 | d = 0.002 |
|---|---|---|---|
| 0.1 | -1.247264 (n 10) [-1.247] | -1.224721 (n 20) [-1.225] | -1.210754 (n 50) [-1.211] |
| 0.5 | -0.960190 (n 50) [-0.960] | -0.931860 (n 100) [-0.932] | -0.914710 (n 250) [-0.915] |
| 1 | -0.648602 (n 100) [-0.649] | -0.618092 (n 200) [-0.618] | -0.599954 (n 500) [-0.600] |
| 2 | -0.217418 (n 200) [-0.217] | -0.187681 (n 400) [-0.188] | -0.170391 (n 1000) [-0.170] |
| 5 | +0.332648 (n 500) [+0.333] | +0.357565 (n 1000) [+0.358] | +0.371564 (n 2500) [+0.372] |
| 10 | +0.621347 (n 1000) | +0.641626 (n 2000) | |
| 20 | +0.792074 (n 2000) [+0.792] | +0.808649 (n 4000) | |

What the table shows:
- At fixed n d each row moves linearly in d, with a slope of 3 to 7 per unit d (smaller at larger n d). That is the O(d^2) term in x*/x0 with a
  constant that does not grow with n. For example, at n d = 2 the steps are 0.0297 over 0.005 and 0.0173 over 0.003.
- The d -> 0 limits are about -1.20, -0.90, -0.58, -0.16 and +0.38 at n d 0.1, 0.5, 1, 2 and 5.
- Every cell the note prints is reproduced to its last digit, including +0.372 (n 2500) and +0.792 (n 2000).
- The n d = 10 row is not in the note; it was added to test the note's 1/(n d) rate, which rests on two points (n d 5 and 20).
  So is the n 4000 cell at n d = 20.
- At n d = 20 the note extrapolates from d = 0.02 and 0.01 and gets c(20) = 0.833. The d = 0.02 root is already outside the
  linear range: the step per unit d is 4.1 between d = 0.02 and 0.01 but 3.3 between 0.01 and 0.005. From d = 0.01 and 0.005,
  c(20) = 0.8252; a three-point Richardson fit with the note's +0.751 gives 0.8226.
- Extrapolating the other rows from their two smallest d: c(5) = 0.3809 and c(10) = 0.6619.
- So (1 - c) n d is 3.10, 3.38 and 3.50 (3.55 by Richardson) at n d 5, 10 and 20. It still levels off, so c -> +1 at a 1/(n d)
  rate, but the constant is nearer 3.5 to 3.7 than the note's 3.2, which came from two points, one of them the d = 0.02 root.
  Neither changes the claim that c is bounded and tends to 1; the sentence giving the rate should be revised.

## Not covered

- The uniform-in-n remainder argument. The counting sketch, that E eta^4 = O(d^2) and the without-replacement mixed moments
  pay for the lag counts, is plausible but not checked line by line.
- Momentum and eps > 0 at large n d.
- Any other distribution of b.
- A closed form for c(s).
