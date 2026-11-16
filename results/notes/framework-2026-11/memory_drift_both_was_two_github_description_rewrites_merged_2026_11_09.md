---
name: memory_drift_both_was_two_github_description_rewrites_merged_2026_11_09
description: "[VERIFIED] Laptop vs GitHub memory drift 'both' class (4,296 files, 9 Nov): 61% differed only in the description line - GitHub-side rewrites (Mac commit ad281ad5ba 8 Nov 'Mac memories (auto)' question leads; aeb13077ca 30 Oct data-node subject leads). Date-free three-way rule (take GitHub's description only when it contains the local one) merged 3,007 files: both 4,296 -> 1,288, same 2,416, workstation-ahead 592"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T01:03:45+02:00
  status: provisional
  evidence: ""
---

Recall loop, an agent, 9 Nov 00:5x. classify_full --write (dev/drift/classify_full.py, resumable blob cache) wrote all 27 origin_ahead and classified head ecb14: both 4296, live_ahead 717, origin_ahead 27, same_lines 10, noblob 1. Splitting 'both' by what differs (dev/drift/both_kinds.py): description only 2497, local body + description 597, link spelling only 132 (GitHub carries the dated slug that resolves; local the short one that does not), the rest mixed. The GitHub descriptions came from two whole-folder rewrites that never reached the workstation, because the pull only takes files where GitHub holds every local line.

Rule (dev/drift/desc_contain.py): for files whose GitHub-only lines are description, link respellings or upload stamps, take GitHub's description only when it CONTAINS the local description text (a lead was prepended to the unchanged ancestor); otherwise keep local's (348 kept, among them data nodes regenerated here with newer counts after 30 Oct). Respell a dead local link to GitHub's resolving spelling. Body and stamps stay local. 3,007 written, each backed up in recall_xc_1d48/dev/drift/merge_bak/ (restore = copy back).

Do not use per-file commit dates for this: a 40-path aliased GraphQL history query returns http 502, and 10 a query ran about 10 files a minute (hours for 3,300). Containment is exact and needs no network.

After (dev/drift/reclass_local.py against the cached GitHub bodies): both 1,288, same 2,416, live_ahead 592 - the workstation's push takes the 592 the rest of the way. Open: the 1,288 with body lines on both sides need a line-union merge (next), and a daily run of this rule so the next whole-folder rewrite on one computer does not strand thousands of files again. Related: [[memory_drift_is_two_way_push_laptop_ahead_only_2026_11_08]] [[plain_question_description_reorders_found_notes_rescues_no_miss_2026_11_08]] [[recall4_randomized_question_lead_desc_top1_6_to_10_hold_flat_p0p11_2026_11_08]]
