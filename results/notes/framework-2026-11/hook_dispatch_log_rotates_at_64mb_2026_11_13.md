---
name: hook_dispatch_log_rotates_at_64mb_2026_11_13
description: "hook_dispatch.log was 415 MB, never rotated: since 13 Nov it rotates at 64 MB to hook_dispatch.<stamp>.<pid>.log (AI output: GitHub, then delete)"
metadata:
  type: project
  created: 2026-11-13
  created_at: 2026-11-13T20:04:09+02:00
  status: verified
  evidence: "hook_dispatch_land.py run 13 Nov 19:57 (635944514a0b2b2d -> 8fff29e143feb25b, clean); new hook_dispatch.log 964 bytes with clean dispatches; rotated file 415,686,932 bytes; brain repo commit dde08131"
---

The dispatcher log ~/.claude/compute/hook_dispatch.log was never rotated. On 13 Nov 2026 it was 415 MB, with lines going back to 15 Sep, and was growing about 5 MB a day. an agent found it in the log tail.

Fix (13 Nov 2026, an agent). The live dispatcher sha256 went from 635944514a0b2b2d to 8fff29e143feb25b, landed with hook_dispatch_land.py --resign touch, so the fast list did not go stale. Before each append, log() checks the file size. Past 64 MB it renames the file to hook_dispatch.<YYYYmmddTHHMMSS>.<pid>.log and starts a new one. If the rename fails because another writer has the file open, it is tried again at the next line. Readers (hook_liveness, the deadman, math_sense) seek to the end of hook_dispatch.log, so they see only the part written since the last rotation.

The first rotation ran at landing and produced hook_dispatch.20261113T195740.59476.log (415,686,932 bytes). Rotated files are AI outputs: they go to GitHub, are checked there, then are deleted. Never delete one here without that check.

If you need the dispatcher's history before a date, look in the rotated files or their GitHub copies, not in hook_dispatch.log.

Related: [[owner_order_ai_outputs_to_github_then_delete_2026_11_09]], [[hook_dispatch_land]].

