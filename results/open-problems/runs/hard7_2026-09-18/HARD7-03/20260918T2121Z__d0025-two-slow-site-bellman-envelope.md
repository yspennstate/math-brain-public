Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **metric `L <= Delta_2(Q)`: `0 -> 0` (no movement); methods B8, B11, B19.** GPT-6/maximum was requested in prompt text, but this runtime does not expose an authenticated reasoning-effort setting and the scheduler has no binding model/reasoning selector, so I do not claim otherwise.

# HARD7-03 — exact two-slow-site current envelope for D0025

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source status, and why this run changes the route

I resumed canonical claim `D0025`, Seppäläinen Problem 4, from the preceding HARD7-03 report

`runs/hard7_2026-09-18/HARD7-03/20260918T2022Z__d0025-admission-k2-product-obstruction.md`.

I reread the controlling HARD7 and new-methods instructions, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the active claim `operations/claims/D0025.md`, and current neighboring ownership screens. The claim remains owned only by `HARD7-03`; I found no successor, retirement, posting, or collision that supersedes it.

The frozen source-valid case remains

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

with primary metric

\[
L\le \Delta_2(Q),\qquad
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The metric remains `L=0`; this run does **not** prove a plateau. It does, however, prove the first nontrivial finite slow-block current ceiling in a form that is valid without product invariant measures, which was the exact remaining obligation from the previous report.

Fresh bounded literature checks dated 2026-09-18 UTC recovered the original 1999 Seppäläinen source, Allan Sly's `K=1` iid-disorder plateau theorem (`arXiv:1609.06589`), and the 2025 published Gonçalves–Hayashi–Sasada partial-exclusion product/gradient characterization. I found no new source closing the constant-rate disordered `K>=2` plateau problem. This remains `OPEN_BY_BOUNDED_SEARCH`, not a worldwide-openness claim.

Primary-source / baseline links checked this run:

- Seppäläinen 1999: https://doi.org/10.11606/resimeusp.v4i1.74889
- Sly 2016: https://arxiv.org/abs/1609.06589
- Gonçalves–Hayashi–Sasada, published 2025 in ALEA 22: https://doi.org/10.30757/ALEA.V22-12

## 2. B8 — discretize the bottleneck into a controlled two-site block

The previous run proved that the homogeneous asymmetric `K=2` process already lacks the naive iid product equilibrium, so the next useful object must not assume explicit stationary marginals.

Take two consecutive slow sites `x,x+1` with

\[
\alpha_x=\alpha_{x+1}=c=\tfrac12.
\]

Write the local state as

\[
X_t=(i_t,j_t)=(\eta_t(x),\eta_t(x+1))\in\{0,1,2\}^2.
\]

Conditioned on the full outside configuration, only three kinds of local transitions are possible:

1. **left injection** `(i,j)->(i+1,j)` when `i<2`, at predictable intensity `u_t` satisfying `0<=u_t<=1`; indeed the actual intensity is `alpha_{x-1} 1{eta(x-1)>0}` and all site rates in the frozen binary environment are at most one;
2. **internal slow jump** `(i,j)->(i-1,j+1)` when `i>0,j<2`, at the fixed rate `c=1/2`;
3. **right exit** `(i,j)->(i,j-1)` when `j>0`, at predictable intensity `v_t` satisfying `0<=v_t<=c`; the actual intensity is `c 1{eta(x+2)<2}`.

Let `N_t` count right exits from `x+1` to `x+2`. Thus the full infinite interacting particle system induces a finite controlled process on nine local states, where the outside world appears only through adapted boundary intensities in the rectangles

\[
0\le u_t\le1,\qquad 0\le v_t\le\tfrac12.
\]

This is exactly the finite envelope needed by the previous report: no Markov assumption on the projected block and no guessed equilibrium are required.

## 3. B11 — exact dual/Bellman certificate

Define

\[
\lambda=\frac{71}{219}
\]

and the potential `h` on the nine states by

\[
\begin{array}{c|ccc}
 h(i,j)&j=0&j=1&j=2\\\hline
 i=0&0&179/219&294/219\\
 i=1&71/219&230/219&313/219\\
 i=2&88/219&239/219&316/219.
\end{array}
\]

For a fixed state `(i,j)`, let `L_{u,v}` be the local generator described above, with the internal rate fixed at `1/2` and with boundary rates `u,v` in their allowed ranges. The key pointwise inequality is

\[
\boxed{\quad v+(L_{u,v}h)(i,j)\le \lambda\quad}
\tag{1}
\]

for every one of the nine states and every allowed `u,v`.

The certificate is especially transparent because the coefficients of the two controls are all nonnegative. For injection they are

\[
\begin{array}{c|ccc}
 h(i+1,j)-h(i,j)&j=0&j=1&j=2\\\hline
 i=0&71/219&51/219&19/219\\
 i=1&17/219&9/219&3/219,
\end{array}
\]

and for right exit, including the unit counting reward, they are

\[
1+h(i,j-1)-h(i,j)\in
\left\{\frac{40}{219},\frac{104}{219},\frac{60}{219},\frac{136}{219},\frac{68}{219},\frac{142}{219}\right\},
\]

all positive. Hence the left side of (1) is maximized pointwise by the extremal controls

\[
u=1\quad(i<2),\qquad v=\frac12\quad(j>0).
\]

For these maximal controls the Bellman relation holds with equality in **every** state:

\[
\frac12\mathbf 1_{\{i>0,j<2\}}
  \bigl[h(i-1,j+1)-h(i,j)\bigr]
+\mathbf 1_{\{i<2\}}\bigl[h(i+1,j)-h(i,j)\bigr]
+\frac12\mathbf 1_{\{j>0\}}
  \bigl[1+h(i,j-1)-h(i,j)\bigr]
=\frac{71}{219}.
\tag{2}
\]

Equations (1)–(2) are the dual certificate. No optimization solver is needed to trust the final bound.

## 4. Exact finite-time theorem

### Theorem

For the frozen `K=2`, binary-rate process, suppose `x,x+1` are two consecutive slow sites of rate `1/2`. For **every** initial configuration and every `t>=0`, if `N_t` is the number of jumps from `x+1` to `x+2` by time `t`, then

\[
\boxed{
\mathbb E N_t\le \frac{71}{219}t+\frac{316}{219}.
}
\tag{3}
\]

In particular,

\[
\limsup_{t\to\infty}\frac{\mathbb E N_t}{t}\le\frac{71}{219}
=0.3242009132\ldots<\frac12.
\tag{4}
\]

### Proof

The compensated exit count

\[
M_t=N_t-\int_0^t v_s\,ds
\]

is a martingale. The usual jump-process Dynkin decomposition for the bounded function `h(X_t)` gives

\[
\mathbb E h(X_t)-h(X_0)
=\mathbb E\int_0^t (L_{u_s,v_s}h)(X_s)\,ds.
\]

Add the two equalities and use (1):

\[
\mathbb E N_t+\mathbb E h(X_t)-h(X_0)
\le \lambda t.
\]

Every displayed value of `h` is nonnegative and

\[
0\le h\le\frac{316}{219}.
\]

Therefore

\[
\mathbb E N_t
\le\lambda t+h(X_0)-\mathbb E h(X_t)
\le\lambda t+\frac{316}{219},
\]

which is (3). No stationarity, finite-volume equilibrium, product measure, or independence between the block and its exterior is used. QED.

This is stronger than the stationary envelope requested in the previous report: it is a uniform finite-time estimate valid under arbitrary adapted exterior forcing consistent with the source dynamics.

## 5. Sharpness for the two-site controlled envelope

The constant `71/219` is not merely a convenient dual upper bound. It is the exact optimum of this two-site controlled envelope.

Under maximal boundary rates `u=1` and `v=1/2`, the open two-site chain has stationary distribution

\[
\begin{array}{c|ccc}
 \pi(i,j)&j=0&j=1&j=2\\\hline
 i=0&3/219&6/219&8/219\\
 i=1&10/219&24/219&20/219\\
 i=2&64/219&44/219&40/219.
\end{array}
\]

The entries sum to one and satisfy the nine generator-balance equations exactly. Its right-exit current is

\[
\frac12\,\pi\{j>0\}
=\frac12\left(1-\frac{3+10+64}{219}\right)
=\frac{71}{219}.
\]

Thus the Bellman upper bound is attained by the extremal open-reservoir chain, so the two-site controlled capacity is exactly

\[
C_2=\frac{71}{219}.
\]

The exact `Fraction`-arithmetic checker and executed output are

- `artifacts/hard7_2026-09-18/HARD7-03/two_slow_pair_bellman.py`
- `artifacts/hard7_2026-09-18/HARD7-03/two_slow_pair_bellman.out`

and the output ends `ALL_EXACT_CHECKS_PASS`.

## 6. B19 — make the slow-block route an algorithm, and monotonicity of its envelopes

The same construction gives a canonical finite optimization problem for every block length `m`.

Define `C_m` as the supremal asymptotic right-exit current of an `m`-site capacity-two block with all internal/source rates `c=1/2`, arbitrary adapted left-boundary injection intensity in `[0,1]`, and arbitrary adapted right-boundary exit intensity in `[0,1/2]`. The interior jumps are the source-model jumps at rate `1/2` whenever allowed.

This definition is deliberately broader than any actual iid exterior, so every real all-slow block induces a feasible controlled block.

Moreover,

\[
\boxed{C_{m+1}\le C_m.}
\tag{5}
\]

Indeed, take any feasible controlled `(m+1)`-site system and project to its first `m` sites. The jump from site `m` into site `m+1` becomes a right-boundary departure for the projected `m`-block; its intensity is at most `1/2`, so the projected dynamics is feasible for the `m`-block problem. The long-time current across that internal bond and the final exit current differ only by the change in occupation of the last site, which is bounded by two; dividing by time removes this difference. Taking suprema proves (5).

Thus the source-model bottleneck program can be organized as the monotone sequence

\[
C_1\ge C_2\ge C_3\ge\cdots\ge C_\infty,
\]

where each `C_m` is a finite-state average-reward control problem with an exact rational Bellman certificate in principle. The previous product-measure obstruction is no longer a blocker.

There is also a direct connection back to the infinite iid environment. Almost surely, the binary iid rate field contains adjacent slow sites at finite distance to the right of any fixed bond. Integrated currents across two fixed bonds differ by the change in the finite number of particles between them, hence by a uniformly bounded amount. Consequently any asymptotic mean through-current in the frozen iid process is bounded by `C_2=71/219`. Translating this ceiling to the exact hydrodynamic-flux notation `f_{2,Q}` uses the standard integrated-current representation in the source hydrodynamics; I have not counted that standard identification as a new theorem here.

## 7. What moved, what did not, and next obligation

The frozen plateau-width metric did not move:

\[
L:0\longrightarrow0.
\]

So the source problem is still `PARTIAL / OPEN_BY_BOUNDED_SEARCH`.

The mathematical route **did** move substantially:

1. the previous vague “define a valid slow-block envelope” obligation is now completed;
2. the envelope is valid at finite time under arbitrary exterior forcing, not merely in stationarity;
3. its two-site value is exactly `C_2=71/219`, certified both by a primal stationary law and a dual Bellman potential;
4. the block envelopes are monotone in length and therefore define a rigorous limiting bottleneck program.

The next run must not repeat `[8,11,19]`. The highest-value next step is **not** another generic checker. It is one of:

- obtain an analytic bound on `C_\infty` (or a structurally informative `C_3`) that can plausibly be matched from below;
- prove a lower-current coupling near density one that reaches the limiting slow-block capacity;
- or identify a new invariant/duality that computes the homogeneous capacity-two maximal current without a product ansatz.

A positive plateau-width lower bound `L>0` remains the first genuine movement on the frozen source metric.

## 8. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  source: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  current_source_status: OPEN_BY_BOUNDED_SEARCH
  frozen_case:
    K: 2
    site_rate_law: "1/2 delta_{1/2} + 1/2 delta_1"
  metric: "certified lower bound L <= Delta_2(Q)"
  before: 0
  after: 0
  movement: no
  methods: [8, 11, 19]
  new_result:
    statement: "For any two consecutive rate-1/2 sites, every admissible exterior forcing satisfies E N_exit(t) <= (71/219)t + 316/219. The controlled two-site capacity is exactly C_2=71/219."
    exact_checker: artifacts/hard7_2026-09-18/HARD7-03/two_slow_pair_bellman.py
    checker_output: artifacts/hard7_2026-09-18/HARD7-03/two_slow_pair_bellman.out
    exact_output_status: ALL_EXACT_CHECKS_PASS
  structural_result: "C_{m+1} <= C_m for controlled all-slow block envelopes C_m."
  remaining_obligation: "Control C_infty and prove a matching lower current on a nontrivial density interval around rho=1; equivalently obtain L>0."
```
