# account01/B20 — N3 low-leverage closure compiler

Status: **ESSENTIAL_STEP_APPLIED**. The full QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN** and is tracked separately.

Run id: `20260923T114521Z-account01-B20-QFORM-auto11`.

## 1. Exact target and source discipline

Target: for arbitrary independent real random variables `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has an essentially bounded density with a universal finite constant, or give a valid counterexample.

No Gaussianity, moments, iid assumption, compact support, log-concavity, or independence after rotation is used below. The known false uniform pointwise quadratic oscillatory-decay route is not used. No small quadratic term is deleted.

Fresh designated partner actually consumed: account02/B20, canonical mathematics
`yspennstate/math-open-problems@19327f690f815425717fcbd07854302df2090970`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T112426Z-account02-B20-QFORM-auto11/REPORT.md`, source-pinned brain handoff at `yspennstate/math-research-brain@55bf41857b7e4f4d5ec12fb3cc0bdf4aebcf96dd`.

That partner reduces the current global no-pivot problem to the class `N3(tau)` with `tau=1/64` and, writing

`P = 1_{|A|>=1}`,

identifies the globally untouched branch `max_i P_ii < 1/2`. It also proves for a high-leverage hub the basic deterministic inequalities from `A^2>=P`, and retains all arbitrary extra spectrum.

Completed Fourier receiver used below: unrestricted fifth-volume theorem `D_5` from
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`:
for every genuine physical cross block `N`, with `Z_5=e_5(N^TN)`,

`||p_Q||_infty <= 5 sqrt(2e) Z_5^{-1/10}`,

with arbitrary same-side quadratic blocks and outside couplings retained.

Completed ridge receiver used below: the spectral-window/ridge theorem at
`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`. I re-run its proof with a larger admissible frame leverage `5/128` below; no new probabilistic input is needed.

## 2. N3 hypotheses

Throughout Sections 3–5, assume

1. `s_3(A)>=1` (equivalently at least three eigenvalues have modulus at least one),
2. `|A_ii|<tau=1/64` for every physical coordinate,
3. `|A_ii A_jj - A_ij^2|<tau` for every `i!=j`.

The third condition gives the uniform physical edge-square cap

`A_ij^2 < tau + tau^2 = 65/4096`.                                      (2.1)

Indeed `A_ij^2 <= |A_iiA_jj-A_ij^2|+|A_iiA_jj| < tau+tau^2`.

## 3. New theorem: leverage 1/32 already yields a balanced physical star plus a large leaf cross cut

### Theorem 3.1 — `QFORM-N3-1OVER32-STAR-BALANCED-CUT-v1`

Let `P=1_{|A|>=1}`. If for some original coordinate `h`

`P_hh >= 1/32`,                                                        (3.1)

then there is a partition of the original leaves

`h^c = J disjoint_union K`

such that simultaneously

`sum_{j in J} A_hj^2 > 31/4096`,

`sum_{k in K} A_hk^2 > 31/4096`,                                      (3.2)

and, for the genuine physical leaf cross block `N=A[J,K]`,

`||N||_F^2 > 3969/16384`.                                              (3.3)

### Proof

Because `A^2-P` is positive semidefinite,

`(A^2)_hh >= P_hh >= 1/32`.

Thus, with `w_j=A_hj^2` and `S=sum_{j!=h}w_j`,

`S = (A^2)_hh-A_hh^2 > 1/32-1/4096 = 127/4096`.                       (3.4)

By (2.1), every atom satisfies

`w_j < 65/4096`.                                                       (3.5)

Sort the `w_j` decreasingly, append one dummy zero if their number is odd, pair consecutive weights, and independently orient each pair so one endpoint goes to `J` and the other to `K`. For every orientation, the star discrepancy is bounded by the alternating sum

`|sum_J w_j - sum_K w_j| <= (w_1-w_2)+(w_3-w_4)+... <= w_1 <65/4096`.

Together with (3.4), both star masses are therefore larger than

`(127/4096-65/4096)/2 =31/4096`,

which proves (3.2) for every orientation.

It remains to choose an orientation with large leaf cross energy. Write `B=A[h^c,h^c]`. Let `p` be the number of eigenvalues of `A` at least one and `q` the number at most minus one. Since `p+q>=3`, Cauchy interlacing after deleting the single coordinate `h` gives at least

`max(p-1,0)+max(q-1,0) >=1`

eigenvalue of `B` with modulus at least one. Hence `||B||_op>=1`.

Let `D=diag(B)` and `Z=B-D`. Since `||D||_op<1/64`,

`||Z||_op > 1-1/64 =63/64`.

Therefore

`sum_{j!=k, j,k!=h} A_jk^2 = ||Z||_F^2 >= ||Z||_op^2 >3969/4096`.      (3.6)

Under the paired random orientation above, any two leaves from different pairs are put in the ordered configuration `j in J, k in K` with probability `1/4`; leaves from the same pair have probability `1/2`, so in every case the probability is at least `1/4`. Consequently

`E ||A[J,K]||_F^2 >= (1/4) sum_{j!=k}A_jk^2 >3969/16384`.

Some deterministic orientation attains at least its expectation, while (3.2) held for every orientation. This proves (3.3). QED.

### What was gained over the designated partner

The designated account02/B20 three-bank theorem used `P_hh>=1/2`. The present two-bank compiler applies already at

`P_hh>=1/32`,

while retaining a fixed physical leaf cross energy. It therefore applies to a large portion of the partner's previously untouched low-leverage branch.

## 4. Spend diffuse fifth-volume before localizing

Let `x_r=s_r(N)^2` and `E_1=sum_r x_r=||N||_F^2`.

### Lemma 4.1

For any nonnegative sequence `(x_r)` and `0<eta<1`, if

`sum_{r=1}^4 x_r <= (1-eta)E_1`,                                      (4.1)

then

`e_5(x) >= eta^4 E_1^5/120`.                                          (4.2)

### Proof

Put `p_r=x_r/E_1`. Five iid draws from the distribution `p` are all distinct with probability `5!e_5(p)`. Once at most four distinct indices have been drawn, their total probability mass is at most the sum of the four largest `p_r`, which by (4.1) is at most `1-eta`. Thus each of draws 2 through 5 is new with conditional probability at least `eta`. Hence

`120 e_5(p) >= eta^4`,

which is (4.2) after multiplying by `E_1^5`. QED.

Take `eta=1/64`. Combining Theorem 3.1, Lemma 4.1 and `D_5` gives the following actual target inequality.

### Theorem 4.2 — `QFORM-N3-1OVER32-STAR-D5-COMPILER-v1`

Under the hypotheses of Theorem 3.1, either

`||p_Q||_infty < 201.787`,                                             (4.3)

and this branch has a continuous `C_0` density by the Fourier receiver, or the same physical partition `J,K` satisfies

`sum_{r=1}^4 s_r(A[J,K])^2 > (63/64)||A[J,K]||_F^2`

and in particular

`sum_{r=1}^4 s_r(A[J,K])^2 > 250047/1048576 =0.238463401794...`.       (4.4)

Moreover the two hub-to-bank square masses in (3.2) remain present.

### Proof

If the alternative to (4.4) holds, Lemma 4.1 and (3.3) give

`Z_5=e_5(N^TN) > (1/64)^4 (3969/16384)^5 /120`.

The `D_5` theorem therefore gives

`||p_Q||_infty`
` <=5 sqrt(2e) [120 / ((1/64)^4(3969/16384)^5)]^(1/10)`
` =201.786346662743... <201.787`.

Otherwise (4.4) follows directly, with

`(63/64)(3969/16384)=250047/1048576`.

All blocks are physical original-coordinate blocks; no rotated random variables are introduced. QED.

The non-paid alternative (4.4) is intentionally retained as a **relative four-direction concentration packet**, not treated as an exact rank-four form and not truncated.

## 5. New theorem: the spectral-window leverage gate improves from 1/32 to 5/128

The prior spectral-window theorem used the sufficient hypothesis `max_i(P_*)_ii<=1/32`, where

`P_* = 1_{|A|>=1/64}`.

Its constants have slack. Re-running the same proof gives a strictly larger admissible threshold.

### Theorem 5.1 — `QFORM-SPECTRAL-WINDOW-5OVER128-v1`

For an arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, let

`P_* = 1_{|A|>=1/64}`.

If

`max_i(P_*)_ii <= epsilon:=5/128`,                                    (5.1)

then for arbitrary independent cap-one coordinate densities, `Q=X^TAX` has a continuous `C_0` density and

`||p_Q||_infty <= 576 sqrt(3e)/(57-16 sqrt(5))`
`                 =77.5042237804...`.                                 (5.2)

### Proof

Write `A=A_H+E`, where `A_H=U Lambda U^T` is the spectral truncation to `|lambda|>=1/64`. Thus

`||E||_op<eta:=1/64`,

`U^TU=I`, and every physical row `u_i` of `U` has `||u_i||^2<=epsilon`.

The two-part MSS frame partition gives a physical partition `I,J` for which each partial Gram matrix lies between `delta I` and `(1-delta)I`, with

`delta =1-(1/sqrt(2)+sqrt(epsilon))^2`
`      =(59-16sqrt(5))/128`.                                          (5.3)

Since `Lambda` has at least three singular values at least one,

`s_3((A_H)[I,J]) >= delta`.

After restoring the tail,

`s_3(A[I,J]) >= sigma:=delta-eta`
`              =(57-16sqrt(5))/128`.                                 (5.4)

The range projection of `(A_H)[I,J]` on the `I` side has diagonal at most `epsilon/delta`. The ridge-stability lemma from the cited receiver, with `gamma=sigma/sqrt(6)`, therefore gives

`max_i(K_gamma)_ii`
` <= [sqrt(epsilon/delta)+eta sqrt(6)/sigma]^2`.                       (5.5)

This is strictly smaller than `1/2`. A completely rational verification is available without decimal arithmetic: `sqrt(5)<9/4` gives

`delta>23/128`, `sigma>21/128`.

Hence

`sqrt(epsilon/delta) < sqrt(5/23) <15/32`,

because `(15/32)^2=225/1024>5/23`, and `sqrt(6)<5/2` gives

`eta sqrt(6)/sigma <5/21`.

Thus the square bracket in (5.5) is smaller than

`15/32+5/21 =475/672`,

and

`(475/672)^2 <1/2`

because `475^2=225625 <225792=672^2/2`.

The cited ridge Fourier theorem now applies with `q=1`; the three singular values in (5.4) yield

`||p_Q||_infty <=9sqrt(3e)/(2sigma)`
`=576sqrt(3e)/(57-16sqrt(5))`.

Its characteristic-function envelope is integrable, so the resulting density is continuous and vanishes at infinity. QED.

## 6. Actual closure consequence for the account02/B20 low-leverage branch

Let

`P_0=1_{|A|>=1}`,

`P_*=1_{|A|>=1/64}`,

and let

`R=P_*-P_0 = 1_{1/64<=|A|<1}`

(the endpoint convention at `1` can be assigned to `P_0`; it does not change the inequalities below).

Start with the exact account02/B20 untouched state

`max_i(P_0)_ii <1/2`.                                                  (6.1)

Theorems 4.2 and 5.1 give the following exhaustive compiler.

### Corollary 6.1 — `QFORM-N3-LOWLEVERAGE-ANNULUS-OR-STAR4DIR-COMPILER-v1`

Every state satisfying (6.1) obeys at least one of:

**(A) paid balanced-star diffuse branch:**

`||p_Q||_infty<201.787`;

**(B) physical balanced-star/four-direction packet:** there are a physical hub `h` and a physical leaf partition `J disjoint_union K=h^c` such that

`sum_{j in J}A_hj^2>31/4096`,

`sum_{k in K}A_hk^2>31/4096`,

`||A[J,K]||_F^2>3969/16384`,

and

`sum_{r<=4}s_r(A[J,K])^2 >(63/64)||A[J,K]||_F^2`;

**(C) paid spectral-window branch:**

`||p_Q||_infty <=576sqrt(3e)/(57-16sqrt(5))=77.5042237804...`;

**(D) genuine extra-spectrum annulus packet:** for some original physical coordinate `h`,

`(P_0)_hh<1/32`,

`(P_*)_hh>5/128`,

hence

`R_hh > 5/128-1/32 =1/128`.                                           (6.2)

In case (D), the annular spectral component `A_ann=A R=R A` obeys the deterministic energy inequality

`(A_ann^2)_hh > (1/64)^2(1/128)=1/524288`.                            (6.3)

### Proof

If some `(P_0)_hh>=1/32`, Theorem 4.2 gives (A) or (B). Otherwise `max_i(P_0)_ii<1/32`. If `max_i(P_*)_ii<=5/128`, Theorem 5.1 gives (C). If not, choose `h` with `(P_*)_hh>5/128`; nested spectral projections give (6.2). Since every eigenvalue in the annulus has squared modulus at least `(1/64)^2`, (6.3) follows from spectral calculus. QED.

This is a strict narrowing of the partner's first globally untouched branch. The word `extra-spectrum` is now literal: every survivor not already routed into the balanced star/four-direction packet carries at least `1/128` original-coordinate leverage in the subunit spectral annulus `[1/64,1)`.

## 7. First remaining implication

The next proof debt is now the disjunction

`QFORM-N3-ANNULUS-OR-STAR4DIR-PAYMENT-v1`:

1. pay the physical packet in Corollary 6.1(B), retaining the `<=1/64` relative singular tail rather than deleting it; or
2. from Corollary 6.1(D), convert the fixed original-coordinate annular leverage `R_hh>1/128`, together with the N3 principal-pivot failures, into an existing whole-law ridge/volume/grouped-square/random-slope receiver.

The second branch is genuinely an extra-spectrum problem and no longer conflates it with leverage of the three target eigen-directions.

## 8. Corrections and scope

- Full QFORM: **OPEN**.
- Full-target continuous representative: **OPEN**.
- The paid branches (A) and (C) above are continuous by their respective integrable-Fourier theorems.
- No uniform pointwise quadratic oscillatory decay was used.
- No post-rotation or projected independence was used.
- No arbitrary-joint three-dimensional coarea bound was used.
- No tiny quadratic term or small singular tail was deleted.
- No inference from aggregate mass to one good minor was used.
- The four-direction alternative is only a structural packet; it is not called paid.
- The annulus projection is used only deterministically; `R X` is not treated as an independent random coordinate.

Execution label remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval/write occurred, but no genuine authenticated learned-memory receiver ingestion was exposed.
