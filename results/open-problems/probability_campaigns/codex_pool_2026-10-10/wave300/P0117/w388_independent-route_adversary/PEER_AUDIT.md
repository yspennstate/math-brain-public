# Independent adversary audit of w387's late packet

The independent approach and C01-C05 derivations were saved in this folder before w387's statement-only message and before reading its ATTEMPT.md. During final validation its packet became available. I then read STATEMENT_ONLY.md, ATTEMPT.md L1-L4, the hardest gap G1, and the exact-control script. This supersedes the earlier availability note in AUDIT.md; no complete no-bigeodesic proof is offered by that packet.

L1 KEEP. Its criterion uses centered graph-length n arms and a shortest path in the l1 box B_n, rather than the global metric at a fixed scale. This is valid: central restriction gives nesting, finite-degree central strings give a simple bi-infinite branch, and every fixed finite competitor is eventually contained in a branch witness's growing box. The last quantifier is essential. A single box-shortest path may be globally nonoptimal, as my C05 example shows, but requiring every level along one consistent branch removes that issue. This is a genuinely finite-cylinder reduction; it needs no lower bound, independence, uniqueness, moments or direction assumption.

L2 KEEP. For a deterministic simple infinite path, infinitely many turns admit a deterministic infinite subsequence of pairwise disjoint square edge supports. Simplicity and local finiteness ensure the greedy selection cannot discard infinitely many turns in one finite support neighborhood. High original edges and low alternative edges yield a strictly cheaper segment; disjoint supports make the trials independent. With only finitely many turns, immediate reversal would repeat a vertex, so a tail is straight. Choosing a finite block length m with m(b-a)>2a and disjoint parallel detours supplies the same positive-probability independent trials. This excludes fixed or countably prescribed paths, not the environment-selected path family.

L3 KEEP. For Uniform[1,2] weights on the full lattice, opposite corners of a unit square have only two candidate two-edge paths. Every other simple path has even length at least4 and cost at least4, whereas the cheaper square route costs less than4 almost surely. On a fixed route the high-low event has probability(1/4)^4=1/256. On the selected minimum route it is impossible: that event would make the other route strictly cheaper. No conditional-independence claim can preserve this event's prior probability after geodesic selection. This counterexample satisfies the continuous positive-speed iid assumptions and rejects the inference only.

L4 KEEP as a prescribed-path bound. A selected turn trial or straight trial has probability at least eta=p^L q^(L+2), since L>=2 and p,q<=1. Each trial support lies within l1 radius L+1 of its deterministic block start. If supports overlap, their starts are within2(L+1), and a simple path supplies distinct block-start vertices. A greedy trial therefore deletes at most D=1+2R(R+1), R=2(L+1), candidates including itself. At least ceil(floor(N/L)/D) disjoint trials remain. The product bound is legitimate precisely because all geometry is fixed before the weights. A dictionary union needs no independence between different paths.

The hardest attempted closing step remains G1: an admissible candidate cover or resampling law for a path chosen using the same weights. Nothing in L4 supplies that cover. The next-step wording should be made quantitative: with kappa=-log(1-eta) and m_N=ceil(floor(N/L)/D), the union bound goes to0 when

    log|P_N| - kappa*m_N -> -infinity.

A sufficient condition is limsup_N log|P_N|/N < c=kappa/(LD). A pointwise assertion log|P_N|<cN without a diverging deficit is insufficient. Concrete inference counterexample: 2^(N-1) disjoint uniform cells each of mass2^-N have total union mass1/2, although log(2^(N-1))<N log2 at every N. The packet's formal subexponential-dictionary corollary is valid; this note sharpens its NEXT line, rather than claiming that theorem is false.

My output-only monotone-raise posterior C06 is a different coupling which may serve as a valid resampling input. It does not restore L3's impossible shortcut event on the same selected geodesic and is not a closure of G1.

No full target, new novelty claim, or formal proof is certified. w389 remains the referee. The proposed main theorem in the September 2026 public manuscript retains UNKNOWN correctness in this packet.

NEXT: Require the exact entropy deficit above, or an explicitly factored posterior for a different coupling; do not transfer deterministic shortcut priors to weight-selected paths.
