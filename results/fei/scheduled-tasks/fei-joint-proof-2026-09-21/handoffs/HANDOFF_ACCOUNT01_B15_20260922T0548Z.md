# account01/B15 FEI handoff — sharp arbitrary-bias posterior credit

Classification: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.

Scientific source: `yspennstate/math-open-problems`, commit `956170387bdf394faa29c7539e6ded3606ef4c67`, path `proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T053153Z-sharp-biased-joint-credit/REPORT.md`.

Exact peer theorem consumed and strengthened: account04/B13 `20260922T051245Z-biased-joint-credit-collar/REPORT.md`, report blob `e77494a14411182d0f20429a349ccfef3d561253`.

For a physical pivot of bias t, restrictions `f_0=sum a_S chi_S`, `f_1=sum b_S chi_S`, disagreement `delta=Pr(f_0 != f_1)`, and `V_t=4t(1-t)`, define

`Psi(z)=h_2((1-sqrt(1-z^2))/2)`.

Using the exact signed Boolean overlap `sum_S a_S b_S=1-2 delta`, posterior weights `T_S=(1-t)a_S^2+t b_S^2`, and `x_S=t b_S^2/T_S`, one has

`H(B|S)=E_T Psi(2 sqrt(x_S(1-x_S)))`.

`Psi` is increasing and convex, with

`Psi''(z)=[ln((1+r)/(1-r))-2r]/[2 r^3 ln 2] >= 0`, `r=sqrt(1-z^2)`.

Therefore the exact source-valid negative entropy credit satisfies

`C_j >= H(B|S) >= Psi(sqrt(V_t) |1-2 delta|)`.

This strictly strengthens the earlier arbitrary-bias quadratic credit `V_t(1-2 delta)^2` and specializes at `t=1/2` to the previously sharp center expression.

Applied to balanced children and the live `Gamma^dagger` candidate, the same report proves analytically

`min(t,1-t) <= 1/64` and `delta=It_j/V_t >= 1/4` imply `R_{Gamma^dagger,j}+C_j>0`.

Thus the proven rare-pivot exclusion collar widens from the peer's `2^-15` to `2^-6`, a factor 512, without sampling. The first remaining balanced-child region is the compact strip `1/64 < min(t,1-t) < 1/2`, `delta >= 1/4`; after that remain `delta<1/4` and unequal child output measures, where the potential Jensen term is nonzero.

Full FEI is not proved. No arbitrary spectral-law relaxation, uncharged coordinate labels, or discarded negative posterior term is used.
