# Independent proof reconstruction

## Reviewed claim

Let (M_0\in\mathbb F_2^{s\times r}) have full column rank and let

\[
P(x,u,z)=(-1)^{x^TM_0u+a\cdot x+b\cdot u+c\cdot z+d}D(u,z),
\]

where (D) is an arbitrary Boolean function and the physical block (z)
has width (t).  Put (D_u^c(z)=(-1)^{c\cdot z}D(u,z)).  The claim reviewed
is

\[
H(P)=2r+\mathbb E_uH(D_u^c),\qquad
I(P)\ge r+\mathbb E_u I(D_u^c),                       \tag{1}
\]

and hence, with (C_t=\max_{g:\mathbb F_2^t\to\{\pm1\}}H(g)/I(g)),

\[
U(P)\le H(P)\le K_tI(P),\qquad K_t=\max\{2,C_t\}.    \tag{2}
\]

## Fourier normalization

At frequency ((\alpha,\gamma,\delta)), summation over (x) is zero unless
(M_0u+a=\alpha).  Full column rank makes this (u) unique whenever it
exists.  With the normalized Walsh convention,

\[
\widehat P(\alpha,\gamma,\delta)
=2^{-r}(-1)^{b\cdot u+d+\gamma\cdot u}
 \widehat{D_u^c}(\delta).                              \tag{3}
\]

There are (2^r) admissible (\alpha)'s and (2^r) choices of (\gamma).
Thus the squared Fourier law assigns mass
(2^{-2r}\widehat{D_u^c}(\delta)^2) to each triple, and sums to one.  Its
entropy is the entropy of two independent uniform (r)-bit labels plus the
mean conditional entropy.  This proves the first identity in (1) with the
claimed normalization.

## Physical influence accounting

- A nonzero physical row of (M_0) makes the derivative in the corresponding
  (x_i) coordinate balanced in (u), even after the affine bit (a_i).
  It therefore contributes (1/2).  Rank (r) requires at least (r)
  nonzero rows, giving (I_x\ge r/2).
- Every column (M_0e_j) is nonzero.  The derivative in (u_j) is balanced
  in (x), independently of the quotient of the two (D)-values and of
  (b_j).  Hence (I_u=r/2).
- The bilinear phase is independent of (z), so
  (I_z=\mathbb E_uI(D_u^c)).

Adding these terms proves the second inequality in (1).  Applying the exact
(t)-bit FEI inequality fiber by fiber proves (2).

## Tree endpoint

For any finite adaptive/pruned physical restriction tree,

\[
\sum_{v}w_v\left(U(P_vh)-\frac12U(P_{v,0}h)
-\frac12U(P_{v,1}h)\right)
=U(Ph)-\sum_\ell w_\ell U(P_\ell h).                 \tag{4}
\]

This is an algebraic telescope; it does not need nodewise positivity or a
local pivotal-credit inequality.  If (h) is one common disjoint Boolean
factor, (U(P_vh)=U(P_v)+U(h)), and the (U(h)) terms cancel.  Since leaf
(U\ge0), (4) is at most (U(P)), and (2) proves the advertised bound.

The result is therefore an endpoint-reservoir theorem.  It does not assign
nonreused physical influence to individual nodes and does not cover
branch-dependent terminal factors.

## Exact constants through width four

The independent checker fixes one truth value to quotient by global output
complement, then exhausts all remaining truth tables.  Unlike the author
checker, it computes every Walsh coefficient by its defining character sum
and computes influence by physical edge disagreements.  Entropy comparisons
use rational, outward logarithm intervals with 56 positive-series terms.

The independent results are

\[
C_1=0,\quad C_2=2,
\]

\[
C_3=\frac73+\frac34\log_2\frac{16}{9}
=2.955889582251598\ldots,
\]

\[
C_4=\frac{45}{16}+\frac{49}{32}\log_2\frac{64}{49}
=3.402475551198587\ldots.
\]

It independently finds 47 nonconstant spectrum/influence profiles in four
bits and the same 16 output-complement representatives with the maximizing
one-point-defect profile.  The interval width for (C_4) is below
(2.07\times10^{-56}).  It also checks 16,092 shields over every small
full-column-rank physical matrix, including nonidentity and rectangular
matrices, reconstructing 237,936 nonzero spectral atoms.

## Width-uniform hardness

For (q(x,u)=(-1)^{xu}), direct reconstruction gives (H(q)=2) and
(I(q)=1).  Disjoint tensor identities give

\[
H(qg^{\otimes N})=2+NH(g),\qquad
I(qg^{\otimes N})=1+NI(g).
\]

A bound uniform in the aligned width therefore implies
(H(g)\le CI(g)) after division by (N) and passage to the limit.  This
hardness conclusion is correct and explains why the remaining width
parameter cannot be removed by a routine finite-dimensional argument.

## Scope correction

The proof establishes that (K_t=\max\{2,C_t\}) is a valid retained-(U)
tree constant, and it establishes the exact values of the auxiliary FEI
constants (C_t) through (t=4).  It does **not** prove that (K_t) is the
smallest possible constant for the retained-(U) inequality.  The phrase
"exact retained-(U) constants" should therefore be read as "explicit bound
using the exact finite-dimensional FEI constant," not as an optimality
claim.  No mathematical step in the displayed theorem needs repair.

