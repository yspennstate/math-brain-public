SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T05:06:10Z.
attacking: the unpaid one-heavy/two-rank-one-bank witness class; close the finite-bank sequence by a Ball-slicing norm argument and extend it to arbitrary leverage weights.

# QFORM B17 — all finite one-heavy majority banks are strictly below `3 sqrt(2)`

Run: `20260923T050610Z-fleet01-B17-QFORM-r14`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Let `m>=1`, let `a=(a_1,...,a_m)` satisfy

\[
\sum_{j=1}^m a_j^2=1,
\]

and let `U_j,V_j` be independent `Unif[-1/2,1/2]`. Put

\[
S_a=\sum_j a_jU_j,\qquad T_a=\sum_j a_jV_j.
\]

Let `X_f` be independent of the banks and have an **arbitrary** probability density `0<=f<=1`; `f` may be translated, disconnected, unbounded, or arbitrarily fragmented. Define

\[
Q_{a,f}=X_f^2+S_a^2-T_a^2.
\tag{1.1}
\]

Then

\[
\boxed{
\sup_{0\le f\le1,\int f=1}\|p_{Q_{a,f}}\|_\infty
=p_{U^2+S_a^2-T_a^2}(0)
\le B_0<3\sqrt2,
}
\tag{1.2}
\]

where `U~Unif[-1/2,1/2]` and

\[
\boxed{
B_0=2\pi\left(1-\frac1{\sqrt3}+\frac1{3\sqrt2}\right)
=4.1365475580\ldots .
}
\tag{1.3}
\]

A purely rational comparison, not the decimal check, gives

\[
B_0<\frac{5148}{1225}<3\sqrt2.
\tag{1.4}
\]

Thus the entire arbitrary-weight one-heavy majority-sign bank architecture is uniformly separated from the known lower-obstruction scale `3sqrt(2)`.

For the equal weights `a_j=1/sqrt(m)`, this proves the precise outstanding inequality in the designated partner's exact finite-extremizer sequence **for every `m`**, not just `m=1,2` and sufficiently large `m`.

## 2. Exact target provenance

The physical matrix is

\[
A_a=\operatorname{diag}(1,aa^T,-aa^T)
\tag{2.1}
\]

on `1+2m` original independent coordinates. Since `aa^T` has spectrum `{1,0,...,0}`, every finite matrix satisfies

\[
\boxed{\operatorname{spec}_{\ne0}(A_a)=\{1,1,-1\}.}
\tag{2.2}
\]

Hence this is an exact instance of the original spectral hypothesis, not a Gaussian surrogate and not an assertion of independence after spectral rotation. For `m>1` the two rank-one bank blocks have genuine off-diagonal physical-coordinate couplings.

Moreover every physical cross cut of (2.1) has rank at most two: each of the two rank-one banks contributes at most one cross direction and the singleton contributes none. The singleton physical row has leverage one in the rank-three range. Thus the family is deliberately positioned outside the direct three-volume/diffuse-leverage exits in the current Claude Fourier package; it is a genuine low-cross-rank/high-leverage stress class.

## 3. Two sharp one-dimensional norm consequences of cube slicing

Let `h` be the density of `S_a`. Convolution of symmetric interval densities shows that `h` is even and nonincreasing on `[0,infinity)`.

Ball's cube-slicing theorem gives the standard one-dimensional marginal consequence

\[
\boxed{\|h\|_\infty\le\sqrt2.}
\tag{3.1}
\]

Indeed `S_a=<a,U>` is the projection of the unit cube in a unit direction. The same conclusion follows from the product-measure marginal theorem of Livshyts--Paouris--Pivovarov, Theorem 1.1, in dimension one.

The second use is the key new estimate. If `S_a'` is an independent copy, Plancherel/convolution gives

\[
\|h\|_2^2=p_{S_a-S_a'}(0).
\tag{3.2}
\]

But

\[
\frac{S_a-S_a'}{\sqrt2}
=\sum_j\frac{a_j}{\sqrt2}U_j-
  \sum_j\frac{a_j}{\sqrt2}U_j',
\]

whose `2m`-dimensional coefficient vector `(a,-a)/sqrt(2)` has Euclidean norm one. Cube slicing therefore bounds the density of `(S_a-S_a')/sqrt(2)` by `sqrt(2)`. Scaling back yields

\[
\boxed{\|h\|_2^2\le1.}
\tag{3.3}
\]

No moment estimate is used.

Source: K. Ball, *Cube slicing in R^n*, Proc. Amer. Math. Soc. 97 (1986), 465--473, DOI `10.1090/S0002-9939-1986-0840631-0`. A product-density formulation is G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1.

## 4. Exact central-density formula

Take now the centered interval heavy law `U`. For `y>0`, since `T_a` has the even density `h`, the density of `T_a^2` is

\[
q(y)=\frac{h(\sqrt y)}{\sqrt y}.
\tag{4.1}
\]

Therefore, with `r=sqrt(u^2+s^2)`, conditioning on `(U,S_a)=(u,s)` gives

\[
C(a):=p_{U^2+S_a^2-T_a^2}(0)
=\int_{|u|\le1/2}\int_{\mathbb R}
 h(s)\frac{h(r)}r\,ds\,du.
\tag{4.2}
\]

By fourfold symmetry and polar coordinates `u=r cos(theta)`, `s=r sin(theta)`, the Jacobian cancels `1/r`:

\[
\boxed{
C(a)=4\int_0^{\pi/2}\int_0^{1/(2\cos\theta)}
 h(r\sin\theta)h(r)\,dr\,d\theta.
}
\tag{4.3}
\]

At `theta=pi/2` the radial cap is interpreted as infinity; this single endpoint is immaterial.

## 5. A two-norm angular envelope

Set

\[
J(\theta)=\int_0^\infty h(r\sin\theta)h(r)\,dr.
\]

First, (3.1) and `integral_0^infinity h=1/2` imply

\[
J(\theta)\le\sqrt2\cdot\frac12=\frac1{\sqrt2}.
\tag{5.1}
\]

Second, Cauchy--Schwarz and (3.3) give, for `theta>0`,

\[
\begin{aligned}
J(\theta)
&\le
\left(\int_0^\infty h(r\sin\theta)^2dr\right)^{1/2}
\left(\int_0^\infty h(r)^2dr\right)^{1/2}\\
&=\frac{\|h\|_2^2}{2\sqrt{\sin\theta}}
\le\frac1{2\sqrt{\sin\theta}}.
\end{aligned}
\tag{5.2}
\]

The bounds cross at `sin(theta)=1/2`, i.e. `theta=pi/6`. Extending the radial range in (4.3) to infinity therefore yields the sharper intermediate bound

\[
C(a)
\le4\left[
\frac{\pi}{6\sqrt2}
+\frac12\int_{\pi/6}^{\pi/2}(\sin\theta)^{-1/2}d\theta
\right].
\tag{5.3}
\]

The right side is about `3.81729`; no numerical value is needed below.

On `[0,pi/2]`, concavity gives `sin(theta)>=2theta/pi`. Hence

\[
\int_{\pi/6}^{\pi/2}(\sin\theta)^{-1/2}d\theta
\le\int_{\pi/6}^{\pi/2}\sqrt{\frac\pi{2\theta}}d\theta
=\pi\left(1-\frac1{\sqrt3}\right).
\tag{5.4}
\]

Substitution into (5.3) proves

\[
\boxed{
C(a)\le B_0
=2\pi\left(1-\frac1{\sqrt3}+\frac1{3\sqrt2}\right).
}
\tag{5.5}
\]

## 6. Elementary strict certificate below `3sqrt(2)`

Use only

\[
\pi<\frac{22}{7},\qquad
\frac1{\sqrt3}>\frac47,\qquad
\frac1{3\sqrt2}<\frac6{25}.
\]

The middle inequality follows from `sqrt(3)<7/4`; the last from `25<18sqrt(2)`. Therefore

\[
1-\frac1{\sqrt3}+\frac1{3\sqrt2}
<1-\frac47+\frac6{25}=\frac{117}{175},
\]

and hence

\[
B_0<\frac{44}{7}\frac{117}{175}
=\frac{5148}{1225}.
\tag{6.1}
\]

Finally

\[
5148^2=26,501,904
<27,011,250=18\cdot1225^2,
\]

so `5148/1225<3sqrt(2)`. This proves the strict inequality in (1.2) without decimal approximations.

## 7. Arbitrary heavy law: exact extremizer transfer

This section extends the designated fleet02/B17 mechanism to the arbitrary-weight bank and also records its direct use on the partner's equal-weight sequence.

Let

\[
k(w)=p_{S_a^2-T_a^2}(w).
\]

The density of `S_a^2` is

\[
a_0(u)=\frac{h(\sqrt u)}{\sqrt u},\qquad u>0,
\]

which is nonincreasing because both factors are. Therefore

\[
k(w)=\int_0^\infty a_0(u)a_0(u+|w|)du
\tag{7.1}
\]

is even and nonincreasing in `|w|` (truncate at the logarithmic singularity and pass by monotone convergence if desired).

For arbitrary cap-one `f`,

\[
p_{Q_{a,f}}(s)=\int_{\mathbb R}f(x)k(s-x^2)dx.
\tag{7.2}
\]

For fixed `s`, the bathtub principle fills a measure-one superlevel set of `x -> k(s-x^2)`, equivalently the points with smallest `|s-x^2|`.

Exactly as in the completed fleet02/B17 finite-extremizer theorem:

* if `s<=1/8` (and in particular if `s<0`), the relevant optimizer on the nonnegative-side transition is the centered unit interval; for `s<0`, the inequality to the `s=0` value is immediate from monotonicity of `k`;
* if `s>=1/8`, the optimizer is the symmetric two-shell set `[-a,-b] union [b,a]`, with `a-b=1/2` and `a^2+b^2=2s`;
* under normalized Lebesgue measure on this shell, `R_s=|x^2-s|` is stochastically increasing for `s>=1/8`, because for `0<=r<1/8`,
  \[
  P(R_s\le r)=2(\sqrt{s+r}-\sqrt{s-r})
  \]
  has negative derivative in `s`;
* hence the shell optimizer at any `s>=1/8` is no larger than the centered-interval value at `s=1/8`.

The completed fleet02/B17 symmetric-unimodal theorem applies to the three independent variables

\[
U,\quad S_a,\quad T_a,
\]

because all three have even densities decreasing on `[0,infinity)`. It gives

\[
p_{U^2+S_a^2-T_a^2}(s)\le p_{U^2+S_a^2-T_a^2}(0)
\quad\hbox{for all }s.
\tag{7.3}
\]

Combining the bathtub/shell comparison with (7.3) proves

\[
\boxed{
\sup_f\|p_{Q_{a,f}}\|_\infty=C(a),
}
\tag{7.4}
\]

and Sections 4--6 give `C(a)<=B_0<3sqrt(2)`.

### Direct application to the designated partner's unpaid scalar sequence

The latest fleet02/B17 report, commit

`7b6249a49017e246c3cbe82fc513d00b8062c3fb`,

reduces its exact source-valid family

\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m)
\]

to

\[
C_m=\sup_f\|p_{X_f^2+S_m^2-T_m^2}\|_\infty
=p_{U^2+S_m^2-T_m^2}(0),
\tag{7.5}
\]

and proves `m=1,2` exactly while leaving the finite/intermediate `m>=3` range open (large `m` was already controlled asymptotically from below the endpoint).

Take `a_j=1/sqrt(m)` in (5.5). Equation (7.5) then gives the actual partner-to-target inequality

\[
\boxed{
C_m\le B_0<3\sqrt2\qquad\text{for every finite }m\ge1.
}
\tag{7.6}
\]

So the partner's entire remaining scalar sequence is closed in one step. This is an application of the completed partner result, not merely a citation.

The generic mode-at-zero input used above is the completed fleet02/B17 theorem at

`yspennstate/math-open-problems@84ffc0f291ae192f4d82742ae6909943f6710bc7`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/B17-20260922T235536Z-r12-symmetric-unimodal/REPORT.md`.

## 8. Required newest-Claude result applied

The current required Claude package at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`,

proves Theorem C: for exact rank-three signature `(+,+,-)` and every one-sheet output `s>=0`,

\[
p_Q(s)\le\pi\sqrt2
\tag{8.1}
\]

(after the stated eigenvalue scaling). Apply it to every `A_a` in (2.1). It immediately controls the positive/one-sheet side, but `pi sqrt(2)>3sqrt(2)` and the two-sheet side is not covered by that theorem.

The present argument upgrades this concrete application to

\[
\boxed{
\sup_{s\in\mathbb R}\sup_f p_{Q_{a,f}}(s)
\le B_0<3\sqrt2<\pi\sqrt2.
}
\tag{8.2}
\]

Thus in this exact low-cross-rank/high-leverage family the Claude one-sheet bound is sharpened below the candidate obstruction and its general two-sheet gap is also closed. This does not transfer to arbitrary exact-rank-three projections because the proof uses the original-coordinate bank product structure.

The same Claude Fourier package also explains why this class is structurally useful as a stress test: every cross cut has rank at most two, so its three-volume exit has `Z=0`, while the singleton leverage is one and prevents direct use of the diffuse `<=1/2` Fresnel gate.

## 9. What this changes in the witness map

The known target-level lower obstruction remains

\[
C_{\rm univ}\ge3\sqrt2.
\]

This report does **not** prove that `3sqrt(2)` is the unrestricted sharp constant and does not prove the full QFORM theorem. It proves that a large exact adversarial architecture cannot exceed that obstruction:

* arbitrary finite bank size;
* arbitrary leverage weights inside the two rank-one banks;
* arbitrary cap-one law on the macroscopic singleton, including fragmented and unbounded support;
* every output level, not just zero;
* exact finite matrices with nonzero spectrum `{1,1,-1}`.

A sharper witness, if one exists, must therefore leave this structure. Serious survivors include genuinely non-collinear/shared-coordinate heavy rows, two or more arbitrary heavy physical laws interacting across spectral directions, coupled non-rank-one tails, or finite/mesoscopic structures that destroy the monotone bank kernel.

Continuity for the unrestricted target remains separate; this report claims essential boundedness only in its stated branch.

## 10. Corrections preserved

No step uses law-uniform pointwise quadratic-phase decay, independence after spectral rotation, the refuted arbitrary-joint rank-three coarea inequality, positive moments of worst conditional projection caps, a worst scalar-remainder conditional density supremum, a uniformly good single physical minor, or a universal rank-three cross cut. The product structure is explicit in the original coordinates throughout.

## 11. Deterministic check

`check_bound.py` and `CHECK_OUTPUT.txt` in this run directory verify the arithmetic only. The saved output is

```
B0=4.136547558097272
rational_certificate=4.202448979591836
3sqrt2=4.242640687119286
gap_3sqrt2_minus_B0=0.106093129022014
square_certificate: 26501904 < 27011250
PASS
```

The checker is not a proof certificate; Sections 2--8 contain the proof.
