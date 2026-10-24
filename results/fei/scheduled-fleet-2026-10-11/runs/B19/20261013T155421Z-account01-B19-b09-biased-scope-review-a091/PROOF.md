# Rare-biased AND lower bound and B09 scope repair

All logarithms are base two. Let `X,Y` be independent Bernoulli variables with
`P(X=1)=p` and `P(Y=1)=q`, and let

\[
g(X,Y)=(-1)^{XY}.
\]

We review the B09 charge associated with restricting the `X` coordinate. In
the notation of the B09 source, `M_X` is the entropy concavity gap and `J_X`
is the conditional Fourier uncertainty term. The exact identity is

\[
L_X=M_X+J_X.
\]

## 1. Exact product-biased spectrum

In the orthonormal product basis the four squared Fourier coefficients,
ordered as `emptyset,{X},{Y},{X,Y}`, are

\[
 a=(1-2pq)^2,\quad b=4q^2p(1-p),\quad
 c=4p^2q(1-q),\quad d=4p(1-p)q(1-q).
\]

They are nonnegative and sum to one.  After the `X` restriction the total
nonconstant `Y`-mass of the parent is

\[
r=c+d=4pq(1-q).
\]

Writing `h_2` for binary entropy and
`H_q=h_2(4q(1-q))`, direct substitution into the definitions gives

\[
M_X=H(a,b,c,d)-h_2(r),\qquad
J_X=h_2(r)-pH_q.
\]

Thus

\[
J_X-M_X=2h_2(r)-H(a,b,c,d)-pH_q. \tag{1}
\]

This is an identity for a genuine two-bit Boolean gate for every
`0<p,q<1`.

## 2. Rare-bias asymptotic

For fixed `0<q<1/2` and `p` tending to zero, the elementary expansion
`h_2(tp)=tp log_2(1/p)+O_t(p)` yields

\[
2h_2(r)=8q(1-q)p\log_2(1/p)+O_q(p).
\]

Among `a,b,c,d`, the three small masses have first-order coefficients
`4q^2`, `0`, and `4q(1-q)` respectively, so

\[
H(a,b,c,d)=4qp\log_2(1/p)+O_q(p).
\]

The remaining term `pH_q` is `O_q(p)`.  Substitution into (1) proves

\[
J_X-M_X
=4q(1-2q)p\log_2(1/p)+O_q(p). \tag{2}
\]

The coefficient is strictly positive for every fixed `q` in `(0,1/2)`.
Consequently no inequality of the form

\[
J_X\le M_X+C p
\]

with a constant `C` uniform in `p` can hold even for this genuine Boolean
two-bit family.  More generally, any additive correction valid uniformly for
this family must have order at least `p log(1/p)`.

For `q=1/4`, the coefficient in (2) is `1/2`.  The accompanying exact-rational
interval checker verifies the source point `p=1/8` and gives normalized ratios
converging to `1/2` at `p=2^{-k}`.  This finite check supports but is not needed
for the analytic all-parameter conclusion.

## 3. What this repairs, and what it does not

The original B09 report correctly expanded its available uncertainty tax
`Delta(p)` as `p log_2(1/p)+O(p^2)`.  An upper bound with that asymptotic does
not by itself prove that every valid correction has the same order.  Equation
(2) supplies the missing Boolean lower-bound family and therefore repairs the
order-of-growth conclusion.

It does **not** prove that the exact B09 tax `Delta(p)` is coefficient-sharp.
At `q=1/4`, the lower-bound coefficient is `1/2`, whereas the leading
coefficient of `Delta(p)` is one.

## 4. Composition scope

For functions on disjoint physical coordinate blocks, the product-biased
Fourier distribution is a product distribution. Entropy, influence, and the
coordinatewise B09 ledgers therefore add exactly. This proves tensor
additivity at the disjoint-product scope.

No argument in the reviewed source proves that a correction is charged only
once through an arbitrary Boolean composition hierarchy, especially when
variables or witnesses overlap or when induced child biases change from node
to node. Such a transfer requires an additional gate cocycle or owned-credit
lemma. The exact disjoint-product statement must not be promoted to that
broader claim.

