# account03/B03 r42 checks

Run: `20260923T232613Z-account03-B03-QFORM-r42`

## A. Rank-one endpoint algebra

Assume `H=a uu^T`, `K=b vv^T` in `R^2`, with `u,v` unit and `Delta=|det(u,v)|`. Then

`P_+=(H+K)/2`, `P_-=(H-K)/2`.

For rank-one sums in dimension two,

`det(a uu^T+b vv^T)=ab Delta^2`,
`det(a uu^T-b vv^T)=-ab Delta^2`.

Therefore

`det P_+=ab Delta^2/4`,
`det P_-=-ab Delta^2/4`,
`D=|det P_+|=|det P_-|=|ab|Delta^2/4`.

If `u` and `v` were parallel, both `P_+` and `P_-` would have rank at most one; invertibility forces `Delta>0`.

## B. Planar density cap under the physical-bank transform

The map `x -> (u^T x,v^T x)` has absolute determinant `Delta`. The original two-coordinate product density is at most one. Therefore the transformed joint density obeys

`rho_Z(z)<=Delta^(-1)`

without asserting independence of `Z_1,Z_2`. The same holds for the independent copy bank `W`.

## C. Slice Hausdorff-Young constant

For a slice `0<=g<=M` of mass `m`, under `x -> x^2`,

`h(y)=[g(sqrt y)+g(-sqrt y)]/(2sqrt y)`.

Then

`int h^(3/2)
 <=int g(x)^(3/2)|x|^(-1/2)dx
 <=M^(1/2) int g(x)|x|^(-1/2)dx`.

The cap/mass rearrangement is the centered interval at height `M`:

`int g(x)|x|^(-1/2)dx
 <=M int_{-m/(2M)}^{m/(2M)} |x|^(-1/2)dx
 =2sqrt(2Mm)`.

Hence

`int h^(3/2)<=2sqrt(2) M sqrt(m)`.

Hausdorff-Young for `hat h(t)=int e^(ity)h(y)dy` gives

`||hat h||_3 <=(2pi)^(1/3)||h||_(3/2)`.

Thus

`int |hat h(t)|^3dt
 <=2pi [2sqrt(2)M sqrt(m)]^2
 =16pi M^2 m`.

After frequency scaling by `a`,

`int |A_t(z_2)|^3dt <=16pi M^2m(z_2)/|a|`.

## D. `F_Z` energy

With `F_Z(t)=int|A_t(z_2)|^2 dz_2`, and `int|A_t(z_2)|dz_2<=1`, Cauchy-Schwarz in the form

`(int q^2)^2 <=(int q)(int q^3)`

gives

`F_Z(t)^2 <=int|A_t(z_2)|^3 dz_2`.

Therefore

`int F_Z(t)^2dt <=16pi M_Z^2/|a|`,
`||F_Z||_2 <=4sqrt(pi)M_Z/sqrt(|a|)`.

Likewise for `W`.

## E. Rank-one bilinear Plancherel

For

`(L_t f)(z)=int exp(i2btzw)f(w)dw=hat f(2btz)`,

Plancherel gives

`||L_t f||_2^2
 =(2|bt|)^(-1)||hat f||_2^2
 =pi/(|bt|)||f||_2^2`.

Hence

`|phi(t)|<=sqrt(pi/(|bt|))sqrt(F_Z(t)F_W(t))`.

Also

`int F_ZF_W <=||F_Z||_2||F_W||_2
 <=16pi M_ZM_W/|a|`.

## F. One-copy weighted integral optimization

For split `T_0=x^2`,

central `<=4x`.

Tail:

`<=sqrt(pi/|b|)(2/T_0)^(1/2)(int F_ZF_W)^(1/2)`

`<=4pi sqrt(2)(M_ZM_W)^(1/2)|ab|^(-1/2)x^(-1)`.

Set

`C=4pi sqrt(2)(M_ZM_W)^(1/2)|ab|^(-1/2)`.

Minimize `4x+C/x`: at `x^2=C/4`, minimum `4sqrt(C)`, equal to

`2^(13/4)sqrt(pi)(M_ZM_W)^(1/4)|ab|^(-1/4)`.

Divide by `sqrt(2pi)` via the Riesz identity to obtain

`2^(11/4)(M_ZM_W)^(1/4)|ab|^(-1/4)`.

At the conjugate endpoint,

`(M_ZM_W)^(1/4)|ab|^(-1/4)
 <=Delta^(-1/2)|ab|^(-1/4)
 =(4D)^(-1/4)=2^(-1/2)D^(-1/4)`.

Therefore the half-Riesz constant is

`2^(9/4)=4.756828460010884...`.

The weighted one-copy Fourier constant is

`2^(11/4)sqrt(pi)=11.92360071543272...`.

## G. Whole-copy weighted integral optimization

From the squared bilinear bound,

`int |t|^(-1/2)|phi(t)|^2dt
 <=4sqrt(T_0)+16pi^2M_ZM_W|ab|^(-1)T_0^(-3/2)`.

Set `x=sqrt(T_0)` and `B=16pi^2M_ZM_W/|ab|`. Minimize

`4x+B/x^3`.

Derivative gives `x^4=3B/4`, so the minimum is

`(16/3)(3B/4)^(1/4)
 =16sqrt(2)3^(-3/4)sqrt(pi)(M_ZM_W)^(1/4)|ab|^(-1/4)`.

After endpoint substitution `(4D)^(-1/4)`, this is

`16 3^(-3/4)sqrt(pi)D^(-1/4)
 =12.440962412449712...D^(-1/4)`.

For an independent whole copy `T'`, `|phi_T|^2=phi_{T-T'}`. Dividing by `sqrt(2pi)` gives

`8sqrt(2)3^(-3/4)D^(-1/4)
 =4.963225915211198...D^(-1/4)`.

No independence of `X-X'` and `X+X'` is invoked.

## H. Independent-square receiver

For a cap-one scalar `Y`, the translated square `d(Y+h)^2` has density envelope

`g(w)<=|d|^(-1/2)|w|^(-1/2)`

on the appropriate half-line. Therefore convolution/conditioning against `S` gives

`||p_(d(Y+h)^2+S)||_infinity
 <=|d|^(-1/2) sup_s E|S-s|^(-1/2)`.

This yields

`2^(9/4)|d|^(-1/2)D^(-1/4)`.

Continuity is not inferred.

## I. Partner splice

account04/B03 proves

`E|R_--s|^(-1/4)|R_+-t|^(-1/4)
 <=sqrt(B(P_-)B(P_+))`,

with `B(P)<=128|detP|^(-1/4)`. Since both determinant magnitudes equal `D`,

`<=128D^(-1/4)`.

On the event `|R_--s|<=epsilon^2`, `|R_+-t|<=epsilon^2`, the integrand is at least `epsilon^(-1)`, hence

`P(event)<=128D^(-1/4)epsilon`.

## J. Four-coordinate determinant cross-check

For `M=[[H,K],[K,H]]`, the orthogonal sum/difference block diagonalization gives

`det M=det(H+K)det(H-K)`.

Since `H+K=2P_+` and `H-K=2P_-`,

`det M=16 detP_+ detP_-`.

The cited physical-four-determinant receiver therefore gives

`||p_S||_infinity <93*(16|detP_+detP_-|)^(-1/4)
 =(93/2)|detP_+detP_-|^(-1/4)`.

This is a source-scoped cross-check, not a full-target structural extraction.

## K. Correction and privacy checks

- `QFORM-RANK1-SAMEBANK-HALFRIESZ-FALSE-v1` is explicitly respected: the proof requires a transverse square direction and does not claim arbitrary rank-one same-bank half-Riesz control.
- No pointwise law-uniform scalar Fresnel decay is used.
- No post-rotation independence is used; transformed coordinates within each bank are allowed to be dependent.
- No conditional cap for conjugate `U,V` is used.
- No moment, compact-support, connected-support, Gaussian or log-concavity assumption is introduced.
- Explicit changed-file allowlist reviewed manually: this `REPORT.md` and `CHECKS.md` only. They contain mathematical statements and private-repository source pins, no credentials/tokens/account secrets or unrelated personal/company/trading material. No installation or external secret-scanner dependency was invoked.

`QFORM_B03_R42_CHECK_PASS`
