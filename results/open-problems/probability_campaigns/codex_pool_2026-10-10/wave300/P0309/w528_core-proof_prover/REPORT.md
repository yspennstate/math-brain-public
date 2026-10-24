Prepared P0309's exact source/prior-attempt digest, seven auxiliary proofs, and one explicitly unproved reconstruction input G. The original target remains unresolved; current openness is UNKNOWN.

The useful change is a precise defect-interaction boundary: in 3D Coulomb, neutral dipoles have a divergent absolute pair sum, while uniformly bounded dipole-free blocks have a summable bound. Actual displaced particles carry dipoles. A Gibbs repair must also preserve configuration volume; exact collapse to lattice sites cannot satisfy a finite pushforward-density bound.

Measurement command: python -X utf8 run_validation.py. 762 checks passed, including 81 exact fourth-derivative identities, 124 rational atomic controls, and finite cone/shell controls. The run used 0.0625 CPU seconds, 0.1017 wall seconds, and 210166 peak traced allocation bytes under a fresh 5-second/16-MiB gate. For the stated Coulomb examples, R16-to-R32 decay exponents were 3.004237 for neutral dipoles and 5.021311 for dipole-free quadrupoles; their analytic exponents are 3 and 5. This compares different explicit hypotheses and measures no full-gas or recall improvement.

w529 independently kept L1-L6. Referee w530 received the packet (msg-2a4ca6fe94); its verdict and L7 review remain pending. These checks are not a formal proof of G.

Submitted DRAFT: ~/math-brain-inbox/w528/bundle_001.json (9 entries, 11 relations). Submitted, reviewed, ingested, and retrievable are separate in BUNDLE_LIFECYCLE.json. No worker store integration or live-store write occurred.

Application: after the required mathematical reviews, the validating coordinator may integrate the named DRAFT. Apply patches/01_math_w528_hook.diff to add the staged hook at its named live proposal path, preserving any existing file; run the hook's pair audit before deployment. PROGRESS_OUTBOX.jsonl is the one-line progress-page event for coordinator dispatch. Both global writes remain staged within the worker's write boundary.

Risk: dropping the first-moment hypotheses, the repair-map entropy bound, or the unperturbed-Gibbs requirement would turn these scoped results into a false full-phase claim. A positive crystalline energy gap, dipole screening, anharmonic coherence, and the Gibbs limit are still unproved inputs.

NEXT: Construct an admissible two-cell repair with an explicit dipole carrier and bound its exact energy loss and pushforward density.
