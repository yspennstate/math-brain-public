# T354: x*/x0 = 1 + O(d) uniformly in beta1, audit 1 (agent C, 20 Oct 2026 10:0x)

Object: agent_B/NOTE.md, "Uniform in beta1" (09:5x, candidate): |e2| <= C d^2 K_rr(beta1) with C free of n and beta1, so
x*/x0(beta1) = 1 + O(d) uniformly in n and beta1 when B3 != 0.

Verdict: CONFIRMED. Steps 1-4 hold as written. The identity of step 2 is exact in an enumeration written apart from the note's. The
exact root's relative error stays O(d) while K_rr(beta1) falls a hundredfold.

## Step 2, the transposition identity (transp_indep.py, transp_indep.txt)

- My own code: one epoch of n slots, all n! orders, and the other epochs as an independent two-point offset of +-0.05 added to eta.
- The weights w and a are random and NOT comonotone, so the test covers the identity for any weights. Comonotonicity is used only in
  step 4.
- Left side sum_q w_q E[b_pi(q) F(eta)] against the right side (1/4n) sum (w_q - w_r)(a_q - a_r) E[Db DZ int F'], with the t integral by
  20-point Gauss-Legendre. Relative difference 5e-15 to 5e-14 at n 5, 6 and 7, eps 0 and 1.
- By hand: X_q - X_r = E[Db F(eta)]. Composing pi with the transposition (q r) preserves the law, so this also equals -E[Db F(eta')].
  Halving the sum gives (1/2)(a_q - a_r) E[Db DZ int F'], and with the (1/2n) of the pair sum that is the (1/4n). The pair-sum form
  needs sum_q X_q = 0, which holds because b is centred over the items and all n slots of the epoch are in the sum (w = 0 on unseen
  slots).

## Step 3, E[Db DZ int F'] = O(d) free of n and beta1 (by hand)

- Range. With the infinite past, v is a convex combination of the g^2 values (weights (1 - beta2) beta2^j, summing to 1). The swapped
  eta' is one too, and so is every point between them. So y stays in [min g^2/V, max g^2/V] and psi is smooth there, at eps 0 when no
  g_i = 0, and at every eps >= 0.
- Hence |F'(xi) - p2 xi| <= C xi^2 there, with C depending only on b and eps.
- Linear part. Epochs other than e: independent of the epoch-e order, and E Z_pi(s) = 0, so they drop out. That includes the current,
  partly seen epoch when it is not e.
- Inside epoch e, given pi(q) = i and pi(r) = j, eta's epoch-e part has conditional mean
      a_q Z_i + a_r Z_j - (Z_i + Z_j) A'/(n - 2),   A' = sum_{s != q, r} a_s <= (n - 2) d/V.
  Each coefficient is at most 2 d/V in size, so |E[Db DZ eta]| <= 4 (d/V) max|Db DZ| max|Z|, with no n and no beta1. The t (a_q - a_r) DZ
  term is O(d) in the same way.
- Quadratic part. E xi^2 <= 2 E eta^2 + O(d^2). E eta^2 <= (n/(n - 1)) var(Z) sum_lags a^2 = O(d/V^2).
- A remark, not a gap. When a is nearly flat over an epoch (n d small), the three coefficients nearly cancel and the term is O(d^2).
  The n = 6 enumeration shows exactly this: max |E[Db DZ int F']|/d falls like d from d 0.1 to 1e-4. The bound O(d) is the n d = O(1)
  case.

## Step 4 (by hand)

- (n/(2(n - 1))) S_e = sum_q w_q a_q - (1/(n - 1)) sum_q w_q (A - a_q), with A = sum_q a_q.
- That is kfactor.py's summand wm (wv - (S[ep] - wv)/(n - 1)) term by term, with a = (d/V) wv. So d K_rr/V = (n/(2(n - 1))) sum_e S_e,
  averaged over p as kfactor does.
- S_e >= 0 for comonotone w and a, so K_rr >= 0 for every beta1. And |T_e| <= (C d/4) S_e sums to |e2| <= C' d . d K_rr.
- The rest of the root equation: the root solves x(1 + E F) + p1 E[(w.b) eta] + e2 = 0.
  - E F = O(E eta^2) = O(d), with no beta1 in it.
  - The 2 x B2 part of E[bZ] moves x by a relative d K_rr B2/V, and K_rr <= sum_lags wm wv <= 1.
  - So x*/x0 = 1 + O(d) with the constant free of n and beta1.

## The exact root at beta1 -> 1 (rrm3m.py, r3mu_batch.sh, r3mu_out/)

b = (6, 2, -1) with weights 0.1, 0.1, 0.8, eps 0, n d = 1, x0 = d K_rr B3/(2 B2). The table gives (x*/x0(beta1) - 1)/d, with
K_rr(beta1) in brackets:

| beta1 | d = 0.02 (n 50) | d = 0.01 (n 100) | d = 0.005 (n 200) |
|---|---|---|---|
| 0.99 | 0.6364 [0.0710] | 0.6186 [0.1346] | 0.5408 [0.2348] |
| 0.999 | 0.6773 [0.00687] | 0.7007 [0.01368] | 0.7033 [0.02751] |
| 0.9999 | 0.6816 [0.00068] | 0.7100 [0.00134] | |

- From beta1 0.99 to 0.9999, K_rr falls by a factor of 100 at fixed d. The coefficient stays between 0.54 and 0.71.
- If e2 were O(d/K_rr) relative, the coefficient would grow a hundredfold. It does not move.
- At beta1 0.999 and 0.9999 the rows have already settled, near 0.70 to 0.71 (A's 9/-1 table levels off near 1.1 on another b).
- At beta1 0.99 the row is still moving with d, as at beta1 0.9 in AUDIT_MOMENTUM2, where the d^2 term grows like beta1/(1 - beta1).
  It stays bounded.

## eps = 1 at beta1 -> 1 (added 20 Oct 10:2x; r3meu_batch.sh, r3meu2_batch.sh, r3meu_out/)

Same b and n d = 1, EPS=1 in rrm3m.py. The printed coefficient is (x*/(r x0) - 1)/d with r = sqrt(B2)/(sqrt(B2) + 1) = 0.686608
(the printed x0 already carries r: 2.1141e-4 against 3.0791e-4 at eps 0, n 100, beta1 .999). K_rr(beta1) in brackets:

| beta1 | d = 0.02 (n 50) | d = 0.01 (n 100) | d = 0.005 (n 200) |
|---|---|---|---|
| 0.99 | 0.3856 [0.0710] | 0.3661 [0.1346] | 0.2965 [0.2348] |
| 0.999 | 0.4226 [0.00687] | 0.4399 [0.01368] | 0.4412 [0.02751] |
| 0.9999 | 0.4263 [0.00068] | 0.4478 [0.00134] | 0.4570 [0.00267] |

- The eps = 0 picture again: K_rr falls a hundredfold from beta1 .99 to .9999 and the coefficient stays between 0.30 and 0.46.
- The beta1 .999 row has settled near 0.44. The .9999 row still rises with falling d, by 0.022 and then 0.009, so it is converging
  (Richardson order 1 gives 0.466). The .99 row moves with d as at eps 0. All rows stay bounded.

## Not covered

- T/(d S) on the note's own three b's (uniform_b1/run_eps0.txt, run_eps1.txt). Those were not re-run; the exact roots above test the
  conclusion directly.
- eps other than 0 and 1 at beta1 -> 1 on the exact root. Step 3 covers eps >= 0 by hand.
- A finite past, where the v weights do not sum to 1 and E eta != 0. The note's setting is stationary.

Files: transp_indep.py, transp_indep.txt, r3mu_batch.sh, r3mu_out/, r3meu_batch.sh, r3meu2_batch.sh, r3meu_out/ (rrm3m.py as in AUDIT_MOMENTUM2).
