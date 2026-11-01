SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-23T17:53:36Z.
attacking: row-marginal-free rank-two cross-volume L2/collision theorem, then square/fusion receivers for linear small-ball scaling.

# fleet01/B03 r30 — row-marginal-free critical two-volume collision theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Decoupled time integral`  
Status: `NEW SUPPORTING THEOREM / CRITICAL 2-VOLUME ROW-MARGINAL GATE REMOVED / LINEAR SMALL-BALL AFTER A THIRD SMOOTHING RESOURCE / FULL QFORM OPEN`  
Brain state: `WITHOUT_VERIFIED_BRAIN`.

The current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` was consumed.  The unrestricted target remains open: independent real coordinate densities bounded by one, arbitrary symmetric `A` with at least three eigenvalues of modulus at least one, no moments/support/log-concavity/rotation-independence assumptions.  Continuity is tracked separately.

This run changes the analytic mechanism from the preceding rank-three `L^1_t` crossing theorem to the critical rank-two `L^2_t` endpoint.  The new point is that the physical row-marginal gate can be removed completely at this endpoint by a finite promotion tree: diffuse two-volume -> one physical hub -> two physical hubs.  The resulting whole-copy integral is dependence-safe and can be spent by either one genuine completed square or a second independent critical packet to recover linear small-ball scaling.

## 1. Source-valid inputs

### 1.1 Weighted-subset / grouped projected crossing

The independently checked source is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The only pieces used are:

* the `k=0, ell=2` specialization of the weighted-subset Fourier lemma; and
* the exact-rank-two crossing/Plancherel theorem for arbitrary internal functions.

The same `k=0` specialization was already written out explicitly and checked in fleet01/B03 r29 for `ell=3`:

`yspennstate/math-open-problems@2062e0f60e39c2cb88fb72c4908d95f19676d00e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260923T165124Z-fleet01-B03-QFORM-r29/ADDENDUM_CROSSBLOCK.md`.

No pointwise law-uniform quadratic phase estimate is used.

### 1.2 Designated partner result actually applied

The completed designated partner result is

`yspennstate/math-open-problems@38920ffa423ec07886112206314249deb7294dd4`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260923T171205Z-fleet02-B03-QFORM-auto11/REPORT.md`.

Its critical grouped-crossing theorem says, in the `k=1, ell=1` branch, that if a one-dimensional physical hub has density cap `M_H`, hub-to-`J` singular product `S`, projected crossing Frobenius norm `F`, and all projected one-volume row marginals are at most `1/2`, then

`|phi(t)| <= min{1, 2*pi*M_H^(1/2)*(S F)^(-1/2)*|t|^(-1)}`.       (1.1)

The partner also derived the corresponding dependence-safe half-Riesz and square receiver.  In the proof below I apply `(1.1)` at the actual inequality `(3.8)`, rather than merely citing it as background.

### 1.3 Corrections retained

The proof never conditions one member of a sum/difference pair and reuses a marginal density cap; it never assumes independence after a spectral rotation; it never uses the refuted arbitrary-joint coarea theorem; and it never assumes a uniformly good single physical minor.  The only independent-copy identity used is the scalar identity

`|phi_R(t)|^2 = E exp(i t (R-R'))`,                                (1.2)

with the entire copy difference left intact.

## 2. Main theorem

### Theorem 2.1 — `QFORM-ROW-MARGINAL-FREE-2VOLUME-COLLISION-v1`

Split the original independent cap-one coordinates into two nonempty banks `I,J` and write

`R = F(X_I) + 2 X_I^T B X_J + G(X_J)`,                            (2.1)

where `F,G` are arbitrary real quadratic-plus-affine functions on their own banks.  Let `b_i`, `i in I`, be the physical rows of `B`, and define the total squared physical two-volume

`Z_2 = sum_{i<j} |b_i wedge b_j|^2 = e_2(BB^T)`.                  (2.2)

Assume `Z_2>0`.  Then:

1. the characteristic function obeys the row-marginal-free critical envelope

`boxed:
 |phi_R(t)| <= min{1, K_2 Z_2^(-1/4)|t|^(-1)},
 K_2 = 2*pi*sqrt(2e) = 14.65015120674476...;
}`                                                                  (2.3)

2. `R` has an `L^2` density and

`boxed:
 ||p_R||_2^2 <= 4*sqrt(2e) Z_2^(-1/4)
              = 9.326575926388497... Z_2^(-1/4);
}`                                                                  (2.4)

3. retaining an independent copy `R'` as one scalar object,

`boxed:
 int_R |t|^(-1/2)|phi_R(t)|^2 dt
 <= (16/3)*sqrt(2*pi)*(2e)^(1/4) Z_2^(-1/8)
 =20.41360850273567... Z_2^(-1/8),
}`                                                                  (2.5)

and hence

`boxed:
 E|R-R'|^(-1/2)
 <= (16/3)*(2e)^(1/4) Z_2^(-1/8)
 =8.143851527303445... Z_2^(-1/8);
}`                                                                  (2.6)

4. the one-copy half-Riesz potential is translation-uniform:

`boxed:
 sup_s E|R-s|^(-1/2)
 <= 8*(2e)^(1/4) Z_2^(-1/8)
 =12.215777290955167... Z_2^(-1/8).
}`                                                                  (2.7)

No continuity claim is made for `R` from `(2.4)` alone.

## 3. Proof of the row-marginal-free envelope

For each physical row define its pair-volume marginal

`alpha_i = Z_2^(-1) sum_{j != i}|b_i wedge b_j|^2`.               (3.1)

Then

`sum_i alpha_i = 2`.                                               (3.2)

We split into three exhaustive cases.

### 3.1 Diffuse pair-volume: every `alpha_i<=1/2`

Apply Cauchy--Schwarz in the whole `I` bank.  If `X_J'` is an independent copy of `X_J`, `D=X_J-X_J'`, and `psi_i` is the characteristic function of the original scalar coordinate `X_i`, then arbitrary internal phases cancel or have modulus one and

`|phi_R(t)|^2
 <= E_D product_{i in I}|psi_i(2t <b_i,D>)|`.                    (3.3)

The coordinates of `D` are independent and each difference density is at most one.  Apply the weighted-subset Fourier lemma with no conditioning projection (`k=0`) and `ell=2`.  Since the volume weights are exactly

`w_{ij}=|b_i wedge b_j|^2/Z_2`,                                   (3.4)

and their inclusion marginals are `(3.1)`, the hypothesis is precisely `alpha_i<=1/2`.  The source constant is

`2^((0+2)/2) (2*pi)^2 exp(2/2) = 8*pi^2*e`.                       (3.5)

Therefore

`|phi_R(t)|^2
 <= min{1, 8*pi^2*e /(sqrt(Z_2)|t|^2)}`.                        (3.6)

Taking square roots gives `(2.3)` because

`sqrt(8*pi^2*e)=2*pi*sqrt(2e)=K_2`.                               (3.7)

### 3.2 One heavy row, but diffuse after projection

Suppose `alpha_i>1/2`.  Put

`m=b_i`, `P_m=orthogonal projection onto span(m)`,

`c_j=b_j(I-P_m)`, `j!=i`, and

`Z_1' = sum_{j!=i}||c_j||^2`.                                     (3.8a)

Exterior algebra gives the exact identity

`||m||^2 Z_1'
 = sum_{j!=i}|m wedge b_j|^2
 = alpha_i Z_2`.                                                   (3.8b)

Define projected one-volume marginals

`beta_j = ||c_j||^2/Z_1'`.                                        (3.8c)

Assume first that every `beta_j<=1/2`.  Promote the genuine physical coordinate `X_i` to a one-dimensional hub.  The hub-to-`J` row is `m`, so its singular product is

`S=||m||`,                                                         (3.8d)

and the projected residual crossing has Frobenius norm

`F=sqrt(Z_1')`.                                                    (3.8e)

The hub is one original coordinate, hence `M_H<=1`.  Apply the completed partner estimate `(1.1)` to this actual packet.  Using `(3.8b)`,

`|phi_R(t)|
 <= min{1, 2*pi*(S F)^(-1/2)|t|^(-1)}`
` = min{1, 2*pi*(alpha_i Z_2)^(-1/4)|t|^(-1)}`
` < min{1, 2*pi*2^(1/4) Z_2^(-1/4)|t|^(-1)}`.                    (3.8)

Numerically `2*pi*2^(1/4)=7.472008672178522...`, strictly below `K_2=14.650151...`.  This is the required designated-partner application at an actual inequality.

### 3.3 Two heavy rows

If instead some `beta_j>1/2`, then `(3.8b)` gives

`|b_i wedge b_j|^2
 = ||m||^2||c_j||^2
 = alpha_i beta_j Z_2
 > Z_2/4`.                                                         (3.9)

Promote the two genuine physical coordinates `i,j` to a two-dimensional hub `H={i,j}` and put all remaining original coordinates in the complementary bank.  Let `M=A_{H,H^c}` be the full physical hub-to-complement cross matrix.  Its two rows are linearly independent because the columns belonging to the old `J` bank contain `b_i,b_j` with nonzero wedge.  Hence `rank M=2`.

The Gram matrix of those old-`J` columns is a positive-definite summand of `M M^T`, so Loewner monotonicity of the two eigenvalues gives

`S_H := sqrt(det(MM^T)) >= |b_i wedge b_j| > sqrt(Z_2)/2`.        (3.10)

Apply the exact-rank-two crossing/Plancherel theorem from the source.  The two-dimensional hub is exactly two original independent coordinates; after the left SVD rotation its joint density cap stays at most one.  The two-dimensional orthonormal projection of the complementary product law has density cap at most `2`.  Therefore

`|phi_R(t)|
 <= min{1, pi*sqrt(2)*S_H^(-1/2)|t|^(-1)}`
` < min{1, 2*pi Z_2^(-1/4)|t|^(-1)}`.                            (3.11)

Again the coefficient `2*pi` is below `K_2`.

The three cases are exhaustive.  Thus the diffuse envelope `(2.3)` dominates globally, with no row-marginal hypothesis left.  QED for `(2.3)`.

## 4. L2 density and dependence-safe time integral

Put

`T_0 = K_2 Z_2^(-1/4)`.                                           (4.1)

From `(2.3)`,

`int_R |phi_R(t)|^2 dt
 <= 2 int_0^T0 1 dt +2 T_0^2 int_T0^infinity t^(-2)dt
 =4T_0`.                                                          (4.2)

A finite measure whose Fourier transform is in `L^2` has an `L^2` density, and Plancherel gives

`||p_R||_2^2
 =(2*pi)^(-1) int|phi_R|^2
 <= (2/pi)K_2 Z_2^(-1/4)
 =4sqrt(2e)Z_2^(-1/4)`,                                          (4.3)

which is `(2.4)`.

Now keep the independent-copy identity in the scalar form `(1.2)`.  Squaring `(2.3)` and splitting at `T_0`,

`int_R |t|^(-1/2)|phi_R(t)|^2dt`
` <=2 int_0^T0 t^(-1/2)dt
   +2 T_0^2 int_T0^infinity t^(-5/2)dt`
` =4sqrt(T_0)+(4/3)sqrt(T_0)`
` =(16/3)sqrt(T_0)`.                                               (4.4)

Since

`sqrt(K_2)=sqrt(2*pi)*(2e)^(1/4)`,                                (4.5)

this is `(2.5)`.  The one-dimensional Riesz identity

`int_R |t|^(-1/2)e^(itx)dt = sqrt(2*pi)|x|^(-1/2)`                (4.6)

(with a standard cutoff justification) applied to the nonnegative characteristic function `|phi_R|^2` gives `(2.6)`.

Crucially, no coordinate-level sum/difference variable is ever separated from its dependent conjugate; `(4.4)` concerns the entire scalar `R-R'`.

## 5. Translation-uniform one-copy half-Riesz bound

The same envelope, without squaring, gives

`int_R |t|^(-1/2)|phi_R(t)|dt`
` <=2 int_0^T0 t^(-1/2)dt
   +2T_0 int_T0^infinity t^(-3/2)dt`
` =8sqrt(T_0)`.                                                     (5.1)

Insert the harmless phase `e^(-its)` and use `(4.6)` to obtain

`sup_s E|R-s|^(-1/2)
 <=(2*pi)^(-1/2)8sqrt(T_0)
 =8(2e)^(1/4)Z_2^(-1/8)`,                                        (5.2)

which is `(2.7)`.

## 6. Linear small-ball receivers

### Corollary 6.1 — one completed physical square

Let `Z` be one further genuine original coordinate, independent of the entire background defining `R`, with density at most one.  Suppose exact physical completion gives

`Q = d[Z+h]^2 + R`, `d!=0`,                                      (6.1)

where `h` may be an arbitrary measurable function of the residual background.  Conditional on that background, the square pushforward density is bounded by

`|d|^(-1/2)|u|^(-1/2)`                                            (6.2)

on the appropriate half-line.  Hence for a.e. `s`,

`p_Q(s)
 <= |d|^(-1/2) E|s-R|^(-1/2)`
 <= 8(2e)^(1/4)|d|^(-1/2)Z_2^(-1/8)`.                            (6.3)

Therefore

`boxed:
 ||p_Q||_infinity
 <=12.215777290955167... |d|^(-1/2)Z_2^(-1/8),
}`                                                                  (6.4)

and every interval `I` obeys the genuine linear small-ball estimate

`P(Q in I)
 <=12.215777290955167... |d|^(-1/2)Z_2^(-1/8)|I|`.                (6.5)

This proves essential boundedness/absolute continuity in the stated branch.  Because the center `h` may depend on the residual background, continuity is **not proved** by this compiler.

### Corollary 6.2 — two independent critical packets

Let `R_1,R_2` be independent packets of the form `(2.1)`, on disjoint original-coordinate sources, with two-volumes `Z_2^(1), Z_2^(2)>0`.  Then

`p_{R_1+R_2}=p_1*p_2`,

and Cauchy--Schwarz plus `(2.4)` gives

`boxed:
 ||p_{R_1+R_2}||_infinity
 <=4sqrt(2e)[Z_2^(1)Z_2^(2)]^(-1/8)
 =9.326575926388497...[Z_2^(1)Z_2^(2)]^(-1/8).
}`                                                                  (6.6)

Moreover `phi_1,phi_2` are both in `L^2`, so `phi_1phi_2` is in `L^1`; Fourier inversion gives a **continuous C_0 density**.  Thus two disjoint critical two-volume resources recover linear small-ball scaling without a physical square.

## 7. Actual target family: the canonical local-extraction obstruction is paid uniformly

The live correction record uses the exact-rank-three family

`A_m = [1] direct_sum J_m/m direct_sum (-J_m/m)`                    (7.1)

as a counterexample to a naive universal dichotomy based on one uniformly good principal `3x3/4x4` block or a rank-three physical cross cut.  Its nonzero spectrum is exactly

`{1,1,-1}`.                                                        (7.2)

The new theorem pays this family directly by **aggregate rank-two crossing plus the third physical square**.

For `m>=2`, let

`r=floor(m/2)`, `s=m-r`.                                           (7.3)

In each of the positive and negative `m`-coordinate banks, put `r` coordinates on the `I` side and `s` on the `J` side.  After peeling the singleton square `X_0^2`, the residual has arbitrary internal quadratic terms on each side and cross block

`B = diag(J_{r x s}/m, -J_{r x s}/m)`.                            (7.4)

The two nonzero singular values of `B` are both

`sqrt(rs)/m`.                                                      (7.5)

Hence

`Z_2 = (rs/m^2)^2`.                                                (7.6)

Use Corollary 6.1 with `d=1` and `h=0`:

`||p_{X^T A_m X}||_infinity
 <=8(2e)^(1/4)(m^2/(rs))^(1/4)`.                                  (7.7)

For every `m>=2`,

`rs/m^2 >= 2/9`,                                                   (7.8)

with the worst case `m=3`.  Therefore

`boxed:
 ||p_{X^T A_m X}||_infinity
 <=8(2e)^(1/4)(9/2)^(1/4)
 =17.791978079303735...,
}`                                                                  (7.9)

uniformly in `m` and in all independent input laws of density at most one.  For even `m` this improves to

`8sqrt(2)(2e)^(1/4)=17.275717919798065...`.                         (7.10)

For `m=1`, the matrix is diagonal and the already-proved diagonal theorem gives the stronger bound `pi`.

Thus the exact family that defeats a uniformly good local principal/cross-rank-three extraction is **not** an obstruction to the critical two-volume route: the two diffuse rank-one banks provide the critical `L^2` collision resource, and the singleton provides the third half-smoothing square.

For this specific family the square is independent and has fixed center.  One can additionally obtain a continuous density by combining the fact that `(2.3)` places the residual density in every finite `L^q`, `q>=2`, with the fact that the square pushforward of any cap-one scalar density belongs to `L^r` for every `1<r<2`.  This continuity remark is specific to the independent fixed-center square application; it is **not** asserted for the general random-center compiler `(6.1)`.

## 8. Exact remaining gap

This result does **not** prove the full conjecture.  It establishes a dimension-free critical `L^2`/collision theorem for every original-coordinate cut with nonzero aggregate two-volume, without any row-marginal gate, and converts it to a bounded output density whenever a third smoothing resource is available as either:

* one genuine completed physical square with quantitative `|d|`; or
* a second independent critical two-volume packet.

The remaining full-target structural implication is to show that every matrix with `s_3(A)>=1` either supplies such a third resource at universal scale together with a rank-two aggregate `Z_2`, or routes into the already-paid rank-three-crossing, diagonal/pivot, grouped-hub, semidefinite, ridge-window, or other certified branches.  A uniformly good single minor remains false, so the extraction must aggregate before reciprocal local payment.

Full QFORM status: **OPEN**.  Full-target continuity status: **OPEN**.
