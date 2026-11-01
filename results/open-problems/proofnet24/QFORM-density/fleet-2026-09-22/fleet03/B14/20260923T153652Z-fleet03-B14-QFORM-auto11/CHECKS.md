# Checks for fleet03/B14 auto11

Run: `20260923T153652Z-fleet03-B14-QFORM-auto11`

## Constant arithmetic

For the cap-only half-Riesz bound, if `p<=M`, the centered interval of length `1/M` gives

`M * integral_{-1/(2M)}^{1/(2M)} |x|^{-1/2} dx = 2 sqrt(2) M^(1/2)`.

For `Y=2(C^T u)^T Z+delta` with `||C^T u||=sigma`, the product-projection cap is

`M <= sqrt(2)/(2 sigma)=1/(sqrt(2) sigma)`.

Hence

`E ||2CZ+d||^(-1/2) <= 2 sqrt(2) M^(1/2) = 2^(5/4) sigma^(-1/2)`.

The receiver projection has

`||p_{b^T W}||_2 <= (sqrt(2)/||b||)^(1/2)=2^(1/4)||b||^(-1/2)`.

Multiplying gives the abstract factor

`2^(1/4) * 2^(5/4) = 2^(3/2)`.

For the partner slice,

`A = 4 sqrt(pi)/( |h| sqrt(|gamma|) )`.

If `C0=sqrt(pi A)`, then

`int_R min(1,C0^2 |t|^(-3/2)) dt = 6 C0^(4/3)`.

Therefore

`||p_T||_2^2 <= (1/(2pi)) * 6 (pi A)^(2/3) = (3/pi)(pi A)^(2/3)`,

and

`||p_T||_2 <= sqrt(3/pi)(pi A)^(1/3) = 2^(2/3) sqrt(3) |h|^(-1/3)|gamma|^(-1/6)`.

Combining with the receiver factor gives

`2^(3/2+2/3) sqrt(3) = 2^(13/6) sqrt(3)`.

At `|h|>=1/sqrt(2)`, the extra factor is at most `2^(1/6)`, so the unit-scale constant is

`2^(14/6) sqrt(3) = 2^(7/3) sqrt(3) = 8.72898908777377...`.

## Structural sanity checks

1. All projections are taken in original independent coordinates; no probabilistic rotation is used.
2. The driver singularity is averaged against the whole law before any fragment normalization.
3. The hub phase is allowed to be arbitrary measurable because it is unimodular in the Plancherel step.
4. No moment, compact support, connected support, diameter, or fragment-count assumption appears.
5. The result is only a structured branch theorem; no claim is made that `s_3(A)>=1` forces the receiver decomposition.
6. Only essential boundedness is proved; continuity is not inferred.
