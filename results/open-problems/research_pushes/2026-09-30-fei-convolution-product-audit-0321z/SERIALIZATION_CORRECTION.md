# Addendum: original floating interval exports are not certificates

30 September 2026. This addendum preserves and qualifies the original [independent audit at commit 933891c](https://github.com/yspennstate/math-open-problems/blob/933891c27be3104c3a6f6e310f2db388d193a123/research_pushes/2026-09-30-fei-convolution-product-audit-0321z/AUDIT.md). No original audit, input, script, or result file has been overwritten by this addendum.

## Corrected verdict

- **Mathematical statements and internal exact acceptance arithmetic: PASS, unchanged.**
- **Original convolution/product JSON fields named `*_interval`, if used as certified enclosures: FAIL.** Ordinary round-to-nearest `float()` conversion does not preserve outward containment.
- **The independent audit's `independent_results.json`: PASS.** Its six enclosure objects contain exact `rational_lower` and `rational_upper` strings; floats are separately labeled `decimal_summary` and are not asserted to be bounds.

The preserved audit input `product/witness.json` is a copy of the original product source. Its old display-interval metadata retain this defect and must not be used as certified bounds. Its explicit Boolean truth table is unaffected. The independent checker reads only `n` and `negative_f` from that file and computes every accepted bound itself.

The original audit noticed that the source's floating endpoint pairs were only summaries and suggested exact serialization as an optional reproducibility improvement. That was insufficiently explicit for artifacts whose field names imply certified intervals. Exact rational serialization or genuinely outward exported bounds are required before those fields can be consumed as enclosures. The original reports' caveat that displayed decimals are summaries does not convert those decimals into rigorous interval endpoints.

The mathematical PASS is not withdrawn: both source scripts decide their inequalities using rational enclosures before converting their output to floats. Their analytic proofs are independent of the serialized floating point pairs. Full FEI remains open, and publication novelty remains unverified.

## Two explicit failures

The affected scientific source versions remain the versions actually audited:

- Convolution package at `2fefba564fdaf0232db13ff468a89063ab29bc6c`, verifier SHA-256 `38a1f30b4cfcdb370796a6b0b37ded893aa99d21e82757260dafd4a3f987be47`
- Product package at `e894a01f20ba02694c099f903fbdf26cc39db0b3`, verifier SHA-256 `d5239cd1e8c000804c65f2f1b54aa86209977e8c2408a353328643cf5dbab501`

Both implement `encl(x)` as `[float(x[0]), float(x[1])]`.

1. Convolution `tensor_certificate.base_L_interval` exports `[1.0772085933443496, 1.0772085933443496]`. The binary64 number is approximately 5.1511e-17 below the exact rational lower bound; the literal decimal is approximately 4.7932e-17 below it. The original rational enclosure width is only about 3.553e-48. Thus the entire exported singleton lies strictly below the true quantity under either parsing convention.
2. Product `seven_bit.excess_interval` exports `[0.1630852002095617, 0.1630852002095617]`. Parsed as binary64, the point is approximately 1.0700e-17 below the exact enclosure. Parsed as an exact decimal, it is approximately 2.2433e-18 above it. It therefore fails under either convention, although the failed endpoint reverses. The original rational enclosure width is about 3.705e-47.

The adjacent `check_serialization.py` independently recomputes rigorous 64-term rational bounds, demonstrates both failures by exact fraction comparisons, and writes `serialization_results.json`. This result records exact positive separation fractions; displayed approximations above are explanatory only.

## Why binary-only directed rounding is insufficient for an unstated JSON contract

A binary float can lie below a true lower endpoint while its shortest round-trip decimal text lies above it. The seven-variable example gives this case directly. Consequently a repair that merely checks `Fraction.from_float(endpoint)` can still emit a decimal number on the wrong side when a consumer treats the JSON token as an exact decimal.

A robust repair must use one of the following contracts:

1. Serialize exact rational numerator/denominator values or fraction strings for every bound, with separately labeled approximate summaries; or
2. Move floating endpoints outward and verify both the exact binary64 value and the emitted decimal token against the original rational endpoints. Any binary-only contract would need explicit labeling and would not certify the decimal token itself.

The author was notified of the original defect and this second parsing issue. The first binary-only patch at `ada352231ccb4f37bf8faa54112a07e2213bd399` was not accepted here as satisfying the stronger exported-text contract.

## Final repaired artifact verdict: PASS

The final repair is [commit 67c4459ae0e8ae85a228c7a5c2629f003910139b](https://github.com/yspennstate/math-open-problems/commit/67c4459ae0e8ae85a228c7a5c2629f003910139b). Both corrected `encl()` implementations step toward the appropriate infinity until **both** `Fraction.from_float(endpoint)` and `Fraction(str(endpoint))` contain the source rational enclosure. The routines then assert both containment conditions. Their regression tests include values exactly represented as binary floats and exact rational midpoints between a float and its emitted decimal spelling.

Both complete corrected verifiers were independently replayed in isolated directories while intercepting every endpoint-export call. The audit checked the exact binary64 endpoint values and, separately, parsed the actual `json.dumps()` output as exact fractions. All 15 convolution and 31 product calls passed both contracts. Generated result bytes exactly matched the author's corrected outputs. The four corrected interval fields in the product's `witness.json` also passed independent 64-term rational bounds under both interpretations. In particular its corrected gap pair is `[0.16308520020956166, 0.16308520020956171]`.

The corrected verifiers' SHA-256 values are:

- Convolution: `2635bf54aab7a0f6b9da28ed9a27839015fc9687034a4997b5d17aeeac515272`
- Product: `180b1a309cd448775413497ea45fecb373c26d34376acb7c00ad26f9353fbdb9`

The two verifiers, their two result files, and the product witness were fetched at the exact final repair commit and matched the executed local bytes. `repaired_serialization_verification.json` records the replay results and hashes. The old scientific commits retain their failed serialization status; the final repair does not retroactively make their old endpoint tokens valid.

## Preservation and independent exact output

The original independent checker was rerun in a separate temporary directory. Its full `independent_results.json` reproduced byte-for-byte, including all exact fraction strings and the executed-file hash. The original six archived audit files remain unchanged. The new serialization check verified all six rational-endpoint objects and recomputed the seven-variable gap exactly.

This is a correction to exported-certificate validation, not a new FEI result or a retraction of the accepted entropy counterexamples.
