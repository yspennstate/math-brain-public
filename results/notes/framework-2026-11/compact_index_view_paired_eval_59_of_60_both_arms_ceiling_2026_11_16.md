---
name: compact_index_view_paired_eval_59_of_60_both_arms_ceiling_2026_11_16
description: "Does the compact memory-index view (link destinations dropped, -33% bytes) make agents pick the wrong memory? No loss seen: 59/60 top-1 in all four arms, zero disagreement - but the bank is at ceiling, so it shows no harm, not a gain"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T14:37:38+02:00
  status: verified
  evidence: "a second machine ~/idxeval_3708/score.py on picks of IDXA1/A2 (canonical) and IDXB1/B2 (compact), bank sha 987e1cca, key 0402cf95; PASS against the bar fixed before picks existed"
---

Paired test of index_text.py's compact view (S38M06, landed dormant) against the canonical MEMORY.md view, 16 Nov.

Setup: frozen live index (104 rows; compact restores byte for byte, sha cd5ee679). A Codex builder (IDXQ01) wrote 60 questions from the memory BODIES, no four-word overlap with any index line, 41 with a nearby decoy; key kept on a second machine only. Four fresh Codex readers saw only the index text and the questions: IDXA1/IDXA2 canonical (forward / reversed order), IDXB1/IDXB2 compact. Logs checked: no reader opened anything outside its arm folder.

Result: top-1 59/60 in every arm, top-2 60/60 in three and 59/60 in one; pairwise top-1 disagreement 0 everywhere (A1-A2, B1-B2 and all cross pairs). Pass bar (compact >= canonical - 2 and cross disagreement <= A1-A2 + 3) passes.

Caveat that matters: the bank is at ceiling, so it cannot separate the views; it rules out a large loss, nothing finer. Each reader took 47-76 s.

What it allows: the compact view may be used where index text is pasted into a prompt (a hook or brief), cutting about a third of the bytes. It does NOT license rewriting the live MEMORY.md (dream-owned; other tools parse its links). Next: a harder bank (the 1,000-row full index, or decoy-only questions) before relying on it at scale. Related: [[s38m06_compact_index_view_landed_dormant_2026_11_16]]
