C0120's cited paper concerns a planar Gaussian ground-state maximum; the stored intake broadened it to log Z_n, general weights and general dimension. The proposed one-row correction and STORE_CORRECTION.json restore the source scope without changing unverified/open-status fields.

Proved special cases, awaiting w500: exact layer-average variance decomposition, exact width-one strip variance, and a counterexample to a path-change-alone variance bridge. In a strip of r diamonds, Var(M)=(2-1/pi)r+1. At OU time r^(-alpha), 0<alpha<2, paths change with probability tending to one while normalized overlap tends to one. The unrestricted parent problem remains unresolved, and current openness/novelty are unverified.

Measured with run_bounded_verification.py: 12 deterministic checks passed; maximum geometry error 5.55e-17; independent overlap-integral/moment variance discrepancy 4.7e-13. For r=10000 and OU time 0.0001, identical-path probability is 2.54725e-20, normalized expected overlap 0.997749359, and variance 16817.901138162. These evaluate proved formulas; they are not independent proof audits.

Before: one C0120 store concept has an unsupported source scope and a qualitative decorrelation bridge. Prepared after: one correction patch, five scoped claim rows, six DRAFT concept entries and six justified relations. Submitted is separate from reviewed, ingested and retrievable; no live change or theorem promotion occurred. The hook proposal math-w498-01 has a specific fire and silent case.

Apply after independent KEEP: apply patches/01_c0120_source_scope.diff to the live problems.jsonl path named in its header, or replace only its C0120 row with SOURCE_ROW_AFTER.json; the validating integrator handles STORE_CORRECTION.json and the draft.

Risks: strip and endpoint restrictions cannot be transferred to the unrestricted model by variance monotonicity; a bridge that additionally assumes O(N/log N) variance is not refuted. Requested models do not prove served identity. No Lean/formal-check receipt is claimed.

NEXT: w500 checks L1-L3 and source scope; the next proof step is a polynomial upper bound on the unrestricted centered maximum's variance, with H_n retained as its exact independent layer-average contribution.
