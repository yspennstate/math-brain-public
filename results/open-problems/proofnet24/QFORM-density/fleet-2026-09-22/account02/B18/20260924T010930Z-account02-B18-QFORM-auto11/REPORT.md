# account02/B18 — zero-self-bank complement-norm funnel

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T010930Z-account02-B18-QFORM-auto11`  
**Role:** literature-to-proof transfer / complementary constructions and source-valid counterexamples  
**Status:** `NEW SUPPORTING TARGET-LEVEL THEOREM / DESIGNATED PARTNER APPLIED / PINNED e5f RESULT APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B18, 2026-09-24T01:09:30Z.
attacking: a zero-self-bank spectral funnel—combine the newest account03/B18 two-singular-direction negative-moment theorem with the pinned e5f cross-volume theorem, and quantify when the full three-large-eigenvalue hypothesis forces the paid cross branch.

## 1. Exact target and correction discipline

The owner target remains the unrestricted one: independent real coordinates with probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moments, compact support, log-concavity, iid hypothesis, smoothness, centering, diagonal-basis independence, or independence after rotation is added here. Continuity is kept separate.

The live correction inbox was consumed before publication. In particular this argument does not use arbitrary-joint coarea, worst conditional-density caps, a uniformly good fixed minor, pointwise law-uniform stationary phase, or perturbative deletion of a small quadratic term on unbounded inputs. The source search outcome is not treated as novelty evidence.

## 2. Designated partner theorem actually used

The newest completed compatible designated-partner result is account03/B18,

`QFORM-ONE-SIDED-CROSS-NEGATIVE-MOMENT-v1`,

at `yspennstate/math-open-problems@a2cf029c5c935d6eadf4216c073911fc8dc404ac`, with deterministic checks at `e08f224d39db493918d786f25de6046c9cf0202a`.

Its ambient quadratic corollary is the exact input used below. Split the ORIGINAL coordinates into disjoint banks `I,J,K`. If

`A_II=0`

and `B=A_IJ` has two largest singular values `beta_1>=beta_2>0`, then, after conditioning only on the original `K` coordinates, the full ambient form has

`||p_Q||_infinity <= 2 sqrt(pi) (beta_1 beta_2)^(-1/2)`.      (2.1)

Arbitrary curvature on the opposite bank and arbitrary outside couplings are retained. No rotated-coordinate independence is asserted.

The proof source uses only a genuine product-marginal theorem plus a radial negative-moment bathtub inequality. I independently checked the primary theorem actually needed: Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1. For a product probability density `f=prod_i f_i` and a `k`-dimensional orthogonal marginal,

`||pi_E f||_infinity <= min((n/(n-k))^((n-k)/2), 2^(k/2)) prod_i ||f_i||_infinity^(gamma_i)`,

for `gamma_i in [0,1]`, `sum gamma_i=k`. Therefore cap-one inputs give `||pi_E f||_infinity<=2^(k/2)`. There is no moment, support, log-concavity, iid, centering, symmetry, or smoothness assumption. The theorem bounds a JOINT marginal density; it does not make the projected coordinates independent. When `k=n`, the original product density itself has cap one, so no extrapolation of the theorem beyond its stated `k<n` range is needed.

## 3. New deterministic funnel

### Theorem `QFORM-ZEROSELF-COMPLEMENT-NORM-FUNNEL-v1`

Let the ORIGINAL coordinates split as `I disjoint J`, and write

`A = [[0,B],[B^T,C]]`,                                      (3.1)

with `A` real symmetric. Let

`s = s_3(A)`

be the third largest singular value of `A` (equivalently the third largest absolute eigenvalue), let

`c = ||C||_op`,

and let `beta_2` be the second singular value of `B` (zero if `rank B<2`). If `c<s`, then

`beta_2^2 >= s(s-c)`.                                      (3.2)

Consequently, for arbitrary independent cap-one inputs (and even after arbitrary affine terms are added),

`||p_{X^T A X}||_infinity <= 2 sqrt(pi) / sqrt(s(s-c))`.    (3.3)

At the owner normalization `s_3(A)>=1`, every exact zero-self-bank state with `||C||_op<1` obeys

`||p_Q||_infinity <= 2 sqrt(pi) / sqrt(1-||C||_op)`.        (3.4)

In particular,

`||C||_op <= 1/2  ==>  ||p_Q||_infinity <= 2 sqrt(2 pi) = 5.013256549262...`.    (3.5)

The pure bipartite case `C=0` gives the sharper scale-covariant bound

`||p_Q||_infinity <= 2 sqrt(pi)/s_3(A)`.                    (3.6)

No continuity claim is made by this theorem.

### Proof of (3.2)

Let `B_1` be a best rank-one approximation to `B`, so by the singular-value approximation formula

`||B-B_1||_op = beta_2`.

Put `E=B-B_1` and

`R = [[0,B_1],[B_1^T,0]]`.

Then `rank R<=2`. Since the third singular value is the best operator-norm error of a rank-at-most-two approximation,

`s_3(A) <= ||A-R||_op`.                                    (3.7)

Now

`A-R = H = [[0,E],[E^T,C]]`.

For a unit vector `(x,y)`, put `a=||x||`, `b=||y||`; then `a^2+b^2=1`, and

`| <(x,y),H(x,y)> |
 <= 2 beta_2 a b + c b^2`.                                  (3.8)

The maximum of the right side over `a^2+b^2=1` is the larger eigenvalue of

`[[0,beta_2],[beta_2,c]]`,

namely

`(c + sqrt(c^2+4 beta_2^2))/2`.                             (3.9)

Because `H` is symmetric, (3.8)--(3.9) give

`||H||_op <= (c + sqrt(c^2+4 beta_2^2))/2`.                 (3.10)

Combining (3.7) and (3.10),

`s <= (c + sqrt(c^2+4 beta_2^2))/2`.

When `c<s`, `2s-c>0`; squaring after rearrangement gives

`4s^2-4sc <= 4 beta_2^2`,

which is (3.2). QED.

### Density implication

Equation (3.2) implies `beta_1 beta_2 >= beta_2^2 >= s(s-c)`. Apply the designated-partner bound (2.1), with `J` the full complement of `I`, to obtain (3.3). If `s>=1` and `c<1`, then `s(s-c)>=1-c`, giving (3.4).

This is a genuinely spectral-to-source-preserving implication: the spectral hypothesis forces a two-dimensional ORIGINAL cross bank only when the complementary self-curvature is separated below the third singular scale.

## 4. The funnel is quantitatively sharp

Fix `s>0` and `0<=c<s`, and set

`beta = sqrt(s(s-c))`,

`U = (1/sqrt(2)) [ I_3 ; I_3 ]`, a `6 x 3` isometry,

`B = beta U`, `C = c I_3`,

and

`A_{s,c} = [[0_{6x6}, B],[B^T,C]]`.                         (4.1)

Since `U^T U=I_3`, the nonzero spectral problem is three copies of

`[[0,beta],[beta,c]]`.

Its two eigenvalues are exactly

`s` and `c-s=-(s-c)`,

because `beta^2=s(s-c)`. Hence

`spec(A_{s,c}) = {s,s,s, -(s-c),-(s-c),-(s-c), 0,0,0}`.     (4.2)

For `0<c<s`, this family has exactly three eigenvalues of modulus at least `s`; moreover

`||C||_op=c`, `beta_2(B)=sqrt(s(s-c))`,

so equality holds in (3.2). Thus the deterministic currency `s(s-c)` cannot be improved using only `s_3(A)` and `||C||_op`.

At `s=1,c=1/2`, the exact target spectrum is

`{1,1,1,-1/2,-1/2,-1/2,0,0,0}`,

and (3.3) gives

`||p_Q||_infinity <= 2 sqrt(2 pi) = 5.013256549262...`.      (4.3)

## 5. Required pinned e5f result spent on the same genuine target family

I read the pinned source exactly at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,
`FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Apply its completed **Theorem D** to (4.1). The cross block is `M=B`. Since

`B^T B = beta^2 I_3`,

`Z=e_3(B^T B)=beta^6`.                                     (5.1)

The cross block has exact rank three. Its left singular frame is `U`, and every one of its six row leverages is exactly `1/2`; for exact rank three, the pinned report identifies these leverages with the volume-sampling row marginals `alpha_i`. Thus Theorem D applies at its literal threshold and gives the whole-line target inequality

`||p_Q||_infinity <= 6 sqrt(e) Z^(-1/6)
                    = 6 sqrt(e)/beta
                    = 6 sqrt(e)/sqrt(s(s-c))`.              (5.2)

At `s=1,c=1/2`,

`||p_Q||_infinity <= 6 sqrt(2e) = 13.989863889583...`.       (5.3)

The designated-partner theorem improves the certificate on this family to (4.3), but both are valid source-preserving whole-line bounds. This is an actual application of a completed pinned theorem, not a search-based novelty claim.

The same pinned `COUNTEREXAMPLE_SEARCH.md` reports no valid QFORM counterexample; I do not use that search miss as evidence of truth or novelty.

## 6. Why the complement-norm hypothesis is necessary

No positive lower bound on `beta_2(B)` follows from `s_3(A)>=1` and `A_II=0` alone. The literal original-coordinate matrix

`A_* = [[0,1,0],[1,0,0],[0,0,1]]`                           (6.1)

has spectrum `{-1,1,1}`. Taking `I={1}` and `J={2,3}` gives `A_II=0`, but `B=[1,0]` has `beta_2=0`, while `||C||_op=1=s_3(A_*)`. Thus the boundary `c=s` is a real structural obstruction to forcing the two-cross-direction receiver.

The pinned e5f ruled-level-set theorem (Theorem C in `COUNTEREXAMPLE_SEARCH.md`) nevertheless applies to this exact rank-three signature and gives the real one-sided inequality

`p_{X^T A_* X}(t) <= pi sqrt(2)` for a.e. `t>=0`.            (6.2)

This source-valid example shows precisely what the new funnel does and does not do: once the two-cross branch collapses, a full target-scale curvature direction can sit in the complementary bank. One must then spend that curvature through another product-preserving receiver; it cannot be manufactured as a second cross singular direction.

## 7. First unpaid implication after this run

Rearranging (3.2) gives the stronger collar statement

`||C||_op >= s - beta_2(B)^2/s`.                            (7.1)

Thus in an owner-normalized zero-self-bank state, if the new two-cross certificate is expensive because `beta_2(B)<=epsilon`, the complementary block must satisfy

`||C||_op >= 1-epsilon^2`.                                  (7.2)

The next unpaid implication is therefore:

`QFORM-ZEROSELF-NEARRANK1-UNITCOMPLEMENT-BRIDGE-v1` — when an exact original-coordinate zero-self bank has almost rank-one cross coupling and the complementary block consequently carries an almost-unit spectral direction, transfer that complement curvature into an already-paid cross-plus-square / hub / ridge / grouped-bank receiver without rotating the source law or discarding the residual same-bank curvature.

The 3x3 matrix (6.1) is the model endpoint: rank-one cross plus one unit complement square. The obstruction in the general case is that the complement's near-unit eigenvector need not be an original coordinate and its residual curvature cannot be deleted under arbitrary unbounded cap-one laws.

## 8. Scope and source audit

- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- New theorem: proved supporting target-level branch, exact original-coordinate hypotheses.
- Partner used: account03/B18 `QFORM-ONE-SIDED-CROSS-NEGATIVE-MOMENT-v1`, source commit `a2cf029c5c935d6eadf4216c073911fc8dc404ac`, checks `e08f224d39db493918d786f25de6046c9cf0202a`.
- Primary external theorem actually needed: Livshyts--Paouris--Pivovarov, arXiv:1507.07949, Theorem 1.1, with exact product/cap hypotheses stated above.
- Pinned completed theorem actually applied: e5f Theorem D to (4.1), plus Theorem C to (6.1).
- No continuity claim from the new argument.
- No post-rotation independence, moment, support, log-concavity, iid, or smoothing hypothesis.
