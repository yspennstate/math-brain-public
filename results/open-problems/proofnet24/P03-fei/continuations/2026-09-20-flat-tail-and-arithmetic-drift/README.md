# Flat tails and arithmetic obstructions — research package

20 September 2026. **Full FEI is not proved.**

Start with [REPORT.md](REPORT.md) for complete analytical proofs and [HANDOFF.md](HANDOFF.md) for the mathematical changes, failed estimates, and remaining universal gap. [COMPUTATION_RECEIPT.json](COMPUTATION_RECEIPT.json) records actual executions and exact reproducibility. This continuation is linked from the already-indexed [spectral-lattices handoff](../../handoffs/2026-09-20__spectral-lattices.md).

## Complete scientific sources

All 21 original scientific files are preserved byte-for-byte in the seven text parts under `bundle/`: the report, worklog, handoff, four executable exact checkers, four actual outputs, all exploratory code/results, and their scientific manifest. The parts encode XZ-compressed UTF-8 JSON. They are an archive, not separate directly executable source files; the full proof and handoff are also native Markdown here for immediate reading.

From a checkout of this directory, using Python 3.10 or later:

```sh
python restore_bundle.py --verify-only
python restore_bundle.py --output restored_sources
cd restored_sources
python verify_flat_tail.py
python verify_selector_small.py
python verify_nand_remainder.py
python verify_symmetric_selector.py
```

The restorer uses only the standard library, verifies every part's byte count/SHA256/Git blob SHA, verifies the compressed capsule, and verifies each scientific file. The destination must not exist; no existing source or repository file is overwritten. The checkers additionally require NumPy. They write their output JSON files inside the restored directory.

All 21 restored files were checked against the original local source bytes. Each of the four scripts was rerun from those restored files, and all four outputs matched the saved originals byte-for-byte. Earlier separate-directory replays also matched. These are reproducibility checks, not independent mathematical review or proof-assistant formalization.

## Scope reminders

The flat-tail theorem has one arbitrary exceptional Fourier coefficient; it is not unrestricted FEI. The few-exception theorem pays the number of exceptional frequency labels, not just the number of magnitudes. The arithmetic remainder's prescribed-coordinate payment is disproved for every fixed coefficient. Global D<=2I and the small-cube existential selector coefficient are also disproved, but no theorem excludes every larger finite global or existential coefficient. The finite symmetric-threshold lower bound exceeds 23.33; it is not an asymptotic divergence theorem.

The 2014 Gangopadhyay--Stanica paper already states FEI for plateaued functions. Retain that prior-art attribution. The new theorems' precise overlap with its full hypotheses and constants remains unchecked; publication priority is not claimed.

No schedules, ownership, permissions, visibility settings, or native finite-dimensional metrics were changed. File availability does not demonstrate subsequent worker uptake.
