SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-22T23:11:37Z.
attacking: aggregate third-compound product-Fourier smoothing after a physical square pivot, avoiding threshold selection of three separate cross singular values

# fleet01/B04 r20 — aggregate exterior-volume half-Riesz smoothing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control observed before publication:** owner revision `2026-09-22.15`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture is **not** proved here. The new square-assisted branch gives an essentially bounded density. Continuity is not proved by that branch alone. Some comparison branches below (the source-pinned ridge / volume-Fourier bounds) do give a continuous representative in their stated scopes.

## 1. Conditional end-to-end route and the first debt attacked

Fix an original coordinate `Z` with a nonzero physical scalar pivot and complete its square:

`Q = a (Z+d(Y))^2 + R(Y)`,  `a != 0`,

where `Y` consists of the other original independent coordinates. The completed shift `d(Y)` may depend on all residual variables. The latest completed fleet02/B04 theorem gives a half-Riesz interface for `R` in terms of the full regularized determinant of any disjoint original-coordinate cross block `B` of the residual quadratic form. The prior threshold corollary paid this route by first selecting `r` singular values all at least a common `sigma`. This can lose logarithmically or worse when cross energy is diffuse over many unequal singular directions.

The first missing implication attacked here is therefore:

> **aggregate before thresholding:** replace the `r`-singular-values-above-`sigma` payment by an exact elementary-symmetric / exterior-volume currency `E_k(B)=e_k(s_1(B)^2,s_2(B)^2,...)`, and compare that currency on the **same physical matrix** with the newest volume-sampling and ridge certificates.

This is an analytic implication only. The still-unpaid global structural task is to force one of these currencies from the bare hypothesis `s_3(A)>=1` without assuming a good local pivot/minor/cut.

## 2. Source-pinned inputs actually used

### 2.1 Designated partner result, fleet02/B04

I use the completed theorem `QFORM-SQUARE-WEIGHTED-DETERMINANT-HALFRIESZ-v1` from

`yspennstate/math-open-problems@6155d85896070c87f6523a30646c38ac10be43a9`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260922T201618Z-fleet02-B04-qform-r13/REPORT.md`.

At its unconditional `q=2` endpoint, if `B` is a disjoint original-coordinate residual cross block, then

`||p_Q||_infinity <= |a|^(-1/2) J_2(B)`,                                      (2.1)

where

`J_2(B) = (1/sqrt(2 pi)) integral_R |t|^(-1/2)
          det(I + 4 t^2 B B^T/(pi^2 e^2))^(-1/8) dt`.                          (2.2)

No leverage hypothesis is present at `q=2`; arbitrary residual self-quadratic terms, outside couplings and the correlated square shift remain allowed. This is the named OTHER-account result applied below.

### 2.2 Newest owner-required Claude source

I also use the current owner-required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

Its relevant proved statements are:

* `D'`: for third cross volume `E_3(B)` and volume-sampling row marginal at most `h<3/4`, a continuous density bound

  `6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) E_3(B)^(-1/6)`

  in the displayed `h>=1/2` parameterization (and the original `6sqrt(e) E_3^(-1/6)` bound when the marginal is at most `1/2`);
* `D_5`: with no marginal condition,

  `||p_Q||_infinity <= 5 sqrt(2e) E_5(B)^(-1/10)`.                            (2.3)

The same source explicitly keeps the full conjecture open.

For the ridge comparison I use the earlier B04 theorem `QFORM-O0-EFFECTIVE3-ADAPTIVE-Q-v1`, canonical at

`yspennstate/math-open-problems@ae419b8c9d837cc4c31eb86b3bcf9cfe7be3e721`.

At the scale where the ridge effective dimension is three, if the maximum physical ridge leverage is `ell_*<3/4`, with `q_*=max(1,2 ell_*)`, it gives the continuous-density estimate

`||p_Q||_infinity <= [3e/(sqrt(2q_*)(3-2q_*))] E_3(B)^(-1/6)`.                (2.4)

## 3. Main theorem: aggregate `E_k`, no singular-value threshold

For a real matrix `B`, write

`E_k(B)=e_k(s_1(B)^2,s_2(B)^2,...)`.

Equivalently, by Cauchy-Binet,

`E_k(B)=sum_{|P|=|Q|=k} det(B[P,Q])^2`.                                        (3.1)

### Theorem 3.1 — `QFORM-SQUARE-EK-HALFRIESZ-v1`

Under the hypotheses of (2.1), for every integer `k>=3` with `E_k(B)>0`, the law of `Q` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity <= C_k |a|^(-1/2) E_k(B)^(-1/(4k)),`                        (3.2)

where

`C_k = [sqrt(e)/(2k)] Beta(1/(4k), 1/8 - 1/(4k)).`                            (3.3)

The first constants are

`C_3 = 9.840655864922018...`,
`C_4 = 6.556148716529986...`,
`C_5 = 5.464743450762853...`,
`C_6 = 4.920327932461009...`.

This theorem retains all arbitrary quadratic leakage already allowed by the partner theorem. It does **not** assert continuity.

#### Proof

Put `x_j=s_j(B)^2` and `c=4/(pi^2 e^2)`. The determinant in (2.2) has the exact expansion

`det(I+c t^2 B B^T)=prod_j(1+c t^2 x_j)
                   =sum_{r>=0}(c t^2)^r e_r(x)`.                              (3.4)

All terms are nonnegative, hence for every fixed `k`,

`det(I+c t^2 B B^T) >= 1+(c t^2)^k E_k(B)`.                                  (3.5)

Insert (3.5) in (2.2). With `A=c^k E_k(B)`,

`J_2(B) <= (1/sqrt(2pi)) integral_R |t|^(-1/2)(1+A t^(2k))^(-1/8) dt`.         (3.6)

For `t>0`, substitute `u=A t^(2k)`. Then

`t^(-1/2)dt = (1/(2k)) A^(-1/(4k)) u^(1/(4k)-1) du`,

so, using both half-lines,

`integral_R ... dt
 = (1/k) A^(-1/(4k))
   Beta(1/(4k), 1/8-1/(4k)).`                                                 (3.7)

The beta integral is finite exactly when `k>2`. Finally

`A^(-1/(4k))/sqrt(2pi)
 = c^(-1/4) E_k(B)^(-1/(4k))/sqrt(2pi)
 = (sqrt(e)/2) E_k(B)^(-1/(4k))`.                                             (3.8)

Combining (2.1), (3.7), and (3.8) proves (3.2)-(3.3). QED.

### 3.2 Variational volume-weight form

Let `Delta_(P,Q)=det(B[P,Q])^2` over nonzero `k x k` minors and let `w` be any probability distribution on those minors. Define

`V_k(w)=exp(H(w)+sum_(P,Q) w_(P,Q) log Delta_(P,Q))`.                         (3.9)

The log-sum inequality gives

`V_k(w) <= sum Delta_(P,Q)=E_k(B)`,                                           (3.10)

with equality for the volume weights

`w_(P,Q)=Delta_(P,Q)/E_k(B)`.                                                 (3.11)

Therefore the best member of the entire weighted-minor family (3.9) is exactly the unthresholded `E_k` certificate used in (3.2). This is the requested volume-weight optimization: no choice of a common minor threshold or of `r` individually large singular values is needed.

## 4. Random-cut identity: aggregate first, choose a physical cut second

For a symmetric matrix `S` and integer `k`, define the disjoint compound mass

`D_k(S)=sum_{P,Q: |P|=|Q|=k, P cap Q=emptyset} det(S[P,Q])^2`,                 (4.1)

where `(P,Q)` is ordered. Choose a random physical bipartition `I sqcup J` by assigning each coordinate independently to `I` or `J` with probability `1/2`, and put `B=S[I,J]`.

### Lemma 4.1 — exact cut average

`boxed: E_I E_k(S[I,J]) = 4^(-k) D_k(S).`                                     (4.2)

#### Proof

By (3.1), `E_k(S[I,J])` is the sum of `det(S[P,Q])^2` over `P subset I`, `Q subset J`, `|P|=|Q|=k`. Such a term is possible only for disjoint `P,Q`. For a fixed ordered disjoint pair, all `2k` prescribed coordinate assignments occur with probability `2^(-2k)=4^(-k)`. Summing proves (4.2). QED.

Hence some physical cut obeys

`E_k(S[I,J]) >= 4^(-k)D_k(S)`,                                               (4.3)

and Theorem 3.1 immediately gives

`boxed:
 ||p_Q||_infinity <= sqrt(2) C_k |a|^(-1/2) D_k(S)^(-1/(4k)).`                (4.4)

The cut penalty is the dimension-free factor `4^(1/4)=sqrt(2)`, independent of `k`. For `k=3` its coefficient is `13.916788986819059...`.

This is useful structurally because it permits aggregation over **all** disjoint physical `k x k` minors before choosing the cut. It still does not show that the bare global spectral hypothesis forces `D_k(S)` at a universal scale after some scalar pivot.

## 5. Diffuse Frobenius corollary

Let `S_1=sum_j s_j(B)^2=||B||_F^2`. If

`max_j s_j(B)^2 <= rho S_1` with `rho<1/3`,                                   (5.1)

then

`E_3(B) >= (1-3rho) S_1^3/6`.                                                (5.2)

Indeed, writing `S_2=sum x_j^2`, `S_3=sum x_j^3`, Newton's identity gives

`e_3(x)=(S_1^3-3S_1S_2+2S_3)/6`,

and `S_2<=rho S_1^2`, `S_3>=0`. Thus Theorem 3.1 yields

`boxed:
 ||p_Q||_infinity
 <= 11.425362339386691...
    (1-3rho)^(-1/12) |a|^(-1/2)||B||_F^(-1/2).`                              (5.3)

This pays genuinely diffuse cross energy without a leverage gate and without selecting any particular singular direction.

## 6. SAME-matrix comparison: volume, ridge, and square-assisted aggregate

Let a single residual physical cross block `B` be fixed. The currently valid certificates can be placed side by side without changing coordinates or matrices.

### Third volume

If its volume-sampling row marginal is at most `1/2`, newest-Claude Theorem D gives the continuous bound

`D_3(B)=6sqrt(e) E_3(B)^(-1/6)`.                                               (6.1)

If the marginal lies in `[1/2,3/4)`, D' replaces (6.1) by its displayed `h`-dependent constant. At the effective-dimension-three ridge scale, if `ell_*<3/4`, (2.4) gives

`R_3(B)=[3e/(sqrt(2q_*)(3-2q_*))]E_3(B)^(-1/6)`.                              (6.2)

The new square-assisted certificate is

`S_3(a,B)=C_3 |a|^(-1/2)E_3(B)^(-1/12)`,                                     (6.3)

with **no marginal or ridge-leverage condition**. Therefore, whenever the relevant hypotheses coexist on the same matrix,

`||p_Q||_infinity <= min{D_3(B), R_3(B), S_3(a,B)}`.                          (6.4)

The first two branches also give continuity; the last branch alone only gives essential boundedness.

### Fifth volume: a near-zero-pivot bridge

Newest-Claude D5 and Theorem 3.1 with `k=5` give, on exactly the same `B`,

`boxed:
 ||p_Q||_infinity <= min{
   11.658219907985621... E_5(B)^(-1/10),
   5.464743450762853... |a|^(-1/2)E_5(B)^(-1/20)
 }.`                                                                          (6.5)

The first term requires no scalar pivot at all and gives continuity; the second spends a usable pivot but only half as much reciprocal fifth-volume power. Their crossover is explicit: the square-assisted term is no larger when

`|a| >= 0.219722772451337... E_5(B)^(1/10)`.                                  (6.6)

Thus a zero or very small pivot is not itself an obstruction if fifth exterior volume is available; D5 takes over. Conversely, when the pivot is moderate, the half-Riesz route is substantially less sensitive to small aggregate volume.

## 7. Genuinely rotated indefinite target family and exact same-matrix comparison

Take `m=8` and let `U` be the normalized `8 x 8` Sylvester-Hadamard matrix, so every entry has modulus `1/sqrt(8)`. Let

`H_8=sum_(j=1)^8 1/j = 761/280`,
`s_j^2=1/(j H_8)`,
`B=U diag(s_1,...,s_8) U^T`,
`u=(1,...,1)/sqrt(8)`.

On original independent coordinates `(z,x_1,...,x_8,y_1,...,y_8)`, define

`Q=z^2 + 2(u^T x)^2 - 2(u^T y)^2 + 2 x^T B y`.                               (7.1)

This is a genuinely nonseparable, rotated, indefinite form in the original product coordinates: `U` is not a signed permutation and the `s_j` are distinct, so `B=U diag(s_j)U^T` is not diagonal.

### 7.1 Exact target certificate

The residual `16 x 16` matrix is

`S = [[2uu^T, B],[B,-2uu^T]]
   = [[2uu^T,0],[0,-2uu^T]] + [[0,B],[B,0]].`                                 (7.2)

The first summand has extremal eigenvalues `+2,-2`; the second has operator norm

`||B||=s_1=sqrt(280/761)<1`.                                                   (7.3)

Weyl therefore gives one residual eigenvalue at least `2-s_1>1` and one at most `-2+s_1<-1`. The isolated `z` coordinate contributes the exact eigenvalue `+1`. Hence the full matrix has at least three eigenvalues of modulus at least one, with both signs present. No probabilistic rotation is used in this certificate.

### 7.2 Exact aggregate currencies

Because the singular-square spectrum is `x_j=1/(jH_8)`, one obtains

`E_3(B)=36632400/440711081 = 0.0831211230652038...`,                           (7.4)

`E_5(B)=193616640000/255225041939801 = 0.000758611453360708...`,              (7.5)

and

`E_6(B)=19576793600000/582678770748565683
      = 0.0000335979180687324...`.                                           (7.6)

The flat Hadamard singular frame makes every physical volume-sampling row marginal exactly `3/8`: the singular-mode inclusion probabilities sum to three and every squared left-singular-vector entry is `1/8`. The calibrated effective-dimension-three ridge matrix likewise has every physical diagonal exactly `3/8`.

Therefore all of the following apply to this **same** matrix for every independent cap-one input law:

* newest-Claude third-volume Theorem D: `<14.975` (continuous);`
* effective-dimension-three ridge theorem: `<8.729` (continuous);`
* newest-Claude D5: `<23.913` (continuous);`
* new square `E_3` theorem: `<12.108` (essential bound);`
* new square `E_5` theorem: `<7.827` (essential bound);`
* new square `E_6` theorem: `<7.558` (essential bound).`

Thus, for (7.1),

`boxed: ||p_Q||_infinity < 7.558`,                                             (7.7)

while independently a continuous representative exists with the ridge bound `<8.729`.

This example also demonstrates why thresholding is avoidable. In the harmonic family `s_j^2=1/(jH_m)` the total cross Frobenius energy is one but no fixed singular-value threshold retains a dimension-free number of directions as `m` grows. The aggregate `E_k` theorem spends all exterior-volume mass directly instead of first paying for a worst selected singular value.

## 8. What this does and does not close

### Paid in this run

1. The partner's regularized-determinant half-Riesz theorem now has an exact **aggregate exterior-volume** corollary for every `k>=3`, with explicit constants and no `q=2` leverage requirement.
2. Arbitrary physical cuts can be aggregated before selection through the exact disjoint-compound identity (4.2), with only a universal `sqrt(2)` cut penalty.
3. The newest-Claude D'/D5 volume certificates and the B04 ridge certificate are now compared on the **same matrix**, producing the explicit hybrid envelopes (6.4)-(6.6).
4. A genuinely rotated indefinite target family exhibits a real quantitative gain from the aggregate square route.

### Still unpaid

The bare assumption `s_3(A)>=1` does not, by itself, yield in this report a nonzero scalar pivot `a` together with a universal lower bound on one `E_k(B)` or `D_k(S)`. Previous correction records already rule out naive universal-good-minor and universal-cross-rank-three reductions.

The first essential remaining implication is therefore:

**`QFORM-LOW-VOLUME-HIGH-MARGINAL-PIVOT-ROUTING-v1`.** Starting only from `s_3(A)>=1`, show that every matrix can be routed, in original product coordinates, into at least one of:

* a scalar-pivot residual with `|a|^(2k) E_k(B)` (or the disjoint-compound analogue) bounded below at a universal scale for some `k>=3`;
* a D'/D5 volume branch on the same residual, including the zero/near-zero-pivot case;
* an effective-dimension-three ridge branch with maximum leverage `<3/4`;
* an already-paid bounded-size mixed-hub / physical-pair / grouped-coordinate branch.

Equivalently, the next structural task is to prove that simultaneous failure of square-assisted aggregate volume, D5, D', and ridge leverage forces a bounded-size physical core of a form already controlled. This is a genuine structural gap, not an analytic one solved here.

## 9. Corrections respected

No step uses law-uniform pointwise quadratic-phase decay; no step rotates the random coordinates and claims independence; no arbitrary-joint rank-three coarea theorem is used; no positive moment of a worst conditional projection density is used; no fiber-sup dimension-free bound is used; no fixed-fragment localization, universal good principal minor, or universal rank-three cross cut is assumed. Numerical values above only evaluate already-proved explicit formulas and are not used as proof of a universal theorem.

**Final status:** `FULL_TARGET_OPEN`; `FULL_TARGET_CONTINUITY_OPEN`; new branch `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED`.
