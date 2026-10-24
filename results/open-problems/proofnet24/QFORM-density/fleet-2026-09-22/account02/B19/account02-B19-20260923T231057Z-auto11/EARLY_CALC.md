# account02/B19 early calculation — aggregate E3 defect behind the D2 diffuse branch

Programme: `QFORM-DENSITY-3EIG-20260922`.

Let `T={t1,t2}` and `L` be disjoint ORIGINAL-coordinate banks and put `M=A[T,L]` (a `2 x |L|` physical cross block), `G=MM^T`, `S^2=det G>0`. Write `m_j` for the column of `M` at `j in L` and `ell_j=m_j^T G^{-1}m_j`.

For each `j`, put `I_j=L\{j}`, `P_j=M[:,I_j]^T`, `c_j=A[I_j,j]`, and

`d_j=dist(c_j,col(P_j))`.

Then the literal three-column cross block `[P_j,c_j]=A[I_j,T union {j}]` has

`E_3([P_j,c_j]) = det([P_j,c_j]^T[P_j,c_j]) = S^2(1-ell_j)d_j^2`.

Indeed `P_j^TP_j=G-m_jm_j^T`, whose determinant is `S^2(1-ell_j)` by the matrix determinant lemma, and the Gram determinant factors as `det(P_j^TP_j) dist(c_j,col(P_j))^2` (with both sides zero when `P_j` drops rank).

Define the aggregate defect

`Zagg=sum_j S^2(1-ell_j)d_j^2`.

Randomly split every light coordinate independently into `I` or `J` with probability `1/2`. For the physical cross block `N=A[I,T union J]`, restrict the Cauchy--Binet sum for `E_3(N)` to column triples `T union {j}`, `j in J`. Every squared `3x3` minor contributing to the `j`-th local defect survives exactly when `j in J` and its three row indices lie in `I`, probability `1/16`. Therefore

`E E_3(N) >= Zagg/16`,

so some physical split satisfies

`E_3(A[I,T union J]) >= Zagg/16`.

This avoids selecting one local third minor and therefore loses no factor depending on `|L|`.

In the diffuse D2 branch `max_j ell_j<=3/4`, the local defects also give a dimension-free common-plane rigidity estimate. Normalize `v_j=G^{-1/2}m_j`, so `sum_j v_jv_j^T=I_2`. Choose least-squares `y_j in R^2` with residuals `r_ij=A_ij-v_i^T y_j` for `i!=j`, so `sum_{i!=j}r_ij^2=d_j^2`. Put `D^2=sum_j d_j^2`.

Symmetry gives `e_ij:=v_i^Ty_j-v_j^Ty_i=r_ji-r_ij`. With `B=sum_i v_i y_i^T`, the Parseval identity yields exactly

`y_j-Bv_j=sum_{i!=j}v_i e_ij`,

hence `sum_j ||y_j-Bv_j||^2 <= 4D^2`. Also

`B-B^T=sum_i v_i(y_i-Bv_i)^T`,

so for `K=(B+B^T)/2`,

`sum_j ||y_j-Kv_j||^2 <=12D^2`.

Consequently, after choosing a physical diagonal `Delta`, there is a symmetric `K` and a zero-diagonal symmetric residual `E` such that

`A[L,L]=Delta+V^T K V+E`, `V=G^{-1/2}M`,

and

`||E||op <= ||E||F <= sqrt(26)D`.

Because `1-ell_j>=1/4`, `Zagg>=S^2 D^2/4`, hence

`||E||op <= 2 sqrt(26) sqrt(Zagg)/S`.

At the live B20 scale `S>S0=1/(480 sqrt(7626))`, if `Zagg<2^-60` then

`||E||op < 2 sqrt(26) 2^-30/S0 = 0.000398113072`.

This is coefficient geometry only; the nonzero residual may NOT be discarded as a small random quadratic perturbation.
