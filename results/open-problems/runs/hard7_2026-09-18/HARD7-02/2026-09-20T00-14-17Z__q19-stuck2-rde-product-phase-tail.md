Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **No movement: `T_corr=4 -> 4`. Methods tried: B18/B22/B23. This is the required Section-I STUCK2 thinking run: no new theorem is claimed. The new route is to replace radial-only estimates by a one-big-jump analysis of Campbell--O'Rourke Proposition 4.12, whose phase algebra predicts that the polynomial tail direction is the half-angle pushforward of the phase of `w_1 w_2`.**

# HARD7-02 — STUCK2 on Campbell--O'Rourke Question 1.9: product-phase resonance in the resolvent RDE

Status: **PARTIAL / source Question 1.9 remains OPEN under a fresh bounded 20 September 2026 literature check / second permitted HARD stuck-recovery cycle.**

Frozen metric:

`T_corr = number of explicit non-i.i.d., non-Hermitian C2 dependence families for which HARD7-02 rigorously determines the asymptotic radial tail exponent/class of mu_{alpha,theta}`.

Before: `T_corr=4`.

After: **`T_corr=4` — no movement.**

The two immediately preceding ordinary runs, at `2026-09-19T22-12-00Z` and `2026-09-19T23-12-00Z`, also left `T_corr=4`. Therefore this run follows Section I instead of manufacturing another radial lemma or another checker. It records the exact obstruction, the failed/saturated routes, the simplest unproved special case, the nearest solved analogue, and one genuinely different recovery route. The source question is not closed.

## 1. Continuity, ownership, exclusions, and current repository state

I resumed the active exclusive canonical claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`

from the newest completed HARD7-02 report

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T23-12-00Z__q19-two-sided-pareto-envelope.md`.

At run start I refreshed the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md` and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the current claim and newest HARD7-02 chain;
- the screened intake/attempt neighborhood for the Campbell--O'Rourke/heavy-tail targets through repository search;
- the neighboring C0032 terminal handoff `research7_2026-09-17/R7-06/handoffs/2026-09-19T095800Z__C0032_terminal_handoff.md`.

C0032 is the distinct i.i.d. heavy-tailed circular-law explicit-density problem and has been terminally handed off by R7-06; it is not an alias of Question 1.9. No conflicting ownership, posting, or claim release for Question 1.9 was found. No claim file, shared root ledger, neighboring track, scheduler, permission, workflow, Gmail, Drive, or public destination was modified.

The scheduler/runtime capability situation is still the same: the exposed task interface has ordinary task/schedule controls but no binding model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed run-duration field. Thus `GPT-6 / maximum` remains prompt-requested only. A real change would require a product/backend surface exposing binding model and effort controls. Historical `You cannot modify this task` errors are permission-context failures; the compliant workaround is the owning/authorized account or workspace, ownership transfer, or platform support, never a duplicate schedule or permission bypass. No scheduler mutation was attempted here.

## 2. Exact source statement and fresh current-literature check

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Source URL: `https://arxiv.org/html/2010.01261v3`.

Section 1.3 asks exactly:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The source explicitly says that the i.i.d. limit has an exponential tail while the Hermitian limit inherits the heavy tail of the entries, and its numerical figures suggest that tails may vary by direction. Theorem 1.6 expresses the limiting ESD through Hermitization, and Proposition 4.12 gives the recursive distributional equation used below.

Fresh bounded searches on 20 September 2026 used the exact title/authors, exact Question 1.9 wording, `mu_{alpha,theta_d}`, `theta_d`, directional tail, heavy-tailed elliptic, PWIT, and 2025--2026 follow-up terms. They recovered the 2022 source, Carpenter--O'Rourke's 2025 sparse elliptic paper (a different finite-variance/sparsity regime), and neighboring heavy-tail/random-matrix work, but no located paper claiming a general solution of Question 1.9 or a directional regular-variation formula for the C2 heavy-tailed elliptic limit. This is bounded negative evidence only, not a worldwide novelty certificate.

For the nearest solved analogue I also refreshed:

- G. Ben Arous and A. Guionnet, *The spectrum of heavy tailed random matrices*, Comm. Math. Phys. 278 (2008), arXiv:0707.2159;
- A. Auffinger, G. Ben Arous and S. Peche, *Poisson convergence for the largest eigenvalues of heavy tailed random matrices*, AIHP 45 (2009), arXiv:0710.3132.

The latter proves, in the symmetric heavy-tailed setting, that the top eigenvalues asymptotically behave like the largest entries. That self-adjoint one-large-entry mechanism is the closest solved comparison, not a solution of the present non-Hermitian directional-tail problem.

## 3. Source-level progress already consumed

The HARD7-02 chain has already extracted essentially all information obtainable from radial-only observables without resolving the angular tail.

1. **Axis support.** Pure coordinate-axis C2 laws are exact deterministic dilations of the i.i.d. heavy-tailed circular law and therefore have exponential radial tails.
2. **Positive off-axis mass.** Every C2 angular law with positive mass on `{w_1w_2 != 0}` has radial logarithmic tail exponent exactly `alpha`.
3. **Moment index.** The radial moment index is `infinity` on pure-axis support and exactly `alpha` for positive off-axis mass.
4. **Pointwise radial order.** The newest report proves constants `0<c_theta<=C_alpha<infinity` such that, for all sufficiently large `r`,

   `c_theta r^(-alpha) <= mu_{alpha,theta}(|z|>r) <= C_alpha r^(-alpha)`.

5. Consequently the truncated critical `alpha`-moment grows as `Theta(log R)` and the near-critical moments have the exact blow-up order `Theta((alpha-p)^(-1))`.

These are substantial PARTIAL results, but they do not determine a regular-variation constant, a limiting angular tail measure, or the directional tails that the source itself highlights. Merely naming additional positive-off-axis families would not move the frozen metric and would violate the owner's metric discipline.

## 4. Section-I blocker: the exact missing statement

The remaining obstruction is not another radial bound. It is the existence and identification of a **tail measure**. For a C2 angular law `theta`, define on sets bounded away from zero

`nu_R^theta(A) := R^alpha mu_{alpha,theta}(R A)`.

The source-level directional problem would become concrete if one could prove, at least in a nontrivial class,

\[
\boxed{\quad \nu_R^\theta \xrightarrow[R\to\infty]{\mathrm{vague}} \nu_\theta\neq 0,\qquad
\nu_\theta(dr\,d\phi)=\alpha r^{-\alpha-1}\,dr\,\kappa_\theta(d\phi).\quad}
\tag{4.1}
\]

The existing two-sided Pareto envelope gives the right radial *order* but neither uniqueness of subsequential tail measures nor the angular measure `kappa_theta`. No previous HARD7-02 route contains a mechanism that controls the phase of a rare large spectral excursion after the full nonnormal background is restored.

## 5. Every serious route already tried, and why it stops here

### 5.1 Direct reciprocal-edge eigenvalue stability — failed at the nonnormal restoration step

The exceedance-skeleton route found a positive density of exact `2 x 2` reciprocal blocks. If an edge has radial mark `r` and angular mark `w=(w_1,w_2)`, the two block eigenvalues have modulus

`r sqrt(|w_1w_2|)`

and phases determined by square roots of `w_1w_2`. This is the right local geometry. But reattaching the sea of sub-threshold edges is a highly nonnormal perturbation. Small operator/Frobenius control does not give eigenvalue-by-eigenvalue stability, and the sparse eigenvalues can disappear into the pseudospectrum. That is why the first stuck recovery abandoned direct eigenvalue perturbation.

### 5.2 Subcritical moments and the critical moment — saturated

Schatten/row estimates prove every moment `p<alpha` is finite; the integrated lower-tail argument proves the `alpha`-moment diverges. This pins the moment index exactly but integrates away angle and does not distinguish `c r^{-alpha}` from a direction-dependent mixture with the same total radial order.

### 5.3 Jensen/Mahler/logarithmic-potential peeling — successful radially, angularly blind

The first stuck recovery moved to Hermitization/logarithmic potentials. This was the key successful change: it bypassed nonnormal eigenvalue stability and eventually proved the exact radial exponent and then the two-sided Pareto envelope. But circular averaging/Jensen identities collapse the angular information that Question 1.9's figures suggest is essential. Pushing the same scalar potential harder will improve constants, not recover directions.

### 5.4 Weak-Schatten endpoint truncation — saturated

The rank-plus-truncated-Frobenius argument upgraded the radial upper bound to `O(r^{-alpha})` without logarithmic loss. It is intrinsically based on singular values and row norms. Those quantities are phase-insensitive, so this route cannot identify `kappa_theta` by itself.

### 5.5 Exact axis classification and phase/gauge symmetries — endpoint only

The exact two-axis dilation law completely explains the i.i.d.-type endpoint and supplies useful covariance checks. It does not interpolate into positive off-axis mass, where the tail index jumps from `infinity` to `alpha`.

The common feature of all five routes is now clear: they either lose phase deliberately or face nonnormal instability directly. A successful next route must keep phase **inside Hermitization/PWIT**, rather than recover it after a radial estimate.

## 6. B18 — say it in another language: a one-big-jump resonance inside Proposition 4.12

This is the genuinely different mechanism found in this thinking run. It is a derivation of a **candidate asymptotic law**, not a theorem.

Campbell--O'Rourke Proposition 4.12 states that the root `2 x 2` bipartized resolvent

`R_root(z,eta) = [[a,b],[b',c]]`

satisfies

`R_root = -([[eta,z],[bar z,eta]] + [[S_1,S_2],[S_3,S_4]])^{-1}`,

where the `alpha/2`-stable spectral measure is generated from

`( c |w_1|^2, b' w_1w_2, b bar(w_1w_2), a |w_2|^2 )`.

Take `z=R e^{i phi}` with `R` large. If the stable feedback is temporarily suppressed, exact inversion gives

`b_0(z,eta) = -z/(R^2-eta^2) = -1/bar z + O(R^{-3})`,

`b'_0(z,eta) = -bar z/(R^2-eta^2) = -1/z + O(R^{-3})`.

Now expose one large PWIT branch with radial mark `r` and angular mark `w`. The off-diagonal feedback generated by that branch has the schematic leading form

`S_2^(one) ~ r^2 b'_child w_1w_2`.

Writing `psi=arg(w_1w_2)`, the free large-`R` approximation gives

`arg S_2^(one) ~ pi - phi + psi`.

A singular-value resonance near the spectral point `z` requires `z+S_2` to be small, hence the rare feedback must point approximately opposite to `z`:

`arg S_2 ~ pi+phi`.

Equating the phases gives the simple relation

\[
\boxed{\qquad \psi \equiv 2\phi \pmod{2\pi}.\qquad}
\tag{6.1}
\]

Thus a large spectral excursion in direction `phi` should be driven by angular marks whose product `w_1w_2` points in direction `2 phi`. The square-root geometry of the old isolated `2 x 2` block has reappeared **inside the Hermitized RDE**, where nonnormal eigenvalue perturbation is no longer the primitive object.

The magnitude algebra is equally suggestive. Since `|b'_child|~R^{-1}`, cancellation at scale `R` requires

`r^2 |w_1w_2|/R ~ R`,

or

`r ~ R / sqrt(|w_1w_2|)`.

The PWIT radial intensity satisfies `m_alpha([r,infinity))=r^{-alpha}`. Therefore the one-jump rate at angle `phi` carries the weight

`R^{-alpha}|w_1w_2|^{alpha/2}`.

This suggests the following **candidate**, not yet proved, angular tail measure. Let `u(w)` be either square root of `(w_1w_2)/|w_1w_2|`; the two roots are `u` and `-u`. Define

\[
\widehat\kappa_\theta
:=\int_{w_1w_2\ne0}|w_1w_2|^{\alpha/2}
\frac{\delta_{u(w)}+\delta_{-u(w)}}{2}\,\theta(dw).
\tag{6.2}
\]

Its total mass is

\[
M_\alpha(\theta):=\int |w_1w_2|^{\alpha/2}\,\theta(dw).
\tag{6.3}
\]

The sharpened conjectural endpoint of this route is that (4.1) holds with angular component proportional to, and perhaps exactly equal to under the current normalization, `widehat kappa_theta`.

What is missing is decisive: one must justify the large-`R` child-resolvent approximation under the rare resonance conditioning, prove that configurations with two or more competing large branches are lower order at the `R^{-alpha}` scale, control the sea of smaller branches, and then transfer the resulting RDE asymptotic through Hermitization to `mu_{alpha,theta}`. None of that is asserted here.

**B18 outcome:** promising new route; no certified metric movement and no new theorem claim.

## 7. B22 — read the failures: why the RDE route is materially different

The first failed route tried to keep an eigenvalue of a finite reciprocal block after restoring the background. The precise obstruction was pseudospectral: in a nonnormal matrix, a perturbation that is small in a global norm can move eigenvalues dramatically.

The RDE route asks a different question. Proposition 4.12 already describes the limiting **Hermitized** resolvent after the entire PWIT background has been included. A rare branch is inserted into a self-consistent resolvent environment rather than into a finite nonnormal eigenvalue problem. The difficult step becomes a one-big-jump asymptotic for a stable recursive equation, not a Bauer--Fike-style stability estimate that cannot be uniform.

The nearest successful analogue explains what ingredient is absent here. In symmetric heavy-tailed matrices, Auffinger--Ben Arous--Peche prove that extreme eigenvalues asymptotically follow the largest entries; self-adjointness supplies ordering/variational control and rules out the worst pseudospectral behavior. Ben Arous--Guionnet identify the limiting heavy-tailed spectral law on the real line. For Campbell--O'Rourke's non-Hermitian law, there is no self-adjoint eigenvalue ordering; the missing replacement is a phase-resolved one-big-jump theorem for the bipartized RDE.

**B22 outcome:** the earlier failure is not evidence against the reciprocal-edge mechanism. It says the mechanism has to be proved at the RDE/Hermitization level, where the background is already present.

## 8. B23 — assume the half-angle law is wrong and try to break it

Before investing in the RDE route, test its negation against source-valid boundary cases. These are consistency tests only.

### 8.1 I.i.d./axis-supported endpoint

On pure coordinate-axis support, `w_1w_2=0` identically, so (6.2) has zero mass and predicts no polynomial one-jump tail. The source says this endpoint instead has an exponential tail. This is consistent.

### 8.2 Hermitian endpoint

For Hermitian marks, `w_2=bar w_1`, hence `w_1w_2=|w_1|^2` has phase zero. Equation (6.1) then permits `phi=0` or `pi`: the real line. The source says the Hermitian limit lives in the heavy-tailed real-line regime. This is consistent.

### 8.3 Rotated Hermitian line

If a Hermitian ensemble is multiplied by `e^{i gamma}`, the paired product acquires phase `2 gamma`, while the spectrum rotates to the line of angle `gamma`. Again (6.1) gives exactly the required half-angle transformation.

### 8.4 The source's Figure-1 cross geometry

In the right panel of Figure 1 the angular mark is real,

`w=(cos omega,sin omega)`.

Then `w_1w_2=(1/2)sin(2omega)` is real and has phase `0` or `pi`. The half-angle rule predicts heavy directions on the real and imaginary axes, i.e. a cross. The source explicitly remarks that this spectrum resembles a hyperbolic cross. This is a particularly nontrivial qualitative match because the rule predicts both axes from the sign change of the product.

### 8.5 Frozen family and recovery of the old local coefficient

For the frozen family `vartheta_x`, every support point has

`w_1w_2=sqrt(x(1-x))>0`.

The route predicts real-axis heavy directions and

`M_alpha(vartheta_x)=(x(1-x))^(alpha/4)`.

At the original `alpha=1,x=1/4` point this becomes

`M_1(vartheta_{1/4})=(3/16)^(1/4)=3^(1/4)/2`,

which is exactly the `kappa_x` coefficient that arose independently from the old isolated reciprocal `2 x 2` block calculation. This agreement is a strong diagnostic, but it is still not a proof that the global tail constant equals this number.

I did not find a boundary case that contradicts the half-angle/product-weight rule. The main remaining risk is recursive renormalization of the constant or angular weight by the background PWIT, not a failure of the phase algebra itself.

**B23 outcome:** negation testing did not break the route; it survived four qualitatively different exact/known endpoints. No theorem is promoted from these checks.

## 9. What a proof must contain that no route so far contains

A successful proof now needs one genuinely new lemma of the following type.

**Phase-resolved one-big-jump RDE lemma (required, unproved).** Uniformly for `phi` in a compact angular sector and with `z=R e^{i phi}`, decompose the Poisson/stable feedback in Proposition 4.12 into its largest branch plus the remainder and prove, at relative error `o(1)` on the `R^{-alpha}` scale, that:

1. a spectral-tail event is produced by exactly one branch with `r=Theta(R/sqrt(|w_1w_2|))`;
2. the child resolvent on that branch may be replaced to leading order by its free large-`R` value `b'=-1/z` in the phase-sensitive term;
3. two-or-more resonant branches and the truncated background contribute `o(R^{-alpha})` to the tail measure on angular continuity sets;
4. the resulting asymptotic survives the `eta downarrow 0` limit and the Laplacian/Hermitization passage from the singular-value resolvent to the planar measure.

Items 2 and 4 are the parts absent from every prior route. Item 2 is where recursive dependence could change the naive coefficient; item 4 is where a statement about a resolvent must become a statement about directional eigenvalue mass.

## 10. Simplest special case still unproved

The smallest source-valid case worth proving next is the original frozen point

`alpha=1`, `theta=vartheta_{1/4}`.

Here the product phase is deterministic and positive, so the angular problem has no mixture. A clean restricted theorem would be: for every `epsilon>0`,

\[
R\,\mu_{1,\vartheta_{1/4}}\!\left(\{|z|>R:\operatorname{dist}(\arg z,\{0,\pi\})>\epsilon\}\right)\longrightarrow0,
\tag{10.1}
\]

and there exists a finite nonzero constant `C_*` such that

\[
R\,\mu_{1,\vartheta_{1/4}}(|z|>R)\longrightarrow C_*\in(0,\infty).
\tag{10.2}
\]

The one-big-jump calculation predicts `C_*=3^(1/4)/2` under the current normalization, but **that exact value is a conjectural target, not a proved claim**. Even proving (10.1)--(10.2) with `C_*` unidentified would be a real source-level advance beyond the current two-sided envelope.

## 11. Nearest solved problem and the missing ingredient

The nearest solved family is the symmetric/Hermitian heavy-tailed problem. Ben Arous--Guionnet establish the limiting heavy-tailed spectral law; Auffinger--Ben Arous--Peche prove the extreme eigenvalues follow the largest entries in the appropriate heavy-tail regime. Their setting has self-adjointness, real ordering and variational/resolvent control that turn a large entry into a stable spectral extreme.

The present problem lacks exactly that structure. The non-Hermitian spectrum can be pseudospectrally unstable, so a large reciprocal edge cannot simply be followed as an eigenvalue after the background is restored. Proposition 4.12 is the plausible replacement: it packages the full background into a self-consistent Hermitized resolvent, but no currently consumed theorem gives the required phase-resolved rare-event asymptotic.

## 12. Section-I recovery choice and next moves

**Recovery choice:** prove the simplest unproved special case from Section 10, rather than rotate. This is the second permitted stuck-recovery cycle for this hard target. A future third stuck episode must trigger handoff/rotation under Section I; it must not be hidden by changing the metric.

The next run should attack (10.1)--(10.2) through three previously unused numbered moves:

- **B9 RANDOMIZE:** Palm-condition on the unique PWIT branch in the resonant radial window and derive the conditional RDE seen from that branch.
- **B12 FIND WHAT IS CONSERVED:** isolate the phase invariant `arg(w_1w_2)-2 arg(z)` and prove that nonresonant phase sectors cannot contribute at first order.
- **B28 REPLACE FOR ALL WITH TYPICAL:** first establish the one-big-jump expansion away from angular collision/boundary sets, where the product phase and radial mark have regular conditional behavior, before attempting arbitrary `theta`.

For the frozen `vartheta_{1/4}` family B28 reduces to a particularly clean typicality statement because the product phase is deterministic.

No code or exact finite checker was created in this thinking-only run: there is no new finite claim to certify, and manufacturing a checker would violate the 90/10 rule. The work product is the new proof architecture and the explicit missing lemma above.

## 13. Honest ledger delta

```text
ledger_delta:
  track: HARD7-02
  canonical_claim: CAMPBELL-OROURKE-2022-Q1.9
  target: Campbell--O'Rourke 2022 Question 1.9
  status: PARTIAL / OPEN
  metric: T_corr
  before: 4
  after: 4
  movement: no movement
  section_I_state: STUCK2 thinking/recovery run
  methods: [B18, B22, B23]
  new_claims: none
  new_route: phase-resolved one-big-jump asymptotic in Proposition 4.12 RDE
  simplest_next_case: alpha=1, theta=vartheta_{1/4}, directional regular variation
  next_methods: [B9, B12, B28]
  shared_root_write: none
```

The claim remains active and the source remains OPEN/PARTIAL. No closure, priority, independent-audit, or worldwide-novelty claim is made.