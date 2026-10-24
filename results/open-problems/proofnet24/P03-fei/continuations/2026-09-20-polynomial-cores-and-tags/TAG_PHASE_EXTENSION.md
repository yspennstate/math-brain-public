# Polynomial tag phases and constant-preserving affine-fibre gluing

20 September 2026. This note builds on `REPORT.md` and a concurrent repository continuation. Unrestricted FEI remains unproved.

## 1. New input from the concurrent continuation

The current repository report

`proofnet24/P03-fei/continuations/2026-09-20-affine-fibres/REPORT.md`

has blob `29d8afcabc09ee1564a1e0db51cf42a21ffa804d`. Its Sections 1–9 were read, including the complete proofs used here. It proves the following stronger-than-total-influence untwisted gluing bound.

Let the **existing physical coordinates** be \((x,y)\in\mathbb F_2^k\times\mathbb F_2^m\), let every nonempty fibre of \(\pi:\mathbb F_2^m\to\mathbb F_2^k\) be affine, and set

\[
F(x,y)=(-1)^{x\cdot\pi(y)}g(y).
\]

For each fibre, decompose its tangent space into the span of the physical standard coordinate vectors tangent to the fibre and an arbitrary complementary subspace. Fixing the complementary parameters gives Boolean sections in those physical coordinate axes. If every such section has a certificate \(H\le C_0J\), then

\[
H(F)\le K_0J_y(F),\qquad K_0=\max\{4,C_0\}.
\tag{1.1}
\]

Here \(J_y\) counts only the original \(y\) coordinates. The report then permits quadratic phases on the tag coordinates \(x\). Its affine-fibre identity, boundary payment, and the quadratic extension are **prior repository results**, not new assertions of this note.

We extend that last operation from quadratic to arbitrary polynomial tag phases. The stronger payment in (1.1), which reserves the tag influences, is essential.

## 2. An exact phase-comparison identity

Use the notation of the main report: \(S^f\) has squared Fourier law, \(j_i(f)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}\), and entropy is in bits.

**Lemma 2.1.** Let \(f\) be any Boolean function, fix a coordinate set \(E\), and let \(\sigma\) be any Boolean function of \(x_E\) only. Put \(g=\sigma f\), \(R=E^c\). Then

\[
\boxed{
H(g)-H(f)=H(S_E^g\mid S_R^g)-H(S_E^f\mid S_R^f).
}
\tag{2.1}
\]

In particular,

\[
\boxed{H(g)\le H(f)+\sum_{i\in E}h_2(j_i(g)).}
\tag{2.2}
\]

**Proof.** For every physical assignment \(x_E=z\), the two restrictions satisfy \(g_z=\sigma(z)f_z\). Their squared Fourier laws therefore agree exactly. Partial Parseval implies equality of the marginal laws of \(S_R^g\) and \(S_R^f\). Subtract the two entropy chain rules to obtain (2.1). Nonnegativity of the second conditional entropy and conditional subadditivity give (2.2). QED.

Equivalently, both the physical-label mutual information and the average leaf entropy in the main report's fixed-block identity cancel. There is **no Jensen–Shannon remainder** in this comparison. This statement is not entropy subadditivity under arbitrary multiplication on shared variables: the right side involves the final function's coordinate marginals, not the Fourier entropy of \(\sigma\).

## 3. Polynomial tag theorem

The following applies to an arbitrary label map, not just affine fibres, provided its base function has the stronger certificate stated in the hypothesis.

**Theorem 3.1.** Suppose

\[
F(x,y)=(-1)^{x\cdot\pi(y)}g(y),\qquad H(F)\le K_0J_y(F).
\]

Let \(Q\) be a polynomial on \(x\) over \(\mathbb F_2\), of degree at most \(r\ge2\). Then

\[
\boxed{
H((-1)^QF)\le \max\{K_0,\phi(r-1)\}\,J((-1)^QF),
\quad \phi(s)=2^s h_2(2^{-s}).
}
\tag{3.1}
\]

An affine \(Q\) preserves entropy and folded influence, so only the coefficient \(K_0\) is needed in that case.

**Proof.** Remove the affine part of \(Q\), which only multiplies by a character and does not change the entropy or any folded influence. Let \(T\) be the tag coordinates appearing in a nonlinear monomial of the remaining \(Q\). The phase now depends only on \(x_T\).

Write \(F_Q=(-1)^QF\). Along a tag coordinate \(i\in T\), the multiplicative derivative is

\[
F_Q(x,y)F_Q(x+e_i,y)=(-1)^{\partial_iQ(x)}(-1)^{\pi_i(y)}.
\]

The two factors depend on independent groups of uniform variables. Therefore, setting \(a_i=\mathbb E_x(-1)^{\partial_iQ(x)}\) and \(b_i=\mathbb E_y(-1)^{\pi_i(y)}\),

\[
1-2\operatorname{Inf}_{x_i}(F_Q)=a_i b_i,
\qquad
j_{x_i}(F_Q)=\frac{1-|a_ib_i|}{2}\ge\frac{1-|a_i|}{2}.
\tag{3.2}
\]

The polynomial \(\partial_iQ\) is nonconstant and has degree \(s_i\le r-1\). Both it and its complement are nonzero polynomials of degree at most \(s_i\). The elementary minimum-weight bound gives

\[
\boxed{j_{x_i}(F_Q)\ge 2^{-s_i}\ge2^{1-r}.}
\tag{3.3}
\]

Every \(y\)-derivative is unchanged by the tag phase, hence \(J_y(F_Q)=J_y(F)\). Apply Lemma 2.1 with \(E=T\), and use the decrease of \(h_2(q)/q\):

\[
\begin{aligned}
H(F_Q)
&\le H(F)+\sum_{i\in T}h_2(j_{x_i}(F_Q))\\
&\le K_0J_y(F_Q)+\sum_{i\in T}\phi(s_i)j_{x_i}(F_Q)\\
&\le K_0J_y(F_Q)+\phi(r-1)J_x(F_Q)\\
&\le\max\{K_0,\phi(r-1)\}J(F_Q).
\end{aligned}
\tag{3.4}
\]

QED. The middle line is a stronger derivative-degree-weighted version of the theorem.

The proof imposes no rank, sparsity, or disjoint-support condition on the polynomial's terms. It does not require a character-valued polynomial derivative. It does require that the phase depends only on existing tag coordinates, not arbitrarily on mixed tag/data variables.

## 4. Consequences for affine-fibre gluing

Combine (1.1) and Theorem 3.1.

**Corollary 4.1.** Under the affine-fibre and physical-section hypotheses in Section 1,

\[
\boxed{
H\!\left((-1)^{Q(x)+x\cdot\pi(y)}g(y)\right)
\le \max\{4,C_0,\phi(r-1)\}\,J\!\left((-1)^{Q(x)+x\cdot\pi(y)}g(y)\right).
}
\tag{4.1}
\]

This is a direct extension of the concurrent quadratic-tag theorem.

**Sharp constant four with cubic tag phases.** If every physical section is quadratic, then its certificate is \(C_0=2\). For an arbitrary cubic tag polynomial, \(r\le3\),

\[
\phi(2)=4h_2(1/4)=3.245112\ldots<4.
\]

Consequently the coefficient remains exactly **four**. It is sharp over the stated class because ordinary addressing functions, with \(Q=0\), have \(H/I\to4\). The sharpness example is the prior report's standard addressing example; it is not a new construction.

**Constant 12.04 with high-degree cores and degree-eleven tags.** The main report certifies arbitrary degree-at-most-seven couplings of independently supported symmetric cores with coefficient 12.04, with no number-of-cores penalty. Such functions may be used as the required physical sections. Since

\[
\phi(10)=11.441990\ldots<12.04,
\]

every tag phase of degree at most **eleven** preserves the coefficient 12.04. More generally the same statement holds with \(12.04+\log_2d_*\) when each section uses cores with at most \(d_*\) symmetry parts.

The symmetry cores may themselves have arbitrary algebraic degree. Different fibres may use different sections on overlapping ambient coordinate sets. The theorem does not assume that the fibre branches are independent.

**Recursive closure.** Affine-fibre gluing can be repeated at arbitrary finite depth, with a polynomial tag phase of degree at most eleven at each step, whenever every required physical section has already been certified with the same coefficient \(12.04+\log_2d_*\). The coefficient remains unchanged: (4.1) maps it to its maximum with two smaller constants. Disjoint products may be interleaved, by exact additivity of \(H\) and \(J\). This is an induction on a valid finite construction, not a claim that every Boolean function has such a construction.

The same reasoning preserves coefficient four at arbitrary finite depth with cubic tag phases and sections already certified with coefficient four.

## 5. Scope and the surviving full-problem gap

The result addresses a specific interaction between independent physical tag and data groups. Appending tags to an unknown function changes the function; fixing them can merge labels and destroy the affine-fibre representation. Nothing here proves that arbitrary Boolean functions admit the required representation with certified sections. Arbitrary mixed polynomial phases on \((x,y)\) are not included.

For an unrestricted phase, Lemma 2.1 is exact but its marginal entropy upper bound need not be payable by a universal multiple of influence. The derivative gap in (3.3) depends on degree, and the initial base certificate must reserve the tag influences as in (1.1). Neither condition is free in a proposed universal reduction.

Thus this is a new restricted closure theorem, not a solution of full FEI. The universal erasure/allocation inequality in Section 9 of the main report remains unpaid. Independent review, formal verification, and publication-priority clearance are not claimed.

## 6. Reproduction and attribution

Run `python3 verify_tag_phase.py --output tag_phase_verification.json` in the folder containing `verify_polynomial_symmetry.py`. The latter supplies the exact integer Walsh and prime-log arithmetic; it is reused explicitly.

The checker tests the phase-comparison identity for every Boolean function, every coordinate subset, and every phase on that subset through dimension three. It also tests affine-fibre examples with quadratic or polynomially coupled symmetric sections, exact tag derivative factorizations and degree gaps, and the source-facing constants. Large-dimensional assertions and recursive closure rely on the proofs, not finite sampling. `tag_phase_verification.json` records the actual coverage and source hashes.

The affine-fibre identity, physical boundary payment, and base bound (1.1) are credited to the concurrent report, blob `29d8afcabc09ee1564a1e0db51cf42a21ffa804d`. The factor-count-free polynomial-core certificate is Theorem 2.1 of the main report. New in this note are their phase-comparison synthesis, the general polynomial tag extension, and its unchanged-constant cubic and degree-eleven regimes. Basic minimum-distance and entropy identities are standard; comprehensive external novelty has not been established.
