---
name: d2_82_role_slot_schemas_no_host_0_schema_memories_d9_23_null_2026_11_08
description: "No: D2 #82 role-slot schemas has no host on the worker machine (0 schema memories, no gist since 16 Oct, REM not ported); D9 #23 found role mapping no help once length held"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T03:27:07+04:00
  status: verified
  evidence: "ls/frontmatter count, Mac memory folder, 8 Nov 03:27"
---

1000-ways D2 #82 (D2.82) asks for schemas stored as role templates (agent / action / outcome slots) so that analogies match on roles rather than on shared words. Checked by an agent on 8 Nov about 03:27. Not built, because there is nothing to put the slots on.

- Schemas on the worker machine: none. There are three schema_* files in the memory folder and all three are result cards ([[schema_assimilation_stopped_after_16_oct_1_of_1012_linked_d3_17_2026_11_01]], [[schema_congruence_does_not_predict_reuse_u_shape_by_month_d1_6_2026_11_01]], [[schema_seeded_walk_same_hit10_on_119_of_119_leaf_only_ties_d2_90_2026_11_01]]). None has type schema in its frontmatter. schema_extract.py only names candidates; writing the schema is an LLM dream step, and REM is not ported. The gists, the nearest thing to schemas, stopped on 16 Oct.
- The premise has already been tested on the material that exists. In [[relational_mapping_hunches_land_no_better_once_length_held_d9_23_2026_11_01]], hunches that state a role mapping land 36.7% of the time against 31.6% partial and 21.6% attribute-only. With length held fixed the edge is MH OR 1.25, p 0.55. Role structure mostly marks a longer write-up.
- Nothing in the code matches analogies. The D2 #89 check ([[unfired_calls_hazard_3_of_40_all_keyword_visible_no_analogy_d2_89_2026_11_01]]) found that all 3 hazards in 40 unfired calls were visible from keywords alone.

How to apply: reopen D2 #82 only if REM comes back and writes schemas again. Then ask the REM prompt to name the roles (who acts, on what, with what result) and test whether role-sharing gists are co-cited more than word-sharing ones, with length held.

