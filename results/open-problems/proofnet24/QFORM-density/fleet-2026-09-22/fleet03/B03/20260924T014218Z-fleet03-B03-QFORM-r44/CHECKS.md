# fleet03/B03 r44 deterministic checks

Run: `20260924T014218Z-fleet03-B03-QFORM-r44`.

These checks verify only algebra/constants of the scoped theorem. They are not numerical evidence for the unrestricted conjecture.

## 1. Rank-two crossing normalization

The pinned exact-rank crossing theorem gives for rank two

`|phi(t)| <= min(1,K/|t|)`,

`K = pi sqrt(M_R M_C) p^(-1/2)`, `p=s_1s_2`.

For product cap-one banks, `M_R,M_C<=2`, hence

`K<=2pi p^(-1/2)`.

The squared envelope integrates exactly as

`2[ int_0^K 1 dt + K^2 int_K^infinity t^-2 dt ]`
`=2[K+K]=4K`.

Thus, with `2pi||p_S||_2^2=||phi||_2^2`,

`||p_S||_2^2 <= 4K/(2pi)=2 sqrt(M_RM_C)p^-1/2`,

and in the cap-two case

`||p_S||_2^2 <=4p^-1/2`.

## 2. Assigned weighted time integral

For the same envelope,

`J = int_R |t|^-1/2 |phi(t)|^2 dt`

is bounded by

`2[ int_0^K t^-1/2 dt + K^2 int_K^infinity t^-5/2 dt ]`
`=2[2sqrt(K)+(2/3)sqrt(K)]`
`=(16/3)sqrt(K)`.

Since

`int_R e^(itx)|t|^-1/2 dt = sqrt(2pi)|x|^-1/2`

in the regularized sense used throughout the QFORM package,

`E|S-S'|^-1/2 <= J/sqrt(2pi)`
`=(16/(3sqrt(2)))(M_RM_C)^(1/4)p^-1/4`.

For `M_R=M_C=2`, the factor `(M_RM_C)^(1/4)=sqrt(2)`, giving exactly

`E|S-S'|^-1/2 <=(16/3)p^-1/4`.

## 3. Quarter-potential optimization

Let `L=||p_S||_2`. For radius `R>0`,

`int_|u|<=R |u|^-1/4 p_S(a+u)du`
`<= L (int_|u|<=R |u|^-1/2 du)^(1/2)`
`=2 L R^(1/4)`.

The complement contributes at most `R^-1/4`. Setting `x=R^(1/4)` reduces the bound to

`2Lx+x^-1`.

Its minimizer is `x=(2L)^-1/2`, with minimum

`2sqrt(2L)`.

From

`L^2 <=2sqrt(M_RM_C)p^-1/2`

we obtain

`L <=sqrt(2)(M_RM_C)^(1/4)p^-1/4`

and hence

`H_1/4(S) <=2^(7/4)(M_RM_C)^(1/8)p^-1/8`.

At `M_R=M_C=2`, `(M_RM_C)^(1/8)=2^(1/4)`, so the constant is exactly `4`.

## 4. Live E2 threshold

For exact rank two,

`E_2(N)=s_1^2s_2^2=p^2`.

Therefore `E_2(N)>4/9` implies `p>2/3`. Substituting the endpoint `p=2/3` gives the conservative constants

- `4 p^-1/2 = 4sqrt(3/2) = 4.898979485566356`,
- `(16/3)sqrt(2pi) p^-1/4 = 14.794881018366613`,
- `(16/3)p^-1/4 = 5.902303571735048`,
- `4p^-1/8 = 4.2079580220345765`,
- partner collision coefficient `8p^-1/2 = 9.797958971132712`.

All inequalities in the report use strict `<` on this branch because the live hypothesis is `p>2/3`.

## 5. Hyperbola splice constant

The pinned coordinate-hyperbola peel uses

`kappa = sup_(y>0) log(1+y)/sqrt(y)`.

The stationary equation is

`y/(1+y) = (1/2)log(1+y)`.

Its positive maximizer is

`y*=3.9215536345676396`,

and

`kappa=0.8047423425494118`.

Multiplying the peel coefficient `2^(3/4)kappa` by the new residual quarter-potential constant `4` gives

`2^(11/4)kappa = 5.413639608421417`.

## 6. Scope checks

- No singular-vector random coordinate is declared independent. Singular frames are used only to invoke a joint projection-density/Plancherel theorem on each genuine independent source bank.
- Conditioning occurs only on the genuinely independent background/hub source group.
- The independent-copy identity is applied only to the whole scalar output after the joint rank-two crossing estimate is established.
- The result is `L^2`/fractional-potential control, not an `L^infinity` theorem for the entire rank-two branch.
- The designated partner's collision lemma is applied after the new `L^2` density bound; the corrected false two-square compiler is not used.

`QFORM_B03_R44_CHECK_PASS`
