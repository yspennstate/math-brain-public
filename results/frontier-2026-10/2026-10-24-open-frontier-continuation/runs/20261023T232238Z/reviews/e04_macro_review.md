# Independent audit: nonorthogonal macroscopic compactness and output action

**Disposition:** `MACRO_COMPACTNESS.md` passes this audit as a **subsequential characterization** for each fixed physical horizon `T`. Its claims stop before uniqueness of the marked endpoint inclusion, convergence of pre-step tangent kernels, or a universal width limit. I found no substantive gap in the energy bootstrap, output integration-by-parts identity, or the positive-semidefinite limiting **action**. The marked joint initialization from the earlier run remains an explicit dependency. This is an internal mathematical review, not an external novelty claim.

## Bootstrap over `N_m=O(L)` steps

Let `a=m^(1/alpha)`, `L=(log m)^(1/alpha)`, `h=gamma/L`, and `S_n=a^(-2)sum_i(W_i,n^2+||U_i,n||^2)`. The row update gives

`S_(n+1)<= [1+(gamma/a)||X||||r_n||]^2 S_n`.

The exact ReLU split of one output increment gives, with constants depending only on `X,gamma`,

`||r_(n+1)-r_n|| <= h [A S_n||r_n||+(B/a)S_n||r_n||^2]`.

On `S_0<=K, ||r_0||<=R`, choose a deterministic `R_*>2(R+1) exp(c K(T+1))` for a sufficiently large fixed `c` and bootstrap `||r_n||<=R_*`. Then `sum_(n<N_m)(gamma/a)||X||||r_n||=O_(R_*,T)(L/a)=o(1)`, so `S_n<=2K` for large `m`. The output bound and discrete Grönwall keep `||r_n||<R_*` (the quadratic term is absorbed since `R_*/a->0`). This closes without finite-width loss descent. Tightness of `S_0,r_0` removes localization. It also gives `max_n||r_(n+1)-r_n||=O_P(h)` and Lipschitz polygonal interpolations of `r`, hence a continuous subsequential residual limit. The held paths differ from those interpolations by `O_P(h)`.

The normalized row displacement is `O_P(L/a)` in `l^2`, uniformly through `T`; in particular

`sup_n a^(-2)sum_i|W_i,n^2-W_i,0^2|=O_P(L/a)`,
`sup_n||C_m,n-C_m,0||=O_P(L/a)`.

Since `max_i (W_i,0^2+||U_i,0||^2)^(1/2)/a<=S_0^(1/2)`, replacing `W_i,j/a` by `z_i,0=W_i,0/a` in the projected recursion costs at most `O_P(L^2/a)` uniformly in `i` and `n<=N_m`. This is unscaled preactivation error, so it also vanishes after division by `L`.

## Endpoint compactness and the threshold inclusion

For each retained marked endpoint `|z|>epsilon` with bounded original mark, set `q_i,m(t)=V_i,floor(t/h)/L` and use polygonal interpolation. Its increments are bounded by `h |z_i,0|||G||||r_n||+o_P(h)`, so finite collections are equi-Lipschitz and start at `V_i,0/L->0`. Along a joint subsequence their paths converge uniformly. The held binary gates `D(V_i,n)` are bounded in `L-infinity`, so a further weak-star subsequence yields diagonal coefficients `theta_i,j(t) in [0,1]`. Uniform convergence implies `theta_i,j=1` almost everywhere on `{q_i,j>0}` and `theta_i,j=0` almost everywhere on `{q_i,j<0}`. Strong convergence of `r_m` then passes the integrated endpoint recurrence to

`q_i'=z_i G diag(theta_i) r`, `q_i(0)=0`.

This is an inclusion, not a selection theorem. The original mark can affect which solution emerges from the collapsed initial value `q_i(0)=0`, as the earlier frozen two-input example demonstrates. Enumerating the countably many Poisson atoms and diagonalizing finite cutoffs is sufficient for this subsequential statement; no uniform path convergence over all atoms is needed.

## Uniform output identity and cutoff

The exact discrete integration-by-parts identity is

`f_n-f_0=(1/L)sum_i z_i,0[(V_i,n)_+-(V_i,0)_+]
          +h sum_(j<n) [a^(-2)sum_i h_i,n h_i,j^T]r_j`.

Here `h_i,j=(V_i,j)_+`. The cross Gram in brackets differs from `C_m,0=a^(-2)sum_i h_i,0 h_i,0^T` by `O_P(L/a)` uniformly in `j,n<=N_m`, by Cauchy-Schwarz and the normalized `l^2` row-displacement bound. Its accumulated error remains `O_P(L/a)` because `h sum_(j<n)||r_j||=O_P(1)` on a fixed horizon. Thus the claimed replacement by `C_m,0 h sum r_j` is uniform in `n`.

The endpoint term must be truncated using **square mass**, not a uniform row-error bound multiplied by the untruncated sum of `|z_i,0|`. For `M_m(epsilon)=a^(-2)sum_(|W_i,0|<=epsilon a)W_i,0^2`, ReLU Lipschitzness and the projected update give

`sup_(n<=N_m) (1/L)||sum_(small) z_i,0[(V_i,n)_+-(V_i,0)_+]||
 <= const_T sup_(j<=N_m) a^(-2)sum_(small)|W_i,0 W_i,j|
 <= const_T [M_m(epsilon)+O_P(L/a)]`.

The prior stable-tail estimate gives `limsup_m E M_m(epsilon)=O(epsilon^(2-alpha))`. Large `|z|` and large original marks are removed by occurrence probabilities. On every finite retained atom set, `L^(-1)[(V_i,n)_+-(V_i,0)_+]->(q_i(t))_+` uniformly. The Poisson limit obeys `sup_(t<=T)|z_i(q_i(t))_+|<=const_T z_i^2`, and `sum_i z_i^2<infinity` almost surely. These bounds yield, along the chosen joint subsequence,

`f(t)=F+C int_0^t r(s)ds+sum_(z_i,u_i) z_i(q_i(t))_+`, `r=y-f`.

The sum is absolutely and uniformly convergent on `[0,T]`. This identifies a subsequential output law but does not show that different subsequences choose the same endpoint paths or output.

## Positive-semidefinite limiting action

Every absolutely continuous scalar `q_j` has `q_j'=0` almost everywhere on its zero set. Hence `(q_j)_+'=theta_j q_j'` almost everywhere: off zero, `theta_j` is the binary sign, and on zero both sides vanish. For each atom, `q'=zG D(theta)r` therefore gives

`d[z(q)_+]/dt=z^2 D(theta)G D(theta)r` almost everywhere.

The bound by `const z^2||r||` and `sum z^2<infinity` justify differentiation through the atom sum. Consequently every subsequential limit has

`f'=[C+sum_i z_i^2 D(theta_i)G D(theta_i)]r` almost everywhere.

The displayed matrix is symmetric PSD (and at least `C`), so the **limiting** squared loss satisfies `d||r||^2/(2dt)<=-r^T C r`. This does not imply finite-step descent, convergence of the pre-step tangent Gram to this matrix, or a unique matrix representation across different weak gate selections. At an attracting face it is an action identity for the selected residual, compatible with the Schur-complement representative; it must not be called an average of binary tangent kernels.
