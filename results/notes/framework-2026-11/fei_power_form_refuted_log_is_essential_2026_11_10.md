---
name: fei_power_form_refuted_log_is_essential_2026_11_10
description: "Can FEI be proved by Cauchy-Schwarz / an L1 bound on coefficient products? No (10 Nov): sum_i sum_U |fhat(U)||fhat(U-i)| <= C I is false, it grows linearly in tower depth (0.667 -> 1.333); the logarithm is essential"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T10:48:02+02:00
  status: verified
  evidence: "06_math_research/fei_solve_2026_11_09/code/power_form.py run 10 Nov 2026 (0.666667 at depth one, 1.333333 at depth two, composition formula to rounding); commit dace99cfd5e1"
---

Can FEI be proved by a norm inequality (Cauchy-Schwarz, L1 against L2 of the spectrum)? No: the power form fails.

**Statement.** mu(S) = fhat(S)^2. FEI is equivalent to L := (1/I) sum_i sum_{T without i} mu(T+i) log2(1 + mu(T)/mu(T+i)) <= C.
Since log2(1+x) <= 1.161 sqrt(x) (the max of log2(1+x)/sqrt(x), near x = 3.9; an earlier "2/(e ln 2) = 1.0615" here was wrong, it is the constant for ln x <= (2/e) sqrt(x) - corrected 10 Nov by an agent), FEI would follow from the "power form"
    sum_i S_i <= C I,    S_i = sum_{U containing i} |fhat(U)| |fhat(U - i)|.
**The power form is false** (10 Nov 2026). For a tower f = F(psi,...,psi) with psi balanced, r_i = S_i/Inf_i obeys
    r(f) = r_i(psi) + (|psihat({i})| / Inf_i(psi)) r_b(F),
and |psihat({i})| = Inf_i(psi) for monotone psi, so r adds one full unit of r(psi) per level instead of contracting.
Checked numerically (computed exactly by `06_math_research/fei_solve_2026_11_09/code/power_form.py`, float64): a
balanced monotone 4-variable base composed with itself has sum_i S_i / I = 0.666667 at depth one and 1.333333 at
depth two, and the composition formula holds to rounding.

**Why it matters.** The entropy cost of a level contracts in a tower because the logarithm sees the ratio
mu(T)/mu(T+i) fall geometrically; any square-root or power bound sees the product and does not contract. So every
route of the type "bound the entropy by an L1 norm of products of coefficients" is closed. The logarithm is essential.

**How to apply.** Before trying a hypercontractive or Cauchy-Schwarz bound on sum_T |ghat(T)||hhat(T)|, test it on a
depth-2 and depth-3 tower of a balanced monotone base; if the quantity grows linearly in depth it cannot bound FEI.

Status: verified on the stated example (measured, exact transforms); the composition formula is proved in FLOW.md
12(z) item 2. Record: commit dace99cfd5e1 (code) and 9d9b6af4bac4 (FLOW 12(z)).
Related: [[fei_step_ratio_towers_4475_referee_2026_11_10]], [[fei_solve_plan_up_ratio_form_h_le_2b_plus_2i_2026_11_09]].


Independent check (an agent, 10 Nov 19:28): full truth tables, own transform, all 16 balanced monotone 4-variable
functions that use every variable: base x0x1 v x1x2 v x0x3 gives 0.666667 at depth one and 1.333333 at depth two (16
variables), as claimed. The other class, x0x1 v x0x2 v x0x3 v x1x2x3, is self-dual and gives 0 at every depth (odd-size
support only), so the counterexample needs a base that is not self-dual. Note and code:
06_math_research/fei_solve_2026_11_09/audit_agent/POWER_FORM_REFEREE_2026_11_10.md, fei_powerform_referee.py.

Since log2(1+x) <= (2/(e ln 2)) sqrt(x), FEI would follow from the "power form"
