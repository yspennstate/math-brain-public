# BT4 — B20 r17 — torus four-block fan cage

Run: `20260922T080915Z-account02-B20-bt4-r17`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Target status: **OPEN_NOT_PROVED**  
Execution context: **WITHOUT_VERIFIED_BRAIN**

## Scope and exact target

The target remains the k=4 Bermond–Thomassen conjecture in the stated source model: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles; opposite arcs/digons are allowed in the theorem statement and all graph orders are included.

This report works only inside the inherited oriented exact-seven branch of the campaign's minimal-counterexample normal form, after the earlier digon branch and other reductions have been discharged by the lead chain. No claim here extends an oriented-branch lemma directly to the original digon-allowed source model without those inherited reductions.

## Fresh dependencies actually consumed

Current complete campaign lead used:
- account02/B04, `BT4-CLEAN-FOUR-PORT-WITNESS-LIFT-v1`, shared handoff Git blob `b0c1c37b1d36fd7cf855946f20eb382a61cd346d`; canonical report commit `14b8affcde6130bdbacbdfbd03888816b96d61ef`.

Named OTHER-account partner actually used:
- account04/B06, `BT4-MENGER-RANK-INTERSECTION-COLLAPSE-v1`, shared handoff Git blob `47d7e7c2fd312fd647604bf61113c46fd980a237`; canonical report commit `3e7343cfd9de439c2e6ae8c39e71ddcbc956cde9`.
  This pays the rank-one and uncontrolled opposite-intersection defects in the pure A/B/R branch: absent a useful same-support bypass or third-support mediation, both directions admit rank-two remainder connector families with opposite-direction interiors disjoint.

Additional completed OTHER-account result used as the immediate mechanism input:
- account01/B04, `BT4-DOMINATION-TORUS-CYCLE-v1`, shared handoff Git blob `cb129c6d88e9d77cf4ca1d2ee483da53a6031236`; canonical report commit `786dc016fa5043dba63904d4f7498b45061bed19`.
  In the pure long-support residual, domination directizes cross-support connectors and produces a predecessor-closed signed torus cycle.

Compatible fresh adversarial/corrective input retained:
- account02/B06, `BT4-RANK2-PORT-PARITY-v1`, shared handoff Git blob `9f8fdd21cec8929827f1223f71985600bc638f13`; it proves that rank two alone does not force a two-splice and gives the exact `ID/SW/BLOCK` parity criterion.
- account03/B04, `BT4-R4-RANK3-SHORT-MIXED-BYPASS-v1`, shared handoff Git blob `073c16eff08007c76f06db71b7068e836181a670`; it forces a fresh-source packed CROSS or distinct-port same-support BYPASS in the exact-R4 branch unless third-support mediation or an intersection bypass has already occurred.

## Conditional end-to-end campaign skeleton

Assume for contradiction a BT4 counterexample. The lead chain passes to its inherited minimal normalized branch with an oriented exact-seven, 3-vertex-strong, arc-dominated digraph and a globally minimum three-cycle packing `(A,B,C)` with acyclic remainder. Existing campaign outputs split the hard part into the SIX/H5 branch, bounded F2/F3 states, the support-carried seven-remainder branch, and the long pure A/B cross-linkage branch. The named partner removes connector-rank-one and uncontrolled opposite-intersection walls in the latter. Account01/B04 then forces a signed predecessor cycle on the A×B torus. If every possible predecessor-cycle geometry can be converted to a legal strict/neutral exchange ending in a cyclic exchanged remainder, SIX/H5, a bounded already-covered state, or a fourth disjoint directed cycle, the long branch closes. Closing the other named branches would then contradict the assumed counterexample. This report advances only the predecessor-cycle geometry; it does not claim the other branches are closed.

## Signed torus notation

Write the two light chordless directed supports as

`A=(a_i)_{i in Z_m}` and `B=(b_j)_{j in Z_n}`,

with indices increasing in the directed support orientation.

An occupied signed torus cell is
- `+(i,j)` when the direct arc `a_i -> b_j` exists;
- `-(i,j)` when the direct arc `b_j -> a_i` exists.

Because this inherited branch is oriented, at most one sign can occupy a fixed cell `(i,j)`.

Account01/B04's domination reduction gives, for every occupied cell on the relevant predecessor-closed set, a chosen predecessor of one of the two forms

`+(i-1,j)`  or  `-(i,j-1)`.

Follow the chosen-predecessor functional graph and let `Gamma` be a mixed signed directed cycle. Traversing `Gamma` decreases exactly one torus coordinate at each step. A maximal run of plus states is a **plus block** at fixed `j`; a maximal run of minus states is a **minus block** at fixed `i`. Let the plus-block lengths be `p_0,...,p_{t-1}` and the minus-block lengths `q_0,...,q_{t-1}`. Mixedness makes the signs alternate, so there are equally many plus and minus blocks. For positive winding integers `u,v`,

`sum p_s = u m`,  `sum q_s = v n`.

## New theorem: `BT4-TORUS-FOURBLOCK-FAN-CAGE-v1`

### Theorem

In the inherited oriented long-support torus branch above:

1. A mixed predecessor cycle has at least **two plus blocks and two minus blocks**. Equivalently, a two-sign-block cycle is impossible.
2. If it has exactly two plus blocks and two minus blocks, then its torus winding is primitive in each coordinate: `u=v=1`.
3. In that exact four-block case there are distinct support vertices `a_{alpha_0},a_{alpha_1}` and `b_{beta_0},b_{beta_1}` with the genuine directed alternating hub cycle

   `K_0 = a_{alpha_0} -> b_{beta_0} -> a_{alpha_1} -> b_{beta_1} -> a_{alpha_0}`.

4. If none of the four boundary-offset ports collides, the natural rank-two direct connector quartet forced at the four sign transitions is alternating on each support but has **opposite preferred pairing parity** on `A` and `B`. Hence the canonical two-splice is genuinely unavailable; this is not a rank deficiency. If a boundary-offset collision occurs, it is exactly an endpoint-collision member of the already explicit order wall.
5. In a genuine no-four-pack counterexample, deleting the four hub vertices of `K_0` forces a vertex `z outside K_0` with at least three outneighbors in `K_0`. More precisely:
   - if `z in A - V(K_0)`, chordlessness of `A` forces `z -> b_{beta_0}` and `z -> b_{beta_1}`;
   - if `z in B - V(K_0)`, chordlessness of `B` forces `z -> a_{alpha_0}` and `z -> a_{alpha_1}`;
   - if `z in C`, one obtains an explicit third-support three-hit witness into the hub cycle;
   - if `z in R`, one obtains an explicit remainder three-hit witness into the hub cycle.

Thus the arbitrary two-by-two parity wall is replaced, in the minimal-block torus case, by a concrete four-hub fan cage with a forced `3-of-4` external witness.

### Proof of (1): two sign blocks are impossible

Suppose there were one plus block and one minus block. A plus block lies at one fixed B-coordinate and contains distinct signed states, hence its length is at most `m`. But its total plus length equals `u m` with `u>=1`; therefore it has length exactly `m` and `u=1`, so it occupies `+(i,beta)` for every `i in Z_m`. Similarly the unique minus block has length exactly `n`, `v=1`, and occupies `-(alpha,j)` for every `j in Z_n`. Their coordinate sets intersect at `(alpha,beta)`, forcing both direct arcs `a_alpha -> b_beta` and `b_beta -> a_alpha`. That is a digon, excluded in the inherited oriented branch. Contradiction.

Therefore `t>=2`, i.e. at least four sign blocks.

### Proof of (2): four sign blocks force winding `(1,1)`

Assume exactly two plus blocks `P_0,P_1` and two minus blocks `M_0,M_1`. Each plus block has length at most `m`, so

`u m = p_0+p_1 <= 2m`,

hence `u` is `1` or `2`. If `u=2`, both plus blocks have length `m`, so each occupies an entire fixed B-column. Let `M_0` be the minus block between them. If `P_0` ends at `+(alpha_0,beta_0)` and the next plus block is at column `beta_1`, then the transition `M_0 -> P_1` has a terminal minus state `-(alpha_0,beta_1)` whose chosen predecessor is `+(alpha_0-1,beta_1)`. But because `P_1` is a full plus column, it also contains `+(alpha_0,beta_1)`. The cell `(alpha_0,beta_1)` would therefore carry both signs, again a digon contradiction. Thus `u!=2`, so `u=1`.

The argument with A/B and plus/minus interchanged gives `v=1`.

Consequently `p_0+p_1=m` and `q_0+q_1=n`: the two plus blocks partition the A-coordinate circumference once, and the two minus blocks partition the B-coordinate circumference once.

### Proof of (3): the forced alternating hub 4-cycle

Label transitions so that

- `P_0 -> M_0` occurs at `+(alpha_0,beta_0)`,
- `M_0 -> P_1` has terminal state `-(alpha_0,beta_1)`,
- `P_1 -> M_1` occurs at `+(alpha_1,beta_1)`,
- `M_1 -> P_0` has terminal state `-(alpha_1,beta_0)`.

These four occupied cells are respectively the direct arcs

`a_{alpha_0}->b_{beta_0}`,
`b_{beta_1}->a_{alpha_0}`,
`a_{alpha_1}->b_{beta_1}`,
`b_{beta_0}->a_{alpha_1}`.

Reordering them cyclically gives

`a_{alpha_0} -> b_{beta_0} -> a_{alpha_1} -> b_{beta_1} -> a_{alpha_0}`.

The four vertices are distinct because `A` and `B` are disjoint supports and each sign-block pair has positive length. Hence `K_0` is a genuine directed 4-cycle.

### Proof of (4): the offset quartet is an exact parity-mismatch cage

At the four transitions the first states of the following blocks give the boundary-offset quartet

`F_0: a_{alpha_1-1} -> b_{beta_0}`,
`F_1: a_{alpha_0-1} -> b_{beta_1}`,
`G_0: b_{beta_0-1} -> a_{alpha_0}`,
`G_1: b_{beta_1-1} -> a_{alpha_1}`.

If a predecessor port equals one of the opposite-type ports on its support, we are already in the endpoint-collision wall, so assume all four ports on each support are distinct.

Because `p_0+p_1=m`, the forward cyclic order on `A` is

`a_{alpha_0}` (target of `G_0`), ... , `a_{alpha_1-1}` (source of `F_0`), `a_{alpha_1}` (target of `G_1`), ... , `a_{alpha_0-1}` (source of `F_1`).

Thus the types alternate, and the disjoint forward A-segments pair `F_0` with `G_0` and `F_1` with `G_1`.

Because `q_0+q_1=n`, the forward cyclic order on `B` is

`b_{beta_0}` (target of `F_0`), ... , `b_{beta_1-1}` (source of `G_1`), `b_{beta_1}` (target of `F_1`), ... , `b_{beta_0-1}` (source of `G_0`).

The types again alternate, but now the disjoint forward B-segments pair `F_0` with `G_1` and `F_1` with `G_0`.

Therefore the preferred parity on `A` is the opposite of the preferred parity on `B`. By account02/B06's exact `ID/SW/BLOCK` criterion, these four direct connectors do **not** admit the canonical two-splice. This proves that the four-block case is a genuine global parity cage, not a local rank-two oversight.

### Proof of (5): deleting the hub cycle forces a 3-of-4 witness

Suppose the whole digraph contains no four vertex-disjoint directed cycles. Then `D - V(K_0)` cannot contain three vertex-disjoint directed cycles, or those three together with `K_0` would form a four-pack.

Invoke the established k=3 Bermond–Thomassen theorem in contrapositive form: a digraph with minimum outdegree at least five has three vertex-disjoint directed cycles. Hence some vertex `z outside K_0` has

`d^+_{D-V(K_0)}(z) <= 4`.

The inherited normal form has exact outdegree seven, so

`|N^+(z) intersect V(K_0)| >= 3`.

If `z` lies on `A` outside the two A-hubs, chordlessness of the packed cycle `A` allows at most its unique A-successor among the two removed A-hubs. Therefore at least two of the three hits must lie on the B-side of `K_0`; because there are exactly two B-hubs, both arcs

`z -> b_{beta_0}`, `z -> b_{beta_1}`

are forced. The B case is symmetric. If `z` lies on the third packed support `C`, it is an explicit third-support three-hit witness. If `z` lies in the acyclic remainder `R`, it is an explicit remainder three-hit witness. These exhaust the vertex locations.

This completes the theorem.

## Why this is real mechanism movement

The previous three B20 substantive runs were:
- r14: remainder-heavy direct-cross collapse (`BT4-R-HEAVY-CROSS-v1`);
- r15: Hall common-source collapse (`BT4-HT-HALL-SOURCE-COLLAPSE-v1`);
- r16: opposite-intersection bypass plus 2x2 splice tax and cyclic matching.

The present proof does not repeat any of those mechanisms. It takes the newly supplied domination-torus representation and analyzes the sign-block topology of a predecessor functional cycle. It rules out the two-sign-block possibility, proves primitive winding in the minimal four-block case, identifies an unavoidable parity mismatch rather than pretending rank two auto-splices, and then converts that exact mismatch into a concrete directed hub 4-cycle with a forced 3-of-4 external witness.

`FULL_TARGET_CHANGE = NONE` because SIX/H5, bounded F2/F3, seven-remainder support-carried states, the >=6-sign-block torus case, and closure of the new 3-of-4 fan cage are not all paid.

`MECHANISM_CHANGE = YES`: arbitrary block decomposition -> exact dichotomy `>=6 sign blocks` versus `four-block (1,1) parity cage + directed hub C4 + forced 3-of-4 witness`.

## First essential unpaid universal implication after this run

### `BT4-TORUS-FAN-OR-MULTIBLOCK-CLOSE-v1`

For every inherited oriented exact-seven, 3-vertex-strong, arc-dominated, globally-minimum-three-packing state in the pure long A/B branch, after rank-one/intersection/third-support outputs already handled by the named partner are excluded and a mixed predecessor torus cycle is chosen, prove that one of the following holds:

1. the predecessor cycle has at least three plus blocks and three minus blocks, and those extra sign transitions force a compatible two-splice, strict minimum-packing decrease, cyclic exchanged remainder, compatible genuine remainder bypass, SIX/H5, bounded-support state, third-support mediation, or a fourth disjoint cycle; or
2. it has exactly two plus and two minus blocks, in which case the forced hub cycle `K_0` and its forced external `3-of-4` witness can be converted to one of the same legitimate outputs.

The remaining hard subcases in (2) are now explicit rather than an unnamed parity wall:
- a light-support witness with a **double head** onto the two opposite hubs;
- a third-support three-hit witness;
- a remainder three-hit witness;
- or a boundary-offset endpoint collision.

A legal two-cycle replacement by itself is not BT4 closure. All replacement cycles must be genuinely directed and pairwise vertex-disjoint, and any claimed progress must respect the original minimum-outdegree-seven source model through the inherited reductions.

## Next method

Attack the four-block fan cage first because it is strictly smaller than the >=6-block staircase. For a light double-head witness, follow the predecessor closure of its off-block cross: either a sign change creates a new non-hub reverse port, or a monotone same-sign feeder enters the four-block cycle. In the latter case record the first-entry support interval and combine it with the forced hub 4-cycle and minimum-packing exchange tax. For a remainder/third-support 3-hit witness, apply the lead's domination lift only with its exact hypotheses; do not reuse the invalid old two-packed-vertex SC2 premise. If that cage does not close in three substantive runs, switch to the >=6-block staircase and use two nonadjacent sign-boundary pairs rather than another rank-only argument.

## Privacy / provenance / integrity

Only the private research repository's technical campaign artifacts and account-local scheduler inventory were used. No installation or benchmark work was performed. No benchmark gold, credentials, scheduler identifiers, machine paths, raw private transcripts, unrelated data, email, Drive content, public posting, paid model/API, Codex, remote workflow, permission change, or other-account authentication was used. Existing artifacts and histories were preserved.
