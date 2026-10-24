SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T17:46:18Z.
attacking: the proposed universal 2/3-moment bound for conditional three-dimensional spectral projection densities, using exact disjoint original-coordinate block geometry.

# QFORM-CONDITIONAL-THREEPROJ-2OVER3-MOMENT-FALSE-v1

Run: `20260922T174618Z-account03-B09-QFORM-r14`  
Worker: `account03/B09` — Bilinear block mechanism  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh prepublication OWNER CONTROL: revision `2026-09-22.10`  
Classification: **REFUTED_INTERMEDIATE_MECHANISM / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

The current owner message proposes the following full-rank route. Choose three spectral coordinates `Y=(Y1,Y2,Y3)` belonging to eigenvalues of modulus at least one, condition on all remaining spectral coordinates `Z`, apply the rank-three coarea estimate

`||p_{Q|Z}||_infinity <= K ||rho_{Y|Z}||_infinity^(2/3)`,

and then seek a universal bound for

`E_Z ||rho_{Y|Z}||_infinity^(2/3)`.                                  (1.1)

This run proves that (1.1) is **not** universally bounded, even for iid unit-density uniforms and even when the target matrix is full rank and has exactly three eigenvalues of modulus at least one. Thus this particular conditional-rank-three completion route cannot prove the full conjecture by taking the conditional `L^infinity` norm before averaging.

This is **not a counterexample to QFORM**. It is a source-valid counterexample to the proposed intermediate conditional-moment bound. The full bounded-density conjecture remains open.

The construction is deliberately blockwise in the original independent coordinates. No post-rotation independence is assumed. In fact the calculation exposes exactly how conditioning destroys the favorable product geometry.

## 2. One-block geometry

Fix an integer `m>=2`. Let

`C_m=[-1/2,1/2]^m`,

and let `X=(X_1,...,X_m)` be uniform on `C_m`, so its coordinates are independent and each density equals one on an interval of length one.

Put

`u=m^(-1/2)(1,...,1)`

and decompose orthogonally

`X=Y u+Z`,  with `Y=<u,X>` and `Z in u^perp`.                         (2.1)

Because this change of variables is orthogonal, the joint density of `(Y,Z)` is simply the indicator of the rotated cube. For fixed `z in u^perp`, the admissible `y` satisfy

`-1/2 <= z_i+y/sqrt(m) <= 1/2` for every `i`.

Therefore the fiber is an interval of length

`ell_m(z)=sqrt(m) [1-(max_i z_i-min_i z_i)]_+`.                       (2.2)

Let

`D_m={z in u^perp: max_i z_i-min_i z_i <=1}`.                         (2.3)

Then the marginal density of `Z` is exactly

`h_m(z)=ell_m(z) 1_{D_m}(z)`,                                        (2.4)

and for almost every `z` with `ell_m(z)>0`, the conditional law of `Y|Z=z` is uniform on that fiber, hence

`||p_{Y|Z=z}||_infinity=ell_m(z)^(-1)`.                              (2.5)

The level sets of the fiber length are homothetic. For `0<=s<=sqrt(m)`,

`{z: ell_m(z)>=s}=(1-s/sqrt(m)) D_m`.                                (2.6)

Indeed `range(cz)=c range(z)` on the linear space `u^perp`. Thus, writing `V_m=vol_{m-1}(D_m)`,

`vol{ell_m>=s}=V_m (1-s/sqrt(m))^(m-1)`.                              (2.7)

Normalization determines `V_m` without any external projection formula. Since the cube has volume one and the orthogonal change of variables has Jacobian one,

`1=int_{D_m} ell_m(z) dz`
` =int_0^{sqrt(m)} vol{ell_m>=s} ds`
` =V_m sqrt(m)/m`.

Hence

`V_m=sqrt(m)`.                                                        (2.8)

For every `alpha>0`, layer cake plus (2.7)-(2.8) yields the exact identity

`I_m(alpha):=int_{D_m} ell_m(z)^alpha dz`
` =alpha m^((alpha+1)/2) B(alpha,m)`.                                (2.9)

The exponent needed below is `alpha=1/3`:

`I_m:=I_m(1/3)`
` =(1/3)m^(2/3) B(1/3,m)`
` =Gamma(4/3) m^(2/3) Gamma(m)/Gamma(m+1/3).`                         (2.10)

An elementary lower bound already proves divergence at the required scale. Restrict the beta integral to `0<=t<=1/m`:

`B(1/3,m)`
` >= (1-1/m)^(m-1) int_0^(1/m) t^(-2/3) dt`
` =3(1-1/m)^(m-1)m^(-1/3)`.

The inequality `log(1-x)>=-x/(1-x)` for `0<x<1` gives

`(1-1/m)^(m-1)>=e^(-1)`,

so

`I_m >= e^(-1) m^(1/3)`.                                             (2.11)

The exact asymptotic is

`I_m ~ Gamma(4/3)m^(1/3)`.                                           (2.12)

## 3. Three independent blocks: the 2/3 conditional moment diverges

Take three independent copies of the preceding block, each of size `m`. Denote their decompositions by

`X^(g)=Y_g u+Z_g`, `g=1,2,3`,

and put

`Y=(Y_1,Y_2,Y_3)`, `Z=(Z_1,Z_2,Z_3)`.                               (3.1)

Because the three physical coordinate blocks are independent, the joint density factors across blocks. Consequently the density of `Z` is

`p_Z(z_1,z_2,z_3)=ell_m(z_1)ell_m(z_2)ell_m(z_3)`,                    (3.2)

while conditioned on `Z=z`, the three `Y_g` are conditionally independent uniforms on their respective fibers. Therefore

`||rho_{Y|Z=z}||_infinity`
` =[ell_m(z_1)ell_m(z_2)ell_m(z_3)]^(-1)`.                           (3.3)

Now average the `2/3` power against the *correct conditioning law* (3.2):

`E_Z ||rho_{Y|Z}||_infinity^(2/3)`
` =int prod_g ell_m(z_g)^(1/3) dz_1 dz_2 dz_3`
` =I_m^3`.                                                           (3.4)

By (2.11),

`boxed{ E_Z ||rho_{Y|Z}||_infinity^(2/3) >= e^(-3) m. }`             (3.5)

Hence the proposed conditional `2/3`-moment has no dimension-free upper bound. More precisely, (2.12) gives

`E_Z ||rho_{Y|Z}||_infinity^(2/3)`
` ~ Gamma(4/3)^3 m`
` =0.7120729426... m`.                                                (3.6)

This is stronger than merely showing that `sup_z ||rho_{Y|Z=z}||_infinity` blows up: the exact weighted moment required by the owner-message Fubini/coarea route itself diverges linearly.

## 4. Embedding into a full-rank target matrix with exactly three large eigenvalues

Let the full original coordinate dimension be `n=3m`. For each block let `P=I_m-uu^T` be the orthogonal projection onto `u^perp`. Fix `epsilon=1/2` and define the real symmetric matrix

`A_m = diag(B_+,B_+,B_-)`,                                           (4.1)

where

`B_+ = (1/2) I_m +(1/2) uu^T`,
`B_- = (1/2) I_m -(3/2) uu^T`.                                      (4.2)

Its spectrum is exactly

`{1,1,-1}` together with `1/2` of multiplicity `3m-3`.               (4.3)

Thus `A_m` is full rank and satisfies the exact owner target hypothesis, with exactly three eigenvalues of absolute value at least one. In the orthogonal spectral coordinates from Sections 2-3,

`Q_m=X^T A_m X`
` =Y_1^2+Y_2^2-Y_3^2 +(1/2)(||Z_1||^2+||Z_2||^2+||Z_3||^2)`.         (4.4)

Conditioning on all `n-3` small-eigenvalue spectral coordinates `Z` therefore gives precisely the owner-message setup: a rank-three form in the three large spectral coordinates plus a constant. Yet its proposed coarea payment is bounded by a quantity proportional to (3.4), and that quantity diverges like `m`.

So the statement

> for every target-valid product law and every choice of three large eigendirections, `E ||rho_{Y|Z}||_infinity^(2/3) <= C`

is false. In fact it is false for this natural canonical choice of the only three large eigendirections in a full-rank target family.

Again, (4.1)-(4.4) do **not** show that `||p_{Q_m}||_infinity` diverges. They show that taking the conditional projection `L^infinity` norm before averaging loses too much product geometry.

## 5. Applying a completed peer result to an actual inequality

The designated partner `account04/B09` still has no completed current-QFORM handoff or canonical QFORM report at the fresh source check, so no result is attributed to that slot. The run proceeds asynchronously as instructed.

A completed compatible peer result is applied quantitatively: account02/B06, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical report

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

Apply that theorem to the three-column matrix whose columns are the blockwise constant unit vectors `u_1,u_2,u_3`. It gives the unconditional three-dimensional spectral projection the uniform bound

`||rho_Y||_infinity <= exp(3/2)`.                                    (5.1)

In this concrete family every physical row has leverage `1/m`, so its sharper product is

`||rho_Y||_infinity`
` <=(1-1/m)^(-3(m-1)/2) <= e^(3/2)`.                                (5.2)

Equations (3.5) and (5.2) exhibit the exact obstruction: the **unconditional** three-dimensional projection remains dimension-free, while the `2/3` moment of its conditional fiber `L^infinity` norm grows at least linearly. This applies the completed peer inequality to the same source-valid family rather than merely citing it.

## 6. Consequence for the proof architecture

The owner-message implication

`rank-3 conditional coarea + universal E ||rho_{Y|Z}||_infinity^(2/3)`

cannot be the missing full-rank bridge. The defect is not merely an unbounded exceptional conditional slice; the conditioning weight is already included in (3.4), and the required moment still diverges.

The replacement must aggregate product structure **before** taking a conditional spectral `L^infinity` norm. This is consistent with the established B09 mechanisms:

1. original-coordinate mixed-Hessian Plancherel for sufficiently large disjoint cross blocks;
2. rank-two half-Riesz payment followed by an untouched physical square;
3. grouped original-coordinate hyperbolic packets;
4. weighted affine-fiber Brascamp--Lieb before curved trace integration.

For the family (4.1), the useful structure is visible before spectral conditioning: it is the direct sum of three independent high-cardinality physical banks. A future full proof needs a bank/ridge/coarea estimate that keeps the conditional fiber mass and curved quadratic integration in one expression, rather than replacing each fiber by its supremum.

A precise next B09 target is:

`QFORM-WEIGHTED-CONDITIONAL-COAREA-WITHOUT-FIBER-SUP-v1`: derive a rank-three coarea/small-ball estimate in which the original product density is integrated jointly over `(Y,Z)` and the residual quadratic shift, and which reduces to a dimension-free bank or ridge estimate on (4.1). Any proposed functional must remain bounded on the exact cube fibers above.

## 7. Verification and status

The accompanying standard-library checker evaluates the exact beta-function formula (2.10), verifies the elementary lower bound (2.11) numerically for representative `m`, and confirms the spectral list of (4.1) analytically by its block eigenvalues. Representative exact-formula values are:

- `m=2`: moment `I_m^3 = 1.6875`;
- `m=8`: `5.9405271926`;
- `m=32`: `23.0253400127`;
- `m=128`: `91.3831063891`;
- asymptotic ratio `I_m^3/m -> Gamma(4/3)^3 = 0.7120729427...`.

**What is proved:** the universal conditional three-projection `2/3`-moment bound proposed as the full-rank gap is false, even for iid unit-cube inputs and full-rank matrices with exactly three large eigenvalues.

**What is not proved:** no target-level counterexample; no unrestricted bounded-density theorem; no continuous-density theorem for the full target.

The unrestricted QFORM conjecture remains **OPEN**.
