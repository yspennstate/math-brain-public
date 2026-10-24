# FEI verification output correction: outward decimal serialization

30 September 2026, 03:35 UTC. **Full classical FEI remains OPEN.** No analytic theorem or exact rational acceptance comparison changes.

## Defect identified by independent review

The helper `encl()` in three September 30 verification scripts converted the lower and upper exact `Fraction` endpoints with ordinary `float()`. That gives nearest-rounded display values, not necessarily outward bounds. Several JSON fields named `*_interval` could consequently exclude the exact mathematical value by a fraction of a floating-point ulp. The old exported decimal intervals must not be treated as certified enclosures.

The Hadamard audit identified examples at L=2 and L=4 where the serialized endpoints lie respectively above or below the exact rational enclosure. The issue also affects the shared helper in the two earlier packages, so all three are repaired together.

## Corrected implementation and scope

The helper now converts each exact rational endpoint, checks both the resulting double by `Fraction.from_float` and its JSON decimal spelling by `Fraction(str(endpoint))`, and uses `math.nextafter` toward negative infinity for a lower endpoint that rounded upward under either interpretation, or toward positive infinity for an upper endpoint that rounded downward under either interpretation. It asserts both

    Fraction.from_float(lo) <= exact_lo <= exact_hi <= Fraction.from_float(hi)
    Fraction(str(lo)) <= exact_lo <= exact_hi <= Fraction(str(hi))

before returning the displayed pair. Exact-point self-tests cover positive, negative, zero, dyadic, and non-dyadic rational inputs. An additional regression places the exact rational value midway between a float's binary value and its decimal spelling; this catches the distinction found in the seven-variable lower endpoint. Each complete verifier was rerun, and its output records the SHA-256 of the corrected executed bytes. The seven-variable witness JSON was regenerated from the corrected product certificate.

The first repair commit `ada352231ccb4f37bf8faa54112a07e2213bd399` checked binary containment only. Independent review then identified that its shortest decimal spelling could still fall on the wrong side of a rational bound when read as an exact decimal number. The final revision checks both semantics. Do not treat that intermediate binary-only repair as a certified exact-decimal enclosure contract.

Affected packages:

- `research_pushes/2026-09-30-fei-normalized-convolution-0236z/verify.py` and `verification.json`
- `research_pushes/2026-09-30-fei-overlapping-product-0302z/verify.py`, `verification.json`, and `witness.json`
- `research_pushes/2026-09-30-fei-hadamard-rounding-0330z/verify.py` and `verification.json`

The rational atanh-series bounds and the rational comparisons deciding the signs were correct and remain unchanged. Integer Walsh transforms, polynomial identities, influences, support counts, tensor identities, and all analytic arguments are unchanged. The amendment strengthens the exported evidence contract; it does not establish an additional mathematical theorem.

## Preserved history

The initial normalized package was at `2fefba564fdaf0232db13ff468a89063ab29bc6c`; the source-corrected product package was at `e894a01f20ba02694c099f903fbdf26cc39db0b3`; the initial Hadamard package was at `c4d07e6e2280aa54c767512540d143f930154d3c`. These immutable versions remain in history, with their output-serialization limitation now explicitly recorded. Wording-only cleanup `f3726e747609b85bfd7503fff55cc93deae443ef` did not address this later-discovered issue.

The independent audits may continue to cite those versions for their exact arithmetic and analytic reviews, but exported decimal bounds should use the corrected outputs. Neither reproducibility nor a positive internal assertion upgrades nearest-rounded display endpoints to rigorous external certificates.

No schedules, shared owner controls, peer proof files, permissions, or repository visibility are modified.
