---
name: multi5c_notes_pilot_10_of_10_paraphrase_on_7kb_notes_too_easy_2026_11_10
description: "[PROVISIONAL] Does the MULTI5C notes-only pilot show flat notes beat the brain on reworded findings? No: 10/10 paraphrase repairs, but NOTES.md was 7 KB (pilot context, no decoy set), so it only shows the repairs are solvable when the finding is reachable"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T03:03:01+04:00
  status: provisional
  evidence: "codex_fleet/20261108_pro/workers/MULTI5C-FIX/runs/multi5c_notes_codex_11_20/codex/grades.json.summary.json"
  originSessionId: 472b1d4f-77c3-4c94-8b40-709cb36c538f
---

The MULTI5C NOTES pilot (Codex gpt-6.1-sol high, run multi5c_notes_codex_11_20, finished 10 Nov 02:5x) passed 10 of 10 paraphrase repairs after the 2 h gap: valid 10, hidden check passed 10, root cause matched 10, median 31 s, 3 to 8 commands and 3.0 to 7.6 KB of output a task, inside the 8 command / 8,192 byte budget.

It does not show that flat notes beat the brain on reworded findings. The pilot context held only the selected tasks and their prerequisites, so NOTES.md was 7,006 bytes, far too small to hold the 4,000-decoy set: one cat fits in the byte budget. On t11 the agent grepped a guessed synonym list plus the incident date and found the note in its second command. What it does show is that the paraphrase repairs are solvable when the finding is reachable, so a BRAIN arm that fails them on the scored bank fails on reach, not on the repair.

For the scored comparison the NOTES file must carry the full decoy set, and the decoys must not be filterable by a 'd' task prefix or 'rehearsal' wording ([[multi5_decoys_filterable_by_d_prefix_and_rehearsal_wording_2026_11_10]]). Recall on this bank is the gate: [[multi5e_two_note_link_minmax_zeroes_cause_2026_11_10]] has joins at 8/10 offline with a co-touch walk and paraphrases at 0/10. Same lesson as the test-rigor rule that a no-brain arm near the ceiling means the test is too easy.

