Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed runtime/scheduler surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen metric: `S=5 -> 5`. Methods tried: B4, B5, B18.**

# HARD7-02 run 14 — exact zero-shift Hermitization scaling on the swap-symmetric cone

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question remains OPEN in bounded current-status search.**

This run leaves the completely solved axis class and attacks the interior swap-symmetric family proposed by run 13. The new result is an exact source-level theorem for the **zero-shift Hermitized/singular-value law**: for every swap-symmetric dependence measure, the entire `z=0` Hermitized root spectral law depends on `theta_d` only through the single marginal alpha-moment

\[
M_\alpha(\theta_d)=\int |w_1|^\alpha\,\theta_d(dw)
=\int |w_2|^\alpha\,\theta_d(dw).
\]

For the one-parameter interior family `vartheta_x`, this yields a closed dilation formula and a strictly monotone regularized resolvent statistic. It is genuine movement in the mathematical understanding of the source question, but **not** a sixth unit of the frozen metric `S`, because `S` counts full transformations `theta_d -> mu_{alpha,theta_d}` and this theorem is only at `z=0` Hermitization. The exact place the extension fails is also identified: for `z != 0`, the Hermitization shift couples the two tree components used below.

## 1. Continuity, repository state, ownership, and source refresh

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T09-12-00Z__axis-cstar-logarithmic-mean.md`.

At run start I re-read or refreshed:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the HARD7-02 report chain and canonical claim;
- the heavy-tail neighborhood in `probability_1000_intake_*/problems.jsonl` by repository search;
- the newest neighboring heavy-tail record, `research7_2026-09-17/R7-06/handoffs/2026-09-19T095800Z__C0032_terminal_handoff.md`.

The neighbor update is material operationally but not a collision: R7-06 has now terminally handed off C0032, the distinct Bordenave–Caputo–Chafaï explicit-density question, after its own two HARD recoveries. Repository claim searches still identify Campbell–O'Rourke Question 1.8 as owned by HARD7-02. No duplicate owner, posted equivalent, Bernoulli-singularity reassignment, or excluded author-manuscript collision was found.

### Primary source and exact question

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`:

- https://arxiv.org/abs/2010.01261
- https://doi.org/10.1214/22-EJP849

The live arXiv record checked on 2026-09-19 still lists v3, revised 2 February 2022, as the latest version. Definition 1.3 uses the finite angular dependence measure `theta_d` on the unit sphere in `C^2`; Condition C2 adds the no-complex-hyperplane condition and `a_n/n^(1/alpha) -> c>0`. Theorem 1.5 gives the deterministic singular-value limit `nu_{z,alpha,theta_d}` for every fixed `z`, and Theorem 1.6 gives the deterministic eigenvalue limit `mu_{alpha,theta_d}` under C2. Section 1.3 asks exactly:

> **Question 1.8.** What properties of `theta_d` determine `mu_{alpha,theta_d}`?

A fresh bounded literature search dated 2026-09-19 used the exact title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, dependence measure, PWIT, classification, and 2023--2026 terms. It recovered the 2022 source and Campbell–O'Rourke's later Lévy–Khintchine random-Laplacian paper (published 2023 / journal volume 2024), but no located paper claiming a full solution of Question 1.8 or the zero-shift theorem below. This is **bounded negative evidence only**, not a worldwide novelty certificate.

### Runtime/scheduler capability

The exposed scheduler/runtime surface still offers task title, prompt, schedule/timing and enabled state, but no authenticated model selector or reasoning-effort selector. Therefore this worker cannot make GPT-6/maximum binding. Changing that would require a platform surface that actually exposes authenticated model/effort controls.

The repository preserves historical `You cannot modify this task` failures for P26/P01/P03, while the current root ledger records that P26 was later editable in another authorized native context. For a task that still rejects modification, the compliant route remains the authorized owner/account/workspace interface or platform support/ownership transfer, not a duplicate schedule or permission bypass. No scheduler mutation was attempted in this run.

## 2. Frozen metric and Section-I state

The canonical claim freezes

`S = number of exact nontrivial full-source transformation laws theta_d -> mu_{alpha,theta_d}`

under the counting rule in the claim file.

Before this run: `S=5`.

After this run: **`S=5` — no movement.**

Run 13 ended with two ordinary post-STUCK1 unchanged runs. This run is therefore the **third ordinary post-STUCK1 unchanged run**. Under section I, the next HARD7-02 execution must be the `STUCK2` thinking-only recovery report: no auxiliary lemma, and it must record the exact blocker, all failed routes and failure reasons, the missing proof ingredient, the simplest still-unproved case, and the nearest solved analogue, then choose exactly one recovery route. This run does not pre-emptively write STUCK2 because the third unchanged outcome is established only at the end of the present substantive attempt.

All thirty Section-B labels have already appeared somewhere in the long HARD7-02 chain, so literal global first-use numbering is exhausted. The present triple differs from the immediately preceding B2/B6/B13 and is applied to a genuinely new interior class:

**B4 / B5 / B18.**

## 3. Idea before code: at `z=0`, Hermitization splits the tree in two

Run 13 proposed the interior family

\[
\eta_x=\operatorname{Law}\left(\sqrt{x}e^{i\phi},\sqrt{1-x}e^{-i\phi}\right),
\qquad \phi\sim\operatorname{Unif}[0,2\pi),
\]

and

\[
\vartheta_x=\frac12\left(\eta_x+\tau_\#\eta_x\right),
\qquad 0<x\le \frac12,
\]

where `tau(w_1,w_2)=(w_2,w_1)`. This is genuinely off-axis for `0<x<1/2`, swap symmetric, and source-valid.

The obvious full-law attack is dangerous. A nonunitary diagonal similarity can balance directional amplitudes on any finite **tree**, but run 13 already showed on the axis class that nonunitary tree similarity does not preserve Hermitization and therefore does not imply equality of the nonnormal limiting ESD. Repeating that route would be bookkeeping, not research.

The new observation is specific to the exact point `z=0`. If `A` is the limiting weighted tree operator, its bipartization is

\[
B_0=\begin{pmatrix}0&A\\A^*&0\end{pmatrix}.
\]

Because the underlying PWIT is a tree, hence bipartite by graph depth, the graph of `B_0` splits **exactly into two disconnected components**. In one component, even-depth edges use the first coordinate of each pair mark and odd-depth edges use the second; in the other component the roles reverse. For a swap-symmetric `theta_d`, the two coordinate projections have the same tail intensity. Thus the matrix-valued non-Hermitian recursion collapses at `z=0` to the scalar self-adjoint Lévy-PWIT law.

No code was needed to discover or prove this; the result below is analytic and has no finite exhaustive core.

## 4. B18 — say it in another language: the bipartized tree is two scalar Lévy trees

Let `theta` be a finite angular measure on the unit sphere of `C^2` satisfying

\[
\tau_\#\theta=\theta.
\]

Define

\[
M_\alpha(\theta)
:=\int |w_1|^\alpha\,\theta(dw).
\]

Swap symmetry gives automatically

\[
M_\alpha(\theta)=\int |w_2|^\alpha\,\theta(dw).
\]

Let `check(nu)_{0,alpha,theta}` denote the symmetrization on `R` of the source singular-value limit `nu_{0,alpha,theta}` from Theorem 1.5.

### Lemma 1 — exact component decomposition

For the swap-symmetric local limiting operator, the `z=0` bipartization decomposes into two rooted self-adjoint PWIT components. In either component the nonzero edge-modulus point process at every vertex has radial intensity

\[
M_\alpha(\theta)\,\alpha r^{-1-\alpha}\,dr.
\tag{4.1}
\]

#### Proof

The corrected rank-marked local kernel from earlier HARD7-02 runs is

\[
K_u(dv,dy)
=\mathbf 1_{v>u}\,dv\,\nu(dy)
 +\mathbf 1_{v<u}\,dv\,(\tau_\#\nu)(dy),
\]

with `nu=theta x m_alpha`. If `tau#theta=theta`, then `tau#nu=nu`; the rank direction therefore disappears from the mark law, and the homogeneous PWIT representation used in the source is valid for this class.

Now color the underlying tree by depth parity and lift every vertex `v` to two bipartization copies `(v,+)` and `(v,-)`. Every `B_0` edge changes both tree parity and the `+/-` copy. Hence the quantity

`depth(v) mod 2 XOR copy(v)`

is conserved. The bipartization graph is exactly the disjoint union of the two corresponding parity classes.

In the component containing `(root,+)`, an edge whose parent has even depth carries the first coordinate of its pair mark; at the next generation the selected coordinate is the second; and so on alternately. The other component has the opposite alternation. Pair marks on distinct tree edges are independent. Swap symmetry makes the first- and second-coordinate marginal tail measures equal.

Project the pair tail measure

\[
\theta(d\omega)\,\alpha r^{-1-\alpha}dr
\]

through `(r,omega) -> r omega_1`. By the Poisson mapping theorem, its nonzero radial modulus projection has intensity coefficient

\[
\int |\omega_1|^\alpha\theta(d\omega)=M_\alpha(\theta),
\]

which gives (4.1). The same calculation applies to coordinate two. Complex edge phases are removable by an exact diagonal **unitary** gauge on each tree component, with the root phase fixed. Thus each component is distributionally a standard scalar self-adjoint Lévy PWIT with radial intensity (4.1). `QED`

**B18 outcome: succeeded.** At `z=0`, the relevant dependence statistic for the entire Hermitized root law is reduced from the full bivariate angular measure to one scalar marginal alpha-moment on the swap-symmetric cone.

## 5. B4 — prove a weaker statement completely: exact zero-shift scaling theorem

Let `sigma_alpha` denote the deterministic expected root spectral measure of the standard self-adjoint Lévy PWIT whose positive edge moduli have intensity

\[
\alpha r^{-1-\alpha}dr.
\]

No particular closed density formula for `sigma_alpha` is needed.

### Theorem 2 — zero-shift Hermitization depends only on `M_alpha`

For every swap-symmetric source dependence measure `theta` as above,

\[
\boxed{
\check\nu_{0,\alpha,\theta}
=(D_{M_\alpha(\theta)^{1/\alpha}})_\#\sigma_\alpha.
}
\tag{5.1}
\]

Consequently, for two swap-symmetric measures `theta_1,theta_2` with positive `M_alpha`,

\[
\boxed{
\check\nu_{0,\alpha,\theta_1}
=
(D_{(M_\alpha(\theta_1)/M_\alpha(\theta_2))^{1/\alpha}})_\#
\check\nu_{0,\alpha,\theta_2}.
}
\tag{5.2}
\]

This statement already holds at the singular-value level under Condition C1; C2 is only needed when one asks for the full eigenvalue limit.

#### Proof

By Lemma 1, each root copy of the `z=0` bipartization sees a scalar self-adjoint PWIT whose radial edge intensity is `M alpha r^{-1-alpha}dr`, with `M=M_alpha(theta)`. If a unit-intensity Poisson process with density `alpha r^{-1-alpha}dr` is multiplied by the deterministic factor

\[
s=M^{1/\alpha},
\]

its pushforward intensity is exactly

\[
s^\alpha\alpha r^{-1-\alpha}dr
=M\alpha r^{-1-\alpha}dr.
\]

Therefore the entire rooted self-adjoint operator is distributionally `s` times the standard one. Spectral calculus then scales its root spectral measure by `D_s`. Both bipartization components have the same marginal law, so the averaged root spectral measure that identifies the deterministic symmetrized singular limit in the source is also `D_s#sigma_alpha`. This proves (5.1), and dividing the two scale factors gives (5.2). `QED`

This is a theorem-sized claim with the full argument on the page. There is no finite enumeration and no simulation. Therefore no checker-only artifact was manufactured.

**B4 outcome: succeeded.** The smallest genuinely interior class suggested by run 13 admits a complete exact output theorem at `z=0`, rather than another sampled or finite-tree statement.

## 6. B5 — add the interior parameter and differentiate it

For the run-13 family `vartheta_x`, put

\[
\beta=\frac\alpha2\in(0,1).
\]

On `eta_x`, the first coordinate has modulus `sqrt(x)`; on its swap it has modulus `sqrt(1-x)`. Hence

\[
\boxed{
M_x:=M_\alpha(\vartheta_x)
=\frac12\left(x^\beta+(1-x)^\beta\right).
}
\tag{6.1}
\]

At the Hermitian endpoint `x=1/2`,

\[
M_{1/2}=2^{-\beta}.
\]

Define the exact relative zero-shift Hermitization scale

\[
R_\alpha(x)
:=\left(\frac{M_x}{M_{1/2}}\right)^{1/\alpha}
=\left[2^{\beta-1}\left(x^\beta+(1-x)^\beta\right)\right]^{1/\alpha}.
\tag{6.2}
\]

Theorem 2 gives

\[
\boxed{
\check\nu_{0,\alpha,\vartheta_x}
=(D_{R_\alpha(x)})_\#
\check\nu_{0,\alpha,\vartheta_{1/2}}.
}
\tag{6.3}
\]

Equivalently, if

\[
G_x(\eta)=\int_\mathbb R\frac{1}{t-\eta}\,
\check\nu_{0,\alpha,\vartheta_x}(dt),
\qquad \eta\in\mathbb C_+,
\]

then for every regularization parameter `eta` in the upper half-plane,

\[
\boxed{
G_x(\eta)
=R_\alpha(x)^{-1}
G_{1/2}\!\left(\eta/R_\alpha(x)\right).
}
\tag{6.4}
\]

This is the requested kind of continuous-path/output statistic: it is an exact limiting resolvent identity, not a discretely sampled simulation.

### Strict monotonicity

For `0<x<1/2`,

\[
M_x'
=\frac\beta2\left(x^{\beta-1}-(1-x)^{\beta-1}\right)>0,
\tag{6.5}
\]

because `beta-1<0` and `x<1-x`. Thus `M_x` and `R_alpha(x)` are strictly increasing on `(0,1/2]`.

The endpoint values are

\[
\boxed{
\lim_{x\downarrow0}R_\alpha(x)
=2^{\frac12-\frac1\alpha},
\qquad
R_\alpha(1/2)=1.
}
\tag{6.6}
\]

In particular the zero-shift Hermitized laws are not constant along this interior-to-Hermitian deformation. The standard root law is not `delta_0` (the root has nonzero weighted edges almost surely), and a nondegenerate probability measure cannot be invariant under a fixed nontrivial dilation; iterating such a dilation across disjoint annuli would force all mass away from zero to vanish. Hence distinct `R_alpha(x)` give genuinely distinct measures in (6.3).

**B5 outcome: succeeded.** The proposed interior family has an exact, strictly monotone source-level Hermitized statistic, with the full parameter range and endpoints identified.

## 7. Why this does not yet move `S`: the exact `z != 0` obstruction

It would be incorrect to promote Theorem 2 to a full transformation law for `mu_{alpha,theta}`.

At nonzero spectral shift,

\[
B_z=\begin{pmatrix}0&A-zI\\(A-zI)^*&0\end{pmatrix}
\]

contains, at every underlying vertex, a same-vertex edge of weight `-z` between the `+` and `-` copies. That edge flips the conserved parity/copy bit used in Lemma 1, so the two scalar tree components are immediately coupled. The resolvent recursion becomes genuinely `2 x 2` again, and the bivariate pair statistic—including the product coordinate retained by the run-4 quotient—re-enters.

This is also why the tempting nonunitary balancing similarity is not a shortcut: it preserves eigenvalues of finite tree truncations but does not preserve the Hermitized resolvent after the `z` shift. The already solved axis family is an exact warning against that false inference.

Therefore this run proves an exact `z=0` law and a strict interior parameter statistic, but not

\[
\mu_{\alpha,\vartheta_x}
=(D_{c(x)})_\#\mu_{\alpha,\vartheta_{1/2}}
\]

or any other full-ESD transformation. No such claim is made, and `S` remains 5.

## 8. What was learned and what must happen next

The source's qualitative interpolation between iid-like and Hermitian-like dependence now has one exact quantitative coordinate on the swap-symmetric cone:

\[
M_\alpha(\theta)=\int |w_1|^\alpha\theta(dw),
\]

which completely determines the zero-shift Hermitized law. For `vartheta_x`, the exact scale is (6.2), strictly increasing from `2^(1/2-1/alpha)` to `1` as the support moves from the axis boundary toward the Hermitian orbit.

The remaining full-source obstruction is sharply localized: control of the **coupled two-component recursion for at least one nonzero `z`** in a way that detects or classifies its dependence on `x`. A mere tree eigenvalue similarity, product-only statistic, or numerical spectrum will not do.

Because this is the third consecutive ordinary no-movement run after STUCK1, section I now activates. The next execution must be STUCK2 and must not append another auxiliary theorem. It should decide one recovery route only after recording the exact coupled-recursion blocker and the nearest solved analogue.

## 9. Closure / audit / persistence state

Question 1.8 remains **PARTIAL**. No paper folder is created and no closure audit is requested. The new theorem is self-contained on the page but is a restricted `z=0` statement, not source closure.

No exact code/output artifact was added: there is no finite exhaustive claim in this run, and producing an algebra checker for (6.1)--(6.6) would violate the new-methods-first allocation without strengthening the proof.

No shared root ledger was edited. The coordinator/P26 shared-ledger ownership rule is preserved.

```yaml
ledger_delta:
  track: HARD7-02
  source: Campbell-O'Rourke 2022 Question 1.8
  metric: S
  before: 5
  after: 5
  movement: false
  status: PARTIAL
  source_status: OPEN_IN_BOUNDED_2026-09-19_SEARCH
  methods: [B4, B5, B18]
  post_STUCK1_ordinary_unchanged_count_before: 2
  post_STUCK1_ordinary_unchanged_count_after: 3
  hard_stuck_recoveries_used: 1
  hard_stuck_recoveries_allowed: 2
  section_I_next_run_required: STUCK2
  new_result: "For every swap-symmetric dependence measure, check(nu) at z=0 is a scalar dilation determined only by M_alpha=int|w1|^alpha dtheta. For vartheta_x, the exact relative scale is [2^(alpha/2-1)(x^(alpha/2)+(1-x)^(alpha/2))]^(1/alpha), strictly increasing in x."
  blocker: "For z != 0 the -z same-vertex Hermitization edges couple the two scalar bipartization components, restoring the full 2x2 recursion."
  closure: false
```
