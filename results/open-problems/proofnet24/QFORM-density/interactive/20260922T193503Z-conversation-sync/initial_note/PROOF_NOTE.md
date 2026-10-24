# Quadratic-form density: absolute continuity and a separable-perturbation theorem

22 September 2026

**Scope.** This note proves absolute continuity for every nonzero quadratic form under the stated product-density assumptions, recalls the exact diagonal bound, and proves a bounded-continuous-density theorem for a diffuse quadratic component with arbitrary separable perturbations. It does not prove the full three-large-eigenvalue conjecture for every symmetric matrix. The new extension below has a complete analytic argument but has not yet received independent end-to-end review. No novelty claim relative to the entire literature is made.

## 1. The full target

Let X_1,...,X_n be independent real random variables with probability densities f_i satisfying 0 <= f_i <= 1 almost everywhere. For every real symmetric matrix A with at least three eigenvalues of absolute value at least 1, the target is one universal finite C such that

\[
\mathbb P\{X^TAX\in[t,t+h]\}\le Ch\qquad(t\in\mathbb R,\ h>0).
\]

Equivalently, the law has an essentially bounded density at most C. Absolute continuity alone, a diagonal special case, and an estimate assuming a special eigenvector geometry are strictly weaker conclusions.

## 2. Absolute continuity for every nonzero symmetric matrix

**Proposition 1.** Suppose the X_i are independent and absolutely continuous. If A is real symmetric and nonzero, then X^TAX is absolutely continuous. No bound on the input densities, three-eigenvalue assumption, or moment hypothesis is needed.

**Proof.** First suppose a_ii is nonzero for some i. Conditional on all coordinates except X_i, the quadratic form is

\[
a_{ii}X_i^2+bX_i+c
\]

with deterministic b,c. A nonconstant one-variable quadratic maps every absolutely continuous probability law to an absolutely continuous law. Indeed, split its domain at its unique critical point; on each open monotonicity interval the inverse is continuously differentiable locally. Exhausting each interval by compact subintervals away from the critical point shows that the preimage of any Lebesgue-null set is null. The critical point itself has probability zero. Every conditional law is therefore absolutely continuous, and their mixture is absolutely continuous.

Now suppose every diagonal entry is zero. Choose i,j with a_ij nonzero. Write

\[
X^TAX=L(X_{-i})X_i+R(X_{-i}),\qquad
L(X_{-i})=2\sum_{k\ne i}a_{ik}X_k.
\]

The random variable L is absolutely continuous: condition on all its summands except the nonzero multiple 2a_ij X_j. In particular P(L=0)=0. Almost every conditional law given X_{-i} is consequently a nonconstant affine image of the absolutely continuous law of X_i. Its mixture is absolutely continuous. This covers every nonzero symmetric A. QED.

The coarea representation, when desired, is

\[
p_Q(t)=\int_{\{x:x^TAx=t,\ Ax\ne0\}}
\frac{\prod_i f_i(x_i)}{2\lVert Ax\rVert_2}\,d\mathcal H^{n-1}(x)
\quad\text{for a.e. }t.
\]

The critical set ker(A) is Lebesgue-null. This identity identifies the remaining integral to be bounded; it supplies no universal bound by itself.

## 3. Diagonal forms: the bound pi

**Proposition 2.** If A is diagonal and at least three diagonal coefficients have magnitude at least 1, then its output density is bounded by pi. The density has a continuous version.

**Proof.** For a>0 and a random variable X with density f<=1, the variable Y=a(X-b)^2 has density, for y>0,

\[
g_{a,b}(y)=\frac{f(b+\sqrt{y/a})+f(b-\sqrt{y/a})}{2\sqrt{ay}}
\le\frac{1}{\sqrt{ay}}.
\]

Two independent positive square terms with coefficients a,b>0 therefore have convolution density at most

\[
\frac1{\sqrt{ab}}\int_0^s\frac{du}{\sqrt{u(s-u)}}
=\frac{\pi}{\sqrt{ab}}\quad(s>0).
\]

Among three coefficients of magnitude at least 1, two have the same sign. Reflect the sum when both are negative. Their density is bounded by pi. Convolution with the independent remaining terms cannot increase this bound.

For continuity, first convolve the bounded density of the same-sign pair with the L^1 density of the third nonzero square term. If g is bounded and h is integrable, then

\[
\sup_t |(g*h)(t+v)-(g*h)(t)|\le\lVert g\rVert_\infty\lVert h(\cdot+v)-h\rVert_1\to0.
\]

Thus this convolution has a uniformly continuous version. Its integrability and nonnegativity imply that it vanishes at infinity. Further convolution with a probability measure preserves boundedness, continuity, and vanishing at infinity. QED.

This argument uses independence in the original coordinates. Diagonalizing a general symmetric matrix does not preserve that independence.

## 4. A bounded-density theorem stable under all separable perturbations

Let U be an n by r real matrix with orthonormal columns, where r>=3. Denote its rows by u_i^T and put

\[
c_i=\lVert u_i\rVert_2^2,\qquad
\sum_i u_i u_i^T=I_r,\qquad\sum_i c_i=r.
\]

Assume c_i<=1/2 for every i. This is an additional geometric hypothesis: no input coordinate accounts for more than half the squared projection in this r-dimensional component. Let Lambda be any invertible real symmetric r by r matrix and set

\[
B(U)=\prod_{i:c_i>0}(1-c_i)^{-(1-c_i)/2},\qquad
\Delta=|\det\Lambda|.
\]

**Theorem 3 (separable-perturbation extension).** For independent X_i with densities 0<=f_i<=1 and arbitrary real-valued measurable functions V_i, the variable

\[
T=(U^TX)^T\Lambda(U^TX)+\sum_{i=1}^n V_i(X_i)
\]

has a bounded continuous density, vanishing at infinity, and

\[
\boxed{\quad
\lVert p_T\rVert_\infty
\le \frac{r}{r-2}\,B(U)^{2/r}\,\Delta^{-1/r}
\le \frac{er}{r-2}\,\Delta^{-1/r}.
\quad}
\]

The V_i need only be finite almost surely. They need not be smooth, bounded, polynomial, or integrable. In particular they can be arbitrary diagonal quadratic terms plus arbitrary linear terms. The theorem imposes no sign restriction on Lambda. If r=3 and Delta>=1, the bound is at most 3e.

### 4.1. The two classical analytic inputs

Use the Fourier convention

\[
\widehat h(\xi)=\int_{\mathbb R}e^{-i\xi x}h(x)\,dx.
\]

The geometric rank-one Brascamp-Lieb inequality states that, for unit vectors v_i and c_i>0 with sum c_i v_i v_i^T=I_r,

\[
\int_{\mathbb R^r}\prod_i H_i(v_i\cdot\xi)^{c_i}\,d\xi
\le\prod_i\left(\int_{\mathbb R}H_i(s)\,ds\right)^{c_i}
\]

for nonnegative integrable H_i. The precise statement also appears as Theorem 3.3 of Livshyts-Paouris-Pivovarov [2].

Beckner's sharp Hausdorff-Young inequality [1], valid for complex-valued h, states that for 1<=p<=2 and q=p/(p-1),

\[
\lVert\widehat h\rVert_q\le
(2\pi)^{1/q}p^{1/(2p)}q^{-1/(2q)}\lVert h\rVert_p.
\]

These are the only non-elementary inequalities used in Theorem 3. The remaining steps, including the complex-amplitude issue and the oscillatory interchange, are proved below.

### 4.2. A phase-uniform Fourier bound

For a fixed real t, define complex input functions

\[
h_{i,t}(x)=f_i(x)e^{itV_i(x)}.
\]

For every p>=1, their norms satisfy

\[
\lVert h_{i,t}\rVert_p=\lVert f_i\rVert_p\le1.
\]

Let nu_t be the pushforward under x -> U^T x of the complex measure with density product_i h_{i,t}(x_i). Since U^T has full row rank, this measure has a complex L^1 density g_t. To see this directly, complete U to an orthogonal matrix (U,W) and integrate the original density at Uy+Wz over z. Fubini gives

\[
\lVert g_t\rVert_1\le1.
\]

Its Fourier transform is

\[
\widehat g_t(\xi)=\prod_i\widehat h_{i,t}(u_i\cdot\xi).
\]

Zero rows contribute scalar factors of modulus at most 1 and may be omitted in estimates. For c_i>0 set v_i=u_i/sqrt(c_i). Brascamp-Lieb, with

\[
H_i(s)=|\widehat h_{i,t}(\sqrt{c_i}s)|^{1/c_i},
\]

gives

\[
\lVert\widehat g_t\rVert_1
\le\prod_{i:c_i>0}c_i^{-c_i/2}
\lVert\widehat h_{i,t}\rVert_{1/c_i}.
\tag{4.1}
\]

Set q_i=1/c_i and p_i=1/(1-c_i). Because c_i<=1/2, q_i>=2 and p_i<=2, so sharp Hausdorff-Young applies:

\[
\lVert\widehat h_{i,t}\rVert_{1/c_i}
\le(2\pi)^{c_i}(1-c_i)^{-(1-c_i)/2}c_i^{c_i/2}.
\]

The powers of c_i cancel in (4.1), leaving

\[
\boxed{\lVert\widehat g_t\rVert_1\le(2\pi)^rB(U).}
\tag{4.2}
\]

This bound is uniform in t and in every V_i. Finally,

\[
-(1-c)\log(1-c)\le c\quad(0\le c<1)
\]

and sum c_i=r imply

\[
B(U)\le e^{r/2}.
\tag{4.3}
\]

### 4.3. Gaussian-regularized quadratic integration

The characteristic function of T is exactly

\[
\varphi_T(t)=\int_{\mathbb R^r}e^{it y^T\Lambda y}g_t(y)\,dy.
\]

There is no claim that the separable perturbation is independent of U^T X. Its entire dependence was retained in the complex density g_t.

For epsilon>0 and t nonzero, introduce

\[
I_\varepsilon(t)=\int e^{it y^T\Lambda y-\varepsilon|y|^2}g_t(y)\,dy.
\]

By (4.2), Fourier inversion for g_t and absolutely justified Fubini yield

\[
I_\varepsilon(t)=(2\pi)^{-r}\int\widehat g_t(\xi)K_{\varepsilon,t}(\xi)\,d\xi,
\]

where

\[
K_{\varepsilon,t}(\xi)=\int e^{-\varepsilon|y|^2+it y^T\Lambda y+i\xi\cdot y}\,dy.
\]

Diagonalize Lambda orthogonally inside this Gaussian integral. If its eigenvalues are lambda_j and the rotated frequency is eta, the j-th factor is

\[
\sqrt\pi\,(\varepsilon-it\lambda_j)^{-1/2}
\exp\!\left(-\frac{\eta_j^2}{4(\varepsilon-it\lambda_j)}\right).
\]

Its exponential has modulus at most 1 because

\[
\operatorname{Re}(\varepsilon-it\lambda_j)^{-1}
=\frac{\varepsilon}{\varepsilon^2+t^2\lambda_j^2}>0.
\]

Consequently,

\[
|K_{\varepsilon,t}(\xi)|
\le\pi^{r/2}\prod_j(\varepsilon^2+t^2\lambda_j^2)^{-1/4}
\le\pi^{r/2}|t|^{-r/2}\Delta^{-1/2}.
\]

Combining this with (4.2) gives

\[
|I_\varepsilon(t)|\le B(U)\pi^{r/2}|t|^{-r/2}\Delta^{-1/2}.
\]

For each fixed t, g_t is integrable, so dominated convergence as epsilon decreases to zero yields

\[
|\varphi_T(t)|\le\min\{1,K|t|^{-r/2}\},
\qquad K=B(U)\pi^{r/2}\Delta^{-1/2}.
\tag{4.4}
\]

This is not a stationary-phase estimate for arbitrary one-dimensional positive densities. It relies essentially on the diffuse-frame hypothesis and a phase-uniform, frequency-integrated product estimate.

### 4.4. Integration and density inversion

Let t_0=K^{2/r}. Since r>2,

\[
\begin{aligned}
\int_{\mathbb R}|\varphi_T(t)|\,dt
&\le2\left[t_0+K\int_{t_0}^\infty t^{-r/2}\,dt\right]\\
&=2\frac{r}{r-2}K^{2/r}.
\end{aligned}
\]

Thus phi_T belongs to L^1(R). Fourier inversion gives a bounded continuous density vanishing at infinity and

\[
\lVert p_T\rVert_\infty
\le\frac1{2\pi}\lVert\varphi_T\rVert_1
\le\frac{r}{r-2}B(U)^{2/r}\Delta^{-1/r}.
\]

Equation (4.3) supplies the simpler bound er/(r-2) times Delta^(-1/r). This proves Theorem 3. QED.

## 5. Consequences for matrices with unrestricted remaining terms

**Corollary 4 (diagonal perturbations).** Theorem 3 applies to

\[
A=D+U\Lambda U^T
\]

for every real diagonal D, with the same constant, and it allows any linear term in Q. The spectrum of the full matrix A need not have rank r or be bounded away from zero. The determinant in the bound is that of the specified component Lambda, not the product of eigenvalues of A.

**Corollary 5 (a principal block suffices).** Let I be a set of original coordinate indices. Suppose the physical principal block A_II has a representation

\[
A_{II}=D+U\Lambda U^T
\]

satisfying Theorem 3. Every other block of A, including the couplings between I and its complement, may be arbitrary. Then X^TAX has the same bounded-continuous-density estimate.

**Proof.** Conditional on X_{I^c}=z, the form is

\[
X_I^TA_{II}X_I+2X_I^TA_{I,I^c}z+z^TA_{I^c,I^c}z.
\]

The conditional X_I retain their original independent densities. Absorb the displayed linear term and the diagonal quadratic terms into the V_i. Theorem 3 provides (4.4) uniformly in z; a constant phase has modulus one. Averaging the conditional characteristic functions preserves (4.4), so the same L^1 inversion argument proves the corollary. QED.

For input bounds f_i<=M_i instead of 1, the same calculation replaces B(U) by B(U) product_i M_i^(c_i). In particular a common bound M introduces exactly the expected M^2 factor in the final density estimate.

### A concrete full-rank indefinite example

Take n=6, r=3,

\[
U=\frac1{\sqrt2}\begin{pmatrix}I_3\\I_3\end{pmatrix},\qquad
\Lambda=\operatorname{diag}(2,2,-2),\qquad D=\tfrac1{10}I_6.
\]

Every leverage equals 1/2. The full matrix A=D+U Lambda U^T has eigenvalues

\[
21/10,\quad21/10,\quad-19/10,\quad1/10,\quad1/10,\quad1/10.
\]

It meets the original three-large-eigenvalue condition, is not diagonal in the independent input coordinates, is indefinite, and has three additional small nonzero eigenvalues. Here B(U)=2^(3/2), Delta=8, so Theorem 3 gives

\[
\lVert p_{X^TAX}\rVert_\infty\le3.
\]

The example illustrates a covered family, not a universal matrix reduction.

## 6. What remains for the full conjecture

The extension removes a real limitation of the earlier diffuse-rank theorem: a diagonal or separable remainder is not independent noise, yet it can be retained exactly without worsening the bound. The principal-block corollary also permits arbitrary couplings outside a suitable physical block.

Two gaps remain. First, the spectral hypothesis alone does not establish a representation A=D+U Lambda U^T with all leverage scores at most 1/2 and determinant bounded below. Second, no argument above covers every leverage-heavy geometry or an arbitrary nonseparable remainder by simply adding its phase. For c_i>1/2 the attempted Fourier step would require an L^q estimate with q<2, outside the available Hausdorff-Young range. A new inequality or a genuine product-preserving reduction is needed there.

The full target therefore remains unproved in this note. No conditional implication is being presented as an unconditional solution.

## 7. Sources and provenance

[1] W. Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159-182. DOI: 10.2307/1970980. Publisher record: https://annals.math.princeton.edu/1975/102-1/p11 . The precise sharp Hausdorff-Young inequality is the imported classical input.

[2] G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949. Theorem 3.3 states the normalized geometric Brascamp-Lieb inequality used above. https://arxiv.org/pdf/1507.07949 . Their marginal-density theorem alone is not a proof of the nonlinear target.

[3] The existing diffuse-rank argument being extended: private research archive `yspennstate/math-open-problems`, commit `0b5925a458d36c1ec1cf8ab344c9676260a97c8a`, file `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T113624Z-qform11/REPORT.md`, blob `212febc02c4c1f3a8e6c073d0a8ed5d2d6b4ea0a`. Its unperturbed Fourier/Brascamp-Lieb calculation was read directly. The new step is the complex product amplitude retaining arbitrary separable phases, followed by the principal-block conditioning corollary.

[4] Exact target, diagonal control, and pointwise-decay correction: private coordination archive `yspennstate/math-research-brain`, snapshot `df47cd8f7a0dd4bf831ff4e659d4dc064528f72d`, file `scheduled_tasks/work/shared/qform-density-2026-09-22/CURRENT_RESEARCH.md`, blob `c8e8cd4d7065799e210a55810a500bbf589cd103`.

A finite algebraic sanity check accompanies this note; it verifies the explicit example and scalar prefactors only. It is not a proof of the universal conjecture or a substitute for review of Theorem 3. This interactive derivation is not an independent scheduled-worker review and is not native learned-memory ingestion.
