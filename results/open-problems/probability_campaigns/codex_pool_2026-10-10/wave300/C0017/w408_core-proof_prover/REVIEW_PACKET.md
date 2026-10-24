# Review packet: w408, C0017

The result to audit is the conditional identification theorem L1 in ATTEMPT.md. Its square-lattice input remains unproved. Current openness is UNKNOWN and novelty is not claimed.

Read STATEMENT_FOR_ADVERSARY.md for the precise crossing/interface targets and boundary scope. PRIOR_ATTEMPTS.md and SOURCE_STATUS.json record the primary historical source, the unverified 2024 claimed solution, the standard parafermion convention and limits of the owner-work search.

Check L1's smooth inversion, localization, signed-measure Ito identities, and the countable global cover. L2 states an actual drift-measure bound; L3 transfers bounded martingales under explicitly assumed joint convergence. COUNTEREXAMPLES.md supplies a genuine wrong-kappa diffusion passing one Cardy test, a vanishing-error/nonvanishing-variation example and a symmetric-marginals/nonzero-conditional-drift example.

The single hardest gap is the stopped Cardy martingale approximation for the square-bond exploration, with the exact discrete crossing event/boundary convention, joint convergence and filtration compatibility. Proving only the derivative identity or running verify_reduction.py does not close that gap.

Final clarification: ATTEMPT.md now defines the candidate as the first-boundary-contact tail event on the right arc. Its exact Doob martingale is indexed by revealed exploration edges; the Cardy approximation and a valid capacity-time embedding remain unproved. STATEMENT_FOR_ADVERSARY.md specifies Caratheodory plus uniform parametrized-boundary convergence for the chosen approximation class. These clarify the unproved input; L1-L4 are unchanged.

Independent adversary w409 received the statement before the proof handoff. Referee w410 is requested to KEEP/FIX/DROP each claim on mathematical grounds. A source/hash match alone is not a mathematical KEEP. If w410 authors a new lemma, w413 must independently review that new result. No review of a review is requested.

Receipt received: w410/VERDICTS.jsonl contains five scoped KEEP verdicts and one FIX for the global exhaustion. The explicit fixed argument is GLOBAL_EXHAUSTION.md. w413 is requested to review that mathematical construction, not the verdict itself. The local proof KEEP does not validate the square-lattice input, and no served-model/different-model gate has been proved.

Reproduce the bounded algebra measurement with:

python -X utf8 ~/brain_workers/w408/verify_reduction.py

The script reads a fresh governor receipt, uses one thread of scalar exact arithmetic, and saves MEASUREMENTS.json. Its two launches in this checkpoint were HELD by pressure/distress gates before arithmetic; zero tested states are claimed. It has no square-lattice simulation, GPU or formal theorem checker. Trusted mathematical inputs to L1 are smooth semimartingale calculus, uniqueness of the finite variation/local martingale decomposition, and Levy's characterization; none is reported as machine-verified here.

The draft bundle will contain definition/concept entries while independent review is pending. The coordinator owns validation, integration and promotion. Submitted, reviewed, ingested and retrievable are recorded separately in INTEGRATION_STATE.json.

NEXT: w410 audit L1-L4; after KEEP, pursue a genuine square-lattice stopped Cardy observable estimate.
