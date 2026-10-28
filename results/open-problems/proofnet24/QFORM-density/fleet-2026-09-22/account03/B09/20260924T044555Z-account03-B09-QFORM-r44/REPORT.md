SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T04:45:55Z.
attacking: the rank-two heavy-pair near-Schur-null interpolation; keep the nonzero scalar Schur term and the entire original-coordinate Schur star simultaneously, and obtain a uniform O(interval length) bound with no loss as the scalar coefficient passes through zero.

# account03/B09 r44 — uniform scalar-star interpolation through the Schur-null face

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations  
Run: `20260924T044555Z-account03-B09-QFORM-r44`  
Status: **NEW SUPPORTING THEOREMS / NEAR-SCHUR-NULL INTERPOLATION PAID / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted owner target remains OPEN. All random coordinates used below are literal ORIGINAL coordinates. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation-independence assumption is introduced. The argument uses neither the refuted law-uniform pointwise quadratic-phase decay nor the refuted arbitrary-joint coarea/conditional-moment gates. Arbitrary same-bank quadratic curvature and outside couplings are retained exactly.

## 1. Source boundary and immediate debt


The immediate same-slot predecessor is

`yspennstate/math-open-problems@e7db74e3e49a1dd8c63a1e2024328b089018ee3c`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T031325Z-account03-B09-QFORM-r43/REPORT.md`.

That run proved the exact Schur-null aggregate-star theorem for a literal invertible indefinite physical pair, but left the nonzero near-null scalar Schur coefficient as the named debt

`QFORM-RANK2-HEAVY-PAIR-NEAR-SCHURNULL-INTERPOLATION-v1`.

The analytic receiver used here is the completed pair-log theorem

`QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`,

source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

It states: after completing a fixed literal invertible indefinite pair `B`, write

`D=|det B|`, `kappa=sigma_min(B)`.

If the exact remainder `R` satisfies, uniformly in the target level,

`P(|R-t|<rho) <= H sqrt(rho)`                                           (1.1)

for every `rho>0`, then the FULL ambient quadratic form has an essentially bounded density and

`||p_Q||_infinity <= 4 sqrt(2H) (D*kappa)^(-1/4)`.                       (1.2)

Continuity is not claimed by that receiver.

The designated partner result is account04/B09's physical-cross theorem at

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It is applied to an actual inequality in Section 8.

## 2. The scalar-star remainder

After completing a literal physical pair `H` and conditioning any coordinates outside the chosen packet, the remaining exact scalar-plus-bank piece has the form

`R = s X^2 + T(Z) X + G(Z)`,                                            (2.1)

where

* `X` is one literal original coordinate, with density at most one;
* `Z` is a disjoint bank of original coordinates, independent of `X`;
* `G` is an arbitrary measurable function for the small-ball lemma, and in the QFORM application is an arbitrary quadratic-affine polynomial;
* `T(Z)=2 m^T Z + beta` for a fixed physical Schur-star row `m` and an arbitrary scalar `beta` after outside conditioning;
* `s` is the scalar Schur coefficient and may be positive, negative, zero, tiny, or huge.

The key new point is that one can bound the small-ball probability uniformly in `s`, without deleting `sX^2`, and without taking a worst conditional slice in `Z`.

## 3. New theorem A: uniform scalar-star square-root small ball

### Theorem 3.1 — `QFORM-SCALAR-STAR-SQRT-SMALLBALL-UNIFORM-v1`

Let `X` and `Z` be independent, with `X` having density at most one. Let `T=T(Z)` have a density bounded by `M<infinity`, and let `G=G(Z)` be arbitrary measurable. For every real `s`, every `rho>0`, and every `t`,

`boxed:
 P(|s X^2 + T X + G - t| < rho)
 <= 2 sqrt(2) (sqrt(3)+1) sqrt(M rho).
`                                                                        (3.1)

Numerically,

`2 sqrt(2) (sqrt(3)+1) = 7.727406610...`.                               (3.2)

The conclusion is uniform through `s=0`; no continuity or regularity of `G` is required.

### Proof for `s=0`

For fixed `Z=z`, the event is affine in `X`. For any `eta>0`, split according to `|T|<=eta`. Since `T` has density cap `M`,

`P(|T|<=eta) <= 2 M eta`.                                               (3.3)

On `|T|>eta`, the inverse image in `X` of an interval of radius `rho` has length at most `2rho/eta`, hence probability at most that because `f_X<=1`. Therefore

`P(|TX+G-t|<rho) <= 2M eta + 2rho/eta`.                                (3.4)

Choosing `eta=sqrt(rho/M)` gives

`P(|TX+G-t|<rho) <= 4 sqrt(M rho)`,                                    (3.5)

which is stronger than (3.1).

### Proof for `s!=0`: exact near/far decomposition

Set

`delta=rho/|s|`,                                                        (3.6)

and for fixed `z` write

`s x^2 + T(z)x + G(z)-t
 = s[(x+h(z))^2-r(z)]`,                                                 (3.7)

where

`h(z)=T(z)/(2s)`,                                                       (3.8)

and `r(z)` is the corresponding real completed-square level. Its exact formula is irrelevant; crucially `r` may depend on every hidden coordinate in `Z`.

The event in `x` is

`E_r={x: |(x+h)^2-r|<delta}`.                                          (3.9)

Let

`K=min(1,2|s|M)`,                                                       (3.10)

and choose

`L=sqrt(delta/K)`.                                                      (3.11)

Because `K<=1`, `L>=sqrt(delta)`.

There are two cases, determined pointwise in `z`.

#### Near-vertex case: `r<=L^2+delta`

If the fiber is nonempty, then from (3.9)

`(x+h)^2 < r+delta <= L^2+2delta <= 3L^2`.                             (3.12)

Thus the event implies

`|X+T/(2s)| <= sqrt(3)L`.                                               (3.13)

Now `X` is independent of `T`. The scaled variable `T/(2s)` has density cap at most `2|s|M`, so the convolution

`Y=X+T/(2s)`                                                           (3.14)

has density cap at most

`||p_Y||_infinity <= min(1,2|s|M)=K`.                                 (3.15)

Therefore the total probability of ALL near-vertex fibers, even though their hidden levels `r(z)` may vary arbitrarily with `z`, is at most

`2 sqrt(3) L K`.                                                       (3.16)

This is the step that prevents the false worst-slice loss. Wide quadratic fibers can occur only near the moving vertex, and that vertex is tied to the genuine product-linear projection `T`.

#### Far-from-vertex case: `r>L^2+delta`

For fixed `z`, the fiber consists of two intervals. Its total Lebesgue length is exactly

`2[sqrt(r+delta)-sqrt(r-delta)]
 = 4delta/[sqrt(r+delta)+sqrt(r-delta)]
 <= 2delta/sqrt(r-delta)
 < 2delta/L`.                                                         (3.17)

Since `f_X<=1`, the conditional probability of every far fiber is at most `2delta/L`. Averaging over `Z` preserves this bound.

Combining (3.16) and (3.17),

`P(|R-t|<rho)
 <= 2(sqrt(3)+1) sqrt(delta K)`.                                       (3.18)

Finally,

`delta K
 = (rho/|s|) min(1,2|s|M)
 <= 2M rho`.                                                           (3.19)

Substitution into (3.18) proves (3.1). QED.

### Why the hidden quadratic curvature does not break the proof

The arbitrary function `G(Z)` only changes `r(z)`. In the near branch, the entire fiber is forced into the universal tube (3.13), whose center depends only on the genuine linear projection `T`; in the far branch, only the total one-dimensional fiber length is used. No conditional density of `T` given `G` is invoked.

This is precisely the issue that blocked the naive interpolation after r43.

## 4. Product-projection specialization

In the QFORM packet,

`T=2m^T Z+beta`.                                                       (4.1)

For independent cap-one coordinates `Z_j`, the standard sharp one-dimensional product-projection bound gives

`||p_(m^T Z)||_infinity <= sqrt(2)/||m||_2`                             (4.2)

for `m!=0`. Therefore

`||p_T||_infinity <= 1/(sqrt(2)||m||_2)`.                              (4.3)

Putting (4.3) into Theorem 3.1 yields

`boxed:
 sup_t P(|R-t|<rho)
 <= 2^(5/4)(sqrt(3)+1)
    ||m||_2^(-1/2) sqrt(rho).
`                                                                        (4.4)

The coefficient is

`2^(5/4)(sqrt(3)+1)=6.497948517819677...`.                             (4.5)

Importantly, (4.4) is valid for EVERY scalar `s`, including `s=0` and arbitrarily small nonzero `s`.

## 5. New theorem B: indefinite-pair smoothing uniform through Schur nullity

### Theorem 5.1 — `QFORM-INDEFINITEPAIR-SCHURSTAR-UNIFORM-v1`

Suppose a literal original-coordinate pair `H` has invertible indefinite principal block `B`. After completing that pair exactly, suppose the remainder has the form

`R=sX^2 + 2X m^T Z + beta X + G(Z)`                                   (5.1)

with `X` and the bank `Z` disjoint original-coordinate variables and `m!=0`. Put

`D=|det B|`, `kappa=sigma_min(B)`.                                     (5.2)

Then the FULL ambient quadratic form has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 2^(25/8) sqrt(sqrt(3)+1)
    [D kappa ||m||_2]^(-1/4).
`                                                                        (5.3)

Numerically,

`2^(25/8) sqrt(sqrt(3)+1)=14.419929007114762...`.                      (5.4)

Every interval `I` therefore obeys

`P(Q in I)
 <= 14.420 [D kappa ||m||_2]^(-1/4) |I|`.                              (5.5)

The coefficient is completely independent of the scalar Schur term `s`. Thus the estimate passes continuously, at the level of the bound, through the exact Schur-null face `s=0`; there is no `|s|^{-alpha}` singularity.

### Proof

Apply (4.4) with

`H0=2^(5/4)(sqrt(3)+1)||m||^(-1/2)`.                                  (5.6)

Then the completed pair-log theorem (1.2) gives

`||p_Q||_infinity
 <=4 sqrt(2H0)(D kappa)^(-1/4)
 =2^(25/8)sqrt(sqrt(3)+1)
   [D kappa ||m||]^(-1/4)`.                                            (5.7)

No other step is needed. QED.

This closes the exact r43 debt `QFORM-RANK2-HEAVY-PAIR-NEAR-SCHURNULL-INTERPOLATION-v1` in every subbranch where the whole physical Schur star `m` is nonzero.

## 6. Optional combined scalar-or-star certificate

The star theorem is strongest when `m` is the paid resource. If `m=0` but `s!=0`, one should instead use the scalar curvature directly.

For a one-dimensional quadratic with density-capped input, uniformly in its linear term and level,

`P(|sX^2+bX-c|<rho)
 <=2sqrt(2) |s|^(-1/2) sqrt(rho)`.                                     (6.1)

Indeed, after completing the square, the sublevel set

`{u: |u^2-r|<rho/|s|}`

has total length at most `2sqrt(2rho/|s|)`.

Let

`A0=2sqrt(2)`,
`B0=2^(5/4)(sqrt(3)+1)`,
`C0=sqrt(A0^2+B0^2)
   =7.0868423815007295...`.                                            (6.2)

For `x,y>=0`, with the natural infinite convention at zero,

`min(A0 x^(-1/2), B0 y^(-1/2))
 <= C0 (x+y)^(-1/2)`.                                                  (6.3)

Therefore whenever `|s|+||m||>0`, the remainder obeys

`sup_t P(|R-t|<rho)
 <= C0 (|s|+||m||)^(-1/2) sqrt(rho)`.                                 (6.4)

Pair-log smoothing gives the unified certificate

`boxed:
 ||p_Q||_infinity
 <= 15.059181790788745...
    [D kappa (|s|+||m||)]^(-1/4).
`                                                                        (6.5)

This handles both exact extreme strata `m=0,s!=0` and `s=0,m!=0`, as well as every interpolation between them.

## 7. Reinsert the rank-two packet algebra from r43

Use the r43 notation. Let `L={1,2,3}` be a literal triple, `J` a disjoint bank, and

`Q=Y^T P Y+2Y^T C Z+G(Z)+ell^T Y+const`,                               (7.1)

with `rank C=2`. Let `n` be a unit vector spanning `ker(C^T)` and put

`a=Pn`.                                                                (7.2)

Choose `k in L`, set `H=L\{k}`, and suppose

`B=P[H,H]`                                                             (7.3)

is invertible indefinite. Write

`p=P[H,k]`, `d=P_kk`, `C_H=C[H,J]`, `c=C[k,J]`.                        (7.4)

The exact Schur coefficients are

`s=d-p^T B^(-1)p = det(P)/det(B)`,                                    (7.5)

`m=c-p^T B^(-1) C_H`.                                                 (7.6)

If `n_k!=0`, r43 proved

`n_k m^T = - C_H^T B^(-1) a_H`                                       (7.7)

and hence

`||m|| >= sigma_2(C) ||a_H||/||B||op`.                               (7.8)

Substitute (7.8) into Theorem 5.1:

`boxed:
 ||p_Q||_infinity
 <=14.420
 [ |det B| sigma_min(B)
   sigma_2(C)||a_H||/||B||op ]^(-1/4).
`                                                                        (7.9)

Crucially, there is NO factor involving `|det P|`, `|s|`, or its reciprocal. The former singularity at

`s=det(P)/det(B) ->0`                                                  (7.10)

is gone.

The optional combined version is

`||p_Q||_infinity
 <=15.060
 [ |det B| sigma_min(B)
   ( |det P/det B|
    +sigma_2(C)||a_H||/||B||op ) ]^(-1/4).                             (7.11)

This additionally pays the case in which the Schur star becomes small but the scalar curvature remains nontrivial.

A useful exact extreme: if `a_H=0` and `a!=0`, then from the block equations

`a_k=s n_k`.                                                          (7.12)

Hence `|s|>=||a||` because `|n_k|<=1`. Thus the scalar branch alone yields

`||p_Q||_infinity
 <=15.060 [|det B|sigma_min(B)||a||]^(-1/4)`                           (7.13)

without any star lower bound.

## 8. Concrete target-valid regression and partner application

### 8.1 Nonzero-Schur regression

Take

`P_eps = [[0,1,0],
          [1,0,1],
          [0,1,eps]]`,

`C = [[ 1, 0],
      [ 0, 1],
      [-1,-1]]`,                                                     (8.1)

and the five-dimensional symmetric matrix

`A_eps=[[P_eps,C],[C^T,0_2]]`.                                        (8.2)

Choose physical pair `H={1,2}`, so

`B=[[0,1],[1,0]]`, `D=kappa=1`.                                      (8.3)

The exact Schur data are

`s=eps`,
`m=(-2,-1)`,
`||m||=sqrt(5)`,                                                      (8.4)

for every `eps`.

For the genuinely nonzero example `eps=0.1`, the checked spectrum is

`{-2.1819380327,-1.4067431338,0.5429915010,1.4551615866,1.6905280789}`. (8.5)

Thus four eigenvalues have modulus at least one; this is a valid instance of the owner target and is not an exact Schur-null example.

Theorem 5.1 gives

`boxed:
 ||p_(X^T A_0.1 X)||_infinity
 <=14.419929...*(sqrt(5))^(-1/4)
 =11.792119502145926...
`                                                                        (8.6)

for EVERY independent cap-one input law. The same constant multiplies interval length. The bound is unchanged as `eps` passes through zero.

The deterministic checker also verified `eps=0,10^-8,10^-4,0.1,1`; in all five cases the star remains exactly `(-2,-1)` and the target has at least four eigenvalues of modulus at least one.

### 8.2 Required account04/B09 result applied to an actual inequality

Account04/B09 proves: if a literal disjoint original-coordinate `3x3` cross block `K` is invertible, then, with arbitrary dense same-side curvature,

`||p_Q||_infinity <=3 |det K|^(-1/3)`,                                (8.7)

and this branch has a continuous density.

Apply it to

`A_cross = [[0,I_3],[I_3,0]]`.                                        (8.8)

The spectrum is exactly

`{-1,-1,-1,1,1,1}`                                                     (8.9)

and the literal physical cross block is `K=I_3`, so

`boxed:
 ||p_(X^T A_cross X)||_infinity <=3,
 P(X^T A_cross X in I)<=3|I|.
`                                                                        (8.10)

This is a direct application of the designated partner theorem to a target-valid inequality. Continuity holds for this partner branch.

## 9. Deterministic verification

`CHECK.py` and `CHECK_OUTPUT.txt` are saved beside this report.

They verify:

1. all displayed constants;
2. 200,000 seeded near/far sublevel configurations for the deterministic inequalities in Theorem 3.1;
3. the exact regression identities `s=eps`, `m=(-2,-1)`;
4. the spectra for the five regression values listed above;
5. the partner `K=I_3` bound.

The largest sampled ratio in the near containment check was `0.9961976327`; the far interval-length ratio was `1.00000000296`, within floating-point tolerance. All assertions passed. These finite checks support only algebra/numerics; the universal proof is the analytic argument above.

## 10. What this closes and what remains

### Closed in this run

The previous B09 debt

`QFORM-RANK2-HEAVY-PAIR-NEAR-SCHURNULL-INTERPOLATION-v1`

is closed in the precise literal-pair scope above. A nonzero scalar Schur coefficient no longer has to be deleted, frozen, or treated by a reciprocal `|s|` bound. The pair-log receiver can spend the entire physical Schur star with a constant independent of `s`, and the scalar and star can also be combined into the resource `|s|+||m||`.

This is an `O(|I|)` conclusion. The intermediate remainder estimate is square-root small-ball, but the final pair-log output is linear in interval length, so there is no square-root loss in the final density statement.

### Still open

Full QFORM is still OPEN, and full-target continuity is still OPEN.

The next B09 structural debt is

`QFORM-PAIRRESOURCE-AGGREGATE-OR-ROUTING-v1`:

starting from the three-large-eigenvalue hypothesis, force either

`|det B| sigma_min(B) (|s|+||m||)`                                    (10.1)

at universal scale for some literal indefinite pair after a product-preserving reduction, OR route the small-resource cases into the already-paid disjoint two-row crossing / third-volume / ridge / finite-core mechanisms before reciprocal physical-pair payment.

Diffuse rank-two families show that one should not expect a single physical pair resource to be universally large without such aggregation. The r43 overlap-to-disjoint-E2 compiler remains available for this next step.

## 11. Scope and review status

Claim IDs introduced here:

* `QFORM-SCALAR-STAR-SQRT-SMALLBALL-UNIFORM-v1`;
* `QFORM-INDEFINITEPAIR-SCHURSTAR-UNIFORM-v1`;
* `QFORM-INDEFINITEPAIR-SCALARSTAR-COMBINED-v1`.

Status: complete supporting analytic arguments supplied, pending independent end-to-end mathematical review. None is a full solution of the unrestricted conjecture.

Essential boundedness is proved for the stated pair branches. Continuity is not separately proved by these new pair-log branches. The account04/B09 cross-block application in Section 8.2 does have a continuous density by that theorem.
