SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T10:05:34Z.
attacking: the indefinite two-dimensional cross-kernel left by fleet03/B01, using product-preserving L^4 square-phase control rather than an arbitrary-joint planar shell bound.

# Coordinate-separable cross-kernel smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T100534Z-fleet02-B01-qform`  
Classification: `PROVED SUPPORTING TARGET-LEVEL ANALYTIC THEOREM + REFUTED INTERMEDIATE EXTENSION / FULL QFORM OPEN`  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The full target remains open: for every dimension, arbitrary independent real probability densities bounded by one, and every real symmetric coefficient matrix with at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of the quadratic form, or give a valid counterexample. No moments, support, Gaussian/log-concavity, connected-support, diagonal-basis or post-rotation independence hypotheses are added.

The phase-aligned-density correction remains in force. There is no law-uniform scalar pointwise estimate `|E exp(isX^2)| <= C|s|^{-1/2}`. The mechanism below is instead an integrated `L^4(dt)` estimate for one ORIGINAL coordinate, then an `L^2(dt)` estimate for two independent ORIGINAL coordinates, followed by two-dimensional Plancherel on a separate product bank.

Fresh inputs used at equations:

* Claude/Fourier source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`. In particular Theorem H is applied in Section 6, and D/D5 are checked on an actual rank-two packet.
* Current volume-stability source: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. It explicitly leaves rank-two cross blocks plus an arbitrarily small third direction unpaid.
* Designated partner fleet03/B01: `yspennstate/math-open-problems@dde65d9e08434761ec633e1acc3865fb9ad05941`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T083025Z-auto11/REPORT.md`. Its theorem pays a rank-two cross packet when the two-dimensional cross-kernel curvature is definite, with constant `3(pi/2)^(1/3) Delta^(-1/3)d2^(-1/6)`.

## 2. Scalar product-preserving L^4 square-phase lemma

### Lemma 2.1

Let `X` have a probability density `f<=1`. For every `a!=0`, `ell,c in R`, put

`F(t)=E exp(it(aX^2+ell X+c))`.

Then

`boxed: integral_R |F(t)|^4 dt <= 27 pi/(2|a|).`                 (2.1)

The bound is uniform in the affine term.

### Proof

Complete the square and translate the density, so it suffices to consider `aY^2` with a translated cap-one density. Let `h` be the density of `Y^2`. For `w>0`,

`h(w)=[f(sqrt w)+f(-sqrt w)]/(2 sqrt w) <= w^(-1/2)`.

Therefore

`integral h^(4/3) <= integral h(w) w^(-1/6) dw = E|Y|^(-1/3).`   (2.2)

Among cap-one probability densities, the last expectation is maximised by filling the measure-one set nearest the singularity (the one-dimensional bathtub/rearrangement principle), hence

`E|Y|^(-1/3) <= integral_(-1/2)^(1/2) |y|^(-1/3)dy = 3*2^(-2/3).` (2.3)

With Fourier convention `hat h(s)=integral exp(-isw)h(w)dw`, interpolation between `L^1->L^infinity` and Plancherel gives Hausdorff-Young

`||hat h||_4 <= (2pi)^(1/4)||h||_(4/3).`                          (2.4)

Thus

`integral |hat h|^4 <= 2pi (3*2^(-2/3))^3 = 27pi/2.`             (2.5)

Finally `F(t)` is a unimodular constant times `hat h(-at)`, so scaling gives (2.1). QED.

### Corollary 2.2 — two independent coordinate squares

If `Z1,Z2` are independent cap-one coordinates and `a,c!=0`, then for arbitrary linear terms

`G(t)=E exp(it[aZ1^2+cZ2^2+l1Z1+l2Z2])`

satisfies

`boxed: integral_R |G(t)|^2 dt <= (27pi/2)|ac|^(-1/2).`          (2.6)

Indeed the expectation factors into the two scalar factors and Cauchy-Schwarz in `t` uses (2.1) twice. The signs of `a,c` are irrelevant. In particular (2.6) covers the indefinite separable kernel `ac<0` without any scalar pointwise decay statement.

## 3. Why arbitrary-joint planar L^2 is false in the indefinite case

A tempting extension of the fleet03/B01 definite planar-shell lemma would replace the two original product coordinates above by an arbitrary joint density cap. That is false even at fixed determinant.

Take `q(x,y)=xy`, `R>e`, and `delta=1/log R`. Let

`E_R={(x,y): 1<=x<=R, 0<=y<=delta/x}`, `rho_R=1_(E_R)`.

Then `rho_R<=1` and

`|E_R|=delta integral_1^R dx/x=1`.

For `0<s<delta`, the pushforward density of `s=xy` is exactly

`g_R(s)=integral_1^R dx/x=log R`,

because `y=s/x` has Jacobian `1/x`. Hence

`boxed: ||g_R||_2^2=(log R)^2 delta=log R -> infinity.`           (3.1)

The symmetric matrix of `xy` has determinant `-1/4`, fixed. Therefore no estimate of the form

`integral |E_rho exp(it z^T H z)|^2 dt <= C |det H|^(-1/2)`

can hold for arbitrary cap-one joint planar densities when `H` is indefinite. This is NOT a QFORM counterexample: `rho_R` is a dependent joint density and need not arise from two original independent coordinates. It is an obstruction to extending the definite-kernel proof by forgetting product provenance.

## 4. Main theorem

Split ORIGINAL coordinates as

`P={p1,p2}`, `Z={z1,z2}`, `J`, `W`,

all disjoint. Condition on `X_W=w`. Suppose the remaining quadratic polynomial has the form

`Q_w = U^T B U + 2 U^T C Z + a Z1^2 + c Z2^2 + 2 U^T K Y + L_w(U,Z) + G_w(Y)`, (4.1)

where `U=(X_p1,X_p2)`, `Z=(X_z1,X_z2)`, `Y=X_J`; `B` and `C` are arbitrary; `L_w` is affine in `(U,Z)`; `G_w` is arbitrary measurable real-valued; and

`a c !=0`, `rank K=2`.                                               (4.2)

Equivalently at the matrix level, the two cross-kernel rows are coordinate-aligned:

`A[Z,J]=0`, `A[Z,Z]=diag(a,c)`, `K=A[P,J]`.                         (4.3)

Put

`Delta=sigma_1(K)sigma_2(K)>0`.                                    (4.4)

### Theorem 4.1 — `QFORM-RANK2-CROSS-COORD-SEPARABLE-KERNEL-L2-v1`

Under (4.1)-(4.4), the full ambient quadratic form has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <= (9/2) Delta^(-1/3)|ac|^(-1/6).`       (4.5)

All `P-P`, `P-Z`, `J-J`, outside couplings and affine terms are retained. The theorem does not require the kernel signs to agree; the intended new branch is `ac<0`, where fleet03/B01's definite-kernel theorem does not apply.

### Proof

Fix `w`. Let `m(u)=f_p1(u1)f_p2(u2)`, so `0<=m<=1` and `integral m=1`. After integrating the two original `Z` coordinates define

`h_(t,w)(u)=m(u) exp(it q_w(u)) E_Z exp(it[aZ1^2+cZ2^2+l_1(u,w)Z1+l_2(u,w)Z2])`. (4.6)

Corollary 2.2 is uniform in the linear terms, so

`integral_R |h_(t,w)(u)|^2 dt <= m(u)^2 (27pi/2)|ac|^(-1/2).`     (4.7)

Set `A_w(t)=||h_(t,w)||_(L^2(du))`. Tonelli and `integral m^2<=integral m=1` give

`||A_w||_2 <= sqrt(27pi/2)|ac|^(-1/4).`                            (4.8)

Average over `W` and put `A(t)=E_W A_w(t)`; Minkowski preserves the same bound.

Now retain the untouched original-product `J` bank. Put `L=2K Y`. The standard two-dimensional product-projection estimate gives

`||p_(KY)||_infinity <= 2/Delta`, hence `||p_L||_infinity <=1/(2Delta)`. (4.9)

Disintegrating the arbitrary phase `exp(itG_w(Y))` over `L` produces a complex density `eta_(t,w)(l)` with `|eta|<=p_L`; therefore

`||eta_(t,w)||_2 <= (2Delta)^(-1/2).`                              (4.10)

The cross phase is `exp(it u.l)`. Cauchy-Schwarz in `l` and two-dimensional Plancherel in the ORIGINAL `U` coordinates give, for `t!=0`,

`|phi_w(t)| <= sqrt(2) pi Delta^(-1/2)|t|^(-1) A_w(t).`           (4.11)

Averaging `w`, using `|phi_Q(t)|<=1`, and applying Cauchy-Schwarz on `|t|>T` yields

`integral_R |phi_Q(t)|dt
 <= 2T + 2pi sqrt(27pi/2) Delta^(-1/2)|ac|^(-1/4) T^(-1/2).`      (4.12)

Let

`B0=2pi sqrt(27pi/2) Delta^(-1/2)|ac|^(-1/4)`.

The minimum of `2T+B0 T^(-1/2)` is `6(B0/4)^(2/3)`. Fourier inversion therefore gives

`||p_Q||_infinity <= (3/pi)(B0/4)^(2/3)`
` = (3/pi)[(pi/2)sqrt(27pi/2)]^(2/3) Delta^(-1/3)|ac|^(-1/6)`
` = (9/2) Delta^(-1/3)|ac|^(-1/6).`                              (4.13)

Thus `phi_Q in L^1`, which also supplies the asserted continuous `C_0` representative. QED.

Scaling check: under `A -> lambda A`, `Delta -> lambda^2 Delta` and `ac -> lambda^2 ac`, so the right side scales by `|lambda|^(-1)` exactly.

## 5. A strict-N3 target family paid uniformly

Let `N` be a large Sylvester-Hadamard order. Choose two orthonormal Hadamard rows `v1,v2 in R^N`, so every coordinate has `v1(j)^2+v2(j)^2=2/N`. Fix `0<epsilon<=1/4`, set

`sigma=epsilon^(-1/2)`, `K=sigma [v1^T;v2^T]`,                  (5.1)

and let the leaf self-curvature be the full-rank dense matrix

`C_N = (epsilon/sqrt(N)) H_N/sqrt(N) = epsilon H_N/N`,          (5.2)

where `H_N H_N^T=N I`; hence `||C_N||op=epsilon/sqrt(N)` and every entry has magnitude `epsilon/N`.

On the ORIGINAL coordinates `(U1,U2,Z1,Z2,Y_1,...,Y_N)`, take

`A_(epsilon,N)=
 [[0_2, 0, K],
  [0, diag(epsilon,-epsilon), 0],
  [K^T,0,C_N]].`                                                (5.3)

The theorem has

`Delta=sigma^2=epsilon^(-1)`, `|ac|=epsilon^2`,

so

`boxed: ||p_(X^T A_(epsilon,N) X)||_infinity <= 9/2`             (5.4)

for every cap-one product input law, uniformly in `epsilon,N`.

This is target-valid. With `C_N=0`, the nonzero spectrum is exactly `{sigma,sigma,-sigma,-sigma,epsilon,-epsilon}`. Adding `C_N` changes every eigenvalue by at most `epsilon/sqrt(N)`. Since `sigma>=2`, at least four eigenvalues retain modulus greater than one.

It is also strict-N3 at every fixed threshold `tau in (0,1]` after choosing `epsilon` and then `N` sufficiently. All physical diagonals are at most `max(epsilon,epsilon/N)=epsilon`. The physical pair determinants have the following bounds:

* `Z1,Z2`: `epsilon^2`;
* hub-leaf: at most `sigma^2/N=1/(epsilon N)`;
* kernel-leaf: at most `epsilon^2/N`;
* leaf-leaf: at most `2epsilon^2/N^2`;
* all remaining center pairs: zero.

Thus choose `0<epsilon<min(1/4,tau)` and then `N>1/(epsilon tau)` (and larger if needed for the displayed leaf bounds). Then every physical diagonal and every physical pair determinant is smaller than `tau`, while the three-large-eigenvalue hypothesis still holds.

The dense leaf term in (5.2) is not discarded as a small random perturbation; it stays inside the arbitrary `G_w(Y)` phase of Theorem 4.1. This is exactly the product-preserving type of robustness needed under unbounded input supports.

## 6. Required newest-source and partner applications

### 6.1 Claude Theorem H on an actual subfamily

Set `C_N=0` in (5.3), take the two `U` coordinates as the hub set `H`, the `N` leaf coordinates as `I`, and the two `Z` coordinates as the conditioned/arbitrary block `J`. In Claude's Theorem H, `r=0`,

`G~=K K^T=sigma^2 I_2`,

and every leaf leverage is exactly `2/N<=1/2` for `N>=4`. Hence

`|phi(t)| <= 4pi^2 sigma^(-2)|t|^(-2)`

and integration gives the actual inequality

`boxed: ||p_Q||_infinity <= 4/sigma = 4 sqrt(epsilon).`          (6.1)

On the natural four-center-versus-leaf packet the cross block has rank two, so `e_3(K^T K)=e_5(K^T K)=0`: Theorem D/D' and D5 do not pay that packet. Equation (6.1) is the source's genuinely joint two-hub averaged-frequency exit. Restoring the full-rank dense leaf phase (5.2) leaves Theorem 4.1 valid without treating that phase as a law-small perturbation.

### 6.2 Designated partner fleet03/B01 on the definite sibling

Replace `diag(epsilon,-epsilon)` in (5.3) by `diag(epsilon,epsilon)`. The four-center-to-leaf cross block still has

`Delta=epsilon^(-1)`,

while the restriction of the center quadratic block to `ker K^T=span(Z1,Z2)` is definite with

`d2=epsilon^2`.

The completed fleet03/B01 theorem therefore gives

`boxed: ||p_Q||_infinity <= 3(pi/2)^(1/3)<3.488`,                (6.2)

uniformly in `epsilon,N`, with the same arbitrary dense leaf curvature retained. Equation (6.2) is an actual application of the designated partner result. The new theorem (4.5) supplies the coordinate-separable indefinite sibling, where the partner's definiteness hypothesis fails, at constant `9/2`.

## 7. What changed and what remains

This run pays a concrete part of `QFORM-RANK2-KERNEL-SIGNATURE-ROUTING-v1`: an exact rank-two cross packet whose two-dimensional cross-kernel is an ORIGINAL coordinate pair with separable nonzero quadratic curvature, including the indefinite and near-null regime after compensating cross scale. It also proves that the tempting arbitrary-joint indefinite planar `L^2` replacement is false, so any further extension must preserve more of the original product source.

The first unpaid implication is now

`QFORM-RANK2-INDEFINITE-KERNEL-PRODUCT-ROUTING-v1`:

in the remaining strict-N3 low-cross-rank state, either route to a coordinate/grouped-product two-dimensional kernel on which a product-preserving analogue of Lemma 2.1 can be spent, route to fleet03/B01's definite-kernel packet, or route to an already-paid volume/hub/ridge/pair/grouped-square/exact-null branch. The hard unresolved case is an indefinite or nearly singular two-dimensional cross-kernel whose basis is genuinely mixed across the same original coordinates, so the kernel variables are dependent after rotation and the arbitrary-joint L^2 statement is false by Section 3.

Full QFORM is not proved or disproved. No two independent end-to-end reviews exist for a full candidate.
