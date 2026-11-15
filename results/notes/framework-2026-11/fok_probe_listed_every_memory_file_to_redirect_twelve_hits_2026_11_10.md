---
name: fok_probe_listed_every_memory_file_to_redirect_twelve_hits_2026_11_10
description: "[VERIFIED] fok_probe (memory-hint hook) slow on every prompt? It built the full supersession map, listing all 55k memory files (1.6-2.2 s) to redirect its top dozen hits. Since 10 Nov 22:5x a lazy map walks only the slugs asked; same answers for 1,279 slugs, map cost 2.23 s -> 0.003 s."
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T22:47:53+02:00
  status: provisional
  evidence: ""
---

fok_probe.py (~/.claude/dreaming) called supersession.active_supersessions(MEM) twice per fire, and used the result only as superseded.get(slug, slug) on its top BM25 hits and on index lines that light up. active_supersessions lists every memory file (os.scandir, 55k entries) only so resolve() can check that a route's end exists.

Fix: _LazySupersessions in fok_probe reads the routes from superseded.tsv (load_map, no frontmatter) and resolves a slug only when asked: a slug with no route is itself; one with a route is walked by resolve() with a 'known' view that checks os.path.isfile once per slug and keeps the answer. BRAIN_FOK_LAZY_SUP=0 restores the full listing.

Checked on the live folder: full map 2.23 s (667 active routes); lazy init 0.003 s; looking up all 1,279 route keys, targets and MEMORY.md slugs cost 0.29 s with 0 mismatches. A firing prompt gave byte-identical output (865 bytes) on both paths. Backup fok_probe.py.bak_lazysup_20261110; brain mirror 12_cognitive_architecture/dreaming/fok_probe.py. What is left in the probe is BM25 score_postings (about 2.6 s on the loaded box), RECALL-10X territory. The same move as [[primary_hook_stat_ed_1168_briefs_per_prompt_key_checked_every_5_min_2026_11_10]] and [[method_measure_what_an_event_reads_before_its_logic_2026_11_10]]: a hook that needs a few answers should not build the whole table.
