# C0048 core-proof adversarial result

The deliverable is a scoped audit of w456's cumulant route and an independently derived obstruction to filling its critical gap. Finite-volume identities, the cubic exclusion lemma and the conditional critical endpoint pass the algebraic check. The missing input is SP(q,d): the actual lattice magnetization must be a stationary minimizing point of a potential with a uniformly positive cubic coefficient and a uniform value/derivative quartic remainder. This is unproved, especially q=d=3. C0048 is not solved here; current general openness is UNKNOWN.

I added an explicit S3-invariant potential with continuous onset despite a fixed cubic polynomial term, and a q=3,d=3 FK example whose positive local edge probabilities coexist with zero infinite-cluster probability. Both show which additional premises matter. w458 independently kept these obstructions, the right-continuity reduction and the finite mixing identity; the exact receipts are in review/w458_verdict_snapshot.json. The fourth Legendre derivative and four-cycle pressure cumulant values have no separate referee receipt and remain conservatively labeled.

Measurements: `python -X utf8 validate_fk.py` checked 73,856 conditionals in 12,352 configurations with zero mismatches (0.679 seconds). On the four-cycle the joint probability is 2.71521754 times the product of marginals. `python -X utf8 validate_cumulant_mixture.py` matched six independently computed spin/FK cumulants (0.00155 seconds): omitting the mixture term gave fourth-cumulant errors 1/9 and 22576/16641; including it gave zero in both cases. w456 already includes this term correctly.

Brain output: a four-entry concept-only draft with four supported relations was submitted to ~/math-brain-inbox/w457/bundle_001.json. SUBMISSION_STATES.json separates submission, scoped review, ingestion and retrieval. Ingestion and retrieval have not been observed; the measurements above concern mathematical audit checks. The single hook proposal is local and undeployed.

Apply: after referee review, the validating coordinator can integrate the authorized inbox draft; the hook reviewer can apply `patches/01_cumulant_mixture_hook.diff` to the live proposal path named in its header, preserving existing rows.

Main limits: no bound for spatial-correlation corrections to the critical potential, no critical-volume remainder, no formal proof receipt, and no response-side served-model attestation. The finite counterexamples do not disprove the Potts conjecture.

NEXT: Prove or refute SP(3,3)'s physical-potential identification and uniform C1 remainder; obtain explicit receipts for the remaining local derivative/numerical claims before promoting them.
