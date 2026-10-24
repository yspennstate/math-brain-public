# r46 addendum — sharpening the Q1 hub tube from rank four to rank two

This addendum strengthens Section 3 of the r46 report. The unrestricted QFORM conjecture remains OPEN.

Keep the notation of `QFORM-Q1-HUBSLICE-DIAGONAL-OR-CROSS-v1`. For each wing tuple `w`,

`M_w=(det B_w)A_H-T_w`, `rank(T_w)<=2`,                          (A.1)

where `A_H=A[H,H]`, and put

`D_w=diag(M_w)`, `F_w=M_w-D_w`.                                  (A.2)

Thus

`(det B_w)A_H-D_w=T_w+F_w`.                                      (A.3)

The left side is symmetric.

## Theorem — `QFORM-Q1-HUBBLOCK-DIAG-RANK2-STABILITY-v1`

Let

`C2(H)={D+R: D physical diagonal on H, R=R^T, rank(R)<=2}`.       (A.4)

Then for every wing tuple `w`,

`boxed:
 |det B_w| dist_F(A_H,C2(H))
 <=(1+sqrt(2)) ||F_w||_F.
`                                                                       (A.5)

Consequently, with

`Delta2=sum_w |det B_w|^2`, `Z1=sum_w ||F_w||_F^2`,             (A.6)

one has

`boxed:
 Delta2 * dist_F(A_H,C2(H))^2
 <=(1+sqrt(2))^2 Z1.
`                                                                       (A.7)

On the unpaid r46 q=1 tube `Z1<P1/16`,

`boxed:
 Delta2 * dist_F(A_H,C2(H))^2
 < ((1+sqrt(2))^2/16) P1
 =((3+2sqrt(2))/16)P1.
`                                                                       (A.8)

At the exact endpoint `Z1=0`, if `Delta2>0` then

`boxed: A[H,H]=D+R, D diagonal, R=R^T, rank(R)<=2.`              (A.9)

Thus exact q=1 overlap-diagonalization forces a literal physical diagonal-plus-rank-two hub block as soon as the mixed wing second compound is nonzero.

### Proof

Write

`T_w=S_w+K_w`,
`S_w=(T_w+T_w^T)/2`,
`K_w=(T_w-T_w^T)/2`.                                             (A.10)

Taking skew parts in (A.3) gives

`K_w=-skew(F_w)`, hence
`||K_w||_op<=||F_w||_F`.                                         (A.11)

Since `rank(T_w)<=2` and `S_w=T_w-K_w`, the rank-perturbation singular-value inequality gives

`s_3(S_w)<=||K_w||_op<=||F_w||_F`.                               (A.12)

Also `rank(S_w)<=rank(T_w)+rank(T_w^T)<=4`, so only its third and fourth singular values can lie below the best symmetric rank-two truncation. Let `R_w` be the spectral truncation of the symmetric matrix `S_w` to its two largest singular directions. Then `R_w=R_w^T`, `rank(R_w)<=2`, and

`||S_w-R_w||_F
 <=sqrt(2) s_3(S_w)
 <=sqrt(2)||F_w||_F`.                                            (A.13)

Taking symmetric parts in (A.3),

`(det B_w)A_H
 =D_w+S_w+sym(F_w)`.                                             (A.14)

Therefore

`dist_F((det B_w)A_H,C2(H))
 <=||S_w-R_w||_F+||sym(F_w)||_F
 <=(1+sqrt(2))||F_w||_F`.                                        (A.15)

The class `C2(H)` is a cone, so the left side equals

`|det B_w| dist_F(A_H,C2(H))`.                                   (A.16)

This proves (A.5); square and sum over `w` to obtain (A.7). Equation (A.8) uses the r46 Q1 tube. If `Z1=0`, every `F_w=0`; any tuple with `det B_w!=0` gives (A.9) directly, and `Delta2>0` guarantees such a tuple. QED.

## Scope

This is a deterministic coefficient theorem. It does **not** delete the nonzero residual in (A.8) from the random quadratic form, and it does not assert that the exact diagonal-plus-rank-two hub block alone supplies the third source of smoothing for the full ambient form. Its value is that the remaining Q1 obstruction now interfaces exactly with the fleet's diagonal-plus-rank-two Fourier/Strichartz machinery without any reciprocal individual-minor selection. The missing analytic receiver must retain the wing couplings and the nonzero residual when present.
