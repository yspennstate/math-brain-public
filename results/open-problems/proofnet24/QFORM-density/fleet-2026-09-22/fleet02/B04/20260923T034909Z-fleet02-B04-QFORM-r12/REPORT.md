SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-23T03:49:09Z.
attacking: quantitative near-coloop interpolation—optimize admissible third-volume weights and compare them with square-assisted ridge on the same genuinely rotated indefinite family.

# fleet02/B04 r12 — exact near-coloop volume optimization and a uniform ridge separation

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: Product Fourier rearrangement. Status: `NEW SUPPORTING THEOREM / EXPLICIT TARGET-VALID ESTIMATE / STRUCTURAL SEPARATION / FULL QFORM OPEN`. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The exact-coloop run showed that positive third volume can have an empty admissible three-volume polytope while square-assisted ridge remains uniform. The first unpaid implication is now the **quantitative near-coloop** case: when the coloop is not exact, optimize the entire admissible volume-weight family rather than one Gibbs weight, determine the entropy price exactly, and decide whether the best volume certificate can regularize a weak singular direction as ridge does.

The answer below is no. On an explicit genuinely rotated indefinite target family, every admissible third-volume weighting is solvable and its global optimum can be written in closed form, including the optimal Fourier exponent `q`; nevertheless every such volume certificate diverges like `epsilon^{-1/3}` as the weak singular value `epsilon -> 0`, whereas the square-assisted ridge estimate stays uniformly bounded. This isolates a real structural difference between the two aggregate mechanisms.

No moments, support bounds, log-concavity, diagonal-basis argument, post-rotation independence, arbitrary-joint coarea, worst conditional-density supremum, or law-uniform pointwise quadratic-phase decay is used.

## 2. Source-pinned completed inputs actually used

1. Claude/e5 Theorem D, source `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. Its arbitrary-weight remark replaces squared-minor volume by

   `G(w)=exp(E_w log det(M_ST)^2 + H(w))`

   for any probability weight on nonzero physical `3 x 3` minors with row marginals at most `1/2`, and gives

   `||p_Q||_inf <= 6 sqrt(e) G(w)^(-1/6)`.

   Section 5 applies this to the exact KL-optimal admissible weight of the family below.

2. B04 weighted fractional extension `QFORM-WEIGHTED-FRACTIONAL-VOLUME-SHARP-v1`, source `yspennstate/math-open-problems@061327b7e45c28e5b8c898ed3729456fcea6f7d7`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T014717Z-fleet02-B04-QFORM-auto11-cont/REPORT.md`. If `1<=q<3/2` and all row marginals obey `alpha_i<=q/2`, then

   `||p_Q||_inf <= C(q) G(w)^(-1/6)`,

   `C(q)=3e/[(3-2q)sqrt(q)]`.

3. Designated partner fleet03/B04 r23, source `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/B04-20260923T032130Z-r23/REPORT.md`. Its reviewed optimized projection-volume gate uses

   `A(L,rho)=[sqrt(L)+sqrt(3) rho sqrt(1-L)]^2`

   and closes the branch when `L<=1/2` and `A(L,rho)<3/4`. Section 6 applies it to the same physical block and computes an exact obstruction: `rho=1`, so the gate cannot certify this near-coloop family even though the top-two projection leverage is small.

4. Square-assisted ridge theorem `QFORM-SQUARE-ASSISTED-RIDGE-L32-v1`, source `yspennstate/math-open-problems@b129377880c18fe011dd4513282f2e0b60e412e0`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T155815Z-qform-r11b/REPORT.md`. For

   `Q=a(Z+m(Y))^2+R(Y)`,

   `K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, `theta=tr K_gamma`, `D=det(I+BB^T/gamma^2)`,

   if `max_i(K_gamma)_ii<=q/2` and `theta>4q/3`, then

   `||p_Q||_inf <= 8*3^(-5/8)*sqrt(e)*q^(-1/4)*sqrt(3theta/(3theta-4q))*D^(-1/(4theta))/sqrt(|a|gamma)`.

## 3. The explicit near-coloop cross block

Fix an integer `m>=4`, parameters `0<eta<=1/4`, `0<epsilon<=1`, and define an `(2+2m) x 3` matrix `U=U_{m,eta}` by disjoint-support columns:

- row 1: `(sqrt(1-eta),0,0)`;
- row 2: `(sqrt(eta),0,0)`;
- rows `3,...,m+2`: `(0,1/sqrt(m),0)`;
- rows `m+3,...,2m+2`: `(0,0,1/sqrt(m))`.

Then `U^T U=I_3`.

Use the fixed orthogonal matrix

`V=[[-2/3,  2/15, 11/15],
    [ 2/3, -1/3,   2/3 ],
    [ 1/3, 14/15,  2/15]]`,

for which `V^T V=I_3`, `det V=1`, and every entry is nonzero. Set

`M_{epsilon,eta}=U diag(epsilon,2,2) V^T`.                       (3.1)

The singular values are exactly `(2,2,epsilon)`. Every physical cross entry is nonzero: rows 1 and 2 are nonzero multiples of the first row of `V^T`, the first `m` strong rows are nonzero multiples of the second row, and the last `m` rows are nonzero multiples of the third row.

A `3 x 3` physical minor is nonzero iff it chooses exactly one row from `{1,2}`, one row from the first strong group, and one row from the second strong group. Its squared determinant is

`16 epsilon^2 (1-eta)/m^2` if row 1 is chosen,

`16 epsilon^2 eta/m^2` if row 2 is chosen.                       (3.2)

There are `m^2` minors of each type, so

`E3=e3(M^T M)=16 epsilon^2`.                                     (3.3)

The squared-minor Gibbs law therefore factorizes exactly as

`Bernoulli(p=1-eta)` on the choice `{row1,row2}`

`x Uniform({1,...,m}) x Uniform({1,...,m})` on the two strong groups. (3.4)

Thus `eta -> 0` is a quantitative near-coloop: the volume law forces row 1 with probability `1-eta`, but unlike the exact-coloop endpoint there is still a nonzero family of bases excluding it.

## 4. Exact optimization of every admissible volume weight

Let `1<=q<3/2`. For a probability law `w` on the nonzero minors, let

`x=P_w(row 1 is selected)`.

Every basis selects exactly one of rows 1 and 2, so the two marginal constraints are

`x<=q/2`, `1-x<=q/2`, hence

`1-q/2 <= x <= q/2`.                                             (4.1)

Because `m>=4`, the uniform marginals `1/m` on each strong group are automatically at most `q/2`.

The e5 entropy identity gives

`log G(w)=log E3-KL(w||w_*)`,                                    (4.2)

where `w_*` is the factorized Gibbs law (3.4). By the KL chain rule, among all laws with a given binary marginal `x`, the unique KL minimizer keeps both strong-group choices independent and uniform. Therefore the full optimization reduces exactly to a one-dimensional Bernoulli projection:

`KL_min(q)=min_{x in [1-q/2,q/2]} D_Ber(x || 1-eta)`.            (4.3)

For `0<eta<=1/4`, one has `1-eta>=3/4>q/2`, so the minimizer is always the upper endpoint

`x_q=q/2`,                                                       (4.4)

and

`KL_min(q)=D_Ber(q/2 || 1-eta)`.                                (4.5)

Consequently the globally optimal admissible entropy-adjusted third volume is

`G_opt(q)=16 epsilon^2 exp[-D_Ber(q/2 || 1-eta)]`.               (4.6)

This is an exact optimization over **all** admissible weights, not only a symmetric ansatz.

### q=1 and direct application of e5 Theorem D

At `q=1`, the admissibility interval in (4.1) collapses to `x=1/2`. Hence

`D_Ber(1/2||1-eta)=-(1/2) log[4 eta(1-eta)]`,

`G_opt(1)=32 epsilon^2 sqrt(eta(1-eta))`.                        (4.7)

Applying the completed e5 arbitrary-weight Theorem D gives the actual inequality

`boxed: ||p_Q||_inf <= 6 sqrt(e) [32 epsilon^2 sqrt(eta(1-eta))]^(-1/6).`  (4.8)

The sharper weighted fractional theorem gives the same optimized weight with coefficient `3e` instead of `6sqrt(e)`.

## 5. The optimal Fourier exponent q is explicit

Define the sharp weighted-volume upper bound

`B_vol(q)=C(q) G_opt(q)^(-1/6)`,

`C(q)=3e/[(3-2q)sqrt(q)]`.                                      (5.1)

For `0<eta<=1/4`, differentiation gives

`d/dq log B_vol(q)
 = 2/(3-2q) - 1/(2q)
   + (1/12) log[ q eta / ((2-q)(1-eta)) ]`.                     (5.2)

A second derivative calculation is strictly positive:

`d^2/dq^2 log B_vol(q)
 = 4/(3-2q)^2 + 1/(2q^2) + (1/12)(1/q+1/(2-q)) >0`.            (5.3)

Hence there is at most one interior optimum. At the endpoint `q=1`,

`(d/dq log B_vol)(1)=3/2 + (1/12) log[eta/(1-eta)]`.            (5.4)

Define

`eta_c=1/(1+e^18)=1.522997951276... x 10^(-8)`.                  (5.5)

Then the globally optimal exponent is:

- if `eta>=eta_c`, `q_*=1`;
- if `0<eta<eta_c`, there is a unique `q_* in (1,3/2)` solving

  `2/(3-2q_*) - 1/(2q_*)
   + (1/12) log[ q_* eta / ((2-q_*)(1-eta)) ]=0`.               (5.6)

Examples: `q_*(10^-8)=1.00742214985346`; `q_*(10^-12)=1.13259839806934`.

Thus extremely near a coloop it is genuinely worthwhile to relax the marginal exponent above one, but the optimum is completely explicit and unique.

### Fundamental limitation of the entire optimized volume mechanism

Since `G_opt(q)<=E3=16 epsilon^2` and `C(q)>=C(1)=3e` for `q>=1`, every admissible weighted fractional-volume certificate obeys the lower limitation

`B_vol(q) >= 3e (16 epsilon^2)^(-1/6)
          = 3e 2^(-2/3) epsilon^(-1/3)`.                        (5.7)

Therefore even the **globally optimized** admissible volume weight and Fourier exponent necessarily pay the weak singular direction as `epsilon^{-1/3}`. No entropy tilt can regularize it away.

This is the main structural conclusion of the run.

## 6. The designated partner's optimized projection gate on the same matrix

Apply fleet03/B04 r23 to the same physical block. Take `P` to be the projection onto the two strong left singular directions. Then

`L=max_i P_ii=1/m`,                                              (6.1)

while the residual tail consists only of the weak singular direction, so

`T2=epsilon^2`, `||(I-P)M||op=epsilon`, and therefore `rho=1`.   (6.2)

The partner certificate has

`A(L,rho)=[sqrt(1/m)+sqrt(3)sqrt(1-1/m)]^2`.                    (6.3)

For every `m>=4`, already the second term squared is `3(1-1/m)>=9/4`, so

`A(L,rho)>3/4`.                                                   (6.4)

Hence the completed partner theorem correctly identifies this near-coloop family as lying **outside** its volume-stability exit despite small top-two leverage. The obstruction is not leverage; it is that the entire tail energy sits in one weak direction, giving `rho=1`.

This is an equation-level application of the latest designated partner result to a real obstruction.

## 7. Same physical matrix: ridge regularizes the weak direction uniformly

Add one untouched independent original coordinate `Z` and consider

`Q_{epsilon,eta}=Z^2 + 2 X^T M_{epsilon,eta} Y`.                 (7.1)

The full physical symmetric matrix is

`A=diag(1, [[0,M],[M^T,0]])`.                                   (7.2)

Its nonzero spectrum is

`{1, +2,+2,+epsilon, -2,-2,-epsilon}`.                          (7.3)

Thus for every `0<epsilon<=1` it is indefinite and has at least five eigenvalues of modulus at least one when `epsilon=1`, and at least the four values `±2,±2` plus the singleton `1` for every `epsilon<1`; in all cases the exact target hypothesis is satisfied. Because `V` has no zero entries, all physical `X-Y` cross coefficients are nonzero.

Use the square-assisted ridge theorem with the genuine original-coordinate square `a=1`, `q=1`, `gamma=1`. Put

`k1=epsilon^2/(1+epsilon^2)`, `k2=4/5`.                          (7.4)

Then

`K_gamma=U diag(k1,k2,k2) U^T`.                                 (7.5)

The row diagonals are

`(1-eta)k1`, `eta k1`, and `k2/m=4/(5m)` on every strong-group row. (7.6)

For `epsilon<=1` and `m>=4`,

`max_i(K_gamma)_ii <= 1/2`.                                     (7.7)

Also

`theta=tr K_gamma=k1+8/5 >=8/5>4/3`,                            (7.8)

`D=det(I+MM^T)=25(1+epsilon^2)`.                                (7.9)

Therefore

`||p_Q||_inf <= 8*3^(-5/8)*sqrt(e)
  *sqrt(3theta/(3theta-4))*D^(-1/(4theta)).`                    (7.10)

A completely elementary uniform bound follows from `theta>=8/5`, `theta<=21/10`, `D>=25`:

`sqrt(3theta/(3theta-4))<=sqrt(6)`,

`D^(-1/(4theta))<=25^(-5/42)`.

Hence for the entire family

`boxed: ||p_{Q_{epsilon,eta}}||_inf
 < 8*3^(-5/8)*sqrt(6e)*25^(-5/42)
 = 11.0838499893... .`                                         (7.11)

The exact formula (7.10) tends as `epsilon->0` to

`9.83295253074...`,                                              (7.12)

so the crude display (7.11) is not close to sharp but is rigorous and universal.

### Concrete numerical comparison

Take `m=8`, `eta=10^-4`, `epsilon=10^-6`. Since `eta>eta_c`, the globally optimal volume exponent is `q_*=1`.

The direct e5 optimized-weight bound (4.8) is

`||p_Q||_inf <= 1196.1265056...`.

The sharper weighted fractional coefficient gives

`||p_Q||_inf <= 986.0396061...`.

The rigorous ridge display gives

`||p_Q||_inf < 11.0838499893`,

while the exact ridge formula evaluates to

`9.83295253073...`.

Thus on one explicit target-valid rotated indefinite matrix, full admissible-volume optimization is roughly two orders of magnitude weaker because it must pay the weak third singular direction, whereas ridge regularizes that direction before inversion.

## 8. What changed in the proof map

The exact-coloop endpoint said finite-KL admissible volume can fail completely. The present theorem shows that even after moving off that endpoint so the admissible polytope is nonempty and the **global** KL/Fourier optimization can be solved exactly, the volume route still cannot imitate ridge regularization: it pays `epsilon^{-1/3}`.

Therefore the first unpaid implication sharpens to:

`QFORM-NEAR-COLOOP-STRUCTURAL-ROUTING-v2` — from the bare three-large-eigenvalue hypothesis, show that any physical cut whose optimized third-volume certificate is forced to pay a near-coloop weak direction either admits a genuine square-assisted ridge certificate at a universal scale, or has enough hub/grouped low-rank structure to enter an already completed endpoint. A proof cannot rely on entropy reweighting alone, because the family above exhaustively optimizes that mechanism and still diverges.

This is a structural routing problem, not an analytic defect in the completed weighted-volume Fourier theorem.

## 9. Review status

The e5 arbitrary-weight step and fleet03/B04 r23 projection/tail chain are used only at their stated scopes. The new near-coloop optimization is a fresh supporting argument from this run and has not yet received an independent review. Full QFORM remains OPEN.
