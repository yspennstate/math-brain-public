# Deterministic algebra checks

Executed during the run with exact symbolic arithmetic.

For the partner rare-fragment law with `eps=c/m^2`, remote center `a sqrt(m)`, centered unit main interval and remote interval of length `eps`:

- exact mean: `a*c/m^(3/2)`;
- exact variance:

`1/12 + a^2*c/m - c/(12m^2) - a^2*c^2/m^3 + c^3/(12m^6)`.

These agree with REPORT.md (9.3)-(9.4), so the normalized bank mean is `ca/m` and the bank variance tends to `1/12`.

For the finite-stage Fresnel--Brascamp--Lieb majorant

`g(t)=min(1,(4pi)^(3/2)|t|^(-3/2))`,

the exact crossover is `|t|=4pi` and

`integral_R g(t) dt = 24pi`.

Thus the common Fourier envelope used for dominated convergence is genuinely integrable; its crude inversion constant would be `12`, consistent with the source theorem.

Status: PASS.
