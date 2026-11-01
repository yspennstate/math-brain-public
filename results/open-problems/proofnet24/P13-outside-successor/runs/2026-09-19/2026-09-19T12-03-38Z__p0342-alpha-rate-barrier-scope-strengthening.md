Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `M_P0342 = 2/2 -> 2/2`; NEW MATHEMATICAL SCOPE STRENGTHENING: the global perturbation family `Phi_alpha` has a sharp `sqrt(n)` phase boundary at `alpha=1/2`. Methods actually tried: B5, B23, B27.**

# P13 / P0342 — square-root stability barrier for fringe-to-finite CLT transfer

UTC run time: 2026-09-19T12:03:38Z  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`  
Own root: `proofnet24/P13-outside-successor/`

## 1. Continuity, ownership, exclusions, and recovered baseline

This run continues the current exclusive P13 successor `P0342`; it does not reopen the retired I0051 clade-covariance target, the six-run C0021 handoff, or any peer-owned claim.

The controlling canonical claim is `operations/claims/P0342.md`. It freezes the single functional `Theta=Psi+Phi`, the exact denominator-two metric `M_P0342`, and the source as Aldous--Janson Open Problem 12. The immediately preceding immutable P13 report is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T11-25-07Z__p0342-reverse-hd-liouville-fringe-clt-metric-complete.md`.

That report proved the remaining positive-variance fringe CLT and moved the frozen source metric `1/2 -> 2/2`. Therefore the source metric is already mathematically complete on P13's page. This invocation does **not** rename the metric, invent a third obligation, or count a strengthening as source-metric movement.

The mandatory I0054 screen was checked first. The newest recovered R11 report is

`runs/R11/2026-09-19T11-37-52Z_i0054-quenched-rademacher-u046-c067-b73e.md`,

which moves R11's own author-side model-class metric `66 -> 67` and still keeps I0054 PARTIAL at source/campaign level. I0054 remains exclusively occupied by R11; P13 did not touch it.

I reread the owner directive at anchor `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the P0342 claim and two newest P13 reports, the latest I0054 neighbor, and repository searches for P0342/P12/P26 audit state. No P0342 end-to-end PASS from P26 or a distinct OTHER track was recovered. Historical P12 audits concern the retired I0051 target and do not count for this successor.

## 2. Source scope and fresh literature check, 2026-09-19 UTC

Source: David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 12, section 4.10.

The source first discusses first-order fringe averages for “suitable functionals,” then asks in Open Problem 12 whether, **for a given functional**, a CLT for the stationary fringe-process sum must also hold for the corresponding finite `DTCS(n)` leaf sum. The current P0342 construction is therefore a counterexample to the literal universal implication, while a strengthened problem restricted to local/stabilizing functionals remains a separate question and is not claimed refuted here.

Fresh dated searches on 2026-09-19 used combinations of `2303.02529 Open Problem 12`, `critical beta-splitting fringe CLT`, `DTCS finite fringe transfer`, `reverse harmonic descent ergodic`, and recent 2026 critical-beta papers. The author’s current beta-splitting page still lists the Overview/Open-Problems paper and later parts; I found no checked author update explicitly resolving Open Problem 12. Brandenberger--Chin--Mossel’s 2025 paper explicitly advertises answers to Open Problems 5 and 6 and partial progress on 8, not 12. The August 2026 fragmentation/height paper and the September 2026 height/separation papers address other beta-splitting questions, not this fringe-to-finite transfer statement. This is bounded negative evidence only, not a global openness or novelty certificate.

The source PDF page inspection succeeded. One direct experimental arXiv HTML route for a later paper was unavailable, but its abstract/source page remained accessible; no mathematical conclusion is based on that failed rendering.

## 3. Frozen completed witness and why this run studies a family

The completed frozen witness is

\[
\Theta=\Psi+\Phi,
\]

where `Psi` is the bounded size-three orientation mark and the historical finite-tree perturbation is

\[
\Phi(T)=n^{-1/4}(B_n-p_n)
\]

on an `n`-leaf finite tree, with `Phi=0` on infinite fringe trees. Here

\[
B_n=1_{\{R_n\le r_n\}},\qquad r_n=\lfloor\sqrt n\rfloor,
\]

and `R_n` is the smaller original root-clade size. The exact root-split computation already proved

\[
p_n:=P(B_n=1)
=\frac{H_{r_n}+\sum_{i=1}^{r_n}(n-i)^{-1}}{H_{n-1}}
\longrightarrow\frac12.
\tag{3.1}
\]

The preceding two runs prove simultaneously for this single `Theta`:

\[
\frac1{\sqrt m}\sum_{i=0}^{m-1}\Theta(T_i)
\Rightarrow N\!\left(0,\lambda_3\right),
\qquad
\lambda_3=\frac3{2\pi^2}>0,
\tag{3.2}
\]

while the corresponding centered finite `DTCS(n)` normalized sums are non-tight. This is the already-completed denominator-two metric.

The new question is not another source obligation. It asks how fast a **global but continuous** finite-tree perturbation must vanish before it becomes harmless at the source’s `sqrt(n)` scale.

For `alpha>0`, define

\[
\Phi_\alpha(T)
=
\begin{cases}
 n^{-\alpha}(B_n(T)-p_n),&T\text{ finite with }n\ge9\text{ leaves},\\
 0,&T\text{ infinite or }n<9,
\end{cases}
\tag{3.3}
\]

and

\[
\Theta_\alpha:=\Psi+\Phi_\alpha.
\tag{3.4}
\]

The original frozen witness is the member `alpha=1/4`.

## 4. Preliminary facts for the whole family

### Lemma 1 — bounded continuity and first-order invisibility

For every `alpha>0`, `Phi_alpha` is bounded and continuous in the same local topology used for the historical P0342 packet. It vanishes identically on every infinite fringe tree. Moreover for every finite `n`-leaf realization,

\[
\left|\frac1n\sum_{i=1}^n\Phi_\alpha(T_i^{(n)})\right|
= n^{-\alpha}|B_n-p_n|
\le n^{-\alpha}\to0.
\tag{4.1}
\]

#### Proof

The bound `|Phi_alpha|<=n^{-alpha}<=1` is immediate. Every finite rooted bounded-degree tree is isolated after a sufficiently large rooted ball is specified. If finite trees converge locally to an infinite tree, their leaf counts tend to infinity; hence `|Phi_alpha|<=n^{-alpha}->0`, which proves continuity at infinite trees. Rerooting a finite tree at another leaf does not alter its leaf count or its unique original degree-two root, so all `n` rerootings have the same `Phi_alpha` value. Equation (4.1) follows. `square`

Thus every `Theta_alpha` has exactly the same stationary fringe process as `Psi`, and by the already-proved fringe theorem,

\[
\boxed{
\frac1{\sqrt m}\sum_{i=0}^{m-1}\Theta_\alpha(T_i)
\Rightarrow N\!\left(0,\frac3{2\pi^2}\right)
\quad\text{for every }\alpha>0.
}
\tag{4.2}
\]

### Lemma 2 — exact conditional symmetry, moments, and orthogonality

Let

\[
Z_n:=\sum_{i=1}^n\Psi(T_i^{(n)}),
\qquad
X_n:=Z_n/\sqrt n.
\tag{4.3}
\]

Let `G_n` be the sigma-field exposing the entire unoriented clade/split-size scaffold, including the root-split indicator `B_n`, but not the left/right orientation of a size-three `1|2` split. If `N_3(n)` is the number of size-three clades, then conditional on `G_n`,

\[
Z_n=\sum_{r=1}^{N_3(n)}\varepsilon_r
\tag{4.4}
\]

with independent Rademacher signs `epsilon_r`. Since distinct size-three clades are disjoint,

\[
N_3(n)\le n/3.
\tag{4.5}
\]

Consequently

\[
E[X_n\mid G_n]=0,
\quad
E[X_n^2\mid G_n]=\frac{N_3(n)}n,
\quad
E[X_n^4\mid G_n]
=\frac{3N_3(n)^2-2N_3(n)}{n^2}.
\tag{4.6}
\]

In particular

\[
E X_n^2\le\frac13,
\qquad
E X_n^4\le\frac13.
\tag{4.7}
\]

For every `alpha`, if

\[
Y_n^{(\alpha)}:=n^{1/2-\alpha}(B_n-p_n),
\tag{4.8}
\]

then `Y_n^(alpha)` is `G_n`-measurable and

\[
\boxed{E[X_nY_n^{(\alpha)}]=0.}
\tag{4.9}
\]

#### Proof

The recursive ordered `DTCS` construction makes the internal orientation of each distinct size-three clade an independent fair `1|2` versus `2|1` choice, because `q(3,1)=q(3,2)=1/2`. The conditional second moment is the standard Rademacher value `K`; the fourth moment of a sum of `K` independent Rademachers is `3K^2-2K`. Dividing by the powers of `n` and using `K=N_3(n)<=n/3` gives (4.6)--(4.7). Finally, because `B_n` depends only on the unoriented root split and is `G_n`-measurable,

\[
E[X_nY_n^{(\alpha)}]
=E\bigl[Y_n^{(\alpha)}E(X_n\mid G_n)\bigr]=0.
\]

`square`

## 5. B5/B23/B27 theorem — the exact square-root phase boundary

### Theorem 3 — `Phi_alpha` phase diagram

For the family `Theta_alpha=Psi+Phi_alpha`, write the centered finite normalized sum

\[
W_n^{(\alpha)}
:=\frac1{\sqrt n}\sum_{i=1}^n\Theta_\alpha(T_i^{(n)})
=X_n+Y_n^{(\alpha)}.
\tag{5.1}
\]

Then:

1. If `0<alpha<1/2`,

\[
|W_n^{(\alpha)}|\xrightarrow{p}\infty.
\tag{5.2}
\]

In particular the finite normalized sums are non-tight.

2. If `alpha=1/2`, the finite normalized sums cannot converge to the same fringe Gaussian

\[
N\!\left(0,\lambda_3\right),
\qquad \lambda_3=\frac3{2\pi^2}.
\tag{5.3}
\]

Thus even a global perturbation whose per-leaf magnitude is only `O(n^{-1/2})` can break the source’s second-order transfer.

3. If `alpha>1/2`,

\[
W_n^{(\alpha)}-X_n=Y_n^{(\alpha)}\longrightarrow0
\quad\text{deterministically}.
\tag{5.4}
\]

Hence this perturbation cannot change any subsequential finite `sqrt(n)`-scale limit of the local mark `Psi`.

#### Proof of (1): `alpha<1/2`

By (3.1), for all sufficiently large `n`, both `p_n` and `1-p_n` exceed `1/3`. Therefore

\[
|Y_n^{(\alpha)}|
=n^{1/2-\alpha}|B_n-p_n|
\ge\frac13n^{1/2-\alpha}
\quad\text{a.s.}
\tag{5.5}
\]

Fix `M<infinity`. If `|W_n^(alpha)|<=M`, then

\[
|X_n|
\ge\frac13n^{1/2-\alpha}-M.
\]

Using `E X_n^2<=1/3`,

\[
P(|W_n^{(\alpha)}|\le M)
\le
\frac{1/3}{(n^{1/2-\alpha}/3-M)^2}
\longrightarrow0.
\tag{5.6}
\]

This is exactly (5.2). `square`

#### Proof of (2): the critical exponent `alpha=1/2`

Now

\[
Y_n^{(1/2)}=B_n-p_n,
\tag{5.7}
\]

so `E Y_n=0` and

\[
E[Y_n^2]=p_n(1-p_n)\longrightarrow\frac14.
\tag{5.8}
\]

By the exact orthogonality (4.9),

\[
E[(W_n^{(1/2)})^2]
=E X_n^2+p_n(1-p_n)
\ge p_n(1-p_n).
\tag{5.9}
\]

Therefore

\[
\liminf_n E[(W_n^{(1/2)})^2]\ge\frac14.
\tag{5.10}
\]

The family of squares is uniformly integrable. Indeed, using `(a+b)^4<=8(a^4+b^4)`, (4.7), and `|Y_n|<=1`,

\[
\sup_n E[(W_n^{(1/2)})^4]
\le8\left(\frac13+1\right)
=\frac{32}{3}<\infty.
\tag{5.11}
\]

Suppose for contradiction that the finite normalized sums had the same limit as the fringe sums:

\[
W_n^{(1/2)}\Rightarrow N(0,\lambda_3),
\qquad
\lambda_3=\frac3{2\pi^2}.
\]

Convergence in distribution plus uniform integrability of the squares would imply

\[
E[(W_n^{(1/2)})^2]\longrightarrow\lambda_3.
\tag{5.12}
\]

But

\[
\lambda_3=\frac3{2\pi^2}<\frac14,
\tag{5.13}
\]

because `pi^2>6`. Equations (5.10) and (5.12) contradict each other. Thus the same fringe Gaussian limit is impossible. `square`

#### Proof of (3): `alpha>1/2`

Since `|B_n-p_n|<=1`,

\[
|Y_n^{(\alpha)}|
\le n^{1/2-\alpha}\longrightarrow0.
\tag{5.14}
\]

This proves deterministic convergence (5.4). Therefore `W_n^(alpha)` and `X_n` have the same subsequential weak limits whenever either is tight, by Slutsky. No finite CLT for `Psi` alone is asserted or needed. `square`

## 6. What the theorem says — and what it does not say

The phase boundary is exact for this perturbation mechanism:

\[
\boxed{
\alpha<\tfrac12:\text{ dominant/non-tight};\qquad
\alpha=\tfrac12:\text{ CLT-scale and still destructive};\qquad
\alpha>\tfrac12:\text{ asymptotically invisible at }\sqrt n\text{ scale}.
}
\tag{6.1}
\]

This sharpens the completed `alpha=1/4` witness in two ways. First, it gives a continuum of literal-source counterexamples for every `0<alpha<1/2`. Second, the boundary case `alpha=1/2` shows that non-tightness is not essential: an `O(n^{-1/2})` global discrepancy can already force a variance mismatch with the positive-variance fringe Gaussian.

The theorem does **not** say that `o(n^{-1/2})` pointwise convergence is universally sufficient for every fringe-to-finite CLT theorem. It proves only that for this explicit root-split perturbation, `o(n^{-1/2})` makes the perturbation itself negligible at the normalized-sum scale. A repaired theorem could instead use locality, stabilization, cancellation, mixing, or a quantitative aggregate finite/infinite approximation estimate. The source’s informal word “suitable” leaves room for such a strengthened formulation.

## 7. Method accounting

### B5 — ADD A PARAMETER AND DIFFERENTIATE/COMPARE: succeeded

The historical amplitude `n^{-1/4}` was embedded in the family `n^{-alpha}`. The normalized perturbation has scale `n^{1/2-alpha}`; equivalently its logarithmic derivative with respect to `alpha` is `-log n`, exposing the unique transition at `alpha=1/2`. This turned one counterexample into a phase diagram.

### B23 — DO WHAT THE PROPOSER DID NOT EXPECT: succeeded

Instead of only falsifying transfer, I tested the strongest immediate repair suggested by the source context: quantitative closeness of finite-tree functional values to their infinite-fringe values. The boundary case shows that even `O(n^{-1/2})` per-leaf global discrepancy is not enough for the same `sqrt(n)` CLT; one needs smaller error or structural cancellation/locality.

### B27 — SWAP THE QUANTIFIERS: succeeded

The one historical witness at `alpha=1/4` was replaced by an all-`alpha` statement. The proof separates the entire parameter range into the three exact regimes above, with the critical exponent proved rather than inferred heuristically.

This triple differs from the two preceding P0342 triples B3/B18/B30 and B1/B11/B25.

## 8. Verification scope

The new result is analytic and all theorem-sized claims are proved on the page. It introduces no bounded finite enumeration claim requiring a new exact-arithmetic checker. I therefore did not manufacture a new checker or receipt-only artifact.

The previous P0342 exact self-check remains a **P13 self-check only** for the earlier finite combinatorics/root-split constants; it is not relabeled as evidence for this new phase-diagram theorem and is not an independent audit.

The B5/B23/B27 idea was written before this proof at

`proofnet24/P13-outside-successor/artifacts/2026-09-19/2026-09-19T12-03-38Z__p0342_b5_b23_b27_rate_barrier_idea.md`.

It was created at commit

`6499d5e8e9a9803480f430bb9ec8c39507c42f15`

and read back at that exact commit with blob

`df312a5b593197f74760862b5dfaf2ce48d2695e`.

## 9. Closure gates remain unchanged

`P0342` remains

`CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`.

The source metric remains `2/2`; source-exact work is not reopened and no stagnation/rotation counter is advanced merely because closure auditing is pending.

Campaign closure still requires a P26 independent end-to-end audit, one distinct OTHER-track end-to-end audit (the owner’s P12 directed duty follows the current P13 successor), and a final source-specific prior-art review. Repository searches in this invocation did not recover such a P0342 PASS. Historical P12 passes on I0051 do not transfer to P0342.

No paper folder is created before those gates pass.

## 10. Structured `ledger_delta` for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  canonical_id: P0342
  source: Aldous-Janson arXiv:2303.02529v3 Open Problem 12 section 4.10
  lane: CLOSABLE_OUTSIDE
  frozen_witness: Theta=Psi+Phi_(alpha=1/4)
  metric_name: M_P0342
  metric_denominator: 2
  metric_before: 2
  metric_after: 2
  source_metric_movement: false
  metric_complete: true
  new_scope_strengthening:
    family: Theta_alpha=Psi+Phi_alpha
    theorem: square-root perturbation phase boundary at alpha=1/2
    alpha_lt_half: finite normalized sums diverge in absolute value in probability
    alpha_eq_half: same fringe Gaussian impossible by exact orthogonality plus second-moment mismatch and uniform integrability
    alpha_gt_half: perturbation is deterministically o(1) at sqrt(n) scale
  methods: [B5, B23, B27]
  source_scope_guard: literal Open Problem 12 implication only; no claim against a strengthened local/stabilizing formulation
  prior_art_scope: bounded 2026-09-19 search found no checked exact OP12 resolution; not a worldwide openness or novelty certificate
  audit_requirements_remaining:
    - P26 independent end-to-end P0342 audit
    - one distinct OTHER-track end-to-end P0342 audit; P12 directed duty follows current successor
  self_check_status: prior P13 exact checker retained as self-check only; no new finite-core checker needed for analytic theorem
  i0054_disposition: exclusively occupied by R11; latest recovered peer metric 66->67; untouched by P13
  shared_root_edits: none
```

## 11. Final status for this invocation

`P0342 = CLAIMED / METRIC-COMPLETE / SOURCE-REFUTATION-CANDIDATE / AUDITS-PENDING`, with a new proved square-root stability barrier around the completed counterexample.

No I0051 restart, C0021 restart, I0054 takeover, new canonical claim, peer edit, shared-root ledger overwrite, scheduler modification, email/Drive action, public post, paid compute, permission change, workflow execution, force-push, or external contact was performed.
