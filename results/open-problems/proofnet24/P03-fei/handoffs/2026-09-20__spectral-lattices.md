# FEI handoff: unequal Fourier weights through lattice-valued components

## Additional continuation: growing-depth remainder stopping and completed recovery

20 September 2026. Read the [growing-depth handoff](2026-09-20__growing-remainder-stopping.md), [full proof](../continuations/2026-09-20-growing-remainder-stopping/REPORT.md), [exact checker/output and manifest](../continuations/2026-09-20-growing-remainder-stopping/MANIFEST.json), and [recovery delivery record](../continuations/2026-09-20-remainder-isolation-and-drift/DELIVERY.md). The preceding remainder-isolation archive originally recorded NOT_CONFIRMED execution; a display-only serialization repair now permits a completed PASS and byte-identical separate replay. The original failed record is preserved, not relabeled as an earlier success. The complete proofs, worklog, actual 1,024-variable input certificates and nine-variable witness are delivered; a checksummed decoder restores the losslessly factored verification JSON.

For the transitive family T_{k,N-1}, N=2^k, the new theorem overcomes its own fixed-depth remainder obstruction by a growing-depth tree. The exact band valuation is nu_2 binom(m,b); after removing a power-of-two number L of blocks, R(T_{k,N-1-L})<=4q^(N-1-L)/L!. Taking the smallest power of two with L!>=N and capping block inspections gives maximum depth <=4L+8k<=16k, expected queries <=2L, and D(root)-E D(leaf)<=5[I(root)-E I(leaf)]. This is a family-specific theorem with maximum depth O(log n), NOT a universal coefficient five or a full FEI proof. The inherited lower bound also excludes maximum depths below (1-eta)ln N/ln ln N asymptotically. Both the old fixed-depth impossibility and the new construction are retained.

Proof commit `31e92f8e7ed45dec82253a6c1bbf9ca5ea102379`; checker `25289a865623751a9fd10374c4a270e7787b6809`; output `e1b328e06a7df59cebc69171537762f129b6cc74`; handoff `92954fca3eb2e41eae339217d442d9b556ecbbfc`. Remote content hashes were read back. The normalized spectral-information route is recorded as an identity with its universal bound still missing. No schedules, ownership, permissions, visibility or metrics changed. The concurrent flat-tail continuation and all original lattice material are preserved below.

## Subsequent continuation: flat tails and arithmetic-selector corrections

20 September 2026. The [new complete proof](../continuations/2026-09-20-flat-tail-and-arithmetic-drift/REPORT.md) and [new handoff](../continuations/2026-09-20-flat-tail-and-arithmetic-drift/HANDOFF.md) continue the work below. All 21 scientific files, including four exact checkers, their actual outputs, and raw exploratory code/results, are preserved in the verified source capsule. Run the [non-overwriting restorer](../continuations/2026-09-20-flat-tail-and-arithmetic-drift/restore_bundle.py) after checking out the directory; [BUNDLE_MANIFEST.json](../continuations/2026-09-20-flat-tail-and-arithmetic-drift/BUNDLE_MANIFEST.json) verifies every part and [COMPUTATION_RECEIPT.json](../continuations/2026-09-20-flat-tail-and-arithmetic-drift/COMPUTATION_RECEIPT.json) records all four actual byte-identical replays. The proof and handoff are also ordinary readable Markdown files, not just encoded content.

**New positive theorem:** one arbitrary exceptional Fourier coefficient and a flat nonzero tail imply H<=4 Ifrak, with the stricter coefficient (4k+2/ln2)/(k+1) when the tail magnitude is 2^-k. No fixed component-lattice denominator is needed. A separate theorem gives 6+log2(R+1) for a unit tail with R exceptional frequency labels. Both retain their stated spectral hypotheses; neither is unrestricted FEI.

**Full-scope corrections:** the same arithmetic remainder D defined below cannot be paid at EVERY prescribed coordinate, by an exponential-ratio Boolean family. The tentative global D<=2I estimate is false by an exact NAND27 calculation. The selector coefficient sufficient through dimension four is false in dimension 27, and symmetric thresholds require any universal existential selector coefficient to exceed 23.33. Existence of a larger finite universal coefficient is still unresolved; finite growth through dimension 512 is not an asymptotic divergence proof. These examples do not refute FEI.

**Prior art:** Gangopadhyay--Stanica, Cryptology ePrint 2014/054, explicitly establishes FEI for plateaued functions. Retain that attribution rather than claiming the plateaued class itself as new. The comparison of its full constants/hypotheses with the new one-exception theorem is incomplete; no priority claim is made.

Native full-proof commit: `c44353afedc127391ecdfbaa7c8fd92815c793b0`; report blob `d7d578e22a5e4ba55d2e06c384330bc7c2a1ffb2`. All seven capsule-part blobs match local bytes. Every restored source matches the original, and all four restored checkers reproduce the saved outputs byte-for-byte. Full FEI remains OPEN. No schedules, ownership, permissions, visibility or atlas metrics changed. The original handoff is retained below without removing any hypothesis.

## Original lattice continuation

20 September 2026. **Full FEI remains OPEN / NOT PROVED.**

Read the [complete proof](../continuations/2026-09-20-spectral-lattices/REPORT.md), [exact checker](../continuations/2026-09-20-spectral-lattices/verify_spectral_packets.py), [actual output](../continuations/2026-09-20-spectral-lattices/verification.json), and [manifest](../continuations/2026-09-20-spectral-lattices/MANIFEST.json). The exploratory folder retains the failed level-degree and automatic-integrality approaches, not merely the successful conclusion.

## Main theorem and exact hypotheses

For each distinct nonzero Fourier magnitude a, define the PHYSICAL function

    f_a(x)=sum_{S:|fhat(S)|=a} fhat(S) chi_S(x).

If every f_a takes values in 2^-s Z, with one fixed integer s>=0, then

    H(f)<=(4+2s) Ifrak(f)<=(4+2s) J(f)<=(4+2s) I(f).

This allows arbitrarily many unequal Fourier magnitudes and several valuation levels. The hypothesis is about the values of the inverse-transformed projections f_a, NOT just about the denominators or sizes of Fourier coefficients. Integer components give class constant four, half-integer components give six. Four is optimal for the integral class in the limit by the standard addressing example; no sharpness is claimed for s>0.

The proof extends the preceding centroid theorem to integer-valued flat packets, uses Boolean projection orthogonality to bound their lattice spacing, and treats large bias separately by edge isoperimetry and a proved scalar inequality. Simply replacing an additive 2s error by 2s I without the large-bias argument would be invalid.

Integer components automatically form a signed physical partition: at every input exactly one equals f and the others vanish. The theorem also yields constant four for nonaffine physical cells whose signed indicators have flat spectra and distinct actual tag characters. An explicit nine-variable example has two magnitudes, three nonaffine cells, H=7, I=15/4 and Ifrak=13/4.

## Composition with no factor-count penalty

Independent logical factors with exponents s_t<=s retain the single coefficient 4+2s after any JOINTLY SURJECTIVE affine input map and output character. This uses the earlier exact affine-minimum tensorization/lifting theorem. Independence and joint surjectivity are not optional.

There is a separate branch rule: flat ternary selectors with disjoint physical supports AND disjoint Fourier supports can multiply arbitrary Boolean branches sharing the same residual variables. Exact entropy and energy identities give max{4,C} when all branches have folded FEI constant C. The selector variables must be disjoint from the residual variables. Arbitrary overlap without spectral separation and arbitrary affine mixing of nonflat branches are not covered.

## What failed

The five-variable Boolean function

    f_*=1-2*1{y1=x1*x2, y2=x1*x3}

has one Fourier coefficient 1/2 and twelve of magnitude 1/4. Nevertheless its magnitude components are 1/2 and f_*-1/2, the latter taking values 1/2 and -3/2. Thus power-of-two coefficients do NOT imply integral components. This failed claim survived the exhaustive checks through dimension four; it must not be reused. The example has H=7/2, I=15/8 and is not a FEI counterexample.

The t-fold independent product of this example has smallest common component grid denominator exactly 2^t, while H/I remains 28/15. Thus a fixed grid cannot be assumed for all power-of-two spectra. The independent-factor certificate still gives constant six for this family; the merged denominator bound is simply wasteful there.

## Universal residual, not a closure claim

Let epsilon_a be the signed mask of one magnitude support, let V_a be its unnormalized Walsh transform, and let r_a=min_{V_a(x)!=0} nu_2(V_a(x)). Put b_a=a 2^r_a and p_a=|A_a|a^2. The report proves

    0<b_a<=1,
    Ifrak >= (1/2) sum_a p_a r_a,
    H = 2 sum_a p_a r_a + 2 D,
    D = sum_a p_a log2(1/b_a) >= 0.

Hence H<=4 Ifrak+2D universally. D is NOT bounded here by a universal multiple of influence. Such a bound would close FEI and remains a substantive missing step; naming this residual is not counted as resolving it. The bounded-grid hypothesis pays it in the proved subclass. Keep the original universal erasure/selector target and all earlier retired-route warnings intact.

## Executed checks, delivery and provenance

The final checker passed all 65,812 Boolean functions through dimension four, with 147,348 nonempty magnitude components; all 6,651 ternary functions through dimension three; exact five-, nine-, ten- and fifteen-variable examples; 16 affine/character images; 24 shared-residual branch pairs; and 257 scalar checks. These families overlap and are not exhaustive Boolean coverage at their largest dimension. A separate replay of the exact committed checker produced byte-identical output. No independent review, proof assistant or publication-priority clearance is claimed.

Proof commit: bce8ebea37f535bc7a9bdc8845f7fc16b1075dab; verified blob 9f981c30a0c8a80b3cbad92eb531d17c64688e03.
Checker commit: 28264ba544ef4b96de2e0f1f4c2b9d893866b88e; verified blob ead06f867ea3078fb50e7d9e908ab06bb4842697.
Output commit: 5f5b7abd061b635575eb00ad9a7718d2eee5ebb3; verified blob 8ea6746411dcbdf7bdd3bb0c155a8f96d3bbd55b.

The proof reuses the centroid/carries report (blob 87923382aa41f3fd4cf355750679846d8e45e35d) and the affine-minimum identities (blob 2fa7fb2f510b10ceedc53fd560b87defa904c6dc), with their original hypotheses. The earlier stronger finite-k plateaued coefficient is preserved, not re-announced as new. No schedules, ownership, permissions, visibility or native atlas metrics changed. Delivery establishes availability, not subsequent worker uptake.
