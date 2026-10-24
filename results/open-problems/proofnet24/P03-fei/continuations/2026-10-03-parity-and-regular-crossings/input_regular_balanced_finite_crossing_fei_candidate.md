# Ordinary FEI for balanced input-regular finite-crossing score functions

Date: 2026-10-03. **Candidate complete proof; independent audit pending.**
This is a restricted ordinary Fourier entropy--influence theorem, with no
output parity.  It removes both the odd-crossing and bounded-crossing-location
hypotheses from the preceding regular-input theorem, at the price of a fixed
lower bound on the two output probabilities.  Historical novelty is not
certified, and the unrestricted FEI conjecture remains open.

## Theorem

Fix an integer \(m\geq1\), \(B\geq1\), and \(r_0\in(0,1/2]\).  Put
\[
 S(X)=\sum_{i=1}^n w_iX_i,\qquad
 \sigma^2=\sum_iw_i^2>0,
\]
and assume
\[
 \max_i|w_i|\leq {B\sigma\over\sqrt n}.                 \tag{1}
\]
Let \(F:\mathbb R\to\{-1,1\}\) have exactly \(m\) distinct genuine
crossings.  Thus it is constant on the complementary open intervals,
successive interval labels alternate, every crossing may be assigned either
adjacent label, and there are no other isolated point anomalies.  The
crossings may be anywhere and may be arbitrarily close.  If
\[
 g(X)=F(S(X)),\qquad
 \min\{\Pr[g=1],\Pr[g=-1]\}\geq r_0,                   \tag{2}
\]
then
\[
 \boxed{H(g)\leq C(m,B,r_0)I(g)}.                      \tag{3}
\]
Here entropy is in bits and influence is the physical flip probability.

The following explicit, deliberately nonoptimized constants work.  Set
\[
 L={2\over\sqrt{r_0}},\quad
 h={r_0\sqrt{2\pi}\over8(m+1)},\quad
 d={e^{-L^2}\over\sqrt{2\pi}},\quad
 c_D=\sqrt{2/3},\quad E=2.24\sqrt2,
\]
\[
 A={41\over\sqrt2(1-e^{-1})},\qquad
 K=\max\left\{1,\left\lceil
       \left({2EmB^2\over dc_D}\right)^2\right\rceil\right\},
\]
and
\[
 N_0=\left\lceil\max\left\{
 2KB^2,{K^2B^2\over h^2},
 \left({4.48(m+1)B\over r_0}\right)^2
 \right\}\right\rceil.                               \tag{4}
\]
Then one may take
\[
 C(m,B,r_0)=\max\left\{\log_2N_0+3,
 { (1+4Am)B\sqrt K\over(\ln2)dc_D}\right\}.           \tag{5}
\]

Coordinate sign changes let us assume \(w_i\geq0\).  Zero weights are
allowed.  The cases \(\sigma=0\), dimension zero, or constant output are
disposed of before division; (2) in fact excludes constant output.

## Established entropy upper bound

Up to a constant sign, \(F(S)\) is a product of the \(m\) crossing
halfspaces, with the legal tie convention chosen separately at every
crossing.  The Klivans--O'Donnell--Servedio halfspace estimate
\(\operatorname{NS}_\varepsilon\leq20.5\sqrt\varepsilon\), followed by a
union bound, gives
\[
 \operatorname{NS}_\varepsilon(g)\leq20.5m\sqrt\varepsilon.
\]
The standard exact degree--noise identity, applied at
\(\varepsilon=1/(2k)\), gives for the squared-Fourier degree law \(D\)
\[
 \Pr[D\geq k]\leq {Am\over\sqrt k}.
\]
Conditioning on degree, using
\(\log_2\binom nj\leq j\ln(en/j)/\ln2\), and integrating the tail yields
\[
 \boxed{H(g)\leq {1+4Am\over\ln2}\sqrt n.}             \tag{6}
\]
The full calculation, including degree zero, appears in the preceding
odd-crossing proof.  Nothing in it uses oddness, crossing locations, weight
lower bounds, or output balance.  This is established prior machinery and
is not claimed as the new step here.

## Balance produces two protected opposite-label intervals

Let \(Z\sim N(0,\sigma^2)\).  Let \(B_+\) and \(B_-\) be the actual Borel
label sets, including every crossing in its assigned class, and let
\(G_+\) and \(G_-\) be their unions of open interval interiors.  The two
versions have the same Gaussian measure.  Berry--Esseen and (1) give
\[
 \sup_t|\Pr[S\leq t]-\Pr[Z\leq t]|
 \leq {0.56B\over\sqrt n}.                             \tag{7}
\]
Each actual label set is a union of at most \(m+1\) intervals with arbitrary
open/closed endpoints.  Comparing its discrete probability with the
Gaussian probability of the corresponding interiors, through CDF values
and left limits, therefore gives
\[
 |\Pr[S\in B_\pm]-\Pr[Z\in G_\pm]|
 \leq {1.12(m+1)B\over\sqrt n}.                        \tag{8}
\]
This comparison includes any discrete score mass assigned at a crossing:
the Gaussian has no atom, while the CDF and its left limit retain the
discrete endpoint convention.

For \(n\geq N_0\), (2), (4), and (8) imply
\(\Pr[Z\in G_\pm]\geq3r_0/4\).  Chebyshev's inequality and the choice of
\(L\) give \(\Pr[|Z|>L\sigma]\leq r_0/4\), so each label occupies Gaussian
mass at least \(r_0/2\) inside \([-L\sigma,L\sigma]\).  The Gaussian density
is at most \(1/(\sigma\sqrt{2\pi})\); consequently the total Lebesgue length
of each label there is at least
\[
 {r_0\sigma\sqrt{2\pi}\over2}.
\]
There are at most \(m+1\) components, so for each label one component has
length at least \(4h\sigma\).  Choose its midpoint.  We obtain two points
\(a,b\in[-L\sigma,L\sigma]\), with opposite labels, such that \(F\) is
constant on the radius-\(2h\sigma\) neighborhoods of both points.

## Local signed translation

For any \(|u|,|v|\leq h\sigma\), write \(J_{a,b}\) for the interval between
\(a\) and \(b\).  If, for definiteness, \(u<v\), then
\[
 \int_{J_{a,b}}[F(r+v)-F(r+u)]\,dr
\]
equals, up to the orientation of \(J_{a,b}\), the difference between the
two boundary integrals
\[
 \int_{b+u}^{b+v}F(t)\,dt-\int_{a+u}^{a+v}F(t)\,dt.
\]
The protected neighborhoods and opposite labels make the absolute value of
this expression exactly \(2(v-u)\).  Since the integrand has magnitude at
most two, the open pivotal set inside \(J_{a,b}\), after deleting translated
crossing endpoints, has Lebesgue measure at least \(|u-v|\):
\[
 \left|\{r\in J_{a,b}:F(r+u)\ne F(r+v)\}^{\circ}\right|
 \geq|u-v|.                                            \tag{9}
\]
This is the replacement for the global opposite-tail lemma.  It works for
even or odd \(m\), and does not refer to the numerical crossing locations.
The pivotal set is a union of at most \(2m\) open intervals (in fact \(m\)
would suffice because it is zero near both endpoints).

## Regular block resampling forces influence

For \(n\geq N_0\), choose a uniform \(K\)-subset \(J\) and independent old
and fresh signs.  Put
\[
 U=\sum_{i\in J}w_iX_i,\quad V=\sum_{i\in J}w_iY_i,
 \quad R=\sum_{i\notin J}w_iX_i,
 a_J=\sum_{i\in J}w_i^2.
\]
Every mask satisfies
\[
 a_J\leq {KB^2\sigma^2\over n}\leq{\sigma^2\over2},
 \qquad |U|,|V|\leq {KB\sigma\over\sqrt n}\leq h\sigma.       \tag{10}
\]
Thus \(R\) has standard deviation between \(\sigma/\sqrt2\) and \(\sigma\).
On \(J_{a,b}\subseteq[-L\sigma,L\sigma]\), the density of the matching
Gaussian remainder is at least \(d/\sigma\).  Berry--Esseen for the
remainder has CDF error at most \(0.56\sqrt2B/\sqrt n\).  Apply it to the at
most \(2m\) open components in (9).  Uniformly in \(J,u,v\),
\[
 \Pr[F(R+u)\ne F(R+v)]
 \geq {d|u-v|\over\sigma}-{EmB\over\sqrt n}.            \tag{11}
\]

The exact selected-difference moments are
\[
 \mathbb E[(U-V)^2\mid J]=2a_J,
 \quad \mathbb E[(U-V)^4\mid J]
 =12a_J^2-4\sum_{i\in J}w_i^4\leq12a_J^2.
\]
Hölder interpolation gives
\[
 \mathbb E[|U-V|\mid J]\geq c_D\sqrt{a_J}.             \tag{12}
\]
The zero-energy case reads \(0\geq0\).  Also
\[
 \mathbb E_Ja_J={K\sigma^2\over n},\qquad
 0\leq a_J\leq {KB^2\sigma^2\over n}.
\]
The pointwise inequality \(\sqrt{x}\geq x/\sqrt M\) for \(0\leq x\leq M\)
therefore yields the lower, not Jensen, estimate
\[
 \mathbb E_J\sqrt{a_J}\geq{\sqrt K\sigma\over B\sqrt n}.       \tag{13}
\]
Average (11)--(13) and use the choice of \(K\):
\[
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
 \geq {dc_D\sqrt K\over2B\sqrt n}.                    \tag{14}
\]
Successive coordinate resampling and the union bound give the opposite
bound
\[
 \Pr[g(X)\ne g(X^{\mathrm{resample}\,J})]
 \leq {K\over2n}I(g).                                  \tag{15}
\]
Hence
\[
 \boxed{I(g)\geq {dc_D\over B\sqrt K}\sqrt n}
 \qquad(n\geq N_0).                                   \tag{16}
\]
Combining (6) and (16) proves (3) in large dimension.  For \(n<N_0\), the
known elementary weak bound \(H(g)\leq(\log_2n+3)I(g)\) proves (5).

## Scope and checks still required

This candidate covers arbitrary finite crossing count, arbitrary crossing
locations and spacing, and weights with no positive lower bound, provided
both output labels have probability at least the fixed \(r_0\).  It does
not give a constant uniform as \(r_0\downarrow0\), does not cover irregular
weights with unbounded \(B\), and does not prove FEI for general Boolean
functions.  The constants are extremely large and not optimized.

The entropy upper bound, Berry--Esseen input, weak logarithmic FEI, and
regular-mask moment argument are prior or separately audited ingredients.
The new content is the balance-to-protected-interval extraction and the
local signed-translation influence lower bound.  Before promotion from
candidate to proof, those steps require an independent analytic audit and
fresh exact finite checks.  No claim of historical priority is made.
