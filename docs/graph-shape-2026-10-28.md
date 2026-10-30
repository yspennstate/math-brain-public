# How wide the brain's graphs are (28 October 2026)

The brain keeps three graphs: the memory graph (written notes and the links between them), the math store
(claims, sources and evidence, joined by `depends_on`, `cites`, semantic and other edges), and the event graph
(files, commands, tools, keywords and recalled notes from every session, joined by sequence and co-occurrence).
On the morning of 28 October we measured the radius and diameter of each.

Distance is the number of hops, with every edge taken in both directions. The radius is the smallest, over all
nodes, of a node's distance to the node farthest from it; the diameter is the largest shortest distance between
two nodes. None of the three graphs is connected, so the figures are for the largest connected component of each.
They are exact: an eccentricity-bounding search closed the gap between its lower and upper bounds after 16, 4
and 4 breadth-first searches. Mean distance and the 90th percentile come from full
searches out of 120 random nodes in each component.

| Graph | Nodes | Edges | Components | Largest component | Radius | Diameter | Mean distance | 90% of pairs within |
|---|---|---|---|---|---|---|---|---|
| Memory graph | 36,256 | 121,590 | 1,556 | 34,694 (96%) | 10 | 17 | 4.89 | 7 |
| Math store | 86,403 | 24,526 | 71,607 | 8,652 (10%) | 20 | 39 | 7.34 | 11 |
| Event graph | 326,383 | 11,177,990 | 27,360 | 299,022 (92%) | 3 | 6 | 2.37 | 3 |

The math store was locked by a writer at the time, so it was read from that morning's backup (86,403 nodes; the
live store had 86,605).

## What the shape says

The event graph is a small world. Any two of its connected nodes are at most six hops apart and a typical pair is
two or three. A few hubs do this: the generic "run a Python command" node is the centre, within three hops of
everything, and the busiest node has about 167,000 neighbours. Hubs that general carry almost no meaning, which is
why recall over the event graph has to discount them rather than follow them.

The memory graph is about three times longer. Its centre is the hub note for compactions, at most ten hops from
every connected note. The longest shortest paths end in old project notes that hang off long chains, and a recall
that walks the graph reaches those late or not at all.

The math store was the stretched one. Only one card in ten sat in the connected component, and that component was
a long chain: diameter 39, mean distance 7.3. The longest path ran from a card on the classical toolkit behind a
theorem in an arXiv paper to the Paris-Harrington theorem, mostly over `depends_on` links, with "compact space" at
the centre. About 70,000 cards had no edge at all.

That measurement is what started the linking work described in [linking-the-store.md](linking-the-store.md). After
it, 90,679 of 90,893 cards touched an edge and the largest component held 91 percent of them. The radius and
diameter after linking have not been measured yet.

## Distance distribution

Share of pairs at each distance in the largest component (rows under 0.1 percent left out).

| Hops | Memory graph | Math store | Event graph |
|---|---|---|---|
| 2 | 11.0% | 0.5% | 64.6% |
| 3 | 9.9% | 2.1% | 33.6% |
| 4 | 19.6% | 8.4% | 1.8% |
| 5 | 22.9% | 17.1% | |
| 6 | 19.4% | 20.0% | |
| 7 | 11.4% | 15.7% | |
| 8 | 4.3% | 11.3% | |
| 9 | 1.2% | 7.5% | |
| 10 | 0.3% | 4.6% | |
| 11 | 0.1% | 3.0% | |
| 12 | | 2.3% | |
| 13 | | 2.0% | |
| 14 | | 1.6% | |
| 15 | | 1.3% | |
| 16 | | 0.9% | |
| 17 | | 0.6% | |
| 18 | | 0.4% | |
| 19 | | 0.2% | |
| 20-21 | | 0.2% | |
