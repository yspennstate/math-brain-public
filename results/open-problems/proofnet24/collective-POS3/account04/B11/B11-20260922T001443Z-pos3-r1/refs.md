# References and exact dependencies

## Current target and inherited repository state

- Inherited source claim: `operations/claims/I0122.md` in this repository. It records the general 1/3–2/3 conjecture and the exact all-posets-through-14 frontier; that finite frontier is not a width-three proof.
- Assigned partner: `proofnet24/collective-POS3/account01/B19/B19-20260921T235148Z-pos3-r01/REPORT.md`, exact chain insertion/deletion recurrence and weighted induced law.
- Connected-core reduction: `proofnet24/collective-POS3/account02/B11/20260921T235736Z-b11-44e20585/REPORT.md`, exact ordinal factorization by incomparability components.
- Exact three-chain path state: `proofnet24/collective-POS3/account01/B10/20260921T235306Z-account01-B10/REPORT.md`, ideal-state path encoding and heavy-slice normal form.
- Same-account neighboring splice: `proofnet24/collective-POS3/account04/B20/20260922T001111Z-b20-auto11/REPORT.md`, adjacent-swap one-boundary-gap law and `|Delta W|<=1` for one-element insertion multiplicity.

## External theorem actually used

Max Aires and Jeff Kahn, **Variance vs. range for linear extensions, and balancing extensions in posets of bounded width**, arXiv:2510.26134v1, 30 October 2025.

- HTML: https://arxiv.org/html/2510.26134
- Abstract: https://arxiv.org/abs/2510.26134
- Theorem 1.5: for fixed width, `delta_x -> 1/2` as rank standard deviation `sigma(x)->infinity`.
- Theorem 1.6: for fixed width, `delta(P)->1/2` as the maximum incomparability range `pi(P)->infinity`.
- Theorem 2.1: Shepp's XYZ inequality `Pr(x succeeds Y) >= product_y Pr(x succeeds y)`.
- Corollary 2.4: `sigma(x)=Theta(1/q(x))`, where `q(x)=max_k Pr(f(x)=k)`.
- Theorem 2.6: an ideal/filter boundary event lower bound. The present report retains the exact boundary sizes and exact pairwise triple-event probabilities through the two XYZ applications, yielding the product form in Lemma 2.1 before specializing to width three.

Theorem 1.6 is used only qualitatively. No numerical `K_3` and no finite-size cutoff are inferred from it.

## Current-status/source selection context

Chan and Pak, **Linear extensions of finite posets**, EMS Surveys in Mathematical Sciences (2025), DOI 10.4171/EMSS/97; arXiv:2311.02743v2, Section 13. Current target control records width two as known and selects width three as the scoped unresolved regime.

No novelty or priority claim is made for the elementary product refinement or its width-three specialization; they are recorded as internal deductions from the cited ingredients for use by the collective proof effort.
