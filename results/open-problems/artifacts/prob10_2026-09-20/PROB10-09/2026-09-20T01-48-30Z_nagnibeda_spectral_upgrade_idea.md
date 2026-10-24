Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-09 idea before code — import sharp surface-group spectral radii into the nonbacktracking certificate

Frozen parent target: for iid **bond** percolation on every locally finite Cayley graph of every finitely generated nonamenable group, prove `p_c(G)<p_u(G)`. This note is an idea record, not source closure.

## Continuity and scope

The preceding R20/PROB10-09 report proved a quantitative `p_c<p_(2->2)<=p_u` certificate for every standard product `X_{g,h}=Cay(Gamma_g x Gamma_h,S_g union S_h)` of two closed-surface groups except `(g,h)=(2,2)`, and improved the frozen `X_{3,4}` gap to `>0.01716108096716552...`. It used the coarse Freiheitssatz adjacency bound `||A_{Gamma_g}|| <= 2 sqrt(4g-3)+2`.

The neighboring NM13-11 worker owns the distinct free-core/complement / `SL_3(Z)` subgroup route. This iteration stays on the standard surface-product route and does not reuse or overwrite that claim.

## New observation

Bartholdi's arXiv:math/0112108, Theorem 1.3, records Nagnibeda's rigorous upper bounds for the standard simple-random-walk Markov operators on the genus-2 and genus-3 surface groups:

`||M_2|| <= 0.662816`, `||M_3|| <= 0.552792`.

Since the standard degrees are 8 and 12, respectively, these are much sharper adjacency estimates than the coarse free-subgroup-plus-one-generator decomposition. For a conservative exact rational import, deliberately relax them to

`||M_2|| <= 663/1000`, `||M_3|| <= 553/1000`,

hence

`||A_{Gamma_2}|| <= 663/125 = 5.304`,
`||A_{Gamma_3}|| <= 1659/250 = 6.636`.

For Cartesian products, `A_{X_{g,h}}=A_g tensor I + I tensor A_h`, so the operator norm is at most the sum of factor norms. Feed the improved product norm into the already proved nonbacktracking polynomial transfer

`p_(2->2)(X) >= 1/beta(D,R)`, where `beta` is the larger root of `z^2-Rz+(D-1)=0`.

## Three genuinely different attacks compared

1. **External spectral-input upgrade (chosen).** Replace only the coarse adjacency norm by Nagnibeda's surface-group bounds. This should improve the frozen `X_{3,4}` `p_u-p_c` certificate without altering the existing exact `p_c<19/400` witness.

2. **Close the missing `(2,2)` pair by the same operator upgrade plus the old exact fiber witness (chosen as a second theorem).** In `X_{2,2}`, the embedded `T_6 square T_6` and radius-two fiber activation at `p=11/100` should give `p_c<11/100`, while the improved genus-2 spectral norm should make `1/beta>11/100`. This would extend the quantitative structural scope from all standard surface products except `(2,2)` to all `g,h>=2`.

3. **Try to defeat the method rather than improve it.** The previous report recorded that the *full* one-sided `T_6 square T_6` fiber recursion had critical comparison about `0.102686`, while the old coarse nonbacktracking lower threshold was only about `0.0858`, so no finite-depth refinement of that old pairing could close `(2,2)`. The spectral upgrade attacks exactly that obstruction rather than adding another depth. The separate nonproduct subgroup route is already owned by NM13-11 and is not duplicated.

## Exact claims to test

- For `X_{2,2}`, use conservative `R=2*(663/125)=1326/125`, `D=16`, `Q=15`. Prove exactly `5 Phi_6^(2)(11/100)>1` and, with `z=100/11`, `z^2-Rz+15>0` and `z^2>15`; this forces the larger nonbacktracking root `beta<z`, hence `p_c<11/100<1/beta<=p_u`.
- For frozen `X_{3,4}`, use `R=1659/250 + 2 + 2 sqrt(13)=2159/250+2 sqrt(13)`, `D=28`, and retain the prior exact `13 Phi_10^(2)(19/400)>1`. Prove `400/19>R` exactly, hence `beta<R<400/19` and `19/400<1/beta<=p_u`.

If either exact inequality fails, record the failure rather than weaken the source target.