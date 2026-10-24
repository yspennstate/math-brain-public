SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T10:31:05Z.
attacking: the all-sign pair-free moderate-residual frontier by proving that every physical diagonal of size at least 1/64 lies in one sign-coherent multiplicative rank-one chamber, with every frustrated heavy triangle paid by a pinned localized 3D theorem.

# account02/B20 r53 — large-diagonal sign balance and frustrated-triangle closure

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-LEVEL STRUCTURAL CLOSURE / FRUSTRATED HEAVY TRIANGLES PAID / BALANCED HEAVY RANK-ONE TUBE / FULL QFORM OPEN**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Authenticated repository retrieval/writeback occurred; no native learned-memory receiver ingestion was exposed.

All coordinate sets below are literal ORIGINAL-coordinate sets. No random coordinate is rotated. Coordinate sign switches, when mentioned, are only independent reflections of original coordinates and preserve the product density-cap hypothesis. No Gaussianity, log-concavity, moments, compact/connected support, iid hypothesis, arbitrary-joint coarea, worst-fibre supremum, conditional density-cap inheritance after projection, law-uniform pointwise quadratic-phase decay, or deletion of nonzero coefficient tails is used.

## 1. Fresh source-pinned inputs and current frontier

Fresh owner controls were read from `yspennstate/math-research-brain/main`; OWNER CONTROL remained revision `2026-09-22.15`, QFORM remained the sole active programme, and no later stop/reassignment of account02/B20 was found at startup.

The newest compatible completed designated partner was account03/B20 r51:

`yspennstate/math-open-problems@ceb973b9c1549a8247baf169db9152844b9decde`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T091209Z-account03-B20-QFORM-auto11-r51/REPORT.md`.

Its headline Schur compression says that on its strong-edge survivor, with `tau=2^-20`,

`s_5(S)<36 tau=9/262144`,

and the full coefficient matrix is rank at most six plus a retained operator tail `<9/262144`. More importantly for the present global synthesis, the same literal original-coordinate strong pair has the exact quantitative thresholds

`D0=9.530157744638501e-7 < 2^-20`,

`kappa0=6.075614261408114e-5 < 2^-14`.

The preceding account02/B20 r52 proved the complementary definite-pair receiver and combined it with the arbitrary-rank indefinite-pair theorem. Therefore every still-unpaid target instance satisfies the **all-sign physical-pair gate**:

* every invertible definite physical principal pair `B` has `|det B|<D0`;
* every invertible indefinite physical principal pair `B` has `|det B|<D0` or `s_min(B)<kappa0`.

If either gate fails, the full ambient law is already paid (`<3219` in the definite case and `<9763` at the stated indefinite thresholds). This applies the partner's exact pair expression directly; the partner's later rank-six retained-tail endpoint is not an additional unpaid leaf.

The inherited separate moderate-residual frontier remains

`A_light=diag(q)+K_12+F`, `rank K_12<=12`, `||F||op<2.1455152587890625`,

or on determinant collapse

`rank K_11<=11`, `||F_collapse||op<2.1456220703125`,

with actual row-small residuals, retained nonzero tails, and the physical D5 failures from r52. The new theorem below constrains the **actual large physical diagonals of A** before one attempts the next joint Fresnel/BL payment.

The owner-required pinned package was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its localized Theorem A is spent in Section 4 and its Theorem F is spent on the stress family in Section 7. Its marginal-free D5 theorem is also re-applied to the live residual-bank cuts in Section 8.

## 2. Opposite-sign heavy physical diagonals are terminal

Fix

`a=2^-6=1/64`,

and let

`H={i: |A_ii|>=a}`.

### Lemma 2.1 — `QFORM-R53-HEAVY-DIAGONAL-COMMON-SIGN-v1`

Every still-unpaid target instance has one common sign on all nonempty entries `A_ii`, `i in H`.

#### Proof

Suppose `A_ii=x>0` and `A_jj=-y<0`, with `x,y>=a`. For the literal physical pair

`B=[[x,b],[b,-y]]`,

`|det B|=xy+b^2>=a^2=2^-12>D0`.

Its two eigenvalues have opposite signs. Writing

`Delta=sqrt((x+y)^2+4b^2)`,

the smaller singular value is

`s_min(B)=(Delta-|x-y|)/2 >= (x+y-|x-y|)/2=min(x,y)>=2^-6>kappa0`.

Thus `B` violates the unpaid indefinite-pair gate and would already pay the full law. Contradiction. QED.

This is an exact target-level sign restriction. It does not say A is semidefinite: all sign-changing spectrum may still be carried by zero/small diagonal coordinates and off-diagonal blocks.

## 3. Every heavy-heavy pair lies in a multiplicative rank-one tube

Let `s in {+1,-1}` be the common sign from Lemma 2.1 and put `d_i=|A_ii|` for `i in H`. For distinct `i,j in H`, define

`r_ij = s A_ij/sqrt(d_i d_j)`.

### Lemma 3.1 — `QFORM-R53-HEAVY-PAIR-MULTIPLICATIVE-TUBE-v1`

For every still-unpaid target instance and every distinct `i,j in H`,

`boxed: 1-2^-8 < |r_ij| < 1+2^-8.`

#### Proof

Multiplying a physical pair by the common sign `s` preserves its determinant magnitude and singular values, so consider

`B=diag(sqrt(d_i),sqrt(d_j)) [[1,r],[r,1]] diag(sqrt(d_i),sqrt(d_j))`.

If `|r|<1`, the pair is definite. The unpaid definite-pair gate gives

`d_i d_j(1-r^2)<D0`,

hence

`1-|r| <=1-r^2 < D0/(d_i d_j) <=D0/a^2 <2^-8`.

If `|r|>1` and `d_i d_j(r^2-1)<D0`, then similarly

`|r|-1<r^2-1<D0/a^2<2^-8`.

Finally suppose `|r|>1` and `d_i d_j(r^2-1)>=D0`. The unpaid indefinite-pair gate forces `s_min(B)<kappa0`. But the singular-value product inequality under the displayed congruence gives

`s_min(B)>=min(d_i,d_j) s_min([[1,r],[r,1]])`
`        =min(d_i,d_j)(|r|-1)`.

Therefore

`|r|-1 < kappa0/min(d_i,d_j) <=kappa0/a <2^-8`.

The source inequalities `D0<2^-20` and `kappa0<2^-14` make both comparisons exact at `a=2^-6`. QED.

Thus large same-sign diagonals cannot behave as a sparse diagonal block in an unpaid state: every heavy-heavy physical edge has essentially the geometric-mean magnitude.

## 4. A frustrated heavy triangle is fully paid

Set `epsilon=2^-8=1/256`.

### Theorem 4.1 — `QFORM-R53-FRUSTRATED-HEAVY-TRIANGLE-CLOSURE-v1`

Suppose three indices `i,j,k in H` have

`sign(r_ij r_ik r_jk)=-1`.

Then their literal physical `3 x 3` principal block has every eigenvalue of absolute value at least

`c0=676783/99123200 >0.00682769`,

and the **full ambient quadratic law** satisfies

`boxed: ||p_Q||_infinity <1558.`

#### Proof

Normalize the common diagonal sign and magnitudes:

`C=D^(-1/2) (s A[{i,j,k},{i,j,k}]) D^(-1/2)`,

where `D=diag(d_i,d_j,d_k)`. Then `C` has diagonal entries one and off-diagonal entries `r_ij,r_ik,r_jk`. Lemma 3.1 gives

`1-epsilon<|r_ab|<1+epsilon`.

For a frustrated sign product,

`det C =1+2 r_ij r_ik r_jk-r_ij^2-r_ik^2-r_jk^2`

obeys

`|det C| >= gamma`

with

`gamma=2(1-epsilon)^3+3(1-epsilon)^2-1`
`     =33162367/8388608`.

Also

`||C||op <= max row sum <3+2epsilon=385/128`.

Hence, since the product of the three singular values is `|det C|`,

`s_min(C)>= gamma/(3+2epsilon)^2`
`        =676783/1548800`.

Congruence by `D^(1/2)` gives

`s_min(A[{i,j,k}])>=min(d_i,d_j,d_k) s_min(C)`
`                  >=2^-6 *676783/1548800`
`                  =c0`.

Now condition on every original coordinate outside this literal triple. The remaining polynomial is a three-variable quadratic form with arbitrary induced linear term and a symmetric coefficient matrix whose three eigenvalues have modulus at least `c0`. The localized Theorem A in the pinned `COUNTEREXAMPLE_SEARCH.md` applies exactly and yields

`||p_Q||_infinity <=6 sqrt(pi)/c0 <1558`.

For a fully rational safety check, `pi<22/7` still gives `<1558`. QED.

No arbitrary three-dimensional joint-density coarea statement is used: after conditioning, these are the original three independent coordinates.

## 5. Every unpaid heavy block is sign-balanced and rank-one-like

### Corollary 5.1 — `QFORM-R53-BALANCED-HEAVY-RANKONE-TUBE-v1`

For every still-unpaid target instance there are signs `sigma_i in {+1,-1}`, `i in H`, such that for all distinct `i,j in H`,

`boxed:`
`| A_ij - s sigma_i sigma_j sqrt(d_i d_j) |`
`    < 2^-8 sqrt(d_i d_j).`

The diagonal entries satisfy exactly `A_ii=s d_i=s(sigma_i sqrt(d_i))^2`.

#### Proof

If `|H|<=2`, choose the signs directly. If `|H|>=3`, Theorem 4.1 says every unpaid triangle has positive product of the normalized edge signs. Fix a root `h`, set `sigma_h=1` and `sigma_i=sign(r_hi)`. Positivity of every triangle `(h,i,j)` gives `sign(r_ij)=sigma_i sigma_j`. Lemma 3.1 then supplies the magnitude estimate. QED.

Equivalently, after only physical coordinate reflections and an optional global output sign, the heavy principal block is entrywise in a `1/256` multiplicative tube around `u u^T`, `u_i=sqrt(d_i)`.

A useful deterministic operator statement follows. If

`R_H = s Sigma A[H,H] Sigma - u u^T`,

then `R_H` has zero diagonal and

`|(R_H)_ij|<2^-8 u_i u_j`,

so

`boxed: ||R_H||op <2^-8 sum_{i in H} d_i.`

This is coefficient geometry only. It is **not** interpreted as a uniformly small random quadratic perturbation, because the heavy diagonal mass can be arbitrarily large.

## 6. One heavy scalar pivot almost annihilates heavy-heavy curvature

The preceding balance has a useful Schur form. Work after the harmless coordinate reflections/global sign of Corollary 5.1, and choose any hub `h in H`. Write each normalized heavy edge as

`A_ij=sqrt(d_i d_j)(1+delta_ij)`, `|delta_ij|<epsilon`.

After completing the scalar square at `h`, the exact Schur complement restricted to `H\{h}` satisfies

`S_ii=d_i[1-(1+delta_ih)^2]`,

`S_ij=sqrt(d_i d_j)[(1+delta_ij)-(1+delta_ih)(1+delta_hj)]`.

Therefore

`boxed: |S_ii| < (2epsilon+epsilon^2)d_i =513/65536 d_i,`

`boxed: |S_ij| < (3epsilon+epsilon^2)sqrt(d_i d_j) =769/65536 sqrt(d_i d_j).`

In particular

`boxed: ||S[H\{h},H\{h}]||op <(769/65536) sum_{i in H\{h}} d_i.`

This is a source-preserving route from a large-diagonal chamber to an almost-annihilated heavy self block after one **physical** scalar pivot. The outside light coordinates and every cross coupling remain present and are the next smoothing resource; no post-rotation independence is claimed.

## 7. Exact stress: the balanced heavy chamber is non-vacuous

The stronger shortcut “the all-sign pair-free target forces all diagonals below `1/64`, or bounds the total heavy diagonal mass” is false.

For arbitrary `L>=1` and `m>=2048`, let `w=1_64/8` and let `u,v` be flat unit vectors on two disjoint `m`-coordinate banks. Define

`A_{L,m}=L w w^T direct_sum [[0,u v^T],[v u^T,0]].`

Its nonzero spectrum is exactly

`{L,1,-1}`,

so it satisfies the full three-large-eigenvalue target. Its first 64 physical diagonals equal `L/64`, hence can be arbitrarily large. Every physical pair within that heavy block is singular rank one; pairs between that block and the two diffuse banks are singular; and every invertible pair across the two diffuse banks has

`|det|=1/m^2 <=1/2048^2=2.384185791015625e-7<D0`.

Thus the family survives the all-sign pair-free gate and sits exactly at `r_ij=1` in the balanced chamber. It is a counterexample to the stronger structural shortcut, **not** to QFORM.

Indeed the pinned `RESULTS.md` Theorem F applies directly to this exact rank-three coefficient matrix. The three eigenspace leverage is `1/64` on the heavy block and `1/m` on either diffuse bank, hence at most `1/64<1/2`. Therefore for every independent cap-one product input law,

`boxed: ||p_Q||_infinity <=12 (L*1*1)^(-1/3) <=12.`

This is an equation-level use of the required pinned completed result and also shows why the next step must exploit balanced aggregate geometry rather than force a single good pair.

## 8. Pinned fifth-volume exit remains active on the actual residual cuts

On each literal residual-bank MSS cut `I,J` inherited from r52, set

`Z5=e_5(A[I,J]^T A[I,J])`.

The pinned `FOURIER_ROUTE_REPORT.md` Theorem D5 is marginal-free:

`||p_Q||_infinity <=5 sqrt(2e) Z5^(-1/10)`.

Hence

`Z5>=1/1024`

implies

`boxed: ||p_Q||_infinity <=10 sqrt(2e)<23.317.`

Every still-unpaid state can therefore retain the already-recorded `Z5<1/1024` failures on the two actual residual-bank cuts while adding the new balanced-heavy constraints above.

## 9. Sharpened first unpaid implication

The first current synthesis debt is now

`QFORM-R53-BALANCED-HEAVY-R1-PLUS-PAIRFREE-MODERATE-RESIDUAL-JOINT-PAYMENT-v1`.

Full hypotheses are the original target quantifiers plus the already-source-pinned survivor gates:

* `s_3(A)>=1` in singular-value notation (at least three eigenvalues of absolute value at least one);
* independent original coordinates with densities at most one, no regularity/moment/support assumptions;
* all-sign physical-pair gate at the exact `(D0,kappa0)` thresholds above;
* the r52 moderate residual carrier/tail forms and their actual physical D5 failures;
* no nonzero coefficient tail deleted;
* heavy set `H={|A_ii|>=1/64}` having one common sign and, after physical coordinate reflections, the pairwise multiplicative tube
  `|A_ij-sqrt(d_i d_j)|<2^-8 sqrt(d_i d_j)`;
* after any heavy physical scalar pivot, the exact heavy-heavy Schur block obeying the `513/65536` diagonal and `769/65536` off-diagonal normalized bounds above.

The next mechanism should combine this balanced rank-one-like heavy chamber with the diffuse moderate residual/crossing resource through a grouped-hub, projected-crossing or joint Fresnel/BL estimate. The stress family in Section 7 rules out replacing that joint argument by a claim that the heavy set or its diagonal mass is bounded.

This is a genuinely narrower endpoint than r52: opposite-sign heavy diagonals, non-geometric heavy edges, and every frustrated heavy triangle are now fully paid or impossible in an unpaid state.

## 10. Status and corrections

Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. No valid counterexample to the owner target was found. Unrestricted continuity remains separately **OPEN**.

Preserved corrections: no law-uniform pointwise quadratic-phase decay; no worst-fibre or conditional-cap transfer; no arbitrary-joint rank-three coarea; no post-rotation independence; no deletion of nonzero coefficient tails; no generic fractional-small-ball-to-`L^infinity` interpolation; small operator coefficient error is not treated as a small random quadratic error on arbitrary unbounded product inputs.

This run is not a full candidate proof, so the two-independent-end-to-end-review requirement is not triggered.
