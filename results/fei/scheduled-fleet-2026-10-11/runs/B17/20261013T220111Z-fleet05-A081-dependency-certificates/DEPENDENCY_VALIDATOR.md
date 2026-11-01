# Stage-3 certificate use

Run code/dependency_check.py against PROOF_DEPENDENCIES.json to verify exact internal statement hashes, hypotheses, units, source snapshot byte hashes, dependency hashes, unresolved closures and cycles. This checker automates structure, not analytic proof validity; REVIEW.md supplies the independent mathematical reconstructions.

Internal hashes use canonical JSON with keys statement and hypotheses. Source-only hashes and source JSON using exact_statement are explicitly typed aliases in out/HASH_RECEIPTS.json. They identify identical pinned literal content, but cannot replace an internal edge's canonical hash. Source version changes require a new exact node, never silent statement edits.

Admitted means the specific imported or independently reconstructed node is usable within this certificate; it does not assert central-registry adoption or independent acceptance of this entire graph. In particular, a conditional theorem may be admitted while its universal antecedent is still an OPEN leaf. Every route to FEI has a separate unpaid obligation.

Source author dependencies are preserved verbatim in source_declared_dependencies. Accepted edges encode the actual A081 reconstruction, which may independently derive a source interface rather than assume its older author dependencies. A compound claim whose full author chain was not reconstructed stays pending and remains an unresolved leaf; an accepted narrower clause never upgrades the rest of that statement.

New universal routes are compatible tree payment (C019/C024), fixed higher-tail payment (C018), and low-influence aggregate payment (C018). The tree premise jointly quantifies one tree and one fixed terminal reference system, so separate existential bounds cannot be combined using different witnesses. Terminal CE, mass normalizers, and one-use physical influence are mandatory. Aggregate parity-tail hardness does not transfer a selected coordinate: the fresh physical parity bits have zero erasure and positive influence.

The latest A064 marker is an availability receipt, not a proof. A100's B05 review is partial. A083's finite rational Lean scope excludes the real endpoint. A085's generic helper contract repair remains a pending mathematical import and does not invalidate the surviving finite certificate domain. Final certificate review is assigned locally to A094/A085; no review message has been sent.
