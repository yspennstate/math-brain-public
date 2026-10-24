# Post-refresh addendum — two-hub sharpening of the cut-free order-two branch

Fresh peer mathematics appeared after the main report write and before publication. It strengthens, rather than invalidates, the order-two cut-free compiler.

## 1. New source

`yspennstate/math-open-problems@c3a17bf12dc8e5fa2ee6d17be9ada1369564567b`, path

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B13/20260923T063002Z-account01-B13-qform-auto16/REPORT.md`

proves `QFORM-SCALAR-E2-ENTROPIC-LP-LINF-v1` for every row-marginal cap `1/2<=h<1`. For a genuine original scalar pivot `d!=0`, an actual scalar-Schur residual cross block of pair-volume `E=e_2(M^TM)`, an entropy-weighted pair-minor law of KL cost at most `L`, and any Fourier exponent `r in (2h,2)`, it gives

`||p_Q||_infinity <= C(h,r)|d|^(-1/2)K_2^(-1/8)`,

with

`C(h,r)=D_r [2 sqrt(e/(2h)) r/(r-2h)]^(1/2)`,

`beta=1-r/2`,

`D_r=(2/r) beta^(-1/2)[r/(2beta)]^beta`.

Its entropy-projection alternative also shows that if the paid branch fails in both orientations, then for every `h>2/3` the pair-minor mass is concentrated onto at most two physical row hubs and at most two physical column hubs. One of the at most four hub pairs then has joint pair-minor mass exceeding `E/8`, with the exact Frobenius identity `||aN-vu^T||_F^2`.

## 2. Apply it to this run's random cut

Keep the notation of the main report. For the scalar pivot `a=A_kk!=0`, let `S` be its full scalar Schur complement and

`D_2^perp(S)=sum_{|R|=|C|=2,R cap C=empty}det(S[R,C])^2`.

Theorem 2.1 of the main report selects an ORIGINAL-coordinate cut satisfying

`E=e_2(S[L,Rside]^T S[L,Rside]) >= D_2^perp(S)/16`.              (2.1)

Choose the rational parameters

`h=667/1000`,

`r=4341/2500=1.7364`,

`L=log 4`.                                                        (2.2)

Then `2h=1.334<r<2` and `2/h<3`, so every nonpaid hub set has cardinality at most two. Direct substitution in the peer formula gives

`C(h,r)=14.276551390329326...`.                                  (2.3)

Since KL cost at most `log4` implies `K_2>=E/4`, the selected-cut paid constant is

`C(h,r) 4^(1/8)=16.977776491081624...`.                          (2.4)

Using (2.1), `16^(1/8)=sqrt(2)`, hence

`||p_Q||_infinity
 <24.01020177262673...
   |a|^(-1/2)D_2^perp(S)^(-1/8)`.                                (2.5)

With the exact bordered identity

`B_{3,k}^perp(A)=a^2D_2^perp(S)`,                                (2.6)

this becomes

`boxed:
 ||p_Q||_infinity
 <24.011 (|A_kk|^2 B_{3,k}^perp(A))^(-1/8).
`                                                                      (2.7)

## 3. Stronger structural survivor

If the paid branch fails in both orientations, the peer theorem gives row and column hub sets of size at most two and a selected hub pair `(i,j)` whose joint pair-minor mass is greater than `E/8`. Combining with (2.1),

`E_ij > D_2^perp(S)/128`.                                         (3.1)

Bordering by the scalar pivot `k`, exactly as in the main report, yields

`boxed:
 J_{k;i,j}^perp(A) > B_{3,k}^perp(A)/128.
`                                                                     (3.2)

This is the strengthened theorem

`QFORM-DISJOINT-BORDER3-LINF-OR-TWOHUB-v1`:

for every `k` with `A_kk!=0` and `B_{3,k}^perp(A)>0`, either (2.7) holds or one physical pivot-row-column trihub captures more than `1/128` of the complete disjoint bordered-three-volume currency.

The main report's earlier theorem remains valid and has the better analytic constant `17.576` but the weaker concentration fraction `1/288`. The two valid Pareto alternatives are therefore

* analytic constant `17.576` versus structural fraction `1/288`;
* analytic constant `24.011` versus structural fraction `1/128` and a two-hub-per-side provenance.

No single determinant is selected in either route.

## 4. Latest correction check

The post-write correction `QFORM-SCALAR-PLUS-3D-ALL-COORD-MARGINAL-CAPS-INSUFFICIENT-v1` (`math-research-brain@d8ee1ecc7b3de107ac20387ea9e638f7f3fdb88b`) does not invalidate this theorem. That correction refutes replacing product provenance by generic one- and two-dimensional marginal caps after a nonlinear/reciprocal shear. Here every analytic input is applied before such a loss: the scalar pivot is an ORIGINAL independent coordinate, `S[L,Rside]` is an ORIGINAL-coordinate cross block of the exact Schur remainder, and the entropy/Fourier theorem is invoked at its proved product-law scope.

It does constrain the successor: the `1/128` trihub cannot be paid by discarding the remaining original-product provenance and retaining only low-dimensional marginal caps.

Full QFORM and full continuity remain OPEN.
