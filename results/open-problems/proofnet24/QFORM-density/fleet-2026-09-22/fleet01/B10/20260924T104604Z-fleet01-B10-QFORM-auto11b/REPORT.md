# fleet01/B10 — sliced L2 Wiener–Fresnel theorem for the punctured near-coloop rank-three case

## Status

**PROVED SUPPORTING THEOREM / NEW SIXTH-ROOT NEAR-COLOOP COMPILER / DESIGNATED PARTNER ENDPOINT APPLIED / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN.**


The new point is a mixed-norm replacement for the previous one-hub residual Wiener bound. If a physical hub has leverage `h` and the remaining normalized leaf frame satisfies a weaker *duplicated-slice leverage* gate, then the punctured near-coloop density cost is only

`[h(1-h)]^(-1/6)`

rather than the previous conditional-residual cost `(1-h)^(-1/3)`. The proof keeps the hub transform in `L^2`, squares only the two-dimensional leaf-frequency slice, and applies geometric Brascamp--Lieb in an exact five-dimensional duplicated frame. For the live harmonic survivor this gives a continuous density bound

`||p_Q||_infinity <= 3*2^(-1/6)*e^(5/6) [c rho]^(-1/6)`.

At the exact endpoint `rho=0`, the newest completed designated partner `fleet02/B10` theorem supplies the finite bound `<9.525`; hence the remaining divergence is again a proof-gluing loss, now reduced to a sixth-root.

## 1. A general leverage-half Wiener lemma in dimension m

We use the following elementary consequence of geometric Brascamp--Lieb and sharp Hausdorff--Young.

Let `b_j in R^m` satisfy

`sum_j b_j b_j^T = I_m`,

and put `c_j=||b_j||^2`. Assume `c_j<=1/2` whenever `c_j>0`. For each `j`, let `f_j` be a probability density on `R` with `0<=f_j<=1`, and use the Fourier convention

`hat f(xi)=int exp(i xi x) f(x) dx`.

Then

`W_m := int_{R^m} prod_j |hat f_j(b_j dot x)| dx
       <= (2*pi)^m exp(m/2).`                                      (1.1)

Proof. Write `b_j=sqrt(c_j) theta_j`; then

`sum_j c_j theta_j theta_j^T=I_m`.

Set `q_j=1/c_j>=2`, `p_j=1/(1-c_j)<=2`, and

`F_j(t)=|hat f_j(sqrt(c_j)t)|^(1/c_j)`.

The rank-one geometric Brascamp--Lieb inequality gives

`W_m <= prod_j c_j^(-c_j/2) ||hat f_j||_{q_j}.`                    (1.2)

Sharp Babenko--Beckner Hausdorff--Young for the above unnormalised Fourier convention gives

`||hat f_j||_{q_j}
 <= (2*pi)^(c_j) c_j^(c_j/2)
    (1-c_j)^(-(1-c_j)/2) ||f_j||_{p_j}.`                          (1.3)

Since `f_j<=1` and `int f_j=1`, `||f_j||_{p_j}<=1`. The `c_j` powers cancel exactly. Also

`(1-c) log(1/(1-c)) <= c`, `0<=c<1`,

so, using `sum c_j=m`, (1.2)--(1.3) yield (1.1). Zero vectors contribute the harmless factor `hat f_j(0)=1` and are omitted.

No independence statement is hidden here: (1.1) is simply an analytic inequality for the product of one-dimensional transforms. In the application those transforms arise from the genuine ORIGINAL-coordinate product source.

## 2. Sliced L2 Wiener theorem

Let `(z_i,l_i,v_i)`, `i=1,...,N`, be the rows of an `N x 3` matrix whose columns are orthonormal. Thus

`sum z_i^2=sum l_i^2=sum v_i^2=1`,
`sum z_i l_i=sum z_i v_i=sum l_i v_i=0`.                           (2.1)

For independent ORIGINAL variables `X_i` with densities `f_i<=1`, define

`Phi(p,q,w)=prod_i hat f_i(p z_i+q l_i+w v_i)`                    (2.2)

and the two-frequency absolute slice

`F(p)=int_{R^2}|Phi(p,q,w)| dq dw`.                                (2.3)

Put

`epsilon_i = z_i^2/2 + l_i^2+v_i^2`.                              (2.4)

### Theorem 2.1 — `QFORM-SLICED-L2-WIENER-v1`

If

`max_i epsilon_i <=1/2`,                                          (2.5)

then

`boxed:
 ||F||_2^2 <= 2^(-1/2)(2*pi)^5 e^(5/2),
 ||F||_2   <= 2^(-1/4)(2*pi)^(5/2)e^(5/4).`                       (2.6)

### Proof

Square (2.3), use Tonelli, and introduce two independent two-frequency variables `eta=(q,w)` and `eta'=(q',w')`:

`||F||_2^2
 =int_{R x R^2 x R^2}
   prod_i |hat f_i(z_i p + l_i q+v_i w)|
          |hat f_i(z_i p + l_i q'+v_i w')|
   dp d eta d eta'.`                                              (2.7)

Set `x_0=sqrt(2)p`. In `R^5=R x R^2 x R^2`, define the duplicated vectors

`b_i^+ = (z_i/sqrt(2), l_i,v_i, 0,0)`,
`b_i^- = (z_i/sqrt(2), 0,0, l_i,v_i)`.                            (2.8)

By (2.1), all cross blocks cancel and

`sum_i (b_i^+ (b_i^+)^T+b_i^- (b_i^-)^T)=I_5`.                  (2.9)

Moreover

`||b_i^+||^2=||b_i^-||^2=epsilon_i<=1/2`.                         (2.10)

The change `x_0=sqrt(2)p` has Jacobian `dx_0=sqrt(2)dp`, hence the five-dimensional Wiener integral associated with the `2N` vectors in (2.8) is exactly `sqrt(2)||F||_2^2`. Apply (1.1) with `m=5`. Repeating the same scalar density `f_i` in the `+` and `-` factors causes no issue: the proof of (1.1) only uses its cap-one `L^p` bounds. Therefore

`sqrt(2)||F||_2^2 <=(2*pi)^5 e^(5/2)`,

which is (2.6).

The significance of (2.5) is that the longitudinal leaf coefficient `z_i` costs only **half leverage** after the slice is squared. This is strictly weaker than requiring the full three-dimensional leaf leverage `z_i^2+l_i^2+v_i^2` to be at most `1/2`.

## 3. One-hub mixed Wiener bound

Let `H` be an ORIGINAL variable independent of all leaf variables and with density `f_H<=1`. Let

`psi_H(xi)=E exp(i xi H)`.

By Plancherel and `int f_H^2<=1`,

`||psi_H(s .)||_2 <= (2*pi/|s|)^(1/2)`                            (3.1)

for every `s!=0`.

For `a!=0`, define the three-dimensional characteristic transform

`Chi_{s,a}(xi,q,w)=psi_H(s xi) Phi(a xi,q,w)`.                    (3.2)

This is precisely the characteristic function of

`Y=(sH+aZ,L,V)`,
`Z=sum z_iX_i`, `L=sum l_iX_i`, `V=sum v_iX_i`.                  (3.3)

No independence among `(Z,L,V)` is asserted.

By Cauchy--Schwarz, the scaling of `F`, (3.1), and (2.6),

`||Chi_{s,a}||_1
 =int |psi_H(s xi)| F(a xi) dxi
 <= ||psi_H(s .)||_2 ||F(a .)||_2
 <= 2^(-1/4)(2*pi)^3 e^(5/4) (|sa|)^(-1/2).`                    (3.4)

Thus the small leakage `a` now costs only `|a|^(-1/2)` in Wiener norm. A direct three-dimensional absolute Wiener payment would cost `|a|^(-1)`; the duplicated slice saves its square root.

## 4. Sliced Wiener--Fresnel compiler

Let `M` be any invertible real symmetric `3 x 3` matrix, `beta in R^3`, and `gamma in R`. Put

`D=|det M|`,
`R=Y^T M Y+beta^T Y+gamma`,                                     (4.1)

where `Y` is (3.3).

### Theorem 4.1 — `QFORM-SLICED-L2-WIENER-FRESNEL-v1`

Under (2.5), `R` has a continuous density and

`boxed:
 ||p_R||_infinity
 <= 3*2^(-1/6)*e^(5/6)
       (D |s a|)^(-1/3).`                                       (4.2)

Numerically the universal front constant is

`3*2^(-1/6)*e^(5/6)=6.1498094150...`.                           (4.3)

### Proof

Because (3.4) is finite, Fourier inversion for the law of `Y` is legitimate. With Gaussian damping and then dominated convergence, the standard three-dimensional Fresnel integral gives for `t!=0`

`|phi_R(t)|
 <= (2*pi)^(-3)||Chi_{s,a}||_1
    pi^(3/2)|t|^(-3/2)D^(-1/2).`                                (4.4)

The arbitrary affine term only shifts the linear phase in the Gaussian integral and does not alter its modulus. From (3.4),

`|phi_R(t)|
 <= min(1,B |t|^(-3/2))`,                                      (4.5)

where

`B=2^(-1/4) pi^(3/2)e^(5/4)
   (D |s a|)^(-1/2).`                                           (4.6)

The crossover is `t_0=B^(2/3)`. Hence

`int_R |phi_R(t)|dt
 <=2[t_0+B int_{t_0}^infinity t^(-3/2)dt]
 =6B^(2/3).`                                                     (4.7)

Therefore `phi_R in L^1`; scalar Fourier inversion yields a continuous density, and

`||p_R||_infinity
 <=(2*pi)^(-1)6B^(2/3)
 =3*2^(-1/6)e^(5/6)(D|sa|)^(-1/3).`                             (4.8)

This proves (4.2).

## 5. Generic exact-rank-three one-heavy-row formulation

Let

`A=U M U^T`, `U^T U=I_3`,                                      (5.1)

be exact rank three, with all three nonzero eigenvalue moduli at least one. Then `D=|det M|>=1`.

Choose an ORIGINAL coordinate `0` whose physical spectral row has leverage

`h=||u_0||^2 in (0,1)`.                                        (5.2)

Rotate only the three-dimensional coefficient bookkeeping so that

`u_0=sqrt(h)e_1`.                                                (5.3)

This is not a probabilistic rotation. Parseval implies that the leaf coefficients can be written

`u_i=(sqrt(1-h) z_i,l_i,v_i)`, `i!=0`,                           (5.4)

where the three leaf coefficient vectors `(z,l,v)` are orthonormal. Let `H=X_0` and define `Z,L,V` from the ORIGINAL leaf coordinates as in (3.3). Then the actual spectral projection is exactly

`U^T X=(sqrt(h)H+sqrt(1-h)Z,L,V)`.                              (5.5)

Consequently, if every leaf row satisfies the anisotropic duplicated-slice gate

`boxed:
 z_i^2/2+l_i^2+v_i^2 <=1/2,`                                    (5.6)

Theorem 4.1 gives the target-valid branch

`boxed:
 ||p_{X^TAX}||_infinity
 <=3*2^(-1/6)e^(5/6)
    D^(-1/3)[h(1-h)]^(-1/6).`                                  (5.7)

The density is continuous on this branch.

Compared with the previous conditional-residual Wiener estimate

`3e [D(1-h)]^(-1/3)`,                                           (5.8)

(5.7) halves the near-coloop blow-up exponent from `(1-h)^(-1/3)` to `(1-h)^(-1/6)` and uses the weaker gate (5.6), where the longitudinal residual direction has half weight.

In the earlier ultra-coloop notation `u_i=t_i r+p_i`, `tau_i=||p_i||^2`, one has after normalizing the residual longitudinal column

`z_i^2=t_i^2/(1-h)`, `l_i^2+v_i^2=tau_i`.                       (5.9)

Thus (5.6) is

`t_i^2/[2(1-h)] + tau_i <=1/2`.                                 (5.10)

Inside the already isolated diffuse-transverse state `tau_i<1/4`, failure of (5.10) forces

`z_i^2>1-2tau_i>1/2`.                                           (5.11)

Hence at most one leaf coordinate can violate the sliced gate there. So the only structural failure of this new compiler in that chamber is a unique **second longitudinal near-coloop** leaf coordinate; this is a sharper obstruction than a generic failure of the full residual leverage-`1/2` gate.

Equation (5.7) is not uniform as `h->1`; (5.11) therefore does not by itself close the near-coloop collar. It identifies exactly what the next gluing argument must improve.

## 6. Concrete application to the designated partner's harmonic survivor

The completed `fleet02/B10` harmonic construction uses `m=123` leaf coordinates

`z_j=sqrt(2/m) cos(2 theta_j)`,
`r_j=sqrt(2/m) cos(theta_j)`,
`y_j=sqrt(2/m) sin(theta_j)`,
`theta_j=2*pi*j/m`,                                               (6.1)

and

`Q_rho=2(sqrt(c)H+sqrt(rho)Z)L+V^2`,
`c=1-rho`, `0<rho<1/64`.                                         (6.2)

The coefficient matrix on `(sqrt(c)H+sqrt(rho)Z,L,V)` is

`M_0=[[0,1,0],[1,0,0],[0,0,1]]`,

so `D=1` and the spectrum is exactly `{-1,1,1}`.

Here

`r_j^2+y_j^2=2/m`,
`z_j^2<=2/m`,

therefore the sliced leverage is

`epsilon_j=z_j^2/2+r_j^2+y_j^2<=3/m=1/41<1/2`.                  (6.3)

Theorem 4.1 applies to **arbitrary cap-one ORIGINAL source densities**, with no bounded-support or smoothness assumption, and yields

`boxed:
 ||p_{Q_rho}||_infinity
 <=3*2^(-1/6)e^(5/6)[c rho]^(-1/6).`                            (6.4)

The density is continuous for every `rho>0`.

For example:

- at `rho=1/64`, `c=63/64`, (6.4) gives `<12.332`;
- throughout `rho>=2^(-12)` and `c>63/64`, (6.4) gives `<24.664`.

This is a substantial improvement over the determinant-after-hub-conditioning cost of order `rho^(-1/3)`. It also converts the partner's exact hyperbolic--Fresnel representation into a complete positive punctured estimate without ever taking a pointwise one-dimensional van-der-Corput bound.

## 7. Newest designated partner endpoint applied at an actual inequality

The newest completed designated partner result is

`yspennstate/math-open-problems@461ca4597face7955d318d0540729ca6b809fce2`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260924T094654Z-fleet02-B10-QFORM-r13/REPORT.md`.

It proves the dependence-safe endpoint receiver: if `H` is genuinely independent of the whole leaf pair `(L,V)`, `||p_(L,V)||_infinity<=K`, and

`Q=2aHL+bL^2+2cLV+dV^2`, `ad!=0`,

then

`||p_Q||_infinity<=6K^(2/3)|a|^(-2/3)|d|^(-1/3)`.              (7.1)

In its exact-coloop/null-hub target geometry, the partner establishes

`K<=2`, `|a|>=1`, `|d|>=1`.                                    (7.2)

Therefore at the actual endpoint `h=1` (equivalently `rho=0` in the harmonic family),

`boxed:
 ||p_Q||_infinity <=6*2^(2/3)<9.525.`                           (7.3)

This is the required actual use of the designated partner theorem. Combining (6.4) with (7.3) proves that the endpoint itself is finite while the best bound furnished by the present punctured absolute-Wiener compiler diverges only as `rho^(-1/6)`. Thus the unresolved issue is a gluing/cancellation problem, not endpoint singularity or lack of third-rank curvature.

The partner's endpoint theorem establishes essential boundedness; it does not claim continuity. The new positive-leakage branch (4.2)/(6.4) does establish continuity.

## 8. Why this mixed-norm mechanism cannot itself become endpoint-uniform

The proof deliberately uses the strongest law-uniform Fourier norm available for an arbitrary cap-one one-dimensional hub: Plancherel gives `psi_H in L^2`. More generally Hausdorff--Young supplies `psi_H in L^q` for `q>=2`, never a law-uniform `L^q` norm with `q<2` under the present assumptions.

If one combines `psi_H in L^q` with a scaled leaf slice `F(a xi)` by ordinary Holder, the conjugate exponent is `p=q/(q-1)<=2`, and scaling costs `|a|^(-1/p)`. This is minimized at `p=2`, namely the `|a|^(-1/2)` Wiener cost used above. After the three-dimensional Fresnel time integration this becomes the `|a|^(-1/3)=rho^(-1/6)` density cost.

Therefore no rearrangement of this same **absolute mixed-norm** interface can remove the endpoint loss. An endpoint-uniform proof must retain additional phase/product provenance (as in the partner's exact endpoint receiver), or introduce a genuinely different source-level argument before the final modulus.

This observation is only a barrier for the present proof architecture, not a counterexample to QFORM.

## 9. Exact remaining implication

The first unpaid implication is now

`QFORM-SIXTH-ROOT-TO-ENDPOINT-PROVENANCE-GLUING-v1`:

> Bridge the target-valid punctured estimate
> 
> `3*2^(-1/6)e^(5/6)D^(-1/3)[h(1-h)]^(-1/6)`
> 
> to the finite exact-coloop partner endpoint without coefficient-continuity assumptions, while retaining ORIGINAL-product provenance. In the diffuse-transverse collar, also handle the unique possible second longitudinal near-coloop singled out by (5.11). The bridge must not use conditional projection caps, arbitrary-joint coarea, pointwise van-der-Corput decay, or a fiber supremum.

Full exact rank three remains **OPEN**. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**; continuity is proved only for the positive-leakage sliced-Wiener branches in this report.

## 10. Source dependencies actually used

- Fresh `math-research-brain` QFORM owner control and live correction ledger, revision `2026-09-22.15`.
- Own predecessor leverage-half Wiener--Fresnel proof:
  `yspennstate/math-open-problems@aff6876a6017be77544c50e8904e9baf8dac3bfe`,
  `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B10/20260924T101649Z-fleet01-B10-QFORM-auto11/REPORT.md`.
- Designated partner endpoint proof:
  `yspennstate/math-open-problems@461ca4597face7955d318d0540729ca6b809fce2`,
  `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260924T094654Z-fleet02-B10-QFORM-r13/REPORT.md`.
- Designated partner harmonic source geometry and exact hyperbolic--Fresnel normal form:
  `yspennstate/math-open-problems@fe4042fe31234cbe45ed47a6b1546fa70f687b68`,
  `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260924T064844Z-fleet02-B10-QFORM-r11/REPORT.md`.

No Gaussianity, log-concavity, moments, compact support, connected support, diagonal-basis assumption, post-rotation independence, Monte Carlo extremality claim, or public release is used.
