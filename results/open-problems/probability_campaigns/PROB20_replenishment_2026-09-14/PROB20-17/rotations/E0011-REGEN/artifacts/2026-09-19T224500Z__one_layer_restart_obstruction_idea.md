# E0011 B30 idea — one-sacrificial-layer damaged states cannot be RETRY endpoints

Written before the supplemental exact checker. This is a local design obstruction, not source closure and not metric movement.

## Geometry

Start from the 4x4 neutral annulus: ring R is the perimeter of [0,3]^2, the 2x2 strict interior is O, and outside is CO. Use one sacrificial CO shell S given by the outer boundary of [-1,4]^2 and one farther quarantine CO shell Q given by the outer boundary of [-2,5]^2.

An O2 event on a ring edge returns its two ring endpoints to vacancy after instantaneous O-CO reactions and removes two S-shell CO atoms, producing two S vacancies. As in the preceding idea artifact, the two S defects are either ADJACENT or SEPARATED.

Question: can either damaged state itself be declared RETRY, so that the next regenerative trial restarts immediately from it, while any removal of a Q-shell CO is FATAL?

## Adjacent damaged state

Take adjacent defects d1=(1,-1), d2=(2,-1), obtained for example from the top middle ring edge. The post-O2 state has V=14 and E_00=15, so at p=1/2 its total scaled effective rate is

2V+E_00 = 43.

The defect pair d1 d2 is a 00 edge. If the next event is O2 on this edge (weight 1), each new O has exactly two adjacent CO atoms: one lateral S-shell CO and one outward Q-shell CO. The two reaction-choice sets are disjoint. Hence, under equal r/4 reaction clocks and r=infinity, each O removes its Q neighbor with probability 1/2 and the probability that at least one Q CO is removed is

1-(1/2)^2 = 3/4.

Therefore a Q-breach subevent has exact probability

(1/43)*(3/4) = 3/172 > 1/64.

If Q breach is FATAL, any trial restarted from this adjacent-defect state has f>=3/172, hence

a-63f <= 1-64f <= 1-64*(3/172) < 0.

So this state cannot be a RETRY endpoint in any positive-M_reg certificate with this one-layer quarantine convention.

## Separated damaged state

Take separated defects d1=(-1,0), d2=(1,-1), the representative obtained from a corner-adjacent ring O2 event when the corner O reacts perpendicular to the ring edge. The post-O2 state has V=14 and E_00=14, so total scaled effective rate is 42.

There are two ring-defect 00 edges, one incident to each defect. If the next event is O2 on either such edge, the O created at the S-shell defect has three adjacent CO atoms: two S-shell neighbors and one outward Q-shell neighbor. Thus it removes Q with probability 1/3. The two possible next O2 edges are disjoint alternatives, each weight 1, so the exact Q-breach subevent has probability

2*(1/42)*(1/3) = 1/63 > 1/64.

Thus the same a-63f argument rules out this state as a RETRY endpoint if Q breach is fatal.

## Consequence for the regenerative design

With only one sacrificial shell and an intact outer quarantine shell, the two natural damaged states produced by the first ring-O2 event are too dangerous to be uniform restart seeds. A viable positive-M_reg trial must therefore do at least one of the following:

1. continue the same trial through the damaged-collar excursion and declare RETRY only after healing back to a safer annular seed;
2. use a deeper sacrificial buffer so that the first damaged shell is not adjacent to the fatal quarantine frontier;
3. redefine the protected-exterior argument so one Q-shell removal is not terminal.

This validates the strict two-refill exact RETRY event from the preceding artifact as a meaningful safe self-loop, while showing why 'soft collar = immediately retry on any collar defect' is not sufficient.
