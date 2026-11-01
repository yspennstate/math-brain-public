# Checks for fleet03/B14 definite-pair localization

Run: `20260924T043626Z-fleet03-B14-QFORM-auto11`.

## Algebraic checks

For `B=[[a,c],[c,b]]`, completing the first coordinate gives residual curvature

`d=b-c^2/a=det(B)/a`.

If `B` is definite then `det(B)>0` and `a,d` have the same sign. The density constant from the two same-sign square integral is

`pi/(sqrt(|a|) sqrt(|d|)) = pi/sqrt(det B)`.

The relevant beta integral is exact:

`int_{-sqrt(s/d)}^{sqrt(s/d)} du/sqrt(s-du^2)=pi/sqrt(d)` for `s>0,d>0`.

The first square pushforward envelope is translation-uniform:

`p_{a(W+r)^2}(v) <= K_W/(sqrt(|a|) sqrt(|v|))`

on the sign-compatible half-line. It follows from summing the two inverse-image branches; each contributes `K_W/(2 sqrt(|a|) sqrt(|v|))`.

## Target-valid matrix check

`A_*=[[2,1,0],[1,2,0],[0,0,-1]]`.

The upper `2x2` block has determinant `3` and eigenvalues `3,1`; the third eigenvalue is `-1`. Thus

`spec(A_*)={3,1,-1}`

and all three eigenvalues have modulus at least one.

The new estimate is

`pi/sqrt(3)=1.8137993642342178...`.

Fleet04/B14 r10 gives on the same block

`6 sqrt(pi)/sigma`, with `sigma=1`, namely

`6 sqrt(pi)=10.634723105433096...`.

## Opposite-sign Schur-cancellation check

For

`Q=W^2-U^2+UZ-Z^2/4 = W^2-(U-Z/2)^2`,

the homogeneous matrix in `(W,U,Z)` is

`[[1,0,0],[0,-1,1/2],[0,1/2,-1/4]]`.

The lower `2x2` block has determinant zero and trace `-5/4`, so

`spec={1,-5/4,0}`.

Hence this is a rank-two obstruction, not a counterexample to the three-large-eigenvalue conjecture.

If `U,Z` are independent `Unif[-1/2,1/2]` and `V=U-Z/2`, then for every `|v|<=1/4`, the whole `z` interval `[-1/2,1/2]` satisfies `v+z/2 in [-1/2,1/2]`; therefore `p_V(v)=1` on `[-1/4,1/4]`.

For `0<epsilon<1/4096`, `v in [2sqrt(epsilon),1/8]`, and `w in [v,v+epsilon/(3v)]`, one has `w<=13v/12<1/4` and

`0<=w^2-v^2=(w-v)(w+v)<=epsilon`.

Thus

`P(0<=Q<=epsilon) >= (epsilon/3) log(1/(16sqrt(epsilon)))`,

so the interval probability divided by length diverges.

## Scope checks

- Conditioning is only on outside original coordinates; no rotation is applied to the source product law.
- Arbitrary conditional translations are absorbed before the density bound and do not affect marginal caps.
- No moment/tail/support/fragment assumptions are used.
- Essential boundedness is proved; continuity is not claimed.
- Full QFORM remains open because no universal lower bound on a definite physical-pair determinant follows here from `s_3(A)>=1`.
