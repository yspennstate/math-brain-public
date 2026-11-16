---
name: d0069_grimmett_li_multigraph_saw_bound_open_atom_reduction_2026_11_13
description: "[PROVISIONAL] D0069 (Grimmett-Li survey Q2.2: mu >= sqrt(Delta-1) for transitive multigraphs, non-simple Delta>=5) still open in print (13 Nov); atom reduction + numerics, no counterexample, ratio >= 1.147 off the bridge graph"
metadata:
  type: project
status: provisional
---
D0069 from the 200 list: Grimmett-Li (arXiv 1704.05884, Q2.2) ask whether mu >= sqrt(Delta-1) holds for every
transitive loopless multigraph. GL arXiv 1210.6277 Thm 4.1 proves it for simple graphs and for non-simple Delta <= 4;
the bridge graph (Z, multiplicities alternating 1 and Delta-1) gives equality. A web search on 13 Nov found no answer
for non-simple Delta >= 5 (GL 2017 EJC and Grimmett arXiv 2608.19349 are about simple graphs).

Reduction (mine, unrefereed). Let lambda be the least edge boundary of a finite vertex set. Atoms (finite sets with
boundary lambda, of least size) are equal or disjoint by submodularity, so Aut(G) permutes them: blocks of size a,
each vertex with e = lambda/a external edges. If lambda = Delta, Menger plus compactness give Delta edge-disjoint
infinite SAWs, hence GL's condition Pi and the bound. So a counterexample needs a >= 2 and lambda < Delta; a = 2,
e = 1 forces the bridge graph (equality). Open cases: a = 2 with e >= 2 (heavy edge m = Delta - e > e), and a >= 3.

Numerics (weighted SAW counts by DFS, scratch area d0069/saw_multi.py, line_pq.py; mu from sqrt(c_N/c_{N-2}), N 14-30).
Smallest ratio mu/sqrt(Delta-1) off the bridge graph: 1.147 (ladder Z x K2, rung 4, Delta 6); 28 pair-atom line
graphs with e 2..6 all >= 1.147 and the ratio grows with e. Ladder with rung c satisfies mu^2 = mu + c exactly
(transfer matrix), which clears the bound for e = 2. Triangle atoms on 3.12^2 with doubled edges: mu ~ 2.565 vs 2.
The D_inf x Z_2 scan with second-neighbour edges timed out at N = 18 (Python too slow); not run.

How to apply: treat D0069 as open with a plausible yes. The next real step is a proof for a = 2, e >= 2 by a transfer
argument (cross or skip each atom), which the ladder identity suggests; a counterexample, if any, needs few forward
external edges per vertex and m close to e. Notes: scratch area d0069/NOTES.md items 1-6 (move to the brain with the
problem folder when written up).
