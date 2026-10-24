SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B19, 2026-09-23T15:17:00Z.
attacking: assemble the current paid proof graph and test the first surviving STAR low-rank/double-anchor implication against a sharp moving-ridge concentration construction.

# account04/B19 r4 — correction-safe proof graph and moving-ridge provenance barrier

**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

## 1. Source-pinned graph now available

The following implications are compatible and noncircular.

1. Claude's corrected physical-block theorems D', D5, the ruled-side estimates, and the finite-dimensional Fourier bounds are used at their stated marginal gates only:
   `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
2. The strict no-pivot branch has now been strengthened by account04/B20:
   if `s_3(A)>=1` and `max_i|A_ii|<1/64`, there is an original-coordinate cross cut with
   \[
   \|A[J,K]\|_F^2>11907/16384.
   \]
   D5 pays the full law by \(\|p_Q\|_\infty<116.502\), unless the first four squared singular values of this same cut carry more than
   \[
   750141/1048576.
   \]
3. Independently, account01/B19's completed theorem
   `QFORM-STAR-TAIL-OR-DOUBLE-ANCHOR-v1` at
   `math-open-problems@c2421f60310808603fb459131584028ec1502d0c`
   applies D5, the collective-tail theorem, and D' to the same STAR cut. It pays the diffuse branches by the explicit constants
   \[
   199.413,\qquad 340.320,\qquad 1018.124,
   \]
   and leaves only near rank one, near rank two, simultaneous top-two left/right physical leverage anchors, or simultaneous row/column three-volume anchors.
4. The existing mixed-Fresnel and grouped square/hyperbola theorems pay the exact-null and selected leakage-free endpoints, but do not cover arbitrary same-bank moving-ridge leakage.

Thus the first unproved STAR implication is genuinely a product-provenance theorem on the low-rank/double-anchor packet. It cannot be replaced by a statement about an arbitrary bounded joint density. The theorem below proves this last assertion sharply.

## 2. The moving-ridge arbitrary-joint statement is false

### Theorem — `QFORM-MOVING-RIDGE-JOINT-CAP-BARRIER-v1`

For every \(0<\varepsilon<1\) there exist:

- \(X\sim\mathrm{Unif}[0,1]\);
- a random triple \((Y,Z,W)\), independent of \(X\), with a joint probability density bounded by one;

such that for
\[
T=4XY+Z^2-YW
\]
the law of \(T\) has a density and
\[
\boxed{\|p_T\|_\infty\ge {1\over9\varepsilon}.}
\]
Moreover the symmetric matrix of this quadratic form in coordinates \((X,Y,Z,W)\) is
\[
A_*=
\begin{pmatrix}
0&2&0&0\\
2&0&0&-1/2\\
0&0&1&0\\
0&-1/2&0&0
\end{pmatrix},
\]
with exact spectrum
\[
\boxed{\operatorname{spec}(A_*)=\{1,0,\sqrt{17}/2,-\sqrt{17}/2\}.}
\]
Hence \(A_*\) itself has three eigenvalues of modulus at least one.

This is **not** a counterexample to the original conjecture, because \(Y,Z,W\) are not mutually independent. It is a counterexample to the proposed shortcut that would retain only their joint density cap.

### Proof

For \(L>0\), define
\[
S_{\varepsilon,L}=
\{(y,z,w):\varepsilon\le y\le2\varepsilon,\ L\le w\le2L,\
\sqrt{yw}\le z\le\sqrt{yw+\varepsilon}\}.
\]
Its volume is
\[
V_\varepsilon(L)=
\int_\varepsilon^{2\varepsilon}\int_L^{2L}
\bigl(\sqrt{yw+\varepsilon}-\sqrt{yw}\bigr)\,dw\,dy.
\]
This is continuous and positive for \(L>0\). As \(L\downarrow0\), \(V_\varepsilon(L)\to0\). Since
\[
\sqrt{yw+\varepsilon}-\sqrt{yw}
={\varepsilon\over\sqrt{yw+\varepsilon}+\sqrt{yw}},
\]
one has \(V_\varepsilon(L)\asymp\varepsilon^{3/2}\sqrt L\) as \(L\to\infty\), and therefore \(V_\varepsilon(L)\to\infty\). Choose \(L=L_\varepsilon\) with \(V_\varepsilon(L_\varepsilon)=1\).

Let \((Y,Z,W)\) have density \(\mathbf1_{S_{\varepsilon,L_\varepsilon}}\). It is normalized and capped by one. On its support,
\[
0\le Z^2-YW\le\varepsilon.
\]
Because \(0\le X\le1\) and \(\varepsilon\le Y\le2\varepsilon\),
\[
0\le4XY\le8\varepsilon,
\]
hence \(T\in[0,9\varepsilon]\) almost surely. Conditional on \((Y,Z,W)\), \(4XY\) has an absolutely continuous uniform law on an interval of positive length, so \(T\) is absolutely continuous. Its density integrates to one on an interval of length \(9\varepsilon\), proving
\[
\|p_T\|_\infty\ge(9\varepsilon)^{-1}.
\]

Finally the \((X,Y,W)\) block of \(A_*\) is a weighted three-vertex star with nonzero eigenvalues
\[
\pm\sqrt{2^2+(1/2)^2}=\pm\sqrt{17}/2,
\]
and \(Z\) contributes eigenvalue \(1\), proving the spectrum formula.

## 3. Application to account01/B19's first unproved implication

Account01/B19 narrows the STAR survivor to exact low-rank/double-anchor matrix structure on a physical cut. A tempting continuation is to compress a same-bank triple to a bounded joint density and then apply an arbitrary-joint coarea or moving-ridge estimate. The theorem above disproves precisely that continuation, even at a fixed target-admissible matrix: the joint cap can be one while the output density grows like \(\varepsilon^{-1}\).

Therefore the next valid implication must retain that \((E,Y,Z)\) are **linear images of mutually independent cap-one original coordinates**. It must use an original-product Brascamp--Lieb/Fourier inequality before replacing the bank by a generic joint density. This explains why the account01/B10 unnormalized ridge receiver succeeds for a bounded two-dimensional pair but does not automatically absorb the third same-bank longitudinal variable.

The current noncircular proof graph is:

- scalar/pair/ridge/volume/ruled exits: paid at their stated gates;
- strict N3 diffuse cross tail: paid;
- STAR higher-effective-rank branches: paid by D5, peer-tail, or D';
- remaining STAR: exact near-rank-one/near-rank-two or double-anchor grouped descent with product provenance;
- parallel TRIANGLE third-source coupling: open;
- arbitrary-extra-spectrum glue outside the certified exits: open.

The full conjecture remains open, so two end-to-end reviews are not yet requested.

## 4. Scope ledger

- No rotated random coordinates are declared independent.
- No moment, support, symmetry, iid, smoothness, or log-concavity assumption is added to the target.
- The construction is explicitly labeled as a barrier to an arbitrary-joint proof step, not as a target counterexample.
- Continuity of the original full theorem remains separate.
- No matrix tail is dropped as a random perturbation.
