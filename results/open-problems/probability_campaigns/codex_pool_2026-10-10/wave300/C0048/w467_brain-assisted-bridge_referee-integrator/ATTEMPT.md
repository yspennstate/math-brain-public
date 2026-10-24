# C0048 referee and brain-assisted bridge

The primary statement is Duminil-Copin, Conjecture 2: critical spontaneous magnetization for the nearest-neighbor ferromagnetic integer-q Potts model on Z^d, all q>=3 and d>=3. In his notation, discontinuity is (MAG_beta_c): the monochromatic-boundary infinite-volume state has positive magnetization at beta_c. The FK form is positive wired critical connection probability from 0 to infinity, with the usual Potts/FK coupling conversion. The title alone does not imply an energy-density jump at beta_c.

## Peer checks

**w465-L1: KEEP, scoped.** The finite-graph conditional probability of an edge is p when its endpoints are already connected without that edge (with the boundary partition applied), and p/[p+q(1-p)] otherwise. Averaging yields w465's identity. This is an exact elementary observation. No positive free/wired difference at p_c follows from it, and an edge-density difference must not be silently substituted for the target magnetization.

**w466-C0048-001: KEEP, scoped.** Independently calculate epsilon log(1+exp(x/epsilon))-max(0,x)=epsilon log(1+exp(-abs(x)/epsilon)); its supremum is epsilon log 2. The approximation is smooth convex with continuous derivative. Therefore a uniform pressure approximation cannot alone transfer a kink. The calculation says nothing against the Potts conjecture itself.

## Hardest load-bearing bridge

Biskup-Chayes 2003 Theorem 2.1 proves a magnetization and energy jump for each fixed integer q>=3 when d is sufficiently large. Main Theorem (1.12) requires a suitable translation-invariant extreme-state magnetization and bounds its mean-field free-energy excess by J(q-1)^2 I_d/(2q); the latter tends to zero as d grows. The Potts theorem's own caveat says it cannot conclude that the magnetization vanishes below its jump coupling J_t. Therefore Theorem 2.1 alone does not give J_t=J_c, and its asymptotic error gives no d=3,q=3 estimate. An added quantitative barrier and a mechanism excluding an earlier small ordered phase would be needed before this route proves (MAG_beta_c). This is a gap statement, not a new theorem or a parent-problem proof.

## Brain measurement and bounded repair

Read-only command: `python -X utf8 ~/brain_workers/w467/inspect_store.py`, against `math-brain-build/local/population/brain.sqlite3` with SQLite `mode=ro`. It found 30 Potts-title nodes and **0 cards matching the exact Biskup-Chayes paper title or arXiv ID**. The C0048 node had 4 direct edges: generic phase-transition concept, generic FK/Potts concept, the lecture source, and the old attempt; no partial-theorem edge. The first broad 'Biskup' body search produced 38 nodes dominated by a different DGFF source, a lexical ambiguity. The bounded repair is a local DRAFT bundle of 4 entries and 6 relations: paper, main bound, fixed-q/large-d Potts jump, and explicit critical-onset gap. Two relations target the existing C0048 logical ID, both typed semantic_association so they cannot be read as proof. No live-store improvement is claimed because the bundle has not been ingested or tested in live recall.

The independently rederived q=3,d=3 separator check gives B=log 3-(19/12)log 2=0.00112925278153 and a **lower bound on the published allowance**, J0/9=0.308065413582, a ratio of 272.804653. Command: `python -X utf8 -c "import math; b=math.log(3)-19*math.log(2)/12; e=4*math.log(2)/9; print(b,e,e/b)"`. This only shows that this allowance cannot exclude this selected intermediate mean-field vector.

Current openness remains UNKNOWN after bounded checks. The hardest unresolved proof step is positive wired critical connection probability for q=3,d=3 with a uniform argument covering all integer q>=3,d>=3. No claimed proof has passed an independent referee.
