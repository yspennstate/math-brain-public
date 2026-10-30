# FOREST handoff — fleet01/B20 08Z

Source run: `20260922T082137Z-fleet01-B20-forest-r11`.
Canonical scientific report: `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet01/B20/20260922T082137Z-fleet01-B20-forest-r11/report.md` in private `yspennstate/math-open-problems`.
Outcome: `ESSENTIAL_STEP_APPLIED`; parent FOREST target remains OPEN.

Exact source-bound inputs: lead fleet01/B01 `20260922T080733Z-b01-forest-auto11` report blob `7eccff21a034648951b1a5886db0330b60c3a5da`; assigned partner fleet04/B03 `20260922T070756Z-B03-forest-r12-34330b0f` report blob `a09681b45ae7e7e2d470fb5a2cdcd23c5c51fa38`; source correction fleet01/B02 `20260922T054825Z-b02-forest-auto11` report blob `7b500e2bc01d8788d526de9db984f52d6abe5d65`; transport fleet04/B02 blobs `70dd12f1c272a763642737810ecf5505b9f9438f` and `536a2157ede22dbddcafeb4f1b28b308ac8222ff`.

New proved facts in a minimum-edge loopless-multigraph counterexample:

- for every distinct edges `i,j,k`, `rho_ij <= rho_ik rho_jk`;
- for violating `e,f`, define `a=rho_ef`, `x_g=-rho_eg`, `y_g=-rho_fg`, `p=p_e+p_f`, `T=T_e+T_f`, and `E_*=p-T-(2-p)a^2` using the correct ground-set CLC denominator `L=m-E|F|`;
- if `P_+` is the sum of positive correlations among third-edge pairs, then `P_+ <= E_*/2`; hence `tau=2 sum_{g<h}rho_gh <= E_*`;
- PSD + Simpson imply `2(m-2)^2 a <= (1+a)(m-2+E_*)`;
- the minimal counterexample matroid is connected and no third series/parallel clone can accompany an endpoint of a positive pair.

Do not use the rank-degree CLC claim appearing in the latest B01 report: B02 gives an exact K3 refutation. Do not return to same-fiber or union/intersection-preserving Hall: fleet04/B02 gives exact K4 obstructions.

Next unpaid step: `GRAPHIC DEFECT-TO-POSITIVE-MASS`. Use the surviving multiplicity-changing T1--T5 cut/join or alternating-exchange network to show that any residual Hall/flow deficit forces `P_+>E_*/2` (or `tau>E_*`). That would contradict the new signed-energy cap.
