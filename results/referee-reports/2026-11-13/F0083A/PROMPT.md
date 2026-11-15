Open problem F0083. Source: C. Hoffman, A. E. Holroyd and Y. Peres, "A stable marriage of Poisson and Lebesgue" (Ann. Probab.
34 (2006); arXiv:math/0505668), the list of open problems near the end, problem (i) "Nonuniqueness": does there exist a discrete
set of centres in R^d which admits two stable allocations (differing on a set of positive Lebesgue measure)? The paper says that by
its Theorems 2 and 3 such a set must have greater than quadratic growth and cannot arise from a translation-invariant point process.
Setting: an allocation of R^d to a discrete set Xi of centres with appetite alpha gives each centre a territory of Lebesgue measure
at most alpha; it is stable in the Gale-Shapley sense with preferences by Euclidean distance (a site x and a centre xi are unstable
if x is unallocated or prefers xi to its centre, and xi is not sated or prefers x to some site of its territory).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). State problem (i), Theorems 2 and 3 and the growth condition
   exactly (what "quadratic growth" means there: number of centres in a ball of radius r, in every dimension d?). Search for later
   work: Hoffman-Holroyd-Peres "Tail bounds for the stable marriage of Poisson and Lebesgue" (Canad. J. Math. 2009), Holroyd-Pemantle-
   Peres-Schramm "Poisson matching", Deijfen-Holroyd-Peres, Chatterjee-Peled-Peres-Romik (gravitational allocation), Markó-Timár,
   Holroyd "Geometric properties of Poisson matchings", Haji-Mirsadeghi and coauthors (stable matchings/allocations on non-Poisson
   sets), and 2006-2026 papers citing the original. If a printed result answers problem (i), give the theorem and page and stop
   with RESOLVED_IN_LITERATURE.
2. Understand why uniqueness holds under at most quadratic growth: the paper's construction (the Gale-Shapley-type algorithm,
   site-optimal and centre-optimal allocations, and the argument that they coincide). Find exactly where the growth bound is used.
3. Try to answer it. The natural route: build a deterministic discrete set (start with d = 1, where growth faster than quadratic
   is easy to arrange with locally finite but increasingly dense clusters far away) for which the site-optimal and the
   centre-optimal stable allocations differ on positive measure; or prove uniqueness for all discrete sets in some dimension, which
   would show the growth condition is an artefact. Give a complete proof either way, with every case checked. If the full answer
   is out of reach, prove a precise partial statement (for example nonuniqueness for a set with infinite appetite total in a bounded
   region excluded, or uniqueness under a weaker growth condition than the paper's).
4. Compute (evidence only): implement the two allocations (site-optimal and centre-optimal) on a fine grid for a candidate set
   truncated to a large window, and check where they differ and whether the difference survives as the window grows.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
