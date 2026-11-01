# Solo FEI continuation: logarithmic criticality

## Outcome and scope

Full FEI remains OPEN. No finite universal bound for B/I, L/I, or the equivalent logarithmic functional K/I has been proved. This continuation disproves the proposed stronger interior-moment route in all positive parameters and develops two limited logarithmic mechanisms. It does not claim a breakthrough solution.

All work was done by the primary assistant. Subagents, other-model calls, commissioned audits and outside contacts: zero. The requested model preference is not a verifiable runtime property; actual model and reasoning-level metadata: UNVERIFIED.

The newest own-folder state at the beginning was the initial report and its follow-on commit `32f09f187b7becf513e83d7bf6d8efd522b11958`. A fresh recursive master tree showed no intervening later solo reports. The original checkpoint remains `bc61775224ee67cf29a712e7e54aafc3f1f43a29`. The root exclusions and P03 hard handoff were checked before reuse. The original finite-dimensional P03 metric 6 is preserved solely as a prior reported fact, not freshly audited. Its exhausted cell enumeration was not resumed.

## 1. New all-parameter obstruction

`ADDRESSING_BARRIER_2026-09-18.md` gives a pointwise Boolean construction on n=m+1+2^m variables, for every positive even m: a tag bit chooses between a bent function of m address bits and the addressed member of 2^m independent data bits.

Every nonzero signed Fourier coefficient is specified explicitly. The exact formulas are

    I=(m+2)/2,
    T_gamma=(m+1+2^(gamma m))/2,
    H=2+3m/2,
    B=m+1+[(2^m+1)log_2(2^m+1)-2^m m]/2,
    L=[m+1+log_2(2^m+1)]/2.

Thus T_gamma/I is unbounded for every fixed gamma>0, including gamma=1/4, but H/I<3. This kills the proposed power-moment proof route, NOT FEI. All-dimension reasoning is on the page, not inferred from finite computations.

More generally, replacing the logarithm of an adjacent mass ratio by any nonnegative function Phi with Phi(m)/m unbounded along even m cannot yield a uniform linear-in-influence bound. The same family rules out every universal nonincreasing integrable tail envelope for the minimum-mass-weighted logarithmic edge contrast. Any viable scale argument must control how the given function allocates its influence across scales, not merely integrate a universal pointwise tail estimate.

The exact logarithmic functional

    K=sum_edges min(p_S,p_T)|log_2(p_S/p_T)|

satisfies K<=B<=K+(2/ln2)I. This equivalence is a convenient sharpening of notation, not further progress toward a universal upper bound by itself.

## 2. A real, restricted selector payment

`SELECTOR_CHARGING_2026-09-18.md` proves

    B_data <= H(J) <= 2 I_selector

when f is affine in the selected group of data bits. Booleanity forces the data coefficients to form disjoint signed input supports, yielding a genuine input-side label J. The note proves the needed cube edge-isoperimetric inequality by induction, then charges label changes to actual selector influence.

Limitations are explicit: higher-degree overlapping data coefficients do not form this partition; selector erasure B_selector is not bounded by the lemma; taking one data coordinate at a time reuses the same influence n-1 times. No step removes those limitations.

An attempted general replacement J=the local sensitivity pattern is also refuted. A one-point flip has H(J)/I >=(n+1)/2, even though its Fourier entropy/influence ratio remains bounded. The exact construction and proof are in the note. Thus the special partition structure cannot be replaced by an arbitrary input-side description.

## 3. A true restricted logarithmic potential, and its failure mode

`NAND_LOG_POTENTIAL_2026-09-18.md` works with the unnormalized squared spectrum of an indicator A. It proves that

    K_A/I(1-2A)+(4/ln2) Q_A/I(1-2A),
    Q_A=sum_i Ahat({i})^2,

does not increase under NAND of k>=2 identical disjoint blocks, with arbitrary changing arities. Thus K_A/I can grow by at most 1/ln2 along such a chain, relative to its arbitrary seed. No unateness assumption is needed.

The same potential fails for unequal blocks: NAND with a constant-one child complements the other child, leaves Q and influence unchanged, and can increase K_A. This is an explicit counterexample, not a vague obstacle. The complement-invariant corrected functional U(A)=K_A-2Q_A log_2(E A) has an exact unequal-product identity with one negative and one positive correction term. That identity is saved as a possible future starting point, not promoted to a bound. A proof only for read-once composition would still leave arbitrary Boolean seeds uncovered.

## 4. Exact computations actually executed

Commands, run in this solo folder:

    python check_addressing_barrier.py
    python check_logarithmic_structures.py

Both returned PASS. Outputs are preserved in `addressing_barrier_certificate.json` and `logarithmic_structures_certificate.json`.

- Full integer Walsh transforms checked all 128 values at m=2 (seven variables) and all 2,097,152 values at m=4 (21 variables), matching every nonzero signed coefficient and verifying no other nonzero coefficients.
- The m=2 case checked all 128 signed convolution identities explicitly. The m=4 case did not enumerate its convolution identities; Booleanity follows directly from the truth table and written construction.
- Both cases checked exact influence, spectral entropy and the complete nonzero-edge histogram. For m=4, an exact rational fourth-root computation gives T_(1/4)=7/2, I=3.
- Large formal dimensions in the addressing output evaluate the proved closed formula only. They are not truth-table enumerations.
- Forty-one identical-block NAND examples checked the exact rational coefficient recurrences and strictly certified the potential decrease using outward rational logarithm intervals.
- Sixteen unequal-block examples checked consistency of the written product and complement identities. Overlapping interval enclosures alone are only consistency checks; the algebraic identities are proved in the note.
- Sixty-four seeded selector/data examples certified B_data<=H(J)<=2 I_selector with rational interval bounds and exact spectral label probabilities. The seed and per-instance intervals are saved.

No floating-point tolerance is used for any asserted finite inequality. NumPy in the m=4 transform uses int64 arithmetic only; transform magnitudes are at most 2^21, far below its overflow threshold. The interval implementation is the already saved standard-library `certify_nand80.py`, with 64 atanh-series terms and outward 160-bit binary rounding.

These are self-checks, not independent audits. Finite checks do not justify universal quantifiers; the proofs do.

## 5. Exploration history and abandoned directions

The initial target was T_(1/4)<=C I. A one-marker/bent construction amplified by a majority selector suggested only a gamma>1/3 obstruction: heuristically the new cost scales like k^gamma N^(gamma-1), while influence is of order m+sqrt(k)/N. Setting k of order N^2 m^2 gives a ratio of order N^(3gamma-1)m^(2gamma-1). This was an unproved exploratory scaling calculation, not a claimed theorem or an executed search. It became unnecessary when independently addressed data bits produced the exact all-positive-gamma construction above.

After that obstruction, the approach changed to retaining the logarithm, deriving its exact edge-tail representation, using real input selector partitions to pay the data cost, and deriving a contracting singleton-square potential for identical NAND composition. The two attempted extensions that actually failed are recorded with explicit counterexamples. No additional finite atlas search, random plateau inference, or new guess of a universal erasure constant was used.

## 6. Literature checks and novelty limits

Fresh web queries in this continuation included:

- `"Fourier entropy influence" "September" "2026"`
- `"Fourier entropy" "fractional" "influence"`
- `"Fourier entropy" "spectral" "edge"`
- `Fourier entropy influence conjecture adjacent coefficients fractional moment`
- `Boolean Fourier coefficients adjacent spectrum Renyi entropy influence conjecture`
- `Fourier entropy influence conjecture erasure entropy conditional entropy`
- `"Fourier" "entropy" "addressing function"`
- `"entropy influence" "partition"`
- `"entropy influence" "Renyi"`
- `"Fourier entropy" "addressing" site:arxiv.org`
- `"Fourier" "entropy" "read-once" site:theoryofcomputing.org`
- `"Fourier entropy" "decision trees" site:math.ias.edu`

Many results were irrelevant or generic; they do not establish absence of prior art or of a later resolution. No novelty claim is made.

Primary sources surfaced or reopened:

- González, MacManus and Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246, https://arxiv.org/abs/2606.00246 . Restriction-induction is acknowledged prior art, not an invention claimed here.
- O'Donnell and Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, https://arxiv.org/abs/1304.1347 . Existing composition results already cover important read-once classes; a restricted NAND potential is not a new solution for arbitrary functions.
- Shalev, *On the Fourier Entropy Influence Conjecture for Extremal Classes*, https://arxiv.org/abs/1806.03646 .
- Han, *A new bound for the Fourier-Entropy-Influence conjecture*, https://arxiv.org/abs/2312.08271 , with displayed v2 date 2025-12-10. Its marginal-influence logarithms must not be mistaken for a universal constant.

The exact relationship of the new obstruction and restricted lemmas to all existing literature remains UNVERIFIED.

## 7. Precise remaining obligation

For every real coefficient vector a whose inverse Walsh transform is Boolean, prove

    sum_edges min(a_S^2,a_T^2)|log_2(a_S^2/a_T^2)|
       <= C sum_S |S|a_S^2

with one finite universal C, or produce an actual Boolean counterexample family. Equivalently use the existing B or L formulation. The exact signed constraints remain sum_S a_S a_(S xor U)=1{U=empty}.

Any positive-power replacement is now known to fail. The live structural issue is a logarithmic payment that preserves signed realizability and does not reuse the same influence across overlapping coordinate or scale charges. The selector lemma supplies such a payment only under its explicit disjoint-support architecture.

## 8. Measured execution and preservation

This continuation began at the supplied run time 2026-09-17T23:59:07Z; the first explicitly sampled shell clock in the run was 23:59:36Z. At the report checkpoint 2026-09-18T00:18:56Z, elapsed wall time was 19 minutes 49 seconds from supplied start, or 19 minutes 20 seconds between verified shell-clock samples. That includes retrieval, reasoning, file writing and checks; it is not a measurement of continuous model compute. Additional GitHub delivery time is not included in these numbers.

The prior initial-session checkpoint was roughly 25 minutes of measured elapsed work. The interval between that session and this continuation is not claimed as active research. Neither this report nor the accepted schedule establishes an hour of work or a continuous ten-hour execution.

All substantive new artifacts and this immutable report are to be committed only beneath the existing solo folder, along with useful updates to its README and NEXT_STEPS. Delivery uses the then-current master head, a non-force ref update, and exact readback at the returned commit SHA. The actual commit receipt belongs in the external delivery record; this file does not invent a future SHA. Shared roots, peer tracks, visibility, access controls and other schedules are untouched.
