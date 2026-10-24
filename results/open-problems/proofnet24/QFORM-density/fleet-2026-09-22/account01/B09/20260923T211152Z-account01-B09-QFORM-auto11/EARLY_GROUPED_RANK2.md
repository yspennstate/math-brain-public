SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T21:11:52Z.
attacking: aggregate the partner 3x2 kernel-derivative receiver over an arbitrary disjoint physical right bank, using a two-dimensional orthogonal pushforward only as a total-variation bound and retaining arbitrary right-bank curvature.

# Early substantive checkpoint: fixed physical triple versus an arbitrary rank-two right bank

Let `L` be three ORIGINAL coordinates, `J` any disjoint original-coordinate bank, `P=A[L,L]`, and `C=A[L,J]`. Assume `rank C=2`. Put

`G=C C^T`, `Delta=sqrt(e_2(G))=s_1(C)s_2(C)>0`.

Let `n` be the unit vector spanning `ker C^T`, and set `a=P n`. The candidate grouped receiver is

`||p_Q||_inf <= C_G Delta^(-2/5)||a||^(-1/5)`,

with

`C_G = 2^(2/5) C_KD = 5*6^(3/5)/2^(7/10) = 9.0186131328...`,

where `C_KD=6.834830666...` is the completed account02/B09 3x2 kernel-derivative constant.

The only new analytic point is the arbitrary size of `J`. Choose an orthonormal `3x2` frame `E` spanning `n^perp`. Factor

`E^T C = S R^T`,

where `S=(E^T C C^T E)^(1/2)` is positive definite and `R` has two orthonormal columns. Then `det S=Delta`. In left coordinates `Y=nx+Eu`, set `r=S u`; the physical cross phase is exactly

`2 Y^T C Z = 2 r^T (R^T Z)`.

The left-fiber calculation from account02/B09 r14 is unchanged: the transformed left density is bounded by `Delta^(-1)`, its `r` marginal is bounded by `2/Delta`, and the moving scalar derivative is exactly `2(Pn)^T Y+beta`. Therefore its quantity `A0(t)` obeys the same `L^4_t` estimate as r14.

For the right bank, do NOT rotate and claim independence. Instead push the complex measure

`F_Z(z) exp(i t psi(z)) dz`

forward by the genuine orthonormal projection `v=R^T z`. Its total variation is dominated by the probability pushforward of `F_Z dz`. The two-dimensional projection-density theorem gives that probability density at most `2`; hence the complex pushforward density `b_t(v)` satisfies

`||b_t||_1<=1`, `||b_t||_inf<=2`, and therefore `||b_t||_2<=sqrt(2)`.

The r14 bilinear Plancherel bound thus gains only a factor `sqrt(2)`:

`|phi_Q(t)| <= sqrt(2) pi |t|^(-1) A0(t)`.

The r14 `L^4` tail optimization raises that factor to power `4/5`, giving `2^(2/5) C_KD` and the displayed `C_G`.

There is an exact aggregate one-overlap identity. If the columns of `C` are `c_j`, for each physical pair `R={r,s} subset J` define `w_R=c_r x c_s`. Then

`sum_R w_R w_R^T = adj(C C^T)`.

Consequently

`V_L := sum_R ||P w_R||^2 = tr(P^2 adj(G))`.

When `rank C=2`, `adj(G)=Delta^2 n n^T`, so

`V_L=Delta^2 ||P n||^2`.

Hence the grouped density bound can be written purely in aggregate physical-minor currency as

`||p_Q||_inf <= C_G [ e_2(G) V_L ]^(-1/10)`.

This aggregates all right pairs before reciprocal payment and directly addresses the source-valid family in account02/B09 r14 where `V_L` stays fixed while every individual 3x2 packet currency tends to zero.

Remaining work this run: write the end-to-end proof with arbitrary outside conditioning and affine terms; verify the compound identity numerically; combine with the completed no-marginal physical-D3 receiver to form a fixed-triple rank>=2 compiler; apply the designated partner theorem to an actual finite-m inequality; refresh live corrections before publication.
