# Audit, duplicate correction, and sharpened overlap-square Fourier theorem

This file is authoritative over novelty labels in `REPORT.md` for this run.

## 0. Correction after wider fleet search

A wider source search after the first report found that its Section 3 mechanism, exact rank-two crossing plus a genuinely fresh independent square, is **not new**. It was already proved as `QFORM-CROSS2-PLUS-FRESH-SQUARE-v1` by account02/B16, source

`yspennstate/math-open-problems@44bff195ea0a90c3fe24628eb2cf3b405368c37c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/account02-B16-20260923T153432Z-auto11/REPORT.md`.

Likewise the cap-one hyperbolic-product half-potential used in Section 6 is a rederivation/specialization of my own earlier `QFORM-AFFINE-HYPERBOLIC-FRACTIONAL-TRACE-SHARP-v1`, source

`yspennstate/math-open-problems`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B02/20260922T192922Z-account01-B02-qform-auto11/REPORT.md`.

Those parts of the first report remain valid proofs/checks but MUST NOT be counted as new theorem scope.

The genuinely new step of this run is the sharper square Fourier budget below and its application to the stronger **overlapping-square** theorem of account01/B16, where the square coordinate may be dependent on the two crossing coordinates inside the same original-coordinate bank.

The overlap source is

`yspennstate/math-open-problems@1e49b6e87c2e7b965beee1261bf66592966c5a01`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/account01-B16-20260923T170732Z-auto11/REPORT.md`,

Theorem `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1`.

## 1. Sharp square-density L^(3/2) budget

### Theorem — `QFORM-SQUARE-L32-SHARP-BUDGET-v1`

Let X have probability density f with `0<=f<=M`, and let

`S=lambda (X-c)^2`, `lambda!=0`.

Then

`boxed: ||p_S||_(3/2) <= 2 M^(2/3)|lambda|^(-1/3).`                (1.1)

The density-norm constant `2` is sharp.

With Fourier convention

`hat h(t)=int exp(itx)h(x)dx`,

the sharp Babenko--Beckner Hausdorff--Young inequality gives

`boxed:
 ||phi_S||_3
 <= 2 pi^(1/3) 3^(1/6) M^(2/3)|lambda|^(-1/3),`                  (1.2)

hence

`boxed:
 int_R |phi_S(t)|^3 dt
 <= 8 pi sqrt(3) M^2/|lambda|.`                                   (1.3)

This improves the `50 pi M^2/|lambda|` square budget used by the current B16 fresh-square and overlap-square sources by the exact factor

`8sqrt(3)/50 = 4sqrt(3)/25 =0.277128...`.                          (1.4)

The sharp Hausdorff--Young constant and Fourier normalization are source-pinned in

`yspennstate/math-open-problems@1fe3d344529b743f64cb37b42a7a12b6a86a9414`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T114830Z-account03-B08-qform-diffuse-v1/REPORT.md`, Lemma 1, which cites Beckner (1975).

### Proof of (1.1)

Translation reduces to c=0 and scaling to lambda=1. For x>0 set

`F(x)=f(x)+f(-x)`.

Then `0<=F<=2M` and `int_0^infinity F=1`. The square density is

`g(u)=F(sqrt u)/(2sqrt u)`, `u>0`.

Therefore, after `u=x^2`,

`int_0^infinity g(u)^(3/2)du
 =2^(-1/2) int_0^infinity F(x)^(3/2)x^(-1/2)dx.`                  (1.5)

Since `F^(3/2)<=sqrt(2M)F`, and the bathtub principle gives

`int F(x)x^(-1/2)dx
 <=2M int_0^(1/(2M)) x^(-1/2)dx
 =2sqrt(2M)`,                                                       (1.6)

we get

`int g^(3/2)<=2sqrt(2)M`.                                          (1.7)

Taking the power `2/3` gives `||g||_(3/2)<=2M^(2/3)`. Equality is attained by `f=M 1_[-1/(2M),1/(2M)]`, so this density-norm constant is sharp.

For (1.2), the sharp Hausdorff--Young constant for `p=3/2`, `p'=3`, in the convention `int exp(itx)` is

`(2pi)^(1/3) * [( (3/2)^(2/3) )/(3^(1/3))]^(1/2)
 = pi^(1/3)3^(1/6)`.                                               (1.8)

Multiply (1.8) by (1.1). Cubing gives (1.3).

No pointwise quadratic-phase decay is used.

## 2. Main sharpened theorem: dependent overlap-square compiler

Take the exact hypotheses of account01/B16 `QFORM-CROSS2-OVERLAP-SQUARE-L1-v1`:

- original source coordinates split into independent banks I and J;
- `(Z,T) in R^2 x R` is a three-dimensional linear image of `X_I` with joint density cap M;
- `W in R^2` is a two-dimensional linear image of `X_J` with density cap N;
- `Sigma=diag(s1,s2)`, `s1,s2>0`;
- `lambda!=0`;
- arbitrary measurable `H(X_J)`;
- the form is

`Q=2 Z^T Sigma W + lambda(T+h^T Z+u0)^2+r(Z)+H(X_J)`.

The original proof used the square budget `50pi`. Replace only that input by (1.3). For the unnormalized slice

`G_z(t)=int rho(z,s) exp(it lambda s^2)ds`,

with slice mass `m(z)`, normalization gives

`int |G_z(t)|^3 dt
 <= 8pi sqrt(3) M^2 m(z)/|lambda|`.                                (2.1)

Since `|G_z(t)|<=m(z)`, also

`int |G_z(t)|^4 dt
 <= 8pi sqrt(3) M^2 m(z)^2/|lambda|`.                              (2.2)

Exactly as in the checked B16 proof, if

`H_4(t)=(int_R2 |G_z(t)|^2 dz)^(1/2)`,

Minkowski gives

`boxed:
 ||H_4||_4
 <=(8pi sqrt(3))^(1/4) M^(1/2)|lambda|^(-1/4).`                   (2.3)

The crossing step is unchanged:

`|phi_Q(t)|
 <= [pi sqrt(N)/( |t| sqrt(s1s2) )] H_4(t).`                      (2.4)

Split at `T0`, use Holder `(4,4/3)` on the tails, and optimize exactly as in B16. The only change is `50pi -> 8pi sqrt(3)`. Therefore the density coefficient improves by `(4sqrt(3)/25)^(1/5)`.

### Theorem — `QFORM-CROSS2-OVERLAP-SQUARE-L1-SHARPENED-v1`

Under the preceding hypotheses,

`boxed:
 ||p_Q||_infinity
 <= Csharp (MN)^(2/5)(s1s2)^(-2/5)|lambda|^(-1/5),`               (2.5)

where

`boxed:
 Csharp=5(27sqrt(3)/64)^(1/5)
       =4.695900517721562... .`                                    (2.6)

Moreover the proof is a genuine unweighted Fourier-L1 argument, so

`boxed:
 integral_R |phi_Q(t)|dt
 <=2pi Csharp (MN)^(2/5)(s1s2)^(-2/5)|lambda|^(-1/5),`             (2.7)

and the density is continuous and vanishes at infinity.

This strictly improves the previous overlap coefficient

`5(675/256)^(1/5)=6.069917185377548...`.                           (2.8)

No source-provenance hypothesis has changed.

### Slight scope strengthening

The same proof does not need the square center `h^Tz+u0` to be affine or `r(z)` to be quadratic. Fiberwise translation shows that (2.5)-(2.7) remain valid for

`lambda(T+c(Z))^2+r(Z)`                                            (2.9)

with arbitrary measurable real `c,r`, because for each z the map `T -> T+c(z)` is a translation and preserves the joint density cap and slice mass. This extra generality is not needed for a quadratic form but can be used after conditioning/reduction without reopening the proof.

## 3. Product-projection constants improve substantially

For orthonormal three- and two-dimensional product projections, the reviewed projection theorem gives

`M<=2^(3/2)`, `N<=2`, hence `(MN)^(2/5)<=2`.                       (3.1)

Therefore

`boxed:
 ||p_Q||_infinity
 <= 2 Csharp (s1s2)^(-2/5)|lambda|^(-1/5)
 <9.392 (s1s2)^(-2/5)|lambda|^(-1/5).`                            (3.2)

For the concrete B16 target family `s1=s2=2`, `|lambda|=1`, the old bound `<6.973` improves to

`boxed: ||p_Q||_infinity <5.395,`                                  (3.3)

and

`boxed: integral |phi_Q| <33.893.`                                 (3.4)

This is an overlapping-source theorem: the square variable T is allowed to be arbitrarily dependent on the crossing pair Z inside bank I.

## 4. The fresh-square partner theorem also sharpens

Applying (1.3) to account02/B16 `QFORM-CROSS2-PLUS-FRESH-SQUARE-v1` at the same proof line replaces its coefficient `900^(1/3)` by

`boxed:
 Cfresh=(144sqrt(3))^(1/3)=6.294690380529889... .`                 (4.1)

Thus its exact scope now admits

`boxed:
 ||p_Q||_infinity
 <=(144sqrt(3))^(1/3)L^(2/3)(|lambda|s1s2)^(-1/3),`               (4.2)

with Fourier L1 and continuous density.

For its concrete target family `s1=s2=2`, `|lambda|=L=1`, the previous `<6.083` improves to

`boxed: ||p_Q||_infinity <3.966,`                                  (4.3)

`boxed: integral |phi_Q| <24.916.`                                 (4.4)

This part is a coefficient sharpening of an existing partner theorem, not new scope.

## 5. Actual strong-cut endpoint using the overlap theorem

Return to the current literal strong cut with

`E=||M||_F^2>E0=11907/16384`.

On the exact-rank-two boundary, outside the near-rank-one tube `x2<E/64`, one has

`x1>=E/2`, `x2>=E/64`,

hence

`s1s2=sqrt(x1x2)>=E/sqrt(128)>E0/sqrt(128).`                      (5.1)

If a same-bank third projection supplies an overlap square with normalized `|lambda|>=1` and the orthonormal projection geometry of (3.1), then (3.2) gives the explicit actual inequality

`boxed:
 ||p_Q||_infinity <28.161,`                                       (5.2)

with a continuous density and genuine Fourier L1.

This does not assert that every target low-rank tube automatically furnishes such an overlap square. It states the exact receiver once that source-valid geometry is exposed.

## 6. Relation to designated account02/B02 and remaining debt

The current account02/B02 physical-E3 theorem remains the complementary aggregate receiver. On the actual strong-cut non-lowrank branch

`Z=E3(M)>2.3061517378361292e-5`,

it gives

`||p_Q||_infinity<61.317722`,

`integral |phi_Q|<385.270608`.

Thus:

- positive third cross volume at the strong-cut scale is paid by account02/B02;
- exact rank two plus a transverse square **in the same crossing bank** is paid by the sharpened B16 overlap compiler above;
- the remaining B02 debt is the rank-one / rank-two low-cross-rank geometry where the needed third curvature is entangled in a way not representable as one scalar square fiber over a bounded three-dimensional joint projection, or where the spectral scale of that square is not yet forced.

No counterexample to the target-wide universal `integral |phi_Q|` criterion is produced here. It remains `OPEN_NOT_REFUTED`.
