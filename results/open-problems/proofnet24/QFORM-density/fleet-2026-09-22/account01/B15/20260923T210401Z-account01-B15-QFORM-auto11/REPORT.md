SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T21:04:01Z.
attacking: near-endpoint regularity of the surviving bilinear-plus-square branch: combine account02/B15's sharp product Fourier L2 theorem with square Lq control, and determine exactly what finite-Lr/continuity information follows without falsely promoting it to L-infinity.

# account01/B15 — sharp finite-L^r ladder for an independent bilinear-plus-square block

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** absolute continuity and regularity  
**Run:** `20260923T210401Z-account01-B15-QFORM-auto11`  
**Fresh publication control:** `yspennstate/math-research-brain@9d8d520585f676828aae45dfe7a1cbdb952ca661`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `SUPPORTING_REGULARITY_THEOREM / PARTNER_RESULT_APPLIED / FULL QFORM OPEN`

## 1. Scope and corrections

The unrestricted theorem remains open. This report proves a scale-explicit finite-L^r theorem for a genuine original-coordinate product block of the form bilinear-plus-square, including arbitrary affine terms and an independent remainder. It does **not** claim that this strict split is forced by the three-large-eigenvalue hypothesis.

No law-uniform pointwise quadratic Fourier decay is used. No orthogonal rotation is used to assert independence. No projection-only or X-ray-only estimate is used. The only product decomposition below is an actual independence hypothesis on the variables entering the displayed block.

The completed designated-partner input actually applied is account02/B15's sharp product endpoint, recorded at `yspennstate/math-open-problems@b1f2bf19f7f3a04b62b74af97b1f0d3b0ce592e6`: if `H,L` are independent with probability densities bounded by one and `G` is the density of `HL`, then

\[
\|G\|_2^2\le 4.
\tag{1.1}
\]

Equivalently, after the normalization `2aHL`,

\[
\boxed{\ \|p_{2aHL}\|_2\le \sqrt{\frac{2}{|a|}}.\ }
\tag{1.2}
\]

The same partner report shows why the corresponding absolute-Fourier Hölder route stops exactly at the endpoint: uniform product-characteristic-function control below `L^2_t` is false, while the generic square Fresnel factor needs a conjugate exponent strictly above two. The theorem below records what one can nevertheless obtain on the **density side** at every finite output exponent.

## 2. Sharp L^p bound for a cap-one square

Let `V` have probability density `f` with `0<=f<=1`, and put `Y=V^2`. For `y>0`,

\[
h(y)=\frac{f(\sqrt y)+f(-\sqrt y)}{2\sqrt y}.
\tag{2.1}
\]

Write

\[
A(x)=f(x)+f(-x),\qquad x>0.
\]

Then `0<=A<=2` and

\[
\int_0^\infty A(x)\,dx=1.
\tag{2.2}
\]

For every `1<=p<2`, changing variables `y=x^2` gives

\[
\|h\|_p^p
=2^{1-p}\int_0^\infty A(x)^p x^{1-p}\,dx.
\tag{2.3}
\]

Since `A^p<=2^{p-1}A`,

\[
\|h\|_p^p
\le \int_0^\infty A(x)x^{1-p}\,dx.
\tag{2.4}
\]

The weight `x^{1-p}` is decreasing. Under the constraints `0<=A<=2` and `int A=1`, the bathtub principle places all mass at the origin: `A=2 1_(0,1/2)`. Hence

\[
\int_0^\infty A(x)x^{1-p}\,dx
\le 2\int_0^{1/2}x^{1-p}\,dx
=\frac{2^{p-1}}{2-p}.
\tag{2.5}
\]

Therefore

\[
\boxed{
\|p_{V^2}\|_p
\le
\left(\frac{2^{p-1}}{2-p}\right)^{1/p},
\qquad 1\le p<2.
}
\tag{2.6}
\]

The constant in (2.6) is sharp: equality holds for `V` uniform on `[-1/2,1/2]`. Scaling gives, for every nonzero `lambda`,

\[
\boxed{
\|p_{\lambda V^2}\|_p
\le
|\lambda|^{-1+1/p}
\left(\frac{2^{p-1}}{2-p}\right)^{1/p}.
}
\tag{2.7}
\]

Notice the exact endpoint obstruction: the right-hand side diverges as `p upward 2`, and the uniform example indeed has a `y^{-1/2}` square-root singularity whose square is nonintegrable at the vertex.

## 3. New theorem: a finite-L^r ladder for bilinear plus square

### Theorem 3.1

Let `H,L,V` be independent real random variables, each with a probability density bounded by one. Let `a lambda !=0`. Let `R` be any random variable independent of `(H,L,V)`; no density or moment assumption on `R` is needed. Allow arbitrary real affine coefficients `alpha,beta,gamma,c`, and set

\[
Q=2aHL+\lambda V^2+\alpha H+\beta L+\gamma V+c+R.
\tag{3.1}
\]

Then `Q` has a density. For every `2<=r<infinity`,

\[
\boxed{
\|p_Q\|_r
\le C_r\,|a|^{-1/2}|\lambda|^{-1/2+1/r},
\qquad
C_r=2^{-3/r}(r+2)^{(r+2)/(2r)}.
}
\tag{3.2}
\]

For `1<=r<=2`,

\[
\boxed{
\|p_Q\|_r
\le
\left(\frac{2}{|a|}\right)^{1-1/r}.
}
\tag{3.3}
\]

In particular, if `|a|,|lambda|>=1`, then every finite `L^r` norm is bounded uniformly over all admissible laws, but the constants produced by this sharp-endpoint interpolation grow like

\[
C_r\sim\sqrt r\qquad(r\to\infty).
\tag{3.4}
\]

Thus this chain does not furnish an `L^infinity` estimate by passage to the endpoint.

### Proof

First remove the affine terms by translations **before doing any estimate**. We have

\[
2aHL+\alpha H+\beta L
=2a\left(H+\frac{\beta}{2a}\right)
       \left(L+\frac{\alpha}{2a}\right)
 -\frac{\alpha\beta}{2a},
\tag{3.5}
\]

and

\[
\lambda V^2+\gamma V
=\lambda\left(V+\frac{\gamma}{2\lambda}\right)^2
 -\frac{\gamma^2}{4\lambda}.
\tag{3.6}
\]

The three translated variables are still independent and their densities are still bounded by one. Constants do not affect density norms. Hence it suffices to prove the theorem for

\[
Q_0=2aHL+\lambda V^2.
\tag{3.7}
\]

The two summands in (3.7) are independent. By the completed account02/B15 endpoint theorem, applied at the actual scaled variable,

\[
\|p_{2aHL}\|_2\le\sqrt{2/|a|}.
\tag{3.8}
\]

Fix `r>=2` and choose

\[
p=\frac{2r}{r+2}.
\tag{3.9}
\]

Then `1<=p<2` and

\[
1+\frac1r=\frac12+\frac1p.
\tag{3.10}
\]

Young's convolution inequality, (3.8), and the sharp square estimate (2.7) give

\[
\|p_{Q_0}\|_r
\le \sqrt{\frac2{|a|}}
|\lambda|^{-1+1/p}
\left(\frac{2^{p-1}}{2-p}\right)^{1/p}.
\tag{3.11}
\]

Since

\[
-1+\frac1p=-\frac12+\frac1r,
\tag{3.12}
\]

and a direct substitution of `p=2r/(r+2)` yields

\[
\sqrt2\left(\frac{2^{p-1}}{2-p}\right)^{1/p}
=2^{-3/r}(r+2)^{(r+2)/(2r)},
\tag{3.13}
\]

we obtain (3.2).

At `r=2`, (3.2) reduces to

\[
\|p_{Q_0}\|_2\le\sqrt{2/|a|},
\]

because the square factor is used only in `L^1`. For `1<=r<=2`, interpolate between the probability-density norm `||p_Q||_1=1` and this `L^2` estimate to obtain (3.3).

Finally, adding the independent remainder `R` convolves the density with a probability measure. Convolution by a probability measure is an `L^r` contraction for every `1<=r<=infinity`, so all displayed estimates survive unchanged. This proves the theorem. `square`

## 4. What the theorem says about regularity — and what it does not say

The theorem is a genuine class-uniform regularity statement below the endpoint. For the strict split block with `|a|,|lambda|>=1`, the family of output densities is bounded in every `L^r(R)`, `r<infinity`, with an explicit law-independent constant. Yet the interpolation constants grow as `sqrt(r)`, so this does not by itself produce a universal essential supremum.

This is a useful separation of three levels:

1. **Absolute continuity:** already follows under far weaker assumptions. For any nonzero symmetric `A` and any absolutely continuous joint input law, `X^TAX` is absolutely continuous; no rank-three or cap-one assumption is required.
2. **Finite-L^r regularity:** Theorem 3.1 supplies uniform, scale-explicit bounds for every finite exponent in the displayed independent bilinear-plus-square branch.
3. **Continuity:** the completed source-pinned B15 fixed-matrix theorem at `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056` gives an individual `C_0(R)` representative for every fixed rank-at-least-three QFORM instance. This qualitative conclusion is separate from the uniform `L^infinity` target and does not supply a target-uniform continuity modulus.

Thus an argument of the form “prove all finite `L^r` bounds and send `r` to infinity” is not presently a closure mechanism: the sharp elementary chain itself records a `sqrt(r)` endpoint loss. Nor can the loss be repaired by splitting the characteristic function into an absolute product-Hölder estimate, because the completed account02/B15 Fourier endpoint obstruction says that the needed law-uniform product exponent below two is false.

## 5. Direct partner application and relation to the full target

Equation (3.8) is the required direct application of a completed designated-partner result to an actual target-side inequality. It propagates through Young to the new finite-L^r estimate (3.2); this is stronger than merely citing the endpoint theorem.

The result is compatible with the owner's physical-sheet work but does not replace it. The full three-large-eigenvalue condition does not force the global form to split into three independent variables as in (3.1). In particular, overlapping leakage and diffuse-light configurations in the current frontier retain correlations among the effective bilinear and square directions. Treating those effective directions as independent after a rotation would violate a live correction.

The exact remaining connection is therefore:

> Find a product-preserving structural receiver that turns the unresolved high-leverage/diffuse-light geometry into either (i) an actual independent/disjoint bilinear-plus-square block to which Theorem 3.1 and an endpoint receiver apply, or (ii) a stronger coupled estimate that avoids the `sqrt(r)` endpoint loss while retaining the original-coordinate product law.

The current theorem identifies a precise regularity endpoint: below `L^infinity` the strict independent split is uniformly controlled at every exponent, and the only missing step in that branch is genuinely endpoint/coupling information rather than existence or finite-exponent regularity. It is not a proof of unrestricted QFORM.

## 6. Logical status

- Full universal bounded-density conjecture: **OPEN / NOT PROVED**.
- Absolute continuity for nonzero quadratic pushforwards of absolutely continuous joint laws: **qualitatively proved**.
- Fixed-instance rank-at-least-three bounded `C_0` density: **source-pinned completed B15 theorem; constant matrix-dependent**.
- New strict-split finite-L^r ladder (3.2)–(3.3): **proved here**.
- Uniform `L^infinity` inferred from `r<infinity`: **not proved; the derived constant grows like `sqrt(r)`**.
- Pointwise quadratic Fourier decay / rotated independence / projection-only shortcut: **not used**.
