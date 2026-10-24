# account04/B16 handoff — exact balanced arity-five gate certificate

Status: `AUXILIARY_ONLY / EXACT_ARITY5_EXCLUSION`; full FEI remains OPEN / NOT PROVED. Execution: `WITHOUT_VERIFIED_BRAIN`.

Latest OWNER CONTROL revision `2026-09-22.2` superseded the older interface-C phase-switch assignment and directed all FEI workers to the all-gate reformulation. Accordingly the older account02/B16 parent-weight and account03/B18 signed-flag-curvature artifacts were preserved but not extended in this run.

Scientific package: `proofnet24/P03-fei/fleet-2026-09-21/account04/B16/20260922T011015Z-arity5-balanced-exact/` in `yspennstate/math-open-problems`, final package commit `49ded0457c52895eb1773bb973118041fac25e39`, report blob `397a5be2b5c5e9b3ce01823e470297300d919080`.

New exact theorem: every balanced Boolean five-input gate satisfies

    H(G) <= 6 (I(G)-1).

If it depends on all five coordinates, the sharp bound is

    H(G)/(I(G)-1) <= 44/5 - (9/5) log_2 3
                  = 5.947067498701919...

and equality is attained by normalized truth table `0x373f001f`, which the exact cofactor test confirms is composition-prime. Therefore for the current read-once candidate C0=6.4548,

    c_G(1/2,...,1/2) <= -2.03093000519232...

on every balanced full-support five-input gate; no balanced-uniform arity-five gate asks for more than the positive AND margin. Any arity-five counterexample must use an unbalanced output and/or nonuniform biases. Together with the account01/B13 prime-descent theorem, a balanced-uniform prime obstruction to this candidate has arity at least six.

Exact coverage: 222 four-variable NPN representatives times all second cofactors, restricted to balance; 1,943,873 normalized balanced rows. The integer/log interval checker had zero inconclusive rows. Full-support balanced rows: 1,942,928; seven exact equality rows. Checker SHA-256 `45c3b203c2951d077f412edf2d76c71fc09fda7da44fa0c537035874bb85915c`; output SHA-256 `d33270ce5056ef1d15ebabca73e00c5c6c65143d971841071bc62bd5f45f6387`.

Consumed sources: gate reformulation blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`; account01/B14 balanced-margin refutation blob `776ade5c2e2017844785b09ab7af50c7eaf54c03`; account01/B13 composition-prime/slack law blob `674213d7e9d2f2952fcd22a94ad1be014a5b741f`; account03/B16 prime-density report blob `d743982431331645bb531911324eec1a6f735cf2`; five-variable NPN coverage checker blob `e19463905d49aa48e7b98edda572306e03718e84`.

Next live implication: certify or falsify the remaining nonuniform-bias/unbalanced arity-five region for a viable replacement potential, or use the known balanced obstruction to constrain the replacement Gamma. Do not revive the superseded interface-C route unless a later owner directive restores it.
