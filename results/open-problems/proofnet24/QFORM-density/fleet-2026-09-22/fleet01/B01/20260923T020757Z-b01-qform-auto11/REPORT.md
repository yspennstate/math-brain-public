SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B01, 2026-09-23T02:07:57Z.
attacking: diffuse e2 after co-heavy: fractional pair-wedge averaging and distribution-function payment before selecting a physical pair.

# QFORM fleet01/B01: pair-volume L^{3/2} Fourier budget and scalar-square lift

## Status

**ESSENTIAL_STEP_APPLIED / NEW AVERAGED-FREQUENCY THEOREM / FULL QFORM OPEN.**

The unrestricted target is not proved here. The result below closes the diffuse natural-2-volume branch left after the fleet02/B01 heavy-3-volume deletion inequality. It proves an essentially bounded density in its scalar-square-lift scope. Continuity is not proved in that general coupled scope.

This report preserves the phase-aligned fragmented-support counterexample to every law-uniform positive-power pointwise decay estimate for one quadratic phase. The new decay arises only after original-coordinate decoupling, physical-minor averaging and Brascamp--Lieb.


## 1. Fixed-order two-volume Fourier theorem at the borderline exponent

Let `R=X_K^T S X_K` be any real quadratic form in independent original coordinates whose one-dimensional densities are bounded by one. Choose disjoint original-coordinate sets `I,J subset K`, let

`M=S[I,J]`,

and let `Omega` be a probability distribution on nonzero physical `2x2` minors `(P,T)` of `M`. Put

`alpha_i=P_Omega(i in P)`, `beta_j=P_Omega(j in T)`,

and define the entropy-determinant currency

`K_2(Omega)=exp(E_Omega log det(M_{P,T})^2 + H(Omega)).`

Assume only

`alpha_i <= 1/2` for every `i in I`.                                      (1.1)

No assumption is made on `S[I,I]`, `S[J,J]`, the remaining coordinates, signs, rank outside this block, supports, moments, or induced affine terms.

### Theorem 1 (pair-volume L^{3/2} budget)

Under (1.1),

`|phi_R(t)| <= min{1, 2 pi sqrt(e) K_2(Omega)^(-1/4) |t|^(-1)}`.          (1.2)

Consequently

`int_R |phi_R(t)|^(3/2) dt <= 12 pi sqrt(e) K_2(Omega)^(-1/4)`,          (1.3)

and the law of `R` has an `L^3` density satisfying

`||p_R||_3 <= 6^(2/3) e^(1/3) K_2(Omega)^(-1/6)`.                       (1.4)

#### Proof

The mixed-order Brascamp--Lieb proof in the source report gives, before imposing the inversion condition `kbar>2`, the pointwise estimate

`|phi(t)| <= e^(kbar/4)(2pi)^(kbar/2)K(Omega)^(-1/4)|t|^(-kbar/2)`

for every minor law whose row marginals are at most one half. The derivation uses the full positive diagonal-plus-PSD determinant expansion, weighted AM--GM, Lieb's Gaussian Brascamp--Lieb formula, and the source characteristic-function `L^p` lemma. None of those steps requires `kbar>2`; that strict inequality was used only for `L^1_t` inversion.

Here every support minor has order two, so `kbar=2`, which gives exactly (1.2). If

`A=2pi sqrt(e) K_2(Omega)^(-1/4)`,

then

`int_R min(1,A/|t|)^(3/2) dt = 6A`,

proving (1.3). With Fourier convention `phi(t)=int e^(itx)p(x)dx`, Hausdorff--Young for the inverse transform gives

`||p_R||_3 <= (2pi)^(-2/3)||phi_R||_(3/2)`.

Using (1.3),

`||p_R||_3 <= (2pi)^(-2/3)(12pi sqrt(e))^(2/3)K_2^(-1/6)`
`             = 6^(2/3)e^(1/3)K_2^(-1/6)`,

which is (1.4). QED.

The theorem is deliberately at the borderline pointwise exponent `|t|^-1`: it does not give `phi_R in L^1`, but it gives exactly the `L^{3/2}` frequency budget needed by a half-Riesz scalar-square lift.

## 2. Natural pair-volume aggregation: all physical pairs are spent at once

Let

`E_2=e_2(M^T M)=sum_{|P|=|T|=2} det(M_{P,T})^2>0`

and use the natural pair-volume law

`w_2(P,T)=det(M_{P,T})^2/E_2`.

Then

`K_2(w_2)=E_2`.                                                        (2.1)

If `r_i` denotes row `i` of `M`, the natural row marginal is

`q_i = [sum_{k != i} ||r_i wedge r_k||^2]/E_2`.                        (2.2)

Therefore, if

`max_i q_i <= 1/2`,                                                    (2.3)

Theorem 1 gives

`|phi_R(t)| <= min{1,2pi sqrt(e)E_2^(-1/4)|t|^-1}`,                    (2.4)

`int |phi_R|^(3/2) <=12pi sqrt(e)E_2^(-1/4)`,                          (2.5)

and

`||p_R||_3 <=6^(2/3)e^(1/3)E_2^(-1/6)`.                               (2.6)

This is the desired aggregate-before-reciprocal statement. It remains dimension-free even if every individual physical `2x2` minor tends to zero, provided their total two-volume remains fixed and no row captures more than half of that natural two-volume.

## 3. Scalar-square lift from L^3 residual density

Now let the full form contain a nonzero original-coordinate scalar pivot `a=A_00 !=0`. Completing the square only in the physical coordinate `X_0` gives

`Q=a(X_0+m(Y))^2+R(Y)`,                                               (3.1)

where `Y` consists of the remaining independent original coordinates and `R` is the exact Schur residual.

For every fixed `Y`, because the density of `X_0` is at most one, the conditional shifted-square density obeys

`p_{Q|Y}(x) <= |a|^(-1/2)|x-R(Y)|^(-1/2)`.                            (3.2)

If `p_R` is any probability density with `||p_R||_3=N`, then for every `x` and every `rho>0`, Holder on `|x-y|<=rho` and mass one outside gives

`int |x-y|^(-1/2)p_R(y)dy <= 4N rho^(1/6)+rho^(-1/2)`.                 (3.3)

The optimum is `rho=(3/(4N))^(3/2)`, yielding

`sup_x int |x-y|^(-1/2)p_R(y)dy <= [8sqrt(2)/3^(3/4)]N^(3/4)`.        (3.4)

Combining (2.6), (3.2), and (3.4) gives the new quantitative branch

**`||p_Q||_infinity <=16 (e/3)^(1/4)|a|^(-1/2)E_2^(-1/8)`.**          (3.5)

Numerically the universal coefficient is

`16(e/3)^(1/4)=15.6103733261280...`.

This proves existence of an essentially bounded density in the stated scope. Because `m(Y)` may depend on `Y`, (3.1) is not in general an independent convolution, so continuity is not claimed from this argument.

## 4. Assigned partner fleet02/B01 r31 applied to an actual inequality

Let a useful physical cross block `M` in the Schur residual have natural three-volume

`Z=e_3(M^T M)>0`,

and let `h` be a natural-three-volume row of marginal

`alpha=P(h in S)>0`,

with row vector `r_h`. Delete `h` and call the remaining cross matrix `N`. The completed assigned-partner fleet02/B01 r31 proves the algebraic inequality

`e_2(N^T N) >= alpha Z / ||r_h||_2^2`.                                (4.1)

Apply the new theorem to `N`. If the natural two-volume law of `N` has every row marginal at most `1/2`, then with `E_2=e_2(N^T N)`,

`||p_Q||_infinity <=16(e/3)^(1/4)|a|^(-1/2)E_2^(-1/8)`
` <=16(e/3)^(1/4)|a|^(-1/2)(alpha Z/||r_h||_2^2)^(-1/8)`.             (4.2)

Equivalently,

**`||p_Q||_infinity <=15.610374 |a|^(-1/2)(||r_h||_2^2/(alpha Z))^(1/8)`.** (4.3)

This closes the branch that the preceding B01 run had left as "diffuse e2 after co-heavy": the partner produces a quantitative complementary `e_2`, and the new pair-volume theorem spends the entire `e_2` without selecting one physical pair.

If (2.3) fails for `N`, there is a row `k` with

`sum_{l != k} ||r_k wedge r_l||^2 > E_2/2`.                           (4.4)

The exact identity

`sum_{l != k} ||r_k wedge r_l||^2
 = ||r_k||^2 sum_{l != k} ||P_{r_k^perp}r_l||^2`                     (4.5)

shows that the only residual obstruction in this branch is now a **heavy wedge hub**: more than half of the complementary two-volume is forced through one physical row. This is qualitatively aligned with the completed fleet02/B01 r32 mixed-hub mechanism, but no universal routing from (4.4) to the exact r32 rank-two/leverage hypotheses is claimed here.

## 5. Exact-target diffuse-pair stress family

Let `r>=2`, `m=2r`, and define `U,V in R^{m x2}` by

- rows `1,...,r` equal `(1/sqrt(r),0)`,
- rows `r+1,...,2r` equal `(0,1/sqrt(r))`.

Then `U^TU=V^TV=I_2`. Set

`M_r=UV^T`

and form the symmetric target matrix

`A_r=[1] direct_sum [[0,M_r],[M_r^T,0]]`.

Its nonzero spectrum is exactly

`{1,1,1,-1,-1}`,

so it satisfies the full target spectral hypothesis. The two nonzero singular values of `M_r` are both one, hence

`E_2=e_2(M_r^T M_r)=1`.

Every natural pair-volume row marginal is `1/r<=1/2`, but every nonzero physical `2x2` determinant has magnitude exactly `r^-2` and therefore tends to zero. Thus any proof that pays one reciprocal physical pair determinant diverges with `r`, while (3.5) gives uniformly for every admissible product law

`||p_{X^T A_r X}||_infinity <=16(e/3)^(1/4)<15.611`.                  (5.1)

The example demonstrates that the new theorem genuinely aggregates the whole pair-volume before inversion.

## 6. Preserved phase-aligned scalar counterexample

For every frequency `s>0` and small `delta>0`, the set

`{x: dist(sx^2,2pi Z)<=delta}`

has infinite Lebesgue measure. Choosing a finite union of components of total length one and taking its indicator as a probability density gives

`Re E exp(isX^2)>=cos(delta)`.

Hence no uniform law-independent pointwise bound `C|s|^-gamma`, `gamma>0`, exists for scalar quadratic phases. Theorems 1--4 do not use or imply such a bound.

## 7. Remaining implication

The next exact structural obligation is

**QFORM-HEAVY-WEDGE-HUB-ROUTING-v1.**

After the heavy-three-volume row deletion, if the complementary natural two-volume law is not diffuse, (4.4)--(4.5) force a physical row carrying more than half of the total pair-wedge energy. Convert that aggregate hub currency, before selecting one vanishing edge/minor, into one of:

1. the fleet02/B01 r32 mixed-hub rank-two/leverage theorem;
2. an outer-pivot plus two-dimensional random-slope gate with dimension-free aggregate determinant;
3. a grouped-square/two-slope packet; or
4. a higher-order mixed-minor law with mean determinant order `>2` and all row marginals `<=1/2`.

The analytic diffuse-e2 payment itself is now complete. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED** and there are not two independent end-to-end reviews of a full candidate.
