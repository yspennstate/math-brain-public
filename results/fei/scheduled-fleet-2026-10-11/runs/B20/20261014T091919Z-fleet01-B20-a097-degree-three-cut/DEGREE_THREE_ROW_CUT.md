# Degree-three localization of the universal GU row cut

All logarithms are base two. For a genuine Boolean function on a finite
uniform cube write

\[
R(f)=G(f)-4I(f)-\frac34U(f).
\]

## Frozen candidate and prior bound

The frozen candidate is the pair \((a,b)=(4,3/4)\).  The source-complete
row-cut theorem gives, in every dimension,

\[
G(f)\le D_{\ge2}(f)+\frac12V_1(f)+\frac{2}{\ln2}I(f),                 \tag{1}
\]

where

\[
D_{\ge2}=\sum_i(B_i-\Gamma_i)+
\sum_i\sum_{|A|\ge2}K_{i,A}
\]

retains the signed term and every KL row of order at least two, and

\[
V_1=\sum_{i\ne j}(p_j+p_{ij})
\log_2\frac{\pi_j}{p_j+p_{ij}}.
\]

Thus the prior unpaid leaf was

\[
D_{\ge2}+\frac12V_1\le
\left(4-\frac2{\ln2}\right)I+\frac34U,                              \tag{2}
\]

on tensor-prime Boolean functions with \(R>0\).

## New localization theorem

It suffices to prove (2) only for genuine Boolean functions satisfying all
three conditions

1. the function is tensor-prime;
2. \(R(f)>0\);
3. the Fourier degree is at least three.

This is a strict removal of the complete degree-at-most-two stratum from the
unpaid universal leaf.

### Proof

The source-pinned B07 theorem makes \(U,I,G\), and hence \(R\), additive
under tensor products.  Therefore a positive-residual Boolean function has a
positive-residual tensor-prime factor.  It is enough to rule out every such
factor.

The B11 degree-two theorem states, for every genuine Boolean function of
Fourier degree at most two in every dimension,

\[
G(f)\le2I(f).                                                        \tag{3}
\]

For a nonconstant such function, \(I(f)>0\), and \(U(f)\ge0\).  Hence

\[
R(f)le2I(f)-4I(f)-\frac34U(f)
=-2I(f)-\frac34U(f)<0.                                              \tag{4}
\]

Constants have \(I=U=G=R=0\).  Consequently no positive-residual factor has
Fourier degree at most two.  It must have degree at least three.

Now assume (2) for every tensor-prime positive-residual Boolean function of
degree at least three.  Combining it with (1) gives \(R\le0\) on that class,
contradicting positive residual.  Equation (4) covers degree at most two.
Tensor additivity then gives \(R\le0\) for every genuine Boolean function,
which is exactly

\[
G\le4I+\frac34U.                                                    \tag{5}
\]

The independently audited induction from universal GU gives
\(U\le aI/(1-b)=16I\).  The separately audited inequality
\(H\le2I+2U\) therefore yields

\[
H\le34I.                                                           \tag{6}
\]

## Exact remaining obligation

Universal GU and FEI remain open.  The sole row-cut obligation is now (2)
on tensor-prime positive-residual genuine Boolean functions of Fourier
degree at least three.  It retains the complete signed
\(\sum_i(B_i-\Gamma_i)\), all order-at-least-two KL rows, the full singleton
reuse cost \(V_1/2\), normalization, and the fixed coefficient losses.

The result is qualitative domain reduction, not a numerical improvement of
the right-hand side.  It gives no bound merely from a small amount of
level-at-least-three Fourier mass.  The next required lemma must be
quantitative in that mass and must not discard the signed term.

