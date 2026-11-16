---
name: related_md_builder_killed_at_cap_now_a_sparse_product_2026_11_08
description: "[VERIFIED] RELATED.md stale / dream build_brain_architecture killed at 2400 s: related() was 0.3 s a memory (5 h for 56k). Now a scipy sparse product, 307 s, identical top-6 on 1850 sampled memories"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T00:11:55+02:00
  status: verified
  evidence: "bba_related_np_2026_11_08 (cmp300.out, cmpnp300.out, cmpnp1500.out, fullnp.out, smoke_installed.out); build_brain_architecture.py 550bf900b1de0acb"
---

Why was RELATED.md stale, and the dream's build_brain_architecture step killed at its 2400 s cap every night (6 Nov 10:36, 6 Nov 22:55, 7 Nov 20:18)? Its related() scored one memory at a time in Python: for each of the memory's distinctive terms it rebuilt the set of current names of every memory carrying that term (terms run up to 12 pct of the corpus, about 6,800 memories), then took a set union per candidate. Measured 7 Nov on the loaded machine: 0.26-0.33 s a memory, so 4-5 hours for 56,613 memories. The other views are written in about 3 minutes; only RELATED never finished, and it had not been rebuilt since 7 Nov 04:36. Measured 7-8 Nov 2026 by an agent rank 3.

Fix (landed 8 Nov 00:0x, manifests/build_tools/build_brain_architecture.py sha256 550bf900b1de0acb, backup .bak_pre_np_20261108 = 015b72ef):
- The same scores as a sparse product, 256 memories at a time (scipy): shared terms = A.B^T, where A is memory x term and B maps each term's members to their current (unsuperseded) names; the union's intersection = A.A^T. The COACT Hebbian bonus, the UNCONSCIOUS 0.25 factor and self-exclusion are applied per row exactly as before, and the top 6 are taken by heapq over every candidate at or above the 6th score, so ties break the same way.
- A pure-Python fast path (term sets mapped to current names once, Counter.update, heapq) is the fallback when scipy is missing; about 3x.
- BBA_RELATED=old brings the original function back, BBA_RELATED=py skips scipy, BBA_OUT writes the views elsewhere, BBA_CMP=N (with BBA_SEED) runs old against new on N sampled memories and exits.
- The dream runs it with plain python (user site on), where numpy and scipy are installed; under python -s they are not, and the fallback runs.

Before/after (evidence in bba_related_np_2026_11_08):
- Parity, top-6 lists compared as (score, shared, name) tuples: 300 of 300 identical (seed 7389; old 78.9 s, new 6.5 s) and 1,500 of 1,500 identical (seed 1108; old 317.5 s, new 9.8 s). The pure-Python path: 300 of 300 identical, 99.7 s against 33.0 s.
- Full build to a scratch folder: rc 0 in 486 s wall (164 s before RELATED, RELATED itself 307 s), 55,611 of 56,613 memories wired, RELATED.md 52 MB. Before: killed at 2400 s with RELATED not written.

Status: verified on the live corpus. What would change it: a change to the scoring in related() that is not mirrored in _related_batch (run BBA_CMP=300 after any edit to either); scipy disappearing from the user site (the fallback would take about 6,200 s, over the cap again); the corpus growing several-fold (the dense 256 x N blocks grow with N).

Related: [[heed_audit_read_33gb_of_transcripts_now_seeks_to_the_window_2026_11_07]], [[overlay_loaded_620k_df_map_per_sidecar_generation_per_word_view_2026_11_07]].

