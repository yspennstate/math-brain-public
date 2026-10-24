# P0321 core-proof adversary attempt

2026-10-10. Worker w541; paired prover w540; independent reviewer w542. Current openness UNKNOWN. No full-target proof or novelty claim.

The dated campaign record asks for the intermediate hexatic phase of a two-dimensional Riesz gas. Lewin's primary discussion (arXiv:2202.09240v2, Section VI.2) distinguishes the phases by positional and sixfold orientational correlations. Its fast/slow terminology does not fix exact decay rates, observables, or quantifiers. An exact quantitative theorem therefore needs those choices stated separately.

## Independent result

INDEPENDENT.md was saved before any paired mathematical artifact was read. For the explicitly stipulated cutoff Gaussian displacement field with spectrum aT |k|^-2 PT + aL |k|^-s PL, aT>0,aL>=0,0<=s<2, density-wave surrogate correlations are bounded above and below by positive multiples of r^-eta, eta=aT |q|^2/(4pi). The linearized orientational correlation tends to exp[-36 aT Lambda^2/(16pi)]>0. The argument uses an exact Gaussian characteristic function, polar integration, integrable Bessel tails, and the Riemann-Lebesgue lemma. It does not multiply conditional bounds.

This is a proved special case awaiting w542's independent check, not a particle-gas theorem. In particular it cannot establish exponential positional decorrelation in a hexatic interval. The missing physical step cannot be replaced by calling the surrogate harmonic calculation a hexatic proof.

The bounded numerical probe ran in 1.44 seconds: 16 radius/direction pairs passed, with predicted eta=0.0795774715 and effective exponents 0.0795773062 and 0.0797341897 at radii 128 to 256. These are consistency checks, not interval enclosures or a mathematical proof receipt. Command: python -X utf8 ~/brain_workers/w541/numerical_probe.py.

## Hardest missing input, expressed as a proof obligation

For a fixed chosen Riesz exponent s and positive density rho, construct an actual infinite-volume particle Gibbs state at every inverse temperature in a nonempty open interval I, and derive its defect distribution and bond/positional observables from the microscopic Gibbs specification. In that same state and uniformly over increasing observation scales, prove the separation needed for a hexatic regime: positional disorder while the sixfold orientational correlations remain slow. Merely assuming the two correlation conclusions restates phase existence.

In a defect-based route the substantive missing lemma is microscopic control of dislocation proliferation together with disclination confinement on one nonempty interval, including the integration over all other particles and long-range energy terms. It must lead to the observable estimates; scalar defect-energy heuristics do not supply those estimates by themselves. Calling dislocations and disclinations independent requires a proved measure decomposition, not a per-defect bound.

An acceptable route has three separate obligations: (1) a stable thermodynamic Gibbs construction and well-defined local bond observables; (2) a justified coarse-graining of the particle measure, including the defect sectors and their weights; (3) correlation estimates in the chosen defect regime and errors strong enough to survive the thermodynamic limit followed by large distance. Neither (2) nor (3) has been proved here.

## Why weak transfer estimates are insufficient

If an effective correlation tends to zero, a scale-independent additive error epsilon cannot establish its asymptotic decay: H(r)=r^-eta and G(r)=H(r)+epsilon obey |G-H|<=epsilon but G has a positive plateau. Likewise H(r)=exp(-r) and G(r)=H(r)+epsilon obey the additive comparison but G is not exponentially decaying. This is a scalar obstruction to an inference, not a constructed Riesz Gibbs state.

A sufficient observable-level transfer hypothesis is a multiplicative comparison c H(r)<=G(r)<=C H(r) with 0<c<=C<infinity independent of distance and volume, followed by justified convergence of those very observables. This implication is elementary; obtaining the comparison from the actual microscopic gas is the unproved input. If the effective model is the defect-free Gaussian one above, even a perfect comparison transfers algebraic positional order rather than the desired positional disorder.

## Prior-work boundary

The exported canonical P0321 attempt records the already-known diagnostic that a rotation-averaged one-point orientation mean can vanish while the two-point orientation correlation remains positive. That observation is not being claimed as a new result. The present lane instead checks the positional conclusion of a Gaussian surrogate and the scale strength of the transfer to a particle Gibbs state.

## Paired-proof audit

Read w540/ATTEMPT.md after INDEPENDENT.md had been saved. AUDIT.md independently derives L1's analytic-continuation step and checks L2-L3, their constants and fixed-distance limit. Verdict: KEEP as conditional reductions; M remains unproved. The statement packet's blanket volume-only-error sentence needs qualification, although L3's actual iterated-limit proof is correct. TRANSFER_COUNTEREXAMPLE.md supplies an exact four-point L2 obstruction at the critical error rate (12 rational cases, 48 atoms), complementing w540's total-variation example.

NEXT: Package the conditional proof audit and unreviewed new claims for w542; draft concept-only brain entries.
