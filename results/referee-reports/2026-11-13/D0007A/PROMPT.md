# Open problem D0007: is every absolutely continuous law on a bounded interval n-CM for all large n?

Source: the 2014 survey of open problems on complete mixability (Open Problem 7, PDF p. 17). Puccetti, Wang and Wang showed
that a law on [a,b] with density f >= 3/(n(b-a)) is n-CM; so a density bounded away from zero gives n-CM for all large n.
Background: Wang and Wang (2011, J. Multivariate Anal.) monotone densities; Puccetti, Wang, Wang (2012, 2013); Wang and Wang
(Math. Oper. Res. 2016, joint mixability); Bellini-Karasan-Mueller-Wang and later papers on mixability of unimodal and
bounded densities. Check the literature 2014-2026 first; if this is settled in print, say where and stop.

Setting. F with mean mu is n-CM if X_1..X_n ~ F exist with X_1+...+X_n = n mu a.s. QUESTION: can the density lower bound be
dropped - is every absolutely continuous F supported on a bounded interval n-CM for all sufficiently large n?

TASK, in order:
1. Necessary conditions that could fail for every n: the mean condition holds for large n automatically; look for an
   obstruction from the Theorem-5 norm inequalities (law-determined norms, s = (n mu - t)/(n-1)) as n -> infinity, e.g. for
   densities with very thin tails at an endpoint (f(x) ~ (x-a)^k, or f(x) ~ exp(-1/(x-a))), or with gaps in the support.
2. Positive results beyond the density lower bound: prove n-CM for all large n for (i) densities vanishing like a power at
   one or both endpoints, (ii) densities with finitely many gaps in the support, (iii) any density that is positive and
   continuous on (a,b). Combine pieces with the known gluing results (a mixture of n-CM laws with the same mean is n-CM;
   the monotone-density and unimodal-density theorems).
3. Numerics: for candidate hard cases, test n-CM for n = 3..20 by linear programming on discretisations and by the
   rearrangement algorithm; report the smallest n that works and the trend.
State a theorem for the class you can handle, or a counterexample with a complete proof.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
