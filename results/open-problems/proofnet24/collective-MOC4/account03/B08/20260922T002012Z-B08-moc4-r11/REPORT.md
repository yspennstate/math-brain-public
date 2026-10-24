# MOC4 account03/B08 r11 — permutation-tangent barrier and an exact generic stress point

**Model self-report:** GPT-5.6 Sol. **Configured reasoning:** not exposed; owner-requested effort is maximum actually supported.  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`.  
**Campaign:** MOC4, the complex-normal 4-by-4 Marcus–de Oliveira target.  
**Effective B08 assignment:** construct exact or rigorously enclosed counterexample candidates over true unitary matrices and complex spectra, checking separation from all 24 permutation products in a common support direction.  
**Outcome:** `ESSENTIAL_STEP_APPLIED`, candidate `MOC4-PERMUTATION-TANGENT-v1`. The parent MOC4 problem remains OPEN.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

The later owner control superseded this slot's older benchmark-building prompt, so this run did no new benchmark work and did not inspect or expose held-out benchmark gold.

## 1. Source-exact target and current campaign state

For all complex normal 4-by-4 matrices A,B, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{
 v_\sigma(a,b):=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}.
\]

After diagonalizing A, write

\[
D_U(a,b)=\det\!\left(\operatorname{diag}(a)+U\operatorname{diag}(b)U^*\right).
\]

The current source ledger points to Drury's weakened n=4 result, Bebiano--da Providencia's 2025 survey, and Mulero-Martinez's 2026 variational work, all of which leave the source-matching n=4 target open. A bounded public status search on 22 September 2026 found no newer source-matching proof or counterexample; this is a bounded check, not a worldwide no-solution certificate.

I used the following completed peer mathematics.

1. **Assigned partner account04/B09, `MOC4-U-LIFT-v1`**, scientific commit `ee33c17ceed673859063d8e53d0ecd9b05fd9fa5`: an exact rational orthogonal matrix refutes the stronger assertion that all one- and two-subset squared-minor marginals have one spectrum-independent common permutation coupling. It does not refute MOC4.
2. **account01/B07, `MOC4-MIXED-ASSIGNMENT-v1`**, scientific commit `2bc09bcf24348893b74ddf06addf605b6392ad90`: the signed complementary-pair orientation matrix is an exact linear image of `P=|U|^2`, and the support inequality reduces exactly to a structured joint `(P,R)` assignment inequality.
3. **account02/B08, `MOC4-DOUBLE-EIGENVALUE-LIFT-v1`**, scientific commit `14542c0b3258ea5763ed145dff8dd4d2e47b2136`: MOC4 holds whenever either spectrum has a repeated eigenvalue and on common reducing-block boundaries.
4. **account04/B08, `MOC4-GENERIC-STRICT-SUPPORT-v1`**, scientific commit `61aba8fc1d9eb46d6ae05b3f61a2706aad194a7f`: if MOC4 fails, it fails arbitrarily nearby on a generic locus with simple nonzero spectra, 24 distinct permutation vertices, no zero 1x1/2x2 unitary minors, strict 2x2 compression inequalities, no common reducing subspace, a positive support gap, and a unique maximizing permutation vertex.

The last item makes local behavior around a permutation unitary directly relevant: a generic counterexample may be assumed to have a unique exposed permutation vertex, so I asked whether a true unitary perturbation can leave the hull through that vertex.

## 2. Research moves used

This run deliberately used four of the fleet's method changes rather than extending the old coefficient-lift route:

- **Move 2 — attack the negation first:** search for true-unitary/simple-spectrum support violations and turn the best surviving candidate into an exact certificate.
- **Move 5 — add a parameter and differentiate:** set `U(t)=exp(tK)` and compute the exact second variation at a permutation unitary.
- **Move 6 — deform to a point you can solve:** start at a monomial/permutation unitary, where the determinant equals a hull vertex, and determine the first nonzero departure term.
- **Move 30 — one direction at a time:** fix a support functional `Re(eta z)` and identify exactly which transposition vertices control its tangent Hessian.

The decisive result is analytic, not a numerical observation.

## 3. Exact two-plane mixing identity

First, one isolated two-coordinate unitary mixing can never yield a counterexample.

### Lemma 1 — a single 2-by-2 unitary block traces a hull edge

Fix distinct indices `i,j`. Let U be the identity off `{i,j}` and let its restriction to that coordinate plane be an arbitrary 2-by-2 unitary W. Put

\[
\alpha=|W_{11}|^2=|W_{22}|^2,
\qquad 1-\alpha=|W_{12}|^2=|W_{21}|^2.
\]

Then

\[
\boxed{
D_U(a,b)=\alpha v_{\mathrm{id}}+(1-\alpha)v_{\tau_{ij}},
}
\tag{1}
\]

where `tau_ij` transposes i and j.

### Proof

All coordinates outside `{i,j}` contribute the common factor

\[
\prod_{k\ne i,j}(a_k+b_k).
\]

On the 2-by-2 block, `W diag(b_i,b_j) W*` has determinant `b_i b_j` and diagonal entries

\[
\alpha b_i+(1-\alpha)b_j,
\qquad
(1-\alpha)b_i+\alpha b_j.
\]

Hence

\[
\begin{aligned}
&\det\left(\operatorname{diag}(a_i,a_j)
+W\operatorname{diag}(b_i,b_j)W^*\right)\\
&=a_i a_j+a_i\bigl((1-\alpha)b_i+\alpha b_j\bigr)
+a_j\bigl(\alpha b_i+(1-\alpha)b_j\bigr)+b_i b_j\\
&=\alpha(a_i+b_i)(a_j+b_j)
 +(1-\alpha)(a_i+b_j)(a_j+b_i).
\end{aligned}
\]

Multiplying by the untouched coordinates gives (1). Thus a one-plane rotation lives exactly on the segment joining two permitted permutation products. ∎

This is consistent with the known common-reducing-block boundary theorem, but the explicit identity exposes the infinitesimal mechanism needed below.

## 4. New tangent theorem at a permutation unitary

By relabeling the b-spectrum, it is enough to work at `U(0)=I`. Let

\[
U(t)=e^{tK},\qquad K^*=-K,
\]

and set

\[
C=\operatorname{diag}(c_1,\ldots,c_4),
\qquad c_i=a_i+b_i.
\]

### Theorem 2 — the Hessian is exactly the transposition support deficit

For every skew-Hermitian K,

\[
\boxed{
D_{e^{tK}}(a,b)
=v_{\mathrm{id}}
+t^2\sum_{i<j}|K_{ij}|^2
\bigl(v_{\tau_{ij}}-v_{\mathrm{id}}\bigr)
+O(t^3).
}
\tag{2}
\]

Equivalently,

\[
\boxed{
\frac{d^2}{dt^2}D_{e^{tK}}(a,b)\bigg|_{t=0}
=2\sum_{i<j}|K_{ij}|^2
\bigl(v_{\tau_{ij}}-v_{\mathrm{id}}\bigr).
}
\tag{3}
\]

The formula is valid even when some `c_i=0`, by polynomial continuation.

### Proof

Let `D_b=diag(b)` and

\[
M(t)=\operatorname{diag}(a)+e^{tK}D_b e^{-tK}.
\]

Then

\[
M'(0)=[K,D_b],\qquad
M''(0)=[K,[K,D_b]].
\tag{4}
\]

Initially suppose every `c_i` is nonzero, so C is invertible. Since `[K,D_b]` has zero diagonal,

\[
\operatorname{tr}(C^{-1}M'(0))=0.
\]

The standard second derivative of determinant therefore gives

\[
D''(0)=\det C\left(
\operatorname{tr}(C^{-1}M''(0))
-\operatorname{tr}(C^{-1}M'(0)C^{-1}M'(0))
\right).
\tag{5}
\]

For `i\ne j`,

\[
M'_{ij}(0)=K_{ij}(b_j-b_i),
\]

while skew-Hermiticity gives

\[
M''_{ii}(0)=2\sum_{j\ne i}|K_{ij}|^2(b_j-b_i).
\tag{6}
\]

Grouping the two traces in (5) by unordered pairs `{i,j}` yields

\[
\frac{D''(0)}{\det C}
=2\sum_{i<j}|K_{ij}|^2
\frac{(a_j-a_i)(b_j-b_i)}{c_i c_j}.
\tag{7}
\]

But direct expansion gives the exact transposition identity

\[
\begin{aligned}
v_{\tau_{ij}}-v_{\mathrm{id}}
&=\left[(a_i+b_j)(a_j+b_i)
 -(a_i+b_i)(a_j+b_j)\right]
\prod_{k\ne i,j}(a_k+b_k)\\
&=(a_j-a_i)(b_j-b_i)
\prod_{k\ne i,j}(a_k+b_k).
\end{aligned}
\tag{8}
\]

Multiplying (7) by `det C=prod_k c_k` proves (3), and Taylor's formula gives (2). Both sides of (3) are polynomial in the spectral variables, so the identity extends from the open set `prod_i c_i != 0` to all spectra. ∎

## 5. Support-functional consequence: permutation vertices are strict local barriers

Fix a unit complex support direction eta and write

\[
L_\eta(z)=\Re(\eta z).
\]

Suppose `v_id` is the unique maximizer of `L_eta(v_sigma)` over all 24 permutations. Then in particular

\[
L_\eta(v_{\tau_{ij}}-v_{\mathrm{id}})<0
\qquad(i<j).
\]

Applying `L_eta` to (3) gives

\[
\boxed{
\frac{d^2}{dt^2}L_\eta(D_{e^{tK}})\bigg|_{0}
=2\sum_{i<j}|K_{ij}|^2
L_\eta(v_{\tau_{ij}}-v_{\mathrm{id}})<0
}
\tag{9}
\]

for every K with a nonzero off-diagonal entry. Diagonal skew-Hermitian K commutes with `D_b` and produces no motion at all.

Thus, modulo the irrelevant diagonal-phase stabilizer, a uniquely exposed permutation unitary is a **strict local maximum** of the determinant support functional. In particular, for each fixed simple generic spectral/support datum with a unique maximizing permutation, there is a neighborhood of the corresponding monomial unitary in which

\[
L_\eta(D_U)\le \max_\sigma L_\eta(v_\sigma).
\tag{10}
\]

The same statement holds around every permutation unitary after relabeling b.

This closes one concrete counterexample mechanism: a generic positive support gap cannot be born by an arbitrarily small true-unitary perturbation of a uniquely exposed permutation vertex. A hypothetical generic counterexample from the account04/B08 reduction must therefore occur at finite mixing distance from every relevant monomial unitary. If the support face is tied rather than unique, the quadratic form may have zero directions; then third and higher order interactions remain possible. That distinction is exactly why the unique-support generic reduction is useful.

### Measurable movement

Tracked quantity: **number of outward quadratic tangent modes at a uniquely exposed permutation unitary**.

- Before this run: `UNKNOWN`.
- After this run: **0**. Every nontrivial off-diagonal tangent mode has second variation equal to a positive weight times a strictly negative transposition support deficit.

This is not the global MOC4 inequality: the support functional can in principle turn upward after leaving the local permutation neighborhood.

## 6. Exact generic stress candidate over a true orthogonal matrix

The counterexample search was run over actual unitary/orthogonal matrices rather than independent doubly stochastic surrogates. It did not produce a MOC4 violation. I retained one dense rational orthogonal candidate because it lies on the generic strict-support locus and admits a complete exact certificate.

Take

\[
U=\begin{pmatrix}
-64884/690625&147/3125&-41416/138125&-7704/8125\\
118503/690625&3076/3125&4872/138125&168/8125\\
668888/690625&-504/3125&-25413/138125&-372/8125\\
-106296/690625&168/3125&-129204/138125&2549/8125
\end{pmatrix},
\tag{11}
\]

with

\[
a=(3+3i,-4-5i,2+5i,5+4i),
\]

\[
b=(-1-2i,5+5i,5+3i,5+2i).
\tag{12}
\]

The companion exact verifier proves, using only `fractions.Fraction`, that:

- `U^T U=I` exactly;
- both spectra are simple and nonzero, and all 16 sums `a_i+b_j` are nonzero;
- all 16 entries and all 36 two-by-two minors of U are nonzero;
- every 2-by-2 compression has nonzero singular-value discriminant;
- the six off-diagonal entries of `U diag(b) U^T` are nonzero, so with simple a there is no coordinate common reducing split;
- all 24 permutation products are distinct.

The determinant is exactly

\[
D_U=
\frac{5647508815927168}{59620361328125}
+i\frac{2616083753751744}{11924072265625}.
\tag{13}
\]

For the integer support functional

\[
L(z)=-985\Re z-12348\Im z,
\tag{14}
\]

the unique maximizing permutation is, in one-based image notation,

\[
\sigma=(3,2,1,4),
\qquad v_\sigma=-280+240i,
\]

with

\[
\max_\sigma L(v_\sigma)=-2687720.
\]

The determinant has

\[
L(D_U)=
-\frac{33415961428064187008}{11924072265625},
\]

so the exact support gap is

\[
\boxed{
L(D_U)-\max_\sigma L(v_\sigma)
=-\frac{1367393918298562008}{11924072265625}<0.
}
\tag{15}
\]

Thus this deliberately generic stress point is not a counterexample in that exposed direction.

More strongly, the verifier gives a complete three-vertex Caratheodory certificate that `D_U` is inside the full 24-point hull. The three one-based permutations are

\[
(3,2,1,4),\quad(3,4,1,2),\quad(4,1,2,3),
\]

with corresponding vertices

\[
-280+240i,\qquad 260+1320i,\qquad 12069-745i,
\]

and nonnegative rational weights

\[
\lambda_1=\frac{7425176834653241}{7720486083984375},
\]

\[
\lambda_2=\frac{417322412914702}{50480101318359375},
\]

\[
\lambda_3=\frac{2186232758361696}{72915701904296875}.
\]

They sum exactly to 1 and satisfy

\[
D_U=\lambda_1v_{(3,2,1,4)}
+\lambda_2v_{(3,4,1,2)}
+\lambda_3v_{(4,1,2,3)}.
\tag{16}
\]

This is a useful negative search result rather than evidence for the theorem by enumeration: it supplies a nondegenerate regression case that any proposed generic-support proof must handle.

## 7. What this changes in the shared proof route

The current end-to-end route can now be sharpened as follows.

1. By account04/B08, it suffices to handle the generic strict-support locus with a unique maximizing permutation.
2. By account01/B07, the target on that locus is the exact structured mixed `(P,R)` assignment inequality, not a universal common permutation-marginal lift.
3. By Theorem 2 here, a uniquely exposed permutation point is a strict local support maximum along every genuine unitary tangent direction. Therefore any failure of the mixed assignment inequality must be a **finite-distance interior phenomenon**, not an infinitesimal escape from a monomial unitary.
4. The exact rational candidate (11)--(16) supplies a true-unitary/simple-spectrum regression point in that interior regime and remains inside the hull by an exact three-vertex certificate.

This removes a natural local counterexample route and narrows the adversarial search toward genuinely multi-plane finite mixing.

## 8. Failed route and next obligation

The negation search did not find a positive support gap. I do not interpret that finite search as evidence that MOC4 is proved. The earlier universal coefficient-lift and P-marginal-preserving routes are already refuted by peers, so they were not retried.

The first remaining obligation for this B08 line is:

> **`MOC4-FINITE-MIXING-ADVERSARY-v1`.** On the generic strict-support locus, either find a true unitary, simple spectra and one common support direction with positive gap against all 24 permutation products, or prove a global obstruction preventing the locally negative transposition-tangent modes from turning into a positive support gap at finite mixing distance.

A promising next calculation is to follow multi-plane geodesics and determine whether the first sign-changing higher-order term can be expressed through 3-cycles/4-cycles of permutation vertices and then bounded by the B07 `(P,R)` compatibility constraints. The one-plane case is already exactly convex by Lemma 1, so any genuine obstruction must use interacting planes.

## 9. Verification and integrity

`verify_local_tangent_stress.py` is a standard-library exact checker for the rational candidate and the transposition identity. `verification.txt` records its successful output. The analytic tangent theorem is proved on the page; the script is not presented as a universal proof certificate.

No benchmark answers, evaluator keys, generation secrets, credentials, scheduler identifiers, machine paths, unrelated private transcripts, email, Drive, public posting, paid model/API call, Codex execution or remote workflow was used. FEI proof material was kept separate from this MOC4 scientific output. Parent status: **OPEN / NOT PROVED / NOT DISPROVED**.
