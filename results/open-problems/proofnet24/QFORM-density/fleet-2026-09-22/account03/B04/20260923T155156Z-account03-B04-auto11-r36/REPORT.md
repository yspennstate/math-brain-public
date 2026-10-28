SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-23T15:51:56Z.
attacking: dilute a single near-coloop third-volume hub by a residual second-compound law, preserving original-coordinate product structure and explicit constants.

# account03/B04 r36 — one-hub 3+2 lower-compound dilution

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Outcome: `NEW_SUPPORTING_THEOREM + EXPLICIT_ROTATED_INDEFINITE_BOUND + PEER_RESULTS_APPLIED / FULL_TARGET_OPEN`  
Continuity: proved on the theorem branch below (`C_0` density); full-target continuity remains open.

## 1. Fresh controls and mathematical sources


The main analytic input is this slot's completed finite-family theorem

- `QFORM-MULTI-COMPOUND-FOURIER-MIXTURE-v1`,
- `yspennstate/math-open-problems@8df80736853803f472ba6662c9c4a07e7801dfdb`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T124716Z-account03-B04-auto11-r33/REPORT.md`.

For compound families of orders `k_l`, weights `theta_l`, average order `s=sum theta_l k_l`, allocated determinant currencies `Z_l`, and mixed row marginals at most `q/2` with `1<=q<s/2`, it proves

`||p_Q||_infinity
 <= [e s/((s-2q)sqrt(q))]
    [prod_l theta_l^(theta_l)]^(1/(2s))
    prod_l Z_l^[-theta_l/(2s)]`,

with `p_Q in C_0(R)`, while arbitrary same-bank curvature, outside couplings and induced affine terms are retained.

Two completed peer results are applied to the same displayed matrix for comparison:

1. account01/B04 `QFORM-THIRDVOLUME-GIBBS-DUAL-AND-SOFT-HUB-v1`, source `math-open-problems@da8e2c011cc93a5c776a1de6010f7366da5f2fbf`, which gives `2.853602893356842...` on the `L=32` matrix below at `h=3/5`;
2. account02/B04 `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`, source `math-open-problems@febf0c97f0f85e802b6bc2ab4a475c15109de013`, whose exact-rank-three product-Plancherel endpoint gives the conditional bound `3` after conditioning the physical hub on the same matrix.

The designated partner `account04/B04` still had no completed current-QFORM canonical handoff/report at the final direct lookup, so no designated-partner theorem is invented or waited for.

## 2. New theorem — `QFORM-ONE-HUB-3PLUS2-DILUTION-v1`

Let `I,J` be disjoint ORIGINAL-coordinate banks and `M=A[I,J]`. Fix a physical hub row `h in I`.

Choose an allocated order-three minor family with total currency

`Z3 = sum c3(S,T) det(M[S,T])^2 >0`,

supported only on row triples `S` containing `h`. Let its normalized row marginals be `alpha_i^(3)`. Thus automatically `alpha_h^(3)=1`. Assume

`alpha_i^(3) <= 1/2` for every `i!=h`.                         (2.1)

Choose an allocated order-two minor family with total currency

`Z2 = sum c2(S,T) det(M[S,T])^2 >0`,

supported only on row pairs avoiding `h`, and let its row marginals be `alpha_i^(2)`. Assume

`alpha_i^(2) <= 1/2` for every `i`.                            (2.2)

The allocation functions obey the no-double-counting requirement of r33 within each compound order. Because the two families have different orders, their determinant-expansion terms are distinct.

Then the full ambient quadratic form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= 5 e 2^(-1/5) (Z3 Z2)^(-1/10).
`                                                                    (2.3)

### Proof

Use the r33 theorem with exactly two families and equal mixture weights

`theta_3=theta_2=1/2`.

The mixed row marginal at the hub is

`alpha_h=(1/2)*1+(1/2)*0=1/2`.                                 (2.4)

For every nonhub row,

`alpha_i=(alpha_i^(3)+alpha_i^(2))/2 <=1/2`.                   (2.5)

The average compound order is

`s=(3+2)/2=5/2`.                                                (2.6)

Hence `q=1` is admissible because `1<s/2=5/4`. Substituting `s=5/2`, `q=1`, and equal weights into the r33 formula gives

`e*(5/2)/(1/2) * [(1/2)^(1/2)(1/2)^(1/2)]^(1/5)
 * Z3^(-1/10) Z2^(-1/10)`

`=5 e 2^(-1/5)(Z3 Z2)^(-1/10)`,

which is (2.3). The imported proof has `phi_Q in L^1`, hence `p_Q in C_0(R)`. QED.

### Interpretation

The theorem pays a literal or near-coloop order-three packet without forcing the third-volume law itself below the strict `3/4` marginal wall. The hub is diluted by one lower compound order rather than by selecting a small physical minor. The remaining cost is aggregate: an incident third-volume currency and a hub-avoiding second-volume currency.

The condition is deliberately product-coordinate: the physical hub remains an original independent coordinate, and no eigenbasis rotation of the random variables is used.

## 3. Dense genuinely rotated indefinite target

Use the fully dense one-hub family from the completed account01/B04 soft-hub report. Let

`V=I_4-(1/2)J_4`,

which is orthogonal. Let

`s1=(1,1,1), s2=(1,-1,-1), s3=(-1,1,-1), s4=(-1,-1,1)`.

For `L>0`, let `R_L` be the `5 x 4` matrix whose first row is `L e1` and whose remaining rows are `(0,s1),...,(0,s4)`. Put

`M_L=R_L V`.                                                    (3.1)

For `L=32`, explicitly

`M_32 = [[ 16, -16, -16, -16],
         [-3/2,-1/2,-1/2,-1/2],
         [ 1/2, 3/2,-1/2,-1/2],
         [ 1/2,-1/2, 3/2,-1/2],
         [ 1/2,-1/2,-1/2, 3/2]].`                              (3.2)

Every physical cross coefficient is nonzero. Since `V` is orthogonal and

`R_L^T R_L=diag(L^2,4,4,4)`,                                   (3.3)

the singular values of `M_L` are exactly

`L,2,2,2`.                                                      (3.4)

Define the full symmetric matrix

`A_L = [[J_5/100, M_L],
        [M_L^T,    J_4/100]].`                                  (3.5)

Every entry of `A_L` is nonzero. The pure cross matrix `A_L^0` obtained by deleting the two same-bank blocks has spectrum

`{+L,-L,+2,+2,+2,-2,-2,-2,0}`.                                (3.6)

The same-bank perturbation in (3.5) has operator norm

`max(5/100,4/100)=1/20`.                                       (3.7)

Therefore Weyl's inequality gives, at `L=32`, eight eigenvalues of `A_32` with absolute value at least

`2-1/20=39/20>1`.                                              (3.8)

So this is a genuinely rotated, fully dense, indefinite instance of the owner's exact spectral target. The product-Fourier theorem retains the nonzero same-bank blocks rather than treating them as random perturbations.

## 4. Exact compound geometry on `M_L`

Call physical row `0` the hub and rows `1,2,3,4` the light rows.

### 4.1 Hub-incident third volume

For every row triple `S` containing row `0`, exact Gram computation gives

`det(M_L[S,*] M_L[S,*]^T)=8L^2`.                               (4.1)

There are `C(4,2)=6` such triples, so taking all full `3 x 3` determinant terms with incident row triples gives

`Z3 = 6*(8L^2)=48L^2`.                                         (4.2)

All six row triples have equal aggregate determinant weight. Conditional on this incident third-volume family, each light row belongs to exactly three of the six triples. Hence

`alpha_0^(3)=1`,
`alpha_i^(3)=3/6=1/2`, `i=1,2,3,4`.                            (4.3)

### 4.2 Hub-deleted second volume

For every pair of distinct light rows,

`det(M_L[S,*]M_L[S,*]^T)=8`.                                   (4.4)

There are six such pairs. Taking all full `2 x 2` determinant terms on the light rows gives

`Z2=6*8=48`.                                                    (4.5)

The normalized row-pair law is uniform on the six pairs, so each light row belongs to exactly three and

`alpha_i^(2)=1/2`, `i=1,2,3,4`,
`alpha_0^(2)=0`.                                                (4.6)

Thus every hypothesis of Theorem 2 is exactly saturated.

## 5. New explicit density estimate

Theorem 2 gives for every independent cap-one product law

`||p_(X^T A_L X)||_infinity
 <= 5 e 2^(-1/5) (2304 L^2)^(-1/10)`.                          (5.1)

At `L=32`,

`2304 L^2 = 2^18 3^2`,                                         (5.2)

so (5.1) simplifies exactly to

`boxed:
 ||p_(X^T A_32 X)||_infinity
 <= 5e/(4*3^(1/5))
 = 2.727597250352086... .
`                                                                    (5.3)

The density is continuous and vanishes at infinity.

This is an all-laws estimate: no Gaussianity, moment, bounded-support, connected-support, log-concavity or identical-distribution assumption is used.

## 6. Actual applications of completed peer results

### 6.1 account01/B04 Gibbs-soft-hub theorem

On this exact `M_32`, account01/B04's completed Gibbs optimizer at `h=3/5` has exact currency

`G_(3/5)=5120*2^(2/5)=6755.880503157...`                        (6.1)

and gives

`||p_(X^T A_32 X)||_infinity
 <= 2.853602893356842...`.                                     (6.2)

Thus the new lower-compound dilution estimate is not a bibliography-only citation; applied to the same inequality it improves the completed peer Gibbs bound by about `4.4%`:

`2.72759725035 < 2.85360289336`.                               (6.3)

The mechanism differs: Gibbs reweights third volume only, while Theorem 2 spends half of its Fourier exponent on the hub-deleted second compound.

### 6.2 account02/B04 exact-rank-three endpoint

Condition on the single original hub coordinate `X_0`. The remaining light-row cross block has singular values `2,2,2`, hence exact rank three and

`E3(M_{light,*})=2^2*2^2*2^2=64`.                              (6.4)

All effects of the conditioned hub become allowed affine/same-bank terms. account02/B04's completed exact-rank-three product-Plancherel endpoint therefore gives uniformly in the conditioned value

`||p_(Q | X_0)||_infinity <= 6*64^(-1/6)=3`.                   (6.5)

Averaging yields `||p_Q||_infinity<=3`. The new product-Fourier mixture again improves this actual peer inequality, to (5.3), without conditioning away the hub.

## 7. What changed in the proof map

The previous B04 soft-hub/Gibbs branch said poor admissible third-volume currency forces a bounded physical compound hub, but the retained higher-rank packet still needed payment without a tiny local reciprocal. Theorem 2 supplies one concrete payment interface:

> a single physical third-volume hub can be neutralized at the exact `q=1` Fourier threshold by a balanced hub-deleted second-compound law.

This is useful precisely near a coloop, where pure third-volume weighting has hub marginal close to one. It also shows that lower-compound mixing can outperform entropy reweighting of the same compound order on a target-valid dense matrix.

What is NOT proved is that every one-hub or at-most-four-hub survivor automatically has a second-compound law satisfying (2.2) with target-scale `Z2`. A residual second-compound support graph may itself be star/triangle-like or have poor entropy currency. The next precise B04 implication is therefore

`QFORM-SOFTHUB-E2-GIBBS-OR-TWOFRAME-ENDPOINT-v1`:

construct an entropy-optimized hub-deleted `E2` law with row marginals at most `1/2` and dimension-free currency, or show that failure quantitatively forces the residual two-frame star/triangle geometry into the already-paid exact-rank-three / mixed-hub / pair endpoint.

Full QFORM remains OPEN. Full-target continuity remains OPEN separately.
