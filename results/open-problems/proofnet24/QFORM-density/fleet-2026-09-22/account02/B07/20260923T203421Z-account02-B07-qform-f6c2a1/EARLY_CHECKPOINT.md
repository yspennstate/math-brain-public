SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-23T20:34:21Z.
attacking: the nonexact rank-two-interface tail — robust determinant-weighted coordinate transfer using the heavy E2 singular pair, then physical coordinate-core reduction without discarding the tail.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full QFORM remains OPEN.
Run: `20260923T203421Z-account02-B07-qform-f6c2a1`.

First unpaid implication: `QFORM-NONEXACT-R2-TAIL-ROBUST-TRANSFER-v1`.

Let `K=A[L,R]` be the physical E2 core from the current account03/B07 interface packet, with squared singular values `x_r`, left singular vectors `u_r`, and `Z=e_2(KK^T)>0`. In the genuinely two-heavy singular branch, the partner calculation gives indices `p,q` with

`x_p x_q > Z/3`.

For the physical row inclusion marginal `mu_i` of the full squared-2-minor law of `K`, exterior SVD gives

`mu_i = sum_{a<b} (x_a x_b/Z) [u_a(i)^2+u_b(i)^2]`,  and  `sum_i mu_i=2`.

Choose the physical heavy set `H={i:mu_i>1/6}`. Then `|H|<=11`. For `i notin H`, put `ell_i=u_p(i)^2+u_q(i)^2`; the spectral-pair weight exceeds `1/3`, so

`mu_i >= (x_p x_q/Z) ell_i > ell_i/3`,

hence `ell_i<1/2`. Delete row `i` and write hats for restricted vectors. Then

`||hat u_p wedge hat u_q||^2=1-ell_i>1/2`.

Let `c_i=A[L\{i},{i}]` and

`d_i=dist(c_i, span{hat u_p,hat u_q})`.

Move original coordinate `i` across the cut and consider the literal physical crossing

`B_i=A[L\{i}, R union {i}]=[K_hat_i,c_i]`.

Right-rotating only the coefficient columns of `K_hat_i` to its SVD basis does not alter `B_iB_i^T`. Cauchy-Binet then lets us retain the single transformed column triple consisting of the `p,q` singular columns and `c_i`. Therefore, with every extra singular direction and the full nonzero interface tail still present,

`e_3(B_iB_i^T)
 >= x_p x_q ||hat u_p wedge hat u_q wedge c_i||^2
 = x_p x_q (1-ell_i)d_i^2
 > (Z/6)d_i^2.`

Thus any nonheavy physical row with `d_i>=delta` creates genuine aggregate physical third volume

`e_3(B_iB_i^T)>Z delta^2/6`,

without selecting or inverting one minor and without deleting the higher-rank tail. The next step is to feed this exact inequality into the marginal-free physical-E3 Fourier receiver; if every nonheavy `d_i<delta`, symmetrize their common two-plane approximants and invoke the bounded-dimensional diagonal-plus-rank coordinate-core theorem.
