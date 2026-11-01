# P0104: adversarial typical-fluctuation to variance bridge

2026-10-10, w370. P0104 has not been solved. Current global openness is
UNKNOWN. The exact source scope and fixed specialization are recorded in
SOURCE_STATUS.json.

The fixed target is iid Exp(1) edge weights on undirected nearest-neighbor
Z^2, with T_n the infimum of path-weight sums from 0 to ne_1, and
lim_n log Var(T_n)/(2 log n)=1/3. ADH Question 13 leaves its suitable
distributional conditions unspecified; Section 3.1 also distinguishes
several possible meanings of variance asymptotics. This target fixes the
exponent-only meaning and does not assert a positive limiting constant.

Before opening the paired proof I saved INDEPENDENT_OBSTRUCTION.md and
INDEPENDENT_BRIDGE.md. The first n/log n versus polynomial calculation
was already present in the September attempt card, so it contributes no
novelty. The second file gives a separate conditional proof and an exact
rare-event sequence with weak n^(1/3) scaling, the known-form exponential
tail bound at sqrt(n/log n), and variance exponent 3/8.

The full paired proof is audited directly in AUDIT_w369.md. Verdict: KEEP
the conditional abstract statements L0-L4. The arbitrary deterministic
centering step, width infimum, constants, independent-copy construction,
tail endpoints, and moment-limit passage withstand the audit. My
symmetrization derivation is independent of the prover's width argument.
Referee w371 still must check new results. No cross-account admission is
certified by this worker.

The math brain returned a useful conditional-KPZ warning and the old
logarithmic barrier. It also returned card
claim_3ccc6fc493b4e17b5c29966949004f575c51205c8a4f0ba3bc516d0b752ebea4,
whose explanation categorically denies that anti-concentration can
lower-bound variance. For square-integrable X, if every closed interval
of length L>0 has mass <=1-epsilon, applying that condition at EX gives
Var(X)>=epsilon L^2/4. The logical explanation needs correction. The
actual cited paper theorem has not been restated or changed here.

The single hardest attempted bridge is uniform standardized fourth
moments for actual lattice T_n. Nondegenerate weak n^(1/3) scaling is
also independently missing. DHS Theorem 1.1 applies to Exp(1) and gives
P(|T_n-ET_n|>=t s_n)<=c1 exp(-c2 t), s_n=sqrt(n/log n).
Tail integration yields only

    E|T_n-ET_n|^4 <= (24 c1/c2^4) s_n^4.

Indeed integrate 4u^3 P(|T_n-ET_n|>u) over u>=0 and substitute u=s_n t.
Dividing by Var(T_n)^2 leaves the unknown ratio
(n/log n)^2 / Var(T_n)^2. This is not a uniform kurtosis estimate; even
the hypothesized Var(T_n)~n^(2/3) would leave a diverging upper bound.
The 3/8 countermodel proves that the larger-scale tail data alone cannot
close this gap. Rotationally invariant Riemannian concentration at the
actual standard deviation has different model assumptions; no lattice
transfer is available in this packet.

Brain access produced a separately measured failure: guarded read-only
recall timed out after 60.756 seconds and recorded 40 attempted opens of
the live attachment write lock. Those attempts were across bundles;
the observation does not attribute the entire latency to a retry loop.
The bounded repair changes only the copied attachment reader to open
the stable lock sidecar read-only while retaining writer exclusion and
all document integrity checks. Its patch and fixture checks are local.
Read-only stores were never modified, and draft submission is staged.

All new math entries remain concept/draft material. No Lean or other
formal prover was run; file hashes and source matches are provenance
checks, not mathematical proofs.

NEXT: Independently check the rare-event and interval-variance claims;
for a new proof step, expand the actual lattice fourth centered moment
through Doob differences and isolate quadratic-variation terms requiring
control relative to Var(T_n)^2, without assuming independence of geodesic
blocks or multiplying conditional probability bounds.

2026-10-10 resume: w371 independently returned KEEP for claims 002, 003 and 005; exact receipts are in review/REFEREE_VERDICTS.jsonl. This discharges those mathematical referee requests only. The third unchanged compute gate declined runtime checks at CPU 85.5%; the code remains an unvalidated proposal.

NEXT: Bound the actual FPP Doob martingale cross and cubic sums relative to Var(T_n)^2 before asserting uniform kurtosis; the reviewed conditional bridge does not provide these bounds.

2026-10-10 resume: The live source changed from the copied baseline and now has a permission-aware snapshot fallback. The historical read-lock diff is SUPERSEDED and must not be applied; live_drift.diff records the exact change. No end-to-end improvement was measured.

NEXT: Bound the actual FPP Doob martingale cross and cubic sums relative to Var(T_n)^2 before asserting uniform kurtosis.
