SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T21:27:39Z.
attacking: rank-free overlap-two receiver: derive a marginal-free first-compound product-Fourier square-root small-ball estimate and combine it with the exact indefinite-pair logarithmic envelope.

# fleet01/B04 r20 — first-compound product Fourier pays a rank-free overlap-two indefinite pair

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: `SUPPORTING_THEOREMS_PROVED / OVERLAP2_RESIDUAL_RANK_RESTRICTION_REMOVED_FOR_ONE_PAIR / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Continuity in the new branch: **not claimed; an essentially bounded density is proved**.  
Independent review: **pending**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

No random variable is rotated. No moment, support, Gaussian, log-concavity, connected-support, pointwise scalar quadratic-phase decay, arbitrary-joint coarea bound, or conditional projection-density moment is used. The argument stays in disjoint banks of the original independent coordinates.

## 1. Fresh source boundary

Immediately before the substantive write, `math-research-brain` main was refreshed at commit

`bae85d53f4e024ee3fe11f7c48ce6ebce8f40985`.


Pinned mathematical inputs:

1. `QFORM-GROUPED-CROSSING-EXACT-SUBSET-ENTROPY-v1`, `yspennstate/math-open-problems@13f0b0b271b4e230cb5493e887ed5ec7dd65f63b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T181304Z-fleet01-B04-QFORM-auto11-r16/REPORT.md`. Its pre-integration product-Fourier characteristic-function estimate is valid before the final `d>2` time integral.
2. `QFORM-CANONICAL-COMPOUND-PROMOTION-v1`, `yspennstate/math-open-problems@d5e114f4a9f515344575756615fce3a754195b13`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B04/20260923T185132Z-fleet01-B04-QFORM-auto11-r17/REPORT.md`. It gives the exact promotion identity `S_+^2 Z_{ell-1}^+=alpha_h S^2 Z_ell` and the terminal physical-hub Fourier estimate.
3. `QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1` / `QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1`, `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, path `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`. For an invertible indefinite physical pair `B`, `D=|det B|`, `kappa=sigma_min(B)`, it gives the conditional logarithmic density envelope and the transducer `Q_R(rho)<=H sqrt(rho) => ||p_Q||_infinity<=4 sqrt(2H)(D kappa)^(-1/4)`.
4. The overlap-two exact pair-Schur identity `W_H^(2)=det(B_H)^2 ||S_H||_F^2` from fleet03/B07, `yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T000734Z-fleet03-B07-qform-r20/REPORT.md`.
5. Designated partner fleet02/B04 theorem `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1`, `yspennstate/math-open-problems@00e728cf7f226ccce4b41ad751d494c5c94f67ec`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T111930Z-qform/REPORT.md`. It is applied to the same explicit matrix in Section 6.

## 2. Marginal-free first-compound Fourier envelope

Let `U=(U_i)_(i in I)` and `V=(V_j)_(j in J)` be two disjoint banks of original independent coordinates, all scalar densities at most one. Let

`R=q_I(U)+2 U^T N V+q_J(V)+linear+constant`,                    (2.1)

where `q_I,q_J` are arbitrary real quadratic forms and

`Z_1=E_1(N)=||N||_F^2>0`.                                      (2.2)

### Theorem 2.1 — `QFORM-FIRSTCOMPOUND-CROSS-FOURIER-PROMOTION-v1`

For every real `t`,

`boxed:
 |phi_R(t)|
 <= min{1,
          2^(3/4) sqrt(pi) Z_1^(-1/4) |t|^(-1/2)}.}`            (2.3)

No rank assumption is made on `N` and no row-marginal condition remains.

### Proof

Use the canonical physical one-volume law on rows of `N`:

`nu({i})=||n_i||_2^2/Z_1`,                                     (2.4)

so its inclusion marginal is simply

`alpha_i=||n_i||_2^2/Z_1`.                                    (2.5)

If every `alpha_i<=1/2`, apply the exact-subset product-Fourier estimate from the r16 source with `k=0`, `ell=1`. For a one-subset law the exact fixed-cardinality entropy factor is `F_1=1`, and the canonical determinant/entropy currency is exactly `G=Z_1`. The pre-integration estimate gives

`|phi_R(t)|
 <=min{1,2^(3/4) sqrt(pi) Z_1^(-1/4)|t|^(-1/2)}.`              (2.6)

Suppose instead that some row `h` has `alpha_h>1/2`. Promote the **original scalar coordinate** `U_h` into the physical hub, exactly as in `QFORM-CANONICAL-COMPOUND-PROMOTION-v1`. Because `ell=1`, the promotion terminates immediately, and the base-times-height identity is

`S_+^2=alpha_h Z_1`.                                            (2.7)

The terminal one-dimensional physical-hub crossing estimate from the same source gives

`|phi_R(t)|
 <=min{1,2^(1/4)sqrt(pi)(alpha_h Z_1)^(-1/4)|t|^(-1/2)}`
` <min{1,2^(1/2)sqrt(pi)Z_1^(-1/4)|t|^(-1/2)}.`                (2.8)

The coefficient in (2.8) is smaller than the balanced coefficient in (2.6). Hence (2.3) holds in both cases. The promotion changes only which **original coordinate** is regarded as the hub; it does not rotate any random variable, and arbitrary same-bank curvature is allowed by the grouped theorem. QED.

The important point is that first-compound energy gives only a `|t|^{-1/2}` envelope, which is not time-integrable and is not enough for a bounded density by itself. It is instead exactly the square-root small-ball currency needed by the indefinite-pair logarithmic transducer.

## 3. Fourier envelope to a translation-uniform square-root small-ball estimate

For `rho>0` and `x in R`,

`1_{|x|<rho} <= exp(v) exp(-v x^2/rho^2)`                       (3.1)

for every `v>0`. Fourier inversion of the Gaussian gives

`exp(-v x^2/rho^2)
 = [rho/(2 sqrt(pi v))]
   integral_R exp(-rho^2 t^2/(4v)) exp(itx) dt.`                (3.2)

Apply (3.1)-(3.2) to `x=R-a`, take absolute values, and use (2.3). Put

`K=2^(3/4)sqrt(pi)Z_1^(-1/4)`.                                 (3.3)

Using only the power part `|phi_R(t)|<=K|t|^(-1/2)`, which is valid for every `t!=0`,

`P(|R-a|<rho)
 <= exp(v) [rho/(2sqrt(pi v))]
    K integral_R exp(-rho^2 t^2/(4v)) |t|^(-1/2) dt.`           (3.4)

The exact gamma integral is

`integral_R exp(-rho^2 t^2/(4v)) |t|^(-1/2)dt
 =sqrt(2) v^(1/4) rho^(-1/2) Gamma(1/4).`                       (3.5)

Therefore

`P(|R-a|<rho)
 <= [exp(v)Gamma(1/4)/(sqrt(2pi)v^(1/4))] K sqrt(rho).`         (3.6)

The factor `exp(v)v^(-1/4)` is minimized at `v=1/4`. Substituting (3.3) yields the clean translation-uniform estimate

### Theorem 3.1 — `QFORM-FIRSTCOMPOUND-CROSS-SQRT-SMALLBALL-v1`

`boxed:
 sup_a P(|R-a|<rho)
 <= H_1 Z_1^(-1/4) sqrt(rho),
 H_1=2^(3/4) exp(1/4) Gamma(1/4).}`                              (3.7)

Numerically `H_1=7.832957...`; no numerical value is used in the proof. Equation (3.7) is valid for every `rho>0`; if its right side exceeds one the inequality is simply nonsharp.

This is an integrated/rearranged product-space consequence. It does **not** imply or use law-uniform pointwise quadratic-phase decay for a scalar input.

## 4. Rank-free indefinite pair plus first-compound Schur energy

Let `H={h_1,h_2}` be two original coordinates. Write the physical pair block

`B=A[H,H]`,                                                      (4.1)

and assume `B` is invertible and indefinite. Put

`D=|det B|>0`, `kappa=sigma_min(B)>0`.                           (4.2)

Condition on any original coordinates outside `H disjoint_union I disjoint_union J`. After completing the physical pair, write

`Q=((X_H)+m(U,V))^T B((X_H)+m(U,V))+R(U,V)`,                    (4.3)

where `I,J` are disjoint original-coordinate banks and the `I-J` cross block of the exact pair-Schur residual is `N`. Let

`Z_1=||N||_F^2>0`.                                              (4.4)

### Theorem 4.1 — `QFORM-INDEFINITE-PAIR-FIRSTCOMPOUND-RANKFREE-v1`

Uniformly over all outside conditioning,

`boxed:
 ||p_Q||_infinity
 <= C_* (D kappa)^(-1/4) Z_1^(-1/8),
 C_*=2^(23/8) exp(1/8) sqrt(Gamma(1/4))
     =15.8284571657... .}`                                      (4.5)

Equivalently,

`||p_Q||_infinity
 <=15.829 (D kappa)^(-1/4) Z_1^(-1/8).`                         (4.6)

No rank assumption is made on the Schur complement or on `N`.

### Proof

By Theorem 3.1, the full residual `R(U,V)`, including arbitrary same-bank quadratic terms and arbitrary affine terms created by outside conditioning, obeys

`sup_a P(|R-a|<rho)
 <=H sqrt(rho),
 H=H_1 Z_1^(-1/4).`                                             (4.7)

The pair-log theorem permits the completed shifts `m(U,V)` to depend arbitrarily on the residual variables and says precisely that (4.7) implies

`||p_Q||_infinity
 <=4 sqrt(2H)(D kappa)^(-1/4).`                                 (4.8)

Substituting `H_1=2^(3/4)e^(1/4)Gamma(1/4)` gives

`4 sqrt(2H_1)
 =2^(23/8)e^(1/8)sqrt(Gamma(1/4))`,                             (4.9)

which is (4.5). The estimate is uniform in the outside conditioning, so averaging the conditional densities proves the full ambient statement. QED.

The homogeneity is exact: under `A -> cA`, `D kappa -> |c|^3 D kappa` and `Z_1 -> c^2 Z_1`, so the right side of (4.5) scales as `|c|^(-1)`.

### Scope and relation to overlap-two third-compound energy

For an invertible physical pair `H`, fleet03/B07 gives

`W_H^(2)=D^2 ||S_H||_F^2`,                                     (4.10)

where `S_H` is the exact pair-Schur complement. Theorem 4.1 pays any branch where a disjoint original-coordinate cut of `S_H` carries first-compound cross energy `Z_1`. In particular, it removes the former requirement that the residual Schur form be exact rank one. It does **not yet** convert the aggregate sum over many physical pairs into one uniformly conditioned pair, and it does not by itself pay a Schur complement whose entire Frobenius energy is diagonal. Those are recorded as the remaining overlap-two aggregation debt in Section 7.

The proof of (4.5) is an essential-supremum density proof. It does not furnish an `L^1` characteristic function, so continuity is **not claimed** for this new branch.

## 5. Fully dense genuinely rotated indefinite stress family

Fix `0<epsilon<=10^(-2)`. Let

`B=[[1,3],[3,1]]`.                                               (5.1)

Then `B` is indefinite with eigenvalues `4,-2`,

`D=8`, `kappa=2`.                                                (5.2)

Let

`V=I_4-(1/2)J_4`,                                               (5.3)

which is an orthogonal Householder matrix with every entry equal to `+/-1/2`, and put

`N_epsilon=diag(2,epsilon,epsilon,epsilon)V`.                    (5.4)

Every one of the sixteen physical entries of `N_epsilon` is nonzero, and its singular values are exactly

`2,epsilon,epsilon,epsilon`.                                    (5.5)

Hence

`Z_1=||N_epsilon||_F^2=4+3epsilon^2`,                           (5.6)

while

`E_3(N_epsilon)=12epsilon^4+epsilon^6`.                          (5.7)

Set `eta=1/100`, `delta=1/1000`, `u=(1,1)`, `v=(1,-1)`. Let `E` be the `8 x 2` matrix whose first four rows are `delta u` and whose last four rows are `delta v`. Define

`S_epsilon=[[eta J_4,N_epsilon],
            [N_epsilon^T,eta J_4]]`,                             (5.8)

`C_epsilon=S_epsilon+E B^(-1) E^T`,                             (5.9)

and the full ten-dimensional symmetric matrix

`A_epsilon=[[B,E^T],
            [E,C_epsilon]].`                                    (5.10)

Because

`B^(-1)=[[-1/8,3/8],[3/8,-1/8]]`,                              (5.11)

we have

`u^T B^(-1)u=1/2`, `v^T B^(-1)v=-1`, `u^T B^(-1)v=0`.           (5.12)

Therefore every physical entry of `A_epsilon` is nonzero: the two-by-two block and all entries of `E` are nonzero, the first residual same-side block has entries `eta+delta^2/2`, the second has entries `eta-delta^2`, and the residual cross block is exactly `N_epsilon`.

More importantly, the exact Schur complement of the physical pair `B` is **exactly** `S_epsilon`, so the cross block entering Theorem 4.1 is exactly `N_epsilon`.

### Target spectral certificate

Let

`A_0=diag(B, [[0,N_epsilon],[N_epsilon^T,0]])`.                  (5.13)

Its spectrum contains

`4,-2,+2,-2`,                                                   (5.14)

in addition to the six values `+/-epsilon`, so it has four singular values at least two. The perturbation satisfies

`||A_epsilon-A_0||_op
 <=4eta+||E||_op+||E B^(-1)E^T||_op`
` <=1/25+sqrt(8)delta+4delta^2`
` <0.042833.`                                                    (5.15)

Here `||E||_op=sqrt(8)delta` and `||B^(-1)||_op=1/2`. By singular-value perturbation, `A_epsilon` therefore has at least four eigenvalues of modulus greater than

`2-0.042833>1.957>1`.                                           (5.16)

Thus (5.10) is a fully dense, non-diagonal, genuinely indefinite member of the exact owner target for every `0<epsilon<=10^(-2)`.

Theorem 4.1 gives, for every admissible cap-one product input law,

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <= C_* 16^(-1/4)(4+3epsilon^2)^(-1/8).}`                       (5.17)

At `epsilon=10^(-6)`, the right side is

`6.655046444819971...`.                                         (5.18)

The bound stays finite as the three small residual singular values tend to zero. This is the intended rank-free feature.

## 6. Designated fleet02/B04 result applied to the same matrix

Condition the two physical pair coordinates in (5.10). Because of the exact orthogonality `u^T B^(-1)v=0`, the retained four-by-four cross block between the two residual original-coordinate banks is still exactly `N_epsilon`.

There are exactly four active rows. For any probability law on physical row triples, the sum of the four row marginals is three, so some row marginal is at least `3/4`. Therefore the designated partner theorem `QFORM-FRACTIONAL-SUPPORT-DEFECT-COMPLETE-EXIT-v1` applies. Its four-row support-defect branch gives the actual inequality

`boxed:
 ||p_(X^T A_epsilon X)||_infinity
 <=6*4^(1/6)(12epsilon^4+epsilon^6)^(-1/6),
 p in C_0.}`                                                     (6.1)

At `epsilon=10^(-6)`, this is

`49960.99065933556...`.                                         (6.2)

On this same target-valid matrix, the new first-compound/pair-log certificate (5.18) is smaller by the factor

`7507.233957506526...`.                                         (6.3)

The comparison does not claim that (6.1) is the partner's globally optimal possible method. It establishes the required equation-level application of a completed partner theorem and illustrates the complementary scaling: the partner's third-volume currency pays the three tiny residual directions, while the new receiver uses only the target-scale first-compound mass left after the indefinite pair.

## 7. Exact remaining implication

The new theorem removes **residual-rank loss for one invertible indefinite overlap-two physical pair**. The remaining structural debt is now

`QFORM-OVERLAP2-AGGREGATE-PAIR-ROUTING-v1`:

> Starting from the overlap-two colored packet `P_2>=1/512` supplied by the third-compound overlap theorem, aggregate over its many physical shared pairs without choosing one dimension-dependent tiny pair. Either produce target-scale combined currency for an invertible indefinite pair together with a disjoint first-compound Schur cut so that Theorem 4.1 applies, or route the mass into (i) definite-pair shells, (ii) the exact singular-pair zero-self star factorization, or (iii) a predominantly diagonal Schur receiver. Do this before paying reciprocal `det(B_H)` or `sigma_min(B_H)` factors and retain arbitrary extra spectrum.

Thus the full conjecture is **not solved**. The advance is analytic: once a genuine indefinite pair is available, the residual no longer needs exact rank one or any lower bound on its second/third/etc. singular values; aggregate first-compound cross energy is enough.

## 8. Audit notes

- No pointwise scalar van-der-Corput claim is made. The pointwise bound (2.3) is for the **full product-space quadratic form** and is proved by the grouped product-Fourier theorem plus physical promotion.
- The false arbitrary-joint coarea theorem and false positive conditional projection-density moment are not used.
- The new correction on arbitrary-remainder slope innovation is respected: the whole Schur remainder is controlled by (3.7).
- No Monte Carlo or histogram is used in any universal claim.
- Continuity is proved for the partner branch (6.1) but is not proved by the new pair-log branch (4.5).
- Full target remains open and would require the aggregate overlap-two routing above together with the other overlap classes.
