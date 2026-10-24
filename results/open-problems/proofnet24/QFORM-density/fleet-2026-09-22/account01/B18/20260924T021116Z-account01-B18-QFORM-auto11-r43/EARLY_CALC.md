# Early substantive calculation — exact rank-one cross + rank-one complement

Status at this checkpoint: supporting calculation; full QFORM remains OPEN.

Let the ORIGINAL coordinates split as `I disjoint_union J`, and suppose

`A=[[0,B],[B^T,C]]`, `rank(B)=rank(C)=1`, `s=s_3(A)>0`.

Write

`B=sigma u v^T`, `C=lambda w w^T`,

with `u` unit in the I-bank, `v,w` unit in the J-bank, `sigma>0`, `lambda!=0`. Since `s_3(A)>0`, `w` is not parallel to `v`. Choose a unit `z perpendicular v` in `span{v,w}` and write

`w=a v+b z`, `a^2+b^2=1`, `b!=0`.

On the active orthonormal basis `(u,v,z)`, the physical matrix is

```
H = [[0, sigma, 0],
     [sigma, lambda a^2, lambda a b],
     [0, lambda a b, lambda b^2]].
```

Direct expansion gives the determinant identity

`det H = - sigma^2 lambda b^2`.                                      (E1)

Because the global matrix has rank at most three and `s_3(A)>0`, its three nonzero eigenvalues are exactly the eigenvalues of `H`. Hence

`|sigma^2 lambda b^2|=|det H|=prod_{r=1}^3 |mu_r(A)| >= s^3`.       (E2)

For cap-one product inputs put

`S=u^T X_I`, `Y=v^T X_J`, `Z=z^T X_J`.

The source sets I,J are disjoint, so S is genuinely independent of the possibly dependent pair `(Y,Z)`. Livshyts--Paouris--Pivovarov, Theorem 1.1, gives

`||p_S||_infinity<=sqrt(2)`, `||p_(Y,Z)||_infinity<=2`,             (E3)

with the obvious direct endpoint improvement if a bank dimension equals the projected dimension. No independence of Y,Z is asserted.

The quadratic form is exactly

`Q=2 sigma S Y + lambda a^2 Y^2 +2 lambda a b Y Z+lambda b^2 Z^2`. (E4)

Apply account02/B18 `QFORM-CAPPED-SCALAR-DEPENDENT-PAIR-v1`, source commit `ba2e2fbc9d22196f83c4ae35080e7f3d23a55fa1`, which gives

`||p_Q||_infinity <= 3(2 M K)^(2/3)|beta^2 gamma|^(-1/3)`.

With `K=sqrt(2)`, `M=2`, `beta=sigma`, `gamma=lambda b^2`, (E2) gives

`||p_Q||_infinity <= 3*2^(5/3)/s = 9.524406311809198.../s`.         (E5)

Thus the literal model endpoint highlighted by account02/B18's latest `QFORM-ZEROSELF-COMPLEMENT-NORM-FUNNEL-v1` is paid when the complementary curvature is exactly rank one, even at the boundary `||C||_op=s` where that funnel no longer forces a second cross singular value.

The newest account02/B18 funnel is also applied on the same class: if `c=||C||_op<s`, then

`||p_Q||_infinity <=2 sqrt(pi)/sqrt(s(s-c))`;                      (E6)

in particular `c<=s/2` gives `<=2 sqrt(2 pi)/s=5.013256549262.../s`.

Continuity is not claimed from (E5). The remaining structural debt after this exact endpoint is the genuinely nonzero near-rank-one cross tail and/or higher-rank same-bank complement; no small coefficient is deleted here.
