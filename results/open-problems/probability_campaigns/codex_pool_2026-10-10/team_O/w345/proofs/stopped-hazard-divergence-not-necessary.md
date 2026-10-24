# C0057: Certain discovery with a finite stopped-hazard sum

Label: proof; author checked only. Independent audit: PENDING w347.

For a target discovered at time T=1 deterministically, p_n=P(T=n+1|F_n) equals one at n=0 and zero thereafter. Thus discovery has probability one, while sum_n p_n=1 is finite. This refutes a general necessity claim for the actual stopped target hazard. It does not refute a perimeter-only equivalence specific to critical Boltzmann maps; that would require a model-specific argument.

Assumptions: Hazards refer to discovery of one fixed target and are stopped at its discovery

Take any probability space with the trivial filtration and T=1. The event {T=1} is certain and all other {T=n+1} events are empty. Taking conditional probabilities gives p_0=1 and p_n=0 for n>=1. Summing proves the assertion. A conditional Borel-Cantelli sufficiency statement cannot supply the converse from this example.

Limits: A generic counterexample only. It supplies no critical weight sequence whose map is or is not exhausted.

Existing card: math:probability.planarmaps:open-problem-c0057-filled-in-peeling-discovers-the-whole-map-for-every-critical-weight-se
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:4364
