# Late-control supplement — scalar-Q_rest correction does not enter the rank-one Schur theorem

Fresh brain main after the primary report was `6174d29522488a240f46048df5e9b908dca12edb`, still owner revision `2026-09-22.11`. The newly completed account02/B12 correction `QFORM-SCALAR-QREST-WORST-FIBER-FALSE-v1` refutes the proposed bridge

`sup_b ||p_(Q3 | Q_rest=b)||_infinity <= C`.

Its target-valid family has exploding worst conditional core density although the full quadratic-form density stays uniformly bounded. Therefore any proof that first takes a supremum over a scalar `Q_rest` fiber is invalid.

The B18 results in `REPORT.md` do **not** use that bridge. In `QFORM-ONE-SIDED-CROSS-HALF-RIESZ-v1`, the original product banks are aggregated before any spectral conditioning. In `QFORM-HALF-RIESZ-SQUARE-TRANSDUCER-v1`, the only conditional law used is the shifted **original physical scalar pivot** given a residual value; because the pivot variable is independent of all residual physical coordinates before the shift, this conditional law is a mixture of translations of its original cap-one density and hence retains density cap one. No supremum over a conditional spectral-core density is taken.

Accordingly the new B12 correction leaves Theorem 4.1, Lemma 5.1 and Corollary 6.1 unchanged. It strengthens the architectural conclusion: retain the residual level weight inside the half-Riesz kernel until the physical square is paid; do not normalize a rare spectral fiber first.

Full QFORM remains OPEN / NOT PROVED.

