# R08 E0011 idea before code — descriptor-carrying stage gluing

Methods for this run: **B18 / B20 / B27**.

## B18 — say the stage reset as a relation, not a scalar

The current `b20_global` global-horizon recursion throws away the actual local descriptor whenever an intermediate horizontal stage first reaches the six-vacancy target.  It replaces the reached target state `s` by

`min_{t in E_next} U_next(n,t)`.

That is source-valid but strictly stronger than the real exterior uncertainty: after a horizontal stage succeeds, the next local window is a one-column translate of the current window, so the overlapping coordinates are already determined by `s`.  Only the newly exposed leading cells can still be chosen by the exterior.

For each target descriptor `s`, define the exact continuation relation

`R_x(s) = { t in E_beh : t(c)=s(c+(1,0)) for every next-window state coordinate c whose translate c+(1,0) lies in the current 14-cell state patch }`.

The six target vacancies at old columns `-1,0,1` become the three required generated-shield vacancy columns `-2,-1,0` in the next frame, so every true translated continuation belongs to `R_x(s)`.

The source-valid Bellman boundary condition for horizontal stage transitions is therefore

`U_j(n,s) = min_{t in R_x(s)} U_{j+1}(n,t)`

rather than the scalar reset over all `E_beh`.

## B27 — quantifier order

The exterior is universal, but it is not allowed to rewrite already observed overlap.  The correct order is:

1. random protected history produces a concrete target descriptor `s`;
2. translate the window;
3. the arbitrary exterior chooses only a completion `t` consistent with the translated overlap;
4. sum all later random histories from that completion.

Thus the minimum may depend on `s`, but only through `R_x(s)`.  Taking a global minimum before seeing `s` commutes the universal quantifier past deterministic information and loses probability.

## B20 — where the algorithm can fail

This relation refinement is valid only when the next stage is literally a one-column horizontal translate of the same generated-shield module.  I will apply it only to the five horizontal transitions

`h3->h4`, `h4->h5`, `h5->h6`, `h6->h7`, `h7->h8`.

I will **not** infer a relation for `h8->g_down` or `g_down->g_up` without separately recovering their guard geometry; those two transitions retain the old scalar worst-entrance reset.  The checker must verify that every target signature encountered has at least one compatible next entrance descriptor.  An empty relation would expose a coordinate/model mismatch rather than count as a proof.

## Expected measurable test

Keep the same common-clock horizon and the same exact Poisson/exponential lower bound as `b20_global`.  Recompute the exact coefficients through tick 40 with relation-aware horizontal gluing.  If the resulting rational corridor probability is strictly larger than the archived `P_global`, then the frozen metric moves by replacing only that factor; otherwise this route is recorded as no movement.
