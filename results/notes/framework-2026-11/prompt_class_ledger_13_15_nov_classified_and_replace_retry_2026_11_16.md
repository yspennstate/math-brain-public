---
name: prompt_class_ledger_13_15_nov_classified_and_replace_retry_2026_11_16
description: "[VERIFIED] Prompt-class ledger was dark 13-16 Nov (0 of ~6,000 rows on 14-15 Nov). Classified with prompt_class_tool (116 unique texts read by hand, the rest mechanical); apply_prompt_classes.py now retries os.replace on WinError 5"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T18:25:59+02:00
  status: provisional
  evidence: ""
---

16 Nov 2026, an agent. hook_liveness flagged the ledger DARK: 11-14 0/1937 and 11-15 0/1751 owner rows. prompt_class_tool heads gave 38/53/25 unique owner texts for 13/14/15 Nov. I wrote verdicts_<day>.txt by the section P boundary rules; agent-written briefs ('the author opened this terminal for you', 'Continue the 10-day loop', worker judge prompts) were marked automation. build added 59 mechanical texts (9,255 rows). After apply: 13, 14 and 15 Nov read N/N and 16 Nov 2012/2238. BUG: the first apply died with PermissionError WinError 5 at os.replace(tmp, LEDGER), because a hook had the ledger open; the second try worked. That alone can leave a day dark with nothing said. The fix retries the replace 40 x 0.25 s and re-runs the tail-race guard on each try; it also no longer copies a half-written last line. Pushed to 12_cognitive_architecture/dreaming. Related: [[the_dream_has_not_committed_since_08_27_and_its_reason_was_swallowed_2026_09_02]].
