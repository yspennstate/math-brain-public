Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO MOVEMENT: external/source-verified `p_comb <= 2 -> <= 2`; the in-track written candidate `p_comb <= 1 -> <= 1` remains pending independent validation. This is the required Section-I STUCK1 thinking run. Methods B20/B21/B22.**

# HARD7-02 — STUCK1: replace global minor control by dynamic singular-value absorption

Status: **PARTIAL / SOURCE CONJECTURE OPEN / FIRST SECTION-I STUCK REPORT ON THE LI--LITVAK--YU TARGET.** No new theorem, closure, audit, or publication-priority claim is made in this run.

## 1. Continuity, ownership, source and runtime

I resumed the exclusive claim

`operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`

and the immediately preceding checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-20T10-10-12Z__lly-gaussian-normal-volume-potential.md`.

The previous checkpoint recorded three consecutive no-movement runs after the internal `p_comb<=1` candidate and therefore forced this invocation into Section I. I did not restart the target, return to the released Han band problem, or promote the internal logarithmic-exponent-one argument beyond its pending-validation status.

Before the mathematical diagnosis I re-read the HARD7 control file, both new-methods control/directive files, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, the current canonical claim, the newest own checkpoint, and targeted neighboring non-Hermitian/heavy-tail ownership records. Targeted intake/alias searches were also repeated. The large JSONL intake files are not exposed here as a faithful one-call semantic read of all roughly 780 rows, so this is recorded as targeted recovery rather than a false claim of a complete fresh semantic reread. No collision with the owner's excluded least-singular-value/Gaussian-row-submatrix/Toeplitz-Hankel/additive-spike/gated-product papers, a Bernoulli-singularity target, C0031/C0032, or a posted result was located.

The exact source remains Dongbin Li, Alexander E. Litvak and Tingzhou Yu, arXiv:2604.10446v2 (11 August 2026), *Least singular values of shifted sparse random combinatorial matrices*, Conjecture 3.9. In the sparse half `d<=n/2`, each row is an independent uniform `d`-subset indicator and the normalized matrix is

`A_n=M_n/sqrt(d(1-d/n))`.

Conjecture 3.9 asks whether `ESD(A_n)` converges in probability to the circular law whenever only `d(n)->infinity`. Corollary 1.4 proves the logarithmic regime `d >= (log n)^(2+eps)`, `d=o(n)`.

A fresh bounded 20 September 2026 web check of arXiv `2604.10446`, both the v1/v2 titles, the authors, and `sparse circular law` / `random combinatorial matrix circular law` again located the current source and the iid minimal-sparsity circular-law literature, but no located theorem lowering the exact row-combinatorial circular-law threshold below the source's `log^(2+eps)` regime. This is bounded negative evidence, not a worldwide novelty certificate.

Runtime metadata available to this invocation identifies **GPT-5.6 Sol**. Reasoning-effort telemetry is not exposed, hence **UNVERIFIED**. The native scheduler/update interface available here still exposes title, prompt, schedule, timing mode and enabled state, but no model selector, no reasoning-effort selector and no guaranteed run duration. Therefore GPT-6/maximum remains prompt-requested only. Changing that would require a platform scheduler surface/API that actually exposes model and reasoning fields; a repository edit cannot do it. I did not probe or modify P26 or any other schedule. The historical `You cannot modify this task` result must be handled from an authorized owner/workspace scheduling context or by platform support, not by duplicating/bypassing the task; the repository policy records that a later authorized context did succeed for P26, so the old denial is historical rather than a mathematical or repository blocker.

## 2. Frozen metric

The fixed source-relevant quantity remains

`p_comb = inf { p>=0 : for every eps>0, the circular law is rigorously established in the frozen model whenever d >= (log n)^(p+eps) and d=o(n) }`.

Evidence levels remain separate:

- external/source-verified: `p_comb <= 2` before and after;
- HARD7-02 written candidate: `p_comb <= 1` before and after, still pending genuinely independent validation.

Thus the metric does not move in this Section-I run.

## 3. (a) Exact statement that blocks

The route-independent obstruction is microscopic singular-value mass for a nonzero spectral shift. The cleanest form exposed by the cube-to-slice coupling is the following de-regularization obligation.

For each fixed `z != 0` (or for a.e. fixed `z`) one needs a deterministic `eta_n -> 0`, compatible with the already-proved transport window

`eta_n d(n)^(1/4) -> infinity`,

such that, with `s_j=s_j(A_n-zI)`,

\[
D_{\eta_n}(A_n;z)
:=\frac1{2n}\sum_{j=1}^n
\log\!\left(1+\frac{\eta_n^2}{s_j^2}\right)
\xrightarrow{\mathbb P}0
\qquad(d(n)\to\infty).
\tag{3.1}
\]

A spatially averaged version over every compact `K` is also sufficient:

\[
\int_K D_{\eta_n}(A_n;z)\,d^2z\xrightarrow{\mathbb P}0.
\tag{3.2}
\]

The positive-ridge comparison already works under `d->infinity`; the nilpotent-versus-cyclic-shift stress test from the 08:12 report proves that Hilbert--Schmidt closeness and positive-ridge potential convergence alone do not imply (3.1) or ESD convergence. The later matching/minor route merely recodes the same problem: its unresolved multi-level volume potential `Psi_j` is a device for preventing excessive small-singular-value mass, not an independent endpoint.

## 4. (b) Routes tried and the precise reason each stopped

### Route 1 — B2/B6/B30 at admission

The negation was attacked through zero columns, sparse dependence and fixed shifts. The zero-column fraction is of order `e^{-d}` and therefore vanishes when `d->infinity`; it does not refute weak ESD convergence. Centered rows are isotropic on `1^perp` after normalization, so second moments also do not expose a counterexample. Fixed `z!=0` removes the literal `z=0` kernel mechanism. **Failure:** these tests say the conjecture survives the obvious sparse obstructions but give no control of the logarithmic singular-value tail.

### Route 2 — B5/B11/B28, ridge hybrid volumes

The 07:12 report replaced unregularized row volumes by

`Phi_eta(H)=1/2 log det(HH^*+eta^2 I)`

and integrated the conditional concentration tail instead of union-bounding over every hybrid row. This produced the written `p_comb<=1` candidate. **Failure below the logarithmic scale:** removing the ridge at the endpoint was still tied to quantitative shifted least-singular-value input in a range beginning at `C log n`. The union-bound `log^2 n` loss was removed, but the hard edge itself was not.

### Route 3 — B1/B4/B18, cube-to-slice transport

A direct coupling to the iid Bernoulli matrix gives normalized Hilbert--Schmidt discrepancy `O_P(d^{-1/4})`. Hence ridge log potentials agree uniformly in `z` at every scale `eta` with `eta d^{1/4}->infinity`, in particular under only `d->infinity`. **Failure:** a rank-one perturbation from the nilpotent shift to the cyclic shift has vanishing fixed-ridge potential discrepancy yet macroscopically different eigenvalue laws. Thus a generic perturbation theorem cannot remove the ridge; the missing input must exploit random row-slice structure.

### Route 4 — B9/B14/B25, randomized matching shift

Randomizing the scalar shift as an independent permutation exposes a large matching-aligned invertible minor and gives strong residual matching anti-concentration. **Failure:** one good minor does not control the full bottom singular-value cloud. The construction leaves enough unaccounted directions that the normalized log determinant can still be dominated by microscopic singular values.

### Route 5 — B3/B13/B29, Gaussian normal and volume potential

For `H=[B C]`, the exact graph potential

`Psi(B,C)=log det(I+(B^{-1}C)^*(B^{-1}C))`

controls Gaussian-normal spread and equals minus the logarithm of the selected minor's Cauchy--Binet volume share. **Failure:** there is no proved monotone/telescoping law for `Psi` through the recursive matching descent. If `Psi` is large at many levels, the spread scale `e^{-Psi/2}` becomes useless. Even choosing a largest-volume minor does not solve this deterministically: Cauchy--Binet only guarantees a share at least the reciprocal of the number of competing minors, an exponentially weak guarantee at the residual dimensions relevant here.

The common diagnosis is now clear: all five routes either smooth away or localize the hard edge; none supplies a mechanism that *dynamically absorbs a positive fraction of the remaining small singular values while tolerating a vanishing exceptional set*.

## 5. (c) What a successful proof must contain that no route so far contains

The missing ingredient is not another one-shot least-singular-value estimate. It must control an **empirical block of small singular values** and must not demand that all `n` rows or columns be simultaneously regular when `d<<log n`.

A viable proof needs all of the following in one mechanism:

1. a sequential exposure in which each step creates a fresh direction with enough conditional randomness;
2. a drift statement saying that a row/column addition absorbs one more singular value with probability `1-o_d(1)`, rather than a union bound requiring every step to succeed;
3. tolerance of `o(n)` atypical rows/columns, because uniform row regularity is false/too costly in the sublogarithmic regime;
4. a final comparison converting that dynamic absorption into (3.1) or an equivalent uniform-integrability statement for the negative logarithm.

This is exactly the type of ingredient supplied in the iid sparse circular-law proof of Sah--Sahasrabudhe--Sawhney, but not yet ported to the fixed-row-sum law.

## 6. Counterexample-oriented stress test of that proposed port

A naive port that asks every row to retain comparable residual degree after revealing a positive fraction of the columns cannot work at arbitrary `d->infinity`.

Fix `0<theta<1` and expose `k=floor(theta n)` columns. For one row, the probability that all `d` ones were already exposed is

`binom(k,d)/binom(n,d) <= theta^d`.

Hence the **fraction** of fully depleted rows has expectation at most `theta^d -> 0` when `d->infinity`; this is compatible with a proof that tolerates a vanishing exceptional set. But the probability that **no** row is depleted cannot be forced from this estimate when `d<<log n`, because the crude all-row cost is `n theta^d`, which may diverge.

This is a useful falsification test: any continuation that reinstates an `all rows are good` event has simply rebuilt the logarithmic barrier in another language. The dynamic route must work with typical rows, not uniform rows.

There is also a positive structural reason the iid dynamic argument may be portable. Conditional on the first `k` columns, the original rows remain independent of one another. For row `i`, if `s_i` ones have appeared in the exposed columns, the bit in the next unrevealed column is Bernoulli with conditional parameter

`q_i=(d-s_i)/(n-k)`.

Thus a newly exposed column has **independent coordinates across rows**, though generally non-identical parameters `q_i`. The dependence obstacle is therefore not independence across the fresh column; it is controlling the empirical profile of the `q_i` while allowing an exceptional set. That is substantially closer to the iid sparse dynamic process than the previous matching/minor formulations made visible.

No new theorem is claimed from this diagnostic calculation, and no checker was manufactured for it.

## 7. (d) Simplest special case still unproved

A deliberately narrow test case is

`d_n = ceil((log n)^(1/2))`, `z=1`, `eta_n=d_n^(-1/8)`.

The simplest still-unproved obligation on this track is

\[
\frac1{2n}\sum_{j=1}^n
\log\!\left(1+\frac{d_n^{-1/4}}
{s_j(A_n-I)^2}\right)
\xrightarrow{\mathbb P}0.
\tag{7.1}
\]

The chosen ridge satisfies `eta_n d_n^(1/4)=d_n^(1/8)->infinity`, so the cube-to-slice ridge comparison already reaches this scale. Establishing (7.1) would not prove the full conjecture, but it would cross below the current `log n` hard-edge input and would directly test whether the dynamic absorption mechanism is doing something genuinely new.

## 8. (e) Nearest solved problem and the ingredient it has

The nearest solved analogue is the **iid sparse circular law under the minimal condition `np->infinity`**, proved by Rudelson--Tikhomirov and revisited by Sah--Sahasrabudhe--Sawhney. The latter proof is especially relevant because it removes a bottom block of singular values from a truncated log potential and then builds the matrix up by alternating row and column additions, absorbing singular values dynamically on quasi-randomness/unique-neighborhood events.

What that model has and this one lacks in its published proof is a ready-made entrywise-iid quasi-randomness package. Li--Litvak--Yu explicitly note that their row-constrained matrix has neither iid entries nor full `d`-regularity, that transpose symmetry is absent, and that sparse conditioning does not provide enough randomness for the dense epsilon-net argument. On the other hand, the conditional-column observation in Section 6 above shows a possible bridge: after row-wise column exposure, fresh column coordinates are independent across rows with inhomogeneous parameters. A successful port would therefore need an **inhomogeneous unique-neighborhood / singular-value-absorption lemma stable under an `o(n)` exceptional set of rows**.

The random-regular-digraph circular law is a second nearby solved model at `d->infinity`, but its switching/permutation structure uses fixed column as well as row degrees; that symmetry is absent here, making it a less direct port than the iid dynamic process.

## 9. The three new Section-B moves actually used

- **B20 — FIND WHY THE ALGORITHM FAILS.** The matching/minor recursion fails because selecting one invertible minor does not control the empirical hard edge, and deterministic volume maximization only gives exponentially weak Cauchy--Binet shares. Outcome: the route's actual missing object is a singular-value *absorption process*, not a better pivot rule.
- **B21 — ASK WHO ELSE HAS THIS SHAPE.** The Sah--Sahasrabudhe--Sawhney iid sparse circular-law process has exactly the desired shape: discard the bottom block, then add rows/columns while dynamically bringing singular values under control. Outcome: this gives a concrete candidate architecture that is not another least-singular-value lemma.
- **B22 — READ THE FAILURES, NOT THE SUCCESSES.** Li--Litvak--Yu's own discussion identifies the asymmetric row-constrained dependence and failure of sparse conditioning/net arguments. Stress-testing the port shows that demanding uniform conditional row regularity recreates a `log n` threshold, while allowing a vanishing exceptional fraction is consistent with arbitrary `d->infinity`. Outcome: the required port must be inhomogeneous and exception-tolerant.

These numbers were not used in the previous Li--Litvak--Yu triples B2/B6/B30, B5/B11/B28, B1/B4/B18, B9/B14/B25, or B3/B13/B29.

## 10. Exactly one Section-I recovery choice

**Chosen recovery: port the technique from the nearest solved problem in Section 8.**

The next research run will not return to the matching-volume recursion or manufacture another endpoint checker. It will attempt a row-slice analogue of the Sah--Sahasrabudhe--Sawhney dynamic singular-value absorption step, starting from the exact conditional law

`q_i=(d-s_i)/(n-k)`

for a fresh column and allowing an `o(n)` exceptional set of rows. The first target is the special case (7.1); only if the dynamic step closes there should the route be generalized.

This is the **first** Section-I recovery choice for the Li--Litvak--Yu target. The target is not released in this run. A second stuck episode may trigger one final recovery; a third requires terminal handoff/rotation under the controlling policy.

## 11. Next three Section-B moves

For the selected recovery, use a new triple:

- **B7 — TAKE THE LIMIT:** derive the deterministic limiting residual-degree profile under column exposure and identify the time interval on which enough `q_i` remain comparable to `d/n`;
- **B12 — FIND WHAT IS CONSERVED:** exploit the exact per-row budget of `d` ones to control the aggregate residual-degree mass without uniform row bounds;
- **B27 — SWAP THE QUANTIFIERS:** replace `every row is regular at every time` by `at every relevant time, enough rows are regular`, which is the only quantifier order compatible with `d<<log n`.

## 12. Ledger delta for coordinator consumption

No shared root ledger was edited by HARD7-02.

Suggested delta:

`HARD7-02 | Li--Litvak--Yu Conjecture 3.9, row-combinatorial circular law | external p_comb <=2 -> <=2; written candidate <=1 -> <=1 pending independent validation | PARTIAL / SOURCE OPEN / STUCK1 | B20/B21/B22 | selected recovery: port SSS dynamic singular-value absorption with inhomogeneous fresh columns and o(n) exceptional rows`

No email, Drive, public posting, workflow, other-track file, permission, or scheduler state was changed.