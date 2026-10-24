SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T08:03:33Z.
attacking: QFORM-RANK2-CROSS-NEAR-COLOOP-STABILITY-v1 — preserve the rank-two cross determinant through an exact original-coordinate repartition, then classify failure of disjoint Pluecker mass into a physical star or a three-row triangle.

# account03/B19 r28 — disjoint-basis repartition and star/triangle near-coloop compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / quantitative inequalities and rigorous computations  
**Fresh owner control:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW TARGET-LEVEL BRANCH + STRUCTURAL COMPILER / FULL QFORM OPEN`.

The unrestricted conjecture remains OPEN. The result below advances the exact-rank-three rank-two-cross near-coloop branch left by account03/B19 r27. It uses only deterministic spectral algebra and repartitions of ORIGINAL independent coordinates. It does not delete a small matrix coefficient, assume moments/support/log-concavity, use independence after rotation, invoke arbitrary-joint coarea, take a worst conditional-density supremum, or use law-uniform pointwise oscillatory decay.

## 1. Source-pinned incoming state

The previous B19 report is

`yspennstate/math-open-problems@a2c543d935168ec8996535219d8c0c25ae261763`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T062711Z-account03-B19-QFORM-r27/REPORT.md`.

Its exact-rank-three setup is

`A=RMR^T`, `R^TR=I_3`,                                           (1.1)

where `M=M^T` is invertible and `s_min(M)>=1`. Split the ORIGINAL coordinates into `I union J`, put

`P=R_I`, `S=R_J`, `G=P^TP`, `H=S^TS=I-G`,                      (1.2)

and assume

`rank(P)=3`, `rank(C)=2`, `C=A[I,J]=PMS^T`.                     (1.3)

Then `rank(S)=2`. Let `u` span `ker H` and `W=u^perp`. On `W`, `H` is positive definite. If

`rho=s1(C)s2(C)`,                                                (1.4)

r27 proved the exact identity

`rho^2 = det(H|_W) det((MGM)|_W)`                               (1.5)

and, equivalently, its frame-defect formula. The live aggregate branch has

`rho >= rho0 := sqrt(29/3072) = 0.097160198469675...`.          (1.6)

The analytic receiver is account01/B19,

`yspennstate/math-open-problems@d72be34399b8d0325c715973e7af3a37df7ce227`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T060843Z-account01-B19-QFORM-auto11/REPORT.md`.

In its stated original-product scope, for an exact rank-two cross block of singular product `rho'`, a three-dimensional source space containing the source self range, and transverse source-row norm `R'>0`, it gives a continuous density with

`||p_Q||_infinity <= C_* (R')^(-1/4) (rho')^(-3/8)`,            (1.7)

where

`C_* = 2^(15/4) 3^(-3/8) = 8.911319467...`.                    (1.8)

The newest partner-side structural input is account02/B19,

`yspennstate/math-open-problems@333dd6db61c9d18e88f9b8be5bae55c811d49b42`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T071320Z-account02-B19-QFORM/REPORT.md`.

It normalizes the two-dimensional `J` frame and proves a repartition under a condition-number/leverage gate. The present run removes that condition-number gate by preserving the **original cross singular-product currency itself** through the repartition.

The designated account04/B19 endpoint theorem is

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.

Its exact-null-coloop residual-diffuse estimate is used at an actual inequality in Section 7, but it is not promoted to a near-coloop theorem.

## 2. Normalize the rank-two physical bank and define the missing invariant

Every physical spectral row `s_j` of `S`, `j in J`, lies in `W`. Define the normalized rows

`v_j=(H|_W)^(-1/2)s_j in W`.                                     (2.1)

Then

`sum_(j in J) v_j v_j^T = I_W`.                                 (2.2)

Thus `(v_j)` is a two-dimensional Parseval frame. For every unordered pair `T={i,k}` put

`d_T=det(v_i,v_k)^2`.                                            (2.3)

Cauchy--Binet gives

`sum_T d_T=1`.                                                    (2.4)

The numbers `d_T` are therefore a probability law on physical two-element bases. Define its ordered disjoint-basis mass

`delta := sum_(T cap U = empty) d_T d_U`.                        (2.5)

Equivalently, if `T,U` are iid from the basis law `(d_T)`, then `delta=P(T cap U=empty)`.

Also define the normalized physical-row leverage

`ell_j=||v_j||^2`.                                                (2.6)

The exact marginal identity is

`sum_(T: j in T)d_T=ell_j`,                                      (2.7)

because

`sum_k det(v_j,v_k)^2
 =||v_j||^2 tr(I_W)-v_j^T I_W v_j
 =ell_j`.                                                        (2.8)

In particular `sum_j ell_j=2`.

The key point is that `delta` does not deteriorate when `H|_W` is ill-conditioned. It records combinatorial/product provenance after the only deterministic whitening needed to identify the rank-two frame.

## 3. Main theorem: disjoint-basis mass pays the near-coloop branch without a condition-number gate

### Theorem 3.1 — `QFORM-RANK2-CROSS-DISJOINT-BASIS-REPARTITION-v1`

Under (1.1)--(1.6), assume `delta>0`. Put

`eta=delta/16`.                                                   (3.1)

Then there is a subset `K subset J` such that, after the exact ORIGINAL-coordinate repartition

`I'=I union K`, `J'=J\K`,                                       (3.2)

writing

`H'=R_(J')^T R_(J')`, `G'=R_(I')^T R_(I')=I-H'`,                (3.3)

and `C'=A[I',J']`, one has

`G' >= eta I_3`,                                                 (3.4)

`rank(C')=2`,                                                     (3.5)

`rho':=s1(C')s2(C') >= eta rho`,                                (3.6)

and the source self block `B'=A[I',I']` obeys

`s_min^+(B')>=eta`.                                              (3.7)

Consequently the full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= C_* eta^(-5/8) rho^(-3/8)
 = C_* (delta/16)^(-5/8) rho^(-3/8).
`                                                                    (3.8)

In particular, throughout the live compound-energy branch (1.6),

`delta>=1/64  =>  ||p_Q||_infinity <1626`.                       (3.9)

No lower bound on `lambda_min(H|_W)` and no individual normalized-leverage upper bound is required.

### Proof

Color every index of `J` independently into `K` with probability `1/2`. Put

`V_K=sum_(j in K)v_jv_j^T`, `V_(K^c)=I_W-V_K`.                  (3.10)

By two-dimensional Cauchy--Binet,

`det V_K=sum_(T subset K, |T|=2)d_T`,
`det V_(K^c)=sum_(U subset K^c, |U|=2)d_U`.                     (3.11)

A pair `T` can lie in `K` while `U` lies in `K^c` exactly when `T cap U=empty`, and then the probability is `2^(-4)=1/16`. Therefore

`E[det V_K det V_(K^c)] = delta/16 = eta`.                      (3.12)

Hence one deterministic `K` satisfies

`det V_K det V_(K^c)>=eta`.                                     (3.13)

Both matrices in (3.13) are positive-semidefinite contractions, so each determinant is at most one; therefore each determinant is at least `eta`. In dimension two, for a positive-semidefinite contraction `T`,

`lambda_min(T)=det(T)/lambda_max(T)>=det(T)`.                    (3.14)

Thus

`eta I_W <= V_K,V_(K^c) <=(1-eta)I_W`.                          (3.15)

Let

`H_K=sum_(j in K)s_js_j^T`, `H_(K^c)=sum_(j in K^c)s_js_j^T`.   (3.16)

Undoing the normalization (2.1), (3.15) gives on `W`

`eta H <= H_K,H_(K^c) <=(1-eta)H`.                              (3.17)

Take `H'=H_(K^c)`. Since `H'u=0`, while on `W`

`H' <=(1-eta)H <=(1-eta)I`,                                    (3.18)

we get

`G'=I-H' >=eta I_3`,                                            (3.19)

proving (3.4). Also `H'` is positive definite on `W`, hence has rank two. Since `P'=R_(I')` has rank three by (3.19) and `M` is invertible,

`C'=P'M(R_(J'))^T`                                               (3.20)

has exact rank two, proving (3.5).

The crucial point is (3.6). Apply the exact determinant identity (1.5) to the new partition:

`(rho')^2 = det(H'|_W) det((MG'M)|_W).`                          (3.21)

From `H'>=eta H` on the two-dimensional space `W`,

`det(H'|_W)>=eta^2 det(H|_W)`.                                  (3.22)

Moreover

`G'-G=H_K >=0`.                                                  (3.23)

Therefore

`MG'M-MGM=M(G'-G)M >=0`.                                       (3.24)

Compression to `W` preserves positive-semidefinite order, and determinant is monotone on positive-definite matrices under this order. Hence

`det((MG'M)|_W)>=det((MGM)|_W)`.                                (3.25)

Combining (3.21), (3.22), (3.25), and the original identity (1.5) yields

`(rho')^2 >=eta^2 rho^2`,                                       (3.26)

which is (3.6). This is the step that removes the former `lambda_min(H|_W)` loss: any amplification supplied by `M` in the thin frame direction is retained rather than replaced by a crude singular-value floor.

For the source self block,

`B'=P'M(P')^T`.                                                   (3.27)

Let `Q'=P'(G')^(-1/2)`, so `(Q')^TQ'=I_3`. Then on `range(P')`, `B'` is orthogonally represented by

`(G')^(1/2)M(G')^(1/2)`.                                        (3.28)

Thus

`s_min^+(B')
 >=lambda_min(G') s_min(M)
 >=eta`,                                                         (3.29)

proving (3.7). Since `B'` has rank three and `C'` rank two, the unit source direction `r'` transverse to `range(C')` satisfies

`R':=||B'r'||>=eta`.                                             (3.30)

Now (1.7), (3.6), and (3.30) give

`||p_Q||_infinity
 <=C_* eta^(-1/4)(eta rho)^(-3/8)
 =C_* eta^(-5/8)rho^(-3/8)`.                                    (3.31)

The receiver supplies continuity and vanishing at infinity. Finally, if `delta>=1/64`, then `eta>=1/1024`, and with (1.6)

`C_* (1/1024)^(-5/8) rho0^(-3/8)
 =1625.81579568156...<1626`.                                    (3.32)

QED.

## 4. What failure of disjoint-basis mass actually means

Theorem 3.1 pays `delta>=1/64`. We now classify `delta<1/64` without extracting a single reciprocal minor.

### Lemma 4.1 — `QFORM-PLUCKER-NONDISJOINT-STAR-TRIANGLE-v1`

Let `(d_T)` be any probability law on two-element subsets of a finite set, and let

`delta=P(T cap U=empty)`                                        (4.1)

for iid `T,U`. If `delta<1/64`, then at least one of the following holds:

**STAR:** some vertex `i` has degree mass

`ell_i=sum_(T: i in T)d_T >47/64`;                              (4.2)

**TRIANGLE:** some three vertices `S={i,j,k}` have internal edge mass

`sum_(T subset S)d_T >377/448`.                                 (4.3)

The constants are absolute and no geometry is assumed.

### Proof

For an edge `e`, let

`q_e=sum_(U: U cap e=empty)d_U`.                                (4.4)

Since `sum_e d_e q_e=delta`, choose an edge, relabelled `{1,2}`, with

`q_{12}<=delta`.                                                 (4.5)

Write

`c=d_{12}`,
`A_x=d_{1x}`, `A=sum_(x>=3)A_x`,
`B_x=d_{2x}`, `B=sum_(x>=3)B_x`,
`O=sum_(T: T cap {1,2}=empty)d_T`.                              (4.6)

Then `O=q_{12}<=delta` and

`c+A+B=1-O>=1-delta`.                                           (4.7)

If `min(A,B)<=1/4`, say `B<=1/4`, then the degree at vertex one is

`ell_1=c+A>=1-delta-B>1-1/64-1/4=47/64`,                       (4.8)

so STAR holds.

Assume therefore `A,B>1/4`. The ordered disjoint-pair probability contains both the `A_x`-then-`B_y` and `B_y`-then-`A_x` contributions for `x!=y`. Hence, with

`D=sum_(x!=y)A_xB_y`,                                           (4.9)

we have

`2D<=delta`, so `D<=1/128`.                                     (4.10)

Normalize `a_x=A_x/A`, `b_x=B_x/B`. Since `AB>1/16`,

`1-sum_x a_xb_x = D/(AB) <1/8`;                                (4.11)

therefore

`sum_x a_xb_x >7/8`.                                            (4.12)

Choose `x0` maximizing `a_x`. Then `a_(x0)>7/8`. Also

`sum_x a_xb_x
 <=a_(x0)b_(x0)+(1-a_(x0))
 =1-a_(x0)(1-b_(x0))`.                                         (4.13)

Together with (4.12), this gives

`b_(x0)>6/7`.                                                    (4.14)

Therefore the triangle `S={1,2,x0}` has mass

`c+A_(x0)+B_(x0)
 >c+(7/8)A+(6/7)B
 >=c+A+B-(A+B)/7
 >=1-delta-1/7
 >1-1/64-1/7
 =377/448`.                                                      (4.15)

Thus TRIANGLE holds. QED.

This is the exact weighted analogue of the elementary graph fact that a graph with matching number one is a star or a triangle. It is the correct structural object here because the weights are the complete normalized Pluecker basis masses, not local minors chosen after inversion.

## 5. Apply the star/triangle lemma to the QFORM frame

Return to the normalized physical `J` frame (2.1)--(2.8), and suppose `delta<1/64`.

### 5.1 STAR: one actual physical normalized coloop

If STAR holds, then some actual original coordinate `j` satisfies

`ell_j=||v_j||^2>47/64`.                                        (5.1)

Deleting this one normalized row leaves the two-dimensional frame operator

`I_W-v_jv_j^T`,                                                 (5.2)

whose eigenvalues are exactly

`1` and `1-ell_j<17/64`.                                       (5.3)

Thus the abstract near-rank-drop alternative is replaced by a **single physical normalized near-coloop**. No small coefficient has been discarded. The remaining payment must use the original-product provenance of that physical coordinate together with the retained residual bank.

### 5.2 TRIANGLE: three actual physical rows carry almost all two-volume

If TRIANGLE holds, there is an actual three-coordinate set `S subset J` such that

`q_S:=sum_(T subset S)d_T>q0:=377/448=0.841517857...`.           (5.4)

By Cauchy--Binet,

`det V_S=q_S`, where `V_S=sum_(j in S)v_jv_j^T`.                (5.5)

Because `0<=V_S<=I_W`, its smallest eigenvalue is at least its determinant. Therefore

`V_S>=q_S I_W>q0 I_W`.                                         (5.6)

Undoing the normalization gives

`H_S:=sum_(j in S)s_js_j^T >=q0 H` on W.                        (5.7)

Now repartition with

`J'=S`, `I'=I union (J\S)`,                                    (5.8)

so `H'=H_S` and `G'=I-H'=G+H_(J\S)>=G`.

The same determinant monotonicity as in Section 3 gives

`rho' >=q0 rho`.                                                 (5.9)

#### Paid triangle subbranch

If

`lambda_min(G')>=1/64`,                                        (5.10)

then `s_min^+(B')>=1/64`. The receiver (1.7), (1.6), and (5.9) yield

`||p_Q||_infinity
 <=C_* 64^(1/4)(q0 rho0)^(-3/8)
 =64.4584871233...<65`.                                         (5.11)

This density is continuous. Thus a three-row concentration of the Pluecker mass is itself harmless unless those three rows nearly saturate a global spectral direction.

#### Remaining triangle geometry is an actual globally heavy row

If (5.10) fails, then

`lambda_max(H_S)>63/64`.                                       (5.12)

Choose a unit vector `w` realizing this Rayleigh quotient. Since `S` has three physical rows,

`sum_(j in S)<s_j,w>^2>63/64`,                                 (5.13)

so for at least one actual physical coordinate `j in S`,

`c_j:=||s_j||^2 >=<s_j,w>^2>21/64`.                            (5.14)

If additionally

`|A_jj|>=1/64`,                                                  (5.15)

then the completed exact-rank-three scalar-pivot theorem

`||p_Q||_infinity <=128[c_j |A_jj| |det M|]^(-1/4)`             (5.16)

pays this subbranch by

`||p_Q||_infinity
 <128[(21/64)(1/64)]^(-1/4)
 =478.349289...<479`.                                            (5.17)

No continuity claim is imported from that scalar-pivot source.

If instead `|A_jj|<1/64`, then the target spectral floor implies

`||Ae_j||^2=||M s_j||^2>=||s_j||^2>21/64`.                      (5.18)

Writing `a=A_jj` and `m` for the off-diagonal row of this physical coordinate,

`||m||^2=||Ae_j||^2-a^2
 >21/64-1/4096
 =1343/4096`.                                                    (5.19)

This is a concrete near-zero, high-leverage physical hub, stronger than the earlier collar threshold `1023/4096`. It is not declared paid here because feeding it through a compiler that can return to the present rank-two-cross branch would be circular. Equation (5.19) is instead the precise remaining currency.

## 6. Compact conditional proof assembly after this run

Inside the current exact-rank-three aggregate rank-two-cross route, the correction-safe chain is now:

1. r27 gives `rho>=rho0` and pays balanced frame defect `Theta>=2^-12` continuously by `<96`.
2. In the surviving near-coloop frame, normalize the physical `J` rows by (2.1) and form the complete two-basis law `(d_T)`.
3. If its disjoint mass `delta>=1/64`, Theorem 3.1 above repartitions ORIGINAL coordinates and pays the exact full form continuously by `<1626`, **even when `H|_W` is arbitrarily ill-conditioned**.
4. If `delta<1/64`, Lemma 4.1 leaves only:
   - a single actual normalized physical near-coloop with `ell_j>47/64`; or
   - a three-row triangle carrying `>377/448` of all normalized two-volume.
5. The triangle is paid continuously by `<65` whenever its complementary source Gram has `lambda_min>=1/64`. If that fails, one of the same three actual rows has global spectral leverage `>21/64`; if its physical diagonal has modulus at least `1/64`, it is paid by `<479`. The sole triangle residue is therefore the explicit small-pivot/high-star currency (5.19).

This removes the previous broad alternatives “`lambda_min(H|W)<1/64`” and “a normalized-heavy core of up to 31 rows” from account02/B19: arbitrary thinness of `H` is no obstruction when the normalized two-basis law has fixed disjoint mass, and low disjoint mass collapses to one physical star or one three-row triangle.

The first unpaid exact-rank-three implication is now:

`QFORM-NORMALIZED-PHYSICAL-COLOOP-OR-SMALLPIVOT-TRIANGLE-v1`:

> Pay, without coefficient deletion, either (A) one original coordinate in the rank-two receiver bank whose normalized-frame leverage exceeds `47/64`, or (B) the three-row triangle endpoint in which one of those rows has global leverage above `21/64`, physical diagonal below `1/64`, and off-diagonal star energy above `1343/4096`.

The full theorem still has the separate arbitrary-extra-spectrum descent debt. None of the exact-rank-three progress in this report is silently promoted to that higher-rank setting.

## 7. Designated partner application at an actual inequality

The designated account04/B19 theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` gives, in its proved residual-diffuse **exact-null-coloop** normal form,

`||p_Q||_infinity <34 sqrt(log(e/D_res))`                       (7.1)

for `0<D_res<=1`, with continuous density. Hence on the concrete endpoint range

`e^(-8)<=D_res<=1`,                                              (7.2)

one has

`log(e/D_res)<=9`, so

`boxed: ||p_Q||_infinity<102.`                                  (7.3)

Its source separately gives bounded exact endpoints at `D_res=0` and `D_res>=1`. This is retained as an actual paid endpoint in the assembly, but (7.1) is **not** used as a stability theorem for the STAR alternative (5.1); proving precisely that product-safe stability remains part of the unpaid work.

## 8. Signs, degeneracies, and scope audit

- `M` may have any signature and repeated eigenvalues. Only `s_min(M)>=1` and invertibility are used; all determinants enter by absolute singular-product identities.
- `H|_W` may be arbitrarily ill-conditioned. Theorem 3.1 deliberately avoids `lambda_min(H)`.
- `delta=0` is not divided by. It falls directly under Lemma 4.1 and yields the exact weighted star/triangle endpoint.
- No singular vector of a random vector is treated as an independent coordinate. The only rotations are deterministic two- or three-dimensional coefficient-space calculations.
- All probabilistic bank changes are literal partitions of the original independent coordinates.
- No small coefficient or small matrix is discarded; every repartition is exact.
- The new paid branches prove continuous density because they invoke the account01/B19 integrated-Fourier receiver. The scalar-pivot triangle subbranch (5.17) is recorded only as essential boundedness. Full-target continuity remains OPEN.
- Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 9. Finite verification

A separate saved check file records the exact constants and randomized algebraic regressions. The random checks are not proof. The proof is the determinant-order and weighted-edge argument above.

Key exact numerical values are

`rho0 = 0.09716019846967515`,
`C_* = 8.911319467025024`,
`delta>=1/64 branch = 1625.815795681563`,
`q0=377/448 = 0.8415178571428572`,
`triangle receiver branch = 64.45848712332457`,
`heavy-row scalar-pivot branch = 478.3492891936769`.

The regression terminates conceptually with `QFORM_B19_R28_DISJOINT_BASIS_CHECK_PASS`.
