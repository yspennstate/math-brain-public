SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-23T15:04:36Z.
attacking: the unpaid N3 one-heavy/shared-diffuse boundary — exact cone-tip optimizer kernel, a strict analytic endpoint ceiling, and finite cap-one partner transfer.

# QFORM B17 — one-heavy N3 kernel and minority-axis ceiling

Run: `20260923T150436Z-fleet03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING ANALYTIC STRESS-FAMILY THEOREM; FULL QFORM OPEN / NOT PROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Compact end-to-end conditional argument and the missing implication attacked

The current no-pivot branch N3 permits matrices with three actual eigenvalues of magnitude at least one while every physical diagonal and every physical 2x2 principal determinant is small. The first question for a sharp-constant worker is whether a single macroscopic physical coordinate, coupled to a highly diffuse two-dimensional complement, can exploit this no-pivot geometry to create a density peak above the known lower obstruction `3 sqrt(2)`.

This report gives an exact analytic answer at the cone tip for a one-parameter family that lies in N3 for arbitrarily small pivot threshold. The family is genuinely coupled for every `0<a<1`. Its Gaussianized complement has an exact cap-one heavy-law optimizer, so arbitrary fragmented/disconnected support in the heavy coordinate is paid rather than assumed away. At the minority-axis endpoint `a=1` the exact optimum is proved strictly below `3 sqrt(2)`, and the completed designated-partner Edgeworth theorem is applied to an actual finite cap-one sequence, showing approach to that endpoint from below.

This does **not** prove the full conjecture: the global off-tip mode, multiple macroscopic shared rows, non-Gaussian surviving complement components and arbitrary added spectrum remain unpaid.

## 2. Exact coupled one-heavy frame

Let

`J = diag(1,1,-1)`, `0<a<=1`, and `d=sqrt(1-a^2)`. Define the orthonormal vectors

\[
r=\left(\sqrt{\frac{1-a}{2}},0,\sqrt{\frac{1+a}{2}}\right),\quad
b=\left(\sqrt{\frac{1+a}{2}},0,-\sqrt{\frac{1-a}{2}}\right),\quad
c=(0,1,0).
\]

A direct calculation gives

\[
r^T J r=-a,\qquad b^T J b=a,\qquad r^T J b=d,\qquad c^T Jc=1,
\]
with the other mixed products zero. Hence in the physical frame `(r,b,c)` the signature matrix is exactly

\[
\begin{pmatrix}
-a&d&0\\
d&a&0\\
0&0&1
\end{pmatrix}. \tag{2.1}
\]

Let `X` have an arbitrary probability density `0<=f<=1`, and let `B,C` be independent `N(0,v)`, `v=1/12`, independent of `X`. The limiting one-heavy quadratic form is

\[
Q_a=-aX^2+2dXB+aB^2+C^2. \tag{2.2}
\]

For `0<a<1`, (2.2) has a genuine heavy/diffuse cross term. No spectral rotation is used to assert independence.

## 3. Exact cone-tip kernel and cap-one optimizer

Complete the square in `B`:

\[
Q_a=a\left(B+\frac{d}{a}X\right)^2+C^2-\frac{X^2}{a}. \tag{3.1}
\]

Condition on `X=x`. Put

\[
u=\sqrt a\left(B+\frac{d}{a}x\right),\qquad w=C.
\]

Then `Q_a=0` is the circle `u^2+w^2=x^2/a`. The joint density of `(u,w)` is

\[
\frac{1}{2\pi v\sqrt a}
\exp\left[-\frac{1}{2v}\left(\left(\frac{u}{\sqrt a}-\frac{dx}{a}\right)^2+w^2\right)\right].
\]

Using polar coarea on the circle gives the exact conditional density at zero

\[
K_a(x)=\frac{1}{4\pi v\sqrt a}\int_0^{2\pi}
\exp\left[-\frac{x^2}{2v}F_a(\theta)\right]d\theta, \tag{3.2}
\]
where

\[
F_a(\theta)=\frac{(\cos\theta-d)^2}{a^2}+\frac{\sin^2\theta}{a}. \tag{3.3}
\]

For every `a>0`, `F_a(theta)>0`: simultaneous vanishing would force `sin(theta)=0` and `cos(theta)=d`, impossible because `d<1` for `a>0`. Thus `K_a` is even and, for `x>0`,

\[
K_a'(x)=-\frac{x}{4\pi v^2\sqrt a}\int_0^{2\pi}
F_a(\theta)e^{-x^2F_a(\theta)/(2v)}d\theta<0. \tag{3.4}
\]

Therefore the reward `K_a(x)` is strictly decreasing in `|x|`. The bathtub principle under `0<=f<=1`, `int f=1` yields the exact optimizer

\[
\boxed{
\sup_{0\le f\le1,\ \int f=1}p_{Q_a}(0)
=C(a):=\int_{-1/2}^{1/2}K_a(x)dx,
} \tag{3.5}
\]

with the centered unit interval as the unique optimizer up to null sets. This pays arbitrary fragmented, disconnected and remotely translated heavy-coordinate supports rather than assuming an interval extremizer.

Integrating (3.2) in `x` gives the exact one-dimensional angular representation

\[
\boxed{
C(a)=\sqrt{\frac{3}{2\pi a}}
\int_0^{2\pi}
\frac{\operatorname{erf}(\sqrt{3F_a(\theta)/2})}{\sqrt{F_a(\theta)}}\,d\theta.
} \tag{3.6}
\]

Equation (3.6) is an analytic stress certificate, not a histogram.

## 4. Exact finite-dimensional provenance and direct N3 membership

For each integer `m>=1`, form a `(2m+1) x 3` matrix `R_m` whose rows are

- one copy of `r`;
- `m` copies of `b/sqrt(m)`;
- `m` copies of `c/sqrt(m)`.

Then

\[
R_m^T R_m=rr^T+bb^T+cc^T=I_3. \tag{4.1}
\]

Set

\[
A_{a,m}=R_m J R_m^T. \tag{4.2}
\]

Since `R_m` is an isometric embedding, the nonzero eigenvalues of `A_{a,m}` are exactly

\[
\boxed{\{1,1,-1\}}. \tag{4.3}
\]

Take all physical inputs independent with density one on `[-1/2,1/2]`; distinguish the first input as the heavy coordinate `X`, and write

\[
B_m=m^{-1/2}\sum_{k=1}^m U_k,\qquad
C_m=m^{-1/2}\sum_{k=1}^m V_k.
\]

Then the exact finite form is

\[
Q_{a,m}=-aX^2+2dXB_m+aB_m^2+C_m^2. \tag{4.4}
\]

For `0<a<1` this is genuinely nonseparable in the original independent coordinates.

The physical principal-pair determinants expose why this is a genuine no-pivot stress family. For the heavy coordinate `h` and any `b`-bank coordinate,

\[
\det A_{\{h,b_k\}}
=(-a)(a/m)-d^2/m=-1/m. \tag{4.5}
\]

For a heavy/`c` pair the determinant is `-a/m`; for a `b`/`c` pair it is `a/m^2`; same-bank pairs have determinant zero. The diagonal entries are `-a`, `a/m`, and `1/m`. Hence for every fixed `tau` with

\[
0<a<\tau\le1,\qquad m>1/\tau, \tag{4.6}
\]

all physical diagonal magnitudes and all physical pair-determinant magnitudes are strictly below `tau`, while (4.3) still supplies three actual unit-magnitude eigenvalues. Thus (4.2) lies directly inside the unpaid N3 inequalities described in the current no-pivot synthesis.

By the ordinary local central limit theorem with the weighted form supplied by the designated partner, `(B_m,C_m)` converges locally to the Gaussian pair `(B,C)`. For fixed `a>0`, (3.2) has an integrable Gaussian majorant, so the cone-tip densities converge to the kernel value. In particular for centered-unit-interval `X`,

\[
p_{Q_{a,m}}(0)\longrightarrow C(a). \tag{4.7}
\]

No claim is made that (4.7) controls the global off-tip maximum.

## 5. Strict analytic endpoint ceiling

At `a=1`, `d=0`, so

\[
Q_1=-X^2+B^2+C^2. \tag{5.1}
\]

Since `B^2+C^2` for independent `N(0,1/12)` variables is exponential with density

\[
h(s)=6e^{-6s}\mathbf1_{s\ge0},
\]

(3.5) becomes

\[
\boxed{
C_-:=C(1)=6\int_{-1/2}^{1/2}e^{-6x^2}dx
=\sqrt{6\pi}\,\operatorname{erf}(\sqrt{3/2}).
} \tag{5.2}
\]

This admits a fully elementary strict comparison with `3 sqrt(2)`. For `z>0`, integration by parts gives the Mills lower bound

\[
\int_z^\infty e^{-t^2}dt
=\frac{e^{-z^2}}{2z}-\frac12\int_z^\infty t^{-2}e^{-t^2}dt
\ge \frac{z e^{-z^2}}{2z^2+1}. \tag{5.3}
\]

At `z=sqrt(3/2)`, (5.3) implies

\[
C_-<\sqrt{6\pi}-\frac32e^{-3/2}. \tag{5.4}
\]

Now `pi<22/7` gives

\[
\sqrt{6\pi}<\sqrt{132/7}<35/8, \tag{5.5}
\]

because `132*64<1225*7`. Also

\[
e^{3/2}
<\sum_{k=0}^{6}\frac{(3/2)^k}{k!}
+\frac{(3/2)^7}{7!}\frac{1}{1-3/16}
=\frac{2088119}{465920}<\frac92, \tag{5.6}
\]

so `e^{-3/2}>2/9`. Combining (5.4)-(5.6),

\[
\boxed{
C_-<\frac{35}{8}-\frac13=\frac{97}{24}<3\sqrt2.
} \tag{5.7}
\]

The last inequality follows by squaring: `9409/576<18`.

Numerically, only as a diagnostic,

\[
C_-=3.9801056750420088\ldots,
\qquad 3\sqrt2=4.2426406871192851\ldots . \tag{5.8}
\]

Thus even allowing an arbitrary cap-one heavy law, the one-heavy minority-axis plus minimum-variance diffuse same-sign Gaussian core is strictly separated from the current universal lower obstruction at the cone tip.

## 6. Actual application of the completed fleet04/B17 result

The designated partner `fleet04/B17` proved, at

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`

path

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260922T211900Z-fleet04-B17-QFORM-r3/REPORT.md`,

the weighted local Edgeworth expansion for a normalized centered-uniform bank,

\[
g_m(y)=\gamma_\sigma(y)
\left[1-\frac{1}{20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8},\qquad \sigma^2=1/12, \tag{6.1}
\]

and independently constructed an exact rotated cap-one family proving

\[
C_*\ge3\sqrt2 \tag{6.2}
\]

for every possible universal constant `C_*`.

Apply (6.1) to the two actual diffuse banks in the finite endpoint family

\[
Q_{1,m}=-X^2+B_m^2+C_m^2,\qquad X\sim\mathrm{Unif}[-1/2,1/2]. \tag{6.3}
\]

If `S_m=B_m^2+C_m^2`, polar coarea gives

\[
p_{S_m}(s)=\frac12\int_0^{2\pi}
 g_m(\sqrt{s}\cos\theta)g_m(\sqrt{s}\sin\theta)d\theta. \tag{6.4}
\]

Writing `rho^2=s/sigma^2=12s`, the circle average in the first Edgeworth term is exactly

\[
\left\langle H_4(\rho\cos\theta)+H_4(\rho\sin\theta)\right\rangle
=\frac34\rho^4-6\rho^2+6
=108s^2-72s+6. \tag{6.5}
\]

Therefore

\[
p_{S_m}(s)=6e^{-6s}
\left[1-\frac{108s^2-72s+6}{20m}\right]+O(m^{-2}) \tag{6.6}
\]

with an integrable weighted remainder on the interval needed below. Substituting `s=x^2` and integrating over the heavy centered interval yields

\[
\boxed{
p_{Q_{1,m}}(0)
=C_- -\frac{I_-}{20m}+O(m^{-2}),
} \tag{6.7}
\]

where direct integration gives

\[
\boxed{
I_-=9e^{-3/2}+\frac94 C_->0.
} \tag{6.8}
\]

Equivalently,

\[
p_{Q_{1,m}}(0)
=C_-\left(1-\frac{\kappa_-}{m}+O(m^{-2})\right),
\quad
\kappa_-=\frac9{80}+\frac{9e^{-3/2}}{20C_-}>0. \tag{6.9}
\]

Numerically `kappa_-=0.1377276146074271...`. Thus the exact finite cap-one sequence approaches its already subcritical cone-tip ceiling **from below**. Combining (5.7) with the partner's source-valid lower witness (6.2),

\[
\boxed{
\lim_m p_{Q_{1,m}}(0)=C_-<3\sqrt2\le C_*.
} \tag{6.10}
\]

This is the required equation-level application of a completed designated-partner result.

## 7. Interior coupled diagnostics — not a proof of monotonicity

Formula (3.6) permits deterministic high-precision evaluation. The values below are diagnostics only:

| a | C(a) |
|---:|---:|
| 0.05 | 3.6304323923 |
| 0.10 | 3.6406660218 |
| 0.20 | 3.6626491333 |
| 0.40 | 3.7137717227 |
| 0.50 | 3.7438270698 |
| 0.60 | 3.7778308020 |
| 0.80 | 3.8626870103 |
| 1.00 | 3.9801056750 |

The scan is consistent with `C(a)<3sqrt(2)` throughout this one-heavy family, including the genuinely coupled N3 region, but **no monotonicity theorem or uniform-in-a strict inequality is claimed from these numbers**. A future useful B17 step would prove such a uniform analytic bound or locate a genuine counterexample if the scan changes under a richer shared-row geometry.

## 8. Scope, continuity, and remaining gap

What is proved here:

1. For every fixed `a>0`, the Gaussianized one-heavy form (2.2) has an exact cone-tip kernel (3.2), and among all heavy-coordinate probability densities bounded by one its cone-tip density is maximized exactly by the centered unit interval, formula (3.5).
2. The finite source-valid family (4.2) has exact nonzero spectrum `{1,1,-1}` and enters the physical no-pivot N3 inequalities for every `tau>a` and sufficiently large `m`.
3. At the minority-axis endpoint `a=1`, the exact optimum satisfies `C_-<97/24<3sqrt(2)` analytically.
4. The partner Edgeworth theorem gives the finite endpoint expansion (6.7)-(6.9), with strictly negative first correction.

What is **not** proved:

- the full universal upper bound;
- that the global output-density mode of (4.4) occurs at zero;
- a uniform analytic `C(a)<3sqrt(2)` theorem for all `0<a<1`;
- control of two or more macroscopic shared rows, a surviving non-Gaussian coupled component, or arbitrary added spectrum.

At the endpoint (5.1), for every cap-one heavy law the limiting density has a continuous representative by dominated convergence in

\[
p(t)=\int f(x)6e^{-6(t+x^2)}\mathbf1_{t+x^2\ge0}\,dx.
\]

The partner theorem supplies continuity for the finite diffuse-bank witness family in its stated range. **Full-target continuity remains OPEN.**

## 9. Provenance and correction discipline


The full QFORM conjecture remains **OPEN / NOT PROVED**. Repository use in this run is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
