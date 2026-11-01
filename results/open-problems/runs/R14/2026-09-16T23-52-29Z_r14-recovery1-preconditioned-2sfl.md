Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector and no reasoning-effort selector; I do not claim otherwise. **NO METRIC MOVEMENT: `6.48139658710 -> 6.48139658710`; unchanged count `3 -> 4`; STUCK-RECOVERY-1 EXECUTION. Section-B moves actually tried: #7 TAKE THE LIMIT, #15 BREAK THE SYMMETRY ON PURPOSE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: Elizabeth Gardner (1988), *The space of interactions in neural network models*, J. Phys. A 21, 257--270, DOI `10.1088/0305-4470/21/1/030`; modern source navigation through Stojnic arXiv:1306.3980, El Alaoui--Sellke arXiv:2010.15811, Montanari--Zhong--Zhou arXiv:2110.15824 / PTRF 188 (2024), and Stojnic arXiv:2312.16531. Frozen target: rigorous high-probability SAT/UNSAT threshold bracket at `kappa=-1` in the iid standard-Gaussian spherical model.

Status: **PARTIAL / source problem OPEN / RECOVERY-1 DID NOT YET MOVE THE BRACKET.** The important change is methodological: the complete `r=2` sfl certificate no longer looks like a badly conditioned five-dimensional interval problem. C188 had already reduced it to three variables; this run shows numerically that a standard preconditioned Poincare--Miranda/Krawczyk certificate should have a very large robustness margin, and it rigorously removes the objective-value Gaussian tails outside `|z|<=9`. The remaining hard part is now only validated first/second derivative integration on a compact one-dimensional Gaussian interval.

## 1. Required continuity, source scope, current status, and ownership

Before new work I reread/rechecked current `master` rather than restarting from chat memory:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- newest own report `runs/R14/2026-09-16T22-50-51Z_r14-stuck1-2sfl-validation.md` and the C188 report immediately before it;
- newest same-source/neighbor reports `runs/R15/20260916_2258Z_i0076_excursion_palm_a19.md` and `runs/R07/20260916T2322Z_i0077_aperiodic_asymmetric_pulses_07.md`;
- targeted repository/intake searches for Gardner / negative spherical perceptron / R14 ownership.

The approximately-780-row `probability_1000_intake_*/problems.jsonl` family remains too large for a literal connector rendering without truncation. Whole-intake reread is therefore **ACCESS-LIMITED / PARTIAL**; the exact R14 target, prior R14 reports, ownership, posted exclusions, and relevant neighboring work were directly checked. `POSTED.md` excludes the owner's Ising-perceptron work, not this spherical Gaussian target.

Canonical rigorous R14 state entering and leaving this run:

- `alpha_L = 630297437506/10^11 = 6.30297437506`, from Montanari--Zhong--Zhou Theorem 4.3 after exact normalization matching;
- `alpha_U = 1278437096216/10^11 = 12.78437096216`, from C182--C184, which globally exhaust the corrected one-parameter Stojnic-2013 partial-lift family;
- width `64813965871/10^10 = 6.48139658710`.

Fresh primary-source/status queries dated 2026-09-16 UTC / 2026-09-17 Asia/Jerusalem again found no later rigorous theorem identifying the unrestricted full-radius threshold for fixed negative margin. El Alaoui--Sellke still describe the negative-margin FRSB geometry as conjectural and their algorithmic pure-state construction has radius `sqrt(qbar N)<sqrt(N)`. Annesi--Malatesta--Zamponi compute the transition using a full-RSB ansatz. Stojnic 2023 gives complete sfl strong-duality/stationarity equations and numerical finite-level tables, explicitly noting that practical realization requires substantial numerical work. This is a bounded current-status search, not a worldwide novelty certificate.

A useful independent source cross-check this run is Montanari--Zhong--Zhou Definition 2 / Theorem 4.2: their rigorous `delta_ub(kappa)` is a one-dimensional exponential-comparison upper bound, and they explicitly state that its first part was already proved in Stojnic 2013 while numerical evaluation was used there to argue superiority to the RS bound. This is consistent with C180--C184: R14 made that first lifted level numerical-free and globally certified, but it cannot reach the source's `2-sfl` numerical `12.32` row.

## 2. Exact blocker inherited from STUCK-RECOVERY-1

Use C188 coordinates

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=1/[D(1-p)]-D/[1-pD^2]`,

with `0<p<1`, `0<D<1`, `gamma>0`. At `kappa=-1`, define

`mu(z)=sqrt(p) z-1`, `sigma=sqrt(1-p)`, `B=c/(4 gamma)`, `A=1+2B sigma^2`,

`f(z)=Phi(-mu/sigma)+A^{-1/2} exp(-B mu^2/A) Phi(mu/(sigma sqrt(A)))`.

The reduced complete-sfl objective is

`Ftilde_alpha(p,D,gamma)`

`= (1/2)(1-p q)c - gamma_p + [1/(2c)] log(D/(2 gamma_p)) - q/(2D) + gamma - (alpha/c) E log f(Z)`.

C188 proves that every interior zero of `grad Ftilde_alpha` recovers all five complete source stationarity equations. The source strong-sfl theorem evaluates the limiting random primal at such a stationary solution. Therefore a source-valid endpoint `alpha_U<=12.5` still requires a **validated stationary root**, not merely a positive arbitrary trial point.

The previous numerical candidate, now expressed in `(p,D,gamma)`, is near

`x_* = (0.656313184757..., 0.652653689820..., 0.158861855012...)`,

with numerical complete comparison value about `0.00637396915>0`. This remains **NUMERICAL ONLY**.

## 3. Move #7 — TAKE THE LIMIT: R14-C189 exact Gaussian objective-tail compactification

**STATUS: PROVED for the objective expectation on the stated rational parameter box.** This is a finite claim and has an executed exact-rational checker.

Fix the compact box

`B0 = [0.6562,0.6564] x [0.6525,0.6528] x [0.1587,0.1591]`

in `(p,D,gamma)`. On this box, the exact checker proves the coarse bounds

`c>0`, `B<7.027`, `A<6`,

and

`B/A < 1/[2(1-p)] < 3/2`.

Also

`0.81 < sqrt(p) < 0.811`.

The quantity `f(z)` is the inner conditional Laplace transform occurring in the complete `r=2` sfl formula, hence

`0 < f(z) <= 1`.

For `z<=-9`, `mu(z)<0`, so the first term `Phi(-mu/sigma)>1/2`. Therefore

`0 <= -log f(z) < log 2 < 1`.

For `z>=9`, `mu(z)>0`, hence the second Gaussian CDF is at least `1/2`. Using `A<6` and `B/A<3/2`,

`f(z) >= [1/(2 sqrt 6)] exp[-(3/2) mu(z)^2]`.

Since `mu(z)<0.811 z` for positive `z` and

`(3/2)(0.811)^2 = 0.9865815 < 1`,

we have

`-log f(z) < log(2 sqrt 6)+z^2 < 2+z^2`.

Thus, writing `Qbar(a)=P(Z>a)` and `phi` for the standard Gaussian density,

`E[-log f(Z); |Z|>9]`

`< Qbar(9) + int_9^infty (2+z^2) phi(z) dz`

`= 4 Qbar(9)+9 phi(9)`

`< (85/9) phi(9)`

by the elementary Mills bound `Qbar(9)<phi(9)/9`.

Finally `phi(9)<e^{-40}` and

`e > 1+1+1/2+1/6+1/24 = 65/24 > 27/10`,

so

`phi(9) < (10/27)^40`.

The exact rational checker therefore certifies

`E[-log f(Z); |Z|>9] < (85/9)(10/27)^40`

`= 5.2556429... x 10^{-17} < 10^{-16}`.

Hence

**C189.** Uniformly on `B0`, the omitted `|Z|>9` contribution to the complete `r=2` objective expectation is less than `10^{-16}`.

This does **not** yet certify the gradient or Hessian tails. It removes the objective-value tail, which was one of the six obligations in the stuck report, and shows that the eventual positivity check is not numerically delicate once a root is validated.

Exact artifact:

`artifacts/R14/2026-09-16T23-52-29Z_r14-recovery1-krawczyk_check_and_scout.py`

Executed output begins `EXACT_C189_PASS` and records the strict rational inequalities. The same file contains a clearly separated `NUMERICAL_ONLY` scout described below.

## 4. Move #15 — BREAK THE SYMMETRY: precondition the stationary equations, not the parameter box

The previous stuck report proposed an anisotropic box. A better idea is to leave a simple small cube in `(p,D,gamma)` and instead precondition the **equations** by the inverse Hessian at the approximate root.

Let

`G(x)=grad Ftilde_12.5(x)`, `H(x)=D G(x)`,

and let `M` be a fixed nonsingular matrix approximating `H(x0)^{-1}` at a rational center `x0` near the scout root.

The following standard Poincare--Miranda validation lemma is the right finite target.

### Preconditioned-face lemma

Let `B=x0+[-r,r]^3`. Suppose, with rigorous bounds,

`rho := ||M G(x0)||_infinity`,

`eta := sup_{x in B} ||I-M H(x)||_infinity < 1`,

and

`rho < (1-eta)r`.

Then `G` has a zero in `B`.

**Proof.** For `delta=x-x0`,

`M G(x)=M G(x0)+int_0^1 M H(x0+t delta) delta dt`

`=M G(x0)+delta-int_0^1 [I-MH(x0+t delta)]delta dt`.

On the positive `i`-face, `delta_i=r`, so the `i`th component is at least

`-rho+r-eta r>0`.

On the negative face it is at most

`rho-r+eta r<0`.

Poincare--Miranda gives a zero of `MG`; nonsingularity of `M` gives a zero of `G`. QED.

This is substantially easier to validate than six raw face-sign inequalities because the first-order cross-couplings are cancelled by `M`.

### Numerical scout only

Using 120-node Gauss--Hermite quadrature and automatic differentiation, the numerical stationary point is

`x0 ~= (0.656313184757223, 0.652653689820474, 0.158861855012242)`

with

`Ftilde_12.5(x0) ~= 0.006373969149841`.

The numerical Hessian is

`[[ 0.64031095, -1.00851417,  2.11788805],`

` [-1.00851417,  1.01613851, -2.88928059],`

` [ 2.11788805, -2.88928059,  5.63976172]]`,

with eigenvalues approximately

`(-0.37263639, -0.12827507, 7.79712263)`,

determinant about `0.37270213`, and 2-norm condition number about `60.78`. Thus the saddle is plainly nondegenerate; root existence, not optimization convexity, is the right local problem.

For the cube radius

`r=10^{-4}`,

a `7^3` numerical grid gives

`max ||I-MH||_infinity ~= 0.0145853`,

while a `21 x 21` grid on each preconditioned face gives the expected strict signs. The weakest sampled positive-face lower margin is about

`9.9272 x 10^{-5}`,

and the weakest negative-face magnitude is about

`9.9751 x 10^{-5}`.

These are **NUMERICAL ONLY** and do not enter the rigorous bracket. Their value is diagnostic: a rigorous certificate does not need a microscopic enclosure such as `eta<10^{-3}`. Even a very coarse proof such as

`eta <= 1/2`, `rho < 5 x 10^{-5}`

would already validate a stationary root in this `10^{-4}` cube.

The scout was independently repeated at Gauss--Hermite orders 64, 80, 96, and 120; the displayed objective values agree to roughly `1.6 x 10^{-14}` and the roots agree at the shown scale. Again, this is stability evidence, not proof.

## 5. Move #30 — ONE SCALE / ONE DIRECTION AT A TIME: the certification burden is now much smaller

The previous plan was "interval-Newton the entire nested expectation." That was too undifferentiated. C189 plus preconditioning split the job into three sharply different scales:

1. **Objective value.** The `|Z|>9` tail is already rigorously below `10^{-16}` by C189. Since the numerical stationary value is about `6.4 x 10^{-3}`, the final positivity verification has enormous slack.
2. **Residual.** It is enough to rigorously evaluate the three components of `M G(x0)` to absolute error far below `5 x 10^{-5}`. No global root optimizer is needed.
3. **Jacobian/Hessian.** It is enough to show the very coarse matrix enclosure `sup_B ||I-MH||_infinity < 1` (preferably `<1/2`). The numerical scout is around `0.015`, leaving more than an order of magnitude of interval slack.

Therefore the remaining finite obstruction is no longer "high-precision multidimensional interval Newton." It is:

> rigorously enclose the three first derivatives and nine second derivatives of the **one-dimensional** compact Gaussian integral on `z in [-9,9]`, plus their derivative-tail contributions, well enough to prove `rho<(1-eta)10^{-4}` and `eta<1`.

This is a much weaker validated-quadrature task than the one formulated in the previous stuck report. A composite high-order quadrature with interval Taylor remainder, or an interval implementation of the analytic first/second derivatives, should have enough slack. A naive interval evaluation that forgets first-order correlations is unnecessary because preconditioning moves the cancellation outside the integral.

### Exact remaining technical gap

C189 controls the **objective** tail only. Before a bracket move, the next certificate still needs rigorous tails for the first and second parameter derivatives, and a compact-interval quadrature enclosure for those derivatives. I did not replace those by floating Gauss--Hermite values.

## 6. Why this still does not move `alpha_U`

Stojnic 2023 Theorem 1 / Corollary 1 identifies the limiting random primal with the complete sfl random dual evaluated at a solution of the stationarity system. The source then specializes this to the spherical perceptron and reports numerical `r=2` values. At `kappa=-1`, its Table 2 gives approximately

`gamma_sq=0.1500`, `gamma_sq^(p)=1.6660`, `p2=0.6649`, `q2=0.2780`, `c2=3.7194`, `alpha=12.32`.

The source explicitly describes numerical evaluation as needed to make the theorem operational. Therefore neither the source's `12.32` row nor R14's present `12.5` numerical root is a rigorous threshold endpoint until the stationary root and comparison sign are certified.

The rigorous bracket stays

`6.30297437506 <= alpha_c(-1) <= 12.78437096216`.

No restricted overlap ansatz or numerical stationarity point is relabeled as a proof.

## 7. Independent R15 audit

Newest R15 package read:

`runs/R15/20260916_2258Z_i0076_excursion_palm_a19.md`.

I independently checked the central mechanism of its C19 finite-intensity excursion-Palm theorem against the cited Palm/shift-coupling literature. Last--Moerters--Thorisson (Ann. Probab. 42 (2014), 431--463) explicitly formulate Palm measures for invariant random measures and their Theorem 2.1 states that a balancing allocation shifts one Palm law to the other. Their introduction also records the standard point-process fact that the Palm version of a stationary Poisson process is the stationary process with an extra point at the origin. Thorisson's continuous-time shift-coupling work supplies the corresponding shift-coupling framework.

For a finite-intensity thinning `A` of the Brownian excursion PPP, the Palm law is therefore the ordinary marked PPP plus one forced `A`-excursion. A finite local-time allocation shift can remove that Palm bias. Finite local-time displacement corresponds to finite physical inverse-local-time displacement almost surely; after the shift, the positive and negative local-time half-lines are independent excursion PPPs, yielding independent Brownian halves.

I therefore record the narrow audit

`R14-AUDIT-R15-I0076-C19-09 = PASS`

for **C19's finite-intensity excursion-Palm no-go theorem only**. This does not audit all details of R15-C20's identification of the a16 candidate with that Palm law, and it does not solve Burdzy--Scheutzow Problem 7.2.

## 8. Recovery verdict and hard-task rule

This was the execution of **hard-task recovery 1 of at most 2** selected by the previous stuck report: reduce the obstruction to a finite computation and run it.

It did not move the bracket, so the unchanged count is now `4`. It did, however, materially change the finite blocker:

- objective tail: rigorously solved (`<10^-16`);
- stationary-root conditioning: numerically very favorable after preconditioning;
- full remaining obstacle: validated first/second derivative Gaussian integration on `[-9,9]` plus derivative tails.

Because the metric remains unchanged and the same source-level obligation survives, the **next R14 invocation must be the second thinking/stuck-recovery report**, not another incremental certificate. It should decide whether to spend the final allowed recovery on a derivative interval-Taylor/quadrature implementation or hand the present package off immediately. A suitable nonrepeating method triple for that thinking run is **#6 DEFORM TO A POINT YOU CAN SOLVE, #10 DERANDOMIZE, #28 REPLACE FOR ALL WITH TYPICAL**. If the second permitted recovery is then executed and the same blocker still survives, the third stuck episode must hand off and rotate according to the owner rule.

## 9. Persistence

Executed artifact output SHA-256:

`8cb3c88b8909dfa1ad5dd1f46b299e44aca6978fffd67aaf8245e9a428fb9679`.

Artifact creation commits:

- checker/scout source: `dc79308a94ef09404264f23d855e9ef5b21fe9dd`;
- executed output: `42ebdd3d4a8a7a7a1069dd8483bf4f0f1f347af2`.

Both were read back at their returned commits before this report was written. No shared root, peer file, email, Drive object, public page, workflow, permission, purchase, or scheduler configuration was changed.

```yaml
ledger_delta:
  track: "R14 HARD OUTSIDE"
  source: "Gardner 1988 negative-margin spherical perceptron; modern navigation arXiv:1306.3980, arXiv:2010.15811, arXiv:2110.15824, arXiv:2312.16531"
  target: "rigorous whp satisfiability threshold at frozen kappa=-1 in the iid Gaussian spherical model"
  metric: "alpha_upper-alpha_lower"
  before: "6.48139658710"
  after: "6.48139658710"
  status: "PARTIAL / OPEN"
  unchanged_count_before: 3
  unchanged_count_after: 4
  recovery_state: "STUCK-RECOVERY-1 executed; metric unchanged; next invocation must be STUCK-RECOVERY-2 thinking report"
  exact_evidence:
    - "R14-C189: objective Gaussian tail outside |Z|<=9 is <1e-16 uniformly on B0"
    - "artifacts/R14/2026-09-16T23-52-29Z_r14-recovery1-krawczyk_check_and_scout.py"
    - "artifacts/R14/2026-09-16T23-52-29Z_r14-recovery1-krawczyk_check_and_scout.out"
  numerical_only:
    - "alpha=12.5 complete-2-sfl root scout near (p,D,gamma)=(0.656313184757,0.652653689820,0.158861855012)"
    - "sampled preconditioned eta about 0.014585 on radius-1e-4 cube; not rigorous"
    - "comparison value about 0.00637396915; not rigorous"
  remaining_obligation: "rigorous derivative tails and validated compact Gaussian quadrature sufficient for rho<(1-eta)1e-4 and eta<1"
  audit_ids:
    - "R14-AUDIT-R15-I0076-C19-09 = PASS (C19 only)"
```
