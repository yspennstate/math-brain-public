SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T08:57:05Z.
attacking: the mixed-(3+2)-volume heavy-marginal residue by a weighted determinant/Fourier interpolation and a common-anchor compiler, without paying any reciprocal tiny physical minor.

# account03/B02 r25 — weighted mixed-volume Fourier interpolation and heavy-marginal compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Owner control:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full QFORM target:** OPEN  
**Target-wide universal unweighted Fourier L1 criterion:** OPEN; neither proved nor refuted here  
**Continuity:** proved on every new weighted-volume branch because `phi_Q in L1`; not proved for the full target.

## 1. Sources actually used at equations

1. The reviewed fractional three-volume theorem and its one-sided original-coordinate Weyl/BL/Hausdorff--Young calculation:
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
2. This slot's preceding equal-weight mixed theorem `QFORM-MIXED-3PLUS2-FOURIER-L1-v1`:
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T072525Z-account03-B02-qform-auto11-r23/REPORT.md`.
3. The fresh complementary account02/B02 cross-disjoint theorem and its four-anchor failure certificate:
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/account02-B02-20260923T071011Z-3508bbe2/REPORT.md`.
4. Designated partner account04/B02 theorem `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`:
   `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.
5. The fresh account03/B07 r29 hub-core transducer at commit `0e842117ca7ec8472538faa120677507f16b5c17`, whose surviving double-anchor third-volume bank is an immediate intended receiver of the theorem below whenever residual `E2` remains.

No law-uniform scalar quadratic-phase decay, post-rotation independence, arbitrary-joint coarea bound, conditional projection-height moment, or small-random-quadratic perturbation is used.

## 2. Setup

Let `I,J` be disjoint sets of ORIGINAL independent coordinates and let

`B=A[I,J]`.

All same-bank quadratic terms, outside variables/couplings, affine terms and extra spectrum are arbitrary. Fix a physical row anchor `x in I` and column anchor `y in J`.

Let

`J3 = sum det B[S,T]^2`,

over `|S|=|T|=3` with `x in S`, `y in T`. Let

`N=B[I\{x},J\{y}]`,  `E2=e2(N^T N)`,

and assume `J3 E2>0`.

Normalize the incident squared `3x3` minors by `J3`; call their row/column inclusion marginals `alpha^(3), beta^(3)`. Normalize the residual squared `2x2` minors by `E2`, extend their anchor marginals by zero, and call them `alpha^(2), beta^(2)`.

For `0<theta<1`, define

`alpha_i = theta alpha_i^(3)+(1-theta)alpha_i^(2)`,
`beta_j  = theta beta_j^(3) +(1-theta)beta_j^(2)`.

Then

`sum_i alpha_i=sum_j beta_j=2+theta`,
`alpha_x=beta_y=theta`.

## 3. New theorem — `QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1`

Let `0<theta<1` and

`1 <= q < (2+theta)/2`.

If every mixed row marginal obeys

`alpha_i <= q/2`,                                                (3.1)

then the full ambient quadratic-plus-affine form has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <= C(theta,q)
    J3^[-theta/(2(2+theta))]
    E2^[-(1-theta)/(2(2+theta))],
`

where

`C(theta,q)
 = e(2+theta)/[(2+theta-2q)sqrt(q)]
   * [theta^theta(1-theta)^(1-theta)]^[1/(2(2+theta))].`       (3.2)

The same conclusion holds if the corresponding mixed COLUMN marginals satisfy (3.1), by transposing `B`.

At `theta=1/2`, (3.2) reduces exactly to r23:

`C(1/2,q)=5e/[2^(1/5)(5-4q)sqrt(q)]`,

with resource `(J3E2)^(-1/10)`.

### 3.1 Weighted determinant interpolation

Put positive Gaussian parameters `d_i` on row maps and `e_j` on coordinate maps. In the exact diagonal-plus-PSD determinant expansion retain only two positive families:

* `A3`: incident `3x3` minors containing `x,y`;
* `A2`: residual `2x2` minors avoiding `x,y`.

Weighted AM-GM within each determinant law gives

`A3 >= J3 prod_i d_i^(alpha_i^(3))
              prod_j e_j^(1-beta_j^(3))`,                      (3.3)

`A2 >= E2 prod_i d_i^(alpha_i^(2))
              prod_j e_j^(1-beta_j^(2))`.                      (3.4)

For positive `u,v`, weighted AM-GM in the form

`u+v >= theta^(-theta)(1-theta)^(-(1-theta))
         u^theta v^(1-theta)`                                  (3.5)

gives, with

`C_theta=theta^(-theta)(1-theta)^(-(1-theta))`,

`det(D_J+B^T D_I B)
 >= C_theta J3^theta E2^(1-theta)
    prod_i d_i^alpha_i prod_j e_j^(1-beta_j).`                 (3.6)

Thus Lieb's Gaussian characterization yields

`BL <= C_theta^(-1/2)
       J3^(-theta/2)E2^(-(1-theta)/2)
       prod_i alpha_i^(-alpha_i/2)
       prod_j (1-beta_j)^(-(1-beta_j)/2).`                     (3.7)

Zero exponents are interpreted by omission/continuity. Equation (3.6) itself supplies the required BL finiteness.

### 3.2 Original-coordinate Weyl differencing and sharp HY

Condition all outside ORIGINAL coordinates. One-sided differencing in the `J` bank gives, exactly as in the reviewed source,

`|phi_Q(t)|^2 <= E_D prod_i |psi_i(2t(BD)_i)|`,                (3.8)

where `D=X_J-X'_J` has independent coordinate densities of mass one and cap at most one. Same-bank quadratic and affine phases disappear only after the legitimate Cauchy--Schwarz/differencing step; no sum/difference conditional cap is asserted.

Write `F_t(D)=prod_i |psi_i(2t(BD)_i)|`. Jensen gives

`E F_t <= (E F_t^q)^(1/q)`.

Under (3.1), sharp Hausdorff--Young at output exponent `q/alpha_i>=2` gives

`|| |psi_i(2t .)|^q ||_(1/alpha_i)
 <= (pi/|t|)^alpha_i
    (alpha_i/q)^(alpha_i/2)
    (1-alpha_i/q)^(-(q-alpha_i)/2).`                            (3.9)

Insert (3.9) into (3.7). The powers of `alpha_i` cancel. Since

`-(1-s)log(1-s)<=s`,

and `sum alpha=sum beta=2+theta`, the row and column entropy products are each at most `exp((2+theta)/2)`. Hence

`boxed:
 E F_t^q
 <= C_theta^(-1/2)e^(2+theta)q^(-(2+theta)/2)
    (pi/|t|)^(2+theta)
    J3^(-theta/2)E2^(-(1-theta)/2).
}`                                                               (3.10)

Combining (3.8), Jensen and (3.10),

`|phi_Q(t)| <= min(1,K |t|^-b)`,
`b=(2+theta)/(2q)>1`.                                           (3.11)

Thus `phi_Q in L1`. For `b>1`,

`integral_R min(1,K|t|^-b)dt=2b K^(1/b)/(b-1)`.                (3.12)

Since the power `1/b` turns the coefficient in (3.10) into

`pi e q^(-1/2) C_theta^[-1/(2(2+theta))]
 J3^[-theta/(2(2+theta))]
 E2^[-(1-theta)/(2(2+theta))]`,

Fourier inversion gives (3.2). This proves the theorem.

## 4. Heavy-gate compiler — `QFORM-MIXED32-HEAVY-MARGINAL-COMPILER-v1`

The preceding r23 report isolated the failure of its mixed marginal gate. That failure now has a quantitative physical consequence.

Take `theta=1/2`, `q=6/5`. Then the admissible gate is

`max_i alpha_i <=3/5`                                           (4.1)

on one physical side, and Theorem 3 gives

`boxed:
 ||p_Q||_infinity
 <=54.005484724 (J3E2)^(-1/10)
}`                                                               (4.2)

with a continuous density whenever (4.1) holds for the row or column marginals.

Suppose instead both the row and column gates fail. Choose a non-anchor row `i` and non-anchor column `j` with

`alpha_i>3/5`, `beta_j>3/5`.

(The anchors themselves have mixed marginal exactly `1/2`, so they cannot be the chosen heavy coordinates.) Under the equal mixture of the incident-3-minor and residual-2-minor determinant laws,

`P(i in R and j in T)
 >=P(i in R)+P(j in T)-1 >1/5`.                                (4.3)

Writing `p3` and `p2` for that joint incidence probability under the two constituent laws,

`(p3+p2)/2>1/5`,

so necessarily

`max(p3,p2)>1/5`.                                               (4.4)

Therefore one of the following **actual physical** aggregate resources is present:

**(H3)** more than one fifth of the incident third-volume also contains `i,j`:

`G3^(x,i;y,j)(B) > J3/5`;                                      (4.5)

or

**(H2)** more than one fifth of the residual second-volume contains `i,j`:

`H2^(i,j)(N) > E2/5`.                                          (4.6)

This turns the former abstract marginal failure into a finite physical common-anchor packet before any reciprocal minor is selected.

More generally, at equal mixing and any `1<q<5/4`, simultaneous failure of the row and column `q/2` gates forces a constituent common-anchor fraction `>q-1`. The choice `q=6/5` fixes a clean `1/5` fraction while retaining a finite explicit Fourier constant.

## 5. Exact algebra of the two failure packets

The two packets (4.5)-(4.6) themselves have exact Schur/star normal forms.

### 5.1 Anchored residual E2

Move physical residual row `i` and column `j` first and write

`N = [[a, r^T], [c, M]]`.

Every anchored `2x2` minor equals

`a M_kl-c_k r_l`.

Hence

`boxed:
 H2^(i,j)(N)=||aM-cr^T||_F^2.
}`                                                               (5.1)

If `a!=0`,

`H2^(i,j)(N)=a^2 ||M-cr^T/a||_F^2`,                             (5.2)

so the heavy packet is an **edge times true cross-Schur Frobenius resource**. If `a=0`,

`H2^(i,j)(N)=||c||_2^2 ||r||_2^2`,                              (5.3)

so it is an exact **two-star product resource**. No approximation and no matrix inverse is used in the zero-edge branch.

### 5.2 Double-anchored incident E3

Move rows `x,i` and columns `y,j` first and write

`B = [[P,R],[C,M]]`,

with `P` physical `2x2`. For each far row `k` and far column `l`, the corresponding anchored `3x3` determinant is

`det(P) M_kl - C_k^T adj(P) R_l`.

Therefore

`boxed:
 G3^(x,i;y,j)(B)
 = || det(P) M - C adj(P) R ||_F^2.
}`                                                               (5.4)

If `det(P)!=0`, this is

`G3=det(P)^2 ||M-CP^(-1)R||_F^2`,                              (5.5)

again an exact pair-determinant times cross-Schur Frobenius resource. If `det(P)=0`, positivity of (4.5) rules out `P=0`; hence `rank P=1` and `adj(P)` has rank one. Factoring `adj(P)=uv^T`,

`G3=||Cu||_2^2 ||R^T v||_2^2`,                                (5.6)

an exact two-star product. The product in (5.6) is invariant under reciprocal rescaling of `u,v`.

Thus the simultaneous heavy-marginal obstruction has been reduced to the same two geometric currencies on both sides: a nonzero edge/pair times a true Schur Frobenius bank, or a genuine two-star packet. This is strictly sharper than merely saying a marginal gate failed.

## 6. Application to the fresh B07 double-anchor branch

Fresh account03/B07 r29 produces, on its `H3` branch, an actual row/column anchor `(x,y)` with

`J3 >= gamma F^6`                                               (6.1)

for an explicit `gamma>0` inherited from that branch. Suppose the residual block after deleting this anchor also has

`E2 >= kappa F^4`, `kappa>0`.                                   (6.2)

Then the present `theta=1/2,q=6/5` theorem gives, whenever either `3/5` mixed marginal gate passes,

`boxed:
 ||p_Q||_infinity
 <=54.005484724 (gamma kappa)^(-1/10) F^(-1).
}`                                                               (6.3)

If both gates fail, Sections 4-5 instead convert the same `J3,E2` currency into a fixed additional physical row/column and one of the exact Schur/star packets (5.1)-(5.6). Thus r29's double-anchor third-volume is no longer sent back to an unspecified marginal obstruction whenever a quantitative residual `E2` bank survives.

This does not assert that (6.2) always follows from r29; its possible failure remains a genuine low-rank/hub branch.

## 7. Designated partner account04/B02 applied to a new inequality

The completed designated partner theorem gives, when a nonsingular physical zero-diagonal `3x3` block `H0` is present,

`||phi_Q||_2^2
 <=6 pi 2^(2/3)|det H0|^(-1/3).`                               (7.1)

On an overlap with the relaxed `theta=1/2,q=6/5` weighted tail, (3.11) has

`b=25/24`,

`K = [2^(-1/2)e^(5/2)(6/5)^(-5/4)pi^(5/2)]^(5/12)
      (J3E2)^(-5/48).`                                         (7.2)

Put `L=||phi_Q||_2`. For every `T>0`,

`integral |phi_Q|
 <= sqrt(2T)L + 48K T^(-1/24).`                                (7.3)

Optimizing at

`T^(13/24)=2sqrt(2)K/L`                                        (7.4)

gives

`integral |phi_Q|
 <=13sqrt(2)(2sqrt(2))^(12/13)
   L^(1/13)K^(12/13).`                                         (7.5)

Substituting (7.1)-(7.2) and dividing by `2pi` yields the actual partner hybrid

`boxed:
 ||p_Q||_infinity
 <=54.893293345
   |det H0|^(-1/78)
   (J3E2)^(-5/52).
}`                                                               (7.6)

This is a genuine new inequality using the completed designated-partner `L2` resource. The overlap is continuous because the weighted tail already proves `phi_Q in L1`.

## 8. Deterministic checks

`CHECK.py` and `CHECK_OUTPUT.txt` are beside this report. A deterministic seed tests 1000 random matrices for the exact anchored identities (5.1) and (5.4), verifies the reduction of the weighted theorem to r23 at `theta=1/2,q=1`, and checks the relaxed and partner-hybrid constants.

Captured output:

`weighted_theta_half_q1=11.832008884813`
`weighted_theta_half_q6over5=54.005484723448`
`max_anchored_E2_relative_error=3.403e-16`
`max_double_anchor_E3_relative_error=3.766e-16`
`partner_hybrid_constant=54.893293344995`
`STATUS=PASS`

The numerical regression is not the proof; Sections 3-7 are symbolic.

## 9. Status and first unpaid implication

The full QFORM conjecture remains OPEN, and full-target continuity remains OPEN. I did not find a valid target counterexample to a universal unweighted `integral |phi_Q|`; that stronger criterion remains OPEN target-wide.

The previous abstract mixed-marginal obstruction is now replaced by an explicit physical alternative:

* an admissible weighted mixed-volume Fourier gate, giving a continuous density; or
* a fixed common row/column carrying a universal fraction of either the incident E3 bank or residual E2 bank; and each such bank is exactly a Schur-Frobenius or two-star packet by (5.1)-(5.6).

The next B02 debt is therefore narrower:

`QFORM-WEIGHTED32-SCHURSTAR-RECEIVER-v1` — spend the exact packets (5.2)/(5.3)/(5.5)/(5.6) by a product-preserving grouped Fresnel/BL estimate, including singular cross-pair and arbitrarily curved same-bank terms, and join this with account02/B02's four-anchor cross-disjointness certificate. Do not revert to one tiny local minor or to a law-uniform pointwise oscillatory envelope.

**Independent-review status:** supporting theorem proved in this report; no new independent end-to-end review is claimed. Full target still requires two actual independent complete reviews if a candidate closure is obtained.
