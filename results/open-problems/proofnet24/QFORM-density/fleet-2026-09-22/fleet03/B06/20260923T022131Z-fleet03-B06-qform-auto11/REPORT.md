# fleet03/B06 auto11 — Pair-log Lp curved receiver and true-Schur obstruction

**Run:** `20260923T022131Z-fleet03-B06-qform-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Status:** `SUPPORTING_THEOREM_PROVED / TARGET-VALID INTERMEDIATE SPLICE REFUTED / FULL QFORM OPEN / CONTINUITY OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and this run's attack

The owner target remains: for every `n`, independent real coordinates with probability densities bounded by one, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `Q=X^TAX`, or give a valid counterexample. No moment, support, log-concavity, Gaussian, connected-support, diagonal-basis-independence, or sign assumption is introduced below.

The immediate B06 debt entering this run was the double-wedge diffuse / rank-two-tube chamber left by the preceding B06 report. The first attempted splice was the natural one suggested by the fresh bicolop currency: use an anchored cross-block Schur `e_2` packet, then feed that packet into the completed aggregate-`e_2` fractional receiver before paying any reciprocal local minor.

Two things were obtained.

1. A positive **pair-log `L^p` curved receiver** that converts an `L^p`, `p>1`, density for the *true full quadratic pair Schur remainder* into an `L^infinity` density for the full pair, with explicit constants. At `p=3` it combines cleanly with the preceding B06 aggregate-`e_2` theorem and, after a genuine outer original-coordinate square, with the completed fleet04/B18 dependence-safe square kernel.
2. A target-valid six-dimensional witness showing that the tempting substitution of the **cross-only anchored Schur `e_2`** for the **true full-pair Schur `e_2`** is false: same-side anchor couplings can erase the entire second-exterior bank after the actual indefinite pair is completed. This does not refute QFORM; it refutes that intermediate splice and identifies the exact currency the next argument must preserve.

The live corrections against scalar pointwise van der Corput, arbitrary-joint coarea, worst conditional projection moments, unrestricted fiber suprema, post-rotation independence, and local-minor-before-aggregation are all respected.

## 2. Source-valid analytic inputs

### 2.1 Physical indefinite-pair logarithmic envelope

The completed pair-log report

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`

proves the following. Let two ORIGINAL independent cap-one coordinates form an invertible indefinite principal pair `B`, with

`D=|det B|`, `kappa=sigma_min(B)>0`.

After completing that pair, write the full form as

`Q=(Y+m(Z))^T B (Y+m(Z))+R(Z)`.

For every cutoff `r>0`, conditionally and then after averaging,

`p_Q(t) <= 2sqrt(2)/r
          + D^(-1/2) E log_+( 2r^2/(kappa |t-R|) ).`          (2.1)

The shifts `m(Z)` may depend arbitrarily on the remainder. No independence is asserted after completing the pair.

### 2.2 Aggregate `e_2` fractional receiver

The immediately preceding B06 report

`yspennstate/math-open-problems@606257652f3c70e90c7b7f80ea7cb76c1abf689b`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T011959Z-fleet03-B06-qform-r24/REPORT.md`

proved `QFORM-CROSS-E2-FRACTIONAL-L3-v1`. For a true original-coordinate cross block `C` inside a quadratic remainder, put

`Delta_2(C)=e_2(CC^T)=sum_(physical 2x2 minors M) det(M)^2`.

If one side's projection onto `range(C)` has coordinate leverage at most `1/2`, then the complete quadratic remainder, with arbitrary self terms and all extra cross singular directions retained, has an `L^3` density with

`||p_R||_3 <= K_E Delta_2(C)^(-1/6),`                          (2.2)

where

`K_E=[3^(1/6)e^(2/3)/4] BETA(1/4,1/8)^(2/3)
    =2.983366279540... .`

This pays the complete Cauchy--Binet `e_2` bank before any reciprocal exponent.

### 2.3 Dependence-safe outer square

The completed fleet04/B18 theorem

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`

proves that after completing an ORIGINAL independent coordinate with coefficient `a!=0`,

`T=S+a V_S^2`,

with conditional density cap one for the translated square variable, one has the actual domination

`p_T(t) <= |a|^(-1/2)
           int_0^infinity p_S(t-sgn(a)u)u^(-1/2)du`,          (2.3)

and hence, if `||p_S||_infinity<=M`,

`||p_T||_infinity <=2 sqrt(M/|a|).`                           (2.4)

The designated partner `fleet04/B06` had no completed current-QFORM canonical artifact at the source lookup for this run, so none is fabricated. The compatible completed fleet04/B18 result is applied below at (5.1), not merely cited.

## 3. New theorem: pair-log smoothing from an `L^p` critical-value density

### Theorem 3.1 — `QFORM-PAIR-LOG-LP-SMOOTHING-v1`

Assume the setting of (2.1). Suppose `R` has a probability density with

`||p_R||_p <= M`, `1<p<infinity`.

Let

`s=p/(p-1)`.

Then `Q` has an essentially bounded density satisfying

`||p_Q||_infinity
 <= C_s M^(s/(s+2))
          D^(-s/(2(s+2)))
          kappa^(-1/(s+2)),`                                  (3.1)

where

`C_s=(1+2/s)(2/s)^(-2/(s+2))(2sqrt(2))^(2/(s+2))
     [4 Gamma(s+1)]^(1/(s+2)).`                               (3.2)

No independence between `R` and the pair translations is used.

#### Proof

For `A>0` define

`K_A(x)=log_+(A/|x|)`.

Its exact `L^s` norm is

`||K_A||_s^s
 =2 int_0^A [log(A/x)]^s dx
 =2A Gamma(s+1).`                                             (3.3)

Indeed set `x=A exp(-v)`. By Holder convolution,

`E log_+(A/|t-R|)
 <= M [2A Gamma(s+1)]^(1/s).`                                 (3.4)

In (2.1), `A=2r^2/kappa`, so

`p_Q(t)
 <= a r^(-1)+b r^(2/s),`                                     (3.5)

with

`a=2sqrt(2)`,
`b=D^(-1/2) M [4 Gamma(s+1)/kappa]^(1/s).`

Put `alpha=2/s`. The minimum of `a/r+b r^alpha` over `r>0` occurs at

`r^(alpha+1)=a/(alpha b)`

and equals

`(alpha+1) alpha^(-alpha/(alpha+1))
 a^(alpha/(alpha+1)) b^(1/(alpha+1)).`

Substituting `alpha=2/s` gives exactly (3.1)--(3.2). QED.

### Corollary 3.2 — the `L^3` form

For `p=3`, `s=3/2` and `Gamma(5/2)=3sqrt(pi)/4`. The constant simplifies exactly to

`C_(3/2)=7 (pi/12)^(1/7)=5.780304284267... .`

Thus

`boxed(
 ||p_Q||_infinity
 <=7(pi/12)^(1/7)
   M^(3/7) D^(-3/14) kappa^(-2/7).
 )`                                                           (3.6)

This is useful precisely because an indefinite physical pair has a logarithmic critical-value singularity: the logarithm is in every finite `L^s`, so an `L^p`, `p>1`, critical-value density is enough. No fiber supremum is taken.

## 4. New aggregate curved receiver: true pair Schur `e_2`

### Theorem 4.1 — `QFORM-PAIR-TRUE-SCHUR-E2-RECEIVER-v1`

Let a quadratic form contain an ORIGINAL invertible indefinite physical pair `B` with `D=|det B|` and `kappa=sigma_min(B)`. Complete this **full quadratic pair**, including every same-side and outside coupling, and denote its true Schur remainder by `R`.

Suppose `R` contains an original-coordinate cross block `C` for which

1. one side's projection onto `range(C)` has coordinate leverage at most `1/2`, and
2. `Delta=e_2(CC^T)>0`.

Then the full quadratic form has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= C_* D^(-3/14) kappa^(-2/7) Delta^(-1/14),
 )`                                                           (4.1)

where

`C_*=7(pi/12)^(1/7) K_E^(3/7)
    =9.234138341911... <9.235.`                               (4.2)

#### Proof

Apply the completed aggregate-`e_2` theorem (2.2) to the **true pair Schur remainder**, obtaining

`M=||p_R||_3 <=K_E Delta^(-1/6).`

Insert this into (3.6). The exponent of `Delta` is `-(1/6)(3/7)=-1/14`, giving (4.1). QED.

The important point is that the reciprocal exponent is paid only after the full physical `e_2` sum has been formed. Individual `2x2` minors are never selected.

## 5. Actual application of the completed fleet04 result

The theorem above can be nested inside a genuine outer original-coordinate square. Suppose

`T=Q_0+aV^2`, `a!=0`,

is obtained by completing one ORIGINAL coordinate, and the residual `Q_0` satisfies Theorem 4.1. Then fleet04/B18 gives, at the actual inequality

`||p_T||_infinity <=2 sqrt(||p_(Q_0)||_infinity/|a|).`        (5.1)

Therefore

`boxed(
 ||p_T||_infinity
 <= C_** |a|^(-1/2)
          D^(-3/28) kappa^(-1/7) Delta^(-1/28),
 )`                                                           (5.2)

with

`C_**=2 sqrt(C_*)=6.077545011569... <6.078.`                  (5.3)

This is `QFORM-OUTER-SQUARE-PAIR-TRUE-SCHUR-E2-v1`. The pair may have either or both diagonal entries equal to zero; only invertibility and indefiniteness of the pair are required. The square variable need not be independent of `Q_0` after completion; the fleet04/B18 conditional-mixture theorem is exactly what permits (5.1).

## 6. The first attempted bicolop splice is false

Fresh fleet02/B08 work supplies, for a **cross block** written

`H=[[z,a^T],[b,C]]`, `z!=0`,

its exact anchored identity

`W^(3)=z^2 e_2(S_cross^T S_cross),`
`S_cross=C-ba^T/z.`                                           (6.1)

That is a valid and useful identity for the cross block. The tempting B06 splice was to put `S_cross` directly into Theorem 4.1 after completing the physical anchor pair. That substitution is false in the presence of arbitrary same-side anchor couplings, because the true full quadratic pair Schur cross block is not generally `S_cross`.

### Proposition 6.1 — `QFORM-CROSS-ONLY-ANCHOR-E2-TO-FULL-PAIR-SCHUR-FALSE-v1`

There is a target-valid real symmetric matrix for which

* the left-right cross block is exactly `I_3`;
* the cross-only anchored Schur complement has `Delta_2=1`;
* the physical anchor pair is the invertible indefinite matrix `[[0,1],[1,0]]`;
* after completing that **full quadratic pair**, the true remaining left-right cross block has rank one and therefore `Delta_2=0`.

#### Exact witness

Order the six original coordinates as

`(x,y,u1,u2,v1,v2)`

and take

`A =
 [[0,1,0,1,0,0],
  [1,0,0,0,0,1],
  [0,0,0,0,1,0],
  [1,0,0,0,0,1],
  [0,0,1,0,0,0],
  [0,1,0,1,0,0]].`                                           (6.2)

Use left bank `(x,u1,u2)` and right bank `(y,v1,v2)`. The physical cross block is

`H=I_3.`                                                       (6.3)

With anchor `z=H_(x,y)=1`, the cross-only Schur complement is

`S_cross=I_2`, so `e_2(S_cross S_cross^T)=1`.

However the actual principal pair on `(x,y)` is

`B=[[0,1],[1,0]]=B^(-1).`

Completing this pair in the FULL quadratic matrix includes the same-side edges `x-u2=1` and `y-v2=1`. In the remaining order `(u1,u2,v1,v2)`, the true Schur cross block becomes

`C_true=[[1,0],[0,0]],`                                       (6.4)

so

`e_2(C_true C_true^T)=0.`                                     (6.5)

The matrix is itself inside the owner's target class. After permutation it is the direct sum of the adjacency matrix of a four-cycle and a two-vertex edge, hence its spectrum is exactly

`{-2,-1,0,0,1,2}.`                                           (6.6)

Thus it has four eigenvalues of absolute value at least one.

This proposition refutes only the intermediate inference

`large cross-only anchored e_2 => large true full-pair-Schur e_2`.

It does **not** refute the fleet02/B08 anchored identity, Theorem 4.1, or the QFORM conjecture.

## 7. Consequence for the double-wedge / rank-two-tube chamber

The positive result and the witness together sharpen the remaining B06 obligation.

The rank-two-tube cannot be closed merely by:

1. taking the cross-block bicolop identity `W=z^2 e_2(S_cross^T S_cross)`,
2. completing the physical anchor pair, and
3. inserting `S_cross` into an aggregate-`e_2` receiver.

Same-side anchor couplings can cancel one full Schur cross direction even in a target-valid matrix with `H=I_3`.

The correct next object is the **true quadratic-pair Schur cross block**. Hence the exact next implication is

`QFORM-BICOLOP-TRUE-SCHUR-E2-OR-SAMESIDE-PAYMENT-v1`:

> In the two-sided bicolop/double-wedge survivor, prove that for some invertible indefinite physical anchor pair, either the true full-pair Schur remainder carries a dimension-free aggregate `e_2` bank satisfying a product/ridge leverage gate, so Theorem 4.1 (and, when present, (5.2)) closes it, or the same-side correction that destroys that `e_2` bank itself forces a paid square/definite-pair/grouped-bank mechanism. The cancellation must be spent, not discarded.

This is narrower than generic rank-two-tube perturbation: the obstruction is now an explicit algebraic cancellation channel, witnessed by (6.2), rather than an unspecified small spectral tail.

## 8. Verification

`check_pair_lp_receiver_v2.py` and `CHECK_OUTPUT.txt` in this run directory verify the numerical constants and the exact witness. The recorded output includes

`C_PAIR_L3=5.780304284267`,
`C_PAIR_E2=9.234138341911`,
`C_OUTER_SQUARE_PAIR_E2=6.077545011569`,

and confirms

`spec(A)=(-2,-1,0,0,1,2)`,
`Delta_2(S_cross)=1`,
`Delta_2(C_true)=0`,

ending `QFORM_B06_AUTO11_CHECK_PASS`. The computation is a sanity check; the proofs above are symbolic.

## 9. Status

* `QFORM-PAIR-LOG-LP-SMOOTHING-v1`: **PROVED**.
* `QFORM-PAIR-TRUE-SCHUR-E2-RECEIVER-v1`: **PROVED**, conditional on its stated true-Schur aggregate/leverage hypotheses.
* `QFORM-OUTER-SQUARE-PAIR-TRUE-SCHUR-E2-v1`: **PROVED**, using fleet04/B18 at the actual inequality (5.1).
* `QFORM-CROSS-ONLY-ANCHOR-E2-TO-FULL-PAIR-SCHUR-FALSE-v1`: **PROVED TARGET-VALID COUNTEREXAMPLE TO THE INTERMEDIATE SPLICE**.
* Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
* Universal continuity: **NOT PROVED** by these arguments; the conclusions here are essential boundedness statements.
