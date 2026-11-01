# FEI continuation handoff — polynomial cores and tag phases

20 September 2026. Full Friedgut–Kalai FEI remains **OPEN / NOT PROVED HERE**. No schedule, ownership, permission, visibility, or native atlas metric is changed.

## Read first

[Main proof](REPORT.md) extends the prior single-core bounded-degree result to arbitrarily many independently supported part-symmetric cores, with arbitrary higher-degree polynomial coupling and no number-of-cores penalty. The constant is

`max(12.04 + log2(max_t d_t), 2^r h2(2^-r) + 2/ln 2)`.

In particular, arbitrary degree-at-most-seven couplings of symmetric cores retain 12.04. The prior scheduled single-core theorem and prior quadratic product theorem are credited in the report. The new proof supplies the missing cross-core derivative gap, weighted local-defect and hereditary variants, and a joint block-deletion identity.

[Polynomial tag extension](TAG_PHASE_EXTENSION.md) consumes the concurrently written affine-fibre gluing theorem, whose proof blob is `29d8afcabc09ee1564a1e0db51cf42a21ffa804d`. For actual physical tag coordinates and certified affine-fibre sections, it replaces quadratic tag phases by arbitrary degree-r phases with coefficient `max(4,C0,2^(r-1) h2(2^(1-r)))`. This retains sharp class constant four for cubic tags, and retains 12.04 through tag degree eleven when the sections have that certificate. Valid gluing can be iterated without a depth penalty. Appending or fixing tags does not transfer this to arbitrary Boolean functions.

[Operator obstruction](UNITARY_ERASURE_OBSTRUCTION.md) records a genuine attempt at the full universal erasure inequality. The proposed general-unitary / real-orthogonal-involution relaxation is false: an explicit family has averaged column erasure / normalized trace-norm commutator ratio greater than `log2(M)/10`. The matrices are not Boolean convolution matrices. This is not an FEI counterexample.

## Exact checks actually run

The main checker ran 46,634 overlapping core/phase parameter cases, 365,403 physical assignments for residual polynomial structure, and 2,308 universal block-deletion cases. Its two coordinate-gap counts are 14,753 cross-core and 126,240 internal checks.

The tag checker ran 81,852 exhaustive phase-comparison cases through dimension three, 280 affine-fibre/tag cases (including degrees through eleven), and 1,040 exact derivative-gap checks. The operator checker verified the full 64-by-64 example by integer matrix products and exact logarithmic identities, plus the Walsh pattern through M=256.

All three complete checkers passed; reruns produced byte-identical JSON output. Integer/rational arithmetic and outward rational log enclosures are used. None of this is independent expert review, formal proof verification, or publication-priority clearance.

```sh
python3 verify_polynomial_symmetry.py --output verification.replay.json
python3 verify_tag_phase.py --output tag_phase_verification.replay.json
python3 verify_unitary_erasure.py --output unitary_verification.replay.json
```

Compare each replay against its corresponding committed JSON. `MANIFEST.json` records SHA256 values.

## Unpaid full-scope step

For a squared Boolean Fourier sample S, a finite universal bound

`sum_i H(S_i | S_{-i}) <= K I(f)`

would imply unrestricted FEI with coefficient `K + 2/ln 2`. It has not been obtained. Alternatively, a valid whole-function dimension-adaptive endpoint selector could close the induction; the concurrent affine-fibre report's single-fibre obstruction does not refute that selector.

Do not replace joint allocations by a universally payable sum of marginal bit entropies; the explicit rare-point family in REPORT.md has a diverging marginal charge/influence ratio. Do not replace Boolean convolution by arbitrary orthogonal involutions; the companion supplies a counterexample. Do not treat the new stopping classes as an unrestricted representation theorem, or duplicate the prior single-core degree-seven result as new.

The strongest surviving use of this continuation is as a larger exact stopping class while retaining signed Boolean convolution or whole-function cancellation at genuinely dependent high-degree nodes. Repository availability does not certify that a later worker has already consumed the result.
