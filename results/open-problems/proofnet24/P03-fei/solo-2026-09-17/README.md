# Solo attempt on the full Fourier entropy–influence conjecture

**Full conjecture: OPEN.** No subagents were used. This is the continuation point for the user's requested ten-hour solo research window, 2026-09-17T22:58:53Z to 2026-09-18T08:58:53Z (01:58 to 11:58 on 18 September in Jerusalem).

The selected target is the Friedgut–Kalai FEI conjecture (1996), a major open problem in Boolean analysis and theoretical computer science. The work aims at a full universal result; a successful solution is not promised.

## Read in this order

1. The newest timestamped report in `runs/`.
2. `FINAL_HANDOFF_2026-09-18.md`: self-contained final status separating proved theorems, exact certificates, experiments, failed routes, and the unresolved full-scope inequality.
3. `ERASURE_REDUCTION.md`: complete proofs reducing FEI, up to an explicit additive constant, to bounding the aggregate conditional entropy of spectral coordinates.
4. `ADDRESSING_BARRIER_2026-09-18.md`: every positive-power adjacent-mass majorant is false; logarithmic growth is critical. This supersedes the initial moment proposal.
5. `SIGNED_BALANCE_AND_LINEAR_BASIS_BARRIER_2026-09-18.md`: exact signed overlap cancellation, its scale-local failure, the obstruction to every fixed linear basis, and the exact partial-Boolean closure barrier for parity-query induction.
6. `UNEQUAL_NAND_CONTRACTION_2026-09-18.md`: a complement-invariant logarithmic potential that contracts under arbitrary unequal disjoint NAND, closing the unequal-block gap of the earlier restricted composition analysis.
7. `SYMMETRIC_MOD8_RESTRICTION_BARRIER_2026-09-18.md`: a transitive family proving that favorable-coordinate and aggregate restriction induction both fail for the unequal-NAND potential and every fixed singleton retuning.
8. `INTERFERENCE_PATCHING_THEOREM_2026-09-18.md`: the general closure theorem combining arbitrary partial cell spectra under bounded coherent interference, with an exact no-reuse inequality for their local Dirichlet energies.
9. `BOUNDED_COLLISION_PARITY_MULTIPLEXERS_2026-09-18.md`: the subcube-character specialization in which the FEI constant is at most four times the pointwise coherent/incoherent spectral ratio, hence at most four times label multiplicity.
10. `SUBCUBE_PARITY_MULTIPLEXERS_2026-09-18.md`: the sharp constant-four theorem for distinct data parities, plus a broader erasure lemma for arbitrary parity multiplexers.
11. `SHANNON_POTENTIAL_BARRIER_2026-09-18.md` and `FAVORABLE_COORDINATE_SEPARATION_2026-09-18.md`: the preceding bent-marker analysis, including the unbounded single-coordinate defect and its exact separation from favorable-coordinate behavior on that family.
12. `ERASURE_SYNERGY_AND_DUALITY_2026-09-18.md`: an exact parity-synergy obstruction and a one-coordinate lift proving that the complementary term H-B is itself FEI-complete.
13. `BLOCK_RESTRICTION_IDENTITY_2026-09-18.md`: the exact block restriction identity, a proved log-Sobolev information charge, and the precise surviving block-selection obligation.
14. `SELECTOR_CHARGING_2026-09-18.md` and `NAND_LOG_POTENTIAL_2026-09-18.md`: earlier restricted logarithmic mechanisms and their explicit limits.
15. `NEXT_STEPS.md`: the current full-scope gap; older text is marked historical.
16. `COMPOSITION_AND_BARRIERS.md` and `IDEA.md`: initial composition obstructions, target selection, repository handoff and source checks.

## Proved here, subject to independent review

Let B(f)=sum_i H(X_i | X_{-i}), where X has squared Fourier-coefficient law. Let K_E=sup B(f)/I(f) and C_FEI=sup H(f)/I(f). Then

    K_E <= C_FEI <= K_E+2/ln 2.

The upper implication is conditional on K_E being finite; finiteness remains unproved.

- A specific 80-variable Boolean function satisfies 4.007<B/I<4.008, by a rational interval certificate. This refutes only the provisional constant 4 for the reformulated inequality.
- For every depth d, an explicit finite unate Boolean construction has aggregate adjacent-amplitude overlap R/I>(4/5)d. Thus no constant works for that stronger majorant.
- A bent-function marker family has a single-coordinate restriction entropy increment divided by influence asymptotic to m+3/ln 2. This recovers a previously known-to-the-repository route obstruction.
- An explicit bent/addressing family has I=(m+2)/2 and T_gamma=(m+1+2^(gamma m))/2. Thus **every fixed positive-power majorant fails**, including the formerly proposed gamma=1/4, while H/I<3 for this family. The same construction proves that superlinear growth in log mass ratio cannot be used in a universal linear-in-influence bound.
- The true logarithmic functional K satisfies K<=B<=K+(2/ln2)I. For functions affine in a group of data bits, that group's erasure entropy is at most twice the selector influence. An exact logarithmic potential also controls growth along identical-block NAND compositions. Neither restricted result settles the general K/I bound.
- One selector bit can mix two parity-supported restriction spectra having B=0 into a bent spectrum having B=m+1. This rules out block-erasure averaging and every fixed restriction potential B+lambda(H-B) with lambda<1.
- The parity lift f(x,z)=g(x_1z,...,x_nz) has B=K=0, H(f)=H(g), and I(f)<=2I(g). Therefore bounding D=H-B, or proving FEI only for the even-Fourier-support subclass, is equivalent to full FEI up to factor two.
- For every restriction block A, an exact identity separates the entropy increment into H(Z_A|Z_{A^c}) and a channel mutual information at most (2/ln2)I_A. A useful universal proper-block selection controlling the first term is unproved.
- For every nonzero spectral translation U, the total absolute overlap on same-sign coefficient pairs equals that on opposite-sign pairs. A one-point-defect family nevertheless places all logarithmic edge cost on the opposite-sign class, so this exact cancellation cannot be localized by magnitude scale without a new transport argument.
- The same one-point family has generalized influence 2/2^n in every nonzero direction. Hence every spanning set of fixed parity measurements incurs a marginal-entropy bound larger than the actual influence by an unbounded factor. Allowing conditioned parity queries leads exactly to Fourier projections of partial Boolean functions; every partial Boolean function occurs as such a branch, and a universal normalized FEI bound for that class would imply full FEI by tensor amplification.
- For indicator functions, the complement-invariant potential V=K_A-2Q_A log_2(EA)+(2/ln2)Q_A contracts under every unequal disjoint NAND composition. It gives K/I<=2+2/ln2 and hence H/I<=2+6/ln2 for read-once NAND/De Morgan formulas. FEI for read-once formulas was already known; this explicit potential does not control arbitrary seeds or arbitrary Boolean functions.
- No fixed singleton correction U+cQ can be inserted into a universal one-coordinate restriction induction. A bent function with a one-point marker has selector influence 2^(-m), while its restriction defect divided by that influence is `[1/4+1/(2ln2)+o(1)]m`, independently of fixed c. Thus product factorization, not merely Booleanity or retuning the Q coefficient, is essential to the NAND contraction.
- The symmetric family `A_n(x)=1{|x| mod 8 in {0,1,2}}`, for `8|n`, defeats even favorable-coordinate and aggregate versions of that restriction induction. Every coordinate is equivalent and its defect/influence ratio is `gamma n+o(n)`, where `gamma=(3sqrt(2)/8)sin^2(pi/8)log_2(cot^2(pi/8))` is about 0.19751. This holds for `U+cQ` with every fixed c and is proved by an exact eighth-root spectral decomposition.
- If selector space is partitioned into subcubes and each cell chooses a distinct signed data parity, then the exact spectral entropy is twice the selector-label entropy and `H(f)<=4I_x(f)<=4I(f)`. The constant four is asymptotically sharp for this class via ordinary addressing. Without the subcube assumption, the data-coordinate erasure still satisfies `B_y<=2I_x` for every parity multiplexer. This is a full theorem for the stated class, not a proof of universal FEI.
- Distinct parity labels are not essential. For a boundary-separated subcube parity multiplexer, let `Lambda` be the maximum pointwise ratio between each coherently combined conditional selector spectrum and its incoherent cell mixture. Then `H(f)<=4 Lambda I_x(f)`. If no data parity is used by more than `R` cells, Cauchy--Schwarz gives `Lambda<=R`, hence `H(f)<=4R I_x(f)`. This is a controlled-overlap class theorem; no bounded-overlap decomposition of arbitrary Boolean functions is known.
- More generally, arbitrary signed selector cells satisfy the exact patching inequality `H(f)<=Lambda[H(J)+sum_j delta_j E_j]`. Under boundary separation, their Dirichlet energies obey `sum_j D(v_j)<=I_x(f)` and `H(J)<=2I_x(f)`. Hence any common local partial-spectrum bound `E_j<=C D(v_j)/delta_j` patches to `H(f)<=Lambda(C+2)I_x(f)`. This is a closure theorem, not a universal bound: arbitrary partial Boolean leaves are FEI-hard, and no canonical bounded-`Lambda` decomposition is known.

No novelty claim is made for these reformulations or obstructions. No independent audit occurred, in accordance with the user's instruction to work alone.

## Reproduce

The initial exact certificates and the new logarithmic-structure checks require only Python's standard library:

```bash
python certify_nand80.py
python check_overlap_recursion.py
python check_logarithmic_structures.py
python check_erasure_synergy.py
python check_block_restriction.py
python check_signed_basis_barrier.py
python check_unequal_nand_potential.py
python check_shannon_potential_barrier.py
python check_favorable_coordinate_separation.py
python check_symmetric_mod8_restriction.py
python check_subcube_parity_multiplexers.py
python check_bounded_collision_parity_multiplexers.py
python check_interference_patching.py
```

The addressing check uses the standard library for a full seven-variable transform and, when NumPy is available, also checks all 2^21 truth-table entries with an integer Walsh transform:

```bash
python check_addressing_barrier.py
```

The exploratory calculations require NumPy:

```bash
python experiments.py --mode baseline --output baseline_results.json
python experiments.py --mode search --output local_search_results.json
python composition_search.py
```

Supplied outputs were generated during the recorded solo sessions. The new addressing and logarithmic-structure outputs use exact integers and rigorous rational logarithm intervals. The older exhaustive entropy calculations through four variables use exact Walsh coefficients but floating logarithms: their maxima are exploratory, not certified optimal constants. The large formal dimensions in composition output use exact algebraic recurrences evaluated numerically, not truth-table enumeration. The highest-depth rows may suffer cancellation or floating-point drift; use the rational certificate for the claimed strict inequality.

## Execution and GitHub provenance

Initial complete checkpoint: `bc61775224ee67cf29a712e7e54aafc3f1f43a29`, read back and matched for all six initial files. Subsequent commits contain the full additional proofs, certificates, outputs and handoff.

The scheduler accepted nine hourly solo continuations from 02:58:53 through 10:58:53 Jerusalem time on 18 September. `schedule_receipt.json` preserves the accepted schedule and full instructions. The schedule is enabled; the returned next-run time was null. Acceptance is not evidence of future execution or a continuous ten-hour process. Each continuation must preserve actual research and report actual execution limits honestly.

The ten-hour window is not ten hours of completed work. The latest run report records the measured elapsed time of the initial session. The scheduler exposes no model or reasoning selector. No existing research worker or other schedule was modified.
