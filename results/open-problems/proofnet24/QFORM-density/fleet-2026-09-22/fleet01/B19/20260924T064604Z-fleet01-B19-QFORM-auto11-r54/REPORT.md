SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B19, 2026-09-24T06:46:04Z.
attacking: the principal-minimal maximal-coloop / physical-hub-star interface; retain the genuine third source and pay it jointly with the hub rather than scalarizing the curved rank-two partial law.

# fleet01/B19 r54 — physical hub + one-square Fresnel receiver, with a six-leaf leverage compiler

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Status: **ESSENTIAL_STEP_APPLIED / NEW COMPLETE SUPPORTING RECEIVER / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native authenticated brain ingestion.  
Continuity: the receiver proved below has an `L^1` characteristic function and therefore a continuous `C_0` density in its stated branch. Full-target continuity remains open.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random variable is rotated and then declared independent. Input coordinates are arbitrary independent real variables with densities bounded by one; no moments, centering, iid, compact support, log-concavity, connected support, or smoothness is assumed. Signs and repeated/degenerate spectral values are allowed exactly as stated. Arbitrary outside quadratic coefficients and affine terms are retained.

## 1. Source-pinned inputs and correction boundary

The completed analytic input is Theorem H (Fresnel--Brascamp--Lieb) from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

In the notation of that theorem, physical hub coordinates `H`, a physical receiver bank `I`, and arbitrary outside coordinates `J` are allowed. On `I`, the quadratic block may be

`A_II = sum_{k<=r} lambda_k v_k v_k^T + D`,

with `D` diagonal in the physical independent coordinates. The blocks `A_HH,A_HJ,A_IJ,A_JJ` are arbitrary. If the augmented physical row frame made from the `v_k` coordinates and hub couplings has normalized leverage at most `1/2`, Theorem H gives the stated product-Fourier decay.

The designated partner fleet02/B19 supplies the fresh maximal-coloop stress at

`yspennstate/math-open-problems@95e4f4427f21a599f0e4fd8f21e9a60e76e88fb3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260924T061029Z-fleet02-B19-QFORM-r53/PRINCIPAL_MINIMAL_ADDENDUM.md`.

Its principal-minimal target family has spectrum `{1,-1,1}`, cross-SVD hub leverage exactly one, literal hub-star norm `1/2`, arbitrarily small scalar/pair/triple physical pivots, and **zero** pair-Schur rank-two currency for every invertible physical pair. Yet its full three-frame leverage is exactly `1/2` and Theorem F pays the full law by `<=12`. The same source records that the curved two-bank partial output has a logarithmically unbounded density for centered product uniforms. Therefore the star branch must keep a genuine third resource through the smoothing step; neither scalarization of the two-bank core nor positive pair-Schur `E2` forcing is valid universally.

This report preserves that correction and exhibits a second full-law receiver for exactly that zero-pair-Schur endpoint.

## 2. New receiver: one literal hub plus one retained rank-one square

### Theorem 2.1 — `QFORM-PHYSICAL-HUB-ONE-SQUARE-FRESNEL-LINFINITY-v1`

Let `h` be one original coordinate, let `I` be a disjoint set of original coordinates, and put all remaining coordinates in `J`. Assume only that, on `I`,

`A[I,I] = D + lambda v v^T`,                                      (2.1)

where `D` is diagonal in the original coordinates, `lambda!=0`, and `v in R^I`. Put

`c=A[I,h]`,                                                        (2.2)

and define the physical two-frame Gram

`G = sum_{i in I} q_i q_i^T
   = [[||v||_2^2, <v,c>], [<v,c>, ||c||_2^2]],
 q_i=(v_i,c_i)^T`.                                                 (2.3)

Assume `G` is positive definite and every physical row satisfies

`ell_i = q_i^T G^(-1) q_i <= 1/2`.                               (2.4)

Then the FULL ambient quadratic polynomial

`Q(X)=X^T A X + b^T X + d`                                       (2.5)

has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 12*2^(-2/3) (|lambda| det G)^(-1/3)
 = 7.559526299369239... (|lambda| det G)^(-1/3).`                 (2.6)

No assumption is made on `A_hh`, `A[h,J]`, `A[I,J]`, `A[J,J]`, or on the affine vector `b`.

#### Proof

Apply the completed Theorem H with one hub, `H={h}`, and one Fresnel square, `r=1`, on the physical bank `I`. Its augmented row vectors are exactly `q_i=(v_i,c_i)`, so its Gram is (2.3), and (2.4) is precisely the theorem's normalized leverage hypothesis. The theorem gives

`|phi_Q(t)|
 <= (2|t|)^(-1) (4 pi |t lambda|)^(-1/2)
    (4 pi)^2 (det G)^(-1/2)`                                     (2.7)

for `t!=0`. Thus

`|phi_Q(t)| <= K |t|^(-3/2)`,                                    (2.8)

where

`K = ((4 pi)^(3/2)/2) (|lambda| det G)^(-1/2)`.                  (2.9)

Together with `|phi_Q|<=1`,

`integral_R |phi_Q(t)| dt
 <= integral_R min(1,K|t|^(-3/2)) dt
 = 6 K^(2/3)`.                                                     (2.10)

Fourier inversion therefore gives

`||p_Q||_infinity
 <= (1/(2 pi)) 6 K^(2/3)
 = 12*2^(-2/3)(|lambda|det G)^(-1/3)`,                            (2.11)

which is (2.6). The same `L^1` bound gives a continuous density vanishing at infinity. The sign of `lambda` is irrelevant because only `|lambda|` enters the Fresnel factor. QED.

The theorem is deliberately formulated with arbitrary outside couplings. Conditioning on `X_J` is not needed to erase them; Theorem H already retains them. Equivalently, conditioning on `X_J` only creates arbitrary linear translations on the hub and receiver bank, which the source theorem treats uniformly.

## 3. A product-preserving two-frame peel

The exact leverage gate (2.4) can be generated from any nondegenerate physical hub-square frame by conditioning at most six exceptional leaves.

### Theorem 3.1 — `QFORM-HUB-SQUARE-TWOFRAME-PEEL-v1`

Keep (2.1)-(2.3) and assume `G>0`. Whiten the two-frame by

`z_i=G^(-1/2)q_i`,                                                (3.1)

so

`sum_i z_i z_i^T=I_2`, `sum_i ||z_i||^2=2`.                      (3.2)

Declare

`H_0={i:||z_i||^2>2/7}`, `L=I\H_0`.                              (3.3)

Then `|H_0|<=6`. Put

`M_L=sum_{i in L} z_i z_i^T`.                                    (3.4)

Exactly one of the following alternatives holds.

**A. Diffuse receiver branch.** If

`lambda_min(M_L)>=4/7`,                                           (3.5)

then, after conditioning the at-most-six variables `X_{H_0}` together with all outside variables that one wishes to condition, the remaining literal hub-plus-light-bank form satisfies Theorem 2.1. More precisely, with

`G_L=sum_{i in L}q_iq_i^T`,                                      (3.6)

one has

`det G_L >= (4/7)^2 det G`                                       (3.7)

and every `i in L` obeys

`q_i^T G_L^(-1)q_i <=1/2`.                                       (3.8)

Consequently the full unconditional law satisfies

`boxed:
 ||p_Q||_infinity
 <= 12 (49/64)^(1/3) (|lambda| det G)^(-1/3)
 < 10.977918 (|lambda| det G)^(-1/3).`                            (3.9)

This branch has a continuous `C_0` density.

**B. Finite physical-leaf branch.** If (3.5) fails, then the same set `H_0`, of cardinality at most six, carries more than `3/7` of one whitened coefficient direction: there exists `y in S^1` such that

`sum_{i in H_0} <z_i,y>^2 >3/7`,                                 (3.10)

and hence some literal physical coordinate `i in H_0` satisfies

`boxed: |<z_i,y>|>1/sqrt(14).}`                                  (3.11)

No density claim is made from (3.11) alone; it is a finite original-coordinate localization of the combined hub-star/third-square frame.

#### Proof

The cardinality statement follows from (3.2): seven rows each of squared norm `>2/7` would have total squared norm `>2`. For (3.5),

`G_L=G^(1/2) M_L G^(1/2)`,                                       (3.12)

so (3.7) follows from `det M_L>=(4/7)^2`. For `i in L`,

`q_i^T G_L^(-1)q_i
 = z_i^T M_L^(-1)z_i
 <= (7/4)||z_i||^2
 <=1/2`,                                                          (3.13)

which proves (3.8). Conditioning `H_0` merely turns its interactions with the surviving variables into affine terms, while the surviving self block remains `D_LL+lambda v_Lv_L^T`; hence Theorem 2.1 applies. Combining (2.6) with (3.7) gives (3.9).

If (3.5) fails, choose a unit `y` with `y^T M_Ly<4/7`. Since the full whitened Gram is `I_2`,

`sum_{i in H_0}<z_i,y>^2 = 1-y^TM_Ly >3/7`.                      (3.14)

There are at most six terms, so one exceeds `(3/7)/6=1/14`, proving (3.11). QED.

This is the same optimal `2/7` versus `4/7` two-dimensional leverage geometry used in the fresh fleet03/B19 compiler, but here it is applied to the **actual augmented hub-square frame** that Theorem H consumes. It therefore produces an endpoint `L^infinity` theorem, not only a fractional potential.

## 4. Designated partner fleet02/B19 applied at an actual inequality

Consider the partner's whole one-parameter aligned family

`A_a = a(l1 l2^T+l2 l1^T)+w w^T`,                               (4.1)

where

`l1=e_h+v1`, `l2=u+v2`,                                          (4.2)

and `u,v1,v2,w` are flat unit vectors on four pairwise disjoint size-`m` physical banks. Since `l1,l2,w` are mutually orthogonal, with `||l1||=||l2||=sqrt(2)`, the nonzero spectrum is

`{2a,-2a,1}`.                                                     (4.3)

Thus `|a|>=1/2` is a full target family.

Choose the physical decomposition

`H={h}`, `I=V2 union W`, `J=U union V1`.                          (4.4)

On the actual receiver bank,

`A_a[I,I]=w w^T`,                                                 (4.5)

so Theorem 2.1 has `lambda=1`, `v=w`, and diagonal part zero. The actual hub coupling is

`c=A_a[I,h]=a v2`.                                                (4.6)

Because `v2` and `w` have disjoint physical supports,

`G=diag(1,a^2)`, `det G=a^2`.                                    (4.7)

For every coordinate of `V2` or `W`, the normalized row leverage is exactly `1/m`. Hence for `m>=2`, (2.4) holds and

`boxed:
 ||p_{X^T A_a X}||_infinity
 <= 12*2^(-2/3)|a|^(-2/3).}`                                    (4.8)

In particular, throughout the target range `|a|>=1/2`,

`boxed: ||p_{X^T A_a X}||_infinity <=12.}`                       (4.9)

At the partner's principal-minimal endpoint `a=1/2`, (4.9) is exactly `12`. At the earlier unscaled stress `a=1`, (4.8) gives

`12*2^(-2/3)=7.559526299369239...`,                              (4.10)

matching the full three-eigenframe payment.

This is an equation-level application to the designated partner's hardest zero-pair-Schur example. It pays the full law while preserving all of the coefficients which make the curved two-bank partial output singular. In particular, the troublesome couplings between `V2` and the conditioned bank `V1`, and between the hub and `U`, are not set to zero: they are among the arbitrary `A_IJ` and `A_HJ` blocks permitted by Theorem H. The proof works for every admissible product law, not only the uniform law used to exhibit the logarithmic singularity of the partial output.

Therefore the partner obstruction has a precise positive interpretation:

> a maximal cross-SVD coloop is not itself bad when the retained third source and the physical hub form a diffuse two-dimensional augmented coefficient frame; the correct currency is `|lambda| det G`, not pair-Schur `E2` and not the density of the curved two-bank partial form.

## 5. Compact conditional proof assembly after this run

The currently source-valid proof tree can be summarized without claiming completion.

1. Principal-minimal descent removes every proper physical principal block already carrying three target eigenvalues, without changing the desired universal constant.
2. Existing diagonal, physical-pair, pair-log, half-Riesz, physical-`E3`, ridge/window, grouped-square, and completed Fresnel/Brascamp--Lieb receivers pay their exact certified branches while keeping original-coordinate product provenance.
3. The fleet03/B19 strong-rank-two compiler gives either a robust light-light rank-two crossing with normalized two-plane leverages `<=1/2` and the completed fleet02/B19 full-law fractional resource `H_(1/4)<12.787535`, or a fixed original-coordinate hub-star `>0.004160698...`.
4. The designated fleet02/B19 r53 stress proves that the hub-star branch cannot be closed by forcing an invertible physical pair, positive pair-Schur rank-two currency, or bounded density of the curved two-bank partial output.
5. Theorem 2.1 above closes a genuine portion of that hub-star branch: whenever the retained third source can be kept on a physical receiver bank as one rank-one square plus physical diagonal and its augmented `(third vector, hub-star)` Gram has a diffuse leverage realization, the whole ambient law is paid directly. Theorem 3.1 shows that failure of this diffuse gate can be localized to at most six physical leaves.

The first new local obligation on the star side is therefore

`QFORM-R51-HUBSTAR-THIRDSOURCE-TWOFRAME-MANUFACTURE-v1`:

> starting from the actual principal-minimal r51 hub-star survivor, either manufacture an original-coordinate receiver bank `I` and retained third source whose self block is `D+lambda vv^T` (or a source-valid extension of Theorem H allowing the actual residual), with `|lambda| det G` at universal scale after the six-leaf peel, or route the finite-leaf failure to an already-paid physical pair, volume, ridge/window, grouped-star, or induction gate. The nonzero remaining coefficients may not be deleted.

The robust r51 light-light branch remains the parallel obligation

`QFORM-BL-DIFFUSE-R2-WITH-RETAINED-TAIL-AND-THIRD-SOURCE-ENDPOINT-v1`:

convert its `H_(1/4)` resource plus the retained third/high-spectrum source to an endpoint density bound without generic interpolation and without losing product provenance.

Thus the unrestricted theorem is still **OPEN**. This run removes neither of those two final synthesis debts, but it does remove the partner's exact maximal-coloop/zero-pair-Schur family as an obstruction: that family is now paid directly through a literal hub-plus-third-square receiver, with the full target endpoint bounded by `12` and continuity proved in that branch.

## 6. Quantifiers and degeneracies

Theorem 2.1 is sign-free in `lambda`; `A_hh` may vanish; all outside blocks may be singular or arbitrary; repeated eigenvalues cause no issue. The only algebraic nondegeneracy is `G>0`. If `G` is singular, the augmented hub-square coefficient frame has rank at most one and is intentionally left as a separate degenerate branch rather than divided by. Theorem 3.1 likewise branches before any inverse of a singular restricted Gram. Every probabilistic statement is uniform over arbitrary independent cap-one densities and arbitrary affine terms.

No claim of a full proof, a universal sharp constant, or a full continuity theorem is made.
