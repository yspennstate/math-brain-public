# A091 independent review of B09 product-biased restriction uncertainty

## Verdict

The main auxiliary theorem `B09-BIASED-BLOCK-UNCERTAINTY-01` is **ACCEPTED**
at its exact product-biased physical-restriction scope:

\[
0\le J_A\le M_A+\Delta_A(p),\qquad
L_A=M_A+J_A,
\]
where
\[
\Delta_A(p)=\sum_{i\in A}
\bigl[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\bigr].
\]

The repaired two-bit certificate is accepted only as the already source-bound
finite helper refutation `J_A\le M_A`; it is not an FEI counterexample.

The broad composition prose in section 5 of the source report is **not
accepted as a theorem**.  Exact additivity is proved for disjoint tensor
products with aligned revealed blocks.  O'Donnell--Tan proves a different
composition statement for biased `FEI+`; it does not, without an additional
interface lemma, make the present `M,J,Delta` charge telescope through every
Boolean composition node.

Finally, the source report's endpoint conclusion can be repaired, but the
repair below is new mathematics contributed during review and therefore needs
a fresh A085/A090 review.  For the genuine two-bit AND sign gate,

\[
J_{\{X\}}-M_{\{X\}}
=\bigl(4q(1-2q)+o(1)\bigr)p\log_2(1/p)
\]

as `p=P(X=1)->0` with fixed `q=P(Y=1)<1/2`.  At `q=1/4`, the leading
coefficient is `1/2`.  Thus a universal `O(p)` correction really is
impossible, now by a lower-bound Boolean family rather than by the asymptotic
size of an upper bound.

Full uniform-cube FEI remains **OPEN**.

## 1. Sources and independence

Reviewed original:

- canonical B09 report, commit
  `adb671ffcda143fa68347806bb96e8c305621a7d`, report blob
  `71b68e4decf9658a42fef6bb2668e19f25bd214a`;
- corrected finite certificate, current report blob
  `c3adb486c8ca9f7a35f384ee82942eef66bd64be`, checker blob
  `0a6917feb25ab0e1cc0703c4c134b299c6e3243f`, and output blob
  `d3db5bd09e009eb3f4f4d3572ccba9b6e6ce3239`;
- B19 contract blob `ee688080aba90acd2daed1b26e809e38285dcb85`.

Primary comparison:

- R. O'Donnell and L.-Y. Tan, *A composition theorem for the Fourier
  Entropy-Influence conjecture*, arXiv:1304.1347.  Theorem 1 composes biased
  `FEI+` for disjoint inner variable sets and an outer gate evaluated at the
  induced biases.  Proposition 3.2 supplies its entropy/influence formulas.
- H. Maassen and J. B. M. Uffink, *Generalized entropic uncertainty
  relations*, Phys. Rev. Lett. 60 (1988), 1103--1106.  The invoked finite
  orthogonal-basis inequality is `H(a^2)+H((Ua)^2)>=-2 log_2 c` with
  `c=max |U_{ij}|`.

The original finite certificate was not rerun as new work.  Its repaired
signed-interval conclusion is reused at its already established scope.  The
main theorem below was reconstructed directly.  No contributor to the original
B09 theorem supplied this review.

## 2. Independent reconstruction of the exact ledger

Let `X` have an interior product law on `{0,1}^n`, with
`P(X_i=1)=p_i`.  Use the orthonormal coordinates

\[
\phi_i(0)=-\sqrt{p_i/(1-p_i)},\qquad
\phi_i(1)=\sqrt{(1-p_i)/p_i}.
\]

For a Boolean `f`, put `mu(S)=hat f_p(S)^2`.  Split the coordinates into a
revealed block `A` and residual block `B`.  For a residual spectral label `T`,

\[
q_T=\sum_{R\subseteq A}\widehat f_p(R\cup T)^2.
\]

For a physical assignment `z` on `A`, biased Fourier inversion on the revealed
coordinates gives

\[
\widehat{f_z}_{p_B}(T)
=\sum_{R\subseteq A}\widehat f_p(R\cup T)\phi_R(z).
\]

Orthogonality therefore implies

\[
q_T=\mathbb E_z\widehat{f_z}_{p_B}(T)^2.
\]

Thus, if `Z` is the physical branch and `T` is sampled from the child spectral
law, the marginal law of `T` is exactly the parent residual marginal.  Hence

\[
J_A=I(Z;T)\ge0,
\]

and the entropy chain rule gives

\[
L_A=M_A+J_A.
\]

This checks normalization, branch probabilities, zero masses, and signs.  No
Boolean-specific inequality is hidden in this identity.

## 3. Independent reconstruction of the uncertainty payment

Fix `T` with `q_T>0` and set

\[
a_R={\widehat f_p(R\cup T)\over\sqrt{q_T}},\qquad
b_z={\sqrt{\mu_{p_A}(z)}\widehat{f_z}_{p_B}(T)\over\sqrt{q_T}}.
\]

Then `a` and `b` are unit vectors and `b=U_Aa`, where

\[
U_A=\bigotimes_{i\in A}
\begin{pmatrix}
\sqrt{1-p_i}&-\sqrt{p_i}\\
\sqrt{p_i}&\sqrt{1-p_i}
\end{pmatrix}.
\]

The maximum entry is

\[
c_A=\prod_{i\in A}\sqrt{\max(p_i,1-p_i)}.
\]

Maassen--Uffink gives

\[
H(a^2)+H(b^2)\ge
-\sum_{i\in A}\log_2\max(p_i,1-p_i).
\]

Averaging with weights `q_T` identifies the two entropies as `M_A` and
`H(Z|T)`.  Since `H(Z)=sum_i h_2(p_i)` and
`J_A=H(Z)-H(Z|T)`, rearrangement yields exactly

\[
J_A\le M_A+\Delta_A(p).
\]

All quantifiers in the source theorem are therefore justified.  The argument
also covers degenerate fibers by omitting `q_T=0`; interior coordinate biases
are necessary only to write the normalized one-bit basis without endpoint
conventions.

## 4. Reviewer-contributed endpoint lower bound

Let

\[
g(X,Y)=(-1)^{XY},\qquad P(X=1)=p,\quad P(Y=1)=q,
\]

and reveal `A={X}`.  Direct biased Fourier calculation gives the squared
masses, ordered as `empty,{X},{Y},{X,Y}`:

\[
\begin{aligned}
\mu_\emptyset&=(1-2pq)^2,\\
\mu_X&=4q^2p(1-p),\\
\mu_Y&=4p^2q(1-q),\\
\mu_{XY}&=4p(1-p)q(1-q).
\end{aligned}
\tag{4.1}
\]

Write `a=4q(1-q)` and `b=4q^2`.  The residual spectral bit has nonempty mass
`ap`.  The `X=0` child is constant; the `X=1` child has spectral entropy
`h_2(a)`.  Therefore the exact formulas are

\[
M=H(\mu)-h_2(ap),\qquad
J=h_2(ap)-p h_2(a).
\tag{4.2}
\]

For fixed `q in (0,1)`,

\[
h_2(cp)=cp\log_2(1/p)+O(p)
\]

for fixed `c>0`.  In (4.1), the two order-`p` nonconstant masses have
coefficients `a` and `b`; the `Y` singleton is order `p^2`, while the constant
mass contributes only `O(p)`.  Consequently

\[
H(\mu)=(a+b)p\log_2(1/p)+O(p),
\]

and (4.2) yields

\[
M=bp\log_2(1/p)+O(p),\qquad
J=ap\log_2(1/p)+O(p).
\]

Hence

\[
J-M=4q(1-2q)p\log_2(1/p)+O(p).
\tag{4.3}
\]

For every fixed `0<q<1/2`, this is a positive lower bound.  At `q=1/4`,

\[
J-M=\left({1\over2}+o(1)\right)p\log_2(1/p).
\tag{4.4}
\]

Thus any correction `R(p)` satisfying `J<=M+R(p)` for all genuine Boolean
gates must have

\[
\limsup_{p\downarrow0}{R(p)\over p\log_2(1/p)}\ge {1\over2}.
\]

Since the proved `Delta(p)` has leading coefficient `1`, its endpoint order is
sharp and its coefficient is within a factor two of this explicit lower bound.
The optimal universal coefficient remains open.

Because this lower-bound family and asymptotic proof were added by this
reviewer, claim (4.3)--(4.4) is `AUTHOR_PROVED_PENDING_FRESH_REVIEW`, not an
independently accepted source claim.

## 5. Composition scope

For an exact product `f=f_1 f_2` on disjoint variable sets and an aligned block
`A=A_1 disjoint_union A_2`, the spectral law and physical posterior channel
are products.  Therefore

\[
(M,J,L,\Delta)_f=(M,J,L,\Delta)_{f_1}+(M,J,L,\Delta)_{f_2}.
\]

This exact tensor statement is accepted and independently checked.

For a general disjoint Boolean composition

\[
f=F(g_1(x^1),\ldots,g_k(x^k)),
\]

O'Donnell--Tan's Theorem 1 applies to their biased `FEI+` functional under
disjointness and appropriate gate/child hypotheses.  Their Proposition 3.2
uses the partition of Fourier support supplied by normalized, mean-zero inner
functions.  The B09 report does not give an interface expressing its physical
restriction channel `M,J,Delta` as that `FEI+` cocycle, nor a proof that the tax
is paid only once along a composition tree.  Therefore the report's statement
that decomposable gates create no new violation “beyond their factors” is
accepted only for exact tensor products, not for arbitrary Boolean
composition.

Shared variables are outside both the exact tensor statement and the cited
O'Donnell--Tan theorem.

## 6. Independent checks and remaining gap

`CHECK.py` independently enumerates every Boolean truth table through three
variables at three nonuniform product-bias vectors and every nonempty revealed
block.  It verifies 5,643 ledger, uncertainty, tensor, and endpoint assertions.
It also checks the exact-product additivity interface and the convergence in
(4.4).  The maximum ledger residual is `6.661e-16`; the largest observed
uncertainty-bound residual is negative.  These finite checks support, but do
not replace, the analytic proof.

The first unpaid universal step is not the main B09 lemma.  It is a
dimension-independent, single-use payment of the actual `M_A` plus endpoint
tax through an arbitrary hierarchy, with explicit handling of changing gates,
address reuse, and shared physical variables.

