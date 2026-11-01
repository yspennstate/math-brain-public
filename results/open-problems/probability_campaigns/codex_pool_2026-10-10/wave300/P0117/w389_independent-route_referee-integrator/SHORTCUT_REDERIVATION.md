Independent reproduction of w387 L1-L4, by w389 on 2026-10-10. Verdict: KEEP for the exact hypotheses below. This is not a P0117 solution.

Let the nearest-neighbor Z^2 edge weights be iid finite, nonnegative and nondegenerate. Choose 0<=a<b with p=P(t>=b)>0 and q=P(t<=a)>0. Fix an integer L>=2 such that L(b-a)>2a. Set eta=p^L q^(L+2), R=2(L+1), D=1+2R(R+1). The path must be prescribed before observing the weights.

For a fixed simple N-edge path, partition its first L floor(N/L) edges into M=floor(N/L) blocks. Every block either contains a perpendicular turn or is straight. Immediate reversal is impossible by simplicity. At a turn, the two original edges and the other two square edges are distinct; high original weights and low alternate weights give strict cost improvement and have probability p^2 q^2>=eta. For a straight block, the parallel detour has L+2 edges distinct from the L original edges; its all-low pattern and the all-high original pattern have probability eta, and its cost is at most (L+2)a<Lb. Only a cheaper competitor between the subsegment endpoints is needed. If a detour touches another portion of the original path, that does not rescue geodesicity; splicing followed by nonnegative loop erasure also gives a shorter full-endpoint path.

Each trial support lies in the l1-ball of radius L+1 about its block start. The M starts are distinct because the path is simple. Two trials sharing an edge have start distance at most 2(L+1)=R. A radius-R integer l1-ball has D=1+2R(R+1) vertices. Greedily choose a trial and remove every remaining trial sharing an edge with it. At most D candidates, including the chosen trial, are removed at each choice. Therefore at least ceil(M/D) selected supports are pairwise edge-disjoint. The entire extraction is deterministic geometry, done before observing weights.

The selected events are independent because they use disjoint iid edges. Their success probabilities are at least eta; they need not be equal. Thus P(no selected shortcut)<=product(1-P(shortcut))<=(1-eta)^ceil(M/D). A geodesic has no strict shortcut, proving

    P(fixed path is geodesic) <= (1-eta)^ceil(floor(N/L)/D).

With kappa=-log(1-eta) and c=kappa/(LD), floor(N/L)>=N/L-1 yields the optional bound exp(kappa/D) exp(-cN). For a finite deterministic dictionary P_N, a union bound gives |P_N| times the exact fixed-path bound, with no independence across dictionary paths. The exact sufficient vanishing condition is

    log|P_N| - kappa ceil(floor(N/L)/D) -> -infinity.

A strict limiting entropy-rate gap limsup log|P_N|/N<c suffices. Merely log|P_N|<cN for every N does not suffice: a bounded deficit only bounds the union estimate by a nonzero constant. A ray with its N-edge prefix in P_N for every N would belong to the success event for every N, so any such class is excluded when those probabilities tend to zero. A bigeodesic is excluded only if one of its tails belongs to the covered class. The full unrestricted candidate class is not shown to have such dictionaries.

For L2, either infinitely many turns allow infinitely many deterministic disjoint square trials, or a finite number of turns leaves a straight tail with separated parallel-detour trials. A simple path meets a fixed finite neighborhood only finitely often, so the disjoint extraction is available. The avoidance probability tends to zero. Countable families and an independently sampled path follow by a countable union and Fubini. This does not exclude an uncountable weight-selected family.

For L1, central restriction of a shortest centered 2(n+1)-edge path in the l1-ball B_(n+1) is shortest in B_n. Splicing and nonnegative loop erasure prove this with ties allowed. The finite witness sets form a finitely branching centered-prefix tree. Every fixed full-lattice competing path lies in a sufficiently late box; the corresponding branch witness compares against it, proving global minimization of the infinite branch. The finite-cylinder intersection is thus exactly bigeodesic existence. The reduction alone does not prove its probabilities vanish.

For L3, iid Uniform[1,2] makes all other simple diagonal-corner paths have at least four edges and cost >=4, while the two square-route sums are <4 and distinct almost surely. The fixed route's threshold event has probability (1/4)^4=1/256. If the selected route has both edges >=7/4 and the other route both <=5/4, it is strictly more costly, contradicting selection. Its event probability is zero, also conditional on the selected route. This demonstrates why the unconditional disjoint-support shortcut product cannot simply be transferred to a path chosen using those weights.

Unresolved G1: cover possible bigeodesic tails by deterministic dictionaries with diverging entropy deficit and vanishing uncovered-candidate probability, or prove a conditional resampling law surviving selection. No such argument is supplied by L1-L4. No novelty or full-solution claim is made.
