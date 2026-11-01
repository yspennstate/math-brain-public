# fleet04/B12 — all-block terminality turns robust derivative rows into influence-relative trigger surplus

**Run:** `B12-20260922T081051Z-r45`  
**Classification:** `ESSENTIAL_STEP_APPLIED / ROBUST_ROW_TERMINAL_OBSTRUCTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Current source state and mechanism change

The latest completed fleet02/B13 report is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`,
blob `68e838a493671ed5c27a29468dfcce7bb621d860`.

It records an important correction: the fixed potential `Gamma^dagger` used by several preceding local-gluing/MUX runs has been source-validly refuted as a universal candidate by an 18-input composition-prime witness. Accordingly, the older fixed-`Gamma^dagger` collars remain valid local theorems but are no longer counted as target-level progress here.

The exact implication from the new fleet02/B13 result used in this report is candidate-independent. If the terminal-class FEI inequality fails, one may choose a centered, essential, tensor-primitive minimum-dimensional ratio core `g` that is terminal for **every nonempty physical block**. In the notation of that report, with

\[
q_i=\operatorname{Inf}_i(g)\le \tfrac12,\qquad
\mathcal J=\sum_i q_i,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\tfrac12+\sqrt{q(1-q)}\right),
\]
for each physical block `A`,

\[
D_A=\sum_{i\in A}q_i+C_A,\qquad
C_A=\sum_{j\notin A}c_j(A),
\]
\[
W_A=\sum_{j\notin A}\mathfrak j'(q_j)c_j(A),\qquad
U_A=\sum_{i\in A}h_2(q_i)-W_A,
\]
and an all-block terminal core at level `K>2` satisfies

\[
\boxed{U_A\ge K D_A\quad\hbox{for every nonempty physical block }A.}
\tag{0.1}
\]

This run changes mechanism from the preceding fixed-potential bias collars to a direct use of (0.1) on the **actual trigger set of one robust derivative row**.

The second source theorem retained exactly is fleet04/B18

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`,
blob `0e8c2cc28da81af8843b565cb47285684b164480`.

For derivative-row support disagreement `p_{ik}` and row depth `d_k`, it proves

\[
\boxed{\sum_{i\ne k}p_{ik}\le4d_k.}
\tag{0.2}
\]

I preserve its central warning: `sum_k d_k` is a second factorial spectral moment and is **not** automatically `O(J)`. No such assumption is made below.

## 1. Robust row notation

Fix a derivative row `i`. On the quotient cube, let

\[
E_i=\{y:D_i g(y)\ne0\},\qquad \mu(E_i)=q_i.
\]

Assume this row is relative-`eta` near a coordinate subcube

\[
Q_i=\{y_{F_i}=a_i\},\qquad s_i=\mu(Q_i)=2^{-|F_i|},
\]
with

\[
\varepsilon_i:=\mu(E_i\triangle Q_i)\le\eta q_i,
\qquad 0\le\eta<\tfrac12.
\tag{1.1}
\]

For `k in F_i`, let

\[
p_{ik}=\Pr[1_{E_i}(Y)\ne1_{E_i}(Y+e_k)].
\]

For a physical block `A`, the fleet02/B13 crossing term is

\[
c_i(A)=\mathbb E_z\left|p_i(z)-\tfrac12\right|-\left|q_i-\tfrac12\right|,
\tag{1.2}
\]
where `p_i(z)=Pr(E_i | Y_A=z)` before child recentering.

Because `q_i<=1/2`, a row satisfying (1.1) with `eta<=1/16` cannot have `F_i` empty. If `F_i` were empty, `s_i=1` and `1-q_i<=eta q_i`, forcing `q_i>1/2`.

## 2. New posterior-polarization lemma on the actual trigger block

### Lemma 2.1

For `A=F_i`,

\[
\boxed{c_i(F_i)\ge q_i-\varepsilon_i\ge(1-\eta)q_i.}
\tag{2.1}
\]

Moreover, every trigger coordinate satisfies

\[
\boxed{p_{ik}\ge2(q_i-2\varepsilon_i)\ge2(1-2\eta)q_i,
\qquad k\in F_i.}
\tag{2.2}
\]

### Proof

Let `b(z)=1_{z=a_i}` be the posterior of the exact subcube `Q_i` after revealing `F_i`, and let `p(z)=Pr(E_i | Y_{F_i}=z)`. Equal fibre sizes give the exact identity

\[
\mathbb E_z|p(z)-b(z)|=\mu(E_i\triangle Q_i)=\varepsilon_i.
\tag{2.3}
\]

Since `|b(z)-1/2|=1/2` for every `z`, the one-Lipschitz property of absolute value gives

\[
\mathbb E_z|p(z)-1/2|\ge1/2-\varepsilon_i.
\]

Subtracting `|q_i-1/2|=1/2-q_i` proves (2.1).

For `k in F_i`, the exact subcube has `k`-boundary `2s_i`. Replacing `Q_i` by `E_i` can change the boundary indicator only when one endpoint lies in `E_i triangle Q_i`, hence by at most `2 epsilon_i`. Thus

\[
p_{ik}\ge2(s_i-\varepsilon_i).
\]

Since `|s_i-q_i|<=epsilon_i`, one has `s_i>=q_i-epsilon_i`, giving (2.2). QED.

The key point is that the trigger block reveals almost the entire derivative indicator: the crossing refund is proportional to `q_i` itself, not to `|F_i|q_i` and not to ambient dimension.

## 3. New theorem: terminal trigger-surplus payment

Define the per-coordinate terminal surplus

\[
\sigma_k(K):=h_2(q_k)-Kq_k.
\tag{3.1}
\]

First note that all-block terminality makes each surplus nonnegative. Apply (0.1) to the singleton block `{k}`:

\[
h_2(q_k)-W_{\{k\}}\ge K(q_k+C_{\{k\}}),
\]
so, because `W_A,C_A>=0`,

\[
\boxed{\sigma_k(K)\ge0.}
\tag{3.2}
\]

### Theorem 3.1 — influence-relative robust-row trigger tax

If row `i` satisfies (1.1), then every all-block terminal core obeys

\[
\boxed{
\sum_{k\in F_i}\sigma_k(K)
\ge
(1-\eta)\,[K+\mathfrak j'(q_i)]q_i.
}
\tag{3.3}
\]

At the live robust threshold `eta=1/16`,

\[
\boxed{
\sum_{k\in F_i}\bigl(h_2(q_k)-Kq_k\bigr)
\ge
\frac{15}{16}[K+\mathfrak j'(q_i)]q_i.
}
\tag{3.4}
\]

For an exact subcube row (`eta=0`), the factor `15/16` becomes `1`.

### Proof

Use the actual trigger block `A=F_i` in (0.1):

\[
\sum_{k\in F_i}h_2(q_k)-W_{F_i}
\ge
K\left(\sum_{k\in F_i}q_k+C_{F_i}\right).
\]

Rearranging gives the exact nonnegative crossing bank

\[
\sum_{k\in F_i}\sigma_k(K)
\ge
\sum_{j\notin F_i}[K+\mathfrak j'(q_j)]c_j(F_i).
\tag{3.5}
\]

Keep only the `j=i` summand and apply (2.1). This yields (3.3). QED.

### Interpretation

Equation (3.3) is the requested influence-relative conversion for the robust row **inside the actual surviving terminal class**. The raw trigger label count `|F_i|`, the ambient dimension and a Fannes alphabet penalty disappear. A row of influence `q_i` can survive all-block terminality only if its trigger coordinates contain terminal entropy surplus of order `q_i`.

This is not yet a decodable full spectral code: the same trigger-coordinate surplus may be requested by several rows. The next theorem uses genuine Boolean mixed-derivative integrability to quantify that reuse without pretending the raw depth bank is `O(J)`.

## 4. New aggregate theorem using fleet04/B18 mixed curvature

Let `R_eta` be any collection of relative-`eta` robust derivative rows at the same Boolean state. Multiply (3.3) by `q_i` and sum over `i in R_eta`. By (3.2) and (2.2), for every `k in F_i`,

\[
q_i\sigma_k(K)
\le
\frac{p_{ik}}{2(1-2\eta)}\sigma_k(K).
\]

Therefore, using the column conservation (0.2),

\[
\begin{aligned}
(1-\eta)
\sum_{i\in R_\eta}q_i^2[K+\mathfrak j'(q_i)]
&\le
\sum_k\sigma_k(K)
\sum_{\substack{i\in R_\eta\\k\in F_i}}q_i\\
&\le
\frac1{2(1-2\eta)}
\sum_k\sigma_k(K)\sum_{i\ne k}p_{ik}\\
&\le
\frac2{1-2\eta}
\sum_k\sigma_k(K)d_k.
\end{aligned}
\]

Hence:

### Theorem 4.1 — weighted-depth obstruction

\[
\boxed{
\sum_{i\in R_\eta}q_i^2[K+\mathfrak j'(q_i)]
\le
\frac{2}{(1-\eta)(1-2\eta)}
\sum_k\sigma_k(K)d_k.
}
\tag{4.1}
\]

At `eta=1/16`,

\[
\boxed{
\sum_{i\in R_{1/16}}q_i^2[K+\mathfrak j'(q_i)]
\le
\frac{256}{105}
\sum_k\bigl(h_2(q_k)-Kq_k\bigr)d_k.
}
\tag{4.2}
\]

For exact-subcube rows, the coefficient improves to `2`.

A useful scale form follows immediately. For any `tau>0`, let

\[
R_{\eta,\tau}=\{i\in R_\eta:q_i\ge\tau\}.
\]

Since `mathfrak j'(q_i)>=0`, (4.2) gives at `eta=1/16`

\[
\boxed{
\sum_k\bigl(h_2(q_k)-Kq_k\bigr)d_k
\ge
\frac{105}{256}K\tau
\sum_{i\in R_{1/16,\tau}}q_i.
}
\tag{4.3}
\]

Thus a hypothetical all-block-terminal obstruction with a positive fraction of its influence in robust rows above scale `tau` is forced to carry a quantitatively large **surplus-weighted depth bank**.

## 5. What this does and does not close

This result improves the old interface-B endpoint in a specific way.

* The local row payment (3.3) is directly influence-relative and does not pay `|F_i|`, `n`, or `log n`.
* Mixed-derivative compatibility aggregates the shared trigger coordinates without an assumed bounded-incidence selector.
* The receiving bank is **not** raw `sum_k d_k`. It is the more selective quantity
  `sum_k (h_2(q_k)-K q_k)d_k` forced by all-block terminality.
* I make **no** claim that this weighted bank, or raw `sum_k d_k`, is universally `O(J)`. The fleet04/B18 warning remains in force.

The surviving missing implication is now sharper on the robust-row branch:

> either show that the surplus-weighted depth bank in (4.2) is influence-relative on an all-block critical core, or use (4.3) to eliminate the medium/heavy robust rows and handle only the remaining small-influence/nonrobust rows by a different nonreusing mechanism.

This is not full FEI. It is a source-valid obstruction on the current candidate-independent terminal class.

## 6. Exact regression checker

`CHECKER.py` exhausts every centered support set in quotient dimensions `1` through `4` and every coordinate subcube satisfying the relative-`1/16` hypothesis. It verifies exactly, with `Fraction` arithmetic,

* a robust centered row cannot have an empty trigger set;
* `c_i(F_i)>=15 q_i/16`;
* `p_{ik}>=7 q_i/4` for every trigger coordinate;
* the aggregate constant is exactly `256/105`.

Executed stdout:

```
robust_support_pairs 116
trigger_boundary_checks 284
min_crossing_over_q 1
min_boundary_over_q 2
eta_1_16_aggregation_constant 256/105
RESULT PASS
```

`py_compile` also passed. Checker blob: `166886104992ef4570277e137d5f02e053f72d5c`. Checker SHA-256: `36cee49a1955e93c509761a6eaf4ca590c730edef9f6dc3ff6d059c0d000ca09`.

The finite checker is a regression test only. Lemma 2.1 and Theorems 3.1/4.1 are analytic for arbitrary dimension.

## 7. Outcome

**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.

The newest fleet02/B13 all-block terminal theorem supplies the exact physical-block inequality used here. The new step converts every robust near-subcube derivative row in that terminal class into an influence-relative trigger-surplus demand and then combines it with fleet04/B18 mixed-curvature conservation to obtain the dimension-free weighted-depth obstruction (4.2). Full FEI remains open; the remaining universal payment of the surplus-weighted depth bank is not assumed.
