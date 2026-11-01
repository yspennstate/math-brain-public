SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B03, 2026-09-24T02:04:13Z.
attacking: exact-rank-two one-anchor transduction — spend one genuinely transverse hub-star direction on top of the rank-two cross Plancherel factor, and identify the exact aligned-star residue through anchored third volume.

# fleet03/B03 r45 — rank-two crossing plus one transverse hub direction gives full `|t|^{-3/2}`

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: decoupled time integral  
Classification: **NEW SUPPORTING THEOREM / LIVE EXACT-RANK-TWO SUBBRANCH PAID / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The branch proved in Theorem 2.1 below has a continuous `C_0` density.

## 1. Fresh source boundary and live debt


The immediate input is fleet03/B03 r44,

`yspennstate/math-open-problems@03013f4567814d42edddfc74ef48c8ee942b17c9`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260924T014218Z-fleet03-B03-QFORM-r44/REPORT.md`.

For two genuine independent product banks with an **exact rank-two** crossing of singular product `p=s_1 s_2`, r44 proved the dependence-safe aggregate estimates

`|phi(t)| <= min(1,2 pi p^(-1/2)|t|^(-1))`,

`||p||_2^2 <=4 p^(-1/2)`,

`int |t|^(-1/2)|phi(t)|^2 dt <=(16/3)sqrt(2pi) p^(-1/4)`,

and

`sup_a E|Q-a|^(-1/4) <=4p^(-1/8)`.

Its unresolved step was to obtain the missing one-copy quarter power from the live one-anchor geometry without selecting a tiny physical minor.

The fresh fleet03/B20 structural funnel is

`yspennstate/math-open-problems@1e8d908588d359d291adf1d9c926bc9870039041`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260924T004659Z-fleet03-B20-QFORM-r43/REPORT.md`.

It shows that after the paid physical-`E_3` branch, every remaining `E_2>4/9` crossing lies in an ultra-thin rank-two tube or a giant near-rank-one tube. The present run pays a substantial **exact-rank-two** part of the first tube whenever the hub has one transverse star direction.

## 2. Main analytic theorem

### Theorem 2.1 — `QFORM-RANK2-TRANSVERSE-HUB-PLANCHEREL-v1`

Let `Z`, `X_R`, `X_C` be three genuinely independent source groups. Assume `Z` has density at most `M_0`. Let

`Y=(Y_1,Y_2,Y_3)`

be a three-dimensional linear projection of `X_R` with joint density at most `M_R`, and let

`W=(W_1,W_2)`

be a two-dimensional linear projection of `X_C` with joint density at most `M_C`. No independence is assumed among the coordinates of `Y` or among those of `W`.

Let `C` be an invertible real `2x2` matrix and let `alpha !=0`. Let `F_0,F_R,F_C` be arbitrary measurable real functions of their respective source groups, let `a=(a_1,a_2)` be arbitrary, and let `L_C(X_C)` be an arbitrary measurable real function. Define

`T = F_0(Z)+F_R(X_R)+F_C(X_C)
     +2 (Y_1,Y_2)^T C W
     +2Z[a_1Y_1+a_2Y_2+alpha Y_3+L_C(X_C)].`                  (2.1)

Then for every `t !=0`,

`boxed:
 |phi_T(t)|
 <= min{1,K |t|^(-3/2)},`                                      (2.2)

where

`K=pi^(3/2)(M_0M_RM_C)^(1/2)
       |det C|^(-1/2)|alpha|^(-1/2).`                           (2.3)

Consequently `T` has a continuous `C_0` density satisfying

`boxed:
 ||p_T||_infinity
 <=3 [M_0M_RM_C/(|det C||alpha|)]^(1/3).`                       (2.4)

The B03 whole-copy time integral obeys

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|^2 dt
 <=(24/5)K^(1/3).`                                               (2.5)

If `T'` is an independent copy of the **whole** scalar output `T`, then

`boxed:
 E|T-T'|^(-1/2)
 <=(24/(5sqrt(2pi)))K^(1/3).`                                   (2.6)

There is a symmetric version with the transverse third projection on the `C` bank instead of the `R` bank.

### Proof

Push the complex measure `exp(itF_R)dP_R` to `Y`; denote its density by `b_t(y_1,y_2,y_3)`. By Radon--Nikodym domination,

`|b_t(y)| <= p_Y(y)`,

so

`int |b_t|^2 <= M_R`.                                           (2.7)

For the fixed value `Z=z`, push

`exp{it[F_C(X_C)+2zL_C(X_C)]}dP_C`

to `W`; call the resulting complex density `c_{t,z}(w)`. Again

`|c_{t,z}(w)|<=p_W(w)`, hence

`||c_{t,z}||_2^2<=M_C`,                                         (2.8)

uniformly in `z`. This is where the arbitrary star on the opposite bank is retained exactly rather than discarded.

Take only the one-dimensional Fourier transform of `b_t` in the transverse coordinate:

`B_t(y_1,y_2;xi)
 =int b_t(y_1,y_2,y_3)e^(i xi y_3)dy_3`,

and put

`G_t(xi)=int_R2 |B_t(y_1,y_2;xi)|^2dy_1dy_2`.                   (2.9)

Partial Plancherel gives

`int_R G_t(xi)dxi
 =2pi int_R3 |b_t(y)|^2dy
 <=2pi M_R.`                                                     (2.10)

For fixed `z`, after integrating `y_3`, the remaining `(y_1,y_2,w_1,w_2)` kernel is

`exp{i2t[y^TCw+z a.y]}`.                                        (2.11)

The modulation `exp(i2tz a.y)` is unitary. With the Fourier convention `hat f(xi)=int e^(ixi.w)f(w)dw`, the bilinear operator

`(L_tf)(y)=int_R2 e^(i2t y^TCw)f(w)dw`

satisfies exactly

`||L_t||_(2->2)=pi/(|t|sqrt(|det C|))`,                          (2.12)

because `L_tf(y)=hat f(2tC^Ty)` and two-dimensional Plancherel gives the Jacobian `|det(2tC^T)|=4t^2|det C|`.

Therefore the fixed-`z` integral obeys

`|I_t(z)|
 <= [pi/(|t|sqrt(|det C|))]
    M_C^(1/2) G_t(2t alpha z)^(1/2).`                            (2.13)

The complex `Z`-amplitude has modulus at most its density `p_Z`. Apply Cauchy--Schwarz with respect to the probability measure `p_Z(z)dz`:

`|phi_T(t)|
 <= [pi M_C^(1/2)/( |t|sqrt(|det C|))]
    [int p_Z(z)G_t(2t alpha z)dz]^(1/2).`                        (2.14)

Since `p_Z<=M_0`, changing variables and using (2.10) yields

`int p_Z(z)G_t(2t alpha z)dz
 <= [M_0/(2|t alpha|)] int G_t(xi)dxi
 <= pi M_0M_R/(|t alpha|).`                                     (2.15)

Substituting into (2.14) proves (2.2)-(2.3).

Let `t_0=K^(2/3)`. Then

`int_R |phi_T(t)|dt
 <=2[t_0+K int_(t_0)^infinity t^(-3/2)dt]
 =6K^(2/3).`                                                     (2.16)

Fourier inversion gives a continuous `C_0` density and

`||p_T||_infinity <=(2pi)^(-1)6K^(2/3)`,

which simplifies to (2.4).

Likewise

`int_R |t|^(-1/2)|phi_T(t)|^2dt
 <=2 int_0^t0 t^(-1/2)dt
   +2K^2 int_t0^infinity t^(-7/2)dt
 =(24/5)K^(1/3),`                                                (2.17)

which is (2.5). Finally,

`int_R e^(itx)|t|^(-1/2)dt=sqrt(2pi)|x|^(-1/2)`                 (2.18)

in the standard regularized Riesz sense. Applying (2.18) only to the independent copy of the **whole** variable gives (2.6). No coordinate sum/difference conjugates are separated. QED.

### Why this survives the source corrections

The theorem uses no law-uniform pointwise quadratic-phase estimate. Its `|t|^{-3/2}` is produced by a rank-two bilinear Plancherel factor `|t|^{-1}` and one **genuinely transverse physical projection** factor `|t|^{-1/2}`. The coordinates of each projection are allowed to be dependent. The argument never conditions one coordinate of a projection on another and never asserts independence after an SVD rotation.

## 3. Application to the live exact-rank-two one-anchor packet

Consider the literal original-coordinate block

`M=[[b,r^T],[c,N]]`,                                             (3.1)

with one original hub coordinate `Z=X_j` and disjoint original-coordinate banks `R,C`. In the quadratic form the displayed block contributes

`bZ^2+2Z c^T X_R+2Z r^T X_C+2X_R^T N X_C`,                     (3.2)

while arbitrary within-`R`, within-`C`, diagonal and affine terms remain allowed.

Assume now that `N` has **exact rank two** with SVD

`N=s_1u_1v_1^T+s_2u_2v_2^T`, `s_1>=s_2>0`,

and write

`p=s_1s_2`, `U=span(u_1,u_2)`, `V=span(v_1,v_2)`,

`alpha=||P_(U^perp)c||_2`, `beta=||P_(V^perp)r||_2`.             (3.3)

If `alpha>0`, use the orthonormal physical-bank projections

`Y=(u_1^TX_R,u_2^TX_R,(P_(U^perp)c/alpha)^TX_R)`,

`W=(v_1^TX_C,v_2^TX_C)`.                                        (3.4)

The reviewed product-projection bound gives

`M_R<=2^(3/2)`, `M_C<=2`, `M_0<=1`.                              (3.5)

The full right star `2Zr^TX_C` is retained inside the `L_C` term of Theorem 2.1. Therefore

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6)(p alpha)^(-1/3),`                                  (3.6)

and the density is continuous and vanishes at infinity. Symmetrically, if `beta>0`,

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6)(p beta)^(-1/3).`                                   (3.7)

Hence

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6)[p max(alpha,beta)]^(-1/3)`                          (3.8)

whenever at least one transverse star is present.

On the actual exact-rank-two part of the live `E_2(N)>4/9` chamber,

`E_2(N)=p^2>4/9`, hence `p>2/3`.                                 (3.9)

Therefore if

`max(alpha,beta)>=1/64`,                                         (3.10)

then

`p max(alpha,beta)>1/96`, and (3.8) gives the completely numerical bound

`boxed: ||p_Q||_infinity <24.4757868319.`                        (3.11)

The corresponding assigned time estimate is

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <24.3009850036,`                                                 (3.12)

and the whole-copy half-Riesz potential is

`boxed: E|Q-Q'|^(-1/2)<9.6946903734.`                            (3.13)

Thus the exact-rank-two `E_2` chamber is no longer a generic one-copy-transduction debt. It is paid whenever even one hub star has a `1/64` transverse component. The remaining exact-rank-two collar has both hub stars nearly confined to the singular planes.

## 4. Exact anchored-volume identity in the aligned collar

The surviving collar can be described without choosing a physical minor.

### Lemma 4.1 — `QFORM-RANK2-ANCHORED-VOLUME-DECOMPOSITION-v1`

In the exact-rank-two setting above, choose SVD coordinates **only for the deterministic exterior-volume computation**. Write

`c=c_1u_1+c_2u_2+c_perp`,
`r=r_1v_1+r_2v_2+r_perp`,

`alpha=||c_perp||`, `beta=||r_perp||`,                           (4.1)

and define

`D_0=b s_1s_2-r_1c_1s_2-r_2c_2s_1.`                            (4.2)

Let

`J_sep=sum_(|P|=|Q|=2)
       det [[b,r_Q^T],[c_P,N_(P,Q)]]^2`                         (4.3)

be the full anchored third-volume used by the one-anchor structural packet. Then

`boxed:
 J_sep=D_0^2
       +alpha^2(s_1^2r_2^2+s_2^2r_1^2)
       +beta^2(s_1^2c_2^2+s_2^2c_1^2)
       +(s_1^2+s_2^2)alpha^2beta^2.`                             (4.4)

#### Proof

The quantity (4.3) is the squared Euclidean norm of the component of the third exterior power using the hub plus two light rows and the hub plus two light columns. It is invariant under orthogonal changes of basis within `R` and within `C`; this is a deterministic identity and does **not** rotate the random inputs.

In SVD coordinates, `N` has only entries `(1,1)=s_1`, `(2,2)=s_2`. The minor with both active rows and columns equals `D_0`. A minor with one perpendicular left row and active right pair contributes either `c_perp s_1r_2` or `c_perp s_2r_1`; summing its squares gives the second term in (4.4). The symmetric family gives the third term. If both row and column pairs contain one perpendicular direction, the only nonzero minors use the same active singular index, giving `(s_1^2+s_2^2)alpha^2beta^2`. All remaining minors vanish. Summing these disjoint families proves (4.4). QED.

In particular, at the **exact aligned endpoint** `alpha=beta=0`,

`boxed: J_sep=D_0^2.`                                           (4.5)

Thus the live threshold `J_sep>=1/2304` forces

`|D_0|>=1/48`                                                     (4.6)

at exact alignment. This does not by itself pay the near-aligned collar, because the coefficients `c_i,r_i` need not be individually bounded. It does, however, identify the exact scalar determinant resource that must be spent next rather than hiding the endpoint behind a reciprocal small singular vector.

## 5. A useful exact-alignment scalar-pivot supplement

When the hub diagonal is also quantitatively nonzero, the determinant resource in (4.6) can already be paid directly.

Assume `alpha=beta=0`, `b!=0`, and `D_0!=0`. Completing the square in the **genuine original hub coordinate** gives

`Q=b[Z+(c^TX_R+r^TX_C)/b]^2+R`,                                 (5.1)

where all same-bank terms remain arbitrary and the residual cross matrix on the two singular planes is

`N_eff=N-cr^T/b`.                                                (5.2)

The matrix determinant lemma gives

`det(N_eff)=D_0/b`.                                               (5.3)

The rank-two crossing Plancherel theorem therefore gives

`sup_s E|R-s|^(-1/2)
 <=8|D_0/b|^(-1/4).`                                             (5.4)

Conditionally on the two light banks, the shifted square of the independent cap-one variable `Z` has density bounded by

`|b|^(-1/2)|y|^(-1/2)`.                                         (5.5)

Combining (5.4)-(5.5),

`boxed:
 ||p_Q||_(infinity,ess)
 <=8|bD_0|^(-1/4).`                                              (5.6)

This supplement proves essential boundedness, not continuity. At the live exact-aligned threshold `|D_0|>=1/48`, any branch with `|b|>=1/64` is paid by

`||p_Q||_infinity <=8(3072)^(1/4)<59.559.`                       (5.7)

The genuinely difficult exact-aligned endpoint is therefore also forced into the **small-hub-diagonal** regime, consistent with the live B20 overlap-one split.

## 6. Designated fleet04/B03 partner applied

The current partner handoff is fleet04/B03 r2, brain commit

`dd2e1bf38270412879a5babd03a592d39b3e88a3`,

with corrected mathematics at

`yspennstate/math-open-problems@05ff82a8d052b024ae584e60dffb7b198fcd7db4`.

Its dependent-sum/difference fractional-budget theorem was reread and is not transplanted to singular-vector coordinates: a rotation of the original product coordinates does not preserve independence.

For an actual numerical consequence of the new branch, I use only the partner line that remains valid independently of its earlier corrected compiler,

`P(|Y-Y'|<=eps)<=2eps ||p_Y||_2^2`.                              (6.1)

Since `||p_Q||_2^2<=||p_Q||_infinity`, (3.11) gives on the newly paid live branch

`boxed:
 P(|Q-Q'|<=eps)
 <48.9515736638 eps.`                                             (6.2)

This is an actual partner-result application to a new inequality, not a citation-only handoff.

## 7. What remains

The full QFORM theorem is **not** proved here. The exact-rank-two live chamber is now reduced to the collar

`p>2/3`, `alpha<1/64`, `beta<1/64`,                              (7.1)

with the exact aligned endpoint carrying the determinant currency `|D_0|>=1/48` when `J_sep>=1/2304`. The small-hub-diagonal part of that aligned packet remains unpaid by this run.

More importantly, the current B20 global survivor is an **ultra-thin near-rank-two tube**, not necessarily an exact-rank-two matrix. The nonzero tail cannot be deleted under the target assumptions. The next B03 mechanism should therefore do one of two things:

1. extend Theorem 2.1 to retain the low-Frobenius cross tail by a coupled/time-integrated estimate rather than treating it as a small random perturbation; or
2. spend the near-aligned determinant currency jointly with the tail and a literal original-coordinate hub receiver.

The new theorem shows exactly why the transverse-star part is easier: rank-two bilinear Plancherel supplies `|t|^-1`, and one honest unused physical projection supplies the missing `|t|^-1/2`. No false pointwise quadratic decay is needed.

## 8. Status

`QFORM-RANK2-TRANSVERSE-HUB-PLANCHEREL-v1`: **PROVED supporting theorem**.  
`QFORM-RANK2-ANCHORED-VOLUME-DECOMPOSITION-v1`: **PROVED exact identity**.  
Exact-rank-two `E_2>4/9`, `max(alpha,beta)>=1/64`: **PAID, continuous `C_0` density, bound <24.476**.  
Exact-aligned `|b|>=1/64`, `J_sep>=1/2304`: **PAID in essential-boundedness sense, bound <59.559**.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.

No scheduler state, notification/email setting, permissions, public release, paid model/API/Codex action, installation, or cross-account authentication was changed in this mathematical run.
