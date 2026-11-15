Open problem C0151. Source: G. Pete, "Probability and Geometry on Groups" (lecture notes; find the current version online),
Conjecture 14.16 (attributed to Szegedy), p. 214: the set of possible asymptotic densities of independent sets in random
d-regular graphs coincides with the set of densities of independent sets that are factors of i.i.d. processes on the d-regular
tree. Read the source for the exact wording (which d, closure, what "possible asymptotic densities" means, factor of i.i.d.
meaning measurable automorphism-equivariant).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read the section around Conjecture 14.16. Search:
   Hatami-Lovasz-Szegedy ("Limits of locally-globally convergent graph sequences", the conjecture that every local statistic
   of random regular graphs is a factor of iid), Gamarnik-Sudan ("Limits of local algorithms over sparse random graphs"),
   Rahman-Virag ("Local algorithms for independent sets are half-optimal", Ann. Probab. 2017), Bayati-Gamarnik-Tetali,
   Ding-Sly-Sun (maximum independent set of random d-regular graphs for large d), Lyons ("Factors of IID on trees"),
   Backhausz-Szegedy-Virag, Csoka-Gerencser-Harangi-Virag (invariant Gaussian processes and independent sets), Lauer-Wormald,
   Harangi, and 2014-2026 work. If the conjecture is refuted or proved in print for some or all d, give the exact theorem and
   page; stop with RESOLVED_IN_LITERATURE when a printed result decides the conjecture as stated, and say for which d it is
   decided and whether small d (3, 4) remain open.
2. If small d remain open, state the best known bounds for d = 3, 4 on both sides (factor-of-iid constructions versus the
   random-regular maximum) and explain the obstruction.
3. Prove what you can, with complete proofs: the inclusion that holds in general (every factor-of-iid density is achievable on
   random regular graphs), and an explicit d for which the conjecture fails, with numbers from the cited theorems.
4. Compute (evidence only): for d = 3, best density from simple local algorithms versus the maximum independent set density
   on sampled random cubic graphs (exact for small n, heuristics larger).
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
