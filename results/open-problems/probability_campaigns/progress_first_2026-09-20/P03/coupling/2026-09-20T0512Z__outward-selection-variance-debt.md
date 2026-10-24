Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.

# P03-B coupling report — outward-selection variance debt at a clean fresh split

**Status:** PROVED PARTIAL / RIGOROUS OBSTRUCTION TO A NAIVE CANCELLATION MECHANISM. The full Lyons–Pemantle–Peres speed-monotonicity conjecture remains unresolved here. This run identifies an exact first-order negative selection mechanism that survives annealed averaging even when the favorable split itself occurs at a completely fresh vertex. It also proves that the same one-step debt cannot by itself erase the initial +2 split credit.

**Native role:** P03-B, `6aabe777361481919c9e614646464772`, probabilistic regeneration/coupling and source-valid counterexample role under `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md` and `REGISTRY.md`.

**Captured master before write:** `ef5338314d7f34f45954f52db8fb90fde7797c63`.

**Previous own result used:** `probability_campaigns/progress_first_2026-09-20/P03/coupling/2026-09-20T0412Z__first-split-hazard-amplification.md`. That report improved the positive first-split term to first order `2 a_D(beta)` but showed that any bound retaining the worst degree-pair reverse-mismatch width diverges near the auxiliary critical line.

**Complementary P03-A result consumed, not duplicated:** `probability_campaigns/progress_first_2026-09-20/P03/analytic/2026-09-20T0401Z__harmonic-tail-stieltjes-extension.md`. P03-A controls the analytic escape tilt through Aidekon/Stieltjes identities. This report does not rederive those identities.

## 1. Source normalization and current baseline

Primary coupling source: Gerard Ben Arous, Alexander Fribergh and Vladas Sidoravicius, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*, arXiv:1111.5865. The tree has offspring variable `Z` with `P(Z=0)=0`. Their parameter `beta` is **outward child bias**: at a non-root vertex with `k` children,

\[
q_k(\beta):=P_\beta(\text{parent})=\frac{1}{1+\beta k},\qquad
P_\beta(\text{a specified child})=\frac{\beta}{1+\beta k}.
\]

Increasing `beta` is therefore stronger outward bias. The conjecture asks that the asymptotic speed `v(beta)` increase throughout the transient interval `beta>1/EZ`. The arXiv abstract records the old high-bias theorem `beta>=717`; later published constants and stronger later results are not confused with the full conjecture.

Bowditch--Tokushige, arXiv:1906.07913, prove differentiability in the ballistic/CLT regime and give a Gaussian covariance representation; arXiv:2006.03433 proves analyticity in the ballistic regime. Neither supplies the missing sign. Song--Wang--Xiang, J. Appl. Probab. 62 (2025), DOI 10.1017/jpr.2024.113, prove strict monotonicity in the reciprocal parent-bias parameter on their low-parent-bias interval when the minimum offspring is at least two; this is consistent with increasing speed in outward `beta`.

The fixed full-source metric remains `R_full: 1 -> 1`.

## 2. The probabilistic question left by the previous coupling bound

Assume for this report that

\[
d\le Z\le D<\infty\quad\text{a.s.},\qquad \beta d>1.
\]

Set

\[
q:=q_d(\beta),\qquad
Q:=q_Z(\beta),\qquad
\bar q:=EQ,\qquad
\sigma_q^2:=\operatorname{Var}(Q),
\]

and for `epsilon>0`

\[
\bar q_+(\epsilon):=E q_Z(\beta+\epsilon),\qquad
\bar\delta_\epsilon:=\bar q-\bar q_+(\epsilon)>0.
\]

Also define the infinitesimal split weight

\[
a_k(\beta):=\frac{k}{(1+\beta k)^2},\qquad
\bar a:=E a_Z(\beta).
\]

The preceding P03-B bounds treated post-split reverse mismatches by the worst possible pair of degrees. The correct next question is whether annealed fresh-environment averaging kills the first-order negative term. The answer is **no**: a simple and exact ancestor-selection tilt creates an order-`epsilon` negative contribution.

## 3. New exact lemma: an exposed parent is outward-step tilted

Consider a vertex `p` whose offspring count has just been revealed and is otherwise fresh. Suppose the two walks are still coincident and make a **common outward step** from `p` before any split at `p`. Conditional on `Z_p=k`, that event has probability

\[
1-q_k(\beta).
\]

Hence the offspring law of the exposed parent after conditioning on this common outward traversal is

\[
\boxed{
P_{\rm out}(Z=k)
=\frac{P(Z=k)(1-q_k(\beta))}{1-\bar q}.
}
\tag{3.1}
\]

This gives the exact mean parent threshold

\[
\begin{aligned}
E_{\rm out} q_Z(\beta)
&=\frac{E[Q(1-Q)]}{1-\bar q}\\
&=\boxed{\bar q-\frac{\sigma_q^2}{1-\bar q}}.
\end{aligned}
\tag{3.2}
\]

Thus conditioning on an outward traversal biases the exposed ancestor toward larger offspring and lowers its future parent probability by the exact amount

\[
\boxed{\frac{\sigma_q^2}{1-\bar q}}.
\tag{3.3}
\]

This is a genuine selection effect, not a worst-pair artifact. It vanishes exactly for a regular tree and is strictly positive for every nondegenerate offspring law.

## 4. Clean three-step cylinder and exact first-order negative debt

We now isolate a source-valid local cylinder in the common-uniform coupling.

1. Start with a fresh common vertex `p` while the walks have not separated.
2. They make a common outward step from `p` to a fresh child `x`.
3. At `x`, the next uniform lies in the favorable split interval

\[
q_{Z_x}(\beta+\epsilon)<U\le q_{Z_x}(\beta),
\]

so the `(beta+epsilon)` walk moves outward to a fresh child `y` while the `beta` walk moves inward back to `p`. The radial gap jumps by `+2`.
4. On the next step condition on the auxiliary-backstep event `U\le q=q_d(beta)`.

Because `x` was fresh and this was its first departure, the child `y` has an independent fresh offspring count with law `Z`. The degree of `p`, however, has the outward-step tilt (3.1).

Let `Delta_next` be the radial-gap increment on step 4. Conditional on the auxiliary backstep, its uniform is uniform on `[0,q]`, and all parent thresholds are at most `q`. Therefore, for any current degree pair `(i,j)`,

\[
E[\Delta_{\rm next}\mid i,j,U\le q]
=\frac{2}{q}\bigl(q_j(\beta)-q_i(\beta+\epsilon)\bigr),
\]

where `i` is the fresh higher-bias degree and `j` is the exposed-parent lower-bias degree. Averaging `i` with the original offspring law and `j` with (3.1) gives the exact identity

\[
\boxed{
E[\Delta_{\rm next}\mid\text{clean split},\ U\le q]
=\frac{2}{q}
\left[
\bar\delta_\epsilon-
\frac{\sigma_q^2}{1-\bar q}
\right].
}
\tag{4.1}
\]

Consequently this expected post-split backstep is **strictly negative** whenever

\[
\boxed{
\bar\delta_\epsilon<\frac{\sigma_q^2}{1-\bar q}.
}
\tag{4.2}
\]

Since

\[
\bar\delta_\epsilon
=E\left[\frac{\epsilon Z}
{(1+\beta Z)(1+(\beta+\epsilon)Z)}\right]
\le \epsilon\bar a,
\]

a completely explicit sufficient condition is

\[
\boxed{
0<\epsilon<
\epsilon_*:=
\frac{\sigma_q^2}{(1-\bar q)\bar a}.
}
\tag{4.3}
\]

For every nondegenerate bounded-support law, `epsilon_*>0`.

### Weighted cylinder contribution

The first common outward step has probability `1-bar q`. At the fresh vertex `x`, the favorable split event has annealed probability exactly `bar delta_epsilon`. The next auxiliary-backstep event has probability `q`, independently of the fresh offspring at `y`. Hence the clean cylinder in (4.1) has probability

\[
(1-\bar q)\bar\delta_\epsilon q.
\]

Multiplying by (4.1), the unconditional expected radial-gap contribution of the **post-split backstep itself** on this cylinder is

\[
\boxed{
2\bar\delta_\epsilon
\left[(1-\bar q)\bar\delta_\epsilon-\sigma_q^2\right].
}
\tag{4.4}
\]

As `epsilon downarrow 0`,

\[
\frac{\bar\delta_\epsilon}{\epsilon}\to\bar a,
\]

so

\[
\boxed{
\frac{1}{\epsilon}
E[\Delta_{\rm next};\text{clean cylinder}]
\longrightarrow
-2\bar a\,\sigma_q^2<0
}
\tag{4.5}
\]

for every nonregular offspring law.

### Interpretation

Equation (4.5) is the key obstruction of this run. It proves that post-split negative debt is **not automatically second order in epsilon after annealed averaging**. A favorable split occurs with probability `O(epsilon)`, but the ancestor it leaves behind has an `O(1)` outward-selection bias. Therefore the very next auxiliary backstep already produces an `O(epsilon)` negative contribution.

Any proof strategy asserting that fresh-environment averaging makes all reverse debt `o(epsilon)` is false.

## 5. New safety lemma: the immediate debt cannot erase the split credit

The previous section isolates a genuine first-order negative term, but it does **not** threaten monotonicity by itself.

On the same clean split event, the split contributes `+2`. On the next step, when `U>q`, both walks necessarily move outward, so the gap increment is zero. Therefore the exact expected contribution of the split plus its immediately following step, weighted by the initial common-outward event, is

\[
\boxed{
2\bar\delta_\epsilon
\left[(1-\bar q)(1+\bar\delta_\epsilon)-\sigma_q^2\right].
}
\tag{5.1}
\]

Because `0<=Q<=1`,

\[
\sigma_q^2\le \bar q(1-\bar q).
\]

Hence

\[
(1-\bar q)(1+\bar\delta_\epsilon)-\sigma_q^2
\ge
(1-\bar q)(1+\bar\delta_\epsilon-\bar q)>0,
\]

and thus

\[
\boxed{
\text{fresh split credit + one-step outward-selection debt is always positive.}
}
\tag{5.2}
\]

At first order, the negative/positive coefficient ratio on this clean interface is exactly

\[
\boxed{
\frac{\sigma_q^2}{1-\bar q}
}
\tag{5.3}
\]

relative to one unit of threshold credit, and the elementary variance bound gives

\[
\frac{\sigma_q^2}{1-\bar q}\le\bar q<1.
\tag{5.4}
\]

Thus one selected ancestor can consume only a strict fraction of the fresh-split credit. The remaining global difficulty is whether **repeated returns through a stack of selected ancestors** can accumulate enough such debt to overturn the credit before regeneration.

## 6. Exact bounded-support test: `{2,6}` at `beta=3/5`

Take the source-valid no-leaf law

\[
P(Z=2)=P(Z=6)=1/2,\qquad \beta=3/5.
\]

Then

\[
q_2=\frac5{11},\qquad q_6=\frac5{23},\qquad
\bar q=\frac{85}{253},
\]

and

\[
\sigma_q^2=\frac{900}{64009},\qquad
\bar a=\frac{22300}{64009}.
\]

Therefore

\[
\boxed{
\epsilon_*=
\frac{\sigma_q^2}{(1-\bar q)\bar a}
=\frac{759}{12488}
\approx0.0607783472.
}
\tag{6.1}
\]

For every `0<epsilon<759/12488`, the immediate post-split auxiliary backstep on the clean cylinder has negative annealed expected gap increment. For example, at `epsilon=1/100`, the bracket in (4.1) is

\[
-\frac{1623955}{91606746}<0,
\]

and the conditional expected radial-gap increment is

\[
-\frac{324791}{4163943}<0.
\]

This is an exact rational certificate, not a simulation. Again, it is **not** a counterexample to speed monotonicity; it is a counterexample to pointwise/one-interface positivity after annealed selection.

## 7. What changed and what remains

### New theorem / bound

* Exact outward-step degree tilt (3.1).
* Exact ancestor-threshold deficit `sigma_q^2/(1-bar q)` in (3.2)--(3.3).
* Exact clean-cylinder post-split debt identity (4.1).
* Explicit finite-epsilon negativity criterion (4.3).
* First-order negative coefficient `-2 bar a sigma_q^2` in (4.5), proving that reverse debt genuinely survives at derivative scale.
* Exact one-step safety inequality (5.1)--(5.4), showing a single selected ancestor cannot erase its generating split credit.

### Remaining obstruction

The missing global lemma is now more precise than the previous worst-pair bound. One must control the **stack of outward-selected exposed ancestors** seen during repeated post-split returns. The key object is no longer the range `q_d-q_D`; it is a return-weighted sum of selection deficits, beginning with

\[
\frac{\operatorname{Var}(q_Z(\beta))}{1-Eq_Z(\beta)}.
\]

A successful argument would show that successive ancestor-selection debts have a summable return kernel whose total is strictly below the initial split credit. The exact downcrossing chain from the earlier P03-B report is the natural clock for that kernel.

## 8. Next attack

1. Attach to every exposed ancestor on a clean outward ray its exact selection deficit

\[
s_k:=\bar q-E[q_Z(\beta)\mid\text{the corresponding outward traversal/return history}].
\]

2. Prove a return-kernel inequality of the form

\[
E\sum_{j\ge1} s_j\,1\{\text{ancestor }j\text{ is revisited before regeneration}\}
<1-\bar q
\]

or an equivalent split-credit normalization. The first-ancestor term is exactly `sigma_q^2/(1-bar q)` by this report.

3. Use the reversible downcrossing chain `D_j` from `2026-09-20T032221Z__exact-backstep-law-and-backstep-only-debt.md` to compute or dominate the revisit weights. The first test family should be two-point offspring, where every selection deficit reduces to one scalar posterior odds ratio.

4. If the stack cannot be bounded below credit, extract an explicit finite-depth cylinder with cumulative negative expectation. That would rigorously rule out the entire proposed regeneration-selection mechanism and force a pivot to a spine/covariance decomposition.

## Obligation ledger

- Full-source speed monotonicity: **OPEN**.
- High-bias/later low-parent-bias ranges: **known externally; not re-proved or claimed as new**.
- Previous exact backstep-chain law: **inherited**.
- Worst-pair divergence obstruction: **inherited**.
- Outward-selection variance identity: **PROVED PARTIAL, new in this campaign**.
- Order-`epsilon` clean-cylinder negative debt: **PROVED PARTIAL, new in this campaign**.
- One-step split-credit safety: **PROVED PARTIAL, new in this campaign**.
- Global return-weighted ancestor-stack bound: **OPEN**.

No simulation is used as proof, no inverse-bias contradiction is asserted, and no peer/historical file or canonical ownership was overwritten.
