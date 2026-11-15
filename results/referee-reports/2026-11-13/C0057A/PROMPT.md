Open problem C0057. Source: N. Curien, "Peeling random planar maps", Saint-Flour lecture notes 2019 (Lecture Notes in Math.
2335, Springer 2023; preprint on the author's web page). Open question after Corollary 27, p. 61 of the preprint: Corollary 27
shows that for a critical weight sequence of type a in [3/2, 5/2] a filled-in peeling exploration of the infinite Boltzmann map
almost surely exhausts the map; is this true for every critical weight sequence? (Read the source for the exact definitions:
critical / subcritical / generic critical weight sequences, types a in (3/2, 5/2], the infinite Boltzmann map of the plane,
filled-in versus simple peeling, the peeling algorithm class allowed, and what "exhausts" means.)

Do this, in order, saving as you go:
1. Literature first. Get the lecture notes text into sources/ (plain text only) and read Corollary 27, its proof and the open
   question exactly. Note what "every critical weight sequence" adds beyond types a in [3/2, 5/2]: are there critical weight
   sequences of no type (non-regularly-varying tails, oscillating), and is that the real content? Search 2017-2026 work
   (Budzinski; Budzinski-Curien; Curien-Marzouk; Timothy Budd "The peeling process of infinite Boltzmann planar maps";
   Budd-Curien "Geometry of infinite planar maps with high degrees"; Curien-Richier; Marzouk; Kammerer; Ambjorn-Budd) for an
   answer. If it is answered in print, give the exact reference and theorem and stop with REPORT.md first line
   RESOLVED_IN_LITERATURE.
2. Reduce. The peeling process of the infinite Boltzmann map is a random walk (perimeter process) conditioned to stay positive,
   with step law nu built from q. Express "filled-in peeling exhausts the map" as a statement about that walk (for example,
   every face at finite distance is eventually swallowed; the number of steps needed to swallow a fixed ball is finite a.s.),
   and identify exactly which property of nu the proof of Corollary 27 uses (regular variation, a moment condition, the
   h^-transform). Decide whether that property holds for every critical nu, using only criticality (the h^-harmonic function
   h^(p) and the identity behind it).
3. Prove or find a counterexample. Either prove exhaustion for every critical weight sequence, or construct a critical weight
   sequence (for instance with oscillating tails between two types) for which a filled-in peeling exploration provably fails
   to exhaust the map with positive probability, with a proof. A partial result (a new class of sequences covered, or a
   precise reduction to a random-walk statement) is worth writing up carefully.
4. Compute (modest, as evidence only). Simulate the perimeter walk for a few weight sequences, including an oscillating one,
   and look at the time to swallow the root face's neighbourhood.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
