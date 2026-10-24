# Early substantive calculation — pair-log + rank-two Schur fractional smoothing

Run `20260924T044522Z-account01-B19-QFORM-auto11-r12`.

Source-pinned inputs:

- account02/B19 `QFORM-PHYSICAL-R2-FRACTIONAL-SMOOTHING-v1`, `math-open-problems@f4d95bc33caf8db11888cceb817c005484f67d31`;
- completed physical indefinite-pair logarithmic transducer, `math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`.

Let two literal original coordinates form an invertible indefinite principal pair `B`, with

`D=|det B|`, `kappa=sigma_min(B)`.

After completing those two variables, write the untouched original-coordinate remainder as `R`. The pair-log proof gives, for every cutoff `r>0`,

`p_Q(t) <= 2 sqrt(2)/r + D^(-1/2) E log_+(2 r^2/(kappa |t-R|))`.          (1)

Suppose more generally that

`sup_s P(|R-s|<rho) <= H rho^alpha`, `alpha>0`.                              (2)

Layer cake gives, with `a=2r^2/kappa`,

`E log_+(a/|t-R|)`
` = integral_0^infty P(|t-R|<a exp(-v)) dv`
` <= H a^alpha / alpha`.                                                     (3)

Therefore

`p_Q(t) <= A r^(-1) + B0 r^(2alpha)`,                                       (4)

where

`A=2 sqrt(2)`,
`B0=(H/alpha) 2^alpha D^(-1/2) kappa^(-alpha)`.

The exact optimizer satisfies `r^(2alpha+1)=A/(2alpha B0)`, hence

`||p_Q||_infinity`
` <= (2alpha+1) B0^(1/(2alpha+1)) [A/(2alpha)]^(2alpha/(2alpha+1))`.           (5)

At `alpha=1/4`, this simplifies exactly to

`||p_Q||_infinity <= 3*2^(4/3) H^(2/3) D^(-1/3) kappa^(-1/6)`.               (6)

Now let the Schur remainder coefficient matrix be `S`, and suppose disjoint original-coordinate banks `I,J` in the remainder satisfy

`Z2=e_2(S[I,J]^T S[I,J])>0`.

The account02/B19 theorem, applied to the ACTUAL remainder including its affine term and all self-curvature, gives

`H=H_(1/4)(R) <= C_R2 Z2^(-1/16)`,
`C_R2=3.929131770449763487...`.                                               (7)

Substitution into (6) yields

`boxed: ||p_Q||_infinity <= C_* D^(-1/3) kappa^(-1/6) Z2^(-1/24)`,           (8)

with

`C_*=3*2^(4/3)*C_R2^(2/3)=18.823150365416575...`.                            (9)

Since `Z2 >= (sigma_1 sigma_2)^2` for the two largest singular values of the Schur cross block,

`||p_Q||_infinity <=18.823151 D^(-1/3) kappa^(-1/6) (sigma_1 sigma_2)^(-1/12)`. (10)

No coefficient tail is deleted, no random coordinate is rotated, and the pair shifts may depend arbitrarily on the remainder variables. Continuity is not asserted by this receiver.

The newest account02/B19 exact-rank-three stress family at `c5347df59a4adcea406d9fa8ca0c88186670d731` is a sharp boundary check rather than a contradiction: if the full matrix has rank three and `B` is invertible, Schur rank additivity gives `rank S=1`, hence every such `Z2` is exactly zero. Thus (8) does not incorrectly scalarize the partner's logarithmically singular curved two-bank partial law; that family still requires its third resource to be spent jointly.
