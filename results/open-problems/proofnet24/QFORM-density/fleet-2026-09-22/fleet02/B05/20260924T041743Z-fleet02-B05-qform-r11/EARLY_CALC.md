# Early calculation — longitudinal-spike survivor after pair-star closure

Programme `QFORM-DENSITY-3EIG-20260922`; fleet02/B05. Full QFORM remains open.

Start from the exact-rank-three heavy-null Witt form of fleet01/B05. The heavy literal coordinate is `H=X_i`, the normalized residual Parseval rows are

`g_j=(xi_j,y_j,z_j)`, `sum_j g_j g_j^T=I_3`,

and, after the partner fleet03/B05 r39 theorem has paid every transverse-heavy row, every remaining normalized-heavy row belongs to

`S={j: ||g_j||^2>1/2, q_j:=y_j^2+z_j^2<1/4}`.

Then `xi_j^2>1/4` for every `j in S`, so `|S|<=3` because `sum_j xi_j^2=1`.

Let `K=S^c`, and restrict the transverse coefficient vectors to K:

`v=(y_k)_(k in K)`, `w=(z_k)_(k in K)`.

Their Gram matrix is

`T_K=[[||v||^2,<v,w>],[<v,w>,||w||^2]] = I_2-sum_(j in S) (y_j,z_j)^T(y_j,z_j)`.

Since each `q_j<1/4` and `|S|<=3`,

`lambda_min(T_K) >= 1-sum_(j in S)q_j >1/4`,

hence

`det T_K>1/16`.

Thus the pair of literal-product projections `(V_K,W_K)=(v.X_K,w.X_K)` has an honest joint-density cap at most

`2/sqrt(det T_K)<8`

by the two-dimensional product-projection bound. This survives conditioning all spike coordinates because K is source-disjoint from S.

Now restrict the longitudinal coefficient vector to K, `u=(xi_k)_(k in K)`, and make the deterministic coefficient-space regression

`u = r v+s w+p`, with `p perpendicular span{v,w}`.

After conditioning the at-most-three literal spike coordinates, the exact Witt form becomes

`Q=2a H V_K+2a kappa V_K P + A V_K^2+2B V_K W_K+delta W_K^2+affine`,

where `P=p.X_K`. No probabilistic independence is asserted among `P,V_K,W_K`; the only genuine independence retained is `H independent X_K`.

The exact endpoint `p=0` is already paid: then the form depends only on the independent hub H and the pair `(V_K,W_K)` of joint-density cap `<8`. Scaling `H` to `aH`, the proved theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` gives

`||p_Q||_(infinity,ess) <= C_* (8/|a|)^(2/3)|delta|^(-1/3)
                         =4 C_* (a^2|delta|)^(-1/3)`

with `C_*=7.761982175235...`. In the target heavy-null chamber the exact star identity is `a^2|delta|=c Delta_3>=1/2`, so

`||p_Q||_(infinity,ess) < 4 C_* 2^(1/3) <39.122`.

Therefore, after the fresh pair-star closure, the surviving longitudinal-spike obstruction has been reduced to one scalar coefficient-space defect `eta=||p||>0`; the endpoint `eta=0` is uniformly paid while the transverse pair remains quantitatively nondegenerate. The next analytic debt is a punctured receiver uniform as `kappa*eta ->0` which keeps P in the same K product bank rather than deleting it as a small random perturbation.
