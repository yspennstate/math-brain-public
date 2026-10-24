# Dependency certificate contract

`PROOF_DEPENDENCIES.json` is a frozen, content-addressed proof interface, not another mutable campaign registry. It covers every entry in the registry snapshot and a selected set of source-complete baseline interfaces. A001's full 37-route map is separately pinned as navigation; its pending audit is not accepted by this artifact.

The protocol's displayed progress-field label `packet_ids (one primary ID, for compatibility)` is serialized as `packet_ids`, following the user's explicit compatibility requirement. All other protocol progress and claim fields are literal keys, without extra bookkeeping fields. PowerShell-redirection outputs were decoded from UTF-16 and saved as UTF-8 JSON before final validation.

Each node has an exact `claim_id@version`, its literal statement and hypotheses, the protocol statement hash, explicit units, evidence state, source and theorem locator, proof dependencies, and the first unpaid line. Each proof edge names both the exact dependency version and its statement hash and includes the hypothesis instantiation. Unit changes require an explicit conversion. The protocol statement hash intentionally covers only statement and hypotheses; the complete JSON file hash also pins units, status, edges, and evidence.

`IMPORTED_ACCEPTED` preserves the independently reviewed B05 no-go and three explicit subclaims reconstructed by that review. `IMPORTED_CERTIFIED` preserves the repaired fixed B09 counterexample and its exact-mass and rational-sign subclaims. These seven nodes are the admitted subgraph. Subclaim acceptance is inherited at the narrow scope of the original accepting report; this run does not add independent acceptance of new theorem scope.

`SOURCE_COMPLETE_BASELINE_NOT_NEW_ACCEPTANCE` denotes inspected manuscript interfaces awaiting whatever source reconstruction or acceptance their downstream use requires. `PENDING_REVIEW` is the original B09 uncertainty lemma. `UNRESOLVED_SOURCE` is its unpinned Maassen-Uffink premise. `OPEN` denotes a mathematical obligation. These states cannot enter an admitted proof closure. Distinguish an outstanding acceptance record from an unproved mathematical inequality.

Proof edges point from a conclusion to premises. Candidate routes are separate AND lists, and the routes are alternatives. They are not added as unconditional edges proving FEI. An implication `P => FEI` is a lemma with P bound as a local assumption; applying it requires a separate proof of P. The converse `FEI => P` does not provide that proof. Workflow and reviewer edges are ignored by proof-cycle checks.

The verifier rejects duplicate versions, literal statement-hash drift, missing exact dependency versions, mismatched dependency hashes, missing sources/locators, source-byte drift, missing hypotheses/units/evidence, unexplained unit changes, all proof cycles, admitted claims with unadmitted dependencies, and candidate routes that directly or transitively assume their conclusion. It emits a dependency-first ordering and the unadmitted closure of each claim. All five current routes remain conditional.

DFS gives a cycle witness whenever an edge encounters a node on the active stack. If no such edge occurs, finishing a node after all dependencies yields a dependency-first order. For an admitted root, induction through that order establishes that every reachable node is admitted, provided the individual leaf proofs and edge inferences are valid. The code verifies the graph structure and evidence fields. It does not verify the mathematical truth of source statements, logical entailment of hypothesis text, or correctness of a supplied unit-conversion sentence. Those obligations belong to independent reconstruction. A malformed or oversized input that cannot be processed has no passing certificate.

Local raw-byte SHA256 values are checked against the files actually read. Provenance metadata is separate. The source audit also checks LF-normalized hashes and Git blob hashes using Python hashing, without invoking git. A CRLF-normalized copy can match an immutable remote blob while its raw hash differs. Curated excerpts match their packaged hash, not necessarily the complete original blob. The archived threshold source fails equality with the related public-release source hash and is pinned as its own local snapshot; no public-release identity is asserted.

Run from A081:

```text
python -X utf8 runs/20261011T214745Z-account05-A081-dependency-certificates/code/dependency_check.py runs/20261011T214745Z-account05-A081-dependency-certificates/PROOF_DEPENDENCIES.json
python -X utf8 runs/20261011T214745Z-account05-A081-dependency-certificates/code/test_certificate.py
python -X utf8 runs/20261011T214745Z-account05-A081-dependency-certificates/code/test_certificate.py --fixtures-only
python -X utf8 runs/20261011T214745Z-account05-A081-dependency-certificates/code/independent_interval.py
```

The full graph test exhausts 66,067 labeled directed graphs with loops, dimensions 0 through 4, without symmetry reduction. Independent Kahn elimination agrees with DFS on each graph. A passing finite graph test is not an all-dimensional FEI proof. The interval test is one specified two-bit Boolean counterexample, not a search over functions or biases.

Review request: A090 should reconstruct the B05 source edges and the two-bit interval derivation, then inspect status and assumption boundaries. A094 is the alternate reviewer. The B09 theorem requires a primary-source pin and exact version for Maassen-Uffink before it can be adopted. No acceptance, shared-index update, mirror receipt, or downstream mathematical use is inferred from a local save.
