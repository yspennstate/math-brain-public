# PROB10-03 / R14 — idea before code: dimensionless capacity chart

Status: preliminary mathematical derivation to be checked before any code is persisted. This is complementary work under the owner-refocused R14 route; it does not alter ownership or any canonical claim.

## Starting point

Use the already-proved strict projective complete-third chart

- `w0=1-p2`, `w1=p2-p3`, `w2=p3`, so `w0,w1,w2>0`, `w0+w1+w2=1`;
- `x=r0 r2/r1^2>1`, `y=r1/r2>1`;
- `Z=x y^2 w0+y w1+w2`;
- `q3=w2/Z`, `q2=(y w1+w2)/Z`;
- `c2=(x-1)sqrt(Z)/(x y w0)`, `c3=(y-1)sqrt(Z)/(y w1)`, `gamma_p=xy/(2sqrt(Z))`;
- on the capacity surface, `B=(x-1)/(2w0)` and `gamma_sq=sqrt(Z)/(2xy)`.

The hierarchy condition remains `(x-1)w1>x(y-1)w0`, equivalently `m=c3/c2 in (0,1)`.

## Attack A: scale out the inner hinge exactly

At capacity, `s^2=1-p2=w0` and `B=(x-1)/(2w0)`. For a spatial argument `z=sqrt(w0)t`,

`B(z+sH)_+^2 = (x-1)(t+H)_+^2/2`.

Therefore the one-step kernel becomes the dimensionless object

`F_x(t)=E_H exp[-(x-1)(t+H)_+^2/2]`, `U_x(t)=log F_x(t)`,

and the exact closed form is

`F_x(t)=Phi(-t)+x^(-1/2) exp[-(x-1)t^2/(2x)] Phi(t/sqrt(x))`.

The outer argument is

`T=sqrt(w1/w0) U + sqrt(w2/w0) V - 1/sqrt(w0)`.

The lifting ratio is already algebraic:

`m=c3/c2 = x w0 (y-1)/[(x-1)w1]`.

For fixed `V=v`, tilt `U` by `exp[m U_x(T)]` and write `<.>_v` for that expectation. Define

`S1=E_V <U_t>_V^2`,

`S2=E_V <U_t^2>_V`,

`H1=E_V < E_{rho_T}(T+H)_+^2 >_V`,

where `rho_T` is the normalized H-tilt proportional to `exp[-(x-1)(T+H)_+^2/2]`.

Because spatial differentiation gives `u_z=w0^(-1/2) U_t`, and `u_B=-w0 E_{rho_T}(T+H)_+^2`, the old score moments satisfy

`M1=S1/w0`, `M2=S2/w0`, `MB=w0 H1`.

Thus the exact stationary score equations become

`w2/Z = S1 / [(x-1)^2 H1]`,

`(y w1+w2)/Z = S2 / [(x-1)^2 H1]`,

and the reconstructed density becomes

`alpha = Z/(x^2 y^2 w0 H1)`.

This removes `B,c2,c3,gamma_p,gamma_sq` and all explicit small-`w0` powers from the score normalization.

Two immediate exact consequences are

`S2/S1 = 1 + y w1/w2`,

and, on the first score equation,

`alpha = w2 (x-1)^2/[x^2 y^2 w0 S1]`.

## Attack B: compile the positive c-sector KL equations in the same chart

Let `D_U` and `D_H` be the already-proved positive relative entropies satisfying

`A_c3=alpha D_U/c3^2`, `A_c2=alpha D_H/(c2 c3)`.

Use the existing projective algebra

`A_c3 = w1 [w2+w1 k(y)]/(2Z)`,

`A_c2 = w0/2 [1-(x y^2 w0/Z) h(x)]`,

with

`k(y)=y(y log y-y+1)/(y-1)^2`,

`h(x)=x(x-1-log x)/(x-1)^2`.

Substituting the capacity formulas above should give the exact two residuals

`(w2+w1 k(y))/Z = 2 w1 D_U/[x^2 w0 (y-1)^2 H1]`,

`w0 [1-(x y^2 w0/Z) h(x)] = 2 w1 D_H/[x(x-1)(y-1) H1]`.

Using the first score equation to eliminate `H1` yields a division-light positive system:

`Rratio = S2/S1 - (1+y w1/w2)=0`,

`Rscale = Z S1 - w2 (x-1)^2 H1=0`,

`RU = x^2 w0 (y-1)^2 S1 [w2+w1 k(y)] - 2 w1 w2 (x-1)^2 D_U =0`,

`RH = x(y-1) w0 S1 [Z-x y^2 w0 h(x)] - 2 w1 w2 (x-1) D_H =0`.

Every non-algebraic term in this system is nonnegative or a score moment; there is no subtraction of nested log-partition derivatives.

A natural unconstrained strict-domain chart is

`w0=e^a/(1+e^a+e^b)`, `w1=e^b/(1+e^a+e^b)`, `w2=1/(1+e^a+e^b)`,

`x=1+e^c`, `y=1+e^d`,

with the single remaining hierarchy inequality checked explicitly. This should be better suited to an interval Krawczyk map because simplex boundaries and `x,y>1` are no longer box faces.

## Attack C: test a genuinely different geometric consequence rather than another entropy inequality

The polar one-facet first moment was proved too weak in the previous R14 run. Do not repeat it. A different geometric route would have to use correlated facet pairs / angular coverage. The first bounded task is to determine whether the second factorial moment of support-distance-`<=1` facets can even have a favorable exponential rate at alpha about 12.3. If its overlap variational exponent is also positive at its optimizer, record that as an obstruction and do not spend later runs refining the same one-/two-facet route.

For this iteration, priority goes to proving the exact dimensionless compiler above because it directly targets the current complete-third outward-root bottleneck. Any conditioning calculation afterward is numerical-only and cannot move the source endpoint by itself.
