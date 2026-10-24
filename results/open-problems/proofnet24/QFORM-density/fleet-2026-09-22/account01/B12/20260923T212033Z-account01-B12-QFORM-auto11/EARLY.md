SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-23T21:20:33Z.
attacking: carrier-relative gain decomposition — isolate the only part of arbitrary signed added spectrum that can contract an original-coordinate square-energy carrier, while making orthogonal carrier action magnitude-free.

# Early checkpoint: carrier-relative gain identity

Status: supporting deterministic theorem proved below; full QFORM remains OPEN.

Let H be m original coordinates and let P_H denote the coordinate inclusion/projection. Put V=A_0 P_H and G_0=V^T V=(A_0^2)[H,H]. Assume G_0>0 on H. For an arbitrary symmetric addition S put D=S P_H and let

Pi=V G_0^{-1} V^T,
K=G_0^{-1} V^T D,
R=(I-Pi)D.

Then Pi is the orthogonal projector onto Ran(V), Pi D=V K, V^T R=0, and the exact identity is

((A_0+S)^2)[H,H]
=(I+K)^T G_0(I+K)+R^T R.                                    (E1)

Thus the entire carrier action R orthogonal to Ran(A_0 P_H) is automatically positive square energy and can be arbitrarily large; it cannot destroy any carrier mode.

Define the relative carrier gain

L=G_0^{1/2}(I+K)G_0^{-1/2}.

If at most r singular values of L are below alpha>0, equivalently s_{m-r}(L)>=alpha, then for every k with k+r<=m,

lambda_k(((A_0+S)^2)[H,H]) >= alpha^2 lambda_{k+r}(G_0).       (E2)

Proof: choose the right-singular bad projection Q of rank r. Then L^T L >= alpha^2(I-Q). Conjugating by G_0^{1/2} and using (E1) gives
G_1 >= alpha^2(G_0-G_0^{1/2}QG_0^{1/2}).
The subtracted matrix is PSD of rank at most r, hence rank-r eigenvalue interlacing gives (E2).

If a further symmetric F is added, only its local action is needed:

sqrt(lambda_k(((A_0+S+F)^2)[H,H]))
=s_k((A_0+S+F)P_H)
>=alpha sqrt(lambda_{k+r}(G_0))-||F P_H||_op.                  (E3)

For a spectral split E=S_h+W_h with S_h=sum_{|theta_a|>h} theta_a v_a v_a^T and W_h=sum_{|theta_a|<=h}..., ||W_h||_op<=h. Hence, after any extra symmetric T,

sqrt(lambda_k(((A_0+E+T)^2)[H,H]))
>=alpha sqrt(lambda_{k+r}(G_0))-h-||T P_H||_op,                (E4)

provided s_{m-r}(L_h)>=alpha for the large packet S_h. No sign, rank, or magnitude bound is imposed on S_h. The large packet is charged only through relative contraction of its aligned carrier action; its orthogonal carrier action is exactly free. The small packet is charged once by h, regardless of rank or signs.

This is not a probabilistic convolution statement and does not rotate the independent variables.
