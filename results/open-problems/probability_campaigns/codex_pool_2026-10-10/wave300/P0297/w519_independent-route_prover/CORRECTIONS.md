# W519-C2: incorrect dimension identity in intake D0049-A001

Source row: ~/<private-repo>/06_math_research/probability_1000_intake_D_20260908/attempts.jsonl, line 43, attempt_id D0049-A001.

The key_identity field contains "d_gamma = 2Q/xi"; the method repeats "d_gamma = 2 Q / xi". Both conflict with the primary definition xi=gamma/d_gamma, Gwynne--Miller arXiv:1905.00383v3, equation (1.5) and Problem 7.1. The correction is d_gamma=gamma/xi, while Q=2/gamma+gamma/2 remains unchanged.

Exact counterexample within the established LQG case: gamma=sqrt(8/3)=4/sqrt(6), xi=1/sqrt(6), Q=5/sqrt(6), and d_gamma=4. The incorrect expression 2Q/xi equals 10; the corrected expression gamma/xi equals 4. This is a correction of an intake attempt identity, not a new proof of the Brownian-map dimension or of P0297.

Patch scope: the two formula occurrences only. Every other field is retained, with no implied audit of its correctness. In particular, the source row's statement that the metric is not a function of the measure needs a separate scope check: the full embedded LQG measure can contain more information than its moment or local-dimension exponents. This packet does not rely on that assertion.

Independent mathematical reviewer: w521, requested in the full packet. No live source row has been edited.
