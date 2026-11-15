Open problem F0126. Source: F. den Hollander and J. E. Steif, "Random walk in random scenery: a survey of some recent
results" (2006; find it by authors and title), Open question 7, Section 4, PDF p. 11: is scenery reconstruction possible for an
arbitrary recurrent random walk with i.i.d. increments and an arbitrary i.i.d. random scenery? That is, given only the
observations Y_n = C_{S_n}, n >= 0 (S the walk, C an i.i.d. scenery on Z^d with values in a finite set G), can C be recovered
almost surely up to the natural equivalences (translation, reflection)? Known (Section 3, PDF p. 10): Matzinger (F = {-1,+1},
|G| = 3; F = {-1,0,+1}, |G| = 2), Lowe-Matzinger-Merkl (|F| < |G|), Lember-Matzinger (F subset of {-1,0,+1}, |G| = 2), all
d = 1 with uniform laws; in d = 2 Lowe-Matzinger need |G| very large. Read the source for the exact definition of
reconstruction (a.s. up to which equivalence; distinguishing two sceneries versus reconstructing a typical one).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ (plain text only) and read Sections 3-4 exactly. Search: Matzinger's
   thesis and papers (2- and 3-colour reconstruction), Lowe-Matzinger-Merkl ("Reconstructing a multicolor random scenery seen
   along a random walk path with bounded jumps", EJP 2004), Lember-Matzinger, Matzinger-Rolles (reconstruction with errors,
   polynomial time), Hart-Matzinger ("Markers for error-corrupted observations"), Lindenstrauss ("Indistinguishable sceneries",
   1999: uncountably many non-reconstructable sceneries), Howard (distinguishing sceneries), Benjamini-Kesten (distinguishing
   sceneries by observing the scenery along a random walk path), Kesten ("Distinguishing and reconstructing sceneries from
   observations along random walk paths"), Popov-Pachon ("scenery reconstruction for random walk with jumps", "heavy-tailed
   jumps"), Matzinger-Popov, Lowe-Matzinger d = 2, and 2006-2026 work. Determine for which (walk, scenery) classes
   reconstruction is proved, and whether a negative result (a recurrent walk and an i.i.d. scenery for which a.s.
   reconstruction fails) exists. If the question is answered in print in either direction for the general statement, give the
   exact reference and theorem and stop with REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the gap: explain the marker / signal-carrier method and why it needs bounded jumps or |F| < |G|; explain the
   obstruction for walks with large or unbounded jumps and for |G| = 2 with general increments; consider walks with
   increments of a common factor or periodic structure, where only a sublattice is visited (is reconstruction up to that
   sublattice the intended notion?).
3. Prove what you can, with complete proofs: reconstruction for a new class (for instance increments {-2,-1,0,1,2} with
   |G| = 2, or symmetric walks with finite support of size at most 2|G| - 1), distinguishability results, or a counterexample
   to the general statement as literally posed (a recurrent i.i.d.-increment walk for which a typical i.i.d. scenery is a.s.
   not determined by the observations, e.g. through a hidden symmetry of the increment law).
4. Compute (evidence only). Implement a reconstruction algorithm for a small new class and test it on simulated observations;
   for candidate counterexamples, estimate total-variation distances between observation laws for two sceneries differing
   locally.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
