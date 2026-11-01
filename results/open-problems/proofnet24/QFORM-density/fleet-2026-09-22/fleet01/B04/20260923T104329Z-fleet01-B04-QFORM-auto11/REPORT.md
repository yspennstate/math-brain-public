SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T10:43:29Z.
attacking: convert fleet02/B04's exact two-disjoint-base support criterion into an explicit q=1 determinant/entropy currency by complement-Hellinger symmetrization on six physical rows, then apply it to a genuinely rotated indefinite target matrix.

# fleet01/B04 — six-row complement-Hellinger volume compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Outcome:** `SUPPORTING_THEOREM_PROVED / PARTNER_APPLIED / EXPLICIT_TARGET_ESTIMATE / FULL_TARGET_OPEN`.  
**Continuity:** proved in the theorem below through the imported integrable-characteristic-function estimate; full-target continuity remains open.  
**Execution memory status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact gap attacked

The newest fleet02/B04 result `QFORM-THIRDVOLUME-Q1-BASEPACKING-v1` gives an exact support criterion: a rank-at-least-three physical row matroid admits a probability law on nonzero physical `3x3` minors with every row inclusion marginal at most `1/2` iff it has two disjoint row bases. Its first unpaid implication was quantitative: even when two disjoint bases exist, determinant/entropy currency might be tiny.

This run pays that quantitative step without selecting a single column minor. It aggregates all column lifts of each row base by Cauchy--Binet and then aggregates all complementary base pairs inside six physical rows by a Hellinger/geometric-mean symmetrization.

The full QFORM conjecture remains open because the bare three-large-eigenvalue hypothesis has not been shown to force this new currency at universal scale, nor has tiny currency yet been routed exhaustively into a completed hub/ridge/pair branch.

## 2. Sources actually used at equations

1. **Designated partner fleet02/B04.** `QFORM-THIRDVOLUME-Q1-BASEPACKING-v1`, source `yspennstate/math-open-problems@cf648c06ce0b8ffeb9f62838dee132c0ca41598b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/fleet02-B04-20260923T094548Z-auto11/REPORT.md`. It proves that a q=1 row-marginal support weight exists iff the rank-three row matroid contains two disjoint bases.

2. **Weighted sharp product-Fourier theorem.** `QFORM-WEIGHTED-FRACTIONAL-VOLUME-SHARP-v1`, read at `yspennstate/math-open-problems@b967ff246e7e5b480b098c17f01cd0fc93072991`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/20260923T014717Z-fleet02-B04-QFORM-auto11-cont/REPORT.md`. For any probability weight `w` on nonzero physical `3x3` minors, with row marginals `alpha_i<=q/2`, `1<=q<3/2`, and

`G(w)=exp(H(w)+sum_w log det(M_ST)^2)`, 

it proves

`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] G(w)^(-1/6)`.

Its scope retains arbitrary same-bank quadratic terms, outside couplings and affine terms in original coordinates. The characteristic function is integrable, so the density is continuous and vanishes at infinity.

3. **Newest Claude Fourier source actually applied.** Claude/e5 Theorem D and its arbitrary-weight/KL remark, `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`. At the q=1 marginal gate the same constructed weight below gives the older explicit bound `6 sqrt(e) G(w)^(-1/6)`; the sharp theorem in item 2 improves its coefficient.

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea estimate, conditional spectral-fiber cap, or universally good single physical minor is used.

## 3. New theorem: complement-Hellinger q=1 compiler

Let `I,J` be disjoint ORIGINAL coordinate banks and let `M=A[I,J]`. Fix a six-element set of physical rows `R subset I`. For every three-set `S subset R`, define the aggregate row-base volume

`a_S := sum_{T subset J, |T|=3} det(M[S,T])^2`
`     = det(M[S,J] M[S,J]^T)`,                              (3.1)

where the second identity is Cauchy--Binet. Write `Sbar=R\S` and define

`C_R(M) := sum_{S subset R, |S|=3} sqrt(a_S a_Sbar)`.        (3.2)

### Theorem `QFORM-SIXROW-COMPLEMENT-HELLINGER-VOLUME-v1`

If `C_R(M)>0`, then for every admissible independent cap-one product input law, in the full weighted-three-volume scope including arbitrary same-bank quadratic terms, outside couplings and affine terms,

`boxed( ||p_Q||_inf <= 3e C_R(M)^(-1/6) ).`                  (3.3)

The proof gives an integrable characteristic function and therefore a representative `p_Q in C_0(R)`.

### Proof

For every `S` with `a_S a_Sbar>0`, put

`mu(S) = sqrt(a_S a_Sbar)/C_R(M)`,                            (3.4)

and put `mu(S)=0` otherwise. Since the summand in (3.2) is complement invariant,

`mu(S)=mu(Sbar)`.                                              (3.5)

Fix any physical row `i in R`. In every complementary pair `{S,Sbar}`, exactly one member contains `i`; equal mass on the two members therefore gives

`P_mu(i in S)=1/2`.                                           (3.6)

Rows outside `R` have marginal zero. Thus the q=1 Fourier marginal gate is met exactly.

Conditional on a row triple `S`, choose a column triple `T` according to

`q_S(T)=det(M[S,T])^2/a_S`.                                  (3.7)

This is a probability law on nonzero column lifts of `S`. Let `w(S,T)=mu(S)q_S(T)`. For fixed `S`, the Gibbs identity gives

`H(q_S)+sum_T q_S(T) log det(M[S,T])^2 = log a_S`.            (3.8)

Hence the determinant/entropy currency of the full minor law is

`log G(w)=H(mu)+sum_S mu(S) log a_S`.                          (3.9)

Using (3.4),

`H(mu)+sum_S mu(S)log a_S`
` = log C_R + (1/2) sum_S mu(S) log(a_S/a_Sbar)`
` = log C_R`,                                                  (3.10)

because the last sum cancels pairwise by (3.5). Therefore

`boxed( G(w)=C_R(M) ).`                                       (3.11)

Apply the weighted sharp theorem at `q=1`; (3.6) and (3.11) give (3.3). Its Fourier inversion proof gives continuity and vanishing at infinity. QED.

The same constructed `w` also lies exactly in Claude/e5 Theorem D's q=1 gate, so that completed Claude result yields the actual inequality

`||p_Q||_inf <= 6 sqrt(e) C_R(M)^(-1/6)`.                    (3.12)

Equation (3.3) is the sharp-Hausdorff--Young refinement on the identical weight.

## 4. Exact Hellinger/KL interpretation

Put

`Z_R=sum_S a_S`, `p_R(S)=a_S/Z_R`, `p_R^c(S)=p_R(Sbar)`.

Then

`boxed( C_R/Z_R = sum_S sqrt(p_R(S)p_R^c(S)) )`,              (4.1)

so the relative currency is exactly the Bhattacharyya/Hellinger affinity between the canonical row-volume law and its complement image. The law (3.4) is their normalized geometric mean. Directly,

`boxed( D_KL(mu||p_R)=log(Z_R/C_R) ).`                         (4.2)

Thus (3.3) can be written

`||p_Q||_inf <= 3e Z_R^(-1/6) exp(D_KL(mu||p_R)/6)`.          (4.3)

Also, since `sum sqrt(pq) >= sum min(p,q)=1-TV(p,q)`, if

`TV(p_R,p_R^c)<=delta<1`,

then

`C_R >= (1-delta)Z_R`                                         (4.4)

and

`||p_Q||_inf <=3e[(1-delta)Z_R]^(-1/6)`.                      (4.5)

This isolates the precise cost of complement imbalance rather than paying a reciprocal individual minor.

## 5. Exact application of the partner support theorem

A summand in (3.2) is positive exactly when both `S` and `Sbar` are rank-three physical row bases. Hence

`C_R(M)>0  <=>  R contains two disjoint row bases`.            (5.1)

The designated partner theorem now gives the global support equivalence

`there exists some q=1 supported minor weight`
` <=> there exists a six-row R with C_R(M)>0`.                 (5.2)

This is an actual use of the partner theorem: its qualitative base-packing exit is compiled into the quantitative product-Fourier inequality (3.3).

As a calibration, apply (3.2) to the partner's own latest `6x6` signed-pair example. It has eight nonzero row bases, and after summing its eight unit column-minor squares each has `a_S=8`. Therefore `C_R=64`, and (3.3) gives

`||p_Q||_inf <=3e*64^(-1/6)=3e/2`,                            (5.3)

exactly reproducing the partner report's globally optimal supported weighted-volume certificate on that matrix.

## 6. Genuinely rotated indefinite target matrix

Let

`U = [[sqrt(3)/2,0,0],
      [1/2,0,0],
      [0,1/sqrt(2),0],
      [0,1/sqrt(2),0],
      [0,0,1/sqrt(2)],
      [0,0,1/sqrt(2)]]`,

`V=(1/7)[[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`,

and `D=diag(4,2,1)`. Then `U^T U=I_3`, `V^T V=I_3`, `det V=-1`. Put

`M=UDV^T`, `A=[[0_6,M],[M^T,0_3]]`.                            (6.1)

Every one of the 18 physical entries of `M` is nonzero. The singular values of `M` are exactly `4,2,1`, so

`spec(A)={+4,+2,+1,-1,-2,-4,0,0,0}`.                          (6.2)

Thus this is a genuinely non-diagonal indefinite original-coordinate target matrix with six eigenvalues of modulus at least one.

Take `R={1,...,6}`. The only nonzero row triple volumes are

`a_{ {1,i,j} }=12`, `a_{ {2,i,j} }=4`,

for `i in {3,4}`, `j in {5,6}`. Therefore

`Z_R=64`,                                                       (6.3)

while each of the four unordered complementary base pairs has geometric mean `sqrt(12*4)=4sqrt(3)`, so

`boxed( C_R=32sqrt(3) )`.                                     (6.4)

The canonical row-volume law has physical marginals

`(3/4,1/4,1/2,1/2,1/2,1/2)`.                                 (6.5)

Hence the unmodified canonical law is outside **every** admissible sharp-q gate `q<3/2`: its first marginal would require `q>=3/2`. In contrast, the complement-Hellinger law is simply uniform on the eight nonzero row bases and has every row marginal exactly `1/2`.

The new all-product-law estimate is therefore

`boxed( ||p_(X^T A X)||_inf`
`       <=3e(32sqrt(3))^(-1/6)`
`       =4.17635398765184... ).`                              (6.6)

The density is continuous and vanishes at infinity. The same actual weight in Claude/e5 gives

`||p||_inf <=6sqrt(e)(32sqrt(3))^(-1/6)`
`          =5.066173478647916...`.                            (6.7)

At q=1 the sharp theorem's characteristic-function envelope also yields the explicit integrated estimate

`||phi_Q||_1 <= 6 pi e (32sqrt(3))^(-1/6)`
`            =26.240806012794916...`.                         (6.8)

For comparison, using only one complementary pair of bases gives currency `8sqrt(3)` and bound `5.261876300854946...`. Entropy-aggregating all four complementary pairs improves the certificate by the exact factor

`4^(1/6)=2^(1/3)=1.2599210498948732...`.                       (6.9)

This improvement comes from product-space volume aggregation, not a selected tiny physical minor.

## 7. What is newly paid and what remains

The partner's support statement left two distinct debts: existence of q=1 support and quantitative determinant/entropy size. On every six-row two-base packet, the second debt is now represented by one exact invariant `C_R`: all column lifts and all complementary base pairs are aggregated before Fourier inversion.

The next exact missing implication is

`QFORM-SIXROW-HELLINGER-CURRENCY-OR-SUPPORTDEFECT-ROUTING-v1`:

> Starting only from the full three-large-eigenvalue hypothesis, force an original-coordinate cross block and six physical rows with `C_R(M)>=c_0` at universal scale, or prove that failure (`C_R=0` for all relevant six-sets, or all positive `C_R` quantitatively tiny) enters a completed coloop/rank-one-flat/five-row, ridge, grouped-hub, physical-pair, aggregate-square, or higher-volume endpoint without paying a vanishing local coefficient.

Fleet02/B04's base-packing trichotomy addresses the **zero-support** side. The genuinely new remaining quantitative regime is `C_R>0` but very small everywhere. The bare spectral hypothesis has not yet been connected to a universal lower bound for this Hellinger volume, so the full theorem is not claimed.

## 8. Verification/status

Exact finite algebra for Section 6 is saved in `CHECKS.json`. The early substantive checkpoint was saved before this final report. These finite checks do not prove the imported analytic theorem. No independent end-to-end review of this new compiler has yet been recorded. A full QFORM solution would still require all target quantifiers plus two actual independent end-to-end reviews.
