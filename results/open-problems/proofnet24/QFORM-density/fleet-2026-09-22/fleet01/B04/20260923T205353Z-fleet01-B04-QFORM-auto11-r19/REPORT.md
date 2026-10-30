SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T20:53:53Z.
attacking: make the overlap-one third-compound Schur packet rank-free by proving a marginal-free second-compound L^p product-Fourier estimate, then bootstrap it with the dependent physical square.

# fleet01/B04 r19 — rank-free overlap-one Schur compound via second-compound product Fourier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `SUPPORTING_THEOREM_PROVED / OVERLAP1_EXACT_RANK_RESTRICTION_REMOVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuity in the new overlap-one branch: **not claimed; an essentially bounded density is proved**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

No random variable is rotated. No moment, support, Gaussian, log-concavity, pointwise one-dimensional quadratic-phase decay, arbitrary-joint coarea estimate, or worst conditional-density cap is used. The source inputs remain disjoint banks of the original independent coordinates.

## 1. Fresh control and source boundary

Immediately before publication, `math-research-brain` main was refreshed to commit

`acdaa8bd7856ada64a4d250502177789b4c8fc52`.


Pinned mathematical inputs:

1. `QFORM-GROUPED-CROSSING-EXACT-SUBSET-ENTROPY-v1`, `yspennstate/math-open-problems@13f0b0b271b4e230cb5493e887ed5ec7dd65f63b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T181304Z-fleet01-B04-QFORM-auto11-r16/REPORT.md`. Its pre-integration product-Fourier estimate is used below; the condition `d>2` in its displayed density theorem is needed only for the final `t`-integral, not for that pre-integration estimate.
2. `QFORM-CANONICAL-COMPOUND-PROMOTION-v1`, `yspennstate/math-open-problems@d5e114f4a9f515344575756615fce3a754195b13`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T185132Z-fleet01-B04-QFORM-auto11-r17/REPORT.md`. Its exact promotion identity is
   `S_+^2 Z_{ell-1}^+=alpha_h S^2 Z_ell`.
3. `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1`, `yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/QFORM-B11-20260922T121344Z/REPORT.md`.
4. The overlap-one Schur determinant and random-cut identities from fleet01/B09, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B09/B09-20260922T144636Z-r12/REPORT.md`, available immutably at `yspennstate/math-open-problems@0d42128032953f968d7a37c82f7ea4413929c508`.
5. Designated partner fleet02/B04 theorem `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`, `yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T111930Z-qform/REPORT.md`. Its exact-rank-three coloop branch is applied to an actual inequality in Section 6.

## 2. New theorem: marginal-free second-compound cross `L^p`

Let `U=(U_i)_{i in I}` and `V=(V_j)_{j in J}` be two disjoint banks of original independent coordinates, each scalar density bounded by one. Let

`R=q_I(U)+2 U^T N V+q_J(V)+linear+constant`,                    (2.1)

where `q_I,q_J` are arbitrary real quadratic forms. Put

`Z_2=E_2(N)=e_2(NN^T)>0`.                                       (2.2)

No rank assumption is made on `N`.

### Theorem `QFORM-SECOND-COMPOUND-CROSS-LP-PROMOTION-v1`

For every `2<=p<infinity`, `R` has a density and

`boxed:
 ||p_R||_p
 <= (2^(7/4) p)^(1-1/p)
    Z_2^{-(p-1)/(4p)}.`                                         (2.3)

In particular,

`boxed:
 ||p_R||_3
 <= 3^(2/3) 2^(7/6) Z_2^(-1/6).`                               (2.4)

### Proof

Use the canonical physical pair-volume law on two-row subsets `E` of `N`,

`nu(E)=det(N_E N_E^T)/Z_2`,                                    (2.5)

and write `alpha_i=P_nu(i in E)`.

#### Balanced branch

If every `alpha_i<=1/2`, apply the exact weighted-subset product-Fourier estimate from the r16 source with `k=0`, `ell=2`. The canonical determinant/entropy currency is exactly `G=Z_2`. The fixed-cardinality identity from r17 gives

`F_2^2=2 exp[-I(I_1;I_2)]<=2`.                                  (2.6)

The pre-integration Fourier estimate therefore gives

`|phi_R(t)|
 <= min{1, K_0/|t|},
 K_0=2^(7/4) pi Z_2^(-1/4).`                                    (2.7)

The derivation of (2.7) is the product-space change of variables plus Hausdorff--Young/rearrangement estimate. It is not a law-uniform pointwise estimate for one scalar quadratic phase.

#### One physical promotion

Suppose instead some physical row `h_1` has `alpha_1>1/2`. Promote the *original scalar coordinate* `U_{h_1}` into the grouped hub. The r17 exact base-times-height identity gives

`S_1^2 Z_1=alpha_1 Z_2`.                                        (2.8)

At the residual one-volume level `F_1=1`. The same pre-integration product-Fourier/Plancherel calculation, now with `k=1,ell=1`, gives

`|phi_R(t)|
 <=min{1,K_1/|t|},
 K_1=2 pi (alpha_1 Z_2)^(-1/4)
 <2^(5/4) pi Z_2^(-1/4).`                                      (2.9)

The promoted coordinate may carry arbitrary same-bank quadratic curvature because the grouped theorem permits an arbitrary internal hub function.

#### Two physical promotions

If the residual canonical one-volume law has a row marginal `alpha_2>1/2`, promote that original coordinate as well. Then

`S_2^2=alpha_1 alpha_2 Z_2`.                                    (2.10)

All two smoothing directions are now physical hub directions. The standard rank-two cross product-Fourier estimate gives

`|phi_R(t)|
 <=min{1,K_2/|t|},
 K_2=2 pi (alpha_1 alpha_2 Z_2)^(-1/4)
 <2^(3/2) pi Z_2^(-1/4).`                                      (2.11)

Both coefficients in (2.9)-(2.11) are smaller than the balanced coefficient. Therefore, with no marginal assumption at all,

`boxed:
 |phi_R(t)|
 <=min{1,K/|t|},
 K=2^(7/4) pi Z_2^(-1/4).}`                                    (2.12)

Now let `q=p/(p-1)`, so `1<q<=2`. Splitting at `|t|=K`,

`||phi_R||_q^q
 <=2K+2K^q int_K^infinity t^(-q)dt
 =2K[1+1/(q-1)]
 =2Kp.`                                                         (2.13)

With Fourier convention `hat f(t)=int exp(itx)f(x)dx`, inverse Hausdorff--Young gives

`||p_R||_p
 <=(2pi)^(-1/q)||phi_R||_q
 <=(Kp/pi)^(1/q)`,                                               (2.14)

which is exactly (2.3). Taking `p=3` gives (2.4). QED.

### Scope

The theorem is rank-free and retains every singular direction of `N`; it only pays the *aggregate* second-compound currency `E_2(N)`. Thus a third or later singular value may tend to zero without appearing reciprocally in (2.3).

## 3. New theorem: arbitrary-rank Schur `E_2` plus one physical square

Partition the original coordinates as

`{h} disjoint_union I disjoint_union J disjoint_union R_out`,   (3.1)

and condition on `R_out`. Put

`a=A_hh !=0`,                                                    (3.2)

and, after completing the square in the **original coordinate** `X_h`, let the `I-J` cross block of the scalar Schur complement be

`N=A[I,J]-A[I,h]A[h,J]/a`.                                      (3.3)

Assume `E_2(N)>0`.

### Theorem `QFORM-ARBITRARYRANK-SCHUR-E2-PIVOT-v1`

Uniformly over the outside conditioning and hence unconditionally,

`boxed:
 ||p_(X^TAX)||_infinity
 <= sqrt(3) 2^(23/8)
    |a|^(-1/2) E_2(N)^(-1/8).`                                  (3.4)

### Proof

After the scalar completion,

`Q=a W^2+R(U,V)`,                                                (3.5)

where `R(U,V)` has cross block `N` and arbitrary same-side quadratic/affine terms, while

`W=X_h+theta(U,V)`.                                              (3.6)

By (2.4),

`||p_R||_3 <=3^(2/3)2^(7/6)E_2(N)^(-1/6).`                      (3.7)

Since `X_h` is an untouched independent cap-one scalar, conditional on `R=r` the law of `W` is a mixture of translates of the original law of `X_h`; hence its conditional density is at most one. Apply `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1`:

`||p_Q||_infinity
 <=4 |a|^(-1/2)||p_R||_3^(3/4)`
 `=sqrt(3)2^(23/8)|a|^(-1/2)E_2(N)^(-1/8).`                     (3.8)

The estimate is uniform in every outside-conditioned affine term, so averaging the conditional densities proves (3.4). QED.

This argument is deliberately different from the newly refuted arbitrary-remainder mechanism: (3.7) is an actual `L^3` density theorem for the whole product Schur residual, not merely a slope or innovation lower bound.

## 4. Main consequence: overlap-one third-compound packets are rank-free

Fix a physical pivot `h` with

`a=A_hh !=0`.                                                    (4.1)

For disjoint two-sets `K,L` outside `h`, define

`m_{h;K,L}=det A[{h} union K,{h} union L]`,                      (4.2)

and the total overlap-one energy

`M_{1,h}(A)
 =sum_{|K|=|L|=2, K cap L=empty} m_{h;K,L}^2.`                   (4.3)

Let `S_h` be the scalar Schur complement after pivoting `h`. The previously proved exact determinant identity is

`m_{h;K,L}=a det S_h[K,L]`,                                     (4.4)

and a uniformly random Bernoulli half-cut `P|P^c` of the residual coordinates satisfies

`E_P E_2(S_h[P,P^c])=M_{1,h}(A)/(16a^2).`                       (4.5)

### Theorem `QFORM-OVERLAP1-SCHUR-COMPOUND-RANKFREE-v1`

If `a!=0` and `M_{1,h}(A)>0`, then the full ambient quadratic form has a density with

`boxed:
 ||p_(X^TAX)||_infinity
 <= sqrt(3) 2^(27/8)
    |a|^(-1/4) M_{1,h}(A)^(-1/8).`                              (4.6)

No rank hypothesis is made on `A`, on `S_h`, or on the selected cross block.

### Proof

By (4.5), some physical cut obeys

`E_2(S_h[P,P^c])
 >=M_{1,h}(A)/(16a^2)>0.`                                       (4.7)

Apply Theorem (3.4) to that actual original-coordinate split:

`||p_Q||_infinity
 <=sqrt(3)2^(23/8)|a|^(-1/2)
   [M_{1,h}/(16a^2)]^(-1/8)`
`=sqrt(3)2^(27/8)|a|^(-1/4)M_{1,h}^(-1/8).`                     (4.8)

QED.

The scaling is correct: under `A -> cA`, `a -> ca` and `M_{1,h}->c^6 M_{1,h}`, so (4.6) scales as `|c|^-1`.

### What was removed

The older overlap-one theorem required `rank(A)=3` so that the selected Schur cross block had exact rank two. Equation (4.6) removes that restriction completely. Extra spectrum and arbitrary same-bank curvature are retained; the Fourier estimate only uses aggregate `E_2` currency.

### Continuity

The new theorem proves an essentially bounded density. The final dependent-square lemma used here does not by itself provide an `L^1` characteristic-function estimate, so **continuity is not claimed** for (4.6). Full-target continuity remains open.

## 5. Genuinely rotated indefinite dense stress family with a vanishing third Schur direction

For `0<epsilon<=10^-2`, define

`N_epsilon=2 I_3+((epsilon-2)/3)J_3`,                            (5.1)

and

`S_epsilon=[[0,N_epsilon],[N_epsilon,0]]`.                       (5.2)

The singular values of `N_epsilon` are exactly

`2,2,epsilon`,                                                   (5.3)

so `S_epsilon` has eigenvalues

`+2,+2,+epsilon,-2,-2,-epsilon`.                                (5.4)

Set `delta=epsilon`, `b=delta 1_6`, and define the fully dense symmetric `7 x 7` matrix

`A_epsilon
 =[[2,                 b^T],
   [b, S_epsilon+(1/2)bb^T]].`                                  (5.5)

Every physical entry of `A_epsilon` is nonzero: the pivot couplings are `delta`, every residual same-side entry is `delta^2/2`, and all entries of `N_epsilon+(delta^2/2)J_3` are nonzero in the stated range.

The scalar Schur complement at the pivot is **exactly** `S_epsilon`. The reference matrix `diag(2,S_epsilon)` has spectrum

`{2,2,2,epsilon,-2,-2,-epsilon}`.                               (5.6)

The perturbation from (5.6) is

`P=[[0,b^T],[b,(1/2)bb^T]]`,                                    (5.7)

with

`||P||op<=||P||F
 =sqrt(12 delta^2+9 delta^4)<0.035`.                             (5.8)

Thus Weyl leaves the five `+-2`/pivot eigenvalues with modulus above `1.965`; in particular every `A_epsilon` satisfies the owner's three-large-eigenvalue hypothesis with room to spare and is indefinite, non-diagonal and fully dense.

The exact disjoint second-compound energy of the Schur matrix is

`D_epsilon
 =sum_{|K|=|L|=2,K cap L=empty} det S_epsilon[K,L]^2`
`=(4/9)(epsilon^4+60epsilon^2+16epsilon+144).`                   (5.9)

This identity follows by direct `2 x 2` determinant classification and is independently checked in `CHECKS.json`. Since `D_epsilon>=64`, the pivot has `a=2` and `M_{1,h}=4D_epsilon`, so (4.6) becomes

`||p_(X^T A_epsilon X)||infinity
 <=sqrt(3)2^(23/8)D_epsilon^(-1/8)`
`<=sqrt(3)2^(17/8)`
`=7.55525919609186... .`                                        (5.10)

Hence the bound remains finite as the third Schur singular direction `epsilon` tends to zero.

At the concrete value `epsilon=delta=10^-2`,

`D_epsilon=14416600001/225000000
 =64.07377778222222...`,                                        (5.11)

and the new bound is

`boxed:
 ||p_(X^T A_epsilon X)||infinity
 <=7.554171209535741... .}`                                     (5.12)

This is an analytic certificate, not a histogram or Monte Carlo estimate.

## 6. Designated fleet02/B04 theorem applied to the same ambient matrix

Condition the physical pivot coordinate in (5.5). The retained left-three/right-three cross block is

`N_tilde_epsilon
 =N_epsilon+(epsilon^2/2)J_3`.                                   (6.1)

Its singular values are exactly

`2,2,epsilon+(3/2)epsilon^2`.                                   (6.2)

There are exactly three physical rows on the constrained side, so every supported third-volume law has all three row marginals equal to one. The strict `h<3/4` gate therefore fails maximally, and the designated partner theorem `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1` enters its coloop/exact-rank-three branch. Uniformly in the conditioned pivot value,

`||p_Q||infinity
 <=6 E_3(N_tilde_epsilon)^(-1/6)`
`=6*2^(-2/3)
  [epsilon+(3/2)epsilon^2]^(-1/3).`                             (6.3)

Averaging gives the same full-law bound. At `epsilon=10^-2`,

`E_3(N_tilde_epsilon)
 =(203/5000)^2
 =0.00164836`,                                                   (6.4)

so the partner certificate is

`17.457252994674807... .`                                       (6.5)

The new rank-free overlap-one certificate (5.12) improves this actual same-matrix bound by the factor

`2.31094219477555...`.                                          (6.6)

More importantly, the partner exact-rank-three bound grows like `epsilon^(-1/3)` along this family, while (5.10) stays below `7.556`. This is precisely the gain from paying second-compound energy before the weak third singular direction.

## 7. Updated proof-map consequence

The previous B04 random-cut result paid disjoint third-compound energy. The main unpaid third-compound geometry was overlap `|R cap T|=1,2,3`. This run removes a major analytic restriction in the overlap-one branch:

- if a shared physical coordinate `h` has `A_hh!=0` and its aggregate overlap-one energy `M_{1,h}` is nonzero, no exact-rank assumption is needed;
- the dimensionless/scaling-correct payment currency is

`C_h=(A_hh^2 M_{1,h})^(1/8)`,                                   (7.1)

because (4.6) is `sqrt(3)2^(27/8) C_h^-1`;
- arbitrary extra singular directions do not hurt, and an arbitrarily weak third singular value of the Schur cross block is not paid reciprocally.

The new first structural obligation is therefore

`QFORM-OVERLAP1-PIVOT-CURRENCY-OR-LIGHTCONE-ROUTING-v1`:

> If a target-scale portion of third-compound energy lies in overlap-one minors, either find a shared physical pivot with target-scale `A_hh^2 M_{1,h}`, so (4.6) applies, or route concentration on pivots with very small/zero diagonal coefficient into the already-developed physical hyperbolic-pair, grouped-bank, principal/diagonal, overlap-two/three, or aggregate-crossing mechanisms.

This implication is **not proved here**. It is genuinely necessary: indefinite target matrices may have many or all physical diagonal entries equal to zero, so overlap-one mass alone cannot force a nonzero scalar pivot of universal size.

## 8. Status

- Full unrestricted QFORM theorem: **OPEN**.
- Full-target continuity: **OPEN**.
- New theorem `QFORM-SECOND-COMPOUND-CROSS-LP-PROMOTION-v1`: proved.
- New theorem `QFORM-ARBITRARYRANK-SCHUR-E2-PIVOT-v1`: proved.
- Main theorem `QFORM-OVERLAP1-SCHUR-COMPOUND-RANKFREE-v1`: proved.
- Exact-rank-three restriction in the overlap-one Schur branch: **removed**.
- Continuity for the new overlap-one theorem: **not proved; only an essentially bounded density is claimed**.
- Two independent end-to-end reviews are not requested because there is no full candidate proof.
