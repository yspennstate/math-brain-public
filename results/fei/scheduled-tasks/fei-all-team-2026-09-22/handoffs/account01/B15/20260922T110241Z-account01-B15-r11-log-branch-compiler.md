# account01/B15 handoff — restriction log-branch compiler

Classification: **ESSENTIAL_STEP_APPLIED**. Full uniform-cube FEI remains **OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

## Source-bound result

Full mathematics: `yspennstate/math-open-problems`, scientific package current head `bdd83ad57c03d2d8c840fd3fd60e6ec3272e3b67`, path `proofnet24/P03-fei/fleet-2026-09-22/account01/B15/20260922T110241Z-account01-B15-r11-log-branch-compiler/`. The report itself was introduced at `1cf41977f200bb8312bdd7d498f91484e5bbb819`, claims at `4ed6410bc009497ce8fe4df3cf212d0427787e7c`, and the adjacent correction at `bdd83ad57c03d2d8c840fd3fd60e6ec3272e3b67` only fixes the Section-1 typography `\nu_T` -> `u_T`; no mathematics changes.

Named compatible other-account result actually consumed: account02/B15 `20260922T103316Z-account02-B15-r11`, repository `yspennstate/math-open-problems`, commit `ad83138c850372d14d0dcacaa76a50a2fe79bcaf`, `REPORT.md`. Its source/reference log-bin KL compiler was applied to the negative `-JS_s(U,V)` term in account01/B15's preceding exact physical-restriction I-projection identity (commit `b293d016f9bd94819fb11385986608b8acc0b83d`).

## New theorem

For a genuine physical restriction at selector bias `s`, with child squared-spectral laws `U,V`, define a statistic `Z_eta(T)` that retains the actual child Fourier signs and eta-width bins of `-log_2 U_T` and `-log_2 V_T`, with separate one-sided-support tags. Let

\[
J_\eta=I(B;Z_\eta(T)),\qquad
R_\eta=I(B;T\mid Z_\eta).
\]

Then exactly
\[
\operatorname{JS}_s(U,V)=J_\eta+R_\eta,
\]
and, writing `rho_j` for the actual parent spectral occurrence mass of the restricted coordinate,
\[
0\le R_\eta\le c_\eta\rho_j,
\qquad
c_\eta={2(1+2^\eta)^2\over\ln2}.
\]
For one-bit log bins, `c_1=18/ln 2=25.9685107360...`. Importantly `c_eta` is independent of `s`; the rare `log(1/s)` information is retained in `J_eta` instead of appearing in the discarded restriction tax.

Substitution into the exact I-projection restriction chain gives
\[
\mathcal K(W)+J_\eta+c_\eta\rho_j
\ge
(1-s)\mathcal K(U)+s\mathcal K(V)
+C_{\rm marg}+C_{\rm erase}+C_{\rm pair}.
\]
The child `K_occ` coefficient stays exactly one and every reference-movement credit remains nonnegative.

For any nonreusing physical restriction tree on the uniform cube,
\[
\sum_u\pi_u\rho_{j(u),u}\le I(f),
\]
so telescoping yields
\[
\mathcal K_{\rm root}
+\sum_u\pi_uJ_{\eta,u}+c_\eta I(f)
\ge
\mathbb E\mathcal K_{\rm leaves}
+\sum_u\pi_u(C_{{\rm marg},u}+C_{{\rm erase},u}+C_{{\rm pair},u}).
\]
This is multiscale/full-spectrum and does not use the refuted fixed-level-plus-one-tail KL compression.

## Exact next unpaid implication

Construct a nonreusing physical restriction/stopping rule for which the exact Bellman deficit is bounded by the accumulated retained bank `sum pi_u J_eta,u` plus a fixed `O(I(f))` reserve, or give a genuine Boolean family refuting such domination. This is now the explicit location of the rare-event logarithm. No full FEI conclusion is claimed.
