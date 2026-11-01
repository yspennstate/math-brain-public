# P0257 idea refinement — widen the new asymmetric D2 sink class before certifying the metric

The first missing-topology probe succeeded, but its shape volume `1/31250` is unnecessarily small. Before treating that checker as the run's metric certificate, widen the same genuinely new topology in a direction that keeps exact inequalities transparent.

Write

`p1=(0,0), p2=(1,0), p3=(x,-r), p4=(z,-s)`.

For the topology

`N2(p1)={p2,p4}, N2(p2)={p1,p4}, N2(p3)={p1,p4}, N2(p4)={p2,p3}`,

a sufficient strict system is

- `x<1/2`;
- `x^2+r^2>1`;
- `x^2+r^2>z^2+s^2`;
- `z>1/2`;
- `x(2z-x)+r(2s-r)>0`;
- `(1-z)^2+s^2<1` (a convenient redundant separator at p2).

A much larger rational box still satisfies these inequalities:

`13/100 <= x <= 49/100`,

`29/25 <= r <= 7/5`,

`51/100 <= z <= 81/100`,

`33/50 <= s <= 21/25`.

Its normalized shape volume is `729/156250 = 0.0046656`, more than two orders of magnitude larger than the first probe. The tight topology margins are expected at `d13^2-d14^2 = 1/1250` and `d14^2-d34^2 = 37/10000`, still strictly positive.

For the source-valid guard, target a common internal second-neighbor envelope `U=297/200` and external radius `H=37/20`, leaving boundary surplus `H-U=73/200`. All centers lie in the rectangle `[0,1] x [-7/5,0]`, so a rational Steiner rectangle-parallel-body bound can control the void area.

This refinement does not add the first narrow-box correction. The final certificate, if successful, will use only this larger family, so overlap between two parameter boxes is irrelevant. The mathematical novelty remains the new non-isomorphic D2 sink topology and topology-independent Hamiltonian boundary charge, not a decimal optimization.
