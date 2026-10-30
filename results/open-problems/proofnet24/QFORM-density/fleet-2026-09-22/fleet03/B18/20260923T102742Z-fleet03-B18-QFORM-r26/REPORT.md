# fleet03/B18 r26 — rank-two cross-block half-Riesz transfer and nested Schur-pivot compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** literature-to-proof transfer  
**Status:** `NEW SUPPORTING ANALYTIC THEOREM + PARTNER COMPILED BRANCH / FULL QFORM OPEN`  
**Continuity:** not claimed for the new scalar-pivot wrappers; absolute continuity and essential boundedness are proved.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and live corrections respected

The target is: for every `n`, every family of independent real `X_i` whose probability densities satisfy `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with universal `L^infinity` bound, or produce a valid counterexample. No Gaussian, log-concavity, moment, bounded-support, connected-support, or diagonal-coordinate hypothesis is added here.

This run uses independence only between **disjoint sets of original coordinates**. It does not use post-rotation independence. It does not use the false law-uniform pointwise scalar Fresnel estimate, arbitrary-joint quadratic coarea, fixed-good-minor extraction, a positive moment of a conditional projection-density cap, or the replacement of a small nonzero self-curvature by zero.

The mechanism is a weighted-frequency estimate at the rank-two cross-block endpoint. The ordinary time integral is logarithmically divergent there; multiplying by the half-Riesz Fourier weight makes it integrable. That is precisely the borderline left open by the prior rank-`>=3` cross-block density theorem.

## 2. Primary source transferred exactly

The source theorem actually used is Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949. Their theorem states that if

`f(x)=prod_i f_i(x_i)` with every `f_i` a one-dimensional probability density bounded by one, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`.

For `k=2`, every two-dimensional orthogonal projection of one original product block therefore has density cap `2`. No moment, centering, iid, Gaussian, log-concavity, smoothness, or support assumption is present in the transferred hypothesis.

A focused comparison with Banks--Garza Vargas--Kulkarni--Srivastava, arXiv:2005.08930, does **not** justify simply adding arbitrary same-side curvature to their bilinear-plus-affine estimates. The theorem below keeps arbitrary same-side terms by treating them as conditional modulus-one amplitudes before Plancherel. I make no search-miss novelty claim.

## 3. New theorem: arbitrary same-side curvature at cross rank two

### Theorem 3.1 — `QFORM-CROSSBLOCK-RANK2-HALFRIESZ-v1`

Let `I,J` be disjoint sets of original independent cap-one coordinates. Write

`X=(X_i)_{i in I}`, `Y=(X_j)_{j in J}`.

Let `F` and `G` be arbitrary real measurable functions of their indicated blocks and let `B` be a real `|I| x |J|` matrix of rank exactly two, with nonzero singular values

`sigma_1 >= sigma_2 > 0`.

Put

`R = F(X)+G(Y)+2 X^T B Y`,

and `Delta=sigma_1 sigma_2`. Then, for every `u in R`,

`boxed( E |R-u|^(-1/2) <= 8 Delta^(-1/4). )`  (3.1)

Equivalently, the half-Riesz potential of the law of `R` is uniformly bounded. No density assertion for `R` itself is made.

This applies in particular when `F=X^T A_II X + ell_I^T X+c_I` and `G=Y^T A_JJ Y+ell_J^T Y+c_J`, with completely arbitrary symmetric same-side blocks.

### Proof

Take a thin singular-value decomposition

`B=P Sigma T^T`, `Sigma=diag(sigma_1,sigma_2)`,

where the columns of `P` and `T` are orthonormal in their respective original-coordinate spaces. Define

`U=P^T X`, `V=T^T Y`.

The blocks `X` and `Y` are genuinely independent because `I` and `J` are disjoint original-coordinate sets, hence `U` and `V` are independent. By the LPP theorem,

`||p_U||_infinity <=2`, `||p_V||_infinity <=2`.  (3.2)

For each real frequency `t`, disintegrate within the original blocks and define

`a_t(u)=p_U(u) E[ exp(i t F(X)) | U=u ]`,

`b_t(v)=p_V(v) E[ exp(i t G(Y)) | V=v ]`.

The same-side terms are retained exactly and only enter through modulus-one conditional factors. Therefore

`|a_t(u)|<=p_U(u)`, `|b_t(v)|<=p_V(v)`,

and because each marginal has mass one,

`||a_t||_2 <= sqrt(2)`, `||b_t||_2 <= sqrt(2)`.  (3.3)

The characteristic function is

`phi_R(t)=int int exp(2 i t u^T Sigma v) a_t(u)b_t(v) du dv`.

Use the Fourier convention

`hat h(xi)=int exp(i xi.v) h(v) dv`,

for which Plancherel reads `||hat h||_2=(2pi)^(1/2)||h||_2` in two dimensions with the corresponding factor `(2pi)^(2/2)=2pi` under squared norms. Cauchy--Schwarz, the change of variables `xi=2t Sigma u`, and Plancherel give for `t!=0`

`|phi_R(t)|
 <= ||a_t||_2 (2|t|)^(-1) Delta^(-1/2) ||hat b_t||_2
 = pi |t|^(-1) Delta^(-1/2) ||a_t||_2||b_t||_2
 <= 2pi |t|^(-1) Delta^(-1/2).`  (3.4)

Together with `|phi_R(t)|<=1`, set

`K=2pi Delta^(-1/2)`

and obtain

`|phi_R(t)| <= min(1,K/|t|).`  (3.5)

The ordinary `L^1(dt)` integral is logarithmically divergent, so (3.5) alone does **not** prove a bounded density for `R`. This is exactly the rank-two endpoint. The half-Riesz weight is different:

`int_R |t|^(-1/2)|phi_R(t)| dt
 <= 2[ int_0^K t^(-1/2)dt + K int_K^infinity t^(-3/2)dt ]
 =8 sqrt(K).`  (3.6)

The classical one-dimensional Riesz identity, with the same Fourier convention, is

`widehat{|x|^(-1/2)}(t)=sqrt(2pi)|t|^(-1/2).`  (3.7)

To avoid any pointwise subtlety at the singular kernel, let `Z` be an independent standard Gaussian and put `R_epsilon=R+epsilon Z`. Its characteristic function is `phi_R(t) exp(-epsilon^2 t^2/2)`, so the weighted integral in (3.6) remains absolutely integrable with the same bound. Standard Fourier inversion for the Riesz potential gives, for every `u`,

`E|R_epsilon-u|^(-1/2)
 <= (1/sqrt(2pi)) int_R |t|^(-1/2)|phi_R(t)|dt
 <= 8 sqrt(K)/sqrt(2pi)
 =8 Delta^(-1/4).`  (3.8)

As `epsilon downarrow 0`, `R_epsilon` converges in distribution to `R`. The extended function `x -> |x-u|^(-1/2)` is nonnegative and lower semicontinuous. Portmanteau therefore gives

`E|R-u|^(-1/2) <= liminf_{epsilon downarrow0} E|R_epsilon-u|^(-1/2)`,

which proves (3.1) for every `u`. QED.

### Relation to existing results

This is not the existing orientation-free global-rank-two affine half-Riesz theorem. That theorem handles a quadratic whose **entire quadratic matrix has rank two**, with arbitrary affine perturbation. Here the same-side functions `F` and `G` can have arbitrarily high quadratic rank (or can be arbitrary measurable functions), while only the physical cross block is required to have rank two. The payment is the product of the two nonzero cross singular values.

It is also the exact endpoint companion to fleet03/B18 r19: cross rank `>=3` gave an ordinary `L^1` characteristic-function integral and a continuous bounded density, whereas cross rank two gives a half-Riesz potential and no bounded-density conclusion for the bicore alone.

## 4. First concrete implication: one physical Schur pivot closes rank-two cross residuals

### Theorem 4.1 — `QFORM-RANK2-CROSS-SCALAR-PIVOT-v1`

Let one original coordinate `Z` have nonzero physical pivot `a`. After completing that scalar square, suppose the Schur residual on all remaining original coordinates can be partitioned into disjoint original-coordinate blocks `I,J` whose cross block has rank two and nonzero singular values `sigma_1,sigma_2`. The same-side Schur blocks are arbitrary.

Then the full quadratic form has an absolutely continuous law and

`boxed( ||p_Q||_infinity <= 8 |a|^(-1/2)(sigma_1 sigma_2)^(-1/4). )`  (4.1)

No continuity conclusion is asserted.

### Proof

After completing the physical scalar square,

`Q=a(Z+h(Y))^2+R(Y)`,  (4.2)

where `Y` denotes all other original coordinates, `h` is linear, and the quadratic part of `R` is exactly the Schur complement. Under the assumed partition, `R` has the form of Theorem 3.1 with arbitrary same-side curvature.

Condition on `Y=y`. Since `Z` is an original coordinate independent of `Y` and has density at most one, the shifted variable `Z+h(y)` still has density at most one. For `a>0`, the conditional density of `a(Z+h(y))^2` at `s>0` is

`[f_Z(-h(y)+sqrt(s/a))+f_Z(-h(y)-sqrt(s/a))]/[2 sqrt(a s)]
 <= 1/sqrt(a s).`  (4.3)

For `a<0`, reflect the output. Hence the mixture density of `Q` satisfies for almost every `q`

`p_Q(q) <= |a|^(-1/2) E |q-R(Y)|^(-1/2).`  (4.4)

Theorem 3.1 gives (4.1). Formula (4.4) also constructs an `L^infinity` density, proving absolute continuity. QED.

The random shift `h(Y)` can be fully dependent on the Schur residual. No post-completion independence is used.

## 5. Required fleet04/B18 partner application: a nested two-pivot compiler

Use the completed fleet04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, scientific commit

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

It proves: if a base variable `S` has density cap `M`, and conditional on `S=s` a square variable `V_s` has density cap one, then for `b!=0`,

`||p_{S+bV_S^2}||_infinity <= 2 sqrt(M/|b|)`,  (5.1)

without requiring independence between `S` and the translated square variable.

Now take a quadratic form admitting two successive physical Schur pivots. Complete the **outer** pivot `b!=0`; in its Schur complement complete a second physical pivot `a!=0`; suppose the second Schur residual has a physical original-coordinate bipartition with rank-two cross block and singular-value product `Delta`.

Theorem 4.1 applied to the inner pivot gives a base-density cap

`M <= 8 |a|^(-1/2) Delta^(-1/4).`  (5.2)

For the outer pivot, the translated original coordinate has conditional density cap one given the entire inner base: it is a mixture of translations of its original cap-one density. Applying the fleet04/B18 theorem literally to (5.2) yields

`boxed(
 ||p_Q||_infinity
 <= 4 sqrt(2) |b|^(-1/2)|a|^(-1/4) Delta^(-1/8).
)`  (5.3)

This is an actual partner-result splice, not a citation-only comparison. It permits all dependence introduced by both square completions and arbitrary same-side curvature in the terminal rank-two cross residual.

I record essential boundedness and absolute continuity for (5.3), not continuity, because the partner theorem proves absolute continuity/L-infinity but does not supply a continuity conclusion in this dependent-square setting.

## 6. Exact target-valid test with exactly three large eigenvalues

Take independent cap-one variables `(W,Z,X1,Y1,X2,Y2)` and

`Q=(W+Z)^2 +(1/4) Z^2 +2 X1 Y1 +(1/2) X2 Y2.`  (6.1)

The physical matrix is block diagonal between

`[[1,1],[1,5/4]]`, `[[0,1],[1,0]]`, and `[[0,1/4],[1/4,0]]`.

Its eigenvalues are

`(9+sqrt(65))/8`, `(9-sqrt(65))/8`, `1`, `-1`, `1/4`, `-1/4`.

Numerically these are approximately

`2.13278221846, 0.117217781463, 1, -1, 0.25, -0.25`.

Thus **exactly three** eigenvalues have modulus at least one.

After completing the outer `W` square, the inner pivot is `a=1/4`; after completing it, the terminal cross block is

`B=diag(1,1/4)`, so `Delta=1/4`. Theorem 4.1 alone gives the base cap

`M <= 8 (1/4)^(-1/2)(1/4)^(-1/4)=16 sqrt(2).`

Applying the fleet04/B18 dependent-square smoother to the outer pivot `b=1` gives

`boxed(
 ||p_Q||_infinity <=2 sqrt(16 sqrt(2))
 =8*2^(1/4)
 =9.513656920021768... .
)`  (6.2)

This is a genuinely coupled target example: the outer square is `(W+Z)^2`, so the partner dependence-safe interface is actually used. The direct one-pivot bound at the outer level would be `8 sqrt(2)`, so the nested partner compilation also improves the constant in this example.

## 7. Literature/hypothesis audit

### LPP — applied

The LPP theorem matches exactly because `U=P^T X` and `V=T^T Y` are orthogonal projections **inside two disjoint original-coordinate product blocks**. It supplies `||p_U||_infinity,||p_V||_infinity<=2` in dimension two. It does not assert that arbitrary eigen-coordinates of the full form are independent, and no such assertion is made here.

### Banks--Garza Vargas--Kulkarni--Srivastava — not broadened

Their bilinear anti-concentration estimates are useful when the expression remains bilinear-plus-affine in independent arrays. The present theorem permits `F(X)` and `G(Y)` to be arbitrary same-side terms. Those terms are paid through conditional complex amplitudes and Plancherel, not by silently inserting them into a theorem whose displayed polynomial class omits them.

### Current rank-two affine half-Riesz theorem — complementary, not duplicated

The current fleet theorem with constant `128` is orientation-free for a globally rank-two quadratic plus arbitrary affine term. The new theorem pays a physical rank-two **cross block** and consequently permits unrestricted same-side curvature of any rank. Neither theorem subsumes the other in its stated hypotheses.

### No exact prior full solution identified

The primary sources checked in this run do not state the owner's unrestricted theorem under only independent cap-one coordinates and three large eigenvalues. The full conjecture remains open in the repository state, and this run does not claim novelty for the supporting theorem beyond recording the proved implication.

## 8. What this changes and what remains open

The rank-two physical cross-block endpoint is now analytically paid whenever one nonzero physical scalar pivot is available, with the explicit scale

`8 |a|^(-1/2) Delta^(-1/4)`.

With two successive pivots, the completed fleet04/B18 dependent-square theorem gives the further compiler (5.3). This removes the need for an ordinary `L^1` characteristic-function estimate at cross rank two in those pivoted branches.

The remaining global debt is structural. From the bare hypothesis `s_3(A)>=1`, one still must route every matrix to one of the paid mechanisms with quantitative parameters bounded away from zero: scalar-pivot/rank-two-cross as above, rank-`>=3` cross volume, grouped zero-pivot, ridge/diffuse frame, physical pair, diagonal, or another completed branch. The live correction families show that one cannot simply select a uniformly good fixed physical triple/minor or declare a rotated spectral basis independent.

**Full QFORM remains OPEN / NOT PROVED. Unrestricted continuity remains OPEN.**

## 9. Deterministic checks

The sibling `CHECK.json` records:

1. the exact rank-two characteristic-function constant `K=2pi Delta^(-1/2)`;
2. the weighted integral identity giving the constant `8 Delta^(-1/4)`;
3. the partner-splice algebra `2 sqrt(8 |a|^(-1/2)Delta^(-1/4)/|b|)=4sqrt(2)|b|^(-1/2)|a|^(-1/4)Delta^(-1/8)`;
4. the exact spectrum of (6.1) and the count of exactly three eigenvalues of modulus at least one;
5. the numerical target-example bound `8*2^(1/4)=9.513656920021768...`.

No Monte Carlo evidence is used.
