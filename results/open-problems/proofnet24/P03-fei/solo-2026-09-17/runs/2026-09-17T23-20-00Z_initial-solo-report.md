Model/reasoning: UNVERIFIED runtime metadata. Main target FEI: OPEN; finite universal erasure bound: UNMEASURED. Methods 18, 2, 11; additional route 5 prepared. One exact intermediate constant was disproved and one universal majorant was ruled out. No subagents.

# First solo checkpoint and continuation handoff

The current user asked for one famous breakthrough-level open problem, ten hours of solo work, and complete GitHub delivery for other agents. The repository was located through prior context and then read directly. The selected target is full Friedgut–Kalai FEI, with its original all-dimensional quantifier. Its significance is supported by the primary literature cited in IDEA.md. The choice reflects a concrete research route and prior relevant work, not confidence that a famous open conjecture can be settled in ten hours.

The previous P03 handoff had explicitly rotated away from FEI without solving it. Its reported certified dimension 6 is preserved as history. The new attempt does not restart that finite-cell atlas. POSTED.md and the campaign ledgers were checked for exclusions. There is no AGENTS.md in the captured repository tree. No shared root or peer report was edited.

## Mathematical work completed

1. A full proof of the erasure-entropy equivalence up to 2/ln2, using an exact Jensen–Shannon remainder, an explicit scalar bound, and coordinate restriction induction.
2. A one-sided logarithmic residual L with L<=B<=L+I/ln2, identifying the exact unpaid spectral-edge term.
3. A self-contained proof and an exact rational certificate for an 80-variable function with 4.007<B/I<4.008. The tentative constant 4 is false. This is not a counterexample to FEI.
4. A complete all-depth construction proving that the aggregate absolute-adjacent-Fourier-overlap majorant R/I is unbounded, even for finite unate functions. Exact integer/Fraction truth-table checks validate the composition identities in 52 small cases; the general proof is analytic, not an extrapolation.
5. An explicit bent-marker asymptotic establishing unbounded single-coordinate payment, in agreement with the older route warnings.
6. A proposed interior moment T_gamma, 0<gamma<1/2, and its exact NAND recursion. This is a new attack to test; no uniform bound is claimed.

All proofs and scope limitations are in ERASURE_REDUCTION.md, COMPOSITION_AND_BARRIERS.md and NEXT_STEPS.md. Their novelty is unverified. Standard information identities and known restriction/composition frameworks are credited. None is advertised as a breakthrough or a solution.

## What the numerical searches actually did

- Exhausted truth tables for dimensions 1 through 4 to check the new identities and exploratory ratios; Walsh coefficients were integers, but entropy extrema were evaluated in floating point.
- Tested 1,500 random functions per dimension 5 through 10, and 30 hill-climbing restarts per dimension 5 through 10. The local-search calculation ran about 248 seconds.
- Tested bent-marker examples for even base dimensions 2 through 16.
- Used compact disjoint-NAND recurrences to examine much larger formal dimensions. No exponentially large truth table was enumerated in those records.
- The random search suggested ratios around 3; structured composition exceeded 4, demonstrating why random-search plateaus are not evidence for a universal constant.
- A compact sweep of lexicographic starting functions on 2 through 8 bits and NAND depths 1 through 8 located the certified 80-variable witness (base size 21 of 32; depth 4). An exploratory ratio about 4.30516 appeared at base size 168 of 256 and depth 8; it is not certified and not a universal lower-bound claim here. This sweep is reproducible using the existing `indicator_state`, `nand` and `boolean_metrics` functions with those finite loop ranges.

## Exact remaining gap

No finite dimension-independent constant for L/I or B/I has been proved. Such a bound would give full FEI. The signed Fourier convolution identities are retained; replacing them by arbitrary probability-law constraints is inadequate. NEXT_STEPS.md explains precisely which stronger estimates failed and which alternative remains worth testing.

## Sources checked, 17 September 2026

- Friedgut–Kalai original source locator retained from the repository, DOI 10.1090/S0002-9939-96-03732-X; no invented conjecture number.
- O'Donnell–Wright–Zhou, primary author-hosted paper at https://www.math.ias.edu/files/ODonnell_Fourier.pdf, for the source statement and importance.
- González–MacManus–Pereyra, https://arxiv.org/pdf/2606.00246, version 2 (9 June 2026), for the current open status and restriction-induction prior art.
- Shalev, https://arxiv.org/abs/1806.03646, for extreme-regime results and limitations.
- Arunachalam et al., https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2020.45, for certificate-based approaches.
- O'Donnell–Tan, https://arxiv.org/abs/1304.1347 and its PDF, for composition prior art.
- Hod, https://arxiv.org/abs/1711.00762, for lexicographic composition lower bounds.
- Han, https://arxiv.org/abs/2312.08271, latest revision identified as 10 December 2025, for a current influence-dependent bound.

Dated search queries included `Fourier entropy influence conjecture 2026 Friedgut Kalai open`, `Fourier entropy influence edge isoperimetric deficit restriction entropy subcube partition`, `Fourier entropy erasure entropy`, and `Fourier entropy influence conditional entropy`. The June HTML initially failed to load; its PDF loaded successfully. The search does not prove novelty or exhaust all literature. No full source-matching FEI resolution was found in this bounded check.

## Delivery and duration

The initial six-file checkpoint was pushed to master as bc61775224ee67cf29a712e7e54aafc3f1f43a29 and all six file contents matched readback at that commit. The present expanded checkpoint also includes the new proofs, exact checks, all generated JSON outputs, this report and the schedule receipt. Its commit is to be reported only after a successful push and readback.

The initial session began at 22:58:53Z; this report was prepared around 23:20Z, about 21 minutes later. This is elapsed session time, not a claim of twenty-one minutes of uninterrupted model computation and certainly not ten completed hours. The requested window ends 08:58:53Z on 18 September.

One new schedule was accepted with nine hourly continuations during that window. It instructs the assistant to work alone, continue the newest repository state, push full work, preserve failures and stop at the deadline. No future run has been observed yet, and no continuous runtime or model setting is guaranteed. The exact receipt is in schedule_receipt.json. No existing schedule was changed. No email, publication, permission change or other person-directed action was taken.

```json
{
  "ledger_delta": {
    "target": "Full Friedgut-Kalai Fourier entropy-influence conjecture",
    "source": "Friedgut-Kalai 1996, unnumbered conjecture p.2999",
    "main_status": "OPEN",
    "erasure_upper_bound_before": "UNMEASURED",
    "erasure_upper_bound_after": "UNMEASURED",
    "new_exact_witness": "B/I > 4.007 on 80 variables",
    "new_route_obstruction": "R/I > (4/5)d for an explicit all-depth unate family",
    "claimed_universal_FEI_solution": false,
    "novelty": "UNVERIFIED",
    "independent_audits": 0,
    "subagents": 0,
    "methods": [18, 2, 11],
    "next_methods": [5, 13, 30],
    "remaining_obligation": "Dimension-free control of the actual logarithmic spectral-edge residual, or a different complete universal proof",
    "unchanged_count": "Not a preexisting metric for this new solo track"
  }
}
```
