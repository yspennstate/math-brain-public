# Open problem C0033, fourth attempt: inequality (21) on connected strict three-point kernels

The problem: for a Hermitian contraction 0 <= Q <= I on a finite ground set, let H(Q) be the Shannon entropy of the
determinantal measure P_Q. Is H concave on the set of contractions? On three points, C0033A-C reduce full concavity to one
scalar inequality: (17) of C0033B, restated as (21) in C0033C, on the connected strict domain 0 < Q < I whose graph of
nonzero off-diagonal entries is connected. The singular stratum is settled (C0033C Theorem A).

Read first, in full: ../C0033C/REPORT.md (especially Sections 4 and 6), ../C0033B/REPORT.md and ../C0033A/REPORT.md. Copy
their code (dpp.py, dpp.cpp) here and credit their results without re-proving them.

TASK, in order:
1. Reduce (21) to its true parameter count. Conjugation by diagonal unitaries and permutations leaves H unchanged, so a
   three-point kernel is fixed by its diagonal (q1,q2,q3), the off-diagonal moduli and one gauge-invariant phase (the
   argument of Q12 Q23 Q31). State the reduced inequality explicitly in these seven real parameters.
2. Search hard for a violation: random sampling, then local minimization of the margin of (21), with particular attention
   to the boundary (eigenvalues of Q near 0 or 1, one off-diagonal modulus near 0, phase near 0 or pi). Report the
   smallest margin found and where.
3. If no violation appears, try to prove (21): asymptotic expansions at each boundary face to show the margin stays
   positive there, then a certified branch-and-bound with interval arithmetic (mpmath.iv or exact rationals) on the
   compact interior that remains. A complete certified cover plus proved boundary estimates IS a proof; say exactly what
   the cover verifies and to what tolerance.
4. If a violation appears, certify it with interval arithmetic, confirm the full entropy Hessian is positive in the
   corresponding direction, and give the segment along which H fails to be concave.
5. If 3 succeeds, state the full three-point concavity theorem (with Theorem A and continuity) and its proof.
Keep peak memory under 4 GB; no worker pools larger than 4 threads; a single run of the branch-and-bound may take hours,
checkpoint it to disk.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem or proof text.
