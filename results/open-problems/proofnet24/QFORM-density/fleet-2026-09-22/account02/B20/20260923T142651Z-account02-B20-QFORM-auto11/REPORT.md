SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T14:26:51Z.
attacking: the newest account03/B20 N3 local-pair / rank2-or-two-anchor survivor, using only original-coordinate product banks.

# account02/B20 — physical-pair payment and augmented-three-volume compiler

**Run:** `20260923T142651Z-account02-B20-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full QFORM remains OPEN; full-target continuity remains OPEN.  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and source discipline

For arbitrary dimension, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, the target is one universal finite essential bound for the density of `Q=X^TAX`. No moments, support, log-concavity, Gaussianity, diagonal-basis assumption, or independence after spectral rotation is used. Continuity is separate.

Fresh designated-partner result actually consumed: account03/B20 r32, canonical mathematics

`yspennstate/math-open-problems@5cb423f9026efd414c2bbc57af2827c3abded292`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T125643Z-account03-B20-QFORM-r32/REPORT.md`.

Its current N3 state is

`N3(1/64): s_3(A)>=1, |A_ii|<1/64, |A_ii A_jj-A_ij^2|<1/64`.

After already-paid branches, r32 leaves one of:

1. a physical diagonal `1/256<=|A_hh|<1/64`;
2. an indefinite physical principal pair `B` with
   `D:=|det B|>53/3276800` and `kappa:=sigma_min(B)>53/428800`;
3. a physical hub/cross packet with hub `h`, partition `h^c=J disjoint_union K`, arm energies
   `||a||^2,||b||^2>A0:=103/6553600`, where `a=A[J,h]`, `b=A[K,h]`, and for `N=A[J,K]`
   `s_1(N)^2+s_2(N)^2>B0:=217279/1048576`;
4. the same arm packet in the two-sided ridge-localized branch, which in the proof of r32 occurs under `s_3(N)>=1/8` and additionally supplies physical ridge anchor row/column energies `>1/768`.

All banks are literal sets of original independent coordinates.

Two completed source theorems are used below at equations, not only cited: the arbitrary-rank physical-pair theorem at commit `742ac943440e41925fe09db9a8c02a96cbd83dbc`, and the D'/D5 physical-cross-block theorems in the pinned Claude source `e5f71d79eff325201dd0274053d20268ce65b837`.

## 2. The r32 indefinite-pair alternative is already fully paid

The arbitrary-rank physical-pair theorem states that if `s_3(A)>=s>0` and an ORIGINAL physical principal pair is invertible indefinite, then, with `D=|det B|` and `kappa=sigma_min(B)`, the full ambient form (arbitrary remaining spectrum, arbitrary couplings and affine terms) has an essentially bounded density satisfying

`||p_Q||_infinity <= 3*400^(1/3) (D^2 kappa s)^(-1/6)`.

Apply it to the exact r32 constants and `s=1`:

`D>53/3276800`, `kappa>53/428800`.

Therefore

`||p_Q||_infinity`
` < 3*400^(1/3)*(53/3276800)^(-1/3)*(53/428800)^(-1/6)`
` =3916.178013... <3917`.                                           (2.1)

Thus item 2 of the r32 unpaid list is not unpaid. This payment is source-preserving: the chosen pair consists of two original independent coordinates and the theorem explicitly retains arbitrary extra spectrum. It proves essential boundedness; no continuity upgrade is inferred.

### Pinned-source D5 check on the preceding compiler

For completeness, the r32 predecessor's balanced physical cut has `E1=||N||_F^2>3969/16384`. If the four largest squared singular values carry at most `(63/64)E1`, then five iid samples from the singular-square weights are distinct with probability at least `(1/64)^4`; hence

`e_5(N^TN) >= (1/64)^4 E1^5/120`
`            > (1/64)^4(3969/16384)^5/120`.

The pinned unrestricted D5 theorem

`||p_Q||_infinity <=5 sqrt(2e) e_5(N^TN)^(-1/10)`

therefore gives exactly

`||p_Q||_infinity`
` <5 sqrt(2e)[120/((1/64)^4(3969/16384)^5)]^(1/10)`
` =201.786346... <201.787`.                                         (2.2)

This is an actual use of the required pinned source on an original-coordinate cross block; arbitrary same-side blocks and outside couplings remain present.

## 3. Exact augmented three-volume identity

The main new deterministic input spends a hub arm together with two cross directions without rotating the random source.

### Lemma 3.1 — `QFORM-AUGMENTED-E3-WEDGE-IDENTITY-v1`

Let `N` be any real `m x n` matrix with singular values `s_1>=s_2>=...` and left singular vectors `u_r`. For any `a in R^m`, form the augmented matrix

`M=[a  N]`.

Then

`e_3(M^TM)`
` =e_3(N^TN)+sum_(r<s) s_r^2 s_s^2 ||P_{span(u_r,u_s)^perp} a||^2`.  (3.1)

In particular, for `U_2=span(u_1,u_2)`,

`e_3(M^TM) >= s_1^2 s_2^2 ||P_{U_2^perp}a||^2`.                    (3.2)

#### Proof

By Cauchy--Binet, `e_3(M^TM)` is the sum of squares of all three-column exterior volumes of `M`. Right-multiplying the `N` columns by the orthogonal right singular matrix does not change that sum, so take the columns of `N` to be `s_r u_r` (plus zero columns). Three-column minors not containing `a` sum to `e_3(N^TN)`. A minor containing `a,s_ru_r,s_su_s` has squared volume

`s_r^2 s_s^2 (||a||^2-|<a,u_r>|^2-|<a,u_s>|^2)`
` =s_r^2 s_s^2 ||P_{span(u_r,u_s)^perp}a||^2`.

Summing proves (3.1), and retaining only `(r,s)=(1,2)` proves (3.2). QED.

This identity is purely deterministic. Its later probabilistic use is on literal physical cross blocks.

## 4. Paying the transverse diffuse part of r32's rank-two-dominated packet

Keep r32 notation

`A0=103/6553600`, `B0=217279/1048576`,
`a=A[J,h]`, `b=A[K,h]`, `N=A[J,K]`.

Fix one SVD of `N`, with top-two left/right subspaces `U_2,V_2`. Define the two literal augmented physical cross blocks

`M_L=A[J,{h} union K]=[a,N]`,
`M_R=A[K,{h} union J]=[b,N^T]`.

Let `alpha_i^L` and `alpha_i^R` denote the D' three-volume row marginals of these cross blocks.

### Theorem 4.1 — `QFORM-R32-RANK2-AUGMENTED-VOLUME-v1`

Assume the r32 rank-two-dominated packet

`||a||^2>A0`, `||b||^2>A0`,
`s_1(N)^2+s_2(N)^2>B0`.                                               (4.1)

Then either the full law has a continuous `C_0` density with

`||p_Q||_infinity <457.013`,                                          (4.2)

or every unpaid state satisfies at least one of the following on each side, after possibly first entering the rank-one-dominated alternative:

**Rank-one-dominated cross:**

`s_2(N)^2 < B0/4`, and hence `s_1(N)^2>3B0/4`.                        (4.3)

If (4.3) fails, then on the left

`||P_{U_2}a||^2>3A0/4`                                                (4.4L)

or

`max_(j in J) alpha_j^L>2/3`,                                        (4.5L)

and on the right

`||P_{V_2}b||^2>3A0/4`                                                (4.4R)

or

`max_(k in K) alpha_k^R>2/3`.                                        (4.5R)

So a surviving genuinely two-direction packet is forced into **top-two alignment or three-volume concentration on both physical sides**.

#### Proof

Assume (4.3) fails, so `y=s_2^2>=B0/4`; put `x=s_1^2>=y`. From `x+y>B0`,

`xy>3B0^2/16`.                                                        (4.6)

Indeed if `y>=B0/2`, then `xy>=y^2>=B0^2/4`; while for `B0/4<=y<B0/2`, `x>B0-y` and the concave function `y(B0-y)` has minimum `3B0^2/16` on that interval.

Suppose first that the left arm is not aligned as in (4.4L). Since `||a||^2>A0`,

`||P_{U_2^perp}a||^2>A0/4`.                                          (4.7)

Lemma 3.1 applied to the literal physical cross block `M_L` yields

`Z_L:=e_3(M_L^T M_L)`
` > (3B0^2/16)(A0/4)=3B0^2 A0/64=:Z0`.                               (4.8)

If also `max alpha_j^L<=2/3`, apply the pinned D' theorem with `h=2/3`. Its exact coefficient is

`6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1)=9 sqrt(3e)`.

Hence

`||p_Q||_infinity <=9 sqrt(3e) Z_L^(-1/6)`
` <9 sqrt(3e) Z0^(-1/6)`
` =457.012419... <457.013`,                                           (4.9)

and the source theorem supplies a continuous `C_0` density. Therefore any unpaid state has (4.4L) or (4.5L). Applying the same argument to `M_R=[b,N^T]` gives (4.4R) or (4.5R). QED.

No singular vector is used as a random coordinate; `U_2,V_2` appear only inside deterministic coefficient geometry. D' is applied to the original-coordinate matrices `M_L,M_R`.

## 5. The same compiler sharpens the two-sided ridge-localized packet

In r32 Theorem 3.1, the two-sided ridge-localized alternative arises only after assuming

`s_3(N)>=1/8`.                                                        (5.1)

Thus `s_1^2 s_2^2>=1/4096`. Apply Lemma 3.1 again. If the left hub arm has transverse top-two mass at least `A0/4`, then

`e_3(M_L^T M_L) >= A0/16384`.                                        (5.2)

If its D' row marginals are all at most `2/3`, then

`||p_Q||_infinity`
` <=9 sqrt(3e)(A0/16384)^(-1/6)`
` =818.390951... <819`.                                               (5.3)

The same holds on the right. Therefore every still-unpaid r32 two-sided ridge packet must, on **each** side, have either top-two arm alignment

`||P_{U_2}a||^2>3A0/4`, respectively `||P_{V_2}b||^2>3A0/4`,

or an augmented three-volume row marginal exceeding `2/3`. This is in addition to r32's already-proved physical ridge anchor row and column energies `>1/768`.

## 6. Updated source-pinned N3 compiler

Combining r32 with Sections 2, 4 and 5, the r32 indefinite-pair packet is fully paid by `<3917`. The previously paid branches remain `<217.085`, `<201.787`, or `<102.805` in their exact scopes. Every currently unpaid `N3(1/64)` state is therefore reduced to one of:

1. **Moderate physical diagonal:** some original `h` has
   `1/256<=|A_hh|<1/64`.
2. **Rank-one-dominated star/cross:** r32's two physical arm energies exceed `A0`, and
   `s_2(N)^2<B0/4`, `s_1(N)^2>3B0/4`.
3. **Aligned/concentrated genuinely-two-direction packet:** the arm/cross hypotheses (4.1) hold with `s_2^2>=B0/4`, and on each physical side the hub arm is `>3A0/4` aligned with the top-two singular subspace or the augmented D' three-volume has a physical row marginal `>2/3`.
4. **Aligned/concentrated two-sided-ridge packet:** r32's `s_3(N)>=1/8` ridge-localized state, with the physical ridge row/column energies `>1/768`, and on each side the same top-two-alignment / augmented-volume-concentration dichotomy.

This removes one entire r32 packet and turns both star packets into strictly narrower aggregate obstructions.

## 7. First unpaid universal implication

The first unpaid implication in this updated compiler is now

`QFORM-N3-MODERATE-DIAGONAL-PAYMENT-v1`:

> Let `X_i` be arbitrary independent real random variables with densities bounded by one. Let `A` be arbitrary real symmetric with `s_3(A)>=1`, all physical diagonals `<1/64` in modulus, all physical principal pair determinants `<1/64` in modulus, and suppose some original coordinate `h` satisfies `|A_hh|>=1/256`. Prove a universal finite essential bound for the density of `X^TAX`, retaining every remaining eigenvalue/coupling; or source-validly reduce this state to one of the already-paid physical pair, volume, ridge, grouped-square or mixed-hub receivers.

Completing the square at `h` is not by itself enough: the Schur residual has two large spectral directions, but the available orientation-free half-Riesz theorem is exact-rank-two, while arbitrary extra quadratic curvature cannot simply be deleted on unbounded product inputs. Thus the genuinely missing object is an **arbitrary-extra-spectrum two-direction fractional receiver** (or an equivalent physical-bank reduction), not a scalar conditioning trick.

## 8. Corrections and status

No step uses law-uniform pointwise quadratic-phase decay, independence after spectral rotation, an arbitrary-joint coarea density cap, worst-fiber suprema, positive moments of worst conditional projection-density caps, or a universally good single minor. Small matrix norm is never treated as a uniformly small random quadratic perturbation.

The full QFORM conjecture remains OPEN. Continuity is established only on source theorems that explicitly provide it; the pair payment (2.1) is only an essential-density statement. No global continuity claim is made.
