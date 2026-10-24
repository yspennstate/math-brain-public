# Review packet for w368 and claude-4a88bc43

The concrete result is the sharp support threshold n(b-a)<=2a, its exact
continuous-uniform variance window, and a necessary prefactor/onset
tradeoff for normalized polynomial variance bounds. Source, full proofs,
counterexamples and measurements are saved. The parent P0104 is unresolved.

Review C001/C002 in INDEPENDENT_OBSTRUCTION.md, then C003 in ATTEMPT.md.
In particular check parity, the equality case, essential support endpoints,
independence of the prescribed detour event, positivity when dividing by
edge variance, and the distinction between a changing law and a fixed law.
The exact check is verify_boundaries.py with receipt VERIFICATION.json.
It uses a finite rectangle only for diagnostics and counterexample witnesses;
the theorem about the full lattice has a separate deterministic proof.

AUDIT_W366_C1.md checks the fixed-endpoint moment argument. PEER_VERDICTS.jsonl
also records KEEP on w366-C2/C3/C4 with the scope attached. My independent
boundary artifact existed before I inspected the peer's later C3/C4. If
the peer submits the same cards, merge these proofs as supporting evidence
instead of ingesting duplicate nodes.

draft_bundle_001.json follows BUNDLE_SPEC.md. It contains three concept
entries visibly marked DRAFT/UNREVIEWED, owner-own-work sources, two
acyclic internal dependencies, and one association to the exact live P0104
concept. No theorem promotion is authorized by this worker's own claim.
The individual statements and source evidence are reviewable without a
live-store mutation. Lifecycle flags are in BRAIN_DELIVERY.json.

All files stay under the assigned worker folder. The unified diff in
patches/01_fpp_boundary_bundle.diff names the intended inbox file. After
independent review, deploy the approved draft to that location; the validating
coordinator handles ingestion. The hook in hooks/math-w367.jsonl is a
proposal with a concrete fire/silent pair and exact evidence.

TEAM_HANDOFF.md and PROGRESS_EVENTS.jsonl contain locally staged claim,
completion and progress lines. A later team instruction authorized a direct
handoff to w366; TEAM_REPLY.json records its successful transport. Progress
posting and draft deployment remain staged under the worker write restriction.
The earlier read-only mesh snapshot found no pending messages for w367.

Nothing is marked ingested or retrievable. No recall improvement is claimed
before integration and a fresh read-only retrieval check.

NEXT: independently audit C001-C003 and admit only their checked scope.
