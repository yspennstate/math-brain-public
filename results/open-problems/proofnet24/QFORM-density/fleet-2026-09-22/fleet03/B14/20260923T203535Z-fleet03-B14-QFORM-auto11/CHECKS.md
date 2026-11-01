# Checks for fleet03/B14 aggregate-row receiver run

Run: `20260923T203535Z-fleet03-B14-QFORM-auto11`.

## Constant algebra

Let `alpha=q-1`. If the derivative-half linear form has density cap `M`, the Riesz estimate gives

`E|S|^(-alpha) <= 2^alpha M^alpha/(1-alpha)`.

Hence

`||p_R||_q <= [2^(q-1)/(2-q)]^(1/q) M^((q-1)/q)`.

For `q=3/2`, this scalar prefactor is exactly

`[2^(1/2)/(1/2)]^(2/3)=2`.

Using the product-projection cap `M<=sqrt(2)/r` gives

`2 (sqrt(2)/r)^(1/3)=2^(7/6) r^(-1/3)`.

The partner-derived core constant is

`K=3^(4/3) 2^(8/9) |h|^(-4/9)|gamma|^(-2/9)`.

Thus the aggregate-row branch is

`3^(4/3) 2^(37/18) r^(-1/3)|h|^(-4/9)|gamma|^(-2/9)`.

Numerically at `r=|h|=|gamma|=1`:

`3^(4/3) 2^(37/18)=17.98645406618923...`.

For the diffuse-star stress family, `|h|=2^(-1/2)`, so the additional factor is `2^(2/9)` and

`3^(4/3) 2^(41/18)=20.98172098721166...`.

## Spectral check for the stress family

The core deterministic coefficient vectors

`l=(1,1,1,1)/2`, `v=(1,1,-1,-1)/2`

satisfy `||l||=||v||=1` and `l·v=0`. In the deterministic basis `(e0,l,v)`, the core matrix is

`[[0,1,0],[1,0,0],[0,0,1/2]]`,

with spectrum `{1,-1,1/2}`.

The receiver star has center-to-leaf coefficient vector

`c=m^(-1/2)(1,...,1)`, `||c||_2=1`,

and matrix `[[0,c^T],[c,0]]`, whose only nonzero eigenvalues are `+||c||_2=1` and `-||c||_2=-1`.

Because the core and receiver use disjoint original coordinates, the full matrix is their direct sum and has nonzero spectrum `{1,-1,1/2,1,-1}`. Therefore it has four eigenvalues of modulus at least one for every `m`.

## Endpoint sanity checks

- If the selected receiver row has only a diagonal `d`, then `mathcal C<=1/|d|` and the theorem reduces exactly to the preceding sharp physical-diagonal Lq bound.
- If the selected diagonal vanishes but the off-diagonal row is diffuse with l2 norm one, the theorem remains finite while every individual coefficient may tend to zero.
- No step uses a pointwise oscillatory-decay estimate for an input marginal.
- No step conditions a projected variable and then assumes its conditional density remains capped.
- The fleet04/B14 r9 input is used only at its slice-Fourier equation (3.6); the corrected interval-to-Borel rough-hub endpoint is not used.
