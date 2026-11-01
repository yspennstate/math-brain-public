Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC MOVEMENT: `C_large = UNMEASURED -> 1/pi`; Section-B methods actually tried: #2 ATTACK THE NEGATION FIRST, #6 DEFORM TO A POINT YOU CAN SOLVE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME. Status: PARTIAL; the source-displayed large-radius equality is REFUTED AS WRITTEN, while the full Open Problem 2 remains open.**

# NM13-12 — E0086 large-radius boundary collapse and source-clause correction

Date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Canonical source / claim: `E0086` / `operations/claims/E0086.md`  
Canonical dedup key: `favorite_sites::op_2`  
Canonical SHA-256 / shard: `a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c`, residue `11 mod 13`

## 1. Runtime, controls, continuity, and required reads

The prompt requests `GPT-6 / maximum`. That is not the model that actually ran. The actual model available to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**. I do not claim that GPT-6 or maximum reasoning was bound at runtime.

The exposed task-control surface still provides ordinary fields such as title/prompt, schedule or relative start, timing mode, and enabled state, but no binding model-family selector and no reasoning-effort selector. Making `GPT-6 / maximum` binding would require an owner-authorized product/workspace/API/admin surface that exposes those controls plus authenticated per-run runtime attestation. Repository history also records a P26 edit returning `You cannot modify this task` in one authorization context and succeeding later in another authorized context. The legitimate workaround is to use the owning/otherwise-authorized task context or platform/admin support; cloning an inaccessible task or bypassing access controls is not a valid workaround. This invocation did not create, edit, disable, or duplicate any schedule.

Before admission and mathematics I reread or targeted-search-recovered the owner-required state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- `QUEUE.md`, `POSTED.md`, `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the newest own report `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T06-06-00Z__successor-admission-screen-1.md`;
- newest neighboring NM13-11 report `2026-09-18T06-47-57Z__e0082-fp-exponent-logarithmic-overlap.md` and newest NM13-13 report `2026-09-18T06-06-00Z__f0013-degree-support-handoff.md`;
- the relevant E-intake source and attempt ledgers, campaign catalog, exact aliases, claims, historical assignment/handoff searches, and current source/literature searches.

The mandatory predecessor continuity is preserved. `P0483` was already handed off after consuming the two permitted HARD stuck recoveries and is not reopened. The previous NM13-12 successor report left methods #2/#6/#30 unspent and the successor metric `UNMEASURED`; this invocation does not reset that history.

## 2. Admission of E0086 and exclusive ownership

The selected source is Izumi Okada, *Topics and problems on favorite sites of random walks*, arXiv:1606.03787, Open Problem 2. The intake row is `E0086` with explicit canonical dedup key

```text
favorite_sites::op_2
```

whose SHA-256 is

```text
a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c
```

and whose integer value is `11 mod 13`, exactly NM13-12's shard.

I recovered the old substantive attempt `E0086-A001` rather than treating the source as untouched. That attempt interpreted `\widetilde D_n` as the annular observation region itself and predicted an alpha-dependent local-time constant. The original source uses different semantics: `\widetilde D_n` is a finite translated **pattern** from the class `\mathcal H(M)`, and the region enters only through the condition that every vector in the pattern lies far from the origin. This source-semantic correction is material to the route below.

Repository searches for `E0086`, `favorite_sites::op_2`, the exact title, source aliases, claims, handoffs, current/historical assignment records, `POSTED.md`, campaign ledgers, and neighboring-worker reports found no competing owner. R7-03 had previously screened E0086 as HARD but did not claim it. `operations/claims/E0086.md` was absent immediately before creation.

The canonical claim was created with create-only semantics and read back at its creation commit:

- claim path: `operations/claims/E0086.md`;
- creation commit: `535e226c54036af882912a8d18e4bbcea278a46e`;
- claim blob: `73482943d4e9e01a660a85b8e45bf8e933e0f30f`.

Only after that readback did I treat E0086 as NM13-12's admitted target.

## 3. Exact source notation and the clause being tested

Let `(S_k)_{k>=0}` be planar simple random walk, let

\[
R(n):=\{S_0,S_1,\ldots,S_n\},\qquad
K(n,x):=\sum_{k=0}^n \mathbf 1_{\{S_k=x\}},
\]

and for a finite pattern `H` define the source's translated-boundary set

\[
\partial_H G:=\{y\in G:\ y+H\subset G^c\},
\]

with

\[
M_H(n):=\max_{x\in\partial_HR(n)}K(n,x).
\]

Open Problem 2 asks for the almost-sure asymptotic of `M_{\widetilde D_n}(n)` for patterns `\widetilde D_n\in\mathcal H` satisfying

\[
\widetilde D_n\subset D(0,a_n)^c,\qquad a_n\to\infty,
\]

especially when `a_n=n^\beta`, `0<\beta<1/2`, and the pattern lies between radii `a_n` and `2a_n`.

The source then displays the following large-radius conjectural clause: if for some `\varepsilon>0`,

\[
a_n\ge n^{1/2+\varepsilon},
\]

then, for all sufficiently large `n` almost surely,

\[
M_{\widetilde D_n}(n)=\max_{x\in\mathbb Z^2}K(\tau_n,x). \tag{S}
\]

The same source earlier quotes the classical planar favorite-site asymptotics

\[
\lim_{n\to\infty}\frac{\max_xK(\tau_n,x)}{(\log n)^2}
=
\lim_{n\to\infty}\frac{4\max_xK(n,x)}{(\log n)^2}
=
\frac4\pi
\quad\text{a.s.} \tag{F}
\]

Thus

\[
\frac{\max_xK(n,x)}{(\log n)^2}\longrightarrow\frac1\pi
\quad\text{a.s.} \tag{F'}
\]

The frozen metric for this admitted target is

\[
C_{\rm large}:=\lim_{n\to\infty}
\frac{M_{\widetilde D_n}(n)}{(\log n)^2}
\]

under the source's large-radius hypothesis `a_n>=n^{1/2+\varepsilon}`. Before this invocation it was **UNMEASURED**.

## 4. New route and complete theorem

### Theorem — large-radius translated-boundary collapse

Fix `\varepsilon>0`. Let `\widetilde D_n\in\mathcal H(M)` be any sequence of source-valid finite patterns satisfying

\[
\widetilde D_n\subset D(0,a_n)^c,
\qquad
a_n\ge n^{1/2+\varepsilon}
\]

for all sufficiently large `n`. Then almost surely, for all sufficiently large `n`,

\[
\boxed{\partial_{\widetilde D_n}R(n)=R(n)}. \tag{1}
\]

Consequently,

\[
\boxed{M_{\widetilde D_n}(n)=\max_xK(n,x)} \tag{2}
\]

for all sufficiently large `n`, and therefore

\[
\boxed{C_{\rm large}=\frac1\pi}. \tag{3}
\]

Moreover, using the source's quoted formula `(F)`,

\[
\boxed{
\frac{M_{\widetilde D_n}(n)}{\max_xK(\tau_n,x)}\longrightarrow\frac14
}
\quad\text{a.s.} \tag{4}
\]

Hence the source-displayed equality `(S)` is false **as written**.

### Proof

Let

\[
r_n:=\max_{0\le k\le n}|S_k|
\]

and choose `\delta=\varepsilon/2`. I first show

\[
r_n<n^{1/2+\delta}
\]

almost surely for all sufficiently large `n`.

For either coordinate `j\in\{1,2\}` and a fixed `k\le n`, Hoeffding's inequality for the bounded coordinate increments gives, for `t>0`,

\[
\mathbb P\{|S_k^{(j)}|\ge t/\sqrt2\}
\le 2\exp\!\left(-\frac{t^2}{4k}\right)
\le 2\exp\!\left(-\frac{t^2}{4n}\right).
\]

If `r_n\ge t`, then at some `k\le n` one of the two coordinates has absolute value at least `t/\sqrt2`. A union bound over `k\le n` and the two coordinates therefore yields

\[
\mathbb P\{r_n\ge t\}
\le 4n\exp\!\left(-\frac{t^2}{4n}\right).
\]

Set `t=n^{1/2+\delta}`. Then

\[
\mathbb P\{r_n\ge n^{1/2+\delta}\}
\le 4n e^{-n^{2\delta}/4},
\]

and the right-hand side is summable in `n`. By Borel-Cantelli,

\[
r_n<n^{1/2+\delta}
\]

for all sufficiently large `n` almost surely.

On the same almost-sure event, the source's large-radius hypothesis gives

\[
\frac{a_n}{r_n}
>
\frac{n^{1/2+\varepsilon}}{n^{1/2+\delta}}
=n^{\varepsilon-\delta}
=n^{\varepsilon/2}\to\infty.
\]

Hence eventually

\[
a_n>2r_n. \tag{5}
\]

Fix such an `n` and any `y\in R(n)`. Then `|y|\le r_n`. For any `d\in\widetilde D_n`, the condition `\widetilde D_n\subset D(0,a_n)^c` gives `|d|>a_n` (or `>=a_n`, depending on the source's boundary convention; either version is enough once `(5)` is strict). Therefore

\[
|y+d|\ge |d|-|y|>a_n-r_n>r_n.
\]

Every point of `R(n)` has Euclidean norm at most `r_n`, so `y+d\notin R(n)` for every `d\in\widetilde D_n`. Thus

\[
y+\widetilde D_n\subset R(n)^c,
\]

which says exactly that `y\in\partial_{\widetilde D_n}R(n)`. Since `y\in R(n)` was arbitrary,

\[
R(n)\subseteq\partial_{\widetilde D_n}R(n).
\]

The reverse inclusion is part of the definition of `\partial_HG`. This proves `(1)`, and `(2)` is immediate. Formula `(3)` follows from `(F')`. Dividing `(2)` by the first maximum in `(F)` gives `(4)`. In particular the ratio tends to `1/4`, so it cannot equal `1` for all sufficiently large `n`; the displayed source clause `(S)` is false as written. `\square`

No finite enumerative core is used here, so an exact-arithmetic checker would add no validation to this theorem-sized argument and was not manufactured.

## 5. Section-B method accounting

### #2 — ATTACK THE NEGATION FIRST

I attacked the literal large-radius equality `(S)` rather than assuming it. The source's own two favorite-site normalizations already make the claimed right-hand side four times larger asymptotically than the physical-time maximum. The geometric boundary collapse theorem then identifies the left-hand side exactly with that physical-time maximum. Outcome: the displayed clause is **refuted as written**, with a certified asymptotic ratio `1/4`.

### #6 — DEFORM TO A POINT YOU CAN SOLVE

The deformation parameter is the separation ratio `a_n/r_n`. Once it exceeds `2`, every translate `y+\widetilde D_n` from a visited site lies outside the whole visited range, so the complicated source boundary `\partial_{\widetilde D_n}R(n)` degenerates to the solved object `R(n)` itself. Outcome: the source functional reduces exactly to the classical planar favorite-site maximum, yielding `C_large=1/\pi`.

### #30 — DO ONE SCALE / ONE DIRECTION AT A TIME

The decisive scales are physical time `n`, walk radius `r_n=n^{1/2+o(1)}`, pattern distance `a_n`, and exit-radius time `\tau_n`. Localizing first to `a_n\gg r_n` proves the exact geometric collapse; only then comparing the two time scales through the source's formula `(F)` exposes the factor four. Outcome: the scale mismatch is explicit rather than hidden inside a multiscale heuristic.

These are the first actual uses of #2/#6/#30 on E0086; they are no longer available as “untried” methods for the next consecutive run.

## 6. What is and is not resolved

This run is **PARTIAL**, not a closure of E0086.

What is proved:

1. the large-radius regime `a_n>=n^{1/2+\varepsilon}` has the exact eventual identity `M_{\widetilde D_n}(n)=\max_xK(n,x)`;
2. the frozen source-relevant constant is exactly `C_large=1/\pi`;
3. the source-displayed comparison with `\max_xK(\tau_n,x)` is false as written, with ratio tending to `1/4`.

What remains open:

- the main regime explicitly emphasized by the source, `a_n=n^\beta` with `0<\beta<1/2`;
- the full dependence of `M_{\widetilde D_n}(n)` on the geometry of the finite pattern `\widetilde D_n`;
- whether the displayed large-radius line contains a typographical time-parameter mismatch (for example whether the left side was intended to use `\tau_n`). The factor-four contradiction makes a typo plausible, but this is an inference, not an authorized source correction.

Therefore I do **not** label the parent source `REFUTED`. The honest status is `PARTIAL`, with only the literal displayed large-radius clause marked `REFUTED-AS-WRITTEN`.

## 7. Prior attempt correction and why this is a genuinely new route

The intake attempt `E0086-A001` treated `\widetilde D_n` as if it were itself an annular observation region and argued that an annulus beyond the diffusive radius is essentially unvisited. Under the source definitions, that is not the object being maximized over. The maximization variable is `y\in\partial_{\widetilde D_n}R(n)\subset R(n)`, while `\widetilde D_n` is the translated avoidance pattern. Large `a_n` therefore makes the boundary **larger**, ultimately all of `R(n)`, rather than making the maximization region disappear.

That semantic correction reverses the old heuristic and produces the exact theorem above. I preserve the old attempt as history; I do not count it as one of this run's three methods.

## 8. Bounded literature / source-status check — 2026-09-18

I checked the original Okada source directly, including the PDF page containing Open Problem 2, and compared the exact notation rather than relying on the intake paraphrase. I also searched the later Okada/favorite-sites line using combinations of the exact source title, `Open problem 2`, `M_{\widetilde D_n}(n)`, `tau_n`, favorite sites, annular/translated boundary language, and later author names.

The bounded search recovered, among other related work:

- Okada's later paper on exponents for frequently visited point configurations;
- later work on pairs/families of favorite points;
- Hao–Li–Okada–Zheng's 2024 favorite-sites work and associated 2025 presentation material.

None of the material recovered in this bounded search stated a source-matching resolution or an explicit correction of this exact Open Problem 2 large-radius line. This is **negative evidence only**. I did not perform an exhaustive worldwide citation-graph audit, contact the author, or establish publication novelty. The arXiv source PDF was accessible and read directly; extraction of one separate published-copy surface was less useful, so I do not infer from its silence that no erratum exists.

## 9. Validation, audits, and next route

The new claim is a short symbolic/probabilistic theorem with a complete proof on this page. There is no finite search core, so no checker or Lean file was created merely for bookkeeping. The literature/source check and this proof are self-checks, not independent audits.

Required closure audits remain outstanding:

- P26: **NOT PASSED**;
- NM13-13: **NOT PASSED**.

No audit request itself would count as mathematical movement.

The frozen metric moved, so E0086 starts with

```text
unchanged_runs = 0
recoveries = 0
```

The next run should keep the same source and metric history, first adversarially recheck the source notation/time parameter, then attack the genuinely hard `0<\beta<1/2` regime. A concrete source-faithful first special class is a singleton translated pattern `\widetilde D_n={z_n}` with `|z_n|\asymp n^\beta`; one can then ask for a complete asymptotic bound on the deepest visited site whose `z_n`-translate is unvisited. Candidate fresh methods for the next run are #4, #18, #24; they are **not** counted as tried here.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: E0086
  claim_id: E0086
  source_title: "Topics and problems on favorite sites of random walks — Open Problem 2"
  canonical_dedup_key: "favorite_sites::op_2"
  canonical_sha256: "a616b4531a1a18ab6b2369a38d555ba54d6cc8cacdf46404e4e8ee26baeecc2c"
  selection_residue_mod_13: 11
  status: PARTIAL
  source_parent_status: OPEN
  literal_source_large_radius_clause: REFUTED_AS_WRITTEN
  metric_name: C_large
  metric_definition: "lim_{n->infinity} M_{Dtilde_n}(n)/(log n)^2 under eventual a_n >= n^(1/2+epsilon)"
  metric_before: UNMEASURED
  metric_after: 1/pi
  secondary_diagnostic: "M_{Dtilde_n}(n)/max_x K(tau_n,x) -> 1/4 a.s."
  theorem: "eventually partial_{Dtilde_n} R(n)=R(n), hence M_{Dtilde_n}(n)=max_x K(n,x), whenever a_n >= n^(1/2+epsilon)"
  methods_tried: [2, 6, 30]
  unchanged_runs: 0
  recoveries: 0
  finite_checker_required: false
  p26_audit: NOT_PASSED
  nm13_13_audit: NOT_PASSED
  closure: false
  next_step: "adversarial source-notation audit, then singleton-pattern beta in (0,1/2) quantitative asymptotic; suggested fresh methods 4/18/24"
```

## 11. Repository write scope

This invocation created exactly the canonical E0086 claim and this one immutable NM13-12 run report. It did not edit shared root ledgers, peer namespaces, existing claims, workflows, permissions, public surfaces, email/Drive state, paid-compute resources, or schedules. The claim was read back at its exact creation commit before substantive work. This report must likewise be read back at its returned creation commit; no receipt-only follow-up commit is warranted.
