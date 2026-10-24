SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B02, 2026-09-22T18:38:29Z.
attacking: translation-uniform fractional-trace synthesis for the full QFORM target, using integrated Fourier/mixed-norm estimates and a completed account03/B02 packet result while testing the stronger global L1 characteristic-function criterion against current corrections.

# QFORM-PAIR-HALF-RIESZ-AND-BANK-CASCADE-v1

Programme: `QFORM-DENSITY-3EIG-20260922`.
Owner control actually read this run: revision `2026-09-22.11` (later than the card's activation revision).
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

## 1. Exact target and correction state

The target remains: for every dimension, every product law of independent real coordinates whose one-dimensional densities are bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal essential-supremum bound for the density of `X^T A X`, or give a valid counterexample.

This report uses no moment assumption, no independence after an orthogonal rotation, no law-uniform pointwise Fresnel decay, no arbitrary-joint coarea bound, no positive conditional-projection-density moment, and no one-good-minor exhaustion. The current scalar-conditioning supremum proposal is also treated as unavailable: account03/B03 produced an exact four-variable target-class counterexample to `sup_b ||p_(Q3|Qrest=b)||_infinity < infinity`, while retaining a bounded full output density.

The target-wide unweighted criterion `integral |phi_Q(t)| dt < infinity` is not used. I did not obtain a source-valid exact-product counterexample to that stronger criterion in this run. Instead the new argument identifies and exploits the strictly weaker weighted integrated quantity

`H_(1/2)(R):=sup_y E |R-y|^(-1/2)`,

which account03/B03 controls by a `|t|^(-1/2)`-weighted characteristic-function integral in determinant-bank regimes.

Source pins used below:

1. Prior account02/B02 translation-uniform pair theorem: `yspennstate/math-open-problems@a68504400f3679153ba22ad2852b3fe0c4048dc1`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T181118Z-account02-B02-QFORM-r11/REPORT.md`, read-back blob `d7023211a6c9285d2defaf4d7f09fa820a0ccbbe`.
2. Named partner account03/B02: `yspennstate/math-open-problems@056867164c939f4e70988e762258f2542e32fd75`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T182919Z-account03-B02-qform-r12/REPORT.md`, read-back blob `1ebddb8061731f94bcdebc702a60b7840e646c28`.
3. Compatible account03/B03 determinant-bank half-Riesz report: `yspennstate/math-open-problems@924b3c4c70f86a64402863fe228f641bf3db60b2`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T175531Z-account03-B03-QFORM-r17/REPORT.md`.
4. The normalized one-dimensional bank-density application uses Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, Theorem 1.2: a normalized linear combination of independent one-dimensional densities bounded by one has density bounded by `sqrt(2)`.

## 2. First new implication: an indefinite physical pair is a half-Riesz transducer

Take the exact setting of the prior account02/B02 pair theorem. Thus `X=(X1,X2)` has independent cap-one densities, `Z` is independent of `X`, `B` is a real symmetric invertible indefinite `2 x 2` matrix, and

`Q=(X+m(Z))^T B (X+m(Z))+R(Z)`.

Write

`D=|det B|`, `kappa=sigma_min(B)`.

The previous proof established a conditional-density envelope independent of the random translation `m(Z)`. With

`T=2D/kappa`,

it can be taken as

`Psi(tau)=D^(-1/2)[2sqrt(2)+log(T/|tau|)]` for `0<|tau|<=T`,

`Psi(tau)=4 kappa^(-1/2)|tau|^(-1/2)` for `|tau|>T`.

The new observation is that the two pieces glue under one exact half-Riesz majorant:

`boxed(Psi(tau) <= 4 kappa^(-1/2)|tau|^(-1/2)  for every tau!=0.)`       (2.1)

Proof. On the outer region this is equality with the displayed envelope. On the inner region put `x=|tau|/T in (0,1]`. Then

`kappa^(1/2) |tau|^(1/2) Psi(tau)`
` = sqrt(2x)[2sqrt(2)+log(1/x)].`

Writing `x=e^(-y)`, `y>=0`, the right side is

`sqrt(2)e^(-y/2)(2sqrt(2)+y)`.

Its derivative has the sign of `1-sqrt(2)-y/2`, hence is strictly negative for `y>=0`; its maximum is the value `4` at `y=0`. This proves (2.1).

Averaging the conditional density over `Z` therefore requires **no density assumption on `R` at all**:

`p_Q(t) <= 4 kappa^(-1/2) E |t-R|^(-1/2)` a.e.

Consequently

`boxed(||p_Q||_infinity <= 4 kappa^(-1/2) H_(1/2)(R).)`                 (2.2)

This is `QFORM-PAIR-HALF-RIESZ-TRANSDUCER-v1`. It is translation-uniform: `m(Z)` may depend arbitrarily on the same residual bank that determines `R(Z)`. The determinant `D` disappears from the final transducer; only the smaller absolute eigenvalue `kappa` of the indefinite physical pair is paid.

This is an integrated-Fourier interface rather than a pointwise-decay assertion: when account03/B03 supplies `H_(1/2)(R)` from `integral |t|^(-1/2)|phi_R(t)|dt`, equation (2.2) converts that weighted time integral into a bounded full density.

## 3. Determinant-bank splices: the missing half-order is now paid once an outer pair exists

The account03/B03 report proves, from the reviewed regularized-determinant estimate, that for a residual cross block `C`,

`H_(1/2)(R) <= 7.673759290384858 E_2(C)^(-1/8)`                         (3.1)

when the selected-side cross-range leverage is at most `1/2`, and unconditionally

`H_(1/2)(R) <= 9.840655864922019 E_3(C)^(-1/12)`.                       (3.2)

It also gives the sharper exact-cross-rank-two estimate

`H_(1/2)(R) <= 7.270461147134126 (sigma_1(C)sigma_2(C))^(-1/4)`.       (3.3)

Substitution into (2.2) gives the new composite branches

`boxed(||p_Q||_infinity <= 30.69503716153943 kappa^(-1/2) E_2(C)^(-1/8))`  (3.4)

under the leverage condition,

`boxed(||p_Q||_infinity <= 39.36262345968808 kappa^(-1/2) E_3(C)^(-1/12))` (3.5)

with no leverage hypothesis, and in exact residual cross rank two,

`boxed(||p_Q||_infinity <= 29.08184458853650 kappa^(-1/2)
       (sigma_1(C)sigma_2(C))^(-1/4)).`                                (3.6)

Thus the determinant-bank half-Riesz resource, which by itself lacks the final half-order for a parent density, becomes a complete density estimate as soon as one independent original-coordinate indefinite pair with controlled `kappa` is available. No single residual minor is selected: `E_k` is the sum of squared `k x k` cross minors.

This does not prove that the bare three-large-eigenvalue hypothesis always supplies such an outer pair; the live one-pair and local-rank-three counterexamples forbid that shortcut. It is an analytic closure of that branch, not a structural exhaustion theorem.

## 4. Named partner account03/B02 applied: pair plus one affine hyperbolic packet

The current named partner report proves for independent `X,U`, with `X` density cap one and `U` density cap `M`, and arbitrary `H(X,V)` with `V` independent of `(X,U)`,

`R=2a XU+H(X,V)`

has

`||p_R||_3 <= 3 |a|^(-2/3) M^(2/3)`                                   (4.1)

and then the half-Riesz estimate

`H_(1/2)(R) <= 8sqrt(2) sqrt(M/|a|)`.                                  (4.2)

The restriction that `H` contain no hidden `U`-dependent curvature is essential and is retained here.

Applying (4.2) to (2.2) gives the new dependence-safe cascade

`boxed(||p_Q||_infinity <= 32sqrt(2) sqrt(M/(kappa |a|))).`             (4.3)

The outer indefinite pair may have an arbitrary random translation depending on `(X,U,V)` and the residual; the inner packet remains product-preserving. This is a direct mathematical use of the designated OTHER-account result, not a citation-only dependency.

## 5. Bank-level version: aggregate before paying reciprocal pair scale

The half-Riesz transducer scales cleanly to already-aggregated independent coordinate banks. Let `Y_1,Y_2` be independent with density caps `M_1,M_2`, independent of `Z`, and consider

`Q=2a(Y_1+s_1(Z))(Y_2+s_2(Z))+R(Z)`, `a!=0`.

Scale `U_i=M_i Y_i`. Their densities are bounded by one. The pair matrix becomes

`[[0,a/(M_1M_2)],[a/(M_1M_2),0]]`,

whose smallest singular value is `|a|/(M_1M_2)`. Hence (2.2) gives

`boxed(||p_Q||_infinity <= 4 sqrt(M_1M_2/|a|) H_(1/2)(R).)`            (5.1)

This is a genuine bank-level analogue of the previous physical-pair estimate: one may first form independent linear aggregates on disjoint original-coordinate banks and only then pay their density caps. It therefore avoids choosing one tiny physical `2 x 2` pair from a spread bank.

Combining (5.1) with the named partner bound (4.2) for a disjoint residual packet

`R=2bXU+H(X,V)`, `||p_U||_infinity<=M_3`,

yields

`boxed(||p_Q||_infinity <= 32sqrt(2)
       sqrt(M_1 M_2 M_3/(|ab|))).`                                    (5.2)

All bank groups in (5.2) are genuinely disjoint original-coordinate groups. The outer shifts `s_1,s_2` may depend on the full residual bank; the inner `H` may depend on `(X,V)` but not on the `U` bank, exactly as in the partner theorem.

If each bank variable is a normalized linear form in independent cap-one coordinates, Rudelson--Vershynin gives `M_i<=sqrt(2)`, so for `|a|,|b|>=1`, (5.2) is at most

`32*2^(5/4) < 76.110`.                                                (5.3)

The numerical value is not intended as sharp; the point is dimension-free grouped-coordinate closure without a selected physical pair.

## 6. Complementary Lp bank cascade and the previous exact stress family

For the same pure hyperbolic outer bank pair, the prior pair-to-residual `L^q` theorem also scales exactly. For `p>2`, `q=p/(p-1)`, if `R` has density `r_R in L^q`, then

`||p_Q||_infinity <= C_p |a|^(1/p-1)
                     (M_1M_2)^(1-1/p) ||r_R||_q`,                    (6.1)

where

`C_p^p=4 int_0^infinity (2sqrt(2)+s)^p e^(-s) ds
        +2^(2+3p/2)/(p/2-1).`

Applying the named partner's affine-hyperbolic `L^q` lemma,

`||r_R||_q <= q |b|^(-1/p) M_3^(1/p)`,                               (6.2)

gives

`boxed(||p_Q||_infinity <= q C_p |a|^(1/p-1)|b|^(-1/p)
       (M_1M_2)^(1-1/p) M_3^(1/p)).`                                 (6.3)

For normalized disjoint banks (`M_1,M_2,M_3<=sqrt(2)`) and `|a|,|b|>=1`, taking `p=6` gives

`C_6^6=25152+16512sqrt(2)`,

and

`boxed(||p_Q||_infinity <= 13.68004670198984.)`                        (6.4)

This is stronger than the half-Riesz-only numerical constant (5.3), but (5.1) remains useful because it can consume determinant-bank half-Riesz control even when no residual `L^q` density estimate is available.

As a second check, revisit the exact target stress family from the preceding B02 run,

`Q_m=2Y_1Y_2+Y_3^2`,

whose three bank variables are independent normalized linear forms and therefore each have density cap at most `sqrt(2)`. Every selected physical pair in that family has vanishing conditioning scale as `m` grows, while the grouped variables stay dimension-free.

For a variable `W` with density cap `M`, any translated square `d(W+h)^2` has, for `1<q<2`,

`||p_(d(W+h)^2)||_q
 <= |d|^(1/q-1) [2^(q-1)/(2-q)]^(1/q) M^(2-2/q).`                    (6.5)

This follows from the exact square pushforward, `(u+v)^q<=2^(q-1)(u^q+v^q)`, and the one-dimensional bathtub bound for the weight `|x|^(1-q)`; mixing arbitrary shifts preserves the `L^q` norm by Minkowski.

Putting (6.5) into (6.1) and choosing `p=8`, `q=8/7`, gives

`C_8^8=957440sqrt(2)+4119040/3`

and the improved uniform stress-family bound

`boxed(||p_(Q_m)||_infinity <= 15.91104060610644)`                     (6.6)

for every `m` and every admissible product input law. This improves the previous `p=4` value `20.4694984974508` and again pays the aggregate bank before any tiny physical pair.

## 7. What is now paid and what remains

The new implication (2.2) is the main analytic advance of this run. An indefinite pair's logarithmic singularity is exactly dominated by a half-Riesz kernel with constant `4/sqrt(kappa)`. Therefore any source-valid residual half-Riesz estimate can close a full density branch even when the residual itself has no useful `L^infinity` density bound and even when the pair translation is maximally dependent on the residual.

Equations (3.4)--(3.6) combine this with determinant-bank integrated Fourier control. Equations (4.3), (5.2), and (6.3) consume the current account03/B02 packet theorem and give physical-pair and grouped-bank cascades. Equation (6.6) improves the exact target family that refuted single-pair extraction.

The first unpaid implication is now structural:

> From the surviving third-compound/O0 aggregate geometry under `s_3(A)>=1`, produce either (i) an original-coordinate indefinite pair with `kappa` bounded at the scale needed by (2.2) whose residual has one of the determinant-bank half-Riesz resources, or (ii) two genuinely disjoint grouped-coordinate bank variables to which (5.1)/(6.1) applies before reciprocal minor selection, or route to an already completed ridge/diffuse/square branch.

The fresh account02/B19 raw heavy-overlap factorization is compatible with this target but does not itself identify its orthogonal row residual with a physical Schur complement or force an indefinite principal pair. Those identifications remain unpaid and must not be assumed.

No full-target theorem or counterexample is claimed. No source-valid exact-product counterexample to universal unweighted `||phi_Q||_1` was produced here; the successful mechanism is the weaker weighted half-Riesz integral plus product-preserving bank aggregation.
