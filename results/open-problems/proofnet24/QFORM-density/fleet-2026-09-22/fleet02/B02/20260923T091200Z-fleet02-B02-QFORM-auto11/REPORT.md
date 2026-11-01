SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T09:12:00Z.
attacking: the first unpaid near-coloop/four-anchor E2 collar by conditioning the mixed incident-E3/residual-E2 determinant laws on physical cross-disjointness and keeping an actual integrated Fourier estimate.

# fleet02/B02 — incident-(3+2) cross-disjoint sharp-HY compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T091200Z-fleet02-B02-QFORM-auto11`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the new `L1_t` branch only; the unrestricted continuity conclusion remains open.  
**Target-wide unweighted Fourier criterion:** `OPEN_NOT_REFUTED`.

## 1. Exact obligation and source boundary

The target remains the unrestricted owner target: the coordinates are independent ORIGINAL real variables with probability densities at most one; `A` is real symmetric and has at least three eigenvalues of modulus at least one; there are no moments, support, log-concavity, identical-law, diagonal-basis-independence or post-rotation-independence assumptions.

This run uses the newest-Claude source package at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`,

and the current sharp-Hausdorff--Young volume-stability derivation at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

The analytic constants/endpoints actually used below were independently checked in this run. For a physical cross block `M=A[I,J]`, with `Z3=E3(M)=e3(M^T M)`, the reviewed theorem is

`||p_Q||infinity <= 3e/[(3-2q)sqrt(q)] Z3^(-1/6)`                (1.1)

when every third-volume row marginal is at most `q/2`, `1<=q<3/2`; transpose gives the column version. The endpoint `q=3/2` is not admissible: the high-frequency power becomes exactly one. The determinant expansion remains valid when a column marginal is one by omitting that coordinate map, as in the source proof. The same sharp-HY refinement at exterior degree five gives the paid ungated exit

`||p_Q||infinity <= (5e/sqrt(2)) E5(M)^(-1/10)`.                (1.2)

Both are genuine `phi_Q in L1` conclusions. The run does not use a law-uniform pointwise scalar Fresnel estimate.

The immediately preceding fleet02/B02 theorem is

`QFORM-EDGE-E2-CROSSDISJOINT-SHARP-HY-L1-v1`,

`yspennstate/math-open-problems@5d35b697d95d20e66fd72c96a5ea2dffa1201958`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/fleet02-B02-20260923T071011Z-3508bbe2/REPORT.md`.

It paid an edge-times-E2 branch but required a nonzero outer physical cross edge in order to express the incident third-volume through a cross-only Schur packet. The first unpaid implication was to spend the resulting four-anchor residual E2 hub without silently identifying a cross-only Schur complement with a TRUE physical-pair Schur complement.

The latest completed designated partner `fleet03/B02` is r25,

`QFORM-WEIGHTED-MIXED32-FOURIER-L1-v1`,

`yspennstate/math-open-problems@ff8ec2ee90d4846f39e728e1ca20d50c717cc894`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T085705Z-fleet03-B02-qform-r25/REPORT.md`.

Its exact common-anchor identity is applied at an inequality in Section 6 below.

The correction boundary is retained throughout: cross-only Schur algebra is not promoted to a TRUE full symmetric pair Schur residual; small matrix norm is not treated as a uniformly small random quadratic perturbation; a dependent projected pair is not assigned an independent cap after conditioning; and no random-variable rotation is used.

## 2. Setup: one live physical cross block

Condition any original coordinates outside two disjoint physical banks `I,J`. The resulting quadratic-plus-affine form has the same cross block

`B=A[I,J]`,                                                       (2.1)

while all same-bank quadratic terms and conditioning-generated affine terms are arbitrary.

Fix a physical row anchor `x in I` and column anchor `y in J`. Let

`J3 = sum det B[{x} union R,{y} union T]^2`,                     (2.2)

where `R subset I\{x}`, `T subset J\{y}`, `|R|=|T|=2`. Let

`N=B[I\{x},J\{y}]`,
`E2=e2(N^T N)=sum_(|R|=|T|=2) det N[R,T]^2`.                    (2.3)

Assume `J3 E2>0`.

Let `mu3` be the normalized squared-minor law from (2.2), viewed as a law on the residual pairs `(R3,T3)`, and let `mu2` be the normalized squared-2-minor law of `N`, on `(R2,T2)`. Draw these samples independently and define

`delta_r=P(R3 cap R2=empty)`,
`delta_c=P(T3 cap T2=empty)`.                                    (2.4)

These are deterministic functions of the literal physical cross block. They do not rotate the random variables.

## 3. Main theorem — `QFORM-INCIDENT32-CROSSDISJOINT-SHARP-HY-L1-v1`

### Theorem 3.1

If `delta_r>0`, then the full ambient quadratic-plus-affine form has a continuous density vanishing at infinity, and

`boxed:
 integral_R |phi_Q(t)| dt
 <= 10*pi*e*2^(-1/5)
    delta_r^(-1/10)(J3 E2)^(-1/10),
}`                                                                  (3.1)

hence

`boxed:
 ||p_Q||infinity
 <= 5e*2^(-1/5)
    delta_r^(-1/10)(J3 E2)^(-1/10)
 < 11.832009 delta_r^(-1/10)(J3 E2)^(-1/10).
}`                                                                  (3.2)

The same conclusion holds with `delta_c` in place of `delta_r`, by transposing the physical cross block.

The theorem requires no nonzero outer cross edge `B_xy`; in particular it strictly removes the pivot hypothesis from the preceding fleet02/B02 cross-disjoint theorem.

### 3.2 Product-preserving Weyl differencing

One-sided Cauchy--Schwarz/Weyl differencing in the original `J` bank gives the source-valid bound

`|phi_Q(t)|^2
 <= integral_(R^J) prod_(i in I) h_i((Bw)_i)
                    prod_(j in J) g_j(w_j) dw`,                  (3.3)

where

`h_i(s)=|psi_i(2ts)|`,                                           (3.4)

`psi_i` is the characteristic function of the original cap-one density `f_i`, and

`g_j=f_j*tilde f_j`, `0<=g_j<=1`, `integral g_j=1`.             (3.5)

The same-bank quadratic phases and affine phases disappear only through this legitimate differencing step. No independence of a sum/difference pair is asserted.

### 3.3 Conditioning the determinant laws

Condition the product law `mu3 tensor mu2` on the row-disjoint event

`E_r={R3 cap R2=empty}`.                                         (3.6)

Let the two conditioned marginal laws be `mu3'` and `mu2'`. Since the conditioned joint law has KL divergence `log(1/delta_r)` from the original product law and KL splits into marginal divergences plus mutual information,

`D3+D2:=D(mu3'||mu3)+D(mu2'||mu2)
 <= log(1/delta_r)`.                                             (3.7)

Write their residual row marginals as `alpha_i^(3),alpha_i^(2)` and residual column marginals as `beta_j^(3),beta_j^(2)`. Define the equal-mixture exponents

`alpha_x=1/2`,
`alpha_i=(alpha_i^(3)+alpha_i^(2))/2` for i!=x,                 (3.8)

and

`beta_y=1/2`,
`beta_j=(beta_j^(3)+beta_j^(2))/2` for j!=y.                    (3.9)

Because the two sampled residual row pairs are disjoint pointwise under (3.6),

`0<=alpha_i<=1/2` for every i, `sum_i alpha_i=5/2`.             (3.10)

On the column side only

`0<=beta_j<=1`, `sum_j beta_j=5/2`                              (3.11)

is needed.

### 3.4 Two positive determinant families

Put positive Gaussian parameters `d_i` on the row maps `w -> (Bw)_i` and `e_j` on the coordinate maps `w -> w_j`. In the exact diagonal-plus-PSD determinant expansion retain two nonnegative basis families.

The incident-three family gives, by weighted AM--GM with `mu3'`,

`A3 >= J3 exp(-D3) d_x
       prod_(i!=x)d_i^(alpha_i^(3))
       prod_(j!=y)e_j^(1-beta_j^(3)).`                           (3.12)

The residual-two family selects two rows of `N` and the coordinate basis vectors outside their selected residual columns. It therefore gives

`A2 >= E2 exp(-D2) e_y
       prod_(i!=x)d_i^(alpha_i^(2))
       prod_(j!=y)e_j^(1-beta_j^(2)).`                           (3.13)

The full Gaussian determinant contains both families, so

`det(D_J+B^T D_I B)
 >= A3+A2
 >= 2 sqrt(A3 A2)`                                               (3.14)

and hence

`det(D_J+B^T D_I B)
 >=2 (J3E2)^(1/2) exp[-(D3+D2)/2]
   prod_i d_i^alpha_i prod_j e_j^(1-beta_j).`                   (3.15)

Lieb's Gaussian characterization of the geometric Brascamp--Lieb constant therefore yields

`BL <=2^(-1/2) exp[(D3+D2)/4](J3E2)^(-1/4)
       prod_i alpha_i^(-alpha_i/2)
       prod_j(1-beta_j)^(-(1-beta_j)/2).`                        (3.16)

Zero exponents are omitted/understood by continuity. Formula (3.15) itself establishes BL finiteness, including endpoint columns with `beta_j=1`.

### 3.5 Sharp Hausdorff--Young at the exact q=1 gate

For every `0<c<=1/2`, Beckner's sharp Hausdorff--Young inequality in the source normalization gives

`integral_R |psi_i(2ts)|^(1/c) ds
 <= (pi/|t|) sqrt(c)
    (1-c)^(-(1-c)/(2c)).`                                       (3.17)

Apply Brascamp--Lieb to (3.3), writing the row factors with exponents `alpha_i`. The powers `alpha_i^(alpha_i/2)` from (3.17) cancel the inverse-alpha normalization in (3.16). The remaining row entropy factor obeys

`prod_i(1-alpha_i)^(-(1-alpha_i)/2) <= exp[(sum alpha_i)/2]=e^(5/4),` (3.18)

and the column entropy factor satisfies

`prod_j(1-beta_j)^(-(1-beta_j)/2) <= e^(5/4)`                   (3.19)

because `-(1-u)log(1-u)<=u` and `sum beta=5/2`.

Combining (3.3), (3.16)--(3.19) gives

`|phi_Q(t)|^2
 <=2^(-1/2)e^(D3+D2)/4 e^(5/2) pi^(5/2)
   (J3E2)^(-1/4)|t|^(-5/2).`                                    (3.20)

By (3.7),

`|phi_Q(t)|
 <= min{1,
  2^(-1/4)e^(5/4)pi^(5/4)
  delta_r^(-1/8)(J3E2)^(-1/8)|t|^(-5/4)}.`                     (3.21)

The exponent `5/4>1` is the paid integrated-Fourier gain. For every `A>0`,

`integral_R min(1,A|t|^(-5/4))dt=10 A^(4/5).`                  (3.22)

Equations (3.21)--(3.22) prove (3.1), and Fourier inversion proves (3.2), continuity and vanishing at infinity. QED.

## 4. Exact complement — a common physical residual anchor

The theorem has an explicit structural failure certificate.

If `delta_r<eta`, then averaging over `(R3,T3)~mu3` shows that some residual row pair `H` in the support of `mu3` obeys

`P_mu2(R2 cap H !=empty)>1-eta`.                                (4.1)

Likewise, if `delta_c<eta`, some residual column pair `L` obeys

`P_mu2(T2 cap L !=empty)>1-eta`.                                (4.2)

If both disjointness probabilities are `<eta`, a union bound under `mu2` gives

`sum_(R cap H !=empty, T cap L !=empty) det N[R,T]^2
 >(1-2eta)E2.`                                                   (4.3)

For a physical residual row `i` and column `j`, let

`H2^(i,j)(N)
 =sum_(R contains i, T contains j) det N[R,T]^2`.                (4.4)

Summing (4.4) over the four pairs `(i,j) in H x L` counts every minor appearing in (4.3) at least once. Hence some fixed physical pair `(i,j)` satisfies

`boxed:
 H2^(i,j)(N) >(1-2eta)E2/4.
}`                                                                  (4.5)

At `eta=1/16`,

`boxed: H2^(i,j)(N)>7E2/32.`                                    (4.6)

Thus failure of the new `L1_t` branch does not return to a diffuse marginal statement: it forces a single common physical residual row/column anchor carrying a fixed fraction of the entire second exterior volume.

## 5. Live D' / D5 application

Return to a physical cross block `B` with

`Z3=E3(B)>0`.                                                     (5.1)

At `q=4/3`, D' pays the row or column branch if the corresponding third-volume marginals are all at most `2/3`. Suppose instead both orientations fail. Choose a heavy physical row `x` and heavy physical column `y`; their inclusion probabilities in the normalized squared-third-minor law are each `>2/3`. Therefore

`P(x in row triple AND y in column triple)>1/3`,                 (5.2)

so their joint incident mass satisfies

`boxed: J3>Z3/3.`                                                (5.3)

If `E2(N)>0` and

`max(delta_r,delta_c)>=eta`,                                     (5.4)

Theorem 3.1 and (5.3) give the actual inequality

`boxed:
 ||p_Q||infinity
 < (5e/2^(1/5)) [3/(eta Z3 E2)]^(1/10).
}`                                                                  (5.5)

At `eta=1/16`,

`boxed:
 ||p_Q||infinity
 <17.425395 (Z3E2)^(-1/10).
}`                                                                  (5.6)

This is a direct integrated-characteristic-function bound in the two-sided D' failure collar. It keeps arbitrary same-bank curvature and all additional spectrum. If instead the ungated D5 currency is substantial, equation (1.2) remains the independent paid exit.

If both disjointness probabilities are `<1/16`, (4.6) supplies the common-anchor packet instead. Thus after D', D5 and the new theorem, the live residual is concentrated on one actual physical row/column pair of the residual second compound.

## 6. Completed designated partner applied to an actual inequality

Apply the latest completed `fleet03/B02` r25 identity to the exact common-anchor packet from Section 4. Move its physical residual row `i` and column `j` first and write

`N=[[a,r^T],[c,M]].`                                             (6.1)

Partner r25 proves the exact algebraic identity

`boxed:
 H2^(i,j)(N)=||aM-c r^T||_F^2.
}`                                                                  (6.2)

Combining (4.5) and (6.2) gives the new quantitative obstruction

`boxed:
 ||aM-c r^T||_F^2 >(1-2eta)E2/4.
}`                                                                  (6.3)

At the concrete `eta=1/16`,

`boxed:
 ||aM-c r^T||_F^2 >7E2/32.
}`                                                                  (6.4)

This is the required actual partner-to-inequality application, not a copied citation. It has two exact geometric forms:

- if `a!=0`,

  `||M-c r^T/a||_F^2 > (1-2eta)E2/(4a^2)`;                      (6.5)

- if `a=0`,

  `||c||_2^2 ||r||_2^2 > (1-2eta)E2/4`.                         (6.6)

At `eta=1/16`, the right side in (6.6) is `7E2/32`.

Equation (6.5) is deliberately called an **algebraic cross-Schur Frobenius packet**. It is not identified with the TRUE full symmetric pair Schur residual: same-side anchor couplings may change that object, exactly as the preserved r21 correction warns. Equation (6.6) is an exact two-star product and does not require any inverse.

A weaker but sometimes useful inverse-free dichotomy follows directly from (6.3): since

`||aM-c r^T||_F <= |a|||M||_F+||c||||r||`,

at least one of

`a^2||M||_F^2 >= (1-2eta)E2/16`,                                (6.7)

`||c||^2||r||^2 >= (1-2eta)E2/16`                               (6.8)

must hold. At `eta=1/16` the threshold is `7E2/128`.

For comparison, partner r25's canonical unconditioned equal-mixture theorem at `q=6/5` pays any mixed-marginal-pass branch by

`||p_Q||infinity <=54.005484724(J3E2)^(-1/10).`                 (6.9)

On the live D' failure branch (5.3), this becomes

`||p_Q||infinity <60.276774(Z3E2)^(-1/10).`                     (6.10)

The conditioned-disjoint theorem (5.6) is substantially sharper whenever its disjointness probability is at least `1/16`; the partner compiler supplies a different structural exit when the canonical mixed gate fails.

The partner r24 physical-square receiver can also pay a genuine subbranch. Its source is

`yspennstate/math-open-problems@10637245c15bc79333cd70bd6f30d417da6874cc`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T080037Z-fleet03-B02-qform-auto11-r24/REPORT.md`.

If the partner r25 failure is of its double-incident H3 type, then some physical heavy row carries more than `J3/5` of complete incident third volume. If that row has physical diagonal `d!=0`, r24 gives

`||p_Q||infinity
 <26.334047*5^(1/8)|d|^(-1/2)||b||^(1/4)J3^(-1/8).`             (6.11)

Using (5.3),

`boxed:
 ||p_Q||infinity
 <36.942732 |d|^(-1/2)||b||^(1/4)Z3^(-1/8).
}`                                                                  (6.12)

This pays a nonnull physical-square subbranch without selecting a tiny minor. It does not pay a small or zero heavy diagonal uniformly; that remains a near-null issue.

## 7. Why this is source-valid

The proof never invokes the false law-uniform pointwise bound `|E exp(itX^2)|<=C|t|^-1/2`. The only scalar Fourier input is the integrated sharp Hausdorff--Young inequality (3.17). It never diagonalizes the random inputs, never declares rotated coordinates independent, never bounds an arbitrary conditional density by one, and never removes a small quadratic matrix perturbation from the random form.

The actual cross block is retained all the way through Weyl differencing and the Gaussian determinant. Every structural statement in Sections 4--6 is an identity/inequality among physical original-coordinate minors. The only Schur expression used without a full symmetric completion is explicitly labeled algebraic cross-Schur and is not fed to a theorem requiring a true pair Schur residual.

The newest-source counterexample search reports no counterexample to the owner target. This run likewise found no source-valid target counterexample to the stronger target-wide statement `integral |phi_Q|<infinity`; therefore that stronger criterion remains open rather than refuted.

## 8. First unpaid implication

The first unpaid implication is now

`QFORM-COMMON-ANCHOR-E2-SCHURSTAR-RECEIVER-v1`.

In the remaining two-sided D' / weak-D5 collar, after the present cross-disjoint `L1_t` exit fails, one has a fixed physical residual row/column anchor satisfying the quantitative lower bound (6.3), and at `eta=1/16` the clean packet (6.4). The next valid mechanism must pay either

1. the exact two-star branch `a=0`, or
2. the nonzero-edge algebraic cross-Schur Frobenius branch,

while retaining arbitrary same-bank curvature, extra spectrum and original-coordinate product provenance. A valid receiver may be a genuine mixed-hub/graph-BL estimate, a TRUE scalar/pair Schur theorem after separately verifying its hypotheses, or another physical cross block with D'/D5/volume currency. It may **not** simply identify `M-cr^T/a` with the true full-pair Schur residual, nor invert a tiny local minor before aggregating.

The full QFORM conjecture remains OPEN.

## 9. Review status

The q-dependent sharp-HY scalar calculation used in (1.1) and the endpoint conventions used here were independently checked in this run for the analytic scope: `PASS_ANALYTIC_CONSTANTS_FOR_USED_SCOPE`. This is not an independent review of every matrix/tail implication in the volume-stability package, and it is not an end-to-end review of the full conjecture. The new theorem in Sections 3--6 is a new supporting argument and remains available for peer review.
