SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T07:25:25Z.
attacking: the compound-hub edge-times-E2 residue by mixing incident 3-minor and residual 2-minor determinant laws inside one Brascamp-Lieb/Fourier estimate, before any reciprocal local-minor payment.

# fleet03/B02 r23 — mixed (3+2)-volume integrated Fourier theorem

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full QFORM target:** OPEN  
**Target-wide unweighted Fourier L1 criterion:** OPEN; neither proved nor refuted here  
**Continuity:** proved on the new mixed-volume branch because the characteristic function is in `L1`.

## 1. Exact scope

Let `I,J` be disjoint sets of ORIGINAL independent coordinates and let `B=A[I,J]` be the corresponding physical cross block. Same-bank quadratic terms, all outside variables/couplings, and all induced affine terms are arbitrary. No moment, support, Gaussian, log-concavity, iid, sign, or post-rotation independence assumption is used.

Fix one physical anchor row `x in I` and one physical anchor column `y in J`. Let

`J3 = sum det(B[S,T])^2`,

over all `|S|=|T|=3` with `x in S` and `y in T`. Let

`N=B[I\{x},J\{y}]`, `E2=e_2(N^T N)`,

so `E2` is the sum of squared `2x2` minors entirely avoiding the two anchors. Assume `J3 E2>0`.

Normalize the incident `3x3` squared-minor weights by `J3`; denote their row and column inclusion marginals by `alpha^(3), beta^(3)`. Normalize the residual `2x2` squared-minor weights by `E2`; extend their inclusion marginals by zero at `x,y`, and denote them by `alpha^(2), beta^(2)`. Define the mixed marginals

`alpha_i=(alpha_i^(3)+alpha_i^(2))/2`,
`beta_j =(beta_j^(3) +beta_j^(2))/2`.

Then

`sum_i alpha_i=sum_j beta_j=5/2`,
`alpha_x=beta_y=1/2`.

## 2. New theorem

### `QFORM-MIXED-3PLUS2-FOURIER-L1-v1`

For every `1<=q<5/4`, if

`alpha_i<=q/2` for every physical row `i`,

then the full ambient quadratic-plus-affine form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= [5e/(2^(1/5)(5-4q)sqrt(q))] (J3 E2)^(-1/10).
`

The same conclusion holds if the corresponding mixed COLUMN marginals satisfy `beta_j<=q/2`, by applying the theorem to `B^T`.

At the endpoint-safe choice `q=1`, the gate is `max alpha_i<=1/2` and

`boxed:
 ||p_Q||_infinity
 <= (5e/2^(1/5)) (J3 E2)^(-1/10)
 <11.832009 (J3 E2)^(-1/10).
`

The proof is an actual unweighted integrated-Fourier argument. It does not use a law-uniform pointwise scalar quadratic-phase decay estimate.

## 3. Determinant interpolation: combine rank 3 and rank 2 before inversion

Write positive Gaussian parameters `d_i` on the row maps and `e_j` on the physical coordinate maps. The exact diagonal-plus-PSD determinant expansion is

`det(D_J+B^T D_I B)
 = sum_(S,T, |S|=|T|) det(B[S,T])^2
     prod_(i in S)d_i prod_(j notin T)e_j.`

Retain only two disjoint collections of terms:

* `A3`: the incident `3x3` minors containing `(x,y)`;
* `A2`: the residual `2x2` minors avoiding `(x,y)`.

Weighted AM-GM inside the first family gives

`A3 >= J3 prod_i d_i^(alpha_i^(3))
              prod_j e_j^(1-beta_j^(3)).`

The same argument in the second family gives

`A2 >= E2 prod_i d_i^(alpha_i^(2))
              prod_j e_j^(1-beta_j^(2)).`

Because the determinant is at least `A3+A2`, ordinary AM-GM yields

`det(D_J+B^T D_I B)
 >= 2 sqrt(J3 E2)
    prod_i d_i^alpha_i prod_j e_j^(1-beta_j).`                  (3.1)

This is the essential missing implication: the third-volume and second-volume currencies are multiplied **before** any individual minor is inverted.

By Lieb's Gaussian characterization of the Brascamp-Lieb constant, (3.1) gives

`BL <= 2^(-1/2)(J3 E2)^(-1/4)
       prod_i alpha_i^(-alpha_i/2)
       prod_j (1-beta_j)^(-(1-beta_j)/2).`                       (3.2)

Zero exponents have their continuous value one. The determinant lower bound itself proves finiteness of the datum, including endpoint columns.

## 4. Decoupling and sharp scalar Hausdorff-Young

Use the standard original-coordinate decoupling on the `J` bank. For the full form

`F(X_I)+2 X_I^T B X_J+G(X_J)`

(after conditioning any outside original coordinates), let `D=X_J-X'_J`, where `X'_J` is an independent copy. If `psi_i` is the characteristic function of the original cap-one density in row coordinate `i`, then

`|phi_Q(t)|^2 <= E_D prod_i |psi_i(2t(BD)_i)|.`                  (4.1)

The difference-coordinate densities have mass one and cap at most one. No sum/difference conditional density cap and no post-rotation independence is asserted.

Set `F_t(D)=prod_i |psi_i(2t(BD)_i)|`. Since the `D` law is a probability law,

`E F_t <= (E F_t^q)^(1/q)`.

For each row, the sharp Hausdorff-Young inequality at output exponent `q/alpha_i>=2` (the marginal gate is exactly what guarantees this) gives

`|| |psi_i(2t .)|^q ||_(1/alpha_i)
 <= (pi/|t|)^alpha_i
    (alpha_i/q)^(alpha_i/2)
    (1-alpha_i/q)^(-(q-alpha_i)/2).`                            (4.2)

Insert (4.2) into (3.2). The powers of `alpha_i` cancel. Since

`-(1-s)log(1-s)<=s`, `0<=s<1`,

and `sum alpha=sum beta=5/2`, the row and column entropy factors are each at most `e^(5/4)`. Hence

`boxed:
 E F_t^q
 <= 2^(-1/2) e^(5/2) q^(-5/4)
    (pi/|t|)^(5/2) (J3 E2)^(-1/4).
}`                                                               (4.3)

Combining (4.1), Jensen and (4.3),

`|phi_Q(t)| <= min(1,K_q |t|^(-5/(4q)))`,                       (4.4)

where

`K_q=[2^(-1/2)e^(5/2)q^(-5/4)pi^(5/2)(J3E2)^(-1/4)]^(1/(2q)).`

Because `q<5/4`, the exponent `b=5/(4q)` is strictly bigger than one. Thus `phi_Q in L1`.

## 5. Exact inversion constant

For `b>1`,

`int_R min(1,K|t|^-b) dt
 =2b/(b-1) K^(1/b).`

Fourier inversion and (4.4) therefore give

`||p_Q||_infinity
 <= b/[pi(b-1)] K_q^(1/b)
 = [5e/(2^(1/5)(5-4q)sqrt(q))](J3E2)^(-1/10).`

This proves the theorem. Since `phi_Q in L1`, the inverse Fourier transform supplies a continuous density vanishing at infinity.

## 6. Actual application to the compound-hub edge/E2 branch

The preceding own B02 compound-hub compiler proved, in the strict no-pivot chamber with

`tau=delta_r=delta_c=1/64`,

that there is a physical anchor pair with joint incident third-volume

`J3 >= (31/288) Z`,                                               (6.1)

where `Z=W3(B)`, and on the edge-times-E2 alternative its residual bank satisfies

`E2 > (992/585) Z`.                                               (6.2)

Therefore

`J3 E2 > [(31/288)(992/585)] Z^2
         =0.182526115859449... Z^2.`                              (6.3)

Whenever the mixed row or column `q=1` marginal gate holds, the new theorem gives the concrete continuous-density exit

`boxed:
 ||p_Q||_infinity
 <14.025747 Z^(-1/5).
}`                                                                 (6.4)

This is a genuine payment of the aggregate edge/E2 currency by an unweighted `L1` Fourier estimate. It does not select or divide by one tiny `2x2` or `3x3` minor.

The remaining analytic gate is now explicit: if the mixed determinant law is itself concentrated so that some mixed marginal exceeds `1/2` (or, more generally, exceeds `q/2` for every usable `q<5/4` on both sides), one must compile that concentration into a new grouped-coordinate/pivot resource rather than discarding it.

## 7. Designated partner fleet04/B02 applied to an actual inequality

The designated partner result is

`QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B02/20260922T193108Z-fleet04-B02-QFORM-r2/REPORT.md`.

If a residual/full form contains a nonsingular physical zero-diagonal `3x3` block `H0`, the partner proves

`||phi_Q||_2^2 <= 6 pi 2^(2/3)|det H0|^(-1/3).`                 (7.1)

On an overlap with the new mixed `q=1` tail, put

`L=||phi_Q||_2`,
`K=2^(-1/4)e^(5/4)pi^(5/4)(J3E2)^(-1/8)`.

For every `T>0`, Cauchy-Schwarz on low frequencies and (4.4) on high frequencies give

`int |phi_Q(t)| dt
 <= sqrt(2T)L + 8K T^(-1/4).`                                   (7.2)

Optimizing at `T=(2sqrt(2)K/L)^(4/3)` yields

`int |phi_Q| <= 6sqrt(2) L^(1/3)K^(2/3).`                       (7.3)

Using (7.1) and Fourier inversion gives the actual hybrid inequality

`boxed:
 ||p_Q||_infinity
 <=12.662409
    |det H0|^(-1/18)(J3E2)^(-1/12).
}`                                                                 (7.4)

This explicitly uses the completed designated-partner Fourier `L2` resource in a new inequality. The overlap has a continuous density because (7.3) proves `phi_Q in L1`.

## 8. Relation to the current fleet02/B02 checkpoint

A same-hour fleet02/B02 checkpoint independently proposed mixing the incident rank-three and residual rank-two determinant families. It correctly identified an effective five-factor Fourier exponent, but explicitly marked its determinant expansion/scaling calculation provisional. The derivation above completes that calculation with the exact factor `2 sqrt(J3E2)`, entropy `e^(5/2)`, and the sharper `q=1` density coefficient `5e/2^(1/5)=11.8320088848...`.

No claim is made that the fleet02 checkpoint had already proved this theorem; this report supplies the proof used here.

## 9. Deterministic regression

`CHECK.py` tests (3.1) on 500 seeded random `5x5` matrices and positive Gaussian parameters. The smallest observed ratio

`det(D_J+B^T D_I B) /
 [2 sqrt(J3E2) prod d^alpha prod e^(1-beta)]`

was `3.164117398317658`; there were zero failures. It also checks the constants in (6.3)-(6.4) and (7.4). `CHECK_OUTPUT.txt` records `STATUS=PASS`.

This finite computation is only a regression. The determinant expansion and analytic proof above are the proof.

## 10. Status and first unpaid implication

The full QFORM conjecture remains OPEN. The target-wide universal unweighted `int |phi_Q|` criterion remains OPEN: this run proves it only on the mixed-(3+2)-volume branch under the stated determinant-marginal gate and does not supply a target-valid counterexample outside that gate.

The first B02 debt after this run is now:

`QFORM-MIXED32-HEAVY-MARGINAL-COMPILER-v1`:

> If both mixed row and mixed column laws have an atom above every admissible `q/2`, use the resulting common heavy coordinate incidence to compile either a paid physical pivot/pair, a zero-diagonal triple, or a genuinely two-star/grouped fractional-Fourier packet, without selecting a reciprocal tiny local minor.

This is complementary to the previously isolated small-`F` two-heavy-star/near-leaf branch; the two residues should be joined through their common heavy-incidence geometry rather than attacked by another one-sided pivot.

**Status:** new supporting theorem proved; continuous density on its scope; full target OPEN; global continuity OPEN; universal target-wide Fourier `L1` OPEN.
