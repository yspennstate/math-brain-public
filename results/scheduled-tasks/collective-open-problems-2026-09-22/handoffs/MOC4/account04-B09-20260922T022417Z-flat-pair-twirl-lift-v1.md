# MOC4 handoff — account04/B09 `MOC4-FLAT-PAIR-TWIRL-LIFT-v1`

Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains OPEN.

Source-bound science report: private canonical archive `proofnet24/collective-MOC4/account04/B09/20260922T022417Z-b09-moc4-r11/REPORT.md`, report blob `1ec092caac4aa78fb3998199849f632387a0c18f`. Exact verifier is adjacent as `verify_flat_pair_twirl.py`; captured output is `VERIFICATION.txt`.

## Result

Fix any row pair of `U in U(4)` and Haar-average the squared exterior-minor data over the embedded `SU(2)` acting on those two rows. The resulting complete `k=1,2,3` minor-square vector has an exact probability lift to the 24 permutation matrices. The proof is constructive:

1. the twirled top two rows have equal one-point marginals; symmetrically orient the invariant top two-set law by `x_{j->k}=q_{jk}/2`;
2. Jacobi complementarity gives the bottom unordered two-set law; a fractional orientation with the required row-3 marginals exists by the exact K4 cut inequalities coming from Hadamard plus the two-row inclusion identities;
3. conditionally couple the oriented top and bottom complementary edges; the resulting law matches all one-point marginals and the top/bottom two-set marginals;
4. row-pair symmetry plus the pointwise inclusion identity determines and matches every cross two-set marginal; complements give `k=3`.

Therefore if a support functional is flat on that entire genuine row-pair orbit,

`h_eta(GU)=h_eta(U)` for every embedded `G in SU(2)`,

then its orbit average is a convex combination of the 24 permutation-product vertices. Hence

`h_eta(U) <= max_sigma Re(eta product_i(a_i+b_sigma(i)))`.

The column-pair version follows from `U*`.

## Consequence for the campaign chain

Combine this with account04/B08 `MOC4-PAIR-FLAT-BOUNDARY-v1`: at a global support maximizer, a non-strict row/column pair is actually a completely flat pair orbit. The theorem above then rules out any support violation on that branch. Thus the previous zero-entry branch generated from pair-flatness is no longer an unpaid branch in the contradiction chain; one does **not** need an individual zero-entry common lift.

The only surviving universal branch is a global maximizer strict on all twelve row/column pair spheres. The next exact target is the OTHER-account partner result account01/B07 `MOC4-SPIN6-STATIONARY-SIX-WITNESS-v1`: prove its six-witness support inequality at a genuine pair-strict global maximizer using the exact Spin(6) stationarity equations. No claim is made that arbitrary stationary saddles satisfy it.

No genericity, simple-spectrum, invertibility, nonzero-minor or limiting hypothesis is used in the flat-pair lift; zero edge masses are handled directly. This handoff therefore closes flat-pair limit cases as well.
