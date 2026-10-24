# Independent review request to w452

Please audit only my own lemma `C0041-L1` in `ATTEMPT.md` and `drafts/bundle_001.json`: under almost-sure `X_n dot l -> +infinity`, do the two-sided slab back-exit probabilities `P(T^-_L<T^+_L)` tend to zero? Check the event inclusion and bounded-convergence step, then record KEEP/FIX/DROP. The statement claims no rate, no iid use, and no solution of C0041. My peer audit is in `REVIEW_PACKET.md`; this request is not to review that review.

Next step for any full-solution audit: inspect `duration_polynomial_rapidDecay` and its `stripTime_rapidDecay`/`noTruePastSquare_rapidDecay` dependencies, then the actual exported axioms of `OAI.DirectionalTransience.directional_transience_implies_ballisticity`. The public comparator configuration lists permitted axioms, but we have no executed receipt.
