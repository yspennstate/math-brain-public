Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE-LEVEL BEFORE/AFTER: the repository-internal binary-LCS interval strictly moves from `L <= gamma_2 <= U_R` to `L <= gamma_2 <= U_C < U_R` by the newest P02 companion certificate, with `L=0.792665992`. P13 MECHANISM BEFORE/AFTER: the previous all-formal-state transfer `|E_s R_N-N gamma_w|<=2w` gives a generic interval of width `4w/N`; this run proves an extremal-boundary finite bracket of width at most `w/N`, equivalently midpoint radius at most `w/(2N)`, and identifies its lower endpoint with the genuine dependent width-`w` band-LCS expectation. At `w=6`, the certified finite-to-infinite radius drops from `12/N` to at most `3/N`.**

# P13 / T02 — extremal boundary envelopes and a band-LCS finite bracket

## 1. Scope, source, continuity, and companion coordination

This run follows `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`, and its LIVE20 assignment of P13 to T02. The target is the genuine Chvátal–Sankoff constant

\[
\gamma_2=\lim_{n\to\infty}\frac{\mathbf E LCS(X_1^n,Y_1^n)}n
\]

for two independent iid uniform binary strings. The LCS match indicators in a column share the same source letter and are therefore dependent; the independent Bernoulli matching model is not substituted anywhere below.

Necessary continuity only was recovered. The latest own substantive report is

`proofnet24/P13-progress-lcs/runs/2026-09-20/2026-09-20T08-17-18Z__strong-pathwise-span-linear-transfer.md`, blob `beccae1f81c74b1404861a99b72eed8ab9b9c1e9`.

That report proved the sharp all-formal-state common-word span

\[
|R_N(s;\omega)-R_N(t;\omega)|\le m=2w
\]

and hence

\[
|\mathbf E_sR_N-N\gamma_w|\le 2w.
\]

The latest P02 companion report now visible is

`proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T08-03-23Z__successor-slack-semigroup-report.md`, blob `a2c532b3ab018a09fbddee273dcd0a39a63a75d6`, creation commit `d2e3fc0fa3e0d7f1fc0ea98ddd9e07245613fedf`.

P02 remains on the complementary covering/cone variational upper-bound route. It proves a new exact finite-operator rate `lambda_C<lambda_R`, hence

\[
\boxed{L\le\gamma_2\le U_C<U_R},
\]

with an exact logarithmic separator

\[
U_C<0.82627594276228262501510658153729663282346199619319002388080618331256294443029954<U_R.
\]

Its reported high-precision diagnostic gain is about `1.56286669461208485518e-80`; that decimal difference is diagnostic only, while `U_C<U_R` is exact in the companion proof. Thus the source-level interval does strictly shrink in this invocation, but that shrink is companion-derived and must not be attributed to the new P13 lower-side mechanism.

Fresh source navigation on 2026-09-20 retained Alexander Tiskin, `arXiv:2212.01582v2`, revised 2024-08-13. Its current abstract still describes the exact binary coefficient as unresolved. The v2 source is the corrected version; this project does not use the earlier removed stochastic-process claims. The retained public lower endpoint remains `0.792665992` from Heineman–Miller–Reichman–Salls–Sárközy–Soiffer, `arXiv:2407.10925`.

Short pre-LIVE20 handoff only: P0342 had already been terminally handed off at frozen `2/2`; the later P0205 screen admitted no successor because its source notation could not be frozen source-faithfully. Retired I0051/clade work remains retired and is not reopened.

## 2. Exact dependence-preserving strip recursion

Fix half-width `w>=1` and put

\[
m=2w.
\]

A formal strip state is

\[
s=(x,g),\qquad x=(x_1,\ldots,x_m),\quad g=(g_1,\ldots,g_m)\in\{0,1\}^m.
\]

Let

\[
V_0=0,\qquad V_k=\sum_{i=1}^k g_i.
\]

For one fresh actual source pair `(u,v)`, define

\[
a_i={\bf1}_{\{x_{i+1}=v\}}\quad(0\le i<m),
\qquad a_m={\bf1}_{\{u=v\}}.
\]

The same incoming `v` is used in every `a_i`, which is precisely the column dependence that an independent Bernoulli match matrix would destroy. The updated profile is

\[
Q_0=\max\{V_1,V_0+a_0\},
\]

\[
Q_k=\max\{Q_{k-1},V_k+a_k,V_{k+1}\},\qquad1\le k<m,
\]

\[
Q_m=\max\{Q_{m-1},V_m+a_m\}.
\]

Then

\[
x'=(x_2,\ldots,x_m,u),
\qquad g'_k=Q_k-Q_{k-1},
\]

and the central one-step reward is

\[
\rho(s;u,v)=Q_w-V_w\in\{0,1\}.
\]

For a fixed length-`N` future source word `omega`, write `R_N(x,g;omega)` for the cumulative central reward.

The inherited unrolled-strip identity from the preceding P13 proof will be used in full. Put initial cross-section points `p_k=(k,0)`, `0<=k<=m`, final central point `z_N=(w+N,N)`, and let `M_k(x;omega)` be the maximum number of match diagonals on a legal directed strip path from `p_k` to `z_N`. Then

\[
\boxed{
R_N(x,g;\omega)
=
\max_{0\le k\le m}\{V_k+M_k(x;\omega)\}-V_w.
}
\tag{2.1}
\]

The path scores `M_k` depend on the raw source letters and future source word but not on the initial gradient profile `g`.

## 3. Extremal normalized boundary profiles

Normalize the initial boundary by its central value:

\[
b_k(g):=V_k-V_w.
\]

Since every gradient bit lies in `{0,1}`, for `k<w`,

\[
k-w\le b_k(g)\le0,
\tag{3.1}
\]

while for `k>w`,

\[
0\le b_k(g)\le k-w.
\tag{3.2}
\]

Define the two deterministic extremal gradient profiles

\[
g^-=(1^w,0^w),
\qquad
g^+=(0^w,1^w).
\]

Their normalized boundaries are

\[
b^-_k=\min(k-w,0),
\qquad
b^+_k=\max(k-w,0).
\tag{3.3}
\]

Therefore every formal binary-gradient boundary is trapped coordinatewise:

\[
\boxed{b^-_k\le b_k(g)\le b^+_k\quad(0\le k\le m).}
\tag{3.4}
\]

This is the structural observation that removes the need to compare an unknown stationary gradient profile with an arbitrary formal state.

## 4. New theorem: pathwise extremal-boundary bracket

### Theorem 4.1

For every `w`, every raw window `x`, every horizon `N`, every actual source word `omega`, and every formal gradient profile `g`,

\[
\boxed{
R_N(x,g^-;\omega)
\le
R_N(x,g;\omega)
\le
R_N(x,g^+;\omega).
}
\tag{4.1}
\]

Moreover,

\[
\boxed{
0\le R_N(x,g^+;\omega)-R_N(x,g^-;\omega)\le w.
}
\tag{4.2}
\]

#### Proof

By (2.1),

\[
R_N(x,g;\omega)=\max_k\{b_k(g)+M_k(x;\omega)\}.
\]

The coordinatewise inequalities (3.4) immediately imply (4.1).

For the width estimate, note that

\[
0\le b^+_k-b^-_k=|k-w|\le w.
\]

Hence, for every `k`,

\[
b^+_k+M_k\le b^-_k+M_k+w\le R_N(x,g^-;\omega)+w.
\]

Taking the maximum over `k` proves

\[
R_N(x,g^+;\omega)\le R_N(x,g^-;\omega)+w.
\]

Together with (4.1), this gives (4.2). QED.

The theorem is pathwise and uses the same actual source word in all three recursions. No independence is inserted among match cells.

## 5. The lower extremal process is exactly central-start band LCS

The lower process has an additional exact simplification.

The preceding P13 report proved the geometric splice inequalities

\[
M_k\le M_w+(w-k)\quad(k<w),
\tag{5.1}
\]

and

\[
M_k\le M_w\quad(k>w).
\tag{5.2}
\]

Using `b^-_k=k-w` for `k<w` and `b^-_k=0` for `k>=w`, (5.1)–(5.2) imply

\[
b^-_k+M_k\le M_w
\]

for every `k`, while the `k=w` term equals `M_w`. Therefore

\[
\boxed{
R_N(x,g^-;\omega)=M_w(x;\omega).
}
\tag{5.3}
\]

This identity is useful because `M_w` is a finite statistic involving only actual iid source letters.

Translate the strip by the central offset `w`. A path from `p_w=(w,0)` to `z_N=(w+N,N)` becomes a path from `(0,0)` to `(N,N)` constrained to

\[
|i-j|\le w.
\]

The `N` horizontal-source letters seen by that translated path are the appropriate consecutive `N` letters from the concatenation of the old raw `X` window and future `U` letters; when the old raw window is uniform iid, these are iid uniform binary letters. The `N` vertical-source letters are the future `V` letters. Since the source pairs `(U_t,V_t)` are iid with independent coordinates and the old raw window comes from past `U` letters, the two length-`N` strings are independent iid uniform binary strings.

Thus, if `L_{N,w}^{band}` denotes the ordinary binary LCS score with paths restricted to the diagonal corridor `|i-j|<=w`, then under a uniform iid raw `X` window and an independent genuine future source word,

\[
\boxed{
R_N(X,g^-;\omega)\ \stackrel d=\ L_{N,w}^{band}.
}
\tag{5.4}
\]

This is the original dependent LCS model: all cells in a row or column inherit their shared source letters exactly as in the usual LCS grid.

## 6. New finite-to-infinite bracket

Let `pi_w` be the inherited unique stationary law of the width-`w` strip chain and let `gamma_w` be its stationary mean reward.

The raw-window component evolves autonomously by

\[
x'=(x_2,\ldots,x_m,U),
\]

where `U` is a fresh fair bit. This shift register has the unique stationary marginal `Unif({0,1}^m)`. Consequently the `x`-marginal of `pi_w` is uniform, even though `x` and the gradient profile `g` are generally dependent. The future source word is independent of the present state.

Define the two finite exact expectations

\[
A^-_{N,w}:=\mathbf E_{X,\omega}R_N(X,g^-;\omega),
\]

\[
A^+_{N,w}:=\mathbf E_{X,\omega}R_N(X,g^+;\omega),
\]

where `X` is uniform on `{0,1}^{2w}` and `omega` is a genuine iid source-pair word, independent of `X`.

Start the strip in stationarity. Then

\[
\mathbf E_{\pi_w}R_N=N\gamma_w.
\]

Applying the pathwise bracket (4.1) conditionally on the stationary raw window `X`, the stationary gradient `G`, and the future word `omega`, then averaging, gives

\[
\boxed{
A^-_{N,w}\le N\gamma_w\le A^+_{N,w}.
}
\tag{6.1}
\]

Averaging (4.2) gives

\[
\boxed{
0\le A^+_{N,w}-A^-_{N,w}\le w.
}
\tag{6.2}
\]

Therefore

\[
\boxed{
\frac{A^-_{N,w}}N
\le\gamma_w\le
\frac{A^+_{N,w}}N,
\qquad
\text{interval width}\le\frac wN.
}
\tag{6.3}
\]

Equivalently, with midpoint

\[
C_{N,w}:=\frac{A^-_{N,w}+A^+_{N,w}}2,
\]

\[
\boxed{
\left|\gamma_w-\frac{C_{N,w}}N\right|
\le\frac{w}{2N}.
}
\tag{6.4}
\]

This is a strict mechanism improvement over the previous all-formal-state theorem. That theorem gave radius `2w/N` around an arbitrary-state finite expectation; (6.4) gives radius at most `w/(2N)` around a completely finite true-source expectation. The radius improves by a factor of four, and the corresponding certified interval width improves from `4w/N` to at most `w/N`.

At `w=6`,

\[
\boxed{
\text{previous generic radius }=\frac{12}{N},
\qquad
\text{new extremal-envelope radius}\le\frac3N.
}
\tag{6.5}
\]

This gain does not rely on reset times or mixing rates.

## 7. Exact finite computation is now a valid lower bound on gamma_2

By (5.3)–(5.4),

\[
A^-_{N,w}=\mathbf E L_{N,w}^{band}.
\tag{7.1}
\]

The bracket (6.3) implies

\[
\frac{\mathbf E L_{N,w}^{band}}N\le\gamma_w.
\tag{7.2}
\]

Also, the band-constrained LCS is no larger than the unrestricted LCS for the same pair of strings. Letting `N->infinity` in (6.3) shows `A^-_{N,w}/N -> gamma_w`, while the unrestricted normalized expectation tends to `gamma_2`. Hence

\[
\boxed{\gamma_w\le\gamma_2.}
\tag{7.3}
\]

Combining (7.2) and (7.3), every exact finite band computation has the proved source transfer

\[
\boxed{
\frac{\mathbf E L_{N,w}^{band}}N
\le\gamma_2.
}
\tag{7.4}
\]

This addresses the owner's warning directly: a finite computation is not being promoted to an asymptotic statement without proof. Equation (7.4) is the transfer proof.

The current exact examples do not beat the public lower endpoint `L`; therefore P13 claims no source lower-endpoint movement from them in this run.

## 8. Exact self-check and finite examples

The analytic proof above is the theorem. The finite checker is a self-check, not the source of the all-width argument.

Code:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T09-17-30Z__boundary_envelope_checker.py`

creation commit `b4eef44d5fbd2a54fca379a26cc6fa387afcb33b`, verified read-back blob `cccb965739bf771fa58f3eec3905494b7a88ecf5`.

Executed output:

`proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T09-17-30Z__boundary_envelope_checker.out`

creation commit `4e1053bb45519f0be1313eaba0e046c5e7b38563`, verified read-back blob `cabe9d40779c442e330ed57239b454163d548143`.

The checker uses the exact shared-`Y` recurrence above. It exhaustively verifies the extremal-envelope inequality, the lower identity `R^-=M_w`, and the central-strip/band-LCS correspondence on:

- `w=1`, all formal states and source words through `N=4`: `5440` state-word checks;
- `w=2`, through `N=3`: `21504` checks;
- `w=3`, through `N=2`: `81920` checks.

It then computes exact finite expectations. At `w=6` it gives

\[
A^-_{1,6}=\frac12,\qquad A^+_{1,6}=1,
\]

\[
A^-_{2,6}=\frac98,\qquad A^+_{2,6}=2,
\]

\[
A^-_{3,6}=\frac{29}{16},\qquad A^+_{3,6}=3.
\]

These short horizons are far below the retained lower endpoint after normalization and are not represented as source progress. The output terminates with

`ALL_EXACT_CHECKS_PASS`.

One checker line uses the independently known small-width value `gamma_1=7/10` only as an additional sanity check of the new bracket; that hard-coded value is not used to prove the theorem.

## 9. What failed and what obstruction remains

The first attempted strengthening after the previous pathwise-span theorem was to improve the arbitrary-state constant below `2w` directly. That cannot work at the same level of generality: the previous report already proved the all-formal-state common-word diameter `2w` is sharp. The successful change of mechanism here is to stop comparing arbitrary formal states. Instead, stationarity supplies an exactly uniform raw-window marginal, and all unknown gradient profiles can be sandwiched between two deterministic extremal normalized boundaries.

A second tempting overclaim would be to say that the new `w/(2N)` midpoint radius itself improves the present source lower endpoint. It does not. The exact finite values checked here are too small, and no width/horizon pair was exactly computed with `A^-_{N,w}/N>L`. Therefore P13 source-level lower movement is **none** in this run.

The computational obstruction is now well localized. Direct enumeration of `A^-_{N,w}` costs exponentially in both the `2w` raw-window bits and the horizon source word. The new theorem removes the asymptotic-transfer penalty but not that state explosion. To convert the mechanism into a source lower-endpoint improvement, one needs an exact compressed recurrence or Bellman subsolution at a width where the band process itself exceeds `L`.

## 10. Next attack

The next P13 attack is an exact **extremal-boundary quotient** rather than another full-state span estimate.

Use `g^-=(1^w,0^w)` as the canonical lower boundary and construct the minimal reachable quotient needed to propagate `A^-_{N,w}` (equivalently the genuine width-`w` band-LCS score) while retaining the actual raw source letters responsible for row/column dependence. The first objective is a rational Bellman lower certificate at a width beyond the inherited `w<=5` obstruction; if a tractable quotient reaches `w>=11`, test whether its exact average reward exceeds

\[
L=0.792665992.
\]

Because (7.4) has zero subtraction, any exact certificate above `L` would immediately raise the source lower endpoint. If the quotient still explodes, the distinct recovery route is to exploit the upper/lower extremal pair itself: derive a carry/second-class recursion for the finite gap `R^+-R^-` and search for a smaller state descriptor than the full band frontier.

P02 should continue its complementary variational/cone upper route; P13 should not duplicate the successor-slack semigroup computation.

## 11. Source-level and mechanism-level accounting

Source-level before:

\[
L\le\gamma_2\le U_R.
\]

Source-level after, by the newest P02 companion certificate:

\[
\boxed{L\le\gamma_2\le U_C<U_R.}
\]

P13 source lower endpoint: unchanged at `L=0.792665992`.

P13 mechanism before:

\[
|\mathbf E_sR_N-N\gamma_w|\le2w,
\]

which gives a generic finite interval of width `4w/N`.

P13 mechanism after:

\[
\boxed{
A^-_{N,w}\le N\gamma_w\le A^+_{N,w},
\qquad
A^+_{N,w}-A^-_{N,w}\le w,
}
\]

with

\[
\boxed{A^-_{N,w}=\mathbf E L_{N,w}^{band}}
\]

for the genuine dependent binary LCS model. Thus the finite interval width is at most `w/N`, midpoint radius at most `w/(2N)`, and every exact lower finite value `A^-_{N,w}/N` is a proved lower bound on `gamma_2`.

Status remains **PARTIAL / source OPEN**. The P02 upper endpoint is repository-internal exact work pending later independent review and public-priority checking; the P13 theorem is a new internal candidate theorem with complete proof here and exact self-check, likewise pending later independent review.

```yaml
ledger_delta:
  slot: P13
  native_assignment: T02_binary_LCS
  status: PARTIAL_SOURCE_OPEN
  runtime:
    model: GPT-5.6_Sol
    reasoning_level: UNVERIFIED
    requested_gpt6_maximum_satisfied: false
  source_metric:
    lower: "L = 0.792665992 = 99083249/125000000"
    before: "L <= gamma_2 <= U_R"
    after: "L <= gamma_2 <= U_C < U_R"
    movement_origin: "P02 companion successor-slack semigroup exact upper certificate"
    p13_lower_endpoint_movement: none
  mechanism:
    before: "for arbitrary formal start, |E_s R_N - N gamma_w| <= 2w; interval width 4w/N"
    after: "A^-_{N,w} <= N gamma_w <= A^+_{N,w}; A^+_{N,w}-A^-_{N,w} <= w; midpoint radius <= w/(2N)"
    width6_before_radius: "12/N"
    width6_after_radius: "<=3/N"
    finite_lower_identity: "A^-_{N,w} = E L^{band}_{N,w}"
    source_transfer: "A^-_{N,w}/N <= gamma_w <= gamma_2"
  new_results:
    - "coordinatewise extremal normalized boundary profiles b^- <= b(g) <= b^+"
    - "pathwise extremal-boundary bracket R^- <= R_g <= R^+"
    - "pathwise gap R^+-R^- <= w"
    - "exact lower extremal identity R^-=M_w"
    - "M_w distribution equals genuine iid binary width-w band LCS"
    - "stationary finite bracket of width <=w/N"
    - "zero-subtraction finite lower transfer E L^{band}_{N,w}/N <= gamma_2"
  checker:
    code_path: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T09-17-30Z__boundary_envelope_checker.py"
    code_commit: b4eef44d5fbd2a54fca379a26cc6fa387afcb33b
    code_blob: cccb965739bf771fa58f3eec3905494b7a88ecf5
    output_path: "proofnet24/P13-progress-lcs/artifacts/2026-09-20/2026-09-20T09-17-30Z__boundary_envelope_checker.out"
    output_commit: 4e1053bb45519f0be1313eaba0e046c5e7b38563
    output_blob: cabe9d40779c442e330ed57239b454163d548143
    status: ALL_EXACT_CHECKS_PASS
  failure:
    - "no exact A^-_{N,w}/N computed in this run exceeds L; therefore no P13 source lower-endpoint movement"
    - "raw exact enumeration remains exponential in width and horizon"
  next_attack: "construct an exact reachable extremal-boundary quotient/Bellman lower certificate beyond the inherited w<=5 obstruction, preferably at w>=11; if state explosion persists, derive a reduced carry recursion for R^+-R^-"
  companion:
    P02_latest_report: "proofnet24/P02-progress-lcs/runs/2026-09-20/2026-09-20T08-03-23Z__successor-slack-semigroup-report.md"
    P02_latest_commit: d2e3fc0fa3e0d7f1fc0ea98ddd9e07245613fedf
    coordination: "P02 upper variational/cone route; P13 dependent band lower/transfer route"
  previous_successor_handoff: "P0342 terminal handoff preserved at 2/2; P0205 not admitted; I0051 clade work remains retired"
```
