Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO MOVEMENT in the frozen source metric this run: externally verified `p_comb <= 2 -> <= 2`; the track's written candidate milestone `p_comb <= 1 -> <= 1` remains pending independent validation. Methods B1/B4/B18.**

# HARD7-02 — cube-to-slice transport at vanishing ridge scale, and the exact pseudospectral obstruction

Status: **PARTIAL / SOURCE CONJECTURE OPEN.** This run does not claim Conjecture 3.9, does not promote the previous `p_comb<=1` argument beyond its pending-validation status, and makes no publication-priority claim.

## 1. Continuity, ownership, and evidence consumed

This run resumes the exclusive Li--Litvak--Yu sparse row-combinatorial circular-law claim. It does not restart HARD7-02 and does not return to the released Han band target.

I reread the controlling files `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, and `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`; the campaign `INDEX.md` and `RANKING.md`; root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`; the current canonical claim `operations/claims/LI-LITVAK-YU-2026-SPARSE-COMBINATORIAL-CIRCULAR-LAW.md`; and the newest own report `2026-09-20T07-12-00Z__lly-regularized-volume-log1-threshold.md`. I also rechecked the neighboring C0031/C0032 non-Hermitian/heavy-tail records: those concern heavy-tailed limiting laws / explicit densities and do not own this independent-row fixed-row-sum model. Targeted searches over the intake `problems.jsonl` material were repeated; the connector truncates the large ledgers, so this is **targeted intake recovery, not a claimed semantic reread of every row**.

No ownership collision or later release was found. No shared-root ledger was edited. No scheduler, email, Drive, workflow, permission, or public-posting action was taken.

### Current-source / literature check

The current source remains Dongbin Li, Alexander E. Litvak, and Tingzhou Yu, *Least singular values of shifted sparse random combinatorial matrices*, arXiv:2604.10446v2 (11 August 2026), whose Conjecture 3.9 asks for the circular law under the sole sparsity condition `d(n)->infinity`. Corollary 1.4 gives the published/current proved fixed-row-sum regime `d >= (log n)^(2+eps)`, `d=o(n)`. The previous run's claimed `p_comb<=1` improvement is an in-repository argument awaiting independent validation, not an external baseline.

Fresh 20 September 2026 searches for the exact arXiv identifier, both v1/v2 titles, the authors, `random combinatorial matrix circular law`, and logarithmic-sparsity improvements found the current v2 metadata and related singular-value papers, but no located theorem lowering Corollary 1.4 for this exact model. The primary-source proof architecture was re-inspected from the arXiv PDF surface: the determinant replacement splits into a head and tail; the head uses conditioned concentration and a simultaneous-row event, while the tail invokes least-singular-value control. This is bounded negative evidence only, not a worldwide novelty certificate.

## 2. Frozen metric and before/after

The frozen quantity remains

`p_comb = inf { p>=0 : for every eps>0, circular law is rigorously established in the fixed-row-sum model whenever d >= (log n)^(p+eps) and d=o(n) }`.

Two levels must be kept separate:

- **external/source-verified baseline:** `p_comb <= 2` before and after this run;
- **current HARD7-02 written candidate, pending independent validation:** `p_comb <= 1` before and after this run.

Thus this run is **no movement** in `p_comb`. Its value is that a different route now reaches a vanishing Hermitization scale under the *full conjectural condition* `d->infinity`, and an exact counterexample shows precisely why that fact alone cannot be converted into the circular law.

The unchanged streak for this admitted target is one run after the previous movement; Section I is not triggered.

## 3. New idea before code: abandon row-by-row replacement at positive ridge scale

The preceding route replaces rows one at a time and pays for conditional concentration. B1 suggests changing category: treat the fixed-sum row law as a transport of the iid Bernoulli cube. At a positive Hermitization ridge, singular values are Lipschitz enough that Hilbert--Schmidt transport controls the entire normalized log determinant in one shot.

The important question is whether this merely repackages the old logarithmic barrier. It does not: the transport estimate below works whenever only `d->infinity`, at a ridge `eta=d^{-1/8}->0`. But B18 exposes a genuine nonnormal obstruction: positive-ridge potentials can converge uniformly while eigenvalue laws are completely different. The obstruction is not bookkeeping or a missing union bound; it is microscopic pseudospectral information lost when the ridge is inserted.

No checker was written because the new claims are analytic, quantified for all dimensions, and proved on the page; there is no finite exhaustive assertion to certify.

## 4. B1 — exact cube-to-slice coupling

Let `p=d/n<=1/2`. Let `X=(X_1,...,X_n)` have iid Bernoulli(`p`) coordinates and set `S=sum_i X_i`.

Construct `R` from `X` as follows.

- If `S>d`, delete exactly `S-d` ones, choosing the surviving `d` ones uniformly among the `S` present ones.
- If `S<d`, add exactly `d-S` ones, choosing the new positions uniformly among the zero coordinates.
- If `S=d`, put `R=X`.

### Lemma 4.1 (slice marginal and exact transport cost)

`R` is uniform on the Hamming slice `{r in {0,1}^n : sum r_i=d}`, and

`||R-X||_2^2 = Hamming(R,X) = |S-d|`.

Consequently,

`E ||R-X||_2^2 <= sqrt(d(1-p))`.

#### Proof

The construction is equivariant under every permutation of the `n` coordinates. Its output always has exactly `d` ones. Since the symmetric group acts transitively on the `d`-slice, the marginal law of `R` is uniform on that slice. Every correction flips exactly `|S-d|` coordinates, proving the identity. Finally,

`E|S-d| <= sqrt(E(S-d)^2) = sqrt(np(1-p)) = sqrt(d(1-p))`.

This proves the lemma. ∎

Apply the construction independently to `n` rows. Let `M` have the desired fixed-row-sum law and let `B` have iid Bernoulli(`p`) entries, coupled row by row in this way. Normalize both by

`sigma = sqrt(d(1-p))`,

so `A=M/sigma` and `G=B/sigma`. Then

`E [ ||A-G||_HS^2 / n ]`
` = E||R-X||_2^2 / [d(1-p)]`
` <= 1/sqrt(d(1-p))`
` <= sqrt(2/d)`.                                           (4.1)

This uses only `p<=1/2`; no logarithmic lower bound on `d` appears.

## 5. B4 — a complete weaker theorem at a vanishing Hermitization scale

For any complex `n x n` matrix `H`, shift `z in C`, and `eta>0`, define the normalized ridge log potential

`U_eta(H;z)`
` = (1/(2n)) log det( (H-zI)(H-zI)^* + eta^2 I )`
` = (1/n) sum_{j=1}^n f_eta(s_j(H-zI))`,

where

`f_eta(s)=1/2 log(s^2+eta^2)`.

### Lemma 5.1 (ridge potential is Hilbert--Schmidt Lipschitz)

For all square `H,K`, all `z`, and all `eta>0`,

`|U_eta(H;z)-U_eta(K;z)| <= ||H-K||_HS / (2 eta sqrt(n))`.   (5.1)

#### Proof

For `s>=0`,

`f_eta'(s)=s/(s^2+eta^2) <= 1/(2 eta)`.

Mirsky's singular-value inequality gives

`sum_j |s_j(H-zI)-s_j(K-zI)|^2 <= ||H-K||_HS^2`.

The mean-value theorem and Cauchy--Schwarz therefore give

`|U_eta(H;z)-U_eta(K;z)|`
` <= (1/(2 eta n)) sum_j |s_j(H-zI)-s_j(K-zI)|`
` <= ||H-K||_HS/(2 eta sqrt(n))`.

The shift cancels from `H-K`, so the bound is uniform in `z`. ∎

Combining (4.1), Jensen, and (5.1) yields the following.

### Theorem 5.2 (full-sparsity ridge comparison)

Under the row coupling above,

`E sup_{z in C} |U_eta(A;z)-U_eta(G;z)|`
` <= 2^(-3/4) eta^(-1) d^(-1/4)`.                         (5.2)

In particular, for any fixed `0<gamma<1/4`, taking `eta=d^(-gamma)` gives

`sup_z |U_eta(A;z)-U_eta(G;z)| -> 0`

in probability whenever only `d->infinity`. With the concrete choice `eta=d^(-1/8)`,

`E sup_z |U_{d^(-1/8)}(A;z)-U_{d^(-1/8)}(G;z)|`
` <= 2^(-3/4) d^(-1/8) -> 0`.                              (5.3)

#### Proof

From (4.1),

`E[||A-G||_HS/sqrt(n)]`
` <= sqrt(E||A-G||_HS^2/n)`
` <= 2^(1/4)d^(-1/4)`.

Insert this into (5.1). Since (5.1) is uniform in `z`, the same estimate controls the supremum. Markov's inequality gives convergence in probability. ∎

This theorem is genuinely stronger in sparsity range than the previous row-replacement head estimate, but it is deliberately labeled **weaker than the circular law**: it controls a regularized Hermitized observable, not the zero-ridge logarithmic potential required to recover eigenvalues.

## 6. B18 — say it as nonnormal potential theory, then attack the implication

A tempting conclusion would be:

> if two matrix ensembles have asymptotically identical `U_eta` for a ridge `eta->0`, then their ESDs must be asymptotically identical.

That implication is false without a quantitative de-regularization hypothesis.

### Proposition 6.1 (rank-one pseudospectral obstruction)

Let `J_n` be the nilpotent unilateral shift matrix with ones on the superdiagonal, and let

`C_n = J_n + e_n e_1^*`

be the cyclic shift. Then

1. `||J_n-C_n||_HS=1`;
2. the ESD of `J_n` is exactly `delta_0` for every `n`;
3. the ESD of `C_n` is uniform on the `n`th roots of unity and hence converges to Haar measure on the unit circle;
4. for every fixed `eta>0`,

   `sup_z |U_eta(J_n;z)-U_eta(C_n;z)| <= 1/(2 eta sqrt(n)) -> 0`.

#### Proof

Only the `(n,1)` entry differs, proving (1). `J_n` is nilpotent, proving (2). `C_n` is the cyclic permutation matrix, so `C_n^n=I` and its eigenvalues are exactly the `n`th roots of unity, proving (3). Assertion (4) is Lemma 5.1. ∎

Thus even an `o(sqrt(n))` Hilbert--Schmidt perturbation, invisible to every fixed positive ridge, can change the limiting ESD macroscopically. This is the exact reason Theorem 5.2 is not a proof of Conjecture 3.9.

The example also tells us what any successful continuation must contain: an input special to the random row-slice model that rules out Jordan-type microscopic pseudospectral mass.

## 7. A spatial potential fact: ordinary determinant singularities are not the obstruction

The obstruction can be narrowed further. Let

`h(w)=(-log|w|)_+`.

For a deterministic square matrix `H` with eigenvalues `lambda_1,...,lambda_n`,

`[-(1/n)log|det(H-zI)|]_+`
` <= (1/n) sum_{j=1}^n h(z-lambda_j)`.                      (7.1)

If a measurable planar set `E` has area `a<=pi`, symmetric decreasing rearrangement gives, uniformly in `lambda`,

`int_E h(z-lambda) d^2z`
` <= (a/2) [1 + log(pi/a)]`.                               (7.2)

Indeed the extremal set is the disk of area `a`, and direct polar integration gives the right-hand side. Hence the normalized **negative determinant potential itself is uniformly integrable in the spatial variable `z` for every matrix**, with a modulus independent of `n` and independent of the matrix.

There is a similarly elementary deterministic bound on the positive singular-log part. Since

`log^+ s <= (1/2)log(1+s^2)`,

Jensen gives

`(1/n) sum_j log^+ s_j(H-zI)`
` <= (1/2) log(1+||H-zI||_HS^2/n)`.                        (7.3)

For the normalized fixed-row-sum matrix `A=M/sqrt(d(1-p))`, deterministically

`||A||_HS^2/n = 1/(1-p) <= 2`.

Thus on every fixed compact `|z|<=R`, the right-hand side of (7.3) is bounded by a constant depending only on `R`.

These observations show that the missing phenomenon is not ordinary logarithmic integrability around the eigenvalue roots. It is the difference between eigenvalue-root potential and the singular-value regularization — i.e. **pseudospectral de-regularization**.

## 8. The exact missing lemma exposed by this run

Write

`U_0(H;z)=(1/n)log|det(H-zI)|`

for almost every `z`. The ridge error is nonnegative:

`D_eta(H;z)=U_eta(H;z)-U_0(H;z)`
` = (1/(2n)) sum_j log(1+eta^2/s_j(H-zI)^2)`.              (8.1)

The transport route would reach the full source conjecture if one can establish a rate-compatible spatial de-regularization statement. A clean version is:

### Missing lemma M (random-slice pseudospectral de-regularization)

For the coupled normalized fixed-sum matrix `A_n` and iid Bernoulli comparator `G_n`, with `d(n)->infinity`, there exists a deterministic `eta_n->0` satisfying

`eta_n d(n)^(1/4) -> infinity`                              (8.2)

such that for every compact disk `K`,

`int_K D_{eta_n}(A_n;z) d^2z + int_K D_{eta_n}(G_n;z) d^2z -> 0`   (8.3)

in probability.

Condition (8.2) makes Theorem 5.2 force the two ridge potentials together; (8.3) then removes the ridge in spatial `L^1`. Combined with the minimal-sparsity iid circular-law input, the Girko distributional identity would transfer the circular law to `A_n` under only `d->infinity`.

The cyclic-shift example proves that (8.3) **cannot** follow from Hilbert--Schmidt closeness or from positive-ridge comparison alone. A proof must exploit randomness/anti-concentration/structural properties of the row-slice ensemble.

This is now a sharper obligation than “improve the least-singular-value bound”: it allows rare bad `z`, averages over the spectral plane, and asks only for enough microscopic singular-value mass control to kill the ridge error.

## 9. Three method moves and what happened

- **B1 — CHANGE THE CATEGORY:** moved from conditioned row-by-row determinant replacement to optimal cube-to-slice transport in Hilbert--Schmidt geometry. **Succeeded** for the full-sparsity regularized problem: Theorem 5.2 works for every `d->infinity`.
- **B4 — PROVE SOMETHING WEAKER, COMPLETELY:** proved the vanishing-ridge comparison `eta=d^{-1/8}` with an explicit `O(d^{-1/8})` expectation bound, rather than claiming eigenvalue convergence. **Succeeded**, but does not move `p_comb`.
- **B18 — SAY IT IN ANOTHER LANGUAGE:** rewrote the gap as spatial Hermitization/pseudospectral de-regularization. **Succeeded in isolating the true gap**; Proposition 6.1 refutes the naive implication from ridge comparison to ESD comparison, and Section 7 shows ordinary eigenvalue-log integrability is not the missing issue.

This triple differs from the previous run's B5/B11/B28.

## 10. Why the source metric did not move

The new transport estimate removes the fixed-row-sum dependence at every positive ridge down to `eta >> d^{-1/4}`. But the circular law is a zero-ridge statement, and nonnormal rank-one perturbations show that the passage `eta->0` can carry macroscopic spectral information even when Hilbert--Schmidt distance is negligible.

Therefore it would be incorrect to change `p_comb` based on Theorem 5.2. The metric remains exactly as stated in Section 2.

## 11. Next mathematical checkpoint

Do **not** return to another simultaneous-row union bound. The next run should attack Missing Lemma M directly, with a different B-triple. Three concrete possibilities are:

1. derive an averaged-in-`z` small-singular-value counting bound from row-slice anti-concentration rather than a pointwise `s_min` estimate;
2. randomize the spectral shift at a mesoscopic scale and seek a Wegner-type bound for the Hermitized matrix;
3. use the slice-to-cube coupling together with a replacement/Lindeberg estimate for the Stieltjes transform of the Hermitization, but at an `eta` that still satisfies (8.2).

The decisive quantity is the spatial integral in (8.3), not another finite-size singularity experiment.

## 12. Runtime capability honesty

The requested model is GPT-6 at maximum reasoning. The runtime actually identified this execution as **GPT-5.6 Sol**; no reasoning-effort telemetry was exposed, so the reasoning level is **UNVERIFIED**. The available scheduler mutation interface exposes title, prompt, schedule/timing mode, and enabled state, but no model selector, no reasoning-effort selector, and no guaranteed execution duration. Therefore GPT-6 maximum remains prompt-requested only. Changing that requires platform support or a scheduler/runtime surface that actually exposes model and reasoning selectors; a repository edit cannot do it.

The controlling policy records an earlier native error `You cannot modify this task` for P26/P01/P03 in one context. I did not probe or modify any scheduler in this run because this worker is expressly forbidden to alter other schedules. The authorized workaround remains to use the task/account/workspace context that owns the native job, or platform support; do not bypass the restriction by creating a duplicate schedule.

## 13. Ledger delta for coordinator consumption

No shared root was edited by HARD7-02. Suggested coordinator delta:

`HARD7-02 | Li--Litvak--Yu Conjecture 3.9, row-combinatorial circular law | source-verified p_comb<=2 unchanged; in-track p_comb<=1 candidate unchanged/pending validation | PARTIAL / SOURCE OPEN | auxiliary: cube-to-slice transport gives uniform ridge-potential comparison for every d->infinity at eta=d^(-1/8); exact remaining lemma is spatial pseudospectral de-regularization`
