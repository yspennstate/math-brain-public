SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T02:34:54Z.
attacking: convert the newest q-dependent three-volume Fourier gate into a matrix-only one-row/one-column hub alternative, then transfer the paid geometric slab inequality to arbitrary cap-one product laws through the completed account04/B13 no-attainment purification theorem.

# account03/B13 r22 — extreme-product bi-hub reduction and optimized tail stable-rank gate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-RELEVANT STRUCTURAL/ANALYTIC SUPPORTING THEOREMS / FULL QFORM OPEN / FULL CONTINUITY OPEN**

## 1. Exact scope and source-valid inputs

The owner target remains the full arbitrary-dimensional statement: independent ORIGINAL-coordinate probability densities `0<=f_i<=1`, real symmetric `A`, and at least three eigenvalues of `A` with absolute value at least one. No moment, compact-support, connected-support, Gaussian, log-concavity, diagonal-basis, post-rotation-independence, or fixed-fragment assumption is used.


Three completed inputs are used at their exact scopes.

1. **Fractional three-volume Fourier theorem and volume marginals.** `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`. For an ORIGINAL-coordinate cross block `M=A[I,J]`, put

   `Z=e_3(M^T M)>0`.

   Give each pair of row/column triples `(S,T)` weight `det(M[S,T])^2/Z`, and write `alpha_i=P(i in S)`. If `1<=q<3/2` and every `alpha_i<=q/2`, then, with arbitrary within-bank terms, outside couplings and affine terms,

   `||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.      (1.1)

   The density is continuous and vanishes at infinity. The same source proves the exact marginal matrix inequalities

   `0<=W<=I`, `W<=(E_2/Z)MM^T`, `E_2/Z<=3/s_3(M)^2`.         (1.2)

   Its tail extension gives, for the projection `P` onto the top two left singular vectors and `T_2=sum_(j>=3)s_j(M)^2`,

   `sqrt(alpha_i)<=sqrt(P_ii)+sqrt(3)s_3(M)/sqrt(T_2)*sqrt(1-P_ii)`.  (1.3)

2. **Designated partner account04/B13 no-attainment purification.** `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`. Every cap-one mass-one marginal is an `L1` limit of finite convex combinations of indicators of bounded finite unions of intervals of measure one. For every bounded product kernel, the supremum over cap-one product laws equals the supremum over such unit-measure product indicators. No optimizer, threshold attainment, single interval, bounded diameter or fixed fragment count is asserted.

3. **Current no-pivot reduction.** `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`. The unrestricted problem is reduced to one strict no-`tau`-pivot density statement `N3(tau,C0)`. `N3` itself is not proved. I use that reduction only to state the relevance of the new structural survivor below, not as a premise for any positive density estimate.

The live false interfaces are avoided: no law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, positive moment of worst conditional projection density, naive fiber-sup integration, uniformly good single minor, bounded-diameter localization, or finite fragment cap.

## 2. Volume notation

Let `I,J` be disjoint ORIGINAL coordinate sets and `M=A[I,J]`. Assume `rank(M)>=3` and

`Z=sum_(|S|=|T|=3) det(M[S,T])^2=e_3(M^T M)>0`.              (2.1)

Define the probability law

`w(S,T)=det(M[S,T])^2/Z`.                                     (2.2)

Its row and column inclusion marginals are

`alpha_i=P_w(i in S)`, `beta_j=P_w(j in T)`.                  (2.3)

For a row `h` and column `k`, define

`Z_h=sum_(S contains h,T) det(M[S,T])^2=alpha_h Z`,
`Z^k=sum_(S,T contains k) det(M[S,T])^2=beta_k Z`,             (2.4)

and the mixed incident mass

`Z_{h,k}=sum_(S contains h,T contains k) det(M[S,T])^2`.       (2.5)

Deleting one physical row or column gives the exact identities

`e_3(M_{I\{h},J}^T M_{I\{h},J})=(1-alpha_h)Z`,                (2.6)

`e_3(M_{I,J\{k}}^T M_{I,J\{k}})=(1-beta_k)Z`.                 (2.7)

These are only Cauchy--Binet bookkeeping; no random coordinate rotation occurs.

## 3. Main structural theorem — `QFORM-VOLUME-BIHUB-DICHOTOMY-v1`

Fix

`1/2 <= r < 3/4`,                                                (3.1)

and put

`C_r = 3e / ((3-4r)sqrt(2r))`.                                  (3.2)

For every cross block `M` as above, exactly one of the following conclusions is available.

### Paid branch

If

`max_i alpha_i <= r` **or** `max_j beta_j <= r`,                 (3.3)

then for every admissible independent cap-one product law, with arbitrary same-side quadratic terms, outside couplings and affine terms,

`boxed: ||p_Q||_infinity <= C_r Z^(-1/6).`                       (3.4)

The output has a continuous density vanishing at infinity.

### Bi-hub structural branch

If (3.3) fails on both sides, there are a physical row `h` and physical column `k` with

`alpha_h>r`, `beta_k>r`.                                        (3.5)

Consequently

`boxed: Z(delete h)<(1-r)Z,  Z(delete k)<(1-r)Z,`                (3.6)

and Bonferroni applied to the volume law gives

`boxed: Z_{h,k}>(2r-1)Z.`                                       (3.7)

If `kappa=s_3(M)`, the same hubs satisfy

`boxed: ||M[h,:]||_2 > kappa sqrt(r/3),
        ||M[:,k]||_2 > kappa sqrt(r/3).}`                        (3.8)

Thus failure of the diffuse volume gate is not an unspecified collection of heavy rows: it produces one ORIGINAL physical row and one ORIGINAL physical column carrying a quantified fraction of the complete third exterior-volume currency.

### Proof

Set `q=2r`. Then `1<=q<3/2`, and the row condition `alpha_i<=r` is exactly the hypothesis `alpha_i<=q/2` of (1.1). This gives (3.4) with

`3e/((3-2q)sqrt(q))=3e/((3-4r)sqrt(2r))=C_r`.

If instead the column condition holds, write the same cross term as `2 X_J^T M^T X_I` and apply (1.1) to `M^T`; `e_3(MM^T)=e_3(M^T M)=Z` on the nonzero singular spectrum. This proves the paid branch.

If neither gate holds, choose `h,k` as in (3.5). Equations (2.6)--(2.7) immediately give (3.6). Under the probability law (2.2), with events `A={h in S}` and `B={k in T}`,

`P(A intersect B)>=P(A)+P(B)-1>2r-1`,

which is (3.7).

Finally (1.2) gives

`alpha_h <= 3 ||M[h,:]||_2^2/kappa^2`.

Since `alpha_h>r`, the first norm bound in (3.8) follows; apply the same argument to `M^T` for the column. QED.

### Concrete `q=4/3` form

Take `r=2/3`. Then

`C_(2/3)=9sqrt(3)e/2=21.186910062820317...`.                    (3.9)

Hence every rank-three cross block satisfies the sharp structural alternative

`boxed: ||p_Q||_infinity <= (9sqrt(3)e/2) Z^(-1/6)`             (3.10)

with continuous density, **or** there are physical `h,k` such that

`alpha_h,beta_k>2/3`,
`Z(delete h),Z(delete k)<Z/3`,
`Z_{h,k}>Z/3`,
`||row_h||,||col_k||>(sqrt(2)/3)kappa`.                         (3.11)

This is a one-row/one-column replacement for the earlier six-hub entropy alternative at the price of keeping the explicit `Z^(-1/6)` scale.

## 4. Actual application of account04/B13 purification — `QFORM-EXTREME-BIHUB-WITNESS-v1`

The preceding theorem can be phrased purely geometrically and then transferred with zero loss to rough laws.

For a fixed interval `J0`, apply (3.4) first only to product-indicator densities `prod_i 1_{E_i}`, where every `E_i` has measure one. It gives

`|{x in prod E_i : Q(x) in J0}| <= C_r Z^(-1/6)|J0|`            (4.1)

whenever either volume-marginal gate in (3.3) holds.

The designated account04/B13 theorem now applies to the actual bounded kernel

`K(x)=1_{Q(x) in J0}`.

Taking finite convex-mixture approximants and expanding their products yields, with **no constant loss**,

`P_f(Q in J0) <= C_r Z^(-1/6)|J0|`                              (4.2)

for every arbitrary cap-one product law. This uses neither an attained bathtub maximizer nor any interval/centered-uniform extremality assumption. The continuity assertion in the paid branch comes separately from the Fourier theorem (1.1); purification alone is only a slab-bound transfer.

There is also a strict-witness extraction useful for counterexamples. Suppose some arbitrary cap-one product law and interval `J0` satisfy

`P_f(Q in J0) > C_r Z^(-1/6)|J0|`.                              (4.3)

Then the matrix cannot satisfy either gate in (3.3), so it has the bi-hub structure (3.5)--(3.8). Moreover, because the violation in (4.3) has a positive gap, choose the account04/B13 finite-mixture product approximation close enough in total variation that the approximating finite mixture still violates (4.3). At least one product-indicator component then violates (4.3). Thus the same matrix admits a violating witness with every marginal the indicator of a bounded finite union of intervals of total measure one.

This is the exact B13 extreme-product interface needed by the current no-pivot programme: rough densities cannot create an additional branch outside the same matrix geometry.

## 5. Quantitative obstruction for a diverging no-pivot witness

Let a candidate witness have slab ratio

`R = P(Q in J0)/|J0|`.                                          (5.1)

From Theorem 3, for **every** disjoint physical cross block `M` with three-volume `Z>0`,

`boxed: either M is bi-hub at level r,
        or Z <= (C_r/R)^6.}`                                    (5.2)

Indeed, a non-bi-hub block is in the paid branch, hence `R<=C_r Z^(-1/6)`.

Apply this inside the single remaining no-`tau`-pivot class `N3` from the current synthesis. If `N3` were false, account04/B13 purification lets a diverging sequence of slab ratios `R_m -> infinity` be chosen with bounded finite-union unit product sets. Then every cross block in such a witness is forced into one of two sharply quantified forms:

* its third exterior volume is tiny, `Z <= (C_r/R_m)^6`; or
* it contains one row and one column hub satisfying (3.5)--(3.8).

At `r=2/3`, every non-bi-hub cross block obeys

`Z <= (21.186910062820317.../R_m)^6`.                           (5.3)

Therefore any fixed-positive cross three-volume surviving along a putative counterexample sequence must eventually be simultaneously row- and column-concentrated. This is a new structural restriction on the unpaid N3 class; it does not prove that the low-volume/bi-hub survivors are impossible.

## 6. Optimizing the collective-tail stable-rank gate

The newest tail extension used the convenient sufficient threshold `T_2/s_3^2>=225`. The exact `q` freedom in (1.1) improves this substantially.

Let `P` project onto the top two left singular vectors of `M`, assume

`max_i P_ii <= 1/2`,                                             (6.1)

and define

`R_tail = T_2/s_3(M)^2`, `a=sqrt(3/R_tail)`.                     (6.2)

When `a<1`, the function

`f(l)=sqrt(l)+a sqrt(1-l)`

is increasing on `0<=l<=1/2`. Hence (1.3) gives

`alpha_i <= (1+a)^2/2`.                                         (6.3)

The smallest admissible exponent in (1.1) is therefore

`q=(1+a)^2`.                                                     (6.4)

It satisfies `q<3/2` exactly when

`boxed: R_tail > R_* := 30+12sqrt(6)=59.39387691339813... .}`    (6.5)

For every such block,

`boxed:
 ||p_Q||_infinity
 <= C(R_tail) [s_1(M)^2 s_2(M)^2 T_2]^(-1/6),`                  (6.6)

with continuous density, where

`C(R)= 3e / { [1-4sqrt(3/R)-6/R] [1+sqrt(3/R)] }`.              (6.7)

### Proof

Equation (6.3) is the preceding monotonicity calculation. Since `q=2*[(1+a)^2/2]`, it is the minimal allowed `q`; the coefficient in (1.1) increases with `q` on `[1,3/2)`, because `(3-2q)sqrt(q)` is strictly decreasing there. Condition `q<3/2` is

`a<sqrt(3/2)-1`,

which is equivalent to (6.5). Substitute `q=(1+a)^2` in (1.1) to obtain (6.7). Finally

`Z=e_3(s_1^2,s_2^2,...) >= s_1^2 s_2^2 sum_(j>=3)s_j^2=s_1^2s_2^2T_2`,

which proves (6.6). QED.

Two useful checkpoints are:

* if `R_tail >= 9(2+sqrt(3))^2 =125.35382907247958...`, then `q<=4/3`, so `C(R_tail)<=9sqrt(3)e/2=21.1869100628...`;
* at `R_tail=225`, optimizing `q` gives `C=14.29394117441255...`, improving the unoptimized `q=4/3` constant while retaining the same hypotheses.

Thus the collective-tail branch becomes analytically payable already above stable rank `59.394...`; the constant becomes large near that sharp threshold, but finiteness is enough for the universal proof map. The remaining obstruction is correspondingly narrower: low tail stable rank or high top-two physical leverage.

## 7. Deterministic checks

The companion script `check_bihub.py` performs exact rational Cauchy--Binet bookkeeping on two fixed matrices. A duplicated-coordinate `6x3` frame has `Z=8` and every row marginal exactly `1/2`, exercising the paid row gate. The diagonal `diag(10,1,1,1)` example has `Z=301`, row/column hub marginal `300/301`, deletion residuals exactly one, and joint hub mass exactly 300. The script also checks the constants and the exact stable-rank thresholds. Its executed output terminates

`QFORM_B13_R22_BIHUB_STABLERANK_CHECK_PASS`.

These checks corroborate finite algebra only; the proof is the analytic argument above.

## 8. Status and first remaining implication

Proved this run:

1. `QFORM-VOLUME-BIHUB-DICHOTOMY-v1`, converting failure of the fractional-volume density gate into one explicit ORIGINAL row and one explicit ORIGINAL column hub;
2. `QFORM-EXTREME-BIHUB-WITNESS-v1`, applying the designated account04/B13 purification to the actual slab inequality and extracting bounded finite-union product witnesses for every strict violation;
3. the no-pivot obstruction (5.2), forcing every substantial cross three-volume in a diverging witness to be bi-hubbed;
4. an optimized collective-tail stable-rank threshold `R_*=30+12sqrt(6)<59.394`, improving the previous convenient threshold 225 for existence of a finite continuous-density certificate.

Still open: the full QFORM conjecture, the single no-pivot statement `N3`, and the separate full continuity conclusion. The next B13-relevant unpaid implication is to exploit the **mixed hub mass** `Z_{h,k}>(2r-1)Z` together with strict no-pivot entry/pair-determinant constraints, or else show that repeated hub peeling forces one of the completed low-rank/star/grouped-bank estimates. No perturbative deletion of unbounded input coordinates is justified.
