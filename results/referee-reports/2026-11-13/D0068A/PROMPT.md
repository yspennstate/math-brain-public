Open problem D0068. Source: G. R. Grimmett and Z. Li, a 2017 survey on self-avoiding walks and connective constants (find it by
authors and title words "self-avoiding walks", "connective constants"), Question 1.4, Section 1.3, PDF p. 7: let I be the
infinite cluster of supercritical bond percolation on Z^2 with p > 1/2 and sigma_n(v) the number of n-step self-avoiding walks
on I starting at v. Does mu(v) = lim_n sigma_n(v)^{1/n} exist almost surely, and is mu(v) = mu(w) a.s. on {v, w in I}?
Read the source for the exact wording.

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only). Search: Lacoin ("Non-coincidence of quenched and annealed
   connective constants on the supercritical planar percolation cluster", PTRF 2014; "Existence of a non-averaging regime for
   the self-avoiding walk on a high-dimensional infinite percolation cluster", JSP 2014), Chen-Shao, Le Doussal-Machta,
   Grimmett-Li later papers, Duminil-Copin, "quenched connective constant", "SAW on percolation cluster", 2014-2026 citers.
   Decide exactly what is known: is the limsup a.s. constant (ergodicity), and is the existence of the limit (not limsup)
   proved anywhere? If both halves are answered in print give the theorem and page and stop with RESOLVED_IN_LITERATURE.
2. Understand the gap: why submultiplicativity (Fekete) fails on a random cluster, what the limsup constancy proof uses
   (tail triviality / translation ergodicity), and what could make liminf < limsup (rare long corridors, regions of
   anomalously high local growth at distance n).
3. Prove what you can, with complete proofs: constancy of limsup and liminf separately; existence of the limit along a
   subsequence or in probability; existence of lim (1/n) E log sigma_n(0) on {0 in I}; a.s. existence for p close to 1; or an
   example of a different translation-invariant random subgraph of Z^2 where the limit fails to exist, showing what any proof
   must use.
4. Compute (evidence only): exact SAW enumeration on sampled clusters for p in {0.6, 0.75, 0.9}, n up to the feasible size,
   comparing sigma_n(v)^{1/n} across v and n.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
