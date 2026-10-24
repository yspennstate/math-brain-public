# Deterministic checks for account01/B09 20260923T091527Z

These checks support the adjacent `REPORT.md`; they are not a substitute for proof.

## 1. Constants

For the designated-partner stress at `m=16`,

`rho=(15/16)^3`,

and

`(5/3) exp(3/5) rho^(-1/5)
 =(5/3) exp(3/5) (15/16)^(-3/5)
 =3.156768053858056 <3.157.`

For the one-hub/one-square stress,

`rho=(15/16)^2`,

and

`3 exp(2/3) rho^(-1/3)
 =3 exp(2/3)(15/16)^(-2/3)
 =6.100096776742413 <6.101.`

For the zero-hub `r=3` endpoint on three disjoint flat groups,

`3e [(15/16)^3]^(-1/3)
 =3e(15/16)^(-1)
 =8.698501851068945.`

## 2. Compressed spectra

For

`Q_m=2X_1<c_1,Y>+2X_2<c_2,Y>+<v,Y>^2`

with `c_1,c_2,v` mutually orthonormal, the compressed matrix is the orthogonal direct sum

`[[0,1],[1,0]] direct_sum [[0,1],[1,0]] direct_sum [1]`,

so its nonzero spectrum is exactly `{1,-1,1,-1,1}`.

For

`F_m=2X<c,Y>+<v,Y>^2`

with `c perp v`, the compressed matrix is

`[[0,1],[1,0]] direct_sum [1]`,

so its spectrum is exactly `{1,-1,1}`.

Both are literal target-valid matrices.

## 3. Quotient Gram identity

For full-column-rank `V` and any `C`,

`G=[[V^TV,V^TC],[C^TV,C^TC]]`.

The Schur complement of `V^TV` is

`C^TC-C^TV(V^TV)^(-1)V^TC=C^T P_(V^perp) C`,

hence

`det G=det(V^TV)det(C^T P_(V^perp)C)`.

## 4. Puncture determinant inequality

With `R=sum_(i in K)u_i u_i^T`, `0<=R<=I`, `tr R=theta<1`, and eigenvalues `r_j`,

`det(I-R)=prod_j(1-r_j)>=1-sum_j r_j=1-theta`.

The punctured leverage bound is

`ell_i=u_i^T(I-R)^(-1)u_i<=||u_i||^2/(1-theta)=p_i/(1-theta)`.

Since `sum_i ell_i=d`, two iid Pluecker bases obey

`P(S cap T != empty)<=sum_i ell_i^2<=dq/(1-theta)`,

and therefore

`rho_I det G_I >=[(1-theta-dq)/(1-theta)] (1-theta)det G
=(1-theta-dq)det G`.

## 5. Scaling

In the theorem certificate,

`det G` contains `r+h` squared coefficient scales and `prod|lambda_k|` contains `r` curvature scales. Under `A -> sA`, the bracket

`det G prod|lambda_k|`

scales as `|s|^(2(r+h)+r)=|s|^(3r+2h)` only if all frame columns were matrix coefficients of the same homogeneity, which they are not after writing `A_II=D+sum lambda_k v_kv_k^T`: the representation has a gauge freedom `v_k -> a_k v_k`, `lambda_k ->lambda_k/a_k^2`. The invariant theorem must therefore be checked under the canonical rescaling induced by the decomposition: `lambda_k ->s lambda_k`, hub couplings `c_a->s c_a`, while the normalized curvature vectors `v_k` remain fixed. Then `det G` scales as `|s|^(2h)` in the quotient hub directions and `prod|lambda_k|` as `|s|^r`, so the bracket scales as `|s|^(r+2h)` and the density bound scales exactly as `|s|^(-1)`, as required.

This also confirms why the quotient formulation with normalized curvature directions is the natural scale-invariant statement.
