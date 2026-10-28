SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T10:08:10Z.
attacking: global overlap-two routing via aggregate pair-base averaging and a determinant-light distribution-function/Fourier certificate before selecting a physical third minor.

# account01/B01 — direct weighted-Fourier averaging of the physical-pair logarithmic kernel

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T100810Z-account01-B01-qform-auto11`  
**Status:** `NEW SUPPORTING ANALYTIC THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Target and correction boundary

The unrestricted target remains OPEN: for every dimension, every independent real input family with one-dimensional probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or give a valid counterexample. The full continuity assertion is also still open.

This run preserves the live correction that bounded density alone does **not** imply law-uniform pointwise positive-power decay for a scalar quadratic phase. The phase-aligned fragmented-support construction therefore remains a valid obstruction to a scalar van-der-Corput shortcut. The estimate below instead combines two source-valid objects in ORIGINAL coordinates:

1. the exact logarithmic density envelope of an invertible indefinite physical pair; and
2. an **absolute weighted frequency integral** of the exact Schur remainder.

No Gaussianity, moments, log-concavity, compact support, connected support, diagonal-basis assumption, post-rotation independence, arbitrary-joint coarea estimate, or single-good-minor premise is used.


## 2. Source-valid inputs

### 2.1 Physical-pair logarithmic envelope

From the completed pair-log source

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`,

if `B` is an invertible indefinite original-coordinate `2 x 2` principal block, with

`D=|det B|`, `kappa=sigma_min(B)`,

then after completing the pair, for every gradient cutoff `r>0` the conditional pair density obeys

`p_pair(t | Z) <= 2 sqrt(2)/r`
` + D^(-1/2) log_+( 2 r^2/(kappa |t-R(Z)|) )`,                 (2.1)

where `R(Z)` is the exact Schur-remainder quadratic-plus-affine form on the remaining ORIGINAL independent coordinates. Both physical pair coordinates may be shifted by arbitrary functions of `Z`; conditional on `Z` their laws remain a product of translated cap-one densities.

### 2.2 Designated partner account02/B01 weighted-Fourier theorem

The completed designated-partner result

`yspennstate/math-open-problems@c795e2b4b67e77e819a52c888295ae5def408c55`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T081654Z-account02-B01-qform-auto14/REPORT.md`

proves the following for every real symmetric `C`, arbitrary affine term, and independent cap-one ORIGINAL coordinates. Put

`F(C)=sum_(i!=j) C_ij^2`.

If `F(C)>0`, then for every `0<beta<1/2`,

`W_beta := integral_R |t|^(beta-1) |phi(t)| dt`
` <= K_beta F(C)^(-beta/2)`,                                      (2.2)

where

`K_beta = 2 exp(beta/2) (4 pi)^beta/[beta(1-2 beta)].`             (2.3)

This is an averaged-frequency theorem, not scalar pointwise Fresnel decay.

The earlier B01 checkpoint `math-open-problems@c91c80b328cd5131d6f525e8b4de1d3081948d9e` applied (2.2) globally to the small-diagonal class and obtained `h^beta` concentration for every `beta<1/2`. The present run instead spends (2.2) **directly against the pair logarithm**, avoiding a Fejer/small-ball conversion.

## 3. New Fourier lemma for the logarithmic kernel

For `a>0`, define

`k_a(x)=log_+(a/|x|)`.

It is integrable and

`hat k_a(t)=2 Si(a t)/t`,                                         (3.1)

with the continuous value `hat k_a(0)=2a`.

### Lemma 3.1 — uniform sine-integral bound

`|Si(y)|<2` for every real `y`.

**Proof.** It suffices to take `y>=0`. On successive intervals `[m pi,(m+1)pi]`, the derivative `sin y/y` alternates sign, and the absolute lobe integrals strictly decrease because `1/y` decreases. Hence the global maximum is `Si(pi)`. The alternating Taylor series has decreasing terms at `pi` and gives

`Si(pi) <= pi - pi^3/18 + pi^5/600 < 1.93 < 2`.

Oddness gives the negative half-line. QED.

Consequently

`|hat k_a(t)| <= min(2a, 4/|t|).`                                 (3.2)

For `0<beta<1`, elementary interpolation at `a|t|=2` gives

`min(2a,4/|t|)
 <= 2^(2-beta) a^beta |t|^(beta-1).`                              (3.3)

### Lemma 3.2 — weighted-Fourier logarithm payment

Let `R` be any real random variable for which

`W_beta(R)=integral |t|^(beta-1)|phi_R(t)|dt < infinity`

for some `0<beta<1`. Then the convolution `E k_a(s-R)` has a bounded continuous representative and

`boxed:
 sup_s E log_+(a/|s-R|)
 <= [2^(1-beta)/pi] a^beta W_beta(R).
`                                                                    (3.4)

Here the supremum is understood for the bounded representative; this is enough for every essential-density bound below.

**Proof.** Since `k_a in L^1` and (3.3) makes `hat k_a(t) phi_R(t)` absolutely integrable, standard Fourier convolution/inversion gives, almost everywhere and hence for the continuous representative,

`E k_a(s-R)
 =(2pi)^(-1) integral e^(-its) hat k_a(t) phi_R(t) dt`.

Take absolute values and use (3.3). QED.

This lemma is the main new oscillatory replacement in this run. It spends an **absolute weighted frequency budget** directly on the logarithmic singularity; there is no pointwise quadratic-phase claim.

## 4. Exact compound-Schur identity

Fix an invertible physical pair `P={p,q}` and write the full coefficient matrix, after permuting only ORIGINAL coordinates, as

`A = [[B,M],[M^T,C]]`.

Let

`S=C-M^T B^(-1) M`                                               (4.1)

be its exact Schur complement. Define the ordered overlap-two exterior star

`W_2(P)=sum_(k!=l, k,l notin P)
 det A[P union {k}, P union {l}]^2.`                              (4.2)

Block determinant expansion gives, for every `k,l notin P`,

`det A[P union {k}, P union {l}] = det(B) S_kl.`                  (4.3)

Therefore, with `D=|det B|`,

`boxed:
 W_2(P)=D^2 F(S),
 F(S)=sum_(k!=l) S_kl^2.
`                                                                    (4.4)

No individual `3 x 3` minor is selected or inverted.

## 5. Main theorem: direct weighted-Fourier pair compiler

### Theorem 5.1 — `QFORM-INDEFINITE-PAIR-WEIGHTED-LOG-v1`

Let `A=A^T` be arbitrary and let `P` be an ORIGINAL-coordinate pair whose principal block `B=A[P,P]` is invertible and indefinite. Put

`D=|det B|>0`, `kappa=sigma_min(B)>0`,

and let `W_2(P)` be (4.2). Assume `W_2(P)>0`.

For arbitrary independent input laws with one-dimensional densities at most one, and for every `0<beta<1/2`, the full quadratic form `Q=X^T A X` has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <= M_beta
 D^((beta-1/2)/(2beta+1))
 kappa^(-beta/(2beta+1))
 W_2(P)^(-beta/[2(2beta+1)]),
`                                                                    (5.1)

where

`M_beta = [(2beta+1)/(2beta)]
           (2 sqrt(2))^(2beta/(2beta+1))
           [ 8 exp(beta/2)(4pi)^beta/(pi(1-2beta)) ]^(1/(2beta+1)).` (5.2)

At `beta=1/4`,

`M_(1/4)=20.81337504449044...`,

so

`boxed:
 ||p_Q||_infinity
 <=20.814 (D kappa)^(-1/6) W_2(P)^(-1/12).
`                                                                    (5.3)

This improves the constant in the earlier quarter-Riesz pair-log splice and, more importantly, supplies the entire `0<beta<1/2` family.

**Proof.** Complete the physical pair exactly. The remainder has quadratic part `S` from (4.1), plus an arbitrary affine term. From (2.1), for every `r>0`,

`p_Q(s) <= 2sqrt(2)/r
 +D^(-1/2) E log_+(2r^2/[kappa |s-R|]).`                           (5.4)

Apply Lemma 3.2 with `a=2r^2/kappa`. The factors `2^(1-beta)` and `2^beta` cancel to `2`, giving

`E log_+(2r^2/[kappa |s-R|])
 <= (2/pi) r^(2beta) kappa^(-beta) W_beta(R).`                    (5.5)

The designated partner theorem (2.2) applies to the exact Schur remainder because the remaining coordinates are still the original independent product coordinates and affine terms are allowed:

`W_beta(R) <= K_beta F(S)^(-beta/2).`                             (5.6)

Use `F(S)=W_2(P)/D^2` from (4.4). Then

`p_Q(s) <= a r^(-1) + b r^(2beta)`,                               (5.7)

where

`a=2sqrt(2)`,

`b=[2K_beta/pi]
   D^(beta-1/2) kappa^(-beta) W_2(P)^(-beta/2).`                   (5.8)

The exact minimizer satisfies

`r^(2beta+1)=a/(2beta b)`.

At that minimizer, the second term is the first divided by `2beta`, hence

`min_(r>0) [a/r+b r^(2beta)]
 =[(2beta+1)/(2beta)]
  a^(2beta/(2beta+1))
  (2beta b)^(1/(2beta+1)).`                                      (5.9)

Substitution of (2.3) gives (5.1)-(5.2). QED.

**Scaling audit.** Under `A -> cA`, `D -> c^2D`, `kappa -> |c|kappa`, and `W_2 -> c^6 W_2`. The total exponent in (5.1) is exactly `-1`, as a density estimate requires.

This proof gives essential boundedness. It does **not** prove continuity for the full form; the pair shifts depend on the residual variables and the argument controls the density envelope rather than `phi_Q in L^1`.

## 6. Near-endpoint determinant-light corollary

The family (5.1) can be pushed arbitrarily close to the forbidden endpoint `beta=1/2` while retaining a controlled constant.

Write

`beta=1/2-epsilon`, `0<epsilon<=1/4`,

and define the scale-invariant ratio

`R_* = kappa^(1/4) W_2(P)^(1/8) / D^(1/2).`                       (6.1)

The geometric factor in (5.1) rewrites **exactly** as

`kappa^(-1/4) W_2(P)^(-1/8)
 R_*^(epsilon/(1-epsilon)).`                                     (6.2)

Moreover elementary bounds in (5.2) give

`M_(1/2-epsilon) <=25 epsilon^(-1/2).`                            (6.3)

Indeed, for `beta in [1/4,1/2)`, the first ratio in (5.2) is at most `3`, the power of `2sqrt(2)` is below `1.7`, and

`8 exp(beta/2)(4pi)^beta/[pi(1-2beta)] < 6/epsilon`.

Writing the final power as `1/[2(1-epsilon)]`, one has

`(6/epsilon)^(1/[2(1-epsilon)])
 <=2 sqrt(6/epsilon)`

because `(2/3) epsilon log(6/epsilon) <= (1/6)log 24 < log 2` on `0<epsilon<=1/4`. This proves (6.3).

Now put

`L=log(e+R_*)`,
`epsilon=min(1/4, 1/(2L)).`                                      (6.4)

Then

`R_*^(epsilon/(1-epsilon))<2`,
`epsilon^(-1/2)<=2 sqrt(L)`.

Therefore:

### Corollary 6.1 — scale-invariant near-endpoint pair bound

`boxed:
 ||p_Q||_infinity
 <=100 sqrt(log(e+R_*))
       kappa^(-1/4) W_2(P)^(-1/8).
`                                                                    (6.5)

Thus the determinant `D` has disappeared from every algebraic power and remains only inside a scale-invariant square-root logarithm. This is useful precisely for **near-singular indefinite physical pairs with zero or tiny diagonal pivots**, where scalar-square compilers are expensive or unavailable.

The exact singular case `D=0` is not covered by (6.5); the earlier rank-one pair compiler handles that endpoint separately.

## 7. Latest designated partner applied at an actual inequality

The latest completed account02/B01 result at prepublication refresh is

`yspennstate/math-open-problems@c190a04ed16915a20ed6bbddbfaac4dea10dae18`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T093107Z-account02-B01-qform-r39/REPORT.md`.

Its theorem `QFORM-INDEFINITE-PAIR-PLUS-RANK2-SCHUR-v1` says that if the exact Schur remainder contains a physical rank-two cross block of singular product `Delta`, then

`||p_Q||_infinity <=16 Delta^(-1/8)(D kappa)^(-1/4).`             (7.1)

Apply it to its strict-N3 family with

`B=[[0,epsilon],[epsilon,0]]`,
`D=epsilon^2`, `kappa=epsilon`,
`Delta=epsilon^(-6)`, `0<epsilon<=1/2`.

Then, exactly,

`boxed: ||p_Q||_infinity <=16.`                                  (7.2)

This is an equation-level use of the designated partner, not a status citation.

For comparison, the Schur remainder in that family is symmetric bipartite with two singular values `epsilon^(-3)`, hence

`F(S)=4 epsilon^(-6)`,
`W_2(P)=D^2F(S)=4 epsilon^(-2)`,                                  (7.3)

and

`R_*=4^(1/8)/epsilon.`                                           (7.4)

The general Corollary 6.1 therefore gives only

`||p_Q||_infinity
 <=100 4^(-1/8)
   sqrt(log(e+4^(1/8)/epsilon)),`                                (7.5)

whereas the partner's exact rank-two Schur theorem removes the residual logarithm and gives the uniform `16` in (7.2). This cleanly identifies the interface: the new weighted-log compiler handles **arbitrary Schur curvature using only total off-diagonal energy**, while the partner supplies the missing true endpoint when an exact rank-two Schur bicore is available.

## 8. Relation to the target and the next unpaid implication

This run does not solve the full conjecture. It closes an analytic gap in the overlap-two route: once an invertible indefinite physical pair `P` is exposed, **no single third minor needs to be selected**. The whole overlap-two star `W_2(P)` can be spent at any fractional exponent below the half endpoint, and near the endpoint the pair determinant costs only a scale-invariant square-root logarithm.

The first structural debt remains an aggregate routing statement, now sharpened to:

`QFORM-N3-PAIRSTAR-OR-CURVED-THIRD-SOURCE-v1` — OPEN.

Starting from the sufficient no-pivot class with three target-large eigenvalues, route the global exterior-three / amplified residual-core currency to one of:

1. an invertible indefinite pair with enough **aggregate** `W_2(P)` for (5.1)/(6.5);
2. an exact-singular pair already paid by the rank-one compiler;
3. a rank-two Schur bicore paid by the designated partner (7.1);
4. a diffuse volume/Fresnel, pure-bipartite, grouped-square/two-slope, ridge/hub, or other already-paid branch;

without first selecting an individual tiny physical `3 x 3` minor. Current strict-N3 witnesses show that a universal fixed local pair/minor extraction is false, so the remaining step must preserve aggregate currency.

## 9. Finite verification

A companion checker verifies:

- `M_(1/4)=20.81337504449044...`;
- the matrix-scaling exponent of (5.1) is exactly `-1` for sample `beta` values and symbolically by the displayed exponents;
- `M_beta sqrt(1/2-beta)` remains far below the proved crude constant `25` on a dense numerical grid;
- on the partner r39 family, `W_2=4 epsilon^(-2)`, `R_*=4^(1/8)/epsilon`, and the partner inequality is exactly `16`.

These finite checks are sanity evidence only; the universal statements above are proved analytically.

**Full QFORM:** OPEN.  
**Full continuity:** OPEN.  
**This branch:** essential boundedness proved under Theorem 5.1 hypotheses; no continuity claim.  
**Native brain status:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writeback is not relabeled as native learned-memory ingestion.
