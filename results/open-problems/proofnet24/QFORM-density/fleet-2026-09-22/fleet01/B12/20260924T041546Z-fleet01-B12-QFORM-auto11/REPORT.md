# fleet01/B12 — two-sided spectral-cover stability and matroid dichotomy

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **new proved supporting stability theorem plus one refuted intermediate extraction; unrestricted QFORM remains OPEN / NOT PROVED / NOT DISPROVED**.

Execution context: `WITHOUT_VERIFIED_BRAIN`. No spectral rotation of the random input is used anywhere below.

## 1. First missing implication attacked

The previous B12 runs produced one-sided carrier, Schur, Woodbury, resonance-repair and protected-domain stability statements. The first remaining local question is whether a large signed spectral packet can be made harmless simultaneously from the row and column sides of an ORIGINAL-coordinate cross block, without paying its amplitudes. This report proves an exact two-sided answer and identifies the precise linear-algebra obstruction by a vector-matroid min-max identity.

The global implication from only `s3(A)>=1` remains unpaid.

## 2. Theorem: QFORM-TWO-SIDED-SPECTRAL-COVER-STABILITY-v1

Let `I,J` be disjoint sets of ORIGINAL coordinates and let

`A = A0 + E_hi + E_lo + T`

be real symmetric. Write the arbitrary signed rank-one packet

`E_hi = sum_{alpha in Gamma} theta_alpha v_alpha v_alpha^T`,

where every `theta_alpha` is an arbitrary real number; no bound on sign or magnitude is imposed. (For a genuine spectral slice, the `v_alpha` are orthonormal, but the proof does not need orthogonality.) Put

`a_alpha = P_I v_alpha in R^I`, `b_alpha = P_J v_alpha in R^J`.

Assume there are subspaces `L subset R^I`, `R subset R^J` such that for every `alpha`,

`a_alpha in L` OR `b_alpha in R`.

Let `U` and `V` be isometries onto `L^perp` and `R^perp`, respectively. Then

`boxed: U^T E_hi[I,J] V = 0.`

Indeed, the `alpha` term is

`theta_alpha (U^T a_alpha)(b_alpha^T V)`,

and one of its two factors is zero by the cover condition.

Assume further

`||E_lo||op <= h`, `||T[I,J]||op <= delta`.

Then for every admissible singular index `k`,

`boxed: s_k(A[I,J]) >= [s_k(U^T A0[I,J] V)-h-delta]_+.`

### Proof

The protected compression satisfies

`U^T A[I,J] V = U^T A0[I,J]V + U^T(E_lo+T)[I,J]V`.

Because `U,V` are contractions,

`||U^T E_lo[I,J]V||op <= ||E_lo||op <= h`

and

`||U^T T[I,J]V||op <= ||T[I,J]||op <= delta`.

Singular-value Weyl gives

`s_k(U^T A[I,J]V) >= s_k(U^T A0[I,J]V)-h-delta`.

Finally, a left/right compression by contractions cannot increase any singular value, hence

`s_k(A[I,J]) >= s_k(U^T A[I,J]V)`.

This proves the claim.

### High/low eigenvalue compiler

If `E_lo` is the spectral slice consisting of all eigenvalues of a remainder whose magnitudes are at most `h`, then automatically `||E_lo||op<=h`, irrespective of the number, signs, multiplicities, supports or orientations of those eigenvectors. Thus:

* every high mode covered on at least one physical side is **exactly free**, no matter how large or of which sign;
* every remaining small eigenvalue is paid all at once by the single threshold `h`;
* only the actual local action `||T[I,J]||op` of any further tail is charged.

No statement is made that `X^T E_lo X` is a small random variable; it need not be.

## 3. Exact cover number = simultaneous left/right independence number

For the high packet define

`c(I,J;Gamma) = min_{Gamma_L disjoint_union Gamma_R = Gamma} [ rank{a_alpha: alpha in Gamma_L} + rank{b_alpha: alpha in Gamma_R} ].`

For a chosen partition, taking

`L=span{a_alpha: alpha in Gamma_L}` and `R=span{b_alpha: alpha in Gamma_R}`

is exactly a two-sided cover, so `c` is the minimum total cover dimension.

Let `M_L,M_R` be the two vector matroids on `Gamma`, with independence meaning linear independence of the `a_alpha` and `b_alpha` families. Edmonds' matroid-intersection min-max theorem gives the exact identity

`boxed: c(I,J;Gamma) = max{|S| : {a_alpha}_{alpha in S} and {b_alpha}_{alpha in S} are both linearly independent}.`

Thus for every integer `r` there is an exact dichotomy:

1. `c<=r`: all high modes admit a two-sided footprint cover of total dimension at most `r`, so the theorem above deletes them exactly while sacrificing only those physical dimensions; or
2. `c>=r+1`: there are `r+1` high modes whose left and right physical projections are simultaneously independent.

This is a useful structural reduction because the number of high eigenvalues can be arbitrarily large while the cover branch pays only the vector-matroid cover number, not the spectral amplitudes.

## 4. Important failure: the bi-independent branch is NOT yet a cross-volume certificate

A tempting next inference is false: a bi-independent set of `k` spectral modes does **not** imply that the aggregate high spectral packet has cross rank `k` or nonzero `k`-volume.

Take `I=span(e_1,...,e_k)`, `J=span(f_1,...,f_k)` and the `2k` orthonormal vectors

`v_j^+ = (e_j+f_j)/sqrt(2)`, `v_j^-=(e_j-f_j)/sqrt(2)`, `j=1,...,k`,

all with eigenvalue `+1`. Then

`sum_j (v_j^+ (v_j^+)^T + v_j^- (v_j^-)^T) = I_(I direct_sum J)`,

so its aggregate `I x J` cross block is exactly zero. Nevertheless the subset `{v_1^+,...,v_k^+}` has linearly independent left projections and linearly independent right projections, hence the common-independence number is at least `k` (in fact exactly `k`).

For `k=5`, this gives five simultaneously bi-independent large eigenmodes but zero fifth cross volume. Therefore the no-small-cover branch cannot be sent directly to D5. One must retain the same-bank curvature / paired spectral cancellation structure or use another already-paid receiver. This example is inside the owner target (`A=I_10`) and is NOT a counterexample to QFORM; it refutes only the intermediate cross-volume inference.

## 5. End-to-end conditional density corollary

Consume the completed designated-partner report

`yspennstate/math-open-problems@e922248c12820c303861233f1a626fdf9aae9687`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260924T040832Z-fleet02-B12-QFORM-auto11/REPORT.md`.

Its original-coordinate D5 corollary states: if an actual final cross block on disjoint original-coordinate banks has

`s5(A[I,J]) >= g > 0`,

then for every independent cap-one product input,

`boxed: ||p_(X^T A X)||infinity <= 5 sqrt(2e)/g`,

and this D5 branch has a continuous `C_0` density representative.

Combining with the two-sided cover theorem gives the complete conditional implication

`g0 := s5(U^T A0[I,J]V) > h+delta`

`=> boxed: ||p_Q||infinity <= 5 sqrt(2e)/(g0-h-delta).`

This retains arbitrary same-bank blocks, arbitrary exterior couplings and arbitrary signed high spectral amplitudes satisfying the cover condition. It never declares rotated spectral coordinates independent.

## 6. Actual inequality / target-class stress family

Take disjoint original-coordinate banks

`I={i1,...,i7}`, `J={j1,...,j7}`,

`L=span(e_i6,e_i7)`, `R=span(e_j6,e_j7)`.

Let the baseline cross block satisfy

`A0[i_r,j_r]=A0[j_r,i_r]=2`, `r=1,...,5`,

with no restriction needed on other baseline same-bank/exterior entries for the D5 receiver. Then on the protected complements,

`U^T A0[I,J]V = 2 I_5`, so `g0=2`.

Now add any signed high packet whose every mode obeys

`P_I v_alpha in L` OR `P_J v_alpha in R`.

The amplitudes may be independently positive or negative and arbitrarily large. Add an arbitrary-rank small signed spectral packet with

`||E_lo||op <= 1/8`

and any further symmetric tail satisfying only

`||T[I,J]||op <= 1/8`.

The theorem gives the actual final-matrix inequality

`boxed: s5(A[I,J]) >= 2-1/8-1/8 = 7/4.`

Applying the completed fleet02/B12 D5 corollary at this exact inequality gives

`boxed: ||p_Q||infinity <= 5 sqrt(2e)/(7/4) = 20 sqrt(2e)/7 = 6.661839947420355... .`

The density has a continuous `C_0` representative in this branch.

Also a submatrix singular value cannot exceed the corresponding singular value of the full symmetric matrix, so

`s5(A) >= s5(A[I,J]) >= 7/4 > 1`.

Hence every member of this family lies literally inside the owner's exact target class with at least three eigenvalues of absolute value at least one.

A concrete nontrivial covered high packet is obtained from the four mutually orthogonal vectors

`(e_i6+e_j1)/sqrt(2)`, `(e_i7+e_j2)/sqrt(2)`, `(e_i1+e_j6)/sqrt(2)`, `(e_i2+e_j7)/sqrt(2)`,

with arbitrary signed amplitudes. The first two are killed by the left annihilator, the last two by the right annihilator. Arbitrarily many further spectator eigenmodes may be appended outside the two banks.

## 7. Sanity checks

The cover identity itself is exact term by term. Separately, a finite brute-force check of the vector-matroid identity on 100 random six-element rational/integer vector systems verified

`min_S [r_L(S)+r_R(E\S)] = max common-independent cardinality`

in every instance. This finite computation is only a check; the proof of the equality is the standard matroid-intersection theorem.

## 8. Remaining gap

This run closes the **small two-sided footprint-cover** branch and identifies the exact obstruction by a common-independence number. It also kills the naive idea that the opposite branch automatically yields a D5 cross-volume certificate: Bell-paired orthogonal eigenmodes can have common-independence number five while their aggregate cross block is exactly zero.

The full conjecture is therefore still open. The next structural step must exploit the cancellation information itself: in the no-small-cover branch, either paired spectral cancellation creates quantitative same-bank curvature that enters a physical-pair/Schur/grouped-hub receiver, or a genuinely uncancelled exterior volume must survive. Proving that exhaustive alternative from only `s3(A)>=1` is not done here.

## 9. Scope / correction guard

No pointwise van-der-Corput decay, arbitrary-joint coarea bound, conditional-density moment, naive fiber supremum, rotated-coordinate independence, or Monte Carlo extremality is used. The Bell example is an exact algebraic warning, not a QFORM counterexample.

Essential boundedness is proved under the stated two-sided cover certificate; continuity is proved there only because the consumed D5 receiver is Fourier-integrable. Unrestricted continuity remains OPEN.
