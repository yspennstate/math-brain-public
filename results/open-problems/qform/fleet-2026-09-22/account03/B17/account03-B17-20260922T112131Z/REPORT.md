# account03/B17 — quadratic-form bounded-density target: diagonal branch at C=pi and failure of uniform one-direction Fourier decay

**Run pivot:** `account03-B17-20260922T112131Z`  
**Live owner control:** revision `2026-09-22.4`, quadratic-form bounded-density conjecture  
**Classification:** `SUBSTANTIVE_BRANCH_CLOSED / METHOD_CORRECTION / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full rotated-eigenbasis conjecture:** **OPEN / NOT PROVED.**

## 0. Target and mid-run control change

The live natural-language owner message changed during this invocation and superseded the earlier FEI order. The active target is now:

> If `X_1,...,X_n` are independent real random variables with densities bounded by 1 and a real quadratic form `Q(x)=x^T A x` has at least three eigenvalues of absolute value at least 1, prove that `Q(X)` has a density bounded by one universal constant.

This report does not continue FEI after that control change. It attacks two immediate pieces of the new target:

1. test the proposed uniform one-dimensional oscillatory-decay step;
2. solve the entire coordinate-diagonal subclass with an explicit constant.

The first test produces a rigorous counterexample to the **method step**, not to the conjecture. The second gives a complete theorem for diagonal forms in the independent-coordinate basis, including indefinite signs and arbitrary additional smaller eigenvalues.

## 1. The suggested uniform single-direction `|t|^{-1/2}` decay is false

A tempting step is to hope for a universal constant `C` such that, for every probability density `f` with `0<=f<=1`,

\[
\left|\int_{\mathbb R} e^{isx^2}f(x)\,dx\right|
\le C|s|^{-1/2}.
\tag{1.1}
\]

This cannot hold without regularity/support assumptions on `f`.

### Proposition 1.1 — `QFORM-NO-UNIFORM-POINTWISE-FRESNEL-v1`

For every `s!=0`,
\[
\boxed{
\sup_{f\ge0,\ \int f=1,\ \|f\|_\infty\le1}
\left|\int e^{isx^2}f(x)\,dx\right|=1.
}
\tag{1.2}
\]
Consequently there is no law-independent pointwise decay envelope tending to zero as `|s|->infinity` for this class.

#### Proof

Fix `0<delta<pi/2` and set
\[
A_{s,\delta}
=\{x:\operatorname{dist}(sx^2,2\pi\mathbb Z)\le\delta\}.
\]
It is enough to treat `s>0`; the other sign is identical after complex conjugation. For each sufficiently large integer `k`, `A_{s,delta}` contains the interval
\[
I_k=
\left[
\sqrt{(2\pi k-\delta)/s},
\sqrt{(2\pi k+\delta)/s}
\right].
\]
Its length is
\[
|I_k|
={2\delta/s\over
\sqrt{(2\pi k+\delta)/s}+\sqrt{(2\pi k-\delta)/s}}
\asymp_{s,\delta}k^{-1/2}.
\]
Hence `sum_k |I_k|=infinity`, so `A_{s,delta}` has infinite Lebesgue measure. Choose a measurable `E subset A_{s,delta}` of measure exactly 1 and put `f=1_E`. Then `f` is a probability density bounded by 1 and, on `E`,
\[
\Re e^{isx^2}\ge\cos\delta.
\]
Therefore
\[
\left|\int e^{isx^2}f(x)dx\right|
\ge\cos\delta.
\]
Letting `delta downarrow0` proves that the supremum is at least 1; the reverse inequality is trivial. `QED`.

### Corollary 1.2 — no uniform `|t|^{-3/2}` envelope even for diagonal three-term forms

Fix any nonzero `t` and any three coefficients `|lambda_j|>=1`. For each `j`, apply Proposition 1.1 to `s=t lambda_j` and choose an independent density `f_j` making the corresponding factor arbitrarily close to 1 in modulus. For the diagonal form
\[
Q=\sum_{j=1}^3\lambda_jX_j^2,
\]
independence gives
\[
\phi_Q(t)=\prod_{j=1}^3\mathbb E e^{it\lambda_jX_j^2}.
\]
Thus
\[
\boxed{
\sup_{f_1,f_2,f_3:\ \|f_j\|_\infty\le1}|\phi_Q(t)|=1
\quad(t\ne0).
}
\tag{1.3}
\]
In particular, a proof cannot take a supremum over laws first and then dominate it by `C|t|^{-3/2}`. A uniform `L^1_t` argument, if true, would have to exploit non-pointwise structure; naive van der Corput with merely an `L^infty` amplitude is insufficient.

This is a methodological correction, **not** a counterexample to bounded density.

## 2. One squared variable has an exact universal singular envelope

Let `X` have density `f` with `0<=f<=1`, and let
\[
Y=\lambda X^2,
\qquad |\lambda|\ge1.
\]
If `lambda>0`, the density of `Y` is
\[
g_\lambda(y)
={\mathbf1_{y>0}\over2\sqrt{\lambda y}}
\left[
 f\!\left(\sqrt{y/\lambda}\right)
+f\!\left(-\sqrt{y/\lambda}\right)
\right],
\tag{2.1}
\]
so
\[
\boxed{
0\le g_\lambda(y)
\le {\mathbf1_{y>0}\over\sqrt{\lambda y}}
\le {\mathbf1_{y>0}\over\sqrt y}.
}
\tag{2.2}
\]
For `lambda<0`, the reflected bound holds on the negative half-line:
\[
g_\lambda(y)\le\mathbf1_{y<0}|y|^{-1/2}.
\tag{2.3}
\]
No regularity of `f` is used.

## 3. Same-sign pair lemma: exact beta-integral bound `pi`

### Lemma 3.1 — `QFORM-SAME-SIGN-PAIR-PI-v1`

Let `X_1,X_2` be independent, each with density bounded by 1, and suppose
\[
|\lambda_1|,|\lambda_2|\ge1,
\qquad \lambda_1\lambda_2>0.
\]
Then
\[
Y=\lambda_1X_1^2+\lambda_2X_2^2
\]
has a density satisfying
\[
\boxed{\|p_Y\|_\infty\le\pi.}
\tag{3.1}
\]
More precisely,
\[
\|p_Y\|_\infty\le {\pi\over\sqrt{|\lambda_1\lambda_2|}}.
\tag{3.2}
\]

#### Proof

Assume first both coefficients are positive. By (2.2), for `y>0`,
\[
\begin{aligned}
p_Y(y)
&=(g_{\lambda_1}*g_{\lambda_2})(y)\\
&\le {1\over\sqrt{\lambda_1\lambda_2}}
\int_0^y {du\over\sqrt{u(y-u)}}.
\end{aligned}
\]
The beta integral is exactly
\[
\int_0^y {du\over\sqrt{u(y-u)}}
=\int_0^1{dv\over\sqrt{v(1-v)}}
=B(1/2,1/2)=\pi.
\]
This proves (3.2). If both coefficients are negative, reflect the random variable and use the same argument. `QED`.

The logarithmic singularity of the opposite-sign two-term form is consistent with this lemma: the same-half-line beta integral becomes a long-tail integral after reflection, and no analogous `pi` bound follows from two opposite signs.

## 4. Complete coordinate-diagonal theorem: the owner's threshold-three statement holds with `C=pi`

### Theorem 4.1 — `QFORM-DIAGONAL-THREE-LARGE-PI-v1`

Let `X_1,...,X_n` be independent real random variables, each with density bounded by 1. Let
\[
Q(X)=\sum_{j=1}^n\lambda_jX_j^2
\tag{4.1}
\]
be diagonal in these independent coordinates. If at least three coefficients satisfy
\[
|\lambda_j|\ge1,
\]
then `Q(X)` is absolutely continuous and
\[
\boxed{\|p_Q\|_\infty\le\pi.}
\tag{4.2}
\]
The bound is independent of `n`, all laws, all remaining coefficients, and the signs of the three large coefficients.

#### Proof

Among any three real nonzero coefficients, two have the same sign. Relabel so that
\[
|\lambda_1|,|\lambda_2|\ge1,
\qquad \lambda_1\lambda_2>0.
\]
By Lemma 3.1,
\[
Y=\lambda_1X_1^2+\lambda_2X_2^2
\]
has density `p_Y` with `||p_Y||_infinity<=pi`.

Let
\[
W=\sum_{j=3}^n\lambda_jX_j^2.
\]
By independence, `Y` and `W` are independent. The law of `W` is some probability measure `mu_W` (no regularity is needed). Hence
\[
p_Q=p_Y*\mu_W,
\]
and convolution with a probability measure is an `L^infinity` contraction:
\[
|p_Q(y)|
\le\int\|p_Y\|_\infty\,d\mu_W
\le\pi.
\]
Thus (4.2) holds. `QED`.

### What this closes

This theorem handles all diagonal sign patterns, including `[+,+,-]`, `[+,-,-]`, repeated eigenvalues, coefficients exactly at magnitude 1, arbitrary additional large/small coefficients, and arbitrary bounded-density laws. It also explains the threshold-three sign logic without Fourier decay: with three large eigenvalues, a same-sign pair always exists; with only two, the opposite-sign configuration is the exceptional logarithmic case.

## 5. Why this does not solve the rotated problem

For the full conjecture the eigenvectors `r_j` need not be coordinate vectors. After rotating to the eigenbasis, the coordinates of `R^T X` are generally dependent, so the convolution step in Theorem 4.1 disappears. Conversely, conditioning on the orthogonal complement of two same-sign eigenvectors leaves on the two-dimensional eigenspace an amplitude
\[
(z_1,z_2)\mapsto\prod_i f_i(w_i+a_i z_1+b_i z_2),
\]
not a product in `z_1,z_2`.

A useful geometric observation is that for any amplitude `0<=h<=1` on a two-dimensional eigenspace, the coarea density of the positive-definite quadratic piece at a **fixed orthogonal slice** is at most `pi/sqrt(|lambda_1lambda_2|)` before integrating over the complementary variable. However, naively integrating this slice bound over all complementary `w` loses normalization and can diverge. The remaining crux can therefore be stated sharply:

> exploit the original product structure to integrate the two-dimensional same-sign coarea bound over `E^perp` without paying the Lebesgue volume of all slices.

This is a more concrete replacement obligation than uniform one-direction van der Corput decay.

Potential tools include Brascamp-Lieb/cube-slicing inequalities for restrictions of product densities to affine two-planes, or a small-ball argument that averages the coarea bound against a normalized projection density. Any such step must preserve a constant independent of dimension.

## 6. Literature check and scope

A quick external literature check found standard quadratic-form concentration results under substantially different hypotheses (e.g. subgaussian variables in Hanson-Wright, and iid/moment assumptions in Goetze-Tikhomirov) and recent smooth-law regularity work. Those results are useful context but are not used as premises in the proofs above. No novelty claim is made from the search.

## 7. Status

**Proved in this report:**

1. the proposed law-uniform one-dimensional pointwise Fresnel decay is false; indeed the supremum characteristic-function modulus is 1 at every nonzero frequency;
2. any same-sign pair of large diagonal coefficients gives a density bounded by `pi`;
3. consequently the full threshold-three conjecture is true with `C=pi` whenever the quadratic form is diagonal in the original independent coordinates.

**Still open:** the arbitrary orthogonal-eigenvector coupling. Full conjecture **OPEN / NOT PROVED**.
