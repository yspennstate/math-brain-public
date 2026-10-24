SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B14, 2026-09-24T09:15:28Z.
attacking: anchor-convolution localization — retain one source-disjoint cap-controlled scalar in each active bank so arbitrary positive localization of the remaining translation bank automatically has mass-proportional unnormalised cap before applying the completed account02/B14 reflection compiler.

# Anchor-convolution localization for active translation banks

Run: `20260924T091528Z-account01-B14-QFORM-auto11`

Status: `NEW SUPPORTING LOCALIZATION THEOREM / TARGET-LEVEL REFLECTION CHAMBER / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`.

## 1. Scope and source discipline

The target remains the unrestricted statement: independent real original coordinates with probability densities at most one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and a universal essential density bound for `X^T A X`. No moment, bounded-support, connected-support, finite-fragment, log-concavity, or post-rotation independence assumption is introduced.

The newest completed designated-partner result used below is account02/B14
`QFORM-REFLECTION-AFFINE-SUBMEASURE-COMPILER-v1`, run
`20260924T090749Z-account02-B14-QFORM-auto11`, canonical report

`yspennstate/math-open-problems@cd7154f14613325003b6346235701b8f067856a1`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B14/20260924T090749Z-account02-B14-QFORM-auto11/REPORT.md`.

Write

`B_* = I_3 - (2/3) 1 1^T`,

so `spec(B_*)={1,1,-1}` and `B_*^2=I`. The partner theorem says: if `S_1,S_2,S_3` are independent probability variables with scalar density caps at most `K`, and `tau` is any finite positive parameter measure of mass `m`, then for arbitrary measurable affine fields `b(omega),c(omega)`, the positive output measure

`eta(E)=int P(S^T B_* S+b(omega)^T S+c(omega) in E) tau(domega)`

has

`||d eta/dt||_infinity <= 6 sqrt(pi) K^2 m`.                 (1.1)

The full QFORM conjecture is still open. The point of this run is to turn (1.1), which is directly zero-tax for an *outside* parameter, into a zero-tax theorem for a large class of genuinely *active* localizations.

Relevant live corrections retained: uniform pointwise quadratic Fourier decay is false; bounded-diameter and fixed-fragment localization are false; a uniformly good physical triple need not exist; post-rotation coordinates are not independent; and mixed-norm/fibre absoluteization is not used.

## 2. One-dimensional anchor-convolution lemma

### Lemma 2.1 — `QFORM-ANCHOR-CONVOLUTION-MASS-CAP-v1`

Let `A` be a real random variable with probability density `g` satisfying

`0 <= g <= K`.

Let `T` be an arbitrary independent random element on a measurable space `(Omega,mu)`, and let `s:Omega->R` be measurable. No density, support, diameter, tail, or moment assumption is imposed on `s(T)`.

Let `(q_j)_{j in J}` be any finite or countable soft positive localization of the `T`-law:

`0 <= q_j(omega) <= 1`,   `sum_j q_j(omega)=1` for `mu`-a.e. `omega`.

Define

`m_j = int q_j dmu`

and let `rho_j(x) dx` be the unnormalised law of `A+s(T)` carrying weight `q_j(T)`. Then

`rho_j(x) = int q_j(omega) g(x-s(omega)) mu(domega)`,       (2.1)

and therefore

`int rho_j = m_j`,

`boxed: ||rho_j||_infinity <= K m_j.`                       (2.2)

For every positive-mass piece, the normalized conditional density `rho_j/m_j` consequently has cap at most `K`, independently of the location or geometry of the piece.

#### Proof

Equation (2.1) follows from independence and Tonelli. Since `g(x-s(omega))<=K` pointwise,

`rho_j(x) <= K int q_j dmu = K m_j`

for every `x`; integration in `x` gives mass `m_j`. No other property of `s(T)` is used. QED.

### Remarks

1. The localization may be deterministic (`q_j=1_{E_j}`) or randomized/soft.
2. The pieces may be arbitrarily distant and countably many.
3. `s(T)` and the anchor itself may have unbounded support and no finite moments.
4. Arbitrary deterministic translations of each piece are invisible to (2.2).
5. The key provenance condition is source disjointness: the localization label may inspect the translation bank, but it must leave the anchor source unconditioned. If the label also localizes the anchor, (2.2) need not hold; this is exactly consistent with the partner's sharp active-cell barrier.

Thus one untouched cap-controlled source converts arbitrary localization of an additive translation bank into the mass-proportional cap condition needed by the positive active-cell compiler.

## 3. Three-bank zero-tax theorem

### Theorem 3.1 — `QFORM-THREE-ANCHOR-ACTIVE-LOCALIZATION-v1`

For `r=1,2,3`, let `A_r` be independent real probability variables with density caps at most `K`. Let `T_r` be arbitrary mutually independent translation-bank random elements, independent of all anchors, and let `s_r(T_r)` be arbitrary measurable real outputs. Put

`S_r=A_r+s_r(T_r)`.

Allow an independent outside environment `W`. For arbitrary measurable `b(W) in R^3` and `c(W) in R`, define

`Q = S^T B_* S + b(W)^T S + c(W)`.                         (3.1)

For each translation bank choose an arbitrary finite/countable soft positive localization `(q_{rj})_j`. Also allow an arbitrary finite/countable positive localization of the outside environment.

Then every active/outside product cell is mass-linear, and after summing all cells the original law obeys

`boxed: ||p_Q||_infinity <= 6 sqrt(pi) K^2.`                (3.2)

The constant is exactly the same partner constant as before any translation-bank localization.

#### Proof

For bank `r` and piece `j`, Lemma 2.1 gives an unnormalised scalar density `rho_{rj}` of mass `m_{rj}` and height at most `K m_{rj}`. Hence, after normalization, each positive-mass cell variable has density cap at most `K`.

Fix a triple cell `alpha=(j_1,j_2,j_3)` and an outside positive piece `tau_k` of mass `n_k`. Conditional on this active cell, the three normalized scalar variables remain independent because the underlying source banks are disjoint. Apply the completed account02/B14 theorem (1.1) to the normalized cell variables and the outside measure `tau_k`. It gives normalized output height at most

`6 sqrt(pi) K^2 n_k`.

Restoring the active cell mass

`m_alpha=product_r m_{rj_r}`

gives the unnormalised inequality

`boxed: ||p_{alpha,k}^{sub}||_infinity
        <= 6 sqrt(pi) K^2 m_alpha n_k.`                     (3.3)

Now sum positive output measures. Since

`sum_alpha m_alpha = product_r sum_j m_{rj}=1`

and `sum_k n_k=1`,

`sum_{alpha,k} 6 sqrt(pi)K^2 m_alpha n_k = 6 sqrt(pi)K^2`.

This proves (3.2). QED.

### What this buys over generic active fragmentation

The partner's generic tiny-cell obstruction shows that ordinary spatial localization of all three active laws can have submeasure height of order the cube side rather than the cube mass; cellwise reciprocal-curvature payment is then not mass-linear. Theorem 3.1 identifies a concrete exception: if each active scalar retains one untouched convolution anchor, then *any* localization of the remaining additive bank automatically has exactly the correct mass homogeneity. No bounded-diameter or finite-fragment surrogate is needed.

## 4. Exact-target quadratic-form chamber

The preceding theorem is not merely an abstract mixture statement. It produces a genuine rotated, off-diagonal, indefinite family inside the exact owner target.

Partition a finite set of original independent coordinates into three disjoint active groups and an outside set. In active group `r`, single out one anchor coordinate `X_{r0}` and write the remaining vector as `Z_r`. Assume only the owner hypothesis that every original coordinate has density at most one. Fix arbitrary finite coefficient vectors `a_r` and set

`S_r = X_{r0} + a_r^T Z_r`.                                (4.1)

Because the anchor is independent of the translation bank, convolution gives

`||p_{S_r}||_infinity <= 1`.                               (4.2)

Let `Z` denote the outside original-coordinate vector, let `C` be any compatible real matrix, and let `D` be any real symmetric matrix. Consider the original-coordinate quadratic form

`Q = S^T B_* S + 2 S^T C Z + Z^T D Z`.                    (4.3)

Conditioning on `Z=z` gives exactly the partner form

`S^T B_* S + (2Cz)^T S + z^T D z`.

Thus Theorem 3.1 (or directly the partner theorem with `K=1`) gives

`boxed: ||p_Q||_infinity <= 6 sqrt(pi)
       = 10.634723105433096... .`                           (4.4)

This estimate is uniform in every coefficient vector `a_r`, every `C,D`, every source translation, every support geometry, and all tails/moments.

### 4.1 Verification of the exact three-large-eigenvalue hypothesis

Let

`e_r=(1,a_r)`

be the coefficient vector of `S_r` inside its disjoint active group and put

`d_r=||e_r||_2=sqrt(1+||a_r||_2^2) >= 1`.

The normalized vectors `u_r=e_r/d_r` are orthonormal because their physical supports are disjoint. Let

`Delta=diag(d_1,d_2,d_3)`.

The compression of the full original matrix of (4.3) to `span{u_1,u_2,u_3}` is

`H = Delta B_* Delta
   = Delta^2 - (2/3) d d^T`,                               (4.5)

where `d=(d_1,d_2,d_3)^T`.

For every `x` in the two-dimensional subspace `d^perp`,

`x^T H x = sum_r d_r^2 x_r^2 >= ||x||_2^2`.               (4.6)

By Courant--Fischer, the second largest eigenvalue of `H` is at least one, hence `H` has two eigenvalues `>=1`.

For the vector

`x=Delta^{-1} 1`,

we have

`x^T H x = 1^T B_* 1 = -3`,

while

`||x||_2^2 = sum_r d_r^{-2} <= 3`.

Therefore the Rayleigh quotient is at most `-1`, so the least eigenvalue of `H` is at most `-1`. Thus the three-dimensional compression itself has two eigenvalues `>=1` and one `<=-1`.

Poincare separation / the min-max principle transfers these signed threshold counts to the full original matrix in (4.3), regardless of the arbitrary cross block `C` and outside block `D`. Hence every form (4.3) satisfies the owner's exact spectral hypothesis.

This verification is important: the result is not a diagonal theorem and does not assert independence after an arbitrary spectral rotation. Independence is used only for the three disjoint original-coordinate groups before their scalar bank compression.

## 5. Simultaneous arbitrary active translation localization

Now localize each `Z_r` bank by an arbitrary finite/countable soft label depending on the entire bank. The scalar pushforward `a_r^T Z_r` may have a wildly disconnected or unbounded conditional law, and the label may select pieces separated by arbitrarily large distances. Lemma 2.1 gives, for every unnormalised piece of mass `m`,

`||rho_piece||_infinity <= m`,                              (5.1)

because the untouched anchor `X_{r0}` has cap one.

Applying the newest account02/B14 theorem cellwise gives the *actual* inequality

`||p_{alpha,k}^{sub}||_infinity
 <= 6 sqrt(pi) (product_r m_{rj_r}) n_k`,                   (5.2)

for every simultaneous active triple cell and every outside positive piece. Summing (5.2) returns exactly (4.4). Therefore arbitrary active translations, distant fragments, countably many fragments, unbounded supports and absent moments cost **zero** in this chamber.

The same proof works if the translation-bank pieces are shifted by additional arbitrary deterministic amounts, since convolution height is translation invariant. A common independent random shift is also free after conditioning because it creates only an affine field, already covered by the designated partner theorem.

## 6. Remote-comb stress test

For a concrete no-moment example, take each anchor `X_{r0}` uniform on `[0,1]`. Let one translation coordinate `T_r` have the cap-one density

`h(t)=sum_{j>=1} 1_[j^3, j^3+m_j](t)`,

where

`m_j=6/(pi^2 j^2)`

so `sum_j m_j=1`. This distribution has unbounded support and no finite first absolute moment. Localize by the individual remote teeth. On tooth `j`, the unnormalised law of `X_{r0}+T_r` is a convolution of the unit-cap anchor with a subprobability of mass `m_j`, so its cap is at most `m_j`, not one.

For three such independent banks, a product tooth `(j_1,j_2,j_3)` therefore costs at most

`6 sqrt(pi) m_{j_1}m_{j_2}m_{j_3}`

under (5.2), and summing all countably many teeth gives exactly `6sqrt(pi)`. This is the opposite of the generic fragment-first comb in the partner report, whose cap-weighted reciprocal certificate can diverge. The untouched anchor is precisely what converts tooth mass into tooth height.

## 7. Exact remaining gap

This does not solve the unrestricted QFORM theorem. A general matrix with `s_3(A)>=1` need not admit three source-disjoint active scalar factors each containing an untouched cap-controlled anchor with all remaining same-bank curvature entering additively as a translation. In particular, arbitrary same-bank quadratic curvature and orthogonal cross leakage cannot be deleted for rough unbounded inputs.

The first unpaid structural implication is therefore:

`QFORM-THREE-ANCHOR-FACTOR-OR-WHOLE-ACTIVE-EXIT-v1`:

> From bare `s_3(A)>=1`, either expose a product-preserving three-bank core in which each paid scalar keeps one source-disjoint cap-controlled anchor and all localized bank dependence enters additively/affinely, or force one of the already proved whole-active ridge, grouped-bank, projected-crossing, pair, Schur, hub or receiver exits before spatial active normalization.

The mathematical advance here is localized and exact: once an additive source-disjoint anchor exists, arbitrary translation-bank localization is no longer an obstruction at all; the completed partner constant is preserved cell-by-cell with exact mass homogeneity.

Full QFORM: `OPEN`. Continuity of the full target: separate/open. Execution label for this run: `WITHOUT_VERIFIED_BRAIN`.
