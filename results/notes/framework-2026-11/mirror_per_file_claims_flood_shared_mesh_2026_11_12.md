---
name: mirror_per_file_claims_flood_shared_mesh_2026_11_12
description: "Memory mirror per file claim assert loop creates hundreds of mesh transactions"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T14:45:01+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: On 2026-11-12 the old mirror needed 120 mesh calls for 60 files and about 300 write transactions for a 150-file run. Batches of 25 cut 60 files to 6 calls; with one peer conflict they used 54 versus 119. All 16 throwaway-mesh checks agreed on claims, file order and copied bytes.

Why it happened: Each file got its own claim and assert, while the final bye released about 150 claims in one transaction. The fix batches claim/assert calls, falls back per file when a batch conflicts and releases in chunks. Its next live run was still unobserved.

**Why:** Per-file coordination multiplied writes on a shared database without changing the useful claims.

**How to apply:** Preserve 25-file batches, per-file refusal semantics and release chunks; inspect the next live mirror log and mesh_slow.log before calling the live gain proven.

[[memory_mirror_claims_in_batches_six_mesh_calls_for_sixty_files_2026_11_12]]

Drafted by Codex worker W02 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

