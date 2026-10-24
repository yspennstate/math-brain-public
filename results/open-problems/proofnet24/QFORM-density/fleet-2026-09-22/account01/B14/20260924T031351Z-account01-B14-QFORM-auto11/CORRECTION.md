# Controlling correction to `REPORT.md`

The theorem, equations (2.1)--(5.3), the two-sided coherent-partition result, the translation corollary, the exact target family (4.1), and the bound

`||p_(2X(L+Z)+Y^2)||_infinity <= 5 pi^(-1/5)2^(2/5)=5.24749493498713...`

are unchanged.

One sentence after (4.6) was too broad about ambient extensions preserving **the same numerical constant**. Conditioning on arbitrary outside original coordinates can create a linear term `beta Y` in the retained square coordinate. Then

`Y^2+beta Y = (Y+beta/2)^2-beta^2/4`,

and the relevant Fresnel integral is over an arbitrary translated interval of length one. The source-valid uniform bound from the same elementary split/integration-by-parts argument is

`|int_a^(a+1) exp(it u^2)du| <= 4 |t|^(-1/2)`,

not the special endpoint-stationary constant `2` used for `a=0` in (4.4).

Therefore:

1. The sharp run-specific constant `5.24749493498713...` is claimed for the exact family (4.1), and for conditioned extensions whose affine terms preserve the aggregate slice certificate `A<=2`.
2. A completely arbitrary outside coupling to the retained `Y` coordinate is still zero-tax with respect to support geometry/translations, but using the uniform shifted-Fresnel certificate `A<=4` gives the safe ambient numerical bound

`5 pi^(-1/5)4^(2/5)=6.924111078456212...`.

This does not affect the localization theorem: its invariant is the aggregate certificate `A`, not a particular numerical value. The correction only narrows the sentence claiming that arbitrary ambient conditioning preserves the special `A=2` value.
