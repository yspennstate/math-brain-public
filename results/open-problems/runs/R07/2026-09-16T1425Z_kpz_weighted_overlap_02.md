Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED by the runtime; GPT-6 maximum was requested, but the scheduler exposes no model or reasoning selector and I do not claim GPT-6 maximum. **No movement in the fixed metric.**
Problem: ordinary undirected Exp(1) first-passage variance on Z^2 — Kardar-Parisi-Zhang (1986); Auffinger-Damron-Hanson (2015), Question 13.
Metric: before `b(n)=c_PP log n` for integers n>=2 with one fixed non-explicit `c_PP>0`; after the same bound; status OPEN; observed unchanged-count since the canonical baseline = 1 (earlier historical stagnation remains UNKNOWN).

# R07 canonical GitHub run — exact weighted geodesic-overlap identity

Run date: 2026-09-16.
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Repository recovery and source/status check

I continued from the newest canonical R07 report

- `runs/R07/2026-09-16T1325Z_kpz_metric_covariance_01.md`.

That report fixed the metric and proved/recorded:

- `R07-GH-C01`: Pemantle-Peres logarithmic variance lower bound;
- `R07-GH-C02`: Doob martingale variance identity;
- `R07-GH-C03`: exact one-edge exponential cavity representation and variance kernel;
- `R07-GH-X01`: Boolean geodesic membership is not uniformly comparable from below to weighted passage sensitivity;
- `R07-GH-C04`: product-refresh/ANOVA integrated sensitivity identity.

I also read the campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/FLEET_2026-09-16.md`, `operations/RFLEET_2026-09-16.md`, and the newest neighboring R08 report

- `runs/R08/2026-09-16T1329Z_fpp-axis-gap-a1c93e.md`.

The discovered root intake ledgers `probability_1000_intake_claude_20260907/problems.jsonl` and D/E/F/G/H/I were read-attempted. The connector truncates these large JSONL resources in model-visible output, so intake ingestion is recorded as **PARTIAL due connector truncation**, not as a complete row-by-row read. No historical `admitted=true` flag was treated as current verification.

Dated current-literature check, 2026-09-16, included queries for ordinary point-to-point FPP variance lower bounds, current arXiv FPP variance/chaos papers, later overlap/coalescence papers, and the original survey questions. Results relevant to the frozen metric:

1. Auffinger-Damron-Hanson Question 13 still asks for `chi<1/2` in `d>=2` and `chi=1/3` in `d=2`.
2. Pemantle-Peres Theorem 1 gives, for iid mean-one exponential FPP on Z^2 and every fixed direction, `Var T >= C log n`. For `e1` this gives the present metric. Their constant is not numerical in the theorem.
3. The same Pemantle-Peres paper notes a power lower bound under nonflat/finite-curvature directional hypotheses. Those hypotheses are not proved here for the `e1` direction and remain **PARTIAL/CONDITIONAL** for this task.
4. Ahlberg-Deijfen-Sfragara establish a rigorous fluctuations/chaos/geodesic-overlap correspondence, but the transition scale is expressed in terms of the unknown variance and cannot be inserted as `n^(2/3)` without circularity.
5. Dembin-Elboim-Peled obtain quantitative coalescence/overlap under a limit-shape extreme-point hypothesis; this is not an unconditional replacement for the present Exp(1), fixed-direction metric.
6. Dembin-Elboim's 2025 polynomial lower bound concerns a different left-right crossing variable and uses curvature-type hypotheses for its strongest scope.
7. Basu-Sidoravicius-Sly (arXiv:2604.01214, 2026-04-01) break the `n/log n` *upper* variance barrier only in a different rotationally invariant Riemannian FPP model.

I found no current unconditional ordinary-lattice point-to-point lower-bound order improving `log n`. This bounded search is evidence for retaining the metric, not a proof that no such paper exists.

Therefore

\[
\boxed{b(n)=c_{\rm PP}\log n,\qquad n\ge2,\qquad c_{\rm PP}>0}
\]

remains the strongest verified uniform lower-bound order for this track.

A useful source cross-check is ADH Question 16: it asks in `d=2` for `a>0` such that the expected overlap of two independently sampled geodesics from `0` to `nx` is at least `n^a`, and explicitly says such an overlap result would improve the Newman-Piza variance lower-bound method. The exact identity below shows why the Exp(1) resampling route needs a **weighted** overlap, not overlap count alone.

No Gmail, Drive, email, public publication, permission change, or schedule change occurred.

## 2. R07-GH-C05 — exact refresh-cavity covariance derivative

**Label: PROVED product-space identity specialized to Exp(1) FPP; no novelty claim.**

Let

\[
T_n=T(0,ne_1),\qquad f=T_n-ET_n.
\]

Since `T_n` is bounded by the sum of the `n` coordinate-edge exponentials on the straight path, `f in L^2`.

For `t>=0`, construct the standard stationary coordinate-refresh coupling `(X,X^t)`: independently for every edge `e`, with probability

\[
\rho=e^{-t}
\]

keep `X_e^t=X_e`, and otherwise replace it by an independent Exp(1) copy. Define

\[
C_n(t)=\operatorname{Cov}(T_n(X),T_n(X^t)).
\]

For one edge, let

\[
D_e f=f-E[f\mid X_{\setminus e}].
\]

The countable-product ANOVA decomposition gives

\[
f=\sum_{\emptyset\ne S}f_S
\]

orthogonally in `L^2`, and hence

\[
C_n(t)=\sum_{S\ne\emptyset}e^{-|S|t}\|f_S\|_2^2.
\tag{2.1}
\]

For every `t>0`, termwise differentiation is justified because

\[
\sup_{k\ge1}k e^{-kt}<\infty
\]

and `sum_S ||f_S||_2^2=Var(T_n)<infinity`. Thus

\[
-C_n'(t)=\sum_{S\ne\emptyset}|S|e^{-|S|t}\|f_S\|_2^2.
\tag{2.2}
\]

Also

\[
D_e f=\sum_{S\ni e}f_S,
\]

so orthogonality under the refresh coupling gives

\[
\boxed{
-C_n'(t)
=
\sum_eE[D_ef(X)D_ef(X^t)].
}
\tag{2.3}
\]

Now specialize to FPP. Freeze every coordinate except edge `e`. As in C03 there is an off-`e` threshold `R_e>=0` and an off-`e` constant `C_e` such that

\[
T_n=C_e+\min\{X_e,R_e\}.
\]

Write

\[
m(r)=E\min(X,r)=1-e^{-r},
\]

\[
h(x,r)=\min(x,r)-m(r).
\]

Then

\[
D_eT_n=h(X_e,R_e).
\tag{2.4}
\]

Let

\[
R_e^t=R_e(X^t_{\setminus e}).
\]

Condition on the coupled off-`e` environments and on the survival indicator of coordinate `e`. If `e` was refreshed, `X_e` and `X_e^t` are independent and both centered in (2.4), so the conditional product has mean zero. If `e` survived, they are the same Exp(1) variable and the conditional product is

\[
\kappa(r,s)
:=\operatorname{Cov}(\min(X,r),\min(X,s)).
\]

Therefore, for every `t>0`, exactly

\[
\boxed{
-C_n'(t)
=e^{-t}\sum_eE\,\kappa(R_e,R_e^t).
}
\tag{C05}
\]

For `0<=r<=s<infinity`, direct integration gives

\[
\boxed{
\kappa(r,s)
=1-(r+1)e^{-r}+(1-r)e^{-s}-e^{-(r+s)}.
}
\tag{2.5}
\]

Since (2.1) implies `C_n(t)->0` as `t->infinity`, integration of (C05) gives the exact representation

\[
\boxed{
\operatorname{Var}(T_n)
=
\int_0^\infty e^{-t}
\sum_eE\,\kappa(R_e,R_e^t)\,dt.
}
\tag{2.6}
\]

There is no curvature assumption in C05.

## 3. R07-GH-C06 — the kernel dominates a depth-weighted overlap kernel

**Label: PROVED.**

Let

\[
q(r)=\operatorname{Var}(\min(X,r))
=1-2re^{-r}-e^{-2r}.
\]

For `0<=r<=s`, algebra from (2.5) gives

\[
\boxed{
\kappa(r,s)-q(r)
=(e^{-r}-e^{-s})(r-1+e^{-r})\ge0,
}
\tag{3.1}
\]

because `e^{-r}>=1-r`. Thus

\[
\boxed{
\kappa(r,s)\ge q(\min\{r,s\}).
}
\tag{3.2}
\]

Next define

\[
p(r)=1-e^{-r}=P(X<r).
\]

I claim the explicit uniform inequality

\[
\boxed{
q(r)
\ge
\frac1{16e}\,p(r)(r\wedge1)^2,
\qquad r\ge0.
}
\tag{C06}
\]

**Proof.** Let `Y=min(X,r)` and `Y'` be an independent copy, so

\[
q(r)=\frac12E(Y-Y')^2.
\]

If `0<r<=1`, on either of the two disjoint events

\[
\{X\le r/2,\ X'\ge r\},
\qquad
\{X'\le r/2,\ X\ge r\},
\]

we have `|Y-Y'|>=r/2`. Hence

\[
q(r)
\ge
P(X\le r/2)P(X\ge r)\frac{r^2}{4}.
\]

Using `e^u>=1+u` gives

\[
1-e^{-r/2}\ge\frac{r/2}{1+r/2}\ge r/4,
\]

and `e^{-r}>=e^{-1}`. Therefore

\[
q(r)\ge\frac{r^3}{16e}
\ge\frac1{16e}p(r)r^2,
\]

since `p(r)<=r`.

If `r>=1`, use the two events

\[
\{X\le1/2,\ X'\ge1\}
\quad\text{and its reverse}.
\]

They give `|Y-Y'|>=1/2`, hence

\[
q(r)\ge\frac1{16e}.
\]

Because `p(r)<=1` and `(r wedge 1)^2=1`, this proves C06. `r=0` is trivial. QED.

## 4. R07-GH-C07 — a precise weighted geodesic-overlap lower reduction

**Label: PROVED REDUCTION.**

Continuous passage weights make the point-to-point geodesic unique almost surely. Let

- `gamma=gamma_n(X)` and `gamma^t=gamma_n(X^t)`;
- `B_e(t)` be the event that coordinate `e` was not refreshed;
- `underline R_e(t)=min(R_e,R_e^t)`.

Conditional on the coupled off-`e` environments and on `B_e(t)`, the shared edge weight is one Exp(1) variable. Hence

\[
B_e(t)\cap\{e\in\gamma\cap\gamma^t\}
\quad\Longleftrightarrow\quad
B_e(t)\cap\{X_e<\underline R_e(t)\}
\]

up to null ties. Therefore

\[
E\left[(\underline R_e(t)\wedge1)^2
1_{B_e(t)}1_{\{e\in\gamma\cap\gamma^t\}}
\mid X_{\setminus e},X^t_{\setminus e}\right]
=
e^{-t}(\underline R_e(t)\wedge1)^2p(\underline R_e(t)).
\tag{4.1}
\]

Combining C05, (3.2), C06 and (4.1) gives, for every `t>0`,

\[
\boxed{
-C_n'(t)
\ge
\frac1{16e}
E\sum_e
(\underline R_e(t)\wedge1)^2
1_{B_e(t)}1_{\{e\in\gamma\cap\gamma^t\}}.
}
\tag{C07.1}
\]

Integrating,

\[
\boxed{
\operatorname{Var}(T_n)
\ge
\frac1{16e}
\int_0^\infty
E\sum_e
(\underline R_e(t)\wedge1)^2
1_{B_e(t)}1_{\{e\in\gamma\cap\gamma^t\}}\,dt.
}
\tag{C07.2}
\]

This is the exact non-circular overlap obligation produced by the present resampling route.

A lower bound of order `n^(2/3+o(1))` for the integral on the right would prove the desired variance lower bound. Importantly, it is **not** enough to count common geodesic edges. Their common cavity depth enters quadratically at shallow depth.

This also clarifies the relation with ADH Question 16: an unweighted polynomial overlap theorem is relevant but is not, by itself, the weighted estimate C07 requires.

## 5. R07-GH-X02 — unweighted overlap alone cannot control weighted sensitivity pointwise

**Label: PROVED ROUTE OBSTRUCTION; it does not refute the FPP conjecture or any expectation-level overlap theorem.**

For every integer `m>=2`, let `L=m+1` and consider the nearest-neighbor two-row ladder

\[
\{0,\dots,L\}\times\{0,1\}.
\]

Give every horizontal edge weight

\[
a=1/m.
\]

Give the two endpoint vertical rungs weight `epsilon/2` with

\[
\epsilon=1/m,
\]

and every internal vertical rung a sufficiently large rational weight. Let

\[
s=(0,0),\qquad t=(L,0),
\]

and mark the first `m` bottom horizontal edges.

The unique geodesic is the bottom rail and contains all `m` marked edges. For any marked edge `e`, the best avoiding path is the top bypass, of cost

\[
La+\epsilon.
\]

The best path using `e`, with the own weight of `e` deleted from its cost, has off-`e` cost

\[
(L-1)a.
\]

Therefore its Exp(1) cavity threshold is exactly

\[
\boxed{R_e=(La+\epsilon)-(L-1)a=a+\epsilon=2/m.}
\tag{5.1}
\]

For any `r`, with `Y=min(X,r)`,

\[
q(r)=\operatorname{Var}(Y)
\le E(Y-r)^2
=E[(r-X)^2 1_{\{X<r\}}]
\le r^2P(X<r)
\le r^3.
\tag{5.2}
\]

Hence the `m` common marked geodesic edges satisfy

\[
\boxed{
\sum_{e\text{ marked}}q(R_e)
\le
m(2/m)^3
=
8/m^2\longrightarrow0,
}
\tag{5.3}
\]

while their unweighted overlap count is `m -> infinity`.

Thus there is no deterministic implication from a large unweighted common-geodesic count to a large weighted cavity-sensitivity sum. Any expectation-level theorem must control shallow-depth rarity or another geometric quantity; raw overlap count alone cannot supply C07.

The construction is a finite positive rational-weight planar ladder. It is a route obstruction, not an assertion that such configurations are typical under iid exponential FPP.

## 6. Independent R08 audit — R08-X001

**Audit ID: `R07-AUDIT-R08-X001-01 = PASS`.**

The neighboring report `runs/R08/2026-09-16T1329Z_fpp-axis-gap-a1c93e.md` proves a shared-bypass obstruction: `m` marked bottom edges can all have the same positive deletion margin `epsilon` while that margin is generated by one common bypass.

I independently rederived it without using R08's checker. With horizontal weights `1`, endpoint rung weights `epsilon/2`, and internal rung weight

\[
H=10L+10+\epsilon,
\]

the bottom rail has unique cost `L`; the endpoint-rung/top-rail bypass has cost `L+epsilon`; and every path using an internal rung costs more than `L+epsilon`. Deleting any one marked bottom edge therefore leaves the same unique top bypass and increases the passage time by exactly `epsilon`.

The R07 exact checker independently verifies `m=1,...,20` and

\[
\epsilon\in\{1/7,2/5,3/2,17/13\}
\]

using `Fraction` arithmetic, exact Dijkstra distances and exact shortest-path counts: 80 parameter cases, all PASS.

**Audit scope:** PASS for R08-X001 only. This does not audit or prove the strict-convexity source problem. R08's metric remains at zero positive strict-gap lower bound and status OPEN.

## 7. Exact checker and readback evidence

Executed locally before upload:

- `artifacts/R07/20260916T1425Z_weighted_overlap_audit_checker.py`
- `artifacts/R07/20260916T1425Z_weighted_overlap_audit_checker.out`

Local SHA-256:

- source: `7f3df333aaa7c4d41cbe36bb53d5f9730dc91f16660b2dfd46c510bcef010c82`;
- output: `78e6e7bc00b80b22c97eebe0a02cb12da23e4b42116e49f25543f7b3fc3f3222`.

The checker verifies exactly:

1. on a rational 3-bit product space, `rho d/d rho Cov(f(X),f(X^rho)) = sum_e E[D_e f(X)D_e f(X^rho)]`;
2. the algebraic kernel decomposition (3.1);
3. the independent 80-case R08-X001 audit;
4. the shallow-overlap ladder thresholds `R_e=2/m` and the exact algebraic bound `m(2/m)^3=8/m^2` for `m=2,...,40`.

GitHub source creation/readback commit:

- `eeb4da6c7f705ab9beba0aae16f5c1ec02ba51b0`.

GitHub output creation/readback commit:

- `1de80fdeea9bbf64db9e6a889db1d0d32f0cc147`.

The archived output ends `PASS`.

These are self-checks for R07 claims except the separately identified independent R08 audit; no audit of R07 by another task is fabricated.

## 8. Ledger, failed routes, and next attack

Current R07 claim ledger:

- `R07-GH-C01`: `Var(T_n)>=c_PP log n`, `n>=2` — **KNOWN**; fixed metric unchanged.
- `R07-GH-C02`: Doob variance identity — **KNOWN / proof on page**.
- `R07-GH-C03`: exact one-edge Exp cavity sensitivity — **PROVED elementary**.
- `R07-GH-X01`: uniform Boolean-membership-to-weighted-sensitivity comparison — **REFUTED ROUTE**.
- `R07-GH-C04`: product-refresh/ANOVA integrated sensitivity — **KNOWN / proof on page**.
- `R07-GH-C05`: exact refresh-cavity covariance derivative — **PROVED**.
- `R07-GH-C06`: explicit depth-weighted kernel lower bound — **PROVED**.
- `R07-GH-C07`: weighted survived-geodesic-overlap variance reduction — **PROVED REDUCTION**.
- `R07-GH-X02`: unweighted overlap count alone controls weighted sensitivity pointwise — **REFUTED ROUTE**.
- KPZ variance target — **OPEN**.
- transversal exponent — **OPEN**.
- limiting law — **OPEN**.

Failed/insufficient routes now preserved explicitly:

1. treating Boolean influence as weighted passage sensitivity (`X01`);
2. inserting the unknown KPZ variance into a chaos-transition scale (circular);
3. using curvature/nonflatness without proving it for the present direction/model;
4. using raw common-geodesic overlap without controlling common cavity depth (`X02`);
5. multiplying one-edge deletion-margin gains as if detours were independent (R08-X001, independently audited here).

### Next attack

The sharp remaining lower-bound obligation produced by this route is to prove, for some non-circular noise window `I_n`,

\[
\int_{I_n}
E\sum_e
(\underline R_e(t)\wedge1)^2
1_{B_e(t)}1_{\{e\in\gamma\cap\gamma^t\}}\,dt
\gg \log n,
\]

and ultimately of order `n^(2/3+o(1))` if this route is to reach KPZ.

The simplest still-unproved special case worth attacking next is a **depth-truncated overlap estimate**: find fixed `delta>0` and a noise scale/window that can be controlled without the unknown variance, and lower-bound

\[
E\#\{e:\ B_e(t),\ e\in\gamma\cap\gamma^t,\ \underline R_e(t)\ge\delta\}.
\]

C07 would then convert it immediately into a variance lower bound with explicit constant `c(delta)>0`.

The closest solved analogue in the literature is the curvature/nonflat Newman-Piza/Pemantle-Peres power-law lower-bound mechanism, which gains localization of the geodesic to a sublinear strip. What the unrestricted `e1` Exp(1) problem lacks is exactly such non-circular geometric localization or an alternative lower control on depth-truncated common overlap.

This is only the first no-movement run after the canonical metric baseline, so the three-run stuck protocol has **not** triggered.

## ledger_delta

```yaml
ledger_delta:
  task: "R07 HARD OUTSIDE"
  source: "Kardar-Parisi-Zhang (1986); Auffinger-Damron-Hanson, arXiv:1511.03262, Question 13"
  target: "For iid Exp(1) undirected nearest-neighbor FPP on Z^2, Var(T(0,n e1)) = n^(2/3+o(1))"
  metric: "strongest rigorously proved uniform lower-bound function b(n) for Var(T(0,n e1)), constants and n-domain retained"
  domain: "integers n>=2, fixed direction e1, iid mean-one Exp edge weights"
  before: "b(n)=c_PP log n, c_PP>0 non-explicit"
  after: "b(n)=c_PP log n, c_PP>0 non-explicit — no movement"
  status: "OPEN"
  unchanged_count: 1
  exact_evidence:
    - "runs/R07/2026-09-16T1425Z_kpz_weighted_overlap_02.md: C05-C07, X02"
    - "artifacts/R07/20260916T1425Z_weighted_overlap_audit_checker.py @ eeb4da6c7f705ab9beba0aae16f5c1ec02ba51b0"
    - "artifacts/R07/20260916T1425Z_weighted_overlap_audit_checker.out @ 1de80fdeea9bbf64db9e6a889db1d0d32f0cc147"
  audit_ids: []
  outgoing_audits:
    - "R07-AUDIT-R08-X001-01=PASS"
  literature_check_date: "2026-09-16"
  access_limitations:
    - "large intake JSONL reads were model-visible truncated; recorded PARTIAL rather than complete"
```
