SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T05:11:16Z.
attacking: the rank-two aggregate cross-bank near-range endpoint — pay the exact zero transverse-square case when the third source survives as a transverse hyperbolic coupling.

# Substantive checkpoint


Designated partner `account03/B19` proved at `yspennstate/math-open-problems@82773d6d0339c8867b76c777216b6c564939f2ae` that for an exact rank-two physical cross bank with singular values `s1,s2`, a three-dimensional source-bank self range, and nonzero transverse square curvature `lambda`,

`||p_Q||_inf < 12.01 |lambda|^(-1/4) (s1 s2)^(-3/8)`.

This checkpoint attacks its exact `lambda=0` boundary without perturbing coefficients.

Let `P=range(C)` and let `r` be a unit vector in the three-dimensional source self range perpendicular to `P`. Assume `r^T B r=0` but `d=PBr` has norm `delta>0`. In orthonormal projected variables `(z=(x,z2),y)` with the first axis of `P` parallel to `d`, the source self phase is

`F(z)+2 delta x y`,

up to affine terms lying in the same three-dimensional source subspace. The joint projected density `p(z,y)` has cap `K3=2 sqrt(2)`, its `z` marginal has cap `K2=2`, and the `x` marginal has cap `K1=sqrt(2)`.

For fixed `z`, let `m(z)=int p(z,y)dy` and

`F_t(z)=exp(i t F(z)) int p(z,y) exp(2 i t delta (x-x0)y)dy`.

Plancherel plus `||hat g||_inf<=||g||_1` gives

`int_R |F_t(z)|^3 dt <= [2 pi K3/(2 delta |x-x0|)] m(z)^2`.

Minkowski (`L_t^3 L_z^2 <= L_z^2 L_t^3`) and `m<=K2` reduce this to the one-dimensional weighted marginal integral

`int |x-x0|^(-2/3) h(x)dx`, `0<=h<=K1`, `int h=1`.

Layer cake/bathtub gives exactly

`sup_h int |x-x0|^(-2/3)h(x)dx = 6*2^(-1/3)K1^(2/3)=6`.

Hence

`|| ||F_t||_2 ||_(L_t^3) <= M delta^(-1/3)`,

`M=2^(2/3) pi^(1/3) sqrt(6)=5.6948057280966...`.

Rank-two bilinear Plancherel on the opposite bank gives

`|phi_Q(t)| <= pi sqrt(2) [|t| sqrt(s1 s2)]^(-1) ||F_t||_2`.

Hölder on `|t|>T` and `|phi|<=1` on `|t|<=T` yield

`int |phi_Q(t)|dt <= 2T + A delta^(-1/3)(s1s2)^(-1/2)T^(-1/3)`,

`A=8 sqrt(3) pi^(4/3)=63.7554200285204...`.

Optimizing gives the candidate endpoint bound

`||p_Q||_inf <= 4(4 sqrt(3)/3)^(3/4) delta^(-1/4)(s1s2)^(-3/8)`

with numerical constant `7.49349659500199 < 7.50`.

The remaining work is to formalize the projection/disintegration scope, preserve arbitrary same-bank curvature on the opposite bank and allowed affine terms, and splice this exact-null endpoint into the N3 proof graph without claiming perturbative stability for `0<|lambda|<<1`.
