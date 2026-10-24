# B19 / A094 independent review — dense-nullity-two tree payment

## Verdict

**INDEPENDENTLY ACCEPTED AT DECLARED SCOPE; NO REPAIR REQUIRED.**

The source claim `B05_A023_DENSE_NULLITY_TWO_TREE_v1`, read at canonical
commit `97ee31ccf5dd58017837d3939ffb012af1ed034f`, is correct:

Let $M\in\mathbb F_2^{s\times m}$ have rank $m-2$, let $D$ be any
Boolean function, and define

\[
P(x,y)=(-1)^{x^TMy+a\cdot x+b\cdot y+c}D(y).
\]

For every finite adaptive or pruned physical-coordinate restriction tree
on $P$, and every one common Boolean factor $h$ on a disjoint block,

\[
U(Ph)-\sum_\ell w_\ell U(P_\ell h)\le 2I(P).
\]

The bound is uniform in the physical orientation of the two-dimensional
kernel, dimension, affine phase, tree depth, reveal order, pruning, leaf
rarity, and the spectrum of $h$.

Full FEI remains **OPEN**.

## Independent reconstruction

Put $r=m-2$, $K=\ker M$, and let $Z$ be the set of zero physical
columns of $M$, with $k=|Z|\le2$. Fourier summation over the control
block splits the spectral law into $2^r$ equally weighted affine
$K$-fibres. If $E_\alpha$ is the Boolean two-bit fibre, then

\[
H(P)=2r+\mathbb E_\alpha H(E_\alpha).
\]

At least $r$ nonzero physical rows and all $m-k$ nonzero physical
columns contribute influence $1/2$. The zero-column contribution is

\[
J=\mathbb E_\alpha\sum_{j\in Z}\operatorname{Inf}_{e_j}(E_\alpha),
\qquad
I(P)\ge \frac r2+\frac{m-k}{2}+J.
\]

Every Boolean function on two bits is affine or bent. Consequently, for
the $k$ specified independent zero-column directions,

\[
H(E)\le2-k+2\sum_{j\in Z}\operatorname{Inf}_{e_j}(E).
\]

Because $m=r+2$, these identities give

\[
H(P)\le2r+2-k+2J\le2I(P),
\qquad U(P)\le H(P).
\]

This argument is in the original physical basis. Arbitrary affine phases
do not compromise it: spectral entropy is translation-invariant, while
the influence lower bounds remain valid (and can only gain contributions
from affine characters on zero rows or columns).

For a restriction tree, the exact signed node charges telescope:

\[
\sum_vw_v\Delta_vU
=U(Ph)-\sum_\ell w_\ell U(P_\ell h).
\]

Disjoint tensor additivity gives $U(P_vh)=U(P_v)+U(h)$, so the common
terminal packet cancels once. Nonnegativity of every leaf $U(P_\ell)$
then yields the advertised bound from the root reservoir. Independently,
the usual first-query influence telescope gives the stronger signed form

\[
\sum_vw_v\Delta_vU
\le2\sum_vw_v\operatorname{Inf}_{i_v}(P_v)
+\sum_\ell w_\ell\bigl(2I(P_\ell)-U(P_\ell)\bigr).
\]

The last bracket is genuinely signed. The proof does not assume that every
descendant satisfies the root coefficient-two certificate.

## Boundary and ordering challenge

For

\[
M=\begin{pmatrix}1&1&0&0\\0&0&1&0\end{pmatrix},
\qquad D(y)=-1\Longleftrightarrow y_1=y_3=y_4=0,
\]

fixing the second control deletes a rank-essential row and creates a
nullity-three child. Independent reconstruction gives

\[
H-2I=-\frac14+\frac9{16}\log_2\frac{16}{9}
=0.216917186688700\ldots>0.
\]

Thus a control-first proof cannot repeatedly invoke the root lemma. This
does not damage the stated theorem because its complete signed ledger is
paid once from the root. Data-only restrictions preserve nullity at most
two; control-first and data-first trees have different local charges but
the same endpoint telescope.

## Independent computation

`INDEPENDENT_CHECK.py` was written without importing the source checker.
It passed:

- all 64 two-bit directional-fibre inequalities;
- 14,336 rank-one $m=3$ root cases: every physical orientation, every
  Boolean core modulo output complement, and every affine phase $a,b$;
- all 210 rank-two $2\times4$ physical orientations, with 2,100
  independently sampled affine/core instances and adaptive/pruned trees;
- 2,100 exact first-query influence telescopes;
- 200 common-disjoint-core cancellation checks;
- the exact nullity-three boundary reconstruction above.

The largest observed $U/I$ was $1$, including the affine-phase
exhaustion. This supports but does not prove the separate open conjecture
$U(P)\le I(P)$ for the class.

## Scope guard and literature overlap

The accepted theorem has exactly one common disjoint terminal factor and
queries only coordinates of the fixed root shield. It does **not** cover:

- a leaf-dependent or newly introduced core;
- a core sharing physical variables with the shield;
- queries of the terminal factor;
- a dimension-uniform nullity bound; or
- a nodewise nonnegative or locally reissuable coefficient-two payment.

Potapov's plateaued-function theorem covers the flat/plateaued FEI
endpoint, not arbitrary unequal four-point fibre spectra or this retained-
$U$ tree endpoint. O'Donnell--Tan's composition theorem assumes disjoint
inner input blocks; it does not transfer the result to a shared-variable or
changing-core hierarchy. No novelty claim beyond the stated retained-
$U$, dense-nullity-two class is accepted.

Primary sources:

- V. N. Potapov, *On the Fourier Entropy-Influence Conjecture for Boolean
  Plateaued Functions*, arXiv:2609.21563 (18 September 2026).
- R. O'Donnell and L.-Y. Tan, *A composition theorem for the Fourier
  Entropy-Influence conjecture*, arXiv:1304.1347 (4 April 2013).

## Status and next unpaid step

`B05_A023_DENSE_NULLITY_TWO_TREE_v1` and its terminal-ledger corollary are
accepted by A094 at their declared scope. The sharper constant-one root
bound remains open. The universal unpaid step is a dimension-free payment
for higher-nullity, changing coherent cores across an arbitrary hierarchy.
No conclusion about full FEI follows.

