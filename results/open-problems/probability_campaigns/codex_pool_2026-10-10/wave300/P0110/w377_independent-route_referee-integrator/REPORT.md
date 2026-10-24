# P0110 referee report — 2026-10-10

Found: The primary Question 22 asks for an iid ordinary FPP law with a proved KPZ exponent relation. Chatterjee and Auffinger–Damron prove conditional exponent relations; neither supplies strong exponent existence for a concrete law. The local ranking's `attempted_un` is historical. Bounded checks leave current openness UNKNOWN.

Changed: Saved independent KEEP verdicts for w375 L1–L4 and w376 C001–C003/C005/C008, with exact statements and limits in `CLAIMS.jsonl` and `REVIEW_PACKET.md`. The harder w375 L2 block claim was rederived through edge-disjoint blocks, iid block costs and the strong law. Submitted a four-lemma, four-relation draft bundle at `~/math-brain-inbox/w377/bundle_001.json`. These lemmas close exact directed-reduction shortcuts; none solves P0110. Filed one narrow hook proposal for the missing exponent-existence gate.

Measurements and reproduction: `python -X utf8 review_repro.py` checked all 256 assignments to the three-edge axis and five-edge detour for iid {1,2}: exactly one positive saving, delta=1/256, proven raw axial gap at least 1/1024. It enumerated all 20 directed paths to (3,3): minimum cost 9 versus exterior detour cost 8 on the constructed event. It checked the L4 {1,2} threshold n=2 versus n=3 and C002 exponent gaps 1/12, 1/24. JSON validation found four entries and four allowed relations. Local and inbox bundle SHA256 match: 484cfe02cd43e97157610da136d09f6e97ef8872574d88f989829d0c7fee1583. A read-only store query found zero of the four submitted titles, so no ingestion or retrieval improvement is claimed yet.

Risk: The w375 bundle already contains related **concept** drafts on L2/L3; the new formal lemma entries should replace or deduplicate those concepts before ingestion. The two auditors' separate accounts were not verified. A source quantifier caution remains: Chatterjee's lower exponents allow a radius cutoff, while the literal Auffinger–Damron (2.2) does not. Do not apply their conditional theorem after silently changing that premise.

Apply: The validating coordinator should review `~/math-brain-inbox/w377/bundle_001.json`, deduplicate it against w375's concepts, verify audit-account independence and relation targets, then use the normal integration pipeline and measure retrieval. No live store file was edited by w377.

NEXT: Audit a variance/width stabilization estimate for a concrete iid law; this is the one missing proof step that would make the conditional KPZ theorem useful for P0110.
