# A032 Boolean phase realizability

## exact target, quantifiers, hypotheses and units

Determine exact phase realizability of labelled spectral laws on every uniform cube, with finite exact admission through n=4 and analytic certificates for support<=4 and uniform affine-subspace laws in every dimension. All outputs are +/-1; H is in bits, I is expected spectral Hamming weight, and D=sum_i min(Inf_i,1-Inf_i). Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Protocol fei-execution-protocol/2, revision2026-10-11-execution-v2, all rules read. Campaign README, CURRENT_STATUS, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS B07, plan Boolean phase subsection and A032 acceptance contract, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and curated sources, and earlier B05/B09/B19 reports supplied context. BOARD snapshot2026-10-11 21:55UTC was read at stage start. B07 lead notes do not exist at the supplied path. Source hashes and reading scopes are in out/SOURCE_MANIFEST.json. The four supplied paper text versions were scanned; introductions and relevant Fourier definitions and threshold Proposition7.1 composition identities were read. These class-specific papers supply no premise for this proof. ERASURE_RIGIDITY.md Section1 already proves coordinate-product spectral rigidity; its Section2 explicitly prevents a naive approximate-independence payment. No novelty is claimed for bent functions, arithmetic granularity, or the finite checking strategy.

## complete derivation or exact first unsupported line

REALIZABILITY_METHOD.md gives complete all-dimensional proofs, general integer-square and modulo4 admission conditions, XOR pair-partition certificates, complete sign enumeration, the four-atom classification, affine-flat characterization and affine quotient equivalence. The four-atom class is exactly characters or uniform affine planes. Uniform rank-r affine support is realizable exactly for even r, with an explicit quadratic truth-table formula and H<=2D<=2I.

The ten-atom law p=a^2/256 with a=(8,8,4,4,4,4,4,4,4,4,0,0,0,0,0,0) passes every separate nonzero-XOR pair partition. Nevertheless every one of its512 phase vectors, modulo global negation, has a nonzero signed convolution coefficient. out/coupled_phase_certificate.json lists each first violating XOR and integer coefficient, and all15 individually possible partitions. This is an exact obstruction to replacing coupled Boolean signs by independent equation-wise cancellations, not an FEI counterexample.

First unsupported universal line: no result here proves a dimension-independent entropy/influence payment from the simultaneous phase identities for general nonflat, growing-affine-rank spectra. The finite catalogue is not extrapolated to that claim.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede searches in SEARCH_SPEC.json and VERIFY_SPEC.json. Commands, from this run directory:

    python -X utf8 code/enumerate_exact.py --n 0 1 2 3
    python -X utf8 code/enumerate_exact.py --n 4
    python -X utf8 code/verify_direct.py
    python -X utf8 code/check_lifts.py

All admission arithmetic is integers/Fraction. The pilot found a mistaken common-mod4 filter at n=1; it was corrected to n>=2 and the pilot reran successfully. Both the endpoint correction and frozen-domain correction are recorded, with no dimension escalation. One computation job ran at a time. Estimated memory stayed below100MB; no job expected to exceed300MB. The full n=4 arithmetic run took51.018seconds, including candidate enumeration and certificate checks, below its180-second cap. n=4 enumerated32768 truth tables after fixing f(0)=+1, exactly representing all65536 tables modulo global output negation. No input or spectral-label symmetry was quotiented.

| n | truth representatives | distinct laws | arithmetic candidate laws |
|---|---:|---:|---:|
|0|1|1|1|
|1|2|2|2|
|2|8|5|5|
|3|128|30|86|
|4|32768|2261|975621|

Candidate laws exhaust nonnegative integer magnitudes of norm2^n satisfying evenness and common-mod4 where applicable; they stream through all labelled placements of every sum-of-squares multiset. Complete Boolean truth enumeration decides each candidate. n=4 has973360 impossible candidate laws. Saved catalogues provide a concrete truth mask for every realizable law and its phase multiplicity modulo global sign. A distinct direct-character implementation reconstructed all2299 saved law witnesses, checked multiset placement counts via factorials, and verified the512 coupled-phase rejections via signed convolution. Six affine examples test ranks2,3,4 and ambient n up to30, including lifted truth tables and direct transforms for n<=5. Larger ambient examples carry an exact reduced truth table and the proved lifting formula. This is author reproduction in a different representation, not independent agent acceptance.

## proof dependencies and changed downstream conclusions

No unreviewed campaign claim is a proof dependency. The new admission interface can be reused by A031/A033/A034/A078/A079. A045 receives only the explicit warning that uniform Walsh arithmetic does not apply to a biased basis. Independent XOR cancellation is now concretely refuted as a sufficient admission relaxation, even after norm, dyadic-square, modulo4 and every individual XOR partition test. The independent-product endpoint remains prior work and is not republished as a new claim. Conditional auxiliary entropy remains unpaid.

## one next mathematical action and independent reviewer

Use the explicit ten-atom coupled obstruction to isolate the first additional common-phase constraint required by A031/A033's signed entropy payment, and derive a conditional entropy consequence from that constraint rather than escalating a fixed convolution prefix. Independent reviewers: A088 and A094. Source-bound handoffs are recorded locally for supervisor collection; no messages were sent.

## actual persistence receipts or precise save blocker

All required files, exact catalogues, certificates and reproducible scripts are written inside A032's designated run; rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/ARTIFACT_RECEIPTS.json lists local file byte counts and SHA256 values. No file exceeds20MB. Shared source trees and other agents were read only; no git, brain mutation, upload, mirror verification or independent review is claimed. No save blocker remains.

## Universal bridge

This stage moves B07's G-BOOLEANITY/G-PHASE-COND admission bridge: complete certificates now distinguish globally realizable phases from independent XOR cancellations, with an ambient-independent affine quotient and closed sparse/affine-flat cases. It does not advance a numerical universal C018/C019/C020/C024 payment. What remains is to convert common-phase consistency into a paid entropy remainder for nonflat spectra of growing affine rank, while retaining arbitrary tensor conditional entropy. Applying the ten-atom obstruction to the live signed-payment derivation is the shortest next route: it identifies information discarded by the relaxation and tests the needed universal mechanism, whereas merely enumerating another dimension would only extend the finite census.
