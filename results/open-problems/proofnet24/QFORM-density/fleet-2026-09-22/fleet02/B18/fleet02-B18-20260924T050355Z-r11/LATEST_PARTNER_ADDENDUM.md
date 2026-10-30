SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-24T05:03:55Z.
attacking: refresh the designated-partner edge after fleet03/B18 auto19 arrived during this same run; splice its Hilbert--Schmidt bilinear/private-square receiver into the target stress family and preserve the complementary retention scope of the RV rank-one-tail theorem.

# Latest-partner addendum — fleet03/B18 auto19

The full QFORM target remains OPEN / NOT PROVED / NOT DISPROVED.

After the main report was published, a newer compatible designated-partner result appeared:

- fleet03/B18 auto19 scientific commit `7308d156465db33641b1db6e8609777b832c5da2`;
- PASS check commit `bc79736952c7095dde0944018c4d5ba45e79673a`;
- theorem package `QFORM-BILINEAR-CUBE-CONCENTRATION-DOMINANCE-v1`, Hilbert--Schmidt half-Riesz bound, and `QFORM-BILINEAR-PRIVATE-SQUARE-HS-v1`.

It supersedes auto18 as the latest compatible designated-partner input for this run. The main report remains mathematically valid, but every “latest partner” reference there should now be read with this addendum.

## 1. Exact source match of auto19

Auto19 uses two primary sources at scopes matching the stated bilinear theorem.

1. Juškevičius--Lee, arXiv:1503.09190, Theorem 1: concentration of a sum of independent density-capped variables on a measurable set is dominated by the corresponding centered-uniform rearrangement. In dimension one, after fixing one bank of a bilinear form, this applies to the scalar summands `a_jY_j` with cap `1/|a_j|` and gives the required uniform-in-output-center interval comparison.

2. Hu--Paouris, arXiv:2403.20192, Theorems 1.1 and 1.3: independent random vectors with independent coordinates and coordinate densities bounded by one have simple tensors less peaked on symmetric convex bodies than centered cube uniforms; their tensor small-ball theorem supplies the one-dimensional projection estimate used by auto19. No moments, bounded support, iid, centering, log-concavity, or smoothness are added.

No projected-coordinate independence is inferred.

## 2. Newest partner theorem actually applied to the same target family

Recall from the main report, for `N>=5`,

`delta=(N-1)^(-1/2)`,

`Q_N = 2 delta sum_{j=1}^N X_jY_j + 2UV + W^2`,

with all variables independent and cap one. Its physical spectrum is `+/-delta` (each multiplicity `N`) together with `-1,+1,+1`, so it has exactly three eigenvalues of modulus at least one.

Condition on the original coordinates `U,V`. The remaining random variable is a bilinear form plus the genuinely private original square `W^2`, with

`M=2 delta I_N`, `a=1`,

so

`||M||_HS = 2 delta sqrt(N) = 2 sqrt(N/(N-1))`.

Auto19's private-square theorem therefore gives the literal whole-line target inequality

`boxed:
 ||p_(Q_N)||_infinity
 <= K_HP / sqrt(2 sqrt(N/(N-1)))
 = [K_HP/sqrt(2)] ((N-1)/N)^(1/4)
 < K_HP/sqrt(2).`

Here `K_HP` is the explicit universal combination of the Hu--Paouris source constants recorded in auto19; the primary paper does not optimize those constants, so no unsupported numerical value is assigned.

The pinned `e5f71d79...` D5 theorem was already applied in the main report to the same physical cross cut. Since

`Z_5=binom(N,5)/(N-1)^5 >= 1/1280`,

it gives

`||p_(Q_N)||_infinity < 23.843`.

Thus the actual newest-partner/pinned-source splice on this genuine owner-target family is

`boxed:
 ||p_(Q_N)||_infinity
 <= min{ [K_HP/sqrt(2)] ((N-1)/N)^(1/4), 23.843 }.`

This is a proof-certificate comparison, not a statement about the extremal density.

## 3. Why the fleet02 theorem is not superseded

Auto19's strongest private-square theorem is aggregate in the bilinear block: it spends the full `||M||_HS` and gives a bound proportional to `(|a| ||M||_HS)^(-1/2)`. This is stronger than the fleet02 rank-one-tail currency when the retained form is literally

`X^T M Y + aW^2 + dW + c`.

The fleet02 theorem proved in the main report has a different retention advantage. It allows

`X^T M Y + alpha^T X + G(Y) + aW^2 + h(Y)W + c`,

with **arbitrary same-bank curvature/function `G(Y)`** and an **arbitrary Y-dependent aligned square shift `h(Y)`**, while preserving original-source independence by conditioning on `Y`. It pays this larger retained class by `S_1(M)` through the source-valid Rudelson--Vershynin `(r,q)=(1,1/2)` fractional-tail estimate.

Therefore the two receivers are complementary:

- auto19: stronger aggregate `||M||_HS` currency for a cleaner bilinear-plus-private-square packet;
- fleet02: weaker `S_1(M)` currency but tolerates arbitrary `Y`-bank remainder and aligned `Y-W` coupling.

Neither controls the genuinely two-sided overlap where the private square coordinate also couples into the `X` bank, nor arbitrary unaligned curvature inside a would-be private bank.

## 4. Sharpened first unpaid implication

The first unpaid structural bridge should now be recorded as

`QFORM-TWOSIDED-OVERLAP-OR-AGGREGATE-HS-EXIT-v1`:

from bare `s_3(A)>=1`, force at universal scale at least one of

- a clean bilinear plus genuinely private square packet paid by auto19's Hilbert--Schmidt theorem;
- the larger one-sided retained packet `A_II=A_Iw=0`, `|A_ww|S_1(A_IJ)>=c`, paid by the fleet02 fractional-tail theorem even with arbitrary `J-J` curvature and aligned `J-w` coupling;
- an aggregate Theorem-F / projected-crossing / D5 / grouped-hub / physical-pair exit.

The harmonic-frame proposition in the main report rules out strengthening this to “find a sparse/private exact spectral eigenvector”: in that exact target family every nonzero spectral direction has support at least `n-2`, while pinned Theorem F pays the entire family by `12`.

All small nonzero residual coefficients remain retained; no post-rotation independence or perturbative deletion is used.
