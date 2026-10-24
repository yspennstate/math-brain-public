# w375 to w377: P0110 independent route

Review the mathematical proofs in PROVED_LEMMAS.md against the precise scope below. The target itself is not proved; current openness UNKNOWN; no novelty claim. The independent approach was saved in APPROACH_PRECOMMIT.md before any peer proof was read. The statement-only handoff to w376 is queued as msg-9c1207390f.

Files: STATEMENT_FOR_ADVERSARY.md (exact target and a sufficient exponent convention), SOURCE_STATUS.json (primary sources and prior status), ATTEMPT.md (route and remaining gap), PROVED_LEMMAS.md (complete author proofs), CLAIMS.jsonl (per-claim statuses). Draft brain bundles will carry concept kind until review; no live store integration is authorized for this worker.

Review four narrow claims:

1. L1: the n axial high-weight edges and n+2 low-weight detour edges are disjoint, so the positive event probability is an unconditional iid product. T_unrestricted is strictly below T_directed on that event.
2. L2: the one-edge connectors make the block sigma-fields independent; min-cost block choices still concatenate into a simple path; the strong law and bounded leftover tail give the all-n limsup bound. The positive drift gap does not prove a fluctuation exponent. Check also the union-bound extension to arbitrary raw marginal couplings, credited to w376 C008.
3. L3: all coordinate-monotone diagonal competitors are covered, with exactly 2*k^2+k high edges and 2*k+2 low edges. The inequality is k*(b+ell-2*a)>2*a, not merely the axial inequality. This is a finite event only.
4. L4: for essential support endpoints 0<r<R<infinity, equality T_unrestricted=T_directed is guaranteed at n*(R-r)<=2*r, including the boundary with possible ties. At strictly larger scale, endpoint-support neighborhoods give a strict detour event. No atom at an essential endpoint is required.

w376 has reported scoped KEEP for L1-L4 in ~/brain_workers/w376/PEER_AUDIT.md. Record that as a peer receipt; do not mistake it for your designated referee verdict, a two-login admission, or an exponent theorem. Their own inference-obstruction results have not been imported here.

Finite verification is prepared as check_detour_certificates.py: exact Dijkstra, independent monotone dynamic programming, all 400 small two-point edge assignments, four weak-disorder support witnesses, and five disjoint block geometries. The actual first call recorded BLOCKED_BY_FRESH_GATE and started none of those checks. COMPUTE_GATE.json and CERTIFICATE_RESULTS.json are the actual receipts. A resource denial must not be reported as a PASS. The numeric examples below are analytic calculations awaiting the gated run: axial high/low costs 6 versus 4; diagonal interval witness cost 33 versus 30; two-point mean block saving 1/32, giving g(e1)<=191/96<2.

Single hardest missing piece: matching fluctuation/wandering exponent pairs for an explicit full-plane iid lattice law. These proofs close a reduction shortcut and do not close that piece. Any centered or growing-width transfer needs a new quantitative proof.

Return a per-claim KEEP/FIX/DROP with exact scope and gaps. New results you contribute go to w380 under the assignment's independent-referee rule. The validating coordinator decides admission and integration after the required independent review.

NEXT: Audit L4's essential-endpoint/tie argument and L2's independence/all-n extension; rerun the finite certificates only when a fresh gate permits them.

Final received outcome, 2026-10-10: w377 KEEP L1-L4 and w376 C008 within the raw/finite/bounded-law scopes; parent P0110 GAP. Receipt: ~/brain_workers/w377/REVIEW_PACKET.md. Local finite numerical checks were held twice, not passed. The two-entry concept draft is submitted; review is recorded separately from admission, ingestion and retrieval.
