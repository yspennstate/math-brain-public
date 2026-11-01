# Deterministic checks for fleet01/B02 r48

No Monte Carlo or histogram is used.

## Constants

With `eta=1/19`, `eps=1/72`,

`delta=1/2-eps-sqrt(2eps)=23/72`,

because `sqrt(2/72)=1/6`.

Hence

`sigma0=delta-eta=23/72-1/19=365/1368=0.266812865497076...`.

The perturbative ridge leverage at `gamma=sigma0*s/sqrt(3)` is

`L=(1/sqrt(23)+72sqrt(3)/365)^2=0.30269718610555...<1/2`.

The rank-two ridge half-Riesz constant is

`C_R=3*2^(5/4)*3^(1/4)*e^(1/4)=12.057650280480967...`.

Thus

`C_2=C_R/sqrt(sigma0)=23.34314135471538...`.

At `s=1/4`,

`H_(1/2)<=2*C_2=46.68628270943076...`.

At `|a|>1/228`, the scalar-square peel gives

`||p_Q||_infinity < 2*C_2*sqrt(228)=704.9474097088915...`.

The residual physical-hub threshold follows from

`(1/76)^2/72 = 2*(1/912)^2`,

so if `S_jj^2+||S[j,j^c]||^2>(1/76)^2/72`, then at least one of `|S_jj|`, `||S[j,j^c]||` exceeds `1/912`.

The partner application gives

`201/sqrt(2)=142.128463018496...`.

## Weighted Fourier integration

If `beta>1/2` and

`|phi(t)|<=min(1,(t0/|t|)^beta)`,

then

`int_R |t|^(-1/2)|phi(t)|dt`

`=2[ int_0^t0 t^(-1/2)dt + t0^beta int_t0^infinity t^(-beta-1/2)dt ]`

`<=4 beta/(beta-1/2) t0^(1/2)`.

For `beta=theta/(2q)`,

`beta/(beta-1/2)=theta/(theta-q)`.

With `t0=L_q/(2gamma)D^(-1/(2theta))`, `log D>=theta`, and `L_q=pi e sqrt(2/q)`, multiplication by the Riesz constant `(2pi)^(-1/2)` simplifies to

`2^(5/4)e^(1/4)q^(-1/4)gamma^(-1/2)*theta/(theta-q)`.

## Schur congruence

For `A=[[a,b^T],[b,C]]`, `a!=0`, let `S=C-bb^T/a` and `u=b/a`. Then

`A=L^T diag(a,S)L`, `L=[[1,u^T],[0,I]]`.

If `||u||<=1`, then `||L||<=1+||u||<=2`. Consequently

`s_3(A)<=||L||^2 s_3(diag(a,S))`,

so under `s_3(A)>=1`,

`s_3(diag(a,S))>=1/4`.

Since the scalar block contributes at most one singular value, `s_2(S)>=1/4`.
