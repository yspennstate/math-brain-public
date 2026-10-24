# account01/B02 — QFORM integrated-Fourier / zero-pivot triple theorem

Run: `20260922T162035Z-account01-B02-qform-auto11`
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`
Execution: `WITHOUT_VERIFIED_BRAIN`

## Exact target

For every dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal bound for the density of the quadratic form, or give a target-level counterexample. Continuity is a separate requested conclusion.

The law-uniform pointwise quadratic-phase decay premise is refuted by the live correction set, so this run does not use it. No counterexample to a target-wide uniform `L1` characteristic-function bound is obtained here. Instead, after the earlier Fourier branches, this run changes mechanism on the same target and proves a direct product/coarea theorem for the exact zero-physical-pivot branch. The theorem also yields a genuine integrated `L2` Fourier estimate.

## New theorem: nonsingular physical triple with one zero diagonal

**Theorem (QFORM-ZERO-DIAGONAL-TRIPLE-v1).** Let `X=(X_1,...,X_n)` have independent real coordinates with densities `0<=f_i<=1`. Let `A` be any real symmetric matrix. Suppose that for some three physical coordinates `I={i,j,k}`, the principal block `B=A[I,I]` is nonsingular and one of its diagonal entries is zero. Then `Q=X^T A X` has an essentially bounded density and

\[
\boxed{\quad \|p_Q\|_\infty\le 3\,2^{2/3}\,|\det B|^{-1/3}.\quad}
\]

No assumption is made on signs, the remaining coordinates, the outside couplings, or the other eigenvalues. The proof is uniform under arbitrary linear terms in the selected three variables, so conditioning on all other coordinates is legitimate. Continuity is **not** proved by this argument.

Consequently, under the same hypothesis,

\[
\int_{\mathbb R}|\phi_Q(t)|^2\,dt
=2\pi\|p_Q\|_2^2
\le 6\pi\,2^{2/3}|\det B|^{-1/3}.
\]

This is an integrated Fourier bound on this branch, but it is `L2`, not the still-open target-wide `L1` estimate.

## Three-variable affine theorem

It is enough to prove the following conditional statement. Let `X,Y,Z` be independent probability variables with densities `f_1,f_2,f_3<=1`. Let

\[
B=\begin{pmatrix}
0&a&b\\
a&c&d\\
b&d&e
\end{pmatrix},\qquad D:=|\det B|>0,
\]

and allow an arbitrary affine perturbation `2 ell_1 x+2 ell_2 y+2 ell_3 z+c_0`. Then the resulting scalar polynomial has density bounded by `3*2^(2/3) D^(-1/3)`.

Because `det B!=0`, `(a,b)!=(0,0)`. Put

\[
\rho^2=a^2+b^2,
\qquad r_0=ay+bz,
\qquad w=-by+az.
\]

The inverse transform is

\[
y=\frac{a r_0-bw}{\rho^2},\qquad
z=\frac{b r_0+aw}{\rho^2},
\]

with Jacobian `dy dz = rho^(-2) dr_0 dw`. After translating `r=r_0+ell_1`, the joint density of `(r,w)` is a translate of

\[
g(r,w)=\rho^{-2}
 f_2\!\left(\frac{a r-bw}{\rho^2}\right)
 f_3\!\left(\frac{b r+aw}{\rho^2}\right),
\]

so

\[
0\le g\le \rho^{-2},\qquad \iint g=1.
\]

The polynomial takes the form

\[
P(x,r,w)=2xr+h(r,w),
\]

where `h` is quadratic-affine in `(r,w)`. Let `gamma` be the coefficient of `w^2` in `h`.

### Exact determinant identity

In coordinates `(x,r_0,w)`, the quadratic matrix is

\[
B'=T^TBT,
\quad
T=\begin{pmatrix}
1&0&0\\
0&a/\rho^2&-b/\rho^2\\
0&b/\rho^2&a/\rho^2
\end{pmatrix}.
\]

Its first row is `(0,1,0)`, hence

\[
\det B'=-\gamma.
\]

Also `det T=rho^(-2)`, so

\[
\det B'=\rho^{-4}\det B.
\]

Therefore

\[
\boxed{\quad |\gamma|=D/\rho^4.\quad}
\]

This identity is the determinant cancellation that makes the final bound independent of the physical row scale `rho`.

### A one-dimensional quadratic rearrangement bound

For every probability density `0<=f<=1`, every `A in R`, and every nonzero `kappa`,

\[
\int_{\mathbb R} f(A-\kappa u^2)\,du\le \frac{2}{\sqrt{|\kappa|}}.
\]

Indeed, after `v=|kappa|u^2`, the integral equals

\[
|\kappa|^{-1/2}\int_0^\infty f(A\mp v)v^{-1/2}\,dv.
\]

The kernel `v^{-1/2}` is decreasing. Subject to `0<=f<=1` and total mass at most one on the relevant half-line, the integral is maximized by placing unit density on `[0,1]`; its value is `2`.

### Exact density formula and two complementary bounds

For almost every `s`, integrate the delta function in `x`. Since the set `r=0` has two-dimensional Lebesgue measure zero,

\[
p_P(s)
=\iint \frac{g(r,w)}{2|r|}
 f_1\!\left(\frac{s-h(r,w)}{2r}\right)\,dw\,dr.
\]

For fixed `r`, complete the square

\[
h(r,w)=\gamma(w-\omega(r))^2+\eta(r).
\]

The rearrangement lemma with `|kappa|=|gamma|/(2|r|)` gives

\[
\int f_1\!\left(\frac{s-h(r,w)}{2r}\right)dw
\le 2\sqrt{\frac{2|r|}{|\gamma|}}.
\]

Using `g<=rho^{-2}` and `|gamma|=D/rho^4`,

\[
\frac1{2|r|}\int g(r,w)
 f_1\!\left(\frac{s-h(r,w)}{2r}\right)dw
\le \frac{\sqrt2}{\sqrt D\,\sqrt{|r|}}.
\tag{1}
\]

There is also the normalization bound. If

\[
m(r):=\int g(r,w)dw,
\]

then `m>=0`, `int m=1`, and simply dropping `f_1<=1` gives

\[
\frac1{2|r|}\int g(r,w)
 f_1\!\left(\frac{s-h(r,w)}{2r}\right)dw
\le \frac{m(r)}{2|r|}.
\tag{2}
\]

Split at `R>0`. From (1),

\[
\int_{|r|\le R}\cdots dr
\le \frac{\sqrt2}{\sqrt D}
\int_{-R}^R |r|^{-1/2}dr
=\frac{4\sqrt2\sqrt R}{\sqrt D}.
\]

From (2),

\[
\int_{|r|>R}\cdots dr
\le \frac1{2R}\int m(r)dr
=\frac1{2R}.
\]

Thus

\[
p_P(s)\le \frac{4\sqrt2\sqrt R}{\sqrt D}+\frac1{2R}.
\]

Writing `x=sqrt(R)`, the right side is `C_0 x+(2x^2)^(-1)` with `C_0=4sqrt(2)D^(-1/2)`. The minimizer satisfies `x=C_0^(-1/3)`, and therefore

\[
p_P(s)\le \frac32 C_0^{2/3}
=3\,2^{2/3}D^{-1/3}.
\]

This proves the three-variable theorem.

## Conditioning back to arbitrary dimension

Fix all coordinates outside `I`. The conditional quadratic polynomial in the selected three variables has the same quadratic block `B`; outside couplings only create an arbitrary linear term and constant. The previous bound is uniform in those affine terms. Hence every conditional law has a density bounded by the same constant. Mixing the conditional densities gives the unconditional density and preserves the same `L-infinity` bound.

No rotation of the selected physical variables is used; the only linear change is internal to the two-coordinate `(Y,Z)` integration after conditioning, where its Jacobian and transformed joint density are tracked exactly. Thus there is no claim of post-rotation independence.

## Integrated Fourier consequence

The density is a probability density, so

\[
\|p_Q\|_2^2\le \|p_Q\|_\infty\|p_Q\|_1
\le 3\,2^{2/3}D^{-1/3}.
\]

With `phi_Q(t)=int exp(it s)p_Q(s)ds`, Plancherel yields

\[
\boxed{\quad
\|\phi_Q\|_2^2\le 6\pi\,2^{2/3}D^{-1/3}.
\quad}
\]

This does not establish `phi_Q in L1` and therefore does not by itself give continuity of the density.

## Named partner result applied to an actual inequality

Partner `account02/B02`, run `20260922T153908Z-account02-B02-qform-auto11-7613470a`, proved the square-pivot ridge-effective-dimension theorem. Its concrete `q=1` corollary states that if a genuine physical square has coefficient `d!=0`, a Schur-remainder physical cross block has two singular values at least `sigma`, and the associated ridge leverage obeys `max diag K<=1/2`, then

\[
\|p_Q\|_\infty<\frac{19.470}{\sqrt{|d|\sigma}}.
\tag{3}
\]

Combining (3) with the theorem above gives a rigorous local certificate ladder:

* exact zero pivot plus a nonsingular three-coordinate principal block `B`: `||p_Q||_infty <= 3*2^(2/3)|det B|^(-1/3)`;
* nonzero pivot with the partner's two-singular-value ridge certificate: `||p_Q||_infty < 19.470/sqrt(|d| sigma)`.

In particular the partner inequality gives the explicit universal constant `19.470` on every certified branch satisfying `|d| sigma>=1`, while the new theorem removes the singular `d->0` problem at the exact endpoint whenever the zero-pivot triple is nonsingular.

A second completed partner theorem, `QFORM-COUPLED-2x3-MIXED-FOURIER-v1` from `account02/B02` run `20260922T130957Z-account02-B02-qform-r11`, gives

\[
\|\phi_Q\|_1\le \pi 2^{175/48}3^{-1/4}\Delta^{-3/8}|\delta|^{-1/4}
\]

for its exact rank-two `2x3` cross-block hypotheses. Hence on any instance carrying both a zero-diagonal triple certificate `(D)` and that mixed-Fourier certificate `(Delta,delta)`, one has the actual combined inequality

\[
\|p_Q\|_\infty
\le \min\!\left\{
3\,2^{2/3}D^{-1/3},
5\Delta^{-3/8}|\delta|^{-1/4}
\right\},
\]

and the second branch supplies a continuous representative. The first branch alone supplies only essential boundedness.

## What this does and does not close

This closes a genuine zero-physical-pivot subproblem without any Gaussian, log-concave, compact-support, connected-support, or diagonal-basis assumption. It is not the full spectral theorem: the three-large-eigenvalue hypothesis does not force a uniformly large fixed physical `3x3` determinant, and the live correction set already refutes fixed-small-minor / fixed-rank-three-cut reductions. The singleton-plus-two-banks and Hadamard-type examples therefore remain relevant.

The first essential missing implication is now an aggregate, product-preserving bridge: starting only from three eigenvalues of modulus at least one, show that either a determinant resource of the zero-pivot type can be paid after grouping/averaging physical coordinates, or the partner ridge / mixed-Fourier resource can be paid at dimension-free scale. A fixed local minor extraction is not enough.

The target-wide `L1` characteristic-function criterion remains unresolved; no source-valid counterexample to it is produced in this run. The full QFORM conjecture remains OPEN.

## Corrections honored

The proof does not use law-uniform pointwise quadratic-phase decay, conditional density caps after sum/difference conditioning, generic bounded projected-pair density as a replacement for product provenance, fixed-small-minor dichotomies, or absolute-value phase-Wiener surrogates. The live correction inbox was refreshed immediately before publication.
