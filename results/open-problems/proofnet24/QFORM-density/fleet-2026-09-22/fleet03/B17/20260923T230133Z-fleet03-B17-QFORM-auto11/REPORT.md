SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T23:01:33Z.
attacking: two-heavy/one-diffuse exact rotated null-pivot witness; prove a global output-density ceiling for arbitrary cap-one heavy laws and transfer it to exact finite uniform-bank approximants.

# QFORM B17 — global two-heavy / one-diffuse null-pivot witness exclusion

Run: `20260923T230133Z-fleet03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING ANALYTIC WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED**  
Full-target continuity: **OPEN**. This report proves essential boundedness for the stated stress family; it does not claim continuity for arbitrary heavy laws.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Let
\[
n=\left(\frac12,\frac12,\frac1{\sqrt2}\right),\qquad
B=I-2nn^T=
\begin{pmatrix}
\frac12&-\frac12&-\frac1{\sqrt2}\\
-\frac12&\frac12&-\frac1{\sqrt2}\\
-\frac1{\sqrt2}&-\frac1{\sqrt2}&0
\end{pmatrix}.
\tag{1.1}
\]
Then `B^2=I` and
\[
\operatorname{spec}(B)=\{1,1,-1\}.
\tag{1.2}
\]
In particular this is a genuinely rotated indefinite three-eigenvalue form with a zero physical pivot and nonzero couplings from that pivot to both heavy coordinates.

Let `(X,Y)` have any joint probability density `rho` on `R^2` satisfying
\[
0\le \rho\le1,
\tag{1.3}
\]
and let `Z~N(0,v)`, `v=1/12`, be independent. (The target case of independent cap-one `X,Y` is included because then `rho(x,y)=f(x)g(y)<=1`.) Put
\[
Q=(X,Y,Z)^TB(X,Y,Z)
 =\frac12(X-Y)^2-\sqrt2(X+Y)Z.
\tag{1.4}
\]
Then `Q` has an essentially bounded density and, **globally over every output level**,
\[
\boxed{
\|p_Q\|_\infty
\le C_{2H1G}:=
\frac{2^{13/6}\sqrt3}{\sqrt\pi}\,
\Gamma\!\left(\frac54\right)^{2/3}
=4.1092705664512960983\ldots
<3\sqrt2.
}
\tag{1.5}
\]
At the cone tip there is the sharper bound
\[
\boxed{
p_Q(0)\le
\frac{2^{11/6}\sqrt3}{\sqrt\pi}\,
\Gamma\!\left(\frac54\right)^{2/3}
=3.2615302100033731854\ldots .}
\tag{1.6}
\]
No connected-support, bounded-support, moment, centering, log-concavity, or interval assumption is made on the heavy law. The argument even allows dependence between the two heavy coordinates provided only their joint density has cap one.

Moreover there is an exact finite target family. For every `m>=3`, let `U_1,...,U_m` be iid `Unif[-1/2,1/2]`, independent of the heavy coordinates, and set
\[
Z_m=m^{-1/2}\sum_{k=1}^m U_k.
\tag{1.7}
\]
Let `R_m` have physical rows `e_1,e_2` and `m` copies of `e_3/sqrt(m)`, and set
\[
A_m=R_mBR_m^T.
\tag{1.8}
\]
Then `R_m^TR_m=I_3`, so the exact nonzero spectrum of every finite `A_m` is
\[
\boxed{\{1,1,-1\}},
\tag{1.9}
\]
and every physical diffuse input has a cap-one uniform density. The physical form is exactly
\[
Q_m=\frac12(X-Y)^2-\sqrt2(X+Y)Z_m.
\tag{1.10}
\]
Using the completed `fleet04/B17` weighted local Edgeworth theorem, uniformly even when the heavy laws change with `m`,
\[
\boxed{
\limsup_{m\to\infty}
\sup_{f_m,g_m\le1}\|p_{Q_m}\|_\infty
\le C_{2H1G}<3\sqrt2.
}
\tag{1.11}
\]
Thus this canonical **two macroscopic heavy rows + one diffuse bank + zero physical pivot** architecture cannot improve the currently certified universal lower obstruction `3sqrt(2)`; this conclusion includes off-tip output levels.

## 2. Exact conditional kernel

Write
\[
u=x-y,\qquad s=x+y.
\]
Conditioning on `(X,Y)=(x,y)`, for `s!=0` the density of `Q` at level `q` is
\[
K_q(x,y)=
\frac1{2\sqrt{\pi v}|s|}
\exp\!\left[-\frac{(q-u^2/2)^2}{4vs^2}\right].
\tag{2.1}
\]
The line `s=0` has two-dimensional Lebesgue measure zero. Hence Tonelli/Fubini gives the density representative
\[
p_Q(q)=\iint \rho(x,y)K_q(x,y)\,dx\,dy
\tag{2.2}
\]
for almost every `q`; the uniform bound below supplies an `L^infty` representative.

## 3. Exact cone-tip superlevel law

Set
\[
c=(2\sqrt{\pi v})^{-1},\qquad a=(16v)^{-1}.
\]
At `q=0`,
\[
K_0=\frac c{|s|}\exp\!\left(-a\frac{u^4}{s^2}\right).
\tag{3.1}
\]
For `t>0`, `K_0>t` forces `|s|<c/t`, and then
\[
|u|<a^{-1/4}|s|^{1/2}
\left[\log\frac{c}{t|s|}\right]^{1/4}.
\tag{3.2}
\]
Since `dx dy=(1/2) du ds`, direct integration yields the **exact** distribution function
\[
|\{(x,y):K_0(x,y)>t\}|=D_vt^{-3/2},
\tag{3.3}
\]
where
\[
D_v=\sqrt2\,\pi^{-3/4}v^{-1/2}
\frac{\Gamma(5/4)}{(3/2)^{5/4}}.
\tag{3.4}
\]
Indeed
\[
\int_0^1 r^{1/2}(-\log r)^{1/4}\,dr
=\frac{\Gamma(5/4)}{(3/2)^{5/4}}.
\]
Therefore the decreasing rearrangement is exactly
\[
K_0^*(r)=\left(\frac{D_v}{r}\right)^{2/3}.
\tag{3.5}
\]
For every probability density `rho<=1`, the bathtub/Hardy--Littlewood inequality gives
\[
p_Q(0)\le\int_0^1K_0^*(r)\,dr=3D_v^{2/3}.
\tag{3.6}
\]
Putting `v=1/12` gives (1.6).

## 4. Uniformity over every output level

For fixed `s` and threshold `t`, the condition `K_q>t` is
\[
\left|\frac{u^2}{2}-q\right|<d,
\qquad
d=2\sqrt v|s|
\sqrt{\log\frac c{t|s|}}.
\tag{4.1}
\]
The `q=0` section in `u` has length `2sqrt(2d)`. If `q<0`, the section length can only decrease. If `0<=q<d`, its ratio to the `q=0` length is
\[
\sqrt{1+q/d}\le\sqrt2.
\tag{4.2}
\]
If `q>=d`, the ratio is
\[
\sqrt{q/d+1}-\sqrt{q/d-1}\le\sqrt2,
\tag{4.3}
\]
the last expression being decreasing for `q/d>=1`. Consequently, for every real `q` and every `t>0`,
\[
|\{K_q>t\}|\le\sqrt2D_vt^{-3/2}.
\tag{4.4}
\]
Thus
\[
K_q^*(r)\le\left(\frac{\sqrt2D_v}{r}\right)^{2/3},
\]
and another bathtub integration gives
\[
\sup_qp_Q(q)\le3(\sqrt2D_v)^{2/3}.
\tag{4.5}
\]
At `v=1/12`, (4.5) simplifies exactly to the constant in (1.5).

This step is deliberately a direct superlevel/coarea calculation. It does not use the refuted arbitrary-joint quadratic coarea cap, does not assert post-rotation independence, and does not use pointwise quadratic-phase decay.

## 5. Analytic strict gap below `3sqrt(2)`

The numerical comparison in (1.5) is not needed for rigor. Strict log-convexity of the gamma function, with `5/4` the midpoint of `1` and `3/2`, gives
\[
\Gamma(5/4)^2<\Gamma(1)\Gamma(3/2)=\frac{\sqrt\pi}{2}.
\tag{5.1}
\]
Hence
\[
C_{2H1G}<2^{11/6}\sqrt3\,\pi^{-1/3}.
\tag{5.2}
\]
After division by `3sqrt(2)`, cubing reduces the desired strict inequality to
\[
\frac{16}{3\sqrt3\,\pi}<1.
\tag{5.3}
\]
For a rational certificate, Archimedes' lower bound `pi>223/71` suffices because
\[
\frac{223}{71}>\frac{16}{3\sqrt3};
\]
a denominator-free verification is
\[
(669\sqrt3)^2=1,342,683>1,290,496=1136^2.
\tag{5.4}
\]
Thus the global ceiling is analytically and strictly below `3sqrt(2)`.

## 6. Exact finite cap-one transfer using the designated partner result

The completed designated-partner result is

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,  
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`.

For the density `g_m` of the normalized uniform bank `Z_m`, that report proves the weighted local Edgeworth expansion at variance `v=1/12`,
\[
g_m(z)=\gamma_v(z)
\left[1-\frac1{20m}H_4(z/\sqrt v)\right]
+O(m^{-2})(1+|z|)^{-8}.
\tag{6.1}
\]
In particular there is an absolute finite `C_E` such that, for all sufficiently large `m`,
\[
|g_m(z)-\gamma_v(z)|
\le \frac{C_E}{m}(1+|z|)^{-8}.
\tag{6.2}
\]
This is the partner theorem applied at an actual inequality in the present proof.

For a heavy joint density `rho<=1`, the exact root formula is
\[
p_{m,\rho}(q)=\iint
\rho(x,y)\frac1{\sqrt2|s|}
 g_m\!\left(\frac{u^2/2-q}{\sqrt2s}\right)dxdy.
\tag{6.3}
\]
Subtracting the Gaussian version and using (6.2),
\[
|p_{m,\rho}(q)-p_{\infty,\rho}(q)|
\le \frac{C_E}{\sqrt2m}J_q(\rho),
\tag{6.4}
\]
where
\[
J_q(\rho)=\iint\rho(x,y)|s|^{-1}
\left(1+\frac{|u^2/2-q|}{\sqrt2|s|}\right)^{-8}dxdy.
\tag{6.5}
\]
This integral is uniformly bounded in `q` and `rho`. On `|s|>=1`, its contribution is at most one. On `|s|<1`, drop `rho<=1`; layer-cake plus the section comparison (4.2)--(4.3) gives at most `sqrt(2)` times the `q=0` section. Define
\[
C_8=\int_{\mathbb R}(1+r^2)^{-8}dr
=\frac{\sqrt\pi\Gamma(15/2)}{\Gamma(8)}.
\tag{6.6}
\]
Then
\[
\int_{\mathbb R}
\left(1+\frac{u^2}{2\sqrt2|s|}\right)^{-8}du
=2^{3/4}|s|^{1/2}C_8.
\tag{6.7}
\]
Using `dxdy=(1/2)duds` therefore yields
\[
\boxed{J_q(\rho)\le C_J:=1+2^{9/4}C_8<\infty.}
\tag{6.8}
\]
Numerically `C_8=0.6580777580...` and `C_J=4.1303630081...`; only finiteness and universality are used.

Combining (6.4), (6.8), and the global Gaussian endpoint bound (1.5),
\[
\sup_{\rho\le1,\int\rho=1}\sup_qp_{m,\rho}(q)
\le C_{2H1G}+\frac{C_EC_J}{\sqrt2m}.
\tag{6.9}
\]
This is uniform even for a sequence of adversarial heavy laws depending on `m`, proving (1.11).

Finally, the same `fleet04/B17` completed family proves by exact finite cap-one rotated forms that every universal target constant satisfies
\[
C_*\ge3\sqrt2.
\tag{6.10}
\]
Applying (6.10) to (1.11) gives the actual witness comparison
\[
\boxed{
\limsup_m\sup_{f_m,g_m\le1}\|p_{Q_m}\|_\infty
\le C_{2H1G}<3\sqrt2\le C_*.
}
\tag{6.11}
\]
So the present two-heavy/one-diffuse null-pivot architecture cannot be the mechanism that raises the sharp universal lower bound beyond `3sqrt(2)`.

## 7. Scope, corrections, and next witness frontier

This is **not** the unrestricted theorem. The argument fixes a specific exact rotated core `B` and a one-bank diffuse third coordinate. It does not cover two or more diffuse/shared banks with surviving non-Gaussian components, arbitrary additional spectrum, or arbitrary physical matrices. The full QFORM conjecture remains open.

Continuity is also kept separate. This report establishes existence of an essentially bounded density in the stated Gaussian endpoint and asymptotic finite-bank family through the explicit conditional/root formulas, but it does not claim a continuous representative for arbitrary rough heavy laws, and it does not establish full-target continuity.

Corrections consumed include: law-uniform pointwise quadratic-phase decay is false; independence is not preserved by spectral rotation; arbitrary-joint quadratic coarea caps are false; naive fiber-supremum integration loses dimension; fixed-fragment and bounded-diameter localization are false; and the near-zero half-Riesz-only interface is false. None is used here.

The next genuinely different B17 witness mechanism is therefore a **two-heavy / multiple-shared-diffuse-row family with a surviving non-Gaussian component**, or a construction where additional spectrum interacts with the heavy core. The canonical one-heavy family, the three-diffuse CLT family, the dense three-heavy Householder cube, and now this two-heavy/one-diffuse zero-pivot family all lie strictly below or approach `3sqrt(2)` without overshooting it in their proved scopes.

## 8. Source provenance

Fresh initial brain main: `3eeed8243e52874c0eb47bf7b710c96f65aa8b16`.  
Fresh prepublication brain main: `359b5871c008e51f8e6ae22ae88c5c3b208e4514`.  
Designated partner theorem actually used: `math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`, exact path given in Section 6.  
Native learned-memory status: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not claimed as native receiver ingestion.
