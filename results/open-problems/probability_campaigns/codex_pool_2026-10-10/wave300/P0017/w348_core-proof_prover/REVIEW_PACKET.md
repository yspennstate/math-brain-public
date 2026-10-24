# w348 / P0017 review packet

Read STATEMENT_FIRST.md before ATTEMPT.md for the independent challenge. w349 and w350 have received the statement through the authorized mesh; w349's own precommitted lane is localization covariance weighting. Other triads' visible lanes are simplex fibers and Gaussian-posterior contraction. This packet is deterministic block recovery plus an exponential-product analytic special case.

Deliverables: ATTEMPT.md (complete prover-written proofs L1--L4), CLAIMS.jsonl (exact assumptions, proof summaries and explicit gap), SOURCE_STATUS.json (dated primary and prior-source status), tests/check_exact.py (bounded arithmetic verification), checks/compute_gate.json (fresh compute admission), checks/exact_results.json (PASS: 0.0272442 seconds), and drafts/bundle_001.json (seven submitted concept drafts, six relations).

Review L1 against the general p<=q incidence coefficient and the sharpness finite difference. Check q=p, p=1 and an untouched trailing Hilbert factor. Published BKL Lemma 2.2 already gives the p=d,q=2d binomial factor inside its proof, so this is not claimed as a new improvement over that proof.

Review L2's commuting original-block projections and the missing-block counterexample. The error coefficient b+1 is valid by two triangle inequalities; optimality of that coefficient is not claimed.

Review L3 independently: normalized ordered-index tensor multiplicities give alpha!/d!, supports are orthogonal because the original law is an independent product, and the frame-operator norm is bounded separately on each support. Taking a trace of the full operator would reintroduce dimension; the proof explicitly takes traces of individual support blocks and then their maximum. Verify the one-coordinate extremizer and why the least common degree base is R=2. This law is not regular in BKL's sense; the result is a direct analytic calculation.

Review L4 as a quadratic-moment operator under finite fourth moments, or as a tilt derivative only when local exponential moments exist. Verify the symmetric-matrix dual norm and the non-log-concave isotropy-only control.

One full-target gap: a universal all-degree Hilbert--Schmidt Taylor bound for every centered regular log-concave law with covariance <= I, or a full independent audit discharging it from the cited current literature. BKL Theorem 3.1, smoothing/approximation and Cheeger comparison are external steps here. The packet is not a full KLS proof.

No formal-check receipt is claimed. Arithmetic PASS is not an independent proof verdict. Review and ingestion are separate states. Until an independent KEEP, draft entries stay concepts and are not promoted to theorems.

Please write a verdict for each of w348-L1 through w348-L4, naming any exact failed assertion and any additional hypotheses. The supervisor sees STATE: NEEDS_REVIEW when packaging and measurements finish.

NEXT: w350 audits L1--L4, prioritizing L3's normalization and the orthogonal support decomposition; w349 supplies an independent adversarial verdict.

2026-10-10 review receipt: w349 KEEP L1-L3; L4 derivative-domain FIX applied in the current proof, claims and submitted concept. Final w350 review and corrected-L4 confirmation remain pending. See checks/independent_review_receipt.json.
