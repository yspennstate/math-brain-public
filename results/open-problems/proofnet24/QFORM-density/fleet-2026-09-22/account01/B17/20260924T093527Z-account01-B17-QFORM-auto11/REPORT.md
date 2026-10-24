# account01/B17 — two-macroscopic-row minority witness

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T093527Z-account01-B17-QFORM-auto11`  
Status: `NEW SUPPORTING THEOREM / EXACT DENSE WITNESS / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted QFORM theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. Unrestricted continuity remains separate. The strongest source-valid numerical lower obstruction remains `C >= 3 sqrt(2)` from the diffuse three-direction cube/Gaussian limit. This run does not improve that number; it makes the near-extremal geometry substantially less diffuse.

## 1. Two equal macroscopic rows: exact global barrier

Let `0 <= q <= 1`. Take independent standard normals `G1,G2,N` and independent `U1,U2 ~ Unif[-1/2,1/2]`. Put

\[
Y_1=G_1/\sqrt{12},\qquad Y_2=G_2/\sqrt{12},
\]
\[
Z_q=\sqrt{\frac{1-q}{12}}N+\sqrt{\frac q2}(U_1+U_2),
\qquad Q_q=Y_1^2+Y_2^2-Z_q^2.
\]

The covariance is exactly minimal/isotropic:

\[
\operatorname{Var}(Y_1)=\operatorname{Var}(Y_2)=\operatorname{Var}(Z_q)=\frac1{12}.
\]

### Theorem A (`QFORM-TWO-MACRO-MINORITY-BARRIER-v1`)

For every `0 <= q <= 1`, the density of `Q_q` is globally maximized at zero and

\[
\boxed{
\|p_{Q_q}\|_\infty=p_{Q_q}(0)
=\frac{12}{\sqrt{2-q}}\int_0^1(1-s)
\exp\!\left[-\frac{3q}{2-q}s^2\right]ds
\le 3\sqrt2 .
}
\tag{1.1}
\]

The inequality is strict for every `q>0`.

#### Global-mode proof

`S=Y_1^2+Y_2^2` is exponential with density `6 exp(-6s)` on `s>=0`. The law of `Z_q` is symmetric log-concave (convolution of a centered Gaussian with a centered triangular law), so its density decreases on `[0,infinity)`. Therefore the density of `T=Z_q^2` is decreasing. For `x>=0`,

\[
p_{Q_q}(x)=e^{-6x}p_{Q_q}(0),
\]

while for `r>=0`,

\[
p_{Q_q}(-r)=\int_0^\infty 6e^{-6u}f_T(u+r)du
\le p_{Q_q}(0).
\]

Hence the global norm equals the cone-tip value.

#### Exact cone-tip formula

Condition on `U_1+U_2=s`, whose density is `1-|s|` on `[-1,1]`. Gaussian integration gives

\[
\mathbb E\left[e^{-6Z_q^2}\mid s\right]
=(2-q)^{-1/2}
\exp\!\left[-\frac{3q}{2-q}s^2\right],
\]

and `p_{Q_q}(0)=6 E exp(-6Z_q^2)`, proving (1.1) except for the last inequality.

Set

\[
a=\frac{3q}{2-q}\in[0,3],\qquad
I_0(a)=\int_0^1(1-s)e^{-as^2}ds,
\]
\[
K(a)=\frac{p_{Q_q}(0)}{3\sqrt2}
=2\sqrt{\frac{a+3}{3}}I_0(a).
\]

For `a>0`, with `I_2(a)=\int_0^1s^2(1-s)e^{-as^2}ds`,

\[
\frac{K'(a)}{K(a)}=\frac1{2(a+3)}-\frac{I_2(a)}{I_0(a)}.
\]

A direct integration gives

\[
2a^2\bigl(2(a+3)I_2-I_0\bigr)
=H(a):=3\sqrt{\pi a}\,\operatorname{erf}(\sqrt a)
-(a+6)(1-e^{-a}).
\tag{1.2}
\]

It remains to show `H(a)>=0` on `[0,3]`. Write `S_9(x)=sum_{j=0}^9(-x)^j/j!`. Taylor's remainder gives `e^{-x}>=S_9(x)` for `x>=0`. Since

\[
H(a)=6a\int_0^1e^{-au^2}du-(a+6)(1-e^{-a}),
\]

we have

\[
H(a)\ge H_9(a):=
6a\int_0^1S_9(au^2)du-(a+6)(1-S_9(a)).
\]

Put `t=a/3`. Exact conversion to the Bernstein basis gives

\[
\frac{H_9(a)}{a^3}
=\sum_{j=0}^7\beta_j{7\choose j}t^j(1-t)^{7-j},
\]

where

\[
(\beta_0,\ldots,\beta_7)=
\left(
\frac1{10},\frac{73}{980},\frac{337}{5880},\frac{4847}{107800},
\frac{100553}{2802800},\frac{973307}{33633600},
\frac{9059871}{381180800},\frac{7674201}{517316800}
\right).
\]

Every coefficient is positive, hence `H(a)>0` for `a>0`. Thus `K` is strictly decreasing and `K(a)<=K(0)=1`. This proves Theorem A.

The small-`q` expansion is

\[
\boxed{
\frac{\|p_{Q_q}\|_\infty}{3\sqrt2}
=1-\frac{3q^2}{160}-\frac{q^3}{224}+O(q^4).
}
\tag{1.3}
\]

For comparison, the previously proved one-macroscopic-row minority family has relative quadratic loss `3q^2/80`; splitting the same macroscopic variance equally over two rows halves the leading loss.

More generally, for `k` equal minority rows

\[
Z_{q,k}=\sqrt{\frac{1-q}{12}}N+\sqrt{\frac qk}\sum_{j=1}^kU_j,
\]

the same moment calculation yields the cone/global-mode expansion

\[
\boxed{
\frac{\|p_{Y_1^2+Y_2^2-Z_{q,k}^2}\|_\infty}{3\sqrt2}
=1-\frac{3q^2}{80k}+O_k(q^3).
}
\tag{1.4}
\]

Thus a proposed sharp proof cannot charge a smoothing penalty depending only on the total macroscopic variance `q`; the fragmentation count / fourth cumulant matters.

## 2. Exact entrywise-dense finite target witness with two leverage-1/4 rows

Let

\[
n=\frac{(1,2,4)^T}{\sqrt{21}},\qquad
P=nn^T,\qquad B=I-2P,
\]

so `B^2=I` and `spec(B)={1,1,-1}`. Let

\[
V=\frac12\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},\qquad V^TV=I.
\]

Fix `q=1/2` and put

\[
S=(I-qP)^{1/2}=I+(2^{-1/2}-1)P.
\]

For every `m>=2`, form `R_m` with two macroscopic rows `n^T/2`, followed by `m` copies of each of the four rows of `VS/sqrt(m)`. Then

\[
R_m^TR_m=\frac12P+S^2=I.
\]

Define the physical matrix

\[
A_m=R_mBR_m^T.
\]

Therefore

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.}
\tag{2.1}
\]

The two distinguished physical rows have leverage exactly `1/4`. Every physical matrix entry is nonzero. Indeed, the diffuse `4 x 4` block before the factor `1/m` is

\[
V(I-\tfrac32P)V^T=
\begin{pmatrix}
-1/8&-1/8&3/8&3/8\\
-1/8&33/56&-11/56&29/56\\
3/8&-11/56&41/56&9/56\\
3/8&29/56&9/56&17/56
\end{pmatrix},
\tag{2.2}
\]

and the four macro-diffuse overlaps are proportional to

\[
Vn=(\sqrt{21}/6,\sqrt{21}/14,-\sqrt{21}/42,-5\sqrt{21}/42)^T,
\]

all nonzero; the macro-macro block is constantly `-1/4`.

Take all physical coordinates iid `U[-1/2,1/2]`. The latent vector `R_m^TX` converges to the hybrid in Theorem A with `q=1/2`. The completed source-pinned Fresnel--Brascamp--Lieb Theorem F at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

applies to the actual finite eigenframe: the two macro leverages are `1/4`, every diffuse leverage is at most `3/(4m)<=3/8`, the residual quadratic part is zero, and the three active eigenvalues have product one. It supplies a common integrable `O(|t|^{-3/2})` characteristic-function majorant. Hence the complete output densities converge uniformly to the hybrid density.

At `q=1/2`, `a=1` and Theorem A gives the exact limit

\[
\boxed{
C_2=2\sqrt6\bigl(\sqrt\pi\,\operatorname{erf}(1)-1+e^{-1}\bigr)
=4.22060656184208255745\ldots .
}
\tag{2.3}
\]

Therefore

\[
\boxed{
\|p_{X^TA_mX}\|_\infty\longrightarrow C_2,
\qquad
3\sqrt2-C_2=0.02203412527720258896\ldots .
}
\tag{2.4}
\]

This does not beat the diffuse obstruction `3 sqrt(2)`, but it shows that an exact target matrix can have **two genuinely non-infinitesimal leverage-1/4 physical coordinates**, be entrywise dense, and still lie within about `0.0221` of the known obstruction. A proof cannot expect a large fixed smoothing gain merely from detecting two macroscopic coordinates.

## 3. Required partner application: uncompensated sibling

Now keep the same `n`, `B`, two macro rows `n^T/2`, but replace the diffuse rows by `m` copies of the rows of `V/sqrt(m)` (no covariance compensation). Call the synthesis matrix `R~_m` and

\[
\widetilde A_m=\widetilde R_mB\widetilde R_m^T.
\]

Then

\[
\widetilde R_m^T\widetilde R_m=I+\frac12P,
\]

which commutes with `B`, and therefore

\[
\boxed{\operatorname{spec}_{\ne0}(\widetilde A_m)=\{1,1,-3/2\}.}
\tag{3.1}
\]

It is again entrywise dense. Its diffuse block before `1/m` is

\[
VBV^T=
\begin{pmatrix}
-5/12&-1/4&5/12&7/12\\
-1/4&15/28&-5/28&17/28\\
5/12&-5/28&61/84&11/84\\
7/12&17/28&11/84&13/84
\end{pmatrix},
\tag{3.2}
\]

and all macro-diffuse overlaps are nonzero.

For iid physical uniforms, the latent limit is

\[
Y=G+M,\qquad
G\sim N(0,I_3/12),\qquad
M=\frac12n(U_1+U_2).
\]

Apply the completed partner theorem `QFORM-RANDOM-LOCATION-GAUSSIAN-INDEFINITE-BARRIER-v1` from

`yspennstate/math-open-problems@97d91254e56ad2f8c79b121a0ce8bf66472a11d9:proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260924T074629Z-account02-B17-QFORM-auto11/REPORT.md`.

Its quantitative deterministic-translation estimate gives, with `s=1/12`,

\[
C_0=3\sqrt2,\qquad
C_1=\frac{12e^{-1/2}}{\sqrt{2\pi}},
\]

and conditional multiplier `exp(-|M|^2/(2s))`. Since `U_1+U_2` has triangular density,

\[
E_*:=\mathbb E\exp\!\left[-\frac32(U_1+U_2)^2\right]
=-\frac23+\frac23e^{-3/2}
+\frac{\sqrt{6\pi}}3\operatorname{erf}(\sqrt6/2)
=0.808788665112956\ldots .
\]

Averaging the partner inequality therefore gives the actual global bound

\[
\boxed{
\|p_{Y^TBY}\|_\infty
\le C_1+(C_0-C_1)E_*
=3.98661024075580832404\ldots<4.
}
\tag{3.3}
\]

For the finite physical matrices, the normalized physical eigenframe has macro leverage `1/6` and diffuse leverage at most `3/(4m)`, so the same pinned Theorem F gives a common integrable Fourier majorant and uniform density convergence. Consequently

\[
\boxed{
\limsup_{m\to\infty}
\|p_{X^T\widetilde A_mX}\|_\infty
\le3.986610240755809,
}
\tag{3.4}
\]

and in particular `||p||_inf<3.99` for all sufficiently large `m`. This is the designated account02/B17 theorem applied to an actual target-valid, entrywise-dense finite family.

## 4. Scope and remaining sharp-witness frontier

The new result pays **two collinear macroscopic rows on the minority eigendirection**. It does not pay two non-collinear shared rows. The strongest surviving witness mechanisms are therefore narrower:

- two or more non-collinear macroscopic rows coupling majority and minority directions before aggregation;
- rough non-Gaussian residual shapes not representable as an independent translation of a covariance-floor Gaussian core;
- additional active spectrum that survives aggregation;
- off-zero/two-sheet effects in those genuinely coupled settings.

The latest live correction `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1` was consumed: no universal `|t|^{-1/2}||G_t||_2` receiver is used here. The older corrections forbidding arbitrary-joint coarea, post-rotation independence, uniform pointwise quadratic-phase decay, fiber-sup dimension-free bounds, and conditional-density shortcuts are also preserved. The only finite-stage Fourier receiver used above is the explicitly scoped source-pinned Theorem F, whose leverage hypotheses are checked on the actual physical eigenframes.

Full unrestricted QFORM status: **OPEN**. Continuity: **separate / OPEN at the unrestricted level**.
