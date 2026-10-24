Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **SCREEN MOVEMENT on D0029: the non-B-convex half is reduced completely (`R^B_{∞,∞}=2β`), all finite-dimensional spaces and all `ℓ_p`, `1<p<∞`, are put in the α-equivalence class; D0029 remains `OPEN_CURRENT_BOUNDED / HARD / NOT_READY_CLOSABLE`, so no successor metric is admitted. I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. Methods used: B18, B11, B21.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-runtime telemetry, so I do not claim GPT-6 / maximum.

# R08 rotation screen — D0029 Banach-space dependence dichotomy

## 1. Continuity / exclusions recovered before research

I re-read the controlling repository surfaces before new work: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the latest R08 report, the canonical historical `operations/claims/I0082.md`, and the relevant D-intake rows. The controlling queue currently says that merely listed/PENDING candidates are not READY and that the latest refresh certified zero new READY rows.

The native prompt still names Hasebe--Ueda Problem 3.11 / I0082, but the immutable R08 history controls: I0082 is already retired after six unchanged runs at `2/3`, and the later F0083 fixed expanding-tube candidate was also retired after six unchanged runs. I did not reopen either route.

Direct repository search found the D0029 intake/catalog/attempt records and **no canonical `operations/claims/D0029.md` or active D0029 owner** in this bounded ownership check. That makes ownership clear enough to *screen*, not to dispatch: the controlling queue still requires a source/current-literature check and a genuinely CLOSABLE frozen metric before admission.

## 2. Source and current-literature check

Source: R. C. Bradley, *Basic Properties of Strong Mixing Conditions. A Survey and Some Open Questions*, Probability Surveys 2 (2005), Question 1, Section 1.2. For a nontrivial real Banach space `B`, Bradley defines

\[
R^B_{\infty,\infty}(\mathcal A,\mathcal C)
=
\sup
\frac{\left|\mathbb E\langle X,Y\rangle-
\langle \mathbb EX,\mathbb EY\rangle\right|}
{\|\|X\|_B\|_\infty\,\|\|Y\|_{B^*}\|_\infty}
\]

over simple `B`-valued `A`-measurable `X` and simple `B*`-valued `C`-measurable `Y`, and asks whether this coefficient is always equivalent either to `α` or to `β`.

The same source records: for any nontrivial Hilbert space it is equivalent to `α`; for `B=ℓ_∞,ℓ_1,c_0`, it is exactly `2β`; and Bradley's 2001 *A Restricted Dichotomy of Equivalence Classes for Some Measures of Dependence* proves only a restricted dichotomy under a bounded `ψ*` hypothesis. Bradley explicitly says the unrestricted question remains open.

Fresh bounded searches on 2026-09-18 for the exact title/question, `R^B_{∞,∞}`, Banach-space dependence coefficients, and later Bradley follow-ups again found the 2001 restricted result and the 2005 survey, but no later primary paper claiming the unrestricted dichotomy. This is **bounded negative evidence only**, not a worldwide novelty/open-status certificate.

The new work below should also be treated conservatively for priority: the mechanism is standard local Banach-space geometry (finite representability, Hahn--Banach, Grothendieck, bilinear interpolation). I prove the statements here because the repository's old D0029 attempt only conjectured the B-convex split and did not supply these proofs; I do **not** claim that these reductions are absent from older functional-analysis literature.

## 3. B18 — say it in another language: covariance matrices

Fix finite partitions `(A_i)_{i=1}^m` of `Ω` in `A` and `(C_j)_{j=1}^n` in `C`, and put

\[
d_{ij}=P(A_i\cap C_j)-P(A_i)P(C_j).
\]

Then every row and every column of `D=(d_{ij})` sums to zero. Define the Banach amplification norm

\[
\Gamma_B(D)
:=
\sup_{\|x_i\|_B\le1,\ \|y_j\|_{B^*}\le1}
\left|\sum_{i,j} d_{ij}\langle x_i,y_j\rangle\right|.
\]

Taking the supremum over all finite partitions gives `R^B_{∞,∞}`. Meanwhile

\[
2\beta(\mathcal A,\mathcal C)
=
\sup_{(A_i),(C_j)}\sum_{i,j}|d_{ij}|,
\]

and, because `D` has zero row/column sums,

\[
4\alpha_D
=
\sup_{\varepsilon_i,\delta_j\in\{-1,1\}}
\left|\sum_{i,j}d_{ij}\varepsilon_i\delta_j\right|,
\]

where `α_D=max_{I,J}|sum_{i∈I,j∈J}d_ij|`. Thus D0029 is a uniform finite-matrix/tensor-norm question, not intrinsically a stochastic-process question.

Two universal bounds follow immediately:

\[
4\alpha(\mathcal A,\mathcal C)
\le R^B_{\infty,\infty}(\mathcal A,\mathcal C)
\le 2\beta(\mathcal A,\mathcal C).
\tag{3.1}
\]

For the upper bound, `|<x_i,y_j>|≤1`, hence `Γ_B(D)≤sum|d_ij|`. For the lower bound, choose `x∈B`, `y∈B*` with `||x||=||y||=1`, `y(x)=1`, and for events `A,C` use

\[
X=(2\mathbf1_A-1)x,\qquad Y=(2\mathbf1_C-1)y.
\]

Their covariance is exactly `4(P(A∩C)-P(A)P(C))`.

## 4. B11 — dualize: exact beta class for every non-B-convex space

### Theorem 4.1
If `B` fails to be B-convex, then for every pair of sigma-fields

\[
\boxed{R^B_{\infty,\infty}(\mathcal A,\mathcal C)=2\beta(\mathcal A,\mathcal C).}
\tag{4.1}
\]

### Proof
A classical characterization of failure of B-convexity is that `ℓ_1` is finitely representable in `B`: for every `m` and every `ε>0` there exists an embedding

\[
T:\ell_1^m\to B
\]

which, after rescaling, satisfies

\[
\|T\|\le1,\qquad \|T^{-1}\|\le1+\varepsilon.
\tag{4.2}
\]

Fix arbitrary finite partitions and their matrix `D=(d_ij)`. Set `x_i=Te_i`. For each column `j`, define on the finite-dimensional range `E=T(ℓ_1^m)`

\[
\varphi_j(Ta)
=
\sum_{i=1}^m \operatorname{sgn}(d_{ij})a_i.
\]

For `z=Ta`, (4.2) gives

\[
|\varphi_j(z)|\le\|a\|_1\le(1+\varepsilon)\|z\|_B,
\]

so `||φ_j||≤1+ε`. Hahn--Banach extends `φ_j` to `\widetilde\varphi_j∈B*` with the same norm. Put

\[
y_j=(1+\varepsilon)^{-1}\widetilde\varphi_j.
\]

Then `||x_i||≤1`, `||y_j||≤1`, and

\[
\sum_{i,j}d_{ij}\langle x_i,y_j\rangle
=
\frac1{1+\varepsilon}\sum_{i,j}|d_{ij}|.
\]

Hence

\[
R^B_{\infty,\infty}
\ge \frac{2}{1+\varepsilon}\beta.
\]

Let `ε↓0` and combine with the universal upper bound in (3.1). This proves (4.1). ∎

### Consequence
The unrestricted Bradley question is automatically settled on the entire **non-B-convex** side: those spaces are in the beta class, in fact with exact equality `R^B=2β`. Therefore any genuinely unresolved example/counterexample must be **B-convex** (equivalently, of nontrivial type / excluding uniform `ℓ_1^n`).

## 5. B21 — ask who else has this shape: the B-convex side and interpolation

The remaining side has the shape of a Grothendieck/interpolation problem. Two additional classes can be put rigorously into the alpha class.

### Theorem 5.1 — finite-dimensional B
For every fixed nonzero finite-dimensional Banach space `B`, `R^B_{∞,∞}` is equivalent to `α`.

Indeed, choose an isomorphism `S:B→ℓ_2^d` with distortion

\[
D_B=\|S\|\,\|S^{-1}\|<\infty.
\]

For every covariance matrix `D`, Grothendieck's inequality on the Hilbert amplification gives

\[
\Gamma_B(D)
\le D_B\Gamma_{\ell_2}(D)
\le 4D_BK_G\alpha_D.
\]

Together with `4α≤R^B` from (3.1), this is quantitative equivalence.

### Theorem 5.2 — all classical `ℓ_p`, `1<p<∞`
For every `1<p<∞`, `R^{ℓ_p}_{∞,∞}` is equivalent to `α`.

For `1<p≤2`, write

\[
\theta=2(1-1/p),\qquad
\frac1p=1-\frac\theta2.
\]

For a finite covariance matrix `D`, consider its bilinear form simultaneously on

\[
\ell_\infty^m(\ell_1^N)\times\ell_\infty^n(\ell_\infty^N)
\]

and

\[
\ell_\infty^m(\ell_2^N)\times\ell_\infty^n(\ell_2^N).
\]

At the first endpoint its norm is at most `sum|d_ij|≤2β`; at the Hilbert endpoint, Grothendieck gives at most `4K_G α`. Bilinear complex interpolation, using

\[
[\ell_1^N,\ell_2^N]_\theta=\ell_p^N,
\qquad
[\ell_\infty^N,\ell_2^N]_\theta=\ell_{p'}^N,
\]

yields

\[
\Gamma_{\ell_p}(D)
\le
(2\beta)^{1-\theta}(4K_G\alpha)^\theta
\le
2^{1-\theta}(4K_G)^\theta\alpha^\theta.
\tag{5.1}
\]

Finite-coordinate truncation passes the estimate from `ℓ_p^N` to `ℓ_p`. Combined with `4α≤R^{ℓ_p}`, this is equivalence. For `p>2`, use reflexivity and the exact dual symmetry

\[
R^{\ell_p}_{\infty,\infty}(\mathcal A,\mathcal C)
=
R^{\ell_{p'}}_{\infty,\infty}(\mathcal C,\mathcal A),
\]

where `p'<2`.

Again, I am **not** making a priority claim for Theorems 5.1--5.2; the source itself points to interpolation theory, so these should be presumed potentially classical until a dedicated older-literature audit says otherwise. Their value here is that they identify the correct residual obstruction instead of leaving the old D0029 B-convexity conjecture as a heuristic.

## 6. Exact remaining obstruction

For a B-convex infinite-dimensional `B`, the source question would be answered on the alpha side by a dimension-free modulus

\[
\boxed{
\Gamma_B(D)\le \omega_B(\|D\|_{\rm cut}),
\qquad \omega_B(t)\downarrow0\quad(t\downarrow0),
}
\tag{6.1}
\]

uniformly over all feasible finite covariance matrices `D` with bounded total variation. Here `||D||_cut=max_{I,J}|sum_{i∈I,j∈J}d_ij|=α_D`.

This is precisely where finite-dimensional approximation stops helping: every *fixed* finite-dimensional subspace has a finite Banach--Mazur distance to Hilbert space, but those distortion constants can diverge with dimension. B-convexity supplies nontrivial type, not an immediately available dimension-free Hilbert distortion. Conversely, to refute Bradley's dichotomy one needs a B-convex space and matrices `D_k` with `α(D_k)→0` while `Γ_B(D_k)` stays bounded away from zero, yet without driving the coefficient all the way to the beta class.

That residual is theorem-sized local Banach-space geometry, not a finite candidate/checker problem. It therefore fails the R08 **CLOSABLE** admission test in this run.

## 7. Section-B method accounting

- **B18 (say it in another language):** succeeded. Rewrote D0029 exactly as uniform comparison of the matrix amplification norm `Γ_B(D)` with cut norm / entrywise `ℓ_1` norm. This isolates the actual obstruction.
- **B11 (dualize):** succeeded. Finite representability of `ℓ_1` plus Hahn--Banach proves the complete non-B-convex half, `R^B=2β`.
- **B21 (ask who else has this shape):** succeeded as a scope reduction, not closure. B-convexity, Grothendieck's inequality and bilinear interpolation put finite-dimensional spaces and every `ℓ_p`, `1<p<∞`, in the alpha class and identify the missing dimension-free B-convex estimate.

These are different from R08's preceding triple B20/B22/B30.

## 8. Admission decision

**D0029 is not claimed by R08.** Bounded ownership search is clear, and bounded current-literature search did not find an unrestricted resolution, but the residual (6.1) is a HARD local-Banach-space problem. The controlling owner rule forbids converting a PENDING/HARD item into a CLOSABLE assignment merely because a useful partial theorem was proved during screening.

Therefore:

- I0082: `RETIRED/FROZEN`, metric `2/3`, retirement count `6`.
- F0083 fixed candidate route: `RETIRED/HANDED_OFF`, metric `1/2` after six unchanged runs.
- D0029: `OPEN_CURRENT_BOUNDED / OWNERSHIP_CLEAR_BOUNDED / HARD / NOT_READY_CLOSABLE`.
- R08 active successor: **none admitted**.

The next invocation should continue current-literature + ownership screening for a genuinely `READY + CLOSABLE OUTSIDE + UNASSIGNED` target rather than starting D0029 research or inventing a narrower personal target.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  native_source_prompt: I0082
  native_source_state: RETIRED_FROZEN
  native_source_metric: "2/3"
  native_source_retirement_count: 6
  prior_successor: F0083_fixed_Xi_star
  prior_successor_state: RETIRED_HANDED_OFF
  screened_target: D0029
  screened_source: "Bradley 2005, Question 1, Section 1.2"
  screened_before: "source_says_open / unverified / no current R08 metric"
  screened_after: "OPEN_CURRENT_BOUNDED / OWNERSHIP_CLEAR_BOUNDED / HARD / NOT_READY_CLOSABLE"
  proved_in_run:
    - "If B is non-B-convex, R^B_{infty,infty}=2 beta exactly"
    - "Every fixed finite-dimensional B is alpha-equivalent"
    - "For every 1<p<infinity, ell_p is alpha-equivalent"
  priority_status: "UNVERIFIED; mechanisms likely overlap classical Banach/interpolation literature"
  active_successor: null
  frozen_metric_created: false
  methods: [18, 11, 21]
  checker: "none; analytic theorem-sized arguments, no finite claim"
  status: ROTATION_SCREEN
```

## 10. Model / scheduler control note

The exposed task-management surface still provides prompt/title/schedule/timing/enabled controls but no authenticated model-family selector, reasoning-effort selector, or completed-run model telemetry. Thus the prompt text can request GPT-6 / maximum but cannot enforce or certify it from this surface. An entry that returns `You cannot modify this task` must be handled from the authorized owning context, by supported ownership/admin transfer, or by platform support; cloning a task or editing repository text does not enforce a runtime model.
