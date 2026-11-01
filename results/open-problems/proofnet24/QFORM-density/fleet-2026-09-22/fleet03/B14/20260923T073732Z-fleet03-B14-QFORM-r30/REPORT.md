SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T07:37:32Z.
attacking: disjoint Schur-bank localization: arbitrary pair-to-bank couplings and outside variables, with a rank-one Schur smoother extracted before any fragment or tail payment.

# QFORM-DISJOINT-SCHUR-BANK-LOCALIZATION-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet03/B14`  
Run: `20260923T073732Z-fleet03-B14-QFORM-r30`  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREM; FULL QFORM OPEN; full-target continuity OPEN.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. What is new

The preceding B14 run closed an arbitrary-dimensional rank-one bank only when the active hyperbolic pair had no quadratic cross coupling into that bank. This run removes that restriction in the natural Schur-complement form.

A fixed indefinite pair may couple arbitrarily strongly to a large independent coordinate bank and to arbitrary outside coordinates. Complete the pair first. If the bank principal block of the resulting Schur complement is rank one, then that whole bank supplies a dimension-free half-order small-ball estimate, while every pair-to-bank coupling is absorbed into a random translation of the physical pair. The completed pair-log theorem explicitly permits those translations to depend on the same variables that generate the remainder. Consequently the bound is uniform in the coupling matrix, outside dimension, all outside coefficients, all deterministic translations, unbounded supports, and arbitrary fragment geometry.

The result is not the full conjecture because the bare condition `s_3(A)>=1` does not force a pair/bank certificate with a uniformly large indefinite pair and uniformly large rank-one Schur curvature.

## 2. Sources actually used


Two completed mathematical inputs are used at actual inequalities.

1. **Physical-pair logarithmic smoothing theorem**, source-pinned at
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   If an invertible indefinite physical pair has block `B`, `D=|det B|`, `kappa=sigma_min(B)`, and after completing that pair the scalar remainder `R` obeys

   `sup_t P(|R-t|<rho) <= H sqrt(rho)` for all `rho>0`,

   then

   `||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.          (2.1)

   Crucially, the completed theorem states that the translations of the two pair coordinates may depend arbitrarily on the same remaining variables that determine `R`.

   Its rank-one affine small-ball lemma also gives, for independent cap-one coordinates `V`, unit `a`, nonzero `lambda`, and arbitrary `b,d`,

   `sup_t P(|lambda (a^T V)^2+b^T V+d-t|<rho)`
   ` <= min(1,10 sqrt(rho/|lambda|))`.                         (2.2)

2. **Designated partner fleet04/B14 affine-family localization compiler**, source-pinned at
   `yspennstate/math-open-problems@19d9434e07142e6b9fe19b4a88bbd46ccec8eeee`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T001323Z-fleet04-B14-affine-mixture-compiler-r5/REPORT.md`.
   Uniform interval estimates for a fixed active physical quadratic block and arbitrary affine parameters transfer from compact finite-fragment indicator product laws to all cap-one product laws with exactly the same constant, while arbitrary outside laws are left untouched. This result is applied in Section 6 to the actual conditional inequality (5.3).

The newest fleet04/B14 scale-shear report was also read (`20260923T051013Z-fleet04-B14-scale-shear-r7`); the present theorem attacks its stated residual issue by allowing a genuinely coupled bank after Schur completion rather than conditioning away that bank.

## 3. Setup and exact Schur identity

Partition the ORIGINAL independent coordinates into three disjoint blocks

`X=(U,V,Z)`,

where `U in R^2` is a physical pair, `V in R^m` is the active bank, and `Z` denotes every remaining original coordinate. Allow an arbitrary affine perturbation from the outset:

`F(X)=X^T A X + eta^T X + c`.                                  (3.1)

Write the matrix in block form

`A = [[B, C_J, C_K],`
`     [C_J^T, D_JJ, D_JK],`
`     [C_K^T, D_KJ, D_KK]]`,                                   (3.2)

where `B` is symmetric, invertible and indefinite. Put

`C=[C_J,C_K]`, `W=(V,Z)`, `D=A_(I^c,I^c)`,

and define the Schur complement of the physical pair

`S := D - C^T B^(-1) C`.                                      (3.3)

Let `S_JJ` be the bank principal block of `S`.

Writing `eta=(eta_I,eta_W)` and

`g(W)=C W + eta_I/2`,

the exact completion identity is

`F = (U+B^(-1)g(W))^T B (U+B^(-1)g(W)) + R(W)`,               (3.4)

where

`R(W)= W^T S W`
`      +(eta_W-C^T B^(-1)eta_I)^T W`
`      +c-(1/4)eta_I^T B^(-1)eta_I`.                          (3.5)

No rotation of the random coordinates occurs. The shift `B^(-1)g(W)` is allowed to be arbitrarily large and to depend on all bank and outside coordinates.

## 4. Main theorem

### Theorem 4.1 — `QFORM-DISJOINT-SCHUR-BANK-LOCALIZATION-v1`

Assume `S_JJ` in (3.3) has rank exactly one and its sole nonzero eigenvalue `lambda` satisfies

`|lambda| >= s > 0`.                                           (4.1)

Then for every collection of independent real input coordinates with probability densities bounded by one, the law of (3.1) has an essentially bounded density and

`boxed( ||p_F||_infinity`
` <= 8 sqrt(5) [ |det B| sigma_min(B) s ]^(-1/4). )`            (4.2)

The estimate is uniform in

- the bank dimension `m` and the outside dimension;
- the full pair-to-bank coupling `C_J` and pair-to-outside coupling `C_K`;
- `S_JK,S_KK`, hence arbitrary remaining quadratic coefficients after pair completion;
- every affine vector `eta` and scalar `c`;
- all support locations, support diameters, fragment counts and fragment separations;
- all moments (none are assumed).

Only essential boundedness is claimed. Continuity is not supplied by this argument.

### Proof

Because `S_JJ` is real symmetric rank one, write

`S_JJ=lambda a a^T`, `||a||_2=1`.                              (4.3)

Fix the outside original coordinates `Z=z`. The variables in `U` and `V` remain mutually independent and each retains its original cap-one density. From (3.5), the remainder becomes

`R_z(V)=lambda(a^T V)^2 + b(z)^T V + d(z)`,                    (4.4)

where explicitly

`b(z)=2 S_JK z + [eta_W-C^T B^(-1)eta_I]_J`,                  (4.5)

and `d(z)` collects the `Z`-only terms. No size bound on `b(z)` or `d(z)` is needed.

Apply the completed rank-one affine small-ball lemma (2.2) to the original independent bank coordinates. Uniformly in `z` and every center `t`,

`P( |R_z-t|<rho | Z=z )`
` <= min(1,10 sqrt(rho/s))`.                                  (4.6)

Thus the pair-log hypothesis holds with

`H=10/sqrt(s)`.                                                (4.7)

Conditional on `Z=z`, equation (3.4) is exactly the setting of the completed physical-pair logarithmic theorem: the physical pair has the fixed block `B`, its two translations equal the components of `B^(-1)g(V,z)`, and those translations may depend arbitrarily on `V`, which also determines the remainder (4.4). This dependence is explicitly permitted by the source theorem; no false conditional-independence substitution is being made.

With

`D=|det B|`, `kappa=sigma_min(B)`,                             (4.8)

substitute (4.7) into (2.1):

`||p_(F|Z=z)||_infinity`
` <= 4 sqrt( 2 * 10/sqrt(s) ) (D kappa)^(-1/4)`
` = 8 sqrt(5) (D kappa s)^(-1/4).`                            (4.9)

The right side is independent of `z`. Averaging the conditional densities gives a density for `F` with the same essential supremum bound. This proves (4.2). QED.

## 5. Concrete target-level branches

Theorem 4.1 immediately gives the certificate

`|det B| sigma_min(B) s >= 1  ==>  ||p_F||_infinity <= 8sqrt(5)`

`=17.888543819998... .`                                        (5.1)

A particularly transparent case is the hyperbolic physical pair

`B=[[0,c],[c,0]]`.

Then `|det B|=c^2` and `sigma_min(B)=|c|`, so

`||p_F||_infinity`
` <= 8sqrt(5) (|c|^3 s)^(-1/4).`                              (5.2)

Hence every such branch with `|c|>=1` and rank-one Schur-bank curvature `s>=1` is uniformly bounded by `8sqrt(5)`, **even when the raw pair-to-bank coupling is nonzero and spread over arbitrarily many coordinates**.

This removes one of the explicit unpaid items in the preceding B14 report: pair-to-bank cross coupling is harmless whenever, after completing the pair, a disjoint original-coordinate bank retains rank-one Schur curvature of universal scale.

### Diffuse coupled stress family inside the original target

Let `a_N=N^(-1/2)(1,...,1) in R^N`, take

`B=[[0,2],[2,0]]`, `S_JJ=2 a_N a_N^T`,

and choose the raw pair-to-bank cross block

`C_J=[[ (3/2) a_N^T ], [ 0 ]]`.                               (5.3)

Because `B^(-1)=[[0,1/2],[1/2,0]]`, one has

`C_J^T B^(-1) C_J=0`,

so the raw bank block can simply be `D_JJ=2a_Na_N^T`; the Schur bank is still exactly `S_JJ` despite the nonzero diffuse coupling. On the three-dimensional active subspace spanned by the two pair coordinates and `a_N`, the homogeneous matrix is

`M=[[0,2,3/2],[2,0,0],[3/2,0,2]]`.                            (5.4)

Its characteristic polynomial is

`4x^3-8x^2-25x+32`.                                           (5.5)

The signs

`p(-3)<0<p(-2)`, `p(1)>0>p(6/5)`, `p(3)<0<p(4)`               (5.6)

show that its three roots lie respectively in `(-3,-2)`, `(1,6/5)`, and `(3,4)`. Thus all three nonzero eigenvalues have modulus greater than one for every `N`: this is a valid original-target family with nonzero diffuse pair-to-bank coupling.

Here `D=4`, `kappa=2`, `s=2`, hence (4.2) gives

`||p_Q||_infinity <= 8sqrt(5) / 2 = 4sqrt(5) < 8.945`,         (5.7)

uniformly in `N`. Every individual coupling coefficient is `(3/2)/sqrt(N) ->0`; the theorem pays the collective Schur bank rather than selecting one coefficient.

## 6. Actual application of the designated partner localization theorem

For the localization step, first restrict the active original coordinates `(U,V)` to compact finite-fragment indicator product laws. The derivation above gives, for every fixed outside value `z`, every interval `I`, and every affine parameter generated by `z`,

`P{ F(U,V,z) in I }`
` <= C_B,s |I|`,                                               (6.1)

where

`C_B,s = 8sqrt(5) [|det B| sigma_min(B) s]^(-1/4)`.            (6.2)

The constant is uniform in the complete affine family and in `z`; neither the fragment count nor fragment locations occur.

Now apply the completed fleet04/B14 affine-family localization compiler to the actual inequality (6.1), taking its active block to be the ORIGINAL coordinates `(U,V)` and its outside block to be `Z`. The compiler gives

`P{F(X) in I} <= C_B,s |I|`                                   (6.3)

for arbitrary cap-one product laws on all coordinates, with **exactly the same constant**. Equivalently, for this structural matrix branch, the optimal interval-concentration constant over all admissible product laws equals the optimal constant over compact finite-fragment active product laws, while the outside law is never approximated or truncated.

This is the designated-partner result applied to a concrete inequality, not a citation-only dependency.

## 7. Translation and rough-support invariance

A deterministic translation `X=Y+h` gives

`F(Y+h)=Y^T A Y + (eta+2Ah)^T Y + constant`.                   (7.1)

The quadratic matrix `A`, hence `B`, the Schur complement `S`, and the bank curvature `s`, are unchanged. Since Theorem 4.1 is uniform in the complete affine vector, (4.2) is therefore exactly invariant under arbitrary coordinate translations. No translation magnitude enters the bound.

Likewise, Section 6 shows that arbitrary unbounded supports and arbitrarily distant or numerous fragments add no localization penalty. There is no moment assumption and no bounded-diameter reduction.

## 8. What remains open

This theorem does **not** show that every matrix with three eigenvalues of modulus at least one possesses the certificate in Theorem 4.1. The remaining structural debt is now more precise:

1. the physical indefinite pair can itself be diffuse, making `|det B| sigma_min(B)` tiny for every coordinate pair;
2. after any useful pair completion, the Schur bank may have rank greater than one on the same original coordinates, so the rank-one affine small-ball lemma cannot simply ignore the remaining same-bank quadratic curvature;
3. the three large global eigenvalues need not force a universal lower bound on `s` for one disjoint rank-one Schur bank.

The exact target family `[1] direct_sum J_m/m direct_sum (-J_m/m)` remains an important control against single-small-minor extraction. The next B14 step should aggregate higher-rank Schur curvature or prove a grouped-bank decomposition before paying any reciprocal physical-pair scale.

Full QFORM therefore remains OPEN / NOT PROVED / NOT DISPROVED. The continuous-density conclusion also remains open in the unrestricted target; Theorem 4.1 establishes only an essentially bounded density in its stated branch.

## 9. Verification notes

A direct numerical algebra check of (3.4) was run on random finite matrices: the original and completed quadratic forms agreed to floating error (`<1.5e-14`). The constant is `8sqrt(5)=17.88854381999832`. These checks are diagnostic only; the proof above is algebraic.

Changed-file privacy review is limited to this mathematical report and subsequent source-pinned handoff/receipt files. No credentials, private personal data, scheduler identifiers, signed URLs, machine paths, or unrelated material are included.
