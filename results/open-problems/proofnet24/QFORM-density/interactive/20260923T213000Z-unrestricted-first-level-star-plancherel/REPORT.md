# Unrestricted first-level small-ball estimate from a physical star

**Status:** proved, dimension-free. This advances the first concentration level for general symmetric matrices. It does **not** prove the desired third-level density theorem. The second-level logarithmic concentration estimate in the indefinite case remains open.

Let \(X=(X_1,\dots,X_n)\) have independent real coordinates with densities \(0\le f_i\le1\). For a real random variable \(Z\), set
\[
 L_Z(u)=\sup_s\Pr(|Z-s|\le u),\qquad
 \alpha_1(Z)=\sup_{u>0}L_Z(u)/\sqrt u.
\]

## A star estimate with arbitrary self functions

Suppose \(H\) is independent of a random object \(Y\), \(H\) has a probability density bounded by \(K\), and the scalar \(L=L(Y)\) has a probability density bounded by \(M\). Let \(R_H\) and \(R_Y\) be **arbitrary measurable real functions**, finite almost surely. For \(c\ne0\), put
\[
 Z=cH L(Y)+R_H(H)+R_Y(Y).
\]
Then
\[
 |\varphi_Z(t)|\le
 \min\left\{1,\sqrt{\frac{2\pi K M}{|ct|}}\right\},
 \quad t\ne0,                                      \tag{1}
\]
and
\[
 \alpha_1(Z)\le
 \frac{2\sqrt2}{\sin^2 1}
 \sqrt{\frac{2\pi K M}{|c|}}.                       \tag{2}
\]

**Proof.** For fixed \(t\), write
\[
 F_t(\ell)=\int f_H(h)e^{itR_H(h)+ict\ell h}\,dh.
\]
Conditioning on \(Y\), taking absolute values, and applying Cauchy–Schwarz under the law of \(L\) yield
\[
 |\varphi_Z(t)|
 \le\mathbb E|F_t(L)|
 \le\bigl(M\int_{\mathbb R}|F_t(\ell)|^2\,d\ell\bigr)^{1/2}.
\]
One-dimensional Plancherel with frequency \(ct\ell\) gives
\[
 \int|F_t(\ell)|^2\,d\ell
 =\frac{2\pi}{|ct|}\int f_H(h)^2\,dh
 \le\frac{2\pi K}{|ct|}.
\]
This proves (1). The Fejér concentration lemma (manuscript semidefinite.tex, Lemma sd:fejer) applied to the \(|t|^{-1/2}\) bound gives (2). No regularity of the self functions is needed. \(\square\)

For the quadratic physical star
\[
 Q=aH^2+bH+2H L(Y)+R(Y),
\]
(1) gives \(|\varphi_Q(t)|\le\sqrt{\pi KM/|t|}\), independently of \(a,b,R\).

## Consequence for every symmetric quadratic matrix

**Theorem.** Let \(A=A^{\mathsf T}\) be real, \(\theta=s_1(A)=\|A\|_{\rm op}>0\), and let \(b,c\) be arbitrary. Then
\[
 \alpha_1(X^{\mathsf T}AX+b^{\mathsf T}X+c)
 <\frac{24}{\sqrt\theta}.                         \tag{3}
\]
In particular the quadratic form has no atoms, uniformly over dimension, rank, inertia, coordinate laws, and affine terms.

**Proof.** Scale to \(\theta=1\) and set \(d=1/6\). First suppose an original coordinate \(i\) has row norm \(\|Ae_i\|>d\). Write \(a=A_{ii}\) and \(v=A_{-i,i}\). If \(|a|\ge d/2=1/12\), condition on all other coordinates and complete the square in \(X_i\). The conditional density is bounded by \(|a|^{-1/2}\) times a one-sided square-root kernel. Integrating this kernel over an interval of radius \(u\) gives \(L_Q(u)\le4\sqrt{u/|a|}\), hence
\[
 \alpha_1(Q)\le4\sqrt{12}<14.
\]
If \(|a|<d/2\), then
\[
 \|v\|>\sqrt{\|Ae_i\|^2-a^2}>
 \frac{\sqrt3}{2}d=\frac{\sqrt3}{12}.
\]
The scalar \(L=v^{\mathsf T}X_{-i}\) has density bounded by
\[
 M\le\sqrt2/\|v\|<12\sqrt{2/3}
\]
by the product-marginal theorem. Apply the star estimate to \(H=X_i\), \(c=2\), \(R_H(h)=ah^2+b_i h\), and \(R_Y(Y)=Y^{\mathsf T}A_{-i,-i}Y+b_{-i}^{\mathsf T}Y+c\). Thus
\[
 \alpha_1(Q)
 \le\frac{2\sqrt2}{\sin^2 1}
       \sqrt{12\pi\sqrt{2/3}}
 =22.162025346\ldots<24.                       \tag{4}
\]

Now suppose every row satisfies \(\|Ae_i\|\le d\). Let \(O=A-\operatorname{diag}A\) and \(F=\|O\|_F\). Because \(\|\operatorname{diag}A\|\le d\) and \(\|A\|=1\),
\[
 F\ge\|O\|\ge1-d=5/6.
\]
Take independent fair signs \(\varepsilon_i\), set \(I=\{i:\varepsilon_i=1\}\), \(J=I^c\), and put \(Z=\|A_{I,J}\|_F^2\). Since each unordered off-diagonal entry occurs exactly once when its endpoints have opposite signs,
\[
 Z=\sum_{i<j}a_{ij}^2\mathbf1_{\{\varepsilon_i\ne\varepsilon_j\}},
 \qquad
 \mathbb EZ=F^2/4.
\]
The distinct-edge indicators are pairwise uncorrelated, even if two edges share a vertex. Thus
\[
 \operatorname{Var}Z=\tfrac14\sum_{i<j}a_{ij}^4
 \le\tfrac18 d^2F^2.
\]
Indeed, \(\sum_{i<j}a_{ij}^4\le\tfrac12\sum_i(\sum_{j\ne i}a_{ij}^2)^2\le\tfrac12d^2F^2\). Chebyshev gives
\[
 \Pr(Z<F^2/8)
 \le\frac{8d^2}{F^2}
 \le\frac8{25}<1.
\]
Fix a cut with
\[
 Z\ge F^2/8\ge25/288.                             \tag{5}
\]
For the first-volume squared-minor weights of \(A_{I,J}\), each row marginal equals \(\alpha_i=\|(A_{I,J})_{i,\cdot}\|^2/Z\), so
\[
 \max_i\alpha_i\le d^2/Z\le 8/25<1/2.
\]
The volume-sampling Fourier lemma with \(k=q=1\) therefore gives
\[
 |\varphi_Q(t)|
 \le e^{1/4}\sqrt{2\pi}\,Z^{-1/4}|t|^{-1/2}.
\]
The Fejér concentration lemma and (5) imply
\[
 \alpha_1(Q)
 \le\frac{2\sqrt2}{\sin^2 1}\,
       e^{1/4}\sqrt{2\pi}\,(288/25)^{1/4}
 =23.686090105\ldots<24.                       \tag{6}
\]
The cut remains valid with arbitrary quadratic self terms and affine terms. These cases prove (3) at scale one. Since \(\alpha_1(\theta Z)=\alpha_1(Z)/\sqrt\theta\), scaling completes the proof. \(\square\)

## Scope and source-pinned inputs

The first-level estimate (3) strengthens the previously archived quarter-power concentration result to a square-root exponent for every symmetric quadratic form. It does not by itself give second-level logarithmic concentration. A global *truncated half-power potential* estimate at the second level is already proved by Lemma schur-count and Lemma pivot-half in the [structural manuscript](https://github.com/yspennstate/math-open-problems/blob/1084cf8ec8916b7e5b9754cbb7ebad2a4c29cf4b/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/structure.tex), combined with Theorem lower:two in the [lower-level manuscript](https://github.com/yspennstate/math-open-problems/blob/1084cf8ec8916b7e5b9754cbb7ebad2a4c29cf4b/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/lower_levels.tex). The unrestricted third-level density theorem remains open.

The first-volume Fourier estimate is Lemma four:volume and the one-dimensional product-marginal cap is Lemma four:projection in [fourier.tex at the source commit](https://github.com/yspennstate/math-open-problems/blob/1084cf8ec8916b7e5b9754cbb7ebad2a4c29cf4b/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/fourier.tex). The Fejér concentration inequality is Lemma sd:fejer in [semidefinite.tex at the same commit](https://github.com/yspennstate/math-open-problems/blob/1084cf8ec8916b7e5b9754cbb7ebad2a4c29cf4b/proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/semidefinite.tex).
