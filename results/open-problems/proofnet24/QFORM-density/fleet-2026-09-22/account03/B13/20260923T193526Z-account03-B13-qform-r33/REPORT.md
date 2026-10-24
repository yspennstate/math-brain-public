SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T19:35:26Z.
attacking: refine the finite-hub normal form from diagonal plus symmetric rank four to diagonal plus symmetric rank two by exploiting near-symmetry of each rank-two bordered skeleton, without deleting the rough-law residual.

# account03/B13 r33 — symmetric-rank recovery and a finite-hub rank-two normal form

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws. Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **NEW PROVED DETERMINISTIC COMPLETION THEOREM + NEW TARGET-LEVEL HIGH-SLAB STRUCTURAL CONSEQUENCE / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation independence, single-interval extremality, bounded support diameter, fixed fragment count, or perturbative deletion of a small quadratic tail is used.

## 1. Fresh source state and premises

Fresh control was resolved from `yspennstate/math-research-brain` main. The initial control commit for this run was `81e68d0e18515b078c03537538a2a7c87acfb00a`; a pre-write refresh reached `f3648d6896766b9fc0cc5a3444fa42bb06f6c90e`. In both, OWNER CONTROL remained revision `2026-09-22.15`, QFORM-only, fleet enabled, account03/B13 unpaused. The full conjecture remains explicitly OPEN.

The live correction inbox was consumed, including `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`, `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1`, and the newer `QFORM-GSTAR-SCALE-FORCING-FALSE-v1`. The argument below does not invoke any of the refuted mechanisms.

### 1.1 Designated account04/B13 product purification

The completed partner result is

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

For every bounded measurable product kernel `K`,

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i`
` = sup_{|E_i|=1} int_{prod E_i} K`,                              (1.1)

and the right supremum is unchanged if each `E_i` is a bounded finite union of intervals. This is equality of suprema, not attainment. It imposes no common diameter, no fragment-count bound, no single interval, and no centered-uniform optimizer.

### 1.2 The r32 target-level currencies

The immediate predecessor is

`yspennstate/math-open-problems@8bf283fe32946ef494410d763e4852d865f225e2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T185827Z-account03-B13-qform-r32/REPORT.md`.

Let

`rho = P{X^T A X in J}/|J|`,

and assume the target spectral hypothesis `s_3(A)>=1`. Define the disjoint exterior-volume currencies

`V_r(A)=sum_{|S|=|T|=r, S cap T=empty} det A[S,T]^2`.             (1.2)

The current marginal-free projected-crossing theorem gives, with

`C_3=3*2^(4/3)*e^(1/3)=10.5501688311648...`,

`V_3(A) <=64 C_3^6 rho^(-6)`.                                   (1.3)

The source is the independently checked projected-crossing package retained at

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The first-volume target floor, with

`c_0=6 sqrt(pi)=10.6347231054331...`,

states that for `rho>c_0`, putting

`eta=1-c_0/rho`,

one has

`V_1(A) >= eta^2/4`.                                             (1.4)

The r32 proof optimized the split in `V_2` using (1.3)-(1.4) and the r31 physical-pivot completion, but its robust carrier was symmetric rank at most four. The new theorem below halves that carrier rank.

### 1.3 The exact bordered residual identity from r31

For a nonsingular disjoint physical `r x r` pivot

`B=A[S,T]`, `S cap T=empty`,

put `H=S union T`, `K=[n]\H`, and

`P=A[K,T] B^(-1) A[S,K]`.                                       (1.5)

Then `rank P<=r`. For distinct `k,l in K`, the bordered determinant formula gives

`Delta_kl := det A[S union{k}, T union{l}]`
`          = det(B)(a_kl-P_kl)`.                                 (1.6)

Define the off-diagonal residual matrix `U` by

`U_kl=a_kl-P_kl` for `k!=l`, and `U_kk=0`.                       (1.7)

Thus

`||U||_F^2 = |det B|^(-2) sum_{k!=l}|Delta_kl|^2`.               (1.8)

Under determinant-squared pivot weights

`w_ST=det(B)^2/V_r(A)`,

the counting argument from r31 gives

`E_w ||U||_F^2 <= (r+1)^2 V_{r+1}(A)/V_r(A)`.                   (1.9)

This is an inequality, not the obsolete skeleton equality corrected in the current projected-crossing addendum.

## 2. New deterministic theorem: recover symmetric rank r, not rank 2r

### Theorem 2.1 — `QFORM-SYMMETRIC-RANK-PIVOT-RECOVERY-v1`

Let `A` be a real symmetric matrix and `B=A[S,T]` any nonsingular disjoint physical `r x r` pivot. With `K,P,U` as in (1.5)-(1.8), there exist

* a diagonal matrix `D` on `K`,
* a symmetric matrix `R` on `K` with `rank R<=r`, and
* a symmetric zero-diagonal matrix `E` on `K`,

such that

`A[K,K]=D+R+E`                                                   (2.1)

and

`boxed: ||E||_F <= sqrt(2) ||U||_F.`                             (2.2)

Consequently

`boxed:
 dist_F(A[K,K], Diag+SymRank_{<=r})
 <= sqrt(2)|det B|^(-1)
    (sum_{k!=l}|det A[S+k,T+l]|^2)^(1/2).}`                      (2.3)

If `V_r(A)>0`, some nonsingular physical pivot with at most `2r` hub coordinates satisfies

`boxed:
 dist_F(A[K,K], Diag+SymRank_{<=r})
 <= sqrt(2)(r+1) sqrt(V_{r+1}(A)/V_r(A)).}`                      (2.4)

More strongly, the determinant-squared pivot average obeys

`E_w dist_F(A[K,K],Diag+SymRank_{<=r})^2`
` <=2(r+1)^2 V_{r+1}(A)/V_r(A)`.                                (2.5)

If `V_{r+1}(A)=0`, the residual is zero and the complement is exactly diagonal plus symmetric rank at most `r`.

#### Proof

Fix the pivot and abbreviate `A_K=A[K,K]`. Set

`L=(P+P^T)/2`, `K_0=(P-P^T)/2`.                                 (2.6)

Choose the diagonal matrix

`D_0=diag(A_K-L)`.

Then

`E_0=A_K-D_0-L`                                                  (2.7)

is symmetric and zero diagonal. For `k!=l`, using symmetry of `A_K`,

`(E_0)_kl`
` = a_kl-(P_kl+P_lk)/2`
` = [(a_kl-P_kl)+(a_lk-P_lk)]/2`
` = (U_kl+U_lk)/2`.                                              (2.8)

Therefore

`E_0 = sym(U)` and `||E_0||_F=||sym U||_F`.                      (2.9)

The skew part of `P` is controlled by the same bordered residual. Indeed, for `k!=l`,

`(K_0)_kl=(P_kl-P_lk)/2=(U_lk-U_kl)/2`,                         (2.10)

and the diagonal is zero. Hence

`K_0=-skew(U)`, `||K_0||_F=||skew U||_F`.                        (2.11)

Now `L` is symmetric, while `P` has rank at most `r`, and

`L-P=-K_0`.                                                       (2.12)

By Eckart--Young, the best rank-`r` approximation error to `L` is at most `||K_0||_F`, because `P` itself is a rank-`r` competitor. Since `L` is symmetric, a best rank-`r` approximation can be chosen symmetric: keep the `r` eigenvalues of `L` having largest absolute values. Call the resulting symmetric rank-at-most-`r` matrix `R`. Thus

`||L-R||_F <= ||K_0||_F = ||skew U||_F`.                         (2.13)

Write `F=L-R`. Absorb its diagonal into the diagonal part:

`D=D_0+diag(F)`,

and put

`E=E_0+offdiag(F)`.                                              (2.14)

Then (2.1) holds, `E` is symmetric and zero diagonal, and

`||E||_F`
` <= ||E_0||_F+||offdiag F||_F`
` <= ||sym U||_F+||skew U||_F`
` <= sqrt(2)(||sym U||_F^2+||skew U||_F^2)^(1/2)`
` = sqrt(2)||U||_F`.                                             (2.15)

This proves (2.2). Equation (2.3) follows from (1.8). Squaring (2.2), averaging with (1.9), and choosing one pivot proves (2.4)-(2.5). If `V_{r+1}=0`, (1.9) forces `U=0` on every positively weighted pivot, so (2.2) gives exact diagonal plus symmetric rank at most `r`. QED.

### Why this is not a perturbative deletion

The theorem is a coefficient identity/approximation in Frobenius norm. The residual `E` remains explicitly in the quadratic form. No claim is made that `X^TEX` is small for arbitrary fragmented or unbounded product laws. This distinction is essential under the live corrections.

## 3. Target-level consequence: finite hubs + symmetric rank two + sub-density-scale twist

The same optimized threshold as r32 is

`T(rho)=6 C_3^3 eta rho^(-3)`,                                  (3.1)

where `eta=1-c_0/rho`.

### Theorem 3.1 — `QFORM-FINITE-HUB-SYMRANK2-RHO32-NORMAL-FORM-v1`

Assume `s_3(A)>=1` and a slab has ratio `rho>c_0`. Then there is a set `H` of at most four **original coordinates**, with complement `K`, such that

`boxed: A[K,K]=D_K+R_K+E_K,`                                    (3.2)

where

* `D_K` is diagonal,
* `R_K` is symmetric with `rank R_K<=2`,
* `E_K` is symmetric and zero diagonal,

and

`boxed:
 ||E_K||_F
 <= K_sym eta^(-1/2) rho^(-3/2),}`                               (3.3)

with

`K_sym=8 sqrt(3) C_3^(3/2)`
`     =474.831725961637... .`                                    (3.4)

More precisely:

* if `V_2(A)>=T(rho)`, one may take `|H|<=4` and `rank R_K<=2`;
* if `V_2(A)<T(rho)`, one may take `|H|<=2` and `rank R_K<=1`.

For the convenient regime

`rho>=2c_0=12 sqrt(pi)=21.2694462108662...`,

`boxed: ||E_K||_F <=671.513466699972 rho^(-3/2).}`               (3.5)

Therefore every hypothetical counterexample sequence with `rho_m -> infinity` admits at most four physical hubs such that on the complement

`A_m=D_m+R_m+E_m`, `rank R_m<=2`, and `rho_m ||E_m||_F ->0`.      (3.6)

#### Proof

**Case A: `V_2>=T(rho)`.** Apply Theorem 2.1 with `r=2`. Using (1.3),

`||E_K||_F`
` <=3 sqrt(2) sqrt(V_3/V_2)`
` <=3 sqrt(2) sqrt(64 C_3^6 rho^(-6)/(6 C_3^3 eta rho^(-3)))`
` =8 sqrt(3) C_3^(3/2) eta^(-1/2) rho^(-3/2).`                  (3.7)

The hub set contains at most four original coordinates and the carrier has symmetric rank at most two.

**Case B: `V_2<T(rho)`.** By (1.4), `V_1>=eta^2/4>0`. Apply Theorem 2.1 with `r=1`:

`||E_K||_F`
` <=2 sqrt(2) sqrt(V_2/V_1)`
` <2 sqrt(2) sqrt([6 C_3^3 eta rho^(-3)]/[eta^2/4])`
` =8 sqrt(3) C_3^(3/2) eta^(-1/2) rho^(-3/2).`                  (3.8)

This branch has only two physical hubs and symmetric rank at most one. The same threshold balances the two cases because Theorem 2.1 multiplies both previous pivot levels by the same factor `sqrt(2)` while halving their carrier ranks.

If `rho>=2c_0`, then `eta>=1/2`, yielding (3.5). Equation (3.6) follows because `eta->1`. QED.

### Comparison with r32

r32 obtained the smaller numerical error constant

`335.756733... eta^(-1/2) rho^(-3/2)`

but only a symmetric rank-at-most-four complementary carrier. Theorem 3.1 pays exactly a factor `sqrt(2)` in residual size and reduces that carrier from rank four to rank two. In the low-`V_2` branch it reduces rank two to rank one. This is a structural rather than cosmetic improvement because rank two is exactly the threshold at which the known logarithmic and grouped-bank mechanisms become decisive.

## 4. Pivotwise rank-two tradeoff

### Corollary 4.1 — `QFORM-PIVOT-SYMRANK2-TRADEOFF-v1`

For every nonsingular disjoint physical `2 x 2` pivot `B=A[S,T]`, with `K=(S union T)^c`,

`boxed:
 |det B| dist_F(A[K,K],Diag+SymRank_{<=2})
 <= sqrt(2) sqrt(V_3(A)).}`                                      (4.1)

For every target-class slab witness, (1.3) therefore gives

`boxed:
 |det B| dist_F(A[K,K],Diag+SymRank_{<=2})
 <=8 sqrt(2) C_3^3 rho^(-3)`                                    (4.2)

with

`8 sqrt(2) C_3^3=13285.6624333179... .`                         (4.3)

#### Proof

Equation (2.3) with `r=2` contains only the bordered 3-minors extending this fixed pivot. Their squared sum is at most the complete disjoint third-volume `V_3(A)`. Insert (1.3). QED.

This avoids the false claim that one uniformly good minor must exist. It is a tradeoff for **every** nonsingular physical two-pivot.

## 5. Actual application of the designated account04/B13 result

The partner theorem (1.1) is applied here to the actual currency inequalities feeding Theorem 3.1, not merely cited as background.

Suppose arbitrary admissible cap-one densities produce slab ratio `rho>c_0`. Fix `epsilon>0` small enough that `rho-epsilon>c_0`. By account04/B13 purification, the same deterministic `A,J` admit bounded finite-union unit-product indicator witnesses with slab ratios arbitrarily close to `rho`; in particular take one with ratio at least `rho-epsilon`.

Apply the product-set form of the current crossing and first-volume estimates to that witness:

`V_3(A) <=64 C_3^6 (rho-epsilon)^(-6)`,                         (5.1)

`V_1(A) >=(1/4)(1-c_0/(rho-epsilon))^2`.                        (5.2)

The left sides depend only on `A`. Let `epsilon downarrow0`. This gives exactly (1.3)-(1.4) for the original rough-law witness with zero constant loss. The deterministic Theorem 2.1 and the optimized split then yield Theorem 3.1. At no point is a product set replaced by an interval or assigned a bounded diameter/fragment count.

Thus the partner result is used at an actual target inequality while preserving arbitrary fragmented original-coordinate laws.

## 6. What this closes and what remains

The unrestricted QFORM conjecture remains **OPEN / not proved / not disproved**. The separate global continuity conclusion remains **OPEN**.

The structural survivor is now narrower than in r32:

* at most four named original-coordinate hubs;
* on their complement, an arbitrary diagonal plus a **symmetric rank-at-most-two** carrier;
* a symmetric zero-diagonal residual `E` with `rho ||E||_F ->0` along any hypothetical diverging slab-ratio sequence.

The small Frobenius residual still cannot be thrown away: on arbitrarily translated/fragmented supports, coefficient-small does not imply random-error-small. The new first B13 obligation is

`QFORM-FINITE-HUB-SYMRANK2-SUBDENSITY-TWIST-GLUE-v1`:

combine the rank-two carrier with the physical hubs and the retained `o(1/rho)` zero-diagonal twist by a product-preserving grouped/projected-crossing or slab-conditioned-core argument. A valid closure should either route the twist into a genuinely paid third smoothing direction or prove a translation-uniform stability statement; it must not perturbatively delete `E`.

The fresh account03/B08 Pythagorean Schur-area theorem is potentially compatible with this reduced carrier because it prevents orthogonal leakage from cancelling rank-two post-Schur area, but no full glue implication is claimed here.

## 7. Deterministic constant check

Using

`C_3=3*2^(4/3)*e^(1/3)`, `c_0=6*sqrt(pi)`,

one obtains

`K_sym=8*sqrt(3)*C_3^(3/2)=474.83172596163683...`,

`sqrt(2)K_sym=671.5134666999717...`,

and

`8*sqrt(2)*C_3^3=13285.66243331791...`.

A sibling checker records these values and tests the linear-algebra inequality on deterministic random examples; those finite checks support the algebra but are not proof of the theorem.
