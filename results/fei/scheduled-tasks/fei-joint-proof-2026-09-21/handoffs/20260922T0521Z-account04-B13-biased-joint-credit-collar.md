# FEI handoff — account04/B13 arbitrary-bias joint credit

Source report: `proofnet24/P03-fei/fleet-2026-09-21/account04/B13/20260922T051245Z-biased-joint-credit-collar/REPORT.md` in `yspennstate/math-open-problems`, creation commit `57de90b61de51a7304cda6b7a6e1746fe3ccba7d`, report blob `e77494a14411182d0f20429a349ccfef3d561253`.

Classification: `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`.

Consumed peer result: account02/B13 `20260922T045511Z-joint-credit-critical-core/REPORT.md`, commit `547cb4e42877590ce8195a5a4859b0facb13877e`. That theorem gives the sharp unbiased-pivot joint-credit bound and excludes balanced-child local gluing with disagreement `delta>=1/4` at the center.

New theorem. For an arbitrary pivot bias `t`, let `delta=Pr(G_0 != G_1)` and `V_t=4t(1-t)`. The exact account04/B17 information credit satisfies

`C_j = H(B|S)+I(S;J) >= V_t (1-2 delta)^2`.

Proof uses the actual Boolean child Fourier coefficients: with posterior `x_S=t b_S^2/(q a_S^2+t b_S^2)` and `u_S=2 sqrt(x_S(1-x_S))`, signed Parseval gives `E_T u_S >= 2 sqrt(tq)|1-2delta|`; then `h_2(x)>=4x(1-x)` and Jensen give the displayed bound. No arbitrary spectral-law relaxation is used.

Inserted into the exact restriction cocycle, this yields for every actual pair of Boolean children

`R_{Gamma,j}+C_j >= q Gamma(r_0)+t Gamma(r_1)-Gamma(qr_0+tr_1) + delta[Gamma(t)+h_2(V_t)] - h_2(t)-h_2(V_t delta) + V_t(1-2delta)^2`.

For balanced children and the live `Gamma^dagger` candidate (`C^dagger=6.521851214`, quadratic lift `a^dagger=0.268204856`), the certified source tail from account01/B18 implies an explicit rare-bias collar:

`min(t,1-t) <= 2^-15` and `delta>=1/4`  =>  `R_{Gamma^dagger,j}+C_j > 0`.

Equivalently, every negative balanced-child local-gluing node in that collar has normalized influence `It_j/V_t<1/4`. The proof is analytic; at `delta=1/4` the displayed lower bound is at least `0.033051214*u`, and the local lower envelope is increasing for `delta>=1/4` with derivative at least `3.864*u` in the collar.

What changed: account02/B13 closed the unbiased center; this handoff extends the same signed-overlap mechanism to arbitrary pivot bias and uses the live linear-log potential tail to close the rare-pivot boundary. Remaining LOCAL-GLUING geometry is small normalized influence, intermediate biases, and/or unequal child output measures where the potential Jensen term must be paid.

Preserved: account04/B18 mixed-curvature conservation `kappa_ik=kappa_ki=p_ik+4o_ik`, `sum_{i!=k}(p_ik+4o_ik)=4d_k`, and the exact zero-defect classification. No `sum d_k=O(J)` claim and no cube-measure-times-dimension continuity payment.

Full uniform-cube FEI remains OPEN / NOT PROVED.
