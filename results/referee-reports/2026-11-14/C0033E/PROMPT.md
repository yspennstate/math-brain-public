# Open problem C0033, fifth attempt: the mixed spectral/graph boundary of inequality (21) on three points

The problem: for a Hermitian contraction 0 <= Q <= I on a finite ground set, let H(Q) be the Shannon entropy of the
determinantal measure P_Q. Is H concave on the set of contractions (Lyons 2003 Conjecture 9.2)? On three points, C0033A-D
reduce full concavity to one scalar inequality on the connected strict domain. C0033D (Theorem 1) states it exactly as
b*^T M^{-1} b* >= 2 for an explicit 7x7 matrix M > 0 in seven real parameters; its margin is m(Q) = 1 - theta(Q).

Read first, in full: ../C0033D/REPORT.md, then ../C0033C/REPORT.md, ../C0033B/REPORT.md, ../C0033A/REPORT.md. Copy their
code (dpp.py, dpp.cpp, reduced.py, boundary.py, interval_core.py, bnb.py) here and credit their results without re-proving.

What C0033D left open: (i) its Theorem 2 family Q_r (diagonal 1/2, off-diagonals +-ir) has margin 4/(L+4) -> 0 as the
eigenvalues approach 0, 1/2, 1, so there is NO uniform positive margin and a plain compact cover cannot close the problem;
(ii) the generic simultaneous approach to a spectral face (an eigenvalue of Q near 0 or 1) and a disconnected graph (an edge
modulus near 0) has no boundary estimate; (iii) the margin formula of Theorem 2 has not been re-derived independently.

TASK, in order:
1. Re-derive the exact margin along Q_r by a route different from C0033D (for example directly from the nine-direction
   Hessian, or a symbolic computation of b*^T M^{-1} b*), and say whether it agrees with C0033D (4) and (12).
2. Search hard, near the limit of Q_r and in the mixed boundary regime of (ii), for a violation: perturb Q_r in all nine
   directions at large L; follow the minimum of m over the boundary collar as L -> infinity; use high precision (mpmath,
   60 digits or more) because atoms go to zero. Report the smallest margin found and where. A margin that tends to zero is
   not a violation; a negative margin is.
3. If no violation: find the right normalisation. Prove a lower bound of the form m(Q) >= c / (L(Q) + C) (or whatever
   rate the data show), with L(Q) an explicit log-scale of the smallest atom, near every spectral face, including the
   mixed faces of (ii). Asymptotic expansions with explicit, uniform remainders. A proof of a scaled margin on the collars
   plus a certified interval cover of the compact rest IS a proof of three-point concavity; say exactly what is covered.
4. If a violation appears: certify it with interval arithmetic, confirm the full ambient Hessian has a positive direction
   from the atom formula alone (finite differences in high precision), and give the segment along which H fails to be concave.
Keep peak memory under 4 GB; no worker pools larger than 4 threads; checkpoint long runs to disk.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem or proof text.
