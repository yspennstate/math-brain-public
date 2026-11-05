# Referee review of T228 (agent H, 3 Nov 2026)

Package: `results/frontier-2026-10/2026-10-23-t228-closure-30-agents/complete/` in this repository. The tex there
differs from the reviewed copy only in the repository links at lines 964-965, 1001, 1010, 1018, 1026, 1034 and 1043.
The manuscript reviewed is `campaign/manuscript/T228_Proof.tex` (1,047 lines, 13 pages in the pinned PDF).

## Declared conflict

Section 7 of the manuscript ("Strict positivity by forward excursions") is built on my own earlier work: `T3_SETUP.md` and `T3_STEP1-3.md` in my folder under `complete/a01/`, credited at tex lines 551, 893 and 1014-1043. I am not an independent reviewer of that section and I do not sign it off. In the package, A07 ("independent audit of T228 tail limit and strict positivity"), A10, A11 and A27 address it. Whether any of them used a method that could disagree with T3_STEP3 still has to be checked (see Next).

## What the row asks, and whether the theorem answers it

The row as repaired by the 16 Oct audit asks for one concrete nonlinear model with Gaussian inputs and persistent label noise, run as unmodified constant-step SGD. For that model it asks for: a stationary law, average contraction, asymptotic linearity, a nonarithmetic multiplier, a nonzero tail constant, the index given by the Lyapunov equation, and alpha < 2 on a nonempty range of (eta, b).

The model: sigma(z) = z + 10^-3 tanh z, one neuron, squared loss, batch b = 1, eta in [0.99, 1.01], teacher theta in [-1, 1], A and E independent standard normals, Y = sigma(A theta) + E.

| requirement | where | status in this review |
|---|---|---|
| concrete nonlinear model, Gaussian inputs, persistent noise, plain SGD | eq. (1)-(3) | met. The maps are nonaffine almost surely. The nonlinearity is a bounded perturbation of size 10^-3 (see remark 1). |
| average contraction | Thm 1.1(i), Lemma 2.1, Sec. 3 | Lemma 2.1 re-derived by hand. The bound E L < q is confirmed by quadrature (below). |
| stationary law (unique, W1-geometric) | Thm 1.1(ii), Sec. 4 | follows from E Lip < 1 by the standard contraction argument. Sec. 4 not yet read line by line. |
| asymptotic linearity | Lemma 2.1, eq. (2.3) | met. Psi(x) = (1 - eta A^2) x + R(x) with sup|R| <= B, and B has every moment. Re-derived by hand. |
| nonarithmetic multiplier | Thm 1.1(iii) | met. log|1 - eta A^2| has a density. |
| index from the Lyapunov equation, alpha < 2 on a range | Thm 1.1(iii) | confirmed by quadrature: alpha in (1.07, 1.11) on the whole eta range. |
| nonzero tail constant | Thm 1.1(iv), Sec. 6-7 | Sec. 6 (Goldie's implicit renewal) not yet read. Sec. 7 is mine; see the conflict above. |

## Independent numerical check

Script: `t228_quad_check.py`, output `t228_quad_check.json` (this folder). It uses adaptive quadrature in scipy 1.17.1. The package's exact checker is A08's rational interval arithmetic, so this check does not share its method.

- E L_theta = E|1 - eta A^2| + eta (4 delta + 3 delta^2) E A^2 + 2 delta eta E[A^2 |Y|]. The inner E|m + E| uses its closed form. Over the 5 x 5 grid eta in {0.99, ..., 1.01}, theta in {0, ..., 1}, the maximum is **0.98140**. That is below the stated q = 0.99010707. The bound in the manuscript is safe by about 0.009, which is about what the crude estimates in its Sec. 3 should cost. Theta < 0 is covered by symmetry, because sigma is odd.
- h_eta(1) = E|1 - eta A^2| ranges from 0.9619 to 0.9739. At eta = 1 this matches the hand value 2(P(|A|<1) - E[A^2; |A|<1]) = 0.9678.
- h_eta(2) = 1 - 2 eta + 3 eta^2, from 1.9603 to 2.0403. This matches the identity A08 checks.
- The root alpha(eta) of E|1 - eta A^2|^alpha = 1 is **1.1093, 1.1000, 1.0908, 1.0817, 1.0727** at eta = 0.99, 0.995, 1.00, 1.005, 1.01. It is inside (1, 2) and decreases in eta, which matches the direction in the source paper. Monotonicity is not part of the repaired requirement, and the manuscript does not claim it on this range.

A grid is not a proof of the supremum. The rigorous bound is A08's. This check only says the claimed number is right in magnitude and in direction.

## Referee remarks so far

1. **How nonlinear the model is.** With delta = 10^-3 the update is linear regression plus a bounded remainder. That is exactly the setting in which Goldie's 1991 implicit renewal theorem applies directly, and the 16 Oct audit's "solver_shape" anticipated this route. The package says so itself ("an application of existing tail theory", README). So it answers the repaired row as written. It does not answer the row's title question about neural-network losses, and it should be cited as a concrete example, not as a result about networks.
2. **Batch size.** The main theorem fixes b = 1. The requirement's "nonempty range of (eta, b)" is met by the eta interval at b = 1. The batch-two statement is a separate extension (`proofs/T228_BATCH_TWO.md`, reviews A22 and A29), not yet read here.
3. **Unbounded activation.** The row suggests a bounded activation as one option. The model's activation is unbounded, and only the perturbation is bounded. The manuscript says so in Sec. 1. This is acceptable, because the row's wording is "e.g.".
4. **The tail constant is not uniform.** C_{eta,theta} > 0 holds for each fixed (eta, theta), but no uniform lower bound is claimed (Remark 1.2). This is stated correctly.

## Part 2 (19:3x): Sec. 6, existence of the tail limit, checked

The external input is Jelenkovic and Olvera-Cravioto (2012), Theorem 3.1, with N = 1. In that case it is Goldie's 1991 implicit renewal theorem for a nonnegative R_0 independent of xi. I checked each hypothesis against the manuscript.
- E xi^alpha = 1 is the root equation. m_alpha = E[xi^alpha log xi] lies in (0, inf), because h is convex with h(0) = h(alpha) = 1, so h'(alpha) > 0, and Gaussian moments make it finite.
- log xi is nonarithmetic, because xi = |1 - eta A^2| > 0 almost surely and log xi has a density. The auxiliary moment holds with gamma = 0.
- E R_0^p < inf for p < alpha holds by Minkowski. From |Psi(x)| <= xi|x| + B we get ||X||_p <= ||B||_p / (1 - (E xi^p)^{1/p}), and E xi^p < 1 for p < alpha. The manuscript cites its Prop. 4.x for this, and this is the standard route.
- The discrepancy integral. U = |Psi(X)| has the law of R_0 by stationarity. W = xi|X| has the law of xi R_0 by independence. ||Psi(X)| - |MX|| <= |R(X)| <= B. So |P(U>t) - P(W>t)| <= E|1{U>t} - 1{W>t}|, which integrates to E|U^alpha - W^alpha| / alpha. The mean value theorem gives <= alpha B (W+B)^{alpha-1}, and subadditivity at exponent alpha - 1 in (0, 1) gives <= alpha [B^alpha + B xi^{alpha-1} |X|^{alpha-1}]. The last term factors as E[B xi^{alpha-1}] E|X|^{alpha-1}, by independence of X from the step. Both factors are finite. Every line holds.
- The constant formula follows as stated: C = E[|Psi(X)|^alpha - |MX|^alpha] / (alpha E[xi^alpha log xi]), via signed Fubini under the integrable bound.

I did not re-read the printed page of JO2012 for the exact wording of Theorem 3.1. The hypotheses as quoted agree with the theorem as I know it, and with Goldie's Theorem 2.3. Sec. 6 gives a limit in [0, inf). Everything about C > 0 rests on Sec. 7.

## Part 3 (19:3x): who checked positivity, and how

A07 (`campaign/reviews/A07.md`) audits the strict-positivity proof. It states that it used no earlier audit verdict and no Brain source as evidence, and that it reconstructed the argument itself. It also read JO2012 Theorem 3.1 on the printed page, from arXiv:1006.3295v5. That closes the one point part 2 left open.

A07 checks these steps line by line:
- the exponential tilt dQ/dP = xi^alpha and the stopped identity P(E, tau < inf) = E_Q[e^{-alpha S_tau} 1{E, tau < inf}]. It notes that no optional stopping is needed.
- Q(S_j > 0 for all j >= 1) > 0.
- a uniform overshoot-tightness bound from a translated occupation estimate, with r_theta = h_eta(alpha - theta) < 1.

Two limits on how independent this is:
1. A07 reviews the same route the authors took: tilt, ladder and overshoot. It does not give a second proof by a different method. It could have found an error in that route. It could not have found that the route itself was the wrong tool. By referee standards this is normal and sufficient.
2. A07 audited Version 1 of `proofs/T228_EXPLICIT_CLOSURE.md`, not the final manuscript's Sec. 7. The final text is covered by A27 ("independent mathematical review of the final T228 manuscript"). Whether Sec. 7 of the PDF matches what A07 passed is the next check: diff the argument, not the bytes.

A07 also asked for one precision edit: state the stopping identity on {tau < inf} explicitly. Whether the final manuscript made that edit is part of the same check.

## Part 4 (19:4x): does the final Sec. 7 match what was audited?

Two reviewers cover Sec. 7, and the gap between them closes.
- A07 audited Version 1 of `T228_EXPLICIT_CLOSURE.md`, then added a follow-up on Version 2 (A07.md line 329). Version 2 makes both of A07's precision edits: the auxiliary moment E xi^gamma < inf with gamma = 0, and the stopping identity on the finite-crossing event, without assuming P-almost-sure finiteness. The package's current `T228_EXPLICIT_CLOSURE.md` is Version 2.
- A27 reviewed the final manuscript itself. Its pinned tex hash matches the reviewed copy, so A27 read exactly the text reviewed here. A27 says it reconstructed the probability arguments before reading T3_STEP3, read no other verdict, and checked JO2012 Theorem 3.1 on printed p. 5. Its verdict is ACCEPT with no required fixes.
- The {tau < inf} edit is in the final text. Eq. (stopped-change), tex lines 579-584, states P(F, tau < inf) = E_Q[e^{-alpha S_tau} 1_{F cap {tau < inf}}] and says no uniform-integrability claim is made. The good event F_u (eq. stopped-event) carries tau_u < inf inside it, which is the optional notational edit A07 still listed after Version 2.

I also read Sec. 7 against the eight steps of A27 Sec. 5 and A07's step list. They agree step for step: the radial lower bound, the tilt and stopped identity, the survival bound p_0 = Q(Z > 1)(1 - e^{-beta}), the translated occupation bound K_U = e^beta / (1 - r), the discounted remainder with the joint moment E_P[xi^{alpha-beta} B^beta], the choice of z and K before t, the unnormalized last-exit inequality, and the compact minorization into the annulus. I checked the arithmetic of each step while reading. Because the mechanism is mine (T3_STEP3), that reading does not count as independent, and I record it only as a consistency check.

Two small points for the authors. Neither is a gap.
- The bound |X_j| >= (3K/2) e^{S_j} for j <= tau_u uses V_j <= V_{tau_u} <= K/2. That holds because B_theta >= 0 makes V_n nondecreasing. The text leaves it implicit.
- In the translated occupation bound, a later visit to I needs a fresh displacement in (-1, 1). The proof bounds it by the one-sided event {S' <= 1}. That is a valid upper bound, but it is looser than the sentence suggests.

Sec. 4-5 (invariance, minorization and full support): I did not read these line by line. A27 Sec. 3 reconstructs them, covering the conditional Gaussian minorization given A in [1, 2] at a nonzero teacher, uniqueness over all laws, and the non-circular subcritical moments. A07 passes the corresponding Sections 4-5 of the closure document. Two reviewers cover these sections, and I add nothing to that.

## Verdict on T228 (agent H, 3 Nov 2026 19:4x)

**Accept as a proof of the stated concrete example, with a declared conflict on Sec. 7.**

What rests on what:
- Items (i)-(iii) rest on my independent checks: contraction (max E L = 0.9814 < q by quadrature), the asymptotic linear form, the nonarithmetic multiplier, and alpha in (1.07, 1.11), which is inside (1, 2).
- The existence of the tail limit (Sec. 6) rests on my line-by-line check against Goldie and JO2012.
- Positivity (Sec. 7) rests on A07 (Versions 1-2) and A27 (the final tex, hash-matched). Both say they reconstructed the argument independently. Both follow the same route, which is the credited route.

Scope, stated once: one scalar neuron, a 10^-3 bounded perturbation of linear regression, batch 1, eta in [0.99, 1.01], |theta| <= 1. No uniform lower bound on C is claimed. The row is closed in its repaired form. The result is not a theorem about neural-network losses.

The one thing that would overturn this verdict is an error in the tilt-and-overshoot route itself. Every reviewer checked within that route, and none gave a second proof by another method. A different lower-bound argument, for example a direct Kesten-type comparison through the Lipschitz envelope, would remove that dependence. It is not required for acceptance.
