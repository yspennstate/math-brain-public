# r48 check record

The mathematics is proved algebraically/analytically in `REPORT.md`. The calculations below are finite sanity checks only.

Using the deterministic code in `check_r48.py` with NumPy's `default_rng(0)`, 10,000 accepted random `2 x 8` shear-frame instances were tested. The observed normalized errors were:

- combined pivot/frame currency identity
  `det(T0) det(G0) = det(T) det(G) (d0/s)(1-alpha)`:
  `1.733830093386679e-12`;
- rank-one resonance identity
  `det(H^{-1}+lambda vv^T) = [1+lambda v^T H v]/det H`:
  `8.469319889769999e-13`.

The constants evaluate to

- `4*2^(5/8) = 6.168843301631763`;
- `3*2^(5/3) = 9.524406311809198`.

All assertions in the checker pass at tolerance `1e-9`; expected terminal marker is `QFORM_B06_R48_CHECK_PASS`.

## Scope and integrity review

Changed-file allowlist for the mathematical repository is confined to this immutable run directory:

- `REPORT.md`
- `check_r48.py`
- `CHECKS.md`
- `SOURCE_PINS.md` (added separately)

Manual content review found only mathematical statements, repository pins, constants, and harmless deterministic test data. No credentials, account secrets, signed URLs, personal archives, financial/client material, or unrelated data are included. A repository-local automated secret scanner was not invoked through the available connector; this is a limited manual/fallback review and is recorded as such.
