SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-24T03:11:45Z.
attacking: the latest account03/B18 Lorentz endpoint; lift its private scalar square to a genuinely delocalized independent product bank, then splice it with the earlier capped-scalar/dependent-pair receiver on an exact rank-three target family.

# account02/B18 auto11 — conditional weak-L2 private-bank endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: literature-to-proof transfer  
Status: **NEW SUPPORTING THEOREM / EXACT TARGET FAMILY PAID / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

## 1. First unpaid implication

The live global debt is still structural. In an original-coordinate retained block, extract at target scale a cross bank and a rank-one square direction with a nontrivial genuinely private product-bank component, while retaining arbitrary curvature on the opposite bank and aligned coupling of that square direction back into it; or route failure into an already-paid physical-pair, grouped-hub, ridge, product-Fourier, or dependent-pair branch.

This report proves the analytic payoff for that extracted configuration. It does **not** prove that bare `s_3(A)>=1` always forces such a configuration.

## 2. Latest designated partner consumed

The latest compatible account03/B18 report is

- commit `3d3c43d327b37347cc67c937d4daae8d28bf433f`;
- result `QFORM-CROSS-SQUARE-LORENTZ-ENDPOINT-v1`.

For disjoint original-coordinate cap-one product banks `X,Y`, one further independent original coordinate `W`, `M!=0`, `sigma=||M||op`, arbitrary `alpha`, arbitrary measurable `G(Y)`, and constants `a!=0,d,c`, it proves

`T=X^T M Y+alpha^T X+G(Y)+aW^2+dW+c`

has a continuous `C_0` density and

`||p_T||_infinity <= 16/sqrt(|a| sigma)`.

Its proof first derives an endpoint `L^{2,1}` bound for the cross-bank density and then convolves with the weak-`L^2` scalar-square density. The present report uses the same source-matched linear-form input but changes the order: condition on the shared bank, convolve conditionally, and integrate a negative half-moment. This both improves the constant on the scalar special case and permits a `Y`-dependent square shift.

## 3. Primary source actually needed

Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492, Theorem 1.2:

If `X_1,...,X_n` are independent real random variables whose densities are bounded by `K`, and `sum a_j^2=1`, then the density of `sum a_j X_j` is bounded by `sqrt(2) K` a.e. The theorem assumes no moments, bounded support, log-concavity, iid structure, centering, symmetry, or smoothness.

Consequently, for any nonzero coefficient vector `v` and cap-one original product bank,

`||p_{v^T X}||_infinity <= sqrt(2)/||v||_2`.                       (3.1)

For the dependent-pair splice below we also use Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1: a genuine product density with one-dimensional factors bounded by one has every `k`-dimensional orthogonal marginal bounded by `2^(k/2)`. In particular, a two-dimensional orthogonal projection has joint density cap at most `2`. This is a joint-density statement, not projected-coordinate independence.

## 4. New theorem: conditional weak-L2 cross/private-bank endpoint

### Theorem 4.1 — `QFORM-CONDITIONAL-CROSS-PRIVATEBANK-WEAKL2-v1`

Let `X in R^m`, `Y in R^n`, and `Z in R^k` be three disjoint ORIGINAL-coordinate banks. Assume every coordinate has a probability density bounded by one and all coordinates are mutually independent. Let

- `M` be a nonzero `m x n` real matrix, `sigma=||M||op`;
- `alpha in R^m`;
- `gamma in R^k\{0}` and `U=gamma^T Z`;
- `a!=0`;
- `G,r : R^n -> R` arbitrary measurable functions;
- `c in R`.

Put

`T = X^T M Y + alpha^T X + G(Y) + a U^2 + r(Y) U + c`.             (4.1)

Then `T` has an essentially bounded density and

`boxed: ||p_T||_infinity <= 8 sqrt(2)/( ||gamma||_2 sqrt(|a| sigma) ).`  (4.2)

No continuity claim is made in this general `r(Y)`-dependent form.

### Proof

By Rudelson--Vershynin (3.1), `U` has a density cap

`L <= sqrt(2)/||gamma||_2`.                                         (4.3)

Condition on the genuine original-coordinate bank `Y=y`. Set

`c_y=My+alpha`, `K_y=sqrt(2)/||c_y||_2`.

Outside a null set, `c_y!=0`, and the conditional linear form `c_y^T X` has density cap at most `K_y` by (3.1).

Complete the square in `U`:

`aU^2+r(y)U = a(U+r(y)/(2a))^2-r(y)^2/(4a)`.                        (4.4)

Translation preserves the cap `L`. If `g_y` is the density of the quadratic variable in (4.4), then, after reflecting the output when `a<0`, the elementary two-root formula gives

`g_y^*(t) <= L/(sqrt(|a| t)),   t>0`,                               (4.5)

where `*` is decreasing rearrangement. Indeed `g_y(s)<=L/(sqrt(|a|s))` for `s>0`, so `|{g_y>lambda}|<=L^2/(|a|lambda^2)`.

For any probability density `f` with `||f||infinity<=K`, the bathtub principle gives

`int_0^infinity t^(-1/2) f^*(t) dt <= 2 sqrt(K)`.                    (4.6)

Conditional on `Y=y`, the variables `c_y^T X` and `U` are genuinely independent because they use disjoint original source banks. Hardy--Littlewood rearrangement, (4.5), and (4.6) therefore yield

`||p_{T|Y=y}||infinity <= 2 L |a|^(-1/2) K_y^(1/2)`.                (4.7)

Choose top left/right singular vectors `u,v` of `M`, so `u^T M=sigma v^T`. Put

`Z_0 = sigma v^T Y + u^T alpha`.                                    (4.8)

Then `||c_Y||_2>=|Z_0|`. Again by (3.1), `Z_0` has density cap

`H <= sqrt(2)/sigma`.                                                (4.9)

For a scalar probability density capped by `H`, another bathtub computation gives

`E |Z_0|^(-1/2) <= 2 sqrt(2) sqrt(H) <= 2^(7/4) sigma^(-1/2)`.       (4.10)

Hence

`E K_Y^(1/2)
 <= 2^(1/4) E|Z_0|^(-1/2)
 <= 4 sigma^(-1/2)`.                                                (4.11)

Averaging (4.7) over `Y` gives

`||p_T||infinity <= 8 L / sqrt(|a| sigma)
                 <= 8 sqrt(2)/(||gamma||_2 sqrt(|a| sigma))`,

which proves (4.2). The exceptional event `c_Y=0` is null because it implies `Z_0=0` and `Z_0` has a density. QED.

### Physical-block corollary

Write the quadratic cross term as `2 X^T B Y`, so `M=2B` and `tau=||B||op`. Let the private rank-one square block have nonzero absolute eigenvalue

`lambda = |a| ||gamma||_2^2`.

Then (4.2) becomes the clean physical-currency bound

`boxed: ||p_T||infinity <= 8/sqrt(tau lambda).`                      (4.12)

The theorem retains arbitrary `Y-Y` curvature through `G(Y)` and arbitrary aligned `Y-Z` coupling through `r(Y)U`. It does not allow an `X-X` quadratic block, an `X-Z` coupling, or an unaligned `Z`-linear/quadratic residual. Those are structural, not analytic, debts.

For one original scalar `W` (`gamma=e_1`, so its actual density cap is `L<=1`), the same proof sharpens the designated partner's constant to

`||p_T||infinity <= 8/sqrt(|a|sigma)`                               (4.13)

and still permits a measurable `Y`-dependent linear coefficient `r(Y)W`. This is an independent new derivation; no claim is made that the partner proof itself contained this stronger conditional estimate.

## 5. Exact-rank-three dependent-bank family and splice

Take eight arbitrary independent cap-one original variables and define

`S  =(X1+X2)/sqrt(2)`,
`C  =(X3+X4+X5+X6)/2`,
`D0 =(X3-X4+X5-X6)/2`,
`U  =(X7+X8)/sqrt(2)`.

The coefficient vectors of `S,C,D0,U` are unit; `C` and `D0` are orthogonal but are generally **dependent** because they use the same original variables. For `0<=rho<=1`, put

`D_rho = sqrt(1-rho^2) D0 + rho U`,
`Q_{a,b,rho}=2 b S C + a D_rho^2`,                                  (5.1)

with `a,b>0`.

The three coefficient vectors `S,C,D_rho` are orthonormal in physical coordinate space. Thus the physical quadratic matrix has exactly the nonzero spectrum

`boxed: {-b, a, b}`                                                  (5.2)

for every `rho`. Therefore `a,b>=1` puts (5.1) literally inside the owner's target class.

### 5.1 New private-bank endpoint

For `rho>0`, rewrite

`a D_rho^2 = a rho^2 ( U + sqrt(1-rho^2)/rho D0 )^2`.               (5.3)

Use Theorem 4.1 with the private bank `(X7,X8)`, `gamma=(1,1)/sqrt(2)`, cross operator `M=2b s c^T` of norm `sigma=2b`, and the `Y`-dependent square shift in (5.3). It gives

`boxed: ||p_{Q_{a,b,rho}}||infinity <= 8/(rho sqrt(ab)).`           (5.4)

No independence of `C,D0`, or of any rotated pair, is asserted.

### 5.2 Earlier capped-scalar/dependent-pair receiver

The completed account02/B18 theorem `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source commit `ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`, states:

If `S` has density cap `K`, is independent of a pair `(C,D)` with arbitrary joint density cap `M`, and

`T=2 beta S C + alpha C^2+2 delta C D+gamma D^2`,

then

`||p_T||infinity <= 3(2 M K)^(2/3)|beta^2 gamma|^(-1/3)`.           (5.5)

Here `S` has cap `K<=sqrt(2)` by Rudelson--Vershynin. The pair `(C,D_rho)` is a two-dimensional **orthogonal marginal of the original product block `(X3,...,X8)`**, so Livshyts--Paouris--Pivovarov gives its joint density cap `M<=2`, with no independence claim. Thus

`boxed: ||p_{Q_{a,b,rho}}||infinity
 <= 3*2^(5/3) (a b^2)^(-1/3)
 = 9.524406311809198... (a b^2)^(-1/3).`                            (5.6)

Combining (5.4)-(5.6), for every `0<rho<=1`,

`boxed: ||p_Q||infinity <= min{ 8/(rho sqrt(ab)),
                                3*2^(5/3)(a b^2)^(-1/3) }.`         (5.7)

At `rho=0`, (5.6) remains valid and pays the fully shared/dependent endpoint. The private-bank estimate is sharper exactly when

`a/b >= (8/(3*2^(5/3) rho))^6
     = 0.3511659807956101... rho^(-6)`.                             (5.8)

In particular, throughout the whole target range `a,b>=1` and `0<=rho<=1`, (5.6) alone gives a uniform bound below `9.525`; at the balanced fully-private point `a=b=rho=1`, the new endpoint gives `8`.

This is the promised analytic splice: the dependent-pair receiver is insensitive to loss of private mass as `rho->0`, while the conditional endpoint gains the square-dominant/private regime.

## 6. Required pinned e5f result applied to the same family

The pinned Claude-compatible record `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Theorem F there is proved: for exact rank-three spectral directions with original-coordinate eigenspace leverages at most `1/2`, and eigenvalues `lambda_1,lambda_2,lambda_3`,

`||p_Q||infinity <= 12 |lambda_1 lambda_2 lambda_3|^(-1/3)`.        (6.1)

For (5.1), the leverage scores of the three-dimensional spectral subspace are

- coordinates `1,2`: `1/2`;
- coordinates `3,...,6`: `(2-rho^2)/4 <=1/2`;
- coordinates `7,8`: `rho^2/2 <=1/2`.

Thus Theorem F applies literally, without rotating the source law or asserting independence of `C,D0`, and gives the real all-line target inequality

`boxed: ||p_{Q_{a,b,rho}}||infinity <= 12 (a b^2)^(-1/3).`          (6.2)

The same pinned record's ruled-level-set Theorem C also applies when `a,b>=1` to the signature `(2+,1-)`, giving the independent one-sheet estimate

`p_{Q_{a,b,rho}}(t) <= pi sqrt(2)` for a.e. `t>=0`.                 (6.3)

The new/capped-pair splice is a whole-line estimate; (6.3) is kept separate. The pinned counterexample search found no valid counterexample, but that search miss is **not** used as novelty evidence.

## 7. Corrections respected

The proof uses only disjoint ORIGINAL source banks for genuine independence. Orthogonal projections such as `(C,D_rho)` are used only through a joint-density cap. It does not infer post-rotation independence, does not use arbitrary-joint three-dimensional coarea, does not treat a conditional cap as independence, does not delete small coefficients, does not assume moments/support/log-concavity/iid laws, and does not infer a universal fixed good minor.

Continuity is separate: the latest partner theorem supplies `C_0` continuity in its narrower independent-scalar-square setting. Theorem 4.1 above is asserted only as an essential-density theorem because its measurable `Y`-dependent square shift destroys the simple global convolution used in the partner continuity argument.

## 8. Remaining implication

Call the next debt `QFORM-PRIVATE-SQUARE-EXTRACTION-OR-OVERLAP-EXIT-v1`:

Given an arbitrary target matrix with `s_3(A)>=1`, force either

1. an original-coordinate decomposition with `tau lambda >= c>0` of the physical form paid by (4.12), including only aligned coupling of the private rank-one square direction into the shared bank; or
2. a quantitatively paid dependent-pair / physical-pair / grouped-hub / ridge / product-Fourier exit.

The delicate survivor is when every candidate square direction has vanishing private product-bank mass **and** the shared two-dimensional projection becomes source-entangled in a way that cannot be isolated without leaving unaligned residual curvature. No small residual may be discarded under arbitrary unbounded cap-one inputs.
