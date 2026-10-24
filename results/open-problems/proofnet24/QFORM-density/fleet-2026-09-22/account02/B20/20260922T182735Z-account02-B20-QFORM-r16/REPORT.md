# account02/B20 — rank-two cross-bank square-root concentration and the indispensable third spectral direction

**Run:** `20260922T182735Z-account02-B20-QFORM-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Proof closure and keeper / pathway SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_REPLACEMENT_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Exact target and source pins

The target remains the full statement: for every dimension `n`, every independent real vector `X=(X_1,...,X_n)` whose coordinate densities satisfy `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has a density with one universal finite essential-supremum bound, or give a valid counterexample. No moments, compactness, log-concavity, diagonal-basis independence, or independence after rotation are assumed.

The fresh control used at the start was `yspennstate/math-research-brain@fb48babff3d0a2b078a9df38923eb2f45bc3f3fa`, whose live OWNER CONTROL is revision `2026-09-22.11`. The pointwise-Fourier-decay, unrestricted-fiber-supremum, and post-rotation-independence corrections remain binding.

The designated partner result actually consumed is account03/B20, run `20260922T175041Z-account03-B20-QFORM-r14`, canonical mathematics

`yspennstate/math-open-problems@e0d5eb88a5c953ca0fce31b386a35e7faea8389e`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T175041Z-account03-B20-QFORM-r14/REPORT.md`.

Its half-barrier theorem says that, after the already-paid branch

`||A-diag A||_(second singular) <= 499/1000`, 

one reaches an original-coordinate cut with cross block `C` for which one of the following source-realizable packets occurs:

1. `s_2(C) >= 499/8000`; or
2. `s_1(C) > 1497/8000` plus a physical diagonal pivot at least `7501/16000`; or
3. `s_1(C) > 1497/8000` plus a nested original-coordinate cross bank with `s_1 > 7501/32000`.

The present run attacks packet 1 directly.

A second source used at an exact inequality is account02/B06, `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical report

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

It proves that if `R` has `k` orthonormal columns and `Z` has independent coordinate densities bounded by one, then `R^T Z` has a joint density bounded by `exp(k/2)`. I use the exact cases `k=1` (cap `sqrt(e)`) and `k=2` (cap `e`).

## 1. Main new theorem

### Theorem — `QFORM-RANK2-CROSS-SQRT-CONCENTRATION-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities at most one. Let `A` be any real symmetric matrix; no spectral assumption is needed in this theorem. Let `L,R` be disjoint sets of original physical coordinates and put

`C=A[L,R]`.

Assume

`s_2(C) >= beta > 0`.

Coordinates outside `L union R`, arbitrary quadratic self blocks `A[L,L]` and `A[R,R]`, arbitrary couplings to the outside coordinates, and arbitrary affine terms are all allowed.

Then for every interval `I` of length `h>0`,

`P(X^T A X in I) <= min(1, sqrt(2 e sqrt(pi)/beta) * h^(1/2)).`      (1.1)

Equivalently, the concentration function satisfies

`L_Q(h) <= sqrt(2 e sqrt(pi)/beta) h^(1/2)`.                          (1.2)

This is a source-valid, dimension-free estimate. It does not assert a density bound and it does not use an unrestricted fiber supremum, pointwise oscillatory decay, or independence after a rotation.

### Proof

Condition first on every coordinate outside `L union R`. Such conditioning preserves independence and the original density caps of the coordinates in `L` and `R`; the outside variables merely create affine terms and a constant. Thus it suffices to prove the estimate for a block form

`q(x,y)=F(x)+G(y)+2 x^T C y`,                                         (1.3)

where `x` and `y` are independent vectors with independent cap-one coordinates, while `F` and `G` are arbitrary quadratic-plus-affine functions on their respective blocks.

Fix an interval `I` of length `h`. For each `x`, set

`g(x)=P_y(q(x,y) in I)`.

Writing `p=P(q(X,Y) in I)` and applying Cauchy--Schwarz only once,

`p^2 <= E_X g(X)^2`                                                   (1.4)

and the right side is the probability, over independent `X,Y,Y'`, that both

`q(X,Y) in I`, `q(X,Y') in I`.                                       (1.5)

Whenever (1.5) occurs, subtraction cancels `F(X)` completely and gives

`G(Y)-G(Y') + 2 X^T C (Y-Y') in [-h,h]`.                             (1.6)

Now freeze `Y,Y'` and write `D=Y-Y'`. The random part of (1.6) is the original-coordinate linear form

`2 (C D)^T X`.                                                        (1.7)

By the `k=1` case of `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, every normalized linear form in independent cap-one coordinates has density at most `sqrt(e)`. Hence, if `C D !=0`, the density of (1.7) is at most

`sqrt(e)/(2 ||C D||_2)`.                                              (1.8)

Because the target interval in (1.6) has length `2h`, its conditional probability is at most

`sqrt(e) h / ||C D||_2`.                                              (1.9)

The same bound may be interpreted in the extended sense on the null set `C D=0`.

It remains to average the reciprocal slope without replacing it by a fiber supremum. Let `v_1,v_2` be orthonormal right singular vectors of `C` corresponding to its two largest singular values. Since both are at least `beta`,

`||C D||_2 >= beta ||Z||_2`,    `Z=(v_1^T D,v_2^T D)`.                (1.10)

Each coordinate of `D=Y-Y'` has density

`d_j(t)=int f_j(s) f_j(s-t) ds`

and therefore

`||d_j||_infinity <= ||f_j||_2^2 <= ||f_j||_infinity ||f_j||_1 <=1`. (1.11)

The coordinates of `D` are independent. Applying the `k=2` case of the same weighted affine-fiber theorem to the orthonormal pair `(v_1,v_2)`, the two-dimensional random vector `Z` has a joint density bounded by `e`.

For `s>0`, therefore,

`P(||Z||_2 < 1/s) <= min(1, pi e / s^2)`.                             (1.12)

Layer cake gives the exact elementary estimate

`E ||Z||_2^(-1)
 = int_0^infinity P(||Z||_2^(-1)>s) ds
 <= int_0^sqrt(pi e) 1 ds + int_sqrt(pi e)^infinity pi e s^(-2) ds
 = 2 sqrt(pi e)`.                                                     (1.13)

Combining (1.9)--(1.13),

`p^2 <= sqrt(e) h E ||C D||_2^(-1)
     <= sqrt(e) h beta^(-1) 2 sqrt(pi e)
     = (2 e sqrt(pi)/beta) h`.                                       (1.14)

Taking square roots proves (1.1). The bound is uniform in the previously conditioned outside coordinates, so averaging those coordinates completes the proof. `QED`

## 2. Exact application to the partner half-barrier packet

In account03/B20's first unresolved packet,

`beta=499/8000`.

Substituting this value in (1.1) gives the exact expression

`P(Q in I)
 <= min(1, sqrt(16000 e sqrt(pi)/499) * |I|^(1/2)).`                  (2.1)

Numerically,

`sqrt(16000 e sqrt(pi)/499) < 12.43`.                                (2.2)

Thus the entire `s_2(C)>=499/8000` packet has a uniform square-root concentration bound with arbitrary self blocks and arbitrary outside couplings. This is strictly stronger than merely extracting another cross singular vector or a large entry: it pays the whole source-realizable bank before reciprocal inversion.

It is not yet the desired density estimate. The remaining exponent gap is exactly from `h^(1/2)` to `h`.

## 3. A source-valid counterexample to a tempting but false free-bank step

The square-root estimate cannot simply be replaced by an `L^infinity` density theorem using only the hypothesis `s_2(C)>=beta` and arbitrary self blocks. The third spectral direction from the full target is genuinely necessary.

Take four independent `U[0,1]` variables `X_1,X_2,Y_1,Y_2` and define

`Q=(X_1-Y_1)(X_2-Y_2)`.                                              (3.1)

In physical coordinate order `(X_1,X_2,Y_1,Y_2)`, this is `Z^T A Z` with

`A = (1/2) * [[0, 1, 0,-1],
              [1, 0,-1, 0],
              [0,-1, 0, 1],
              [-1,0, 1, 0]]`.                                       (3.2)

For the cut `L={X_1,X_2}`, `R={Y_1,Y_2}`,

`C=(1/2) * [[0,-1],[-1,0]]`,                                        (3.3)

so

`s_1(C)=s_2(C)=1/2`.                                                  (3.4)

Nevertheless the density of `Q` is unbounded at zero. Indeed

`U=X_1-Y_1`, `V=X_2-Y_2`

are independent and each has triangular density

`g(u)=1-|u|`, `|u|<=1`.                                              (3.5)

For `0<t<1/4`, the product density obeys

`p_Q(t)=int g(u) g(t/u) du/|u|
      >= (1/4) int_(2t)^(1/2) du/u
      = (1/4) log(1/(4t)) -> infinity`.                              (3.6)

The eigenvalues of (3.2) are exactly `{1,-1,0,0}`. Thus this example is **not** a counterexample to the full QFORM target, because it has only two eigenvalues of modulus at least one. It does prove the following route-level no-go:

> A rank-two original-coordinate cross bank, even with `s_2(C)=1/2`, does not by itself force a bounded output density when arbitrary self blocks are retained.

Therefore any closure of partner packet 1 must quantitatively exploit the full target's third spectral direction; it cannot declare the cross-bank choice free or erase the self blocks.

## 4. Strongest conditional end-to-end argument after this run

The current source-backed proof skeleton is now:

1. The half-offdiagonal branch `s_2(A-diag A)<=499/1000` is already paid by the current campaign with a universal bound below `84`.
2. Otherwise account03/B20 gives the half-barrier source-realizable trichotomy. In its packet 1, `s_2(C)>=499/8000`; Theorem 1 above gives the exact dimension-free estimate (2.1).
3. In the other two partner packets, one has either an outer bank plus a strong physical pivot or an outer bank plus a strong nested bank; current campaign results pay some pivot/cross-dominated subbranches but do not yet universally pay the residual entangled cases.
4. Consequently a full proof follows if the remaining packet-payment theorem converts either (a) the packet-1 `h^(1/2)` estimate plus `s_3(A)>=1`, or (b) the outer+nested packet, into a linear concentration estimate `P(Q in I)<=K|I|` with universal `K`, without post-rotation independence and while retaining arbitrary same-bank quadratic terms.

The first unpaid implication can therefore be stated sharply as follows.

### `QFORM-THIRD-DIRECTION-UPGRADE-v1` — first unpaid universal implication

There is a universal finite `K` such that for every independent cap-one input vector `X` and every real symmetric `A` with `s_3(A)>=1`, whenever there is an original-coordinate cut with

`s_2(A[L,R]) >= 499/8000`,                                            (4.1)

one has for every interval `I`

`P(X^T A X in I) <= K |I|`.                                          (4.2)

No condition may be added on the two self blocks, outside couplings, support, moments, or post-rotation independence.

The factorized construction in Section 3 proves that the hypothesis `s_3(A)>=1` in this upgrade is essential: dropping it makes (4.2) false even when `s_2(C)=1/2`.

The exact quantitative replacement proved in this run is (2.1). It reduces the analytic task from arbitrary concentration to an exponent upgrade that must spend the third spectral direction.

## 5. Mechanism movement and next attack

**Before:** account03/B20 isolated a large rank-two physical cross bank but its payment with arbitrary self blocks was completely unpaid.

**After:** the entire rank-two bank now yields a source-valid dimension-free `1/2`-Hölder concentration estimate, and a concrete independent-uniform family proves that no argument using only that bank can upgrade it to `L^infinity`. The third spectral direction is now identified as the exact missing resource.

This suggests a different next mechanism from repeated local pair extraction: apply a second, source-preserving square-kernel or logarithmic-pair step only after the rank-two bank has produced the reciprocal-slope expectation (1.13), and force the third spectral direction to enter that second averaging. A successful version must improve the small-ball exponent from `1/2` to `1`; if it merely repeats Cauchy--Schwarz it cannot close the target.

## 6. Status

`ESSENTIAL_STEP_APPLIED / QUANTITATIVE_REPLACEMENT_PROVED / FULL_TARGET_OPEN`.

No claim of a full QFORM proof is made. No continuity conclusion beyond already established campaign branches is added. The counterexample in Section 3 is a counterexample only to the **free rank-two cross-bank payment step**, not to the three-eigenvalue conjecture.
