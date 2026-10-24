Model actually run: **GPT-5.6 Sol. Configured reasoning level: UNKNOWN/UNVERIFIED.** The prompt requests maximum supported reasoning, but no authenticated runtime selector/readback is exposed here.

# FOREST / account03 B02 — a sign-cluster reduction for any lexicographically minimal counterexample

Status: **AUXILIARY_ONLY / CANDIDATE_FULL for the structural lemma below, pending independent review. The Grimmett–Winkler uniform-forest conjecture remains OPEN.**

Current collective assignment: prove a useful minimal-counterexample reduction that reaches the genuinely unresolved 3-connected obstruction rather than another finite graph class. Named partner: `account04/B03`. No completed current-reallocation partner snapshot was found at the fresh observation point, so this run followed the collective order's missing-peer rule: reconstruct the minimal source-valid state and do the mathematics without waiting.

## 1. Source and inherited boundary

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{h\in F}y_h.
\]

At unit weights write `Z=I_G(1)`, `Z_e=I_e(1)`, `Z_{ef}=I_{ef}(1)` and

\[
\Delta_G(e,f)=Z_eZ_f-ZZ_{ef}.
\]

The source conjecture asks for `Delta_G(e,f)>=0` for every finite simple graph and every distinct edge pair. Equivalently, with `X_e=1_{e\in F}` under the uniform law on all forests,

\[
\operatorname{Cov}(X_e,X_f)=-\frac{\Delta_G(e,f)}{Z^2}\le0.
\]

The preserved P14 state used here is exact:

1. every simple graph through nine vertices is covered at unit weights;
2. the fixed-graph Cocks/Semple–Welsh implication upgrades a source-valid simple graph to all positive edge weights;
3. block factorization and the two-separator transfer reduce a vertex-minimal source counterexample to a **3-connected** graph;
4. the generic degree-three star/mesh route is genuinely blocked by an old-edge/old-edge mixed three-terminal polarization with no universal sign.

This run does not retry that killed mixed-polarization inequality. Instead it extracts a consequence of deletion/contraction that any *minimal* 3-connected counterexample would have to satisfy simultaneously for every third edge.

## 2. Exact three-edge identity

Fix distinct edges `e,f,g` of an arbitrary graph. Split the forest polynomial with respect to `g`:

\[
I_G=A+y_g B,
\]

where `A=I_{G\setminus g}` and `B=I_{G/g}` in the graphic-matroid deletion/contraction sense. Evaluate all remaining edge weights at one and use the same letters for the resulting counts. Thus

\[
Z=A+B,
\]

and similarly

\[
Z_e=A_e+B_e,\quad Z_f=A_f+B_f,\quad Z_{ef}=A_{ef}+B_{ef}.
\]

Put

\[
D_0=A_eA_f-AA_{ef},\qquad
D_1=B_eB_f-BB_{ef}.
\]

These are the `e,f` Rayleigh gaps in the deletion and contraction strata. Also

\[
\Delta_G(g,e)=BA_e-AB_e,
\qquad
\Delta_G(g,f)=BA_f-AB_f.
\]

A direct expansion gives the exact integer identity

\[
\boxed{
AB\,\Delta_G(e,f)
=
BZ\,D_0+AZ\,D_1
-
\Delta_G(g,e)\Delta_G(g,f).
}
\tag{2.1}
\]

Equivalently, since `A,B>0`,

\[
\boxed{
\Delta_G(e,f)
=Z\left(\frac{D_0}{A}+\frac{D_1}{B}\right)
-
\frac{\Delta_G(g,e)\Delta_G(g,f)}{AB}.
}
\tag{2.2}
\]

This is stronger than the usual statement that the one-edge-field Rayleigh polynomial is quadratic: it solves the mixed coefficient exactly in terms of the two `g`-pair Rayleigh gaps.

### Proof

Starting from the definitions,

\[
\Delta_G(e,f)
=(A_e+B_e)(A_f+B_f)-(A+B)(A_{ef}+B_{ef}).
\]

Multiply by `AB`, expand, and group the pure `A` and pure `B` terms. The remaining cross terms are exactly

\[
-(BA_e-AB_e)(BA_f-AB_f).
\]

This yields (2.1), and division by `AB` yields (2.2). No probabilistic approximation or asymptotic argument is used.

## 3. Minimal-counterexample sign forcing

Choose a source counterexample `G` lexicographically minimal in

\[
(|V(G)|,|E(G)|).
\]

By the inherited P14 reduction it may also be taken 3-connected, and current complete coverage implies `|V(G)|>=10`.

Fix any violating pair `e,f`, so

\[
\Delta_G(e,f)<0.
\]

Now take **any** third edge `g`.

- `G\setminus g` has the same vertex count and fewer edges, so lexicographic minimality gives `D_0>=0`.
- `G/g` has fewer vertices. Contraction can create loops and parallel classes. Loops are irrelevant to forests. If the two target labels fall in one parallel class, their conditional covariance is automatically nonpositive because they cannot coexist. Otherwise parallel classes compress to positive-weight edges of a smaller simple graph; the preserved fixed-graph unit-to-positive-weight theorem then gives `D_1>=0`, and resolving labels inside a parallel class only multiplies the relevant covariance by positive class-size factors.

Applying (2.1) therefore gives

\[
\boxed{
\Delta_G(g,e)\Delta_G(g,f)
>
Z\bigl(BD_0+AD_1\bigr)
\ge0.
}
\tag{3.1}
\]

In particular:

### Theorem `FOREST-MINIMAL-SIGN-COHERENCE-20260922`

If `G` is lexicographically minimal among finite simple counterexamples to uniform-forest pairwise negative correlation and `e,f` is any violating pair, then for **every** third edge `g`,

\[
\boxed{
\Delta_G(g,e)\Delta_G(g,f)>0.
}
\tag{3.2}
\]

Thus `g` has the same strict Rayleigh sign relative to `e` and `f`. In covariance language,

\[
\boxed{
\operatorname{Cov}(X_g,X_e)
\operatorname{Cov}(X_g,X_f)>0.
}
\tag{3.3}
\]

The quantitative excess in (3.1), not merely its sign, is forced by the deletion and contraction conditional gaps.

## 4. Bad pairs form equivalence classes

Define a relation on `E(G)` by

\[
e\sim f
\quad\Longleftrightarrow\quad
(e=f)\ \text{or}\ \Delta_G(e,f)<0.
\]

Recall that `Delta<0` means **positive** covariance, i.e. a source violation.

The relation is reflexive and symmetric. It is also transitive. Indeed, suppose `e,f,h` are distinct and

\[
\Delta_G(e,f)<0,\qquad \Delta_G(f,h)<0.
\]

Apply Theorem (3.2) to the violating pair `e,f` and the third edge `h`. Then

\[
\Delta_G(h,e)\Delta_G(h,f)>0.
\]

The second factor is negative, so the first factor must also be negative. Hence `e\sim h`.

Therefore:

### Corollary `FOREST-MINIMAL-BAD-CLUSTERS-20260922`

In a lexicographically minimal counterexample, the positive-covariance edge pairs partition the edge set into equivalence classes. Every nontrivial class is a clique of source violations.

Moreover, if `C` is a nontrivial class and `h\notin C`, then for every `e\in C`,

\[
\boxed{\Delta_G(h,e)>0}
\tag{4.1}
\]

(strict negative covariance). To see this, choose distinct `e,f\in C`. By (3.2), `Delta(h,e)` and `Delta(h,f)` have the same nonzero sign. If that sign were negative, transitivity would place `h` in `C`. Hence it is positive.

So a minimal counterexample cannot have an arbitrary scattered pattern of violating pairs. Its covariance-sign graph is forced to be a disjoint union of complete positive-covariance clusters, with **strictly negative covariance from every nontrivial cluster to every external edge**.

This is a global restriction on the surviving 3-connected obstruction, not a theorem for a convenient subclass.

## 5. Why this is useful against the old 3-terminal blocker

The prior degree-three star/mesh route tried to prove one mixed three-terminal polarization nonnegative for every environment. Exact physical examples show that universal statement is false. The present reduction avoids requiring that false sign.

If a degree-three apex occurs inside a true lexicographically minimal counterexample, any old-edge/old-edge violation produced by the surviving mixed term must also satisfy the sign-cluster law above against **each of the three star edges and every other edge of the graph**. Thus a locally negative mixed polarization is not sufficient: it must extend to a globally coherent equivalence-class sign pattern and meet the quantitative lower bound (3.1) for every deletion/contraction stratum.

This turns the next attack into a narrower target:

> **Next missing implication.** Show that no 3-connected graphic forest measure can realize a nontrivial Rayleigh-negative equivalence class satisfying (3.1) simultaneously for every external edge.

A promising concrete subtarget is to combine (3.1) with the exact three-terminal response cone at a degree-three vertex and prove that at least one star edge necessarily has opposite-sign Rayleigh responses to a violating old-edge pair. That would rule out the entire unresolved degree-three 3-connected branch without asserting the already-refuted universal mixed-polarization inequality.

No such contradiction is claimed in this run.

## 6. Exact computational sanity check

The analytic identity was independently checked by exact forest enumeration over **every labelled simple graph on 2,3,4,5 vertices** and every unordered marked pair `e,f` with a distinct third present edge `g`.

Counts:

- graphs checked: `1098`;
- marked triples checked: `46,563`;
- identity failures: `0`;
- failures of the quantitative implication `D_0,D_1>=0` and `Delta_G(e,f)<0 => (3.1)`: `0`.

The finite check is only a sanity check of the algebra; it is **not** evidence that the source conjecture is solved beyond the inherited nine-vertex baseline.

Checker creation commit: `c9c2a5082ef764baa3326374688d893b578c7f68`.

Executed-output archive commit: `5e12ab226f073d961d69ee23a4438ecd802c290d`.

The output ends `ALL_EXACT_CHECKS_PASSED`.

## 7. Status and handoff

**Target-level status:** OPEN.

**New structural progress:** a lexicographically minimal 3-connected counterexample, if one exists, must obey the exact three-edge identity (2.1), the quantitative sign-forcing inequality (3.1) for every third edge, and the bad-pair equivalence-class structure of §4.

**Not claimed:** no full proof, no ten-vertex census advance, no novelty/priority claim, no universal star-mesh mixed-term sign, no stronger negative association result.

**Partner state:** the exact assigned partner is `account04/B03`; no completed current collective FOREST snapshot from that slot was available at the observation point. The next compatible partner result should be tested directly against (3.1), not merely cited.

**Suggested next recipient/action:** `account04/B03` should try to falsify the sign-cluster condition inside the exact three-terminal response cone or derive an edge-local obstruction to a nontrivial bad class. Any counterexample to the structural lemma must identify which minor nonnegativity premise fails; any successful contradiction would remove a genuine 3-connected branch of the parent problem.
