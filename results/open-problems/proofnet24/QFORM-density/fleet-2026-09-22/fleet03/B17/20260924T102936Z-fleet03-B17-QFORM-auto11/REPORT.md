SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-24T10:29:36Z.

attacking: one-heavy-row Gaussian-sea cone-tip rigidity and an exact fully dense cap-one stress family.

# QFORM-ONE-HEAVY-GAUSSIAN-SEA-CONE-TIP-RIGIDITY-v1

Run: `20260924T102936Z-fleet03-B17-QFORM-auto11`  
Classification: **PROVED SUPPORTING LEMMA / EXACT ROTATED STRESS FAMILY / FULL TARGET OPEN**  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Full conjecture: **OPEN / NOT PROVED / NOT DISPROVED**  
Full-target continuity: **OPEN**

## 1. Result in one paragraph

Let `s=1/12`. Let `X` be any real random variable with probability density `f_X<=1`, let `G1,G2,G3` be independent `N(0,s)`, and for `0<=ell<=1` put

\[
H_\ell=\sqrt\ell\,X+\sqrt{1-\ell}\,G_1,
\qquad Y_\ell=(H_\ell,G_2,G_3).
\]

For every real symmetric orthogonal `3x3` matrix `B` with spectrum `{1,1,-1}`, the cone-tip density of

\[
Q_\ell=Y_\ell^T B Y_\ell
\]

satisfies

\[
\boxed{p_{Q_\ell}(0)\le 3\sqrt2.}
\]

If `ell>0`, the inequality is strict. Thus a single arbitrary cap-one macroscopic row inserted into an otherwise minimum-variance Gaussian sea cannot raise the zero-cone peak above the known Gaussian obstruction `3sqrt(2)`, in any spectral orientation. This is a comparator theorem, not a Gaussian assumption on the owner's conjecture.

I then realize an exact target-admissible, entrywise-dense finite family with all original inputs `Uniform[-1/2,1/2]` and exact nonzero spectrum `{1,1,-1}`. For the explicit fully coupled orientation

\[
B=I-2nn^T,
\qquad n=(1,2,3)/\sqrt{14},
\]

the cone-tip densities converge to the one-heavy Gaussian-sea limit and obey the explicit rigorous bound

\[
\boxed{
\limsup_{m\to\infty}p_{Q_m}(0)
\le C_{\rm heavy}
:=3\sqrt2\,\kappa_*
=3.788500928605675\ldots,
}
\]

where

\[
\kappa_*=1-\mu_*\left(1-\sqrt{\frac{2\pi}{9}}\right),
\qquad
\mu_*=1-\frac1\pi\arccos\!\left(\frac{\sqrt7-1}{\sqrt{13}}\right)
=0.650879015434499\ldots .
\]

This is a cone-tip statement only. A larger global peak for this family, if present, must occur off the zero cone, in particular on the negative two-sheet side.

## 2. A sharp one-dimensional Laplace inequality forced by the density cap

The key estimate is independent of the quadratic-form geometry.

### Lemma 2.1 (cap-one Gaussian Laplace domination)

If `X` has a probability density `f<=1`, then for every `b>=0`,

\[
\boxed{
\mathbb E e^{-bX^2}
\le
\int_{-1/2}^{1/2}e^{-bx^2}\,dx
\le
\left(1+\frac b6\right)^{-1/2}.
}
\tag{2.1}
\]

The first inequality is the exact one-dimensional bathtub principle: the even decreasing weight `e^{-b x^2}` is maximized under `0<=f<=1`, `int f=1`, by the centered interval indicator of length one.

For the second inequality put `r=b/4` and

\[
A(r)=\int_0^1 e^{-ru^2}\,du,
\qquad
g(r)=\left(1+\frac{2r}{3}\right)^{-1/2}.
\]

Then the desired inequality is `A(r)<=g(r)`. Integration by parts gives

\[
A(r)+2rA'(r)=e^{-r}.
\tag{2.2}
\]

Direct differentiation gives

\[
g(r)+2rg'(r)=g(r)^3.
\tag{2.3}
\]

Since `log(1+x)<=x`,

\[
e^{-r}
\le
\left(1+\frac{2r}{3}\right)^{-3/2}
=g(r)^3.
\tag{2.4}
\]

Hence `h=A-g` satisfies

\[
h+2rh'\le0.
\]

For `r>0`,

\[
\frac{d}{dr}(\sqrt r\,h(r))
=\frac{h+2rh'}{2\sqrt r}\le0.
\]

Because `sqrt(r) h(r)->0` as `r downarrow0`, one gets `h(r)<=0`. The logarithmic inequality is strict for `r>0`, so the second inequality in (2.1) is strict for `b>0`.

This proof uses only the density cap and probability normalization. It allows disconnected, fragmented, asymmetric and unbounded-support laws.

## 3. Gaussian smoothing preserves the same Laplace ceiling

Let `s=1/12` and

\[
H_\ell=\sqrt\ell X+\sqrt{1-\ell}G,
\qquad G\sim N(0,s),
\]

independently. For every `a>=0`, Gaussian completion of the square gives

\[
\mathbb E e^{-aH_\ell^2}
=
D^{-1/2}
\mathbb E\exp\!\left(-\frac{a\ell}{D}X^2\right),
\qquad
D=1+2as(1-\ell).
\tag{3.1}
\]

Apply Lemma 2.1 with `b=a ell/D`. Since `2s=1/6`,

\[
\begin{aligned}
\mathbb E e^{-aH_\ell^2}
&\le
D^{-1/2}\left(1+\frac{a\ell}{6D}\right)^{-1/2}\\
&=
\left(1+\frac a6\right)^{-1/2}
=
(1+2as)^{-1/2}.
\end{aligned}
\tag{3.2}
\]

Thus the square-Laplace transform of the heavy coordinate, after any amount of minimum-variance Gaussian smoothing, is no larger than that of `N(0,1/12)`. For `ell>0` and `a>0`, the inequality is strict.

## 4. Cone-ray formula and orientation-free tip rigidity

Let `B=B^T`, `B^2=I`, `spec(B)={1,1,-1}` and

\[
q(y)=y^TBy.
\]

Let

\[
\mathcal C_B=\{\omega\in S^2:\omega^TB\omega=0\}.
\]

Because `B` is orthogonal, on the spherical zero set

\[
|\nabla_{S^2}(\omega^TB\omega)|=2|B\omega|=2.
\]

Therefore the density at the homogeneous critical level has the exact polar/coarea representation

\[
\boxed{
p_Q(0)
=\frac12\int_{\mathcal C_B}\int_0^\infty \rho(r\omega)\,dr\,d\ell(\omega),
}
\tag{4.1}
\]

whenever the displayed integral is finite. Here `rho` is the joint density of `Y_ell` and `d ell` is arc length on the cone section.

In the physical basis used above,

\[
\rho(y_1,y_2,y_3)=h_\ell(y_1)\,\gamma_s(y_2)\,\gamma_s(y_3),
\]

where `h_ell` is the density of `H_ell`. Pair each cone ray `omega` with its antipode `-omega`. Put

\[
t=|\omega_1|,
\qquad
a=\frac{1-t^2}{2st^2}
\quad(t>0).
\]

The two Gaussian transverse coordinates give

\[
\begin{aligned}
I(\omega)+I(-\omega)
&:=\int_0^\infty[\rho(r\omega)+\rho(-r\omega)]\,dr\\
&=\frac{1}{2\pi s\,t}\,\mathbb E e^{-aH_\ell^2}.
\end{aligned}
\tag{4.2}
\]

For an isotropic `N(0,sI_3)` density, every single ray integral equals

\[
I_G=\frac1{4\pi s}.
\tag{4.3}
\]

Hence the paired-ray ratio is

\[
\frac{I(\omega)+I(-\omega)}{2I_G}
=
\frac{\mathbb E e^{-aH_\ell^2}}{t}.
\tag{4.4}
\]

But

\[
1+2as=t^{-2}.
\]

By (3.2), the numerator in (4.4) is at most `t`. Therefore every antipodal ray pair contributes no more than the isotropic Gaussian pair. The `t=0` case follows by continuity/monotone limiting of the paired expression. Integrating over the cone proves

\[
p_{Q_\ell}(0)\le p_{G^TBG}(0).
\tag{4.5}
\]

The cone section of a `(2,1)` involution consists of two circles of radius `1/sqrt(2)`, hence total arc length `2sqrt(2) pi`. Combining this with (4.1) and (4.3),

\[
p_{G^TBG}(0)
=\frac12(2\sqrt2\pi)\frac1{4\pi s}
=\frac1{2\sqrt2 s}
=3\sqrt2.
\tag{4.6}
\]

This proves the orientation-free theorem.

If `ell>0`, (3.2) is strict for every ray with `0<t<1`. A cone circle has positive arc-length measure of such rays, so

\[
\boxed{p_{Q_\ell}(0)<3\sqrt2\qquad(\ell>0).}
\tag{4.7}
\]

No post-rotation independence is used: independence exists only in the displayed original heavy coordinate and the two Gaussian sea coordinates before applying the fixed quadratic matrix `B`.

## 5. Explicit fully coupled orientation and a quantitative tip gap

Take

\[
n=\frac{(1,2,3)}{\sqrt{14}},
\qquad
B=I-2nn^T
=\frac17
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\tag{5.1}
\]

Every entry is nonzero, `B^2=I`, and `spec(B)={1,1,-1}`.

Now take the fully heavy limit `ell=1`; the first coordinate is an arbitrary cap-one `X`, while the other two coordinates are independent `N(0,1/12)`. The paired-ray estimate can be made quantitatively sharper without using Lemma 2.1's Gaussian comparison. Since `f_X<=1`,

\[
\mathbb E e^{-aX^2}
\le
\min\left\{1,\int_{\mathbb R}e^{-ax^2}dx\right\}
=
\min\left\{1,\sqrt{\frac\pi a}\right\}.
\]

Thus the paired-ray ratio in (4.4) obeys

\[
R(t)
\le
\min\left\{1,
\sqrt{\frac{\pi}{6(1-t^2)}}
\right\}.
\tag{5.2}
\]

In particular, whenever `t^2<=1/4`,

\[
R(t)\le r_*:=\sqrt{\frac{2\pi}{9}}
=0.8355427582103335\ldots .
\tag{5.3}
\]

Parameterize one cone circle by

\[
\omega(\theta)
=\frac n{\sqrt2}+\frac{u\cos\theta+v\sin\theta}{\sqrt2},
\]

where `u,v` are an orthonormal basis of `n^perp` chosen with `e_1 dot v=0`. Then

\[
|\omega_1(\theta)|
=
\frac{|1+\sqrt{13}\cos\theta|}{\sqrt{28}}.
\tag{5.4}
\]

The condition `t^2<=1/4` becomes

\[
|1+\sqrt{13}\cos\theta|\le\sqrt7.
\]

The lower inequality is automatic because `(-sqrt(7)-1)/sqrt(13)<-1`. Therefore the fraction of the circle on which (5.3) applies is exactly

\[
\boxed{
\mu_*
=1-\frac1\pi\arccos\!\left(\frac{\sqrt7-1}{\sqrt{13}}\right)
=0.6508790154344992\ldots .
}
\tag{5.5}
\]

On the remaining fraction use only `R(t)<=1`. Since the other cone circle is the antipodal copy, (4.1) gives

\[
\frac{p_Q(0)}{3\sqrt2}
\le
\mu_*r_*+(1-\mu_*)
=:\kappa_*.
\tag{5.6}
\]

Numerically,

\[
\kappa_*=0.8929582323828685\ldots,
\]

and hence

\[
\boxed{
p_Q(0)\le C_{\rm heavy}
=3\sqrt2\,\kappa_*
=3.788500928605675\ldots .}
\tag{5.7}
\]

This estimate is valid for every cap-one heavy law `X` in the Gaussian-sea comparator for this orientation. No symmetry, moments, compact support or connected support of `X` are needed.

## 6. Exact finite cap-one rotated stress family

The preceding Gaussian sea can be reached by an exact admissible family without rotating the independent inputs.

For each integer `m>=2`, let `R_m` be the `(2m+1) x 3` matrix with rows

- one heavy row `e_1`;
- `m` copies of `e_2/sqrt(m)`;
- `m` copies of `e_3/sqrt(m)`.

Then

\[
R_m^TR_m=I_3.
\]

Define

\[
A_m=R_mBR_m^T.
\tag{6.1}
\]

Therefore the nonzero spectrum is exactly

\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-1\}.}
\tag{6.2}
\]

Because every entry of `B` is nonzero, every entry of the physical matrix `A_m` is nonzero as well. Explicitly its block coefficients are proportional to

\[
\frac67,
\quad -\frac{2}{7\sqrt m},
\quad -\frac{3}{7\sqrt m},
\quad \frac{3}{7m},
\quad -\frac{6}{7m},
\quad -\frac{2}{7m},
\]

so this is genuinely fully coupled in the independent physical coordinates.

Let all `2m+1` physical coordinates be independent `Uniform[-1/2,1/2]`. Write

\[
U_0\sim\operatorname{Unif}[-1/2,1/2],
\qquad
S_{j,m}=m^{-1/2}\sum_{k=1}^mU_{j,k},\quad j=2,3.
\]

Then

\[
X^TA_mX
\stackrel d=
(U_0,S_{2,m},S_{3,m})^TB(U_0,S_{2,m},S_{3,m}).
\tag{6.3}
\]

Let `g_m` be the density of `S_{j,m}`. Its characteristic function is

\[
\widehat g_m(t)=\operatorname{sinc}\!\left(\frac{t}{2\sqrt m}\right)^m.
\]

The standard three-region estimate (`|t|<=sqrt(m)`, `sqrt(m)<=|t|<=4sqrt(m)`, and the tail) gives

\[
\|g_m-\gamma_{1/12}\|_\infty\to0,
\qquad
\sup_m\|g_m\|_\infty<\infty,
\tag{6.4}
\]

and `E S_{j,m}^2=1/12` exactly. This is the same elementary Fourier local-CLT mechanism already used in the source-pinned fleet03/B17 symmetric-bank report; no law-uniform pointwise quadratic-phase estimate is involved.

For the zero cone, coarea gives

\[
p_m(0)
=\frac12\int_{\mathcal C_B}\int_0^\infty
\mathbf1_{\{|r\omega_1|\le1/2\}}
\,g_m(r\omega_2)g_m(r\omega_3)\,dr\,d\ell(\omega).
\tag{6.5}
\]

On every bounded radial range, (6.4) gives uniform convergence to the Gaussian-sea integrand. The radial tail is uniform: if `|omega_1|>=1/(2M)`, the heavy interval kills the integrand for `r>M`; otherwise `omega_2^2+omega_3^2>1-1/(4M^2)`, so for `M>=1` one of `|omega_2|,|omega_3|` is at least `1/2`. With the other bank density uniformly bounded and `E S_{j,m}^2=1/12`, Chebyshev integration gives an `O(M^{-2})` ray tail uniformly in `m` and `omega`. Hence dominated cone convergence yields

\[
\boxed{p_m(0)\longrightarrow p_\infty(0).}
\tag{6.6}
\]

Combining (5.7) and (6.6),

\[
\boxed{
\limsup_{m\to\infty}p_m(0)
\le3.788500928605675\ldots .
}
\tag{6.7}
\]

Every finite member of (6.3) satisfies the owner's exact hypotheses. The statement is only about the cone-tip value; it does not assert that zero is the global mode.

## 7. Completed fleet04/B17 partner result applied to an actual inequality

The designated partner `fleet04/B17` proved `QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1` at

`yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260924T011922Z-fleet04-B17-QFORM-r6/REPORT.md`.

For `theta=0.01`, that exact cap-one, entrywise-dense target family satisfies

\[
\liminf_m\|p_{Q_m}^{\rm partner}\|_\infty
\ge
3\sqrt2 e^{-0.03}
=4.117251705266084\ldots .
\tag{7.1}
\]

Combining (7.1) with the new exact-family cone-tip bound (6.7) gives the concrete inequality

\[
\boxed{
\liminf_m\|p_{Q_m}^{\rm partner}\|_\infty
-
\limsup_m p_{Q_m}^{\rm heavy}(0)
\ge
0.3287507766604085\ldots .
}
\tag{7.2}
\]

Thus the completed partner's fragmented mechanism beats the zero-cone tip of this fully coupled one-heavy-row stress family by a certified positive amount. Consequently, if the one-heavy family is ever to compete with that witness level, it must generate a genuinely off-tip peak. This makes the negative two-sheet side, rather than the cone vertex, the next sharp-witness location to test for this architecture.

## 8. What this rules out and what it does not

This run rules out one substantial witness mechanism at the cone tip:

- one arbitrary cap-one macroscopic physical coordinate;
- any leverage `0<ell<=1` into a minimum-variance Gaussian sea;
- any spectral orientation of a rank-three `(1,1,-1)` involution;
- in particular an exact fully dense physical family with one leverage-one coordinate and two diffuse uniform banks.

The cone-tip cannot exceed `3sqrt(2)`, and in the explicit fully dense leverage-one family it is asymptotically at most `3.7885009286...`.

This does **not** prove the universal conjecture. In particular it does not control:

1. a negative two-sheet off-tip peak in the same family;
2. two or more non-collinear macroscopic rows;
3. a surviving non-Gaussian multivariate macroscopic component;
4. additional active spectrum beyond the rank-three core;
5. the full continuity conclusion under arbitrary rough cap-one laws.

The current universal lower obstruction therefore remains

\[
\boxed{C_*\ge3\sqrt2.}
\]

No improved universal lower bound is claimed in this run.

## 9. Correction compliance and provenance

The proof never assumes independence after a general spectral rotation. It does not use the refuted law-uniform pointwise van-der-Corput estimate, arbitrary-joint coarea bound, conditional projection-density moment, naive fiber-supremum estimate, fixed fragment count, or Monte Carlo extremality. The only coarea calculation is for the explicit product/Gaussian-sea density and the exact homogeneous rank-three cone, where the ray formula is derived directly.

Dependencies actually used:

- fresh owner control and QFORM-only assignment from `yspennstate/math-research-brain` main;
- live QFORM correction inbox refreshed immediately before publication;
- fleet03/B17 local-CLT bank argument: `yspennstate/math-open-problems@7a64594fceb49b99698431a4d57b6658b49ebc28`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260924T053018Z-fleet03-B17-QFORM-auto11/REPORT.md`;
- completed designated partner theorem: `yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`, exact path given in Section 7.

Repository transport is not native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN` unless an authenticated native receiver-use event is separately observed.
