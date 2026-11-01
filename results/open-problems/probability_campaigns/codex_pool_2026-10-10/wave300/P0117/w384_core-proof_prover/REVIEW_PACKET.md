# P0117 review packet: w384 to w386

Statement-only packet was sent first to w385 via the existing mesh, receipt msg-efda4c71c4. The threshold route was saved independently before reading any adversary proof. Referee: w386. Referee's own new results require w389 as independent referee.

Review ATTEMPT.md Lemmas 1-3, Proposition 4 and Lemma 5. These are author-proved reductions with a remaining gap, not a claimed resolution of P0117. In particular check the fixed-path independence in the moment-free properness proof, the metric formula when the two concatenated arms intersect, preservation of strict preference under outer-to-inner restriction, both arms in diagonal compactness, and the conditional null event at the limiting threshold. Lemma 5 lowers exactly one edge: check preservation of subsegments not containing the changed edge, the countable probability exhaustion above a positive essential infimum, and the independence of the fresh resampled weight. Check singular continuous laws as well as laws touching zero. Finite checks in verify_threshold.py are instrument checks, not a formal proof or an independent audit. Its first launch was held by the fresh governor before any graph computation; see MEASUREMENTS.json.

The only proposed hard input is support collapse H_infinity<=a. It is explicitly UNPROVED. Do not keep it as a theorem. A proof gap in the reduction should be reported against its exact lemma rather than treated as evidence for or against the full conjecture.

SOURCE_STATUS.json distinguishes the old Question 31 card, the standard moment-restricted formulation, and a newer primary PDF claiming that formulation is settled. The primary PDF's presence and theorem statement are verified; its full mathematical proof has not been audited by w384. No claim of current openness or novelty is certified.

The DRAFT bundle uses a definition and concept entries, with the author proof and unproved-input scope in the statements. DELIVERY_STATE.json tracks submitted, reviewed, ingested and retrievable independently. No store integration is authorized for this worker; the validating coordinator integrates after review. The unified diff is for the draft JSON artifact, not a live recall-engine change.

NEXT: Independently check Proposition 4, then decide whether to keep its reduction as a concept/lemma draft while leaving support collapse unproved.
