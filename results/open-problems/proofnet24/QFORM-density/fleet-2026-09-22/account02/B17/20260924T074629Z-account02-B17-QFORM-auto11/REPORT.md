# account02/B17 — random-location Gaussian barrier and off-axis Poisson satellites

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T074629Z-account02-B17-QFORM-auto11`  
Status: `NEW SUPPORTING THEOREM / PARTNER RESULT APPLIED / PINNED THEOREM-F RECEIVER / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains OPEN. This report rules out a previously unpaid sharp-witness mechanism: **off-axis / majority-plane compound-Poisson displacement of a minimum-variance Gaussian core on the negative two-sheet side**. The proof is global in the output level. It uses no independence after spectral rotation of a finite product law.

## 1. Random-location Gaussian barrier

### Theorem 1 (`QFORM-RANDOM-LOCATION-GAUSSIAN-INDEFINITE-BARRIER-v1`)

Let `A` be a real symmetric `3 x 3` indefinite matrix whose three eigenvalues satisfy

\[
|\lambda_j(A)|\ge 1.
\]

Let `G ~ N(0,\Sigma)`, with `\Sigma` positive definite and

\[
\lambda_{\min}(\Sigma)\ge v_0>0,
\]

and let `M` be an arbitrary random vector in `R^3`, independent of `G` (no density or moment assumption on `M`). Then

\[
Q=(G+M)^T A(G+M)
\]

has a bounded density and

\[
\boxed{\|p_Q\|_\infty\le \frac1{2\sqrt2\,v_0}.}
\tag{1.1}
\]

In particular, if `v_0=1/12`,

\[
\boxed{\|p_Q\|_\infty\le 3\sqrt2.}
\tag{1.2}
\]

#### Proof

Condition on `M=m`. The latest compatible account03/B17 theorem `QFORM-GAUSSIAN-TRANSLATION-MIXTURE-RIGIDITY-v1`, source

`yspennstate/math-open-problems@e6dfe24dd09057f92549593fd763444bc930ab99:proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260924T070819Z-account03-B17-QFORM-auto11/REPORT.md`,

proves, for every fixed Gaussian mean,

\[
\|p_{(G+m)^TA(G+m)}\|_\infty
\le
\|p_{G^TAG}\|_\infty.
\tag{1.3}
\]

It is enough therefore to bound the centered comparator uniformly.

Put

\[
C=\Sigma^{1/2}A\Sigma^{1/2}.
\]

Since `A` is invertible and `s_min(A)>=1`,

\[
\|C^{-1}\|
=\|\Sigma^{-1/2}A^{-1}\Sigma^{-1/2}\|
\le v_0^{-1},
\]

so every eigenvalue of `C` has absolute value at least `v_0`. By Sylvester inertia, after possibly replacing `C` by `-C`, its eigenvalues are `a,b,-c` with

\[
a,b,c\ge v_0.
\]

For standard independent normals `Z_j`, rotational invariance gives

\[
G^TAG\stackrel d=aZ_1^2+bZ_2^2-cZ_3^2.
\tag{1.4}
\]

The density of `U=aZ_1^2+bZ_2^2` is, for `u>0`,

\[
f_{a,b}(u)=\frac1{2\sqrt{ab}}e^{-\alpha u}I_0(\beta u),
\qquad
\alpha=\frac{a+b}{4ab},\quad
\beta=\frac{|a-b|}{4ab}.
\tag{1.5}
\]

Because `I_1(x)<I_0(x)` for `x>0` and `\beta<\alpha`, this density is decreasing. The density of `V=cZ_3^2` is also decreasing. Hence the density of `U-V` is globally maximized at zero: for `s>=0`,

\[
p(s)=\int_0^\infty f_{a,b}(s+v)g_c(v)\,dv\le p(0),
\]

and for `r>=0`,

\[
p(-r)=\int_0^\infty f_{a,b}(u)g_c(u+r)\,du\le p(0).
\]

At zero, direct cone integration gives

\[
p(0)
=\frac1{4\pi}
\int_0^{2\pi}
\frac{d\theta}{
\sqrt{bc\cos^2\theta+ac\sin^2\theta+ab}}.
\tag{1.6}
\]

Since `a,b,c>=v_0`, the denominator is at least `\sqrt2 v_0`, hence

\[
\|p_{G^TAG}\|_\infty=p(0)
\le \frac1{2\sqrt2 v_0}.
\tag{1.7}
\]

Averaging the conditional densities in (1.3) proves (1.1). `square`

This theorem is a **random-location lift** of the partner's deterministic-translation theorem. It pays arbitrary off-axis discrete, singular, compound-Poisson, or other independent location mixtures whenever a Gaussian core with covariance floor `v_0` survives.

## 2. Quantitative strict gap for isotropic reflections

Let now `A=B` satisfy `B^2=I_3`, `spec(B)={1,1,-1}`, and let `G~N(0,sI_3)`. Define

\[
C_0=\frac1{2\sqrt2 s},
\qquad
C_1=\frac{e^{-1/2}}{\sqrt{2\pi}\,s}.
\tag{2.1}
\]

The partner's quantitative noncentral estimate gives, for every deterministic mean `m`, with `D=|m|^2/s`,

\[
\|p_{(G+m)^TB(G+m)}\|_\infty
\le e^{-D/2}C_0+(1-e^{-D/2})C_1.
\tag{2.2}
\]

Therefore if an independent random shift `M` satisfies

\[
\mathbb P(M=0)=p_0,
\qquad
|M|\ge d>0\quad\text{on }\{M\ne0\},
\]

then

\[
\boxed{
\|p_{(G+M)^TB(G+M)}\|_\infty
\le p_0C_0+(1-p_0)
\left[e^{-d^2/(2s)}C_0+(1-e^{-d^2/(2s)})C_1\right].
}
\tag{2.3}
\]

Since `C_1<C_0`, this is strictly below `C_0` whenever `p_0<1` and `d>0`.

## 3. A source-valid root-m off-axis Poisson stress family

Let

\[
n=\frac1{\sqrt{14}}(1,2,3)^T,
\qquad
B=I_3-2nn^T
=\frac17
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\tag{3.1}
\]

Then `B^2=I_3`,

\[
\boxed{\operatorname{spec}(B)=\{1,1,-1\},}
\tag{3.2}
\]

and every entry of `B` is nonzero.

For each `m>=2`, let `T_m` be the `3m x 3` bank synthesis matrix whose rows are `e_j/sqrt(m)` in bank `j`, and put

\[
A_m=T_mBT_m^T.
\tag{3.3}
\]

Since `T_m^TT_m=I_3`,

\[
\boxed{\operatorname{spec}(A_m)=\{1,1,-1,0,\ldots,0\}.}
\tag{3.4}
\]

Moreover every physical entry of `A_m` equals a nonzero entry of `B` divided by `m`, so `A_m` is entrywise dense.

On every one of the `3m` original physical coordinates take the density

\[
f_m(x)
=
\mathbf1_{[-(1-1/m)/2,(1-1/m)/2]}(x)
+
\mathbf1_{[\sqrt m-1/(2m),\sqrt m+1/(2m)]}(x).
\tag{3.5}
\]

The two support lengths add exactly to one, hence `f_m` is an exact cap-one probability density. Its support gap is `sqrt(m)-1/2+o(1)`. A physical coordinate visits the remote satellite with probability `1/m`; among all `3m` coordinates the expected number of visits is `3`, and the probability of at least one visit tends to `1-e^{-3}`.

This family is genuinely non-Lindeberg. For every fixed `0<delta<1`, the bankwise Lindeberg tail satisfies

\[
\sum_{k=1}^m
\mathbb E\left[
\left(\frac{X_{jk}^{(m)}}{\sqrt m}\right)^2
\mathbf1_{\{|X_{jk}^{(m)}|>\delta\sqrt m\}}
\right]
\longrightarrow1.
\tag{3.6}
\]

Define the normalized bank sums

\[
Y_{j,m}=m^{-1/2}\sum_{k=1}^mX_{jk}^{(m)},
\qquad
Q_m=Y_m^TBY_m=X^TA_mX.
\tag{3.7}
\]

For one normalized summand the characteristic function is exactly

\[
\chi_m(t)
=\left(1-\frac1m\right)
\operatorname{sinc}\!\left(\frac{t(1-1/m)}{2\sqrt m}\right)
+\frac1m e^{it}
\operatorname{sinc}\!\left(\frac{t}{2m\sqrt m}\right).
\tag{3.8}
\]

For fixed `t`,

\[
\chi_m(t)
=1+\frac{e^{it}-1-t^2/24}{m}+O_t(m^{-2}),
\]

hence

\[
\chi_m(t)^m
\longrightarrow
\exp\left(-\frac{t^2}{24}+e^{it}-1\right).
\tag{3.9}
\]

Thus the three bank sums converge jointly to

\[
Y_m\Rightarrow G+N,
\tag{3.10}
\]

where `G~N(0,I_3/12)` and `N=(N_1,N_2,N_3)` has independent `Poisson(1)` coordinates, independent of `G`. Consequently

\[
Q_m\Rightarrow Q_\infty=(G+N)^TB(G+N).
\tag{3.11}
\]

The displacement is not confined to the minority axis; after diagonalizing the dense reflection `B`, generic Poisson atoms have components in both the majority plane and minority direction.

## 4. Pinned Theorem F pays the finite-stage spike obstruction

The required pinned source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Its completed Fresnel--Brascamp--Lieb Theorem F applies to the **actual finite physical eigenframe**. If `B=O diag(1,1,-1) O^T`, put `V_m=T_mO`. Then

\[
V_m^TV_m=I_3,
\qquad
\|\text{row}_i(V_m)\|^2=\frac1m\le\frac12,
\]

and the residual quadratic part is zero. Therefore, for every `m>=2`, the finite-stage output characteristic function satisfies the real inequality

\[
\boxed{
|\Phi_m(t)|
\le
\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.
}
\tag{4.1}
\]

The majorant is integrable (mass `24pi`). By (3.11), `Phi_m(t)->Phi_infty(t)` pointwise. Dominated convergence gives

\[
\|\Phi_m-\Phi_\infty\|_{L^1(\mathbb R)}\to0,
\]

and Fourier inversion yields the global all-output convergence

\[
\boxed{\|p_m-p_\infty\|_\infty\to0.}
\tag{4.2}
\]

Thus weak convergence cannot hide a narrowing finite-stage peak.

## 5. Global strict barrier for the off-axis Poisson limit

Condition on `N=k`. Since `G` is isotropic, after the orthogonal diagonalization of `B` the conditional law is a `(1,1,-1)` Gaussian quadratic form with mean of Euclidean norm `|k|`. For `k=0` its density norm is

\[
C_0=3\sqrt2.
\]

For `k\ne0`, `|k|>=1`; with `s=1/12`, equation (2.2) has `D>=12`, so

\[
\|p_{\infty\mid N=k}\|_\infty
\le
C_{12}:=e^{-6}(3\sqrt2)
+(1-e^{-6})\frac{12e^{-1/2}}{\sqrt{2\pi}}.
\tag{5.1}
\]

Because `P(N=0)=e^{-3}`,

\[
\boxed{
\|p_\infty\|_\infty
\le
C_{\rm Pois}
:=e^{-3}(3\sqrt2)
+(1-e^{-3})C_{12}
=2.973466964701133\ldots
<3\sqrt2.
}
\tag{5.2}
\]

Combining (4.2) and (5.2),

\[
\boxed{
\limsup_{m\to\infty}\|p_{Q_m}\|_\infty
\le2.973466964701133\ldots<3\sqrt2.
}
\tag{5.3}
\]

So root-`m`, non-Lindeberg, entrywise-dense, off-axis compound-Poisson displacement does **not** create a sharp-constant overshoot. In this explicit family the limiting global peak is even forced below `pi` by the displayed certificate.

## 6. Consequence for the sharp-witness search

The preceding argument pays more than the explicit Poisson construction. **Any** asymptotic witness mechanism that reduces to

\[
G+M,
\]

with `M` independent of a three-dimensional Gaussian core `G` whose covariance has minimum eigenvalue at least `1/12`, and whose indefinite quadratic coefficient matrix has spectral floor at least one, is globally capped by `3sqrt(2)` by Theorem 1. The location law may be discrete, singular, compound-Poisson, infinite-support, or otherwise rough.

Therefore the surviving sharp-witness frontier must alter more than the location of a minimum-variance Gaussian core: e.g. remove/deplete that Gaussian core, create a non-location shape component, couple the macroscopic component to the Gaussian core, retain several shared non-collinear macroscopic rows before aggregation, or exploit additional active spectrum in a way not representable as an independent random translation. Failure of a proof mechanism there would not be a QFORM counterexample. A finite peak above `3sqrt(2)` would refute only the candidate sharp constant; a genuine counterexample to QFORM must defeat every finite universal constant.

No continuity statement for the unrestricted target is claimed.
