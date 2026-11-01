Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime interface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **Movement: `S=4 -> 5`. Methods tried: B4, B19, B23.**

# HARD7-02 run 6 — exact mass homogeneity, canonical normalization, and a support-only obstruction

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.**

This run separates one parameter of the dependence measure completely. If `theta` is the finite C1 angular measure and `s>0`, then

`mu_{alpha,s^alpha theta} = D_s# mu_{alpha,theta}`,              (1)

where `D_s(z)=s z`. Equivalently, if `m=theta(S(C^2))`, `bar theta=theta/m`, then

`mu_{alpha,theta}=D_{m^(1/alpha)}#mu_{alpha,bar theta}`.          (2)

Combining (2) with run 4's exact quotient theorem gives a canonical source-valid reduction: **total mass of `theta` controls only the overall spectral scale, while the normalized pushforward under**

`q(z,w)=(|z|^2,zw)`                                             (3)

**is sufficient for the remaining shape information.** This does not claim that `q` is minimal, and it does not solve the source question.

The homogeneity mechanism is elementary regular-variation scaling and is very likely folklore; the source itself remarks that a stable vector can be scaled so that its spectral measure is a probability measure. I therefore make **no literature-novelty claim** for (1) in isolation. What is useful for this track is the exact source-level formulation, its inclusion in the frozen transformation-law metric, and its combination with the previously proved `q` quotient.

## 1. Continuity, ownership, fleet state, and current-source check

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T01-12-00Z__subcritical-product-universality.md`.

At run start I re-read the controlling HARD7/new-methods files, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, all five earlier HARD7-02 reports, the current HARD7-02 artifact directory, repository claim/alias search hits, and the newest neighboring R7-06 heavy-tail report. The adjacent R7-06/C0032 target remains the distinct Bordenave--Chafai i.i.d. heavy-tail density-identification problem. Repository search still identifies Campbell--O'Rourke Question 1.8 as exclusively owned by HARD7-02; no posted, retired, Bernoulli-singularity, personal-manuscript, or equivalent claimed target was found.

The current master observed immediately before this write was `95877f0d9e5a47a13eae2ba3d7c6a21a9b7dec50`; concurrent unrelated fleet commits were present, so this report does not modify a shared root ledger.

### Exact source statement and assumptions rechecked

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, arXiv:2010.01261v3, DOI `10.1214/22-EJP849`.

Primary links:

- `https://arxiv.org/abs/2010.01261`
- `https://arxiv.org/html/2010.01261v3`

Section 1.3, Question 1.8 still asks exactly:

> “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

Condition C1(i) uses a **finite** angular measure `theta_d` on the unit sphere and a scaling sequence `a_n=ell(n)n^(1/alpha)` with the radial tail measure `m_alpha(dr)=alpha r^(-1-alpha)dr`. Condition C2 adds the no-complex-hyperplane support condition and `a_n/n^(1/alpha)->c>0`. Theorem 1.6 gives convergence in probability of the ESD of `A_n=X_n/a_n` to the deterministic `mu_{alpha,theta_d}`. The source also notes in its stable-vector discussion that a stable vector can be scaled so that its spectral measure is a probability measure; this is consistent with the homogeneity proved below.

### Fresh bounded literature check, 2026-09-19 UTC

Searches used the exact source title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `scaling`, `spectral measure`, `homogeneity`, `PWIT`, `corrigendum`, and 2023--2026 date terms. They recovered the 2022 source, Campbell--O'Rourke's later Levy--Khintchine random-Laplacian paper, and a 2025 finite-moment global elliptic-law paper, but no located paper claiming a full solution of Question 1.8. Searches for an explicit `mu_{alpha,c theta}` formula likewise did not locate a source-specific statement. This is **bounded negative evidence only**, not a novelty certificate or proof of worldwide openness.

The underlying fact that multivariate regular-variation limit measures are `-alpha` homogeneous is standard. Accordingly, the theorem below is recorded as an exact structural reduction for the source problem, not advertised as a new general theorem about regular variation.

### Scheduler/interface capability statement

The exposed task interface still offers title/prompt/schedule/timing/enabled controls but no binding model selector or reasoning-effort selector. Thus the requested GPT-6/maximum setting cannot be enforced or authenticated from this worker. Historical native modification probes for P26/P01/P03 returned `You cannot modify this task`; the repository also records that P26 later succeeded in a different authorized native context. For any task that still refuses modification, the compliant route is the authorized owner/account/workspace interface or platform support/ownership transfer, not a permission bypass or duplicate schedule. This run made no scheduler changes.

## 2. Frozen metric

The canonical claim fixes

`S = number of exact nontrivial transformation laws for theta -> mu_{alpha,theta}`

proved by HARD7-02 at the **full source limiting-measure level under C2**, with exact mathematics rather than finite simulation.

Before: `S=4`.

After: **`S=5`.**

The fifth counted law is the positive-mass/scaling covariance (1). It is a full-source identity inherited from the exact finite-`n` relation obtained by changing the normalization sequence. It is not the subcritical truncation theorem of run 5. Because the metric moved, the ordinary unchanged streak resets to zero; Section I is not triggered.

The previously counted four laws remain: transpose/swap invariance, common-phase covariance, complex-conjugation covariance, and opposite-coordinate-phase invariance. Run 4's arbitrary relative-phase mixing and `q`-quotient theorem are consequences of the fourth law and were not counted separately.

## 3. B4 — prove a weaker statement completely: exact homogeneity in the mass of `theta`

The source's C1 parameterization contains a simple normalization freedom that had not yet been isolated in this track.

### Theorem 1 — mass homogeneity

Fix `0<alpha<2`. Let a C2 elliptic ensemble have scaling sequence `a_n`, dependence measure `theta`, and limiting ESD `mu_{alpha,theta}`. For every `s>0`, the same atom variables with the new scaling sequence

`b_n = a_n/s`                                                   (4)

satisfy C2 with dependence measure

`theta_s = s^alpha theta`.                                     (5)

Consequently

`mu_{alpha,s^alpha theta}=D_s#mu_{alpha,theta}`,                (6)

where `D_s(z)=s z`.

#### Proof

Write the C1 tail statement in polar form. For every angular continuity set `D` and every `r>0`,

`n P( ||(xi_1,xi_2)|| >= r a_n,
      (xi_1,xi_2)/||(xi_1,xi_2)|| in D )
   -> theta(D) r^(-alpha)`.                                    (7)

With `b_n=a_n/s`,

`n P( ||(xi_1,xi_2)|| >= r b_n, angle in D )`

`= n P( ||(xi_1,xi_2)|| >= (r/s) a_n, angle in D )`

`-> theta(D)(r/s)^(-alpha)
 = s^alpha theta(D) r^(-alpha)`.                               (8)

Thus C1 holds with `theta_s=s^alpha theta`. The diagonal-tail condition is unchanged because the atom variables themselves were not changed. The support of `theta_s` equals the support of `theta`, so the C2 hyperplane condition is unchanged. Finally

`b_n/n^(1/alpha) -> c/s > 0`,                                  (9)

so C2(ii) also holds.

At finite `n`, the two normalized matrices satisfy the exact identity

`X_n/b_n = s X_n/a_n`.                                         (10)

Hence their empirical spectral measures satisfy, realization by realization,

`mu_{X_n/b_n}=D_s#mu_{X_n/a_n}`.                               (11)

Theorem 1.6 applied to the two C2 parameterizations gives convergence in probability of the left side to `mu_{alpha,s^alpha theta}` and of the right side to `D_s#mu_{alpha,theta}`. Pushforward by the continuous map `D_s` preserves weak convergence, and deterministic weak limits are unique. This proves (6). `QED`

### Corollary 2 — complex scalar covariance

Combining Theorem 1 with run 1's common-phase law, for `s>0` and real `psi`,

`mu_{alpha,s^alpha (rho_psi#theta)}
 = (z -> s e^(i psi) z)#mu_{alpha,theta}`.                      (12)

Thus the modulus of a common complex scalar sets the spectral scale and its phase rotates the output plane.

### Corollary 3 — exact radial-tail scaling

For every Borel angular set `A` whose boundary carries no relevant output mass and every `R>0`,

`mu_{alpha,s^alpha theta}{|z|>R, arg z in A}
 = mu_{alpha,theta}{|z|>R/s, arg z in A}`.                      (13)

This is a source-valid consequence relevant to neighboring Question 1.9, but Question 1.9 is not separately claimed and (13) does not determine its unknown tail exponents.

**B4 outcome:** succeeded completely. One scalar degree of freedom in the finite measure `theta` is now explicit rather than being left inside the unknown map `theta -> mu`.

## 4. B19 — make the classification constructive: canonical probability normalization

Let

`m(theta)=theta(S(C^2))`.                                      (14)

Under C2, `m(theta)>0`. Define

`bar theta = theta/m(theta)`.                                  (15)

Taking `s=m(theta)^(1/alpha)` in Theorem 1 gives

`boxed: mu_{alpha,theta}
       = D_{m(theta)^(1/alpha)}#mu_{alpha,bar theta}`.           (16)

Thus every finite C2 dependence measure has a canonical probability-measure representative. The source classification can be performed in two stages:

1. record the scalar mass `m(theta)`;
2. classify the probability measure `bar theta`; then restore the output scale by `m(theta)^(1/alpha)`.

This by itself removes only one scalar. The stronger payoff comes by composing it with run 4.

Recall the run-4 quotient map

`q(z,w)=(|z|^2,zw)`,                                           (17)

and the proved implication

`q#eta_1=q#eta_2  =>  mu_{alpha,eta_1}=mu_{alpha,eta_2}`        (18)

for C2 dependence measures `eta_i`.

Define the **normalized quotient law**

`nu_theta := (1/m(theta)) q#theta = q#bar theta.                (19)

### Theorem 4 — mass/shape factorization of the source map

There is a well-defined source-limit functional `F_alpha` on the realizable normalized quotient laws such that

`mu_{alpha,theta}
 = D_{m(theta)^(1/alpha)} # F_alpha(nu_theta)`.                  (20)

Equivalently, if `theta_1,theta_2` are C2 and

`nu_{theta_1}=nu_{theta_2}`,                                   (21)

then

`D_{m(theta_1)^(-1/alpha)}#mu_{alpha,theta_1}
 = D_{m(theta_2)^(-1/alpha)}#mu_{alpha,theta_2}`.               (22)

#### Proof

Equation (19) says `q#bar theta_i=nu_{theta_i}`. If the normalized quotient laws agree, run 4 gives

`mu_{alpha,bar theta_1}=mu_{alpha,bar theta_2}`.                (23)

Apply (16) to each `theta_i`. This yields (22), and defining `F_alpha(nu)` to be the common normalized spectral law proves (20). `QED`

This is the cleanest current structural answer produced by HARD7-02: after removing an explicit scalar scale, the unknown dependence information lives on the two-real-dimensional quotient `Q=q(S(C^2))`, rather than on the full three-real-dimensional sphere. It remains entirely possible that `nu_theta` contains redundant information; run 5's product-only theorem shows such a further collapse in the subcritical hard-edge truncation but not yet at the full source limit.

**B19 outcome:** succeeded. The source question now has a canonical preprocessing map `theta -> (m(theta),nu_theta)` with exact reconstruction of spectral scale.

## 5. B23 — do what the support heuristic does not expect: support alone cannot be a complete invariant

The source discusses how the geometry of `supp(theta_d)` appears numerically to control how close the limit is to isotropic or Hermitian. That qualitative observation is compatible with the following negative result, but it shows that **support by itself cannot determine the full limiting measure in the printed finite-measure C1 parameterization**.

Take the axis-supported probability measure

`theta_0 = (1/2) delta_(1,0) + (1/2) delta_(0,1).`               (24)

Its support is not contained in a complex hyperplane, so it satisfies the C2 support condition when realized by the standard iid heavy-tail model. Source Remark 1.7 identifies its limit with the Bordenave--Caputo--Chafai iid heavy-tailed non-Hermitian law; the source introduction records that this law is isotropic with unbounded support, hence in particular is not `delta_0`.

For any `c>0`, put

`theta_c = c theta_0`.                                         (25)

Then

`supp(theta_c)=supp(theta_0)`                                  (26)

exactly, while Theorem 1 gives

`mu_{alpha,theta_c}
 = D_{c^(1/alpha)}#mu_{alpha,theta_0}`.                         (27)

For `c != 1`, these two probability measures are distinct. Indeed, a probability measure invariant under a fixed dilation `D_a` with `a>1` must be `delta_0`: the disjoint half-open annuli

`A_k={a^k <= |z| < a^(k+1)},  k in Z`,                         (28)

partition `C\{0}`, and dilation invariance makes all `mu(A_k)` equal; finiteness of total mass forces each to be zero. The case `0<a<1` reduces to `1/a>1`. Since the iid heavy-tail limit is not `delta_0`, (27) is genuinely different whenever `c != 1`.

Therefore two C2 dependence measures can have exactly the same support and different limiting ESDs. The missing property here is simply the total mass/scale, which Theorem 1 handles explicitly.

This is **not** a counterexample to the source's qualitative numerical statement that support geometry influences closeness to isotropic/Hermitian behavior, and it is not a claim that support plus normalization is insufficient. Once one imposes `theta(S)=1`, this particular obstruction vanishes and the nontrivial shape problem remains.

**B23 outcome:** succeeded as a counterexample-oriented stress test. It rules out “support alone” as a complete answer to Question 1.8 in the finite-measure C1 formulation while identifying exactly how to repair that naive classifier.

## 6. Why this run moves the source metric but does not close the question

The new identity (6) is at the full source limiting-measure level and comes from the exact finite-`n` spectral identity (10), so it qualifies for the frozen metric. It also combines nontrivially with the run-4 quotient theorem to give the factorization (20).

But Question 1.8 asks for the properties of `theta_d` determining `mu_{alpha,theta_d}`. HARD7-02 still has only a **sufficient** statistic, not a minimal or necessary-and-sufficient one. The key unresolved fork remains:

`Does pi#theta,  pi(z,w)=zw, determine the full mu_{alpha,theta}`   (29)

(after the explicit scale and elementary symmetries are factored out), or does the branch information in `|z|^2` survive the full infinite small-edge limit?

Run 5 proved product-only universality for every fixed subcritical hard-edge cutoff and produced an exact cycle obstruction to extending the finite-tree matching-polynomial argument mechanically. The full problem therefore requires a genuinely new bridge across the supercritical/infinite-small-edge regime, not another tree characteristic-polynomial lemma.

## 7. Method rotation and next checkpoint

Methods used over the six runs are now:

- run 1: B2, B6, B30;
- run 2: B1, B15, B20;
- run 3: B7, B18, B27;
- run 4: B5, B11, B14;
- run 5: B3, B12, B24;
- this run: **B4, B19, B23**.

No numbered method was repeated on this target. The frozen metric moved this run, so Section I is not active.

The best next attack is not another normalization identity. It should target (29) from a new angle. Three as-yet-unused candidates are:

- **B8**: discretize the full small-edge cloud into dyadic radial shells and identify exactly which shell interactions retain the `|z|^2` branch;
- **B13**: search for a monotone interpolation in the branch-mixing parameter at fixed `pi#theta`;
- **B29**: compactify the radial-shell recursion so the `R downarrow 0` boundary becomes an actual limit point rather than an uncontrolled passage through the giant-component regime.

If that route yields no movement, a later run should use another unused triple rather than returning to B12/B24 tree-product calculations.

## 8. Verification / artifacts

No new code artifact was created. The new claims are theorem-sized identities proved completely on the page from C1 homogeneity and exact finite-matrix scaling; an exact-arithmetic checker would add no evidentiary value and would violate the new-methods-first instruction if produced merely as a receipt. The finite support-only obstruction is also analytic, not an exhaustive finite computation.

This is a **self-check**, not an independent audit. No closure is claimed and no audit was requested from another task.

## 9. Ledger delta for the shared maintainer

```text
track: HARD7-02
target: Campbell-O'Rourke 2022 Question 1.8
status: PARTIAL / source OPEN_BY_BOUNDED_SEARCH
metric: S = exact full-source transformation laws theta -> mu
before: 4
after: 5
movement: +1
new_counted_law: mu_{alpha,s^alpha theta}=D_s#mu_{alpha,theta}, s>0
new_structural_reduction: mu_theta = D_{m(theta)^(1/alpha)}#F_alpha((q#theta)/m(theta))
methods: B4,B19,B23
unchanged_streak: 0
section_I: not triggered
artifacts: none warranted this run
```

No shared-root file was edited by HARD7-02.