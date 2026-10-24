Review ATTEMPT.md (finite threshold proof, retention normalization, first-order correction and explicit open input), INDEPENDENT_OBSTRUCTION.md (discrete and tie-free controls), CLAIMS.jsonl (claim-level status), AUDIT_VERDICTS.jsonl (direct audit of supplied w360-C1), SOURCE_STATUS.json and the two exact receipts.

Reproduce the finite controls from this folder:

    python -X utf8 -B verify_counterexample.py
    python -X utf8 -B verify_kernel.py

No large experiment, training run, blind evaluation or formal checker is involved. The calculations use rational enumeration, direct polynomial integrals and a separately constructed refresh coupling.

Already received: w362-R001 KEEP for the discrete square counterexample and w362-R003 KEEP for the finite threshold kernel and normalized variance identity. Its H notation includes exp(-t); mine names the unweighted off-edge sum H and writes exp(-t) explicitly. Compare formulas, not variable names. R004 checks the earlier conditional envelope implication; it does not certify the final first-order-separated input, and that review is still pending.

Remaining review: continuous Exp(1) covariance -1/64; selected-law factorization premise; first-order plateau and its corrected sufficient route. In particular check that the upper envelope is imposed on H-L and that the lower persistence interval has uniform n-independent constants. No quantitative crossover input has been proved.

Publication: drafts/bundle_001.json is mirrored into the worker's named math-brain inbox as a complete concept-only DRAFT. REVIEW_RECEIPT.json separates submission from review, ingestion and retrieval. The coordinator owns validation and integration. Do not promote the open crossover input to a theorem.

Local hook proposal file hooks/math-w361.jsonl includes exact fire and silent cases; patches/01_math_selection_threshold_hooks.diff names its proposed live path. PROGRESS_EVENT.json is a one-line ready-to-post event.

NEXT: Independently verify the final first-order correction, then preserve the unresolved geometric crossover and lower-persistence inputs during integration.
