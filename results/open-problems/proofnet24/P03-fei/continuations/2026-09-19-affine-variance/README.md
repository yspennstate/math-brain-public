# FEI affine-influence and variance continuation

**Full FEI has not been proved.** This directory preserves the affine-variance research package, with analytical proofs and executed exact self-checks. It is not an independent audit or a Lean proof.

## Read and reproduce

Read [REPORT.md](REPORT.md) and the [worker handoff](../../handoffs/2026-09-19__affine-variance-positive-results.md). Run:

```sh
python verify_affine_variance.py --part all --output reproduced.json
```

Python 3.10 or newer and its standard library suffice. `prior_exact_entropy.py` is the unchanged, attributed dependency from the September 19 balanced-substitution checker. Compare the parsed output with `verification.json` after removing `elapsed_seconds`; timings need not agree. Do not overwrite the historical output to imply an independent audit.

## Scope

The saved report establishes a sharp accumulated-variance bound, tensorization and a monotone formula for minimum affine influence, and a constant-four FEI theorem for the explicitly stated class under jointly surjective affine mixing. It does not prove unrestricted FEI, justify dropping surjectivity, or reinstate either disproved pointwise resolvent bound.

## Delivery recovery

This directory is the connected-GitHub delivery of the actual conversation artifact `FEI_Affine_Variance_2026-09-19.zip`. [DELIVERY_RECOVERY.md](DELIVERY_RECOVERY.md) records the byte hashes, successful local replay during delivery, and scope. The proof report, checker, dependency, saved results, and handoff are unchanged from that ZIP. This navigation README is updated for repository use.

Statements about failed GitHub delivery in the report and handoff describe the earlier creator session. `LOCAL_DELIVERY_ORIGINAL.json` is its unchanged historical receipt, not the current upload status. Use this directory's actual commit history for the recovered delivery. File availability does not establish that a scheduled agent has already read or improved the work.
