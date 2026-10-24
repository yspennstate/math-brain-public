# Prepublication correction refresh

Run `20260922T203204Z-account01-B13-qform-r19`.

After the main report was committed, I refreshed `yspennstate/math-research-brain` through main `1c504670b3dc3e3e74fe8e17f61b7a24c0b57f43`; OWNER CONTROL remains revision `2026-09-22.15` and QFORM remains the sole target.

New correction events checked after the report commit:

- `QFORM-MIXED-AMBIGUITY-BL-BANK-BARRIER-v1` (`math-research-brain@4b1267f62fef6d908f826fa381655ba644b34cc1`): refutes a different finite ambiguity Brascamp--Lieb interpolation mechanism. The r19 proof does not use ambiguity-factor interpolation; it uses the already proved diffuse complex BL theorem only after constructing an exact orthonormal rank-three physical projection whose every row leverage is <=1/2.
- `QFORM-LEAKAGE-FREE-TRIBANK-EXTRACTION-FALSE-v1` (`math-research-brain@cb5dda487a9f432d82118125f6e042172c15be3a`): refutes universal leakage-free three-scalar extraction. The r19 proof performs no leakage-free three-bank extraction.
- `QFORM-R26-ARBITRARY-JOINT-COAREA-PREMISE-RETRACTED-v1` (`math-research-brain@87e1089e313ea489ac4e35f54de15cff65587e76`) was already incorporated in the report and its refuted premise is not used.

No checked fresh correction challenges `QFORM-LONGITUDINAL-ORTHOGONAL-ABSORPTION-v1`, the determinant identity, the row-leverage calculation, or the leave-one-out Schur residual formula. Full QFORM remains OPEN.
