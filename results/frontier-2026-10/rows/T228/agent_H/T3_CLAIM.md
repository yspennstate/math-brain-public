# T228 target 3: class (A) single-index SGD in R^d. Claim, version 2

agent H, 22 Oct 2026 04:5x (v1), 05:2x (v2). STATE: REVIEWED_ONCE. Independent review by agent AF
(REVIEW.tsv, 22 Oct 02:09Z): 16 PASS, 0 FIX, 0 FAIL; its one OPEN row (novelty) is answered in T3_NOVELTY.md. A second
independent audit is still wanted before VERIFIED. The mathematics is unchanged from v1.

## Model
d >= 1, b >= 1, eta > 0, c = eta/b. Each step draws fresh a_i ~ N(0, I_d) and eps_i ~ N(0, s^2), i <= b, s > 0, with
y_i = sigma(a_i.x*) + eps_i, and sets
    x_(k+1) = Psi_k(x_k) = x_k - c sum_(i<=b) sigma'(a_i.x_k) (sigma(a_i.x_k) - y_i) a_i.
Class (A): sigma(z) = z + phi(z) with r := sup|phi'| < 1, sup|phi| < oo and sup|z phi'(z)| < oo (the dossier's class (A)
assumes more: phi in C^2 and z phi'' bounded; those are not used).

Put xi := sqrt((1 - cX)^2 + c^2 X Y) with X ~ chi2_b and Y ~ chi2_(d-1) independent (Y = 0 when d = 1), h(p) = E xi^p, and
assume
    (S_d)  gamma := E log xi < 0.

## Theorem
Under class (A), s > 0 and (S_d):
 (1) the chain has a unique invariant probability pi; it has a density bounded below on every ball, and P^n(x, .) -> pi
     geometrically fast in the (1 + |x|^p)-weighted norm for every p < alpha;
 (2) t^alpha P_pi(|x| > t) -> c0 with 0 < c0 < oo, where
         c0 = E[ |Psi(x)|^alpha - |M x|^alpha ] / (alpha E[xi^alpha log xi]),   M = I - c sum a_i a_i^T,  x ~ pi independent;
     in particular E_pi |x|^p < oo exactly for p < alpha;
 (3) alpha is the unique positive root of E[ ((1 - cX)^2 + c^2 X Y)^(alpha/2) ] = 1;
 (4) for every (d, b), alpha < 2 on a nonempty interval of eta: E xi^2 = 1 - 2 eta + eta^2 (b + d + 1)/b, so alpha < 2
     iff eta > eta0 := 2b/(b + d + 1), and (S_d) holds on (eta0, eta0 + delta) for some delta > 0.
For d = 1 this is target 1's class (A) statement with an explicit c0.

## Where each part is proved
- Lemma R (|M u| =_d xi for every unit u, and the pairs (|M_k u_k|, B_k) are iid along the chain): T3_SETUP.md.
- (1), the index (Lemma 1), drift and minorization: T3_STEP1.md, Theorem 1. Uses Hairer-Mattingly Theorem 1.2
  (arXiv 0810.2777v1, read on the page).
- (2), existence of the limit and the formula for c0 >= 0: T3_STEP2.md, Theorem 2. Uses Goldie's implicit renewal
  theorem in the form of Jelenkovic-Olvera-Cravioto arXiv 1006.3295v5, Theorem 3.1 (read on the page).
- (2), c0 > 0 and the infinite alpha-moment: T3_STEP3.md, Theorem 3. Self-contained: forward radial bound, a tilted
  random walk, a last-exit decomposition of pi.
- (3): Lemma 1 of T3_STEP1.md with Lemma R.
- (4): T3_SETUP.md (c), (d): at eta0, h(2) = 1 and strict Jensen gives gamma < 0; continuity in eta.

## Why the known theorems do not already give it
Mirek (PTRF 2011), the source of GSZ Theorem 1, requires M in R_+ x K with K a subgroup of O(d), i.e. similarities;
I - c sum a a^T is not one when d >= 2. ABB (2102.02299) is on the real line. The new point is that Gaussian data make
|M_k u_k| independent of the direction u_k, so the norm of the d-dimensional chain is an exact one-dimensional implicit
renewal problem, and the positivity of c0 can be proved forward in time without operator norms.

## Checks done since v1
- Novelty (T3_NOVELTY.md): web search in three wordings found linear-regression results (GSZ 2006.04740, with a
  direction-dependent constant), general implicit-renewal frameworks and a scalar paper (ABB), but no statement for a
  nonlinear link in d >= 2 with a positive norm constant. Web only, not an arXiv full-text sweep.
- Numbers (t3_tail_check.py, t3_tail_check_run1.txt, seed 1; sigma = z + 0.5 tanh z, x* = e1, s = 1; 4,000 chains x
  100,000 steps, 19M thinned samples): at (d, b, eta) = (2, 1, 0.6) the root of h is alpha = 1.3015, Hill gives
  1.296-1.308 over k = 5.7k-190k, and c0 by the formula of (2) is 2.247 +- 0.007 against t^alpha P(|x| > t) = 2.23 at
  the 0.99, 0.999 and 0.9999 quantiles. At (2, 1, 0.8): alpha = 0.4023, Hill 0.399-0.410, c0 formula 1.401 against
  1.42-1.445 empirically (about 2 percent; slower second-order convergence at small alpha). At (3, 2, 0.9): alpha =
  0.3576, Hill 0.356-0.372 for k >= 19k (0.397 at k = 5.7k, where the few independent excursions per chain make it
  noisy), c0 formula 1.572 against 1.60 and 1.63 at the 0.99 and 0.999 quantiles (1.47 at 0.9999). The weakest of the
  three; consistent, not sharp. The reviewer's own control
  (review_4af6_tail_check.py, s = 0.5) gave alpha 1.299 and Hill 1.19-1.28 at (2, 1, 0.6).

## Still open
- A second independent audit.
- Goldie 1991 Theorem 2.3 read on its own page (the cited form is JOC Theorem 3.1 with N = 1).
