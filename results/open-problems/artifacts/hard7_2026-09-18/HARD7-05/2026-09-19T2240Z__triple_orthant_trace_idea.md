# HARD7-05 route note — replace the four-orthant trace by an exact three-coordinate projection

Status: exploratory route written before the checker. Canonical target remains `MOLCHAN-2025-THETA2H`; no closure claim.

Incoming certified point: `H=1/4`, `theta_{2,1/4}>1647/10000`, hence `W_{1/4}=853/10000`. Keep the already certified comparator parameters

`r=7/8`, `s=24861/25000`, `c=s(1+r)/2=74583/80000`.

The previous proof loses information at exactly one place: it bounds the softened fourth trace by the **hard-edge** fourth trace,

`tr(K_{r,s}^4) <= tr(K_{r,1}^4) < 553151/500000`.

Do not optimize `s` again. Instead change category from the operator to the normalized Gaussian four-cycle underlying the trace.

## B1 — change category: operator trace -> Gaussian cycle geometry

Under the normalized trace measure for four AR(1) edges, the vertex vector `(X_0,...,X_3)` is centered Gaussian with unit variances and

`a := Cov(X_i,X_{i+1}) = (r+r^3)/(1+r^4)`,
`b := Cov(X_i,X_{i+2}) = 2r^2/(1+r^4)`.

For the edge sums `A_i=(X_i+X_{i+1})/sqrt(2(1+r))` and softened edge variables

`V_i=sqrt(s) A_i + sqrt(1-s) E_i`,

with iid standard `E_i`, one has

`tr(K_{r,s}^4) = (1-r^4)^(-1) P(V_0<0,V_1<0,V_2<0,V_3<0)`.

At `r=7/8`, exact simplification gives

`a=6328/6497`, `b=6272/6497`,
`Var(A_i)=6840/6497`,
`Cov(A_i,A_{i+1})=6780/6497`,
`Cov(A_i,A_{i+2})=6720/6497`.

After softening,

`rho_adj = 168557580/170952323`,
`rho_opp = 167065920/170952323`.

## B4 — prove something weaker, completely

Do **not** evaluate the four-dimensional orthant probability. Drop one inequality:

`P(V_0<0,V_1<0,V_2<0,V_3<0) <= P(V_0<0,V_1<0,V_2<0)`.

The right side is exact by the centered trivariate Gaussian sign identity:

`P(V_0,V_1,V_2<0) = 1/8 + [2 asin(rho_adj)+asin(rho_opp)]/(4 pi)`.

This follows directly by expanding the three sign indicators and using `E sgn(X)sgn(Y)=(2/pi)asin Corr(X,Y)`; odd sign moments vanish by global sign symmetry. Rational `atan`/Machin bounds should certify

`tr(K_{r,s}^4) < 110273/100000 = 1.10273`,

strictly sharper than `1.106302` without any 4-D numerical quadrature.

## B25 — count the same object twice

Use the same normalized four-cycle both (i) as `tr(P_r^4)=1/(1-r^4)` times a Gaussian orthant probability and (ii) as a spectral fourth moment `sum_j lambda_j^4`. The improved orthant cap therefore directly lowers the non-Perron spectral-tail cap in the existing Temple argument.

Keep the already exact degree-18 quasimode bounds from the previous checkpoint:

`9116948312/10^10 < mu < 9116948313/10^10`,
`eps^2 < 47004495/10^11`.

Candidate source movement to test exactly:

`theta_* = 103/625 = 0.1648`.

Take `x=183147/200000=0.915735`; check `x^625 < (7/8)^412`, so `x<r^(4 theta_*)`. With the new trace cap try `beta=9938/12500=0.79504`. The intended exact contradictions are

`beta^4 > 110273/100000 - x^4`

and

`(x-mu_upper)(mu_lower-beta) > eps_upper^2`.

If both hold, the existing all-lag covariance domination plus the Lamperti/Slepian reduction yields the genuine continuous-path bound `theta_{2,1/4}>103/625`, moving the frozen width to `1/4-103/625=213/2500=0.0852`.

No sampled-path numerics enter the proposed proof.