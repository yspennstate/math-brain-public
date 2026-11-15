Open problem I0006. Source: arXiv:2609.02820 (identify the title, authors, date and version exactly from the arXiv listing). In its
Section 3, after the statement of the odometer asymptotics, the source proves for d >= 5 that c (log n)^{2/d} <= E u_n(0) <= C log(n+1)
in general, with E u_n(0) asymptotic to (log n)^{2/d} when eta(0) is bounded below, and says: "When eta(0) is not bounded below, the
exact rate in dimensions at least five depends on its lower tail." State the exact model: what u_n is (the odometer of which
process: divisible sandpile, abelian sandpile, parking, internal aggregation; on which box or torus of size n; with what boundary
condition), what eta is (i.i.d. field, which moments, mean or criticality assumptions), and which theorem of the source and of the
paper it cites contains the bounds and the bounded-below asymptotic. The question: determine the order of E u_n(0) for d >= 5 as a
function of the lower tail P(eta(0) < -t).

Do this, in order, saving as you go:
1. Literature first. Get the source into sources/ as plain text and state, with page numbers, the theorem with the bounds, its proof
   idea (where (log n)^{2/d} comes from: the extreme value of a field, the largest hole, a variational or Green-function argument),
   and the cited primary papers (Levine-Peres divisible sandpile, Levine-Murugan-Peres-Ugurcan "The divisible sandpile at critical
   density", Cipriani-Hazra-Ruszel and co-authors on random divisible sandpiles and odometer scaling, Chiarini-Cipriani-Hazra,
   Damron-Gravner-Junge-Lyu-Sivakoff and Bahl-Junge-Lyu and others on parking, as relevant). Find the exact paper and theorem that
   proves the general bounds; read its proof. Search for later work (2026). If a printed result answers the question, report it and
   stop with RESOLVED_IN_LITERATURE.
2. Otherwise attack it. First decide the heuristic: if E u_n(0) is driven by the deepest hole (most negative values) in a region
   of size n^d or by a sum of local deficits, the answer should be a functional of the lower tail, e.g. for P(eta < -t) ~ exp(-t^a)
   versus polynomial tails. Prove matching upper and lower bounds for as broad a class of lower tails as you can (state the class
   exactly: e.g. tails between Gaussian and exponential, Weibull exp(-t^a), polynomial t^(-p) with enough moments for the model to
   be defined), with every constant and every step checked. A sharp order for a natural class (all Weibull tails, or all tails with
   a stated regularity) is PROVED; a sharp order for some tails and bounds for others is PARTIAL.
3. Compute only to check (small exact or numerical solutions of the odometer on boxes for d = 5 are expensive; low-dimensional
   analogues and the one-site variational problem are fine). Keep runs small; no simulation stands in for a proof.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature results with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
