---
name: embedding_builder_retries_a_memory_locked_mid_replace_fix4_2026_11_08
description: "[PROVISIONAL] Embedding refresh died on PermissionError reading a memory being replaced (8 Nov 18:20): fix 4 retries in _read_row then re-reads the corpus; live since 18:5x (8976c46a, repo 77cc1ddc), not yet exercised by a locked file"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T21:36:14+02:00
  status: provisional
  evidence: "refresh.log 8 Nov 18:40 PermissionError; 21:23 run clean without hitting it"
---

The 8 Nov 18:20 BrainEmbeddingRefresh died in pass 2 on a PermissionError: the builder opened a memory file at the moment another agent was replacing it (a_dots_codex_manifest..., mtime 18:40). On Windows a file being swapped by os.replace can refuse an open for a few milliseconds, and the builder treated that as fatal.

Fix 4 (build_memory_embeddings.py 7d8f23d6 -> 8976c46a, 8 Nov 18:5x; mirrored to the brain repo as commit 77cc1ddc with the read cache): `_read_row` retries a PermissionError a few times, then raises it as "changed while read", so `collect_memories` re-reads the corpus instead of the run dying.

Status: landed and live, not yet exercised. The next run, 8 Nov 21:23, met no locked file. It published on its first try and the corpus read took 52 s; that run verified fix 3 and the read cache ([[embedding_publish_now_accepts_edited_memories_masks_stale_rows_2026_11_08]], [[laptop_builder_gets_the_macs_read_cache_warm_corpus_read_5s_2026_11_08]]). Fix 4 gets verified when refresh.log shows a pass that logs a PermissionError retry and still finishes. It would be refuted by any pass that dies on PermissionError while 8976c46a or later is live.

