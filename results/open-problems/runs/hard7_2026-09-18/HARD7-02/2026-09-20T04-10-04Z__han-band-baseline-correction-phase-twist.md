Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **NO NEW SOURCE-THEOREM MOVEMENT. A source-baseline error was found and corrected: the repository's recorded `beta_band <= 8/9` is not certified for Rademacher atoms because Han, arXiv:2410.16457v3, Theorem 1.5(2), assumes bounded density. The currently verified theorem for the exact periodic hard-cutoff Rademacher model is Han, arXiv:2508.18143v3 (12 September 2026), Theorem 1.12, giving `beta_band <= gamma_* := log_2(5)/(log_2(5)+1/5) = 0.920695597782722...`. This is a correction of evidence, not a worsening of the unknown mathematical truth. Methods tried: B14 / B24 / B25. New mathematics: cyclic-cut/gauge symmetries are proved to preserve the physical resonance exactly; the exponent `R^5` in the bare separator Schur recursion is proved sharp by an exact 2x2 family; and a deterministic phase-twist theorem gives `\int (-log|det(I-e^{it}P)|)_+ dt/(2pi) <= d log 2` plus exact exterior-degree Parseval.**

# HARD7-02 — STUCK1 recovery: correct the discrete baseline, prove the Schur exponent is genuinely sharp, and isolate a twist-transfer route

Status: **PARTIAL / SOURCE OPEN / STUCK1 recovery run.**  One Section-I recovery has been consumed.  No closure, no independent audit, and no source-level exponent improvement are claimed.

## 1. Continuity, ownership, exclusions, and evidence consumed

This run resumes the active exclusive claim

`operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`

and the immediately preceding checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-20T03-12-25Z__han-band-stuck1-monodromy-resonance.md`.

The previous run triggered STUCK1 after the third unchanged attempt and selected exactly one recovery action: keep the frozen model and try to improve the power threshold, with the concrete milestone `beta_band <= 7/8`, using B14/B24/B25 next.  I preserve that recovery rather than restarting the target.

I re-read the controlling files and current repository state required by the contract:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the active Han claim and the complete newest HARD7-02 STUCK1 report;
- the nearby non-Hermitian/heavy-tail ownership material, in particular the C0031 handoff `research7_2026-09-17/R7-05/handoffs/2026-09-19T032418Z__C0031_sixrun_handoff.md`, which is a different heavy-tailed iid almost-sure-convergence question and is not an alias of this target;
- repository searches for periodic-band/Rademacher/circular-law aliases and the relevant intake material.

No peer claim was overwritten and no shared root ledger was edited.  The target remains distinct from the author's excluded least-singular-value, Gaussian row-submatrix, Toeplitz/Hankel, additive-spike and gated-product manuscripts and from Bernoulli/sign-matrix singularity targets.

## 2. Current-source audit: the recorded 8/9 Rademacher baseline was wrong

This run rechecked the **full theorem statements**, not just abstracts.  That changes the certified baseline.

### 2.1 Han 2024/2026 general-profile theorem does not certify Rademacher at 8/9

Current source:

Yi Han, *The circular law for random band matrices with arbitrary doubly stochastic variance profiles*, arXiv:2410.16457v3, revised **8 August 2026**,
https://arxiv.org/abs/2410.16457v3 .

Its abstract says `gamma>8/9` for subgaussian entries, but the actual Theorem 1.5(2) additionally assumes that the real atom has a **distributional density bounded by L** (or, in the complex case, bounded densities for the real and imaginary parts).  Symmetric Rademacher has no density.  Therefore the sentence in the HARD7-02 claim saying that this theorem "includes this normalized Rademacher hard-indicator profile" is false.

This is an applicability error, not a disagreement about a constant.  The 8/9 theorem cannot be retained as evidence for the frozen discrete model.

### 2.2 A newer revision directly covers the exact frozen Rademacher strip, but at exponent 0.920695...

Current source:

Yi Han, *The circular law for non-Hermitian random band matrices up to bandwidth N^{2/3+c}*, arXiv:2508.18143v3, revised **12 September 2026**,
https://arxiv.org/abs/2508.18143v3 .

This revision postdates the 8 September revision of the primary Han-2026 source used at admission and must be consumed as a current follow-up.  It also explicitly withdraws the older `N^{1/2+c}` proof from v2 because of a sign error in the fine local-law argument.

Assumption 1.8 defines periodic scalar strips with weights `p_{N,s}`.  For `q=1`, it is exactly a flat hard cutoff.  Indeed its condition says

`p_{N,s}=a_N/W` for every `|s|<=W`, and `sum_{s=-W}^W p_{N,s}=1`.

Hence necessarily

`a_N = W/(2W+1)` and `p_{N,s}=1/(2W+1)`.

With the real atom `xi=+-1`, its matrix entry is therefore exactly

`xi/sqrt(2W+1)`,

with the same cyclic support and normalization frozen in the HARD7-02 claim.

Theorem 1.12 sets

`nu_q = q log_2 5`,

and, when `E xi^3=0`,

`alpha=1/5`, `gamma_{q,alpha}=nu_q/(nu_q+alpha)`.

Rademacher has zero third moment.  Thus for `q=1` the exact proved threshold is

`gamma_* = log_2(5)/(log_2(5)+1/5) = 0.920695597782722...`,

and every fixed `gamma>gamma_*` is proved to give the circular law.  The paper rounds this in its introduction to the convenient sufficient condition `W >= N^0.93`.

Consequently the **currently source-certified upper bound for the exact frozen metric is**

`beta_band <= gamma_* = 0.920695597782722...`.

The primary September paper, arXiv:2609.01295v2, still formulates `W_N -> infinity` as the universality conjecture, proves the optimal growing-band result for bounded-density scalar profiles, and proves `W_N >> log N` without density only for the different periodic full-block model.  A bounded 20 September 2026 search of these papers and current arXiv aliases found no theorem with a smaller certified exponent for the exact scalar hard-cutoff Rademacher model.  This is bounded negative evidence, not a worldwide novelty certificate.

### 2.3 Correct before/after accounting

The mathematical quantity `beta_band` itself has not been shown to increase.  What changed is our **certificate**.

- repository record before this run: `beta_band <= 8/9 = 0.888888...`;
- audit verdict on that record: **UNSUPPORTED for Rademacher** because the cited theorem requires bounded density;
- source-certified bound after this run: `beta_band <= gamma_* = 0.920695597782722...` from arXiv:2508.18143v3, Theorem 1.12;
- conjectural source target: `beta_band=0`;
- STUCK1 recovery milestone remains `beta_band <= 7/8=0.875`;
- correctly measured certified gap from the present theorem to that milestone is `gamma_*-7/8 = 0.045695597782722...`.

The previous apparent gap `8/9-7/8=1/72` was based on a theorem that did not apply to the atom distribution.  I do **not** call this correction a negative theorem or infer that `gamma_*` is necessary.

## 3. Idea before code

The current v3 theorem reveals exactly where its discrete exponent comes from.  For `q=1`, Han's separator tree uses a local deformed-iid inverse lemma with a **cubic** dependence on the deformation norm.  A child inverse scale `R`, followed by the Schur complement and the two exterior block-inverse factors, produces a parent scale `R^5`.  Balanced bisection has height `log_2(N/W)`, hence the exponent `nu_1=log_2 5`.  Combining that least-singular-value floor with the coarse singular-value count at scale `W^{-1/5}` gives `gamma_*`.

There are therefore two logically different ways forward:

1. improve the separator recursion itself; or
2. bypass physical-boundary resonance by exploiting the compatible transfer structure isolated in STUCK1.

B24 below proves that route (1) **cannot** improve merely by sharpening the deterministic block-inverse norm algebra: the fifth power is exactly attainable already in dimension two.  B14 then shows that the obvious cut/gauge symmetries do not randomize the bad eigenangle.  B25 supplies a different positive fact: if one is allowed to vary the scalar boundary twist, the whole cross-degree cancellation problem has a universal `O(W)` negative-log bound.  Thus the new missing mechanism is no longer "some better norm inequality"; it is a **stochastic transfer from a good twist to the physical twist**.

Only after those mathematical steps did I write the small exact checker for the finite 2x2 obstruction.

## 4. B14 — find the group acting: cut rotation is conjugacy, so it cannot cure resonance

Let `T_i` be the invertible scalar companion transfer matrices around the periodic ring.  Endpoint Rademacher coefficients are nonzero, so the transfer matrices are invertible.  Extend them periodically, `T_{i+N}=T_i`, and define the monodromy based at cut `k` by

`P_k = T_{k+N-1} T_{k+N-2} ... T_k`.

Then

`P_{k+1} = T_k P_k T_k^{-1}`.

Indeed write `P_k = Q_k T_k`, where `Q_k=T_{k+N-1}...T_{k+1}`.  Periodicity gives `P_{k+1}=T_{k+N}Q_k=T_kQ_k=T_kP_kT_k^{-1}`.

Therefore every cyclic change of the cut acts on the monodromy by conjugation, and in particular

`det(I-P_{k+1})=det(I-P_k)`.

The same is true for periodic changes of transfer-state gauge: a gauge `v_i -> G_i v_i` with `G_{i+N}=G_i` changes each transfer to `G_{i+1}T_iG_i^{-1}`, hence changes the full monodromy by conjugation.

**Consequence.** The large obvious symmetry group of the ring does not spread the physical resonance over different phases.  `det(I-P)` is a class function for these actions.  Randomizing the cut, or rephrasing the recurrence in a different periodic gauge, leaves the exact bad quantity unchanged.

There is a genuinely different `U(1)` operation: impose a twisted boundary condition `v_{N}=omega v_0`, `|omega|=1`.  Then the closure condition is

`det(omega I-P)=0`

(up to the harmless scalar normalization already isolated in STUCK1).  But varying `omega` is **not** a law-preserving symmetry of a real Rademacher ring: implementing a general complex twist in the wrap couplings multiplies signs by complex phases.  Only special real sign operations preserve the entry law, and periodic ones reduce to the conjugacies above.

**B14 outcome:** cut/gauge symmetry is an exact dead end for anti-resonance, but it identifies the right extra parameter: a nonphysical scalar boundary twist.

## 5. B24 — find the extremal object: the `R^5` separator loss is sharp from deterministic Schur data

Han v3, Section 5, obtains for `q=1` the schematic parent recursion

`R_parent <= N^C R^5`.

It is tempting to try to improve the exponent five by a more careful use of the block inverse formula.  That cannot work if one uses only the same deterministic information about the child inverse, the Schur inverse, and polynomial coupling norms.

For any real `R>1`, consider the exact `2 x 2` matrix

`M_R = [[R^{-1}, 1], [1, R+R^{-3}]]`.

Take the upper-left block as `A=R^{-1}`, and `B=C=1`.  Its Schur complement is

`S = (R+R^{-3}) - C A^{-1} B = R^{-3}`.

Thus

`||A^{-1}||=R`, `||S^{-1}||=R^3`, and the two couplings have norm one.

Direct inversion gives

`M_R^{-1} = [[R^5+R, -R^4], [-R^4, R^3]]`.

Hence

`||M_R^{-1}|| >= R^5+R`.

So the fifth power is not an artifact of applying triangle inequalities twice: it is exactly realizable under the bare deterministic Schur hypotheses.  A recursion improvement must exploit **additional stochastic or structural information** about the Rademacher coupling blocks or must improve the local deformed-iid dependence before the Schur reconstruction.

A second extremal diagnostic applies to the transfer route.  Singular-value or exterior-norm information alone cannot control physical resonance: `P=I_d` has `|det P|=1` and every singular value equal to one, yet

`det(I-P)=0`.

This is only a deterministic obstruction, not a claim that `P=I_d` occurs with positive probability for generic spectral parameter `z`.  It shows why the STUCK1 norm/Pluecker refresh theorems cannot by themselves prove anti-resonance.

### Exact finite verification

The 2x2 identities were checked symbolically over `Q(R)` in

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T04-10-04Z__separator-r5-sharpness-check.py`

and the executed output is archived in

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-20T04-10-04Z__separator-r5-sharpness-check.out`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

These are self-checks, not independent audits.

**B24 outcome:** optimizing the deterministic block inverse cannot lower Han's factor `5`; the next improvement must use randomness/phase rather than more careful norm bookkeeping.

## 6. B25 — count the same thing twice: phase averaging removes all exterior-degree cancellation

The compatible closure from STUCK1 is

`det(I-P) = sum_{r=0}^d (-1)^r tr(wedge^r P)`.

Introduce a scalar boundary phase `omega=e^{it}` and set

`F_P(omega)=det(I-omega P)`.

Then the exterior-power identity gives the exact Fourier polynomial

`F_P(omega)=sum_{r=0}^d (-omega)^r tr(wedge^r P)`.

Therefore Parseval gives

`(1/(2pi)) integral_0^{2pi} |F_P(e^{it})|^2 dt = sum_{r=0}^d |tr(wedge^r P)|^2`.       (6.1)

This is the desired degree-compatible orthogonalization: every cancellation between different exterior degrees disappears after phase averaging.

More importantly, there is a universal **negative-log** estimate which does not use a norm bound on `P`.

### Lemma 6.1 — universal twisted-boundary anti-resonance

For every complex `d x d` matrix `P`,

`(1/(2pi)) integral_0^{2pi} (-log |det(I-e^{it}P)|)_+ dt <= d log 2`.       (6.2)

Consequently, for every `a>0`,

`Leb{t in [0,2pi]: |det(I-e^{it}P)| <= e^{-ad}}/(2pi) <= (log 2)/a`,       (6.3)

and there exists at least one phase `t` such that

`|det(I-e^{it}P)| >= 2^{-d}`.       (6.4)

#### Proof

Let `lambda_1,...,lambda_d` be the eigenvalues of `P`, with algebraic multiplicity.  Then

`det(I-e^{it}P)=product_j (1-e^{it}lambda_j)`.

For one complex number `lambda`, rotate `t` and put `r=|lambda|`.  Define

`g_r(t)=(-log|1-r e^{it}|)_+`.

If `r>=2`, then `|1-r e^{it}|>=r-1>=1`, so `g_r=0`.

If `0<=r<=1/2`, then `|1-r e^{it}|>=1-r>=1/2`, hence `g_r(t)<=log 2` pointwise.

If `1/2<=r<=2`, then

`|1-r e^{it}|^2=(1-r)^2+4r sin^2(t/2) >= 2 sin^2(t/2)`.

Because `|sin(t/2)|<=1`, monotonicity of the positive part gives

`g_r(t) <= -log|sin(t/2)|`.

The classical elementary integral

`(1/(2pi)) integral_0^{2pi} -log|sin(t/2)| dt = log 2`

therefore proves, uniformly in `lambda`,

`(1/(2pi)) integral g_r(t) dt <= log 2`.

Finally,

`(-log product_j |1-e^{it}lambda_j|)_+ <= sum_j (-log|1-e^{it}lambda_j|)_+`.

Integrating proves (6.2).  Markov's inequality gives (6.3), and (6.4) follows from the mean bound.  QED.

### Source relevance

For the scalar band transfer problem, `d=2W`.  Thus **some boundary twist always has negative-log cost at most `2W log 2`**, much smaller than the `O(W log W)` scale isolated in STUCK1.  This theorem is deterministic and survives arbitrarily nonnormal `P`.

However, it does not solve the source problem because the physical periodic ring is the single phase `omega=1`.  The extremizer `P=I_d` shows no deterministic inequality can compare that phase to the phase average.  B14 shows that changing the cyclic cut or periodic gauge also cannot perform the comparison, because those operations only conjugate `P`.

Thus the exact missing statement has become sharply localized:

> **Twist-transfer problem.** For the *actual annealed Rademacher companion-product law* and for Lebesgue-a.e. fixed spectral shift `z`, prove that the physical phase `omega=1` is not exponentially more resonant than a typical scalar boundary twist, at a logarithmic cost small enough for the circular-law replacement argument.

A uniform deterministic-outside version is already ruled out by the archived `W=1` counterexample.  Any valid theorem must exploit the law of the outside product, additional fresh signs, or a typical-outside exceptional-set estimate.

The phase lemma itself is elementary (essentially a one-variable logarithmic-integrability/Jensen observation), and I make **no novelty claim** for it.  Its value here is that it exactly diagonalizes the exterior-degree cancellation identified in STUCK1 and proves that only the physical-twist transfer remains.

**B25 outcome:** positive structural progress, but not a source exponent improvement.

## 7. What the newer separator theorem says about the recovery target

Han v3 makes the source-relevant numerical bottleneck transparent.  For Rademacher `q=1`, its least-singular-value exponent has

`Theta = (N/W)^{log_2 5} log N`.

The moment-comparison/coarse-count theorem reaches scale `W^{-1/5}`.  Requiring

`W^{-1/5} Theta -> 0`

is exactly what produces

`gamma > log_2 5/(log_2 5+1/5)`.

The B24 example proves that replacing `5` by a smaller number cannot come solely from deterministic Schur algebra.  More generally, if a future local deformed-iid theorem changed the cubic deformation loss `R^3` to `R^p` while all other bookkeeping remained identical, the same tree would have factor `lambda=p+2` and the formal threshold

`gamma(p)=log_2(p+2)/(log_2(p+2)+1/5)`.

For orientation only:

- `p=3` gives the proved `0.9206955977...`;
- `p=2` would give `10/11 = 0.909090...`;
- `p=1` would give `0.8879528...`, just below `8/9`;
- reaching the chosen `7/8` milestone **through this same coarse-count/tree architecture alone** would require `p <= 2^{7/5}-2 = 0.6390158...`.

These are conditional algebraic consequences, not new circular-law theorems and not claims that such a local exponent is possible.  They show quantitatively that the `7/8` recovery target is unlikely to come from a cosmetic improvement of the separator proof; it needs a qualitatively different mechanism such as phase/twist transfer, a stronger coarse-count scale, or stochastic cancellation inside the Schur reconstruction.

## 8. Negation tests performed this run

The owner requires trying to refute the proposed route before promoting it.

1. **Can cyclic cut randomization supply phase averaging?** No.  B14 proves all cut monodromies are conjugate, so `det(I-P)` is identical at every cut.
2. **Can a sharper deterministic block inverse lower the `R^5` recursion?** No.  B24 gives an exact 2x2 family attaining `R^5+R` in the inverse while the child and Schur scales are exactly `R` and `R^3`.
3. **Does phase averaging itself control the physical phase?** No.  `P=I_d` has perfect singular-value conditioning and satisfies the phase-average theorem, but the physical determinant is exactly zero.  The bridge must be probabilistic and source-specific.

These failures are informative: they exclude three tempting but false shortcuts without spending the run on another certificate for an unchanged exponent.

## 9. Remaining full-scope gap and next method change

The exact source remains

`W_N -> infinity  ==>  mu_{X_N} => mu_circ in probability`

for the frozen periodic hard-cutoff Rademacher model.

No theorem in this run lowers the current valid exponent `gamma_*`.  The remaining proof obligation can now be stated in two equivalent research languages:

1. **separator language:** exploit Rademacher randomness beyond worst-case Schur norm data strongly enough to reduce the accumulated inverse floor and then combine it with the coarse count; or
2. **transfer language:** prove an annealed physical-twist anti-resonance estimate for `det(I-P)` by transferring the universal good-twist bound (6.2) to `omega=1` for the actual random companion-product law.

The second route is genuinely different from the retired generic smoothing/norm-refresh attacks.

The next nonrepeating Section-B triple is **B9 / B20 / B28**:

- **B9 RANDOMIZE:** introduce an auxiliary scalar boundary twist and seek a coupling/exposure scheme in which a genuinely fresh Rademacher packet makes the physical phase statistically typical rather than deterministically worst-case;
- **B20 FIND WHY THE ALGORITHM FAILS:** locate the minimal fresh-sign configuration for which the good-twist-to-physical-twist comparison fails, rather than redoing a full Fock estimate;
- **B28 REPLACE FOR ALL WITH TYPICAL:** the circular-law proof needs a.e. fixed `z`, so seek a typical-outside / typical-`z` twist-transfer theorem rather than the already-false uniform deterministic-frame statement.

No rotation is made.  This is the first recovery run after STUCK1, and the source/baseline correction materially changes the quantitative obstruction.  A second Section-I recovery remains available under the controlling policy; a third stuck episode would require a terminal handoff and fresh target.

## 10. Runtime / scheduler capability honesty

GPT-6 maximum remains prompt-requested only.  The exposed automation interface in this run provides schedule/prompt/title/enabled/timing controls but no binding model selector and no reasoning-effort selector, and no authenticated maximum-effort telemetry was available.  Therefore the reasoning level is reported as `UNVERIFIED`.

`operations/NEW_METHODS_2026-09-16.md` records historical native-edit denials such as `You cannot modify this task`; the compliant workaround is an authorized owner/workspace scheduler context or platform support, not a duplicate task or permission bypass.  The current root `RESULTS.md` additionally records that P26 was later successfully updated in another authorized exposed context, so the historical P26 denial is not evidence that P26 is presently immutable everywhere.  No scheduler probe or mutation was made in this research run.

## 11. Validation actually performed

Mathematical checks performed:

1. full theorem-scope check of arXiv:2410.16457v3 Theorem 1.5(2), detecting the bounded-density hypothesis that invalidates the old Rademacher 8/9 baseline;
2. exact normalization match from arXiv:2508.18143v3 Assumption 1.8 with `q=1` to the frozen `1/sqrt(2W+1)` Rademacher model;
3. exact extraction of Theorem 1.12's Rademacher exponent `gamma_*`;
4. exact conjugacy proof for cut-rotated monodromies;
5. exact symbolic 2x2 Schur-complement obstruction, executed and archived, ending `ALL_EXACT_CHECKS_PASS = True`;
6. complete on-page proof of the phase-averaged negative-log determinant bound and its tail/existence corollaries;
7. exact Fourier/exterior Parseval identity (6.1).

No finite simulation is used as asymptotic evidence.  The 2x2 checker is a finite self-check only.  No source closure or novelty certification is claimed.

## 12. Source-level before/after and ledger delta

`ledger_delta`:

- track: `HARD7-02`
- target: Han periodic scalar hard-cutoff Rademacher circular law
- canonical claim: `operations/claims/HAN-2026-PERIODIC-RADEMACHER-BAND-CIRCULAR-LAW.md`
- metric: `beta_band`
- before, as recorded: `beta_band <= 8/9`
- source audit of before-value: **INVALID / unsupported for Rademacher**; cited Theorem 1.5(2) requires bounded density
- corrected verified literature bound: `beta_band <= gamma_* = log_2(5)/(log_2(5)+1/5) = 0.920695597782722...`
- source theorem movement produced by this run: **NONE**
- evidence correction: **YES, material**
- status: **PARTIAL / SOURCE OPEN / STUCK1 recovery in progress**
- methods: `B14`, `B24`, `B25`
- new auxiliary theorem: phase-twist averaged anti-resonance `average_t (-log|det(I-e^{it}P)|)_+ <= d log 2`
- new obstruction: cyclic cut/gauge actions only conjugate monodromy and cannot randomize the physical resonance
- new exact sharpness result: the bare child-`R`, Schur-`R^3` block hypotheses can force full inverse scale `R^5+R`; deterministic separator exponent five is genuinely sharp
- recovery milestone: `beta_band <= 7/8` remains unproved
- remaining full-scope gap: source-specific stochastic twist transfer or another mechanism that beats both the sharp worst-case Schur recursion and the physical eigenangle resonance
- next methods: `B9 / B20 / B28`

Artifacts:

- checker creation commit: `d9c94e176696db812206ae0113917bf7a99843af`
- checker-output creation commit: `fa14d330e8f0fd43408a1041cdc86d721432399f`

No email, Drive, public posting, scheduler modification, permission change, workflow execution, force push, peer-file edit, or shared-root ledger mutation occurred.
