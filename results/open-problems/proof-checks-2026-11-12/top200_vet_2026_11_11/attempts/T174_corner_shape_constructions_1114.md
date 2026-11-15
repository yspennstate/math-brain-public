# T174 (p_max of 1-independent bond percolation on Z^2): corner-shape constructions, 14 Nov 2026

State of the row (read from Balister-Johnston-Savery-Scott arXiv:2206.12335v2, Sec. 4):
rigorous 0.555197 = (35 - 3 sqrt 33)/32 <= p_max(Z^2) <= 0.8457; high-confidence p_max > 0.5921.
The rigorous lower bound is inf_x max(1 - 3x/4, x^2 + (1-x)/2), the two constructions crossing at
x = (sqrt(33) - 1)/8 = 0.59307, which is 0.0003 above the estimated p_site(Z^2) = 0.592746. So no
rigorous bound on p_site can improve it: one would need p_site < 0.59307 proved, a 0.0003 window.
A rigorous gain needs a construction whose non-percolation reduces to a threshold known exactly.

Setting. Write Z^2 = even sublattice (faces) + odd sublattice M (corners of those faces). If only
the even vertices carry randomness, each face f opens a random subset S_f of its four corners and
fuses them; edge (f,c) is present with probability P(c in S_f). If the "connector" faces use one
fixed shape S and all other faces open a single corner (dead ends), connector faces f and f+d are
linked iff d = pos(k) - pos(k') for corners k, k' in S. Hence:
- |S| = 4 (BJSS): 8-neighbour matching lattice, threshold 1 - p_site; coverage (1 + 3a)/4.
- |S| = 3, e.g. S = {SW, SE, NE}: offsets +-(1,0), +-(0,1), +-(1,1), i.e. exactly the triangular
  lattice, and three faces sharing a corner form a triangle, so connector clusters are site clusters
  of the triangular lattice, p_c = 1/2 exactly with no percolation at 1/2. This gives a rigorous,
  p_site-free construction, but coverage is at most (3a + (1-a))/4 = (1 + 2a)/4 <= 1/2 at a = 1/2.
  Worse than 0.5552.
- |S| = 2: lines, no percolation at any density, coverage (1 + a)/4 <= 1/2.
- Mixing shapes breaks the exact reduction: a {SW,SE,NE} face and a {SW,NE,NW} face differing by
  (1,-1) link through their shared corner, so the adjacency is no longer triangular.
Adding randomness at the odd vertices (a corner c opening the edge to the face it is the NW corner
of, with probability r) restores the missing corner's coverage, but it adds the (-1,1) links
independently with probability r. The result is a mixed site-bond model on the triangular lattice
plus random anti-diagonals, which has no exactly known threshold. A non-connector face reached on
two edges also becomes a connector. Not rigorous.

Verdict: no improvement. Single-sublattice corner-shape constructions with an exact threshold top
out at coverage 1/2 (triangular) or need p_site (matching lattice). A rigorous gain would need a
two-sublattice rule whose clusters embed in an exactly solved model (triangular site at 1/2, or
square/triangular/hexagonal bond). None was found. Row unchanged.
