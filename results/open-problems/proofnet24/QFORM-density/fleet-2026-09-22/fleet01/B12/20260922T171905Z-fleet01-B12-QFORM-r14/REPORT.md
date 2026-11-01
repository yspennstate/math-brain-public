# fleet01/B12 — endpoint Schur absorption for an arbitrary rank-one spectral addition

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Additional eigenvalue control  
**Run:** `20260922T171905Z-fleet01-B12-QFORM-r14`  
**Classification:** `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and first unpaid implication

The full target remains open: for every dimension, every product law with independent real coordinate densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `X^T A X` (with continuity tracked separately), or give a valid counterexample.

This run addresses the B12 question: how can an arbitrarily large added eigen-direction be transported through the original-coordinate argument without falsely treating the new quadratic term as an independent convolution?

The designated partner `fleet02/B12` supplied two relevant exact facts. First, its stress family

`A_M = I_4-(M+1)vv^T-(3/2)ww^T`,

with `v=(1,1,1,1)/2`, `w=(1,1,-1,-1)/2`, has spectrum `{1,1,-1/2,-M}` and sends asymptotically all third-compound mass into the overlap-two channel while every physical pair is indefinite and every physical principal triple has smallest singular value of order `1/M`. Source: `yspennstate/math-open-problems@c831c437535fc6dcffe0e2cd8fb40f9f7dbe9810`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/fleet02-B12-20260922T165319Z-qform-r11/REPORT.md`.

Second, its Schur-tail stability theorem says that, at a nonzero physical pivot `a_0`, a symmetric perturbation `E` with `||E||_op<=delta<|a_0|` moves the Schur complement by at most

`epsilon = delta (1+||b_0||/|a_0|)^2/(1-delta/|a_0|)`,

where `b_0` is the off-diagonal pivot column. Source: `yspennstate/math-open-problems@c1c87a33cb9223e78b3b50398328ff73d7dc85d1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260922T155613Z-fleet02-B12-qform-add-eigen-r11/REPORT.md`.

The new step below produces an exact endpoint Schur identity for a rank-one spectral addition, then applies the partner tail theorem to obtain an explicit mixed large-spike + full-rank-tail density inequality.

## 2. Exact endpoint Schur identity

Let

`A_tau = A_0 + tau v v^T`

with `A_0` symmetric, `tau` arbitrary, and choose an ORIGINAL coordinate `i` for which `u=v_i !=0`. Split that coordinate from the others:

`A_0 = [[alpha,b^T],[b,C]]`,  `v=(u,w)`.

Put

`a_tau = alpha + tau u^2`,

`z = b-(alpha/u)w`,

and define the tau-independent endpoint matrix

`S_infty = C-(b w^T+w b^T)/u+(alpha/u^2) w w^T`.

### Theorem 2.1 — `QFORM-RANK1-ENDPOINT-SCHUR-v1`

Whenever `a_tau !=0`, the physical Schur complement is exactly

`Sc_i(A_tau) = S_infty - a_tau^(-1) z z^T`.                 (2.1)

#### Proof

The pivot row of `A_tau` is `b+tau u w` and its residual block is `C+tau w w^T`, hence

`Sc_i(A_tau)=C+tau w w^T-(b+tau u w)(b+tau u w)^T/a_tau`.

Expanding the proposed right side of (2.1), the coefficient of `bb^T` is `-1/a_tau`; the coefficient of `bw^T+wb^T` is

`-1/u + alpha/(a_tau u) = -tau u/a_tau`;

and the coefficient of `ww^T` is

`alpha/u^2-alpha^2/(a_tau u^2)=alpha tau/a_tau`

which equals `tau-tau^2u^2/a_tau`. These are exactly the coefficients in the direct Schur expansion. QED.

The sign information is the useful point:

- if `a_tau<0`, then `Sc_i(A_tau)=S_infty + |a_tau|^(-1)zz^T`, a PSD update;
- if `a_tau>0`, then `Sc_i(A_tau)=S_infty - a_tau^(-1)zz^T`, an NSD update.

Thus the large added eigendirection need not be treated as an independent random variable: after one physical-coordinate completion of the square, it becomes a **sign-controlled rank-one Loewner update of a tau-independent endpoint residual**.

## 3. Sign-opposed endpoint absorber

Use the completed physical-three-block theorem `QFORM-TWO-SAMESIGN-THREEBLOCK-v1`: if an original-coordinate physical `3x3` block has two eigenvalues at least `L>0` (or two at most `-L`), while the third is arbitrary, then after conditioning all outside original coordinates the quadratic form has density at most

`C_*/L`,  `C_*=24.183038289961516...`.

Source: `yspennstate/math-open-problems@b3c543b40dfaef13468466fa82625303a7719af8`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`.

### Theorem 3.1 — `QFORM-SIGN-OPPOSED-RANK1-ABSORBER-v1`

With the notation above, let `T` be three residual ORIGINAL coordinates. Suppose there is `sigma in {+1,-1}` such that `sigma S_infty[T,T]` has at least two eigenvalues at least `L>0`, and suppose

`sigma a_tau <0`.                                             (3.1)

Then, for arbitrary independent coordinate laws with densities at most one and arbitrary coefficients/couplings outside these coordinates,

`||p_{X^T A_tau X}||_infinity <= 2 sqrt(C_*/(L |a_tau|)).`      (3.2)

#### Proof

By (2.1) and (3.1),

`sigma Sc_i(A_tau)[T,T] = sigma S_infty[T,T] + |a_tau|^(-1) z_T z_T^T`.

The correction is PSD, so the two required same-sign eigenvalues remain at least `L`. The physical-three-block theorem therefore bounds the Schur-residual density by `M=C_*/L`.

Now complete the square only in the original coordinate `X_i`:

`Q = a_tau V^2 + R`,

where `R=X_{-i}^T Sc_i(A_tau) X_{-i}` and `V=X_i+ell(X_{-i})`. Conditional on all other original coordinates, `V` is a translate of the independent variable `X_i`, hence its conditional density is at most one. Mixing this conditional law over a level set of `R` preserves the cap one.

For completeness, if a random variable `R` has density at most `M` and `V|R=r` has density at most one, then the density of `R+aV^2` is at most `2 sqrt(M/|a|)`: conditional on `R=r`, the square density is bounded by `(|a|u)^(-1/2)` on the appropriate half-line, and the decreasing-kernel bathtub bound under `0<=p_R<=M`, `int p_R=1` is

`sup_t int_0^infinity p_R(t-u) u^(-1/2)du <= 2 sqrt(M)`.

Taking `M=C_*/L` gives (3.2). No independence between `R` and `V` is asserted or needed. QED.

A simple large-spike consequence is useful. If `sign(tau)=-sigma` and

`|tau| u^2 >= 2|alpha|`,

then `sign(a_tau)=sign(tau)=-sigma` and `|a_tau|>=|tau|u^2/2`; hence

`||p_Q||_infinity <= [2 sqrt(2 C_*/L)]/(|u| sqrt(|tau|)).`      (3.3)

Thus, in this sign-compatible endpoint geometry, an arbitrarily large added eigenvalue of either sign is not merely harmless: the bound improves like `|tau|^(-1/2)`.

## 4. Actual application of the designated partner tail theorem

Now add an arbitrary symmetric full-rank tail `E`:

`A = A_tau + E`,  `||E||_op <= delta < |a_tau|`.

Let `b_tau=b+tau u w` and define the partner's exact tail loss

`epsilon_tail = delta (1+||b_tau||/|a_tau|)^2 /(1-delta/|a_tau|).`  (4.1)

Assume the hypotheses of Theorem 3.1 and additionally `epsilon_tail<L`. The designated `fleet02/B12` theorem gives

`||Sc_i(A)-Sc_i(A_tau)||_op <= epsilon_tail`.                  (4.2)

Weyl therefore leaves two residual eigenvalues of sign `sigma` and magnitude at least `L-epsilon_tail`. Also the final physical pivot satisfies

`|A_ii| >= |a_tau|-delta`.

Applying the same original-coordinate square completion to the final matrix gives the explicit inequality

`||p_{X^T A X}||_infinity`
` <= 2 sqrt( C_* / [ (L-epsilon_tail)(|a_tau|-delta) ] ).`       (4.3)

This is a direct mathematical use of the assigned partner result. It controls one arbitrary rank-one added eigen-direction of unrestricted magnitude plus a genuinely dependent, arbitrary-rank, mixed-sign spectral tail of small operator norm. There is no convolution after a rotation.

## 5. The partner stress family is uniformly paid

The latest designated-partner stress family is

`A_M=I_4-(M+1)vv^T-(3/2)ww^T`, `M>1`,

with `v=(1,1,1,1)/2`, `w=(1,1,-1,-1)/2`, and `A_M=A_1-(M-1)vv^T`.

The partner proved that every physical pair is indefinite and every physical principal triple has eigenvalues

`1, rho_M, -1/(8 rho_M)`,

`rho_M=2/(sqrt((6M-1)^2+32)+6M-1)`,

so the direct local three-block constant degrades as `M` grows even though the target remains in force.

Apply Theorem 2.1 to base `A_1`, spike `tau=-(M-1)`, and coordinate `i=1`. Here

`alpha=1/8`,

`b=(-7/8,-1/8,-1/8)^T`,

`u=1/2`, `w=(1/2,1/2,1/2)^T`,

`z=(-1,-1/4,-1/4)^T`,

and the endpoint residual is exactly

`S_infty = [[2,1,1],[1,1/2,-1/2],[1,-1/2,1/2]]`.

Its eigenvalues are

`1, 1-sqrt(3), 1+sqrt(3)`,

so it has two positive eigenvalues at least one. The actual pivot is

`a_M=(3-2M)/8`.

For `M>3/2`, `a_M<0`; hence Theorem 3.1 with `sigma=+1`, `L=1` gives

`||p_{X^T A_M X}||_infinity <= 2 sqrt(C_*/|a_M|)`
` = sqrt(32 C_*/(2M-3)).`                                     (5.1)

To cover the narrow pivot-zero region without division, use the partner's exact principal-triple formula. For `1<M<=151/100`, write `x=6M-1<=403/50<73/9`. Since

`sqrt(x^2+32)+x<18` iff `x<73/9`,

we have `rho_M>1/9`. The physical-three-block theorem then gives

`||p_Q||_infinity < 9 C_*`.                                   (5.2)

For `M>=151/100`, `|a_M|=(2M-3)/8>=1/400`, so (5.1) gives

`||p_Q||_infinity <= 40 sqrt(C_*) < 9 C_*`.

Therefore the entire partner stress family, including the regime where every principal triple becomes ill-conditioned, satisfies the uniform bound

`||p_{X^T A_M X}||_infinity < 9 C_* <218`,  `M>1`.             (5.3)

Reflection gives exactly the same bound for `-A_M`.

This does not prove the full conjecture. It does show that the partner's overlap-two transfer family is **not itself an obstruction** to a product-preserving original-coordinate proof: the large spectral spike can be routed through the endpoint Schur sign.

## 6. Scope, corrections, and remaining implication

The result uses no Gaussianity, moments, log-concavity, compact support, spectral-coordinate independence, pointwise van-der-Corput decay, fixed-small-minor dichotomy, or raw fiber-supremum bound. It is consistent with the live corrections including `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`, `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`, and `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1`.

**Continuity:** not proved by the new argument; (3.2), (4.3), and (5.3) establish an essentially bounded density only.

**Full target status:** OPEN.

**First unpaid implication after this run:** make the endpoint certificate exhaustive. Starting from only `s_3(A)>=1`, one still has to force either (i) a ridge/grouped-coordinate branch already paid in the archive, or (ii) an original-coordinate rank-one endpoint representation for which the pivot sign is opposite a two-same-sign endpoint residual at a universal quantitative scale. The third-compound overlap theorem supplies conserved aggregate mass, but a universal passage from the O1/O2 heavy overlap channels to this sign-opposed endpoint geometry is not yet proved.

A promising next algebraic subproblem is to formulate the O2 overlap-two aggregate as an average of endpoint Schur forms **before** reciprocal local pivots are taken. The exact identity (2.1) suggests using the sign of the physical pivot to route each contribution to a Loewner-monotone endpoint residual, while the partner family shows why taking the smallest singular value of a principal triple first is the wrong order.

## 7. Provenance and verification note

Current owner control at the prepublication refresh: QFORM-only, control revision `2026-09-22.8`; programme revision `2026-09-22.5`. The full conjecture is still explicitly open in the shared state. Repository retrieval was used directly; no native learned-memory receiver was verified, so execution remains `WITHOUT_VERIFIED_BRAIN`.

Changed-file review for this report is restricted to this mathematical file. It contains only mathematical statements and source pins; no credentials, scheduler IDs, machine paths, unrelated private data, or public-release action. Algebraic equalities above were derived symbolically/exactly; numerical constants are only displayed consequences and are not used in place of proof.
