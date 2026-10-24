# Source-valid constant sharpening for the fixed-multiplicity theorem

Run: `20260924T115853Z-account03-B18-QFORM-fixedmult-audit-r11`
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Status: supporting improvement proved below; baseline manuscript is not overwritten.

## Result

Using the same 17-direction proof architecture, plus the sharp one-dimensional bounded-density theorem of Rudelson--Vershynin, the numerical conclusion can be strengthened from

\[
\|p_Q\|_\infty\le 10^4 K^2/s
\]

to the source-valid bound

\[
\boxed{\|p_Q\|_\infty<1960\,K^2/s}
\]

under exactly the same hypotheses: independent real coordinates with densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, and arbitrary affine terms. This does **not** lower the multiplicity 17 and is not claimed novel.

Primary source transferred: M. Rudelson and R. Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2. It states that if independent real `X_j` have densities bounded by `K` and `sum a_j^2=1`, then `sum a_j X_j` has density bounded by `sqrt(2) K`. There are no moment, support, iid, log-concavity, centering, or smoothness hypotheses.

## 1. Sharper integrated scalar Fourier powers

Let `f` be a probability density with `0<=f<=1`, and use the manuscript Fourier convention. For `p>=2`, let `m=floor(p/2)`. Then `m>=p/4` and, since `|fhat|<=1`,

\[
\int |\widehat f|^p\le\int|\widehat f|^{2m}.
\]

If `X_1,...,X_m,X'_1,...,X'_m` are independent with density `f`, then the last integrand is the characteristic function of

\[
S=\sum_{j=1}^m(X_j-X'_j).
\]

It is integrable because `|fhat|^{2m}<=|fhat|^2` and Plancherel applies. Fourier inversion at zero and Rudelson--Vershynin Theorem 1.2 give

\[
\int|\widehat f(t)|^{2m}dt=2\pi p_S(0)
\le \frac{2\pi}{\sqrt m}
\le\frac{4\pi}{\sqrt p}.
\tag{1}
\]

Indeed, the coefficient vector of `S` has Euclidean norm `sqrt(2m)`, so the normalized sum has density cap `sqrt(2)` and hence `p_S<=1/sqrt(m)`.

This replaces the manuscript's self-contained `2*pi*sqrt(2e)/sqrt(p)` by the sharper source-backed `4*pi/sqrt(p)`.

## 2. Sharper regularized crossing determinant

Repeat the manuscript proof of the regularized determinant theorem. With its weights `c_j,d_i`, put `h_i=|fhat_i|^2`. Applying (1) with `p=2/d_i` gives

\[
\|h_i\|_{1/d_i}
\le (2\sqrt2\,\pi\sqrt{d_i})^{d_i}.
\]

The factor `d_i^{-d_i/2}` from the graph Brascamp--Lieb change of variables cancels `d_i^{d_i/2}`. The physical-coordinate factors still contribute

\[
\prod_jc_j^{-c_j/2}\le e^{\theta/2}.
\]

Thus the full scalar factor is `(2*pi*sqrt(2e))^theta`. Choose

\[
\alpha=(2\pi\sqrt{2e})^2=8\pi^2e.
\]

Since the bilinear coefficient in the decoupling proof is `a=2t`, fourth-rooting yields

\[
\boxed{
|\phi_Z(t)|\le
\det\left(I+\frac{t^2}{2\pi^2e}M^TM\right)^{-1/8}.}
\tag{2}
\]

No other step of the determinant proof changes.

If `Z_k(M)>0`, (2) implies

\[
|\phi_Z(t)|\le
\min\left\{1,
\left(\frac{u_k}{|t|}\right)^{k/4}\right\},
\qquad
u_k=\pi\sqrt{2e}\,Z_k(M)^{-1/(2k)}.
\tag{3}
\]

Consequently

\[
Z_5>0\implies
\|p_Z\|_\infty\le5\sqrt{2e}\,Z_5^{-1/10},
\tag{4}
\]

and

\[
Z_3>0\implies
\sup_a\mathbb E|Z-a|^{-1/2}
\le12\sqrt{\frac{\sqrt{2e}}2 Z_3^{-1/6}}.
\tag{5}
\]

## 3. Re-optimize the pivot and volume parameters

Use

\[
\eta=\frac{11}{400},
\qquad
q=\frac1{84},
\qquad
\kappa=q^2=\frac1{84^2}.
\tag{6}
\]

If there is no `eta`-pivot, then

\[
|a_{ii}|<\eta,
\qquad
|a_{ij}|<h:=\sqrt{\eta^2+\eta}=\frac{\sqrt{4521}}{400}.
\tag{7}
\]

The manuscript's sampled interpolation and completion lemmas are unchanged. If a bad volume ratio occurs at order `1<=r<=4`, then

\[
\epsilon:=\|E\|_F<(r+1)q.
\]

The large diagonal coordinates of `D` obey

\[
|R_{ii}|>1-\eta-(r+1)q,
\]

whereas a row of the relevant `(r+1)`-coordinate compression has off-diagonal sum less than

\[
r\bigl(h+(r+1)q\bigr).
\]

It therefore suffices that

\[
1-\eta-rh-(r+1)^2q>0.
\tag{8}
\]

The left side decreases with `r`, so only `r=4` needs checking. There

\[
1-\frac{11}{400}-\frac{\sqrt{4521}}{100}-\frac{25}{84}
=
\frac{5669}{8400}-\frac{\sqrt{4521}}{100}>0,
\]

because

\[
5669^2-84^2\cdot4521=237385>0.
\]

The `r=0` case is also immediate since `eta+q<1`. Hence the manuscript's spectral-to-volume proposition remains valid with (6): for `k<=5`, no pivot and `s_{4k-3}(A)>=1` imply

\[
V_k(A)\ge\kappa^k.
\tag{9}
\]

A fair coordinate cut then gives

\[
Z_k(A_{I,J})^{-1/(2k)}\le2\kappa^{-1/2}=168.
\tag{10}
\]

## 4. New no-pivot constants

For `k=5`, (4) and (10) give

\[
\|p_Q\|_\infty\le840\sqrt{2e}<1960.
\tag{11}
\]

A fully rational check is available: from the exponential series,

\[
e<\frac83+\frac{1/24}{1-1/5}=\frac{87}{32},
\]

so

\[
840\sqrt{2e}<210\sqrt{87}<1960,
\]

with `1960^2-210^2*87=4900>0`.

For `k=3`, (5) and (10) give the full negative-half-moment bound

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le12\sqrt{84\sqrt{2e}}<180.
\tag{12}
\]

Indeed `e<87/32` implies `sqrt(2e)<sqrt(87)/4<5/2`, so the quantity under the outer square root is below `210<225`.

## 5. New pivot constants and the global 1960 bound

The manuscript's one-direction log bound is unchanged:

\[
L_0=4+4\log16.
\]

For a scalar pivot in the nine-direction half-potential proposition,

\[
H(Q)\le\eta^{-1/2}(8+3L_0)
=\frac{20}{\sqrt{11}}(20+12\log16).
\tag{13}
\]

The definite- and indefinite-pair pivot estimates are smaller than (13); the no-pivot nine-direction full half potential is `<180` by (12), also smaller. Thus every nine-direction remainder satisfies

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le1+\frac{20}{\sqrt{11}}(20+12\log16).
\tag{14}
\]

For the outer scalar-pivot branch of the 17-direction theorem, multiply (14) by `eta^{-1/2}=20/sqrt(11)`:

\[
\|p_Q\|_\infty
\le
\frac{20}{\sqrt{11}}+
\frac{400}{11}(20+12\log16)
<1960.
\tag{15}
\]

For an elementary numerical verification, `e^{7/10}>1+7/10+49/200+343/6000>2`, hence `log2<7/10` and `log16<14/5`. Also `sqrt(11)>33/10`. Therefore the right side of (15) is less than

\[
\frac{200}{33}+\frac{21440}{11}
=\frac{64520}{33}<1960.
\]

The definite-pair branch is at most `pi/sqrt(eta)`, and the indefinite-pair branch remains far below this scale by the manuscript's logarithmic estimate. Combining those branches with (11) proves the normalized constant `1960`. The original scaling then gives

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty
<1960\,K^2/s
\quad\text{whenever }s_{17}(A)\ge s>0.}
\]

## 6. What this does and does not improve

This is a genuine literature-to-proof transfer: the sharp Rudelson--Vershynin scalar density theorem improves the integrated Fourier input, which improves the crossing determinant, permits a better `(eta,kappa)` balance, and reduces the global constant by more than a factor of five.

It does **not** lower 17. In this architecture bounded density still needs crossing order five (`5/4>1`), and the worst sampled seed has `r=4`; with global correction rank `3r` and restricted rank `r`, the diagonal-dominance contradiction still needs `m>=3r+(r+1)=17`. Lower multiplicity needs a new structural or endpoint analytic mechanism.
