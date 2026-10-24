SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B19, 2026-09-24T07:02:20Z.
attacking: QFORM-BL-RANK2-PLUS-DIFFUSE-THIRD-SOURCE-ENDPOINT-v1 — isolate and pay the exact four-latent BL-compatible carrier, then quantify the only determinant-collapse branch in which the third source must still be supplied by the retained diffuse residual/tail.

# account03/B19 r52 — four-latent Fresnel endpoint and determinant-collapse funnel

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW COMPLETE SUPPORTING RECEIVER / NEW QUANTITATIVE FUNNEL / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository access is not native authenticated brain ingestion.

Regularity: the new receiver below gives a continuous `C_0` density on its exact scope. The full-target continuity statement remains **OPEN**.

All coordinate sets are literal ORIGINAL-coordinate sets. No random coordinate rotation is used. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, arbitrary-joint coarea, fiber-supremum, or law-uniform pointwise oscillatory-decay hypothesis is introduced. Arbitrary outside curvature, outside couplings and affine terms are retained.

## 1. Source-pinned frontier

Fresh owner control was read from `yspennstate/math-research-brain@baa01934f6a0f49fdbac5600772948e341986443` and refreshed again before publication. OWNER CONTROL remains revision `2026-09-22.15`, with QFORM as the sole research target.

Immediate same-slot source:

`yspennstate/math-open-problems@bcb36a7573a7e9f23f1ea78792e0b72bc8bb0d9c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260924T060028Z-account03-B19-QFORM-r51/REPORT.md`.

The r51 robust branch has a literal physical rank-two crossing `N=A[R,C]`, its top-two truncation `N_2=U Sigma V^T`,

`||N-N_2||_F<2^-16`, `sigma_2(N)>=1/64`,

and after the `2/7` leverage peel, light sets `L_R,L_C` with Gram matrices

`G_R=U[L_R]^T U[L_R]`, `G_C=V[L_C]^T V[L_C]`

satisfying

`lambda_min(G_R),lambda_min(G_C)>=4/7`.

The normalized restricted frames

`U~=U[L_R] G_R^(-1/2)`, `V~=V[L_C] G_C^(-1/2)`

are orthonormal two-frames and every literal physical row has leverage at most `1/2`. The ACTUAL light-light crossing retains

`sigma_2(A[L_R,L_C])>4089/458752=0.0089133126395...`,

and the full ambient law has the proved fractional resource

`H_(1/4)(Q)<12.787535`.

The earlier r49 common-plane compiler, on its aligned-self branch, supplies an exact four-latent skeleton plus retained residuals. On the new r51 light sets its skeleton has the form described in Section 3 below; the residual self blocks and the genuine cross tail are **not** deleted.

The analytic input used here is Theorem H from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

It is a product-preserving Fresnel/Brascamp--Lieb theorem for independent cap-one ORIGINAL coordinates and permits arbitrary outside blocks.

## 2. A four-latent endpoint theorem

### Theorem 2.1 — `QFORM-BL-FOURLATENT-DETERMINANT-ENDPOINT-v1`

Let `I` be a literal original-coordinate set. Suppose the physical principal block has

`A[I,I]=D+W H W^T`,

where

- `D` is physical diagonal;
- `W` is `|I| x 4` with `W^T W=I_4`;
- every literal row has leverage `||W_{i,*}||_2^2<=1/2`;
- `H=H^T` is an invertible real `4 x 4` matrix.

All blocks touching `I^c`, all curvature inside `I^c`, and all affine terms may be arbitrary. For every independent input law with coordinate densities at most one, the full ambient quadratic polynomial has a continuous `C_0` density and

`boxed: ||p_Q||_infinity <= 8 |det H|^(-1/4).`                 (2.1)

This is sign-free: `H` may have any signature; repeated eigenvalues are allowed. The only excluded case in this theorem is `det H=0`, which is retained as a separate structural branch rather than divided by.

### Proof

Diagonalize in the **coefficient space only**,

`H=O diag(mu_1,mu_2,mu_3,mu_4) O^T`,

with `O` orthogonal. Put `Z=W O`. Then `Z^T Z=I_4`, and orthogonal mixing of the four coefficient columns preserves each physical row leverage:

`||Z_{i,*}||^2=||W_{i,*}||^2<=1/2`.

No random variable has been rotated.

Apply Theorem H with zero physical hub coordinates, `r=4`, coefficient vectors the four columns of `Z`, and diagonal twist `D`. Its Gram matrix is `I_4`, so for the full ambient characteristic function

`|phi_Q(t)| <= (4 pi)^2 |t|^-2 |mu_1 mu_2 mu_3 mu_4|^-1/2`

`=16 pi^2 |det H|^-1/2 |t|^-2`.                                (2.2)

Of course `|phi_Q(t)|<=1`. If `K=16 pi^2 |det H|^-1/2`, then

`integral_R min(1,K |t|^-2) dt =4 sqrt(K)`.

Fourier inversion therefore yields

`||p_Q||_infinity <= (1/(2 pi)) 4 sqrt(K)=8 |det H|^-1/4`,

proving (2.1). The integrable characteristic function also gives a continuous density vanishing at infinity. QED.

## 3. Exact application to the r49/r51 aligned four-latent skeleton

Work on the intersection of the r49 common-plane branch and the r51 BL-compatible robust crossing branch. Condition every r51-heavy physical coordinate and every coordinate outside `L_R union L_C`; conditioning only original coordinates preserves independence of the remaining coordinates and converts the conditioned couplings into affine terms.

The aligned rank-two self pieces on the two light banks and the rank-two crossing truncation can be written

`W_0 H_4 W_0^T`,

with

`W_0=diag(U[L_R],V[L_C])`,

`H_4=[[B_R,Sigma],[Sigma,B_C]]`.                                (3.1)

Set

`S=diag(G_R^(1/2),G_C^(1/2))`,

`W=diag(U~,V~)`,

`H_L=S H_4 S`.                                                    (3.2)

Then **exactly**

`W H_L W^T=W_0 H_4 W_0^T`,                                      (3.3)

`W^T W=I_4`, and every row of `W` has leverage at most `1/2` by r51. Furthermore

`det H_L = det(G_R) det(G_C) det H_4`.                            (3.4)

Since each `G_R,G_C` is `2 x 2` with minimum eigenvalue at least `4/7`,

`det(G_R),det(G_C)>=(4/7)^2`.                                    (3.5)

Consequently, whenever `det H_4!=0`, Theorem 2.1 gives the exact-skeleton endpoint

`||p||_infinity <=8 |det H_L|^-1/4`

`<=14 |det H_4|^-1/4`.                                           (3.6)

This is a full-ambient statement for the quadratic form whose light-light principal block is `diag(q)+W_0H_4W_0^T`: every conditioned heavy-coordinate contribution, every outside block, and every outside coupling is already allowed by Theorem 2.1.

What (3.6) does **not** do is delete the r49 residual self blocks `E_R,E_C` or the genuine nonzero cross tail `T_cross`. Those remain in the actual QFORM branch. Thus (3.6) identifies a complete endpoint receiver for the exact aligned carrier and isolates the retained residual/tail as the first analytic debt.

## 4. Determinant collapse is quantitatively a rank-three latent collapse

The same normalization gives a sharp algebraic funnel for the skeleton.

The normalized latent cross block is

`C_L=G_R^(1/2) Sigma G_C^(1/2)`.                                 (4.1)

Because `sigma_2(Sigma)=sigma_2(N)>=1/64` and both Gram square roots have least singular value at least `sqrt(4/7)`,

`boxed: sigma_2(C_L)>=1/112.`                                    (4.2)

Since `C_L` is a `2 x 2` subblock of the symmetric `4 x 4` matrix `H_L`, contraction monotonicity of singular values gives

`s_1(H_L),s_2(H_L)>=s_2(C_L)>=1/112`.                             (4.3)

Let `s_1>=s_2>=s_3>=s_4` be the singular values of `H_L`. Then

`|det H_L|=s_1s_2s_3s_4 >=(1/112)^2 s_4^2`,                     (4.4)

because `s_3>=s_4`. Therefore

`boxed: s_4(H_L)<=112 sqrt(|det H_L|).`                           (4.5)

Equivalently, the operator-norm distance from `H_L` to the set of rank-at-most-three symmetric matrices is at most the right side.

At the concrete gate

`|det H_L|>=2^-40`,                                               (4.6)

Theorem 2.1 pays the exact skeleton by

`boxed: ||p||_infinity <=8192.`                                  (4.7)

If (4.6) fails, then instead

`boxed: dist_op(H_L,rank<=3)<112*2^-20`

`=0.0001068115234375.`                                           (4.8)

If one states the gate before normalization, `|det H_4|>=2^-40`, then (3.6) gives the concrete bound

`boxed: ||p||_infinity <=14336.`                                 (4.9)

This yields the new compiler

`QFORM-R51-FOURLATENT-DET-OR-RANK3-COLLAPSE-v1`:

> the exact BL-compatible four-latent carrier is either paid with a continuous density by a universal determinant gate, or it is quantitatively within `1.07e-4` of a three-latent carrier at the normalized r51 scale.

The small fourth latent coefficient in the collapse branch is **not** treated as a small random perturbation. Under cap-one laws there are no moment or support bounds that would justify doing so.

## 5. Why this does not yet close the actual r51 robust branch

The actual r49/r51 light block is

`diag(q)+W H_L W^T+(E_R direct_sum E_C)+T_cross`,                 (5.1)

where the r49 residual high-spectrum projections are physically diffuse and `T_cross` is the retained `2^-16`-scale coefficient tail. Theorem 2.1 allows arbitrary *outside* blocks but not arbitrary nonseparable additions inside its Fresnel coordinate set. Hence the following implication is still missing:

`QFORM-BL-R2-PLUS-DIFFUSE-THIRD-SOURCE-RETAINED-TAIL-ENDPOINT-v2`:

> combine the r51 two-plane leverage `<=1/2` and `H_(1/4)<12.787535` resource with the r49 physically diffuse residual/high-spectrum source to get `L^1` characteristic-function decay or a linear small-ball bound **without deleting** `E_R,E_C,T_cross`; or route the rank-three latent-collapse geometry into a completed physical-pair, grouped-star, ridge/window, incident-volume, hub+square, or inductive receiver.

The new determinant theorem shows that no additional difficulty remains in the exact nonsingular four-latent carrier itself. The first unresolved analytic interaction is precisely the retained diffuse third source/tail, especially when the latent determinant collapses.

Fresh account01/B19 r54 supplies a complete hub+one-square Fresnel receiver in an adjacent branch: if a literal hub and a rank-one square produce an augmented two-frame with row leverage at most `1/2`, then

`||p_Q||_infinity <=7.5595263 (|lambda| det G)^(-1/3)`

with continuous density, arbitrary outside blocks retained. This is an available exit after a genuine hub+square manufacture, not a premise that such a manufacture always occurs in (5.1).

## 6. Designated account04/B19 result applied and boundary preserved

The completed account04/B19 null-coloop theorem is

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

Inside its exact residual-diffuse rank-three null-coloop scope,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`,                        (6.1)

for `0<D_res<=1`, `|det M_3|>=1`, with continuous `C_0` density. At the concrete gate

`2^-56<=D_res<=1`,                                                (6.2)

this gives the actual inequality

`boxed: ||p_Q||_infinity<214.540383<215.`                         (6.3)

No near-null interpolation and no arbitrary-joint extension is inferred.

The designated partner's newer moving-ridge barrier is

`yspennstate/math-open-problems@ac55b70485c4108c7073a75365127e00be3bc097`.

It proves that replacing original-product provenance by only a bounded joint-density cap is invalid. At `epsilon=2^-20` its fixed three-large-eigenvalue surrogate satisfies

`boxed: ||p_(4XY+Z^2-YW)||_infinity >=2^20/9`

`=116508.444444...`,                                             (6.4)

although the relevant joint density cap is one. The variables in that construction are dependent, so it is not a target counterexample; it is a rigorous prohibition on the tempting shortcut of projecting (5.1) to a few latent variables and forgetting their product-source provenance.

## 7. Computation and exact checks

The constants in Sections 3--6 were recomputed independently. In addition, 5,000 seeded noncommuting random frame instances satisfying the r51 Gram gate were checked for the determinant congruence (3.4), the normalized leverage bound, the cross singular lower bound, and the determinant-collapse inequality (4.4). Results:

- maximum normalized determinant residual: `1.772897745163291e-15`;
- maximum leverage excess above `1/2`: `0`;
- minimum observed `sigma_2(C_L)/((4/7)sigma_2(Sigma))`: `1.0444062920607573`;
- determinant-collapse violations: `0`.

These finite computations are diagnostics only. The results above have exact proofs.

## 8. Compact conditional proof assembly after r52

The current end-to-end conditional route is now:

1. same-constant principal-minimal descent removes proper original-coordinate principal blocks already carrying three target eigenvalues;
2. completed diagonal, physical-pair, pair-log, physical-E3, ridge/window, grouped, null-coloop, rank-two half-Riesz/fractional and related receivers pay their exact branches while retaining stated outside curvature;
3. the r47--r51 compilers reduce one major singular-pair/large-leaf chamber to strong BL-compatible rank-two light banks or a finite physical hub-star branch;
4. on the common-plane part of the robust branch, the present theorem completely pays the exact nonsingular four-latent skeleton and quantitatively identifies determinant failure with a rank-three latent collapse;
5. the unresolved object is no longer the exact four-latent carrier: it is the coupling of that carrier (or its rank-three collapse) to the **retained physically diffuse residual self curvature and genuine cross tail**, plus the parallel giant-near-rank-one and small-Pluecker aggregate branches.

All signs and repeated-eigenvalue cases are included in the new theorem; exact determinant zero is preserved as a branch rather than perturbed away. The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.
