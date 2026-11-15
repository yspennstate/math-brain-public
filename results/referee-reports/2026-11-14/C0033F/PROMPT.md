# Open problem C0033, sixth attempt: the general mixed collar and the global constant for three-point concavity

The problem: for a Hermitian contraction 0 <= Q <= I on a finite ground set, let H(Q) be the Shannon entropy of the
determinantal measure P_Q. Is H concave on the set of contractions (Lyons 2003 Conjecture 9.2)? On three points, C0033A-D
reduce full concavity to one scalar inequality on the connected strict domain: the margin m(Q) = 1 - theta(Q) is positive.
C0033E proved an exact formula for m on the cyclic family, a uniform lower bound m >= 1/(4 Lambda + 2) on a RESTRICTED mixed
collar (equal real connections e, balanced two-point block [[1/2, h-1/2],[h-1/2, 1/2]], x = e^2 small), and showed that a
global bound m >= c/(Lambda + C) needs c <= 1/2. Lambda(Q) = -log min_S p_S(Q).

Read first, in full: claim_files/C0033E/REPORT.md, then ../C0033D/REPORT.md, ../C0033C/REPORT.md, ../C0033B/REPORT.md,
../C0033A/REPORT.md. Copy the code you need from ../C0033E and ../C0033D and credit their results without re-proving.
An independent check of C0033E (claim_files/C0033E_check/CHECK.md) confirmed Theorems 1-2 and Corollary 3 numerically.

TASK, in order:
1. Remove the restrictions of C0033E Theorem 2: unequal and complex connections (e_12, e_13 separately, with phases), an
   unbalanced two-point block (any 2x2 contraction with eigenvalues near 0 and 1, or one eigenvalue near 0 or 1), and the
   isolated point's weight a anywhere in (0,1). Derive the leading term m_0 of m on this general mixed collar as x -> 0 with
   an explicit uniform remainder, and prove m_0 >= c/(Lambda + C) with explicit constants, or exhibit where it fails.
2. Search hard, in high precision (mpmath, 60+ digits; atoms go to zero), for the infimum of Lambda(Q) m(Q) over the whole
   connected strict domain and over each boundary face separately. Report the smallest values found, where, and whether
   1/2 (the C0033E corollary) is the right constant. A margin that tends to zero is not a violation; a negative margin is.
3. Classify the boundary of the three-point domain into faces (spectral: an eigenvalue of Q at 0 or 1; graph: one or more
   edge moduli at 0; and their intersections). For each face, say whether a scaled margin bound is now PROVED (by C0033C-E
   or here), or still open. Then say what compact remainder is left and whether the interval cover of C0033D (bnb.py)
   covers it with the scaled margin. A scaled margin on every collar plus a certified cover of the compact rest IS a proof
   of three-point concavity; say exactly what is covered and what is not.
4. If a violation appears: certify it with interval arithmetic, confirm the ambient Hessian has a positive direction from
   the atom formula alone, and give the segment along which H fails to be concave.
Keep peak memory under 4 GB; no worker pools larger than 4 threads; checkpoint long runs to disk.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem or proof text.
