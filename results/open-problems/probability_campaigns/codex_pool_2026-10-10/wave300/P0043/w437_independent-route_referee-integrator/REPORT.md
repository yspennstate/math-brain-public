# w437 P0043 report — 2026-10-10

Found: Lyons–Peres Conjecture 8.15 includes p_c<1. A 24 September 2026 public preprint states the full bond result as Theorem 1.1. Its separate Lean solution module has a theorem proof body, but I did not verify the import closure, compiler run or trusted axioms. The dated open label is stale as a current-status assertion; the solution is claimed, not independently certified by this packet. The older C0084-A001 speculation about finite critical susceptibility is false on every regular tree of degree at least three; Hutchcroft's cited theorem only applies below p_c.

Changed: saved the independent route before peer proofs, reviewed both peers' auxiliary claims and relations, and staged a two-card, two-relation DRAFT bundle in the math-brain inbox. The tree card is an independently checked boundary example outside quasi-transitivity. The source-status card explicitly withholds parent-proof certification. One hook proposal was submitted. No live store or recall control was edited.

Handoff: w435 and w436 received scoped referee verdicts, and codex-01a12190 received the integration packet path. This packet does not contain response-side served-model evidence; requested model settings were not treated as proof of the served model.

Measurement and validation: `python -X utf8 validate_deliverables.py` passed with 2 entries, 2 relations, 4 claim rows and 13 peer verdicts (11 KEEP, 1 FIX, 1 DROP). It also checked byte equality between the local and submitted draft. These are artifact counts, not a measured retrieval improvement; ingestion and recall are separate pending states in SUBMISSION.json.

Apply: the coordinator should validate and ingest `~/math-brain-inbox/w437/bundle_001.json`, review the two relation rationales, and probe recall. `patches/01_p0043_bundle.diff` records the new draft file with the inbox path in its header; the draft is already submitted, so it need not be reapplied. For w436's separate draft, change E1's relation kind from `refutes` to `proves` before ingestion.

Risk: the public 42-page proof's fresh-collar and nilpotent-quotient steps remain unchecked here. A full P0043 KEEP would be premature. Peer bundles may duplicate the tree or source-status card; deduplicate by logical name and exact statement.

NEXT: Independently audit Proposition 9.2's deterministic contact-shell selection and conditional joint-gluing step under the actual revealed sigma-field.
