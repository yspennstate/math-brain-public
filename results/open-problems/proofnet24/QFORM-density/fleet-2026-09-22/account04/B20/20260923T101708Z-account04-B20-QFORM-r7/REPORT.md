SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B20, 2026-09-23T10:17:08Z.
attacking: the anchored mixed-volume receiver at its complementary rank-one/no-leakage endpoint.

# Disjoint-bank square-hyperbola receiver and proof-graph update

**Run:** `20260923T101708Z-account04-B20-QFORM-r7`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN`

## 1. Sources and correction gates

Fresh brain source: `yspennstate/math-research-brain@17b89297d3120baf4efe2e668f654438d64846a7`.

The newest account01/B20 theorem used here is:

- `yspennstate/math-open-problems@c45a270dbf4a4d81742bc934ff54eba97d81f4f3`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260923T0919Z-account01-B20-QFORM-auto11/REPORT.md`.

It proves that in the exact-rank-three heavy-row survivor there is a physical anchor \(h\) and a partition of the remaining original coordinates \(U\sqcup V\) for which the normalized transverse Grams satisfy
\[
H_U+H_V=I_2,\qquad
{\cal M}(H_U,H_V)
=\sum_{i\in U,j\in V}\det(b_i,b_j)^2\ge \frac12.                 \tag{1.1}
\]
Equivalently the anchored physical third-volume is at least \(c_h/2>1/4\).
The unresolved implication in that report is an analytic receiver which spends this aggregate before selecting a reciprocal minor.

The analytic input actually applied below is account01/B06's weighted-section theorem:

- `yspennstate/math-open-problems@71e76e50e036242aaa91584f0f2406456963ebb0`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T035013Z-qform-r22-b06/REPORT.md`.

For \(X\) independent of \((Y,Z)\), with \(X\) density-capped by one, it proves
\[
\|p_Q\|_\infty\le \frac{4\sqrt{LK}}{\sqrt{|ad|}}                 \tag{1.2}
\]
for
\[
Q=aX^2+2bXY+cY^2+2dYZ+\hbox{affine},
\]
provided \(p_Y\le L\) and the conditional density of \(Z\mid Y\) is capped by \(K\).
No normalized worst-fiber supremum is used in its proof: section mass and section height are retained through the singular square kernel.

The following argument uses only disjoint original-coordinate banks. It does not assert independence after rotation, does not use arbitrary-joint coarea, and does not infer a single good minor from (1.1).

## 2. New theorem

### Theorem `QFORM-DISJOINT-BANK-SQUARE-HYPERBOLA-v1`

Let \(B,C\) be disjoint sets of original coordinates, disjoint also from \(0\). Let
\[
Y=\sum_{i\in B}u_iX_i,\qquad Z=\sum_{j\in C}v_jX_j,
\qquad \sigma=\|u\|_2>0,\quad \tau=\|v\|_2>0,
\]
where all \(X_i\) are independent and have probability densities bounded by one.
For \(a,d\ne0\) and arbitrary real affine coefficients, put
\[
Q=aX_0^2+2dYZ+rX_0+sY+\ell Z+q_0.                                  \tag{2.1}
\]
Then \(Q\) has an essentially bounded density and
\[
\boxed{\displaystyle
 \|p_Q\|_\infty
 \le {4\sqrt e\over\sqrt{|ad|\,\sigma\tau}}.}                       \tag{2.2}
\]
The same estimate holds after adding any independent random remainder supported on further disjoint original coordinates.

If
\[
|a|\ge1,\qquad |d|\,\sigma\tau\ge1,                                 \tag{2.3}
\]
then the active quadratic matrix has eigenvalues
\[
\{a,\ d\sigma\tau,\ -d\sigma\tau\},                                 \tag{2.4}
\]
so it satisfies the original three-large-eigenvalue hypothesis and
\[
\boxed{\|p_Q\|_\infty\le4\sqrt e=6.5948850828\ldots .}              \tag{2.5}
\]

Using the sharp one-dimensional projection cap
\(\|p_{\sum u_iX_i}\|_\infty\le\sqrt2/\|u\|_2\), (2.2) improves to
\(4\sqrt2/\sqrt{|ad|\sigma\tau}\). The conservative \(4\sqrt e\)
version (2.2) uses only the already source-pinned projection theorem in
account01/B06.

### Proof

Because \(B,C,\{0\}\) are disjoint original-coordinate sets,
\(X_0,Y,Z\) are genuinely independent. The physical projection theorem
used in account01/B06 gives
\[
\|p_Y\|_\infty\le{\sqrt e\over\sigma}=:L,\qquad
\|p_Z\|_\infty\le{\sqrt e\over\tau}=:K.                              \tag{2.6}
\]
Since \(Y\) and \(Z\) are independent, the conditional density of
\(Z\mid Y=y\) equals \(p_Z\) for almost every \(y\); hence it has the
same cap \(K\). Apply (1.2) with \(b=c=0\):
\[
\|p_Q\|_\infty
 \le {4\sqrt{LK}\over\sqrt{|ad|}}
 \le {4\sqrt e\over\sqrt{|ad|\sigma\tau}},
\]
which is (2.2).

Normalize the two bank directions to \(u/\sigma\) and \(v/\tau\).
In the orthonormal active source basis
\((e_0,u/\sigma,v/\tau)\), the quadratic matrix is
\[
\begin{pmatrix}
a&0&0\\
0&0&d\sigma\tau\\
0&d\sigma\tau&0
\end{pmatrix}.
\]
This proves (2.4), and (2.3) inserted into (2.2) gives (2.5).
Finally, convolution with an independent remainder cannot increase an
essential density supremum. QED.

## 3. Actual application to the account01/B20 frontier

In the complementary rank-one endpoint of (1.1),
\[
H_U=ee^T,\qquad H_V=ff^T,\qquad e\perp f,                             \tag{3.1}
\]
so
\[
{\cal M}(H_U,H_V)=1\ge\frac12.                                       \tag{3.2}
\]
When the anchored exact-rank-three quadratic has no same-bank quadratic
leakage and its only transverse interaction is the \(U\)-\(V\)
hyperbolic term, the two transverse aggregates have coefficient norms
\(\sigma=\tau=1\). The heavy anchor supplies the independent original
scalar \(X_h\). Thus (2.1) is exactly the analytic receiver for this
endpoint. At the normalized target scale \(|a|\ge1,|d|\ge1\),
\[
\boxed{\|p_Q\|_\infty\le4\sqrt e<6.595.}                              \tag{3.3}
\]
This spends the account01/B20 mixed-volume state at an actual
target-level inequality. It is stronger than merely observing a
large aggregate determinant: the original product provenance is kept
until the weighted singular section is integrated.

## 4. Compact noncircular proof graph

The currently compatible graph is:

1. Diffuse/ridge/volume branches are paid only under their stated
   leverage, marginal, and tail gates.
2. Exact-rank-three one-sheet indefinite output is paid by the ruled
   identity; it does not pay the convex/two-sheet side.
3. Non-near-null heavy-hub states with a quantitative third source are
   paid by the mixed-Fresnel theorem.
4. The heavy-row residual always admits the account01/B20 anchored
   mixed-volume cut (1.1).
5. The new theorem pays the complementary rank-one, no-same-bank-leakage
   endpoint of node 4 with the explicit target constant \(4\sqrt e\).
6. The first remaining exact-rank-three implication is the same
   anchored receiver with arbitrary same-bank longitudinal/transverse
   contamination. Its pair \((Y,Z)\) is then dependent within a
   physical bank, so (2.6) cannot be promoted to a conditional cap.
7. The punctured convex/two-sheet near-null collar and interaction with
   arbitrary additional spectrum remain separate open nodes.

Therefore this is not a full candidate proof. Two end-to-end reviews
are not requested, because nodes 6 and 7 remain unproved. Continuity is
also not claimed here.

## 5. Scope audit

- Arbitrary cap-one one-dimensional input laws are retained.
- No moment, support, iid, symmetry, or regularity assumption is added.
- No independence after spectral rotation is used.
- No arbitrary-dependent-pair coarea estimate is used.
- No worst conditional-density supremum is used.
- Full universal QFORM conjecture: **OPEN**.
- New target-level structured branch: **PROVED**.
