Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO MOVEMENT in the frozen source metric: `beta_band <= 8/9 -> beta_band <= 8/9`. This is the mandatory first Section-I stuck run on the fresh Han-2026 target. Methods tried: B5 / B13 / B18. New mathematical diagnosis: fixed-degree exterior packets can be refreshed/steered at only `O(W log W)` logarithmic cost, so the real unpaid debt is not norm survival but quantitative anti-resonance of the compatible scalar monodromy at eigenvalue `1`, equivalently a lower-tail bound for `det(I-P)`.**

# HARD7-02 — STUCK1: smoothing cannot cross the discrete endpoint; exterior packet refresh; compatible closure = monodromy anti-resonance

Status: **PARTIAL / SOURCE OPEN / STUCK1 on the active Han-2026 periodic scalar Rademacher target.**

## 1. Continuity, ownership, exclusions, and evidence consumed

This run resumes, without resetting, the exclusive target in

`operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`

and the immediately preceding checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-20T02-14-29Z__periodic-rademacher-fourier-annealed-closure.md`

at commit `6b3f65098e70381f385085a15b6d4026d480ef6d`.

I re-read the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the active claim above;
- the newest HARD7-02 report and the neighboring circular-law / non-Hermitian searches, including the distinct C0031/C0032 heavy-tailed circular-law tracks;
- the relevant probability-intake search, which recovers the Bordenave--Chafaï circular-law intake material and confirms that C0031/C0032 are different heavy-tailed questions rather than aliases of this periodic discrete-band target.

The exact Han target remains owned by HARD7-02. No peer claim, root shared ledger, peer artifact, workflow, permission, schedule, Gmail item, Drive item, or public posting was modified.

The target remains outside the author's excluded least-singular-value, Gaussian row-submatrix, Toeplitz/Hankel, additive-spike, gated-product, and Bernoulli-singularity work.

### Bounded current-literature refresh, 20 September 2026

A fresh arXiv-bounded search again recovered:

1. Yi Han, *The circular law for non-Hermitian random band matrices: optimal bandwidth, periodic profile and discrete law*, arXiv:2609.01295v2, revised 8 September 2026, https://arxiv.org/abs/2609.01295 . It states the universality conjecture `W_N -> infinity`; for the scalar periodic hard-indicator model the optimal theorem uses bounded density, while the density-free discrete result is for the periodic **full-block** model with `W_N >> log N`.
2. Yi Han, *The circular law for non-Hermitian random band matrices up to bandwidth N^{1/2+c}*, arXiv:2508.18143, https://arxiv.org/abs/2508.18143 . Its scalar improvement assumes bounded density; the block exception is different.
3. Yi Han, *Invertibility for non-Hermitian and symmetric random band matrices with sublinear bandwidth and discrete entries*, arXiv:2507.05417, https://arxiv.org/abs/2507.05417 . Its `alpha>2/3` theorem is an unshifted discrete invertibility result, not the fixed-complex-shift logarithmic integrability needed for the circular law.
4. Han's earlier general-profile subgaussian circular-law result, arXiv:2410.16457, remains the verified `gamma>8/9` scalar Rademacher baseline used by the claim.

The bounded search found no later source closing the frozen scalar periodic Rademacher `W_N -> infinity` case and no theorem lowering its rigorously verified exponent below `8/9`. This is bounded negative evidence, not a worldwide novelty claim.

The runtime/configuration situation is unchanged: GPT-6/maximum is prompt-requested only. The exposed scheduler controls do not bind a model selector or reasoning-effort selector and expose no authenticated maximum-effort telemetry. Historical policy records task-edit failures such as `You cannot modify this task`; the compliant remedy is the authorized owner/workspace context or platform support, not a duplicate task or bypass. No scheduler mutation was attempted.

## 2. Frozen model and source metric

Let `d=2W`, `L=2W+1`, indices lie in `Z/NZ`, and

`X(i,j)=epsilon_ij/sqrt(L)` if `dist_N(i,j)<=W`,

`X(i,j)=0` otherwise,

with independent symmetric Rademacher `epsilon_ij`.

The source target is

`W_N -> infinity  ==>  mu_{X_N} => mu_circ in probability`.

The frozen quantity is

`beta_band = inf { beta in [0,1] : for every eps>0, the frozen circular law is rigorously known whenever W_N >= N^(beta+eps) eventually }`.

Verified baseline at admission: `beta_band <= 8/9`.

**Before this run:** `beta_band <= 8/9`.

**After this run:** `beta_band <= 8/9`.

**Movement:** none.

This is the third consecutive unchanged run on this newly admitted target, so Section I is triggered now. The auxiliary algebra below is not relabeled as source-threshold movement.

## 3. Idea before code

The previous run showed two apparently conflicting facts:

- fresh Rademacher transfer blocks have strong `L^2` observability and deterministic one-row conditioning;
- the bounded-density proof's uniform arbitrary-frame logarithmic closure is literally false for Rademacher rows, already at `W=1`.

It also found a scalar record-refresh mechanism. The first question this run is therefore not another small-ball lemma. It is:

> Is the obstruction really projective/norm alignment, or does it survive after one upgrades the refresh mechanism to every exterior degree?

The answer of B13 below is useful: **for every fixed exterior degree, a chosen Plücker coefficient can be driven to a canonical top-packed coordinate in at most `r<=2W` rows with probability at least `2^{-r}`, losing only the unavoidable denominator factor `L^{-r/2}`.** Thus a fixed-degree packet costs only `O(W log W)` in logarithmic scale, which is of the right order for Han's interface bookkeeping.

The remaining obstruction appears only when one recombines all exterior degrees. B18 makes this exact: for the **actual compatible** outside family the alternating Fock trace is simply `det(I-P)` for the scalar companion monodromy `P`. The missing inequality is therefore an anti-resonance statement near eigenvalue `1`, not a generic norm-survival statement.

No code is needed for this Section-I thinking run; the new statements are algebraic and proved on the page. The prior exact `W=1` checker remains evidence for the already-recorded arbitrary-frame obstruction and was not rerun merely to generate another receipt.

## 4. B5 — add a parameter and differentiate/deform: Gaussian smoothing hits a genuine endpoint wall

Let `G_N` have independent standard real Gaussians on the same periodic band support, independent of the Rademacher matrix `X_N`, and set for `delta>0`

`X_N(delta) = (X_N + delta G_N)/sqrt(1+delta^2)`.

For every fixed `delta>0`, each nonzero atom has a bounded density and finite moments. Han's 2026 scalar hard-indicator theorem therefore puts `X_N(delta)` in the optimal `W_N -> infinity` circular-law regime.

The tempting deformation is `delta downarrow 0`. Two independent obstructions prevent this from proving the discrete endpoint.

### 4.1 The source theorem is not uniform in `delta`

The one-dimensional atom density has supremum of order `delta^{-1}`. The bounded-density transfer/small-ball constants are therefore allowed to diverge as `delta->0`. The source theorem for each fixed positive `delta` supplies no estimate uniform enough to choose `delta=delta_N->0` while retaining the needed logarithmic singular-value control.

This is not a cosmetic bookkeeping issue: the disappearing Gaussian density is exactly the regularity used to rule out the discrete cancellation found in the prior `W=1` example.

### 4.2 Tiny perturbation does not control a nonnormal ESD

There is no general continuity principle that transfers the eigenvalue empirical measure of a highly nonnormal matrix through an arbitrarily small perturbation. A deterministic exact model shows why. Let `J_N` be the nilpotent Jordan shift and

`A_N = J_N + eta_N e_N e_1^T`.

Then `J_N` has every eigenvalue equal to `0`, while

`det(lambda I-A_N)=lambda^N-eta_N`,

so the eigenvalues of `A_N` are the `N` roots of `eta_N`, all on the circle of radius `eta_N^(1/N)`. Choosing `eta_N=exp(-sqrt(N))` gives `||A_N-J_N||=eta_N->0` but `eta_N^(1/N)=exp(-1/sqrt(N))->1`; the two ESDs have macroscopically different limits.

Thus a smoothing proof would still have to compare logarithmic potentials, i.e. prove for a.e. fixed `z` a uniform-integrability statement of the form

`(1/N) log|det(X_N(delta_N)-z)| - (1/N) log|det(X_N-z)| -> 0`,

with `delta_N->0`. That comparison is itself a least-singular-value / negative-log problem of the same type we are trying to solve.

**B5 outcome:** the deformation gives no endpoint theorem. The failure is structural, not just a missing rate in an otherwise continuous argument.

## 5. B13 — find what only increases: an exterior packet staircase refresh

This attack upgrades the scalar record-refresh lemma from the previous run to every fixed exterior degree.

Use the denominator-normalized scalar companion transfer

`T = S - e_d q^T`,

where `S e_1=0`, `S e_j=e_{j-1}` for `j>=2`. For the hard-indicator Rademacher row, after conditioning on the endpoint denominator sign and all numerator signs except one chosen numerator sign, the corresponding coordinate `q_j` is an affine function of one fresh symmetric sign with coefficient of modulus one. This remains true for the coordinate containing the spectral shift `z`: the deterministic `-z sqrt(L)` part is absorbed into the conditioned constant term.

For an `r`-subset

`J={j_1<...<j_r} subset {1,...,d}`

define the staircase map

`R(J) = {j_2-1,...,j_r-1,d}`.

(The displayed set is understood in increasing order; when `r=1` it is `{d}`.)

### Lemma 5.1 — one-step exterior refresh

Let `v=sum_J v_J e_J` be any past-measurable vector in `wedge^r C^d`, and fix an index set `J={j_1<...<j_r}`. For one fresh Rademacher transfer row,

`P( |(wedge^r T v)_{R(J)}| >= |v_J|  | past ) >= 1/2`.

#### Proof

In

`T e_{j_1} wedge ... wedge T e_{j_r}`,

the contribution obtained by taking the `-q_{j_1} e_d` term from `T e_{j_1}` and the shift terms `e_{j_k-1}` from all `k>=2` lands in the basis coordinate `R(J)` with coefficient `+- q_{j_1} v_J`.

Condition on every fresh row sign except the numerator sign entering `q_{j_1}`. Every other contribution to the same output coordinate becomes a fixed complex number `a`, while the unconditioned sign contributes `+- epsilon v_J` with a coefficient of modulus one. Hence the output coordinate has the form

`a + epsilon b`, with `|b|=|v_J|`.

The parallelogram identity gives

`(|a+b|^2+|a-b|^2)/2 = |a|^2+|b|^2`,

so at least one of the two equiprobable signs has modulus at least `|b|=|v_J|`. `QED`

### Lemma 5.2 — the staircase reaches the top-packed Plücker coordinate in at most `r` successful rows

Let

`J_*^(r)={d-r+1,...,d}`.

For `0<=k<r`, direct induction gives

`R^k(J) = {j_{k+1}-k,...,j_r-k,d-k+1,...,d}`,

and therefore

`R^r(J)=J_*^(r)`.

Moreover the integer potential

`Phi(J)=sum_{j in J} j`

satisfies

`Phi(R(J))-Phi(J)=d-r+1-j_1 >=0`.

Equality occurs exactly when `J` is already top-packed at its left edge; iterating `R` reaches the unique maximum `J_*^(r)`.

Combining Lemma 5.1 through `r` independent fresh rows and using the tower property yields

`P( |(wedge^r T_r ... wedge^r T_1 v)_{J_*^(r)}| >= |v_J| | past ) >= 2^{-r}`.

For the denominator-cleared matrices of Han's Fock transfer,

`A_i^(r)=beta_i wedge^r T_i`, `|beta_i|=L^{-1/2}`,

so on the same event

`|(A_r^(r)...A_1^(r)v)_{J_*^(r)}| >= L^{-r/2}|v_J|`.

Since `r<=d=2W`, the probability cost is at most `r log 2=O(W)` and the amplitude cost is at most `(r/2)log L=O(W log W)`.

### What this does and does not buy

This is a fixed-degree packet theorem, not a circular-law theorem. It shows that the scalar B19 refresh was not a one-dimensional accident: **within any one exterior degree, there is an explicit monovariant staircase and a canonical packet can be refreshed at the correct logarithmic cost scale.**

It does **not** control the alternating sum across exterior degrees. In particular, keeping one Plücker packet alive does not stop a contribution in degree `r` from cancelling contributions in degrees `q!=r`.

**B13 outcome:** fixed-degree volume steering is no longer the leading conceptual obstruction; cross-degree spectral resonance is.

## 6. B18 — say it in another language: the compatible Fock closure is exactly `det(I-P)`

The previous report already isolated the crucial compatibility of the real outside transfer family:

`B^(r)=c_B wedge^r P_B`,

and the fresh family has the same form

`Q^(r)=c_Q wedge^r P_Q`,

with scalar factors `c_B,c_Q` independent of the exterior degree `r`.

Therefore the alternating closure is not an arbitrary sum of unrelated operators. Writing

`P=P_B P_Q`,

we have exactly

`Z_B`
` = sum_{r=0}^d (-1)^r tr(B^(r)Q^(r))`
` = c_B c_Q sum_{r=0}^d (-1)^r tr(wedge^r P)`
` = c_B c_Q det(I-P)`.

The last identity is the standard finite-dimensional exterior-power identity for the characteristic polynomial.

For the hard-indicator Rademacher row, the scalar companion matrix has

`|det T_i|=1`

because the two endpoint coefficients have equal magnitude. Hence the actual scalar monodromy satisfies

`|det P|=1`.

Thus the negative-log closure problem can be restated as a **quantitative random-product anti-resonance problem at eigenvalue `1`**:

> control the lower tail of `|det(I-P)|` for the actual product of growing-dimensional random companion matrices, with logarithmic cost `O(W log W)` on the interface scale.

Equivalently, if `lambda_1,...,lambda_d` are the eigenvalues of `P`, then

`log|det(I-P)| = sum_{j=1}^d log|1-lambda_j|`.

The one-row conditioning theorem from the previous run controls singular-value distortion of each factor, and B13 controls a fixed Plücker packet. Neither prevents an eigenvalue of the long monodromy from lying extremely close to `1`. This identifies precisely why the norm-based refresh algorithm can succeed while the determinant closure still fails.

It also explains why bounded density is so effective in Han's proof: continuous polynomial anti-concentration directly suppresses the resonance. At the Rademacher endpoint the resonance variable is arithmetic and the generic deterministic-frame statement is false.

**B18 outcome:** the missing closure is reduced to a source-compatible monodromy resonance problem, not an arbitrary Fock-frame problem. This is a change of language with a sharper target, but it does not yet lower `beta_band`.

## 7. Mandatory Section-I obstruction report

This is the third unchanged run on the active Han target. The required five-part obstruction record follows.

### (a) Exact blocking statement

A source-level improvement by the present transfer route still requires, in compatible notation, a bound of the form

`E [ ( log M_B - log |c_B c_Q det(I-P_B P_Q)| )_+ ] <= C W log(eW)`,       (OBSTRUCTION)

with `B` distributed as the actual independent outside Rademacher transfer product, `Q` the fresh interface block, and constants strong enough to feed Han's pressure-concentration and ring-replacement chain.

After factoring the harmless common scalar normalization, the essential unpaid term is a quantitative negative-log bound for

`det(I-P_B P_Q)`.

### (b) Routes tried on this exact target and why each stopped

1. **B2, attack the negation (admission run).** The hard interval support does not admit the naive tiny-support exact kernel obstruction: any nonzero kernel vector for an everywhere-nonzero in-band matrix must have support larger than `N/L`. This kills the simplest counterexample but gives no approximate-invertibility or log-integrability theorem.
2. **B6, deform from a solvable ensemble (admission run).** Continuous/Gaussian smoothing enters Han's bounded-density theory, but the constants are not uniform as the density spike diverges and nonnormal ESDs cannot be transferred by a small-norm perturbation alone.
3. **B30, localize by interface scale (admission run).** The high-band short-ring anchor is available, but the discrete scalar local comparison needed to transport it remained missing.
4. **B1, Fourier category (previous run).** Exact Walsh/HS observability gives `L^2` mass for every deterministic frame, but `L^2` mass does not control negative logarithms when exact atoms are present.
5. **B11, dualize (previous run).** It correctly replaces `sup_B` by an annealed compatible-product defect, but no quantitative entropy/negative-log estimate was obtained.
6. **B19, algorithmic scalar refresh (previous run).** A scalar record survives unless `2W` adapted failures occur, but scalar norm survival says nothing about alternating exterior-degree cancellation.
7. **B5, smoothing parameter (this run).** Fixed positive smoothing solves the wrong continuous model. Sending smoothing to zero requires precisely the missing logarithmic determinant control and is blocked by nonnormal pseudospectral instability.
8. **B13, monovariant exterior refresh (this run).** Fixed-degree Plücker packets can in fact be refreshed at `O(W log W)` logarithmic cost. This removes one suspected obstruction but still gives no control of cross-degree cancellation / monodromy resonance.
9. **B18, rewrite as monodromy resonance (this run).** The compatible closure is exactly `det(I-P)`. This sharpens the target but leaves the growing-dimensional discrete anti-resonance estimate unproved.

The exact `W=1` arbitrary-frame counterexample from the previous report remains an important negative test: one cannot retreat to a uniform deterministic-frame logarithmic closure lemma.

### (c) What a proof now has to contain that the attempted routes do not

A successful proof needs a **degree-compatible phase/angle anti-concentration mechanism** for the actual scalar monodromy. Concretely, it must show that the random product does not place too much logarithmic mass near the resonance variety

`det(I-P)=0`

at a total cost at most `O(W log W)` per interface, uniformly enough in the outside product and spectral parameter to run the pressure/replacement argument.

Norm lower bounds, fixed-degree packet refresh, and `L^2` Fourier observability are insufficient because none controls the eigenangle `1` resonance of a nonnormal product.

After that local step, the proof must still verify the discrete pressure concentration and long-ring replacement errors are `o(N)` in the desired bandwidth regime.

### (d) Simplest source-relevant special case still unproved by this track

A concrete narrower milestone, keeping **exactly** the frozen periodic scalar Rademacher model, is:

`for every eps>0, prove the circular law whenever W_N >= N^(7/8+eps)`.

This lies strictly below the verified `8/9` source baseline and would therefore produce genuine movement of `beta_band`. No theorem in this report proves it.

### (e) Nearest solved analogues and the missing ingredient

There are two nearest source analogues.

- **Same scalar geometry, continuous atoms:** Han 2026 proves the hard-indicator periodic scalar model at the optimal `W_N->infinity` threshold under bounded density. Its local polynomial small-ball input suppresses interface resonance continuously. The Rademacher endpoint lacks that density mechanism.
- **Same discrete/subgaussian atoms, different geometry:** Han 2026 proves the periodic **full-block** model for `W_N >> log N`. The block geometry provides many independent coordinates at an interface and a different anti-concentration mechanism. The scalar hard-indicator companion product has only the tightly coupled exterior/Fock structure above.

The fixed-dimensional theory of random matrix products can also control projective mixing under irreducibility/proximality hypotheses, but here the dimension `d=2W` grows and the needed constants must remain within `O(W log W)`; none of the recovered source results supplies that quantitative growing-dimensional resonance estimate.

## 8. Section-I recovery choice

Exactly one recovery action is chosen:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE from (d): target `beta_band <= 7/8` without changing the model.**

The next run should not return to generic smoothing or scalar norm refresh. It should attack the monodromy resonance directly and ask whether the high-band anchor plus an `O(W log W)` resonance estimate can already close the replacement inequalities at exponent `7/8`, before aiming at arbitrary `W->infinity`.

The next three Section-B moves are **B14 / B24 / B25**:

- B14: identify the symmetry/group action of the companion-product law and the resonance variety;
- B24: identify the extremal compatible monodromy causing the worst `det(I-P)` smallness;
- B25: double-count / orthogonalize characteristic-polynomial coefficients to turn exterior observability into a degree-compatible resonance estimate.

No target rotation is made at STUCK1. A second Section-I recovery is still permitted if required; a third stuck episode would force a handoff/rotation under the controlling policy.

## 9. Validation actually performed

No numerical or finite exhaustive experiment was used this run. This was intentionally a Section-I thinking run.

On-page checks performed:

1. exact Jordan companion determinant `det(lambda I-A_N)=lambda^N-eta_N`, showing tiny nonnormal perturbations can move the ESD macroscopically;
2. exact one-step wedge expansion giving the affine fresh-sign coefficient in Lemma 5.1;
3. exact induction formula for `R^k(J)` and the monotonicity of `Phi(J)`;
4. exact exterior identity `sum_r (-1)^r tr(wedge^r P)=det(I-P)` for the actual compatible family.

The previously archived exact `W=1` closure counterexample checker remains a self-check, not an independent audit. It was not rerun.

No finite evidence is promoted to an asymptotic theorem.

## 10. Source-level before/after and ledger delta

`ledger_delta`:

- track: `HARD7-02`
- target: Han 2026 periodic scalar hard-indicator Rademacher circular law
- claim: `operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`
- metric: `beta_band`
- before: certified `beta_band <= 8/9`
- after: certified `beta_band <= 8/9`
- movement: **NO MOVEMENT**
- unchanged streak on this target: `3` => **STUCK1 triggered**
- status: **PARTIAL / SOURCE OPEN / STUCK1 recovery selected**
- methods this run: `B5`, `B13`, `B18`
- new auxiliary progress: exact fixed-degree exterior packet staircase refresh with probability `>=2^{-r}` and amplitude loss `L^{-r/2}`; exact compatible closure identity reducing the unpaid discrete logarithmic debt to monodromy anti-resonance `det(I-P)`
- source-level theorem advance: none
- recovery choice: prove the frozen `W_N >= N^(7/8+eps)` special case, i.e. seek `beta_band <= 7/8`
- next method triple: `B14 / B24 / B25`
- remaining full-scope gap: obtain a growing-dimensional Rademacher companion-product anti-resonance bound at cost `O(W log W)`, then complete pressure concentration/ring replacement; ultimately continue from `7/8` toward the source target `beta_band=0`

No closure is claimed. No independent audit is claimed. No email, Drive, public posting, scheduler change, permission change, force push, peer-file edit, or workflow execution occurred.
