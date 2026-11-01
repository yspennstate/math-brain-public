SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T22:31:16Z.
attacking: grouped pair-volume cancellation after the newly published grouped-hub/three-leaf theorem: prove a dimension-free intrinsic L1 transverse-curvature collapse and four-point finite-center rigidity in the diffuse exact-rank-two survivor.

# fleet03/B13 r36 — intrinsic pair-volume cancellation law and four-point rigidity

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T223116Z-fleet03-B13-qform-r36`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **new supporting theorems proved; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED; global continuity remains OPEN.**

No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation independence, interval extremality, uniform support diameter, fixed fragment count, or deletion of a coefficient-small quadratic tail is used.

## 1. Source-pinned premises and duplicate-avoidance


The designated partner actually used is fleet04/B13:

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T201653Z-fleet04-B13-extremal-slab-dichotomy-r1/REPORT.md`.

Its two inputs used here are:

1. the optimizer-free product-law identity

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 = sup_{|E_i|=1} int_{prod_i E_i} K`

for nonnegative measurable `K`, with bounded finite-union epsilon witnesses but no attained interval optimizer, bounded diameter, or bounded fragment count; and

2. in the diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`, `c_i=||u_i||^2`, `s_3(A)>=1`,

there is a physical `k` with `|d_k|>=1` such that every slab ratio

`rho=P{X^T A X in J}/|J|`

satisfies

`|A_kk det Lambda| <=1536 e^2 rho^(-4)`.                          (1.1)

Put

`H0=sqrt(1536 e^2)=106.53445530886934...`.                         (1.2)

Thus the following exhaustive split is valid:

- if `|det Lambda|<=H0 rho^(-2)`, then
  `dist_op(U Lambda U^T, SymRank_{<=1})<=sqrt(H0) rho^(-1)`;
- otherwise `|det Lambda|>H0 rho^(-2)` and (1.1) forces
  `|A_kk|<=H0 rho^(-2)`.                                           (1.3)

During this run, fleet01/B13 independently published the exact grouped-hub / three-leaf theorem I was beginning to derive. Per the owner rule that a source-matching completed theorem ends duplicate work on that exact scope, I did not republish it. I consumed its stronger constant instead:

`yspennstate/math-open-problems@38a8a2ae1cb319211ab4be60f6f8d6f7f03f85f9`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T223205Z-fleet01-B13-qform-auto11/REPORT.md`.

For `L={r,s,t}`, `I=L^c`, in the exact rank-two form above write

`q_ab=det(u_a,u_b)^2`,

`Delta_L=det(U_I^T U_I)=sum_{a<b, a,b in I} q_ab`,

`tau_L=d_r q_st+d_s q_rt+d_t q_rs`.

The fleet01 theorem proves that every slab ratio satisfies

`boxed: Delta_L (det Lambda)^2 |tau_L|
 <= C_T rho^(-5),`

where

`C_T=759375/2=379687.5`.                                          (1.4)

The theorem already works for arbitrary cap-one product laws and aggregates the entire complementary physical hub bank before any pair selection.

The other prior result used is my r34 pair-volume stability theorem:

`yspennstate/math-open-problems@7ebaff80e4d6d1c5c45a561d1ff17a87cfd7a052`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T203053Z-fleet03-B13-qform-r34/REPORT.md`.

For the normalized leave-one-out rank-two Parseval frame at the partner-selected `k`, its physical pair law has disjointness probability at least `1/512` in the diffuse chamber.

## 2. A dimension-free intrinsic pair-volume probability law

Fix the partner-selected `k`. For every unordered pair

`E={r,s} subset [n]\{k}`

put

`q_E=q_rs`,

`Delta_E=det(U_{[n]\{k,r,s}}^T U_{[n]\{k,r,s}})`.                 (2.1)

By Cauchy-Binet,

`Delta_E=sum_{F subset [n]\{k,r,s}, |F|=2} q_F`.                  (2.2)

Also

`Q_k:=sum_{E subset [n]\{k}, |E|=2} q_E
    =det(I_2-u_k u_k^T)=1-c_k`.                                  (2.3)

Normalize the leave-one-out pair law by

`tilde q_E=q_E/Q_k`.

If `delta_k` is the probability that two independent `tilde q`-pairs are disjoint, then (2.2) gives the exact identity

`boxed:
 W_k:=sum_E q_E Delta_E
     =Q_k^2 delta_k.`                                              (2.4)

Indeed both sides equal the ordered sum `sum_{E cap F=empty} q_E q_F`.

The r34 leverage calculation gives `delta_k>=1/512`. Since `c_k<=1/3`, `Q_k>=2/3`, hence

`boxed: W_k>=1/1152.`                                              (2.5)

Therefore

`mu_k(E):=q_E Delta_E/W_k`                                        (2.6)

is a genuine probability law on physical pairs and its normalization is bounded away from zero by a universal constant. This is important: `mu_k` does not select one reciprocal minor and it does not lose the number of coordinates.

## 3. Main new theorem: weighted transverse curvature is L1-small

### Theorem `QFORM-DPP-WEIGHTED-TRANSVERSE-L1-v1`

In the diffuse exact-rank-two chamber above, for the partner-selected `k`, define

`tau_E=tau_{krs}=d_k q_rs+d_r q_ks+d_s q_kr`

for `E={r,s}`. Then

`boxed:
 E_{E~mu_k} |tau_E|
 <=437400000 |det Lambda|^(-2) rho^(-5).}`                         (3.1)

#### Proof

For a pair with `q_E Delta_E>0`, the triple `L={k,r,s}` has rank two and its complement has rank two, so the source-pinned grouped-hub theorem (1.4) applies:

`Delta_E (det Lambda)^2 |tau_E|<=C_T rho^(-5)`.                   (3.2)

If `q_E Delta_E=0`, its contribution below is zero anyway. Multiply (3.2) by `q_E` and sum:

`sum_E q_E Delta_E |tau_E|
 <= C_T |det Lambda|^(-2) rho^(-5) sum_E q_E`

`= C_T Q_k |det Lambda|^(-2) rho^(-5)`

`<= C_T |det Lambda|^(-2) rho^(-5)`.                              (3.3)

Divide by `W_k>=1/1152`. Since `1152 C_T=437400000`, (3.1) follows. QED.

This is the first point at which the new grouped-hub theorem and the r34 DPP disjointness floor combine to eliminate **both** the reciprocal-hub-pair loss and the raw number-of-pairs loss.

### Corollary 3.2 — actual application of fleet04/B13

Apply the exhaustive partner split (1.3).

If the rank-one branch occurs, then

`dist_op(U Lambda U^T, SymRank_{<=1})
 <=10.321552950446426 rho^(-1)`.                                  (3.4)

Otherwise

`|det Lambda|>H0 rho^(-2)` and `|A_kk|<=H0 rho^(-2)`.              (3.5)

Substituting the determinant lower bound into (3.1) gives

`boxed:
 E_{mu_k}|tau_E|
 <= [437400000/(1536 e^2)] rho^(-1)
 <38538.837 rho^(-1).}`                                           (3.6)

Consequently Markov gives the dimension-free positive-mass conclusion

`boxed:
 mu_k{E: |tau_E|<=77077.674 rho^(-1)} >=1/2.}`                    (3.7)

So the partner's non-rank-one near-null branch cannot escape merely because the physical Pluecker mass is spread over arbitrarily many tiny pairs: at least half of a canonically normalized aggregate pair-volume law lies on leaf pairs with transverse diagonal curvature `O(rho^-1)`.

This is an equation-level use of the designated fleet04/B13 theorem, not a status citation.

## 4. Four-point algebra for systematic cancellation

The remaining obstruction in (3.7) is not lack of pair volume; it is the algebraic possibility that many `tau_{krs}` are small by signed cancellation. The following exact identity exposes that cancellation.

Assume `c_k>0`. Rotate only the **two-dimensional coefficient basis** (not the random coordinates) so that

`u_k=(sqrt(c),0)`, `c=c_k`.

For every `i!=k` with `q_ki>0`, write

`u_i=(x_i,y_i)`, `s_i=y_i^2=q_ki/c`, `z_i=x_i/y_i`.

Then

`q_ij=s_i s_j (z_i-z_j)^2`.                                      (4.1)

Put

`alpha=d_k/c`, `e_i=d_i/s_i`.

A direct substitution gives

`tau_{kij}
 =c s_i s_j [alpha(z_i-z_j)^2+e_i+e_j]`.                          (4.2)

Equivalently define

`F_ij:=c tau_{kij}/(q_ki q_kj)`.

Then

`F_ij=alpha(z_i-z_j)^2+e_i+e_j`.                                  (4.3)

For four distinct indices `r,s,t,u` with positive `q_k*`, the `e` terms cancel and

`boxed:
 F_rt+F_su-F_ru-F_st
 =-2(d_k/c)(z_r-z_s)(z_t-z_u).}`                                  (4.4)

This is an exact four-point rigidity identity.

## 5. Quantitative finite-center rigidity

### Theorem `QFORM-FOURPOINT-TRANSVERSE-CANCELLATION-RIGIDITY-v1`

Continue in the diffuse chamber and use the same partner-selected `k`, so `|d_k|>=1` and `c<=1/3`.

Let `S subset [n]\{k}` have at least four indices and suppose there are numbers `a,b>0` such that

`q_ki>=a` for every `i in S`,                                     (5.1)

and

`Delta_{kij}:=det(U_{[n]\{k,i,j}}^T U_{[n]\{k,i,j}})>=b`
for all distinct `i,j in S`.                                      (5.2)

Then there is at most one exceptional index `i_* in S` such that the projective slopes of the remaining rows satisfy

`boxed:
 diam{z_i: i in S\{i_*}}
 <= 580.948 a^(-1)b^(-1/2)|det Lambda|^(-1) rho^(-5/2).}`         (5.3)

In the non-rank-one branch (3.5), this strengthens to

`boxed:
 diam{z_i: i in S\{i_*}}
 <5.454 a^(-1)b^(-1/2) rho^(-1/2).}`                              (5.4)

#### Proof

For distinct `i,j in S`, (1.4), (5.1), and (5.2) imply

`|F_ij|
 = c |tau_{kij}|/(q_ki q_kj)
 <= c C_T [a^2 b (det Lambda)^2]^{-1} rho^(-5).`                  (5.5)

Apply (4.4). The sum of the four `F` terms is at most four times (5.5), hence

`|(z_r-z_s)(z_t-z_u)|
 <= [2 c^2 C_T/(|d_k| a^2 b (det Lambda)^2)] rho^(-5)`

`<= 84375 [a^2 b (det Lambda)^2]^{-1} rho^(-5)`                   (5.6)

for every four distinct indices in `S`; the last step uses `c<=1/3`, `|d_k|>=1`, and `(2/9)C_T=84375`.

We use the elementary one-dimensional cluster lemma: if real numbers `{z_i}` satisfy

`|z_r-z_s||z_t-z_u|<=epsilon`

for every four distinct indices, then all but at most one lie in an interval of length at most `2 sqrt(epsilon)`. To see this, choose a diameter pair. If its diameter is at most `2sqrt(epsilon)`, everything is already clustered. Otherwise every pair among the remaining points has separation below `sqrt(epsilon)/2`; two remaining points then show that at least one endpoint of the diameter pair is within `sqrt(epsilon)` of that cluster, so deleting the other endpoint leaves diameter below `2sqrt(epsilon)`.

Taking the square root of (5.6) gives (5.3), because

`2 sqrt(84375)=580.947501931...`.                                 (5.7)

In branch (3.5), `|det Lambda|^{-1}<H0^{-1}rho^2`; insertion into (5.3) gives (5.4), since

`580.947501931/H0=5.453141899...`. QED.

The theorem does not claim a dimension-free lower bound `a` or `b` for one chosen physical row/minor. It says that **wherever** a positive-scale physical star/complement packet exists, systematic transverse cancellation itself forces a one-center-plus-one-outlier projective geometry at an explicit rate. The remaining global step must aggregate over packets rather than select one tiny coordinate.

## 6. Exact zero-set classification

The four-point theorem also identifies the exact algebraic endpoint.

Assume `c_i<=1/3`, `d_k!=0`, `c_k>0`, and every eligible grouped invariant with leaf triple `{k,r,s}` is zero.

First, if for some pair `r,s`

`Delta_{krs}=det(I-U_{krs}^T U_{krs})=0`,                          (6.1)

then `U_{krs}^T U_{krs}` has eigenvalue one. Its trace is at most
`c_k+c_r+c_s<=1`, so equality must hold throughout: all three leverages equal `1/3`, the three rows are collinear, and the complement Gram matrix is the orthogonal rank-one projector. Hence **all remaining rows are collinear on the orthogonal coefficient line**. This is an exact two-bank localization.

Otherwise every complement determinant is positive. Put `u_k=(sqrt(c),0)` as above and let

`S={i!=k:q_ki>0}`.

Since the second column of `U` has squared norm one and every row leverage is at most `1/3`, `|S|>=3`. All equations (4.3) vanish on pairs in `S`.

If `|S|=3`, then `sum_{i in S}y_i^2=1` and `y_i^2<=1/3`, so all `y_i^2=1/3`; the leverage bound forces `x_i=0`, hence all three slopes coincide.

If `|S|>=4`, (4.4) with zero left side says

`(z_r-z_s)(z_t-z_u)=0`

for every four distinct indices. Therefore all but at most one of the `z_i` are equal. Thus the rows of `U` lie on at most three coefficient lines: the pivot line, one common nonpivot line, and at most one exceptional nonpivot line.

Moreover, on the repeated nonpivot line (which has at least three members in the only nontrivial case), (4.3) reduces to `e_i+e_j=0` for every pair, forcing every such `e_i=0`, hence `d_i=0` there. If there is one exceptional nonpivot row `j`, its diagonal is fixed by

`e_j=-alpha(z_j-z_0)^2`.                                         (6.2)

For a row `p` parallel to `u_k`, pairing it with any nonparallel row in the zero-invariant equations gives

`d_p=-d_k c_p/c_k`.                                               (6.3)

Thus the exact systematic-cancellation zero set is not arbitrary: it is a finite-center coefficient geometry with explicit diagonal relations. What remains is to pay this finite-center normal form in the original product variables, not to rediscover pair volume.

## 7. Extremal product-law interpretation

The designated fleet04/B13 bathtub theorem means every slab statement above has an equivalent geometric unit-product-set formulation. In particular, no centered interval or single connected support is assumed. Strict cap-one product witnesses may be moved to bounded finite-union unit sets with arbitrary small loss, and the inequalities are then passed back by the supremum identity.

This is the correct extremal-product reduction for the present calculations; it does not assert an attained global optimizer.

## 8. Deterministic checks

A local deterministic numerical check sampled random rank-two Parseval frames and verified:

1. `Delta_E=sum_{F disjoint E,k}q_F` by Cauchy-Binet;
2. `sum_E q_E Delta_E=(1-c_k)^2 delta_k` for the normalized leave-one-out pair law;
3. the exact four-point identity (4.4).

The first two identities were checked on 3000 random frames with normalized errors below `1.0e-15`. The four-point identity was checked on 5000 random frames / random diagonals with normalized error below `3.4e-11`. These are sanity checks only; the proofs above are exact algebra.

Exact constants:

`C_T=759375/2=379687.5`,

`1152 C_T=437400000`,

`437400000/(1536 e^2)=38538.836515426...`,

`(2/9)C_T=84375`,

`2 sqrt(84375)=580.947501931...`,

`580.947501931/H0=5.453141899...`.

## 9. What remains

**Full QFORM remains OPEN. Global continuity remains OPEN.** No counterexample is produced.

The grouped-hub theorem removes the old reciprocal-hub-pair obstruction. The new L1 theorem removes the raw pair-count obstruction as well: the remaining diffuse exact-rank-two survivor has a canonical probability law `mu_k` on physical leaf pairs for which transverse curvature is `O(rho^-1)` in the partner non-rank-one branch. The four-point identity shows that whenever this cancellation occurs on a packet with nonnegligible pivot-star and complement-volume weights, its projective carrier rows collapse to one center plus at most one outlier at `O(rho^-1/2)` scale.

The next B13 implication is therefore

`QFORM-MU-CANCELLATION-TO-FINITECENTER-GLUE-v1`:

upgrade the `mu_k`-average `O(rho^-1)` cancellation to a product-preserving finite-center/bank receiver without imposing a lower bound on a single `q_ki` or `Delta_{kij}`. The exact zero-set classification above supplies the target normal form; the missing step is a weighted stability/aggregation theorem, not another local minor selection.
