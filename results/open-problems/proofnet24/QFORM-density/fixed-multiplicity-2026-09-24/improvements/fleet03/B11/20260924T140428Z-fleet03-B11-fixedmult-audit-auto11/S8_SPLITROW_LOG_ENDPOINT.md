# fleet03/B11 — s8 two-sided collar to a rank-two logarithmic endpoint

Run: `20260924T140428Z-fleet03-B11-fixedmult-audit-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Status: **PROVED SUPPORTING THEOREM; general s8 L-infinity theorem remains open.**

Pinned baseline source: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Inputs read and checked at fresh master `dd12ba4cca03c6e18c228fbff8b176398d1a95bf`:

1. fleet03/B04, `QFORM-EIGHT-DIRECTION-TERMINAL-OVERLAP1-COLLAR-v1`, blob `851e0ae9c78a4d9a49f60a1cc5f0026b734579e6`;
2. fleet01/B03, split-row shared-environment determinant theorem, blob `4dc6e469304cffc3afd1b1d5f5d0dba976c818b7`;
3. fleet01/B11, marginal-free E3/E2 receivers and the complete nine-direction reconstruction, blob `b25ece64d7409b420d826c87449b32f51f444f38`.

No post-rotation independence, moment, support, Gaussian, log-concavity, arbitrary-joint coarea, or pointwise rough quadratic-phase decay is used.

## 1. Constants

Normalize the coordinate density caps and spectral threshold to one. Keep

`eta=1/100`, `kappa=1/6400`,

and put

`delta_* = 97/100-(297 sqrt(2)+3 sqrt(202))/4000`

`         =0.8543351401911337710037464...`.

The B04 terminal theorem says that under no `eta`-pivot and `s_8(A)>=1`, either

`V_3(A)>=kappa^3`,

or the two-sided collar obeys

`Xi_2(A)>= (delta_*^2/2) kappa^2
          =8.9097721162769067e-9...`.                                    (1)

The first branch is already paid by the completed marginal-free E3 receiver, with

`||p_Q||_infinity <2400`.

The rest of this note treats the second branch.

## 2. Three-color extraction retains the matched two-sided packet

Color each original coordinate independently and uniformly by the ordered colors `L,M,R`. For every ordered pairwise-disjoint triple `(S,H,T)` of two-element sets, the event

`S subset L, H subset M, T subset R`

has probability `3^-6`. Hence some deterministic partition

`[n]=L disjoint_union M disjoint_union R`

satisfies

`Xi(L,M,R)
 := sum_{H subset M, |H|=2}
      [sum_{S subset L, |S|=2} det A[S,H]^2]
      [sum_{T subset R, |T|=2} det A[H,T]^2]
 >=3^-6 Xi_2(A).`                                                    (2)

For each middle pair `H` set

`L_H=sum_{S subset L, |S|=2} det A[S,H]^2`,

`R_H=sum_{T subset R, |T|=2} det A[H,T]^2`.

Define the literal cross blocks

`B_L=A[L,M]`,  `B_R=A[R,M]`.

Cauchy--Binet gives

`Z_2(B_L)=sum_H L_H`,  `Z_2(B_R)=sum_H R_H`.

Therefore, without selecting a local minor and without paying the number of middle pairs,

`P_*:=Z_2(B_L) Z_2(B_R)
    =(sum_H L_H)(sum_K R_K)
    >=sum_H L_H R_H
    =Xi(L,M,R)`.

Combining this with (1)-(2),

`boxed: P_* >= 3^-6 (delta_*^2/2) kappa^2
             =1.2221909624522506e-11... .`                         (3)

This is the key aggregate step: the matched two-sided collar is spent before any reciprocal local-minor estimate.

## 3. Split-row Fourier endpoint

Use the physical cut

`I=L union R`, `J=M`.

The full quadratic polynomial has the exact original-coordinate form

`Q=F(X_I)+2 X_I^T A[I,M] X_M+G(X_M)`,

where `F` contains every `L-L`, `R-R`, and `L-R` quadratic/affine term and `G` contains every `M-M` term. Thus arbitrary same-bank curvature is retained.

Apply the proved split-row shared-environment determinant theorem with row packets `I_1=L`, `I_2=R`. Both packets use the same difference vector from the middle bank; no independence between them is asserted. It gives

`|phi_Q(t)|
 <= prod_{g=L,R} det(I+t^2 B_g^T B_g/(pi^2 e^2))^(-1/8).`       (4)

Retain the order-two term in each determinant. Since

`det(I+z B_g^T B_g)>=z^2 Z_2(B_g)`,

(4) and `|phi_Q|<=1` imply

`boxed: |phi_Q(t)| <= min(1,U_*/|t|),`                           (5)

where

`U_* = pi e P_*^(-1/8)
     <=197.49312010958636... .`                                  (6)

Equivalently define

`C_*:=U_*/pi <=62.86401258416414... .`                            (7)

The exponent is exactly the critical order-four exponent one. The proof has not collapsed the collar to a scalar half-potential or to a dimension-dependent local reciprocal.

## 4. Every finite L^r norm is uniformly controlled

Let `r>=2` and `q=r/(r-1) in (1,2]`. From (5),

`int_R |phi_Q(t)|^q dt
 <=2 U_* q/(q-1)=2U_* r.`                                        (8)

To avoid assuming a density in advance, convolve the law of `Q` with the manuscript Gaussian approximate identity. Its Fourier transform is `phi_Q(t)e^{-epsilon t^2}`. These transforms converge to `phi_Q` in `L^q`; inverse Hausdorff--Young therefore produces an `L^r` limit density, and weak convergence identifies it with the law of `Q`.

With the manuscript Fourier convention the inverse Hausdorff--Young norm is `(2pi)^(-1/q)`. Hence

`boxed: ||p_Q||_r <= (C_* r)^(1-1/r),   r>=2,`                    (9)

and numerically

`||p_Q||_r <= (62.865 r)^(1-1/r).`                               (10)

Thus the only unpaid normalized `s_8` chamber already has a density in every finite `L^r`, uniformly in dimension and in all rough coordinate laws. This is strictly stronger than the previously recorded half-potential statement, but it is not an `L^infinity` conclusion.

For an interval `J`, Holder gives

`boxed: P{Q in J} <= (C_* r |J|)^(1-1/r),  r>=2.`                (11)

If `x=C_*|J|<=e^-2`, choose `r=log(1/x)>=2`. Since `x r<1`,

`(xr)^(1-1/r)
 =xr exp(log(1/(xr))/r)
 <= e x log(1/x).`

Therefore

`boxed: P{Q in J}
 <= e C_* |J| log(1/(C_*|J|))`                                  (12)

whenever `|J|<=e^-2/C_*=0.00215282603946768...`. The front factor is

`e C_*=170.8821030715541...`.

## 5. Scaled statement and a global s8 finite-r corollary

For general density cap `K` and spectral scale `s`, normalize by `Y=KX` and `A/s` exactly as in the baseline manuscript. Density scaling yields, in the terminal collar,

`boxed: ||p_Q||_r
 <= [C_* r (K^2/s)]^(1-1/r),  r>=2.`                             (13)

The pivot branches of the complete nine-direction proof actually require only `s_8>=s`: a scalar pivot loses one direction and still leaves enough for the pivot or order-two half-potential child; a pair pivot loses at most two and needs still fewer. The no-pivot non-collar branch has the E3 `L^infinity` bound. Consequently one obtains the unconditional finite-r statement

`boxed: s_8(A)>=s
 => p_Q belongs to L^r for every finite r>=2,`

with for example the uniform quantitative envelope

`||p_Q||_r
 <= [max(5338, C_* r) K^2/s]^(1-1/r).`                          (14)

Equation (14) is not asserted optimal; its purpose is to isolate the endpoint, not optimize constants.

## 6. Exact comparison with the opposite-sign rank-two saddle

Let `X,Y` be independent `Unif[-1/2,1/2]`. For

`R=2XY`

one has

`p_R(t)=log(1/(2|t|)),  0<|t|<1/2`,

and therefore, for every finite `r>=1`,

`||p_R||_r^r
 =2 int_0^(1/2) log(1/(2t))^r dt
 =Gamma(r+1).`                                                   (15)

Hence

`||p_R||_r=Gamma(r+1)^(1/r) ~ r/e`,                              (16)

and

`P{|R|<=epsilon}
 =2 epsilon [log(1/(2epsilon))+1]`                               (17)

for `0<epsilon<=1/2`.

Thus the `s_8` collar estimate (9)-(12) lands in exactly the same *functional endpoint class* as the mandatory opposite-sign rank-two logarithmic control example: all finite `L^r` norms with linear-in-r growth, and `epsilon log(1/epsilon)` small balls. The still-missing `s_8` implication is now literally a **logarithm-removal problem**: spend the additional overlap-one currency `Omega_1`/rank-saturation provenance before it is forgotten by (3)-(5), and upgrade the critical `1/|t|` endpoint to `L^1_t` or an equivalent direct linear small-ball bound.

This does not prove the general `s_8` bounded-density theorem and does not prove the unrestricted three-eigenvalue conjecture.

## 7. Designated fleet04/B11 result applied at an actual target inequality

The completed partner theorem `QFORM-LDL-SOURCE-DISJOINT-THIRD-CURVATURE-v1` is source-pinned at

`yspennstate/math-open-problems@494e4a18bff08cc3fbc9ba668ba14a3983e51da6`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B11/20260924T091618Z-fleet04-B11-source-disjoint-ldl-r2/REPORT.md`.

Apply it to independent cap-one original coordinates `X_1,X_2,X_3` and

`Q_0=2X_1X_2+X_3^2`.

The rank-two block is `[[0,1],[1,0]]`, so `D_2=1`; the disjoint third coefficient is `d=1`. The effective matrix has eigenvalues `{1,-1,1}`, hence this is an actual three-large-eigenvalue target family. The partner theorem gives the concrete inequality

`boxed: ||p_(Q_0)||_infinity <=128,  p_(Q_0) in C_0(R).`          (18)

For centered unit uniforms, the first summand `2X_1X_2` alone has the logarithmic density (15). Equation (18) is therefore a literal example of a third source-disjoint curvature direction removing that rank-two logarithm without rotating the independent inputs.

## 8. Remaining implication

The aggregate two-sided collar has now been converted, without dimension loss, to a critical split-row Fourier endpoint. What remains for multiplicity eight is not to prove absolute continuity or finite `L^r` control; those are already available. The missing theorem is a dependence-safe mechanism that uses `Omega_1` or the exact rank-saturated interpolation geometry to gain any integrable improvement over (5), or a direct small-ball argument that turns (12) into `C|J|`.

Full `s_8` L-infinity theorem: OPEN.  
Full three-eigenvalue conjecture: OPEN.  
Global continuity: OPEN/not claimed.
