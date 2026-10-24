# r36 addendum — localized exit from the amplified transverse three-frame

This addendum complements `REPORT.md`. It treats the failure of the diffuse-frame gate in Corollary 4.1 and converts it into explicit ORIGINAL-coordinate matrix currency. It does not claim that every resulting off-diagonal-star or two-pivot branch is already paid.

Keep the notation and hypotheses of REPORT.md Sections 3--4 through

`p<=1/48`, `x=s_3(C)/L<=1/130`, `d>=1/2`.

Then

`tau=||(I-UU^T)b|| >= tau_0 L`,
`tau_0=(129/130)sqrt(47)=6.802918795782...`,

and the top-two child singular values are at least

`sigma L`, `sigma=sqrt(47/48)=0.989528507253...`.

Let

`s=b/||b||=d w+U c`,
`w perpendicular range(U)`, `||w||=1`, `||c||=sqrt(1-d^2)`,
`W=[w,U]`.

Assume now that the diffuse-frame gate fails:

`max_j ||W_{j,*}||^2 >1/48`.                                  (A.1)

## A.1 A rowwise angle lemma

For an ORIGINAL child coordinate `j`, put

`ell_j=||U^T e_j||^2`,
`h_j=w_j^2+ell_j`.

Then

`boxed{
 max{|s_j|, sqrt(ell_j)}
 >= sqrt((1-sqrt(1-d^2))/2) sqrt(h_j).
}`                                                               (A.2)

### Proof

Set `c_0=sqrt(1-d^2)`. Since the `U`-component of `s` has coefficient vector of norm `c_0`,

`|(Uc)_j|<=c_0 sqrt(ell_j)`.

If `t=max{|s_j|,sqrt(ell_j)}/sqrt(h_j)`, then from

`s_j=d w_j+(Uc)_j`

we get

`|w_j|<=t(1+c_0)sqrt(h_j)/d`.

Therefore

`h_j=w_j^2+ell_j
 <=t^2 h_j[(1+c_0)^2/d^2+1]
 =t^2 h_j * 2/(1-c_0)`.

Cancel `h_j` and rearrange to obtain (A.2). QED.

Since `d>=1/2`,

`sqrt((1-sqrt(1-d^2))/2)
 >=sqrt((1-sqrt(3)/2)/2)
 =sin(pi/12)
 =0.2588190451025... .`                                         (A.3)

By (A.1), some physical row has `h_j>1/48`. Hence either

`|s_j| > sin(pi/12)/sqrt(48)`                                   (A.4)

or

`sqrt(ell_j) > sin(pi/12)/sqrt(48)`.                            (A.5)

## A.2 First localized exit: a macroscopic literal hub coefficient

In case (A.4), since `||b||>=tau>=tau_0L`,

`boxed{
 |b_j| > [tau_0 sin(pi/12)/sqrt(48)] L
       =0.254138755477... L.
}`                                                               (A.6)

Thus a heavy frame row cannot remain only an abstract leverage certificate: it produces an actual ORIGINAL-coordinate off-diagonal coefficient exceeding `0.254L`.

Let `rho=0.254138755477...`. For the physical principal pair `(i,j)`, either

`max{|A_ii|,|A_jj|} >= (rho/2)L
                     =0.127069377738... L`,                     (A.7)

or both diagonals are smaller than `|A_ij|/2`, in which case

`boxed{
 |det A[{i,j},{i,j}]|
 =|A_ii A_jj-A_ij^2|
 > (3/4)rho^2 L^2
 =0.0484398802766... L^2.
}`                                                               (A.8)

If (A.7) occurs, the completed all-sign scalar-pivot theorem

`proofnet24/QFORM-density/interactive/20260923T192150Z-all-sign-scalar-pivot/REPORT.md`

pays the whole ambient form (essential density; continuity not supplied by that theorem):

`||p_Q||_infinity
 <= C_*/sqrt(0.127069377738...) * L^(-1)
 <3.904e9/L`,                                                    (A.9)

where `C_*=1.391402171...e9` is the source theorem's universal constant.

If not, (A.8) supplies a fixed-scale ORIGINAL physical two-pivot determinant. No claim is made here that this determinant alone closes the QFORM target.

## A.3 Second localized exit: a macroscopic child row

In case (A.5), spectral orthogonality of `U` and the child tail gives

`||C e_j||^2
 =||D U^T e_j||^2+||C_tail(I-UU^T)e_j||^2
 >=sigma^2 L^2 ell_j`.

Therefore

`boxed{
 ||C e_j||
 > [sigma sin(pi/12)/sqrt(48)] L
 =0.0369661245256... L.
}`                                                               (A.10)

Hence either

`|C_jj|>0.0261389973262... L`,                                  (A.11)

or

`||C_{-j,j}||_2>0.0261389973262... L`.                          (A.12)

The diagonal alternative (A.11) is again paid by the completed all-sign scalar-pivot theorem:

`||p_Q||_infinity<8.607e9/L`                                    (A.13)

as an essential-density estimate. The remaining alternative (A.12) is a literal ORIGINAL-coordinate child star of fixed scale.

## A.4 Localized router obtained

Combining the cases: under the amplified low-tail transverse hypotheses, failure of the diffuse three-frame gate forces at least one of

1. an already-paid scalar pivot `|A_kk|>0.02613L`;
2. a physical two-coordinate principal determinant `>0.04843L^2`;
3. a literal child off-diagonal row star `>0.02613L`.

Thus the only genuinely diffuse branch is paid by REPORT.md Corollary 4.1, while the non-diffuse branch is converted to explicit physical currency. The remaining task is to compile the determinant/star alternatives without invoking any refuted one-minor or one-star shortcut.
