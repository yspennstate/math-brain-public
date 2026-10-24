SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-23T19:19:21Z.
attacking: the R2 adaptive-alignment survivor by an exact Pythagorean Schur-area identity, then spend the surviving physical rank-two volume with a dependence-safe scalar-square transducer.

# account03/B08 r43 — Pythagorean Schur area and an R2 adaptive-alignment compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T191921Z-account03-B08-qform-diffuse-r43`  
Assignment: diffuse eigenvector case  
Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Owner control: `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Classification: `NEW SUPPORTING ANALYTIC/STRUCTURAL THEOREM / FULL TARGET OPEN`.

The unrestricted conjecture remains OPEN. Global continuity remains OPEN. All coordinates below are ORIGINAL independent coordinates. No moment, support, log-concavity, Gaussian-mixture, iid, post-rotation independence, arbitrary-joint coarea, pointwise quadratic-phase decay, coefficient-small random-error deletion, or fiber-supremum argument is used.

The run began from brain main `c27181f672cb5f8930fd42a41d9f7411ab0c5881`; the prepublication control refresh reached `f62c3a8c1aadd3845d48c1c1ab1fd7c6fedc4bfb`, with the same owner-control revision `2026-09-22.15` and no later stop or reassignment.

## 1. Immediate predecessor and the first missing implication

The immediate B08 predecessor is

`yspennstate/math-open-problems@d2d64042e84bba8609cd2a27ae2dada21e215c38`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T165737Z-account03-B08-qform-diffuse-r42/REPORT.md`.

Inside the near-rank-one physical-triangle branch, r42 reduced the remaining outside cross geometry to the quantitative R1/R2 states

`R1: s1(C)>3L/8, s2(C)<L/8`,

or

`R2: s1(C)>3L/8, s2(C)>=L/8, s3(C)<L/64`,

unless a projected-crossing theorem already pays the full form. Its R2 aligned failure has a two-hub partner bank plus a third physical triangle coordinate whose outside row is almost contained in the partner-row space. The precise unresolved issue was whether this adaptive alignment survives an exact scalar Schur completion without silently throwing away the orthogonal leakage.

The new theorem below answers that question exactly: the post-Schur rank-two area is a **Pythagorean sum** of the aligned determinant factor and the orthogonal leakage factor. Thus leakage cannot cancel aligned volume; it can only add a perpendicular exterior component.

## 2. Source-valid analytic input: exact rank-two crossing

I use Section 1 of

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For an exact rank-two ORIGINAL-coordinate crossing `B` between two physical coordinates on one side and an arbitrary independent product bank on the other, with

`S(B)=s1(B)s2(B)=sqrt(det(BB^T))`,

the source Plancherel estimate has projection caps `M_X=1`, `M_Y<=2`, hence

`|phi_R(t)| <= min(1, pi sqrt(2) S(B)^(-1/2) |t|^(-1)).`        (2.1)

Therefore

`int |phi_R|^(3/2) <= 6 pi sqrt(2) S(B)^(-1/2)`,                 (2.2)

and inverse Hausdorff--Young gives

`boxed: ||p_R||_3 <= 3^(2/3) 2^(1/3) S(B)^(-1/3).`              (2.3)

Arbitrary same-bank quadratic-affine functions are retained by the source theorem.

I also rederive the one-square transducer needed below, so no independence between the Schur remainder and the shifted pivot is assumed. If `R` has density `p_R in L^3` and, conditional on the variables defining `R`, `V` has a translated density cap one, then for `a!=0`

`T=R+aV^2`

satisfies

`p_T(t) <= |a|^(-1/2) int_0^infinity p_R(t +/- u) u^(-1/2) du`.  (2.4)

For `P=||p_R||_3`, splitting at `r>0` gives

`int_0^r p_R(t-u)u^(-1/2)du <= 2^(4/3) P r^(1/6)`,

`int_r^infinity p_R(t-u)u^(-1/2)du <= r^(-1/2)`.                (2.5)

Optimizing at `r=[3/(2^(4/3)P)]^(3/2)` gives

`sup_t int_0^infinity p_R(t-u)u^(-1/2)du
 <= 8*3^(-3/4) P^(3/4)`.                                       (2.6)

Combining (2.3) and (2.6) proves the convenient exact-rank-two-plus-square bound

`boxed: ||p_T||_infinity <= C_* |a|^(-1/2) S(B)^(-1/4),}`       (2.7)

where

`C_* = 8 (2/3)^(1/4) = 7.228816028878758...`.                   (2.8)

This is essential boundedness. I do **not** claim continuity from the one-square transducer.

## 3. New exact identity — `QFORM-SCHUR-PYTHAGOREAN-RANK2-AREA-v1`

Let `M in R^(2 x m)` have full row rank. Let its rows be `m1,m2`. Let

- `a!=0` be an ORIGINAL-coordinate scalar pivot;
- `h=(h1,h2)^T` be its couplings to two physical hub coordinates;
- `b in R^m` be its row of couplings to the partner bank.

Decompose `b` orthogonally relative to the physical row space of `M`:

`b = k^T M + e`, `e perpendicular row(M)`,                       (3.1)

where `k in R^2` is unique. Put

`d = a-k.h`,                                                     (3.2)

and let the exact post-Schur two-hub/partner crossing be

`M' = M - h b/a`.                                                (3.3)

Then

`boxed:
 det(M'M'^T)
 = (d^2/a^2) det(MM^T)
   + ( ||(-h2,h1)M||_2^2 / a^2 ) ||e||_2^2 .}`                  (3.4)

In particular the two terms are nonnegative and there is no cancellation between aligned Schur loss and orthogonal leakage.

### Proof

Set

`T=I_2-hk^T/a`.

Then `M'=TM-(h/a)e`. If `t1,t2` are the rows of `TM`, exterior algebra gives

`m1' wedge m2'
 = t1 wedge t2 + [(h1 t2-h2 t1)/a] wedge e`.                    (3.5)

The rank-one terms in `t1,t2` cancel in the bracket, so

`h1 t2-h2 t1 = h1 m2-h2 m1 = (-h2,h1)M`.                       (3.6)

Also

`det T = 1-k.h/a = d/a`,                                        (3.7)

hence

`t1 wedge t2 = (d/a)(m1 wedge m2)`.                             (3.8)

The first term in (3.5) lies in `Lambda^2 row(M)`. The second lies in
`row(M) wedge row(M)^perp`, because `e perpendicular row(M)`. These two exterior subspaces are orthogonal. Moreover the vector in (3.6) lies in `row(M)`, so its wedge with `e` has norm equal to the product of the norms. Squaring (3.5) proves (3.4), since

`||m1 wedge m2||^2=det(MM^T)` and `||m1' wedge m2'||^2=det(M'M'^T)`. QED.

### Two immediate consequences

If the adaptive alignment is exact (`e=0`), then

`S(M') = |d/a| S(M)`.                                            (3.9)

Thus the only way exact alignment can collapse the rank-two partner area is the single scalar cancellation `d=a-k.h=0`.

If `d=0` but `e!=0`, then

`S(M') = ||(-h2,h1)M|| ||e|| / |a|`.                            (3.10)

So orthogonal leakage itself regenerates rank-two area unless its product with the transverse physical coupling is small.

## 4. Target-level conditional receiver

Condition only original coordinates outside the pivot, the two hubs, and the partner bank. The remaining quadratic form has the structure

`Q = a x^2 + 2x(h.y+b.z+beta) + F(y) + 2 y^T M z + G(z)`,        (4.1)

where `x` is one physical coordinate, `y in R^2` are two physical coordinates, `z` is an arbitrary original-coordinate product bank, and `F,G` are arbitrary quadratic-affine functions generated by the full ambient matrix and the conditioning.

Completing the physical pivot gives a translated cap-one square plus a remainder whose y-z crossing is exactly `M'` in (3.3). If the right side of (3.4) is positive, apply (2.7):

`boxed:
 ||p_Q||_infinity
 <= C_* |a|^(-1/2)
    [det(M'M'^T)]^(-1/8).}`                                     (4.2)

Equivalently, using (3.4),

`||p_Q||_infinity
 <= C_* |a|^(-1/2)
 [ (d^2/a^2)det(MM^T)
   +(||(-h2,h1)M||^2/a^2)||e||^2 ]^(-1/8).`                    (4.3)

All same-bank curvature and every conditioned outside coupling are retained. This is the promised analytic receiver for the adaptive-alignment state.

## 5. R2 compiler with an actual physical pivot

Now return to r42/R2. Let the three physical triangle coordinates be `{p,1,2}`, and designate `p` as a nonzero scalar pivot with

`|a|=|A_pp| >= tau L`.                                           (5.1)

Let the three rows of the outside cross block `C` be `c_p,c_1,c_2`. Define the physical row-pair exterior masses

`V_p1=||c_p wedge c_1||^2`,
`V_p2=||c_p wedge c_2||^2`,
`V_12=||c_1 wedge c_2||^2`.                                     (5.2)

Cauchy--Binet gives

`V_p1+V_p2+V_12=e_2(CC^T)
 >=s1(C)^2 s2(C)^2
 >9 L^4/4096.`                                                   (5.3)

There are now two exhaustive physical alternatives.

### R2-LP — pivot-incidence localization

If

`V_p1+V_p2 > (1/2)e_2(CC^T)`,                                   (5.4)

then the actual pivot coordinate carries aggregate second exterior mass

`boxed: V_p1+V_p2 > 9 L^4/8192.}`                               (5.5)

This is a genuine ORIGINAL-coordinate localized certificate. No single minor is selected or inverted. It is intentionally handed to localized-coordinate conditioning rather than falsely called a diffuse closure.

### R2-DP — pivot-excluding diffuse pair

Otherwise

`V_12 >= (1/2)e_2(CC^T)`,                                       (5.6)

so with

`M = [c_1; c_2]`

we have

`S(M)=sqrt(det(MM^T))
 >=s1(C)s2(C)/sqrt(2)
 > c_2 L^2`,                                                     (5.7)

where

`c_2=3/(64 sqrt(2))=0.03314563036811941...`.                    (5.8)

Use the FULL outside bank; unlike r42's projected-crossing split, no half-bank loss is needed. Decompose the pivot row `c_p=k^TM+e`, `e perpendicular row(M)`, and set `d=a-k.h` as above.

If either

`|d| >= |a|/2`,                                                  (5.9)

or

`||(-h2,h1)M|| ||e|| >= (c_2/2)|a| L^2`,                        (5.10)

then (3.4) gives

`S(M') >= (c_2/2)L^2`.                                          (5.11)

Equation (4.2) therefore yields the concrete target-scale estimate

`boxed:
 ||p_Q||_infinity
 < 20.148 tau^(-1/2) L^(-1).}`                                  (5.12)

The exact numerical coefficient from (2.8) is `20.14735785624496...`.

If (5.9) and (5.10) both fail, the formerly vague adaptive-alignment obstruction has been sharpened to the simultaneous packet

`boxed:
 |a-k.h|<|a|/2,
 ||(-h2,h1)M|| ||e||
   < [3/(128 sqrt(2))] |a| L^2.}`                               (5.13)

Thus in the R2 chamber with a quantitative scalar pivot, the diffuse branch is now:

`localized pivot exterior bank  OR  continuous? no -- essential L-infinity <20.148 tau^(-1/2)/L  OR  precise adaptive cancellation + small transverse leakage product.`

The paid branch proves essential boundedness. Continuity is not established by the square transducer.

## 6. The adaptive scalar factor cannot be bounded away from zero from the target spectrum alone

The remaining factor in (5.13) is genuine. Consider the symmetric matrix, in original coordinates `(p,h1,h2,j1,j2)`,

```
A0 = [[1,1,0,1,0],
      [1,0,0,1,0],
      [0,0,0,0,1],
      [1,1,0,0,0],
      [0,0,1,0,0]].
```

Its characteristic polynomial is

`(lambda-1)(lambda+1)^2(lambda^2-2lambda-1)`,                   (6.1)

so its eigenvalues are

`1, -1, -1, 1-sqrt(2), 1+sqrt(2)`.                              (6.2)

Hence it satisfies the owner target's three-large-eigenvalue condition.

Take the scalar pivot `p`, hubs `(h1,h2)`, and partner bank `(j1,j2)`. Then

`a=1`, `M=I_2`, `h=(1,0)`, `b=(1,0)`, `k=(1,0)`, `e=0`,

so

`d=a-k.h=0`,                                                     (6.3)

and the exact Schur crossing is `diag(0,1)`, rank one. Therefore no proof may assert a universal lower bound on `|a-k.h|/|a|` from the bare target spectrum. This is a refuted intermediate implication, not a counterexample to QFORM: the physical principal triple `(p,h1,j1)` has determinant one and is a localized configuration.

## 7. Designated partner account04/B08 applied at an actual endpoint

The completed designated partner is

`yspennstate/math-open-problems@abbec61f52e1f4b4d367fd67e73e4d2501ac9c74`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T091414Z-account04-B08-QFORM-r1/REPORT.md`.

For

`Q_(R,L)=L X0^2+2LR U1V1+2L R^(-1)U2V2`, `R>=3`,                (7.1)

the partner theorem proves

`boxed: ||p_(Q_(R,L))||_infinity <7.251/L.`                     (7.2)

This is an actual endpoint of the new compiler: choose pivot `X0`, hubs `(U1,U2)`, partner bank `(V1,V2)`. Then

`a=L`, `h=0`, `b=0`, `e=0`, `d=L`,
`M=L diag(R,R^(-1))`, `S(M)=L^2`.                               (7.3)

Thus the partner endpoint lies in the Schur-survival branch with no loss as `R to infinity`. Substitution into the self-contained estimate (4.2) gives the compatible value `C_*/L=7.228817/L`; the designated partner result (7.2) independently supplies the required completed-partner inequality on precisely the same target-valid family. The difference is only the harmless optimization of the one-sided half-kernel split in (2.5)-(2.6).

## 8. What changed and what remains

The r42 R2 adaptive-alignment state is no longer merely `B approximately K M_J`. Once a quantitative physical scalar pivot is designated, **all** of the outside bank can be used and the exact Schur area is given by (3.4). In the pivot-excluding diffuse half of the exterior bank, either the full form is paid by `<20.148 tau^(-1/2)/L`, or two explicit quantities must simultaneously be small: the aligned scalar factor `a-k.h` and the product of orthogonal leakage with the transverse physical hub direction.

The remaining B08 debts are now:

1. pay the localized pivot-incidence exterior bank (5.5) by a localized-coordinate receiver without selecting one tiny minor;
2. pay the simultaneous adaptive-cancellation packet (5.13), using the rank-one post-Schur channel together with the pivot-induced outside square direction while retaining arbitrary same-bank curvature;
3. handle the R1 chamber and the small/zero scalar-pivot branch.

The exact matrix (6.1) shows debt 2 cannot be removed by a spectral lower bound on `d`; its resolution must use the localized determinant or a grouped rank-one-plus-square mechanism.

Full QFORM status: **OPEN**. No counterexample to the conjecture was found.

## 9. Regression computation

`CHECKS.py` and `CHECKS.txt` beside this report verify:

- 5,000 seeded random instances of (3.4), with `e` constructed exactly orthogonal to `row(M)` numerically;
- the constants `C_*=7.228816028878758`, `c_2=0.03314563036811941`, and the R2 payment constant `20.14735785624496`;
- the exact characteristic polynomial in (6.1).

The maximum normalized numerical discrepancy in (3.4) was `2.554e-11`. This finite calculation is regression evidence only; the proof is the exterior-orthogonality argument in Section 3.

Checker terminator: `QFORM_B08_R43_CHECK_PASS`.
