# P0117 independent proof attempt

Status: incomplete; no proof of absence of all random bigeodesics. Independent mathematical review is pending.

## Target and source boundary

See STATEMENT_ONLY.md. The classical source named by the intake is Auffinger--Damron--Hanson, *50 years of first-passage percolation*, Question 31, PDF page 98. The intake describes nondegenerate continuous iid planar weights in the positive-speed regime. Its ranking is dated 7 September 2026, and current openness is UNKNOWN. A 24 September 2026 public claimed resolution requires checking.

## Prior-attempt digest and method boundary

The exact local attempt at-p0117 in probability_1000_intake_claude_20260907/brain_bundle_C006a04.json considers geodesics from -n e1 to n e1. It correctly identifies a missing anchor: such paths may escape every fixed ball, so finite-degree compactness does not produce a bigeodesic through a bounded region. Related at-p0113 gives anchored compactness and warns that midpoint probabilities tending to zero alone do not imply an almost-sure eventual exclusion by Borel--Cantelli. Targeted ID/title searches of the named H and I attempt directories found no P0117-specific record. These are search findings, not a comprehensive certification that none exists.

The present route was recorded in APPROACH_PRECOMMIT.md before reading a current proof lane. It first uses a pinned, genuinely finite-cylinder criterion. The first constructive exclusion step uses shortcuts on *prescribed paths*, separating actual disjoint-edge independence from the unproved adaptation to a path selected by the weights. This differs from unanchored compactness between opposite deterministic endpoints. No current peer proof packet has been read.

## L1: exact finite-cylinder pinned criterion

Assume a deterministic finite nonnegative weight on every nearest-neighbor edge of Z^2. Fix v. Put B_n(v)={x: ||x-v||_1 <= n}, with all edges induced by this finite vertex set. Let A_n(v) be the event that some simple path (x_-n,...,x_n), with x_0=v, is a shortest path between its endpoints *in B_n(v)*. Every such centered length-2n path automatically lies in B_n(v).

Then A_(n+1)(v) is contained in A_n(v), each A_n depends on finitely many weights, and the intersection of all A_n(v) is exactly the existence of a bigeodesic through v in the full lattice.

Proof. A shortest finite path has shortest subpaths: a shorter competitor could be spliced into it, and any resulting loops erased without increasing weight. Restrict a witness at level n+1 to its central length-2n segment; every competitor in B_n is also in B_(n+1), proving nesting. The finite set of centered simple paths at each level is a finitely branching tree under central restriction. If every level has a witness, choose an infinite branch by the elementary finite-branching compactness argument. The resulting integer-indexed path is simple because every finite central segment is simple. To verify full-lattice optimality, take any finite subsegment and any finite competitor. Choose a level R large enough to contain both the competitor and the subsegment, and then a branch witness at level at least R. The relevant subsegment is shortest in that witness's box, so the competitor cannot be shorter. Conversely, every centered segment of a full-lattice bigeodesic is shortest in its finite box, proving membership in all A_n.

Consequently, for any random nonnegative finite weights, P(bigeodesic through v)=lim_n P(A_n(v)) by continuity from above. For translation-invariant weights, P(A_n(v)) does not depend on v. The simultaneous absence target is equivalent to lim_n P(A_n(0))=0, followed by the countable union over vertices. Independence, moments, and limit-shape hypotheses are unnecessary for this equivalence. This is a reduction, not the missing estimate.

## L2: every prescribed infinite simple path is excluded

Assume iid finite nonnegative weights whose common law is nondegenerate. For every fixed deterministic infinite simple nearest-neighbor path gamma in Z^2, the probability that all its finite subpaths minimize full-lattice passage time is zero. Thus every fixed bigeodesic path is excluded; the conclusion also holds simultaneously for any *countable* prescribed family. There is no moment or nonatomicity requirement for this lemma.

Choose finite a<b with q=P(t<=a)>0 and p=P(t>=b)>0; such a,b exist by nondegeneracy. If gamma has infinitely many turns, take infinitely many turns with disjoint four-edge square supports. This is possible since the path is simple and each finite edge neighborhood contains only finitely many of its vertices. At a turn, the two path edges and the two edges around the other half of the square are distinct. The event that both path edges have weight >=b and both alternate edges weight <=a has probability eta=p^2 q^2>0, and makes that two-edge segment strictly nonoptimal. The chosen supports are deterministic and disjoint, so these events are independent. The probability that all of the first k selected turns avoid a shortcut is (1-eta)^k, which tends to zero.

If gamma has only finitely many turns, its tail is a straight lattice ray: a simple nearest-neighbor path cannot reverse immediately, and after its last perpendicular turn its step direction cannot change. Choose an integer m>=1 with m(b-a)>2a. Replace each of infinitely many disjoint straight m-edge blocks by a parallel m-edge segment connected at its two ends by perpendicular edges. The alternate path has m+2 edges, all disjoint from the original block; space blocks sufficiently far apart so their combined supports are disjoint. The event original edges >=b and alternate edges <=a has probability eta=p^m q^(m+2)>0, and makes the alternate weight at most (m+2)a<mb. Again the deterministic supports are disjoint, and (1-eta)^k tends to zero.

The same argument applies to one tail of a bi-infinite path. Countable families are excluded by a countable union of null events. An externally sampled path independent of the weights is also excluded by conditioning/Fubini, since the fixed-path probability is zero for every path.

## L3: selection destroys the fixed-route shortcut probability

In the actual full-lattice model with iid Uniform[1,2] edge weights, take opposite corners x=(0,0), y=(1,1) of a unit square. Its two two-edge routes A,B have weights S_A,S_B. Any other simple path has at least four edges and weight at least 4, while min(S_A,S_B)<4 almost surely; hence the full-lattice geodesic between x,y is the cheaper of A,B, uniquely almost surely. Put a=5/4, b=7/4. For fixed A, the event both A edges >=b and both B edges <=a has probability (1/4)^4=1/256, and makes B strictly cheaper. For the route R selected as the geodesic, the corresponding event (both R edges >=b, both other edges <=a) is impossible, hence has probability zero. It also has conditional probability zero given R=A or R=B. This is a counterexample within a nonatomic positive-speed planar iid law to retaining that fixed-route event probability after selection; it does not refute the no-bigeodesics conjecture.

## L4: uniform exponential bound for each deterministic finite path

The fixed-path lemma has a quantitative extension. Under the nondegenerate iid finite nonnegative law of L2, choose a<b with p=P(t>=b)>0 and q=P(t<=a)>0. Choose integer L>=2 with L(b-a)>2a. Write R=2(L+1), D=|B_R(0)|=1+2R(R+1), eta=p^L q^(L+2). For any prescribed simple nearest-neighbor path gamma with N edges,

P(gamma is a full-lattice geodesic) <= (1-eta)^(ceil(floor(N/L)/D)).

Proof. Partition the first L floor(N/L) edges into length-L blocks. If a block contains two successive perpendicular steps, choose the two-edge turn and its opposite two-edge square detour. Otherwise its L steps have a common oriented direction (immediate reversal would repeat a vertex), and choose the L-edge straight block with its parallel (L+2)-edge detour. In each case the original and alternate edge sets are disjoint; the high-original/low-alternate pattern is a strict shortcut. Its probability is p^2 q^2 for a turn or p^L q^(L+2) for a straight block, in either case at least eta.

Every candidate trial support lies in B_(L+1) of its block's starting vertex. When two supports share an edge, their starting vertices are within l1-distance at most 2(L+1). Since gamma is simple, the block starting vertices are distinct; at most D candidates (including the chosen one) can be removed by choosing a trial and deleting all trials with overlapping supports. Greedy selection therefore gives at least ceil(floor(N/L)/D) mutually disjoint supports. These supports are selected from gamma's deterministic geometry before observing the weights. Their high/low events are independent. A geodesic can realize none of them, proving the bound.

In particular, kappa=-log(1-eta)>0 and c=kappa/(LD)>0 give an exponential bound, with a fixed multiplicative constant accounting for the floor. For a deterministic finite dictionary P_N of prescribed N-edge simple paths, a union bound gives

P(some gamma in P_N is geodesic) <= |P_N| (1-eta)^(ceil(floor(N/L)/D)).

No independence between different dictionary paths is needed. The exact vanishing condition is log|P_N|-kappa ceil(floor(N/L)/D) -> -infinity; a sufficient entropy-rate condition is limsup_N log|P_N|/N < c. Merely having log|P_N|<cN for each N does not ensure the union bound tends to zero. Thus any class of rays starting at a fixed vertex whose N-edge prefixes lie in deterministic dictionaries of subexponential cardinality contains almost surely no geodesic ray; use the bound tending to zero and the fact an infinite witness has a geodesic prefix at every N. The same excludes bigeodesics with a tail in such a class. Covering all arms of *possible bigeodesics through the fixed vertex* by such dictionaries is unproved. The unrestricted number of simple lattice paths is exponential, and this bound supplies no successful unrestricted union estimate.

## Single hardest remaining gap G1

Promote the prescribed-path shortcuts to an exclusion uniform over bigeodesic arms chosen using the same weights. Such a selection changes the conditional law on shortcut supports: a minimizing path is chosen precisely to avoid cheaper alternatives. Neither L2/L4 nor disjointness before path selection justifies multiplying post-selection shortcut probabilities. A valid extension needs a derived conditional resampling law or deterministic dictionaries covering prefixes of possible bigeodesic arms through 0, with log|P_N|-kappa ceil(floor(N/L)/D) -> -infinity. Any uncovered-candidate probability must also tend to zero. No such uniform conditional bound, endpoint-uniform annular barrier, vanishing dictionary union bound, or proof that P(A_n(0)) tends to zero has been established. G1 is the entire unresolved step needed for the target, and no claim of a full proof is made.

Next concrete proof step: cover prefixes of possible bigeodesic arms through 0 by deterministic P_N with log|P_N|-kappa ceil(floor(N/L)/D) -> -infinity (or limsup entropy rate < c), including control of any uncovered-candidate probability; alternatively derive a resampling law that survives that selection. The square obstruction L3 shows why merely reusing original iid shortcut probabilities cannot provide it.
