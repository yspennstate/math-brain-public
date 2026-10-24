# Shifted thresholds and Han's FEI criterion

**Full FEI is not proved.** `REPORT.md` proves logarithmic divergence of Han's absolute-overlap/influence ratio at every coordinate of an explicit symmetric threshold family. This negatively resolves the stronger auxiliary Question 3.1; known FEI for symmetric functions remains unaffected.

Read `REPORT.md` for the complete proof and primary-source references. Run

```sh
python verify_threshold_obstruction.py --max-m 64 --output verification_replayed.json
```

Compare the parsed results with `verification.json`, allowing only elapsed time to differ. The integer/Fraction checker verifies finite Fourier formulas, all-coordinate identities and outward rational decimal intervals. It does not prove the infinite-dimensional asymptotics by enumeration. Do not run Python with `-O`, which disables assertions.

`RECOVERED_STATUS.md` separately describes the unpushed prior September 19 patch and its critical drift warning. The new proof is independent of it. That notice does not claim the entire recovered patch is uploaded to this repository.

Research handoff: `../../handoffs/2026-09-20__shifted-thresholds-refute-han.md`.

No independent expert audit, exhaustive priority check, Lean verification, public publication or full-FEI closure is asserted.
