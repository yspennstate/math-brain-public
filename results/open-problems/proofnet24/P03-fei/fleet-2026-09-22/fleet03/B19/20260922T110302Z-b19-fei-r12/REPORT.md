# fleet03/B19 — robust trigger forest forces occurrence KL after exact tensor-baseline subtraction

**Run:** `20260922T110302Z-b19-fei-r12`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, owner-control revision `2026-09-22.3`  
**Assignment:** Terminal-to-KL conversion  
**Classification:** `ESSENTIAL_STEP_APPLIED / TERMINAL_TO_KL_FOREST_BRIDGE / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Novelty/publication:** not assessed; private source-bound research artifact.

## 0. Exact target and change from the preceding B19 run

The current B19 target is to turn full terminal/critical-core information into a measurable nonlocal occurrence-dependence credit, preserving the exact tensor/conditioning baseline and proving that the same information credit is not silently reused.

The immediately preceding B19 run proved a **one-randomized-pair** data-processing inequality

\[
vK_{\rm occ}\ge \mathbb E_{(I,J)\sim\alpha}
 d_2(s_{IJ}\Vert b_{IJ}),
\qquad b_{ij}=\frac c v q_iq_j,
\]

and the corresponding one-sided hidden-curvature payment. That was a correct nonreuse statement, but the missing implication was how a terminal branch produces a selector carrying target-scale mass.

This run changes mechanism. It uses the actual trigger graph supplied by robust derivative rows, extracts an **acyclic forest** from that graph, and spends pair information only on the forest. The entropy chain rule then proves nonreuse globally. The resulting total-correlation credit is finally decomposed, by an exact balanced-suspension/I-projection identity, into (i) the canonical nonempty occurrence KL and (ii) two explicit tensor/conditioning baseline terms. No raw-`U_4` estimate and no all-pairs KL sum is used.

The designated partner is `fleet04/B19`. It had no completed artifact in either the current `fleet-2026-09-22/fleet04/B19` scientific root or its current shared FEI handoff root at the two checks made before publication. I therefore do not claim partner uptake. The newest compatible completed fleet04 theorem actually inserted below is `fleet04/B17`, together with the assignment-prescribed `fleet04/B12` and `fleet04/B18` results.

## 1. Source-pinned premises actually used

### 1.1 All-block ratio-critical core

Source: `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T075416Z-all-block-terminal-core/REPORT.md`.

In the median-character gauge write

\[
q_i=\operatorname{Inf}_i(g)\le\frac12,
\qquad J=\sum_iq_i,
\qquad \mathcal P=\sum_i\mathfrak j(q_i),
\qquad \mathcal F=H-\mathcal P.
\]

If `F<=4J` fails on the terminal class, one may take a minimum-essential-dimension ratio core with

\[
\rho=\frac{\mathcal F}{J}>4
\]

which is essential, tensor-primitive, character-centered and satisfies the all-block criticality inequalities. We use only consequences already proved in the cited source chain.

### 1.2 Exact two-coordinate support/spectral identity

Source: `yspennstate/math-open-problems@85ffa60db26997421d980b1f86c03d82259504ca`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T093723Z-copair-terminal-tax/REPORT.md`.

For distinct physical coordinates `i,k`, let

\[
s_{ik}:=\Pr(i,k\in X),
\]

where `X` is the full squared-Fourier random set, let `p_{ik}` be derivative-support disagreement, and let `o_{ik}` be opposite-sign overlap. The exact identity is

\[
\boxed{s_{ik}=\frac{p_{ik}}4+o_{ik}\ge\frac{p_{ik}}4.}
\tag{1.1}
\]

The same source proves

\[
\omega_{i\leftarrow k}=4s_{ik}-2c_{i\leftarrow k}\ge0,
\]

but this run does **not** attempt to sum the raw hidden-curvature bank.

### 1.3 Robust-row trigger edge

Source: `yspennstate/math-open-problems@fdbfbcc1beed0db4cb6d13c8d61fd92db53a8113`,
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T081051Z-terminal-trigger-surplus/REPORT.md`.

If derivative row `i` is relative-`eta` close to a coordinate subcube with trigger set `F_i`, then for every `k in F_i`,

\[
\boxed{p_{ik}\ge2(1-2\eta)q_i.}
\tag{1.2}
\]

The live robust threshold is `eta=1/16`, where `p_{ik}>=(7/4)q_i`.

### 1.4 Critical-core small-influence consequence

Source: `yspennstate/math-open-problems@200e3fd37fe201f78d882ba8809414d201efb829`,
`proofnet24/P03-fei/fleet-2026-09-22/fleet04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`.

On a genuine ratio-`rho>4` core, singleton terminality implies

\[
\boxed{0<q_k<\frac16}
\tag{1.3}
\]

for every essential coordinate. The same report reduces the robust weighted-depth obstruction to already-paid phase plus raw hidden curvature, but explicitly leaves raw `U_4` unpaid. We preserve that boundary.

### 1.5 Exact balanced-suspension information split

Newest compatible completed fleet04 result applied in this run:

`yspennstate/math-open-problems@4724c29ba5e11543763408355504049e05e4e6e3`,
`proofnet24/P03-fei/fleet-2026-09-22/fleet04/B17/20260922T102740Z-b17-fei-r17/REPORT.md`.

For the genuine balanced Boolean suspension `F(y,x)=y g(x)`, if the full spectral law of `g` has empty mass `a`, `v=1-a`, and coordinate occurrence marginals `q_i`, define

\[
c_0:=1-\prod_i(1-q_i).
\]

Let `P^+` be the full spectral law conditioned on nonemptiness, `Q^+` its canonical nonempty maximum-entropy I-projection with the same conditional occurrence marginals, and let

\[
K_{\rm occ}:=D_{\rm KL,2}(P^+\Vert Q^+).
\]

Let `R_q` be the unconditioned independent Bernoulli product with marginals `q_i`, and `R_q^+=R_q(.\mid X\ne\varnothing)`. The source proves the exact identity

\[
\boxed{
K_{\rm susp}
=
 d_2(v\Vert c_0)
+vK_{\rm occ}
+vD_{\rm KL,2}(Q^+\Vert R_q^+),
}
\tag{1.4}
\]

where

\[
\boxed{K_{\rm susp}=\sum_i h_2(q_i)-H(X)}
\tag{1.5}
\]

is the total correlation of the full spectral indicator vector. This exact decomposition keeps the empty-mass mismatch and product-reference mismatch; neither is silently assigned to `K_occ`.

## 2. Robust triggers force a fixed pair-information density

Let `R_eta` be any set of derivative rows satisfying the B12 relative-`eta` robust condition at the same ratio-critical core, with `0<=eta<=1/16`. For each `i in R_eta`, choose one actual trigger coordinate

\[
k(i)\in F_i.
\]

Set

\[
\alpha_\eta:=\frac{1-2\eta}{2}.
\tag{2.1}
\]

Combining (1.1) and (1.2) gives

\[
s_{i,k(i)}\ge\frac{p_{i,k(i)}}4
\ge\alpha_\eta q_i,
\]

and hence

\[
\boxed{
\Pr(X_{k(i)}=1\mid X_i=1)
=\frac{s_{i,k(i)}}{q_i}
\ge\alpha_\eta.
}
\tag{2.2}
\]

At `eta=1/16`, `alpha_eta=7/16`. By (1.3), the target marginal satisfies `q_{k(i)}<1/6<alpha_eta`.

### Lemma 2.1 — each robust trigger edge carries influence-relative mutual information

Define

\[
\kappa_\eta:=d_2\!\left(\alpha_\eta\middle\Vert\frac16\right)>0.
\tag{2.3}
\]

Then every selected robust trigger edge obeys

\[
\boxed{
I(X_i;X_{k(i)})\ge q_i\kappa_\eta.
}
\tag{2.4}
\]

**Proof.** For Bernoulli variables, conditioning on `X_i` gives the exact representation

\[
I(X_i;X_k)
=q_i d_2\!\left(\frac{s_{ik}}{q_i}\middle\Vert q_k\right)
+(1-q_i)d_2\!\left(\frac{q_k-s_{ik}}{1-q_i}\middle\Vert q_k\right).
\]

Drop the second nonnegative term. On the first term, (2.2) puts the first argument at least `alpha_eta`, while (1.3) puts `q_k<1/6<alpha_eta`. For fixed `b`, `a -> d_2(a||b)` is increasing on `[b,1]`; for fixed `a`, `b -> d_2(a||b)` is decreasing on `(0,a)`. Therefore

\[
d_2\!\left(\frac{s_{ik}}{q_i}\middle\Vert q_k\right)
\ge d_2\!\left(\alpha_\eta\middle\Vert\frac16\right),
\]

which proves (2.4). QED.

At the live threshold,

\[
\boxed{
\kappa_{1/16}
=d_2\!\left(\frac7{16}\middle\Vert\frac16\right)
=0.2901785390585173\ldots\ {m bits}.
}
\tag{2.5}
\]

Positivity alone is not the point: the lower bound is proportional to the actual row influence `q_i` and has a fixed quantitative constant on the source-valid critical domain.

## 3. Nonreuse theorem: extract a forest and spend pair information once

The selected trigger edges define a directed graph

\[
i\longrightarrow k(i),\qquad i\in R_\eta,
\tag{3.1}
\]

in which every robust-row tail has one outgoing edge. Targets need not lie in `R_eta`.

For every directed cycle, delete the edge whose tail has minimum `q_i`. A directed cycle has length at least two, so its deleted tail weight is at most half the total tail weight on that cycle. The remaining underlying undirected graph is a forest: in a functional graph, any undirected cycle would force a directed cycle, and one edge has been removed from every such component.

Let `T` denote the surviving forest and

\[
J_R:=\sum_{i\in R_\eta}q_i.
\tag{3.2}
\]

Then

\[
\boxed{
\sum_{i\to k(i)\in T}q_i\ge\frac12J_R.
}
\tag{3.3}
\]

### Lemma 3.1 — forest mutual information is bounded by total correlation

For any forest `T` on the spectral indicator variables,

\[
\boxed{
\sum_{\{i,k\}\in E(T)}I(X_i;X_k)
\le \sum_i h_2(q_i)-H(X)=K_{\rm susp}.
}
\tag{3.4}
\]

**Proof.** Root each component and order each parent before its children. Entropy chain rule and conditioning-reduces-entropy give

\[
H(X)
\le \sum_{r\ {m root}}H(X_r)
  +\sum_{u\to w\in T}H(X_w\mid X_u)
  +\sum_{z\ {m isolated}}H(X_z).
\]

Subtract from `sum_i H(X_i)`. Each forest edge contributes exactly
`H(X_w)-H(X_w|X_u)=I(X_u;X_w)`. QED.

This is the nonreuse step. It does not claim `K_susp >= sum_{i!=k} I(X_i;X_k)`, which is false in general. It spends only an acyclic subset selected from the actual terminal trigger graph.

### Theorem 3.2 — robust-row total-correlation payment

Combining (2.4), (3.3), and (3.4),

\[
\boxed{
K_{\rm susp}\ge\frac{\kappa_\eta}{2}J_R.
}
\tag{3.5}
\]

At `eta=1/16`,

\[
\boxed{
K_{\rm susp}
\ge
0.14508926952925866\ldots\,J_R.
}
\tag{3.6}
\]

Thus a terminal ratio-critical core carrying robust derivative-row influence mass cannot have arbitrarily small nonlocal spectral dependence after the tensor baseline is handled correctly below.

## 4. Main terminal-to-occurrence-KL inequality with exact baseline removal

Define the explicit tensor/conditioning baseline

\[
\boxed{
B_{\rm tens}
:=d_2(v\Vert c_0)
 +vD_{\rm KL,2}(Q^+\Vert R_q^+)\ge0.
}
\tag{4.1}
\]

Equation (1.4) is exactly

\[
K_{\rm susp}=B_{\rm tens}+vK_{\rm occ}.
\tag{4.2}
\]

Insert Theorem 3.2.

### Theorem 4.1 — robust trigger forest -> irreducible occurrence dependence

On every genuine median-gauged ratio-`rho>4` all-block critical core, for every collection `R_eta` of relative-`eta` robust derivative rows with `0<=eta<=1/16`,

\[
\boxed{
 vK_{\rm occ}
\ge
\left[
\frac{\kappa_\eta}{2}J_R
-B_{\rm tens}
\right]_+,
\qquad
\kappa_\eta=d_2\!\left(\frac{1-2\eta}{2}\middle\Vert\frac16\right).
}
\tag{4.3}
\]

In particular at the live threshold,

\[
\boxed{
 vK_{\rm occ}
\ge
\left[
0.14508926952925866\ldots\,J_R
-d_2(v\Vert c_0)
-vD_{\rm KL,2}(Q^+\Vert R_q^+)
\right]_+.
}
\tag{4.4}
\]

**Sign/source domain.** Every term on the right is defined for the actual squared-Fourier law of the genuine Boolean critical core. `K_occ` is the canonical nonempty occurrence I-projection KL in bits. `B_tens` is nonnegative and is subtracted rather than silently treated as dependence. The positive part is justified because `K_occ>=0` independently.

**Why this meets the information-path requirement.** The theorem is stronger than saying some pair mutual information is positive. Terminal robust geometry yields a fixed per-influence pair-information rate; an acyclic extraction proves that those rates can be charged simultaneously without reuse; then the exact suspension decomposition subtracts the empty-mass and conditional-product reference mismatches before calling anything irreducible occurrence dependence.

## 5. What the theorem rules out and what remains

The result closes one concrete portion of the preceding `TERMINAL-SELECTOR-TO-KL` gap:

* If
  \[
  B_{\rm tens}<\frac{\kappa_\eta}{2}J_R,
  \]
  then the robust terminal branch forces a **strictly positive quantitative** occurrence-dependence credit under the canonical I-projection.
* There is no dimension factor and no reuse of one global KL over all physical pairs.
* The exact support/orientation relation is respected through `s=p/4+o`; the opposite-sign term is not discarded.
* The refuted implication `raw U_4=O(J)` is not invoked.
* No fixed-depth KL projection is used; `K_occ` and `K_susp` retain the full set-valued source, so the recursive-majority low-level barrier does not apply to this statement.

The theorem does **not** prove full FEI. Two branches remain genuinely unpaid:

1. **baseline-dominated robust branch:**
   \[
   B_{\rm tens}\ge\frac{\kappa_\eta}{2}J_R;
   \]
   one must prove that this explicit empty/reference-mismatch reserve itself forces an affordable physical block, a ratio descent, or another paid centered-orientation branch on a genuine critical core;
2. **small/nonrobust rows:** the assignment-prescribed fleet04/B12/B18 chain still requires a distinct nonreusing mechanism there.

The exact next implication handed to integration is therefore:

> **BASELINE-DOMINATED ROBUST EXCLUSION.** On a genuine ratio-`rho>4` all-block critical core, show that the explicit quantity `d2(v||c0)+vD(Q+||R_q+)` cannot absorb all of `(kappa_eta/2) J_R` for the robust-row mass without triggering an affordable physical restriction, strict ratio descent, or another quantitatively paid Path-C branch. Combine with the future `fleet04/B19` exhaustive alternative when that source actually exists.

This is narrower than the previous generic selector gap: the only loss in the robust branch is now an explicit, sign-known tensor/conditioning reference mismatch.

## 6. Arithmetic reproducibility

The only numerical constant used is

\[
d_2(7/16\Vert1/6)=0.2901785390585173\ldots,
\]

so its post-cycle-removal coefficient is

\[
0.14508926952925866\ldots.
\]

No finite enumeration is used as proof of Theorems 2.1, 3.2, or 4.1; they are analytic for arbitrary dimension under the stated source domain.

## 7. Status

`ESSENTIAL_STEP_APPLIED / TERMINAL_TO_KL_FOREST_BRIDGE / FULL_FEI_OPEN`.

Full FEI remains open. The robust terminal branch now has a source-valid, dimension-free and nonreusing conversion to canonical occurrence relative entropy after exact baseline subtraction. The remaining robust obstruction is the explicitly baseline-dominated branch, not an unspecified pair-information gap.
