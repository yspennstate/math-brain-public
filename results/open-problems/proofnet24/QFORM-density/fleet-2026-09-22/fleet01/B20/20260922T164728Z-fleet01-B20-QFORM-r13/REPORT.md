# fleet01/B20 — shared-anchor exterior square and opposite-sign second-pivot closure

**Run:** `20260922T164728Z-fleet01-B20-QFORM-r13`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.7`  
**Assignment:** Proof closure and keeper  
**Classification:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCH_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The sole target is the full arbitrary-dimensional statement: for independent real coordinates `X_i` with probability densities `0<=f_i<=1` and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has an essentially bounded density with one universal finite constant, or give a valid counterexample. Continuity is tracked separately.

No Gaussian, moment, iid, compact-support, log-concavity, post-rotation independence, pointwise scalar Fresnel-decay, or approximate-block extraction hypothesis is used. In particular this run does not use the newly refuted `QFORM-DIFFUSE-APPROX-BLOCK-EXTRACTION-ALONE-FALSE-v1` mechanism.

The full conjecture remains OPEN.

## 2. Source-pinned dependencies actually used

1. **Required partner fleet02/B20.** Run `20260922T155719Z-fleet02-B20-QFORM-r12`, canonical report `yspennstate/math-open-problems@527fb9dfef73a5218883c057db14a491992a30d9`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260922T155719Z-fleet02-B20-QFORM-r12/REPORT.md`. In the diagonal-dominated first-pivot branch it gives

   `|a|>=tau>=1/4`, `s_2(S)>=tau`,

   where `S` is the first Schur complement and `tau=(1+||b||/|a|)^(-2)`.

2. **Immediately preceding B20 closure.** `yspennstate/math-open-problems@36765bac9a785445139d5b79db651ca9d51e050f`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B20/20260922T162317Z-fleet01-B20-QFORM-r12/REPORT.md`. It proves

   `s_3(S)<tau/128`,

   hence for `P=1_{|S|>=tau/64}`, `H=PSP`, `E=S-H`, one has `rank(P)=2`, both nonzero eigenvalues of `H` have modulus at least `tau`, `||E||_op<tau/64`, and there is a physical coordinate `j` with `P_jj>1/32`. It also proves

   `max{|S_jj|,||S_{j,-j}||}>tau/9`.

   In the diagonal-dominated second-row branch, writing `d=S_jj`, `c=S_{j,-j}`, it gives `|d|>tau/9`. The same-sign case `ad>0` is already closed with density `<12 pi`; only `ad<0` remained unpaid.

3. **Physical three-pivot endpoint.** fleet02/B20 run `20260922T152608Z-fleet02-B20-QFORM-r12`, canonical source at `yspennstate/math-open-problems@2979c262e6ba9c4cef66314aabd714431f5e9c95`. If a physical ordered triple has successive scalar Schur pivots `p_1,p_2,p_3`, then

   `||p_Q||_infinity <= C_3 (|p_1|^4 |p_2|^3 |p_3|)^(-1/8)`,

   with `C_3<94.356`. This allows arbitrary outside spectrum and couplings.

4. **Original-coordinate cross-bank quarter moment.** fleet01/B19 run `20260922T155027Z-fleet01-B19-QFORM-r11`, canonical report `yspennstate/math-open-problems@2e5d5cdc3bb7121673bc920497fb11cac9eceb46`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260922T155027Z-fleet01-B19-QFORM-r11/REPORT.md`. For disjoint original-coordinate banks `X,Y`, arbitrary same-bank quadratic terms `F(X),G(Y)`, and cross block `C` with `sigma=s_1(C)>0`,

   `K=F(X)+2X^TCY+G(Y)`

   satisfies

   `sup_t E|K-t|^(-1/4) <= (2+sqrt(pi))(4e/sigma)^(1/4)`.

This run applies the partner inequalities to actual quantitative density estimates; it does not merely cite them.

## 3. Current unresolved branch before this run

Work in a minimum-dimensional counterexample to the candidate cap

`C_* = 32768 sqrt(2)`.

After the first physical pivot and the previous run, write

`S = [[d,c^T],[c,C]]`

in the physical coordinate `j` selected by the rank-two high spectral window. In the branch treated here,

`|a|>=tau>=1/4`, `|d|>tau/9`, `|d|>=||c||`, and `a d<0`.            (3.1)

The previous `L^3` certificate for the indefinite physical pair did not by itself imply an `L^infinity` bound. The first unpaid implication was to extract, without rotating the product law and without a ridge hypothesis, enough exact outside curvature to integrate the binary indefinite singularity.

The main new observation is that the **shared-anchor compression of the exterior square** carries a dimension-free amount of the rank-two high window and is exactly `d` times the second Schur complement.

## 4. New theorem I — shared-anchor exterior-square reserve

Let `V` be the residual physical coordinate space after the first pivot and let

`W_j = e_j wedge e_j^perp subset wedge^2 V`.

For a symmetric matrix `M`, the matrix of the compression

`P_{W_j} (wedge^2 M) P_{W_j}`

in the basis `{e_j wedge e_k:k!=j}` has entries

`det M[{j,k},{j,l}]`.                                                (4.1)

Because `d!=0`, define the second Schur complement

`T = C - c c^T/d`.                                                   (4.2)

Then (4.1) gives exactly

`P_{W_j}(wedge^2 S)P_{W_j} = d T`.                                  (4.3)

### Proposition 4.1 — `QFORM-SHARED-ANCHOR-EXTERIOR-RESERVE-v1`

Under the current branch,

`boxed( |d| s_1(T) > tau^2/64. )`                                   (4.4)

### Proof

The high-window part has rank two. Write

`H = U diag(lambda_1,lambda_2) U^T`,

with `U^TU=I_2`, `|lambda_1|,|lambda_2|>=tau`, and let

`D=|lambda_1 lambda_2| >= tau^2`.

On `wedge^2 V`, `wedge^2 H` is rank one:

`wedge^2 H = (lambda_1 lambda_2) w w^T`,

where the unit Pluecker vector `w` has coordinates `det U_{k,l}`. The tight-frame identity gives

`||P_{W_j}w||^2 = sum_{k!=j} det(U_{j,k})^2 = P_jj >1/32`.          (4.5)

Therefore the compression of `wedge^2 H` to `W_j` has one singular value

`D P_jj > D/32`.                                                     (4.6)

Now use the spectral decomposition `S=H+E`. Because `H` and `E` are disjoint spectral pieces, the exterior-square operator decomposes orthogonally into

`wedge^2 S = (wedge^2 H) direct_sum (H wedge E) direct_sum (wedge^2 E)`.

Consequently

`||wedge^2 S-wedge^2 H||_op
 = max{s_1(H)||E||_op, s_1(E)s_2(E)}`.

Since `||E||_op<tau/64` and `s_2(H)>=tau`,

`s_1(H)||E||_op < s_1(H)s_2(H)/64 = D/64`,

while `s_1(E)s_2(E)<tau^2/4096<=D/4096`. Hence

`||wedge^2 S-wedge^2 H||_op <D/64`.                                 (4.7)

Compression cannot increase operator norm. Combining (4.6)-(4.7),

`||P_{W_j}(wedge^2 S)P_{W_j}||_op
 >D(1/32-1/64)=D/64>=tau^2/64`.

Use (4.3) to obtain (4.4). QED.

This is stronger than the preceding total two-minor-bank statement for the present branch: it places a definite amount of curvature specifically in the shared-anchor matrix that becomes the exact second Schur complement.

## 5. New theorem II — physical diagonal or product-preserving cross cut

### Lemma 5.1 — symmetric diagonal/cut dichotomy

For every real symmetric matrix `T` with `mu=s_1(T)>0`, at least one of the following holds:

1. some physical diagonal satisfies `|T_kk|>=mu/2`; or
2. there is a bipartition of all remaining physical coordinates `L disjoint_union R` such that

   `s_1(T[L,R])>mu/4`.                                               (5.1)

### Proof

If the first alternative fails, put `O=T-diag(T)`. Then

`||O||_op >= ||T||_op-||diag(T)||_op >mu/2`.

Choose a unit vector `x` with `|x^TOx|=||O||_op`. Randomly put each coordinate in `L` or `R` with probability `1/2` and set

`Y=2 x_L^T O[L,R] x_R`.

Because `O` has zero diagonal, each unordered off-diagonal pair is separated with probability `1/2`, so

`E Y = (1/2)x^T O x`.

Thus some cut has `|Y|>=||O||_op/2`. But

`|Y|<=2 s_1(O[L,R])||x_L||||x_R||<=s_1(O[L,R])`,

because `||x_L||||x_R||<=1/2`. The cross block of `O` is the same as that of `T`, so (5.1) follows. QED.

Combining Lemma 5.1 with (4.4), put `mu=s_1(T)`. Either

`|T_kk| > tau^2/(128|d|)`                                           (5.2)

for a physical coordinate `k`, or there is a physical bipartition with

`boxed( sigma:=s_1(T[L,R]) > tau^2/(256|d|). )`                     (5.3)

No spectral rotation is used in either alternative.

## 6. New theorem III — a sequential indefinite quarter kernel

The physical `2x2` block need not have opposite-sign **diagonal entries**; what is guaranteed here is that its successive Schur pivots `a,d` have opposite signs. The following kernel handles exactly that situation.

### Lemma 6.1 — `QFORM-SEQUENTIAL-INDEFINITE-QUARTER-KERNEL-v1`

Let `X,Y` be independent real random variables with densities bounded by one and

`q(X,Y)=aX^2+2cXY+eY^2`,

where `a!=0` and

`d=e-c^2/a`

has sign opposite to `a`. Then `q` has a density `h` satisfying, for almost every `s!=0`,

`boxed( h(s) <= 2 sqrt(2) |a|^(-1/2)|d|^(-1/4)|s|^(-1/4). )`       (6.1)

The same estimate is uniform under arbitrary translations of `X,Y`.

### Proof

Multiplying the form by `-1` if necessary, assume `a>0`, `d<0`; put `alpha=a`, `beta=|d|`. Completing the first physical square gives

`q=a(X+(c/a)Y)^2-beta Y^2`.

For each fixed `Y=y`, the translated first coordinate still has density cap one. The density of `alpha Z^2` is at most `(alpha u)^(-1/2)` at `u>0`. Hence

`h(s)<=alpha^(-1/2) int f_Y(y) 1_{s+beta y^2>0}(s+beta y^2)^(-1/2)dy`.  (6.2)

If `s<0`, let `r=sqrt(|s|/beta)`. The domain is `|y|>r`. On each tail,

`y^2-r^2>=2r(|y|-r)`.

For a cap-one density carrying tail mass `m`, the decreasing kernel `(u-r)^(-1/2)` is maximized by filling the interval adjacent to `r`, giving integral at most `2 sqrt(m)`. Summing the two tails and using `sqrt(m_+)+sqrt(m_-)<=sqrt(2)` yields

`int f_Y(y)1_{|y|>r}(y^2-r^2)^(-1/2)dy <=2 r^(-1/2)`.

Thus the right side of (6.2) is at most

`2 alpha^(-1/2) beta^(-1/4)|s|^(-1/4)`.

If `s>0`, again put `r=sqrt(s/beta)`. The kernel `(y^2+r^2)^(-1/2)` is symmetric decreasing, so the one-dimensional bathtub principle gives

`int f_Y(y)(y^2+r^2)^(-1/2)dy
 <= int_{-1/2}^{1/2}(y^2+r^2)^(-1/2)dy
 =2 asinh(1/(2r)).`

For every `u>=0`, `asinh(u)<=2 sqrt(u)`: for `u<=1` use `asinh(u)<=u<=sqrt(u)`; for `u>=1`, use `asinh(u)<=1+log u<=2sqrt(u)`. Therefore

`2 asinh(1/(2r))<=2sqrt(2) r^(-1/2)`.

After restoring the factor `beta^(-1/2)`, (6.1) follows. Translation uniformity is immediate because conditioning only translates the original one-dimensional cap-one factors. QED.

## 7. Closing the previously unpaid opposite-sign diagonal-dominated branch

We now combine the three new lemmas with the completed peer theorems.

### Case A: a physical third diagonal appears

Suppose (5.2) holds. The successive physical Schur pivots are

`p_1=a`, `p_2=d`, `p_3=T_kk`.

The physical three-pivot endpoint gives

`||p_Q||_infinity <= C_3 (|a|^4 |d|^3 |p_3|)^(-1/8)`.

Using `|a|>=tau`, `|d|>tau/9`, and (5.2),

`|a|^4 |d|^3 |p_3|
 > tau^4 |d|^3 [tau^2/(128|d|)]
 = tau^6 |d|^2/128
 > tau^8/(81*128).`

Therefore

`||p_Q||_infinity
 < C_3 (81*128)^(1/8) tau^(-1)
 <= 4 C_3 (81*128)^(1/8)
 <1198.924 < C_*`.                                                   (7.1)

So this branch cannot occur in the minimum counterexample.

### Case B: the residual curvature exports to an original-coordinate cut

Suppose instead (5.3) holds. Partition the residual variables exactly into the physical banks `L,R`. The residual critical-value quadratic is

`R(Z)=Z^T T Z
    =F(Z_L)+2 Z_L^T T[L,R]Z_R+G(Z_R)`.

The fleet01/B19 theorem applies directly because the two banks consist of disjoint original coordinates and all self terms are allowed. Hence

`sup_t E|R-t|^(-1/4)
 <=(2+sqrt(pi))(4e/sigma)^(1/4).`                                  (7.2)

Condition on the residual variables and apply Lemma 6.1 to the two original pivot coordinates. Completing the physical pair only translates those two coordinates, so

`p_Q(t)
 <=2sqrt(2)|a|^(-1/2)|d|^(-1/4) E|t-R|^(-1/4).`

Using (7.2),

`||p_Q||_infinity
 <=2sqrt(2)(2+sqrt(pi))(4e)^(1/4)
    |a|^(-1/2)(|d| sigma)^(-1/4).`                                (7.3)

From (5.3), `|d|sigma>tau^2/256`, while `|a|>=tau`. Therefore

`||p_Q||_infinity
 <2sqrt(2)(2+sqrt(pi))(4e)^(1/4)
   tau^(-1/2)(256/tau^2)^(1/4)`

`=8sqrt(2)(2+sqrt(pi))(4e)^(1/4) tau^(-1)`

`<=32sqrt(2)(2+sqrt(pi))(4e)^(1/4)`

`=310.01130418... < C_*`.                                          (7.4)

So the cross-cut alternative is also impossible in a minimum counterexample.

### Corollary 7.1 — complete closure of the diagonal-dominated second row

The preceding B20 run already closed `ad>0` with `<12pi`. Equations (7.1)-(7.4) now close `ad<0`. Consequently:

`boxed(
In any surviving minimum counterexample in the fleet02/B20 diagonal-dominated FIRST-pivot branch, the high-window-localized SECOND Schur row cannot be diagonal-dominated.
)`

Thus the only remaining localized second-row alternative is

`boxed(
 ||S_{j,-j}||_2 > |S_jj|,
 ||S_{j,-j}||_2 > tau/9 >=1/36.
)`                                                               (7.5)

This is a genuine target-level branch closure with all arbitrary extra spectrum retained. It uses only original-coordinate conditioning/cuts and source-valid integrated estimates.

## 8. What remains open

The full QFORM conjecture is **not proved**. The first unpaid implication in this chain is now the **cross-dominated second Schur row** (7.5). A single cross row gives only the critical `sqrt(r log(1/r))`-type small-ball scale behind the quarter moment; the first pivot requires a half-Riesz endpoint, so the already-refuted one-heavy-row/same-square absorption shortcut cannot be used.

A useful next target is therefore precise: combine the exact rank-two high spectral window with the strong star `||S_{j,-j}||>tau/9` to produce either

1. a second product-compatible cross direction at universal scale;
2. a physical scalar curvature coefficient that upgrades the star to an already-paid three-pivot packet; or
3. a grouped-coordinate endpoint that directly bounds the half-Riesz potential of
   `dX_j^2+2X_j c^TY+Y^TCY`
   without treating the same-bank contaminant as independent.

The newly refuted approximate-block-extraction mechanism is not among the allowed next steps.

Continuity is not claimed for the new quarter-moment branch; only essential boundedness/absolute continuity is proved in the stated branch.

## 9. Verification

The accompanying `CHECK.py` reproduces the explicit constants in (7.1) and (7.4) and verifies they are below `C_*=32768sqrt(2)`. These numerical evaluations audit closed-form inequalities only; no finite computation is used as a universal proof.

## 10. Keeper note

Fresh native fleet01 inventory contained the same twenty B01-B20 QFORM tasks, all enabled, hourly-valid and quiet, so no scheduler mutation was needed or authorized. The post-request acknowledgement set remains complete for all twenty slots; this operational evidence is recorded separately from mathematical validity. No missing login was treated as an outage, and no other-account native action was attempted.
