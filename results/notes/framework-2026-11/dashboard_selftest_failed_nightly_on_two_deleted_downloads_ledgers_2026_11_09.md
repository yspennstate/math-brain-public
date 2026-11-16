---
name: dashboard_selftest_failed_nightly_on_two_deleted_downloads_ledgers_2026_11_09
description: "[VERIFIED] Dream 'brain_improvement dashboard selftest' STEP FAILED every night since 1 Nov: STATUS.json/DASHBOARD.json name two Downloads prompt ledgers (BRAIN_MATH_BRAIN_PROMPT_LEDGER_200.md, _V2.md) that are gone; now a record with exists:false warns instead of failing (a96da607, fcd4b03b, 8521809f)"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T00:04:18+02:00
  status: provisional
  evidence: ""
---

The dream's dashboard selftest (brain_improvement/dashboard_selftest.py) walks every path string in STATUS.json, DASHBOARD.json and CURRENT_CAMPAIGN.json and fails if one is missing. Since at least the 1 Nov dream it failed every run on two files from the 18 Aug campaign: ~/Downloads/BRAIN_MATH_BRAIN_PROMPT_LEDGER_200.md (sha256 d8c9c544..., 179,131 bytes) and _V2.md (sha256 0173eadc..., 194,759 bytes). They are not in Downloads and not in the brain repo's git tree; a find across the home folder timed out under disk contention, so a copy elsewhere is not ruled out. The sha256 in the records identifies one if it turns up.

Fix on 9 Nov 00:0x (an agent, task rank 3): the four records now say exists:false with absent_as_of and absent_note; walk_paths treats a record whose own exists is false as a stated absence and reports it as a warning ('sources recorded as absent'), and warns 'present again' if the file comes back. Any other missing path still fails. Control: a fixture with one stated-absent record, one live record and one bare string splits as expected. Selftest now: OK, 6 checks, 1 warning, 0 failures. Pushed by the API to main: dashboard_selftest.py a96da607, STATUS.json fcd4b03b (CRLF kept), DASHBOARD.json 8521809f (GitHub's copy was the 24 Sep refresh; this is tonight's). DASHBOARD.md unchanged (render_markdown does not show those records).

Why it mattered: a step that fails every night trains everyone to read STEP FAILED as noise, and the dream log's real failures hide among it. When a source is deliberately or accidentally gone, record the absence in the data rather than leaving a check to fail forever.

Same class as [[a_red_that_is_always_red_stops_being_read]] and [[prompt_archive_verify_by_line_hashes_not_a_second_copy_2026_11_08]] (tonight's other dream-step fix).
