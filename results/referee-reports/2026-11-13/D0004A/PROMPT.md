# Open problem D0004: when do the law-determined-norm inequalities imply complete mixability?

Source: the 2014 survey of open problems on complete mixability (Open Problem 4, PDF p. 16; Theorem 5 and Definition 5 there;
the survey is by B. Wang and R. Wang or by Puccetti-Wang - locate it). Background: Wang and Wang, "Complete mixability and
asymptotic equivalence of worst-possible VaR and ES estimates" / "Joint mixability" (Math. Oper. Res. 2016); Puccetti, Wang and
Wang (2012, 2013); Wang and Wang (2011, J. Multivariate Anal.) for monotone densities. Check the literature (including
2015-2026 follow-ups) first; if a converse to Theorem 5 is already in print, say where.

Setting. F with finite mean mu is n-CM if there are X_1..X_n ~ F with X_1+...+X_n = n mu a.s. Theorem 5: if F is n-CM then
||(X-t)_+|| <= (n-1)||(X-s)_-|| and ||(X-t)_-|| <= (n-1)||(X-s)_+|| for every law-determined norm, every t, s = (n mu - t)/(n-1).
QUESTION: under what extra conditions do these inequalities (for all norms and all t) imply n-CM?

TASK, in order:
1. Reduce "for all law-determined norms" to a majorization statement (Hardy-Littlewood-Polya / Calderon / Lorentz-Shimogaki;
   take care with infinite-valued norms and with the Fatou property), and state it as a lemma with proof.
2. n = 2: prove the inequalities are equivalent to symmetry of F about mu, hence to 2-CM.
3. Atoms: decide whether Bernoulli(1/2) with n = 3 (and more generally a law on a lattice whose n mu is not reachable)
   satisfies all the inequalities; if so this is a counterexample to sufficiency without extra conditions - prove it fully,
   and extract the natural extra condition for discrete laws.
4. Absolutely continuous laws: is the condition sufficient for laws with a density? Search for a counterexample among
   bimodal or compactly supported densities on [0,1] (test n-CM numerically by linear programming on fine discretisations
   and by the rearrangement algorithm, n = 3,4; verify any candidate carefully, ideally with an exact obstruction), or prove
   sufficiency for a class strictly larger than the monotone densities (unimodal densities, densities bounded below, ...).
5. The subsidiary question: characterise law-determined norms in the sense of Definition 5, as far as is clean.
Keep peak memory under 4 GB; no worker pools larger than 4 threads.

OUTPUT: REPORT.md whose FIRST LINE is one of PROVED / PARTIAL / COUNTEREXAMPLE / NO_PROGRESS, then the theorem
statement(s), complete proofs written as for a referee, numerical tables with code paths, and what remains open.
Keep a running LOG.md. Save all code and data in this folder. Write like a professional mathematician; no narration of
your process inside the theorem/proof text.
