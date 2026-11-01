# Decoupled-time collision-to-density splice through one independent physical saddle

Programme: QFORM-DENSITY-3EIG-20260922  
Worker: fleet02/B03, Decoupled time integral  
Run: `20260923T092452Z-fleet02-B03-QFORM-r11`  
Status: supporting theorem proved; full conjecture remains open.

## 1. Exact obligation and sources

Target: independent real coordinates with densities at most one, symmetric `A` with at least three eigenvalues of modulus at least one; prove one universal essential density bound for `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, diagonal-basis or post-rotation-independence assumption is used here.

Fresh designated-partner input is fleet03/B03 r29, canonical mathematics

`yspennstate/math-open-problems@f7c9ef92371b6602f9a432a16555c48c2ed45a51:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T090012Z-fleet03-B03-QFORM-r29/REPORT.md`.

For its exact angular-cancellation packet `T`, with spectral parameter `s=s_3(A_T)>0`, r29 proves

\[
\int_{\mathbb R}|\phi_T(t)|^2dt
 < {54.27326850232713\over s},                                      \tag{1.1}
\]

hence

\[
\|p_T\|_2^2<{8.637858959899031\over s}.                             \tag{1.2}
\]

It also proves a weighted collision integral, but (1.1) is the endpoint needed below. The proof of r29 retains the whole-copy identity `|phi|^2=E exp(it(T-T'))`; no conjugate sum/difference pair is split.

Required pinned Claude package read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its Theorem D5 says that for a disjoint original-coordinate cross block `M`, with

\[
Z_5=e_5(M^TM),
\]

one has, without a marginal condition,

\[
\|p_Q\|_\infty\le5\sqrt{2e}\,Z_5^{-1/10}.                            \tag{1.3}
\]

Thus (1.3) is an immediate paid exit whenever `Z_5` is bounded below; the new work below addresses a different low-volume / collision branch.

Corrections retained: no law-uniform pointwise quadratic-phase decay; no independence after spectral rotation; no conditional sum/difference density cap; no arbitrary-joint rank-three coarea bound; no universally good physical minor or rank-three cross cut; no localization-before-aggregation step; and no use of the false arbitrary-self cross-Frobenius one-copy half-Riesz extension.

## 2. Uniform L2 packet for one shifted physical saddle

This packet was available in earlier B03 work; it is re-proved here because the exact constant enters the splice.

### Lemma 2.1

Let `U,V` be independent real random variables with probability densities bounded by one. For arbitrary `alpha,beta in R` and `c != 0`, put

\[
S=c(U+\alpha)(V+\beta).
\]

Then `S` has an `L^2` density and

\[
\boxed{\|p_S\|_2^2\le {3\sqrt3\over |c|}}.                          \tag{2.1}
\]

Equivalently,

\[
\boxed{\int_{\mathbb R}|\phi_S(t)|^2dt\le {6\pi\sqrt3\over |c|}}.  \tag{2.2}
\]

#### Proof

Translations preserve the cap-one hypothesis, so take `alpha=beta=0`; scaling reduces to `c=1`.

First restrict both variables to positive half-lines, allowing subprobability masses `m,n`. If `f,g` are the corresponding subdensities and `h` is the product subdensity, then for `z=e^w`,

\[
h(e^w)=\int_{\mathbb R}f(e^u)g(e^{w-u})\,du.
\]

Set

\[
a(u)=e^{u/2}f(e^u),\qquad b(u)=e^{u/2}g(e^u).
\]

Then

\[
e^{w/2}h(e^w)=(a*b)(w),
\qquad
\int_0^\infty h(z)^2dz=\|a*b\|_2^2.                                 \tag{2.3}
\]

Moreover

\[
\|a\|_{4/3}^{4/3}=\int_0^\infty x^{-1/3}f(x)^{4/3}dx
\le\int_0^\infty x^{-1/3}f(x)dx
\le {3\over2}m^{2/3}.                                                \tag{2.4}
\]

The last inequality is the decreasing-weight bathtub bound under `0<=f<=1`, `int f=m`.

Sharp Young on `R`, with `p=q=4/3`, `r=2`, has coefficient

\[
Y={ (4/3)^{3/4}\over 4^{1/4}},\qquad Y^2={4\over3\sqrt3}.
\]

Combining (2.3)-(2.4), one sign-pair contribution obeys

\[
\|h\|_2^2
\le Y^2\left({3\over2}\right)^3 mn
={3\sqrt3\over2}mn.                                                  \tag{2.5}
\]

For positive products, add the `++` and `--` pieces and use Minkowski followed by Cauchy-Schwarz:

\[
\|h_++\|_2^2
\le {3\sqrt3\over2}
 \left(\sqrt{m_+n_+}+\sqrt{m_-n_-}\right)^2
\le {3\sqrt3\over2}.                                                 \tag{2.6}
\]

The negative half-line, from `+-` and `-+`, has the same bound. The two half-lines are disjoint, so

\[
\|p_{UV}\|_2^2\le3\sqrt3.
\]

Scaling by `c` gives (2.1). Plancherel gives (2.2). QED.

## 3. Main new splice: two L2 time endpoints give L1 Fourier integrability

### Theorem 3.1 (collision-to-density saddle splice)

Let `T` be independent of `U,V`. Assume the partner r29 estimate (1.1) holds for `T` with parameter `s>0`. Let

\[
Q=T+c(U+\alpha)(V+\beta)+r,\qquad c\ne0,                              \tag{3.1}
\]

where `U,V` are independent cap-one variables and `alpha,beta,r` are arbitrary constants. Then `phi_Q` is integrable and

\[
\boxed{
\|p_Q\|_\infty
<6.699524741463198\,(s|c|)^{-1/2}.                                   \tag{3.2}
}
\]

In particular, for every interval `I`,

\[
\boxed{
\Pr(Q\in I)
<6.699524741463198\,(s|c|)^{-1/2}|I|.                                \tag{3.3}
}
\]

The density supplied by Fourier inversion is continuous, although continuity is not needed for the owner target.

#### Proof

Independence gives

\[
|\phi_Q(t)|=|\phi_T(t)|\,|\phi_S(t)|,
\qquad S=c(U+\alpha)(V+\beta).
\]

Cauchy-Schwarz in **time**, (1.1), and (2.2) yield

\[
\int |\phi_Q(t)|dt
\le
\left(\int|\phi_T|^2\right)^{1/2}
\left(\int|\phi_S|^2\right)^{1/2}
<
\left({54.27326850232713\over s}
      {6\pi\sqrt3\over |c|}\right)^{1/2}.                            \tag{3.4}
\]

Therefore Fourier inversion gives

\[
\|p_Q\|_\infty
\le {1\over2\pi}\int|\phi_Q|
< {1\over2\pi}
\left(54.27326850232713\,6\pi\sqrt3\right)^{1/2}
(s|c|)^{-1/2},
\]

and the numerical coefficient is `6.699524741463198`. This proves (3.2)-(3.3).

No independent-copy sum/difference coordinate is conditioned upon. The partner's dependence-safe `|phi_T|^2` estimate is consumed as a whole object, and the only extra independence is the genuine original-product independence of the disjoint saddle variables. QED.

### Conditional original-coordinate version

The same proof works after conditioning only outside original coordinates. Precisely, suppose original coordinates split as `K disjoint I disjoint {u,v}` and for almost every fixed `X_K=x_K`,

\[
Q=T_{x_K}(X_I)
 +c(X_u+\alpha(x_K))(X_v+\beta(x_K))+r(x_K),                          \tag{3.5}
\]

with the r29 bound (1.1) valid for `T_{x_K}` uniformly with the same `s`. Since conditioning on `X_K` leaves `X_I,X_u,X_v` mutually independent with their original cap-one laws, (3.2) holds conditionally, uniformly in `x_K`, and averaging gives the same unconditional bound.

In matrix language, if the saddle is represented by a zero-diagonal physical principal pair with off-diagonal matrix entry `b`, then its quadratic term is `2bUV`, i.e. `c=2b`. Thus

\[
\boxed{
\|p_Q\|_\infty
<4.737279375415678\,(s|b|)^{-1/2}.                                   \tag{3.6}
}
\]

This permits arbitrary affine shifts of that pair generated by the conditioned outside coordinates. What is not permitted in this splice is an unconditioned quadratic coupling between the saddle pair and the r29 active block, because that would destroy the genuine product factorisation used in (3.4).

## 4. Why the saddle is the correct two-factor endpoint, not one square

The partner r29 packet also controls

\[
\int |t|^{-1/2}|\phi_T(t)|^2dt.
\]

A tempting two-factor Cauchy-Schwarz splice with a single independent square `Z^2` would require a complementary positive-weight estimate

\[
\int |t|^{1/2}|\phi_{Z^2}(t)|^2dt<\infty.                            \tag{4.1}
\]

This is false already for `Z` uniform on a bounded interval containing zero: stationary phase gives `|phi_{Z^2}(t)|` of order `|t|^{-1/2}` along the tail, so the integrand in (4.1) is of order `|t|^{-1/2}` and is not integrable. Even the unweighted `L^2` norm of a single square characteristic function has a logarithmic endpoint divergence. Thus the partner weighted collision endpoint does not close the one-copy problem by a naive two-factor weighted Cauchy-Schwarz with one square.

By contrast, one **physical saddle product** has the uniform true `L^2` estimate (2.2), exactly matching the partner r29 `L^2` endpoint and producing the `L^1` time integral (3.4). This identifies a genuine product-preserving closure mechanism rather than a false endpoint promotion.

## 5. Application of the pinned Claude D5 result to the same proof map

Before entering the collision collar, apply the completed D5 theorem at the required pinned source. If an original-coordinate disjoint cross block `M` has

\[
Z_5=e_5(M^TM)\ge \zeta>0,
\]

then (1.3) gives the actual one-copy inequality

\[
\boxed{\|p_Q\|_\infty\le5\sqrt{2e}\,\zeta^{-1/10}.}                 \tag{5.1}
\]

For example `Z_5>=1` gives `||p_Q||_infty <= 5 sqrt(2e) < 11.66` with every self block, outside coupling and affine term retained exactly as in D5. Hence any survivor requiring Theorem 3.1 may be assumed to have small fifth cross-volume on every candidate disjoint cut. This is a real reduction, not a claim that D5 follows from the three-eigenvalue hypothesis.

Combining (5.1) and (3.6) yields the following paid alternatives inside a product-preserving decomposition:

* fifth cross-volume bounded below: D5 gives a universal density bound;
* exact-cancellation r29 core plus a disjoint physical saddle edge of controlled `|b|`: the new L2-to-L1 time splice gives a universal density bound.

## 6. Source-valid target family and remaining structural debt

Take any exact angular-cancellation packet from r29 with `s_3(A_T)>=1`, and direct-sum it with the physical saddle matrix

\[
B_b=\begin{pmatrix}0&b\\ b&0\end{pmatrix},\qquad |b|\ge1.
\]

For arbitrary independent cap-one inputs, the full matrix is in the owner target and (3.6) gives

\[
\|p_Q\|_\infty<4.737279375415678.                                   \tag{6.1}
\]

More generally the conditional version allows outside coordinates to generate arbitrary affine shifts of the saddle pair while preserving the same bound.

The first unpaid implication is therefore narrower than at the start of this run. In the strict near-coloop / angular-cancellation collar, after the D5 exit, a survivor must fail to expose a controlled disjoint physical saddle packet whose removal leaves a uniform r29 collision core. Equivalently, every moderate saddle edge must remain quadratically entangled with the active core, or have coefficient tending to zero, while all fifth cross-volumes stay small. The next useful step is a structural or analytic treatment of precisely that **entangled-saddle, low-5-volume collar**; one may not delete the transverse coupling or take a worst conditional projection-density supremum.

This does not prove the unrestricted conjecture. It converts a completed target-scale collision theorem into a genuine one-copy linear small-ball theorem on a new, correction-safe product-preserving branch and records the exact branch still unpaid.
