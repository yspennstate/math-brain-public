Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime interface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen source metric: `T_corr=0 -> 0`. Methods tried: B2, B24, B30. New rigorous partial result: for the admitted `alpha=1`, `theta=vartheta_{1/4}` family, every radial moment of order `p<1` is finite with an explicit bound, hence the radial tail exponent has certified lower endpoint at least `1`; the matching lower-tail bound remains open.**

# HARD7-02 — Question 1.9: reciprocal-edge order parameter and all subcritical moments

Status: **PARTIAL / Campbell–O'Rourke Question 1.9 remains OPEN by bounded current-status search.**

Frozen metric: `T_corr=0 -> 0` (**no movement**). This is the first ordinary research run on Question 1.9 after the mandatory Question 1.8 handoff, so the Q1.9 unchanged streak is `1`; Section I is not triggered.

## 1. Continuity, repository read, ownership, and runtime honesty

I resumed the admitted successor claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

rather than restarting the released Question 1.8 problem. At run start I re-read the controlling HARD7 policy, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the newest HARD7-02 handoff/admission report, the active Q1.9 claim, the non-Hermitian/heavy-tail claim neighborhood, and the latest relevant neighboring C0032 terminal handoff. Repository searches continue to separate Q1.9 from C0031/C0032, the released Q1.8 target, Bernoulli singularity work, and the owner's excluded least-singular-value / Gaussian-row-submatrix / Toeplitz-Hankel / additive-spike / gated-product manuscripts. No ownership collision was found and no claim file was modified.

The scheduler capability statement is unchanged. The available automation surface exposes title, prompt, schedule/timing, enabled state, but no binding model selector, reasoning-effort selector, or guaranteed execution-duration field. Therefore GPT-6 maximum cannot be enforced or authenticated here. Changing that requires a product/backend surface that exposes binding model/effort controls, or an authorized account/workspace context that already has them. Historical native modification probes for P26/P01/P03 returned `You cannot modify this task`; current repository evidence records that P26 later became editable in a different authorized context. The compliant workaround for a task that still refuses modification is the owning/authorized account or workspace context, or platform support/ownership transfer — never a duplicate schedule and never a permission bypass. No scheduler mutation was attempted in this run.

No email, Drive, public posting, paid compute, workflow execution, neighboring-track edit, shared-root ledger edit, force push, or permission bypass was performed.

## 2. Source statement and current-status refresh

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The source's endpoint contrast is important: in the iid/axis-supported case the limiting non-Hermitian law is much lighter-tailed (the underlying Bordenave–Caputo–Chafaï theorem describes stretched-exponential decay and all finite moments), whereas in the Hermitian case the limiting spectral law inherits the heavy input tail. These are literature baselines, not HARD7-02 discoveries.

A fresh bounded 19 September 2026 check used the exact source title/authors and the terms `Question 1.9`, `tail behavior`, `theta_d`, `mu_{alpha,theta_d}`, `heavy-tailed elliptic`, `PWIT`, and 2023–2026 follow-up terms. It recovered the 2022 source, Bordenave–Caputo–Chafaï's iid heavy-tailed paper, Campbell–O'Rourke's 2023/2024 Lévy–Khintchine random-Laplacian paper, and unrelated finite-variance elliptic-law work, but no located paper claiming a general solution of Q1.9 or a tail classification for the frozen interior family below. This is bounded negative evidence only, not a worldwide novelty certificate.

The source itself already proves in Lemma 6.1 the existence of **some** positive moment sufficient for tightness. The theorem below is stronger only in the frozen deterministic limiting-law slice: it reaches **every** `p<1`. I do not claim that this strengthening is absent from all prior literature without a broader novelty audit.

## 3. Frozen target and exact source-valid representative

The canonical Q1.9 claim freezes `alpha=1` and

`eta_x = Law(sqrt(x)e^{i phi}, sqrt(1-x)e^{-i phi})`,

`vartheta_x = (eta_x + tau#eta_x)/2`,

with `x=1/4`, where `tau(w_1,w_2)=(w_2,w_1)`.

The metric is

`T_corr = number of explicit non-iid, non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class is rigorously determined`.

Before: `T_corr=0`.

After: **`T_corr=0`**.

To prove source-level statements about `mu_{1,vartheta_{1/4}}`, exploit Theorem 1.6's fact that the deterministic limit depends only on `(alpha,theta_d)` and choose a convenient representative of that domain-of-attraction class.

Let

- `R` have the exact Pareto-1 tail `P(R>r)=r^{-1}` for `r>=1`;
- `phi` be uniform on `[0,2pi)`;
- independently choose one of
  `(1/2 e^{i phi}, sqrt(3)/2 e^{-i phi})`
  and its coordinate swap, each with probability `1/2`;
- denote that unit vector by `W~vartheta_{1/4}` and set `(xi_1,xi_2)=R W`;
- take the diagonal atom `zeta=0` and `a_n=n`.

Then for every continuity set `D` of `vartheta_{1/4}` and every `r>0`, for all sufficiently large `n`,

`n P(W in D, R>=rn)=vartheta_{1/4}(D) r^{-1}`.

Thus C1 holds exactly with `alpha=1`, `theta_d=vartheta_{1/4}`. C2(ii) holds with `a_n/n=1`. C2(i) also holds: if a complex linear form `a z+b w` vanished on the first support curve for every `phi`, then

`a e^{2i phi}+b sqrt(3)=0`

for every `phi`, forcing `a=b=0`. Hence this representative is source-valid and has the desired limiting ESD.

## 4. B2 — attack the smooth-interpolation negation first

For one marked reciprocal edge define

`B(r,w)=[[0,r w_1],[r w_2,0]]`.

Its exact characteristic equation is

`lambda^2=r^2 w_1w_2`,

so both eigenvalues have modulus

`r |w_1w_2|^{1/2}`.

For `vartheta_x`,

`|w_1w_2|=sqrt(x(1-x))`

on the entire support. Therefore the local two-cycle mechanism retains the input Pareto exponent for every off-axis `x>0`, however small, while it vanishes identically on the axis-supported iid endpoint where `w_1w_2=0`.

At the frozen point `x=1/4`,

`|w_1w_2|=sqrt(3)/4`,

and the reciprocal-edge eigenvalue scale is

`kappa=(3/16)^{1/4}=3^{1/4}/2 = 0.6580370064...`.

**Outcome of B2:** the naive idea that the tail class must interpolate smoothly from the iid endpoint fails already as a local mechanism: an arbitrarily small amount of off-axis angular mass creates a power-law reciprocal-edge channel. This is *not* a counterexample to the source question and not a proof of the infinite-volume ESD tail. The exact missing step is stability of a positive density of such large reciprocal edges under coupling to the rest of a nonnormal matrix.

## 5. B24 — extremal angular product gives an exact Poisson tail-order parameter

Define for any angular measure `theta`

`K_alpha(theta) := int |w_1w_2|^{alpha/2} theta(dw)`.

This quantity has an exact interpretation on the source PWIT. The radial marks have intensity

`alpha r^{-1-alpha} dr theta(dw)`.

For one mark, the associated reciprocal `2 x 2` block has radius `r|w_1w_2|^{1/2}`. Therefore the number of root-incident marks whose reciprocal-block radius exceeds `R` is Poisson with mean

`int theta(dw) int_{R/|w_1w_2|^{1/2}}^infinity alpha r^{-1-alpha} dr`

`= R^{-alpha} K_alpha(theta)`.

This is exact, with the integrand interpreted as zero when `w_1w_2=0`.

For the frozen family,

`K_1(vartheta_{1/4})=(3/16)^{1/4}=3^{1/4}/2>0`.

For the iid axis measure, `K_alpha=0`. At the Hermitian endpoint `x=1/2`, `K_1=1/sqrt(2)`.

Thus `K_alpha` is an exact local order parameter which separates the axis endpoint from every member of the off-axis family. It suggests the concrete conjectural large-radius law

`mu_{1,vartheta_{1/4}}(|z|>R) asymp R^{-1}`,

but the present run does **not** promote that conjecture to a theorem. A Poisson count of local marks is not an eigenvalue count for the full nonnormal operator.

**Outcome of B24:** succeeded in reducing the lower-tail problem to a quantitatively sharp mechanism. The coefficient is exact; the global nonnormal stability step is the obstruction.

## 6. B30 — all subcritical moments of the limiting planar law

The complementary direction *can* be proved fully.

### Theorem 6.1 — explicit `p<1` moment bound for the frozen correlated family

Let

`mu := mu_{1,vartheta_{1/4}}`.

Put

`m := (1+sqrt(3))/4`

and

`C_* := 1+3 sqrt(2)m = 1+(3/4)(sqrt(2)+sqrt(6))`.

Then for every `0<p<1`,

`int_C |z|^p mu(dz) <= B_p := 1 + p C_*/(1-p)`.

Consequently, for every `R>0`,

`mu({|z|>R}) <= B_p R^{-p}`,

and therefore

`liminf_{R->infinity} [-log mu({|z|>R})]/log R >= 1`.

#### Proof

Use the Pareto representative from Section 3. The two coordinate marginals are identical by swap symmetry. Let

`Z=|xi_1|^2`.

Since `|W_1|` equals `1/2` or `sqrt(3)/2` with equal probabilities and `P(R>r)=r^{-1}`, for every `y>=1`,

`P(Z>y)`
`= (1/2)(1/2)y^{-1/2} + (1/2)(sqrt(3)/2)y^{-1/2}`
`= m y^{-1/2}`.                                                    (6.1)

Fix a row of `A_n=X_n/n`. Its `n-1` off-diagonal entries are independent and all have this common marginal; the diagonal is zero. Add one independent extra copy if necessary and dominate the squared row norm by

`S_n := n^{-2} sum_{j=1}^n Z_j`.

For `n>=2` and `t>=1`, split according to whether one summand exceeds `t/2`:

`P(S_n>t)`
`<= P(max_j Z_j/n^2>t/2)`
`   + P(sum_j (Z_j/n^2) 1_{Z_j/n^2<=t/2}>t/2)`.                    (6.2)

For the first term, (6.1) gives

`P(max_j Z_j/n^2>t/2) <= sqrt(2)m t^{-1/2}`.                       (6.3)

For `T>=1`,

`E[Z 1_{Z<=T}] <= int_0^T P(Z>s) ds`
`<= 1+2m sqrt(T)`.                                                  (6.4)

Taking `T=n^2t/2` and using Markov's inequality, the second term in (6.2) is at most

`2/(nt) [1+2m n sqrt(t/2)]`
`<= t^{-1}+2sqrt(2)m t^{-1/2}`                                    (6.5)

because `n>=2` and `t>=1`. Combining (6.3)--(6.5),

`P(S_n>t) <= C_* t^{-1/2}`,  `t>=1`,                              (6.6)

uniformly in `n`.

Let `q=p/2<1/2`. Tail integration gives

`E S_n^q`
`= q int_0^infinity t^{q-1} P(S_n>t) dt`
`<= 1 + q C_* int_1^infinity t^{q-3/2} dt`
`= 1 + p C_*/(1-p) = B_p`.                                        (6.7)

Now use exactly the finite-matrix inequalities quoted by Campbell--O'Rourke as Lemmas A.7 and A.8: for every `0<p<=2`, Weyl majorization and the Schatten row bound imply

`sum_k |lambda_k(A_n)|^p <= sum_k s_k(A_n)^p <= sum_i ||Row_i(A_n)||_2^p`.

Divide by `n`, take expectations, and apply (6.7):

`E int |z|^p mu_{A_n}(dz) <= B_p`.                                 (6.8)

By Theorem 1.6, `mu_{A_n}` converges weakly in probability to the deterministic `mu`. For `M>0`, the function

`f_M(z)=min(|z|^p,M)`

is bounded and continuous. Hence `int f_M dmu_{A_n}` converges in probability to the constant `int f_M dmu`; boundedness by `M` implies convergence of expectations. From (6.8),

`int f_M dmu <= B_p`.

Letting `M->infinity` and using monotone convergence proves the moment bound. Markov's inequality yields the tail bound. Finally, for each fixed `p<1`,

`-log mu(|z|>R) >= p log R - log B_p`;

dividing by `log R`, taking `liminf`, and then `p upward 1` gives the claimed lower endpoint `>=1`. `QED`

### What this theorem does and does not say

It is a theorem-sized source-relevant partial result with the complete argument on the page. It strengthens the source's unspecified positive-moment tightness statement for this exact deterministic limiting slice to every `p<1`. It does **not** show that the tail is polynomial, because a stretched-exponential tail also has every `p<1` moment. Thus it does not increment `T_corr`.

The exact finite constants were self-checked in

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T15-09-49Z__q19-tail-constant-check.py`

at commit `88daca4e49355e7c70cf8c0c31d82e1b0d9d0552`, with archived output

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T15-09-49Z__q19-tail-constant-check.out`

at commit `8d69c10c17e3b5cd7f9e99fd0c0e31bc29ddffd1`, ending

`ALL_EXACT_CHECKS_PASS = True`.

The mathematical route was checkpointed before code at commit

`667774f3c0a3ec591420a1d60fbc2e6c927cf7d8`.

As one concrete exact specialization, for `p=3/4`,

`B_{3/4}=4+(9/4)(sqrt(2)+sqrt(6)) = 12.6933324366...`.

## 7. What actually blocks `T_corr=1`

The proven direction is now

`liminf tail-exponent >= 1`.

To determine the full tail exponent as `1`, it remains to prove a matching lower bound of the form

`mu_{1,vartheta_{1/4}}(|z|>R) >= c R^{-1+o(1)}`

(or any equivalent statement forcing `limsup` exponent `<=1`).

B2/B24 identify the most concrete candidate mechanism: the large-edge graph at radial scale `R` has reciprocal edges with exact intensity proportional to `K_1(vartheta_{1/4}) R^{-1}`. On a tree component, reciprocal weights can be balanced by diagonal similarity, so an isolated two-cycle carries eigenvalues of size `kappa R`. What is missing is a source-valid argument that a positive density of those large local modes survive the coupling to all smaller edges. Nonnormal eigenvalues are not Lipschitz under arbitrary additive perturbations, so ordinary Weyl/Hoffman--Wielandt arguments cannot simply transfer the local count.

This is a substantially narrower obstruction than at admission: the upper-decay half is complete to the natural input exponent, and the lower-decay half has an exact angular coefficient and scale.

Next run must use a different triple. The most promising planned moves are **B1 / B6 / B20**: change category from eigenvalue perturbation to logarithmic-potential/Schur-complement zeros; deform from the Hermitian endpoint where the lower tail is known; and identify exactly why the large-edge exploration algorithm fails to protect zeros of the determinant.

## 8. Metric / lifecycle / ledger delta

`T_corr` before: `0`.

`T_corr` after: **`0` (no movement)**.

Status: **PARTIAL / OPEN**.

Q1.9 ordinary unchanged count: `1`.

No closure, REFUTED, PROVED, KNOWN, audit-complete, or publication claim is made. No independent audits are requested yet because the source target is not closed.

```text
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.9
  canonical_claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md
  status: PARTIAL_OPEN
  metric: T_corr
  before: 0
  after: 0
  movement: no
  new_partial_theorem: for alpha=1, theta=vartheta_{1/4}, all p<1 radial moments finite with explicit B_p; liminf tail exponent >=1
  exact_local_order_parameter: K_1(vartheta_{1/4})=(3/16)^(1/4)
  shared_root_write: false
```
