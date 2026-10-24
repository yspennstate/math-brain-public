SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B15, 2026-09-22T20:05:44Z.
attacking: the qualitative regularity closure independently; verify and complete the zero-diagonal rough-input C0 mechanism, apply completed account03/B15 nonzero-diagonal result, and keep the universal height implication separate.

# QFORM B15 r11 — full fixed-matrix regularity, universal height still open

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `account02/B15`  
**Run:** `20260922T200544Z-account02-B15-qform-r11`  
**Fresh control before publication:** `yspennstate/math-research-brain@200ae47caf9830c8810adcf4c513470ba03c8d6d`, OWNER CONTROL revision `2026-09-22.15`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `TARGET_LEVEL_REGULARITY_PROOF / UNIVERSAL_HEIGHT_OPEN`

## 1. First unpaid implication

The owner target remains the matrix- and dimension-uniform estimate

\[
\sup_{\substack{A:\;\#\{|\lambda(A)|\ge1\}\ge3\\ f_i\le1\text{ independent}}}
\|p_{X^TAX}\|_\infty<\infty.
\]

This report does **not** prove that estimate. The new result is qualitative but target-wide:

> **Theorem.** For every fixed real symmetric `A` with `rank(A)>=3`, and every collection of independent real variables with probability densities bounded by one, `Q=X^TAX` has an instance-dependent bounded density with a representative in `C_0(R)`.

The constants below depend on physical entries/minors of `A`; they can deteriorate along diffuse matrices. Thus continuity and fixed-matrix boundedness are kept separate from the universal-height conjecture.

The theorem closes the remaining zero-physical-diagonal rough-input branch independently and then applies the completed assigned-partner result account03/B15 for the complementary nonzero-diagonal branch.

## 2. Corrections and partner premise actually used

I used no arbitrary-joint rank-three coarea estimate, no positive conditional projection moment, no law-uniform pointwise oscillatory decay, no independence after spectral rotation, and no dimension-free fiber supremum. Those interfaces are corrected/refuted in the live state.

Completed assigned-partner result actually applied:

- `account03/B15`, `yspennstate/math-open-problems@d73760eb784a86c356c64f05dd92f84655618f02`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260922T153101Z-account03-B15-r12/REPORT.md`.

Its high-dimensional theorem proves

\[
\operatorname{rank}(A)\ge3,\quad \exists j\;A_{jj}\ne0
\quad\Longrightarrow\quad
p_{X^TAX}\in C_0(\mathbb R),
\]

with a finite bound depending on a selected physical block, uniformly over all cap-one product laws. I use exactly that scope in Section 8.

A concurrent account03/B15 candidate (`math-open-problems@ad09656b2fda9de070137f9df96550d87f73f278`) contains a closely related zero-diagonal stability argument. I re-derived the zero-diagonal proof below rather than treating that unfinished candidate as a completed premise.

## 3. Baseline: absolute continuity is much weaker

Let `A` be any nonzero real symmetric matrix and let `X` have any absolutely continuous joint law (product structure is not needed here). Put `q(x)=x^TAx`. For a null set `N subset R`, use the coarea formula on

\[
E_k=\{x:|x|\le k,\ |\nabla q(x)|\ge1/k\}.
\]

Since `q` is locally Lipschitz,

\[
\int_{E_k\cap q^{-1}(N)}|\nabla q(x)|\,dx
=\int_N \mathcal H^{n-1}(E_k\cap q^{-1}(t))\,dt=0.
\]

Hence `Leb(E_k cap q^{-1}(N))=0`. The complement of the union of the `E_k` is contained, up to a null set, in the critical set `ker A`, which is a proper linear subspace because `A!=0`. Therefore `q^{-1}(N)` is Lebesgue-null and every absolutely continuous input law pushes forward to an absolutely continuous output law.

This proves existence of a density only. It supplies no uniform or even fixed-matrix `L^infinity` estimate.

## 4. Smooth compact product inputs give C0 for every rank >= 3 matrix

This is the approximation endpoint used later.

Assume each marginal is `C_c^infinity` and let `F(x)=prod_i f_i(x_i)`. Orthogonally diagonalize `A`. If `r=rank(A)>=3`, after integrating the null directions the characteristic function has the form

\[
\phi(t)=\int_{\mathbb R^r}e^{it y^T\Lambda y}a(y)\,dy,
\]

where `Lambda` is invertible diagonal and `a in C_c^infinity(R^r)`. Fourier inversion for `a` and the exact Fresnel integral give

\[
|\phi(t)|\le
(2\pi)^{-r}\|\widehat a\|_1\,\pi^{r/2}|\det\Lambda|^{-1/2}|t|^{-r/2},
\qquad |t|\ge1.
\]

(The identity is obtained rigorously by inserting a Gaussian regulator and passing to the limit.) Since `r>=3`, `phi in L^1(R)`. Fourier inversion therefore gives a bounded continuous output density, and the Riemann--Lebesgue lemma gives its vanishing at infinity:

\[
p_Q\in C_0(\mathbb R).
\]

No independence is asserted after the orthogonal rotation; the entire rotated joint density is kept as the smooth amplitude `a`.

Every cap-one one-dimensional density has cap-preserving compactly supported smooth approximants in `L^1`: truncate to mass `1-delta`, mollify (which preserves the cap one), and place the missing mass `delta` in a disjoint far-away smooth bump whose height is at most one. Thus it remains only to obtain a fixed-matrix `L^1`-input to `L^infinity`-output stability modulus for the rough zero-diagonal case.

## 5. A product-variation kernel

Let `0<=h<=1` have mass `delta`, and let `0<=g<=1` be a probability density. The density of the product of independent variables having these (sub)density factors satisfies, for `s!=0`,

\[
k(s)=\int h(u)g(s/u)\frac{du}{|u|}.
\]

For any `r>0`, split at `|u|=r`. On the exterior use `g<=1`; the bathtub principle for `h` gives

\[
\int_{|u|\ge r}\cdots\le2\log\left(1+\frac{\delta}{2r}\right).
\]

On the interior substitute `v=s/u`, use `h(s/v)<=1`, and apply the same bathtub bound to the probability density `g`:

\[
\int_{|u|<r}\cdots\le2\log\left(1+\frac r{2|s|}\right).
\]

Choosing `r=sqrt(delta |s|)` yields

\[
\boxed{\ k(s)\le\Phi_\delta(s):=
4\log\left(1+\frac12\sqrt{\frac\delta{|s|}}\right).\ }
\tag{5.1}
\]

Now suppose a random variable `W` obeys

\[
\Pr(|W|\le\rho)\le\min(1,L\sqrt\rho).
\tag{5.2}
\]

Set

\[
\Omega(a)=2a\log(1+2/a)+4\log(1+a/2),\qquad \Omega(0)=0.
\]

Writing `R=|W|/delta`, differentiating
`Psi(r)=4 log(1+1/(2sqrt(r)))`, and integrating by parts against the bound in (5.2) gives exactly

\[
\boxed{\ \mathbb E\Phi_\delta(W)\le\Omega(L\sqrt\delta).\ }
\tag{5.3}
\]

Indeed `-Psi'(r)=2/[r(2sqrt(r)+1)]`; with `x=sqrt(r)` the resulting integral is

\[
\int_0^\infty\min(1,ax)\frac4{x(2x+1)}\,dx,
\]

whose split at `x=1/a` is precisely `Omega(a)`. In particular `Omega(L sqrt(delta))->0`.

## 6. Zero-diagonal matrices: triangle branch

Assume `diag(A)=0` and the physical support graph contains a triangle. Condition on every coordinate outside three triangle vertices. Up to relabeling, the conditional polynomial is

\[
2axy+2bxz+2cyz+\ell_1x+\ell_2y+\ell_3z+d,
\qquad abc\ne0.
\]

For fixed `z`, put

\[
U=x+(c/a)z+\ell_2/(2a),\qquad
V=y+(b/a)z+\ell_1/(2a).
\]

Then the polynomial is `2aUV+H(z)`, where the quadratic coefficient of `H` is `-2bc/a`.

Replace the `x` marginal by another cap-one marginal at `L^1` distance `delta`. The absolute marginal difference is a cap-one subdensity of mass `delta`. By (5.1), the conditional output-density difference at `t`, after fixing `z`, is at most

\[
\frac1{2|a|}\Phi_\delta\left(\frac{t-H(z)}{2a}\right).
\]

The argument

\[
W=(t-H(Z))/(2a)
\]

is a one-dimensional quadratic whose quadratic coefficient has magnitude `|bc|/a^2`. Since the density of `Z` is at most one, the preimage of an interval of length `2rho` under a nonconstant quadratic has length at most `2sqrt(2rho/|alpha|)`. Hence

\[
\Pr(|W|\le\rho)\le
\frac{2\sqrt2|a|}{\sqrt{|bc|}}\sqrt\rho.
\]

Equation (5.3) yields the uniform modulus

\[
\boxed{
\|p_f-p_g\|_\infty\le
\omega_x(\delta):=
\frac1{2|a|}\Omega\left(
\frac{2\sqrt2|a|}{\sqrt{|bc|}}\sqrt\delta
\right).
}
\tag{6.1}
\]

The same argument gives `omega_y`, and using the pair `(x,z)` gives

\[
\omega_z(\delta)=
\frac1{2|b|}\Omega\left(
\frac{2\sqrt2|b|}{\sqrt{|ac|}}\sqrt\delta
\right).
\tag{6.2}
\]

All tend to zero. Taking `delta=1` in the same calculation also yields an affine-uniform conditional core height

\[
M_T=\frac1{2|a|}\Omega\left(
\frac{2\sqrt2|a|}{\sqrt{|bc|}}
\right)<\infty.
\tag{6.3}
\]

Therefore replacement of any outside marginal at `L^1` distance `delta` changes the full output density by at most `M_T delta`.

## 7. Zero-diagonal matrices: triangle-free branch

Assume now `diag(A)=0`, `rank(A)>=3`, and the support graph is triangle-free. Choose a nonzero edge `{i,j}` with weight `a=A_ij`. The principal pivot

\[
P=\begin{pmatrix}0&a\\a&0\end{pmatrix}
\]

is invertible. Its Schur complement `S` on the remaining coordinates has rank `rank(A)-2>=1`. For every remaining `k`,

\[
S_{kk}=-2A_{ki}A_{kj}/a=0
\]

because triangle-freeness prevents both factors from being nonzero. Thus the nonzero symmetric matrix `S` has some off-diagonal entry `S_kl!=0`.

The principal four-block on `{i,j,k,l}` is invertible, since its Schur complement relative to `P` is

\[
\begin{pmatrix}0&S_{kl}\\S_{kl}&0\end{pmatrix}.
\]

Every triangle-free graph on four vertices is bipartite; invertibility excludes a `1+3` bipartition. After permutation the block is therefore

\[
B=\begin{pmatrix}0&C\\ C^T&0\end{pmatrix},\qquad C\in GL_2(\mathbb R).
\tag{7.1}
\]

Conditioning outside the block adds only affine terms. Since `C` is invertible, translations of the two original-coordinate pairs remove those affine terms while preserving independence and cap one, so the core is `2U^TCV`.

For fixed `u`, the density of `2u^TCV` in the independent pair `V` is at most

\[
\frac1{\sqrt2\,\|C^Tu\|}
\le\frac1{\sqrt2\,\sigma_{\min}(C)|u|}.
\]

If `0<=F<=1` is a planar subdensity of mass `delta`, the planar bathtub principle gives

\[
\int_{\mathbb R^2}\frac{F(u)}{|u|}\,du\le2\sqrt{\pi\delta}.
\]

Hence changing any one of the four block marginals by `L^1` distance `delta` changes the output density by at most

\[
\boxed{
\|p_f-p_g\|_\infty\le
\frac{\sqrt{2\pi\delta}}{\sigma_{\min}(C)}.
}
\tag{7.2}
\]

At `delta=1` the same argument gives the affine-uniform conditional core bound

\[
M_B=\frac{\sqrt{2\pi}}{\sigma_{\min}(C)}.
\tag{7.3}
\]

Therefore an outside-marginal replacement costs at most `M_B` times its `L^1` distance.

## 8. Rough zero-diagonal outputs are C0, and partner completion of the other branch

Fix `diag(A)=0`, `rank(A)>=3`, and arbitrary cap-one product marginals. Let `f_i^(m)` be the cap-preserving compactly supported smooth approximants from Section 4, with

\[
\delta_{i,m}=\|f_i^{(m)}-f_i\|_1\to0.
\]

For each `m`, Section 4 gives a density `p_m in C_0(R)`.

In the triangle case, telescope the marginals and apply (6.1)--(6.3):

\[
\|p_m-p\|_\infty
\le
\omega_x(\delta_{1,m})+
\omega_y(\delta_{2,m})+
\omega_z(\delta_{3,m})+
M_T\sum_{j\notin T}\delta_{j,m}
\longrightarrow0.
\]

In the triangle-free case, (7.2)--(7.3) give

\[
\|p_m-p\|_\infty
\le
\frac{\sqrt{2\pi}}{\sigma_{\min}(C)}
\sum_{j\in B}\sqrt{\delta_{j,m}}
+M_B\sum_{j\notin B}\delta_{j,m}
\longrightarrow0.
\]

The product input measures converge in total variation, hence their quadratic pushforwards do too, so the uniform limit is a density of the original output. Since `C_0(R)` is closed under uniform convergence,

\[
\boxed{
\operatorname{diag}(A)=0,\ \operatorname{rank}(A)\ge3
\Longrightarrow p_{X^TAX}\in C_0(\mathbb R)\cap L^\infty(\mathbb R).
}
\tag{8.1}
\]

Now apply the completed assigned-partner theorem `account03/B15@d73760e...`, which handles every rank-`>=3` matrix with some nonzero physical diagonal entry. The two physical classes exhaust all symmetric matrices. Therefore

\[
\boxed{
\operatorname{rank}(A)\ge3
\Longrightarrow
p_{X^TAX}\in C_0(\mathbb R)\cap L^\infty(\mathbb R)
\quad\text{for every cap-one product law.}
}
\tag{8.2}
\]

All bounds in (8.2) are **instance-dependent**. Under the owner hypothesis of three eigenvalues with modulus at least one, rank is at least three, so (8.2) covers every target instance qualitatively.

## 9. Exact implication ledger and strict controls

Under the target hypotheses we now have, for each fixed instance,

\[
\boxed{
C_0\text{ density}\ \Longrightarrow\ \text{continuous density}\ \Longrightarrow\ \text{absolute continuity},
}
\]

and `C_0` also gives a finite instancewise `L^infinity` norm. The essential-boundedness and continuity statements here are proved from the product/quadratic structure; neither is being inferred from the other.

Outside this structural theorem the logical implications are strict:

1. **Absolute continuity does not imply essential boundedness.** If `X` is uniform on `[0,1]`, then `X^2` has density `1/(2sqrt(t))` on `(0,1)`.
2. **Essential boundedness does not imply a continuous representative.** If `X,Y` are independent uniform `[0,1]`, then `X^2+Y^2` has density `pi/4` for `0<t<1` and density zero for `t<0`; no value assigned at zero can make it continuous there.

Most importantly, the proved instancewise statement

\[
\forall(A,f)\quad \|p_{A,f}\|_\infty<\infty
\]

does **not** imply the owner's required quantifier reversal

\[
\sup_{(A,f)\text{ target}}\|p_{A,f}\|_\infty<\infty.
\]

That is the first unpaid implication.

Because every target output now has a `C_0` representative, each individual supremum is actually attained. Thus the full conjecture can equivalently be written

\[
\boxed{
\sup_{(A,f)\text{ target}}\ \max_{t\in\mathbb R}p_{A,f}(t)<\infty.
}
\tag{9.1}
\]

This removes representative/tail ambiguity but gives no uniform constant. The local constants in Sections 6--8 contain quantities such as `1/|a|`, `1/sqrt(|bc|)`, and `1/sigma_min(C)`, which need not be uniformly controlled by the three-large-eigenvalue hypothesis. The live correction state already contains diffuse families defeating one-minor/cross-rank dichotomies. Universal height must therefore aggregate original-coordinate product structure before paying reciprocal local-minor costs.

## 10. Integrity ledger

- Full universal QFORM constant: **OPEN / NOT PROVED**.
- Valid counterexample to full QFORM: **none produced**.
- Absolute continuity: proved for every nonzero quadratic under any absolutely continuous joint input.
- Fixed-matrix target essential boundedness: proved for every rank-`>=3` matrix, with matrix-dependent constant.
- Fixed-matrix target continuity/vanishing: proved `C_0` for every rank-`>=3` matrix.
- Completed partner applied: account03/B15 nonzero-diagonal theorem at `d73760eb784a86c356c64f05dd92f84655618f02`.
- Concurrent account03/B15 zero-diagonal candidate was checked but not used as an unreviewed premise.
- No moment, support, smoothness, connectedness, sign, Gaussian, or post-rotation independence assumption was added to the rough-input theorem.
- No refuted conditional-moment, arbitrary-joint coarea, pointwise-decay, fiber-supremum, one-minor, or raw-Wiener shortcut was used.

**Next mathematical step:** retain the actual attained-peak formulation (9.1) and seek a product-coordinate aggregate-curvature / grouped-bank inequality with a uniform constant; qualitative regularity itself is no longer the missing bridge.
