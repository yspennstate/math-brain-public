SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B19, 2026-09-24T04:45:22Z.
attacking: the pair-plus-rank-two-Schur interface — turn fleet02/B19's physical-rank-two fractional smoothing into an actual L^infinity receiver through a literal indefinite physical pair, then identify the exact algebraic boundary where that receiver has zero currency.

# fleet01/B19 r12 — pair-log + rank-two Schur receiver and disjoint-tetrad rigidity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not claimed by the new receiver; full-target continuity remains OPEN**.

All random coordinates below are literal ORIGINAL coordinates. No random variable is rotated. The laws are arbitrary independent real probability densities bounded by one; no moments, centering, iid, support, smoothness or log-concavity assumption is introduced. All coefficient tails, same-bank curvature, extra spectrum and affine terms are retained.

## 1. Fresh source graph and completed inputs actually used


The designated partner theorem used at equation level is fleet02/B19

`yspennstate/math-open-problems@f4d95bc33caf8db11888cceb817c005484f67d31`,

`QFORM-PHYSICAL-R2-FRACTIONAL-SMOOTHING-v1`.

For any literal physical cross block `M=A[I,J]`, with

`Z_2=e_2(M^T M)>0`,

it gives for the FULL ambient quadratic law, including arbitrary self blocks, outside couplings, affine terms, signs and extra spectrum,

`H_(1/4):=sup_s E |Q-s|^(-1/4) <= C_R2 Z_2^(-1/16)`,              (1.1)

where

`C_R2=3.9291317704497634871249193093...`.                         (1.2)

The completed physical indefinite-pair logarithmic transducer is source-pinned at

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`.

If two original coordinates have an invertible indefinite principal block `B`, put

`D=|det B|`, `kappa=sigma_min(B)`.                                (1.3)

After completing that pair, if the exact untouched remainder is `R`, then for every `r>0`, almost everywhere in `t`,

`p_Q(t) <= 2 sqrt(2)/r`
`          +D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`                (1.4)

The pair shifts may depend arbitrarily on all remainder variables. This is precisely the interface needed below.

The newest partner stress/correction is fleet02/B19

`yspennstate/math-open-problems@c5347df59a4adcea406d9fa8ca0c88186670d731`.

It exhibits an exact target family with spectrum `{2,-2,1}` whose curved two-bank partial output has a logarithmically unbounded density, even though the FULL target is paid once the third square is retained jointly. This forbids scalarizing an arbitrary curved rank-two two-bank core before spending the third resource. Section 6 below checks that the new theorem respects this obstruction exactly.

## 2. General fractional-small-ball version of the physical-pair logarithmic transducer

### Theorem 2.1 — `QFORM-PAIRLOG-FRACTIONAL-SMALLBALL-TRANSDUCER-v1`

Assume the setting of (1.3)-(1.4). Suppose for some `alpha>0` and `H<infinity`,

`sup_s P{|R-s|<rho} <= H rho^alpha` for every `rho>0`.             (2.1)

Then `Q` has an essentially bounded density and

`||p_Q||_infinity`
` <=(2alpha+1) B_alpha^(1/(2alpha+1))`
`       *[sqrt(2)/(alpha)]^(2alpha/(2alpha+1)),`                  (2.2)

where

`B_alpha=(H/alpha) 2^alpha D^(-1/2) kappa^(-alpha)`.              (2.3)

Equivalently, at `alpha=1/4`,

`boxed: ||p_Q||_infinity`
` <=3*2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6).`                    (2.4)

#### Proof

For `a>0`, layer cake and (2.1) give

`E log_+(a/|t-R|)`
` = integral_0^infinity P{|t-R|<a e^(-v)} dv`
` <= H a^alpha integral_0^infinity e^(-alpha v)dv`
` = (H/alpha)a^alpha.`                                           (2.5)

Put `a=2r^2/kappa` in (1.4):

`p_Q(t)<=A r^(-1)+B_alpha r^(2alpha)`, `A=2sqrt(2)`.              (2.6)

The exact minimizer satisfies

`r^(2alpha+1)=A/(2alpha B_alpha)`.                                (2.7)

Substitution gives (2.2). For `alpha=1/4`, direct simplification gives (2.4). No density or independence assumption on `R` was used; only the original physical pair is conditioned. QED.

This strengthens the source pair-log theorem's `alpha=1/2` use in a direction needed by the partner's new `H_(1/4)` estimate.

## 3. New L^infinity receiver: indefinite physical pair + rank-two Schur crossing

Let the two selected literal coordinates be `T`, and write an arbitrary affine quadratic form as

`q(x)=x^T A x+b^T x+c`,

with the original-coordinate block decomposition

`A=[[B,C],[C^T,D_0]]`,                                           (3.1)

where `B=A[T,T]` is invertible indefinite and the complementary coordinates are `U=T^c`.

Completing the physical pair is exact:

`h(x_U)=Cx_U+b_T/2`,

`q=(x_T+B^(-1)h)^T B (x_T+B^(-1)h)+R(x_U)`,                     (3.2)

where

`R(x_U)=x_U^T S x_U + beta^T x_U+c_0`,                           (3.3)

`S=D_0-C^T B^(-1)C`,                                             (3.4)

`beta=b_U-C^T B^(-1)b_T`,                                        (3.5)

`c_0=c-(1/4)b_T^T B^(-1)b_T`.                                   (3.6)

Thus the remainder variables are still independent ORIGINAL coordinates and their quadratic coefficient is the literal Schur matrix `S`; no coefficient is thrown away.

Take any disjoint original-coordinate banks `I,J subset U` and put

`M=S[I,J]`,

`Z_2=e_2(M^T M)`.                                                 (3.7)

### Theorem 3.1 — `QFORM-PHYSICAL-PAIR-PLUS-R2-SCHUR-LINFINITY-v1`

If `Z_2>0`, then

`boxed: ||p_q||_infinity`
` <= C_* D^(-1/3) kappa^(-1/6) Z_2^(-1/24),`                    (3.8)

where

`C_*=3*2^(4/3) C_R2^(2/3)`
`   =18.823150365416575003...`.                                  (3.9)

If `sigma_1>=sigma_2` are the two largest singular values of `S[I,J]`, then

`boxed: ||p_q||_infinity`
` <=18.823151 D^(-1/3) kappa^(-1/6)`
`                   *(sigma_1 sigma_2)^(-1/12).`                 (3.10)

#### Proof

Apply the completed fleet02/B19 theorem (1.1) to the ACTUAL remainder (3.3), including its affine vector `beta`, arbitrary self-curvature in `S[I,I]`,`S[J,J]`, every coordinate outside `I union J`, and every extra spectral direction. It gives

`H_(1/4)(R)<=C_R2 Z_2^(-1/16)`.                                  (3.11)

Markov's inequality gives the exact small-ball consequence

`sup_s P{|R-s|<rho}<=H_(1/4)(R) rho^(1/4)`.                      (3.12)

Insert (3.11) into Theorem 2.1 with `alpha=1/4`. This gives (3.8). Cauchy-Binet gives

`Z_2>=sigma_1^2 sigma_2^2`,                                      (3.13)

which gives (3.10). QED.

This is a true density receiver, not merely a fractional-potential estimate. It handles both signs of the Schur crossing and all repeated/singular extra modes. Exact zero diagonals in `B` are allowed as long as `B` is invertible indefinite. No continuity conclusion is added.

## 4. Original-coordinate aggregate version: incident physical four-volume

The theorem above can be stated without selecting one Schur minor or one Schur cut.

For the same physical pair `T`, define the **disjoint incident four-volume**

`W_T = sum det A[T union I, T union J]^2`,                         (4.1)

where the sum is over all ordered pairs of disjoint two-subsets

`I,J subset U`, `|I|=|J|=2`, `I intersect J=emptyset`.             (4.2)

Every determinant in (4.1) is a literal original-coordinate nonprincipal `4 x 4` minor of the actual coefficient matrix.

### Lemma 4.1 — exact bordered-Schur four-minor identity

For every such `I,J`,

`det A[T union I,T union J]=det(B) det S[I,J]`.                   (4.3)

Consequently

`W_T=D^2 W_dis(S)`,                                               (4.4)

where

`W_dis(S)=sum_(I intersect J=emptyset) det S[I,J]^2`.             (4.5)

#### Proof

In the indicated row/column order the minor is

`[[B,C_J],[C_I^T,D_0[I,J]]]`.

Schur's determinant formula gives (4.3) with the exact Schur block (3.4). Squaring and summing gives (4.4). QED.

### Lemma 4.2 — physical cut paving

There is a literal bipartition `U=R disjoint_union C0` such that

`e_2(S[R,C0]^T S[R,C0]) >= W_dis(S)/16`.                         (4.6)

#### Proof

Independently assign every physical coordinate of `U` to `R` or `C0` with probability `1/2`. For each ordered disjoint `(I,J)` in (4.5), the event `I subset R`, `J subset C0` has probability `1/16`. On that event its squared minor appears in the Cauchy-Binet sum for the left side. Therefore the expected left side equals `W_dis(S)/16`; one deterministic cut attains at least the expectation. QED.

Combining Lemmas 4.1-4.2 with Theorem 3.1 gives a fully aggregate physical receiver.

### Theorem 4.3 — `QFORM-INDEFINITE-PAIR-INCIDENT4VOLUME-RECEIVER-v1`

If `W_T>0`, then

`boxed: ||p_q||_infinity`
` <= C_4 D^(-1/4) kappa^(-1/6) W_T^(-1/24),`                    (4.7)

where

`C_4=2^(1/6) C_*`
`   =21.1282719148008113...`.                                    (4.8)

Indeed (4.6) and (4.4) give

`Z_2>=W_T/(16D^2)`,                                               (4.9)

and substitution into (3.8) gives (4.7).

Equivalently the dimensionless payment currency is

`J_T:=D^6 kappa^4 W_T`;                                          (4.10)

then

`||p_q||_infinity <= C_4 J_T^(-1/24)`.                           (4.11)

This is useful for proof assembly because it pays **aggregate** original-coordinate fourth-order volume incident on a physical pair; no single good `4 x 4` minor is required.

## 5. Exact zero-currency boundary: disjoint tetrad rigidity

The vanishing boundary `W_T=0` also has rigid deterministic structure.

### Theorem 5.1 — `QFORM-DISJOINT-TETRAD-RIGIDITY-v1`

Let `S=S^T` be any finite real symmetric matrix. If

`det S[I,J]=0`                                                     (5.1)

for every disjoint two-subsets `I,J`, then there are a diagonal matrix `Delta` and a symmetric matrix `K` with

`boxed: S=Delta+K, rank K<=2.`                                    (5.2)

The conclusion includes all zero patterns and all signs.

#### Proof

Build the graph `G` on the physical coordinates, putting an edge `ij` exactly when `S_ij !=0`, `i!=j`.

**Case 1: `G` has no triangle.** If it contained two vertex-disjoint edges `ij` and `kl`, the minor with rows `{i,k}` and columns `{j,l}` would give

`S_ij S_kl=S_il S_kj`,                                           (5.3)

so both `il` and `kj` would be edges. The minor with rows `{i,l}` and columns `{j,k}` would then force both `ik` and `lj` to be edges, creating a triangle. Hence a triangle-free `G` has no two disjoint edges. It follows that all edges share one common center `c` (or there are no edges). Put `z_c=0`, `z_i=S_ci` for `i!=c`. Then

`K=e_c z^T+z e_c^T`                                              (5.4)

has rank at most two and agrees with every off-diagonal entry of `S`. Hence `S-K` is diagonal.

**Case 2: `G` contains a triangle `a,b,c`.** Any vertex connected to one of `a,b,c` is connected to all three: for example the disjoint minor with rows `{a,b}` and columns `{c,i}` gives

`S_ac S_bi=S_ai S_bc`,                                           (5.5)

and the analogous partition gives the third edge. If an outside vertex were incident only to another outside vertex, that edge would be disjoint from the triangle edge `ab`; the Case-1 two-disjoint-edge calculation forces connections back to the triangle. Finally two nonisolated outside vertices `i,j` are adjacent because

`S_ab S_ij=S_aj S_ib`                                            (5.6)

and the right side is nonzero. Thus all nonisolated vertices form one complete graph; every other vertex is isolated.

Let

`epsilon=sign(S_ab S_ac S_bc) in {+1,-1}`.                       (5.7)

Choose real nonzero `x_a,x_b,x_c` so that

`S_ab=epsilon x_a x_b`, `S_ac=epsilon x_a x_c`,
`S_bc=epsilon x_b x_c`;                                          (5.8)

for instance take

`x_a=sqrt(|S_ab S_ac/S_bc|)`,
`x_b=S_ab/(epsilon x_a)`, `x_c=S_ac/(epsilon x_a)`.              (5.9)

For every other nonisolated `i`, set

`x_i=S_ai/(epsilon x_a)`,                                        (5.10)

and put `x_i=0` on isolated vertices. Equations (5.5) and (5.6) show successively that

`S_ij=epsilon x_i x_j` for every `i!=j`.                         (5.11)

Thus `K=epsilon x x^T` has rank one and matches all off-diagonal entries; again `S-K` is diagonal. This proves (5.2). QED.

So the exact failure of the incident-four-volume receiver is not an amorphous matrix: after pair completion the entire remainder is **physical diagonal + rank at most two**.

## 6. Application to the newest fleet02/B19 obstruction

The newest partner family `c5347df...` has exact rank three and spectrum `{2,-2,1}`. Take any invertible physical pair `B` in that family. Block Gaussian elimination gives the exact rank identity

`rank A = rank B + rank S`,                                       (6.1)

hence

`rank S=3-2=1`.                                                   (6.2)

Therefore

`Z_2(S[I,J])=0` for every physical cut and `W_T=0` exactly.       (6.3)

Thus Theorems 3.1 and 4.3 **do not** claim to pay that family by prematurely scalarizing the curved two-bank output. Instead it lands precisely on the zero-currency low-rank boundary of Theorem 5.1. This matches the partner's explicit logarithmic two-bank singularity.

The partner then pays the FULL family only by retaining the genuine third `W` square inside the checked three-Fresnel theorem, obtaining

`||p_Q||_infinity <=12*4^(-1/3)=7.559526299...`,                 (6.4)

with a continuous `C_0` density. This is the correct order of smoothing and is preserved here.

For higher-rank survivors the new receiver is genuinely stronger: whenever a physical indefinite pair leaves any quantitative disjoint rank-two Schur volume, the branch is now paid by (4.7), with arbitrary same-bank curvature and nonzero coefficient tails retained.

## 7. Compact conditional proof assembly after this run

A correction-aware conditional proof of the full theorem can now be written as follows.

1. Use the completed same-constant principal-minimal descent in ORIGINAL coordinates. This preserves all input laws and coefficient tails.
2. Apply the already completed diagonal, principal-localized, physical-`E3/E5`, ridge/window, Fresnel/frame, pair-log, half-Riesz, grouped-bank, null-coloop and physical-pair receivers only in their exact recorded scopes.
3. In the strong physical rank-two crossing frontier, use fleet02/B19 `f4d95bc...` to obtain the full ambient `H_alpha`, in particular (1.1), without deleting same-bank curvature.
4. Whenever a literal indefinite physical pair survives and its Schur remainder has positive disjoint rank-two cross currency, Theorem 4.3 upgrades that fractional smoothing to an actual `L^infinity` density bound.
5. If the incident currency is exactly zero, Theorem 5.1 forces the Schur remainder to `physical diagonal + rank<=2`; the newest fleet02/B19 stress confirms that this boundary is real and that one must retain the third target resource jointly rather than scalarize a curved two-bank output.

The current fleet03/B19 r49 compiler independently reduces a major adaptive-rank-two survivor to

`physical diagonal + rank<=16 carrier + two high-spectrum-diffuse self residuals + retained 2^-16 cross tail`,

or to explicit self-star / small-Pluecker / giant-near-rank-one branches. The new theorem supplies a clean additional exit from any of those states once an indefinite physical pair leaves quantitative Schur two-volume.

## 8. First essential missing inequality after this run

The remaining structural/analytic splice can now be stated sharply as

`QFORM-PAIR-INCIDENT4VOLUME-OR-DIAG-R2-JOINT-THIRD-PAYMENT-v1`:

> In every still-unpaid principal-minimal survivor with `s_3(A)>=1`, either force a literal indefinite physical pair `T` with the aggregate currency
>
> `J_T=|det B_T|^6 sigma_min(B_T)^4 W_T`
>
> bounded below by one universal positive constant (then (4.11) pays the law), or route quantitatively to the `W_T approx 0` geometry and spend the resulting physical-diagonal-plus-rank-two Schur structure **jointly with the retained third target resource** through an already-paid Fresnel/grouped/ridge/volume receiver.

The exact zero endpoint is now proved by Theorem 5.1. What is still missing is a **dimension-free quantitative stability/coverage statement** through small but nonzero `W_T`, without dividing by one tiny minor or anchor. The newest partner stress shows why the alternative joint-third-resource branch is mandatory: exact rank-three examples have `W_T=0` for every invertible pair and nevertheless satisfy the target by a three-direction joint Fresnel payment.

Parallel branches already tracked by the fleet — giant near-rank-one crossings, small-Pluecker aggregate geometry, explicit aligned self-stars, finite low-rank carriers and arbitrary-extra-spectrum coupling — remain open unless another completed receiver applies. Nothing in this report declares those branches solved.

## 9. Scope and corrections preserved

- No arbitrary-joint coarea estimate is used.
- No conditional-density-supremum or positive conditional-moment gate is used.
- No independence is asserted after spectral rotation.
- No law-uniform pointwise quadratic-phase decay is used.
- No single uniformly good physical minor is assumed; Theorem 4.3 is aggregate.
- A small coefficient matrix is never deleted as a small random error.
- The rank-two logarithmic singularity is retained and explicitly appears in the partner stress.
- Signs, repeated eigenvalues, exact zero diagonals, singular extra modes and arbitrary affine terms are included in the stated scopes.

Full unrestricted bounded-density theorem: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full unrestricted continuity theorem: **OPEN**.
