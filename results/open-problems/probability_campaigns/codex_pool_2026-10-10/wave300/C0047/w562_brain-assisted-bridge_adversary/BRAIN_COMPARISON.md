# Returned material versus the C0047 bridge need

The query and recorded top-six results are in math_recall_output.json. Neither target card was returned. The rank-three generic Spectral radius card (RETURNED_SPECTRAL_CARD.json) states a bounded-operator definition only. It has no percolation theorem, no prescribed generating set, no degree factor, and no supercritical parameter. It cannot discharge a theorem dependency in this proof. The measured failure is 0/2 required target cards in the top six, not a claim that every returned source is irrelevant.

The bounded target lookup instead retrieves both full C0047 records. The open-problem card explicitly carries unverified status dated September 7. The attempt card also carries unverified status and says its rho is the spectral radius of simple random walk, while asserting a degree-free p_c<1/rho sufficient route. Retaining those statuses is essential. Exact end quotes and stored digests are in EDGE_AUDIT.jsonl and target_cards.json.

| Hypothesis / conclusion | Needed for the prescribed Cayley graph | Primary 1996 Theorem 4 | Retrieved generic radius card |
| --- | --- | --- | --- |
| Graph class | Infinite, connected, locally finite, vertex-transitive | Almost transitive, finite maximal degree k | None |
| Radius convention | Normalized random-walk rho, adjacency norm d*rho | Random-walk rho, explicit factor k | Generic bounded-operator radius; graph operator unspecified |
| Parameter | Some p>p_c giving a strict interval | Percolation occurs at p | None |
| Quantitative condition | Must justify one p with p*d*rho<1 if using this route | rho*k*p<1 | None |
| What nonamenability supplies | rho<1 and positive expansion | Does not replace the quantitative condition | None |
| Conclusion | Nonuniqueness above p_c on this fixed graph | Infinitely many infinite clusters at such p | None |

Even if the theorem is correctly normalized, its hypotheses do not follow from nonamenability alone. T4 fails p_c*d*rho<1 while satisfying the parent conjecture. The separate existence-of-a-generating-set result has an existential generating-set quantifier, whereas C0047 needs the fixed set prescribed at the start. The overlapping-path counterexample and slot-coupling proof isolate the dependence and merger losses in this transfer.

The recent manuscript's Theorem 1.1 supplies the exact critical-norm assertion needed by w561's conditional route if its proof is sound. Its statement was verified against the public PDF, but this packet does not independently check its full proof. No checked theorem was returned by recall that closes the critical-norm or routing-merger step.

Bounded repair proposal: exact candidate-ID metadata lookup, read-only, with a two-second SQL budget, at most four returned cards, full text/metadata, and a no-proof-certification warning. It recovered the two expected target cards in 0.227 seconds in the documented run. Supersession/current-note resolution and broader retrieval quality still need separate validation before use as a general serving policy.
