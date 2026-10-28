SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T03:44:05Z.
attacking: recursive pair-volume extremality inside the live bi-hub Schur-E2 survivor, together with a product-law two-coordinate L^{3/2} endpoint that retains arbitrary diagonals and affine leakage.

# account03/B13 r23 — physical-pair L^{3/2} regularity and recursive E2 tri-hub descent

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Extremal product laws`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-RELEVANT ANALYTIC AND STRUCTURAL SUPPORTING THEOREMS / FULL QFORM OPEN / FULL CONTINUITY OPEN**

## 1. Exact scope and source boundary

The owner target remains the full arbitrary-dimensional statement for independent ORIGINAL-coordinate real random variables with probability densities bounded by one and a real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, compact-support, connected-support, Gaussian, log-concavity, interval-support, finite-fragment, or post-rotation-independence hypothesis is used below.


The live corrections are respected. In particular, no law-uniform pointwise scalar quadratic-phase decay, arbitrary-joint coarea theorem, positive moment of a worst conditional projection density, bounded-diameter localization, fixed fragment cap, single-good-minor extraction, or deletion of small quadratic curvature on unbounded supports is used.

Completed mathematics used at exact scope:

1. **Order-two pair-volume Fourier budget.** `yspennstate/math-open-problems@fe7160607c46aec2c9b53e2dfc5aee1c1588bc46`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T020757Z-b01-qform-auto11/REPORT.md`. At row-marginal cap `1/2`, an entropy-determinant law on physical `2x2` cross minors gives the borderline `|t|^{-1}` characteristic-function bound, an `L^{3/2}` Fourier budget, and an `L^3` output density.
2. **Entropic D' minor-law proof template and the first Schur-E2 resource.** `yspennstate/math-open-problems@ac50e5d5f2c3030c4bd87d5188117d92ceaf55a1`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T013927Z-account02-B13-fourhub-r12/REPORT.md`. For third volume `Z`, either the ambient density is already bounded by `48 sqrt(e/5) Z^(-1/6)`, or a physical pair yields, in the nonzero-edge branch,

   `a^2 e_2(S_* S_*^T) > (31/512) Z`.                         (1.1)

3. **Designated partner account04/B13 no-attainment purification.** `yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`. Every cap-one marginal is an `L^1` limit of finite convex mixtures of indicators of bounded finite unions of intervals of measure one; fixed bounded product kernels therefore transfer with zero loss. No single interval, bounded diameter, or attained infinite-line optimizer is asserted.
4. **Orientation-uniform hyperbolic pair envelope.** `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, Section 1.2. For an invertible indefinite physical `2x2` matrix `B`, `D=|det B|`, and arbitrary translation of two independent cap-one coordinates,

   `p(t) <= D^(-1/2)[5.2+log_+(16 sqrt(D)/|t-kappa|)]`.        (1.2)

The new results below do not claim the full conjecture.

## 2. New analytic theorem: every nonzero physical cross edge gives uniform L^{3/2}

### Lemma 2.1 — square output L^{3/2}

Let `X` have a probability density bounded by one. For every nonzero `d` and every translation `m`, the law of

`Y=d(X-m)^2`

has an `L^{3/2}` density satisfying

`||p_Y||_(3/2) <= 2^(4/3) |d|^(-1/3)`.                         (2.1)

**Proof.** The density is supported on one half-line and obeys

`p_Y(y) <= A |y|^(-1/2)`, `A=|d|^(-1/2)`.                       (2.2)

For any `T>0`,

`int_(|y|<=T) p_Y(y)^(3/2) dy <=4 A^(3/2) T^(1/4)`,

while on the complement, `p_Y^(3/2)<=A^(1/2)T^(-1/4)p_Y`, so

`int_(|y|>T) p_Y(y)^(3/2) dy <=A^(1/2)T^(-1/4)`.               (2.3)

With `T^(1/4)=1/(2sqrt(A))`, the sum is at most `4A`. Raising to power `2/3` proves (2.1). QED.

### Lemma 2.2 — a self-contained product endpoint

If `U,V` are independent cap-one probability densities and `W=UV`, then for `z!=0`

`p_W(z)<=2/sqrt(|z|)`,                                           (2.4)

and

`||p_W||_(3/2) <=2^(7/3)`.                                      (2.5)

Indeed

`p_W(z)=int f(x)g(z/x) dx/|x|`.

Split at `|x|=r`. The outer part is at most `1/r`. In the inner part use `y=z/x`; it is at most `(r/|z|) int g(y)dy=r/|z|`. The choice `r=sqrt(|z|)` proves (2.4). For any `T>0`, (2.4) and mass one give

`int p_W^(3/2)
 <=16sqrt(2) T^(1/4)+sqrt(2)T^(-1/4)`.                          (2.6)

The optimum is `T^(1/4)=1/4`, giving `int p_W^(3/2)<=8sqrt(2)` and hence (2.5). In particular

`||p_(2aUV)||_(3/2) <=4 |a|^(-1/3)`.                            (2.7)

This endpoint is not needed for the best constant in the next theorem but is a useful independent check on the singular hyperbolic geometry.

### Theorem 2.3 — `QFORM-PHYSICAL-CROSS-PAIR-L32-v1`

Let `U,V` be independent real random variables with probability densities bounded by one. Let

`P=d U^2+2aUV+eV^2+bU+cV+k`, `a!=0`.                             (2.8)

Then `P` has an `L^{3/2}` density and

`boxed: ||p_P||_(3/2) <=2^(5/3)|a|^(-1/3).`                     (2.9)

The constant is uniform in `d,e,b,c,k`.

Consequently, for an arbitrary ambient quadratic polynomial in independent cap-one ORIGINAL coordinates, if one physical off-diagonal coefficient `A_ij=a!=0`, then after conditioning on all other coordinates,

`boxed: ||p_Q||_(3/2) <=2^(5/3)|a|^(-1/3).}`                    (2.10)

No assumption is made on any other matrix entry or eigenvalue.

#### Proof

If `|d|>=|a|/2`, condition on `V`. After completing the scalar square in `U`, Lemma 2.1 gives every conditional density an `L^{3/2}` norm at most

`2^(4/3)|d|^(-1/3) <=2^(5/3)|a|^(-1/3)`.                        (2.11)

Minkowski transfers the same bound to the mixture. The case `|e|>=|a|/2` is symmetric.

It remains to treat

`|d|<|a|/2`, `|e|<|a|/2`.                                      (2.12)

Then the physical pair matrix is invertible indefinite and

`D=|de-a^2| >=3a^2/4`.                                          (2.13)

Complete the deterministic affine square in the two physical coordinates and apply (1.2). Normalize

`g(y)=sqrt(D) p_P(kappa+sqrt(D)y)`.

Then `g` is a probability density and

`g(y)<=5.2+log_+(16/|y|)`.                                      (2.14)

Put `T=16 exp(-10)`. On `|y|<=T`, substitute `t=log(16/|y|)` and use

`(15.2+s)^(3/2)<=sqrt(2)[15.2^(3/2)+s^(3/2)]`.

This yields

`int_(|y|<=T) g(y)^(3/2)dy
 <=32 e^(-10)sqrt(2)[15.2^(3/2)+Gamma(5/2)]`.                   (2.15)

On `|y|>T`, (2.14) is at most `15.2`, hence mass one gives

`int_(|y|>T)g(y)^(3/2)dy <=sqrt(15.2)`.                          (2.16)

The right sides sum to

`4.023203600945891...`,                                         (2.17)

so

`||g||_(3/2)<2.529578`.                                         (2.18)

Scaling back and using (2.13),

`||p_P||_(3/2)<2.529578 (4/3)^(1/6)|a|^(-1/3)
                <2.654 |a|^(-1/3)
                <2^(5/3)|a|^(-1/3)`.                            (2.19)

This proves (2.9). For the ambient statement, condition on every coordinate except `i,j`. The conditional polynomial has the same fixed `d=A_ii`, `e=A_jj`, `a=A_ij`, while all outside couplings merely change `b,c,k`. The uniform conditional `L^{3/2}` bound and Minkowski prove (2.10). QED.

### Actual application of the designated account04/B13 result

For a product of arbitrary unit-measure indicator densities, Theorem 2.3 and Holder give, for every interval `J`,

`P{Q in J} <=2^(5/3)|a|^(-1/3)|J|^(1/3)`.                      (2.20)

Apply the completed account04/B13 finite-mixture/no-attainment theorem to the bounded kernel `1_{Q in J}`. Expanding the finite product mixtures transfers (2.20), with **zero constant loss**, to every admissible cap-one product law. This is an actual inequality-level use of the designated partner. The direct Minkowski proof above independently yields the stronger `L^{3/2}` statement.

## 3. New recursive extremal theorem for aggregate second exterior volume

Let `R` be any quadratic polynomial in independent cap-one original coordinates. Choose disjoint original-coordinate banks and let `S` be their physical cross block. Put

`E=e_2(S^T S)=sum_(|P|=|T|=2) det(S[P,T])^2>0`.                 (3.1)

Let `A_2` be the finite set of nonzero physical `2x2` minors and let `mu` be any probability law on `A_2`. Define row/column inclusion marginals

`alpha_i=P_mu(i in P)`, `beta_j=P_mu(j in T)`,

and entropy-determinant currency

`K_2(mu)=exp(H(mu)+E_mu log det(S[P,T])^2)`.                     (3.2)

### Theorem 3.1 — `QFORM-E2-ENTROPIC-L3-v1`

Fix `1/2<=h<3/4` and put `q=2h`. If

`alpha_i<=h` for every physical row,                             (3.3)

then `R` has an `L^3` density satisfying

`boxed:
 ||p_R||_3
 <= A(h) K_2(mu)^(-1/6),
 A(h)=[6 sqrt(e/(2h))/(3-4h)]^(2/3).
`                                                                  (3.4)

No condition is imposed on same-bank quadratic curvature, outside couplings, affine terms, signs, or column marginals.

#### Proof

Use the same original-coordinate one-sided Weyl differencing and Gaussian Brascamp--Lieb determinant expansion as the completed order-two theorem and the entropic order-three D' theorem. If `F` is the resulting product of scalar characteristic-function factors, then

`|phi_R(t)|^2<=E F`, `0<=F<=1`.                                  (3.5)

Since `q>=1`,

`E F <=(E F^q)^(1/q)`.                                          (3.6)

Weighted AM--GM over the minor law gives the determinant lower bound with currency `K_2(mu)`. Sharp Hausdorff--Young is admissible because `q/alpha_i>=2`. The row alpha factors cancel the Gaussian BL factors. Since `sum alpha_i=sum beta_j=2` and `-(1-x)log(1-x)<=x`, the column entropy factor is at most `e`. Therefore

`E F^q
 <= e (2pi/|t|)^2 q^(-1) K_2(mu)^(-1/2)`.                  (3.7)

Hence

`|phi_R(t)|
 <=min{1,
 [e(2pi)^2/q]^(1/(2q)) K_2(mu)^(-1/(4q)) |t|^(-1/q)}.           (3.8)

Because `q<3/2`, its `3/2` power is integrable. If `T` denotes the crossover scale, direct integration gives

`int_R |phi_R(t)|^(3/2)dt
 <= [12pi sqrt(e/q)/(3-2q)] K_2(mu)^(-1/4).`                    (3.9)

Inverse Hausdorff--Young then gives exactly (3.4). At `h=1/2`, (3.4) reduces to the completed account01/B01 constant `6^(2/3)e^(1/3)`, providing an endpoint consistency check. QED.

### Theorem 3.2 — `QFORM-E2-ENTROPY-OR-TRIHUB-v1`

Let `w_2(P,T)=det(S[P,T])^2/E` be the natural pair-volume law. Fix `h in [1/2,3/4)` and `L>0`. In each orientation, one of the following holds:

1. there is a minor law `mu` with all row marginals at most `h` and `D(mu||w_2)<=L`; consequently

   `||p_R||_3 <= A(h)e^(L/6) E^(-1/6)`;                         (3.10)

2. there is a physical row hub set `H` with

   `|H|<=floor(2/h)`                                             (3.11)

   such that deleting `H` leaves less than `e^(-L)E` of the total pair volume.

If the cap-feasible set is empty, at most `ceil(2/h)-1` rows kill all nonzero pair volume.

#### Proof

The exact identity

`K_2(mu)=E exp(-D(mu||w_2))`                                     (3.12)

is immediate from the definition. If a feasible law has entropy cost at most `L`, Theorem 3.1 proves (3.10).

If the feasible set is empty, regard supported row pairs as a weighted graph. Absence of a probability law with vertex loads at most `h` is equivalent, by fractional matching/vertex-cover duality, to a fractional vertex cover `y_i>=0` with `sum y_i<1/h` and `y_i+y_j>=1` on every supported edge. The set `H={i:y_i>=1/2}` meets every supported edge and has `|H|/2<=sum y_i<1/h`, proving the zero-residual statement.

If the feasible set is nonempty but every feasible law has relative entropy greater than `L`, the finite entropy-projection dual gives nonnegative `lambda_i`, with `R=sum lambda_i`, such that

`E_w exp[-(lambda_i+lambda_j)] < exp(-L-hR)`.                    (3.13)

Set `H={i:lambda_i>=hR/2}`. Then `|H|<=2/h`. On every pair disjoint from `H`, `lambda_i+lambda_j<hR`; multiplying (3.13) by `exp(hR)` gives

`P_w(P cap H=empty)<e^(-L)`.                                    (3.14)

Cauchy--Binet identifies this probability with the residual pair-volume ratio. QED.

### Clean three-hub specialization

Choose

`h=3/5`, `L=log 4`.                                              (3.15)

Then `floor(2/h)=3`, and either

`boxed: ||p_R||_3 <7.681 E^(-1/6),}`                             (3.16)

or there are at most three physical row hubs whose deletion leaves less than `E/4`.

Apply the same statement to `S^T`. If neither orientation pays (3.16), there are row and column hub sets `H_R,H_C`, each of size at most three, for which the natural pair-volume law satisfies

`P(P intersects H_R)>3/4`, `P(T intersects H_C)>3/4`.            (3.17)

Hence

`P(P intersects H_R and T intersects H_C)>1/2`.                 (3.18)

There are at most nine row-column hub pairs, so some physical pair `(i,j)` has joint pair-minor mass

`boxed:
 E_ij:=sum_(P contains i,T contains j)det(S[P,T])^2 > E/18.
}`                                                                  (3.19)

Reindex this pair first and write

`S=[[b,p^T],[q,T]]`.                                             (3.20)

Every joint `2x2` minor is `b T_kl-q_k p_l`, so the complete joint mass has the exact Frobenius identity

`boxed: E_ij=||bT-q p^T||_F^2.}`                                 (3.21)

Thus the unpaid nested branch has the explicit alternatives

`b!=0:  b^2 ||T-q p^T/b||_F^2 > E/18`,                          (3.22)

or

`b=0:   ||p||_2^2 ||q||_2^2 > E/18`.                            (3.23)

No single residual entry or minor is selected.

## 4. Apply the recursive theorem to the live first Schur-E2 survivor

Take the completed account02/B13 nonzero-edge survivor (1.1). Put

`E=e_2(S_*S_*^T)`.

Apply Theorem 3.2 to the actual Schur critical quadratic on the remaining ORIGINAL coordinates. Either its density is `L^3` with

`||p_R||_3 <7.681 E^(-1/6)
             <12.257 |a|^(1/3) Z^(-1/6)`,                       (4.1)

where the second inequality uses `a^2E>31Z/512`, or the Schur cross block itself contains a nested physical row-column pair obeying (3.22) or (3.23) with `E` in place of the total second volume.

This is a genuine recursive descent of the exterior-volume obstruction:

`third volume Z -> physical pair -> Schur E2 -> either L3 smoothing or one pair carrying a Frobenius/rank-one-star packet.`

The important exponent in (4.1) is `|a|^(1/3)`. Theorem 2.3 supplies the exactly complementary physical-pair exponent `|a|^(-1/3)`.

### Dependence-safe endpoint that is now fully paid

If, in addition, the selected physical pair is independent of the Schur residual after the exact algebraic decomposition, so that

`Q=P(U,V)+R(Y)`                                                   (4.2)

with `(U,V)` independent of `Y`, the pair polynomial has cross coefficient `a` and `R` is the residual in (4.1), then Young's inequality gives

`||p_Q||_infinity
 <= ||p_P||_(3/2) ||p_R||_3
 < 2^(5/3)*12.257 Z^(-1/6)
 <38.912 Z^(-1/6).`                                              (4.3)

Thus the **independent-pair endpoint of the Schur-E2 survivor is closed with a linear slab bound**. This endpoint allows arbitrary pair diagonals and affine terms; it does not require the pair to be hyperbolic or nonsingular.

For the general live survivor, however, the pair's affine translations depend on the same residual coordinates that generate `R`. Uniform conditional `L^{3/2}` control plus an `L^3` critical-value density does **not** by itself justify the convolution step (4.3). The current conditional-cap/dependence corrections prohibit silently replacing this dependence by independence. Therefore the general branch is not claimed solved.

## 5. Why this changes the remaining problem

Before this run, the nonzero-edge Schur survivor was summarized only by the aggregate currency `a^2E`. The new results show more:

* every physical cross edge, with completely arbitrary surrounding curvature, already supplies a dimension-free **full-output `L^{3/2}` norm** at the critical exponent `|a|^(-1/3)`;
* the entire Schur `E2` bank can be entropy-rebalanced into an `L^3` critical-value density with the complementary scale `E^(-1/6)`, or else it collapses onto at most three row and three column hubs;
* in the paid residual branch, the first-level resource `a^2E>31Z/512` cancels the two exponents exactly; the only missing step is a dependence-safe replacement for convolution;
* if the residual pair-volume is not payable, the obstruction descends one exterior order further to the exact Frobenius/star identities (3.22)-(3.23).

So the new first B13 obligation is no longer an unspecified `edge + E2` smoothing problem. It is:

**`QFORM-DEPENDENT-PAIR-L32-L3-GLUING-v1`.** In the exact physical-pair completion, retain the original-coordinate provenance of the pair translations and prove a linear small-ball estimate from the uniform conditional `L^{3/2}` pair theorem plus the `L^3` Schur critical-value theorem; or construct a valid source-level counterexample to that gluing interface. If this gluing fails, route the nested tri-hub Frobenius/star packet (3.22)-(3.23) through the completed grouped-bank/mixed-hub mechanisms before selecting any reciprocal local minor.

This is materially narrower than the preceding `QFORM-N3-ENTROPIC-PAIR-SCHUR-AGGREGATE-SMOOTHING-v1` obligation.

## 6. Status

Proved in this run:

1. `QFORM-PHYSICAL-CROSS-PAIR-L32-v1`: every nonzero physical off-diagonal coefficient gives the full ambient output an `L^{3/2}` density with norm at most `2^(5/3)|A_ij|^(-1/3)`, uniformly over every other coefficient and every admissible product law;
2. `QFORM-E2-ENTROPIC-L3-v1`: arbitrary entropy-reweighted physical pair-volume laws with row marginal cap `<3/4` give an explicit `L^3` output theorem;
3. `QFORM-E2-ENTROPY-OR-TRIHUB-v1`: failure of that payment in both orientations compresses the entire residual `E2` currency to at most three row hubs and three column hubs, then to one physical pair carrying `>E/18`, with exact Frobenius/Schur identities;
4. a direct application to the live account02/B13 first Schur-E2 survivor, including exact critical-exponent cancellation and a complete independent-pair endpoint bound `<38.912 Z^(-1/6)`;
5. the designated account04/B13 extremal-product theorem is applied to the actual slab inequality (2.20), with zero loss and no interval-extremality assumption.

Still open: full QFORM, the general dependent pair-to-Schur gluing, the zero-edge first-level cofactor branch, and the separate full continuity assertion. The new theorems establish essential densities in their stated `L^{3/2}`/`L^3` scopes; they do not establish a continuous representative there.
