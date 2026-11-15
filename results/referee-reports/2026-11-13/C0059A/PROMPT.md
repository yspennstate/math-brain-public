Open problem C0059. Source: N. Curien, "Peeling random planar maps", Saint-Flour lecture notes 2019 (Lecture Notes in Math.
2335, Springer 2023; preprint on the author's web page), open question p. 93 of the preprint: let q be a critical weight
sequence of type a in [2, 5/2); is the dual map m-dagger of the infinite Boltzmann map of the plane transient for simple random
walk under P^{(1)}_infinity? (Read the source for the exact setting: types a in (3/2, 5/2], the dilute phase a in (2, 5/2), the
dense phase a in (3/2, 2), the case a = 2, the infinite Boltzmann map of the plane, and the results the notes already give on
recurrence/transience of the primal and dual maps, with the methods used: electrical networks, peeling, resistance bounds.)

Do this, in order, saving as you go:
1. Literature first. Get the lecture notes text into sources/ (plain text only) and read the chapter on simple random walk
   (recurrence of the primal maps, the dual in the dense phase, what is known for a in [2, 5/2)), and the open question exactly.
   Search 2017-2026 work (Budd-Curien "Geometry of infinite planar maps with high degrees"; Budd-Curien-Marzouk "Infinite random
   planar maps related to Cauchy processes"; Gurel-Gurevich and Nachmias recurrence; Curien-Marzouk; Budzinski-Curien;
   Timothy Budd; Kammerer; Bjornberg-Stefansson; "resistance growth" or "transience of the dual" of Boltzmann maps; Le Gall and
   Miermont on large faces) for an answer. If it is answered in print, give the exact reference and theorem and stop with
   REPORT.md first line RESOLVED_IN_LITERATURE.
2. Understand the dichotomy. Explain why the dual is transient in the dense phase (the argument in the notes) and what breaks
   for a in [2, 5/2): the face degrees, the perimeter process, and the resistance from the root face to infinity in the dual.
3. Prove or disprove. Try to decide transience of the dual for a in [2, 5/2), or for part of that range (for example a = 2, or
   a close to 5/2), with complete proofs: lower bounds on resistance via disjoint cutsets from the peeling layers (Nash-Williams)
   for recurrence, or a flow of finite energy built along a peeling exploration for transience. A partial result covering part
   of the range, or a precise reduction to a statement about the perimeter random walk, is worth writing up carefully.
4. Compute (modest, as evidence only). Simulate peeling-layer cutsets or effective resistance on large finite approximations
   for a few values of a and report the growth.
Write REPORT.md. Its first line is exactly one of PROVED, COUNTEREXAMPLE, PARTIAL, NO_PROGRESS, RESOLVED_IN_LITERATURE.
Then the statement, the proof, what was checked and how, and the literature result with exact theorem numbers and pages.
Keep LOG.md as you go. Code in code/, data in data/. Source texts may go in sources/ as plain text only; no PDFs kept, no
page images or scans of any paper or book anywhere in this folder. Work only in this directory. At most 4 threads, under
4 GB, nice 10. No publication anywhere, no pushes.
