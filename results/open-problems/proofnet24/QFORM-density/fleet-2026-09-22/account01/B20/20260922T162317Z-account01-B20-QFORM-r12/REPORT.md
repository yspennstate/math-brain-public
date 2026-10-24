# account01/B20 — Schur third-singular collar and anchored rank-two bank

**Run:** `20260922T162317Z-account01-B20-QFORM-r12`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Proof closure and keeper  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The sole target is the full arbitrary-dimensional statement: for independent real `X_i` with probability densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. Continuity is tracked separately.

No Gaussian, moment, iid, compact-support, log-concavity, post-rotation independence, or law-uniform pointwise quadratic oscillatory-decay assumption is used. In particular the fresh correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` is respected: a heavy row plus a same-bank quadratic contaminant is not treated as a paid density branch.

## 2. Source-pinned dependencies actually used

1. **Named partner required by the assignment:** account02/B20 run `20260922T155719Z-account02-B20-QFORM-r12`, canonical mathematics `yspennstate/math-open-problems@527fb9dfef73a5218883c057db14a491992a30d9`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260922T155719Z-account02-B20-QFORM-r12/REPORT.md`. In the diagonal-dominated heavy-pivot branch it supplies, for
   
   `A=[[a,b^T],[b,C]]`, `S=C-bb^T/a`, `tau=(1+||b||/|a|)^(-2)`,
   
   the inequalities
   
   `|a|>=tau>=1/4`, `s_2(S)>=tau`,
   
   and, for `P_tau=1_{|S|>=tau/64}`, the localization
   
   `max_j (P_tau)_{jj}>1/32`.
   
   The same report records the dependence-safe square estimate used below.
2. account01/B20 preceding run `yspennstate/math-open-problems@42db8aea74161970fec7b53664e087875026c6cf`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B20/20260922T152039Z-account01-B20-QFORM-r11/REPORT.md`, which first excluded the diffuse Schur-window branch.
3. `QFORM-REGULARIZED-DETERMINANT-v1`, `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`, path `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`. For an original-coordinate cross block `B`, if one side's range projection has maximum coordinate leverage at most `1/2`, then with `c=2/(pi^2 e^2)`,
   
   `|phi(t)| <= det(I+c t^2 BB^T)^(-1/4)`.
4. account01/B03 `QFORM-RANK2-FRACTIONAL-TRACE-v1`, canonical report under `yspennstate/math-open-problems@4dc15077ae03c87d09ca46370af1d8cea76440b5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/account01-B03-20260922T141917Z/REPORT.md`, for the Abel/Riesz bridge
   
   `sup_z E|z-R|^(-1/2) <= (2pi)^(-1/2) int |phi_R(t)| |t|^(-1/2) dt`.
5. account01/B11 `QFORM-BINARY-INDEFINITE-L3-v1`, canonical report under `yspennstate/math-open-problems@1bc95193312b70572b2765529ac3b6d98e3fe754`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`, used only for the final `L^3` certificate in the opposite-sign physical-pair subbranch.

The full conjecture is still OPEN in the live claims state.

## 3. Conditional end-to-end route and first unpaid implication

Fix the candidate universal cap

`C_* = 32768 sqrt(2)`.

Assume for contradiction that there is a counterexample to this cap and choose one of minimum dimension. In the partner's heavy diagonal-dominated physical-pivot branch, the first unpaid implication was to turn the second Schur localization into a quantitative, source-realizable smoothing packet without discarding arbitrary extra spectrum.

The new argument proves four things:

1. the Schur complement cannot have a third singular value as large as `tau/128`;
2. therefore its `tau/64` spectral window is **exactly rank two**, and the partner's leverage localization amplifies from a row of size `tau/512` to a row of size `>tau/9` in a physical coordinate;
3. if that strong second row is diagonal-dominated, the same-sign case is already impossible by a two-coordinate definite coarea estimate, while the opposite-sign case has a uniform determinant-scale `L^3` certificate;
4. independently of diagonal versus cross dominance, the exact-rank-two Schur window produces an **anchored physical two-minor bank** of dimension-free mass. Its disjoint-overlap branch is fully paid whenever the existing `q=1` range-leverage gate holds, with density bound `<77`.

Thus the residual debt is reduced to the mixed-overlap/high-leverage packets; no small spectral tail is discarded as independent noise.

## 4. New theorem I: the third-Schur-singular collar

### Theorem `QFORM-SCHUR-S3-COLLAR-v1`

In the preceding minimum-dimensional counterexample branch,

`boxed( s_3(S) < tau/128. )`                                      (4.1)

### Proof

Suppose instead that

`s_3(S) >= sigma := tau/128`.

Then `S/sigma` has at least three eigenvalues of modulus at least one. It acts on one fewer original coordinate, so minimum dimensionality gives an essentially bounded density for

`R=Y^T S Y`

with

`||p_R||_infinity <= C_*/sigma`.

Because `p_R` is a probability density,

`||p_R||_3 <= ||p_R||_infinity^(2/3) <= (C_*/sigma)^(2/3)`.

After completing the physical pivot,

`Q=a(X_i+m(Y))^2+R(Y)`.

The dependence-safe square estimate used by the partner gives

`||p_Q||_infinity
 <=4 |a|^(-1/2) ||p_R||_3^(3/4)
 <=4 sqrt(C_*/(|a| sigma)).`                                      (4.2)

For this to exceed `C_*`, it is necessary that

`C_* < 16/(|a|sigma)`.

But the partner's actual inequalities give `|a|>=tau>=1/4`, hence

`16/(|a|sigma)
 <=16/(tau*(tau/128))
 =2048/tau^2
 <=32768
 <32768 sqrt(2)=C_*`,

a contradiction. This proves (4.1). QED.

This is the required direct application of the completed account02/B20 result to an actual target inequality: both `|a|>=tau` and `tau>=1/4` are quantitatively used in the contradiction.

## 5. New theorem II: exact rank-two Schur window and row amplification

Let

`P=1_{|S|>=tau/64}`, `H=PSP`, `E=S-H`.

By (4.1), `rank(P)<=2`. Since the partner also gives `s_2(S)>=tau`, in fact

`boxed( rank(P)=2 )`,                                             (5.1)

and both eigenvalues of `H` have modulus at least `tau`. Moreover

`||E||_op < tau/64`.                                              (5.2)

The partner's localization supplies a physical coordinate `j` with

`h:=P_jj>1/32`.                                                   (5.3)

Because `H` has exactly two eigenvalues of modulus at least `tau`,

`||H e_j||^2=(H^2)_{jj} >= tau^2 h > tau^2/32`.

Using (5.2),

`||S e_j||
 >= ||H e_j||-||E e_j||
 > tau(1/sqrt(32)-1/64).`                                        (5.4)

Write `d=S_jj` and `c=S_{j,-j}`. Since

`||S e_j||^2=d^2+||c||^2`,

at least one of `|d|,||c||` exceeds `||S e_j||/sqrt(2)`. The exact constant satisfies

`(1/sqrt(32)-1/64)/sqrt(2)
 =1/8-1/(64 sqrt(2))
 >1/9`

(the last inequality is equivalent to `8 sqrt(2)>9`). Therefore

`boxed( max{|S_jj|, ||S_{j,-j}||_2} > tau/9 >=1/36. )`            (5.5)

This improves the preceding `tau/512` physical Schur-row certificate by more than a factor of fifty in the minimum-counterexample branch.

## 6. Consequence for a diagonal-dominated second Schur row

Suppose

`|d|>=||c||`.

Then (5.4) gives

`|d|>tau/9`.                                                       (6.1)

The original physical `2x2` principal block on coordinates `(i,j)` has first pivot `a` and scalar Schur complement exactly `d`; hence its determinant is

`det B_2 = a d`.                                                   (6.2)

### Same-sign case is impossible

If `ad>0`, `B_2` is definite. Condition on every other original coordinate. The remaining two-dimensional quadratic has fixed definite matrix `B_2`; outside variables contribute only linear and constant terms. Translating the two physical coordinates preserves the product density cap `<=1`.

For a definite binary quadratic, the sublevel-set area is `pi t/sqrt(|det B_2|)`, so its pushforward density is bounded by

`pi/sqrt(|det B_2|)`.

Using `|a|>=tau`, (6.1), and `tau>=1/4`,

`||p_Q||_infinity
 <= pi/sqrt(|ad|)
 < pi/sqrt(tau^2/9)
 =3pi/tau
 <=12pi
 < C_*.`                                                         (6.3)

Thus an unresolved minimum counterexample with a diagonal-dominated second Schur row must satisfy

`boxed( a d <0. )`                                                (6.4)

### Opposite-sign case has a uniform `L^3` certificate

When `ad<0`, the same physical binary block is indefinite with discriminant scale

`D=|det B_2|=|ad|>tau^2/9>=1/144`.

Conditioning on all remaining coordinates only adds affine terms. `QFORM-BINARY-INDEFINITE-L3-v1` is uniform in those affine terms, and Minkowski survives the mixture over the outside coordinates. Hence

`boxed( ||p_Q||_3 <= C_bin D^(-1/3) <= C_bin 144^(1/3). )`        (6.5)

This does not by itself prove `L^infinity`; it records the exact regularity still available in the only surviving diagonal-dominated sign branch.

## 7. New theorem III: an anchored physical two-minor bank

The rank-two high window also yields a dimension-free packet that survives the arbitrary low spectral tail.

Write `H=U Lambda U^T` with `U in R^{(n-1)x2}`, `U^TU=I_2`, and `|lambda_1|,|lambda_2|>=tau`. The selected coordinate `j` has row leverage `||u_j||^2=h>1/32`.

For every `k!=j`,

`det((H^2)[{j,k},{j,k}])
 =lambda_1^2 lambda_2^2 det(U_{j,k})^2`.

The rank-two tight-frame identity gives

`sum_k det(U_{j,k})^2=||u_j||^2=h`.                               (7.1)

Because `H` and `E` are spectral pieces of the same symmetric matrix,

`S^2=H^2+E^2 >= H^2`.

Principal compression preserves Loewner order, and determinant is monotone on positive semidefinite `2x2` matrices. Therefore

`det((S^2)[{j,k},{j,k}])
 >=det((H^2)[{j,k},{j,k}]).`

Cauchy--Binet gives

`det((S^2)[R,R])=sum_{|K|=2} det(S[R,K])^2` for every `|R|=2`.

Summing over `R={j,k}` and using (7.1),

`boxed(
 M_j:=sum_{k!=j} sum_{|K|=2} det(S[{j,k},K])^2
 > tau^4/32.
 )`                                                               (7.2)

Thus the partner's localized Schur window produces a full-`S` physical determinant bank without cancellation by the low spectral tail.

There is also an exact lift back to the original matrix. Whenever row and column sets both contain the first pivot `i`, block elimination gives

`det A[{i} union R,{i} union K]=a det S[R,K]`.                    (7.3)

Hence (7.2) is an anchored full-matrix `3x3` mixed-minor bank with squared mass greater than `a^2 tau^4/32 >=tau^6/32`.

## 8. Paying the disjoint-overlap bank under the existing leverage gate

Decompose (7.2) by

`r=|{j,k} cap K| in {0,1,2}`.

At least one class carries mass `>tau^4/96`. Suppose the winning class is the disjoint class `r=0`.

Color each residual physical coordinate independently left/right with probability `1/2`. For a fixed disjoint row pair `{j,k}` and column pair `K`, the event that the row pair is entirely left and the column pair entirely right has probability `1/16`. Therefore some deterministic cut `L,R` satisfies, for the physical cross block

`B=S[L,R]`,

`E_2(B):=sum_{|I|=|J|=2} det(B[I,J])^2
 >= tau^4/1536.`                                                  (8.1)

Assume the existing `q=1` gate holds on at least one side of this cross block:

`max diag P_range(B) <=1/2`

(or the analogous condition for `B^T`). The regularized determinant theorem then gives

`|phi_R(t)| <= det(I+c t^2 BB^T)^(-1/4)`,
`c=2/(pi^2 e^2)`,                                                  (8.2)

for the full residual quadratic `R=Y^T S Y`, including every within-bank phase and every additional small singular direction.

Expanding the determinant in nonnegative elementary symmetric polynomials,

`det(I+c t^2 BB^T)
 >=1+c^2 t^4 E_2(B).`                                             (8.3)

The Abel/Riesz bridge and the beta integral therefore give

`sup_z E|z-R|^(-1/2)
 <= C_FR E_2(B)^(-1/8)`,                                         (8.4)

where

`C_FR=(2pi)^(-1/2) * (1/2) B(1/8,1/8) * c^(-1/4)
     =7.6737592903...`.

Finally the original physical pivot yields, by its translation-uniform square kernel,

`||p_Q||_infinity
 <= |a|^(-1/2) sup_z E|z-R|^(-1/2)`.

Using `|a|>=tau`, (8.1), and `tau>=1/4`,

`||p_Q||_infinity
 <= C_FR tau^(-1/2) (1536/tau^4)^(1/8)
 = C_FR 1536^(1/8) tau^(-1)
 <=4 C_FR 1536^(1/8)
 <76.802.`                                                        (8.5)

Thus this entire branch is incompatible with a `C_*` counterexample.

Equivalently, if the disjoint overlap class wins in an unresolved minimum counterexample, **every cut obtained with the mass guarantee (8.1) must fail the `q=1` gate on both orientations**. That turns the remaining branch into a concrete high-leverage structural problem rather than a generic cross-block problem.

The argument in (8.2)--(8.5) proves essential boundedness only. I do not claim a continuous representative from this square/fractional-trace composition; continuity remains separate.

## 9. Fresh correction check

The same-hour correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` gives the exact counterexample

`U^2+X^2+2UX=(U+X)^2`

for independent uniforms, whose density is unbounded at zero. Nothing above invokes the refuted shortcut. In particular:

- the `s_3` collar uses minimum dimensionality plus the already-proved dependence-safe square theorem;
- the row amplification is purely spectral and physical-coordinate algebra;
- the definite pair is paid directly by two-dimensional coarea;
- the disjoint bank is paid by the full residual characteristic function through a source-valid original-coordinate cross block.

## 10. Status and exact next unpaid implication

**Outcome: `ESSENTIAL_STEP_APPLIED`; full QFORM remains OPEN.**

The first remaining implication after this run is now narrower:

> In the minimum-counterexample heavy-pivot branch, the Schur `tau/64` window is exactly rank two and has a physical row of size `>tau/9`. Its anchored two-minor bank has mass `>tau^4/32`. Pay the `r=1` and `r=2` overlap banks, and the `r=0` high-leverage subcase, by a product-preserving grouped-coordinate mechanism. Do not condition on a rotated aggregate, do not discard the low spectral tail as independent noise, and do not use the refuted one-heavy-row same-square absorption.

A particularly concrete next subtarget is to combine the forced `q=1` leverage failure on both sides of every mass-carrying disjoint cut with the rank-two window's heavy physical row, to produce either a paid physical indefinite/definite pair packet or a mixed-overlap bank with a second shared pivot.

No full-solution, continuity, novelty, or independent-review claim is made.
