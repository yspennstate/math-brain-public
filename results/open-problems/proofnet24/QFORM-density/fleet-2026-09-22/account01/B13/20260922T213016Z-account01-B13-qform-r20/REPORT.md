SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B13, 2026-09-22T21:30:16Z.
attacking: the exact-rank-three high-leverage remainder by a leave-one-out regression identity and aggregate-before-inversion two-bank cross collar.

# Leave-one-out collapse to one heavy original coordinate and two robust cross banks

**Run:** `20260922T213016Z-account01-B13-qform-r20`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Extremal product laws  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_REDUCTION / FULL-QFORM-OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The full quadratic-form bounded-density conjecture remains OPEN. This report proves a new exact-rank-three reduction inside the only mixed heavy/light geometry left by the designated partner. Every still-unpaid mixed exact-rank-three instance can, after conditioning on at most one additional **original** light coordinate, be put into a canonical product-preserving collar with exactly one leverage-heavy original coordinate and all remaining normalized rows below leverage one half. A non-small physical pivot in that collar is then paid by the completed rank-three fractional-trace theorem. If the pivot is small, the heavy coordinate necessarily has a dimension-free aggregate cross interaction with the light product source, and that cross interaction can be split into two disjoint original-coordinate banks, each carrying a fixed fraction of the total cross energy. This is an aggregate-before-inversion structural gain; it does not yet close the two-bank smoothing step.

No arbitrary-joint coarea estimate, conditional projection-density positive moment, conditional-cap-as-independence step, law-uniform pointwise quadratic oscillatory decay, fixed good minor, bounded support, bounded diameter, single-interval extremality, or uniformly bounded fragment count is used.

## 1. Fresh source state and exact dependencies

The current owner control is revision `2026-09-22.15`; QFORM remains the sole research target. The full conjecture is still recorded OPEN. The live correction inbox was reread before this write, including the false arbitrary-joint coarea gate, the divergent conditional positive-moment gate, the false fixed-minor/cross-rank reductions, the bounded-diameter and bounded-fragment counterexamples, and the one-heavy-square absorption obstruction.

The designated partner actually applied is **account02/B13**.

1. `QFORM-PRODUCT-BANGBANG-REDUCTION-v1`, canonical source

   `yspennstate/math-open-problems@604a08009638981da254a72f09a24dd50e3a3c94`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T115714Z-account02-B13-qform-480ba28b/REPORT.md`.

   For every fixed measurable slab kernel, the supremum over all independent one-dimensional densities `0<=f_i<=1`, `integral f_i=1`, equals the supremum over arbitrary product indicators `1_{E_i}` with `|E_i|=1`. The reduction is performed in the original independent coordinates and costs no constant. No single-interval or centered-uniform conclusion is made.

2. `QFORM-RANK3-HEAVY-LIGHT-TRICHOTOMY-v1`, canonical source

   `yspennstate/math-open-problems@d511859edaa636cdc00fcd64155ab07506875c3d`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T182158Z-account02-B13-qform-4ebdd821/REPORT.md`.

   For exact rank three

   `A=R Lambda R^T`, `R^T R=I_3`, `min |eig(Lambda)|>=1`,

   put `c_k=||r_k||^2`, `H={k:c_k>3/10}`, `L=H^c`, and let the light Gram have eigenvalues `s_1>=s_2>=s_3`. The branches `s_3>=3/5` and `s_2<=3/5` are already universally paid. The only surviving Gram regime is

   `s_3<3/5<s_2`.

The immediate predecessor is account01/B13 r19,

`yspennstate/math-open-problems@0d8f0844c9d680bf98ab4315c5dbbf17e59fd051`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260922T210011Z-account01-B13-qform-r19/REPORT.md`.

Inside the mixed branch, after an already-paid transverse-leverage branch, it furnishes a heavy original coordinate `i`, a unit spectral vector `u`, and `c>3/10` such that

`r_i=sqrt(c) u`,

while every light row has the orthogonal decomposition

`r_j=q_j u+p_j`, `p_j in u^perp`.

Writing

`G=sum_(j in L) p_j p_j^T`,

one has

`(1/25) I_(u^perp) <= G <= I_(u^perp)`, `det G>=1/25`,                 (1.1)

and, throughout the still-unpaid branch,

`a_j:=p_j^T G^(-1)p_j <1/32` for every `j in L`.                     (1.2)

Define

`h=sum q_j p_j`, `ell=G^(-1)h`, `w_j=q_j-ell^T p_j`,

and

`tau=sum w_j^2=sum q_j^2-h^T G^(-1)h >=0`.                           (1.3)

Then

`sum w_j p_j=0`.                                                       (1.4)

For the retained block `{i} union L`, a shear only in the three-dimensional spectral target gives Gram `diag(c+tau,G)`. Hence its normalized row leverages are exactly

`lambda_i=c/(c+tau)`,                                                  (1.5)

`lambda_j=w_j^2/(c+tau)+a_j`.                                         (1.6)

The r19 theorem pays the branch `tau>=c` if every residual term `w_j^2/(c+tau)<=15/32`. Thus every case still unpaid after r19 satisfies either `tau<c`, or it contains at least one residual-heavy light index with

`w_j^2/(c+tau)>15/32`.                                                 (1.7)

The analytic local theorem used below is `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, canonical source

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

If an original-coordinate principal block has exact rank three, `A_II=V M V^T`, `V^T V=I_3`, and a physical row `i` has normalized squared norm `d_i`, with nonzero physical pivot `A_ii`, then the full ambient form, with arbitrary outside coefficients and cross couplings, satisfies

`||p_Q||_infinity <=128 [d_i |A_ii| |det M|]^(-1/4)`.                 (1.8)

## 2. A global longitudinal budget that was not used in r19

Because `R^T R=I_3`, evaluating the Parseval identity in the direction `u` gives

`1=sum_k (u^T r_k)^2`.

The selected heavy row contributes exactly `c`, and all other contributions are nonnegative. Hence for the light longitudinal coefficients

`s:=sum_(j in L) q_j^2 <=1-c`.                                        (2.1)

Since `tau` is a least-squares residual,

`0<=tau<=s<=1-c`.                                                      (2.2)

In particular, because `c>3/10`,

`tau/c <(1-c)/c <7/3`.                                                 (2.3)

This elementary global budget is what makes one residual-heavy atom removable with a uniform quantitative gain.

## 3. Exact leave-one-out regression identity

Fix a light index `j` and delete it from the light cloud. Put

`G_-j=G-p_j p_j^T`,

and let `tau_-j` be the least-squares residual obtained from the remaining pairs `(q_k,p_k)`, `k!=j`.

### Lemma 3.1 — `QFORM-LIGHT-LEAVEONEOUT-REGRESSION-v1`

If `a_j=p_j^T G^(-1)p_j<1`, then

`boxed(tau_-j = tau - w_j^2/(1-a_j)).`                                (3.1)

Moreover

`G_-j >=(1-a_j)G`, in the normalized sense more precisely
`G_-j=G^(1/2)(I-z_j z_j^T)G^(1/2)`, `z_j=G^(-1/2)p_j`,                (3.2)

so under (1.1)--(1.2)

`boxed(G_-j >=(31/32)G >=(31/800)I)`,                                 (3.3)

`boxed(det G_-j=(1-a_j)det G >31/800)`.                               (3.4)

For every remaining light row,

`a_k^(-j):=p_k^T G_-j^(-1)p_k <1/31`.                                (3.5)

#### Proof

Let `P` be the matrix with rows `p_k^T`, let `q=(q_k)`, and write `ell=G^(-1)P^Tq`. The residual vector is `w=q-Pell`, with `P^T w=0` and `tau=||w||^2`. Deleting observation `j` is a rank-one update of the normal equations. Sherman--Morrison gives

`G_-j^(-1)=G^(-1)+G^(-1)p_j p_j^T G^(-1)/(1-a_j)`.

Substituting this into the exact residual sum of squares

`tau_-j=sum_(k!=j) q_k^2 - h_-j^T G_-j^(-1)h_-j`

and using `w_j=q_j-p_j^T ell` yields (3.1), the standard exact deletion formula.

Equation (3.2) is immediate from `p_j=G^(1/2)z_j`, with `||z_j||^2=a_j`; its smallest eigenvalue is `1-a_j`. The determinant lemma gives (3.4). Finally, for `k!=j`,

`a_k^(-j)=a_k+(p_k^T G^(-1)p_j)^2/(1-a_j)`

and Cauchy--Schwarz in the `G^(-1)` metric gives

`(p_k^T G^(-1)p_j)^2<=a_k a_j`.

Thus `a_k^(-j)<=a_k/(1-a_j)<(1/32)/(31/32)=1/31`. QED.

## 4. One residual-heavy atom collapses the remaining leverage obstruction

Suppose (1.7) holds for some `j`. By Lemma 3.1,

`tau_-j < tau -(15/32)(c+tau)
        =(17 tau-15c)/32`.                                            (4.1)

Using (2.3),

`boxed(tau_-j <(37/48)c)`.                                            (4.2)

Condition on this single original coordinate `X_j`. This is a legal product-preserving operation: all retained original coordinates stay independent with their original one-dimensional density caps, and the conditioned coordinate creates only affine and constant terms in the retained quadratic form.

Recompute the regression on the remaining light set. Its combined-block heavy leverage is

`lambda_i'=c/(c+tau_-j)>48/85`.                                       (4.3)

For every remaining light row, its residual contribution is at most

`w_k'^2/(c+tau_-j) <=tau_-j/(c+tau_-j)<37/85`,                        (4.4)

while (3.5) gives transverse leverage `<1/31`. Therefore

`boxed(lambda_k' <37/85+1/31=1232/2635<1/2)`.                         (4.5)

The margin is explicit:

`1/2-1232/2635=171/5270`.                                             (4.6)

Now consider the other still-unpaid possibility from r19: `tau<c`. If there is a residual-heavy index (1.7), the same deletion argument applies. If there is no such index, then already, without deleting anything,

`lambda_j<15/32+1/32=1/2` for every light `j`,                        (4.7)

while `lambda_i=c/(c+tau)>1/2`.

We have proved the following canonical reduction.

### Theorem 4.1 — `QFORM-RANK3-ONEHEAVY-CANONICAL-COLLAR-v1`

After all branches paid before r20, every still-unpaid exact-rank-three mixed instance can be reduced, by conditioning on **at most one additional original light coordinate**, to a retained exact-rank-three product block with:

1. one distinguished original heavy row `r_i=sqrt(c)u`, `c>3/10`;
2. a light transverse Gram

   `boxed(G_* >=(31/800)I,   det G_*>31/800)`;                         (4.8)

3. light normalized transverse leverages

   `boxed(a_j^*<1/31)`;                                                (4.9)

4. regression residual `tau_*<c`;
5. exactly one normalized row with leverage above one half, namely

   `lambda_i^*=c/(c+tau_*)>1/2`,                                      (4.10)

   while

   `lambda_j^*<1/2` for every remaining light original coordinate.    (4.11)

The conditioning is uniform in the conditioned value and preserves arbitrary outside affine terms. No spectral rotation of the independent source is performed.

This turns the previous finite set of possible high-leverage rows into **one distinguished original coordinate**.

## 5. A non-small physical pivot in the collar is already paid

Work in the collar of Theorem 4.1 and suppress stars. Write the spectral coefficient in the orthogonal decomposition `R u direct_sum u^perp` as

`Lambda u = alpha u + b`, `b in u^perp`,                              (5.1)

where

`alpha=u^T Lambda u`.

The physical pivot on the distinguished original coordinate is

`A_ii=c alpha`.                                                        (5.2)

Normalize the retained rank-three block. Its Gram is `diag(c+tau,G)`, so its normalized heavy-row squared norm is

`d_i=c/(c+tau)`.                                                       (5.3)

The normalized rank-three quadratic coefficient `M` has determinant

`|det M|=(c+tau) det G |det Lambda|`.                                 (5.4)

Thus the product appearing in the completed rank-three fractional-trace theorem (1.8) is exactly

`d_i |A_ii| |det M|
 =c^2 |alpha| det G |det Lambda|`.                                    (5.5)

If

`|alpha|>=1/20`,                                                      (5.6)

then, using `c>3/10`, `det G>31/800`, and `|det Lambda|>=1`,

`d_i |A_ii| |det M|
 > (9/100)(1/20)(31/800)
 =279/1600000`.                                                        (5.7)

Hence

`boxed(||p_Q||_infinity
 <128 (1600000/279)^(1/4)
 <1114).`                                                             (5.8)

This bound is uniform in every coordinate conditioned in reaching the collar, so it also bounds the original unconditional form.

Applying the designated partner's exact bang-bang theorem, the same branch has the genuine product-set slab estimate

`boxed(|{x in product E_k: x^T A x in J}| <1114 |J|)`                 (5.9)

for arbitrary measurable `E_k` with `|E_k|=1`. No interval or bounded-fragment assumption appears.

Therefore the only new exact-rank-three collar still requiring a smoothing mechanism satisfies

`boxed(|alpha|<1/20)`.                                                 (5.10)

## 6. Small pivot forces robust aggregate heavy-light cross energy

Continue under (5.10). Because every eigenvalue of `Lambda` has modulus at least one,

`||Lambda u||>=1`,

and hence from (5.1)

`||b||^2>=1-alpha^2`.                                                  (6.1)

For the current light regression write

`q_j=ell^T p_j+w_j`, `sum w_j p_j=0`, `sum w_j^2=tau`.                (6.2)

The heavy-light physical cross coefficients are

`A_ij=sqrt(c) u^T Lambda r_j
     =sqrt(c)[(b+alpha ell)^T p_j+alpha w_j]`.                         (6.3)

Put

`v=b+alpha ell`,

`X=v^T G v`, `Y=alpha^2 tau`.                                        (6.4)

The orthogonality in (6.2) gives the exact energy identity

`boxed(sum_(j in L) A_ij^2 = c(X+Y)).`                                (6.5)

We now lower-bound `X`. Since `G>=(31/800)I`,

`||G^(1/2)v||
 >=sqrt(31/800)||b||-|alpha| sqrt(ell^T G ell)`.                       (6.6)

Moreover

`ell^T G ell=s-tau<=s<=1-c<7/10`.                                    (6.7)

Under `|alpha|<1/20`, (6.1), (6.6), and (6.7) imply

`||G^(1/2)v||
 >sqrt(31/800)sqrt(399/400)-(1/20)sqrt(7/10)`.                        (6.8)

For a completely rational check,

`sqrt(31/800)>19/100`,
`sqrt(399/400)>99/100`,
`sqrt(7/10)<17/20`,

so the right side of (6.8) is greater than

`(19*99)/10000-17/400=91/625>1/7`.                                   (6.9)

Therefore

`boxed(X>1/49>1/50)`.                                                  (6.10)

Since `Y>=0`, (6.5), `c>3/10`, and (6.10) yield the dimension-free aggregate cross-star bound

`boxed(E_i:=sum_(j in L) A_ij^2 >3/500).`                             (6.11)

Thus a small physical pivot cannot make the heavy coordinate nearly decouple from the light product source.

## 7. The cross star is itself atom-free

The same collar also prevents one light coordinate from carrying most of (6.11). Define

`x_j=v^T p_j`, `y_j=alpha w_j`, so that `A_ij=sqrt(c)(x_j+y_j)`.       (7.1)

By Cauchy--Schwarz in the `G` metric and (4.9),

`x_j^2 <=(p_j^T G^(-1)p_j) X <X/31`.                                 (7.2)

Also

`Y=alpha^2 tau <(1/400)(1-c)<7/4000`.                                (7.3)

Combining (6.10) and (7.3),

`Y/X <7/80`.                                                          (7.4)

Thus, for every light coordinate,

`|x_j+y_j|
 <=sqrt(X/31)+sqrt(Y)
 <sqrt(X)(1/sqrt(31)+sqrt(7/80)).`                                    (7.5)

Use the elementary rational bounds

`1/sqrt(31)<9/50`, `sqrt(7/80)<3/10`.

Their sum is `<12/25<1/2`, so

`(x_j+y_j)^2 <(1/4)X <(1/4)(X+Y)`.                                   (7.6)

Multiplying by `c` and using (6.5),

`boxed(A_ij^2 <E_i/4 for every j in L).`                              (7.7)

This is a genuine anti-atomicity statement for the **physical** heavy-light cross interaction, not merely for spectral leverage.

## 8. Two disjoint robust cross banks

The nonnegative weights `e_j=A_ij^2` have total `E_i` and each is `<E_i/4`. Order the light coordinates arbitrarily and take the first partial sum that reaches `E_i/4`. Because the previous partial sum is below `E_i/4` and the added atom is below `E_i/4`, the resulting bank has weight strictly below `E_i/2`. Its complement therefore has weight above `E_i/2`.

Hence the light original coordinates admit a partition

`L=L_1 disjoint_union L_2`                                           (8.1)

such that

`boxed(sum_(j in L_a) A_ij^2 >=E_i/4 >3/2000,  a=1,2).`               (8.2)

The two banks are disjoint sets of the **original independent coordinates**. Therefore their product sources are genuinely independent of each other and of `X_i`; no independence after a spectral rotation is asserted.

This proves the main new structural theorem.

### Theorem 8.1 — `QFORM-RANK3-ONEHEAVY-TWOCROSSBANK-COLLAR-v1`

After the designated account02/B13 heavy/light trichotomy and the previously paid account01/B13 branches, every still-unpaid exact-rank-three target can be reduced by conditioning on at most one additional light original coordinate to one of two alternatives:

**(P) Pivot-paid.** The distinguished heavy spectral direction has `|u^T Lambda u|>=1/20`, in which case

`||p_Q||_infinity<1114`,

and equivalently every unit-measure product set obeys the slab estimate (5.9).

**(C) Canonical two-cross-bank collar.** The retained exact-rank-three product block has exactly one normalized row of leverage above `1/2`, its physical pivot obeys

`|u^T Lambda u|<1/20`,

and its light original coordinates split into two disjoint banks `L_1,L_2` such that

`sum_(j in L_a) A_ij^2 >3/2000`, `a=1,2`,                            (8.3)

while globally on the light cloud

`G>=(31/800)I`, `det G>31/800`, `a_j<1/31`, `tau<c`,                 (8.4)

and each individual cross atom satisfies `A_ij^2<E_i/4`.

All statements are uniform in the values of the conditioned original coordinates and retain arbitrary induced affine terms.

## 9. Exact use of the extremal-product reduction

The assigned B13 front end is now active at two levels.

First, the partner's bang-bang theorem says that proving a slab inequality on arbitrary unit-measure product indicators is **exactly equivalent** to proving the worst-case small-ball estimate over all cap-one product densities. Thus no generality is lost by formulating the remaining collar problem geometrically.

Second, in the paid pivot branch, (5.8) immediately gives, with no further approximation,

`sup_(|E_k|=1) |{x in product E_k: x^T A x in J}| <1114 |J|`.         (9.1)

The still-unpaid collar therefore has the following exact geometric formulation:

> For arbitrary measurable unit-measure sets `E_k`, prove a universal linear-in-`|J|` bound for the quadratic slab under the structural conditions (8.3)--(8.4), using both disjoint cross banks jointly with the heavy scalar before taking any reciprocal individual coefficient.

This is substantially narrower than the previous unrestricted high-leverage branch and directly implements the requested aggregate-before-inversion strategy.

## 10. What remains unpaid

The first exact missing implication is now

`QFORM-RANK3-ONEHEAVY-TWOCROSSBANK-SMOOTHING-v1`:

> Let one original scalar `X_i` be independent of two disjoint original-coordinate product banks `L_1,L_2`, with small physical pivot `|u^T Lambda u|<1/20`, robust bankwise heavy-light cross energies `sum_(j in L_a)A_ij^2>3/2000`, uniformly elliptic transverse Gram (8.4), and no cross atom carrying one quarter of the total star energy. Prove a universal bounded-density/slab estimate by aggregating the two banks before any reciprocal coefficient or fixed-minor payment.

A valid proof must retain the light-light quadratic interactions and cannot replace either bank by a mere bounded projected density if that destroys source product provenance. The existing corrections specifically rule out the corresponding conditional-cap shortcut.

Separately, even after exact rank three is fully closed, the unrestricted theorem still needs the bridge allowing arbitrary additional spectral directions. Nothing in this report claims that bridge.

Therefore **FULL-QFORM remains OPEN / NOT PROVED**.

## 11. Integrity and status

This report is an immutable private mathematical artifact under the authorized QFORM root. The changed-file content was reviewed for scope and contains no credential, scheduler identifier, personal archive, email content, paid/remote call, public release, machine path, permission change, or cross-account authentication. Repository synchronization is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
