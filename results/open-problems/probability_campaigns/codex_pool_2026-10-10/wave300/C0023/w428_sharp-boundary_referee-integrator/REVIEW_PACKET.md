# C0023 referee packet — 10 October 2026

The dated 7 September ranking is stale for the nearest-neighbor **bond** target. OpenAI's 24 September 2026 preprint states Theorem 1.1 for every infinite connected locally finite quasi-transitive graph with p_c<1, and Corollary 10.1 explicitly states the Z^d bond result for every d>=2. The source PDF SHA-256 is `5929CCEA200FD7433C5AC519C924316CCDD56FC0208EA0CC65D5A424BB2E425F`. This is a published resolution claim and a checked statement; it is not my independent certification of the long proof. The comparator challenge's `sorry` states the trusted goal, while the separate solution `Main.lean` contains a proof; I did not run the comparator or inspect every dependency.

## Peer verdicts

- **KEEP w426 L1-L3:** The fixed separator witness and Harris-FKG imply the finite-forest product inequality. The earliest attachment on the unique o-b path is a valid separator for every relay. The exact forest near-one modulus is `1-sqrt(1-epsilon)`; a two-edge path realizes equality and rules out a larger universal modulus.
- **KEEP w426 B1-B2:** The three-edge selected-relay example makes the conditional a2-to-b chance zero even though its unconditional chance is positive. At probability 1/2, replacing the conditional chance by the marginal produces 3/16 instead of 1/8. On the five-edge cyclic graph, neither relay is a fixed pointwise witness. The product gluing inequality still holds there, with margin 1/128.
- **KEEP w427 strip lemma:** The cut events on different column interfaces use disjoint bonds. For width `2k+1`, `q=(1-p)^(2k+1)` and the one-arm bound is `2(1-q)^R`; thus `p_c(S_k)=1` for every finite k.
- **KEEP w427 exhaustion criterion:** `theta_G(p)=inf_R sup_n a_n(R)` and `theta_Gn(p)=inf_R a_n(R)` follow from finite path witnesses, continuity of probability, and local finiteness. The missing transfer premise is a radius giving a small *uniform* ambient one-arm probability across all n.
- **KEEP w427 counterexample:** At `p=99/100`, every finite-width strip has no infinite cluster, while `Z²` has `theta(p)>0.99999` by the closed dual-circuit count. This refutes unrestricted transfer only.

## Independent reproduction and limits

Run `python -X utf8 ~/brain_workers/w428/verify_review.py`. It enumerates the finite edge configurations independently and computes the exact Peierls series with rational arithmetic. Output: `square: 7/32 3/4 9/32 1/128`; `relay: 1/8 3/16 1/16`; `Peierls ...: 10557/2352250000`.

The strip proof uses independence only for disjoint interfaces. The forest proof uses positive association of two increasing events. No conditional per-relay bound is multiplied without accounting for selection. The two counterexamples attack stronger auxiliary bridges; they do not disprove critical nonpercolation. The published preprint itself says fixed-slab critical extinction alone does not imply its lattice theorem.

The hardest unchecked item in this referee pass is the 2026 preprint's joint-gluing Theorem 6.1 and its conditional use in Theorem 1.1. A source/hash check and inspection of the final Lean theorem statement do not audit that chain. Integrate the status correction as a source-backed **published result claim**, retaining a distinct independent-proof-audit state. Keep peer special cases scoped; there is no new solution claim by this triad.

NEXT: Validate the proposed math-brain draft bundle against BUNDLE_SPEC, then hand the reviewed packet and status correction to the integration contact with the proof-audit limit explicit.
