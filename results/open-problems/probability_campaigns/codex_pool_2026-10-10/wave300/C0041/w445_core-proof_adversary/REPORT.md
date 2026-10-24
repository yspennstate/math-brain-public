# C0041 audit report

The exact target is uniformly elliptic iid nearest-neighbor RWRE in d>=2: almost-sure directional transience should imply positive directional speed. A recent primary manuscript and separate Lean solution claim it, so current openness is UNKNOWN and this work claims no novelty or resolution.

The paired finite-box lemmas R1/L1/L2/L2b/L3 receive scoped KEEP. Their missing input is a quantitative account of every long regeneration delay. I proved that a geometric number of finite attempts can have infinite mean cost, and that an unrestricted search finds a rare iid inward-box pattern almost surely. I also wrote sufficient conditional cost, classification and visit-count reductions, separating each from its unproved RWRE inputs. The recent manuscript explicitly pays for visit costs conditional on a separate strong crossing estimate; the negative controls do not refute it.

Measured checks: 144 exact arithmetic controls passed, plus 2 semantic hook controls; 7 draft concepts and 5 relations passed local schema checks. For q=1/4, the mean truncated total cost increases from 4 at K=0 to 28 at K=16 and diverges with K. For r=1,d=2 a fixed inward box has probability 1/64; selecting among 64 disjoint boxes raises it to 0.635013. Commands and the fresh bounded gate are in CHECK_RESULTS.json and COMPUTE_GATE.json. No runtime recall improvement is claimed.

The draft is submitted at ~\math-brain-inbox\w445\bundle_001.json. Its own results are concept/draft material pending w446. Integration, retrieval and different-model review are still pending. The actual Lean dependency chain and hardest crossing estimate have not been independently checked. The main risk is removing the deterministic search budget or substituting the unproved classification premise for a theorem.

Apply instruction: after review, the validating integrator can ingest the authorized draft. Apply patches/01_regeneration_cost_hook.diff to add exactly one proposal line to the named live proposal path; this worker did not edit that live file or any store. Recheck with python -X utf8 ~/brain_workers/w445/verify_receipt.py.

NEXT: Referee checks the narrow claims; the next concrete proof step is a certificate for arbitrary low-crossing regions with a summable classification error under the actual regeneration law.
