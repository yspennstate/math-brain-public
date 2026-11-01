Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT: `D_bis: 2 -> 2`; unchanged count `4 -> 5`; `STUCK-RECOVERY-2/2`. Methods actually tried: #15 BREAK THE SYMMETRY ON PURPOSE, #9 RANDOMIZE, #19 MAKE IT AN ALGORITHM.**

# R14 — RS-2026-BIS32 STUCK-RECOVERY-2: the stable-gauge special case decodes back to the source problem

Status: **OPEN / PARTIAL**. This is the second and final permitted HARD stuck-recovery on `RS-2026-BIS32` for R14. The original negative-margin spherical-perceptron target remains handed off and is **not reopened**; its last supported rigorous bracket remains

\[
6.30297437506\le \alpha_c(-1)\le 12.78437096216,
\qquad
\alpha_U-\alpha_L=6.48139658710.
\]

The intervening I0089 Riesz target also remains handed off. The active canonical ownership claim remains `operations/claims/RS-2026-BIS32.md`.

This run continues from `runs/R14/2026-09-17T12-51-20Z_rs2026bis32_stuck1_stable_gauge.md`. Because that report triggered the first HARD stuck recovery and selected the one-sided local-stable-gauge special case `(SC)`, this run is a thinking/recovery run. I did **not** manufacture another finite checker or auxiliary theorem merely to document an unchanged metric.

## 1. Repository and source continuity

At run start I reread the campaign index/ranking, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the controlling owner directive, the current R14 claim, the newest R14 report, and current neighboring R13/R15 evidence. I also used targeted repository searches for the exact bisection source/ownership and preserved the current claim instead of treating PENDING queue rows as READY.

Fresh source/literature checks on 2026-09-17 still leave the exact fixed-degree source statement open in the material recovered:

- Afonso S. Bandeira, Randomstrasse 101, “Bisections of large random sparse regular graphs (problems 32 and 33),” posted 2026-02-16, still states Conjecture 32 for fixed `d>=3`:
  `https://randomstrasse101.math.ethz.ch/posts/GraphBisections/`.
- Gheissari–Perkins–Yap, arXiv:2511.16620, remains positive-temperature and below reconstruction; it does not reach the balanced zero-temperature fixed-`d` statement.
- Behrens–Arpino–Kivva–Zdeborová, arXiv:2202.10379 / J. Phys. A 55 (2022) 395004, gives cavity-method evidence and entropy-level assortative/disassortative symmetry for local stable states, not a rigorous single-instance extremal-bisection theorem.
- Díaz–Do–Serna–Wormald, TCS 307 (2003), DOI `10.1016/S0304-3975(03)00236-6`, gives randomized algorithms yielding complementary-looking rigorous bounds for min/max bisection, but not equality of the true optima.
- Balliu–Boudier–d'Amore–Kuhn–Olivetti–Schmid–Suomela, PODC 2026, gives polylogarithmic distributed algorithms for locally optimal cuts in bounded-degree graphs, but no correlation control against a graph-dependent global bisection extremizer.
- Robinson–Wormald, RSA 19 (2001), DOI `10.1002/rsa.1024`, gives Hamilton-cycle small-subgraph-conditioning/contiguity machinery useful for a possible future cubic route.

This is bounded negative evidence, not a novelty certificate.

The fixed source metric remains

\[
D_{\rm bis}=2.
\]

## 2. Exact source blocker

For a cubic graph `G` on even `n`, put `m=3n/2`. The source movement obligation is

\[
\boxed{
B_{n,3}:=
\mathbf E[\mathrm{MinBis}(G_3)+\mathrm{MaxBis}(G_3)]
-\frac{3n^2}{2(n-1)}=o(n).
}
\tag{S0}
\]

The finite-`n` center differs from `m=3n/2` by only `O(1)`, so equivalently one needs

\[
\mathbf E[\mathrm{MinBis}(G_3)+\mathrm{MaxBis}(G_3)-m]=o(n).
\]

The first stuck recovery selected the one-sided special case: for a measurable minimum-bisection optimizer `sigma_-`, find a one-flip-stable max-cut gauge `eta` with

\[
|R_\eta(\sigma_-)|+\frac32|\langle\sigma_-,\eta\rangle|=o(n)
\]

in expectation. This run tested whether that special case is genuinely simpler.

## 3. Exact gauge-decoder identity: the key structural obstruction

Use spins `x in {+1,-1}^V` and

\[
H_G(x)=\sum_{uv\in E}x_ux_v,
\qquad
\mathrm{cut}_G(x)=\frac{m-H_G(x)}2.
\]

For any two spin configurations `sigma, eta`, define

\[
\tau:=\sigma\eta
\quad\text{(coordinatewise product)},
\]

and let

\[
F_\eta:=\{uv\in E:\eta_u\eta_v=+1\},
\qquad
R_\eta(\sigma):=\sum_{uv\in F_\eta}\sigma_u\sigma_v.
\]

Then, **without any stability assumption on `eta`**, one has exactly

\[
\begin{aligned}
H_G(\sigma)+H_G(\tau)
&=\sum_{uv\in E}\sigma_u\sigma_v(1+\eta_u\eta_v)\\
&=2R_\eta(\sigma),
\end{aligned}
\]

hence

\[
\boxed{
R_\eta(\sigma)=\frac{H_G(\sigma)+H_G(\sigma\eta)}2.
}
\tag{E1}
\]

Also

\[
\boxed{
\langle\sigma,\eta\rangle=\sum_v\tau_v,
}
\tag{E2}
\]

so the overlap term is exactly the magnetization defect of the decoded spin `tau`.

Combining (E1) with the cut/Hamiltonian identity gives

\[
\boxed{
\mathrm{cut}_G(\tau)
=m-\mathrm{cut}_G(\sigma)-R_\eta(\sigma).
}
\tag{E3}
\]

Thus the previous gauge objective has a direct interpretation:

\[
\boxed{
|R_\eta(\sigma)|+\frac32|\langle\sigma,\eta\rangle|
}
\]

is precisely the error budget for turning `tau=sigma eta` into a balanced cut whose cut value is complementary to that of `sigma`.

### Balance repair

If `sigma` is balanced, let

\[
M:=\langle\sigma,\eta\rangle=\sum_v\tau_v.
\]

Because `n` is even, `M` is even. Flip exactly `|M|/2` majority-spin vertices of `tau`. The resulting `tau^b` is balanced. In a cubic graph a single vertex flip changes the cut by at most `3`, so

\[
\boxed{
|\mathrm{cut}(\tau^b)-\mathrm{cut}(\tau)|
\le \frac32|M|.
}
\tag{E4}
\]

No probability or asymptotics enter (E1)–(E4).

## 4. Method #15 — BREAK THE SYMMETRY ON PURPOSE: the one-sided special case proves only one half

Take `sigma=sigma_-`, a minimum-bisection optimizer. From (E3)–(E4), any gauge `eta` gives a balanced `tau^b` with

\[
\mathrm{MaxBis}(G)
\ge m-\mathrm{MinBis}(G)
-|R_\eta(\sigma_-)|
-\frac32|\langle\sigma_-,\eta\rangle|.
\]

Therefore the `(SC)` selected in recovery 1 implies only

\[
\boxed{
\mathrm{MinBis}(G)+\mathrm{MaxBis}(G)\ge m-o(n).
}
\tag{L}
\]

For the opposite inequality one needs the analogous statement starting from a maximum-bisection optimizer `sigma_+`:

\[
\boxed{
\mathrm{MinBis}(G)+\mathrm{MaxBis}(G)\le m+o(n).
}
\tag{U}
\]

This is an important correction to the route: proving the recovery-1 special case alone would **not** move `D_bis` from 2 to 3, because the fixed metric requires the full source equality.

More strongly, if the stability restriction on `eta` is removed, the *pair* of gauge obligations is equivalent to the source statement. Indeed, if

\[
\Delta_G:=\mathrm{MinBis}(G)+\mathrm{MaxBis}(G)-m,
\]

choose balanced optimizers `sigma_-`, `sigma_+` and put `eta=sigma_- sigma_+`. Then `tau=sigma_+` is balanced, and (E3) gives

\[
R_\eta(\sigma_-)=-\Delta_G,
\qquad
\langle\sigma_-,\eta\rangle=0.
\]

The same construction in the reverse direction gives the max-side obligation. Conversely, the two gauge obligations plus (E3)–(E4) imply (L) and (U).

So the unrestricted “find a good gauge” formulation is **not a reduction to an easier problem**; it is the source complementability statement written in different variables. Requiring `eta` to be one-flip-stable only makes the witness class smaller. The local-stable route can still be useful if stability supplies new probabilistic structure, but it cannot be advertised as a simplification by itself.

I record this as a **certified structural obstruction / route diagnosis**, not as source closure and not as metric movement.

## 5. Method #9 — RANDOMIZE: naive independent gauges have the wrong bias

The first recovery hoped that the entropy of many one-flip-stable gauges could provide anti-concentration against the extremal bisection. The decoder identity shows why a naive random-gauge argument cannot work.

For a fixed extremal balanced `sigma`, if `eta` were an independent unbiased random spin configuration, then `tau=sigma eta` is again unbiased and

\[
\mathbf E_\eta H_G(\tau)=0.
\]

By (E1),

\[
\mathbf E_\eta R_\eta(\sigma)=\frac12 H_G(\sigma).
\]

For a minimum-bisection optimizer on a cubic random graph, `H_G(sigma_-)` is of linear order. Hence an independent random gauge has a **linear residual bias**, not the desired `o(n)` residual. Randomness must therefore come from a graph-correlated gauge ensemble with a very specific negative-energy response; generic anti-concentration is insufficient.

This also explains why sampling an arbitrary local optimum is not automatically useful. The same random graph determines both `sigma_-` and the stable-gauge landscape, so conditional independence is exactly what is unavailable.

### A concrete future randomization route: the Hamilton-cycle planted model

There is, however, one sharper ensemble worth handing off. In the cubic Hamilton-cycle model write

\[
G=C\cup M,
\]

where `C` is an even Hamilton cycle and `M` is an independent uniform perfect matching (before the usual simplicity conditioning). Let `eta_C` alternate around `C`. Then every cycle edge is cut by `eta_C`, so `eta_C` is automatically one-flip-stable; its uncut edges lie in the matching.

For a **fixed balanced** spin `sigma` independent of `M`, put

\[
a=\langle\sigma,\eta_C\rangle.
\]

The exact perfect-matching average of the residual is

\[
\boxed{
\mathbf E_M R_{\eta_C}(\sigma)
=
\frac{a^2-2n}{4(n-1)}.
}
\tag{H1}
\]

Proof: the two parity classes of `eta_C` each have size `n/2`; balance of `sigma` gives their spin sums `a/2` and `-a/2`. A pair `{u,v}` appears in a uniform perfect matching with probability `1/(n-1)`, so summing `sigma_u sigma_v` over same-parity unordered pairs gives

\[
\frac1{n-1}
\left(\frac{a^2}{4}-\frac n2\right).
\]

Thus if `|a|=O(\sqrt n)`, the residual has only `O(1)` mean; a standard bounded-difference exposure of the matching gives `O(\sqrt n)` fluctuations for a fixed `sigma`. This is exactly the scale needed by (E3)–(E4).

But this does **not** prove anything for `sigma_-`: the extremizer is a function of the same random matching `M`. Applying the fixed-`sigma` concentration after optimizing over `sigma` would be an invalid independence swap. The missing theorem becomes concrete:

> In the Hamilton-cycle planted cubic model, prove a quenched version of (H1) for an actual extremal balanced state, or show that among Hamilton-cycle representations of a typical cubic graph one representation yields `|a|+|R|=o(n)` for that extremizer.

Robinson–Wormald small-subgraph conditioning gives genuine contiguity machinery for Hamilton-cycle-biased regular-graph models, and Sorkin’s cubic-cut work already uses a Hamilton-cycle model for rigorous cut bounds. That makes this a better handoff route than generic “sample a stable state,” but the extremizer/matching dependence remains the exact unresolved step.

## 6. Method #19 — MAKE IT AN ALGORITHM: a good-gauge algorithm is already a complementary-bisection algorithm

Suppose an algorithm takes `(G,sigma_-)` and returns `eta` with

\[
|R_\eta(\sigma_-)|+\frac32|\langle\sigma_-,\eta\rangle|=o(n).
\]

Then the explicit decoder

1. set `tau=sigma_- eta`;
2. flip `|sum tau|/2` majority vertices to balance;
3. output the repaired `tau^b`;

constructs a bisection of value at least

\[
m-\mathrm{MinBis}(G)-o(n).
\]

So a successful good-gauge algorithm already solves the lower complementary-bisection half of the source problem. The analogous max-side algorithm solves the upper half. This is why merely making local-max-cut search efficient does not address the source obstruction.

The July-2026 local-potential algorithms of Balliu et al. are informative here: they can find a locally optimal cut efficiently in bounded degree, but their guarantee contains no control of either decoder statistic `R_eta(sigma_ext)` or `<sigma_ext,eta>` against a graph-dependent global extremizer. Likewise, Díaz–Do–Serna–Wormald obtain paired min/max **bounds** through a symmetric randomized procedure; the proof symmetry does not certify that either algorithm attains the true fixed-degree optimum.

The algorithmic failure is therefore precise: **local stability is computationally accessible, but source closure requires global quenched correlation control.**

## 7. Why this is a genuine recovery-2 obstruction, not another missing lemma

The first recovery deliberately replaced global maximum-cut gauges by a much larger set of one-flip-stable gauges. The hope was that their entropy would make a small-overlap/small-residual witness easy to find.

Equations (E1)–(E4) show that the objective being minimized is exactly the error in decoding a complementary bisection. The stable-state entropy does not by itself decouple that error from the extremizer. Behrens et al. reach essentially the same conceptual boundary from the cavity side: their assortative/disassortative correspondence is an ensemble/entropy statement, not a rigorous map on a single random regular graph between a given extremal state and an opposite one.

The nearest rigorous algorithmic analogue, Díaz–Do–Serna–Wormald (and the later Hoppen–Wormald discussion), exhibits a “quirk” by which the same local process yields complementary-looking lower/upper bounds. The remaining gap is exactly tightness: a symmetric algorithmic construction need not locate the global extrema.

Thus the route selected in recovery 1 does not fail because one more local lemma is missing. It fails because, after exact decoding, its promised witness is already an encoded form of the source complementability phenomenon.

## 8. Required handoff state

This consumes **STUCK-RECOVERY-2/2** for `RS-2026-BIS32` under R14.

The fixed metric is unchanged:

\[
D_{\rm bis}:2\to2,
\]

and the supported unchanged count advances `4 -> 5`.

There is **no third BIS32 thinking recovery for R14**. Unless a closure-quality result arrives independently before the next invocation, the next R14 run must write the immutable handoff/release state and rotate only to a freshly source-checked, ownership-eligible outside HARD target. `PENDING` queue rows are not automatically READY and must not be invented into assignments.

For a future fresh reassignment of BIS32, the strongest handoff direction is the Hamilton-cycle planted/contiguity route, not generic stable-state sampling. Suggested new-method triple for that future owner is:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** work first in the distinguished Hamilton-cycle plus random-perfect-matching model where (H1) is exact, then identify precisely what simplicity/contiguity and extremizer dependence cost;
- **#25 COUNT THE SAME THING TWICE:** double-count triples `(G,C,sigma_ext)` by graph-first and planted-cycle-first descriptions to attack the invalid independence swap;
- **#28 REPLACE FOR ALL WITH FOR TYPICAL:** target a quenched statement only for the actual extremizer of a typical cubic graph, not a uniform theorem over all balanced spins.

R14 itself should not spend a third recovery on those moves without a fresh reassignment after handoff.

## 9. Closure / audit status

- Full Conjecture 32 at `d=3`: **OPEN**.
- `D_bis`: **2**.
- New source theorem this run: **none**.
- New finite checker this run: **none by design**; this was a thinking-only stuck recovery.
- Exact algebraic structural obstruction (E1)–(E4): **proved on the page / self-check only**.
- External audits on source closure: **0/2**.
- No paper folder created because nothing source-level closed.

## 10. Model / scheduler control

The exposed scheduler control surface still provides prompt/title, schedule or relative start, enablement and timing-mode controls, but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Therefore GPT-6/maximum remains prompt-only and cannot be honestly certified here.

To make the requested model setting enforceable would require an authorized scheduler/product/API surface exposing explicit model and reasoning fields plus completed-run telemetry, or a platform-side change. A `You cannot modify this task` response is an ownership/authorization-context issue: use the authorized owning workspace/account context or platform support; do not duplicate the task or bypass permissions.

## Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  target: RS-2026-BIS32
  category: HARD_OUTSIDE
  status: OPEN_PARTIAL
  metric:
    name: D_bis
    before: 2
    after: 2
  unchanged_count:
    before: 4
    after: 5
  stuck_recovery: "2/2 consumed"
  methods_actual: [15, 9, 19]
  source_result: "no movement"
  certified_obstruction:
    summary: "stable-gauge objective decodes exactly into complementary-bisection error; unrestricted two-sided gauge formulation is source-equivalent"
    equations: [E1, E2, E3, E4]
  strongest_future_route:
    name: "Hamilton-cycle planted/contiguity route"
    exact_fixed_sigma_identity: "E_M R = (a^2-2n)/(4(n-1))"
    missing_step: "quenched control for graph-dependent extremal bisection / invalid independence swap"
  audits_source_closure: "0/2"
  next_R14_action: "HANDOFF_AND_ROTATE; no third BIS32 recovery"
  shared_roots_modified: false
  peer_files_modified: false
  email: false
  drive: false
  scheduler_changes: false
```
