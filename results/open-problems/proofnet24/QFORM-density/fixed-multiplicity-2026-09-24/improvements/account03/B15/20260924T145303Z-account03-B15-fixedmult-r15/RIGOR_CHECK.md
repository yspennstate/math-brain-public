# Rigor check and one explicit correction for account03/B15 r15

This file is part of the same run and is authoritative where it corrects `REPORT.md`.

## 1. Correction to Proposition 5.1 notation

`REPORT.md` equation (5.1) writes

`int ||a_t||_2^2 dt <= J^2`.

For **that** definition of `J`, the correct consequence of the displayed Cauchy--Schwarz calculation is

`int |phi_Q(t)| dt <= 2 + pi sqrt(2) J`,

hence

`boxed: ||p_Q||_infinity <= 1/pi + J/sqrt(2).`

The report's equation (5.2), which wrote `1/pi+sqrt(pi)J` immediately after defining `J` as the spacetime-energy square root, is a notation mismatch and should not be used.

The **joint-density formulation** later in the same section is correct. If `h(z,r)` is the joint density of `(CY,R(Y))` and

`H:=||h||_2`,

then partial Plancherel gives

`int ||a_t||_2^2 dt = 2pi H^2`,

so the preceding corrected inequality becomes

`boxed: ||p_Q||_infinity <= 1/pi + sqrt(pi) H.`

This is the endpoint compiler used in the handoff.

## 2. Singular-value inheritance checks

For `E={0_H} direct_sum ker C`, `codim(E)=2+rank(C)=4`. Compression of `A^2` to the domain subspace, or the min-max principle for approximation numbers, gives

`s_j(A|E)>=s_{j+4}(A)`.

On `E`, `A(0,y)=(0,Dy)`, so `s_4(D|ker C)>=s_8(A)`.

If `B` is invertible and `S=D-C^TB^{-1}C`, then

`A-diag(0_2,S)=[I_2;C^TB^{-1}] B [I_2,B^{-1}C]`

has rank at most two. The rank-perturbation inequality

`s_{j+2}(A)<=s_j(diag(0_2,S))`

therefore gives `s_6(S)>=s_8(A)`.

No norm of `B^{-1}` enters either singular-value conclusion.

## 3. Physical-pair Fourier calculation

With

`F_t(z)=hat g_t(2tz)`,  `g_t(x)=e^{itx^TBx} f_1(x_1)f_2(x_2)`,

change variables `xi=2tz` in two dimensions and use the manuscript Fourier convention:

`||F_t||_2^2=(4t^2)^(-1)(2pi)^2||g_t||_2^2
             <=pi^2/t^2`,

because `int f_i^2<=int f_i=1` for cap-one probability densities. Thus

`|phi_Q(t)|<=pi |t|^-1 ||a_t||_2`.

This retains arbitrary `B`; no perturbation in the self block and no rotation of random coordinates occurs.

## 4. Critical-envelope regularity arithmetic

For `|phi(t)|<=min(1,U/|t|)`,

`int |phi|^2 <=4U`, hence `||p||_2^2<=2U/pi`.

For `0<=sigma<1/2`,

`(2pi)^(-1)int |t|^(2sigma)|phi|^2
 <=2U^(2sigma+1)/[pi(1-4sigma^2)]`.

When `U|h|<=2`, splitting the positive half-line at `U` and `2/|h|` gives

`int_0^infinity min(4,t^2h^2)min(1,U^2/t^2)dt
 =4U^2|h|-(2/3)U^3h^2`.

After symmetry and the `(2pi)^(-1)` Plancherel factor,

`||tau_h p-p||_2^2
 <=[4U^2|h|-(2/3)U^3h^2]/pi
 <=4U^2|h|/pi`.

For the terminal eight-direction collar,

`g_*=0.36494426588270207...`,
`C_*=sqrt(e)g_*^(-1/4)=2.121243892402635...`,
`U=pi C_*=6.664084228844336...`,

so

`||p||_2<=2.059730027165034...`,
`2U/sqrt(pi)=7.519613811597714...`,
`2/U=0.3001162547350986...`.

## 5. Scope check

Nothing here proves a universal `L^infinity` bound at multiplicity eight. The exact-zero self-block chamber is already paid separately. The new endpoint criterion asks for a uniform `L^2(R^3)` density bound for `(CY,R(Y))` (or equivalently finite spacetime complex-fiber energy). This is deliberately an averaged joint statement and does not assume the refuted arbitrary-joint coarea bound or a positive moment of conditional density suprema.
