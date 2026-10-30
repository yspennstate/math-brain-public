# FOREST B20 handoff — weighted nullity-three exclusion

Source run: `fleet01/B20/20260922T101949Z-B20-forest-r11b`.

Consume together with lead `fleet01/B01/20260922T080733Z-b01-forest-auto11` and partner `fleet04/B03/20260922T070756Z-B03-forest-r12-34330b0f`.

**New source-safe theorem.** In the partner's minimum-labelled-edge loopless-multigraph counterexample frame, a violating pair `e,f` must be singleton parallel classes. Collapse the remaining classes to positive integer activities on a simple support graph `H`. Every simple graph whose nontrivial 2-connected blocks have cyclomatic number at most `3` is weighted I-Rayleigh: series and parallel extension preserve weighted forest Rayleigh by exact polynomial identities; `K4` is weighted I-Rayleigh by the two explicit orbit formulas in the report; and a 2-connected cyclomatic-three graph with a `K4` minor is a subdivision of `K4`. Therefore the marked support block of any counterexample has cyclomatic number at least `4`.

Combining this with the source-safe loopless two-row CLC inequality yields, for `a=rho_ef>0` and total parallel excess `E`,

`a^2 + 4a(E+3) <= 1`,

hence

`a <= sqrt(4(E+3)^2+1)-2(E+3)`.

Numerically: `E=0` gives `a<=0.0827625302982196890`; `E>=1` gives `a<=0.0622577482985496524`.

**Correction boundary.** Do not use B20 `20260922T094714Z-B20-forest-r11`'s fixed-graph Cocks step. The repository correction `fleet02/B02/B02-20260922T013646Z-forest-r12/cocks_scope_correction.md` says that implication is not source-secure. The present theorem avoids it entirely.

**Next exact obligation.** Combine the existing path-cut / multi-step quotient-flow identities with the all-edge Simpson/matching constraints and the cap above. A decisive next theorem should either force the marked Rayleigh gap nonnegative directly or force a lower bound on `a` larger than the displayed nullity/parallel cap. Parent FOREST remains OPEN.

Exact checker: `weighted_nullity3_checker.py`; exact output terminates `STATUS=PASS`.
