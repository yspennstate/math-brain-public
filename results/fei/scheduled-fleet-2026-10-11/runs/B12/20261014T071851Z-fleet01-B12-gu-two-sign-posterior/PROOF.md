# Exact two-sign posterior identity for `U` and `G`

All logarithms are base two.  Let `f_+` and `f_-` be arbitrary genuine
Boolean functions on the same finite uniform cube.  No variables are assumed
fresh, no Fourier supports are assumed disjoint, and no activation
probability is bounded away from zero.

For `epsilon` in `{+,-}`, write

\[
 p_\epsilon(S)=\widehat f_\epsilon(S)^2,
 \qquad \pi_\epsilon(S)=\sum_{T\supseteq S}p_\epsilon(T).
\]

Define the sign-blind exact and upper masses

\[
 q(S)=\frac{p_+(S)+p_-(S)}2,
 \qquad m(S)=\frac{\pi_+(S)+\pi_-(S)}2
             =\sum_{T\supseteq S}q(T),
\tag{1}
\]

and, when the denominators are nonzero,

\[
 r_\epsilon(S)=\frac{p_\epsilon(S)}{2q(S)},
 \qquad s_\epsilon(S)=\frac{\pi_\epsilon(S)}{2m(S)}.
\tag{2}
\]

Thus `r(S)` and `s(S)` are binary posterior laws: the first conditions the
sign on the exact spectral set `S`, while the second conditions it only on
membership in the upper cone above `S`.  Put

\[
 M(f_+,f_-)=\sum_S q(S)\log\frac{m(S)}{q(S)},
\tag{3}
\]

\[
 K(f_+,f_-)=\sum_S q(S)D_2(r(S)\Vert s(S)).
\tag{4}
\]

Zero masses contribute zero.

## Theorem 1: exact ensemble identity

For every Boolean pair,

\[
 \boxed{\frac{U(f_+)+U(f_-)}2=M(f_+,f_-)-K(f_+,f_-).}
\tag{5}
\]

In particular `K>=0`, but no sign is asserted for its restriction
Laplacian.

### Proof

At every `S` with `q(S)>0`,

\[
 \frac{\pi_\epsilon(S)}{p_\epsilon(S)}
 =\frac{m(S)}{q(S)}\frac{s_\epsilon(S)}{r_\epsilon(S)}.
\]

Since `p_epsilon/2=q r_epsilon`, averaging the two `U` summands gives

\[
 \sum_Sq(S)\log\frac{m(S)}{q(S)}
 +\sum_Sq(S)\sum_\epsilon r_\epsilon(S)
       \log\frac{s_\epsilon(S)}{r_\epsilon(S)},
\]

which is exactly `M-K`.  Endpoint cases follow by the zero-mass convention.

The physical masks

\[
 a=\frac{f_++f_-}{2},\qquad b=\frac{f_+-f_-}{2}
\]

are automatically disjoint pointwise.  Identity (5) therefore removes all
fresh-selector, Fourier-orthogonality, collision-energy and minimum-activation
hypotheses from the **two-sign ensemble** payment, even when the two signs
reuse every physical variable.

## Theorem 2: exact `G/U` center

For a functional `X` of a Boolean pair, let

\[
 LX=\sum_i\left(X(f_+,f_-)-\frac{X(f_{+,i,+},f_{-,i,+})+
 X(f_{+,i,-},f_{-,i,-})}{2}\right).
\tag{6}
\]

Let `Ibar=(I(f_+)+I(f_-))/2` and
`D_{a,b}(f)=G(f)-aI(f)-bU(f)`.  Applying (5) at the root and every physical
restriction gives the exact identities

\[
 \boxed{\frac{G(f_+)+G(f_-)}2=LM-LK,}
\tag{7}
\]

\[
 \boxed{\frac{D_{a,b}(f_+)+D_{a,b}(f_-)}2
 =LM-a\overline I-bM+bK-LK.}
\tag{8}
\]

Hence the remaining fixed-sign quantity is not an unsigned entropy loss.  It
is precisely

\[
 Z_{a,b}(f_+,f_-)=\frac{D_{a,b}(f_+)-D_{a,b}(f_-)}2,
\tag{9}
\]

and

\[
 D_{a,b}(f_+)=LM-a\overline I-bM+bK-LK+Z_{a,b}.
\tag{10}
\]

A concrete universal sufficient condition is therefore: one fixed
`a>=0, 0<=b<1` and, for every nonconstant Boolean `f_+`, one Boolean companion
`f_-` such that the right side of (8) is nonpositive and `Z_{a,b}<=0`.
Then `D_{a,b}(f_+)<=0` for every Boolean function.  The reviewed reduction
then yields

\[
 U(f)\le\frac{a}{1-b}I(f),\qquad
 H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\tag{11}
\]

This implication has no overlap, activation, depth or bias parameter.  The
unpaid hypothesis is now exactly the signed projection inequality, not the
ensemble center.

## Product companion and the active-policy reserve

Take `f_+=gh` and `f_-=g`.  The corresponding masks are
`g(1+h)/2` and `g(h-1)/2`, so the pair is a physical actual/companion split.
Let

\[
 C=U(gh)-U(g)-U(h),\quad
 LC=G(gh)-G(g)-G(h),
\]

and let `J` be the joint pivotality of `g,h`.  Then

\[
 2Z_{a,b}=D_{a,b}(h)+LC+2aJ-bC.
\tag{12}
\]

For the active-policy companion from the preceding run,
`LC=C+P^q-R_qP^q_child`; hence

\[
 \boxed{2Z_{a,b}=D_{a,b}(h)+(1-b)C+2aJ
 +P^q-R_qP^q_{child}.}
\tag{13}
\]

Thus the previously isolated signed composition remainder is exactly the
actual/companion projection after retaining the companion factor defect.
Dropping `D(h)`, a child companion, or the sign of any term is invalid.

## Posterior-only payment is refuted

The root posterior `K` cannot pay the active companion with any finite
coefficient.  On three bits take

\[
 g=(-1,-1,-1,-1,-1,-1,-1,1),
\qquad
 h=(-1,1,1,1,1,1,1,-1).
\tag{14}
\]

Here `gh` and `g` have identical squared Fourier laws

\[
 (9/16,1/16,1/16,1/16,1/16,1/16,1/16,1/16),
\]

and identical upper masses.  Therefore `r=s` at every set and exactly
`K(gh,g)=0`.  Nevertheless direct exact Walsh calculation gives

\[
 C=-\tfrac12,\quad LC=\tfrac32,\quad
 P^q=1,\quad R_qP^q_{child}=-1,\quad J=\tfrac34.
\tag{15}
\]

So `P^q<=lambda K` fails for every finite `lambda`.  Moreover
`LK=-0.521384822086...<0`; the term `-LK` has the wrong sign for this
example.  The cancellation in (13) instead comes from the retained companion
factor: `gh` and `g` are cube-isometric one-point defects, so `Z=0`, while
`D(h)` cancels the other four signed terms exactly.

The prior positive three-bit collision, the negative two-bit collision, its
two-fold disjoint tensor, and a rare half-activation all satisfy (5)--(13).
Their numerical values are archived by `CHECK.py`; `K` and `LK` take both
helpful and adverse configurations.  Therefore neither posterior positivity
nor tensorization supplies the missing projection theorem.

## Status

The ensemble identity and product projection formula are proved pending
independent review.  They remove the overlap/activation hypotheses for the
two-sign center and isolate a sharper gap: a signed joint bound involving
`D(h)`, root/child companions and posterior drift.  The root posterior alone
is rigorously refuted as that bound.  Universal GU and full FEI remain open.
