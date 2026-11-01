# T228 Heavy-tailed stationary law of constant-step SGD for a nonlinear model

Lead: unassigned. Dossier written 2026-10-16 02:3x by claude-99aebc7f from the auditor's record (codex-w687, 02:21) and
a reading of 2006.04740 (Theorem 1, Proposition 5, Appendix C.6.4) and 2006.06293 (Theorem 1). Whoever takes the row
owns the dossier from then on.

## STATEMENT
Repaired statement (the list row named no model, loss, data law or noise; auditor codex-w687, 16 Oct, statement_ok NO).
Scalar single-neuron regression. Data a ~ N(0,1), label y = sigma(a x*) + eps with eps ~ N(0, s^2), s > 0, independent
of a. Loss f(x; a, y) = (sigma(a x) - y)^2 / 2. Constant-step minibatch SGD with batch b and step eta:
    x_{k+1} = Psi_k(x_k) = x_k - (eta/b) sum_{i<=b} sigma'(a_i x_k) (sigma(a_i x_k) - y_i) a_i,   fresh (a_i, y_i) each step.
Two activation classes:
  (A) asymptotically linear: sigma(z) = z + phi(z), phi in C^2, sup|phi'| < 1, and phi, z phi'(z), z phi''(z) bounded
      (example phi = c tanh, |c| < 1);
  (B) leaky ReLU: sigma(z) = max(z, beta z), 0 <= beta < 1.
Prove: (1) the chain has a unique stationary law pi; (2) t^alpha P_pi(|x| > t) -> c0 with c0 > 0 (for (B): a constant
for each sign); (3) alpha is the positive root of an explicit moment equation in (eta, b); (4) alpha < 2 on a nonempty
set of (eta, b).

## FRONTIER
- Gurbuzbalaban-Simsekli-Zhu arXiv:2006.04740 (ICML 2021): linear regression (quadratic loss, Gaussian data): exact
  index from E|det-type moment| = 1 via Kesten-Goldie / Alsmeyer-Mentemeier; 0 < alpha < 2 on a stable step interval
  (Proposition 5); monotone in eta/b under Gaussian data (A3) and alpha >= 1 (Theorem 4). Their Theorem 1 restates
  Mirek (2011) for asymptotically linear random maps: if a stationary solution exists, |Psi(x) - M x| <= B,
  log|M| non-arithmetic, E|M|^alpha = 1, E B^alpha < oo, E|M|^alpha log+|M| < oo, then t^alpha P(|x| > t) -> c0 > 0.
- Hodgkinson-Mahoney arXiv:2006.06293: Lipschitz random maps with k|w - w*| - M <= |Psi(w) - Psi(w*)| <= K|w - w*|,
  E log K < 0, P(k > 1) > 0: geometric ergodicity, two-sided power-law bounds, E k^alpha = 1, E K^beta = 1,
  limsup t^(alpha+eps) P > 0 and limsup t^(beta-eps) P < oo for every eps > 0. Bounds only; not the exact index, not c0 > 0.
- Jiao-Keller-Ressel arXiv:2402.01382: homogenized SGD (a diffusion), explicit upper and lower bounds on the index.
- Raj-Zhu-Gurbuzbalaban-Simsekli arXiv:2310.18455: offline SGD has approximate power-law tails (quadratic losses).
- arXiv search 16 Oct 02:2x (five queries, newest first): nothing on an exact index for a nonlinear model.

## ARCHITECTURE
Write Psi(x) = M x + R(x). Class (A): the gradient is a^2 x + a (a x) phi'(a x) + a (1 + phi'(a x)) (phi(a x) - y), so
M = 1 - (eta/b) sum a_i^2 (the linear-regression multiplier) and |R(x)| <= B = (eta/b) sum |a_i| (C1 + C2 |y_i|).
Then: (i) existence and uniqueness of pi by a Foster drift V = |x|^p (small p, E|M|^p < 1) plus a minorization (the
label noise gives Psi_k(x) a Gaussian component of variance >= (eta/b)^2 s^2 (1 - sup|phi'|)^2 sum a_i^2 > 0, so
compact sets are small) -> positive Harris recurrence; (ii) Mirek's theorem for the limit; (iii) a separate argument
for c0 > 0; (iv) the moment equation E|1 - (eta/b) chi2_b|^alpha = 1, which is the linear one: the nonlinearity does
not move the index. Class (B): Psi(x) = M_{sgn x} x + Q_{sgn x} with M_+ = 1 - (eta/b) sum w(a_i)^2 a_i^2,
w(a) = 1{a > 0} + beta 1{a < 0}, M_- the same with -a_i: an affine recursion whose coefficients switch with the sign of
the state, i.e. a Markov-modulated Kesten recursion (Kesten 1974, renewal theory for functionals of a Markov chain).

## FAILURE POINT
Two places. (1) c0 > 0 is not delivered by any theorem in hand. GSZ's restatement of Mirek asserts c0 > 0 under
(i)-(iii) alone, and that is false as written: Psi(x) = M sgn(x) (|x| - K)^+ satisfies (i) with B = |M| K, (ii) and
(iii) for suitable M, and delta_0 is its unique stationary law, so c0 = 0. Whatever nondegeneracy Mirek actually assumes
(read Mirek, PTRF 2011, Theorems 1.8 and 1.15, which GSZ's Appendix C.6.4 cites) has to be verified for the GLM.
Hodgkinson-Mahoney give only limsup t^(alpha+eps) P > 0. (2) For class (B) the map is not asymptotically linear in
Mirek's sense (the multiplier depends on sgn x), so Theorem 1 does not apply at all; Hodgkinson-Mahoney give bounds
with k = min(|M_+|, |M_-|) and K = max, which differ.

## SHAPE
DAYS for class (A): every step is a known tool; the work is checking hypotheses, plus a positivity lemma (the Gaussian
label noise gives the stationary law a density everywhere and unbounded support, which is the natural input).
Days to weeks for class (B): the index guess is explicit. By the symmetry a -> -a, M_+ and M_- have the same law, so
the 2x2 matrix Lambda(s)_{sigma,tau} = E[|M_sigma|^s 1{sgn(M_sigma) sigma = tau}] has both row sums E|M_+|^s and
spectral radius E|M_+|^s: conjecturally alpha solves E|1 - (eta/b) sum w(a_i)^2 a_i^2|^alpha = 1. The work is
verifying Kesten's Markov-renewal hypotheses (the sign chain is a two-state chain driven by the same Omega as the
increments, so the modulation is not independent of the jumps).

## OBSTRUCTION
What makes the general problem hard is the growth of Psi, not the tail theory. Bounded activations (tanh, sigmoid)
give a gradient bounded by C |a| (1 + |y|) uniformly in x: with weight decay the recursion is a deterministic
contraction plus light-tailed noise (light tails); without it there is no contraction (M = 1). Two-layer networks give
cubic growth of Psi in the parameters; with Gaussian inputs and a constant step the chain then plausibly escapes to
infinity almost surely (from size R a step multiplies by about eta a^2 R^2, and the chance of not doing so is
summable along a geometric escape) - an argument sketch, not written up - so no stationary law exists to have a tail.
So Kesten-type heavy tails need activations of linear growth (class A, leaky ReLU) or bounded inputs. Moves: an exact
index with c0 > 0 for one honest nonlinear model; the sign-modulated index for leaky ReLU; d dimensions.

## SETTLED
- Linear regression: exact index, alpha < 2 range, monotonicity under (A3) and alpha >= 1 (GSZ 2006.04740).
- General Lipschitz maps: two-sided bounds only (Hodgkinson-Mahoney 2006.06293, Theorem 1).
- GSZ Theorem 1 as restated (c0 > 0 from (i)-(iii) plus existence) is false without a nondegeneracy hypothesis; the
  counterexample is in FAILURE POINT. Read Mirek's own statement before citing it.
- Scalar b = 1, unit-variance Gaussian a, class (A): alpha < 2 iff E(1 - eta a^2)^2 > 1 iff eta > 2/3, and
  E log|1 - eta a^2| < 0 on the whole of [0.3, 2.0] (numerical quadrature, 16 Oct: -0.49 at 0.6, -0.42 at 1.0,
  -0.12 at 2.0). For batch b the threshold is eta > 2b/(b + 2); E log|M| < 0 at eta = 2 for b = 1, 2, 4, 8. So (4) holds
  on a nonempty interval once (1)-(3) are proved.
- NOT moves: another linear model; numerical tail-index estimates for networks; heavy-tailed additive noise (that is
  the input's tail, not the multiplicative mechanism).

## TARGETS
1. Class (A), scalar: prove (1)-(4) in full, with c0 > 0. Expected index: the linear one, E|1 - (eta/b) chi2_b|^alpha = 1.
   Days. DONE under the stability condition (S) E log|1 - (eta/b) chi2_b| < 0: w688-T228-A/L v1, accepted by claude-b1e26540
   16 Oct 06:44 (brain_workers/w688/T228/AUDITS_FROM_REVIEWER.tsv). (S) is necessary: at b = 2, eta = 100 the index equation
   has no root.
2. Class (B), leaky ReLU, scalar: the stationary tail under the sign-modulated recursion, index from E|M_+|^alpha = 1 by
   the symmetry above; constants c0+ and c0- for the two signs. The first activation used in practice with an exact
   index.
3. Class (A) in R^d with a ~ N(0, I_d): M = I - (eta/b) sum a_i a_i^T, |R| bounded as in d = 1; Mirek's d-dimensional
   theorem or Alsmeyer-Mentemeier with the asymptotically linear perturbation. Index equals GSZ's linear one.
   DONE 22 Oct under (S_d) E log xi < 0: claude_b1e26540/T3_CLAIM.md v2, reviewed by claude-4af6ff1a and claude-fc67971c.
NOT targets: two-layer networks with Gaussian inputs at constant step (see OBSTRUCTION: likely transient).

## 2026-10-21 19:3x claude-4af6ff1a: TARGET 2 submitted (v1, not yet reviewed)
claude_4af6ff1a/T228_B_v1.md: leaky ReLU, any beta in [0,1), (S') E log|A+|<0. The map is piecewise affine and A- has the law of A+, so the multiplier the chain uses is independent of the state (the SHAPE paragraph above calls the modulation dependent; it is harmless). ABB Thm 2.1 Case 1, matrix [[d,o],[o,d]], index E|1-c sum w(a_i)^2 a_i^2|^k = 1, C+ = C- > 0 by (16) and Prop 8.1. Open review point: Psi jumps at x=0 (Q+ != Q-), so ABB (1) fails at one point; ABB uses it only for Feller existence (replaced by Harris). gamma=sigma'(0)=0 with beta=0 adds delta_0 as a second invariant law. kappa<2 on an interval for every b, beta. Numbers: leaky_index_run1.txt.
21:5x: second self-check of review point 1 (claude_4af6ff1a/REVIEW_POINT1_CHECK.md): every use of continuity in ABB is (1)/Feller, an example, rho or the renewal function; section 8 uses only (4) via Lemma 3.1. Outside review still owed (the assigned reviewer has left the mesh).

## 2026-10-21 23:2x claude-4af6ff1a: TARGET 2 DONE under (S') (reviewed)
claude-b1e26540 reviewed T228_B_v1 PASS with three wording fixes (claude_4af6ff1a/REVIEW.tsv); version 2 (claude_4af6ff1a/T228_B_v2.md) carries them. Class (B) scalar leaky ReLU, any beta in [0,1): exact index from E|1-c sum w(a_i)^2 a_i^2|^k = 1, C+ = C- > 0, under (S') E log|A+| < 0. Left on the row: target 3 (class A in R^d) and a rerun of the 16 Oct novelty search before any paper.

## 2026-10-22 02:4x claude-b1e26540: TARGET 3 setup (no claim yet)
claude_b1e26540/T3_SETUP.md. Mirek's Theorem 1.8 does not reach d >= 2 here: its (H1) requires M in R_+ x K, K in O(d) (similarities), and I - c sum a a^T is not one. Route: for Gaussian a the norm |M_k u_k| is iid and independent of the past whatever the direction (checked by Monte Carlo, t3_numcheck_run1.txt), so Goldie's scalar implicit renewal theorem applies to |x| directly. Index from E[((1-cX)^2 + c^2 X Y)^(alpha/2)] = 1, X ~ chi2_b, Y ~ chi2_(d-1); alpha < 2 iff eta > 2b/(b+d+1). Left: k-step minorization (noise has rank b), c0 > 0, novelty search.

## 2026-10-22 03:4x claude-b1e26540: TARGET 3 step 1 drafted (not yet reviewed)
claude_b1e26540/T3_STEP1.md: under class (A), s>0 and (S_d) E log xi < 0, unique invariant pi in R^d, E_pi|x|^p < oo for p < alpha, geometric V-ergodicity, positive density on every ball. The label-noise rank is no obstacle: one sample's Gaussian direction a_1 with its radius spread by eps_1 gives a one-step minorization by Lebesgue on each ball (polar coordinates), so the k-step plan in T3_SETUP is dropped. Data point: (d,b,eta)=(5,4,1.0) has gamma=+0.008, so (S_d) bites inside the alpha<2 range. Next: step 2 (Goldie 1991 Thm 2.3 on |x|, hypotheses read on the page), then step 3 (c0>0).

## 2026-10-22 04:5x claude-b1e26540: TARGET 3 claimed in draft (NEEDS_REVIEW)
claude_b1e26540/T3_CLAIM.md collects steps 1-3: under class (A), s>0 and (S_d) E log xi < 0 in R^d, unique pi, t^alpha P_pi(|x|>t) -> c0 in (0,oo) with c0 = E[|Psi x|^alpha - |Mx|^alpha]/(alpha E xi^alpha log xi), alpha the root of E[((1-cX)^2+c^2XY)^(alpha/2)] = 1, alpha<2 just above eta0 = 2b/(b+d+1). Step 3 (c0>0, bf4cf3c7) runs forward (radial bound, tilted walk, last-exit) and cites nothing; step 1 citation (Hairer-Mattingly Thm 1.2) read on the page (03a570e8). Open: independent review, novelty rerun for the d-dimensional statement, a simulated tail check.

## 2026-10-22 05:2x claude-b1e26540: TARGET 3 reviewed once (REVIEWED_ONCE)
claude-4af6ff1a's independent review (claude_b1e26540/REVIEW.tsv): 16 PASS, 0 FIX, 0 FAIL; its one OPEN row, novelty for the d-dimensional statement, is answered in claude_b1e26540/T3_NOVELTY.md (web search: linear-regression and scalar results only). T3_CLAIM.md v2, mathematics unchanged. Numerical control t3_tail_check.py: at (d,b,eta)=(2,1,0.6) alpha 1.3015 from h, Hill 1.296-1.308, c0 formula 2.247 against empirical 2.23; at (2,1,0.8) alpha 0.4023, Hill 0.399-0.410, c0 1.401 against 1.42-1.445. A second independent audit is wanted before VERIFIED.

## 2026-10-22 05:4x claude-4af6ff1a: TARGET 2 novelty rerun
claude_4af6ff1a/T2_NOVELTY.md: ten arXiv wordings (the 16 Oct five plus leaky ReLU, power-law stationary, single-index heavy-tailed, stochastic recurrence, Gaussian approximation). Nothing states an exact two-sided stationary tail with C+ = C- > 0 for SGD under a nonlinear activation; nonlinear-SGD hits (Armacki et al.) are about heavy-tailed noise and rates. Title/abstract level only; before a paper, read the forward citations of 2006.04740 and 2006.06293. lit.json history appended.
05:5x: forward citations of 2006.04740 and 2006.06293 screened (199 papers, Semantic Scholar): none proves a nonlinear stationary index; 2204.12554 measures the ReLU-gate index empirically and finds it unlike the linear one (related work, the motivation to cite). Verdict open, no prior statement found.

## 2026-10-22 07:2x claude-b1e26540: TARGET 3 VERIFIED (two independent reviews)
claude_b1e26540/T3_CLAIM.md v2: class (A) single-index SGD in R^d under (S_d) E log xi < 0 has a unique invariant law
with t^alpha P(|x| > t) -> c0 in (0, oo), alpha the positive root of E[((1 - cX)^2 + c^2 X Y)^(alpha/2)] = 1, explicit c0,
and alpha < 2 on a nonempty eta-interval for every (d, b). Reviews: claude-4af6ff1a (02:09Z, 16 PASS) and claude-fc67971c
(04:06Z, all PASS, commit 06966f6ae36). Novelty: T3_NOVELTY.md (no prior statement found). With targets 1 and 2 done, the
row's three targets are proved and reviewed; posting a paper is his call.
