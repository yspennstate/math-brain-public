# Addendum — a complementary one-point gap certificate

This addendum strengthens the main r11 report with a second, independent synchronization estimate. It uses only the exact Hadamard identity `D=D(P)` and the complementary-minor domination `|d_{alpha beta}|<=r_{alpha beta}`; it is therefore compatible with, but logically independent of, the `SO(6)` component-separation lemma used for the `6 kappa` pair-gap certificate.

Keep the notation of the main report:

\[
L(P,R)=\langle P,C\rangle+\frac12\langle R,X\rangle,
\]

\[
c_\sigma=\sum_iC_{i,\sigma(i)},\qquad
x_\rho=\sum_\alpha X_{\alpha,\rho(\alpha)},
\]

\[
B:=c_{\max}+\frac12x_{\max},\qquad
M:=\max_{\sigma\in S_4}\left(c_\sigma+\frac12x_{\rho_\sigma}\right),
\qquad \kappa=B-M.
\]

## Theorem — one-point assignment gap pays the mixed coupling defect

Assume `c_sigma` has a unique maximizer `sigma_0`. Define

\[
\beta:=c_{\sigma_0}-\max_{\sigma\ne\sigma_0}c_\sigma>0,
\qquad
\rho_0:=\rho_{\sigma_0},
\]

\[
\delta:=x_{\max}-x_{\rho_0}\ge0.
\]

Then every unitary-generated pair `(P,R)` satisfies

\[
\boxed{
L(P,R)\le B-\frac12\min\{\beta,\delta\}.}
\tag{A1}
\]

In particular, since

\[
M\ge c_{\max}+\frac12x_{\rho_0}
=B-\frac\delta2,
\]

we automatically have `delta>=2 kappa`. Therefore the purely spectral condition

\[
\boxed{\beta\ge2\kappa}
\tag{A2}
\]

is sufficient for the exact mixed inequality `L(P,R)<=M`, hence for the full determinant support inequality in that spectral/support direction.

Equivalently, any support-direction MOC4 counterexample for which `c_sigma` has a unique maximizer must satisfy

\[
\boxed{\beta<2\kappa.}
\tag{A3}
\]

### Proof

Take a Birkhoff decomposition

\[
P=\sum_{\sigma\in S_4}\lambda_\sigma P_\sigma,
\qquad \lambda:=\lambda_{\sigma_0}.
\]

The one-point assignment gap gives

\[
\langle P,C\rangle
\le c_{\max}-\beta(1-\lambda).
\tag{A4}
\]

Let `W_sigma` be the `3 x 3` signed Weyl matrix obtained from `P_sigma` by the mean-zero Hadamard representation, so

\[
D=\sum_\sigma\lambda_\sigma W_\sigma.
\tag{A5}
\]

For the three selected entries of `W_{sigma_0}`, write their signs as `s_alpha in {+1,-1}`. Since every other signed-permutation entry at the same position belongs to `{-1,0,+1}`,

\[
s_\alpha d_{\alpha,\rho_0(\alpha)}
\ge \lambda-(1-\lambda)=2\lambda-1.
\tag{A6}
\]

If `lambda>1/2`, the complementary-minor inequality `r>=|d|` therefore gives

\[
r_{\alpha,\rho_0(\alpha)}\ge2\lambda-1
\qquad(\alpha=1,2,3).
\tag{A7}
\]

Set `t=2 lambda-1`. Subtracting `t P_{rho_0}` from `R` leaves a nonnegative matrix with every row and column sum `1-t`. Hence

\[
R=tP_{\rho_0}+(1-t)R'
\]

for another doubly stochastic `R'`, and therefore

\[
\langle R,X\rangle
\le x_{\max}-t\delta.
\tag{A8}
\]

If `lambda<=1/2`, ordinary Birkhoff on `R` and (A4) already lose at least `beta/2` from `B`. If `lambda>=1/2`, combining (A4) and (A8) loses at least

\[
\beta(1-\lambda)+\frac\delta2(2\lambda-1).
\tag{A9}
\]

The right side is affine in `lambda` on `[1/2,1]`, with endpoint values `beta/2` and `delta/2`. Hence it is at least

\[
\frac12\min\{\beta,\delta\}.
\]

This proves (A1), and (A2) follows from `delta>=2 kappa`. `square`

## Combined near-tie reduction

The main report proves that, when the pair-class assignment has a unique maximizer with gap `gamma`, any counterexample must satisfy

\[
\gamma<6\kappa.
\]

The present addendum shows that, when the one-point assignment has a unique maximizer with gap `beta`, any counterexample must also satisfy

\[
\beta<2\kappa.
\]

Thus on the generic locus where both constituent assignment problems have unique maximizers, every hypothetical counterexample is forced into the simultaneous near-tie region

\[
\boxed{\beta<2\kappa,\qquad \gamma<6\kappa.}
\tag{A10}
\]

This is a stricter finite spectral localization of the unresolved mixed-support obstruction. It does not prove MOC4 globally and does not assert a common positive `(P,R)` permutation lift.

## Exact complex example covered by (A2) but not by the `6 kappa` criterion

Take

\[
a=(-4-3i,\ i,\ -4+4i,\ -1+i),
\]

\[
b=(-1+4i,\ -4+4i,\ i,\ 3+i),\qquad \eta=1.
\]

Exact enumeration gives

\[
c_{\max}=313,\qquad \beta=60,
\]

\[
x_{\max}=-362,\qquad \gamma=48,
\]

\[
M=108,\qquad \kappa=24.
\]

The maximizing one-point permutation has pair class with `x=-410`, so `delta=48`. Hence

\[
\beta=60\ge2\kappa=48,
\]

and Theorem (A2) proves the support inequality for every unitary. In contrast,

\[
\gamma=48<6\kappa=144,
\]

so the main report's pair-gap criterion alone does not certify this instance. The fixed endpoint term is `C_0=40`, so the exact 24-vertex support maximum is `148`, whereas the independent assignment relaxation is `172`; the addendum pays the full `24` coupling overshoot.

This example shows the two certificates are genuinely complementary.
