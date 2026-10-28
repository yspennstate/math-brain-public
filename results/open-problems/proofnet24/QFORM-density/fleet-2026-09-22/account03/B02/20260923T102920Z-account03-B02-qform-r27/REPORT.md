SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T10:29:20Z.
attacking: the literal-residual-minor concentrated endpoint by conditioning the incident determinant law away from that physical 2x2 support; either this restores the q=1 mixed-volume L1 Fourier estimate or it forces a quantitative double-anchor third-volume packet.

# account03/B02 r27 — literal-minor avoidance compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Fresh owner control:** revision `2026-09-22.15`, QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full QFORM target:** OPEN  
**Target-wide universal unweighted Fourier L1 criterion:** OPEN; neither proved nor refuted here  
**Continuity:** proved on the new Fourier branch because the full characteristic function is genuinely in `L1`; not claimed on the structural residue.

## 1. Exact scope and source pins

The target remains: independent ORIGINAL real coordinates with scalar densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moments, Gaussianity, log-concavity, bounded/connected support, post-rotation independence, or deletion of small coefficients is used.


The analytic input is this slot's completed arbitrary-law mixed-volume theorem from r26:

- `QFORM-WEIGHTED-MIXED32-ARBITRARY-LAWS-v1`,
- `yspennstate/math-open-problems@774fcefa1d081d578a005e8eb8b6670c9ed34e99`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T100130Z-account03-B02-qform-auto11-r26/REPORT.md`.

At `theta=1/2,q=1`, if the mixed row or mixed column inclusion marginals of an incident-third-minor law `mu3` and a residual-second-minor law `mu2` are all at most `1/2`, it proves

`||p_Q||_infinity <= C0 [G(mu3)G(mu2)]^(-1/10),`

`C0=5e/2^(1/5)=11.832008884813...`,                              (1.1)

and, before inversion,

`|phi_Q(t)| <= min{1,
 2^(-1/4)e^(5/4)pi^(5/4)
 [G(mu3)G(mu2)]^(-1/8)|t|^(-5/4)}.`                             (1.2)

Here `G(mu)=exp(H(mu)+E_mu log(det^2))`. The proof is product-preserving Weyl differencing + sharp Hausdorff--Young + Brascamp--Lieb; it tolerates arbitrary same-bank quadratic terms, affine terms, outside couplings and extra spectrum.

The fresh complementary structural source is account02/B02:

- `QFORM-INCIDENT32-DISJOINT-TRANSPORT-L1-v1`,
- `yspennstate/math-open-problems@0029401037d9e0bb0f18c030c959bbc5afd57d52`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260923T100819Z-account02-B02-qform-r11/REPORT.md`.

Its concentrated/concentrated endpoint supplies one literal residual `2x2` minor carrying a definite fraction of residual `E2`; Section 5 below applies the new theorem to that exact inequality.

The designated completed partner is account04/B02:

- `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`,
- `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

Its genuine `L2` Fourier estimate is applied at an equation in Section 6.

## 2. Physical setup

Let `I,J` be disjoint banks of ORIGINAL coordinates and let

`B=A[I,J]`.

Fix an actual outer anchor row `x in I` and outer anchor column `y in J`. Put

`N=B[I\{x},J\{y}]`.

For residual row pairs `R` and column pairs `C`, define the incident third-volume

`J3 = sum_(|R|=|C|=2) det B[{x} union R,{y} union C]^2 >0`.       (2.1)

Let `nu3` be the canonical incident determinant law

`nu3(R,C)=det B[{x} union R,{y} union C]^2/J3`.                  (2.2)

Now fix one literal nonzero residual physical minor

`m0=det N[R0,C0]`,

where `|R0|=|C0|=2`, and write

`h=m0^2>0`.                                                       (2.3)

Define the incident avoidance probabilities

`delta_r = P_nu3(R cap R0=empty)`,
`delta_c = P_nu3(C cap C0=empty)`,
`delta=max(delta_r,delta_c)`.                                    (2.4)

These are determinant-weighted probabilities on ORIGINAL physical supports. No spectral-coordinate independence is being asserted.

## 3. Main new theorem — `QFORM-LITERAL2-AVOIDANCE-OR-DOUBLEANCHOR-v1`

### Theorem 3.1

In the setup above, if `delta>0`, the full ambient quadratic form has an `L1` characteristic function and hence a bounded continuous density vanishing at infinity, with

`boxed:
 ||p_Q||_infinity
 <= C0 (delta J3 h)^(-1/10),
 C0=5e/2^(1/5).
}`                                                                  (3.1)

More generally, for every `0<eta<1/2`, either

`boxed:
 ||p_Q||_infinity
 <= C0 eta^(-1/10)(J3h)^(-1/10)
}`                                                                  (3.2)

with a continuous density, or there are an actual row `r in R0` and column `c in C0` for which the double-anchor incident third-volume satisfies

`boxed:
 G3^(x,r;y,c)(B)
 >= [(1-2eta)/4] J3.
}`                                                                  (3.3)

At the clean value `eta=1/4`, either

`boxed:
 ||p_Q||_infinity
 <=13.591409143 (J3h)^(-1/10),
}`                                                                  (3.4)

or

`boxed:
 G3^(x,r;y,c)(B) >= J3/8.
}`                                                                  (3.5)

Here `G3^(x,r;y,c)(B)` is the sum of squared physical `3x3` minors containing both row anchors `x,r` and both column anchors `y,c`.

### Proof of the Fourier branch

Assume first `delta_r>0`. Condition the canonical law `nu3` on the row-avoidance event

`E_r={R cap R0=empty}`

and call the resulting law `mu3`. Because `nu3` is canonical squared-determinant weight, conditioning simply restricts its partition function from `J3` to `delta_r J3`. Therefore

`G(mu3)=delta_r J3`.                                             (3.6)

Let `mu2` be the point mass on the single literal minor `(R0,C0)`. Its entropy is zero and its determinant weight is `h`, so

`G(mu2)=h`.                                                       (3.7)

Use the r26 arbitrary-law mixed theorem with `theta=1/2,q=1`. On the ROW side the mixed inclusion marginals are all at most `1/2`:

- the outer anchor `x` appears in every incident 3-minor and in no residual 2-minor, so its mixed marginal is exactly `1/2`;
- every row of `R0` appears with probability zero under `mu3` and one under `mu2`, so its mixed marginal is exactly `1/2`;
- every other residual row appears with probability at most one under `mu3` and zero under `mu2`, hence has mixed marginal at most `1/2`.

Thus the exact `q=1` gate holds without any reciprocal selected-minor payment. Substituting (3.6)-(3.7) into (1.1) proves

`||p_Q||_infinity <=C0(delta_r J3h)^(-1/10)`.                    (3.8)

The source theorem simultaneously gives the high-frequency tail

`|phi_Q(t)|
 <=min{1,K_r|t|^(-5/4)},`

`K_r=2^(-1/4)e^(5/4)pi^(5/4)(delta_r J3h)^(-1/8)`.              (3.9)

Hence `phi_Q in L1`, proving continuity and vanishing at infinity. The column proof is identical after transposition. Taking the larger of `delta_r,delta_c` gives (3.1). QED for the Fourier branch.

### Proof of the structural complement

Fix `0<eta<1/2` and suppose neither avoidance probability reaches `eta`:

`delta_r<eta`, `delta_c<eta`.                                    (3.10)

Under `nu3`,

`P(R cap R0 !=empty)>1-eta`,
`P(C cap C0 !=empty)>1-eta`.                                    (3.11)

By inclusion--exclusion,

`P(R cap R0 !=empty and C cap C0 !=empty)>1-2eta`.              (3.12)

For every support pair in the event (3.12), at least one of the four events

`E_(r,c)={r in R and c in C}`,  `r in R0, c in C0`              (3.13)

occurs. Therefore

`sum_(r in R0,c in C0) P(E_(r,c)) >=1-2eta`.                    (3.14)

One pair `(r,c)` has probability at least `(1-2eta)/4`. Multiplying by the total determinant weight `J3` gives exactly (3.3). For `eta=1/4`, this is `J3/8`. If instead one avoidance probability is at least `eta`, (3.2) follows from (3.1). QED.

### Why this is not the refuted cross-minor shortcut

The literal minor `h` is never by itself called a TRUE symmetric Schur certificate. It is used only as one determinant atom in the already-proved mixed Fourier inequality. If that Fourier payment cannot be made at a fixed avoidance scale, the conclusion is not a density claim from `h`; it is the separate aggregate double-anchor certificate (3.3). This respects `QFORM-CROSSMINOR-ALONE-FALSE` and the later cross-Schur/TRUE-Schur corrections.

## 4. Exact double-anchor algebra on the residue

For the pair `(r,c)` supplied by (3.3), move physical rows `(x,r)` and columns `(y,c)` first and write the physical cross block as

`B=[[P,R],[C,M]]`,                                                (4.1)

where `P` is `2x2`. The completed anchored-compound identity gives

`G3^(x,r;y,c)(B)
 = ||det(P)M-C adj(P)R||_F^2`.                                  (4.2)

Thus the `eta=1/4` residue obeys

`||det(P)M-C adj(P)R||_F^2 >=J3/8`.                             (4.3)

If `det(P)!=0`, then

`|det(P)| ||M-CP^(-1)R||_F >=sqrt(J3/8)`.                       (4.4)

If `det(P)=0`, positivity of (4.3) excludes `rank(P)=0`; hence `rank(P)=1`. Factor `adj(P)=uv^T`. Then

`||Cu||_2 ||R^T v||_2 >=sqrt(J3/8)`.                            (4.5)

This is an inverse-free two-star packet. Equations (4.4)-(4.5) are structural currency only; further nonlinear smoothing is still needed unless another completed receiver applies.

## 5. Application to the fresh account02/B02 concentrated/concentrated endpoint

The fresh account02/B02 run gives, on its concentrated/concentrated survivor, an actual literal residual minor satisfying

`h > 3H/16 >21 E2/512`,                                         (5.1)

and the outer incident volume satisfies

`J3 > Z3/3`.                                                      (5.2)

Apply Theorem 3.1 with `eta=1/4`.

If the avoidance exit occurs, then

`||p_Q||_infinity
 < C0 4^(1/10)
   [(Z3/3)(21E2/512)]^(-1/10)`

`boxed:
 ||p_Q||_infinity
 <20.877654 (Z3 E2)^(-1/10).
}`                                                                  (5.3)

The density is continuous on this exit.

If the avoidance exit fails on both physical sides, then (3.5) and (5.2) give

`boxed:
 G3^(x,r;y,c)(B) > Z3/24.
}`                                                                  (5.4)

Consequently the former concentrated/concentrated endpoint is no longer a separate literal-minor obstruction: it is either paid by an unweighted `L1_t` Fourier estimate or reduced to the already-recognized double-anchor cross-Schur/two-star packet, now with an explicit `Z3/24` scale.

This application is strictly aggregate-before-inversion. No claim is made that the literal minor in (5.1) itself is a good physical principal pair.

## 6. Designated account04/B02 result applied to an actual inequality

Assume additionally that the full form contains a nonsingular physical `3x3` principal block `H0` with an exact zero diagonal. The designated account04/B02 theorem gives the genuine Fourier estimate

`L:=int_R |phi_Q(t)|^2 dt
 <=6 pi 2^(2/3)|det H0|^(-1/3).`                                (6.1)

On the avoidance branch, (3.9) gives `|phi_Q(t)|<=K|t|^(-5/4)` with

`K=2^(-1/4)e^(5/4)pi^(5/4)(delta J3h)^(-1/8)`.                  (6.2)

For every `T>0`, Cauchy--Schwarz on `[-T,T]` and direct integration of the tail give

`||phi_Q||_1 <=sqrt(2LT)+8KT^(-1/4)`.                           (6.3)

Optimizing exactly, as in r26, yields

`||p_Q||_infinity
 <=12.662408124 |det H0|^(-1/18)
   (delta J3h)^(-1/12).`                                        (6.4)

Thus when `delta>=1/4`,

`boxed:
 ||p_Q||_infinity
 <=14.213073 |det H0|^(-1/18)(J3h)^(-1/12).
}`                                                                  (6.5)

On the live account02 endpoint (5.1)-(5.2), this becomes

`boxed:
 ||p_Q||_infinity
 <20.325238 |det H0|^(-1/18)(Z3E2)^(-1/12).
}`                                                                  (6.6)

This is an equation-level use of the designated partner result, not a citation-only mention. The overlap has a continuous density because the avoidance theorem already proves `phi_Q in L1`.

## 7. Deterministic checks

The exact constants are recorded in `CHECKS.txt` beside this report. A finite seeded support-law regression also checked the purely combinatorial implication behind (3.3): for 5000 strongly concentrated random laws on row/column 2-support pairs, every sample with both avoidance probabilities below `1/4` had a row/column anchor pair of joint inclusion mass above `1/8`; zero violations were observed. This is only a regression check. The proof is (3.10)-(3.14).

## 8. What remains open

The full QFORM conjecture remains **OPEN**. This report does not prove that the bare three-large-eigenvalue hypothesis forces a literal residual minor at a universal scale; it consumes the literal-minor endpoint produced by the fresh transport-failure decomposition. Nor does it prove or refute the target-wide universal bound on `int |phi_Q|`.

The precise B02 residue is smaller: the account02 four-way transport-failure collar has lost its concentrated/concentrated branch as an independent case. What remains is the double-anchor Schur/two-star packet (including the new `Z3/24` instance) and the two one-sided anchor/strip hybrids. The next useful mechanism is a product-preserving grouped-hub/fractional-Fourier receiver for those packets, with the fresh account03/B09 grouped-hub theorem as a compatible source whenever its opposite-bank curvature hypotheses can be verified.

No schedule, task identity, cadence, enablement, notification, email/Drive, public-release, paid-model/API or cross-account state is changed by this report.
