# P0043 independent adversary review packet

Review requested from w437. Current state: author-proved special cases and independently reproduced original-prover audit; the new results and draft relations await the assigned referee. No full P0043 proof or novelty claim is made.

Exact target: independent Bernoulli bond percolation on an infinite connected locally finite quasi-transitive undirected graph G with p_c(G)<1 has no infinite cluster at p_c(G). SOURCE_STATUS.json distinguishes the historical conjecture, the September 24 primary preprint's full-result claim, and the admitted comparator statement. Current openness is UNKNOWN pending verification of that primary proof. The comparator is not a formal-check receipt.

Independent result C1: the tree with 8 children at generations n that are powers of two and 2 children otherwise has maximum degree 9, p_c=1/2, and critical root survival probability at least 4/5. Its unique degree-8 root forces infinitely many vertex orbits, so it is outside the conjecture's quasi-transitive class. INDEPENDENT_DERIVATION.md was saved before the paired proof was read. The proof uses the fresh-offspring conditional second moment; it differs from the prior regular-tree fixed-point proof and the core lane's critical-window uniform-integrability reduction.

Result C2: the same host has uniform-ray common-edge energy I_(1/2)=5/4. Nevertheless every surviving critical component almost surely has quenched threshold 1 and therefore admits no finite I_r ray measure for any r<1. This is a concrete counterexample to inheriting finite energy from a host graph, with critical survival probability at least 4/5.

Original paired proof audit: AUDIT_w435.md independently reproduces L1-L4 and gives KEEP for those auxiliary results. AUDIT_VERDICTS.jsonl gives FIX for G1: the missing critical-component measure cannot be supplied merely by finite energy on the host. A structural argument using the full quasi-transitive hypotheses is still needed, and recurrent classes require another argument.

Reproduction: python -X utf8 verify_arithmetic.py. MEASUREMENTS.json records 4,095 generations, four exact rational identities per generation, zero failed assertions, and the analytic omitted tail 1/8192. The full reciprocal sum is 1/2, normalized second moment bound 5/4, and critical survival lower bound 4/5. The separate square-burst calculation in w435's proof also checks, including its explicit tail. Arithmetic verification is corroboration of these auxiliary calculations; it is not a proof of the full P0043 statement.

Brain material: drafts/bundle_001.json contains three concept-only entries and three supported relations, including a semantic link to the existing P0043 logical node. EDGE_EVIDENCE.jsonl quotes both endpoints of each relation. Source license is owner-own-work. No unreviewed statement has been promoted to theorem, and the relation to P0043 is not a refutation edge. SUBMISSION_STATE.json will record submission, independent review, integration, and retrievability separately.

The hook is a proposed graph-hypothesis check with one fire case and one silent case. HOOK_PROPOSAL.jsonl and patches/01_critical_graph_hypotheses_hook.diff are staged for the reviewer under the worker's write-scope restriction; no global hook control was changed.

NEXT: Independently check C1 and C2, verify the three relation endpoints, then let the validating coordinator integrate the correctly labeled draft and verify that it is retrievable.
