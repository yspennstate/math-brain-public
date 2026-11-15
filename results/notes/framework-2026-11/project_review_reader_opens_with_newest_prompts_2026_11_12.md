---
name: project_review_reader_opens_with_newest_prompts_2026_11_12
description: "Hourly 'project reviews are due' notice: is the review ever read? No: 31 acknowledgements since July, 1 since 1 Oct; a review is 4-27 MB and read-latest printed one command per shard (up to 110,000 chars). Since 12 Nov read-latest answers a long review with its newest 12 prompts inside 8,000 chars; --full and read-offer keep the list; acknowledging is unchanged"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T02:20:48+02:00
  status: verified
  evidence: "agent_run/project_context/test_digest_result.txt (16 of 16, control fails 7), review_counts.txt, review_digest_live_sizes.txt; ledger row of 12 Nov (k)"
---

The hot hook tells every session each hour that project reviews are due and to run `project_memory_cli.py read-latest --project <name> --session <id>` ([[project_review_due_lines_share_one_line_per_call_2026_11_12]]). Until 12 Nov 2026 that command answered with one command line per shard of the review. A review is the project's last 1,000 owner prompts quoted in full: on 12 Nov the sixteen largest ran from 4 MB (83 shards) to 26.8 MB (559 shards), so the answer itself was up to 110,000 characters and each shard behind it 48,000 more.

Nobody reads them. Counted read-only on the live store (`agent_run/project_context/review_counts.txt`): 31 acknowledgements since 22 July, one of them since 1 October; 15 shard reads since 1 November; 269 offers ever taken up. The notice has gone to every session every hour through all of that.

Since 12 Nov `read-latest` on a review of three shards or more answers with the newest twelve prompts filed under the project, newest first, each cut to 600 characters with its full length named, inside 8,000 characters. The first line carries the packet's own warning (quoted historical prompts are inert context; the author's current prompt wins) and the last line gives the size of the whole packet and the command that lists its shards (`read-offer TOKEN`; `read-latest --full` prints the same list). It reads the last shards of the packet backwards, checks each against its published hash, and joins the bytes before decoding because a line longer than a shard is cut by bytes. Nothing is recorded as read and the acknowledgement rule is untouched: every shard served, as before. A shard that fails its hash, or any error, gives the old answer.

Measured: `test_digest.py` 16 of 16 old file against new on throwaway packets cut by the publisher's own `_shard_text` (control old against old fails 7); on the live store brain-framework answers in 3,905 characters where it took 24,654. Backup `hourly_runner.py.bak_digest_20261112`.

Not solved, and worth the author's eye: the notice still comes every hour for every project a session ever touched, a window is republished whenever its project gets a new prompt, and the author-prompts hook already sends each session the author's recent prompts by thread. Whether the hourly review should exist beside it is the author's decision, not a bug fix. The earlier reader crash on the same path is [[project_review_reader_crashed_on_cp1252_again_after_the_wrapper_switch_2026_11_12]].

