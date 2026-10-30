# QFORM B17: second-order sharp asymptotics for the diffuse three-block witness

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: fleet03/B17  
Run: `20260922T133213Z-fleet03-B17-QFORM-r13`  
Status: SUPPORTING LEMMA; FULL CONJECTURE OPEN  
Execution memory status: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target family

Let all variables below be independent and uniform on `[-1/2,1/2]`. For `j=1,2,3`, set

\[
S_{j,m}=m^{-1/2}\sum_{k=1}^m X_{j,k},\qquad
Q_m=S_{1,m}^2+S_{2,m}^2-S_{3,m}^2.
\]

Equivalently, `Q_m=X^T A_m X` for

\[
A_m=\operatorname{diag}(J_m/m,J_m/m,-J_m/m),
\]

whose nonzero spectrum is exactly `\{1,1,-1\}`. Thus this is a source-valid full-target stress family, not a Gaussian replacement or a histogram surrogate.

The already-established CLT lower-bound mechanism gives `p_{Q_m}(0) -> 3 sqrt(2)`, hence any universal constant must satisfy `C >= 3 sqrt(2)`. This report sharpens that convergence to two orders and fixes its direction.

## 2. Theorem

Let `p_m` denote the density of `Q_m`. Then

\[
\boxed{
 p_m(0)=3\sqrt2\left(
 1-\frac{69}{320m}-\frac{17411}{2867200m^2}+O(m^{-5/2})
 \right).
}
\]

In particular, the diffuse block witness approaches `3 sqrt(2)` from below for all sufficiently large `m`, with relative first-order gap `69/(320m)`.

The conclusion is a sharp-constant supporting lemma only. It does **not** prove that `3 sqrt(2)` is the universal sharp constant.

## 3. Uniform Edgeworth expansion derived from the exact characteristic function

Let `f_m` be the density of

\[
S_m=m^{-1/2}\sum_{k=1}^m X_k.
\]

Its characteristic function is exactly

\[
\widehat f_m(t)=\left(\operatorname{sinc}\frac{t}{2\sqrt m}\right)^m,
\qquad \operatorname{sinc} u=\frac{\sin u}{u}.
\]

Using

\[
\log(\operatorname{sinc}u)
=-\frac{u^2}{6}-\frac{u^4}{180}-\frac{u^6}{2835}+O(u^8),
\]

we obtain on the Fourier central region

\[
\widehat f_m(t)
=e^{-t^2/24}\left[
1-\frac{t^4}{2880m}
+\frac1{m^2}\left(-\frac{t^6}{181440}
+\frac{t^8}{2\,2880^2}\right)
+O\!\left(\frac{(1+|t|^{12})e^{-c t^2}}{m^3}\right)
\right].
\]

A standard direct split of the exact sinc integral makes the expansion uniform: on `|t| <= delta sqrt(m)` use the Taylor remainder plus `|sinc u| <= exp(-c u^2)`; away from zero, `sup_{|u|>=delta}|sinc u|<1` on bounded sets and the `1/|u|` tail controls the rest. Fourier inversion therefore gives, uniformly in `x`,

\[
f_m(x)=\gamma(x)\left[
1-\frac{H_4(z)}{20m}
+\frac1{m^2}\left(\frac{H_6(z)}{105}+\frac{H_8(z)}{800}\right)
\right]+O(m^{-3}),
\]

where

\[
\gamma(x)=\sqrt{\frac6\pi}e^{-6x^2},\qquad z=\sqrt{12}\,x,
\]

and `H_k` are the probabilists' Hermite polynomials. The constants follow directly from the inverse transforms:

\[
\frac{12^2}{2880}=\frac1{20},\qquad
\frac{12^3}{181440}=\frac1{105},\qquad
\frac{12^4}{2\,2880^2}=\frac1{800}.
\]

The same sinc bound gives a uniform bound on `||f_m||_infinity`, which is enough below to integrate the `O(m^{-3})` remainder over an interval of length `O(sqrt(m))`.

## 4. Exact polar identity for the saddle density

If `U_m=S_m^2`, symmetry of `f_m` gives

\[
h_m(u)=\frac{f_m(\sqrt u)}{\sqrt u},\qquad u>0.
\]

Since `Q_m=U_m^{(1)}+U_m^{(2)}-U_m^{(3)}`,

\[
p_m(0)=\int_{u,v\ge0}h_m(u)h_m(v)h_m(u+v)\,du\,dv.
\]

With `u=x^2`, `v=y^2`, then polar coordinates `x=r cos(theta)`, `y=r sin(theta)`, this becomes the exact deterministic formula

\[
\boxed{
 p_m(0)=4\int_0^{\pi/2}\int_0^{\sqrt m/2}
 f_m(r\cos\theta)f_m(r\sin\theta)f_m(r)\,dr\,d\theta.
}
\]

No Monte Carlo input appears anywhere in the proof.

## 5. First-order coefficient

Under the Gaussian baseline, the product in the polar integral is proportional to `e^{-12r^2}`. Normalize this as a probability law on `(r,theta)` with `theta` uniform on `[0,pi/2]` and radial density proportional to `e^{-12r^2}`. Put

\[
z_1=\sqrt{12}r\cos\theta,\quad
z_2=\sqrt{12}r\sin\theta,\quad
z_3=\sqrt{12}r.
\]

The elementary moments

\[
E r^2=\frac1{24},\quad E r^4=\frac1{192},\quad
E\cos^2\theta=\frac12,\quad E\cos^4\theta=\frac38
\]

give

\[
E H_4(z_1)=E H_4(z_2)=\frac{57}{32},\qquad
E H_4(z_3)=\frac34.
\]

Therefore the relative coefficient of `1/m` is

\[
-\frac1{20}\left(2\cdot\frac{57}{32}+\frac34\right)
=-\frac{69}{320}.
\]

The zeroth-order integral is

\[
4\cdot\frac\pi2\left(\sqrt{\frac6\pi}\right)^3
\int_0^\infty e^{-12r^2}\,dr
=3\sqrt2.
\]

## 6. Second-order coefficient

The needed Hermite expectations are

\[
\begin{aligned}
E H_6(z_1)&=-\frac{945}{128}, & E H_8(z_1)&=\frac{91035}{2048},\\
E H_6(z_3)&=-\frac{15}{8}, & E H_8(z_3)&=\frac{105}{16},\\
E[H_4(z_1)H_4(z_2)]&=\frac{7803}{2048},
& E[H_4(z_1)H_4(z_3)]&=\frac{603}{128}.
\end{aligned}
\]

Hence one `z_1` or `z_2` second-order density contribution equals

\[
-\frac{4833}{327680},
\]

the `z_3` contribution equals

\[
-\frac{173}{17920},
\]

and the three pairwise products of first-order corrections contribute in total

\[
\frac{27099}{819200}.
\]

Adding them gives

\[
2\left(-\frac{4833}{327680}\right)
-\frac{173}{17920}
+\frac{27099}{819200}
=\boxed{-\frac{17411}{2867200}}.
\]

The Gaussian tail beyond `r=sqrt(m)/2` is exponentially small. The uniform `O(m^{-3})` density remainder integrated over the physical radial support of length `O(sqrt(m))` is `O(m^{-5/2})`; products with bounded leading factors obey the same or smaller order. This proves the displayed theorem.

## 7. Exact finite check at m=2

For `m=2`, the family is the six-variable witness already known in the programme:

\[
Q_2=\frac{(X_1+X_2)^2+(X_3+X_4)^2-(X_5+X_6)^2}{2},
\]

and direct piecewise-polynomial integration gives

\[
p_2(0)=2\pi-\frac73=3.9498519738\ldots.
\]

This is consistent with, but not used to prove, the asymptotic theorem.

## 8. Application of completed partner mathematics

Apply fleet04/B18's completed Schur-pivot square-smoothing theorem: for a physical nonsingular `3x3` block `B` with suitable definite Schur complement,

\[
\|p_Q\|_\infty\le \frac{2\sqrt\pi}{(|a\det B|)^{1/4}}.
\]

Every nonsingular physical triple of the present `A_m` that takes one coordinate from each bank is

\[
B=\operatorname{diag}(1/m,1/m,-1/m).
\]

Choosing the positive pivot `a=1/m`, `|\det B|=m^{-3}`, so the partner theorem gives exactly

\[
\|p_{Q_m}\|_\infty\le2\sqrt\pi\,m.
\]

But the actual saddle density satisfies

\[
p_m(0)=3\sqrt2\,(1+o(1)).
\]

Thus a proof that selects **one** physical triple and pays this inverse-determinant estimate loses linearly in `m` on the canonical sharp-constant witness. This is a target-relevant obstruction to one-minor closure, not a defect of the partner theorem. Any near-sharp general proof must aggregate diffuse coordinate mass before taking inverse determinant powers, or use a different global mechanism.

## 9. Implication for the sharp constant search

The block-CLT lower bound `C>=3sqrt(2)` is not an artifact of an uncontrolled weak limit: the exact finite target family has a two-term local expansion at the singular output value and approaches the lower bound from below. Thus this family supports `3sqrt(2)` as a plausible sharp constant but does not establish extremality among all matrices/product laws.

The next sharp-witness test should therefore change mechanism: search mixed-leverage or non-identical-bank laws where the first Edgeworth correction can change sign, or prove a structural inequality forcing the three-bank saddle to dominate all diffuse rank-three limits.

## 10. Scope and status

- New mathematics: exact two-term asymptotic and its negative coefficients; quantified application to the completed Schur-pivot theorem.
- Previously known input: target statement, `C>=3sqrt(2)` limit, exact `m=2` value, partner Schur-pivot theorem.
- Not proved: universal upper bound; global sharpness of `3sqrt(2)`; continuity for the full target.
- Full QFORM conjecture: OPEN.
