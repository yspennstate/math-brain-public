# P01-A -> P01-B handoff: arbitrary record-span coefficient

Source target remains Scully–Harchol-Balter–Scheller-Wolf (2020), Conjecture 8.1. Full-source status is still OPEN / PROVED PARTIAL. This handoff does not modify P01-B ownership.

Newest P01-B report recovered before this work: `probability_campaigns/progress_first_2026-09-20/P01/general/2026-09-20T155200Z__report.md`.

## New exact lemma

For any consecutive finite M-SERPT record span `a_0<...<a_k`, set

`x_j=S(a_j)`, `y_j=lambda N(a_j)`, `A_j=c+y_j`, `p_j=x_{j-1}-x_j`, `P=x_0-x_k`.

M-record ordering gives `y_j/x_j` nondecreasing and `y_j` nonincreasing. Define

`Sigma=sum_j p_j/(A_{j-1}A_j)`

and

`K=2P/(A_0 A_k)-Sigma`.

Let `r0=y_0/x_0`, `xi=y_k/r0`, `L=x_0-xi`, `R=xi-x_k`. Then

`Sigma <= L/(A_0 A_k)+R/A_k^2`

and hence

`K >= R/(A_0 A_k)+L(c+r0 x_k)/(A_0 A_k^2) > 0`.

Proof: lower-envelope every `A_j` by `c+max(r0 x_j,y_k)`, refine at `xi`, telescope the linear piece and integrate the constant piece exactly.

## Consequence for one Gittins valley

If one Gittins valley merges this M-record span and `V_j=E[(X wedge a_j)^2]`, then exactly

`2 P V_k/(A_0 A_k) - sum_j p_j V_j/(A_{j-1}A_j)`

`= K V_k + sum_{j<k} p_j(V_k-V_j)/(A_{j-1}A_j) >= K V_k > 0`.

After multiplying by `lambda/2`, this is the local factor-two waiting reserve. Thus an arbitrary number of skipped M-records has a strictly positive endpoint waiting coefficient; the remaining difficulty is residence/prefix compensation.

## Scalar skipped-prefix compression

For an initial skipped prefix with endpoint load level `a=A_m`, terminal mass `r`, prefix mass `P=1-r`, put

`w_j=1/A_{j-1}`, `wbar=P^{-1} sum p_j w_j`,

`sigma_w^2=sum p_j(w_j-wbar)^2`,

`K=2P/a-sum p_j/(A_{j-1}A_j)`, `C=K+r/(ac)`,

`q_j=lambda E[X 1_{block j}]`, `u=sum q_j`, `y=1-a`.

For the combined target `H=2 Qbar_G-Q_MS+2E[X]-R_MS`, block Cauchy and square completion give

`lambda H >= B_*(u)`

where

`B_*(u)=2rho-rho/a + u(1/a-wbar) - sigma_w^2/(2C) + C u^2/(2P) + K(y-u)^2/(2r) + (rho-u)^2/(2ac)`.

Moreover

`sigma_w^2 <= 2P/a-K-P wbar^2`.

The final-record condition gives `rho P >= 1-a`; writing `t=(1-a)/rho`, `R=P-t`,

`K >= R/a+t(c+rho r)/a^2 = P/a-(1-a)R/a^2`.

This is the clean endpoint interface I think should be combined with your `(EP)/(CHAIN)` prefix potential. I have **not** proved `B_*(u)>=0` in the full multi-record domain, so please treat that as the remaining shared bottleneck, not as a theorem.

Canonical proof artifact: `research7_2026-09-17/R7-04/artifacts/2026-09-20/2026-09-20T180100Z__P0434_record_span_coefficient_lemma.md`.

Notation note: in §4 of that artifact, the scalar later written `u` appears once at its definition as LaTeX `\nu`; it is the same scalar `u=sum q_j` used in all following formulas. This is a notation typo only, not a mathematical change.
