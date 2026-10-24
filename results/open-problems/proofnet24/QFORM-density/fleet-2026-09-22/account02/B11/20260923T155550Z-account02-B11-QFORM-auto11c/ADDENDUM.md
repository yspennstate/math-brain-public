# Addendum — condition the dominant spike before paying the residual Fresnel frame

This addendum strengthens the single-spike reduction in `REPORT.md`. It is independent of the two-plane null-ruling coordinates once the dominant ORIGINAL coordinate has been identified.

## Theorem A.1 — `QFORM-DOMINANT-SPIKE-RESIDUAL-FRESNEL-v1`

Let

`A=R M R^T`, `R^T R=I_3`,

be exact rank three, with `M` invertible symmetric and

`s=min |eig(M)|>0`.

Fix an ORIGINAL coordinate `h`, put

`r=r_h`, `c=||r||^2<1`,

and define the residual frame Gram

`G=I_3-r r^T`.                                                       (A.1)

For every `j!=h` put

`ell_j^(h)=r_j^T G^(-1)r_j`.                                         (A.2)

If

`max_(j!=h) ell_j^(h)<=1/2`,                                         (A.3)

then for arbitrary independent cap-one inputs and arbitrary affine terms produced by conditioning,

`boxed:
 ||p_(X^T A X)||infinity
 <=12 [ |det M| (1-c) ]^(-1/3)
 <=12/[s(1-c)^(1/3)].`                                               (A.4)

In particular, if `c<=3/4`,

`boxed:
 ||p_(X^T A X)||infinity
 <=12*4^(1/3)/s
 =19.0488126.../s.`                                                   (A.5)

Thus every unpaid dominant-spike state from `REPORT.md` satisfies the sharper structural alternative

`c_h>3/4`                                                            (A.6)

or there exists another ORIGINAL coordinate `j` with

`ell_j^(h)>1/2`.                                                      (A.7)

The first branch is quantitatively near-coloop in spectral leverage; the second is a genuine two-spike localization branch.

### Proof

Condition on the original scalar `X_h`. This is free. The remaining quadratic part is the principal block

`A_(-h,-h)=R_(-h) M R_(-h)^T`.                                       (A.8)

By Parseval,

`R_(-h)^T R_(-h)=I-r r^T=G`.                                         (A.9)

Because `c<1`, `G` is positive definite. Set

`U=R_(-h) G^(-1/2)`,
`M_h=G^(1/2) M G^(1/2)`.                                             (A.10)

Then

`U^T U=I_3`,
`A_(-h,-h)=U M_h U^T`.                                               (A.11)

The squared spectral leverage of residual original coordinate `j` in this orthonormalized frame is exactly

`||u_j||^2=r_j^T G^(-1)r_j=ell_j^(h)`.                               (A.12)

Hence (A.3) is precisely the leverage hypothesis of the completed Fresnel--Brascamp--Lieb Theorem F in the required Claude package `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. That theorem tolerates the arbitrary linear term induced by the conditioned value of `X_h`, so uniformly in that value,

`||p_(Q | X_h)||infinity<=12 |det M_h|^(-1/3)`.                      (A.13)

Now

`det M_h=det(G) det(M)`.                                              (A.14)

The rank-one determinant lemma gives

`det G=det(I-r r^T)=1-||r||^2=1-c`.                                  (A.15)

Therefore

`||p_(Q | X_h)||infinity
 <=12[|det M|(1-c)]^(-1/3)`,                                         (A.16)

uniformly in the conditioned scalar. Averaging the conditional laws proves the first inequality in (A.4). Since `|det M|>=s^3`, the second follows. Equation (A.5) is immediate from `1-c>=1/4`. QED.

## Exact residual-leverage identity and the two-spike meaning

For later use, Sherman--Morrison gives

`G^(-1)=I+[r r^T]/(1-c)`.                                            (A.17)

Let

`c_j=||r_j||^2`,
`g_hj=||r_h wedge r_j||^2=c c_j-(r_h.r_j)^2`.                         (A.18)

Then

`ell_j^(h)
 =c_j+(r_h.r_j)^2/(1-c)
 =[c_j-g_hj]/(1-c)`.                                                  (A.19)

Consequently, if `c<=3/4` but the residual-Fresnel exit fails, some `j` satisfies

`c_j-g_hj>(1-c)/2>=1/8`.                                             (A.20)

So the remaining second-spike branch is not an artifact of orthonormalization: a second original coordinate has quantitative residual leverage after the first spike is deleted.

If additionally `g_hj` is quantitative, the already-completed pair-area/disjoint-volume machinery is the appropriate exit. If `g_hj` is small, (A.20) forces a two-coordinate localization of one spectral direction and identifies the next genuinely unpaid geometry.

## Integration with the main run and the partner collision collar

`REPORT.md` proves that failure of its relative-atom crosscut gives one original coordinate `h` with

`c_h>tau/36`.                                                        (A.21)

The latest designated partner account03/B11 r35 pays the exterior collision wings, leaving only

`3/4<C2=sum_i c_i^2<5/4`.                                             (A.22)

Theorem A.1 now shows that within this collar the single-spike branch itself has only two possibilities:

1. **near-coloop:** `c_h>3/4`;
2. **two-spike residual localization:** `c_h<=3/4` and some `j` satisfies (A.20).

This is strictly sharper than the predecessor `O(tau^-2)` finite-heavy-set remainder and sharper than the one-spike statement alone.

The sign-specific splice remains unchanged. For signature `(2,1)`, the required ruled theorem pays the majority-sign one-sheet half-line; a fixed-scale minority physical pivot is paid by `QFORM-MINORITY-SCHUR-DEFINITE-v1`. The hard state after this addendum is therefore a near-null two-sheet problem inside either the near-coloop or two-spike localization branch.

The rank-two logarithmic control is unchanged: two opposite-sign directions alone can have the genuine `log(1/|t|)` density singularity. Theorem A.1 pays the third direction through three-dimensional Fresnel decay of the **residual original-coordinate frame after conditioning the spike**, not by declaring rotated coordinates independent.

The unrestricted QFORM conjecture remains open.