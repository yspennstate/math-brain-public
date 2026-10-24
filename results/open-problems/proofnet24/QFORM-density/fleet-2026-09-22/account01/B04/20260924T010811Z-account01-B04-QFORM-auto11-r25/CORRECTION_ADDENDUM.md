# r25 correction addendum — zero-diagonal partner-scope stress example

This addendum preserves the original REPORT.md and corrects only its Sections 6–7 example/application. The main theorems in Sections 2–5 (`QFORM-EXTERIOR-LEVERAGE-DISJOINT-E3-v1`, `QFORM-COLLISION-LEVERAGE-CROSS-E3-v1`, the stable-rank corollary, and the small-pair complement-curvature payment) are unchanged.

The original Section 6 matrix is a valid target example for the new collision-leverage theorem, but its diagonal is not identically zero. Therefore the statement that account02/B04 r16 applies to that exact carrier "as stated" was too broad: r16 is formulated in the zero-anchor C1 residual-curvature setting, where the residual matrix is symmetric and zero diagonal. The numerical comparison in the original Sections 6–7 is withdrawn. The following corrected example lies literally inside the partner theorem's scope.

## Corrected zero-diagonal genuinely rotated indefinite example

Let `U` be a `66 x 4` real matrix. Use two distinguished physical rows

`u_0 = sqrt(3/20) (1,0,1,0)`,
`u_1 = sqrt(3/20) (1,0,-1,0)`.                                   (A.1)

Index the other 64 rows by `x in F_2^6`. Choose four distinct nontrivial Walsh characters `chi_1,...,chi_4` and put

`u_x = ( sqrt(7/10) chi_1(x)/8,
          chi_2(x)/8,
          sqrt(7/10) chi_3(x)/8,
          chi_4(x)/8 ).`                                          (A.2)

Walsh orthogonality and the sign cancellation between `u_0,u_1` give exactly

`U^T U = I_4`.                                                     (A.3)

Let

`Lambda = diag(2,2,-2,-2)`,
`E=U Lambda U^T`.                                                  (A.4)

Then the nonzero spectrum of `E` is exactly

`{2,2,-2,-2}`.                                                     (A.5)

Moreover every physical diagonal entry of `E` is zero. For the two distinguished rows this follows because their positive and negative squared coordinates agree. For each Walsh row,

`u_x^T Lambda u_x
 =2[(7/10)/64+1/64]-2[(7/10)/64+1/64]=0`.                        (A.6)

The leverage scores are

`ell_0=ell_1=3/10`,
`ell_x=17/320` for each of the 64 Walsh rows.                      (A.7)

Hence the basic undeleted max-leverage gate of account02/B04 r16 fails:

`r beta =4*(3/10)=6/5>1`.                                         (A.8)

But the collision leverage is

`tau=2*(3/10)^2+64*(17/320)^2
    =577/1600 <1`,                                                (A.9)

while

`e_3(E^2)=C(4,3)*4^3=256`.                                       (A.10)

Therefore the new collision theorem guarantees a literal physical cut with

`E_3(E[I,J]) >= (1-577/1600)*256/64 =1023/400`,                  (A.11)

and the completed cross-E3 compiler yields

`boxed:
 ||p_(X^T E X)||_infinity
 <= C_* (1023/400)^(-1/6)
 =7.228408463978281... ,
 p in C_0(R).}`                                                   (A.12)

To place the same carrier literally in the zero-anchor C1 setting, add two original coordinates `h,n` and define

`A_* = [[0,1],[1,0]] direct_sum E`.                               (A.13)

Relative to the physical anchor `h`, `N={n}` and the 66 residual coordinates form `Z`; the residual `E_ZZ=E` is symmetric, zero diagonal, rank four, and genuinely rotated. The nonzero spectrum of `A_*` is

`{2,2,1,-1,-2,-2}`,                                               (A.14)

so the exact owner spectral hypothesis holds with room to spare.

## Correct designated-partner application on the same carrier

Apply account02/B04 r16 to `A_*` after deleting only the two heavy residual rows

`H={0,1}`.                                                         (A.15)

On the remaining 64-row Walsh bank,

`G=U_L^T U_L=diag(7/10,1,7/10,1) >= (7/10) I`,                   (A.16)

so take

`gamma=7/10`.                                                      (A.17)

Every residual row has leverage

`beta_H=17/320`,                                                   (A.18)

and therefore

`r beta_H/gamma
 =4*(17/320)/(7/10)
 =17/56<1`.                                                        (A.19)

The partner theorem gives

`g=(1-sqrt(17/56))/2
 =0.22451341749033016...`.                                        (A.20)

Since `s_3(E)=2`, its completed inequality is

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= C_*/[(7/10)*2*g]
 =26.893146839247372... .}`                                       (A.21)

The new collision-leverage theorem on the same ambient matrix uses the residual bank `E` and gives the sharper bound (A.12), improving the completed partner certificate by

`26.893146839247372 / 7.228408463978281
 =3.720479684188497...`.                                          (A.22)

The comparison is scoped: r16 remains valuable when collision leverage is large but a small physical heavy set can be deleted while retaining the residual frame.

## Status after correction

The full conjecture remains open. The paid small-pair complement-curvature branch and the exterior-power theorem are unaffected by this correction. The current remaining structural implication is still

`QFORM-SMALLPAIR-LOW-STABLERANK-OR-HIGH-COLLISION-ROUTING-v1`:

route `stable-rank(off(C))<3` or `sum_i (P_range(off(C)))_ii^2>1/2` into completed rank-two rough-curvature, grouped-hub, fixed-pair, projected-crossing, ridge, or square-bank receivers, without deleting a nonzero random quadratic remainder or inverting a vanishing local coefficient.
