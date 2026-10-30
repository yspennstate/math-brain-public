# Quadratic-seed transfer for the upper-set functional

## Definitions

For a Boolean function `f` on a finite coordinate set, put

\[
p_f(S)=\widehat f(S)^2,\qquad
\pi_f(S)=\sum_{T\supseteq S}p_f(T),\qquad
U(f)=\sum_Sp_f(S)\log_2\frac{\pi_f(S)}{p_f(S)}.
\]

Write

\[
G(f)=\sum_i\left(U(f)-\frac{U(f_{i=1})+U(f_{i=-1})}{2}\right).
\]

All products below use disjoint physical coordinate blocks. A quadratic phase is
`q(x)=(-1)^{Q(x)}` with `deg_F2 Q <= 2`.

## Lemma 1: exact tensor identities (PROVED)

For arbitrary Boolean `f` and `g` on disjoint blocks,

\[
U(fg)=U(f)+U(g),\quad H(fg)=H(f)+H(g),\quad
I(fg)=I(f)+I(g),\quad G(fg)=G(f)+G(g).
\]

### Proof

The Fourier coefficient of the product at `A cup B` is
`hat f(A) hat g(B)`. Hence

\[
p_{fg}(A\cup B)=p_f(A)p_g(B)
\]

and the upper cap factors:

\[
\pi_{fg}(A\cup B)
=\sum_{A'\supseteq A,\,B'\supseteq B}p_f(A')p_g(B')
=\pi_f(A)\pi_g(B).
\]

Substitution gives additivity of `U`; the usual product-distribution argument
gives additivity of `H`, and Fourier level additivity gives additivity of `I`.
If coordinate `i` is in the `f` block, then

\[
U(fg)-\mathbb E_{x_i}U((fg)_{x_i})
=U(f)-\mathbb E_{x_i}U(f_{x_i}),
\]

because the `U(g)` terms cancel. The analogous statement holds in the `g`
block, proving additivity of `G`.

## Theorem 2: GU' transfer through an arbitrary quadratic block (PROVED)

Let `C` be a restriction-closed Boolean class satisfying, for fixed constants
`a < infinity` and `0 <= b < 1`,

\[
G(g)\le aI(g)+bU(g)\qquad(g\in C).
\]

Then the restriction-closed class

\[
\mathcal Q\otimes C=\{qg:q\text{ is an arbitrary-dimensional quadratic
phase and }g\in C\}
\]

satisfies

\[
G(qg)\le \max\{3,a\}I(qg)+bU(qg).
\]

Thus quadratic multiplication preserves the strict contraction coefficient
`b` exactly, with no dependence on quadratic dimension, rank, interaction
graph, or number of overlapping quadratic monomials.

### Proof

Restrictions of a quadratic phase remain quadratic phases, and restrictions
of `g` remain in `C`, so the product class is restriction closed. The accepted
quadratic theorem gives `G(q) <= 3I(q)`. Lemma 1 and the hypothesis give

\[
\begin{aligned}
G(qg)&=G(q)+G(g)\\
&\le 3I(q)+aI(g)+bU(g)\\
&\le \max\{3,a\}(I(q)+I(g))+b(U(q)+U(g)),
\end{aligned}
\]

where the final step uses `bU(q) >= 0`. Lemma 1 identifies the last line with
the claimed bound.

This theorem is a transfer mechanism, not a universal payment: it does not
control the seed `g`.

## Theorem 3: an expanding restriction-closed class (PROVED)

Let `B_k` be all Boolean functions on at most `k` variables. For every integer
`k >= 1`, the class `Q tensor B_k` is restriction closed and satisfies

\[
G(F)\le A_k I(F),\qquad A_k=\max\{3,k2^{k-1}\}.
\]

It also satisfies

\[
U(F)\le 2^{k-1}I(F),\qquad
H(F)\le \max\{2,2^{k-1}\}I(F).
\]

For `k >= 3` this strictly extends the quadratic phases, since the seed may
have Fourier/F2 degree greater than two. The quadratic block can have
arbitrarily many coordinates and arbitrary rank.

### Proof of the seed bounds

Let nonconstant `g` use `m <= k` coordinates. Since `p_g` is a probability
distribution on at most `2^m` sets,

\[
0\le U(g)\le H(g)\le m.
\]

Every restricted child has nonnegative `U`, hence each restriction drop is at
most `U(g)`, and therefore `G(g) <= mU(g) <= m^2`. A nonconstant cut of the
`m`-cube has at least `m` boundary edges (edge connectivity of the cube), so

\[
I(g)\ge \frac{m}{2^{m-1}}.
\]

Consequently

\[
G(g)\le m2^{m-1}I(g)\le k2^{k-1}I(g),
\quad U(g)\le2^{m-1}I(g),
\quad H(g)\le2^{m-1}I(g).
\]

The constant seed has all four quantities zero. Theorem 2 with `b=0` proves
the GU' bound. The reviewed quadratic estimates `U(q)<=I(q)` and
`H(q)<=2I(q)`, together with Lemma 1, prove the displayed `U` and `H` bounds.

As a concrete new class, `Q tensor B_4` has

\[
G(F)\le32I(F),\qquad U(F)\le8I(F),\qquad H(F)\le8I(F).
\]

The general universal bridge `H <= 2I+2U` would separately give the weaker
`H(F) <= (2+2^k)I(F)`; tensor entropy additivity supplies the sharper bound.

## Exact audit

`CHECK_QUADRATIC_SEED_TRANSFER.py` uses integer Walsh transforms, rational
spectral masses, and exact coefficient vectors of logarithms of primes. It
checks:

- all 32,906 Boolean functions modulo output sign through four variables;
- 197,436 seed inequalities, including the cube-edge lower bound and the
  derived `G` and entropy estimates;
- 5,328 exact `U`, `H`, `I`, and `G` tensor identities across 1,332 products
  of 18 seeds and 74 quadratic phases.

The checker is deterministic and reports `RESULT=PASS`.

## Exact remaining gap

The constants for `B_k` grow with `k` (`A_k=k2^{k-1}` by this proof, while
the entropy coefficient is `2^{k-1}`). The transfer theorem deliberately
leaves the seed unchanged. Therefore it does not control the aggregate
upper-set asymmetry mismatch inside an arbitrary-dimensional seed and does
not prove full FEI. The next unpaid step is a dimension-free GU' bound for a
seed class whose width tends to infinity, or a genuinely coupled argument
that uses quadratic structure to pay seed asymmetry rather than merely adding
the two blocks.
