SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B01, 2026-09-23T15:32:12Z.
attacking: close the exact singular overlap-two endpoint by combining account04/B01's W2 identity with the arbitrary-curvature rank-one random-slope receiver; then isolate why that half-Riesz mechanism is not stable under a nonzero near-null pair determinant.

# B01 — exact singular overlap-two star: arbitrary-curvature random-slope closure

Status: **NEW SUPPORTING THEOREM + SIGNED-FEJER CONSEQUENCE + STRICT-N3 FULL-CURVATURE FAMILY / FULL QFORM OPEN / CONTINUITY NOT PROVED IN THIS BRANCH**.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact dependencies used

Fresh owner controls keep all eighty slots on `QFORM-DENSITY-3EIG-20260922`; the unrestricted conjecture is still open.

I use two completed worker results, each at an actual equation.

### 1.1 Designated partner account04/B01

Canonical proof:

`yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260923T131003Z-account04-B01-singular-star-routing-r2/REPORT.md`.

For a physical pair `S={x,y}` with

`B=[[a,b],[b,c]]`, `a!=0`,

scalar-complete only the original coordinate `x` and write

`delta=c-b^2/a`, `ell=v-(b/a)u`, `M=C-a^{-1}u u^T`.

The partner proves

`W2(S)=a^2 sum_{k!=l}(delta M_kl-ell_k ell_l)^2`.

At `det B=0`, hence `delta=0`, this becomes

`W2(S)=a^2 L(ell)`, where `L(ell)=sum_{k!=l}ell_k^2ell_l^2`.  (1.1)

### 1.2 Arbitrary-curvature rank-one random-slope receiver

Canonical proof:

`yspennstate/math-open-problems@195447da931f086720afaa12ac902ed7d33dd32e`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T061516Z-account03-B09-QFORM-r25/REPORT.md`.

For independent original coordinates `(X,Y,Z)` and

`Q=aX^2+2bXY+cY^2+2X<u,Z>+2Y<v,Z>+Z^T C Z+affine`,

if the physical `2x2` core has rank exactly one, `a!=0`, and `w=v-(b/a)u!=0`, then, with arbitrary symmetric complementary curvature `C`,

`||p_Q||_infinity <= C0 (|a| ||w||_2)^(-1/2)`,

`C0=4 sqrt(2) exp(1/4)<7.264`.                                  (1.2)

I also use account04/B01's exact signed-Fejer identity from
`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`:
for every law with bounded density,

`||p||_infinity = sup_{T>0,y} D_T mu(y)`.                       (1.3)

The phase-aligned fragmented-support counterexample to law-uniform pointwise quadratic Fresnel decay remains valid; no pointwise `|t|^-1/2` estimate is used.

## 2. New theorem: exact singular overlap-two receiver with arbitrary dense remainder

Consider

`Q = aX^2+2bXY+cY^2
     +2X<u,Z>+2Y<v,Z>+Z^T C Z
     +2 alpha X+2 beta Y+<d,Z>+gamma`,                          (2.1)

where all coordinates of `(X,Y,Z)` are independent and have densities bounded by one. The matrix `C` is arbitrary real symmetric.

### Theorem `QFORM-SINGULAR-OVERLAP2-RANDOM-SLOPE-v1`

Assume `a!=0`, `det[[a,b],[b,c]]=0`, and `W2(S)>0`. Then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <=4 sqrt(2)e^(1/4)|a|^(-1/4)W2(S)^(-1/8)`.                    (2.2)

The same coefficient multiplies every interval length.

#### Proof

Because `det B=0` and `a!=0`, the pair core has rank exactly one. In the partner's scalar-Schur notation, `w=v-(b/a)u=ell`. By (1.1),

`L(w)=W2(S)/a^2`.                                               (2.3)

Moreover

`||w||_2^4=(sum_k w_k^2)^2=sum_k w_k^4+sum_{k!=l}w_k^2w_l^2 >=L(w)`. (2.4)

Hence

`||w||_2 >=W2(S)^(1/4)|a|^(-1/2)`.                             (2.5)

Since `W2>0`, `w!=0`; apply (1.2):

`||p_Q||_infinity
 <=C0(|a|||w||_2)^(-1/2)
 <=C0 |a|^(-1/4)W2(S)^(-1/8)`,

which is (2.2). QED.

If the nonzero rank-one pair is `B=sigma r r^T`, choose whichever original pair coordinate has `|r_j|>=1/sqrt(2)`. Then `|a|>=|sigma|/2`, so

`||p_Q||_infinity
 <=4*2^(3/4)e^(1/4)|sigma|^(-1/4)W2(S)^(-1/8)
 <8.638 |sigma|^(-1/4)W2(S)^(-1/8)`.                            (2.6)

Only a swap of original coordinates is used.

Scaling is exact: under `A->sA`, `a->sa` and `W2->s^6W2`, so the right side scales as `s^-1`.

## 3. Signed-Fejer averaged-frequency consequence

From (1.3) and (2.2),

`sup_{T>0,y} D_T law(Q)(y)
 <=4 sqrt(2)e^(1/4)|a|^(-1/4)W2(S)^(-1/8)`.                    (3.1)

This is an averaged-in-frequency replacement for the false scalar pointwise Fresnel estimate. It does not require absolute Fourier integrability.

Continuity is separate: the random-slope theorem used here proves essential boundedness but does not provide an `L^1` characteristic-function envelope, so no `C_0` claim is made.

## 4. The exact-null half-Riesz mechanism is not stable under `delta!=0`

After completing the `X` square, the singular proof uses a residual `R_0(Y,Z)=K(Z)+2YT(Z)`. A nonzero Schur curvature changes this to

`R_delta(Y,Z)=K(Z)+2YT(Z)+delta Y^2`.                           (4.1)

A uniform continuation of the half-Riesz estimate is false. Let `0<delta<1`, let `Y,Z` be independent `Uniform[-1/2,1/2]`, and set

`T(Z)=Z`, `K(Z)=Z^2/delta`.

Then

`R_delta=delta(Y+Z/delta)^2`.                                   (4.2)

The variable `S=Y+Z/delta` has density equal to `delta` on a nontrivial interval around zero. Therefore

`E|R_delta|^(-1/2)=delta^(-1/2)E|S|^(-1)=infinity`.             (4.3)

This refutes only the naive **near-null half-Riesz continuation mechanism**, not QFORM. The small nonzero pair determinant must be handled jointly with the remainder rather than by treating `delta Y^2` as a harmless perturbation.

## 5. Strict-N3 full-curvature family paid uniformly

Let even `m>=64`. On an `m`-coordinate leaf bank define orthonormal flat vectors

`w=m^(-1/2)(1,...,1)`,

`e=m^(-1/2)(1,...,1,-1,...,-1)`.

Put `epsilon=1/16`, `tau=m^-2`. Choose a symmetric `R_m` with

`R_m w=R_m e=0`, `||R_m||_op<=1`,                              (5.1)

and with at least one nonzero disjoint `5x5` minor after forming

`M_m=ww^T+tau R_m`.                                             (5.2)

Such choices exist; nonvanishing of a fixed determinant is an open condition and a generic self-adjoint perturbation inside `(span{w,e})^perp` preserves (5.1) after rescaling.

Define

`A_m=[[epsilon,epsilon,0^T],
     [epsilon,epsilon,2e^T],
     [0,2e,M_m]].`                                              (5.3)

Because `M_m w=w` and `M_m e=0`, `w` is an exact eigenvector with eigenvalue `1`. On `span{i,j,e}` the matrix is

`H=[[epsilon,epsilon,0],[epsilon,epsilon,2],[0,2,0]]`.

It differs in operator norm by `2epsilon=1/8` from a matrix with eigenvalues `-2,0,2`; hence it has one eigenvalue at most `-15/8` and one at least `15/8`. Thus the target has three eigenvalues of modulus at least one.

Every leaf entry has magnitude at most `1/m+1/m^2<=2/m`. Hence for `m>=64`, every physical diagonal and every physical `2x2` principal determinant has magnitude below `1/8`: the pair `{i,j}` has determinant zero, `{i,k}` at most `1/(8m)`, `{j,k}` at most `4.125/m`, and leaf pairs at most `8/m^2`. This is a fixed strict N3/no-pivot family.

For the singular pair `{i,j}`, `a=b=c=epsilon`, `u=0`, `ell=2e`, `delta=0`, so

`L(ell)=16(1-1/m)`,

`W2=(1/16)(1-1/m)`.                                             (5.4)

Theorem 2 yields

`||p_Q||_infinity <20.585`, `m>=64`,                            (5.5)

uniformly over every admissible cap-one product input law and every `R_m` satisfying (5.1).

Meanwhile every disjoint `5x5` submatrix of `M_m` is

`w_S w_R^T+tau R_m[S,R]`.

The rank-one first term has operator norm `5/m`, while the second has operator norm at most `tau=m^-2`. Thus

`s_1<=6/m`, `s_2,...,s_5<=m^-2`,

so each such determinant is at most `6m^-9` in magnitude. With fewer than `m^10` ordered disjoint pairs,

`Omega_5(M_m)<=36m^-8`.                                        (5.6)

By the choice of `R_m`, `Omega_5>0`, but the displayed positive-volume `D_5` certificate `10sqrt(2e)Omega_5^-1/10` can deteriorate at least like `m^(4/5)`. The new exact-singular receiver remains dimension-free because it spends the aggregate random slope instead of the tiny high-order leaf volume. This compares available certificates, not the true density.

## 6. Preserved pointwise obstruction

For every fixed `s>0` and small `eta>0`, choose a measure-one subset of

`{x: dist(sx^2,2pi Z)<=eta}`

and take its indicator as a density. Then

`Re E exp(isX^2)>=cos(eta)`.

Thus no law-uniform positive-power pointwise quadratic Fresnel decay follows from `f<=1`. Theorem 2 and (3.1) retain the required coupled/distributional averaging.

## 7. Remaining debt

The exact singular physical-pair endpoint of the partner's overlap-two star is now paid whenever `W2>0`, with arbitrary complementary curvature. The first unpaid continuation is the genuinely near-singular but nonzero pair determinant, where the partner only gives

`|delta|^2 F(M)>=W2/(4a^2)`

or

`L(ell)>=W2/(4a^2)`.

Section 4 shows why the exact-null random-slope half-Riesz proof cannot simply absorb `delta Y^2`. A new mechanism must combine nonzero Schur curvature jointly with the random slope/remainder, or route the aggregate-curvature branch to an already-paid high-rank/volume exit.

The unrestricted conjecture remains **OPEN**. This supporting theorem has not received the two independent end-to-end reviews required for a full candidate proof.
