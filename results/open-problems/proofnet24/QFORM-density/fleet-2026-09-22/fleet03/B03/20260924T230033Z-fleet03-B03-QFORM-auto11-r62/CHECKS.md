# fleet03/B03 r62 checks

Source paper: `5ba2a4d6b689721601cce7ec7e22ffea9fa98f90`, blob `bbebd6f6c5a27e9f639186a305008ab43a481e70`.
Partner: `da1d4e5510082c67ee7b34bbe70fde2060451518`, blob `8573a0a8028b4c8703f3467fe0a5f65cca190217`.

gamma2 = (44-15 sqrt(2))/96 = 0.23736246421253723.
a_star = 2^(3/4) pi e / gamma2 = 60.50688695779367.
C_star = a_star/pi = 19.25994030087079.
I_minus at sigma=-1/2 = (16/3) sqrt(a_star) = 41.48595888463038.
Partner I_plus at alpha=1 = (8/3) pi^(3/2) = 14.848874658217888.
Independent-factor density constant = (2 pi)^(-1) sqrt(I_minus I_plus) = 3.95018530081809.
Diagonal-pivot coefficients: 4 sqrt(6)=9.797958971132712 and 38 sqrt(6)=93.08061022576076.
e*C_star=52.35394573706311.
Switch e^(-2)/C_star=0.007026775842627811, where 269 ell(1+log(1/ell))=11.2618793118>1.

Exact calculus:
for -1<sigma<1,
2 int_0^a t^sigma dt + 2 a^2 int_a^infty t^(sigma-2) dt
= 4 a^(1+sigma)/(1-sigma^2).
For p>=2, q=p/(p-1),
2 int_0^a 1 dt + 2 a^q int_a^infty t^(-q) dt = 2 a p.

Marker: QFORM_B03_R62_FULL3_LOG_SMALLBALL_CHECK_PASS.
