SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T18:11:24.900489Z.
attacking: the four-anchor diagonal-plus-rank-four plus zero-diagonal max-norm twist chamber: derive a product-preserving finite-anchor payment or a sharper obstruction without treating small coefficients as a perturbation.

# fleet02/B13 — unconditional D5 skeleton and rough-law nonperturbation obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws / complementary constructions. Status: **NEW UNCONDITIONAL TARGET-LEVEL REDUCTION; FULL QFORM OPEN; CONTINUITY OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication

`QFORM-DIAG-RANK16-FROB-TWIST-ROUGH-GLUE-v1`: prove a universal slab bound in the chamber

`A = D + R + E`,  `D` diagonal, `rank(R) <= 16`, `E` symmetric zero-diagonal,

`||E||_F <= K_*/rho`,

where `rho=P{X^TAX in J}/|J|` is the slab ratio and `K_*` is the absolute constant below, while the input marginals are arbitrary cap-one laws with fragmented/unbounded supports. The twist `E` must remain inside the actual quadratic form; Section 5 gives an explicit target-class family showing that `||E||_F -> 0` does not make `X^T E X -> 0` uniformly over admissible product laws. Otherwise construct a genuine bounded-finite-union product-indicator counterexample sequence.

## 1. Fresh source pins and exact scopes

Required pinned source:

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, with `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md` all read.

Two completed results are used at equations:

1. `D_5`: for every disjoint ORIGINAL-coordinate cross block `M=A[I,J]`, with arbitrary same-side blocks, outside terms and affine terms,

`||p_Q||_infinity <= C5 e_5(M^T M)^(-1/10)`,  `C5=5 sqrt(2e)`,

with no volume-marginal condition.

2. Localized Theorem A: if an ORIGINAL physical principal `3 x 3` block has all three eigenvalues of modulus at least `c>0`, then after conditioning all other original coordinates the full ambient form has

`||p_Q||_infinity <= 6 sqrt(pi)/c`.

Latest designated partner fleet03/B13 r30:

`yspennstate/math-open-problems@feda06c104c0d8c62661daf01eed33c10f55fa99`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T173317Z-fleet03-B13-qform-r30/REPORT.md`, with exact constants checked at `73399f1d5184095fcfd61bf258789bf0bba2dba6`.

That report obtains a stronger rank-eight Frobenius skeleton from a global third-volume estimate, but explicitly retains the grouped projected-crossing receiver as a pending dependency. The result below replaces that conditional third-volume input by the unconditional pinned `D_5` theorem and telescopes four adjacent exterior-volume ratios. The price is rank sixteen instead of eight.

Deterministic skeleton source:

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`,

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/structure/REPORT.md`, Corollary 3.2:

if `V_{r+1}(A) <= kappa V_r(A)`, where

`V_r(A)=sum det(A[S,T])^2`

over ordered disjoint physical `r`-sets `S,T`, then

`A=D+R+E`,  `rank(R)<=4r`,  `E` zero-diagonal,

`||E||_F <= 3(r+1) sqrt(kappa)`.

The source proves this by a volume-sampled physical skeleton identity; no random variables are rotated.

No-attainment transfer source:

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`, fleet04/B13. For every bounded nonnegative product kernel, the supremum over cap-one mass-one product densities equals the supremum over products of indicators of unit-measure sets, and every marginal may be approximated in `L^1` by finite convex mixtures of indicators of bounded finite unions of intervals. It asserts no optimizer, interval extremality, diameter bound or fragment-count bound.

## 2. Unconditional fifth-volume bound in global physical coordinates

Let `J` be an interval of positive length and

`rho = P{X^T A X in J}/|J|`.

For every physical partition `[n]=I sqcup Jc`, put `M=A[I,Jc]`. If `e_5(M^T M)=0` the next inequality is trivial. Otherwise pinned `D_5` gives a bounded density and hence

`rho <= C5 e_5(M^T M)^(-1/10)`,

so

`e_5(M^T M) <= (C5/rho)^10`.                                      (2.1)

Choose the physical partition by independent fair Bernoulli labels. A fixed ordered pair of disjoint five-sets `(S,T)` lands with `S subset I`, `T subset Jc` with probability `4^-5`. Cauchy--Binet therefore gives the exact identity

`E_cut e_5(A[I,Jc]^T A[I,Jc]) = 4^-5 V_5(A)`.

Averaging (2.1) over cuts yields

`boxed: V_5(A) <= 4^5 C5^10 rho^-10.}`                              (2.2)

This is an unconditional global algebraic obstruction on every high-density witness. It is a direct use of the required pinned Fourier result.

## 3. High slab ratio forces nontrivial first exterior volume

Write

`D0=diag(A)`,  `O=A-D0`,  `V_1(A)=||O||_F^2`.

### Lemma 3.1

If `s_3(A)>=1` and

`rho > 2 + 6 sqrt(pi) = 12.634723105433096...`,                    (3.1)

then

`boxed: V_1(A) >= rho^-2.}`                                        (3.2)

### Proof

Suppose `V_1<rho^-2`. Then

`||O||_op <= ||O||_F < rho^-1`.

Weyl's singular-value inequality gives

`s_3(D0) >= s_3(A)-||O||_op > 1-rho^-1`.

Since `D0` is diagonal, there are three original coordinates `K` for which every corresponding diagonal entry has modulus `>1-rho^-1`. The physical principal block satisfies

`sigma_min(A[K,K])
 >= sigma_min(D0[K,K])-||O[K,K]||_op
 > 1-2/rho`.                                                        (3.3)

Pinned localized Theorem A, after conditioning all coordinates outside `K`, gives

`rho <= ||p_Q||_infinity
     <= 6 sqrt(pi)/(1-2/rho)`.

Thus `rho-2 <= 6 sqrt(pi)`, contradicting (3.1). QED.

No arbitrary-joint coarea claim is used: Theorem A is the completed physical-coordinate localized theorem from the pinned source.

## 4. Main theorem: unconditional diagonal + rank <=16 + O(rho^-1) Frobenius twist

### Theorem 4.1 — `QFORM-UNCONDITIONAL-D5-RANK16-FROB-SKELETON-v1`

Under the exact target hypotheses `s_3(A)>=1`, arbitrary independent cap-one marginals, and slab ratio satisfying (3.1), there exist a diagonal matrix `D`, a symmetric matrix `R` of rank at most sixteen, and a symmetric zero-diagonal matrix `E` such that

`boxed: A=D+R+E,  rank(R)<=16,  ||E||_F <= K_*/rho,}`              (4.1)

where

`K_* = 3 * 120^(1/4) * (4^5 C5^10)^(1/8)`

`    = 3 * 120^(1/4) * 2^(5/4) * (5 sqrt(2e))^(5/4)`

`    = 508.73821835096095...`.                                     (4.2)

This theorem is independent of the pending grouped projected-crossing receiver used by the designated partner r30.

### Proof

By Lemma 3.1, `V_1>=rho^-2>0`. If some `V_m=0` for `2<=m<=5`, take the least such `m`. Then `V_{m-1}>0` and the skeleton corollary with `r=m-1<=4` and `kappa=0` gives (4.1) with `E=0`, so assume `V_2,...,V_5>0`.

Set

`q_r = V_{r+1}/V_r`,  `r=1,2,3,4`.

Equations (2.2) and (3.2) give

`prod_{r=1}^4 q_r = V_5/V_1
 <= 4^5 C5^10 rho^-8`.                                             (4.3)

Put `C=4^5 C5^10`. Suppose, contrary to the desired conclusion, that for every `r=1,...,4`,

`3(r+1) sqrt(q_r) > K_*/rho`.                                     (4.4)

Then

`q_r > K_*^2/[9(r+1)^2 rho^2]`.

Multiplying over `r` and using `prod_{r=1}^4(r+1)=2*3*4*5=120` gives

`prod q_r > K_*^8/[3^8 * 120^2 * rho^8]
           = C rho^-8`,                                            (4.5)

where the equality is exactly the definition (4.2) of `K_*`. This contradicts (4.3). Hence some `r in {1,2,3,4}` satisfies

`3(r+1) sqrt(q_r) <= K_*/rho`.                                    (4.6)

Apply the proved skeleton corollary with `kappa=q_r`. It gives `rank(R)<=4r<=16` and

`||E||_F <= 3(r+1)sqrt(q_r) <= K_*/rho`.

This is (4.1). QED.

### Comparison with the designated partner

The partner r30 route, conditional on its pending projected-crossing receiver, proves `V_3=O(rho^-6)` and obtains rank at most eight with residual constant about `1.22e6/rho`. The present route uses only completed `D_5`, completed localized Theorem A, and the proved deterministic skeleton identity; it gives a weaker rank bound sixteen but is unconditional with respect to that receiver, and its explicit Frobenius constant is `508.739`.

Thus the two routes isolate the same genuine analytic endpoint from complementary directions: a bounded-rank carrier plus a coefficient-small but probabilistically non-perturbative zero-diagonal twist.

## 5. Complementary construction: Frobenius-small twists are not law-uniformly small random errors

### Proposition 5.1 — `QFORM-FROB-TWIST-NONPERTURBATION-v1`

There are target-class matrices `A_R=A_0+E_R`, with `A_0` already having three eigenvalues equal to one, and independent unit-measure finite-union indicator laws, such that

`||E_R||_F -> 0`

but

`|X^T E_R X| -> 2`

uniformly in absolute value. In particular `X^T E_R X` does not converge to zero in probability. Therefore no proof may delete the residual in (4.1) solely from its Frobenius norm, even after the valid finite-union purification.

### Proof

Take five coordinates and

`A_0=diag(1,1,1,0,0)`.

On the last two coordinates put

`E_R[4,5]=E_R[5,4]=R^-2`,

all other entries zero. Then

`||E_R||_F=sqrt(2) R^-2 ->0`,

while every `A_R` still has at least three eigenvalues of modulus at least one.

For `i=4,5`, let `X_i` have density one on

`F_R=[R-1/4,R+1/4] union [-R-1/4,-R+1/4]`,

which has total measure one. Write

`X_i=S_i R+U_i`,

where `S_i` are independent fair signs and `U_i` are independent uniform variables on `[-1/4,1/4]`, independent of the signs. Then

`X^T E_R X = 2 R^-2 X_4 X_5`

`=2 S_4S_5 + (2/R)(S_4U_5+S_5U_4) + (2/R^2)U_4U_5`,

so deterministically

`|X^T E_R X - 2S_4S_5| <= R^-1 + (8R^2)^-1`.                     (5.1)

Hence `|X^T E_R X|` tends uniformly to two. The first three marginals may be any cap-one laws; they do not affect this conclusion. QED.

This is not a counterexample to QFORM. It is a source-valid obstruction to the tempting continuity step `small coefficient matrix => small random quadratic perturbation`. The danger comes from legal separated supports whose scale grows as the coefficient shrinks.

## 6. Extremal-product consequence: normal form for any actual counterexample sequence

The no-attainment purification theorem applies to the bounded slab kernel

`K(x)=1_{x^T A x in J}`.

Thus if the full universal slab bound is false, for every target ratio one may transfer a strict bad slab, with arbitrarily small loss, to a product of indicators of bounded finite unions `F_i` of total measure one. No optimizer is claimed and the support diameters or numbers of fragments may diverge.

Applying Theorem 4.1 to such a sequence gives the following source-valid normal form. Any hypothetical sequence with `rho_m -> infinity` may be taken to have finite-union product-indicator marginals and matrices

`A_m = D_m + R_m + E_m`,

`rank(R_m)<=16`,

`||E_m||_F <= (K_*+o(1))/rho_m`,                                   (6.1)

while, independently from (2.2),

`V_5(A_m) <= 4^5 C5^10 rho_m^-10`.                                (6.2)

The obstruction in Proposition 5.1 shows exactly why (6.1) does not finish the theorem: arbitrarily fragmented/separated product supports can amplify a coefficient-small twist into an order-one random term. A successful glue theorem must exploit product/Fourier geometry of that twist, not erase it.

## 7. What changed and next step

Before this run, the current B13 path had a four-anchor max-norm skeleton and the designated partner had a stronger but receiver-conditional rank-eight Frobenius skeleton. The present run adds an **unconditional** global reduction using the pinned fifth-volume theorem:

`high slab ratio => diagonal + rank <=16 + O(rho^-1) Frobenius twist`,

with explicit threshold `rho>2+6sqrt(pi)` and explicit residual constant `K_*=508.73821835096095...`.

It also supplies a finite-union target-class construction proving that the remaining twist cannot be treated perturbatively from coefficient norm alone.

The first unpaid implication is therefore genuinely analytic and product-preserving:

`QFORM-DIAG-RANK16-FROB-TWIST-ROUGH-GLUE-v1`.

A promising next move is to apply Fresnel linearisation only to the rank-sixteen carrier and use the pinned one-dimensional twisted `L^p` bound on the actual product coordinates while charging the zero-diagonal twist by a graph/partition decomposition. Any such step must remain uniform under the separated-support construction above.

## 8. Integrity / scope

No moments, support bounds, log-concavity, identical laws, centered intervals, diagonal-basis independence, or independence after a spectral rotation are used. Continuity is not inferred beyond source theorems that prove it in their own paid branches. The counterexample search at the required pinned source reports no valid counterexample in tested families; none of its numerical evidence is used as proof.

Changed-file privacy check: manual allowlist review of this mathematical report only. It contains pure mathematics, public/source commit pins and logical fleet labels; no credentials, scheduler identifiers, machine paths, unrelated data, or private source excerpts.
