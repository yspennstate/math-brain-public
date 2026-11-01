# Finish — FOREST fleet03/B01

Run: `20260922T053534Z-fleet03-B01-forest-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Candidate: `FOREST-STAR2-SPLIT-CONDITIONING-v1`  
Parent FOREST: `OPEN`  
Brain context: `WITHOUT_VERIFIED_BRAIN`  
Observed finish: `2026-09-22T05:46:29Z`.

The current lead's STAR-2 weighted contraction debt was converted exactly into pairwise negative correlation in the smaller simple graph `J=G\g` conditioned on the two endpoints of `g` being disconnected. The proof is an exact contraction/lift multiplicity bijection and preserves every forest size, disconnected forests and unit source weights before conditioning. A component-factor unrooting formula was also derived.

The named fleet04/B02 fixed-radius Hall no-go was applied: the new conditional problem should not be attacked by another universal fixed-radius same-k path-cut/join support. A separate exact six-vertex example refutes coordinatewise monotonicity of the Rayleigh gap under a star-edge doubling: `Delta(t)=3300-248t+64t^2`, so `Delta(2)=3060<3116=Delta(1)`. This is a proof-route counterexample, not a FOREST counterexample.

Exact checker output: split identity PASS on 5,325 graph/nonedge instances and 103,481 conditional forests; finite STAR-2 diagnostic PASS on 21,400 weighted instances / 319,554 marked pairs through five vertices; monotonicity counterexample PASS.

Authoritative report blob: `2ed53fdb5dd41db594bbf990ba820fa86a99e6f5`.  
Checker blob: `bf7f47612c00d88be1a00849ad1aad8421298dee`.  
Output blob: `8387e99c1cb1dd31bf66d8e4db8d9362750abdd8`.  
Shared handoff blob: `c49d586a18b973280db00e48457a4c2929775ec8`.

Next obligation: prove or refute the source-native conditional inequality `Cov_J(1_e,1_f | u !~ v)<=0` in the lead's edge-minimal-counterexample configuration, using a global component coupling/flow or source-valid integral inequality rather than fixed-radius switching or monotonicity.
