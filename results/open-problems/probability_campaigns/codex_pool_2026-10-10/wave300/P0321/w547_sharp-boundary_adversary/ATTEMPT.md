# P0321 adversarial boundary attempt

Worker w547, 2026-10-10. This document freezes an independent derivation before reading w546's proof. No solution or novelty claim for P0321.

## Source boundary

The dated ranking, RANKING_2026-09-07.csv:556, records `5,P0321,Existence of a hexatic phase for two-dimensional Riesz gases,unsolved,hexatic phase for 2D Riesz gases`. The exact catalogue entry is op-p0321 in brain_bundle_C006p02.json: prove or refute an intermediate phase in the 2D Riesz-gas diagram, with orientational order and no crystalline positional order. Its source is Lewin, arXiv:2202.09240v2, VI.B, printed pp.66-67 (PDF indices 65-66). The survey describes fast positional and slow sixfold orientational decay and distinguishes the quasi-solid by slow positional decay and persistent rotational order. It covers s>2 and numerical evidence at s=0,1. It gives no unique rigorous observable, rate, exponent or temperature-interval quantifiers. Current openness on 2026-10-10 is UNKNOWN; source recovery is complete at catalogue/qualitative-source level, not at an invented formal theorem level.

## Independent obstruction 1

Take one common uniform angle Theta in [0,2*pi), and psi6(x)=exp(6*i*Theta) for all x. A common rotation preserves the law. Integrating exp(6*i*Theta) gives E psi6(x)=0, while psi6(x) conjugate(psi6(y)) is identically one. Thus rotational invariance and zero mean do not imply absent orientational long-range order. The implication fails even in this elementary auxiliary field.

This is not a Riesz Gibbs measure and is not a counterexample to P0321. It isolates the minimum needed observable: a two-point orientational correlation, with phase and thermodynamic-limit quantifiers specified. Independent referee pending.

After this independent derivation, the targeted prior-work read located the same example in brain_bundle_C006a05.json, key at-p0321, and in export/population/nodes.jsonl:8627. C001 is a reproduction, not a new brain contribution. It will not be resubmitted as a new result. The prior diagnostic does not construct a positive-temperature Riesz Gibbs law merely by naming a global-angle field.

## Next independent step

Completed in GAUSSIAN_BOUNDARY.md: C002 computes exact asymptotic exponents and a strictly positive curl-orientation plateau in a stipulated Gaussian stiffness model; C003 proves the endpoint p=2 and distance limits do not commute. The letter p deliberately denotes stiffness, not the microscopic Riesz exponent s. Fixed-p asymptotics cannot be transferred uniformly to the endpoint.

## Paired proof read after independent derivation

w546 L01 is correct for the stated stationary real Gaussian field with an integrable even spectral density; AUDIT_W546_L01.md records the original-proof verdict. Its hardest unchecked application is the microscopic/defect/correlation comparison. No review of a review was performed.

## Applied brain scar

The requested recall timed out after 60 seconds. The targeted MEMORY.md search found no relevant index entry; the explicitly required memory perceptron_proof_open_gaps_fleet_2026_07_12.md was read directly. It records that verified auxiliary computations and successful runners can coexist with unresolved proof gaps. Here the hardest gap is the microscopic positive-temperature defect theory, not the correctness of a Gaussian integral. Numerical receipts, source provenance and hashes are not proofs of P0321.
