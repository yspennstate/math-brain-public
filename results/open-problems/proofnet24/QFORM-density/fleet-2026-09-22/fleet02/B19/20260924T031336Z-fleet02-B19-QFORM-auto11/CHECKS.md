# fleet02/B19 auto11 deterministic checks

Run: `20260924T031336Z-fleet02-B19-QFORM-auto11`.

All displayed numerical constants were recomputed from the exact formulas in REPORT.md.

```text
gamma0 = 28159/(4194304*sqrt(2))
       = 0.0047472524288730601643570366841579542391828763888764

c_1/4 = 2^(3/4)*Gamma(3/8)/(2*sqrt(pi)*Gamma(1/8))
      = 0.14927036108294766127126394913894754810358693405039

C_phi = (2*e*pi^2)^(1/4)
      = 2.7064876876447046674939886080404695294264168450351

C_R2 = 16*c_1/4*(2*e*pi^2)^(1/8)
     = 3.9291317704497634871249193093253251298294614232702

C_R2 * gamma0^(-1/8)
     = 7.6690453023101717039638752035893386434898026333

[C_R2 * gamma0^(-1/8)] * 2^(-1/4)
     = 6.4488727031309629282582886936168994724823803625517

8*gamma0^(-1/2)
     = 116.10978591674266203844150593486818118264750074727
```

Algebraic checks:

1. k=2, q=2 in the source D'/BL formula gives

`E F^2 <= e^(2/2)(2pi)^2 2^(-2/2)|t|^-2 Z_2^-1/2
          =2e pi^2 |t|^-2 Z_2^-1/2`.

Together with `|phi|^2<=E F<=(E F^2)^(1/2)` this gives

`|phi| <= (2e pi^2)^(1/4)|t|^-1/2 Z_2^-1/8`.

2. Source Lemma 4.1 with `b=1/2` gives

`H_alpha <= c_alpha/[alpha(1/2-alpha)] * B^(2alpha)`.

For `alpha=1/4`, this is

`H_1/4 <=16 c_1/4 (2e pi^2)^(1/8) Z_2^-1/16`.

3. Since `Z_2=e_2(M^TM)>=sigma_1^2 sigma_2^2`,

`Z_2^-1/16 <= (sigma_1 sigma_2)^-1/8`.

4. For the exact-rank-two symmetric crossing, the four Fresnel eigenvectors are

`(u_1,+v_1)/sqrt2, (u_1,-v_1)/sqrt2,
 (u_2,+v_2)/sqrt2, (u_2,-v_2)/sqrt2`,

with eigenvalues `+sigma_1,-sigma_1,+sigma_2,-sigma_2`.
Their coefficient product has modulus `(sigma_1 sigma_2)^2=P^2`, so the r=4 Fresnel bound is

`|phi(t)| <= (4pi)^2 P^-1 |t|^-2`.

If `C=(4pi)^2/P`, then

`integral_R min(1,C|t|^-2) dt =4 sqrt(C)`,

and Fourier inversion gives

`||p||_infinity <=(1/(2pi))*4sqrt(C)=8P^-1/2`.

Terminal marker: `QFORM_B19_AUTO11_R2_FRACTIONAL_CHECK_PASS`.
