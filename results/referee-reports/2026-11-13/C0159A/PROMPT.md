Open problem C0159. Source: O. Haggstrom and J. Jonasson, "Uniqueness and non-uniqueness in percolation theory", Probability
Surveys 3 (2006), Section 6, PDF pp. 20-21: cluster repulsion (Haggstrom-Peres-Schonmann). For Bernoulli percolation on a
transitive graph at a p with infinitely many infinite clusters, is it true that almost surely no two distinct infinite clusters
come within distance one of each other along an infinite set of vertices? Timar (2006) proved it for unimodular transitive
graphs by mass transport. Read the source for the exact statement and conventions.

Do this, in order, saving as you go:
1. Literature first. Get the survey text into sources/ (plain text only) and read Section 6. Read Timar, "Neighboring clusters
   in Bernoulli percolation" (Ann. Probab. 2006), and Bell-Chu-Rodgers-Terlov-Tserunyan arXiv:2509.10631 (2025), who proved for
   nonunimodular quasi-transitive graphs that for two heavy clusters the touching set has finite total weight. Search for
   anything later: Hutchcroft on nonunimodular percolation (heavy and light clusters, pc < pu for nonunimodular graphs), Tang,
   Timar, Lyons-Schramm indistinguishability, Haggstrom-Peres-Schonmann, Pete, Benjamini-Lyons-Peres-Schramm, and 2025-2026
   work citing 2509.10631. If it is answered in print, give the exact reference and theorem and stop with REPORT.md first line
   RESOLVED_IN_LITERATURE.
2. Understand the gap. State exactly what BCRTT prove and what remains (light clusters; finiteness of the touching set rather
   than finite weight; a heavy cluster against a light one). Explain why the unimodular mass transport fails and what the
   tilted mass transport principle (with the modular function) gives instead.
3. Prove what you can, with complete proofs: the full conjecture; or finiteness for two heavy clusters; or the heavy/light
   case; or the conjecture on a natural class (a Cayley graph times a regular tree, grandparent graphs, Diestel-Leader graphs,
   free products with a nonunimodular factor). Or a counterexample, if one exists.
4. Compute (modest, evidence only). Simulate percolation on a finite piece of a grandparent graph or another nonunimodular
   tree-like graph in the non-uniqueness phase and count adjacencies between large clusters by level.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
