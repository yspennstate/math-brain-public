# FEI positive continuation: quadratic coupling and cubic cores

19 September 2026. **Full Friedgut–Kalai FEI: OPEN.** This is a substantive owner-requested continuation, not an independent audit or a scheduled-run receipt.

## Read and reproduce

Read the complete [report](../continuations/2026-09-19-quadratic-coupling/REPORT.md), [checker](../continuations/2026-09-19-quadratic-coupling/verify_quadratic_coupling.py), [included dependency](../continuations/2026-09-19-quadratic-coupling/prior_exact_entropy.py), and [actual output](../continuations/2026-09-19-quadratic-coupling/verification.json). The [folder README](../continuations/2026-09-19-quadratic-coupling/README.md) explains the separate exploratory files.

Run `python verify_quadratic_coupling.py --output verification.json` in that folder. The final checker was executed twice and every non-timing output matched. This is a self-check, not Lean or independent expert validation.

## Actual mathematical delta

The prior affine-variance theorem required the quadratic seed to use parameter coordinates independent of the clause seeds. The new theorem permits arbitrary quadratic terms involving the SAME clause variables and arbitrary cross-block/free-variable couplings.

For any quadratic Q and jointly surjective collection of affine clause parameter maps L_j, the function

    F(x)=(-1)^Q(x) product_j [1-2*1{L_j x=b_j}]

satisfies `H(F)<=4 I_aff(F)<=4J(F)<=4I(F)`. Clauses of widths one and two can be absorbed into Q without independence assumptions. The joint-surjectivity requirement remains for higher-degree clauses. The constant four is sharp over this class.

The strongest version permits an arbitrary cubic phase on a separate independent core of parameter coordinates, with arbitrary quadratic coupling to all wide-clause and free coordinates. Width-three clauses are absorbed into that cubic core, removing the initial constant-eight loss. A degree-d core gives explicit constant 2^(d-1), not an absolute constant when d grows.

## Mechanism and usable lemmas

1. Multiplication by a Boolean q whose affine Fourier support has dimension rho changes squared-Fourier entropy by at most rho. The proof conserves every coset's squared amplitude mass, retaining coherent interference. For quadratic q, rho is its polar rank.
2. For a disjoint product G of one-point clauses, let epsilon_j=2^(1-r_j), epsilon=max epsilon_j, and A=sum r_j epsilon_j. If F=G(-1)^Q with polar rank rho, then

       I_aff(F)>=A+(1/2-2epsilon)rho,
       H(F)<=H(G)+rho<=4A+rho.

   This proves constant four immediately for widths at least four. The rank bound is exact for a single quadratically twisted clause; its spectrum is given explicitly by three masses.
3. For an independent k-dimensional core with every nonzero derivative having all Fourier amplitudes at most 1-2gamma, and quadratic polar blocks [Bcc,D;D^T,E], put r=rank[D^T,E]. If epsilon<=gamma<=1/2-epsilon, then

       H(F)<=k+H(G)+r,
       I_aff(F)>=gamma k+A+(1/2-2epsilon)r.

   The entropy proof uses the ACTUAL marginal coset masses, not independence of samples from the same derivative.
4. An arbitrary cubic core reduces, after absorbing its affine-derivative radical into Q, to gamma=1/4. This yields the sharp constant-four theorem even with arbitrarily many width-three clauses and more general overlapping cubic terms inside the independent core.
5. The unconditional predecessor bound T(F)<=2H(F) therefore gives T(F)<=8 I_aff(F) for the entire derivative chain on this class. No derivative-closure assumption is made.

## Exact scope and remaining gap

These statements do NOT prove full FEI. Jointly dependent higher-degree clause forms remain uncontrolled. Nor can an arbitrary cubic perturbation involving wide-clause variables be treated as an independent core. A general higher-degree derivative is a sum of characters; the rank proof uses one character for the quadratic factor and cannot simply be reused for that signed sum.

The global affine-influence-drift probe on odd majority through dimension 19 found rising finite ratios but proved no asymptotic or universal inequality. Its floating output is preserved as exploration only. Do not mark it as a refutation or proof.

Continue toward a genuinely global accumulated-allocation or hereditary-erasure estimate, or a proved extension controlling dependent higher-degree interference. Do not count a smaller class constant, an unchanged checker, or a renamed remaining inequality as source closure.

## Consumed sources and checks

Read prior `2026-09-19-affine-variance/REPORT.md` in full, blob `2fa7fb2f510b10ceedc53fd560b87defa904c6dc`; initial FEI index blob `5f9136739dcd11c90629aa4482ac0be1edfde16f`; addressing barrier blob `c1e52dff50095854d85c20e8b13a5385d91efaca`. The minimum-affine-influence framework, one-point entropy, and unconditional T<=2H are reused explicitly. No exhaustive archive reread is claimed.

Executed final checks: 2,086 entropy-gate pairs; 263 coupled-clause examples and 103,488 exact direction formulas; 18 affine lifts; 76 cubic-core examples, 32,000 direction formulas and 76 exact marginal-coset identities; 192 adapted cubic-radical reductions; exact single-clause spectra and closed-form sharpness checks. The script SHA256 is `6fbb0fe0cdf5d9b35d62df17c98b3b1985b4009410608dcfa0aebb2503d27c2b`. The included unchanged dependency SHA256 is `9600d6b961d26f9131277b830894c0e9497fefdaee2a9291507885cdf40326ab`, existing Git blob `e867ba6b12e1a3e7588fd812eba6841319cd97b9`.

Prior work by O'Donnell–Tan and Gangopadhyay–Stanica is credited. The bounded-degree special cases and quadratic Fourier facts are established ingredients. Targeted primary-source comparison is not a publication-priority clearance.

No schedules, source ownership, repository visibility, access controls, or native finite-dimensional metrics are changed. This handoff plus the current-master FEI index makes the work available to scheduled agents; it does not assert that a later worker has already read it.

## Later scheduled-worker update consumed and corrected

While delivering this continuation, the scheduled report `scheduled-continuation/runs/2026-09-19/2026-09-19T18-46-55Z__report.md` appeared, blob `2bee28b73ccddc731c5b16022412981b7e0a94f7`. It contains a valid-looking universal D_cross<=6 I_aff proof and two explicitly unproved potentials. See [our exact response](../continuations/2026-09-19-quadratic-coupling/SCHEDULED_POTENTIAL_CHECK.md), [checker](../continuations/2026-09-19-quadratic-coupling/check_scheduled_potentials.py), and [output](../continuations/2026-09-19-quadratic-coupling/scheduled_potential_checks.json).

The resource potential I_aff<=C(v+delta_Iaff) fails for every constant on one-point defects; coefficient one already fails on five variables by 13/256. The entropy potential D_cross<=4(v+delta_Iaff) fails on w_3 tensor power 22 (66 variables), by more than 0.044368942168. More generally a bounded mode-defect addition cannot repair an additive drift bound after tensorization. This does NOT refute all possible entropy-drift constants or FEI. Preserve the worker's proved one-step bound and the positive coupled-class theorem, but do not keep attempting its two false proposed potentials.
