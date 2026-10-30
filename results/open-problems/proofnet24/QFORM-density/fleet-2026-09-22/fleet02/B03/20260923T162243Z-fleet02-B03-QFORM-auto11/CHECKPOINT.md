# fleet02/B03 early checkpoint — scalar/pair weak-kernel interpolation

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T162243Z-fleet02-B03-QFORM-auto11`  
Assignment: Decoupled time integral.  
Status at checkpoint: new supporting calculation proved; full target open.

Fresh control includes owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`; the full conjecture remains open. The newest completed projected-crossing theorem at `math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a` and newest designated-partner fleet03/B03 r36 are being consumed at their exact gates. No independence after a spectral rotation and no conditional density supremum are used.

## New weak-kernel calculation

Let `X` have density `f<=1`, let `(C,D)` be independent of `X` with arbitrary joint density `g<=M`, and let `a` be arbitrary and `beta*gamma!=0`. For

`Q=a X^2+2 beta X C+gamma D^2`

(and, by deterministic translation, arbitrary affine terms), I obtain

`||p_Q||_infinity <= 3(8 sqrt(2) M)^(2/3) |beta^2 gamma|^(-1/3)`.

Normalize `beta=1`, `gamma=+/-1`, so the pair cap becomes `M'=M/(|beta|sqrt(|gamma|))`. For fixed output level `t`, the scalar pushforward kernel is

`K_t(c,d)=sum_{x: a x^2+2cx+sign(gamma)d^2=t} f(x)/(2|a x+c|)`.

If `K_t(c,d)>s`, one of the at most two roots satisfies `f(x)>s|u|`, where `u=ax+c`. Parameterize such points by `(x,u)`, so `c=u-ax` and

`sign(gamma)d^2=t+a x^2-2ux`.

Each of the two square-root branches has Jacobian `|u|/|d|`. For `m=f(x)/s`, changing variable from `u` to `y=t+a x^2-2ux` gives

`int_{|u|<m, sign(gamma)y>0} |u|/sqrt(|y|) du <= 2 m^(3/2)/sqrt(|x|)`.

Therefore

`|{(c,d):K_t(c,d)>s}| <= 4 s^(-3/2) int f(x)^(3/2)|x|^(-1/2) dx`.

Since `f^(3/2)<=f`, the cap-one bathtub bound gives

`int f(x)^(3/2)|x|^(-1/2) dx <= int_{-1/2}^{1/2}|x|^(-1/2)dx=2sqrt(2)`.

Thus

`|{K_t>s}| <= 8sqrt(2) s^(-3/2)`.

Layer cake against the pair density yields

`p_Q(t) <= int_0^infinity min(1,8sqrt(2)M' s^(-3/2)) ds =3(8sqrt(2)M')^(2/3)`.

This bound is independent of the scalar self-curvature `a`; it pays a genuine near-null interpolation whenever the dependent pair curvature is rank one and the scalar couples to its null direction.

## Immediate target-valid corridor

Let `Y` have independent cap-one coordinates and let `(v,w)` be orthonormal. Put `C=v.Y`, `D=w.Y`; the proved two-dimensional product-projection density cap is `M<=2`. Let `X_0` be another original independent cap-one coordinate and, for `|a|<=1`,

`Q_a=aX_0^2+4X_0 C+D^2`.

The nonzero matrix in the orthonormal grouped basis is

`B_a=[[a,2,0],[2,0,0],[0,0,1]]`.

Its eigenvalues are `1` and `(a +/- sqrt(a^2+16))/2`, so all three have modulus at least one for `|a|<=1`. Hence this is an actual owner-target family in arbitrary ambient dimension, and the new estimate gives

`||p_{Q_a}||_infinity <= 3(16sqrt(2))^(2/3)4^(-1/3)=15.1190525988...`,

uniformly through the nonzero near-null pivot `a->0`.

A limitation/counterexample and the required partner/projected-crossing applications will be included in the final report.
