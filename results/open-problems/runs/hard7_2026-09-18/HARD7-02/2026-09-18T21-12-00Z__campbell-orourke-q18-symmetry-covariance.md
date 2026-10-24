Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; GPT-6/maximum was requested in prompt text, but no model/reasoning selector or authenticated runtime telemetry is exposed here. Movement: `S=0 -> S=3` exact transformation laws for `theta_d -> mu_{alpha,theta_d}`. Methods tried: B2, B6, B30.

# HARD7-02 run 1 — Campbell–O'Rourke Question 1.8: exact symmetry covariance and non-injectivity

Status: **PARTIAL** for Campbell–O'Rourke Question 1.8. This run proves three exact transformation laws for the limiting spectral measure and gives an explicit non-injectivity family for the map `theta_d -> mu_{alpha,theta_d}`. It does **not** classify all dependence measures and does not close Question 1.8. The neighboring tail Question 1.9 is not claimed.

## 1. Continuity, exclusions, source, ownership

I read `operations/hard7_2026-09-18/CONTROL.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, and the available neighboring HARD7 state. There was no pre-existing `runs/hard7_2026-09-18/HARD7-02/` report.

I searched repository claims and reports for Campbell, O'Rourke, heavy-tailed elliptic matrices, `theta_d`, circular/elliptic law aliases, non-Hermitian universality, and random-matrix singularity targets. No existing owner for the source question below was found. R03/F0001 Bernoulli singularity is active and excluded; owner least-singular-value/submatrix, Toeplitz/Hankel, additive-spike and related manuscripts are also excluded.

The create-only claim is

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

created at commit `07e2759d8f5e7ae2522707d9e490da404a48e5be` and read back at that commit before this report.

### Primary source

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, DOI `10.1214/22-EJP849`; arXiv:2010.01261v3 (revised 2 February 2022):

https://arxiv.org/abs/2010.01261

Section 1.3, Question 1.8 asks exactly:

> What properties of `theta_d` determine `mu_{alpha,theta_d}`?

Theorem 1.6 in the source is already proved: under Condition C2, the empirical spectral measure of the normalized heavy-tailed elliptic matrix converges in probability to the deterministic `mu_{alpha,theta_d}`. The open target here is the dependence/classification question for that limit, not existence of the limit.

### Source hypotheses preserved

Condition C2 includes Condition C1, the regular-variation/spectral-measure hypothesis, plus:

1. `supp(theta_d)` is not contained in any complex linear hyperplane `{(z,w): a z+b w=0}` with `(a,b)!=(0,0)`;
2. `a_n/n^(1/alpha) -> c>0`.

The transformations below preserve these hypotheses. They also preserve the diagonal-tail requirement because they preserve absolute value.

### Current-status check, bounded 2026-09-18 UTC

The source itself was checked through arXiv v3 and its EJP record. Bounded web searches used the paper title and authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `tail`, `spectral measure`, and 2023--2026 date terms. The searches recovered the 2022 paper, bibliographic/citation pages, and later Campbell--O'Rourke work such as *Spectrum of Levy--Khintchine Random Laplacian Matrices* (J. Theor. Probab. 2024), but no source claiming a solution or full classification of Question 1.8. This is a bounded negative search, **not** proof of worldwide openness or novelty.

Historical Bordenave--Chafai intake questions C0026--C0030 were also screened. The repository records local non-Hermitian universality C0026, elliptic law C0027, oriented regular-graph ESD C0028 and Weyl-polynomial C0030 as resolved; C0029 is the excluded Bernoulli least-singular-value problem. None is this target.

## 2. Frozen source-relevant metric

Let `S` be the number of exact nontrivial transformation identities for the source map

`theta -> mu_{alpha,theta}`

proved by HARD7-02, where an identity counts only if it holds under Condition C2 at the full limiting-measure level and is inherited from an exact finite-matrix spectral identity rather than simulation.

Baseline before this run: `S=0` (no previous HARD7-02 report existed).

After this run: **`S=3`**, consisting of transpose/swap invariance, common-phase covariance, and complex-conjugation covariance.

The metric is deliberately structural: it measures exact information toward the source's Question 1.8, not a numerical proxy for the ESD.

## 3. Setup

Write `S(C^2)` for the unit sphere in `C^2`. For a finite dependence measure `theta` on `S(C^2)`, define three maps

- coordinate swap: `tau(z,w)=(w,z)`;
- common phase: `rho_phi(z,w)=(e^{i phi} z,e^{i phi} w)`;
- conjugation: `kappa(z,w)=(bar z,bar w)`.

For a probability measure `mu` on `C`, use the same notation `rho_phi#mu` for rotation by `e^{i phi}` and `kappa#mu` for reflection by complex conjugation.

The source limit corresponding to `theta` is abbreviated `mu_theta=mu_{alpha,theta}` with `alpha` fixed.

## 4. Main theorem — an exact symmetry-covariance quotient for Question 1.8

### Theorem 1

Assume `theta` is realized by atom variables satisfying Campbell--O'Rourke Condition C2. Then the transformed dependence measures also satisfy Condition C2, and

`(T1)   mu_{tau#theta} = mu_theta,`

`(T2)   mu_{rho_phi#theta} = rho_phi#mu_theta       for every real phi,`

`(T3)   mu_{kappa#theta} = kappa#mu_theta.`

In particular, the map `theta -> mu_theta` is not injective: it factors at least through coordinate-swap orbits, and it is equivariant under the natural `U(1)` rotation and conjugation actions.

### Proof

Let `X_n` be an elliptic ensemble with atom pair `(xi_1,xi_2)`, diagonal atom `zeta`, scaling `a_n`, dependence measure `theta`, and limiting ESD `mu_theta` from source Theorem 1.6.

#### (T1): transpose / swap

Set

`Y_n = X_n^T`.

Then `Y_n` is again elliptic. Its off-diagonal atom pair is exactly `(xi_2,xi_1)`, so its regular-variation angular measure is `tau#theta`; its diagonal atom is still `zeta`. The support nondegeneracy in Condition C2(i) is preserved because a support contained in `a z+b w=0` after swapping would imply that the original support is contained in `b z+a w=0`. The scaling condition C2(ii) is unchanged.

For every deterministic square matrix,

`det(lambda I-X_n^T)=det((lambda I-X_n)^T)=det(lambda I-X_n)`.

Therefore `X_n` and `X_n^T` have exactly the same eigenvalue multiset, including algebraic multiplicities, for every `n` and every realization. Hence their empirical spectral measures are exactly equal:

`mu_{a_n^{-1}Y_n}=mu_{a_n^{-1}X_n}`.

Theorem 1.6 applied to the two ensembles gives convergence in probability to `mu_{tau#theta}` and `mu_theta`, respectively. A sequence of random probability measures cannot converge in probability to two distinct deterministic weak limits. Thus

`mu_{tau#theta}=mu_theta`.

#### (T2): common phase

Fix real `phi` and set

`Y_n=e^{i phi}X_n`.

The atom pair becomes `(e^{i phi}xi_1,e^{i phi}xi_2)`, so the angular regular-variation measure is `rho_phi#theta`; the diagonal atom becomes `e^{i phi}zeta`. Absolute values, the radial tail, and `a_n` are unchanged. The C2 hyperplane condition is preserved because `rho_phi` is invertible complex-linear.

At finite `n`, every eigenvalue is multiplied by `e^{i phi}`. Therefore

`mu_{a_n^{-1}Y_n}=rho_phi#mu_{a_n^{-1}X_n}`

exactly. Passing to the deterministic limits in probability yields

`mu_{rho_phi#theta}=rho_phi#mu_theta`.

#### (T3): conjugation

Set

`Y_n=bar X_n`.

Its atom pair is `(bar xi_1,bar xi_2)` and its angular measure is `kappa#theta`. C2(i) is preserved: if the conjugated support lay in `a z+b w=0`, then the original support would lie in `bar a z+bar b w=0` after conjugation. C2(ii) and the diagonal-tail bound are unchanged.

The eigenvalues of `bar X_n` are the complex conjugates of those of `X_n`, with algebraic multiplicity. Hence exactly

`mu_{a_n^{-1}Y_n}=kappa#mu_{a_n^{-1}X_n}`.

Passing to the source limits gives

`mu_{kappa#theta}=kappa#mu_theta`.

This proves all three identities. `□`

## 5. B2 — attack injectivity first: an explicit non-injectivity family

The source states that `mu_{alpha,theta}` depends on `theta` but not on every aspect of it. The most direct negation attack is to ask whether the entire oriented dependence measure can nevertheless be reconstructed from `mu`.

The answer is **no**, already for a continuum of nondegenerate dependence measures.

For `0<p<1`, define

`theta_p = p delta_(1,0) + (1-p) delta_(0,1)`.

Its support contains both coordinate directions, so it is not contained in a single complex hyperplane through the origin; hence the C2(i) support obstruction is absent. Such a dependence measure is realized, for example, by an alpha-stable vector with independent coordinates having unequal tail scales (one may take `alpha in (0,1)` to avoid centering distractions), and `a_n ~ c n^(1/alpha)` gives C2(ii).

Coordinate swap sends

`tau#theta_p = theta_{1-p}`.

Therefore Theorem 1 gives

`mu_{alpha,theta_p}=mu_{alpha,theta_{1-p}}`.

For every `p != 1/2`, `theta_p != theta_{1-p}`. Thus the source map is rigorously non-injective even inside a simple C2-admissible family. The orientation imbalance `p-(1-p)` of the two coordinate axes is invisible to the limiting ESD up to sign: only its swap-orbit can matter.

This is a genuine source-level obstruction, not a finite simulation: no proposed complete set of invariants for Question 1.8 can distinguish `theta` from `tau#theta` if it is supposed to be recoverable from `mu_{alpha,theta}`.

## 6. B6 — deform by a solvable continuous group rather than perturb cumulants

The common-phase identity gives an exact one-parameter deformation. Define

`theta_phi = rho_phi#theta`.

Once `mu_theta` is known for one representative, the entire family is known with no new PWIT or Hermitization calculation:

`mu_{theta_phi}=rho_phi#mu_theta`.

So classification may quotient out one continuous phase parameter before any nonlinear fixed-point analysis. This is stronger than saying the pictures rotate: it is an exact equality of deterministic limiting measures inherited from the finite matrix identity `spec(e^{i phi}X)=e^{i phi}spec(X)`.

The attempt therefore succeeded, but in a structural rather than perturbative way. It does not show continuity of `theta -> mu_theta` under arbitrary deformations; it identifies one deformation direction exactly.

## 7. B30 — localize angular information one direction at a time

The exact covariance laws immediately impose angular constraints useful for both Question 1.8 and its neighboring tail Question 1.9.

### Corollary 2 — inherited rotational and reflection symmetries

If `rho_phi#theta=theta`, then

`rho_phi#mu_theta=mu_theta`.

If `kappa#theta=theta`, then

`kappa#mu_theta=mu_theta`.

Thus every exact angular symmetry of the dependence measure generated by common phase or conjugation is inherited by the limiting ESD.

In particular, if `theta` is invariant under rotation by `2 pi/k`, then the limiting spectrum is exactly `k`-fold rotationally invariant. If `theta` is invariant under all common phases, then `mu_theta` is isotropic.

### Corollary 3 — directional tail covariance

For a Borel set of angles `A` and `R>0`, define, whenever angular representatives are chosen away from boundary ambiguity,

`T_theta(R,A)=mu_theta({z: |z|>R, arg z in A}).`

Then

`T_{rho_phi#theta}(R,A)=T_theta(R,A-phi)`.

Consequently, if `theta` has `k`-fold common-phase symmetry, all rotated sectors of angle `2 pi/k` have identical tail mass at every radius `R`, not merely the same asymptotic exponent. If `theta` is conjugation invariant, the upper/lower reflected angular tail masses agree exactly.

This does not answer the radial tail-rate part of Question 1.9, but it proves that the **directional** tail profile transforms equivariantly and inherits these source symmetries.

## 8. Why the theorem is more than a notation cleanup

The source's Figure 1--3 discussion treats the geometry of `supp(theta_d)` as carrying dependence information. Theorem 1 identifies information that is provably redundant before solving the PWIT recursion:

1. orientation of the two mirrored coordinates is invisible (`theta` and `tau#theta` give exactly the same `mu`);
2. absolute common phase is only a gauge for rotation of the output spectrum;
3. complex conjugation only reflects the output spectrum.

Hence any eventual answer to Question 1.8 can be sought on a quotient of dependence measures by these exact transformations. The non-injectivity family `theta_p ~ theta_{1-p}` is especially useful because it rules out any proposed scalar classifier that changes under coordinate swap while claiming to be determined by the limiting ESD.

No assertion is made that these are the **only** redundancies. Determining the full quotient/fixed-point invariants is still the hard source question.

## 9. Method outcomes

- **B2 ATTACK THE NEGATION:** asked whether `theta -> mu_theta` could be injective after all. **Succeeded negatively.** Transposition proves `mu_{tau#theta}=mu_theta`; the explicit `theta_p,theta_{1-p}` family gives distinct C2 dependence measures with identical limiting ESD.
- **B6 DEFORM TO A POINT/FAMILY YOU CAN SOLVE:** used the common-phase orbit. **Succeeded exactly.** A full continuous one-parameter family is obtained by rotating one representative, with no repeated resolvent analysis.
- **B30 ONE DIRECTION AT A TIME:** localized to angular sectors. **Succeeded partially.** Directional tail masses obey exact rotation/reflection covariance and inherit finite or continuous angular symmetry of `theta`; the radial decay rate remains open.

No exact-arithmetic checker was created because the new claims are theorem-sized identities proved on the page from exact characteristic-polynomial/eigenvalue identities; a checker would add no evidentiary value.

## 10. Next mathematical obstruction

The first nontrivial target after quotienting these elementary symmetries is to decide whether `mu_theta` depends only on a smaller **swap-symmetrized functional** of `theta`, or whether genuinely higher angular information survives. Theorem 1 proves only

`mu_theta=mu_{tau#theta}`,

not

`mu_theta = mu_{(theta+tau#theta)/2}`.

Those statements are very different. The next run should attack the latter equality by searching for a finite-moment/resolvent statistic sensitive to replacing `theta` by its swap average, or by proving from the PWIT recursion that the root law sees only a symmetrized intensity. This is a source-valid fork: a counterexample would prove that more than the swap orbit matters; a proof would collapse the dependence classification substantially.

A second route toward Question 1.9 is to test whether positive `theta`-mass on directions with both coordinates simultaneously nonzero forces a polynomial spectral tail, interpolating between the axis-supported i.i.d. exponential-tail case and the Hermitian power-tail case. That claim is **not proved here** and should not be reported as progress until a rigorous PWIT or spectral argument exists.

## 11. ledger_delta

```yaml
track: HARD7-02
source: Campbell-O'Rourke 2022, Question 1.8
claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
claim_commit: 07e2759d8f5e7ae2522707d9e490da404a48e5be
metric: exact nontrivial transformation laws S for theta_d -> mu_{alpha,theta_d}
metric_before: 0
metric_after: 3
status_before: ADMISSION_PENDING
status_after: PARTIAL
unchanged_count_before: UNKNOWN
unchanged_count_after: 0
methods_this_run: [2, 6, 30]
proved:
  - mu_{tau#theta}=mu_theta
  - mu_{rho_phi#theta}=rho_phi#mu_theta
  - mu_{kappa#theta}=kappa#mu_theta
  - explicit noninjectivity theta_p versus theta_{1-p}
remaining_obligation: classify the genuinely surviving dependence data beyond exact swap/phase/conjugation symmetries; next test swap-symmetrization versus only swap-orbit invariance
novelty: UNVERIFIED; bounded 2026-09-18 search found no resolution of Question 1.8, but these elementary symmetry identities may be folklore
closure_audits: 0
```
