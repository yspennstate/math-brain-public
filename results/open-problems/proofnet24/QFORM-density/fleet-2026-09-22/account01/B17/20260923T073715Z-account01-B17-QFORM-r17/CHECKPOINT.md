# B17 checkpoint: anisotropic three-bank rotational Edgeworth penalty

Run `20260923T073715Z-account01-B17-QFORM-r17`. Status: supporting sharp-witness derivation; full QFORM open.

Take `J=diag(1,1,-1)`, any `O in O(3)`, physical bank directions `v_j=O e_j`, and bank sizes `m_j>=3`. Repeat the row `v_j/sqrt(m_j)` exactly `m_j` times. Then `R^T R=I_3`, hence `A=R J R^T` has nonzero spectrum exactly `{1,1,-1}`. With independent physical inputs `Unif[-1/2,1/2]`, put

`Y_j=m_j^(-1/2) sum_{k<=m_j} X_{jk}`, so `Q=Y^T (O^T J O)Y` and the `Y_j` are independent with variance `sigma^2=1/12`.

Use the source-proved weighted one-dimensional local Edgeworth expansion

`g_m(y)=gamma_sigma(y)[1-H4(y/sigma)/(20m)]+O(m^-2)(1+|y|)^-8`.

On the cone `z_1^2+z_2^2-z_3^2=0`, write `z=r(cos theta,sin theta,epsilon)` and `y=O^T z`. Set `u_j=O_{3j}^2`, so `u_j>=0`, `sum u_j=1`. If `a_j=(O^T(cos theta,sin theta,epsilon))_j`, then

`E a_j^2=(1+u_j)/2`,

`E a_j^4=3(1-u_j)^2/8+3u_j(1-u_j)+u_j^2=(3+18u_j-13u_j^2)/8`.

The Gaussian radial law on the cone has `E q^2=1/2`, `E q^4=3/4`, where `q=r/sigma`. Therefore

`E H4(q a_j)=3(19+2u_j-13u_j^2)/32`.

Consequently, with `m_*=min_j m_j`,

`p_Q(0)=3sqrt(2)[1-D_O(m_1,m_2,m_3)+O(m_*^-2)]`,

`D_O=(3/640) sum_j (19+2u_j-13u_j^2)/m_j`.

Every summand is positive on `[0,1]`. Writing `w_j=1/m_j`, `D_O` is concave in `u` on the simplex, so its minimum is attained at a vertex. At vertex `k`,

`D_k=(3/640)(19 sum_j w_j-11w_k)`.

Thus

`D_O >= (3/640)(19 sum_j 1/m_j-11 max_j 1/m_j) >= 3/(80m_*)`.

For equal banks `m_j=m`,

`D_O=(177-39 sum_j u_j^2)/(640m)=69/(320m)+(39/(640m))(1-sum_j u_j^2)`.

Hence the aligned physical orientation minimizes the first-order deficit; every genuine mixing of the minority-sign eigendirection causes an explicit extra loss. For the source rotation with `sum u_j^2=199/343`, this gives exactly `5295/21952`, reproducing its published coefficient.

Dependencies to verify before final publication: source weighted Edgeworth remainder and source-valid finite partner theorem. Continuity is only in this witness family, not the full target.
