# STRAT17 log

2026-11-13 15:57 +04 — Initial request. Read-only derivation found negative increments but a split-class endpoint comparison. Shared mesh writes were denied. No source was edited.

2026-11-13 16:09 +04 — Resume authorized. Parent an agent holds exclusive coordination claim clm-d65c361681 for this workspace. No local mesh/database writes are needed.

PROVED preparation (replay_all.py will verify): copied the exact STRAT16 proof closure and its three STRAT7 inputs byte for byte into inherited16; copied the STRAT15 theorem statement and replay receipt into prior15 as black-box provenance. source_hashes.json records their SHA256 values. The original source trees remain read-only. Full STRAT15 cover replay is not claimed.

OPEN: packaging and auditing the new split proof; five-double lower-component extension.

PROVED algebra step (lower_formula.py; split_endpoint_certificate.py, replay pending): the increment is concave in the entire lower matrix, with quadratic coefficient -2 tr(E^2)-(tr E)^2/k. Dropping its nonnegative spectral term and using trace <= k-6 reduces every lower collection for nominal seven-vertex split carriers to trace endpoints 0 and k-6. Twelve positive rational polynomial controls give a 3/10 surplus over the k=5 baseline at the latter endpoint. This stronger spectral relaxation covers every lower component family without enumerating its extreme supports.

PROVED partial double-carrier step (double_increment.py, replay pending): gap trace >=1 ensures nonnegative increment, including both inherited equality neighborhoods. OPEN: gap trace <1.

PROVED (double_small_gap.py; double_small_gap_audit.py, full replay pending): gap trace <=1 is now closed by two weighted Cauchy inequalities. The maximal lower-trace endpoint is >=1/270 for every k>=5. Combined with the gap-trace >=1 increment and the STRAT15 isolate theorem, this closes all five-double lower components. No new STRAT15 cover or solver was used. A coarse exploratory moment polytope failed first; its negative relaxed values were not feasible graphs and were not accepted as evidence.

PROVED operational audit: the first replay completed all seventeen inherited stages but stopped on a structural SymPy comparison (expanded polynomial versus factored square). Replaced it by exact zero testing of their difference. All new split and double stages then passed targeted runs; the complete final replay follows after the result ledger is updated.

PROVED setup (split44_setup.py, full replay pending): fixed both four-vertex top vectors, audited separate concavity, and identified the remaining endpoint pairs. OPEN: their complete sign certificates.

PROVED (replay_all.py): 24 stages PASS. NUMERICAL seconds 79.08078454202041, aggregate peak upper bound 109641728 bytes.

PROVED final audit: all 24 replay stages PASS; all 42 proof hashes match current files; all 30 inherited inputs remain byte-identical to their read-only origins. NUMERICAL full replay 79.08078454202041 seconds; conservative aggregate RSS upper bound 109641728 bytes. Both split extensions and the entire five-double lower extension are closed; only the four larger split pairs remain OPEN.
