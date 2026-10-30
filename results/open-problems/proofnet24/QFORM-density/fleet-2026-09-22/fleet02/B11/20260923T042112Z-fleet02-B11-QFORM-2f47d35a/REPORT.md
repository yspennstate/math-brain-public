SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B11, 2026-09-23T04:21:12Z.
attacking: the remaining opposite-sign two-sheet branch when a good indefinite pair survives but the third square direction is diffuse across a disjoint original-coordinate bank.

# fleet02/B11 — banked square consumes the rank-two logarithm before local determinant payment

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T042112Z-fleet02-B11-QFORM-2f47d35a`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / SOURCE-VALID PROOF-INTERFACE COUNTEREXAMPLE / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** only essential boundedness is asserted for the new theorem.

## 1. First unpaid implication and source boundary

The full owner target remains open: arbitrary independent real coordinates with densities bounded by one, arbitrary symmetric ambient matrix with at least three eigenvalues of modulus at least one, no moments/support/log-concavity/diagonal-basis/post-rotation-independence assumptions.

The first B11 debt after the preceding minority-Schur run is the near-null one-sign physical-diagonal chamber. The present run changes mechanism: instead of choosing a small physical scalar pivot and paying its reciprocal determinant, it asks whether a **whole third spectral direction can be aggregated as an independent square bank before inversion**. This is only a subclass of the full no-pivot problem, but it is a genuine near-null interpolation and it identifies a local-selection obstruction sharply.

Three completed sources are used at equations below.

1. Required Claude package: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem C. For an exact-rank-three `(2,1)` form whose three nonzero eigenvalue magnitudes are at least one, it gives the ruled one-sheet estimate `p_Q(t)<=pi sqrt(2)` on the majority-sign side `t>=0`.
2. Designated partner fleet03/B11 r24: `yspennstate/math-open-problems@31b72d5e536a81344c1242b9c0356e488310f81e`, especially `ADDENDUM_SIGNED_HALF_RIESZ.md`. Equation (A.1), sourced there from the completed rank-two fusion theorem, states for two independent cap-one original coordinates and any invertible symmetric `2x2` matrix `B`, with arbitrary affine term,

   `sup_s E |U^T B U+ell^T U-s|^(-1/2) <=16 sqrt(30)|det B|^(-1/4)`.       (1.1)

3. The sharp product-marginal input of Livshyts--Paouris--Pivovarov, source-pinned in `math-open-problems@1809b7ee5deef19744f1c36bbdd445b9b1992997`, fleet03/B18: if `b` is a unit coefficient vector and the coordinates are independent with density caps one, then `W=sum b_jX_j` has density cap at most `sqrt(2)`.

No result below treats a small matrix coefficient as a small random perturbation. No rotated variables are declared independent.

## 2. The banked-square half-Riesz theorem

### Theorem 2.1 — `QFORM-INDEFINITE-PAIR-DIFFUSE-SQUARE-v1`

Let `U=(X_1,X_2)` consist of two independent real random variables with densities at most one. Let

`P=U^T B U+ell^T U+c`,                                             (2.1)

where `B` is any invertible real symmetric `2x2` matrix. Let `W` be independent of `U`, with probability density satisfying

`||p_W||_infinity <=L`.                                            (2.2)

For `d!=0` and arbitrary `r,q in R`, put

`Q=P+dW^2+2rW+q`.                                                  (2.3)

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(30) L |det B|^(-1/4)|d|^(-1/2).`                       (2.4)

In particular, if `W=sum_{j in J} b_jX_j` is a normalized linear form (`sum b_j^2=1`) on an original-coordinate bank disjoint from `{1,2}`, then

`boxed:
 ||p_Q||_infinity
 <=16 sqrt(60)|det B|^(-1/4)|d|^(-1/2).`                          (2.5)

The theorem is especially useful when `B` is indefinite. It does **not** require the rank-two quadratic output `P` itself to have a bounded density.

### Proof

Complete the square in the bank variable:

`dW^2+2rW=d(W+r/d)^2-r^2/d`.                                      (2.6)

Translation preserves the density cap `L`, so write `V=W+r/d`. For `d>0`, the density of `dV^2` at `y>0` is

`[p_V(sqrt(y/d))+p_V(-sqrt(y/d))]/[2 sqrt(dy)]
 <=L/[sqrt(d)y^(1/2)]`.                                           (2.7)

For `d<0` the same estimate holds on the opposite half-line. Therefore, after conditioning on `P`, for almost every target `t`,

`p_Q(t)
 <=L |d|^(-1/2)
   E[(sign(d)(t'-P))_+^(-1/2)]
 <=L |d|^(-1/2) sup_s E|P-s|^(-1/2),`                            (2.8)

where `t'` is `t` shifted by the harmless constants. Apply the designated-partner half-Riesz inequality (1.1) to obtain (2.4).

If `W` is the normalized disjoint product projection in the second statement, the sharp one-dimensional product-marginal theorem gives `L<=sqrt(2)`. Substitution in (2.4) gives (2.5). QED.

The proof uses the third direction at exactly the right regularity. The square kernel is a one-sided `1/2`-Riesz kernel; therefore it asks only for the half-order potential (1.1) of the rank-two receiver, not an `L^infinity` density bound for that receiver.

## 3. Rank-two logarithmic singularity is retained, not hidden

Take the endpoint

`B_0=[[0,1],[1,0]]`,                                               (3.1)

and independent `X_1,X_2~Uniform[-1/2,1/2]`. Then

`P=2X_1X_2`                                                       (3.2)

has, for `0<|t|<1/2`,

`p_P(t)=log(1/(2|t|))`.                                           (3.3)

Thus the opposite-sign rank-two form really has the logarithmic density divergence. Theorem 2.1 does not contradict or bypass it. Adding the genuinely independent square bank convolves this logarithmic receiver with the one-sided square kernel, and the completed half-Riesz estimate says precisely that this convolution is bounded.

This is the sign-specific third-direction mechanism requested by B11: the third direction removes the rank-two logarithm by consuming its finite half-order potential. It does not turn the rank-two density itself into a bounded function.

## 4. Exact target-valid near-null/diffuse-third family

For `m>=1` and `epsilon>=0`, define

`B_epsilon = [[epsilon, sqrt(1+epsilon^2)],
              [sqrt(1+epsilon^2), -epsilon]]`,                    (4.1)

and on a disjoint bank of `m` original coordinates put

`b_m=m^(-1/2)(1,...,1)`, `W_m=<b_m,X_bank>`.                      (4.2)

Let

`A_{m,epsilon}=B_epsilon direct_sum (b_m b_m^T)`.                  (4.3)

Then

`det B_epsilon=-(1+2epsilon^2)`,                                  (4.4)

and the exact nonzero spectrum of `A_{m,epsilon}` is

`{-sqrt(1+2epsilon^2), 1, sqrt(1+2epsilon^2)}`.                   (4.5)

Hence every `A_{m,epsilon}` is inside the owner's exact target: signature `(2,1)` and three eigenvalue magnitudes at least one. It is non-diagonal in the first two independent coordinates, while the positive third eigendirection is spread over all `m` bank coordinates.

Theorem 2.1 gives, uniformly in `m` and all `epsilon>=0`,

`||p_{X^T A_{m,epsilon}X}||_infinity
 <=16 sqrt(60)(1+2epsilon^2)^(-1/4)
 <=16 sqrt(60)
 =123.9354670786... .`                                            (4.6)

Most importantly, (4.6) is continuous through the exact-null limit `epsilon->0`: no inverse power of `epsilon` appears. This is a nonperturbative near-null interpolation for this whole separable-bank chamber.

### Required Claude theorem applied to an actual inequality

The same family lets us use the required `e5f71d...` result at its exact scope rather than as a bibliography citation. Its positive eigenvalues are `sqrt(1+2epsilon^2)` and `1`, and its negative magnitude is `sqrt(1+2epsilon^2)`. Therefore Claude's proved ruled Theorem C gives the **much sharper sign-specific one-sheet inequality**

`boxed:
 p_{A_{m,epsilon}}(t) <=pi sqrt(2)
 for every t>=0.`                                                  (4.7)

Consequently, in an end-to-end signature splice the new half-Riesz theorem is needed only for the opposite two-sheet side `t<0` (although (4.6) itself holds for all `t`). Negating the form gives the reflected `(1,2)` statement.

This makes the geometric division exact: one sheet is paid by real rulings and two-dimensional product marginals; the other sheet is paid here by the rank-two half-Riesz receiver plus an independent square bank.

## 5. Counterexample to selecting one third physical coordinate before smoothing

The family (4.3) is also a source-valid counterexample to a tempting proof mechanism. Every invertible physical `3x3` principal block must contain the two pair coordinates and exactly one bank coordinate `k`. Such a block is

`H_k=B_epsilon direct_sum [1/m]`,                                 (5.1)

so

`det H_k=-(1+2epsilon^2)/m`.                                      (5.2)

Every other physical principal triple is singular because the bank block has rank one and there are no pair-bank cross terms.

Now apply the completed fleet03/B11 r24 scalar compilers **at their stated inequalities**.

For fixed `epsilon>0`, the diagonal `-epsilon` is the visible minority sign. The partner minority theorem therefore gives at best

`||p_Q||_infinity
 <=2 sqrt(pi)[epsilon(1+2epsilon^2)/m]^(-1/4)
 =Theta(m^(1/4)).`                                                 (5.3)

Using the bank pivot `1/m` in the partner all-nonzero-pivot theorem is worse:

`||p_Q||_infinity
 <=16 sqrt(30)[(1+2epsilon^2)/m^2]^(-1/4)
 =Theta(m^(1/2)).`                                                 (5.4)

At the exact endpoint `epsilon=0`, the partner affine zero-pivot theorem on `H_k` gives

`||p_Q||_infinity
 <=3*2^(2/3)[m/(1+2epsilon^2)]^(1/3)
 =Theta(m^(1/3)).`                                                 (5.5)

Thus **every available one-third-coordinate scalar compiler diverges with the bank size**, while the aggregate-before-inversion estimate (4.6) stays bounded. This does not refute any partner theorem and is not a QFORM counterexample. It refutes only the structural strategy

> find the good opposite-sign pair, select one physical coordinate carrying the third direction, then pay a local reciprocal determinant/pivot.

The third direction must be allowed to aggregate across the whole independent bank before the square kernel is paid.

## 6. Why this is genuinely a near-null improvement

For every fixed `m`, the local partner bound (5.3) deteriorates as `epsilon^(-1/4)` when `epsilon->0+`, and at `epsilon=0` one must switch discontinuously to the null-pivot mechanism (5.5). By contrast, the banked bound (4.6) is uniform and continuous across `epsilon=0`, because its currency is the determinant of the **whole indefinite pair**,

`|det B_epsilon|=1+2epsilon^2>=1`,                                (6.1)

not the size of either physical diagonal.

This is exactly the sort of aggregation the live `QFORM-NEAR-ZERO-HALF-RIESZ-ONLY-FALSE-v1` correction allows: we do not retain merely a cross-row norm while discarding self curvature. We retain the entire invertible pair matrix `B_epsilon`, apply its proved half-Riesz estimate, and only then smooth with a genuinely independent third bank.

## 7. Exact regression check

`VERIFY.py` and `VERIFY_OUTPUT.txt` in this run directory check the algebra for `m=64` and `epsilon in {0,0.01,0.1,0.5}`. They verify the exact three-eigenvalue spectrum numerically, that the only nonsingular physical triples are (5.1), and the determinant formula (5.2). The captured run ends

`QFORM_BANKED_PAIR_SQUARE_INTERPOLATION_CHECK_PASS`.

The check is regression evidence only, not a finite-dimensional proof substitute.

## 8. What remains unpaid

The theorem closes a real opposite-sign branch, but the full conjecture remains open. The surviving B11 implication is now more precise:

**`QFORM-OVERLAPPING-THIRD-DIRECTION-HALF-RIESZ-v1`.** In the no-pivot/high-leverage chamber, the third spectral direction need not live on a coordinate bank disjoint from the two coordinates generating the indefinite pair. Prove a dimension-free replacement for Theorem 2.1 when the square direction overlaps those original coordinates, while retaining the exact product provenance; or force a ruled/volume/physical-pair exit. One may not simply rotate to make the pair and square independent, and small overlap coefficients cannot be deleted perturbatively on arbitrary unbounded supports.

This is strictly narrower than the prior generic near-null statement: the disjoint-bank interpolation, including all nonzero near-null pair diagonals, is now paid uniformly. Arbitrary extra nonseparable spectrum remains a separate full-QFORM interface.

Independent-review status: not independently reviewed in this run. Full QFORM remains OPEN.
