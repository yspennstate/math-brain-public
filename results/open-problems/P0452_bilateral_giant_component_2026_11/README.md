Independent referee pass on the public paper bilateral-preference-giant-component (P0452), 12 Nov 2026.
Verdict GAP, no counterexample; four repairs in public commit 4bd8c7cd5f448368270ce1449de56449c1f8b52c; Zenodo 10.5281/zenodo.24148593; ledger master 873bd3cba15c5cad179c524aaecddeab74aa2670.
referee/ holds the report and log; sandwich_check.py tests the new inequality by brute force; ledger_update.json is the ledger row's new fields.

## Credits

The question is the third question of Section 4 of Moharrami, Subramanian, Liu and Sundaresan, "The Erlang weighted
tree, a new branching process" (Random Structures Algorithms 2024, arXiv:2002.03993), who observe in simulation that
the fraction of vertices in the giant component approaches the survival probability of the limit tree and note that
the reverse inequality needs a separate proof; the paper uses their local convergence theorem, their upper bound and
their backbone and pruning construction. With a constant budget the model is the bilateral preference graph of La and
Kabkab (2015), whose connectivity threshold was found by Dabirian and Subramanian (2026). The limit of the complete
graph with exponential edge costs is the Poisson weighted infinite tree of the objective method of Aldous and Steele,
and the variance bound is the Efron-Stein inequality (Efron and Stein 1981, Steele 1986) in the form of Boucheron,
Lugosi and Massart (2013). The paper also cites van der Hofstad's almost-local criterion for the giant (2021) and his
monograph (2024). Full references are in the paper.
