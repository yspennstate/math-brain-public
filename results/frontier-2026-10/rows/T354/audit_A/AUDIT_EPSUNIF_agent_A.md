# Audit 2 of the eps > 0 remainder, uniform in n (agent_B/NOTE.md, "The remainder, uniform in n", last paragraph)

agent A, 20 Oct 2026 10:3x. Audit 1 is agent C's audit_C/AUDIT_EPS_agent_C.md. Claim, at beta1 = 0,
a_i = 1 and fixed eps >= 0: (s + eps) D(x) = x + p1 d K_rr (2 x B2 + B3)/V + x e1(x) + e2(x), with |e1| <= C d and |e2| <= C d^2 on
|x| <= rho for all n >= 4. Hence x* = r x0 (1 + O(d)) uniformly in n, where s = sqrt(V) and r = s/(s + eps).

Verdict: CONFIRMED (11:0x). The hand part checks (items 1-5), and all six Monte Carlo rows agree with the exact roots within 1.6 se, from
n 10 to n 500 at eps 1 and eps 3.

## By hand

1. eps enters only through psi(y) = (s + eps)/(s sqrt(y) + eps). The quantities eta, v, V, the permutation moments and the bounds on
   E[b eta_c^k] from the verified eps = 0 argument contain no eps, so each of those steps carries over word for word.
2. The substitution is the Taylor coefficients p1, p2/2, p3/6, not p1, p2, p3. They were derived by series in AUDIT_CEPS, part A.
   I agree with audit 1's correction of the NOTE's first wording; the NOTE now reads "Taylor coefficients p1, p2/2, p3/6".
3. The step that is new at eps > 0 is the cubic Taylor remainder R of psi at y = 1, taken over the range the stream can reach.
   v is a convex combination of the g_i^2, so y lies in [min g^2/V, max g^2/V].
   - Audit 1 bounds R through sup |psi''''|. That constant is very large on this model (6.6e7 at eps 0), because psi'''' blows up as
     y approaches y_min.
   - Here I measured the quantity that is actually used, sup |R|/u^4 with u = y - 1, directly (epsunif/taylor_rem.py, run1.txt).
   - On the 9/-1 model with |x| <= 0.5 (y in [0.027, 9.76]), sup |R|/u^4 is 4.41, 3.52, 1.04, 0.317, 0.0735 and 0.0060 at
     eps 0, 0.1, 1, 3, 10 and 100. Divided by r, these are 4.41, 3.63, 1.39, 0.63, 0.32 and 0.21.
   - So |R| <= 4.5 r u^4 for every eps on this range. The bound is free of n, and it is also uniform in eps relative to the
     first-order scale r. This is a sharper form of audit 1's "does not grow with eps".
   - Near u = 0 the eps = 0 ratio is 0.286 against the series coefficient 35/128 = 0.273, which checks the code.
   - The eps = 1e4 row, sup/r about 0.4 at u = -0.001, is float cancellation and not a feature of psi.
   - Then E[g R] <= C r E eta^4 = O(r d^2), using the verified E eta^4 = O(d^2).
4. s, r and the p_k depend on x through V = x^2 + B2 only. At the zero, x* = O(d), so they move by O(d^2) relative. Their product with
   terms of size d K_rr or x d is O(d^3). Audit 1 makes the same point.
5. The zero: x (1 - r d K_rr B2/V + e1) = r d K_rr B3/(2V) - e2. The bracket is 1 - O(d), so |x*| <= C d, and x* = r x0 (1 + O(d)).
   The sign change at r x0 +- C' d^2 gives existence. Both are the eps = 0 argument with r carried through.

## Monte Carlo of the stream (rrm_mc_cv_eps.py; own code, no shared solver with rrm_eps.py)

The question is uniformity in n: whether (x*/(r x0) - 1)/d stays bounded from n = 10 up to n in the thousands, at eps 1 and eps 3.
Audit 1's exact table starts at n = 100. For the small-n rows I ran audit 1's solver rrm_eps.py at those four points
(epsunif/exact_small_n/). Seed 7, 4000 chains (rrmc_epsunif_batch.sh, rrmc_epsunif_out/).

| eps | n | beta2 | n d | MC | exact (rrm_eps.py) | MC - exact, in se |
|---|---|---|---|---|---|---|
| 1 | 10 | 0.99 | 0.1 | -1.08939 +- 0.00003 | -1.089407 | +0.6 |
| 1 | 20 | 0.99 | 0.2 | -1.04362 +- 0.00008 | -1.043502 | -1.5 |
| 3 | 100 | 0.99 | 1 | -0.7092 +- 0.0009 | -0.708233 | -1.1 |
| 3 | 500 | 0.99 | 5 | -0.3844 +- 0.0034 | -0.379022 | -1.6 |
| 1 | 10 | 0.999 | 0.01 | -1.10467 +- 0.00001 | -1.104672 | below 0.04 |
| 3 | 10 | 0.999 | 0.01 | -0.93439 +- 0.00001 | -0.934392 | below 0.06 |

At d = 0.001 the MC prints x0 to 8 digits, and that rounding moves the coefficient by about 1e-5, the size of its error bar. So the last
two rows compare x* itself: MC 0.001503825945 +- 1.5e-11 against 0.00150382594451, and 0.001002721532 +- 8e-12 against 0.00100272153204.
They agree to the 10 digits the MC prints. That is tighter than the error bars lead one to expect (both under 0.06 se, about 1 chance in 400),
so the chain-spread error bar may be conservative at beta2 0.999. A conservative bar does not weaken the agreement.

With the eps 1 rows of AUDIT_CEPS (n 100 to 2000, all within 1.6 se), the coefficient runs from -1.10 at n 10 to +0.06 at n 1000.
It is bounded on n = 10 to 2500 at both eps, and its size is set by n d, not by n. This is what x* = r x0 (1 + O(d)) uniformly in n
predicts.
