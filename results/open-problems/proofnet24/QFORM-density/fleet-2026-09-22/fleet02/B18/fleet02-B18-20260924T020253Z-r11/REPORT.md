# fleet02/B18 — stable-rank / fifth-volume / rank-four zero-self funnel

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `fleet02-B18-20260924T020253Z-r11`  
**Role:** literature-to-proof transfer / complementary constructions and source-valid counterexamples  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREM / LATEST DESIGNATED PARTNER APPLIED / PINNED e5f RESULT APPLIED / TARGET-VALID FAMILY CLOSED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-24T02:02:53Z.  
attacking: the zero-self-bank residual chamber—combine the newest fleet03/B18 Hilbert--Schmidt stable-rank negative-moment receiver with the pinned e5f fifth-volume theorem, and force every crossing-heavy unpaid block into a quantitatively rank-four carrier while retaining its residual.

## 1. Exact target and first unpaid implication

The owner target remains unrestricted: independent real coordinates with probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one.  No moments, compact support, log-concavity, iid hypothesis, smoothness, centering, symmetry of the laws, diagonal-basis independence, or independence after rotation is added.  Continuity remains separate.

The first unpaid implication isolated here is the following zero-self-bank bridge.  In original coordinates write

`A = [[0,B],[B^T,C]]`,

and put `s=s_3(A)`.  After the paid low-`C` branch, the paid stable-rank branch, and the paid fifth-volume branch, show that the remaining crossing-heavy state

`||C||op > s/2`, `||B||op >= s/2`,

with floored stable rank one and small fifth cross volume, is controlled despite the fact that `B` is only *approximately* rank four.  The residual cannot be deleted: arbitrary cap-one laws may have unbounded support, and the live correction inbox forbids treating a small operator coefficient as a uniformly small random quadratic perturbation.

The result below makes this endpoint quantitative: the residual has Hilbert--Schmidt and operator norm `< ||B||op/4` while the entire residual is retained in the formulation.  This is a structural reduction, not a proof that the residual is harmless.

## 2. Primary-source transfer: the newest designated partner

The latest completed compatible designated-partner result is fleet03/B18

`QFORM-STABLERANK-CROSS-HS-NEGATIVE-MOMENT-v1`,

at scientific commit `040ad387a0384004f328f6d9342c899ea11a247e`, with checks at `8fc3be74bf627f5a983341fb160e8149e0de3d06`.

Its primary source is Mark Rudelson and Roman Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, IMRN 2015, arXiv:1402.4492v2.  I checked the two source statements actually used.

1. **Theorem 1.2.**  For independent real variables with densities bounded by `K`, every normalized scalar linear combination has density at most `sqrt(2) K` almost everywhere.
2. **Corollary 8.5 / equation (8.12).**  With the paper's floored stable rank

   `r(M)=floor(||M||HS^2/||M||op^2)`,

   independent coordinate densities bounded by `K` satisfy, for every `eps in (0,1)`,

   `L(MY,t||M||HS) <= (C K t/sqrt(eps))^ceil((1-eps)r(M))`.

   The paper explicitly points out that this lossless-power concentration estimate can be used for negative moments.  The concentration function is a supremum over centers, so the translated vector `MY+alpha` is covered.

There are no moment, bounded-support, log-concavity, iid, centering, symmetry, or smoothness hypotheses in these statements.  They are applied only to genuine disjoint original-coordinate product banks.

Fleet03/B18 takes `eps=1/4`, integrates the reciprocal norm, then applies Theorem 1.2 conditionally.  Its ambient corollary is:

> If the ORIGINAL coordinates split as `I sqcup J sqcup K`, `A_II=0`, `B=A_IJ`, and
> `r(B)>=2`, then, with arbitrary remaining blocks and couplings retained,
>
> `||p_{X^TAX}||infinity <= 2 sqrt(2) C_RV / ||B||HS`,               (2.1)
>
> where `C_RV` is the absolute constant in Rudelson--Vershynin (8.12).

No generic continuity claim is part of (2.1).

## 3. The pinned completed receiver used in this run

The required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.  The completed result spent below is the fifth-volume extension `D_5`:

For an arbitrary original-coordinate cut `I sqcup J`, put

`M=A_IJ`, `Z_5=e_5(M^T M)`.

Then, with **no volume-marginal condition at all** and with the diagonal blocks and affine terms arbitrary,

`||p_Q||infinity <= 5 sqrt(2e) Z_5^(-1/10)`.                    (3.1)

This is a whole-line density estimate.  It preserves original-coordinate product structure through the decoupling/Brascamp--Lieb proof; it does not infer independence after any spectral rotation.

The pinned counterexample search reports no QFORM counterexample and leaves convex/two-sheet and diffuse higher-rank geometry open.  That search miss is not used as novelty evidence.

## 4. New deterministic lemma: fifth volume forces rank-four approximation

### Lemma `QFORM-E5-RANK4-TAIL-v1`

Let the singular values of a real matrix `B` be

`sigma_1 >= sigma_2 >= ... >= 0`,

put `x_j=sigma_j^2`,

`Z_5=e_5(B^T B)=e_5(x_1,x_2,...)`,

and define the squared Hilbert--Schmidt tail beyond rank four by

`R_5=sum_{j>=5} sigma_j^2`.

Then

`boxed: Z_5 >= sigma_1^2 (R_5/4)^4`.                            (4.1)

Consequently

`R_5 <= 4 (Z_5/sigma_1^2)^(1/4)`.                              (4.2)

If `B_4` is the rank-four truncated SVD of `B`, then

`||B-B_4||HS^2 = R_5`,

so for every `zeta>0`,

`Z_5 < zeta sigma_1^10`

implies

`||B-B_4||HS < 2 zeta^(1/8) sigma_1`,

and hence also

`||B-B_4||op < 2 zeta^(1/8) sigma_1`.                           (4.3)

In particular, at

`zeta=2^-24`,

`boxed: ||B-B_4||HS < sigma_1/4`,

`boxed: ||B-B_4||op < sigma_1/4`.                               (4.4)

### Proof

We first prove the elementary inequality

`e_4(y_1,y_2,...) >= (R/4)^4`,                                  (4.5)

for every decreasing nonnegative finite sequence `y_1>=y_2>=...`, where

`R=sum_{j>=4} y_j`.

If `y_4>=R/4`, then the single term `y_1 y_2 y_3 y_4` in `e_4(y)` is already at least `(R/4)^4`.

Otherwise `y_4<R/4`.  Normalize the tail `(y_4,y_5,...)/R`.  It has total mass one and every coordinate is at most `1/4`.  The vector

`u=(1/4,1/4,1/4,1/4,0,...)`

majorizes every such normalized tail.  The elementary symmetric polynomial `e_4` is Schur-concave on the nonnegative cone at fixed sum: for a two-coordinate transfer holding `a+b` fixed, its dependence on that pair is

`ab e_2(rest) + (a+b)e_3(rest) + e_4(rest)`,

so making the pair more unequal decreases `e_4`.  Therefore

`e_4((y_4,y_5,...)/R) >= e_4(u)=4^-4`,

which proves (4.5).

Apply (4.5) to `y=(x_2,x_3,...)`.  Since its tail from the fourth coordinate is exactly

`sum_{j>=5}x_j=R_5`,

and

`Z_5=x_1 e_4(x_2,x_3,...)+e_5(x_2,x_3,...)`,

we obtain

`Z_5 >= x_1 (R_5/4)^4`.

This is (4.1), and (4.2)--(4.4) follow immediately. QED.

No residual coefficient has been discarded in this lemma; (4.4) is only a deterministic decomposition certificate.

## 5. Combined target-level funnel

### Theorem `QFORM-ZEROSELF-HS-D5-RANK4-FUNNEL-v1`

Let the full ORIGINAL coordinate set split as `I sqcup J` and write

`A = [[0,B],[B^T,C]]`.

Let

`s=s_3(A)>0`, `c=||C||op`, `beta=||B||op`, `H=||B||HS`,

`r=floor(H^2/beta^2)` for `B!=0`, and

`Z_5=e_5(B^T B)`.

Then the following statements hold.

### (a) Low complementary norm is already paid

If

`c <= s/2`,

then the previous fleet02/B18 complement-norm funnel, combined with the completed two-cross negative-moment receiver, gives

`boxed: ||p_Q||infinity <= 2 sqrt(2pi)/s`.                     (5.1)

The earlier deterministic input was

`sigma_2(B)^2 >= s(s-c)`

whenever `c<s`.

### (b) Small cross operator norm transfers all three large directions to the complement

Let

`A_0=diag(0,C)`.

Since

`||A-A_0||op = || [[0,B],[B^T,0]] ||op = beta`,

singular-value perturbation gives

`s_3(C)=s_3(A_0) >= s_3(A)-beta = s-beta`.                     (5.2)

Thus

`beta < s/2  ==>  s_3(C) > s/2`.                              (5.3)

Conditioning on the original `I` coordinates leaves the `J`-bank form

`X_J^T C X_J + 2(B^T x_I)^T X_J`,

so (5.3) is an exact **affine recursive branch** at half the spectral scale.  I do not count this as paid: a full proof still needs an affine-uniform closure that does not accumulate a dimension-dependent recursion loss.

### (c) Crossing-heavy stable rank at least two is paid by the newest partner

Assume

`beta >= s/2`, `r>=2`.

Apply (2.1).  Since `H>=beta`,

`||p_Q||infinity <= 2 sqrt(2) C_RV/H`

`                    <= 2 sqrt(2) C_RV/beta`

`                    <= 4 sqrt(2) C_RV/s`.                    (5.4)

This is the newest designated-partner theorem used at an actual target-scale inequality.

### (d) Crossing-heavy fifth volume is paid by pinned D5 even when stable rank equals one

Assume

`beta >= s/2`,

and

`Z_5 >= 2^-24 beta^10`.                                       (5.5)

The pinned result (3.1) gives

`||p_Q||infinity <= 5 sqrt(2e) Z_5^(-1/10)`

` <= 5 sqrt(2e) 2^(12/5) beta^-1`

` <= 10 sqrt(2e) 2^(12/5) s^-1`

` = 123.06490715293657... s^-1`.                              (5.6)

This branch has no volume-row-marginal hypothesis.

### (e) The crossing-heavy survivor is a retained rank-four carrier

Suppose neither (c) nor (d) applies while `beta>=s/2`.  Then

`r=1`,

so

`H^2/beta^2 < 2`,

hence

`sum_{j>=2} sigma_j(B)^2 = H^2-beta^2 < beta^2`.               (5.7)

Also

`Z_5 < 2^-24 beta^10`.

By (4.4) there is a rank-at-most-four matrix `B_4` such that, writing

`B=B_4+E`,

we have

`boxed: ||E||HS < beta/4`,

`boxed: ||E||op < beta/4`.                                    (5.8)

If the low-complement branch (a) has also failed, then additionally

`c>s/2`.                                                       (5.9)

Therefore, apart from the explicit affine-recursive branch (b), every zero-self state at target scale is either paid by a whole-line source-preserving theorem or is forced into the quantitative chamber

`boxed: c>s/2, beta>=s/2, r(B)=1, B=B_4+E, rank(B_4)<=4, ||E||HS<beta/4`,  (5.10)

with the residual `E` still present.

This is the promised rank-four funnel.  It does not claim that (5.10) is solved.

## 6. A genuine target family where pinned D5 adds scope beyond the newest stable-rank theorem

Let

`B=diag(1,1/4,1/4,1/4,1/4)`

and use three original-coordinate blocks to define

`A_* = [[0,B,0],[B,0,0],[0,0,1]]`.                             (6.1)

Its spectrum is exactly

`{-1,+1,+1, -1/4 (four copies), +1/4 (four copies)}`.          (6.2)

Hence it belongs to the owner target and has exactly three eigenvalues of modulus at least one.

For its cross block,

`||B||op=1`,

`||B||HS^2 = 1+4/16 = 5/4`,

so the Rudelson--Vershynin floored stable rank is

`r(B)=floor(5/4)=1`.                                           (6.3)

Thus the newest fleet03/B18 stable-rank theorem is **not available** on this family.

But

`Z_5=e_5(B^TB)=1*(1/4)^8=2^-16`.                              (6.4)

The pinned `D_5` theorem applies literally and gives the real whole-line target inequality

`boxed: ||p_{X^T A_* X}||infinity`

` <= 5 sqrt(2e) (2^-16)^(-1/10)`

` = 5 sqrt(2e) 2^(8/5)`

` = 35.34111410111027...`.                                    (6.5)

This is a source-valid closure of a stable-rank-one target family.  It shows that failure of the newest partner gate does not itself identify the obstruction; one must also suppress aggregate fifth cross volume.  Conversely, when that fifth volume is suppressed, Lemma 4 forces concentration into four singular directions plus the explicitly retained residual.

No continuity claim is made for (6.5).

## 7. Why this does not violate the live corrections

The argument never uses post-rotation independence.  Singular vectors appear only in deterministic matrix inequalities and in the definition of a truncated SVD; probabilistic conditioning is always on original coordinate banks.

No arbitrary-joint coarea bound or worst conditional-density-cap replacement is used.  The partner theorem invokes Rudelson--Vershynin only on an original-coordinate product bank; the pinned `D_5` theorem likewise preserves product structure through its decoupling proof.

The small residual `E` in (5.10) is **not deleted** or treated as a small random perturbation.  The correction inbox explicitly forbids that step for arbitrary unbounded cap-one inputs.  Equation (5.8) is only a structural certificate for the next receiver.

No fixed physical minor is asserted.  `Z_5` is an aggregate fifth-volume currency; the entire point of (4.1) is to convert failure of the aggregate receiver into low-rank concentration without selecting one uniformly good coordinate minor.

## 8. Literature scope boundary

Rudelson--Vershynin's Theorem 1.2 and Corollary 8.5 exactly match the independent bounded-density assumptions needed here.  Their constants are source constants; I do not replace the absolute `C_RV` by an invented numerical value.

The pinned e5f result is used at its exact completed scope.  The separate counterexample search's failure to find a counterexample is not a proof of novelty or of the conjecture.

The full unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 9. Sharpened next implication

The next crossing-heavy debt is

`QFORM-ZEROSELF-RANK4-RETAINED-RESIDUAL-BRIDGE-v1`:

starting from (5.10), obtain a universal density bound while retaining both the rank-at-most-four carrier and the residual `E`, or route the configuration into an already-paid physical-pair, grouped-hub, projected-crossing, or square receiver.  Because `||E||op<beta/4` alone gives no probabilistic perturbation control, the bridge has to use `E` structurally rather than discard it.

In parallel, the `beta<s/2` branch (5.3) is an affine-recursive complement with three singular directions at scale `s/2`; a complete proof must close that recursion without a dimension-dependent loss.

Those are precise remaining implications.  Neither is replaced by a search miss or a continuity assertion.
