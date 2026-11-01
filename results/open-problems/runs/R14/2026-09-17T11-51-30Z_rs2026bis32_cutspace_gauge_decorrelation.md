Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `D_bis: 2 -> 2`; unchanged count `2 -> 3`, so the next R14 invocation is mandatory `STUCK-RECOVERY-1`. Methods actually tried: #1 CHANGE THE CATEGORY, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS.**

# R14 — RS-2026-BIS32: affine cut-space geometry, cubic frustration matchings, and a gauge-decorrelation reduction

Status: **OPEN / PARTIAL**. Active exclusive target remains `RS-2026-BIS32`, Afonso S. Bandeira's Randomstrasse 101 Conjecture 32 (Min and Max Bisections), tracing to Zdeborová--Boettcher. The original negative-margin spherical-perceptron target remains handed off and is **not reopened**; its last supported rigorous bracket remains

\[
6.30297437506\le \alpha_c(-1)\le12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

The intervening I0089 target also remains handed off. I continued from `runs/R14/2026-09-17T09-53-05Z_rs2026bis32_centered-defect-local-obstruction.md` and preserved the newer R14 artifacts already present at `2026-09-17T11-35-15Z` rather than re-deriving them.

## 1. Continuity, repository read, source status, and literature correction

At run start I recovered the campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, current `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the canonical ownership claim `operations/claims/RS-2026-BIS32.md`, the newest complete R14 report, and current neighboring R13/R15 evidence. The very large intake JSONL collection remains connector-truncated and was therefore used through targeted source/ownership searches rather than falsely claimed as a row-by-row complete rendering.

The live Randomstrasse page was checked again on 2026-09-17. It still states, for fixed integer `d>=3`, even `n`, and uniform simple `d`-regular `G_d`,

\[
\frac{\mathbf E\,\mathrm{MinBis}(G_d)+\mathbf E\,\mathrm{MaxBis}(G_d)}{n}
=\frac d2+o(1).
\tag{BIS32}
\]

The page is still explicitly labeled Conjecture 32. The current fixed metric is

\[
D_{\rm bis}:=\sup\{D\ge2:\text{(BIS32) is rigorously proved for every fixed }3\le d\le D\}.
\]

It remains `D_bis=2`.

A useful literature correction: Gheissari--Perkins--Yap, arXiv:2511.16620 (2025), proves a **positive-temperature Zdeborová--Boettcher relation up to reconstruction**, but its antiferromagnetic side is the unconstrained MaxCut model while its ferromagnetic side is the zero-magnetization MinBis model. It does **not** supply the balanced MaxBis side of Randomstrasse Conjecture 32. Its own abstract says the original zero-temperature fixed-degree relation remains open. Behrens--Arpino--Kivva--Zdeborová, arXiv:2202.10379, gives cavity-method arguments for an assortative/disassortative partition symmetry, but this is nonrigorous and concerns local partition constraints rather than the exact balanced ground-state identity here. I found no 2025--2026 primary theorem closing (BIS32) at fixed `d=3`; this is bounded negative evidence, not a novelty certificate.

## 2. Preserved spin/cut notation

For balanced spins

\[
\Omega_n=\{\sigma\in\{\pm1\}^n:\sum_i\sigma_i=0\},
\]

write `C_sigma` for the edge cut and

\[
H_G(\sigma)=\sum_{uv\in E(G)}\sigma_u\sigma_v.
\]

If `m=|E(G)|`, then

\[
|C_\sigma|=\frac{m-H_G(\sigma)}2.
\]

The previous run's exact centered defect remains

\[
B_{n,d}=\mathbf E[\mathrm{MinBis}+\mathrm{MaxBis}]
-\frac{dn^2}{2(n-1)},
\]

with `BIS32` equivalent to `B_{n,d}=o(n)` for each fixed `d`.

## 3. Method #1 — CHANGE THE CATEGORY: an affine cut-code nearest-word problem

Let

\[
\mathcal C(G)=\{C_\eta:\eta\in\{\pm1\}^{V(G)}\}\subseteq\mathbb F_2^{E(G)}
\]

be the binary cut space, with Hamming distance on edge indicators. Since `\mathcal C(G)` is linear, translation by any cut preserves it. Thus for **every** spin `sigma`,

\[
\begin{aligned}
\min_{\eta}d_H(C_\eta,E\setminus C_\sigma)
&=\min_{\eta}d_H(C_\eta,E\triangle C_\sigma)\\
&=d_H(E,\mathcal C(G))\\
&=m-\mathrm{MaxCut}(G).
\end{aligned}
\tag{C202}
\]

So the complement of every cut lies in the same affine cut-code coset, and its unconstrained distance back to the cut space is exactly the odd-cycle frustration index. The pre-existing exact checker `artifacts/R14/2026-09-17T11-35-15Z_rs2026bis32_cutspace_checker.py` exhaustively verified C202 on every simple graph with `n<=5`; the archived output records `1098` graphs, `16932` sigma cases, and `266376` distance tests, ending `ALL_EXACT_CHECKS_PASS`.

The bisection constraint has a particularly clean exact form. Fix **balanced** `sigma`. Put `tau=sigma*eta` vertexwise. Then

\[
\tau\in\Omega_n
\iff
\langle\sigma,\eta\rangle:=\sum_i\sigma_i\eta_i=0,
\]

and `C_tau=C_sigma triangle C_eta`. Hence

\[
\boxed{
 m-\mathrm{MaxBis}(G)
 =
 \min_{\eta:\,\langle\sigma,\eta\rangle=0}
 d_H(C_\eta,E\setminus C_\sigma).
}
\tag{C203}
\]

This is the sharp category change: **without** the orthogonality slice the nearest-word distance is simply `m-MaxCut`; **with** it, the distance is `m-MaxBis`. Thus a proof that only understands the affine cut-code coset but discards the overlap/orthogonality constraint cannot close Conjecture 32.

I added a new exact checker for C203. It exhaustively checked every simple graph on `n=2,4,6` and every balanced `sigma` representative: `32834` graphs and `327874` constrained cases. The output ends `C203_ORTHOGONAL_CUTSPACE_IDENTITY_PASS` and `ALL_EXACT_CHECKS_PASS`.

## 4. Method #24 — FIND THE EXTREMAL OBJECT: maximum-cut frustration is a matching in cubic graphs

Take now a cubic graph and let `eta` be a maximum-cut spin. Define its frustration set

\[
F_\eta:=E\setminus C_\eta.
\]

A one-vertex flip proves

\[
\boxed{F_\eta\text{ is a matching}.}
\tag{C204}
\]

Indeed, if a vertex had two or three incident uncut edges, flipping that vertex would turn more uncut edges into cut edges than vice versa, strictly increasing the cut. The pre-existing exact checker exhaustively verified C204 on all `71` labeled cubic graphs at `n=4,6` and `193` maximum-cut colorings.

For any graph, any spins `sigma,eta`, and `F_eta=E\setminus C_eta`, the exact gauge identity is

\[
\boxed{
|C_{\sigma\eta}|
=m-|C_\sigma|-R_\eta(\sigma),
\qquad
R_\eta(\sigma):=\sum_{uv\in F_\eta}\sigma_u\sigma_v.
}
\tag{4.1}
\]

The same pre-existing checker verified this identity in `266376` cases.

For `d=3`, choosing `eta` as a maximum cut therefore converts the entire failure of exact cut-complementation into two concrete quantities:

1. a signed sum `R_eta(sigma)` over a **matching**; and
2. the magnetization of the gauged spin `sigma*eta`, namely `\langle sigma,eta\rangle`.

This is much narrower than the original extremal-graph statement. It is also an honest obstruction: the matching structure alone does not force either quantity to be sublinear, so a naive “maximum cut makes the graph almost bipartite” argument is insufficient.

## 5. Method #27 — SWAP THE QUANTIFIERS: a deterministic gauge-decorrelation reduction for `d=3`

The proof does **not** need one maximum-cut gauge that works for every bisection. It is enough to choose a different maximum-cut gauge for each of the two extremal bisections.

Let

\[
\mathcal M(G)=\operatorname{ArgMaxCut}(G),
\]

and define, for a balanced spin `sigma`,

\[
\Phi_G(\sigma)
:=
\min_{\eta\in\mathcal M(G)}
\left(
 |R_\eta(\sigma)|
 +\frac32|\langle\sigma,\eta\rangle|
\right).
\tag{5.1}
\]

Then define the best extremal values

\[
\Phi_-(G)=\min_{\sigma\in\operatorname{ArgMinBis}(G)}\Phi_G(\sigma),
\qquad
\Phi_+(G)=\min_{\sigma\in\operatorname{ArgMaxBis}(G)}\Phi_G(\sigma).
\]

### C205 — deterministic cubic reduction

For every cubic graph on even `n`, with `m=3n/2`,

\[
\boxed{
 m-\Phi_-(G)
 \le
 \mathrm{MinBis}(G)+\mathrm{MaxBis}(G)
 \le
 m+\Phi_+(G).
}
\tag{C205.1}
\]

Consequently

\[
\boxed{
\left|\mathrm{MinBis}(G)+\mathrm{MaxBis}(G)-\frac{3n}{2}\right|
\le
\max\{\Phi_-(G),\Phi_+(G)\}.
}
\tag{C205.2}
\]

**Proof.** Let `sigma_-` be a minimum bisection and choose any maximum-cut `eta`. Set `tau=sigma_- eta`. Its magnetization is

\[
M(\tau)=\langle\sigma_-,\eta\rangle.
\]

Flipping exactly `|M(tau)|/2` majority spins makes `tau` balanced. Each vertex flip changes a cubic cut by at most `3`, hence there exists a balanced `tau'` with

\[
|C_{\tau'}|\ge |C_\tau|-\frac32|M(\tau)|.
\]

Using (4.1),

\[
\mathrm{MaxBis}(G)
\ge
m-\mathrm{MinBis}(G)-R_\eta(\sigma_-)
-\frac32|\langle\sigma_-,\eta\rangle|
\]

and therefore the lower bound follows after replacing `R` by `|R|` and minimizing over `sigma_-` and `eta`.

For a maximum bisection `sigma_+`, the same repair gives a balanced `tau'` with

\[
|C_{\tau'}|\le |C_{\sigma_+\eta}|+\frac32|\langle\sigma_+,\eta\rangle|.
\]

Since `MinBis<=|C_tau'|`, (4.1) gives the upper bound. This proves C205.

The new exact checker exhaustively tested C205 on all `71` labeled cubic graphs at `n=4,6` and all `343` extremal-bisection representatives encountered; it ends `C205_GAUGE_DECORRELATION_REDUCTION_PASS` and `ALL_EXACT_CHECKS_PASS`.

### Source-level sufficient condition

C205 turns the `d=3` source problem into one precise random-graph statement:

\[
\boxed{
\mathbf E\max\{\Phi_-(G_3),\Phi_+(G_3)\}=o(n)
\quad\Longrightarrow\quad
\text{Conjecture 32 at }d=3.
}
\tag{5.2}
\]

If (5.2) were proved, the fixed metric would move `D_bis:2->3` immediately.

This is a useful quantifier swap. We do **not** need a single gauge working uniformly over exponentially many balanced spins. For each actual minimum bisection and each actual maximum bisection, we only need existence of one suitable maximum-cut gauge. C204 then says its frustration correction is a signed sum over a matching.

I am not promoting (5.2) to a theorem about random cubic graphs: no current argument controls the joint zero-temperature correlations between an extremal bisection and a maximum-cut frustration matching. The cavity literature gives heuristic support for related ferro/antiferro symmetries, but not this estimate.

## 6. What the three moves actually taught us

- **#1 CHANGE THE CATEGORY succeeded as an exact reduction.** C203 identifies MaxBis as an orthogonality-constrained nearest-word problem in the affine cut-code coset. The unconstrained version collapses to the MaxCut frustration index, so the overlap constraint is genuinely the missing datum.
- **#24 FIND THE EXTREMAL OBJECT succeeded structurally but did not move the source metric.** In cubic graphs the maximum-cut obstruction is literally a matching (C204), reducing the energy defect to a matching signed sum.
- **#27 SWAP THE QUANTIFIERS produced the strongest new route, C205.** It is enough to find separate good maximum-cut gauges for the actual min- and max-bisection optimizers. Proving their residual-plus-overlap cost is `o(n)` would settle `d=3`.

The route is now falsifiable: if the next thinking run cannot find a mechanism forcing (5.2), R14 should not manufacture another max-cut-gauge lemma. It should abandon this route or reduce it to a genuinely decidable probabilistic statement.

## 7. Exact artifacts

Pre-existing, recovered and used rather than recreated:

- `artifacts/R14/2026-09-17T11-35-15Z_rs2026bis32_cutspace_checker.py`
- `artifacts/R14/2026-09-17T11-35-15Z_rs2026bis32_cutspace_checker.out`
- output commit: `8412f32a136aa6de5d49b14ed9ecc9d1d095d228`
- output ends `ALL_EXACT_CHECKS_PASS`.

New in this run:

- `artifacts/R14/2026-09-17T11-51-30Z_rs2026bis32_c203_c205_check.py`
- `artifacts/R14/2026-09-17T11-51-30Z_rs2026bis32_c203_c205_check.out`
- checker commit: `e0b260ef0efe1234231474bbea1f4833bee4164f`
- output commit: `22bceaa64687343c62a9e88ea913bd77055badc4`
- script SHA-256: `43bbb81fb141bfaf170390e74bf8de805ee862ec0f43152a105ef78a5978475c`
- output SHA-256: `a90d797898391783f6248111b9113496e14798d8089ae143d9f133eb8459dff7`
- output ends `ALL_EXACT_CHECKS_PASS`.

These are self-checks, not independent audits.

## 8. Stagnation trigger and exact next obligation

The metric did not move for the third consecutive RS-2026-BIS32 run:

\[
D_{\rm bis}:2\to2,
\qquad
\text{unchanged count }2\to3.
\]

Therefore the **next** R14 invocation is mandatory `STUCK-RECOVERY-1` under Section I. It must be a thinking run with no new theorem claim unless the stuck analysis itself chooses and completes one of the allowed recovery actions.

The exact blocker entering that run is

\[
\boxed{
\mathbf E\max\{\Phi_-(G_3),\Phi_+(G_3)\}=o(n)
}
\tag{8.1}
\]

or a genuinely different route proving `B_{n,3}=o(n)` without C205.

The next methods to examine in that thinking run are **#7 TAKE THE LIMIT, #21 ASK WHO ELSE HAS THIS SHAPE, #22 READ THE FAILURES, NOT THE SUCCESSES**. In particular, the run should compare the max-cut-gauge reduction with the exact point at which fixed-magnetization Ising arguments stop at reconstruction and with the cavity/locally-stable partition literature; if no ingredient controls the zero-temperature extremal overlap, the route should be dropped rather than extended by another local lemma.

## 9. Model/scheduler control

The exposed scheduling/editing surface still provides prompt/title/schedule/timing/enablement controls but **no authenticated model-family selector, no reasoning-effort selector, and no completed-run model telemetry**. GPT-6/maximum therefore remains prompt-only here. Enforcing it would require an authorized scheduler/product/API surface exposing those fields, or a platform-side change. Repository history also confirms that `You cannot modify this task` failures are ownership/context dependent; the legitimate workaround is the authorized owning workspace/account or platform support, not duplication or permission bypass. No scheduler change was attempted in this run, per the owner restriction.

```yaml
ledger_delta:
  track: R14
  target: RS-2026-BIS32
  source: "Randomstrasse 101, Conjecture 32 (Min and Max Bisections), 2026-02-16"
  status: OPEN/PARTIAL
  metric: D_bis
  before: 2
  after: 2
  moved: false
  unchanged_count_before: 2
  unchanged_count_after: 3
  stuck_state_after: "TRIGGERED; next run must be STUCK-RECOVERY-1"
  methods_actual: [1, 24, 27]
  new_exact_claims:
    - C202: "affine cut-space distance equals m-MaxCut (recovered pre-existing exact artifact)"
    - C203: "MaxBis is orthogonality-constrained nearest cut-code distance"
    - C204: "maximum-cut frustration edges form a matching in cubic graphs (recovered pre-existing exact artifact)"
    - C205: "cubic min+max-bisection defect bounded by tailored max-cut gauge residual/overlap"
  exact_checks:
    c202_c204_output: "artifacts/R14/2026-09-17T11-35-15Z_rs2026bis32_cutspace_checker.out"
    c203_c205_output: "artifacts/R14/2026-09-17T11-51-30Z_rs2026bis32_c203_c205_check.out"
    result: ALL_EXACT_CHECKS_PASS
  external_audits: "0/2 for C203/C205; self-check only"
  remaining_obligation: "prove B_{n,3}=o(n), e.g. by E max(Phi_-,Phi_+)=o(n), or abandon the max-cut-gauge route after the mandatory stuck analysis"
  next_methods: [7, 21, 22]
```
