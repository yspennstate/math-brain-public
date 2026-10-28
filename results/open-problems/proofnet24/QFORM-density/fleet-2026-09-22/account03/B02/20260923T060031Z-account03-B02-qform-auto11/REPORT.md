SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T06:00:31Z.
attacking: the same-side correction packet from the true-pair Schur repair; convert each correction star plus its transverse packet into a genuine one-sided physical E2 bank, then spend that bank by integrated half-Riesz Fourier smoothing before any reciprocal minor extraction.

# account03/B02 auto11 — one-sided Schur E2 receiver for the same-side correction packet

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Prepublication control refresh:** `yspennstate/math-research-brain@3a7d935988c296199df80dcb731f12ccc1e87029`; revision still `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`  
**Full QFORM target:** OPEN  
**Target-wide unweighted Fourier L1 criterion:** OPEN / neither proved nor refuted here  
**Continuity:** the new receiver proves essential boundedness only; full continuity remains OPEN.

## 1. Exact target and correction boundary

The target remains the unrestricted owner statement: independent real ORIGINAL coordinates with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, Gaussian, iid, compact-support, connected-support, log-concavity, sign, or post-rotation-independence hypothesis is introduced.

The live corrections against law-uniform scalar pointwise quadratic-phase decay, arbitrary-joint coarea, conditional cap substitution for independence, naive fiber suprema, and reciprocal selection of one tiny local minor are all retained. The argument below conditions/completes only ORIGINAL physical coordinates, and every probability-facing cross block remains a block between surviving original independent coordinates.

The immediately preceding B02 result is

`yspennstate/math-open-problems@40bf94187444ad5a6008bcf4b06931689b0e7383`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T053047Z-account03-B02-qform-auto11/REPORT.md`.

It paid the correction-safe TRUE-Schur `E2` branch unconditionally. The remaining r21 branch is the same-side correction resource described next.

## 2. Source algebra inherited from r21

Choose two physical coordinates `x,y`; write

`d=A_xx`, `e=A_yy`, `a=A_xy`,
`P=[[d,a],[a,e]]`, `delta=de-a^2`.

Let `U,V` be disjoint surviving original-coordinate banks and write

`u=A[U,x]`, `c=A[U,y]`,
`r=A[x,V]`, `v=A[y,V]`,
`N=A[U,V]`.

When `delta!=0`, the true cross block after completing the full physical pair is

`T=N-[u,c] P^(-1) [r;v]`.

Define

`xi=a u-d c`, `eta=a v-e r`.

The r21 rank-one repair proved that the cross-only anchored packet either leaves true-Schur second volume or forces

`R_corr := (||xi||^2 ||eta||^2/delta^2) F^2`,

where

`F=||P_(xi^perp) T P_(eta^perp)||_F`.

At the concrete third-volume gate used there,

`max{a^2 E2(T), R_corr}>Z/12`.

The first term is now paid by the preceding B02 run. This run attacks the second term without pretending that the correction vectors are independent random coordinates.

## 3. New exact one-sided Schur identities

### Theorem 3.1 — `QFORM-SAMESIDE-ONE-SQUARE-E2-IDENTITY-v1`

Assume `delta!=0`.

### x-side completion

If `d!=0`, complete only the ORIGINAL coordinate `x`. The quadratic form becomes

`Q=d(X_x+L_x(W))^2+R_x(W)`,

where `W` consists of the other original independent coordinates. In the `x`-Schur residual define

`K_x=N-u r^T/d`,
`w=(d v-a r)/d`.

The surviving physical couplings are

`A^(x)[y,U]=c^T-(a/d)u^T=-xi^T/d`,
`A^(x)[U,V]=K_x`.

Moreover the TRUE two-coordinate Schur block satisfies the exact identity

`boxed: T=K_x+xi w^T/delta.`                                      (3.1)

Hence

`P_(xi^perp) K_x=P_(xi^perp) T`.                                 (3.2)

Now take the actual physical cross cut in `R_x` with row bank `{y} union V` and column bank `U`:

`C_x=[ -xi^T/d ; K_x^T ]`.                                      (3.3)

The complete second-compound mass of this physical block obeys

`boxed:
 E2(C_x)
 >= (||xi||^2/d^2) ||P_(xi^perp)K_x||_F^2
 >= (||xi||^2/d^2) F^2.
}`                                                               (3.4)

#### Proof

Equation (3.1) follows by direct expansion of `P^(-1)`. For (3.4), retain only the `2x2` minors of `C_x` involving its first row. If `k_j` denotes column `j` of `K_x`, Cauchy--Binet / the two-vector Gram determinant gives

`sum_j ||(-xi/d) wedge k_j||^2
 =(||xi||^2/d^2)||P_(xi^perp)K_x||_F^2`.

This is a sub-sum of `E2(C_x)`. Equation (3.2) identifies the projection with `P_(xi^perp)T`; projecting additionally on the right by `P_(eta^perp)` can only decrease Frobenius norm, giving the final inequality. QED.

### y-side completion

Symmetrically, if `e!=0`, put

`K_y=N-c v^T/e`, `z=(e u-a c)/e`.

Then

`boxed: T=K_y+z eta^T/delta`,                                     (3.5)

so `K_y P_(eta^perp)=T P_(eta^perp)`. The actual physical cross block in the `y`-Schur residual, with row bank `{x} union U` and column bank `V`, is

`C_y=[ -eta^T/e ; K_y ]`,                                        (3.6)

and

`boxed:
 E2(C_y)
 >= (||eta||^2/e^2)||K_y P_(eta^perp)||_F^2
 >= (||eta||^2/e^2)F^2.
}`                                                               (3.7)

The point is structural and probability-safe: both correction stars generate genuine aggregate second-compound currency after completing only one ORIGINAL square. No spectral rotation and no selected local `2x2` minor occurs.

## 4. Integrated-Fourier payment of the one-sided packet

The completed account01/B01 theorem `QFORM-PAIRVOLUME-HALF-RIESZ-UNCONDITIONAL-v1` is at

`yspennstate/math-open-problems@1f3af9dc58afb9e902b972466d6da01cece89734`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T030821Z-account01-B01-qform-auto11/REPORT.md`.

For every quadratic-plus-affine residual in independent cap-one ORIGINAL coordinates and every physical cross block `C` with `Delta=E2(C)>0`, it proves by an integrated-frequency argument

`H_(1/2)(R):=sup_s E|R-s|^(-1/2)
 <= C_E2 Delta^(-1/8)`,                                          (4.1)

with

`C_E2=12*2^(5/6)*exp(5/24)=26.334046180759735... .`              (4.2)

There is no second-minor leverage gate.

The other required ingredient is elementary and dependence-safe. For

`Q=d(X_x+L_x(W))^2+R_x(W)`

with `X_x` independent of `W` and `f_x<=1`, conditioning on `W` gives the square-pushforward bound

`p_(Q|W)(t) <= |d|^(-1/2)|t-R_x(W)|^(-1/2)`.                     (4.3)

Therefore

`||p_Q||_infinity <= |d|^(-1/2) H_(1/2)(R_x)`.                  (4.4)

Combining (3.4), (4.1), and (4.4) proves the main new receiver.

### Theorem 4.1 — `QFORM-SAMESIDE-ONE-SQUARE-E2-RECEIVER-v1`

If `d!=0`, `delta!=0`, `||xi||F>0`, then

`boxed:
 ||p_Q||_infinity
 <= C_E2 ( |d| ||xi|| F )^(-1/4).
}`                                                               (4.5)

If `e!=0`, `delta!=0`, `||eta||F>0`, then

`boxed:
 ||p_Q||_infinity
 <= C_E2 ( |e| ||eta|| F )^(-1/4).
}`                                                               (4.6)

When both apply,

`boxed:
 ||p_Q||_infinity
 <= C_E2 [max{|d|||xi||F, |e|||eta||F}]^(-1/4).
}`                                                               (4.7)

These are essential-density bounds. They do not prove `phi_Q in L1` and do not by themselves prove continuity.

This is an actual integrated-Fourier advance on the same-side correction packet: the factor `F` no longer sits only in an algebraic exterior identity; it is spent through a literal physical `E2` bank and the unconditional half-Riesz Fourier theorem.

## 5. What the new receiver does and does not close

The r21 correction branch supplies

`(||xi||||eta||F/|delta|)^2 > Z/12`.                              (5.1)

Equations (4.5)-(4.7) show that this branch is paid whenever either one-sided currency

`|d|||xi||F` or `|e|||eta||F`

has a dimension-free lower bound. However (5.1) alone does not force such a lower bound: one may algebraically keep `||xi||||eta||F` fixed while making `F` small and the two star norms large. Therefore I do **not** claim that Theorem 4.1 closes the entire correction branch.

The remaining geometry is now sharper: the only unpaid correction states are simultaneously

1. large normalized two-star product `||xi||||eta||F/|delta|`, but
2. small one-sided products `|d|||xi||F` and `|e|||eta||F`.

Thus the next mechanism must use the two stars jointly in the small-`F` / near-leaf scaling, rather than trying another single-star pivot. This matches the independent checkerboard/near-leaf obstruction already found by the B07 workers.

## 6. Designated partner account04/B02 applied to an actual inequality

The designated partner theorem is `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`, canonical source

`yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

If a quadratic residual in independent cap-one ORIGINAL coordinates contains a nonsingular physical `3x3` principal block `H_0` with a zero diagonal entry, the partner proves a **continuous** residual density and

`||p_R||_infinity <= M_H:=3*2^(2/3)|det H_0|^(-1/3).`            (6.1)

For any probability density bounded by `M`, centered rearrangement gives

`sup_t E|R-t|^(-1/2) <= 2 sqrt(2M)`.                              (6.2)

Apply (6.1)-(6.2) to the one-sided Schur residual `R_x`, then use the exact square transfer (4.4). This gives the new nested partner inequality

`boxed:
 ||p_Q||_infinity
 <= 2^(4/3) sqrt(6)
    |d|^(-1/2)|det H_0|^(-1/6)
 < 6.172328 |d|^(-1/2)|det H_0|^(-1/6).
}`                                                               (6.3)

The symmetric `e`-side statement is identical. This is particularly relevant to the singular-pair debt: if `delta=0` and `d!=0`, completing `x` makes the surviving `y` diagonal exactly zero; whenever the resulting residual has a nonsingular physical triple containing (or otherwise using) that zero diagonal, the partner theorem plus (6.3) pays the branch. Such a nonsingular triple is not claimed to be automatic.

The partner residual itself has a continuous density. The final correlated shifted-square mixture in (6.3) is recorded here only as essentially bounded; no full continuity statement is silently inferred.

## 7. Fourier status

I again attempted to push the assigned unweighted criterion

`int_R |E exp(it X^T A X)| dt`.

No valid exact-target counterexample was obtained, and no full-scope proof was obtained. The new result instead uses the strongest correction-safe integrated-frequency statement presently available at the needed exterior order: a half-Riesz Fourier estimate from aggregate `E2`, followed by an exact physical-square kernel. Hence the target-wide unweighted `L1` criterion remains **OPEN**, not false.

## 8. Algebra regression

`CHECK.py` in this run folder tests (3.1)-(3.7) on 1,398 seeded random nonsingular configurations. The largest true-Schur identity errors were below `9.7e-14`; the projection identities were below `1.8e-14`; every tested `E2` incident-minor lower bound had positive numerical slack. `CHECK_OUTPUT.txt` records `STATUS PASS`. This is only a finite algebra regression; the symbolic proof above is primary.

## 9. First unpaid implication after this run

The immediate B02 target is now

`QFORM-SAMESIDE-TWOSTAR-SMALLF-TO-FRACTIONAL-v1`:

> In the correction branch (5.1), under simultaneous failure of both one-sided payments (4.5)-(4.6), use the forced two-star / near-leaf structure to build a product-preserving grouped random-slope or fractional-Fourier certificate, without rotating random coordinates or selecting a reciprocal tiny minor.

The sibling singular-pair branch remains only partially paid by (6.3), and the aggregate overlap-one/two/principal-third-volume compiler is still needed for a full target proof.

**Status:** supporting theorem proved; full QFORM remains OPEN; global continuity OPEN; target-wide unweighted Fourier `L1` OPEN.
