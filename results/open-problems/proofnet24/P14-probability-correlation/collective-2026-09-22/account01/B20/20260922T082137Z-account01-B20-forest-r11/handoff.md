# FOREST source-bound handoff — account01/B20

Run `20260922T082137Z-account01-B20-forest-r11`, outcome `ESSENTIAL_STEP_APPLIED`; parent target remains OPEN.

Consume these exact sources before continuing:

- lead: account01/B01 `20260922T080733Z-b01-forest-auto11`, report blob `7eccff21a034648951b1a5886db0330b60c3a5da`;
- required partner: account04/B03 `20260922T070756Z-B03-forest-r12-34330b0f`, report blob `a09681b45ae7e7e2d470fb5a2cdcd23c5c51fa38`;
- source correction: account01/B02 `20260922T054825Z-b02-forest-auto11`, report blob `7b500e2bc01d8788d526de9db984f52d6abe5d65`;
- exact path-cut transport: account04/B02 `20260922T011134Z-account04-B02-forest-r11`, report blob `70dd12f1c272a763642737810ecf5505b9f9438f`;
- union/intersection Hall no-go: account04/B02 `20260922T070653Z-account04-B02-forest-exchange-v4`, report blob `536a2157ede22dbddcafeb4f1b28b308ac8222ff`.

New proved package in this run:

1. In a minimum-edge loopless-multigraph counterexample, for every distinct physical edges `i,j,k`,
   `rho_ij <= rho_ik rho_jk`.
2. For a violating pair `e,f`, let `a=rho_ef>0`, `x_g=-rho_eg`, `y_g=-rho_fg`, `p=p_e+p_f`, `T=T_e+T_f`, and
   `E_*=p-T-(2-p)a^2` using the correct ground-set CLC denominator `L=m-E|F|`.
3. If `P_+` is the sum of positive correlations over third-edge pairs, then
   `P_+ <= E_*/2`.
   Therefore `tau=2 sum_{g<h} rho_gh <= E_*`.
4. PSD plus Simpson gives
   `2(m-2)^2 a <= (1+a)(m-2+E_*)`.
5. The minimal counterexample matroid is connected; no third parallel or series clone can accompany an endpoint of a positive pair.

Do **not** use the rank-degree CLC assertion in the newest lead report; account01/B02 gives an exact K3 refutation. Do not return to same-fiber/union-intersection-preserving Hall; account04/B02 has exact K4 obstructions.

Next direct mathematical target: prove a `GRAPHIC DEFECT-TO-POSITIVE-MASS` statement for the surviving multiplicity-changing T1--T5 cut/join or alternating-exchange network. It is sufficient to show that a residual Hall/flow deficit forces `P_+>E_*/2` (or `tau>E_*`). This must use genuine graphic path/cut structure; scalar PSD+CLC alone is insufficient.
