Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but no authenticated applied-effort telemetry is exposed, so I do not claim GPT-6 maximum.**

# NM13-13 — T04 cluster-aware random 3-SAT: three-node Gaussian/Hankel tail gives a 4.38890 candidate upper bound

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker root: `proofnet24/NM13-13/progress-3sat/`  
Parent: **T04 — classical iid random 3-SAT with independent fair signs on three distinct variables per clause**  
Status: **OPEN / PARTIAL; CANDIDATE_FULL for the explicit fixed-count upper endpoint 4.38890, pending later independent review**

Claim ID: `NM13-13-T04-GAUSS3-TAIL-438890-UPPER-07`.

## 0. Source threshold before / after, separate from mechanism gain

The strongest explicit-decimal bracket I can presently support directly from the published source literature remains

\[
\boxed{3.52\le \liminf c_n\le \limsup c_n\le 4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability with high probability below `3.52` for the classical independent random 3-SAT model. Díaz--Kirousis--Mitsche--Pérez-Giménez prove asymptotic unsatisfiability at density `4.4898`. The August 2026 Carenini scaling-window theorem gives an `O(n/log n)` window for each fixed `k>=3` but does not locate the `k=3` center or prove convergence of the center sequence. Large-`k` threshold theorems do not settle `k=3`. Recent Gibbs-uniqueness results concern a different threshold. Rigorous interpolation provides stronger symbolic variational upper mechanisms, but this track has still not independently interval-certified a smaller published small-`k=3` decimal from that full variational problem. Therefore the **external explicit-decimal source metric is unchanged**:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]}.
\]

Separately, the strongest preserved project candidate before this run was the two-node Gaussian-tail interpolation certificate at `4.38900`. This run proves a stronger finite-support trial at

\[
\boxed{4.38890}.
\]

Thus the **project CANDIDATE_FULL bracket** moves

\[
\boxed{[3.52,4.38900]\longrightarrow[3.52,4.38890]},
\]

with width

\[
0.86900\longrightarrow0.86890
\]

and explicit endpoint gain

\[
\boxed{10^{-4}}.
\]

The candidate remains pending later independent review of the inherited interpolation transfer and this run's numerical certificate; it is not promoted here to the externally published literature metric.

## 1. Short handoff and preserved failures

The predecessor run introduced a two-node Gaussian quadrature lower envelope for the omitted Hausdorff-moment tail of the hard-field one-step K-SAT interpolation functional

\[
A(\alpha,\nu)
=-\sum_{k\ge1}\frac{\mu_k^2}{k}-2\alpha L,
\qquad
\mu_k=\mathbb E Q^k,
\qquad 0\le Q\le1,
\tag{1.1}
\]

and certified the project endpoint `4.38900`. The two-node rule uses tilted moments through degree three and a fourth-derivative Hermite remainder. Its residual obstruction was clear: the high-`Q` tilted law is narrow but measurably non-degenerate, so collapsing it to two nodes discards another order of curvature information.

The parked failures remain preserved and are not recycled: arbitrary rescue stars fail composition because separately safe child flips can jointly falsify a third clause; anchored degree-one rescue matching supplies a correct local penalty but has not been globally reoptimized in the full Díaz type polytope; positive clause-local multiplicative second moments hit the identical-pair obstruction at `log(2)/log(5/4)=3.10628...`; quotienting sublinear solution balls gives only `exp(o(n))` savings; quotienting whole connected components leaves an uncontrolled cross-component overlap moment; whitening/core counting lacks a uniform exponential cluster-multiplicity theorem; the q-binomial radius-two route reached only about `4.5923`; and the equal-weight two-support hard-field family stalls near `4.4178`.

Companion NM13-06 is on a distinct constructive/lower-bound route. Its newest report derives a hidden 2/3-degree split compiler and terminal-adjoint transfer for the Hajiaghayi--Sorkin process; it does not duplicate the present interpolation upper-bound argument.

## 2. New theorem: three-node Gaussian lower envelope for the tilted Hausdorff tail

Fix `K>=1` with `mu_K>0` and tilt the law `rho` of `Q` by `Q^K`:

\[
d\rho_K(q)=\frac{q^K}{\mu_K}\,d\rho(q),
\qquad
m_j=\mathbb E_{\rho_K}Q^j=\frac{\mu_{K+j}}{\mu_K}.
\tag{2.1}
\]

Let `pi_3` be the monic cubic orthogonal to `1,q,q^2` under `rho_K`:

\[
\pi_3(q)=q^3+a q^2+b q+c.
\tag{2.2}
\]

Its coefficients are the unique solution of

\[
\begin{pmatrix}
1&m_1&m_2\\
m_1&m_2&m_3\\
m_2&m_3&m_4
\end{pmatrix}
\begin{pmatrix}c\\b\\a\end{pmatrix}
=-
\begin{pmatrix}m_3\\m_4\\m_5\end{pmatrix}.
\tag{2.3}
\]

For a non-degenerate positive measure on `[0,1]`, the orthogonal cubic has three simple roots

\[
0<x_1<x_2<x_3<1.
\]

Let `w_1,w_2,w_3>0` be the corresponding Gaussian quadrature weights. Then the three-node Gaussian rule is exact on every polynomial of degree at most five:

\[
\mathbb E_{\rho_K}p(Q)=\sum_{i=1}^3w_i p(x_i),
\qquad \deg p\le5.
\tag{2.4}
\]

### Lemma 2.1 — sixth-derivative Gaussian tail lower bound

Define

\[
g_t=\sum_{i=1}^3w_i x_i^t.
\tag{2.5}
\]

Then

\[
g_t=m_t\quad(0\le t\le5),
\tag{2.6}
\]

and

\[
\boxed{g_t\le m_t\quad\text{for every integer }t\ge6.}
\tag{2.7}
\]

#### Proof

For `t<=5`, (2.6) is Gaussian exactness. For `t>=6`, put `f(q)=q^t` and let `H` be the degree-at-most-five Hermite interpolant matching both `f` and `f'` at all three Gaussian nodes. For each `q in [0,1]`, the Hermite remainder is

\[
f(q)-H(q)
=\frac{f^{(6)}(\xi_q)}{6!}
\prod_{i=1}^3(q-x_i)^2
\tag{2.8}
\]

for some `xi_q in [0,1]`. Since

\[
f^{(6)}(x)
=t(t-1)(t-2)(t-3)(t-4)(t-5)x^{t-6}\ge0,
\]

we have `H(q)<=f(q)` pointwise. Integrating against `rho_K` and using degree-five Gaussian exactness for `H`,

\[
m_t=\mathbb E f(Q)
\ge \mathbb E H(Q)
=\sum_iw_iH(x_i)
=\sum_iw_if(x_i)=g_t.
\]

This proves (2.7). QED.

Consequently, for every finite `T`,

\[
\mu_{K+t}=\mu_Km_t\ge\mu_Kg_t
\]

and hence

\[
\boxed{
A(\alpha,\nu)
\le
A_K-\mu_K^2\sum_{t=1}^T\frac{g_t^2}{K+t},
}
\tag{2.9}
\]

where

\[
A_K=-\sum_{k=1}^K\frac{\mu_k^2}{k}-2\alpha L.
\]

This is strictly stronger information than the predecessor's two-node rule whenever the third quadrature node carries nonzero mass and the omitted tail is not already exactly represented by the two-node measure.

## 3. Exact compound-Poisson moments

The interpolation-side compound-Poisson formulas are unchanged. For one literal orientation, the warning count is Poisson with mean

\[
\lambda=\frac{3\alpha}{2}.
\]

For independent survey variables `R_1,R_2`, let `P=R_1R_2`,

\[
Z=\prod_j(1-P_j),\qquad Q=1-Z.
\]

Then

\[
\mathbb EZ^j
=\exp\left\{\lambda\left(\mathbb E(1-R_1R_2)^j-1\right)\right\},
\tag{3.1}
\]

and binomial inversion gives

\[
\mu_k=\mathbb E(1-Z)^k
=\sum_{j=0}^k(-1)^j\binom{k}{j}\mathbb EZ^j.
\tag{3.2}
\]

The clause term remains

\[
L=\mathbb E\log(1-R_1R_2R_3).
\tag{3.3}
\]

Thus (2.9) is completely explicit for a finite-support rational survey law.

## 4. Rational five-support survey at alpha = 4.38890

A bounded exploratory search around the predecessor's five-support law was used only to locate a better rational point; it is not part of the proof. The retained law is exactly symmetric under `R -> 1-R`:

\[
R\in
\left\{
\frac{33}{5000},
\frac{49}{625},
\frac12,
\frac{576}{625},
\frac{4967}{5000}
\right\}
=
\{0.0066,0.0784,0.5,0.9216,0.9934\},
\tag{4.1}
\]

with weights

\[
\left\{
\frac{139}{2500},
\frac{1831}{10000},
\frac{2613}{5000},
\frac{1831}{10000},
\frac{139}{2500}
\right\}
=
\{0.0556,0.1831,0.5226,0.1831,0.0556\}.
\tag{4.2}
\]

Take

\[
\alpha_0=\frac{43889}{10000}=4.3889,
\qquad K=2300,
\qquad T=60000.
\tag{4.3}
\]

The outward-interval certificate is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T09-07-39Z__gauss3_tail_438890_interval.py`

created at commit `0fb34c1633e784d7055fed2b3b1dcbd231702be1`; its archived executed output is

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T09-07-39Z__gauss3_tail_438890_interval.out`

created at commit `79bbd8e7b3f552d66651b6217fffcba9c0ee0165`.

The checker uses exact rational inputs and outward `mpmath.iv` arithmetic at 1450 decimal digits. It computes `mu_1,...,mu_2305`, verifies all required moments positive, solves the cubic orthogonality system by interval Cramer's rule, certifies one root in each of three pairwise disjoint intervals by opposite polynomial signs at the bracket endpoints, obtains positive Lagrange/Gaussian weights, checks degree-0-through-5 moment matching by interval containment, and sums 60,000 rigorously forced tail terms.

The decisive values are

\[
A_{2300}
=4.605730243921202871820357890991\times10^{-5}>0,
\tag{4.4}
\]

so the exact finite truncation alone does **not** prove negativity. The certified root brackets are centered at

\[
x_1\approx0.99743724084625049463,
\quad
x_2\approx0.99909696793420480410,
\quad
x_3\approx0.99985091160335669062,
\tag{4.5}
\]

with positive weights approximately

\[
w_1\approx0.00867335983133,
\quad
w_2\approx0.249485017588,
\quad
w_3\approx0.741841622581.
\tag{4.6}
\]

The finite three-node Gaussian tail is rigorously bounded below by

\[
\boxed{
\mu_K^2\sum_{t=1}^{60000}\frac{g_t^2}{K+t}
\ge
4.791743437617725359463296078959\times10^{-5}.
}
\tag{4.7}
\]

Therefore

\[
\boxed{
A(4.3889,\nu)
\le
-1.860131936965224876429381879685\times10^{-6}<0.
}
\tag{4.8}
\]

The archived output ends

`CERTIFIED_STRUCTURAL_CHECKS = True`,

`CERTIFIED_A_UPPER_NEGATIVE = True`, and

`CERTIFIED_A_NEGATIVE = True because A <= A_K - finite_Gauss3_tail_LB`.

### Mechanism gain, stated separately from threshold movement

The auxiliary finite truncation is positive by about `4.606e-5`; the new three-node Hausdorff envelope forces at least `4.792e-5` of omitted positive moment mass, crossing zero by a certified margin of about `1.860e-6`. This is the demonstrated mechanism gain. It should not be confused with the source-connected endpoint movement, which is only `4.38900 -> 4.38890`.

A non-rigorous high-precision diagnostic at the **same new survey law and same K,T** gives the predecessor two-node Gaussian tail upper estimate `A <= +1.024e-6`, still positive. Thus the third node is not cosmetic at this point: the new sixth-derivative envelope is what changes the sign. This comparison is diagnostic only; the theorem claim rests on the outward-interval three-node certificate above.

## 5. Transfer to the exact proper iid source model

The source transfer is inherited unchanged from the earlier interpolation reports; this run changes only the admissible finite-support trial and the rigorous evaluation of its hard-field coefficient.

The Franz--Leone / Panchenko--Talagrand K-SAT interpolation bound applies to `p=3`; in the K-SAT specialization the interpolation remainder is controlled by convexity on nonnegative replica quantities, so the broader even-`p` restriction appearing in diluted-spin-glass formulations is not an odd-3-SAT obstruction. The survey support (4.1) is finite and lies strictly inside `(0,1)`, the Poisson warning count has exponential moments, and the clause factor is uniformly separated from zero on this finite support. Therefore the dominated-convergence argument from the predecessor applies: strict negativity of the hard-field `m downarrow 0` coefficient (4.8) implies that finite hard-field magnitude, finite inverse temperature and finite positive Parisi parameter already give a strict negative interpolation margin.

The inherited free-energy-to-energy argument then yields a linear lower bound on the minimum number of violated clauses with high probability in the Poissonized with-replacement model. Repeated-variable clauses occur only `O_p(1)` times and deleting them changes minimum energy by at most that count. Passing from the resulting proper Poisson clause count to exactly `floor(alpha_0 n)` proper iid clauses requires adding or deleting only `O_p(sqrt(n))` clauses; each edit changes minimum energy by at most one, so the linear energy gap survives at the same density. Thus the candidate theorem is

\[
\boxed{
\Pr\!\left[\Phi_{n,\lfloor4.3889n\rfloor}\text{ is satisfiable}\right]\to0
}
\tag{5.1}
\]

for the exact classical iid random 3-SAT model with independent fair signs and three distinct variables per clause.

This is labeled **CANDIDATE_FULL pending later independent review**. The new finite core is exact/interval-certified here; the inherited interpolation-to-source transfer is not re-audited in this run because the current owner directive prioritizes new mathematics and defers independent review.

## 6. Bounded literature check, 2026-09-20

Queries were limited to the exact classical iid random 3-SAT threshold and recent 2026 threshold/window papers. The search recovered:

- Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52*, arXiv `math/0310193` / 2003: lower endpoint `3.52` for the classical model.
- Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT*, arXiv `0807.3600` / FSTTCS 2008: upper endpoint `4.4898` for the classical model.
- Gaia Carenini, ECCC TR26-145, *The Scaling Window of Random k-SAT*, August 2026: `O(n/log n)` scaling-window upper bound for every fixed `k>=3`, not a location of the `k=3` center.
- Chatterjee--Coja-Oghlan--Greenhill--Pfenninger--Rolvien--Zakharov--Zampetakis, *The random k-SAT Gibbs uniqueness threshold revisited*, published March 2026: Gibbs-uniqueness threshold and solution-counting regime, not the satisfiability threshold itself.

No later public source was found in this bounded search that directly replaces the `3.52` or `4.4898` explicit decimals for the exact classical `k=3` model. This is a bounded search statement, not proof of worldwide novelty or priority.

## 7. Residual obstruction and next attack

The project candidate endpoint is now limited less by finite-tail truncation than by the expressiveness of the five-support survey. The natural next route is one of two genuinely new extensions:

1. a four-node Gaussian / degree-seven Hermite envelope using tilted moments through degree seven, only if the resulting gain is large enough to move the endpoint rather than merely polish the same law; or
2. a seven-support symmetric survey optimized jointly against the present three-node bound, which is more likely to alter the actual order parameter rather than just its numerical evaluation.

If the next substantive run cannot move the endpoint with either extension, the route should switch rather than accumulate deeper truncations.

## 8. ledger_delta

```yaml
ledger_delta:
  worker: NM13-13
  parent: T04
  source: classical iid random 3-SAT, uniform fair signs, three distinct variables per clause
  status: OPEN / PARTIAL
  external_explicit_bracket_before: "[3.52,4.4898]"
  external_explicit_bracket_after: "[3.52,4.4898]"
  project_candidate_upper_before: "4.38900"
  project_candidate_upper_after: "4.38890"
  project_candidate_width_before: "0.86900"
  project_candidate_width_after: "0.86890"
  source_connected_gain: "0.00010 on project CANDIDATE_FULL upper endpoint; external published decimal unchanged"
  mechanism: "three-node Gaussian quadrature for Q^K-tilted Hausdorff measure; sixth-derivative Hermite remainder forces omitted moment tail"
  exact_trial:
    alpha: "43889/10000"
    support: ["33/5000","49/625","1/2","576/625","4967/5000"]
    weights: ["139/2500","1831/10000","2613/5000","1831/10000","139/2500"]
    K: 2300
    T: 60000
    A_K: "+4.6057302439212028718e-5"
    tail_lower_bound: ">=4.7917434376177253594e-5"
    A_upper: "<=-1.8601319369652248764e-6"
  theorem_label: "CANDIDATE_FULL pending later independent review"
  code: "proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T09-07-39Z__gauss3_tail_438890_interval.py"
  output: "proofnet24/NM13-13/progress-3sat/runs/2026-09-20/artifacts/2026-09-20T09-07-39Z__gauss3_tail_438890_interval.out"
  prior_failures_preserved:
    - "arbitrary rescue stars fail composition"
    - "anchored degree-one matching lacks global Diaz-polytope reoptimization"
    - "positive local second moments hit the 3.10628... identical-pair barrier"
    - "sublinear solution-ball quotienting gives only exp(o(n)) savings"
    - "whole-component quotienting leaves cross-component overlap uncontrolled"
    - "whitening lacks uniform exponential cluster-multiplicity control"
    - "q-binomial radius-two route reached only about 4.5923"
    - "equal-weight two-support hard-field family stalls near 4.4178"
  companion: "NM13-06 remains on constructive hidden-split/adjoint lower-bound route"
  residual_obstruction: "finite-support survey not globally optimized; inherited interpolation-to-source transfer awaits independent review"
  next_attack: "seven-support survey jointly optimized against three-node tail, or four-node Gaussian envelope only if it moves the endpoint"
  unchanged_substantive_runs: 0
  recovery_failures: 0
```
