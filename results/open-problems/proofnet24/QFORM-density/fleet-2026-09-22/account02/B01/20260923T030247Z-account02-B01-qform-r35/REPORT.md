SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T03:02:47Z.
attacking: the critical two-row volume endpoint by replacing the failed h<1 Jensen limit with projected-slope L2/Plancherel smoothing, then spending a third independent grouped square on a strict-N3 dense-leaf stress family.

# Critical two-row projected-slope smoothing

Run: `20260923T030247Z-account02-B01-qform-r35`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: account02/B01, Oscillatory replacement  
Status: **SUPPORTING TARGET-LEVEL THEOREM + STRICT-N3 APPLICATION / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and source boundary
The target remains: for arbitrary independent real coordinates with probability densities bounded by one and every real symmetric A with at least three eigenvalues of modulus at least one, prove one universal finite essential-supremum bound for the density of X^TAX, or give a valid counterexample. No moments, compact support, log-concavity, Gaussianity, identical laws, diagonal-basis independence, or post-rotation independence are used.

The law-uniform scalar pointwise Fresnel estimate remains false: for any prescribed frequency s and small delta, one may choose a cap-one density supported on finitely many intervals inside `{x: dist(s x^2,2 pi Z)<=delta}` and obtain `Re E exp(i s X^2)>=cos(delta)`. Nothing below uses a scalar law-uniform `|s|^{-1/2}` envelope.

Current completed sources actually used:

1. `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`. In particular, the two-dimensional product-projection density cap `<=2` after orthonormal projection and Theorem H are used below at equations, not only cited.
2. Designated partner account03/B01, bundle tip `f651c96b5c87b1b0df9a5701b9b47293d08dc94c`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T013054Z-auto11/REPORT.md`. Its critical rank-two volume half-Riesz theorem is applied in Section 5.
3. The source square-peel/fractional-Riesz interface from the same Claude directory (later source-pinned update `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`) is used in Section 4.

## 2. New theorem: the exact h=1 two-row half-Riesz endpoint

### Theorem 2.1 (two-physical-hub critical half-Riesz)
Let `X=(X1,X2)` and `Y=(Y1,...,Ym)` have mutually independent real coordinates, each with density at most one. Let `C` be any real symmetric `2 x 2` matrix, `M` any real `2 x m` matrix of rank two, `c in R^2` fixed, and `R(Y)` any real measurable function finite almost surely. Put

`S = X^T C X + 2 X^T(MY+c) + R(Y)`,

`D = det(M M^T)>0`.

Then

`boxed: H_{1/2}(S):=sup_s E|S-s|^(-1/2) <= 2^(11/4) D^(-1/8).`        (2.1)

There is no restriction on `C` or `R`. In particular, arbitrary quadratic curvature, signs and affine terms among the Y variables are allowed.

### Proof
For `t !=0` define

`F_t(u)=int_R2 f1(x1) f2(x2) exp(i t x^T C x + 2 i t u.x) dx`.

If

`g_t(x)=f1(x1)f2(x2)exp(i t x^T Cx)`,

then with Fourier convention `ghat(xi)=int exp(i xi.x)g(x)dx`,

`F_t(u)=ghat_t(2t u)`.                                             (2.2)

Let `p` be the density of `MY+c`. Factor `M=(MM^T)^(1/2)R0` with `R0 R0^T=I2`. The current product-projection theorem gives `||p_{R0Y}||_infinity<=2`; change of variables therefore gives

`||p||_infinity <= 2 D^(-1/2)`,

hence

`||p||_2 <= sqrt(2) D^(-1/4)`.                                    (2.3)

The arbitrary self phase `R(Y)` is discarded only after the joint slope has been formed:

`|phi_S(t)|
 <= E_Y |F_t(MY+c)|
 <= ||p||_2 ||F_t||_2`.                                            (2.4)

By Plancherel in the two physical hub variables,

`||F_t||_2^2
 = (2|t|)^(-2) int_R2 |ghat_t(xi)|^2 dxi
 = pi^2 |t|^(-2) int_R2 f1(x1)^2 f2(x2)^2 dx
 <= pi^2 |t|^(-2)`,                                                (2.5)

because `0<=fi<=1` and `int fi=1`. Combining (2.3)-(2.5),

`|phi_S(t)| <= min(1, K/|t|)`,

`K = pi sqrt(2) D^(-1/4)`.                                        (2.6)

At exponent one half the one-sided Riesz representation is

`|x|^(-1/2)=sqrt(2/pi) int_0^infinity cos(tx)t^(-1/2)dt`.          (2.7)

The integral is now absolutely integrable after expectation: (2.6) gives `t^(-1/2)` at zero and `t^(-3/2)` at infinity. Hence, uniformly in `s`,

`E|S-s|^(-1/2)
 <= sqrt(2/pi) int_0^infinity t^(-1/2) min(1,K/t) dt
 = 4 sqrt(2/pi) sqrt(K)
 = 2^(11/4) D^(-1/8)`.                                            (2.8)

This proves (2.1).

### Why this is a genuinely new endpoint
For the designated partner's rank-two volume theorem, if the constrained bank consists of exactly these two physical rows then the two squared-volume row marginals are both `alpha=1`; thus `h=1`, `q=2`, and its factor `(2-q)^(-1)` is unavailable. Theorem 2.1 changes mechanism exactly at that endpoint: it uses the L2 density of the **joint projected slope** `MY` and two-dimensional Plancherel in the original hub coordinates. It neither assumes nor implies scalar quadratic-phase pointwise decay.

## 3. Averaged-frequency interpretation
Equation (2.6) is a joint averaged-slope estimate. It is pointwise in the final frequency only after integrating the random two-dimensional slope against its product-projection density. The scalar phase-alignment counterexample is therefore preserved. The critical consequence is distributional:

`H_{1/2}(S) <= 2^(11/4)D^(-1/8)`,

which is exactly the quantity needed by a third square. Absolute Fourier inversion of (2.6) alone would still have the expected logarithmic divergence; no density bound for a generic two-hub packet is claimed from (2.6) by itself.

## 4. Physical third-pivot certificate
Let `Q=X^TAX+b^TX+c0` and choose an ORIGINAL coordinate `k` with `a=A_kk !=0`. Complete the square exactly:

`Q = a (X_k + ell(X_-k))^2 + S(X_-k)`.                            (4.1)

Choose two further original coordinates `i,j`. Write the Schur residual in these two hub coordinates `X_H=(X_i,X_j)` and all other residual coordinates `Y` as

`S = X_H^T C X_H + 2 X_H^T(MY+c) + R(Y)`.                       (4.2)

If `rank(M)=2`, `D=det(MM^T)`, then the dependence-safe source square peel and Theorem 2.1 give

`boxed: ||p_Q||_infinity
 <= 2^(11/4) |a|^(-1/2) D^(-1/8).`                              (4.3)

All other Schur curvature and all affine leakage are retained. This does not assert that the bare three-large-eigenvalue hypothesis supplies a uniform lower bound on `|a|^4 D`; that structural implication remains unpaid.

## 5. Designated partner applied at an actual inequality
Take disjoint original banks `I={1,...,2m}` and `J={h1,h2}`. Let

`u=m^(-1/2)(1,...,1,0,...,0)`,
`v=m^(-1/2)(0,...,0,1,...,1)`,

with m entries in each half, and let the cross block from I to J be

`M0 = c [u v]`, `c>=1`.

Then `M0^T M0=c^2 I2`, so

`Z2=e2(M0^T M0)=c^4`,

and because this block has exact rank two, its squared two-volume row marginals are its row leverages, all exactly `1/m`. For `m>=2`, the completed account03/B01 theorem applies with `h<=1/2`, `q=1`, and gives, for **arbitrary within-bank self phases**,

`H_{1/2}(S) <= 4 sqrt(2e) c^(-1/2) < 9.327 c^(-1/2).`           (5.1)

If an independent grouped square `Z^2` is added and the density of `Z` is at most `sqrt(2)`, the square kernel gives

`||p_{S+Z^2}||_infinity <= sqrt(2) H_{1/2}(S)
                         <= 8 sqrt(e)c^(-1/2)
                         < 13.190 c^(-1/2).`                     (5.2)

Thus the designated partner has been used on the same family at the exact fractional-potential inequality. Theorem 2.1, applied with the two physical hubs on the J side, gives instead

`H_{1/2}(S) <= 2^(11/4)c^(-1/2)`,

and therefore

`||p_{S+Z^2}||_infinity <= 2^(13/4)c^(-1/2) < 9.514 c^(-1/2).`  (5.3)

The point is not the constant improvement; it is that Theorem 2.1 remains valid at the exact two-row `h=1` orientation where the partner's Jensen/volume compiler reaches its critical denominator.

## 6. Newest Claude Theorem H applied to a strict-N3 baseline
For the same two disjoint m-coordinate leaf banks, take physical hubs `X1,X2` and

`S0 = 2c X1 (u^T Y) + 2c X2 (v^T Y)`.                            (6.1)

Apply Theorem H from `RESULTS.md` with hub set `{X1,X2}`, leaf set `Y`, no Fresnel square directions (`r=0`) and diagonal leaf self block zero. The augmented Gram matrix is

`G = c^2 I2`,

and every leaf leverage is exactly `1/m<=1/2`. The theorem gives the actual frequency inequality

`|phi_{S0}(t)| <= min(1, 4 pi^2 c^(-2)|t|^(-2)).`               (6.2)

Integrating the envelope gives

`boxed: ||p_{S0}||_infinity <= 4/c.`                            (6.3)

Adding any independent random variable cannot increase this density cap. In particular, adding the independent grouped square from Section 7 preserves `<=4/c`. This is an equation-level application of a completed result in the owner-required newest Claude report, not a summary.

## 7. Strict-N3 dense-leaf family: the new theorem survives arbitrary full-rank leaf curvature
Let `2m=2^r` and let `H_{2m}` be the symmetric Sylvester Hadamard matrix, so

`K_m := H_{2m}/sqrt(2m)`, `K_m^2=I`, `||K_m||op=1`.              (7.1)

Fix `0<eta<=1/4` and put `c=1+eta`. Let all coordinates below be mutually independent with densities at most one. Use two physical hubs `X1,X2`, a `2m`-coordinate leaf bank `Y`, and an independent m-coordinate bank `W`. With u,v as above and

`w=m^(-1/2)(1,...,1)`,

define

`S_{m,eta}
 = 2c X1 u^T Y + 2c X2 v^T Y + eta Y^T K_m Y`,                 (7.2)

`Q_{m,eta}=S_{m,eta} + (w^T W)^2`.                              (7.3)

### 7.1 Exact target spectrum
At `eta=0` the hub/leaf block has nonzero spectrum `{c,c,-c,-c}`. The dense leaf perturbation in (7.2) has operator norm eta. Weyl therefore gives at least two eigenvalues `>=c-eta=1` and at least two eigenvalues `<=-c+eta=-1`. The independent rank-one square contributes one further eigenvalue `1`. Thus every `Q_{m,eta}` is inside the exact target, with at least five eigenvalues of modulus at least one.

### 7.2 Strict no-pivot geometry
All physical hub diagonals are zero. Leaf diagonals have magnitude `eta/sqrt(2m)`; W-bank diagonals are `1/m`. The only hub-leaf entries have magnitude `c/sqrt(m)`. Hence a hub-leaf physical pair has determinant magnitude at most `c^2/m`. For two leaf coordinates,

`|A_ii A_jj-A_ij^2| <= eta^2/m`,

because every entry of `K_m` has magnitude `1/sqrt(2m)`. W-W pair determinants vanish because `ww^T` has rank one, and cross-bank pair determinants are still smaller products of the displayed diagonals. Consequently, for every fixed `tau>0`, all physical diagonals and all physical pair determinants are `<tau` once m is large enough. This is therefore a strict-N3 stress family for every fixed no-pivot threshold.

### 7.3 Uniform density bound despite dense non-diagonal leaf curvature
The two-hub slope matrix in (7.2) is

`M = c [u^T; v^T]`,

so `MM^T=c^2 I2`, `D=c^4`. Theorem 2.1 ignores the full-rank dense self block `eta K_m` and gives

`H_{1/2}(S_{m,eta}) <= 2^(11/4)c^(-1/2).`                       (7.4)

The normalized sum `Z=w^TW` has density at most `sqrt(2)` by the one-dimensional Rogozin/Ball product-projection estimate. Therefore `Z^2` has density at `y>0` at most `sqrt(2)y^(-1/2)`. Since Z is independent of `S_{m,eta}`,

`boxed: ||p_{Q_{m,eta}}||_infinity
 <= sqrt(2) H_{1/2}(S_{m,eta})
 <= 2^(13/4)c^(-1/2)
 < 9.514.`                                                       (7.5)

This is uniform in m, eta and all admissible input laws. It spends the third grouped square only **after** the arbitrary dense leaf curvature has been absorbed into the two-hub half-Riesz packet.

The direct Theorem-H calculation (6.2) pays the zero-curvature endpoint `eta=0` with the stronger density constant `4/c`. Equation (7.5) is the complementary dense-leaf continuation: it does not need to represent `eta K_m` as a low-rank-plus-diagonal leaf phase.

## 8. What remains unpaid
The new theorem removes an analytic endpoint, not the structural N3 problem. The first unpaid implication is

`QFORM-CRITICAL-TWO-ROW-TO-N3-ROUTING-v1`:

from the general strict-N3 hypotheses, show that every survivor of the diffuse-volume/tail exits either

1. exposes a physical scalar pivot whose Schur residual has two original-coordinate hub rows with quantitative slope Gram `det(MM^T)` sufficient for (4.3), or
2. exposes an independent/grouped third-square or equivalent curvature packet that can spend (2.1), or
3. routes to the existing exact-null, mixed-hub, volume, ridge, pair-log or grouped-square branches,

without paying an uncontrolled reciprocal tiny physical determinant first.

Neither N3 nor full QFORM is proved here. In particular, the bare spectral hypothesis does not currently force a uniform lower bound on the product currency in (4.3). Existing counterexamples to a universally good fixed minor/cross cut remain respected.

## 9. Review status
This is a new supporting proof supplied for use and review. It has not received two independent end-to-end reviews, and it is not a full-proof candidate. The phase-aligned scalar counterexample, independence-after-rotation correction, arbitrary-joint coarea correction and conditional-fiber corrections remain in force.
