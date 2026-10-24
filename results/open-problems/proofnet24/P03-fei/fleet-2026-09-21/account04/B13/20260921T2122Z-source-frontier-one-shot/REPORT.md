# B13 FEI quantitative all-row stability — source-frontier one-shot elimination with influence-relative exceptional-row budget

**Account/slot:** account04/B13  
**Scientific status:** full uniform-cube Fourier entropy--influence conjecture remains **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Native `math_brain` / `brain` were not available in this invocation, so no authenticated brain retrieval or receiver-context use occurred.  
**Claim level:** universal conditional Boolean theorem on the current robust near-subcube sector, with an explicit influence-relative all-row remainder. No novelty or publication-priority claim.

## 0. Missing implication and the new change of argument

The live joint interface B asks for a quantitative all-row stability theorem including exceptional rows, or a nonreusing adaptive elimination with an influence-relative error budget. The previous account04/B13 result handled the **exact zero-defect** sector in the presence of arbitrary exceptional rows and proved

\[
H_Z(f)\le 4J_Z+4D_E,
\]
while preserving the account04/B18 mixed-curvature law and exact zero-defect classification. It did not give a positive-error elimination of all near-rigid rows.

This run consumes, substantively rather than as a reference list, the newest compatible other-account result

`account03/B13/20260921T203308Z-integrability-dag/REPORT.md`, blob `56210613208b533b79a875f1289133924ec74ab8`.

That report proves, in the simultaneous low-defect / physical-near-subcube regime at the stated `1/16` thresholds, that reciprocal trigger incidences form exact compatible components and that the contracted trigger graph is a DAG. In particular every component has one common trigger signature

\[
T_C=\{i\}\cup F_i\qquad(i\in C),
\]
while every cross-component trigger is a directed DAG edge.

The same-account integration input is

`account04/B18/20260921T201525Z-sink-component-peeling/REPORT.md`, blob `2575d3945985e76d1f61831a65366b29b5052d27`.

It proved that a **sink** representative family is collision-free and that, for a near-subcube row with support error `e_i`, revealing any block containing its trigger block `F_i` leaves expected folded influence at most `e_i`. That argument still described successive sink-frontier peeling as an open issue.

The new observation is that repeated sink peeling is unnecessary for the robust sector. Use the DAG in the opposite way: choose one representative in every component, but choose each **non-source** representative to be a coordinate deliberately hit by one incoming trigger. Then reveal the union of the representatives' trigger blocks. Incoming collisions, which a Hall-selector argument normally avoids, become useful: they delete every non-source representative. Exactly one representative of each **source** component survives, and those source representatives are automatically outside the whole revealed union. Thus one physical block simultaneously eliminates every other robust row.

This produces the dimension-free all-row remainder

\[
\boxed{
\mathbb E_z J(f_{A=z})
\le J_E+\varepsilon J_R,
}
\]

where `R` is the robust row set, `E` is the arbitrary exceptional set, and `e_i\le\varepsilon j_i` on robust rows. At the current physical threshold `\varepsilon=1/16`, an all-robust state contracts expected centered influence by a factor at least sixteen in **one** restriction step. No cube-measure error is multiplied by the ambient dimension.

This is not full FEI: the theorem does not yet prove that the exceptional influence mass `J_E` is universally small, nor does it pay the whole Shannon cost of the reveal block by `O(J)`.

---

## 1. Source-exact setup

Work in the median-character gauge and delete irrelevant coordinates. Thus

\[
f:\mathbb F_2^n\to\{-1,+1\},
\qquad
0<j_i=\operatorname{Inf}_i(f)\le\frac12
\]

for every active coordinate. For row `i`, write

\[
g_i=D_i f,\qquad
E_i=\{g_i\ne0\}.
\]

Let `R` be a collection of robust rows for which there is a coordinate subcube

\[
Q_i=\{x_{F_i}=a_i\},
\qquad
s_i=\mu(Q_i),
\]

with physical support error

\[
e_i=\mu(E_i\triangle Q_i)\le\varepsilon j_i.
\tag{1.1}
\]

For the current account03/B13 theorem one may take the simultaneous defect / physical thresholds at `1/16`; below, the combinatorial theorem only needs the two conclusions that it proved:

1. reciprocal trigger components have an exact common signature
   \[
   T_C=\{i\}\cup F_i\quad(i\in C);
   \tag{1.2}
   \]
2. after contracting reciprocal components, the cross-component trigger relation
   \[
   C\longrightarrow D
   \quad\Longleftrightarrow\quad
   \exists i\in C,\ k\in D:\ k\in F_i
   \tag{1.3}
   \]
   is a DAG.

Let `E=[n]\setminus R` be the arbitrary exceptional rows. No hypothesis is imposed on their cardinality, geometry, or cube measure.

The mixed-curvature conservation of account04/B18 remains live throughout:

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k.
\tag{1.4}
\]

In particular

\[
\sum_{i\ne k}p_{ik}\le4d_k.
\tag{1.5}
\]

---

## 2. PROVED: source-frontier representatives give one-shot elimination

Let `\mathcal C` be the reciprocal components of `R`, and let `\mathsf{DAG}` be the quotient graph (1.3).

Choose one representative `r_C\in C` for every component as follows.

* If `C` is a source of `\mathsf{DAG}` (indegree zero), choose `r_C` arbitrarily.
* If `C` is not a source, choose one incoming edge `P\to C`, choose a witness `k\in C` hit by that edge, and set `r_C=k`.

Define the single physical reveal block

\[
A=\bigcup_{C\in\mathcal C}F_{r_C}
\tag{2.1}
\]

and the source-representative set

\[
S=\{r_C:C\text{ is a source component}\}.
\tag{2.2}
\]

### Theorem 2.1 — exact survivor identity

\[
\boxed{R\setminus A=S.}
\tag{2.3}
\]

Equivalently, one reveal block `A` deletes every nonrepresentative robust coordinate and every representative of a non-source component, while preserving exactly one representative from each source component.

### Proof

First consider `x\in C\setminus\{r_C\}`. By the common signature (1.2),

\[
x\in T_C=\{r_C\}\cup F_{r_C}.
\]

Since `x\ne r_C`, necessarily `x\in F_{r_C}\subseteq A`. Thus every nonrepresentative is revealed.

Now suppose `C` is not a source. By construction there is an incoming component `P` and the chosen representative `r_C` is a witness hit by some row `i\in P`:

\[
r_C\in F_i.
\]

Because `r_C\notin P` and all rows of `P` have the same external trigger signature `T_P`, membership of the external coordinate `r_C` is independent of which row in `P` is used. Hence

\[
r_C\in F_{r_P}\subseteq A.
\]

So every non-source representative is also revealed.

It remains to show that a source representative survives. Clearly `r_C\notin F_{r_C}`. If for a different component `D` one had

\[
r_C\in F_{r_D},
\]

then by definition there would be a quotient edge `D\to C`, contradicting that `C` is a source. Hence `r_C\notin A` for every source component. Combining the three cases proves (2.3). QED.

### Why this is different from sink peeling

The prior sink-frontier theorem selected representatives so that **no selected representative was hit**. Here only the representatives that are meant to survive are protected. Every non-source representative is chosen precisely so that an incoming component hits it. Thus the same trigger collisions become an elimination mechanism rather than an obstruction.

The construction is one-shot: no coordinate in `A` is revealed twice, and no iterative sink removal is needed to eliminate the robust quotient DAG.

---

## 3. PROVED: source representatives are still a Hall-survivor family

The stronger global block (2.1) contains trigger blocks of representatives from *all* components, not only source components. Nevertheless Theorem 2.1 gives

\[
S\cap A=\varnothing.
\tag{3.1}
\]

For every `r\in S`, of course

\[
F_r\subseteq A.
\tag{3.2}
\]

Therefore the source representatives satisfy exactly the noncollision hypothesis required by the account01/B13 block-crossing/Hall theorem, but with a reveal block that simultaneously kills all downstream robust components.

The account04/B18 larger-block refinement applies unchanged. Put on a branch `z` of the restriction `A`

\[
U_r(z)=\operatorname{Inf}_r(f_{A=z}),
\qquad
q_r(z)=\min(U_r(z),1-U_r(z)).
\]

Then

\[
\boxed{
\mathbb E_z q_r(z)\le e_r
\qquad(r\in S).
}
\tag{3.3}
\]

Indeed the near-subcube elimination theorem gives the same bound after revealing `F_r`, and `A` is a refinement of that sigma-field; concavity of `u\mapsto\min(u,1-u)` makes the expected folded influence nonincreasing under the refinement.

The corresponding posterior-majority crossing obeys

\[
\boxed{
c_r(A)\ge j_r-e_r.}
\tag{3.4}
\]

Thus the common block simultaneously supplies a real physical crossing to every surviving source representative.

On a median-centered corrected-entropy critical core, the same B18 budget therefore applies with this new source frontier:

\[
\boxed{
B_A\ge \rho I_A+
\sum_{r\in S}
\left[
\rho(j_r-e_r)+\mathfrak j(j_r)-\frac{2}{\ln2}e_r
\right].
}
\tag{3.5}
\]

The difference from the earlier sink theorem is not the scalar coefficient. It is that the very same `A` has already removed every non-source robust component.

At the inherited `e_r\le j_r/16` calibration and the current lower-bound-scale value used by the B18 report, each source term has the same positive coefficient `>5.8884 j_r`. This numerical statement is only a calibration of (3.5), not a universal FEI closure.

---

## 4. PROVED: all-row influence-relative remainder, including arbitrary exceptions

Define

\[
J_R=\sum_{i\in R}j_i,
\qquad
J_E=\sum_{k\in E}j_k,
\qquad
J=J_R+J_E.
\]

After restricting the one block `A`, every robust coordinate outside `S` is physically gone by Theorem 2.1. For the surviving source representatives, (3.3) gives

\[
\mathbb E_z\sum_{r\in S}q_r(z)
\le\sum_{r\in S}e_r.
\tag{4.1}
\]

Now take an exceptional coordinate `k\in E` that is not itself revealed by `A`. Raw influence is an exact martingale under restriction of other coordinates:

\[
\mathbb E_z\operatorname{Inf}_k(f_{A=z})
=\operatorname{Inf}_k(f)
=j_k.
\tag{4.2}
\]

Since folded influence is at most raw influence on every branch,

\[
\mathbb E_z\min\bigl(
\operatorname{Inf}_k(f_{A=z}),
1-\operatorname{Inf}_k(f_{A=z})
\bigr)
\le j_k.
\tag{4.3}
\]

Exceptional coordinates lying in `A` contribute zero because they are revealed. Summing (4.1)--(4.3) proves:

### Theorem 4.1 — dimension-free all-row residual budget

\[
\boxed{
\mathbb E_z J(f_{A=z})
\le
J_E+\sum_{r\in S}e_r.
}
\tag{4.4}
\]

If every robust row has relative physical error `e_i\le\varepsilon j_i`, then

\[
\boxed{
\mathbb E_z J(f_{A=z})
\le
J_E+\varepsilon\sum_{r\in S}j_r
\le
J_E+\varepsilon J_R.
}
\tag{4.5}
\]

Equivalently, if the exceptional influence fraction satisfies `J_E\le\alpha J`,

\[
\boxed{
\mathbb E_z J(f_{A=z})
\le(\alpha+\varepsilon)J.
}
\tag{4.6}
\]

At the current `\varepsilon=1/16` physical threshold:

\[
\boxed{
\mathbb E_z J(f_{A=z})
\le J_E+\frac1{16}J_R.
}
\tag{4.7}
\]

This is the requested type of influence-relative error accounting. The exceptional rows are not converted into a cube-measure error and no factor of the ambient dimension appears.

### Exact-support endpoint

If `e_i=0` for every robust row, then every surviving source representative has nonnegative folded influence with expectation zero, hence folded influence zero on every branch. It is therefore irrelevant or a pure character factor branchwise and can be removed by character recentering without additional spectral entropy or centered-influence cost. So a single block eliminates the entire robust sector exactly, even while arbitrary exceptional rows remain.

This is compatible with, and does not weaken, the preceding exact zero-defect component classification. That classification remains the sharper statement about the root function when **all depth defects vanish**.

---

## 5. PROVED: mixed-curvature still pays representative-trigger multiplicity

The one-shot selector must retain the account04/B18 conservation bank rather than replacing it by a graph-only argument.

For a representative `r` and `k\in F_r`, the coordinate-subcube boundary estimate gives

\[
p_{rk}\ge2(s_r-e_r).
\]

Because `|s_r-j_r|\le e_r`, if `e_r\le\varepsilon j_r` then

\[
p_{rk}
\ge2(j_r-2e_r)
\ge2(1-2\varepsilon)j_r.
\tag{5.1}
\]

Sum (5.1) over all representative-trigger incidences and apply mixed-curvature conservation (1.5):

\[
2(1-2\varepsilon)
\sum_Cj_{r_C}|F_{r_C}|
\le
\sum_k\sum_{r_C:k\in F_{r_C}}p_{r_Ck}
\le4\sum_kd_k.
\]

Hence:

### Theorem 5.1 — one-shot trigger-load certificate

\[
\boxed{
\sum_Cj_{r_C}|F_{r_C}|
\le
\frac{2}{1-2\varepsilon}\sum_kd_k.
}
\tag{5.2}
\]

At `\varepsilon=1/16`,

\[
\boxed{
\sum_Cj_{r_C}|F_{r_C}|
\le\frac{16}{7}\sum_kd_k.
}
\tag{5.3}
\]

The constant `16/7` is exact from the displayed inequalities. Equation (5.2) does **not** assert `\sum d_k=O(J)`; that false/unpaid arrow remains visible. Its role is to show that the one-shot construction introduces no new trigger multiplicity beyond the already identified mixed-curvature depth bank.

---

## 6. What the other-account result changed exactly

Before consuming account03/B13, the strongest current physical elimination step was the account04/B18 **sink** frontier:

* one collision-free representative per sink component;
* one common block eliminates the rest of those sink components;
* successive frontiers were still needed to reach upstream components.

The account03/B13 theorem adds the exact reciprocal-component signature and a true quotient DAG. The new proof uses the common signature twice in a way the sink argument did not:

1. an incoming edge can be made to hit the chosen representative of every non-source component, independent of which representative was chosen in the predecessor component;
2. a source representative cannot lie in any representative trigger block, because that would create a forbidden incoming edge.

Those two facts yield the exact survivor identity `R\setminus A=S`. Thus **all** robust components, not just one frontier, are handled by one physical restriction. The only robust rows left are source representatives, and their total post-restriction folded influence is at most their physical support-error mass.

This is a real mechanism change, not a restatement of the DAG.

---

## 7. Remaining universal gap

The result removes a combinatorial nonreuse/repeated-peeling obstruction in the robust sector, but it does not complete interface B or FEI. Three source-exact arrows remain unpaid.

1. **Low depth defect to physical near-subcube stability.** The account02/B12 defect identity
   \[
   \operatorname{Slack}_{\rm sign}+\operatorname{Slack}_{\rm iso}
   =4j_i\Delta_i
   \]
   identifies the correct quantitative input, but the fleet has not yet proved a source-exact theorem turning every sufficiently small positive `\Delta_i` into (1.1) with a dimension-free relative error.

2. **Exceptional influence mass.** Theorem 4.1 charges arbitrary exceptional rows by `J_E`, which is dimension-free and honest, but no universal theorem yet makes `J_E` a small fraction of `J` or pays it by another already-controlled bank.

3. **Reveal-block Shannon/depth payment.** Theorem 5.1 charges representative trigger multiplicity to `\sum d_k`, preserving the exact mixed-curvature conservation. But `\sum d_k` is the second factorial spectral moment and is not universally `O(J)`. The source-frontier elimination therefore cannot be turned into a full FEI proof by silently replacing depth with influence.

A useful conditional corollary makes the next target precise. If a quantitative row-shape theorem gives, for some `\eta>0`,

* every row with `\Delta_i\le\eta` is robust with `e_i\le\varepsilon(\eta)j_i`, and
* the remaining rows satisfy an influence-mass estimate `J_E\le\alpha(\eta)J`,

then this run gives one physical block with

\[
\mathbb E J(\text{child})
\le[\alpha(\eta)+\varepsilon(\eta)]J.
\tag{7.1}
\]

That is now the clean quantitative interface to B12/B18: prove `\alpha(\eta)+\varepsilon(\eta)<1` with a simultaneously paid reveal-block entropy budget, or construct a genuine Boolean counterfamily to that proposed positive-defect stability statement.

---

## 8. Claim ledger and handoff

**PROVED here, conditional only on the already proved robust-component/DAG hypotheses:**

* exact source-frontier survivor identity `R\setminus A=S`;
* one-shot elimination of every non-source robust component;
* simultaneous Hall/crossing property for the surviving source representatives;
* all-row expected centered-influence remainder `J_E+\sum_{S}e_r`;
* relative specialization `J_E+\varepsilon J_R`, giving `J/16` contraction in the all-robust `1/16` regime;
* one-shot mixed-curvature trigger-load bound `(2/(1-2\varepsilon))\sum d_k`, equal to `(16/7)\sum d_k` at `1/16`.

**PRESERVED:** account04/B18 mixed signed-curvature conservation and exact zero-defect classification; account04/B13 exact zero-defect exceptional-gate theorem; all known failures of ambient-dimension continuity and of treating `\sum d_k` as `O(J)`.

**OPEN:** quantitative low-positive-defect row shape with controlled exceptional influence mass; dimension-free Shannon payment for the one-shot reveal block; full uniform-cube FEI.

`consumed_peer_artifact`: `proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260921T203308Z-integrability-dag/REPORT.md`, blob `56210613208b533b79a875f1289133924ec74ab8`.

`applied_to_claim`: source-frontier representative selection, one-shot robust-component elimination, and the influence-relative all-row remainder.

`next_recipient`: account04/B18 for proof integration, and account04/B12 / account02 stability workers for the positive-defect row-shape and exceptional-mass arrow.

`remaining_implication`: derive a source-exact quantitative theorem that turns the defect budget into `J_E+\varepsilon J_R` with controlled `J_E`, while paying the single reveal block's Shannon cost by centered influence rather than ambient dimension or uncontrolled total depth.

`full_problem_change`: repeated robust sink-frontier peeling is no longer necessary; the robust quotient DAG can be eliminated in one physical block up to an influence-relative source-frontier error. Full FEI remains OPEN.
