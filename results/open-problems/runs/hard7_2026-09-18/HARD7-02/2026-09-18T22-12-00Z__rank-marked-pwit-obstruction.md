Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; GPT-6/maximum was requested in prompt text, but this runtime exposes no binding model/reasoning selector or authenticated effort telemetry. **No movement in the frozen metric: `S=3 -> 3`. Methods tried: B1, B15, B20.**

# HARD7-02 run 2 — a rank-marked PWIT obstruction in the asymmetric heavy-tailed elliptic model

Status of the claimed Campbell–O'Rourke Question 1.8 target: **PARTIAL / source question still OPEN_BY_BOUNDED_SEARCH.** This run does not classify `theta_d -> mu_{alpha,theta_d}` and therefore does not increase the frozen symmetry-law count `S`. It does prove a source-level obstruction that changes the correct route: for non-swap-invariant dependence measures, the uniformly rerooted matrix has a rank-mixed depth-one heavy-edge law, not the homogeneous `PWIT(theta_d x m_alpha)` asserted in the source's Theorem 4.8. The proof is exact and asymptotic; it is not a simulation.

## 1. Continuity, exclusions, and source/current-status check

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-18T21-12-00Z__campbell-orourke-q18-symmetry-covariance.md`.

That run proved three exact finite-matrix-induced laws (`S=0 -> 3`): transpose/swap invariance, common-phase covariance, and complex-conjugation covariance, and then identified the next fork as whether the source recursion actually sees only a symmetrization of `theta_d`.

At run start and again before writing I checked the controlling HARD7/new-methods files, campaign `INDEX.md`/`RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current claim registry/search hits, the newest neighboring HARD7 reports, and the related R7-06 heavy-tailed circular-law report. Repository search still shows Campbell–O'Rourke Question 1.8 exclusively owned by HARD7-02. No posted/retired equivalent target or ownership collision appeared. The adjacent R7-06 claim `C0032` concerns an explicit all-radius density for the i.i.d. Bordenave–Caputo–Chafaï law and is distinct.

Fresh primary-source check, 2026-09-18/19 UTC:

- Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, EJP 27 (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`.
- arXiv v3 remains the displayed current version, last revised 2022-02-02.
- Definition 1.1 says that for `i<j`, the ordered pairs `(X_ij,X_ji)` are iid copies of an arbitrary atom pair `(xi_1,xi_2)`; no swap-exchangeability hypothesis is imposed.
- Condition C1 records the regular-variation angular measure `theta_d`; C2 adds nondegeneracy and `a_n/n^(1/alpha) -> c>0`, not swap symmetry.
- Question 1.8 is still printed verbatim: **“What properties of `theta_d` determine `mu_{alpha,theta_d}`?”**
- Theorem 4.8 still states that for a uniform random permutation `P_n` independent of `A_n`, `(P_n A_n P_n^T,1)` converges locally in distribution to the operator on `PWIT(theta_d x m_alpha)`.
- Remark 4.9 still says this holds for any permutation sequence, while uniform independent permutations are used later because the entries are not exchangeable.
- In the proof, (4.4-section display immediately after the definition of the permuted edge vector) defines
  `xi^n_ij=(X_{pi_n(i),pi_n(j)}/a_n, X_{pi_n(j),pi_n(i)}/a_n)`, and the subsequent argument treats the unexplored outgoing vectors as if they had the same iid `theta_d` tail law.

A bounded current-literature search on the exact title together with `Theorem 4.8`, `PWIT`, `permutation`, `erratum`, `correction`, and the `theta_d` notation found the 2022 source and bibliographic/citation pages but no erratum or later source correcting this local-convergence point, and no solution of Question 1.8. This is negative evidence only, not a worldwide novelty certificate.

Primary source used this run:

- https://arxiv.org/html/2010.01261v3
- https://arxiv.org/abs/2010.01261

## 2. Frozen metric

The claim fixed

`S = number of exact nontrivial transformation laws for theta_d -> mu_{alpha,theta_d}`

proved by this track from exact finite-matrix spectral identities.

Before: `S=3`.

After: **`S=3` (no movement).**

The theorem below is intentionally not counted as `S=4`: it is a correction/obstruction for the source's local weak limit, not a new exact transformation law for the limiting ESD.

Unchanged streak for this metric: `1`.

## 3. B15 — break swap symmetry on purpose

Let `0<alpha<1` and choose `p in (0,1)`, `p != 1/2`; for a concrete value take `p=3/4`. Let `R` be positive Pareto,

`P(R >= t)=t^{-alpha},   t>=1`,

and let `B` be Bernoulli(`p`), independent of `R`. Define the off-diagonal atom pair

`(xi_1,xi_2) = (R,0)` if `B=1`, and `(0,R)` if `B=0`.

Take the diagonal atom `zeta=0` and `a_n=n^(1/alpha)`. Then Condition C1 holds with the probability spectral measure

`theta_p = p delta_(1,0) + (1-p) delta_(0,1)`

because for every angular continuity set `D` and fixed `r>0`, the defining tail limit is exactly the corresponding axis mass times `r^{-alpha}` once `r a_n>=1`. Condition C2(ii) holds with limiting constant `1`. Condition C2(i) also holds: no nonzero complex linear functional `az+bw` vanishes on both `(1,0)` and `(0,1)`.

Thus this is not a boundary ensemble outside the source theorem. It is an explicit C2-admissible family with

`tau#theta_p = theta_(1-p) != theta_p`,

where `tau(z,w)=(w,z)`.

## 4. Exact rank-conditioned root law

Let `pi_n` be the uniform permutation associated with `P_n`, and put

`K_n := pi_n(1)`.

Then `K_n` is uniform on `{1,...,n}` and independent of the atom pairs. Conditional on `K_n=k`, the root `1` of the permuted matrix corresponds to original vertex `k`.

For an original neighbor `j>k`, the root-oriented pair is

`(X_kj,X_jk) ~ (xi_1,xi_2)`;

for an original neighbor `j<k`, it is

`(X_kj,X_jk) ~ (xi_2,xi_1)`.

The edge pairs remain mutually independent conditional on the root rank. Hence the random permutation does **not** make the root edge-pairs iid with angular law `theta_d`: it creates exactly `n-k` edges of orientation `theta_d` and `k-1` edges of orientation `tau#theta_d`.

This has a general consequence under Condition C1.

### Proposition 1 — mixed-Poisson depth-one extreme law

Let `D` be an angular continuity set for both `theta_d` and `tau#theta_d`, and fix `r>0`. Let `N_n(D,r)` count root edges of the permuted matrix whose normalized oriented pair has angle in `D` and norm at least `r` after division by `a_n`.

Set

`a = r^{-alpha} theta_d(D)`,

`b = r^{-alpha} (tau#theta_d)(D)`.

If `K_n/n -> u`, then conditionally along such a sequence

`N_n(D,r) => Poisson((1-u)a + u b)`.

With the actual uniform random root,

`N_n(D,r) => Poisson(Lambda_U) conditionally on U`,

where

`U ~ Uniform[0,1]`,

`Lambda_U=(1-U)a+U b`.

In particular the limiting void probability is

`V(a,b)= integral_0^1 exp(-((1-u)a+u b)) du`

and for `a!=b`,

`V(a,b) = (exp(-a)-exp(-b))/(b-a)`.

#### Proof

Let `q_n` be the probability that an unscaled atom pair has direction in `D` and norm at least `r a_n`, and let `q_n^tau` be the same probability after swapping coordinates. Condition C1 gives

`n q_n -> a`,  `n q_n^tau -> b`.

Conditional on `K_n=k`, independence of the unordered matrix-edge atom pairs gives the exact probability generating function

`E[s^{N_n} | K_n=k]`

`= (1-(1-s)q_n)^(n-k) (1-(1-s)q_n^tau)^(k-1)`.

If `k/n->u`, logarithms and `n q_n->a`, `n q_n^tau->b` give

`exp(-(1-s)((1-u)a+u b))`,

the pgf of the displayed Poisson law. Since `K_n/n => U` and the pgfs are bounded by one, averaging over `K_n` gives the mixed law and the stated Riemann-integral void probability. ∎

For the explicit axis family, take an open spherical cap `D` containing `(1,0)` but not `(0,1)`, with boundary containing neither atom. Then

`a=p r^{-alpha}`, `b=(1-p)r^{-alpha}`.

For `p=3/4` and `r=1`,

`V = 2(exp(-1/4)-exp(-3/4))`,

whereas `PWIT(theta_p x m_alpha)` has a Poisson(`3/4`) root count in that cap and hence void probability `exp(-3/4)`. These are unequal. Moreover the simple averaged measure `(theta_p+tau#theta_p)/2` would give void probability `exp(-1/2)`, also unequal by strict Jensen convexity. Thus the random root is not repaired by merely replacing `theta_p` by its swap average: the shared rank `U` is genuine latent information.

## 5. B20 — find exactly where the source local-convergence algorithm fails

The preceding count already contradicts the homogeneous depth-one PWIT assertion used inside the proof. There is also a direct operator-topology contradiction to Theorem 4.8 itself, so this is not merely a complaint about one proof presentation.

Put `beta=alpha/2 in (0,1)`. For the explicit axis-Pareto family define

`Q_n := || P_n A_n P_n^T delta_1 ||_2^2`.

The diagonal is zero. Conditional on `K_n=k`, the column at the root contains:

- `n-k` independent potential Pareto entries switched on with probability `1-p`;
- `k-1` independent potential Pareto entries switched on with probability `p`.

Since `R^2` has tail exponent `beta` and `a_n^2=n^(1/beta)`, the standard one-big-jump/Laplace calculation gives, for every `s>0` and `k/n->u`,

`E[exp(-s Q_n) | K_n=k]`

`-> exp(-Gamma(1-beta) s^beta ((1-u)(1-p)+u p)).`            (5.1)

For completeness, this follows from

`n(1-E exp(-s R^2/n^(1/beta))) -> Gamma(1-beta) s^beta`

and the exact Bernoulli thinning product.

Averaging over the uniform root rank gives the nondegenerate mixture

`L_mix(s)= integral_0^1 exp(-c_s((1-u)(1-p)+u p)) du`,

where `c_s=Gamma(1-beta)s^beta`.

By contrast, in the source operator `A` built from `PWIT(theta_p x m_alpha)`,

`||A delta_root||_2^2 = sum_children |y_child^(2)|^2`

is a positive `beta`-stable variable with Laplace transform

`L_PWIT(s)=exp(-c_s(1-p)).`                                  (5.2)

For `p!=1/2`, (5.1) averaged over `u` is not (5.2); for `p=3/4` the integrand decreases strictly from `exp(-c_s/4)` to `exp(-3c_s/4)`, so its average is strictly smaller than the source value `exp(-c_s/4)`.

Definition 4.4 of the source defines local convergence by strong convergence, after a vertex bijection, on every finitely supported vector. Taking the root basis vector, strong convergence would force convergence in distribution of the norm `||P_n A_n P_n^T delta_1||_2`. Equations (5.1)-(5.2) rule this out.

### Corollary 2 — exact obstruction to Theorem 4.8 as printed

For the C2-admissible family `theta_p` above with `p!=1/2`, the uniformly permuted rooted operators do **not** converge locally in distribution to the homogeneous operator on `PWIT(theta_p x m_alpha)` asserted in Theorem 4.8.

The source proof's failure is visible before the later resolvent step. Its generic-network paragraph begins with iid unordered edge weights, but after substituting

`xi^n_ij=(X_{pi(i),pi(j)},X_{pi(j),pi(i)})/a_n`,

the root vectors are not iid unless the atom-pair law is swap invariant. Conditional on the root rank they split into `theta_d` and `tau#theta_d` populations; unconditionally they retain dependence through the common root rank. The subsequent iid point-process argument therefore cannot be applied with a single intensity `theta_d x m_alpha` in this generality.

Remark 4.9 has the same obstruction in an even simpler form: the identity permutation roots at original label `1` and sees asymptotically only `theta_d`, whereas the reversing permutation roots at original label `n` and sees asymptotically only `tau#theta_d`. They cannot both converge to the same oriented PWIT unless the relevant law is swap invariant.

This is a correction to a source tool, **not** a claim that Theorems 1.5 or 1.6 are false. Those global spectral/singular-value conclusions may admit a repaired proof and possibly a different recursive description. I have not proved their negations and do not label the source question REFUTED.

## 6. B1 — change category: from an unmarked PWIT to a rank-marked branching kernel

The obstruction suggests a concrete replacement object rather than another lemma inside the homogeneous PWIT recursion.

Give every limiting vertex a type `u in [0,1]`, representing its normalized original matrix rank. Conditional on a parent type `u`, propose the offspring Poisson intensity

`K_theta(u; dv,dy)`

`= 1_{v>u} dv (theta_d x m_alpha)(dy)`

`  + 1_{v<u} dv ((tau#theta_d) x m_alpha)(dy)`,             (6.1)

where `v` is the child rank type and `y=(y^(1),y^(2))` is the pair oriented from parent to child. The root type is `U~Uniform[0,1]` for the uniform permutation used in (4.5).

Equation (6.1) exactly reproduces Proposition 1 after integrating out `v`. It also records information lost by the naive swap average: a single latent `u` controls every root edge, explaining the mixed-Poisson overdispersion.

For a fixed parent sequence `k_n/n->u`, the marked depth-one point process convergence to (6.1) follows directly from Condition C1 by splitting the deterministic rank grid at `u` and applying the Laplace-functional triangular-array Poisson limit separately on the two sides. The two sides use disjoint independent unordered edge pairs and hence are independent. This is a full depth-one statement, not a simulation.

I am **not yet claiming** full all-depth local operator convergence to the corresponding marked PWIT. The next proof obligation is to run the source's fixed-`B,H` exploration with the rank mark retained and verify inductively that: (i) sampling without replacement of finitely many child labels converges to the `dv` type kernel, (ii) collisions/shared unexplored vertices are negligible, and (iii) the square-summability/self-adjointness argument survives the type-dependent orientation. Only after that should Proposition 4.12 be replaced by a type-indexed resolvent recursion.

This route also naturally explains the exact transpose law from run 1: replacing `theta_d` by `tau#theta_d` and reflecting the rank type `u -> 1-u` leaves the uniform-root marked environment equivalent after transposition.

## 7. What this says about Question 1.8

The previous run's proposed fork was to test

`mu_theta ?= mu_((theta+tau#theta)/2)`.

This run shows that the source's homogeneous PWIT cannot decide that equality in the stated nonsymmetric model: at the local-root level, averaging `theta` and `tau#theta` destroys a persistent latent-rank variable. The right next object is the type-indexed recursion generated by (6.1), not the untyped recursion with either `theta` or its arithmetic swap average.

This does **not** prove that the final ESD distinguishes `theta` from its swap average; global spectral averaging could conceivably erase the extra type information. A source-valid next run should therefore derive the first type-sensitive resolvent statistic for the marked recursion and compare it with the homogeneous swap-average recursion. A strict difference would refute the symmetrization hypothesis; an exact collapse would identify a genuine additional invariant for Question 1.8.

## 8. Method outcomes

- **B15 BREAK THE SYMMETRY ON PURPOSE:** successful. The C2-admissible axis family `theta_p`, `p!=1/2`, isolates the orientation defect exactly.
- **B20 FIND WHY THE ALGORITHM FAILS:** successful. Uniform relabeling produces a common random rank and two tail populations, so the iid homogeneous-PWIT point-process step fails. The root-column stable norm gives an operator-topology contradiction to Theorem 4.8 as printed.
- **B1 CHANGE THE CATEGORY:** productive. Recasting the limit as a continuum-type/rank-marked branching kernel produces the candidate corrected local object (6.1) and a complete depth-one convergence statement.

No checker was manufactured: the new result is an asymptotic theorem proved on the page from exact conditional independence, regular variation, pgfs/Laplace transforms, and strong-local-convergence invariance. There is no finite enumeration claim to certify.

## 9. Runtime/configuration honesty

The repository control and current deployment records still say the native scheduler interface exposes title/prompt/schedule/timing/enabled controls but no model selector, reasoning-effort selector, authenticated runtime model/effort telemetry, or guaranteed hour-long execution. Therefore GPT-6/maximum remains text-requested only here; actual reasoning effort is `UNVERIFIED`.

The historical `You cannot modify this task` permission issue is not evidence that every context remains blocked: current `RESULTS.md` records that a later authorized context succeeded in updating P26, while other IDs have separately denied edits. The compliant workaround remains to use an authorized owner/interface context or platform support for that exact task; creating a duplicate schedule or bypassing permissions would violate policy. This run did not modify, create, enable, or disable any other schedule.

## 10. ledger_delta

```yaml
track: HARD7-02
source: Campbell-O'Rourke 2022, Question 1.8
claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
metric: exact nontrivial transformation laws S for theta_d -> mu_{alpha,theta_d}
metric_before: 3
metric_after: 3
movement: no movement
status_before: PARTIAL
status_after: PARTIAL
unchanged_count_before: 0
unchanged_count_after: 1
methods_this_run: [1, 15, 20]
proved:
  - uniform-rank root extreme count converges to a mixed Poisson law with intensity (1-U)theta + U tau#theta on angular tests
  - for an explicit C2 axis-Pareto family, the root-column squared norm converges to a nontrivial mixture of positive stable laws
  - this mixture disagrees with the homogeneous PWIT(theta_d x m_alpha) root law when theta_d is not swap invariant
  - therefore Campbell-O'Rourke Theorem 4.8 is obstructed as printed in the nonswap-symmetric C2 class
  - rank-marked kernel (6.1) gives the correct proved depth-one point-process limit
not_claimed:
  - no refutation of Theorem 1.5 or Theorem 1.6
  - no proof or disproof that mu_theta equals mu_swap-average(theta)
  - no all-depth marked-PWIT operator convergence yet
  - no novelty certificate
remaining_obligation: prove fixed-depth/all-depth marked-PWIT convergence, derive the type-indexed resolvent recursion, and test whether global ESD averaging erases or retains the latent rank variable
next_methods_suggested: [5, 11, 27]
closure_audits: 0
```
