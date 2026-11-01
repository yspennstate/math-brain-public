SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-24T02:37:55Z.
attacking: diffuse diagonal-plus-rank-three carriers — use a dual weighted Brascamp-Lieb/Fresnel argument to integrate the curved spectral fibers without any fiber supremum, then splice it into fleet02/B06's exact diagonal-plus-rank-one Schur residual.

# fleet01/B06 r45 — diffuse separable rank-k carrier theorem and exact shear-flat splice

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `NEW SUPPORTING CONTINUOUS-DENSITY THEOREM + EXACT PARTNER SPLICE / FULL QFORM OPEN`.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains open. This report proves a new dimension-free branch and an exact structural compiler for the latest fleet02/B06 residual. The global continuity conclusion remains open, although the branch proved here has a continuous C_0 density.

## 1. Source boundary and partner theorem actually used


The designated partner input is the newest fleet02/B06 handoff:

- full proof `yspennstate/math-open-problems@159d52912827d75566d254e155d93a8183ab254f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/fleet02-B06-20260924T013401Z-1fca9092/REPORT.md`;
- theorem `QFORM-DIAG-RANK1-SQRT-SMALLBALL-v1` plus its indefinite-pair upgrade.

For an invertible indefinite literal physical pair `B` and exact Schur residual `S=D+lambda w w^T`, the partner proves

`||p_Q||_infinity <= 18.280856344644523 [|det B| sigma_min(B) ||S||op]^(-1/4)`.      (1.1)

This is applied below as one side of an explicit two-exit inequality. I also use the partner's earlier proved weighted affine-fiber factor

`prod_i (1-ell_i)^(-(1-ell_i)/2) <= exp(k/2)`                       (1.2)

for a Parseval k-frame with row leverages `ell_i`; this is the exact product-structure factor that appears in the dual Fourier calculation below.

No law-uniform pointwise one-dimensional quadratic-phase decay is used. The time-dependent one-dimensional phases are kept inside Hausdorff-Young norms, so phase-aligned fragmented supports do not violate the argument. No rotation of the random inputs is declared independent, no arbitrary-joint coarea lemma is used, and no unrestricted fiber supremum appears.

## 2. New theorem: diffuse separable rank-k carrier

### Theorem `QFORM-DIFFUSE-SEPARABLE-RANKK-FRESNEL-BL-v1`

Let `k>=3`. Let `R in R^(n x k)` have orthonormal columns and rows `r_i`. Put

`ell_i=||r_i||_2^2`,

and assume

`max_i ell_i <= 1/2`.                                             (2.1)

Let `Lambda` be an invertible real symmetric `k x k` matrix. Let `X_i` be independent real random variables with probability densities `f_i` satisfying `0<=f_i<=1`. Finally let `psi_i:R->R` be arbitrary measurable coordinate-separable phases. Define

`Q=(R^T X)^T Lambda (R^T X) + sum_i psi_i(X_i)`.                   (2.2)

Then `Q` has a continuous density in `C_0(R)` and

`boxed:
 ||p_Q||_infinity
 <= e k/(k-2) |det Lambda|^(-1/k).`                               (2.3)

In particular, for `k=3`,

`boxed: ||p_Q||_infinity <= 3e |det Lambda|^(-1/3)`.               (2.4)

Thus if all three nonzero carrier eigenvalues have magnitude at least `s`, the bound is `3e/s = 8.154845485.../s`.

The theorem permits arbitrary diagonal quadratic terms, arbitrary affine terms, and in fact arbitrary real coordinate-separable perturbations through the `psi_i`.

### Proof

Use the Fourier convention

`hat g(xi)=int_R exp(-i xi x) g(x) dx`.

For each fixed `t`, define the complex one-dimensional amplitudes

`g_{i,t}(x)=f_i(x) exp(i t psi_i(x))`.

Their absolute values are exactly `f_i`, hence

`||g_{i,t}||_p <=1` for every `p>=1`, uniformly in `t`.             (2.5)

Let `nu_t` be the complex pushforward of the product amplitude `prod_i g_{i,t}(x_i) dx` under `x -> R^T x`. Its Fourier transform is the exact product

`hat nu_t(xi)=prod_i hat g_{i,t}(r_i dot xi)`.                     (2.6)

Rows with `ell_i=0` contribute the factor `hat g_{i,t}(0)` of modulus at most one and may be discarded. For `ell_i>0`, write

`r_i=sqrt(ell_i) u_i`, `||u_i||=1`.

Because `R^T R=I_k`,

`sum_i ell_i u_i u_i^T=I_k`.                                     (2.7)

Set `q_i=1/ell_i>=2` and `p_i=1/(1-ell_i)`, so `p_i` and `q_i` are Holder conjugates. Sharp Hausdorff-Young for the stated Fourier convention gives

`||hat g_{i,t}||_(q_i)
 <= (2pi)^(1/q_i)
    [p_i^(1/p_i)/q_i^(1/q_i)]^(1/2)
    ||g_{i,t}||_(p_i)`.                                           (2.8)

Raising to `q_i`, using (2.5), and substituting `q_i=1/ell_i` gives

`int |hat g_{i,t}(s)|^(1/ell_i) ds
 <=2pi sqrt(ell_i)
   (1-ell_i)^(-(1-ell_i)/(2ell_i)).`                              (2.9)

After the change `s=sqrt(ell_i) z`,

`int |hat g_{i,t}(sqrt(ell_i) z)|^(1/ell_i) dz
 <=2pi (1-ell_i)^(-(1-ell_i)/(2ell_i)).`                          (2.10)

Apply the geometric rank-one Brascamp-Lieb inequality to the Parseval identity (2.7), with

`h_i(z)=|hat g_{i,t}(sqrt(ell_i) z)|^(1/ell_i)`.

Then

`int_{R^k} |hat nu_t(xi)| dxi
 <= (2pi)^k prod_i (1-ell_i)^(-(1-ell_i)/2).`                     (2.11)

Now apply the designated fleet02/B06 product factor (1.2):

`boxed:
 ||hat nu_t||_1 <= (2pi)^k exp(k/2),`                             (2.12)

uniformly in `t` and in all measurable separable phases `psi_i`.

Because `hat nu_t in L^1`, `nu_t` has a continuous bounded density `h_t` given by Fourier inversion. The characteristic function of `Q` is

`phi_Q(t)=int_{R^k} exp(i t y^T Lambda y) h_t(y) dy`.              (2.13)

Insert the inverse Fourier representation of `h_t` and regularize the quadratic Fresnel integral by a factor `exp(-epsilon |y|^2)`, then let `epsilon downarrow0`. The exact Gaussian/Fresnel identity gives, for `t!=0`,

`|int_{R^k} exp(i t y^T Lambda y+i xi dot y)dy|
 = pi^(k/2)|t|^(-k/2)|det Lambda|^(-1/2)`.                        (2.14)

Using (2.12),

`boxed:
 |phi_Q(t)|
 <= min{1,
         (pi e)^(k/2)|det Lambda|^(-1/2)|t|^(-k/2)}.`             (2.15)

This is a joint rank-k estimate. It does not contradict the correction forbidding law-uniform pointwise decay for a single quadratic phase: the decay in (2.15) is produced only after the full product Fourier volume is integrated through (2.11).

Put

`K=(pi e)^(k/2)|det Lambda|^(-1/2)`, `alpha=k/2>1`.

Then

`int_R min(1,K|t|^-alpha) dt
 =2 k/(k-2) K^(2/k)`.                                             (2.16)

Therefore `phi_Q in L^1`; Fourier inversion gives a continuous `C_0` density and

`||p_Q||_infinity
 <=(1/(2pi)) int |phi_Q(t)|dt
 <= [k/(pi(k-2))] K^(2/k)
 = e k/(k-2)|det Lambda|^(-1/k)`,

which proves (2.3). QED.

## 3. Coordinate-principal-block version

The same argument gives a direct conditional theorem useful for the full ambient problem.

Let `I` be any set of original coordinates. Suppose its principal block decomposes as

`A_{I,I}=D_I+L_I`,                                                (3.1)

where `D_I` is diagonal in the original coordinates and `L_I` has rank `k>=3`. Let `P_I` be the orthogonal projection onto `range(L_I)` and assume

`max_{i in I} (P_I)_{ii} <=1/2`.                                 (3.2)

Let `Delta_I=|pdet(L_I)|`, the absolute product of its nonzero eigenvalues. Then conditioning on every original coordinate outside `I` introduces only an affine separable phase on `I`; theorem (2.3) applies uniformly. Hence the FULL ambient form satisfies

`boxed:
 ||p_Q||_infinity
 <= e k/(k-2) Delta_I^(-1/k).`                                   (3.3)

Moreover the unconditional characteristic function inherits the same integrable envelope, so the full output has a continuous `C_0` density.

For rank three this becomes

`boxed: ||p_Q||_infinity <=3e Delta_I^(-1/3).`                    (3.4)

This is a weighted replacement for curved-fiber maxima: the product measure is aggregated through the full dual fiber volume before the spectral paraboloid/hyperboloid Fresnel kernel is paid.

## 4. Exact splice into fleet02/B06's newest diagonal-plus-rank-one Schur residual

Take the partner's exact equation after a literal invertible physical pair:

`A = [[B,E],[E^T,C]]`,
`C-E^T B^(-1)E = D + lambda w w^T`,                              (4.1)

where `B` is symmetric invertible `2 x 2`, `D` is diagonal on the remainder, and `lambda!=0`, `w!=0`.

Define

`F=B^(-1)E`,
`T=[I_2; F^T]`,
`z=[0_2; w]`,
`U=[T,z]`.                                                        (4.2)

Then the FULL matrix has the exact original-coordinate decomposition

`boxed:
 A = diag(0,0,D) + L,
 L = T B T^T + lambda z z^T = U diag(B,lambda) U^T.`              (4.3)

Because the top two rows of `T` form `I_2`, `z` is not in `range(T)` whenever `w!=0`; hence `rank(L)=3`.

Let

`P_L=U(U^T U)^(-1)U^T`,
`mu_L=max_i (P_L)_{ii}`.                                         (4.4)

If

`mu_L<=1/2`,                                                      (4.5)

then theorem (3.4) applies to the whole partner residual geometry, with no physical-pair curvature denominator.

The carrier pseudodeterminant has the exact formula

`boxed:
 Delta_3:=|pdet L|
 = |lambda det B| det(U^T U)
 = |lambda det B| det(I_2+F F^T)
   w^T(I+F^T F)^(-1)w.`                                          (4.6)

Proof: the nonzero eigenvalues of `U diag(B,lambda) U^T` have product

`det(diag(B,lambda)) det(U^T U)`;

the Gram matrix is

`U^T U = [[I+F F^T, Fw],[(Fw)^T,||w||^2]]`,

and its Schur complement is

`||w||^2-(Fw)^T(I+FF^T)^(-1)Fw
 =w^T(I+F^TF)^(-1)w`                                             (4.7)

by Woodbury.

Therefore the new diffuse-carrier exit is

`boxed:
 mu_L<=1/2  =>
 ||p_Q||_infinity <=3e Delta_3^(-1/3),`                           (4.8)

and the output density is continuous `C_0`.

This is complementary to the designated partner's physical-pair exit, which is actually applied to the same equation as

`boxed:
 ||p_Q||_infinity
 <=18.28085635 [|det B| sigma_min(B) ||D+lambda w w^T||op]^(-1/4).` (4.9)

Thus the exact two-exit compiler is

`||p_Q||_infinity <= min{
 18.28085635 [|det B| sigma_min(B) ||D+lambda w w^T||op]^(-1/4),
 3e Delta_3^(-1/3)   if mu_L<=1/2
}.`                                                               (4.10)

The second exit can remain quantitative precisely when the literal pair itself degenerates, because the shear `E` is retained inside `F=B^(-1)E` before any reciprocal pair cost is paid.

## 5. Exact shear currencies inside Delta_3

Let the two singular values of `F` be `s_1>=s_2>=0`, and decompose

`w=alpha_1 v_1+alpha_2 v_2+w_perp`

in the right singular basis plus `ker F`. From (4.6),

`boxed:
 Delta_3/(|lambda det B|)
 = alpha_1^2(1+s_2^2)
  +alpha_2^2(1+s_1^2)
  +||w_perp||^2(1+s_1^2)(1+s_2^2).`                              (5.1)

In particular,

`boxed:
 Delta_3
 >= |lambda det B|(1+s_2(F)^2)||w||^2.`                          (5.2)

This gives an explicit mechanism for the partner's first unpaid implication `QFORM-R49-SMALL-PAIR-CURRENCY-TO-SHEAR-EXIT-v1`: if the pair matrix shrinks in two directions while the two-row shear survives, `s_2(B^(-1)E)` grows and can cancel the small determinant at the level of the rank-three carrier pseudodeterminant.

The exact formula also identifies the genuinely hard orientation: one highly anisotropic small pair, effectively rank-one shear after applying `B^(-1)`, and `w` concentrated in the corresponding strong-shear right singular direction. That is the case in which (5.2) may still be small and a leverage-hub or another grouped receiver is required.

## 6. Finite algebra audit

For random dimensions `m=1,2,5,10`, symmetric invertible indefinite/indefinite-agnostic test pairs `B`, random `E,w`, and nonzero signed `lambda`, a direct eigenvalue product of `L` was compared with both expressions in (4.6). Across the test batch, the maximum absolute discrepancy was below `2.3e-8`; the larger residual is explained by floating-point eigenvalue conditioning when one of the three nonzero carrier eigenvalues is small. The symbolic identities (4.3), (4.6), (4.7), and (5.1) are exact and do not rely on the numerical check.

The rank-three front constant is

`3e = 8.154845485377136...`.

## 7. Remaining implication

The new local obligation is now

`QFORM-R49-HEAVY-CARRIER-OR-ANISOTROPIC-SHEAR-EXIT-v1`:

within the exact diagonal-plus-rank-one Schur residual (4.1), if the partner pair currency in (4.9) is small AND either `mu_L>1/2` or `Delta_3` is small, use the resulting heavy carrier row / anisotropic-shear structure together with the intact third large spectral resource to force one of the already proved physical-hub, projected-crossing, grouped-bank, or diagonal endpoints.

The present run does not prove that the carrier pseudodeterminant is automatically target-scale under the bare three-large-eigenvalue hypothesis, and does not prove that every arbitrary symmetric matrix admits a decomposition (4.1). Therefore the full QFORM conjecture remains OPEN. No target counterexample was found.

Global continuity remains OPEN; the new branch (2.3)/(3.3)/(4.8) does prove continuous `C_0` densities in its exact scope.
