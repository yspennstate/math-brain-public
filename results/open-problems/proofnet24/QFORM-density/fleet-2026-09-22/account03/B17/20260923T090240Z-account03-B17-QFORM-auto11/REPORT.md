SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B17, 2026-09-23T09:02:40Z.
attacking: off-center/two-sheet peaks for the two-heavy/finite-dimensional rotated witness boundary; derive a translation-uniform level-set envelope and compare it to the 3sqrt(2) obstruction.

# QFORM B17 — global ball-envelope exclusion for all 3D centered-cube rotations

Run: `20260923T090240Z-account03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING ANALYTIC WITNESS THEOREM; FULL QFORM OPEN / NOT PROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Let
\[
J=\operatorname{diag}(1,1,-1),
\]
let \(O\in O(3)\) be arbitrary, put \(A=OJO^T\), and let
\[
X_1,X_2,X_3\stackrel{\rm ind}{\sim}{\rm Unif}[-1/2,1/2].
\]
Then \(A\) has exact spectrum \(\{1,1,-1\}\), the input laws satisfy the owner's density cap exactly, and the law of
\[
Q=X^TAX
\]
has an essentially bounded density satisfying the orientation-uniform estimate
\[
\boxed{
\|p_Q\|_\infty\le \pi\sqrt{\frac32}
=3.8476494904855918\ldots
<3\sqrt2.
}
\tag{1.1}
\]
The same statement holds with the opposite signature \((-1,-1,1)\), by reflection of the output.

Thus **no three-variable centered-unit-interval witness with exact equal-magnitude indefinite spectrum can attain the current universal obstruction \(3\sqrt2\), no matter how densely the three physical coordinates are rotated together**.  A gap of at least
\[
3\sqrt2-\pi\sqrt{\frac32}=0.3949911966336938\ldots
\tag{1.2}
\]
remains throughout this entire finite-dimensional orientation class.

This is not the full conjecture: arbitrary cap-one laws need not be compactly supported or centered, the ambient dimension is arbitrary, and a general target matrix can have unequal large eigenvalues and arbitrary additional spectrum.

## 2. Ball-envelope lemma

The result follows from a useful exact three-dimensional envelope that keeps the curved level-set geometry.

**Lemma.** Let \(\rho\) be any measurable density on \(\mathbb R^3\) such that
\[
0\le \rho\le1,
\qquad
\operatorname{supp}\rho\subset B_R(0).
\]
For
\[
S=Y_1^2+Y_2^2-Y_3^2,
\]
the pushforward has an a.e. density satisfying, for \(|s|\le R^2\),
\[
p_S(s)\le
\begin{cases}
2\pi\sqrt{\dfrac{R^2-s}{2}}, & 0\le s\le R^2,\\[1.2ex]
2\pi\left(\sqrt{\dfrac{R^2-s}{2}}-\sqrt{-s}\right), & -R^2\le s\le0,
\end{cases}
\tag{2.1}
\]
and \(p_S(s)=0\) outside \([-R^2,R^2]\). Consequently
\[
\boxed{\|p_S\|_\infty\le \sqrt2\,\pi R.}
\tag{2.2}
\]

This lemma does **not** assert a bound from \(\|\rho\|_\infty\) alone.  The explicit support-radius hypothesis is essential and is exactly what avoids the live correction refuting arbitrary-joint coarea bounds.

### Proof for \(s>0\)

Write cylindrical spectral coordinates
\[
y_1=r\cos\theta,\qquad y_2=r\sin\theta,\qquad y_3=w.
\]
Resolving the delta constraint \(r^2-w^2=s\) in \(w\) gives, for a.e. \(s>0\),
\[
p_S(s)
=
\int_0^{2\pi}\int_{\sqrt s}^{\infty}
\frac{r}{2\sqrt{r^2-s}}
\Bigl[
\rho(r\cos\theta,r\sin\theta,+\sqrt{r^2-s})
+
\rho(r\cos\theta,r\sin\theta,-\sqrt{r^2-s})
\Bigr]dr\,d\theta.
\tag{2.3}
\]
If either summand is nonzero, the ball support implies
\[
r^2+(r^2-s)\le R^2,
\]
hence
\[
r^2\le \frac{R^2+s}{2}.
\tag{2.4}
\]
Since each density value is at most one, the bracket in (2.3) is at most two. Therefore
\[
\begin{aligned}
p_S(s)
&\le 2\pi
\int_{\sqrt s}^{\sqrt{(R^2+s)/2}}
\frac{r}{\sqrt{r^2-s}}\,dr\\
&=2\pi\sqrt{\frac{R^2-s}{2}},
\end{aligned}
\tag{2.5}
\]
which is the first branch of (2.1).

### Proof for \(s<0\)

Put \(a=-s>0\).  The roots are now
\[
w=\pm\sqrt{r^2+a}.
\]
The same coarea resolution gives
\[
p_S(-a)
=
\int_0^{2\pi}\int_0^{\infty}
\frac{r}{2\sqrt{r^2+a}}
\left[\rho(\cdots,+\sqrt{r^2+a})+\rho(\cdots,-\sqrt{r^2+a})\right]
 dr\,d\theta.
\tag{2.6}
\]
Whenever either term is nonzero,
\[
r^2+(r^2+a)\le R^2,
\]
so
\[
r^2\le\frac{R^2-a}{2}.
\tag{2.7}
\]
Thus
\[
\begin{aligned}
p_S(-a)
&\le 2\pi\int_0^{\sqrt{(R^2-a)/2}}
\frac{r}{\sqrt{r^2+a}}\,dr\\
&=2\pi\left(
\sqrt{\frac{R^2+a}{2}}-\sqrt a
\right),
\end{aligned}
\tag{2.8}
\]
which is the second branch in (2.1).

The positive branch is decreasing in \(s\).  The negative branch is also decreasing as a function of \(a=-s\), because
\[
\frac{d}{da}\left(
\sqrt{\frac{R^2+a}{2}}-\sqrt a
\right)
=
\frac1{4\sqrt{(R^2+a)/2}}-\frac1{2\sqrt a}<0.
\tag{2.9}
\]
Hence the common limiting value at the cone tip controls the essential supremum:
\[
\|p_S\|_\infty\le2\pi\sqrt{\frac{R^2}{2}}=\sqrt2\pi R.
\]
This proves the lemma.

The argument is a direct coarea/small-ball calculation; it uses neither a pointwise oscillatory-decay estimate nor independence after spectral rotation.

## 3. Apply the lemma to every rotated centered cube

For \(A=OJO^T\), set \(Y=O^TX\).  The coordinates of \(Y\) are generally dependent; we do not claim otherwise.  Their joint density is exactly the indicator of the rotated cube
\[
O^T[-1/2,1/2]^3.
\]
Because orthogonal maps preserve Euclidean norm,
\[
O^T[-1/2,1/2]^3
\subset B_{\sqrt3/2}(0).
\tag{3.1}
\]
Moreover
\[
Q=Y^TJY=Y_1^2+Y_2^2-Y_3^2.
\]
Apply the ball-envelope lemma with
\[
R=\frac{\sqrt3}{2}.
\]
This gives
\[
\|p_Q\|_\infty
\le \sqrt2\pi\frac{\sqrt3}{2}
=\pi\sqrt{\frac32}.
\tag{3.2}
\]
The strict comparison with the known obstruction is analytic:
\[
\pi\sqrt{\frac32}<3\sqrt2
\iff \pi<2\sqrt3.
\tag{3.3}
\]
For example \(\pi<22/7<2\sqrt3\), since \(484<588\).

Thus the bound is orientation-uniform over the full Householder family
\[
A_u=I-2uu^T,\qquad u\in S^2,
\tag{3.4}
\]
including choices with every entry nonzero and hence genuinely shared-coordinate.

## 4. Equation-level application of the designated partner result

The designated partner `account04/B17` completed the exact dense Householder witness
\[
u=e=(1,1,1)/\sqrt3,
\qquad
A_e=I-2ee^T
=\frac13
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix},
\tag{4.1}
\]
and proved the exact cone-tip value
\[
p_{Q_e}(0)
=6\sqrt3\,\operatorname{artanh}
\left(\frac{\sqrt2-1}{\sqrt3}\right)
=2.5343552034856036\ldots .
\tag{4.2}
\]
Partner source:
`yspennstate/math-open-problems`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260923T081528Z-account04-B17-QFORM-r4/REPORT.md`.

Applying (3.2) to that **same exact matrix and same exact product law** pays the partner's previously open off-tip/two-sheet question in one inequality:
\[
\boxed{
\sup_{s\in\mathbb R}p_{Q_e}(s)
\le \pi\sqrt{\frac32}
<3\sqrt2.
}
\tag{4.3}
\]
So even if the global maximum of the partner witness occurs away from zero, it cannot approach the current universal obstruction.  Numerically,
\[
\pi\sqrt{\frac32}=3.8476494904855918\ldots,
\qquad
3\sqrt2=4.2426406871192857\ldots .
\]
The partner's exact tip lies a further
\[
\pi\sqrt{\frac32}-p_{Q_e}(0)
=1.3132942869999882\ldots
\]
below this global envelope.

This is an actual application of a completed `account04/B17` result, not a parallel subclass computation: their exact matrix (4.1) and source-valid cube law are inserted into the new level-uniform inequality (3.2).

## 5. Sharp-constant consequence and the diffuse partner lower bound

The earlier completed `account04/B17` diffuse-bank construction gives, for exact source-valid finite-dimensional product inputs and exact nonzero spectrum \(\{1,1,-1\}\),
\[
p_{Q_m}(0)
=3\sqrt2\left(1-\frac{5295}{21952m}+O(m^{-2})\right).
\tag{5.1}
\]
Its pinned source is
`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`.
Therefore every valid universal constant obeys
\[
\boxed{C_*\ge3\sqrt2.}
\tag{5.2}
\]
Combining (1.1) and (5.2) yields a structural separation:
\[
\boxed{
\sup_{O\in O(3)}
\left\|p_{X^TOJO^TX}\right\|_\infty
\le \pi\sqrt{\frac32}
<3\sqrt2
\le C_*.
}
\tag{5.3}
\]
Thus the \(3\sqrt2\) obstruction is genuinely a diffuse/growing-dimensional effect within the centered-unit-interval equal-magnitude signature architecture; no fixed three-variable rotation can realize it.

This does **not** prove that growing dimension is necessary for arbitrary cap-one laws or arbitrary matrices.  It is a sharp-witness constraint on the exact centered-cube/equal-magnitude family only.

## 6. Continuity status

The lemma proves existence of an essentially bounded density and the displayed a.e. bounds.  This run does **not** prove a continuous representative for every rotated-cube orientation.  The partner's diffuse family has continuity by its weighted local Edgeworth/coarea proof, but the owner's full-target continuity conclusion remains open.

## 7. Correction discipline and next mechanism


The finite all-heavy three-dimensional centered-cube orientation frontier is therefore closed below \(3\sqrt2\).  A stronger witness must leave at least one of these constraints: use genuinely non-Gaussian multiscale/fragmented support, nontrivial mesoscopic or diffuse banks, translations/affine structure, growing dimension, unequal spectral scales, or additional spectrum.  The next B17 mechanism should test a multiscale fragmented three-bank construction while retaining exact product provenance, because both the pure finite 3D cube and the Gaussian endpoint are now separated from any value above \(3\sqrt2\).
