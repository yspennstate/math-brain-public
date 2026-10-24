# Layer-III interface: what the target constant means, and why description length is the right currency

Author: main session c53c1d50, 2026-08-19 ~02:2x, written while iteration-2 agents run (no lane is assigned this question). Status: the arithmetic of §1 is elementary and independently verified here; §2–§3 are inference from it, labelled. Provenance note: §1 is standard folklore about the conjecture, NOT taken from the dossier — the dossier states the target constant but never unpacks it. That independence is the point: it lets us check the transfer lane's interface reading without re-using the dossier's own framing.

## 1. The constant 2n²2⁻ⁿ is the two-equal-rows-or-columns count (verified)

Count the dominant singularity mechanism directly for B_n ∈ {−1,+1}^{n×n}:

- Row pairs: C(n,2) = n(n−1)/2 of them. For a fixed pair, Pr(row_i = row_j) = 2^{−n} and Pr(row_i = −row_j) = 2^{−n}, so 2·2^{−n} per pair.
  Expected number of coincident row pairs = (n(n−1)/2)·2·2^{−n} = n(n−1)·2^{−n} = (1+o(1))·n²2^{−n}.
- Column pairs: identical count, another (1+o(1))·n²2^{−n}.
- These events are pairwise nearly disjoint at leading order (two distinct coincidences force a codimension-2 event, cost 2^{−2n+O(log n)}), so first-moment = probability at leading order.

**Total: (1+o(1))·2n²2^{−n} — exactly the conjectured value.** So the sharp conjecture says precisely: *singularity of a random sign matrix is asymptotically caused by two equal or opposite rows or columns, and by nothing else.*

## 2. Consequence for the interface (the transfer lane's risk 1, substantially de-risked)

The lower bound Pr(det = 0) ≥ (1+o(1))2n²2^{−n} is the easy direction — the explicit mechanism of §1 supplies it (inclusion–exclusion truncation). **The entire difficulty of the sharp conjecture is the matching UPPER bound**, i.e.

  Pr(det B_n = 0, and no two rows/columns coincide up to sign) = o(n²2^{−n}).

That is a statement that a SUM OVER NON-DOMINANT STRUCTURES is small. Sums over structures are bounded by union/triangle inequalities, and the cost of a union bound over a family is the log-cardinality of the family — *however that family is described*. Therefore:

**[INFERENCE, high confidence]** the deterministic input can only enter through the cost of naming a structure, i.e. through description length — which is exactly the transfer lane's W2 reading (attack_transfer.md §3.2), and exactly what makes W3 (certify-or-count) lawful. The alternative the transfer lane feared — a moment expansion whose signed terms CANCEL, so that a mere count is insufficient — is a feature of *sharp-asymptotics-by-cancellation* arguments; but here the sharp asymptotics come from the explicit dominant mechanism of §1, and the residual task is a one-sided smallness bound where cancellation buys nothing that counting cannot. A signed expansion may still be the technical vehicle (centered moments over F_p are used to detect singularity), but its role is to certify smallness of a sum whose terms are indexed by structures, and each term's admission cost remains its description.

**What this does NOT settle.** (a) The *organisation* of the sum — which structures are grouped, and at what "required order" the centered-moment expansion is truncated — can still change which descriptions are admissible (e.g. a truncation that needs uniformity across a slice would forbid per-slice codes). (b) Over F_p the detection functional is a signed character sum; if the argument needs cancellation *within* one structure class to beat 2^{−n}, then that class's internal structure, not its count, is what matters. (c) None of this touches the deterministic core.

## 3. A second reading of the same fact: where the residual class sits

The dominant mechanism's null vectors are v = e_i ± e_j — support 2, the sparsest possible. The dossier's Layer-I reductions remove exactly the tame end of the structure hierarchy (acyclic tails, private pivots, sparse cycles, low-corank cores), and its residual class sits at the opposite extreme: dense, polylogarithmically-supported rows, corank ≥ 5. **So the campaign's open core is maximally far from the mechanism that produces the answer.** This is the structural reason the problem is hard in the way it is: the constant is decided by the sparsest structures, while the last unproved bound concerns the densest ones, and the two are connected only through the requirement that the dense ones contribute o(n²2^{−n}) — a smallness statement with an enormous margin (they need only beat n²2^{−n}, and the endpoint bookkeeping shows they have a full log-factor of slack, cf. transfer-lane W1).

**[OBSERVATION worth testing in iteration 3]** if the residual class needs only to be o(n²2^{−n}) rather than exponentially smaller, then the o(log n)-coefficient relaxation (W1) and the count-instead-of-certify route (W3) are not merely convenient — they may be *generous*. The right question for the next transfer-side pass is: at the residual class's own parameters (ℓ ≈ ½log₂log n, k = O(n/log n)), how much smaller than n²2^{−n} does the class sum have to be, and what deterministic coefficient does exactly that? A quantified answer replaces "o(log n)" with a number.

## Strongest case this is wrong

The §1 arithmetic is textbook and I re-derived it here, so the risk is not there; it is in §2's inference. The strongest counter: sharp (1+o(1)) results sometimes DO require cancellation, because a union bound over a family of size N loses a factor N even when each term is small — if the non-dominant structure count is itself of order n²2^{−n}/(per-term probability), union bounding is exactly borderline and only cancellation saves it. If the packet's centered-moment machinery exists precisely because the union bound is borderline at the endpoint, then description length is necessary but not sufficient, and W2/W3 need a supplementary uniformity. The concrete check: take the endpoint parameters (k = O(n/log n), ℓ at threshold (32)) and compute whether the count-times-probability product has room to spare or is borderline. That computation is one page and is now the sharpest open question on the Layer-III side — it is a *quantitative* question, not a structural one, which is progress over "the transfer is unwritten".
