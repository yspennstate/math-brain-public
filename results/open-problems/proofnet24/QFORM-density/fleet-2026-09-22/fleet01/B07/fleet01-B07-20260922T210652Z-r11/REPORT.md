SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B07, 2026-09-22T21:06:52Z.
attacking: coordinate-minor selection via a sharp compound-order transfer E3 -> E2, then fuse the designated partner's effective-dimension-three density theorem with the effective-dimension-two near-coloop collar.

# fleet01/B07 — compound-order transfer and two-scale coordinate-minor collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `fleet01-B07-20260922T210652Z-r11`  
**Assignment:** coordinate minor selection / GEOMETRY  
**Initial control commit:** `yspennstate/math-research-brain@4ccdb6c551bc0372651374b3da132ff3ae8a7067`  
**Pre-write refresh:** `yspennstate/math-research-brain@a0ca57f8ad2170f13c1de4dee842239fcd80f420`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL THEOREM / FULL TARGET OPEN`.

The exact target is unchanged: independent real original coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, no moment/support/log-concavity/sign/diagonal assumptions. The full continuity conclusion remains open. Nothing below uses post-rotation independence, the refuted arbitrary-joint coarea lemma, law-uniform pointwise quadratic-phase decay, worst conditional projection caps, or reciprocal extraction of one tiny coordinate minor.

## 1. Compact conditional end-to-end argument for the coordinate-minor branch

The current fleet03/B07 O0 reduction supplies an original-coordinate cross block `B` with

`E_3(B):=e_3(BB^T)>=1/256`.

The designated partner fleet02/B07 proved `QFORM-EK-EFFECTIVE-DIMENSION-PAYMENT-v1`: at the unique ridge scale with effective dimension three, the entire third compound is paid directly by a continuous-density estimate whenever one physical side has maximum ridge leverage at most `2/3`; exact cross rank three is also paid with no leverage assumption.

The first missing implication was therefore to understand what the same third-compound resource forces at effective dimension two, where fleet03/B07 has a half-Riesz collar and a precise two-sided near-coloop theorem. This run proves an exact dimension-free transfer `E_3 -> E_2`, and it is strong enough to import the entire effective-dimension-two collar without any new selection assumption.

Consequently O0 is now reduced as follows:

1. exact cross rank three: continuously bounded density, partner fleet02/B07;
2. rank >3 and effective-dimension-three ridge-diffuse on one side: continuously bounded density, partner fleet02/B07;
3. at effective dimension two, if one side is not a `23/24` near-coloop: uniform half-Riesz bound `<120`;
4. otherwise there are physical row/column anchors carrying a constant fraction of the complete second compound, quantitatively producing an edge-times-bank or two-star reserve `>1/200`.

The only unpaid coordinate-minor implication is therefore the product-preserving payment of that anchored edge/two-star reserve (or its routing into an already-paid scalar-pivot/pair-log/zero-self/grouped branch). No individual reciprocal minor is selected.

## 2. Dependencies actually read and used

### Designated partner fleet02/B07

`QFORM-EK-EFFECTIVE-DIMENSION-PAYMENT-v1`, complete proof:

`yspennstate/math-open-problems@1ee49306b266915b9806d78498d9861f5a642b4a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T203121Z-fleet02-B07-QFORM-4f9c2e/REPORT.md`.

Its exact statements used here are:

- if `rank(B)=3`, then
  `||p_Q||_infinity <= 3e E_3(B)^(-1/6)` with a continuous density;
- if `rank(B)>3`, at the unique `gamma_3` such that
  `tr K_(gamma_3)=3`, and one physical side has
  `max diag K_(gamma_3)<=2/3`, then
  `||p_Q||_infinity <= 9e sqrt(3/8) E_3(B)^(-1/6)`, again with a continuous density.

All same-side blocks, outside couplings, affine terms, signs and extra spectrum remain present.

### Compatible completed fleet03/B07 result

`QFORM-E2-RIDGE-HALFRIESZ-COLLAR-v1` and `QFORM-TWOSIDED-RIDGE-COLOOP-ANCHOR-v1`, complete proof:

`yspennstate/math-open-problems@a20d669ff2c433cc70cb70234f49431da4518fa5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T203738Z-fleet03-B07-qform-r17/REPORT.md`.

At the unique `gamma_2` with `tr K_(gamma_2)=2`, it proves:

- if one physical side has `max diag K_(gamma_2)<=23/24`, then
  `H_(1/2)(R)<=C_* E_2(B)^(-1/8)`, where
  `C_*=48 sqrt(e)(24/23)^(1/4)=79.98514376669046...`;
- if both sides instead have a coordinate leverage `>23/24`, there are physical anchors `(i,j)` such that
  `M_ij:=sum_(k!=i,l!=j) det B[{i,k},{j,l}]^2 > E_2(B)/2`, and if
  `B=[[b,r^T],[c,C]]` in those anchored coordinates then
  `M_ij=||bC-c r^T||_F^2`, hence either
  `b^2||C||_F^2>E_2(B)/8` or `||r||_2^2||c||_2^2>E_2(B)/8`.

## 3. New theorem: sharp dimension-free transfer from the third compound to the second

Let the positive eigenvalues of `BB^T` be `x_1,...,x_r`, where `r=rank(B)>=3`. Write

`E_j=e_j(x_1,...,x_r)`.

### Theorem 3.1 — `QFORM-COMPOUND-ORDER-TRANSFER-v1`

For every `r>=3`,

`boxed(
 E_2^3 >= (9/2) [r(r-1)/(r-2)^2] E_3^2
          >= (9/2) E_3^2.
)`

The rank-dependent constant in the first inequality is sharp for equal nonzero singular values.

### Proof

Newton's inequality in normalized form gives

`(E_2 / C(r,2))^2 >= (E_1/r)(E_3/C(r,3))`.

Therefore

`E_2^2 >= c_r E_1 E_3`,

where

`c_r=C(r,2)^2/[r C(r,3)]
    =(3/2)(r-1)/(r-2).`                                      (3.1)

Cauchy--Schwarz gives

`E_1^2=(sum x_a)^2 >= [2r/(r-1)] E_2`,                        (3.2)

because `E_2=(E_1^2-sum x_a^2)/2` and
`sum x_a^2>=E_1^2/r`.

Substituting (3.2) into (3.1),

`E_2^2 >= c_r sqrt(2r/(r-1)) E_2^(1/2) E_3`.

After division by `E_2^(1/2)` and squaring,

`E_2^3 >= c_r^2 [2r/(r-1)] E_3^2
 = (9/2) [r(r-1)/(r-2)^2] E_3^2.`                            (3.3)

Since `r(r-1)>(r-2)^2`, the universal second inequality follows.
For equal `x_a=x`, both normalized Newton and Cauchy--Schwarz are equalities, proving sharpness of the rank-dependent factor. QED.

### Corollary 3.2 — the O0 third-compound resource automatically supplies S0-scale second-compound mass

If

`E_3(B)>=1/256`,

then

`boxed(
 E_2(B) >= c_2 := (9/2^17)^(1/3)
 =0.04094908428451402... >1/25>1/48.
)`                                                         (3.4)

Thus no separate second-compound selection theorem is needed on O0: the whole second-compound bank is already dimension-free.

This is a scale-sensitive fact, not a local-minor claim. Individual `2x2` minors may still all be tiny.

## 4. Actual application of the designated partner result

Apply fleet02/B07's theorem to the O0 inequality `E_3(B)>=1/256`.

### Exact rank three

`||p_Q||_infinity
 <=3e 256^(1/6)
 =20.548922971333656... .`                                    (4.1)

The density is continuous.

### Rank >3, effective-dimension-three diffuse branch

At `tr K_(gamma_3)=3`, if either physical side has maximum ridge leverage at most `2/3`,

`||p_Q||_infinity
 <=9e sqrt(3/8) 256^(1/6)
 =37.750782032642554... .`                                    (4.2)

Again the density is continuous.

Therefore any O0 state not already continuously paid by the designated partner has rank at least four and is bi-heavy at effective dimension three.

## 5. New two-scale fusion: O0 reduces to a quantitatively anchored near-coloop packet

Independently of the effective-dimension-three leverage, Corollary 3.2 allows fleet03/B07's effective-dimension-two theorem to be applied to the same physical cross block.

Let `gamma_2` be the unique scale such that `tr K_(gamma_2)=2`.

### Moderate effective-dimension-two branch

If either physical side satisfies

`max diag K_(gamma_2)<=23/24`,

then

`H_(1/2)(R)
 <=79.98514376669046... c_2^(-1/8)
 =119.2556065018121... <120.`                                (5.1)

This is a half-Riesz estimate, not by itself a density theorem. It is the exact input needed by the existing physical scalar-pivot transducer.

### Two-sided near-coloop branch

Otherwise fleet03/B07 gives physical anchors `i,j` with

`M_ij>E_2(B)/2 >=c_2/2 >1/50.`                               (5.2)

Writing the cross block in anchored form

`B = [[b, r^T], [c, C]]`,

we have exactly

`M_ij=||bC-c r^T||_F^2`.                                     (5.3)

Hence

`boxed(
 b^2||C||_F^2 > E_2/8 >1/200
)`                                                            (5.4)

or

`boxed(
 ||r||_2^2 ||c||_2^2 > E_2/8 >1/200.
)`                                                            (5.5)

This improves the previous generic S0 reserve `1/384` on the O0 subbranch, and it is obtained solely from the already available third-compound currency.

The conclusion is invariant under arbitrarily diffuse coordinate realizations: the second row/column coordinates in (5.2)-(5.5) remain summed over their full physical banks.

## 6. Relation to the previous fleet01/B07 fixed-pair theorem

The previous run proved, for every physical row pair `P` of a matrix `B`,

`sum_(k notin P) det(B_(P union {k})B_(P union {k})^T)
 =det(B_PB_P^T) ||B_R(I-Pi_P)||_F^2`,                         (6.1)

and for a contraction `K` of trace three the corresponding Schur residual always has trace at least one.

The present result is a different mechanism: instead of fixing a pair and studying its residual third direction, it transfers the complete third exterior mass down one compound level before making any physical selection. The two mechanisms are complementary. Equation (6.1) remains the exact local description once the new two-scale collar forces an anchored pair/edge configuration.

## 7. First unpaid implication

`QFORM-O0-ANCHORED-EDGE-OR-TWOSTAR-PAYMENT-v2`:

Starting from the surviving near-coloop branch

`rank(B)>=4`,
`E_3(B)>=1/256`,
`E_2(B)>1/25`,
`maxdiag K_L(gamma_2)>23/24`,
`maxdiag K_R(gamma_2)>23/24`,

and the physical reserve

`b^2||C||_F^2>1/200`

or

`||r||^2||c||^2>1/200`,

prove a translation-uniform, product-preserving density or half-Riesz estimate while retaining arbitrary same-bank curvature and extra spectrum; alternatively route the reserve to an already-paid scalar-pivot, pair-log, zero-self, grouped-coordinate, or exact-cross-rank branch.

A valid proof must spend the bank before reciprocal inversion. The two-star alternative alone is only rank two and cannot be mislabeled as a three-direction density theorem. The edge-times-bank alternative also needs a genuinely second residual direction or another paid curvature mechanism. These are the exact remaining difficulties.

## 8. Exact checks

The accompanying checker verifies on exact rational spectra, for ranks 3 through 10, the sharper finite-rank inequality

`E_2^3 >= (9/2) r(r-1)/(r-2)^2 E_3^2`,

and records the constants (3.4), (5.1), (5.2)-(5.5). The proof itself is the algebra above; the finite test is only a regression check.

Numerical constants:

`c_2 =0.04094908428451402...`,
`c_2/2=0.02047454214225701... >1/50`,
`c_2/8=0.005118635535564252... >1/200`,
`79.98514376669046*c_2^(-1/8)=119.2556065018121...`.

## 9. Status

This is a genuine supporting structural theorem and a strict reduction of the O0 coordinate-minor branch. It is **not** a proof of the full QFORM conjecture and **not** a counterexample. Continuous density is proved only on the designated partner's exact-rank-three and effective-dimension-three ridge-diffuse branches. The moderate effective-dimension-two branch currently gives a half-Riesz bound, while the two-sided near-coloop branch gives a physical determinant reserve.
