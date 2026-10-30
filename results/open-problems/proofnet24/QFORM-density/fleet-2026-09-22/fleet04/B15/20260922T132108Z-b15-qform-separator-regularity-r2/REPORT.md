# fleet04/B15 — conditional separator smoothing for quadratic forms

**Run:** 20260922T132108Z-b15-qform-separator-regularity-r2  
**Programme:** QFORM-DENSITY-3EIG-20260922, control revision 2026-09-22.5  
**Assignment:** Absolute continuity and regularity  
**Classification:** TARGET-SUPPORTING-THEOREM / ESSENTIAL-STEP-APPLIED / FULL-TARGET-OPEN  
**Execution context:** WITHOUT_VERIFIED_BRAIN

## 1. Status and exact scope

The owner target asks for a universal finite constant \(C\) such that, for every dimension, every product input law with coordinate densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, the law of \(Q=X^TAX\) has density bounded by \(C\). The owner separately asks for a continuous representative.

The universal-constant conjecture remains open. This report proves a new continuity mechanism for a nontrivial original-coordinate separator branch. It strictly extends the block-direct-sum continuity theorem in the preceding fleet04/B15 report: both smoothing blocks may couple arbitrarily to a third block. The only required separator is that the two smoothing blocks do not couple directly to one another.

The completed assigned-partner theorem actually used is fleet01/B15:

- repository: yspennstate/math-open-problems
- commit: 47dc925729bbf269333cc6e1256178a538d2f553
- path: proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md

It gives affine-quadratic density bounds, uniform over all linear terms:
\[
 \|p\|_\infty\le \frac{2\pi+3\sqrt3}{\sigma_{\min}(B)}
 \quad (B\in\mathbb R^{3\times3}\text{ invertible symmetric}),
\]
and
\[
 \|p\|_\infty\le \frac{4\pi+8}{\sigma_{\min}(B)}
 \quad (B\in\mathbb R^{4\times4}\text{ invertible symmetric}).
\]
The present proof applies this result to an actual conditional inequality and then upgrades the mixture to a continuous density.

The fresh fleet01/B15 correction QFORM-LOCAL-CROSSBLOCK-DICHOTOMY-FALSE was also read before publication. Nothing below asserts that the present separator branch, a good principal block, and a high-rank cross block form an exhaustive dichotomy.

## 2. Two elementary regularity lemmas

### Lemma 2.1 — nonconstant affine quadratics are absolutely continuous

Let \(Y\) have a Lebesgue density on \(\mathbb R^m\), and let
\[
 P(y)=y^TDy+2\ell^Ty+c
\]
be nonconstant. Then \(P(Y)\) has an \(L^1\) density.

#### Proof

Choose a coordinate \(j\) on which \(P\) depends. Conditional on the other coordinates, \(P\) is a one-variable polynomial of degree one or two. If its quadratic coefficient is nonzero, it is nonconstant for every conditioning value. If the quadratic coefficient is zero, its linear coefficient is a nonzero affine function of the other coordinates except on a proper affine hyperplane, hence outside a Lebesgue-null set. A nonconstant one-variable affine or quadratic polynomial pulls one-dimensional null sets back to null sets. Fubini therefore shows that \(P(Y)\) charges no Lebesgue-null set. Its Radon–Nikodym derivative is an \(L^1\) probability density. \(\square\)

This is the affine version of the absolute-continuity theorem recorded in the preceding fleet04/B15 report. No density bound, moments, support condition, or independence among the coordinates of \(Y\) is needed once the joint density exists.

### Lemma 2.2 — conditional convolution smoothing

Let \(Z\) be any random element. Suppose that, conditional on \(Z=z\), random variables \(R_z,S_z\) are independent and:

1. \(R_z\) has a density \(p_z\) satisfying
   \[
   \|p_z\|_\infty\le C
   \tag{2.1}
   \]
   for almost every \(z\), with the same finite \(C\);
2. \(S_z\) has an \(L^1\) density \(g_z\) for almost every \(z\).

Let \(c(z)\) be measurable and set
\[
 T=R_Z+S_Z+c(Z).
\]
Then \(T\) has a density \(p_T\in C_0(\mathbb R)\), hence a bounded uniformly continuous density, and
\[
 \boxed{\|p_T\|_\infty\le C.}
 \tag{2.2}
\]

#### Proof

For almost every \(z\), the conditional density is
\[
 h_z(t)=(p_z*g_z)(t-c(z)).
\]
Young's inequality gives \(0\le h_z(t)\le C\).

We first verify \(h_z\in C_0(\mathbb R)\). Approximate \(g_z\) in \(L^1\) by \(\varphi_n\in C_c^\infty\). Since \(p_z\in L^1\),
\[
 p_z*\varphi_n\in C_0(\mathbb R).
\]
Moreover,
\[
 \|p_z*g_z-p_z*\varphi_n\|_\infty
 \le \|p_z\|_\infty\|g_z-\varphi_n\|_1\longrightarrow0.
\]
Thus \(p_z*g_z\), and hence \(h_z\), is a uniform limit of \(C_0\) functions.

Parameterized Radon–Nikodym disintegration supplies jointly measurable versions of the conditional densities, so
\[
 p_T(t)=\mathbb E[h_Z(t)]
 \tag{2.3}
\]
is a density of \(T\). If \(t_n\to t\), then \(h_z(t_n)\to h_z(t)\) for almost every \(z\), while \(|h_z(t_n)|\le C\). Dominated convergence applied to (2.3) proves continuity of \(p_T\). Likewise, \(h_z(t)\to0\) as \(|t|\to\infty\) for almost every \(z\), again dominated by \(C\), so \(p_T(t)\to0\). Therefore \(p_T\in C_0(\mathbb R)\), and (2.2) follows from (2.1). Every continuous function vanishing at infinity is uniformly continuous. \(\square\)

The point is that no common modulus of continuity for the conditional densities is required. The common height bound is enough for dominated convergence.

## 3. Main theorem: separator smoothing with arbitrary third-block couplings

Partition the original independent coordinate set as
\[
 [n]=I\sqcup J\sqcup K.
\]
After the corresponding coordinate permutation, write
\[
 A=
 \begin{pmatrix}
 B&0&E\\
 0&D&F\\
 E^T&F^T&G
 \end{pmatrix}.
 \tag{3.1}
\]
Here \(B=A_{I,I}\), \(D=A_{J,J}\), and the zero block means exactly \(A_{I,J}=0\). No restriction is imposed on \(E,F,G\).

For \(d\in\{3,4\}\), put
\[
 C_3=2\pi+3\sqrt3,\qquad C_4=4\pi+8.
\]

### Theorem 3.1 — QFORM-CONDITIONAL-SEPARATOR-SMOOTHING-v1

Assume:

1. \(|I|=d\in\{3,4\}\);
2. \(B\) is invertible;
3. the conditional \(J\)-polynomial is nonconstant for almost every \(X_K\), namely
   \[
   x_J\longmapsto x_J^TDx_J+2x_J^TFX_K
   \tag{3.2}
   \]
   is nonconstant almost surely.

Then for every independent input vector \(X\) whose coordinate densities are bounded by one, \(Q=X^TAX\) has a density
\[
 p_Q\in C_0(\mathbb R)
\]
and
\[
 \boxed{
 \|p_Q\|_\infty\le \frac{C_d}{\sigma_{\min}(B)}.
 }
 \tag{3.3}
\]
In particular, \(p_Q\) is uniformly continuous.

A simple purely algebraic sufficient condition for assumption 3 is
\[
 D\ne0\quad\text{or}\quad F\ne0.
 \tag{3.4}
\]

#### Proof

Condition on \(X_K=z\). Up to the additive constant \(z^TGz\), (3.1) gives
\[
 Q=
 \underbrace{X_I^TBX_I+2X_I^TEz}_{R_z}
 +
 \underbrace{X_J^TDX_J+2X_J^TFz}_{S_z}
 +
 z^TGz.
 \tag{3.5}
\]

Because the input law is a product in the original coordinates, \(X_I\) and \(X_J\) remain independent after conditioning on \(X_K=z\). The fleet01/B15 affine principal-block theorem applies to \(R_z\) for every \(z\), and the bound is independent of the linear term \(2E z\). Hence \(R_z\) has a density \(p_z\) satisfying
\[
 \|p_z\|_\infty
 \le \frac{C_d}{\sigma_{\min}(B)}
 \tag{3.6}
\]
uniformly in \(z\).

By assumption 3 and Lemma 2.1, \(S_z\) has an \(L^1\) density for almost every \(z\). Lemma 2.2, with the common constant from (3.6), now proves that the unconditional law of \(Q\) has a \(C_0\) density satisfying (3.3).

It remains only to justify the advertised sufficient condition. If \(D\ne0\), (3.2) has a nonzero quadratic part for every \(z\). If \(D=0\) and \(F\ne0\), then \(Fz\ne0\) outside the proper linear subspace \(\ker F\). The vector \(X_K\) has a joint Lebesgue density, so it gives that proper subspace probability zero. Thus (3.2) is nonconstant almost surely. \(\square\)

## 4. What the theorem adds

The preceding fleet04/B15 continuity branch required an original-coordinate direct sum
\[
 A=B\oplus D.
\]
Theorem 3.1 allows
\[
 E\ne0,\qquad F\ne0,\qquad G\ \text{arbitrary}.
\]
Thus both the bounded block and the smoothing block may be densely and indefinitely coupled to an arbitrarily large third block. Conditioning absorbs those couplings into linear terms, while the single separator \(A_{I,J}=0\) preserves conditional independence of the two summands.

The proof works for every sign pattern of \(B,D,G\), repeated eigenvalues, zero diagonal entries, and arbitrary unbounded or disconnected coordinate supports. It does not rotate the input variables and therefore never assumes independence in an eigenbasis.

The theorem also exposes a useful general principle:

> A uniform conditional \(L^\infty\) estimate plus an independent nonconstant conditional polynomial produces an unconditional \(C_0\) density with no loss in the height constant.

This is a genuine regularity upgrade. Bounded density alone does not imply a continuous representative, as the uniform law on an interval shows.

## 5. Application of the partner theorem to an actual interval bound

For every interval \(H\subset\mathbb R\), Theorem 3.1 yields
\[
 \Pr(Q\in H)
 =\int_Hp_Q(t)\,dt
 \le \frac{C_d}{\sigma_{\min}(B)}|H|.
 \tag{5.1}
\]
Thus the completed fleet01/B15 estimate is not merely cited: it enters the conditional inequality (3.6), survives convolution and mixing without loss, and gives both (3.3) and the small-ball bound (5.1).

For \(d=3\), the explicit constant is
\[
 \frac{2\pi+3\sqrt3}{\sigma_{\min}(B)}.
\]
For \(d=4\), it is
\[
 \frac{4\pi+8}{\sigma_{\min}(B)}.
\]

## 6. Sharp boundary of the mechanism

This theorem is not a proof of the owner target.

1. The bound still contains \(\sigma_{\min}(B)^{-1}\). A target matrix can have all physical \(3\times3\) and \(4\times4\) principal blocks badly conditioned even though it has three eigenvalues of magnitude at least one.
2. A fully dense matrix may admit no disjoint nonempty \(I,J\) with \(A_{I,J}=0\).
3. The fresh fleet01/B15 correction gives an explicit target family
   \[
   A_m=e_0e_0^T+u_mu_m^T-v_mv_m^T
   \]
   with the relevant local principal-block scale of order \(1/m\) and every physical cross block of rank at most two. Hence one cannot turn the present theorem into a universal proof by asserting a false “good local block or rank-three cut” dichotomy.
4. The diffuse separable-phase theorem is complementary: it handles a delocalized rank-\(r\) frame under a leverage hypothesis and arbitrary coordinate-separable perturbations. The unresolved global problem is a mixed localized/diffuse mechanism that covers matrices missed by both clean branches.

Accordingly the exact remaining implication is:

\[
 \boxed{\text{derive a universal conditional height bound without requiring a well-conditioned fixed principal block or an exact coordinate separator.}}
\]

Only after such an \(A\)-independent height estimate is found can Lemma 2.2 be used to upgrade regularity wherever an independent conditional smoothing component is available. For a completely dense form with no separator, continuity still requires a different target-level argument, such as locally uniform control of Steklov averages.

## 7. Correction and quantifier audit

- No Gaussianity, log-concavity, moment, compact-support, connected-support, or interval-support assumption is used.
- Independence is used only in the original coordinate partition.
- No rotation of the independent inputs is performed.
- No pointwise law-uniform van der Corput bound is invoked.
- No bounded projection theorem is used as a substitute for a quadratic pushforward bound.
- No universal constant is claimed.
- The new theorem proves a continuous bounded density only on the precise separator branch (3.1)–(3.4).
- The full conjecture remains OPEN / NOT PROVED / NOT DISPROVED.
- No novelty or publication-priority claim is made.
