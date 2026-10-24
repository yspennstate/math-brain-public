# account01/B16 supplement — three-source-bank nonlinear compiler

Status: **NEW SUPPORTING THEOREM + TARGET-FRAME APPLICATION; FULL QFORM OPEN.**

Programme: `QFORM-DENSITY-3EIG-20260922`. This supplement belongs to run `account01-B16-20260923T180525Z-auto11` and preserves the live correction that flat projected-density caps alone do not control curved quadratic pushforwards. The positive result below uses the projection theorem only to produce genuinely independent scalar receivers from disjoint ORIGINAL source banks, and then applies a nonlinear three-variable quadratic theorem before averaging the conditioned coordinates.

Source pins actually used:

- designated partner account02/B16: `yspennstate/math-open-problems@c8258480a0bfb67e9b128e67c477c5c5dcdd38e8`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/account02-B16-20260923T163017Z-auto11b/REPORT.md`; in its true-near-coloop exact-rank-three scope with nonzero hub pivot it proves
  `||p_Q||_infinity <= 13.0639452949/sqrt(|A_00|)`;
- actual bounded-density projection theorem: `yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`; a normalized one-dimensional projection of independent cap-one coordinates has density cap at most `sqrt(2)`;
- nonlinear receiver: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem A; for three genuinely independent cap-one scalar variables and a symmetric `3 x 3` quadratic matrix whose eigenvalues all have modulus at least `sigma`, arbitrary affine terms included, the output density is at most `6 sqrt(pi)/sigma`.

## 1. Three-source-bank conditioning compiler

### `QFORM-THREE-SOURCE-BANK-CONDITIONING-COMPILER-v1`

Let the original independent coordinates be partitioned into four disjoint sets

`I_0 disjoint_union I_1 disjoint_union I_2 disjoint_union K`.

For `j=0,1,2`, let

`Z_j = a_j^T X_{I_j}`

be scalar random variables with density bounds

`||p_{Z_j}||_infinity <= K_j < infinity`.

Assume that after conditioning on `X_K`, the three-dimensional spectral coordinate entering the quadratic form has the affine representation

`Y = p_0 Z_0 + p_1 Z_1 + p_2 Z_2 + y_K`,

where `p_j in R^3`, `y_K` is deterministic under the conditioning, and the spectral quadratic core is a real symmetric `3 x 3` matrix `Lambda` satisfying

`sigma_min(Lambda) >= 1`.

Define

`P_K = [p_0/K_0, p_1/K_1, p_2/K_2]`.

If

`sigma_min(P_K) >= rho > 0`,

then the full quadratic output, with all affine terms induced by the conditioned variables retained, satisfies

`boxed: ||p_Q||_infinity <= 6 sqrt(pi) rho^(-2).`                 (1.1)

No independence among coordinates of any multidimensional projection is asserted. Independence is used only for the three scalar variables `Z_0,Z_1,Z_2`, and that independence is genuine because their ORIGINAL source banks are disjoint.

### Proof

Set

`W_j = K_j Z_j`.

Then

`p_{W_j}(w) = K_j^(-1) p_{Z_j}(w/K_j) <= 1`,

and `W_0,W_1,W_2` are independent. Conditional on `X_K`, write `W=(W_0,W_1,W_2)^T`. The spectral vector is

`Y = P_K W + y_K`.

Hence the conditional quadratic polynomial in the active variables is

`Q = W^T B W + ell_K^T W + c_K`,

where

`B = P_K^T Lambda P_K`.

Since all three factors are square and `P_K` is invertible,

`sigma_min(B)
 >= sigma_min(P_K^T) sigma_min(Lambda) sigma_min(P_K)
 >= rho^2`.                                                       (1.2)

Because `B` is symmetric, every eigenvalue of `B` has modulus at least `rho^2`. The pinned nonlinear three-variable Theorem A therefore gives, uniformly in the conditioned value of `X_K`,

`||p_(Q | X_K)||_infinity <= 6 sqrt(pi)/rho^2`.

Averaging the conditional laws cannot enlarge the same pointwise density bound, proving (1.1). QED.

This statement is deliberately stronger than a use of a bounded joint projection density: the scalar projection caps are first attached to three disjoint ORIGINAL source banks, and the entire curved quadratic pushforward is then paid by the three-independent-variable receiver.

## 2. Universal spectral-core bound for the partner Walsh frame

The newest account02/B16 report uses the true-near-coloop Parseval frame

`r_0=(sqrt(c),0,0)`, `c=1-delta`,

`r_j=m^(-1/2)(sqrt(delta), sigma_j, tau_j)`,

where `0<=delta<=1/64`, `m` is divisible by four, and each of the four sign pairs `(sigma_j,tau_j) in {+1,-1}^2` occurs exactly `m/4` times. The partner specialized one spectral core to expose the near-null square-envelope barrier. Here keep the SAME physical frame but allow **an arbitrary real symmetric spectral core** `Lambda` with

`min_i |lambda_i(Lambda)| >= 1`.                                  (2.1)

Thus

`A=R Lambda R^T`

is an exact-rank-three member of the full spectral target for every such `Lambda`.

Condition on the two original sign classes `B_{-+}` and `B_{--}`. On the two active classes put

`Z_+ = (2/sqrt(m)) sum_(j in B_{++}) X_j`,
`Z_- = (2/sqrt(m)) sum_(j in B_{+-}) X_j`.                         (2.2)

Both coefficient vectors in (2.2) have Euclidean norm one. The actual one-dimensional product-projection theorem therefore gives

`||p_{Z_+}||_infinity, ||p_{Z_-}||_infinity <= sqrt(2)`.            (2.3)

The three active scalar variables `X_0,Z_+,Z_-` are independent because their ORIGINAL coordinate sets are disjoint. Put

`W_+=sqrt(2) Z_+`, `W_-=sqrt(2) Z_-`.

Then each of `X_0,W_+,W_-` has density at most one. Their spectral coefficient matrix is

`P = [[sqrt(c), sqrt(delta)/(2sqrt(2)), sqrt(delta)/(2sqrt(2))],
      [0,       1/(2sqrt(2)),          1/(2sqrt(2))],
      [0,       1/(2sqrt(2)),         -1/(2sqrt(2))]]`.             (2.4)

A direct multiplication gives

`P P^T = [[1-3delta/4, sqrt(delta)/4, 0],
           [sqrt(delta)/4, 1/4,       0],
           [0,             0,          1/4]].`                     (2.5)

Set

`q=127/512`.

The third eigenvalue in (2.5) is `1/4>q`. For the leading `2 x 2` block, the lower-right diagonal after subtracting `qI` is `1/512`, while

`det( [leading block] - q I )
 = 385/262144 - (16768/262144) delta
 >= (385-262)/262144
 = 123/262144 >0`                                                   (2.6)

because `delta<=1/64`. The other diagonal is positive as well. Hence

`P P^T >= (127/512) I_3`,

so

`sigma_min(P)^2 >= 127/512`.                                       (2.7)

Apply the compiler with `rho^2=127/512`. Since (2.1) gives `sigma_min(Lambda)>=1`, every conditioned active quadratic matrix `P^T Lambda P` has all eigenvalues of modulus at least `127/512`. Consequently

`boxed:
 ||p_(X^T A X)||_infinity
 <= (3072 sqrt(pi))/127
 = 42.8738443306... <43.`                                           (2.8)

This bound holds for **every** spectral core `Lambda` satisfying (2.1), every balanced Walsh-frame size, every `0<=delta<=1/64`, and every collection of independent cap-one original source laws. It is not restricted to the partner's special near-null matrix `Lambda_epsilon`.

Thus the earlier `<43` estimate for one hard collar is promoted to a universal bound for the entire spectral-core family carried by this physical Walsh frame.

## 3. Actual application of the newest account02/B16 Schur theorem

For the same arbitrary core write

`alpha = e_1^T Lambda e_1`.

The physical hub pivot is

`A_00 = c alpha`.                                                   (3.1)

Whenever `alpha !=0`, the completed newest account02/B16 theorem at commit `c8258480...` applies to this same true-near-coloop frame and gives

`||p_Q||_infinity <= 13.0639452949 / sqrt(c |alpha|).`              (3.2)

Combining the partner inequality (3.2) with the new source-bank compiler bound (2.8) gives the concrete all-core interpolation

`boxed:
 ||p_Q||_infinity
 <= min{3072 sqrt(pi)/127,
        13.0639452949 / sqrt(c |alpha|)}`                           (3.3)

for `alpha!=0`, while (2.8) remains valid at the exact null pivot `alpha=0`.

In particular, the bank receiver is uniform through the null pivot, whereas the Schur certificate becomes sharper when the physical pivot is quantitatively non-small. This is exactly the complementary behavior needed at the projection-product interface, and no translation-uniform square envelope is introduced.

## 4. Remaining implication

The result does **not** prove the unrestricted theorem because an arbitrary true-near-coloop frame need not have four repeated Walsh source directions. The remaining structural problem can now be stated cleanly:

`QFORM-GENERAL-NEARCOLOOP-THREE-SOURCE-FRAME-EXTRACTION-v1`:

from an arbitrary surviving near-coloop rank-three frame, either extract three disjoint original source banks whose active scalar factorization has a rescaled spectral coefficient matrix `P_K` with `sigma_min(P_K)>=rho_0>0`, or trigger one of the already proved projected-crossing/source-plane exits, or prove the source-adapted hub estimate for the residual rough-law endpoint.

The compiler above shows that any uniform `rho_0` would immediately give the full nonlinear density estimate `6 sqrt(pi) rho_0^(-2)` on that branch. What remains is the source-preserving structural extraction, not an additional arbitrary-joint coarea estimate.

Full unrestricted QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**. Continuity is not newly claimed here.
