# QFORM-HOUSEHOLDER-ONEHEAVY-GAUSSIANPAIR-GLOBAL-v1

Run: `20260924T110434Z-account03-B17-QFORM-auto11`
Worker: `account03/B17` (Sharp constant and witnesses)
Status: **PROVED SUPPORTING THEOREM / EXACT SOURCE-VALID STRESS FAMILY**. Full QFORM remains OPEN. Full-target continuity remains OPEN.


## 1. Exact source-valid family

Let

\[
n=\frac{(1,2,3)}{\sqrt{14}},\qquad
B=I-2nn^T=\frac17
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\]

Then `B=B^T`, `B^2=I`, every entry of `B` is nonzero, and

\[
\operatorname{spec}(B)=\{1,1,-1\}.
\]

Let `H,G_2,G_3` be independent. Assume only that `H` has a probability density `f_H` satisfying `0<=f_H<=1`. Let

\[
G_2,G_3\stackrel{\rm iid}{\sim}N(0,s),\qquad s\ge \frac1{2\pi}.
\]

The Gaussian density cap is

\[
\|\gamma_s\|_\infty=(2\pi s)^{-1/2}\le1,
\]

so **all three original inputs satisfy the exact target cap-one hypothesis**. Define

\[
Q=(H,G_2,G_3)^TB(H,G_2,G_3).
\]

The theorem proved below is

\[
\boxed{
\|p_Q\|_\infty\le
\sqrt{\frac{2d}{\pi s}}\,K(-d),\qquad d=\frac76,
}
\tag{1}
\]

where

\[
K(m):=\int_0^{\pi/2}\frac{du}{\sqrt{1-m\sin^2u}}
\]

is the complete elliptic integral in the parameter convention. In particular, at the smallest source-valid Gaussian variance `s=1/(2pi)`,

\[
\boxed{
\|p_Q\|_\infty
\le \sqrt{\frac{14}{3}}\,K\!\left(-\frac76\right)
=2.7709849277641085\ldots
}
\tag{2}
\]

and, without using the numerical evaluation,

\[
\boxed{
\|p_Q\|_\infty
\le \pi\sqrt{\frac76}
=3.393307894656420\ldots .
}
\tag{3}
\]

Thus the entire negative-two-sheet/off-tip output of this fully coupled one-heavy architecture is uniformly controlled, not merely its cone tip.

## 2. Product-preserving reduction

Only the isotropic Gaussian pair is rotated. Set

\[
Z=\frac{2G_2+3G_3}{\sqrt{13}},\qquad
W=\frac{-3G_2+2G_3}{\sqrt{13}}.
\]

Because `(G_2,G_3)` is an isotropic Gaussian pair, `Z,W` remain independent `N(0,s)` and remain independent of `H`. **No analogous rotation is asserted for general cap-one product inputs.**

A direct expansion gives

\[
Q=\frac67H^2-\frac{2\sqrt{13}}7HZ-\frac67Z^2+W^2.
\]

Completing the square in the original arbitrary variable `H`,

\[
\boxed{
Q=\frac67\left(H-\frac{\sqrt{13}}6Z\right)^2+W^2-\frac76Z^2.
}
\tag{4}
\]

Write

\[
a=\frac67,\qquad d=\frac76=a^{-1}.
\]

## 3. Conditional density in the arbitrary cap-one coordinate

Fix `z,w`. The random variable

\[
Y_z=a\left(H-\frac{\sqrt{13}}6z\right)^2
\]

has a density on `(0,infinity)` equal to

\[
g_z(y)=
\frac{
 f_H(\frac{\sqrt{13}}6z+\sqrt{y/a})+
 f_H(\frac{\sqrt{13}}6z-\sqrt{y/a})
}{2\sqrt{ay}}.
\]

Therefore, using only `0<=f_H<=1`,

\[
0\le g_z(y)\le \frac1{\sqrt{ay}}.
\tag{5}
\]

Averaging the conditional densities in `(Z,W)` proves that `Q` is absolutely continuous and, for every real `q`,

\[
p_Q(q)
\le a^{-1/2}\,
\mathbb E\left[(q-W^2+dZ^2)_+^{-1/2}\right].
\tag{6}
\]

This step is a genuine original-product conditioning argument; it does not invoke an arbitrary-joint coarea bound or a conditional projection-density moment.

Scale

\[
Z=\sqrt{s}\,A,\qquad W=\sqrt{s}\,C,
\]

with independent standard normals `A,C`, and put `x=q/s`. Then

\[
p_Q(q)\le \sqrt{\frac d s}\,F(x),
\qquad
F(x):=\mathbb E\big[(x+dA^2-C^2)_+^{-1/2}\big].
\tag{7}
\]

The essential missing implication is therefore to bound `sup_x F(x)` globally, including the negative two-sheet side.

## 4. Global mode theorem: `F(x)<=F(0)` for every real x

### 4.1 Nonnegative output side

For `y>0` define

\[
\psi(y):=\mathbb E[(y-C^2)_+^{-1/2}].
\]

With `C=sqrt(y) sin(theta)`, one obtains the exact representation

\[
\psi(y)=\frac1{\sqrt{2\pi}}
\int_{-\pi/2}^{\pi/2}
\exp\!\left(-\frac y2\sin^2\theta\right)d\theta.
\tag{8}
\]

The integrand decreases pointwise in `y`, hence `psi` is decreasing. For `x>=0`,

\[
F(x)=\mathbb E\,\psi(x+dA^2)
\le \mathbb E\,\psi(dA^2)=F(0).
\tag{9}
\]

### 4.2 Negative two-sheet side

For `c>0` define

\[
\chi(c):=\mathbb E[(dA^2-c)_+^{-1/2}].
\]

With `A=sqrt(c/d) cosh(u)` on the two Gaussian tails,

\[
\chi(c)=\sqrt{\frac2{\pi d}}
\int_0^\infty
\exp\!\left[-\frac{c}{2d}\cosh^2u\right]du.
\tag{10}
\]

Again the integrand decreases pointwise in `c`, so `chi` is decreasing. For `r>0`, conditioning on `C`,

\[
F(-r)=\mathbb E\,\chi(C^2+r)
\le \mathbb E\,\chi(C^2)=F(0).
\tag{11}
\]

Equations (9) and (11) prove the exact global statement

\[
\boxed{\sup_{x\in\mathbb R}F(x)=F(0).}
\tag{12}
\]

This is the new step relative to the preceding B17 cone-tip run: the entire off-tip negative two-sheet regime is now paid for this exact family.

## 5. Exact cone integral

At zero,

\[
F(0)=\mathbb E[(dA^2-C^2)_+^{-1/2}].
\]

Use polar coordinates `A=r cos(theta)`, `C=r sin(theta)`. The radial singularity cancels the polar Jacobian:

\[
F(0)=\frac1{2\pi}
\left(\int_0^\infty e^{-r^2/2}dr\right)
\int_{d\cos^2\theta>\sin^2\theta}
\frac{d\theta}{\sqrt{d\cos^2\theta-\sin^2\theta}}.
\tag{13}
\]

The radial integral is `sqrt(pi/2)`. On one of the four congruent angular sectors set `t=tan(theta)=sqrt(d) sin(u)`. Then

\[
\int_0^{\arctan\sqrt d}
\frac{d\theta}{\sqrt{d\cos^2\theta-\sin^2\theta}}
=
\int_0^{\pi/2}\frac{du}{\sqrt{1+d\sin^2u}}
=K(-d).
\tag{14}
\]

Consequently

\[
\boxed{F(0)=\sqrt{\frac2\pi}\,K(-d).}
\tag{15}
\]

Combining (7), (12), and (15) proves (1). Since `K(-d)<=pi/2`, (3) follows at `s=1/(2pi)`.

## 6. Application of completed designated partner result

The completed designated partner theorem is account04/B17 `QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1`, canonical source

`yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260924T011922Z-account04-B17-QFORM-r6/REPORT.md`.

At its parameter `theta=0.01`, that exact source-valid fragmented sequence satisfies

\[
\liminf_m\|p_{Q_m}^{\rm partner}\|_\infty
\ge 3\sqrt2\,e^{-0.03}
=4.117251705266084\ldots .
\tag{16}
\]

The present exact source-valid fully coupled family satisfies the stronger exact formula (2), hence the actual inequality

\[
\boxed{
\liminf_m\|p_{Q_m}^{\rm partner}\|_\infty
-\sup_{H:\,\|f_H\|_\infty\le1}
\|p_Q^{\rm oneheavy+GaussPair}\|_\infty
\ge 1.3462667775019757\ldots .
}
\tag{17}
\]

Even without numerical elliptic evaluation, `K(-7/6)<=pi/2` gives

\[
3\sqrt2e^{-0.03}-\pi\sqrt{7/6}
=0.7239438106096641\ldots>0.
\tag{18}
\]

A coarse symbolic certificate is available from `pi<22/7` and `e^{-0.03}>0.97`: the partner lower bound is `>2.91 sqrt(2)`, whereas the present family is `<(11/7)sqrt(14/3)`; squaring already separates these bounds by a wide margin.

Interpretation: the completed partner's fragmented non-Gaussian mechanism is strictly more adverse than **every output level** of this one-heavy plus isotropic cap-one Gaussian-pair mechanism with the same fully coupled `(1,1,-1)` Householder geometry. An overshoot beyond the known `3sqrt(2)` obstruction cannot come from this mechanism.

## 7. Scope, continuity, and corrections

This theorem is **not** the unrestricted QFORM theorem. It fixes one exact fully coupled Householder orientation and permits one arbitrary cap-one coordinate plus an isotropic Gaussian pair whose variance is large enough for the original density-cap hypothesis. It does not treat arbitrary laws in all three coordinates, additional active spectrum, or several non-collinear macroscopic rows.

Essential boundedness and absolute continuity are proved above. **Continuity of the output density is not claimed in this run** for arbitrary merely measurable `f_H<=1`.

No step uses post-rotation independence for non-Gaussian coordinates, law-uniform pointwise van der Corput decay, arbitrary-joint coarea, a conditional projection-cap moment, naive fiber-sup integration, bounded fragment count, interval extremality, or Monte Carlo evidence.

Full QFORM and full-target continuity remain OPEN.

## 8. Next B17 mechanism

The one-heavy exact orientation is now globally closed for an arbitrary cap-one heavy coordinate against an isotropic cap-one Gaussian pair. The next materially different sharp-witness mechanism is therefore: (i) two or more non-collinear macroscopic original rows that survive bank aggregation, or (ii) a genuinely non-Gaussian pair on the two-sheet side, or (iii) extra active spectrum interacting with a non-Gaussian macroscopic component.
