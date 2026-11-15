# Open problem C0033, third attempt: entropy concavity of determinantal point processes on three points and in rank two

The problem: for a Hermitian contraction 0 <= Q <= I on a finite ground set, let H(Q) be the Shannon entropy of the
determinantal measure P_Q. Is H concave on the whole set of contractions (the conjecture recorded in Gu's work, which proves
concavity along rank-one directions)?

Read first, in full: ../C0033B/REPORT.md (this run's predecessor; it proves joint concavity in one row and column in every
dimension, concavity along indefinite rank-two directions aa*-bb* on three points, and reduces three-point concavity at a
strict contraction to the scalar inequality (17) when R_Q > 0) and ../C0033A/REPORT.md (two-point theorem, conditional lifting,
product-kernel Hessian). Use their code (dpp.py, dpp.cpp) by copying it here. Credit their results; do not re-prove them.

TASK, in order:
1. Prove inequality (17) of C0033B on the whole strict three-point domain, or find a point where it fails (then check whether
   the full Hessian is really positive there, with exact or interval arithmetic, and whether that gives an entropy
   counterexample along a segment). Treat the boundary case R_Q singular separately.
2. Rank-two positive semidefinite directions A = aa* + bb* on three points (excluded from the aa*-bb* case): concave or not?
3. Any rank-two direction in dimension n >= 4, using conditioning and the one-row result.
4. If 1-3 give full three-point concavity, state it as a theorem with a complete proof; if a counterexample appears, give it
   with a certified computation (interval arithmetic or exact rationals) a referee can rerun.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
