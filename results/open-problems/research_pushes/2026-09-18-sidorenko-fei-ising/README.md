# Major-target continuation: Sidorenko, FEI, and Ising capacity

18 September 2026. Author of this continuation: OpenAI ChatGPT assistant. One research continuation; no delegated agents, independent human reviewers, or independent second audit. This is research delivery to the owner's private open-problems repository, not a publication or a claim that any full target was newly solved.

The owner's request quoted Ising capacity, the K(5,5) minus C(10) Sidorenko case, and FEI. This package addresses all three. **The strongest positive new calculation is the exact rank-two Sidorenko extremizer; the main general FEI result is an obstruction, not an upper bound; the Ising contribution is an explicit analytic collar and auxiliary geometry, not a complete certificate replay.**

## Results and exact boundaries

| Target | Delivered result | What is not established |
|---|---|---|
| Sidorenko, H=K(5,5) minus C(10) | At fixed negative nonconstant eigenvalue -r, the exact minimum over all rank-two nonnegative regular kernels is attained by an explicit two-block boundary kernel. A sharp sixth-order improvement is proved, and two rational rank-three counterexamples invalidate naive spectral addition. | The unrestricted graphon inequality or a reduction from all ranks to this class. Rank-two validity itself was already proved in C30's earlier report. |
| Full FEI | Systematic spectral codes and tensor amplification show that the full optimal FEI constant survives on functions whose spectra have minimum distance >k, for every fixed k; even growing-block erasure isolation is possible. The false pointwise inequality in the prior handoff is corrected, with an exact witness. | A uniform FEI constant, a counterexample to FEI, or the required universal interference decomposition. |
| Zero-margin Ising capacity | An explicit fixed tilt certifies a rational-width collar beyond Huang's known excluded half-body; explicit moment-body frontier and entropy-slack bounds; limited stored-packet inball replay. | A new complete capacity proof or a fresh end-to-end numerical replay. The qualitative half-body exclusion is already Huang Lemma 7.17. |

## Important FEI correction

The old `FINAL_HANDOFF_2026-09-18.md` asserts the false pointwise shortcut

    H(f)<=B(f)+(2/ln2)I(f).

The underlying `ERASURE_REDUCTION.md` proves only a universal implication / comparison of global optimal constants. `FEI.md` gives the exact 265-variable counterexample, the valid replacement involving all restrictions, and a broader constant-preserving coding theorem. The original files were not overwritten. Future agents should read this correction before using the handoff's first displayed reduction.

## Reading order

`SIDORENKO.md`, `FEI.md`, and `ISING.md` contain the complete arguments and remaining obligations. `SOURCES.md` pins the existing material and records relevant literature. `WORKLOG.md` separates successful arguments, rediscoveries, and failed extensions. The JSON files contain actual outputs from the supplied programs.

Run the checks from this directory:

```sh
python check_sidorenko.py
python check_fei.py
python check_ising.py
```

Python standard library only; no network, external numerical library, or proof-assistant installation is needed. The scripts regenerate the JSON next to themselves. Exact assertions use integers, rational numbers, and integer square-root enclosures. No floating-point sign decision is used.

| Check | Actual scope |
|---|---|
| Sidorenko | 32,768 edge subsets; 625 surviving terms; exact power-basis reconstruction of the Bernstein certificates; six direct two-block integrations; three exact rank-three density evaluations |
| FEI | 768 Boolean lifts; 53,248 Fourier coefficient identities; 88 spectral-block erasure tests; four random-code union bounds; exact addressing/parity witness |
| Ising | 16 finite moment-body vertices; eight frontier vertices; 288 support directions; rational collar and denominator inequalities; geometric consequences of four previously stored interval packets |

All three programs ended in `ALL_EXACT_CHECKS_PASS`. The asymptotic coding and analytic Gaussian statements are justified by the written proofs, not by finite enumeration. The Ising output expressly records that its Gaussian integral enclosures and full capacity certificate chain were **not** recomputed.

## Use by other research tracks

This is an owner-requested continuation, not a new exclusive assignment or a reopening of a retired native scheduler. It does not change problem ownership, the fleet allocation, source closure labels, public posting status, or audit counts. No peer report or shared root ledger is edited. A new restricted theorem must not be counted as closure of its parent conjecture.

Next decisive steps are mathematical: control mixed spectral directions for Sidorenko while surviving the exact counterexamples; prove a hereditary restriction or coherence bound for FEI that survives the code construction; and reproduce/review the full Ising certificate chain or replace the remaining positive-interior numerical step analytically. Mere replay of this package's finite tests is not progress on those missing steps.
