SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B14, 2026-09-22T23:29:42Z.

# account04/B14 — translation-uniform localized core and ruled Schur fibers

**Run:** `20260922T232942Z-account04-B14-schur-threshold-r5`  
**Assignment:** Translations and localization  
**Status:** `LOCALIZED-CORE THEOREM / RULED-SIDE REFINEMENT / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source state

The target is the universal essential density bound for `Q=X^T A X` when the real coordinates of `X` are independent probability densities bounded by one and `A=A^T` has at least three eigenvalues of modulus at least one. No moment, bounded-support, connected-support, or post-rotation independence hypothesis is added. Continuity is separate.

Fresh owner control is revision `2026-09-22.15`; the live correction inbox was consumed at blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`. The starting Claude source was `e5f71d79eff325201dd0274053d20268ce65b837`. The same directory has a later substantive revision at `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`, retained unchanged in `29e682234ef18500588293f4e947e79ca768a251`. At that revision the three requested files have blobs

- `RESULTS.md`: `56edacbd7aa105e7aaabfcfb6f377c268a134817`;
- `FOURIER_ROUTE_REPORT.md`: `9da148eed6cd43b1046a6f91d0f9329e12921cb4`;
- `COUNTEREXAMPLE_SEARCH.md`: `d11ace6dbf5ecdf6ce5921f80f727e92e95bf8fc`.

The later source proves the full `n=3` theorem with constant 20, including arbitrary linear and constant terms. The older ruled theorem supplies a sharper constant on the one-sheet side. Both results use the original product provenance; neither infers a trace estimate from an arbitrary bounded joint density.

The account04/B14 law-level purification theorem used below is at
`yspennstate/math-open-problems@321ec7899f4972d125d641408512fe9e5e9dcf4c`.
The completed account01/B14 result actually applied is at
`yspennstate/math-open-problems@b111363ff02b67015d14db35482e0150591744cd`,
path
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B14/20260922T221141Z-account01-B14-QFORM-r22/REPORT.md`,
blob `0f94532a63c300534bcc7ef2dd61cfac7df94e14`.

## 2. Translation-uniform localized-core theorem

Split the original coordinates as `X=(W,Z)`, where `W=(X_i,X_j,X_k)` consists of three singleton physical coordinates. Write the affine quadratic expression as

`Q = W^T B W + 2 W^T C Z + Z^T D Z + 2 a^T W + 2 b^T Z + c.`     (2.1)

Assume that the physical principal block `B` is invertible and

`gamma := sigma_min(B) > 0.`                                      (2.2)

### Theorem 2.1

For arbitrary independent cap-one input laws, arbitrary `C,D,a,b,c`, and every interval `I`,

`P(Q in I) <= (20/gamma) |I|,`

and consequently

`||p_Q||_infinity <= 20/gamma.`                                  (2.3)

### Proof

Condition on the outside original coordinates, `Z=z`. The three entries of `W` remain independent and their densities remain bounded by one. The conditional polynomial is

`q_z(w)=w^T B w + 2(Cz+a)^T w + z^T D z + 2b^T z + c.`           (2.4)

The later Claude source proves that every three-variable quadratic polynomial whose quadratic matrix has all three eigenvalues of modulus at least one has output density at most 20, uniformly in all linear and constant terms. Apply that theorem to `B/gamma` and then rescale the output by `gamma`. This gives a conditional density `p_z` satisfying

`||p_z||_infinity <= 20/gamma`                                   (2.5)

for every conditioning value for which the regular conditional law is defined. Therefore

`P(Q in I)=E[P(q_Z(W) in I | Z)] <= (20/gamma)|I|.`

This interval domination constructs an essentially bounded density and proves (2.3). No completion-of-squares integrability, tail control, or support localization is needed. QED.

This is a genuine localized-core theorem: arbitrary dense couplings `C`, arbitrary outside self-couplings `D`, and every conditioning-generated affine term are retained. The gate is an actual principal-block spectral gate (2.2). The bare global assumption `s_3(A)>=1` does not imply a dimension-free lower bound on `gamma` for some physical triple, so Theorem 2.1 is not the full conjecture.

## 3. Ruled Schur-fiber refinement

Assume now that `B` has inertia `(+,+,-)`, with eigenvalues `lambda_1, lambda_2, -mu`, all positive in modulus. Completing the physical block gives

`m(z)=B^{-1}(Cz+a),`

`Q=(W+m(Z))^T B(W+m(Z))+h(Z),`                                  (3.1)

where

`h(z)=z^T(D-C^T B^{-1}C)z + 2(b-C^T B^{-1}a)^T z + c-a^T B^{-1}a.`  (3.2)

For an interval `I=[u,v]`, the event `h(Z)<=u` places `I-h(Z)` entirely on the one-sheet side. Translation of the three physical coordinates preserves their independence and density caps. The rough ruled interval theorem therefore gives

`P(Q in I, h(Z)<=u) <= C(B)|I|,`                                 (3.3)

where

`C(B)=(lambda_1 lambda_2 mu)^(-1/2) * integral_0^(2pi)
       (sin(theta)^2/lambda_1 + cos(theta)^2/lambda_2 + 1/mu)^(-1/2) dtheta`

and

`C(B) <= pi sqrt(2)/gamma.`                                      (3.4)

For inertia `(+,-,-)`, the corresponding assertion holds on the opposite side, with `h(Z)>=v`.

Equations (3.1)-(3.4) identify the exact random Schur critical value and preserve arbitrary translations and outside couplings. If only the ruled theorem were available, the complementary two-sheet event would still be unpaid: the bound `P(h(Z)>u)` is not of order `|I|`. The later three-dimensional theorem pays that complement uniformly through (2.5), yielding the full localized estimate (2.3). Thus kernel/critical-value leakage is exposed rather than hidden.

## 4. Finite-mixture transfer and geometric slab form

The account04/B14 purification theorem states that every cap-one probability density is an `L1` limit of finite convex combinations of indicators `1_E`, where `E` is a bounded finite union of intervals and `|E|=1`. Coordinatewise expansion, product total variation, and pushforward contraction show that a uniform interval inequality for all such product indicators transfers to all cap-one product laws with exactly the same constant.

Consequently Theorem 2.1 is equivalently reduced, with no loss, to the geometric slab estimate

`Leb{x in E_1 x ... x E_n : x^T A x + linear(x)+c in I}
   <= (20/gamma)|I|`                                             (4.1)

for bounded finite-interval unions `E_r` of total measure one, whenever the selected physical principal triple obeys (2.2). There is no assertion that an extremizing threshold set exists on the infinite line, and no bound on fragment count, diameter, or separation.

The same transfer applies to (3.3), including its random Schur threshold after conditioning. Total-variation passage proves essential boundedness; it does not by itself transfer continuity.

## 5. Concrete application of account01/B14

Account01/B14 proves the following translation-uniform pair-plus-bank theorem. Let `P={i,j}` be two singleton physical coordinates, let `G` be a disjoint original-coordinate bank, let `u` be a unit vector supported on `G`, and put `U=[e_i,e_j,u]`. Suppose for `S=P union G`

`A_SS=U M U^T,    A_SR=U C,`                                   (5.1)

with `M` nonsingular, arbitrary `C`, arbitrary outside block, and the leading physical `2x2` block `B_2` of `M` invertible indefinite. Put

`D_2=|det B_2|,   kappa=sigma_min(B_2),   s=sigma_min(M).`

Then

`||p_(X^T A X)||_infinity
 <= 8(2e)^(1/4) (D_2 kappa s)^(-1/4)
 < 12.216 (D_2 kappa s)^(-1/4).`                                 (5.2)

The dependence is preserved: conditioning only on outside original coordinates leaves the pair and bank scalar mutually independent; the physical-pair shift may depend arbitrarily on the bank scalar. No nonseparable remainder is treated as a product twist.

Combining (5.2) with the finite-mixture theorem gives the concrete next geometric inequality

`Leb{x in product_r E_r : x^T A x in I}
 <= 8(2e)^(1/4)(D_2 kappa s)^(-1/4)|I|`                         (5.3)

for every collection of bounded finite-interval unions `E_r` with `|E_r|=1`, and hence the identical inequality for every arbitrary cap-one product law. This applies the assigned partner theorem at an actual target-level inequality while retaining unbounded and arbitrarily fragmented laws through the zero-loss approximation.

## 6. Continuity and remaining obstruction

The arguments above prove interval domination and therefore an essentially bounded density. The finite-mixture limit alone does not prove continuity. The separate fixed-instance regularity theorem may be invoked to choose a `C_0` representative, but no uniform modulus of continuity follows from this localization.

The full universal conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Two precise structural debts remain:

1. the global three-large-eigenvalue condition does not guarantee a physical `3x3` principal block with `sigma_min(B)` bounded below universally;
2. outside the factorization (5.1), the linear innovation and quadratic leakage can occupy the same coordinate bank, so account01/B14's independence-preserving pair-plus-bank compiler cannot be applied.

The next step is a product-preserving structural dichotomy: either expose a quantitatively conditioned physical triple and use (2.3), expose the exact pair-plus-bank factorization and use (5.2), or route the remaining no-pivot/same-bank configuration to the decoupling or hub mechanisms. No support or moment assumption can pay this debt.
