P0104 is not solved. Current global openness is UNKNOWN. I saved an
independent abstract obstruction, then audited the paired conditional proof.
w371 independently kept my rare-event counterexample, conditional variance
bridge and interval correction: review/REFEREE_VERDICTS.jsonl records the
exact decisions. Uniform lattice kurtosis and nondegenerate n^(1/3) weak
scaling remain unproved.

The counterexample has weak n^(1/3) scaling and an exponential tail at
sqrt(n/log n), but variance exponent 3/8. It shows why the larger-scale
concentration theorem cannot replace moment control. The correction is
Var(X)>=epsilon L^2/4 under a uniform closed-interval probability deficit;
it does not restate the cited paper's theorem.

Measurement command:
    python -X utf8 ~/brain_workers/w370/readonly_recall.py
The guarded recall timed out after 60.756 seconds, with 40 blocked
write-lock open attempts across bundles. This is a read-only access
failure, not an unguarded latency benchmark or proof of retry delay.

Runtime check command:
    python -X utf8 ~/brain_workers/w370/test_read_lock.py
Three unchanged gates declined admission at CPU 80.9%, 88.4% and 85.5%
against the 75% cap; RAM cleared the 2 GiB minimum each time. No fixture
tests ran. There is no measured reader-lock improvement or speedup.

The live source changed while this task ran: the saved baseline starts
cc0f2cdf and the observed current source starts f326206c. The exact diff
adds a permission-aware verified snapshot fallback. The worker did not
make that live change. My earlier read-lock proposal is SUPERSEDED.

Apply line: DO NOT APPLY patches/01_readonly_attachment_lock.diff; its
pinned baseline is stale. Keep it as a historical proposal. Validate the
current live fallback separately before making performance or concurrency
claims. See patches/01_STATUS.md and review/LIVE_DRIFT_RECEIPT.json.

Seven claim rows, five typed draft entries and four supported relations
are saved. The three math claims are independently checked; draft nodes
remain concepts. Submission, full bundle review, ingestion and
retrievability remain false. Structural/AST results are recorded in
validation_receipt.json: 50 checks passed using
    python -X utf8 ~/brain_workers/w370/validate_packet.py
These are separate from mathematical and runtime checks. Bundle, hook,
progress rows and peer acknowledgments are staged
inside w370 under the worker-folder restriction.

Review: review/REVIEW_PACKET.md, SOURCE_STATUS.json, CLAIMS.jsonl,
AUDIT_w369.md and INDEPENDENT_BRIDGE.md.

NEXT: Integrate the checked mathematical drafts and validate the current
live fallback. The next proof obligation is to bound the actual FPP Doob
cross and cubic sums relative to Var(T_n)^2 before asserting uniform
kurtosis.
