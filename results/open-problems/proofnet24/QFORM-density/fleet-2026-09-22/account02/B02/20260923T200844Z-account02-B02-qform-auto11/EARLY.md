# account02/B02 early checkpoint — exact rank-one shared-hub Fourier operator

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN.

Consider three independent banks: a physical scalar hub `H` with density at most one, and two original-coordinate banks whose two-dimensional orthonormal projections are `Y=(Y1,Y2)` and `Z=(Z1,Z2)`. Let their projected densities be bounded by `M_Y,M_Z`. After absorbing arbitrary within-bank quadratic/affine phases into complex pushforward densities `a_t,b_t`, suppose the only inter-bank phase is

`2 H(alpha Y1+beta Z1)+2 sigma Y2 Z2`, with `alpha,beta,sigma !=0`.

Writing `g_t(h)` for the phase-twisted hub density, set

`k_t(s)=int g_t(h) exp(i 2 t h s) dh = hat(g_t)(2ts)`.

The characteristic-function integral is the `L2(R^2)` pairing with tensor-product kernel

`K_t(y,z)=k_t(alpha y1+beta z1) exp(i2t sigma y2 z2)`.

For `T1 f(y)=int k_t(alpha y+beta z)f(z)dz`, angular Fourier transform and Plancherel give

`||T1||_{2->2} <= |alpha beta|^(-1/2) ||hat(k_t)||_infinity`.

Since

`hat(k_t)(xi)=(pi/|t|) g_t(-xi/(2t))`, 

and `|g_t|<=f_H<=1`,

`||T1||_{2->2} <= pi |t|^(-1)|alpha beta|^(-1/2)`.

For `T2 f(y)=int exp(i2t sigma yz)f(z)dz`, Plancherel gives

`||T2||_{2->2}=(pi/(|t sigma|))^(1/2)`.

Hence

`|phi_Q(t)| <= sqrt(M_Y M_Z) pi^(3/2) |alpha beta sigma|^(-1/2)|t|^(-3/2)`.

For independent cap-one scalar coordinates, the two-dimensional projection theorem gives `M_Y,M_Z<=2`. Therefore

`|phi_Q(t)| <= min{1, 2 pi^(3/2) T^(-1/4)|t|^(-3/2)}`

whenever `T=(alpha beta sigma)^2`.

Exact integration yields

`int |phi_Q| <= 6 pi 2^(2/3) T^(-1/6)`

and

`||p_Q||_infinity <= 3*2^(2/3) T^(-1/6)=4.7622031559... T^(-1/6)`.

This checkpoint will be embedded in the final report only after the coefficient reduction from a literal original-coordinate zero-pivot rank-one crossing is proved. No rotation-created independence is used: only joint projected density caps and `L2` norms occur.