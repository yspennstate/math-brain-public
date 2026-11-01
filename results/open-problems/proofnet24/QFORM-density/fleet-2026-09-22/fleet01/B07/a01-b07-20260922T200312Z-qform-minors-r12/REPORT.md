SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-22T20:03:12Z.
attacking: coordinate-minor selection by an exact fixed-pair Schur/exterior hierarchy; compress the diffuse third-direction determinant bank without selecting one tiny minor.

# fleet01/B07 — fixed-pair Schur determinant hierarchy and a sharpened bounded-cardinality collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** coordinate minor selection  
**Run:** `a01-b07-20260922T200312Z-qform-minors-r12`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_STRUCTURAL_THEOREM_PROVED / FULL_TARGET_OPEN`.

The exact target remains: for every finite `n`, every independent real `X_i` with probability densities at most one, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential bound on the density of `X^T A X`, or produce a target-valid counterexample. No post-rotation independence, moment, support, log-concavity, or sign assumption is introduced here. The full continuity conclusion is also still open; continuity is obtained only in the rank-three subbranch explicitly paid below.

The live correction ledger was consumed before this argument. In particular, nothing below uses the refuted arbitrary-joint rank-three coarea bound, a worst conditional density cap, law-uniform pointwise quadratic-phase decay, or reciprocal selection of one coordinate minor.

## 1. Complete peer inputs actually used

The designated partner result used in an actual inequality is fleet02/B07, `QFORM-CROSS-FIBER-PLANCHEREL-v1`, canonical source

`yspennstate/math-open-problems@5266d24ea98d9bb5902c51a92eca0e3e38112e39`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T193347Z-b07-639234ec/REPORT.md`.

For a physical cross block `B` of exact rank `r>=3`, with nonzero singular-value product `D`, it proves for the full ambient form

`||p_Q||_infinity <= e r/(r-2) D^(-1/r)`,

with a continuous density. It retains arbitrary self blocks, outside couplings, affine terms, signs, and extra ambient coordinates.

I also use the current O0 structural state from fleet03/B07. Its completed effective-dimension-three reduction gives a physical cross block `B` with

`E_3(B)=e_3(s_1(B)^2,s_2(B)^2,...) >= 1/256`,

and calibrates the ridge kernel to trace three. Its r15 result `QFORM-O0-EXCLUSION-PAIR-DICHOTOMY-v1` isolates, in the two-heavy-row branch, a physical row pair `P={i,j}` with

`3/4 <= ell=K_ii <= 7/8`,
`m=(K^(-i))_jj >=1/2`,
`g=det K_P`,
`K_jj=(1-ell)m+g`.

The `g>=1/16` branch was previously known to carry a constant determinant-law mass on exact row sets of cardinality three through five. The derivation below identifies the exact residual object behind that bank and strengthens its quantitative mass.

## 2. Exact physical fixed-pair exterior identity

The first identity does not involve a ridge regularizer.

### Theorem 2.1 — `QFORM-FIXED-PAIR-WEDGE-SCHUR-IDENTITY-v1`

Let `B` be any real matrix, let `P` be a set of `p` physical rows such that

`G_P=B_P B_P^T`

is invertible, and let `R` denote the remaining rows. Put

`Pi_P=B_P^T (B_P B_P^T)^(-1) B_P`,
`C=B_R (I-Pi_P)`.

Then for every integer `m>=0`,

`boxed(
 sum_{T subset R, |T|=m}
 det(B_{P union T} B_{P union T}^T)
 = det(B_P B_P^T) e_m(CC^T).
)`                                                     (2.1)

Equivalently, the whole fixed-pair/fixed-packet determinant hierarchy has generating polynomial

`boxed(
 sum_{T subset R} z^(|T|) det(B_{P union T}B_{P union T}^T)
 =det(B_PB_P^T) det(I+z CC^T).
)`                                                     (2.2)

For a physical pair `P={i,j}` this gives, in particular,

`boxed(
 sum_{k notin P} det(B_{P union {k}}B_{P union {k}}^T)
 =det(B_PB_P^T) ||B_R(I-Pi_P)||_F^2.
)`                                                     (2.3)

Thus the determinant weights of every possible third row are not a collection of unrelated minors: after a fixed pair is chosen they are exactly the squared residual row lengths after orthogonal projection away from the pair span.

### Proof

Write `G=BB^T` in the row decomposition `P union R`. The Schur complement of `G_P` is

`G/G_P
 =B_RB_R^T-B_RB_P^T(B_PB_P^T)^(-1)B_PB_R^T
 =B_R(I-Pi_P)B_R^T
 =CC^T`.                                                (2.4)

For every `T subset R`, the block determinant formula gives

`det G_{P union T}=det G_P det((CC^T)_T)`.             (2.5)

Summing (2.5) over all `|T|=m` gives (2.1), because the sum of the principal `m x m` minors of `CC^T` is `e_m(CC^T)`. Summing over all `m` gives (2.2). `QED`

### Partner stress explained exactly

The current fleet02/B07 stress family has distinguished rows

`u_i=sqrt(3/4)e_1`, `u_j=sqrt(1/2)e_2`,

plus rows in the same two directions and `N` rows `N^(-1/2)e_3`. For the pair `P={i,j}`,

`det(B_PB_P^T)=3/8`,

while `B_R(I-Pi_P)` consists exactly of the `N` diffuse third-direction rows, so

`||B_R(I-Pi_P)||_F^2=1`.

Identity (2.3) therefore forces total pair-containing third-volume `3/8`, although every individual nonzero pair-containing triple has determinant `3/(8N)`. This is the exact algebraic reason single-packet extraction fails while aggregate payment remains viable.

## 3. A trace-three contraction always leaves one full residual direction after a pair

The ridge form gives an unexpectedly strong dimension-free statement.

### Theorem 3.1 — `QFORM-TRACE3-PAIR-RESIDUAL-MASS-v1`

Let `K` be any finite real symmetric positive-semidefinite contraction,

`0 <= K <= I`,

with `theta=tr K`. Let `P` be a `p`-element coordinate set for which `K_P` is invertible, put `R=P^c`, and define the Schur complement

`S=K_RR-K_RP K_P^(-1) K_PR`.                              (3.1)

Then

`0<=S<=I`,                                                  (3.2)

`boxed( tr S >= theta-p, )`                                (3.3)

and, writing `g=det K_P`,

`boxed(
 sum_{T subset R, |T|=m} det K_{P union T}
 =g e_m(S)
)`                                                         (3.4)

for every `m`. Consequently

`sum_T z^(|T|) det K_{P union T}=g det(I+zS)`.             (3.5)

At the QFORM effective-dimension-three scale (`theta=3`) and for a pair (`p=2`),

`boxed( tr S >=1 )`                                        (3.6)

and hence

`boxed(
 sum_{k notin P} det K_{P union {k}}=g tr S >=g.
)`                                                         (3.7)

So every invertible physical ridge pair leaves at least one complete unit of aggregate conditional ridge direction, even if that direction is spread over arbitrarily many physical coordinates.

### Proof

Schur positivity gives `S>=0`. Since `K<=I`, its lower-right principal block obeys `K_RR<=I`, and therefore

`I-S=I-K_RR+K_RP K_P^(-1)K_PR>=0`,                        (3.8)

which proves `S<=I`.

The contraction property also gives `K^2<=K`. Its `P x P` block is

`K_P^2+K_PRK_RP<=K_P`.                                     (3.9)

Conjugating by `K_P^(-1/2)` yields

`K_P^(-1/2) K_PRK_RP K_P^(-1/2)<=I-K_P`.                  (3.10)

Taking traces,

`tr(K_RP K_P^(-1)K_PR)<=p-tr K_P`.                         (3.11)

Hence

`tr S
 =theta-trK_P-tr(K_RP K_P^(-1)K_PR)
 >=theta-p`,                                               (3.12)

which is (3.3). Finally the block determinant identity gives

`det K_{P union T}=det K_P det S_T`;                       (3.13)

summing its principal minors proves (3.4)-(3.5). `QED`

## 4. The r15 determinant-law collar is a conditional DPP, and its constant improves

For a physical cross block `B` and finite `gamma>0`, put

`L=gamma^(-2) BB^T`,
`K=L(I+L)^(-1)`,
`D_gamma=det(I+L)`.

The exact determinant-law distribution on physical row sets is

`P(Y=F)=gamma^(-2|F|) det(B_FB_F^T)/D_gamma`.              (4.1)

Its inclusion kernel is `K`, so `P(P subset Y)=det K_P=g`. Conditional on inclusion of `P`, (3.13) gives

`P(T subset Y\P | P subset Y)=det S_T`;                   (4.2)

thus the residual set is itself a determinantal process with kernel `S`. If `lambda_a` are the eigenvalues of `S`, the residual cardinality

`N=|Y\P|`

has generating function

`E z^N=det(I-S+zS)=prod_a(1-lambda_a+z lambda_a)`,          (4.3)

so it has the law of a sum of independent Bernoulli variables with parameters `lambda_a`.

Now specialize to the r15 area branch. Its ridge scale has `tr K=3`, the pair satisfies

`3/4<=ell<=7/8`, `m>=1/2`, `g>=1/16`,
`K_jj=(1-ell)m+g`.                                        (4.4)

Theorem 3.1 gives

`tau:=trS>=1`.                                             (4.5)

On the other hand, the Schur correction in (3.1) is positive, so

`tau<=3-tr K_P`.                                           (4.6)

From (4.4),

`tr K_P
 =ell+(1-ell)m+g
 >=ell+(1-ell)/2+1/16
 =9/16+ell/2
 >=15/16`,                                                 (4.7)

and therefore

`boxed( 1<=tau<=33/16. )`                                  (4.8)

This interval is enough to sharpen the old bounded-cardinality mass by a Chernoff argument.

First,

`P(N=0)=prod_a(1-lambda_a)<=exp(-tau)`.                    (4.9)

For `tau<4`, Chernoff gives, for every `s>0`,

`P(N>=4)
 <=exp(-4s) prod_a(1+lambda_a(e^s-1))
 <=exp(-4s+tau(e^s-1)).`                                  (4.10)

Choosing `e^s=4/tau` gives

`P(N>=4)<=exp(4-tau)(tau/4)^4`.                            (4.11)

Thus

`P(1<=N<=3)>=h(tau)`,                                      (4.12)

where

`h(tau)=1-e^(-tau)-e^(4-tau)(tau/4)^4`.                   (4.13)

On `[1,33/16]`,

`h'(tau)=e^(-tau)[1-e^4 tau^3(4-tau)/256]`.               (4.14)

The bracketed second term is monotone increasing on this interval because `tau<3`; hence `h'` changes sign at most once, from positive to negative. Therefore the minimum of `h` on this interval occurs at an endpoint. Direct endpoint comparison gives

`h(1)=1-e^(-1)-e^3/256=0.5536614302...`,

while

`beta_*:=h(33/16)
 =1-e^(-33/16)-e^(31/16)(33/64)^4
 =0.3822033996600577...`.                                  (4.15)

Therefore

`P(1<=N<=3 | P subset Y)>=beta_*`.                         (4.16)

Multiplying by `P(P subset Y)=g>=1/16` and substituting the exact weights (4.1) proves the strengthened bounded-cardinality collar

`boxed(
 sum_{F superset P, 3<=|F|<=5}
 gamma^(-2|F|) det(B_FB_F^T)
 >=c_new D_gamma,
)`                                                         (4.17)

with

`boxed(
 c_new=beta_*/16
 =0.02388771247875361... .
)`                                                         (4.18)

The r15 bound was

`c_old=(31/64-e^(-1))/16
 =0.007280972426784854...`;                                (4.19)

thus (4.18) improves that determinant-law mass by the factor

`c_new/c_old=3.280840947958649...`.                        (4.20)

This is not yet a density theorem for the full area branch; it is a stronger, exact dimension-free determinant currency for the next product-preserving transducer.

### Exact-rank-three endpoint

When the effective kernel is the rank-three range projection (the `gamma downarrow0` endpoint), Theorem 3.1 gives `rank S=1` and `trS>=1`, while `S<=I`; hence its unique nonzero eigenvalue is exactly one. Conditional on `P subset Y`, `N=1` almost surely. Thus the endpoint places all pair-containing volume-sampling mass at cardinality three and is stronger than (4.17).

## 5. A new residual dichotomy: four-row currency or a near-coloop eigenvalue

The Schur hierarchy also isolates the next obstruction without any coordinate-minor inversion.

### Corollary 5.1 — `QFORM-PAIR-RESIDUAL-E2-DICHOTOMY-v1`

At trace three with a pair `P` satisfying `g>=1/16`, let `S` be as above. Then either

`boxed(
 sum_{T subset R, |T|=2} det K_{P union T}
 =g e_2(S) >=1/256,
)`                                                         (5.1)

or

`boxed( lambda_max(S)>=7/8. )`                             (5.2)

### Proof

If `e_2(S)>=1/16`, (5.1) follows from `g>=1/16`. Otherwise let `tau=trS>=1` and `lambda=lambda_max(S)`. Since

`sum_a lambda_a^2=tau^2-2e_2(S)<=lambda tau`,              (5.3)

we have

`lambda>=tau-2e_2(S)/tau>tau-(1/8)/tau>=7/8`,              (5.4)

because the last expression is increasing for `tau>=1`. `QED`

Thus the r15 area branch does not merely say “there are many small packets.” After conditioning on the fixed physical pair, the unpaid determinant geometry is forced into one of two dimension-free forms: a constant pair-plus-two-residual fourth-minor bank, or a residual conditional ridge direction with eigenvalue at least `7/8`. The latter is a spectral near-coloop of the conditional contraction; no claim is made that it is already a heavy *physical coordinate*.

## 6. Actual application of the designated fleet02/B07 theorem

The rank-one residual subbranch closes immediately and cleanly.

If `rank S=1`, then block Gaussian elimination gives

`rank K=rank K_P+rank S=3`.                                 (6.1)

At finite positive ridge scale `rank K=rank B`; hence the physical cross block `B` itself has exact rank three. In the O0 branch we already have

`E_3(B)>=1/256`.                                            (6.2)

For rank three, `E_3(B)` is exactly the pseudodeterminant `pdet(BB^T)`, i.e. the square of the product of its three nonzero singular values. Applying the designated partner theorem `QFORM-CROSS-FIBER-PLANCHEREL-v1` with `r=3` gives the actual full-form inequality

`||p_Q||_infinity
 <=3e E_3(B)^(-1/6)
 <=3e 256^(1/6)
 =20.5489229713... .`                                      (6.3)

The density is continuous on this subbranch. Arbitrary self blocks, outside couplings, signs and extra ambient coordinates are retained exactly as in the partner theorem.

Consequently the genuinely unpaid r15 area branch may now be restricted to

`rank S>=2`.                                                (6.4)

Together with Corollary 5.1, it is enough to understand either the constant fourth-minor currency (5.1) or the conditional near-coloop alternative (5.2).

## 7. Why this is the right determinant bookkeeping for coordinate selection

The key point is that the third direction need not live on one coordinate. The exact fleet02/B07 stress has `N` third-direction rows of size `N^(-1/2)`; every individual triple is `O(1/N)`, but Theorems 2.1 and 3.1 retain the entire third direction as one aggregate Schur/Frobenius unit. This is precisely the currency that a dimension-free proof must preserve before reciprocal inversion.

The same mechanism extends to every higher overlap order through (2.1) and (3.4): after fixing a physical pair, pair-containing `(2+m)`-row determinants are not arbitrary; they are exactly `det(pair) e_m(residual Schur Gram)`. Thus size-three, four, and five banks are the first three elementary symmetric polynomials of one residual positive contraction, not three unrelated combinatorial cases.

## 8. First essential missing implication

The next B07 obligation is now narrower than the previous generic “area-bank payment”:

`QFORM-PAIR-RESIDUAL-TRANSDUCER-v1`.

> At effective ridge trace three, start with a physical pair `P` with `g=det K_P>=1/16` and its conditional residual contraction `S`, where `1<=trS<=33/16` and `rankS>=2`. Convert, without selecting a reciprocal tiny minor, either
> 
> (a) `g e_2(S)>=1/256`, or
> 
> (b) `lambda_max(S)>=7/8`,
> 
> into a dimension-free density/half-Riesz estimate for the full quadratic form, retaining arbitrary self blocks and additional spectrum.

A viable mechanism is a grouped two-row plus residual-direction Fourier/Brascamp--Lieb estimate: the physical pair must be paid jointly and the residual Schur contraction must remain aggregated. Worst-packet selection is ruled out by the source-valid diffuse-third-direction stress.

This does not close O0 by itself. The r15 small-`g` replacement-pair branch and the earlier physical near-coloop branch remain siblings, while O1/O2/O3 remain separate full-synthesis debts. The unrestricted QFORM conjecture and its global continuity conclusion therefore remain OPEN.

## 9. Exact finite verification

`CHECK.py` and `check_results.json` in this run directory verify the determinant identities on an exact rational trace-three contraction

`K=[[3/4,1/20,1/10,0],
    [1/20,3/4,0,1/10],
    [1/10,0,3/4,1/20],
    [0,1/10,1/20,3/4]]`.

For `P={1,2}` they give

`g=14/25`,
`trS=165/112`,
`sum_k det K_{P union {k}}=33/40=g trS`,
`det K=189/625=g det S`.

The checker also records `c_new=0.023887712478753608`, the old `0.007280972426784854`, the improvement factor `3.2808409479586493`, and the partner rank-one O0 bound `20.548922971333656`. These finite checks are regression/calibration only; the universal argument is the analytic proof above.
