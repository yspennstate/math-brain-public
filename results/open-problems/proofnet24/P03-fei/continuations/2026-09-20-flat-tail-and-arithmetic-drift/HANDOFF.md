# FEI handoff: flat tails and arithmetic-selector corrections

20 September 2026. **Full FEI remains OPEN / NOT PROVED.**

The complete research report, four exact checkers, their actual outputs, and all exploratory programs/results are included in this directory's scientific bundle. `restore_bundle.py` restores every listed source file into a separate local directory, verifies SHA256 values, and does not overwrite the repository. `COMPUTATION_RECEIPT.json` gives the executed checks and reproducibility results. No independent review or publication-priority clearance is claimed.

## New complete results

**One exceptional coefficient.** If all nonzero Fourier coefficients away from one arbitrary label have the same magnitude, a noncharacter Boolean function automatically has tail magnitude 2^-k and satisfies

    H(f) <= [(4k+2/ln 2)/(k+1)] Ifrak(f) < 4 Ifrak(f).

The exceptional coefficient is unrestricted. No fixed physical component-lattice denominator is needed. The proof uses the preceding centroid/bottom-digit result and pays the exceptional atom by the tail mass. Constant four is optimal over the class in the limit. This is not a new claim of priority for plateaued or monomial cases.

**Few exceptional frequencies.** If all coefficients are multiples of 2^-k and R frequencies have magnitude larger than that unit, then

    H(f) <= [6+log2(R+1)] Ifrak(f).

R counts labels, not distinct magnitudes; it can be unbounded. One-exception and plateaued bounds are sharper on their own subclasses. The proof includes the elementary universal coarse-label entropy estimate H(label)<=(2+log2 M)I for at most M spectral cells.

**Concrete family beyond a fixed lattice denominator.** For q=2^m, f(x,z,y)=1-2*1{y=xz} on three existing m-bit finite-field blocks has exceptional mean 1-2/q, flat tail 2/q^2, I=6m/q-4m/q^2, and Ifrak=6m(q-1)/q^2. Its old grid exponent m-1 grows, while the new FEI coefficient stays below four. This compares sufficient bounds, not all possible prior representations.

## Failed full-scope arithmetic shortcuts

The arithmetic remainder D is EXACTLY the one defined in the preceding spectral-lattices report; it is not a new function silently substituted for it.

- EVERY prescribed coordinate cannot be paid: a bent-background/one-point-control family has queried influence 2^-2m and Delta D>=1/8, with ratio asymptotic to 2^(2m-1).
- The proposed global coefficient two fails: the already-known ternary NAND27 function has D/I in (2.18026320913,2.18026320915). Its older H/I value is not a new record. The complete magnitude-mask calculation uses 64 seed-profile triples, not a 2^27 truth table.
- The small-cube existential selector coefficient 8-(9/4)log2(3) is correct through dimension four but FALSE globally. Every coordinate of NAND27 has Delta D/j in (8.07845974688,8.07845974689).
- Symmetric thresholds give exact all-coordinate lower bounds greater than 23.33 in dimension 512. The certificate uses rational changes in sum p_a r_a plus Delta H>=0, with exact Krawtchouk level data. No 2^512 truth table is generated.

These failures are NOT FEI counterexamples. Existence of a larger finite universal D/I bound or existential D-selector constant is still unresolved. The increasing finite threshold data do not prove all-dimensional divergence. Do not revive the refuted coefficients based on the earlier random tests.

## Actual checks

`verify_flat_tail.py`: all 65,812 Boolean functions through dimension four, including 4,480 nonunit-one-exception and 2,136 noncharacter plateaued cases; four actual finite-field truth tables through dimension fifteen with 37,436 directional checks; four prescribed-drift examples through dimension eleven; 257 scalar checks.

`verify_selector_small.py`: 65,752 positive-folded-influence coordinate certificates through dimension four, with 2,176 selected equality cases and exact prime-log margins.

`verify_nand_remainder.py`: the exact NAND27 spectrum through 64 profiles, its two 26-variable restrictions through 96 and 48 profiles, plus a full nine-bit compressor calibration. It verifies both D/I>2 and the all-coordinate charge >8.078.

`verify_symmetric_selector.py`: 29 full small-transform calibrations and six exact compressed threshold instances n=16,32,64,128,256,512. All coordinate lower bounds are exact rationals; no floating entropy subtraction is used.

All four final outputs were reproduced byte-identically in a separate directory. These are finite self-checks and analytical certificates, not a formal proof assistant or an exhaustive Boolean atlas at the largest dimensions.

## Sources and priority

Reused source blobs: spectral-lattices report `9f981c30a0c8a80b3cbad92eb531d17c64688e03`; centroid/carries `87923382aa41f3fd4cf355750679846d8e45e35d`; old NAND obstruction `014b56965a5ddd604411e0c824f5e7dbab5f866d`.

The Gangopadhyay--Stanica 2014/054 author abstract explicitly states FEI for plateaued functions. Preserve this prior-art attribution; do not market the plateaued case as a new class resolution. Full comparison with that paper's constants and concatenation hypotheses is not completed because its PDF fetch failed. No novelty claim is made for the new class theorems pending that comparison.

The remaining universal obligation is a dimension-independent estimate for arbitrary unequal Boolean Fourier weights. Neither the bounded-exception theorem, the old lattice remainder identity, nor the finite selector checks close it. No schedules, ownership, permissions or visibility settings are changed. Repository delivery alone does not demonstrate later worker uptake.
