# Checks — QFORM quantile-gauge zero-loss localization

Run: `20260924T060127Z-account03-B14-QFORM-auto11`.

## 1. Quantile facts

For fixed `p in (0,1)` and any probability law on `R`,

`q_p=inf{x:F(x)>=p}`

is finite because `F(x)->0` as `x->-infinity` and `F(x)->1` as `x->+infinity`. For every deterministic `a`, the shifted CDF is `F_a(x)=F(x-a)`, hence

`q_p(X+a)=q_p(X)+a`.

Thus `Y=X-q_p(X)` satisfies `q_p(Y)=0` exactly. Translation preserves the one-dimensional density cap and independence.

## 2. Polynomial recentering identity

For symmetric `A_k`, vectors `a,b`, scalar `c`,

`(y+a)^T A_k(y+a)+b^T(y+a)+c`

`=y^T A_k y+(2A_k a+b)^T y + a^T A_k a+b^T a+c`.

Therefore recentering a smooth compact approximation at its own quantile does not change its output law once the affine coefficients are updated. No bound on `a` is required.

## 3. Varying-polynomial convergence without moments

Let `A_k=(1+eta_k)A`, `eta_k->0`, and

`F_k(z)=z^T A_k z+b^Tz+c`, `F(z)=z^TAz+b^Tz+c`.

For every finite `z`, `F_k(z)->F(z)`. Since a real random vector is finite almost surely,

`F_k(Z)->F(Z)` almost surely

with no expectation or moment assumption.

If `law(W_k)` tends to `law(Z)` in total variation, then for the same measurable map `F_k`,

`d_TV(law(F_k(W_k)),law(F_k(Z))) <= d_TV(law(W_k),law(Z))`.

Combining this with `F_k(Z)=>F(Z)` gives `F_k(W_k)=>F(Z)`.

For any bounded open interval `I`, Portmanteau yields

`P(F(Z) in I)<=liminf_k P(F_k(W_k) in I)`.

Because each ratio is bounded above by the corresponding interval-height functional,

`H(law(F(Z))) <= liminf_k H(law(F_k(W_k)))`.

This is the exact no-loss passage used in the report.

## 4. Reverse affine homogenization check

For strict-margin `A` and arbitrary `b`, let `V_T=T+U`, `U~Unif[0,1]`, and

`B_T=[[A,b/(2T)],[b^T/(2T),0]]`.

The perturbation from `diag(A,0)` has operator norm

`||b||_2/(2T)`.

If `delta=s_3(A)-1>0`, choose `T>||b||_2/(2delta)`. Every positive target eigenvalue `>1+delta` remains `>1`; every negative target eigenvalue `<-1-delta` remains `<-1`. Hence `B_T` has at least three eigenvalues of modulus `>1`.

The homogeneous output is exactly

`(Y,V_T)^T B_T(Y,V_T)=Y^TAY+(V_T/T)b^TY`,

and `V_T/T->1` uniformly in `U`. Therefore it converges almost surely to `Y^TAY+b^TY`, without moments.

## 5. Designated partner constant

For

`B_*=I_3-(2/3)11^T`,

`1` is an eigenvalue on the two-dimensional orthogonal complement of `1`, while on `span{1}` the eigenvalue is

`1-(2/3)*3=-1`.

Hence

`spec(B_*)={1,1,-1}`, `sigma_min_abs(B_*)=1`.

The account04/B14 r10 theorem therefore gives

`6 sqrt(pi)=10.634723105433096...`.

The quantile recentering changes only deterministic affine coefficients; the physical principal block remains `B_*`, so its `sigma` is unchanged.

## 6. Source match / non-duplication check

Visible-corpus searches for

- `median centering affine homogenization`, and
- `quantile gauge p-quantile centered affine`

returned no exact matching theorem.

The result deliberately cites and reuses two nearby existing mechanisms instead of relabelling them:

1. account03/B14 `QFORM-EXACT-CONSTANT-COMPACT-AFFINE-LOCALIZATION-v1` for cap-preserving compactification and affine homogenization;
2. account04/B14 r10 for the physical-three-block inequality.

The new statement is the exact fixed-quantile gauge equality for the optimal universal constant and its smooth-compact strict-margin affine normal form.

## 7. Scope checks

No step assumes moments, common support radius, connected support, finite fragment count, Gaussianity, log-concavity, identical laws, spectral-coordinate independence, or pointwise van-der-Corput decay.

The theorem concerns the interval-height / essential-density constant. It does not pass continuity through the limiting approximation and does not change the official `OPEN` status of full-target continuity.
