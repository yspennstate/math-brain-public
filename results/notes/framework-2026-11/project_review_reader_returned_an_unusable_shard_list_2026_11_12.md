---
name: project_review_reader_returned_an_unusable_shard_list_2026_11_12
description: "project_memory_cli read-latest huge shard command list newest prompts digest acknowledgement"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T15:13:04+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: Reviews ranged from 4 MB/83 shards to 26.8 MB/559 shards among the 16 largest. read-latest could return 110,000 characters of shard commands, each leading to another roughly 48,000 characters. The live store had 31 acknowledgements since 22 July and only 1 since 1 October. The new digest passed 16/16 tests while an old-against-old control failed 7; one live answer shrank from 24,654 to 3,905 characters. Low acknowledgement counts measure recorded uptake, not proof that no human ever read anything.

Why it happened: The command behind an hourly reminder exposed a complete transport manifest before giving an agent a usable entry into the content. Shards were byte slices, so independent decoding also risked cutting a long prompt's UTF-8 bytes.

**Why:** Delivering a reminder and a huge list of follow-up commands does not establish that its content is consumed.

**How to apply:** For reviews of at least 3 shards show the newest 12 prompts, each bounded to 600 characters with its full length named, within 8,000 characters; preserve historical-context warnings, hash checks, byte joining, full-list escape paths, fallback on error, and the unchanged all-shards acknowledgement rule.

[[project_review_reader_opens_with_newest_prompts_2026_11_12]]
[[project_review_due_lines_share_one_line_per_call_2026_11_12]]

Drafted by Codex worker W05 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

