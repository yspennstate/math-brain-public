Open problem C0149. Source: G. Pete, "Probability and Geometry on Groups" (lecture notes, find the current version by title on
the author's page), Conjecture 14.4 (Bowen), p. 201: any Cayley graph of a Kazhdan (property (T)) group can be Benjamini-
Schramm approximated only by essential expanders: there is c > 0 such that for every eps > 0 and every sufficiently far
approximating graph G_n one can remove eps|V(G_n)| vertices so that every remaining component is a c-expander. Read the source
for the exact wording (bounded degree, sofic approximation versus local convergence, the expansion notion: vertex or edge
Cheeger constant, c depending on the group and generating set only).

Do this, in order, saving as you go:
1. Literature first. Get the notes into sources/ (plain text only) and read Chapter 14 exactly, including the surrounding
   results (Lyons-Nazarov, Abert-Elek, hyperfiniteness and amenability, Schramm's hyperfinite characterisation). Search:
   L. Bowen's original statement and any paper titled or about "essential expanders", "property (T) and sofic
   approximations", "Kazhdan groups and Benjamini-Schramm limits", Kun ("On sofic approximations of property (T) groups",
   arXiv 2016, which I believe proves Bowen's conjecture or a form of it - check exactly what it proves), Abert-Jaikin-Zapirain-
   Nikolov (rank gradient), Elek ("Finite graphs and amenability"), Hutchcroft-Pete (cost and property (T)), Kun-Thom, and
   2010-2026 work citing Pete's notes or Kun. If the conjecture is proved in print, give the exact reference and theorem with
   page, check that its hypotheses and its expansion notion match the source's statement (c uniform, eps arbitrary), and stop
   with REPORT.md first line RESOLVED_IN_LITERATURE. If a weaker form is proved, state the gap exactly.
2. Understand the gap if one remains: write out the proof idea (spectral gap of the Markov operator on the approximating
   graphs via the property (T) Kazhdan constant applied to an ultraproduct / graphing; where the eps-removal comes from), and
   identify the precise step that would fail for the strong form.
3. Prove what you can, with complete proofs: the missing step, a uniform c in terms of the Kazhdan constant of the
   generating set, or the statement for a natural class (lattices in higher-rank groups, groups with strong property (T)).
4. Compute (evidence only). For SL(3, Z/pZ) Cayley quotients and random lifts / perturbations that are Benjamini-Schramm
   close to the Cayley graph of SL(3, Z), compute spectral gaps and Cheeger estimates of the components after removing small
   sets; also a negative control with an amenable or Haagerup group.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
