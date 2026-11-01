Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **Movement: `T_corr=0 -> 1`. Methods tried: B6/B11/B29. New theorem-sized PARTIAL result: for the explicit non-i.i.d., non-Hermitian Campbell--O'Rourke C2 family `vartheta_x`, every fixed `0<x<1`, `x != 1/2`, has radial power exponent exactly `1`; in particular the frozen `x=1/4` slice is classified. The full source Question 1.9 remains open.**

# HARD7-02 — Campbell--O'Rourke Question 1.9: phase-Mahler peeling gives the exact interior power exponent

Status: **PARTIAL / source Question 1.9 remains OPEN by bounded current-status search / internal theorem candidate self-checked but not independently audited.**

Frozen metric:

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which the full asymptotic radial tail exponent/class of mu_{alpha,theta} is rigorously determined`.

Before: `T_corr=0`.

After: **`T_corr=1`**.

This run is the first substantive recovery run after Q1.9 STUCK1. Because the frozen metric moved, the Q1.9 unchanged streak resets to zero; no STUCK2 is triggered. The source itself is not closed, so the claim remains active.

## 1. Continuity, repository read, ownership, and capability honesty

I resumed the active exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

and the mandatory STUCK1 checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T17-12-36Z__q19-stuck1-jensen-potential-route.md`.

At run start I re-read:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the active Q1.9 claim and newest own reports;
- repository-wide Campbell--O'Rourke / intake / claim hits, including the C0026--C0032 intake neighborhood already recovered in the Q1.8 chain;
- the neighboring heavy-tail terminal handoff `research7_2026-09-17/R7-06/handoffs/2026-09-19T095800Z__C0032_terminal_handoff.md`.

C0032 is the distinct i.i.d. heavy-tailed circular-law explicit-density problem and is in terminal handoff. Q1.9 remains exclusively owned by HARD7-02. Repository search still finds no equivalent live claim under an alias. No claim file was overwritten and no shared root ledger was edited.

The runtime/scheduler capability situation is unchanged. The exposed automation surface has title, prompt, schedule/timing mode and enabled state, but no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution-duration control. `GPT-6 / maximum` is therefore a prompt request only. A real change requires a product/backend surface exposing binding model/effort controls, or an authorized workspace/account context where those controls exist. Historical repository records of `You cannot modify this task` for P26/P01/P03 are permission-context failures; the compliant workaround is the owning/authorized context or platform support/ownership transfer, not a duplicate task or bypass. No scheduler mutation was attempted here.

No Gmail, Drive, public posting, paid compute, workflow execution, force push, neighboring-track edit, or shared-ledger write was performed.

## 2. Exact source statement and current-status refresh

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

Primary source: `https://arxiv.org/abs/2010.01261`.

A fresh bounded 19 September 2026 search used the exact title/authors, `Question 1.9`, `theta_d`, `mu_{alpha,theta_d}`, `tail behavior`, `heavy-tailed elliptic`, `PWIT`, `Hermitization`, and 2023--2026 follow-up terms. It recovered the 2022 source, Bordenave--Caputo--Chafaï's i.i.d. heavy-tailed endpoint, Campbell--O'Rourke's later Lévy--Khintchine random-Laplacian work, and Carpenter--O'Rourke's 2025 sparse elliptic paper, but I did **not** locate a paper claiming a general solution of Q1.9 or the interior phase-family exponent proved below. This is bounded negative evidence only, not a worldwide novelty certificate.

The source itself contrasts a light/stretched-exponential i.i.d. axis-supported endpoint with the heavy Hermitian endpoint. Those endpoint results are literature baselines, not HARD7-02 discoveries.

## 3. Frozen source-valid family

Fix `alpha=1`. For `0<x<1`, let

`eta_x = Law(sqrt(x)e^{i phi}, sqrt(1-x)e^{-i phi})`,

`vartheta_x = (eta_x + tau#eta_x)/2`,

where `phi` is uniform on `[0,2pi)` and `tau(w_1,w_2)=(w_2,w_1)`.

The frozen point is `x=1/4`. Write

`mu_x := mu_{1,vartheta_x}`,

`kappa_x := (x(1-x))^(1/4)`,

`g_x := kappa_x^2 = sqrt(x(1-x))`.

Use the exact source-valid representative already verified in the preceding Q1.9 reports:

- `P(R>r)=r^{-1}` for `r>=1`;
- `R` independent of the angular mark;
- `(xi_1,xi_2)=R W`, `W~vartheta_x`;
- diagonal atom zero;
- normalization `a_n=n`.

For every interior `x`, the support is nondegenerate in the source's C2 sense. The source theorem says the deterministic limiting ESD depends on `(alpha,theta_d)`, so it is legitimate to compute `mu_x` with this convenient representative.

The already-proved Q1.9 moment theorem gives, uniformly over `0<x<1`,

`int |z|^p mu_x(dz) <= 1 + 4p/(1-p)`, `0<p<1`.                  (3.1)

In particular, for `p=1/2`,

`int |z|^(1/2) mu_x(dz) <= 5`.                                    (3.2)

It also implies

`liminf_{r->infinity} [-log mu_x(|z|>r)]/log r >= 1`.             (3.3)

The missing direction was a lower tail for the **full nonnormal matrix**, not its exceedance skeleton.

## 4. B6 — deform from the solvable reciprocal-edge skeleton without perturbing eigenvalues

The STUCK1 obstruction was that individual nonnormal eigenvalues are unstable under reattaching the sub-threshold background. The key replacement is a determinant inequality which is uniform in the background, so the background can be deformed from zero to full strength without any spectral perturbation estimate.

Let `A_n=X_n/n`, fix an unordered edge `e={i,j}`, and condition on all variables except this edge's phase and radial overshoot. For fixed radial size and swap choice, the two directed entries are

`a u` and `b u^{-1}`, `u=e^{i phi}`,

with product

`ab = g_x (R_e/n)^2 =: q`.                                        (4.1)

For fixed `z`, set

`D(u)=det(zI-A_n)`.

### Lemma 4.1 — exact phase Laurent form

There exist coefficients `c_{-1},c_0,c_1`, independent of `u`, such that

`D(u)=c_{-1}u^{-1}+c_0+c_1u`,                                    (4.2)

and

`c_0=A_0-qB`,                                                     (4.3)

where `A_0` is the determinant after setting both directed entries of `e` to zero and

`B=det(zI-A_n^{\setminus{i,j}})`                                  (4.4)

is the principal minor obtained by deleting endpoints `i,j`.

**Proof.** In the Leibniz expansion, a permutation uses neither distinguished directed entry, exactly one of them, or both. Their phase exponents are therefore `0`, `+1`, `-1`, or `(+1)+(-1)=0`, which gives (4.2). Terms using both entries force the transposition `i<->j`; its permutation sign is `-1`, while the two off-diagonal signs in `zI-A_n` multiply to `+1`. The remaining permutation is arbitrary on the complement, giving exactly `-qB`. Terms using neither give `A_0`. Hence (4.3). `QED`

The exact symbolic 4-by-4 generic-matrix self-check in this run verifies (4.3) independently of any numerical sampling.

### Lemma 4.2 — phase Mahler lower bound

For every quadratic polynomial `h(u)=d_0+d_1u+d_2u^2`,

`(1/(2pi)) int_0^{2pi} log|h(e^{i theta})| dtheta >= log|d_1|-log2`.  (4.5)

**Proof.** If `d_2 != 0`, write `h(u)=d_2(u-r_1)(u-r_2)`. Jensen's formula gives Mahler measure

`M(h)=|d_2|max(1,|r_1|)max(1,|r_2|)`.

Since `|d_1|=|d_2||r_1+r_2| <= 2M(h)`, taking logs proves (4.5). Lower degree follows directly or by continuity. `QED`

Because `|u|=1`, multiplying (4.2) by `u` does not change the logarithmic modulus. Lemmas 4.1--4.2 give

`E_phi log|det(zI-A_n)| >= log|A_0-qB|-log2`.                    (4.6)

Crucially, **all other matrix entries are arbitrary in (4.6)**. If they are multiplied by a deformation parameter `tau in [0,1]`, the same inequality holds with the same constant. Thus the lower-bound mechanism survives continuously from the reciprocal-edge skeleton `tau=0` to the full background `tau=1`; it never asks individual eigenvalues to move continuously.

### Lemma 4.3 — Pareto overshoot logarithmic anti-concentration

Condition on `R_e>sn`, `s>=1`. Write `R_e=snY`. Then

`P(Y>y)=y^{-1}`, `y>=1`,

and `X:=Y^2` has density `(1/2)x^{-3/2}` on `[1,infinity)`. For every `c in C`,

`E log|X-c| >= -1`.                                                (4.7)

**Proof.** Since `|X-c|>=|X-Re c|`, it suffices to take `c` real. The integrand can be negative only when `|x-c|<1`. On `[1,infinity)` the density is at most `1/2`, while

`int_{-1}^1 log|t| dt=-2`.

Restricting this interval to `[1,infinity)-c` can only discard negative mass, so the negative contribution is at least `-1`; outside it the logarithm is nonnegative. `QED`

Now `q=QX` with

`Q=g_x s^2`.                                                       (4.8)

For `B!=0`, factor `QB` inside (4.6) and apply Lemma 4.3:

`E_{phi,Y} log|det(zI-A_n)|`
`>= log Q + log|det(zI-A_n^{\setminus{i,j}})| -(1+log2)`.         (4.9)

For a fixed positive-radius circle, the exceptional zeros of the minor characteristic polynomial form a finite set. Standard logarithmic truncation (or integration away from those points followed by monotone limit) justifies using (4.9) under the circle integral. The Pareto log moment is finite, so no hidden infinite positive term is needed.

**B6 outcome: success.** The skeleton-to-full-background deformation is handled exactly at the determinant level; the former nonnormal reattachment obstruction disappears for the circular log potential.

## 5. B11 — dualize the tail problem to a circular log determinant

For fixed `s>=1`, let `G_s` be the exceedance graph on unordered pairs with

`R_e>sn`.

It is exactly `G(n,1/(sn))`. Let `M_s` be the set of isolated edges of `G_s`, and put `m_s=|M_s|`. The edges in `M_s` are disjoint. Conditional on the indicator graph, their phases and Pareto overshoots remain independent. Therefore (4.9) can be iterated over every selected edge:

`E_selected log|det(zI-A_n)|`
`>= m_s[log(g_x s^2)-(1+log2)]`
`   + log|det(zI-A_n^{\setminus V(M_s)})|`.                       (5.1)

This is the decisive global replacement for eigenvalue perturbation.

For every finite matrix `M`, Jensen's formula gives the exact identity

`(1/(2pi)) int_0^{2pi} log|det(re^{i theta}I-M)| dtheta`
`= sum_j log max(r,|lambda_j(M)|)`.                               (5.2)

Define

`V_n(r):=(1/n) sum_j log^+(|lambda_j(A_n)|/r)`.                   (5.3)

Circle-average (5.1), apply (5.2), and bound the `(n-2m_s)`-dimensional minor's average below by `(n-2m_s)log r`. Subtract `n log r` and divide by `n`:

`E V_n(r)`
`>= (E m_s/n)[log(g_x s^2/r^2)-(1+log2)]`.                       (5.4)

No isotropy of `mu_x` is assumed.

The isolated-edge expectation is elementary and exact:

`E m_s/n`
`= ((n-1)/(2sn))(1-1/(sn))^(2(n-2))`
` -> e^{-2/s}/(2s)`.                                               (5.5)

Choose

`c_x:=kappa_x/(2e)`, `r=c_x s`.                                  (5.6)

Since `g_x=kappa_x^2`, the bracket in (5.4) is exactly

`log(4e^2)-(1+log2)=1+log2`.                                      (5.7)

Thus

`liminf_{n->infinity} E V_n(c_xs)`
`>= (1+log2)e^{-2/s}/(2s)`.                                       (5.8)

### Lemma 5.1 — transfer from finite matrices to `mu_x`

For every fixed `r>0`,

`E V_n(r) -> V_x(r):=int log^+(|z|/r) mu_x(dz)`.                  (5.9)

**Proof.** Campbell--O'Rourke's theorem gives weak convergence in probability of the empirical ESD to deterministic `mu_x`. For a bounded continuous truncation of `log^+(|z|/r)`, this implies convergence in probability and hence convergence of expectations because the truncation is bounded. To remove the truncation, fix any `p in (0,1)`. The previous finite-`n` moment proof gives

`sup_n E int |z|^p mu_{A_n}(dz)<infinity`.

Moreover `log^+(u/r)/u^p ->0` as `u->infinity`. Hence for radial cutoff `K`,

`sup_n E int_{|z|>K} log^+(|z|/r) mu_{A_n}(dz)`
`<= [sup_{u>K} log^+(u/r)/u^p] sup_n E int |z|^p mu_{A_n}(dz) ->0`.

The same bound passes to `mu_x` by the already-proved moment theorem. Therefore the truncation error is uniformly negligible, proving (5.9). `QED`

Combining (5.8)--(5.9), for every `s>=1`,

`V_x(c_xs) >= (1+log2)e^{-2/s}/(2s)`.                             (5.10)

**B11 outcome: success.** The tail question is dualized to the logarithmic potential, where phase averaging produces a background-uniform lower bound.

## 6. B29 — add infinity and extract the boundary exponent

Write `r=c_xs`. Equation (5.10) becomes

`V_x(r)`
`>= ((1+log2)kappa_x/(4er)) exp(-kappa_x/(er))`.                  (6.1)

For `r>=c_x`, the exponential factor is at least `e^{-2}`, so

`V_x(r) >= A_x/r`,                                                (6.2)

where

`A_x := (1+log2)kappa_x/(4e^3)>0`.                                (6.3)

Thus with the compactifying coordinate `rho=1/r`, the circular potential has a strictly positive linear boundary lower coefficient at `rho=0`.

Let

`F_x(r):=mu_x({|z|>r})`.

The standard layer-cake/Jensen identity is

`V_x(r)=int_r^infinity F_x(u) du/u`.                              (6.4)

This identity is classical; it is not a novelty claim.

Using (3.2), Markov gives `F_x(u)<=5u^{-1/2}`. Since `F_x` is decreasing, for `r>1`,

`V_x(r)`
`<= int_r^{r^3} F_x(u)du/u + int_{r^3}^infinity 5u^{-1/2}du/u`
`<= 2F_x(r)log r + 10r^{-3/2}`.                                   (6.5)

For all sufficiently large `r`, `10r^{-3/2}<=A_x/(2r)`. Combining (6.2) and (6.5) yields

`F_x(r) >= A_x/(4r log r)`.                                      (6.6)

Consequently,

`limsup_{r->infinity} [-log F_x(r)]/log r <=1`.                  (6.7)

On the other hand, (3.1) and Markov imply for every fixed `p<1`,

`F_x(r) <= B_p r^{-p}`,

so

`liminf_{r->infinity} [-log F_x(r)]/log r >=p`.

Letting `p upward 1` gives the opposite bound `>=1`. Therefore:

### Theorem 6.1 — exact radial power exponent on the interior phase family

For every fixed `0<x<1` with `x != 1/2`,

`lim_{r->infinity}`
`  [-log mu_{1,vartheta_x}({|z|>r})]/log r`
`=1`.                                                             (6.8)

In particular, at the frozen non-Hermitian point `x=1/4`, the full limiting ESD has radial power exponent exactly `1`.

The proof actually supplies the explicit lower bound

`mu_x(|z|>r) >= [(1+log2)kappa_x/(16e^3)] * 1/(r log r)`           (6.9)

for all sufficiently large `r` (with the threshold determined explicitly by (6.5)). The constant is not claimed sharp.

At `x=1/2` the same argument algebraically gives exponent one but that endpoint is Hermitian and is excluded from `T_corr`. At `x=0` or `1`, `kappa_x=0` and the lower-bound mechanism vanishes, exactly where the axis-supported i.i.d. endpoint has a much lighter tail.

**B29 outcome: success.** Compactifying infinity reveals a nonzero first-order logarithmic-potential boundary term, enough to determine the radial power exponent even though the exact `K/r` tail coefficient remains unresolved.

## 7. Counterexample-oriented interpretation

The initial counterexample question was whether tail class might interpolate smoothly away from the i.i.d. axis endpoint. For this explicit source-valid path of dependence measures, the answer is sharply negative at the level of power class:

- at the axis-supported i.i.d. endpoint, the literature gives a much lighter/stretched-exponential limiting tail;
- for every fixed interior `x` with nonzero reciprocal product, Theorem 6.1 gives power exponent exactly `1`.

Thus the power-tail mechanism turns on immediately when `kappa_x>0`; its coefficient tends to zero as `x->0`, but its exponent does not. This is a source-relevant qualitative answer for one continuous path in `theta_d`, not a classification of all dependence measures.

## 8. Why this is metric movement but not source closure

The frozen metric asked for one explicit non-i.i.d., non-Hermitian C2 family with the full asymptotic radial exponent/class determined. Theorem 6.1 supplies that for the entire interior one-parameter phase family, and in particular for the frozen `x=1/4` point. Therefore the conservative metric update is

`T_corr: 0 -> 1`.

I do **not** claim:

- the sharp asymptotic coefficient `F_x(r)~K_x/r`;
- a classification for arbitrary `theta_d`;
- a solution of all of Campbell--O'Rourke Question 1.9;
- novelty beyond the bounded prior-art search;
- closure before independent audits.

The honest source status remains **PARTIAL**.

## 9. Verification and artifacts

The mathematical idea was checkpointed before code at

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T18-14-04Z__idea-before-code-q19-mahler-peeling.md`

commit `e58b0e3a160203bb0690ce57c2909caff6ee1f0f`, read back successfully.

A small exact symbolic self-check was then executed for the finite algebraic core:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T18-14-04Z__q19-mahler-peeling-check.py`

commit `a1006f9b545d0abf4a3d5b9a623818b9d7b16a64`, read back successfully;

and its exact output was archived at

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T18-14-04Z__q19-mahler-peeling-check.out`

commit `19a8eccde96b0729b2ac4d531e9679372288d1fb`, read back successfully, ending

`ALL_EXACT_CHECKS_PASS = True`.

The checker verifies the generic 4-by-4 determinant middle-coefficient identity `c_0=A_0-abB`, the exact integral `int_{-1}^1 log|t|dt=-2`, and the constant simplification yielding `delta=1+log2` and `A_x=(1+log2)kappa_x/(4e^3)`. It is a **self-check**, not an independent audit. The theorem-sized proof is the argument on this page, not the checker.

## 10. Prior-art and audit posture

Searches this run were exact-title/source/question and mechanism searches, including `theta_d`, `mu_{alpha,theta_d}`, `tail behavior`, `Hermitization`, `PWIT`, phase/determinant/Mahler terms, and 2023--2026 follow-ups. No located source claimed this interior phase-family power-exponent theorem. That negative search is not a novelty certificate. The determinant/Mahler inequality and Jensen formula are classical mechanisms and are not claimed as new individually; the potentially new content is their combination with isolated Pareto reciprocal edges to answer this source slice.

No P26 or second OTHER-track independent audit was requested or invented in this run. Under the owner protocol, closure requires two independent audits; until then this remains an internal PARTIAL theorem candidate.

## 11. Next research obligation

Because `T_corr` moved, Section I does not force rotation. The next run should not re-prove exponent one. The strongest source-relevant next targets are:

1. determine whether `r F_x(r)` has a positive finite limit and identify its dependence on `x`, or prove that no such limit exists;
2. generalize the Mahler-peeling criterion from this phase family to angular laws with positive reciprocal-product mass and quantify exactly which `theta_d` produce power-one tails;
3. test whether the discontinuity at axis support can be formulated as a sharp necessary/sufficient condition on `theta_d`.

Use a fresh Section-B triple rather than B6/B11/B29.

## 12. Structured ledger delta (for the authorized shared-root maintainer)

`track`: `HARD7-02`

`target`: Campbell--O'Rourke (2022), Question 1.9, frozen `alpha=1`, `vartheta_x` phase family

`metric`: `T_corr`

`before`: `0`

`after`: `1`

`status`: `PARTIAL`

`new_result`: exact radial power exponent `1` for every fixed non-i.i.d., non-Hermitian interior `vartheta_x` (`0<x<1`, `x != 1/2`), including `x=1/4`; explicit eventual lower tail `>= const_x/(r log r)` plus all `p<1` moments

`source_closed`: `false`

`claim_action`: none; keep `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md` active

`shared_root_write`: none in this run
