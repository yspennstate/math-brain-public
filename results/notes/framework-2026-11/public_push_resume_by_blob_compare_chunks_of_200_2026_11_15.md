---
name: public_push_resume_by_blob_compare_chunks_of_200_2026_11_15
description: "[VERIFIED] Big push to math-brain-public times out on the slow laptop? Chunks of 200 under timeout 2400, clone path first, resume by comparing git hash-object blobs to origin ls-tree; one pusher per clone"
metadata:
  type: reference
  created: 2026-11-15
  created_at: 2026-11-15T10:43:36+02:00
  status: verified
  evidence: "B11 push 15 Nov: chunk 6 rc 124 at 900 s but landed; resume 09:56-10:41 ended 'final pending 0 of 2765 origin 75c8ff51b'"
---

On this laptop (PowerShell start 30-38 s, commit near 88 pct) a push of more than a few hundred files to math-brain-public through push_paths.sh does not finish in one call. On 15 Nov the B11 batch (2,765 files) ran its sixth 200-file chunk into a 900 s timeout (rc 124), though the chunk had in fact landed.

What works:
- push_paths.sh takes the CLONE PATH as its first argument ("$HOME/mbp_agent"), then the message, then the files.
- Chunks of 200 files, each under `timeout 2400`, with ALLOW_REMOVALS=1 PUSH_PATHS_NO_PROMPT=1 and [skip ci] in the message.
- Resume by comparison, not by memory: fetch, `git -c core.quotepath=off ls-tree -r origin/main`, then hash the local files with `git hash-object --stdin-paths` (so CRLF filters apply; a raw sha1 of the bytes marks every text file as changed) and push only the paths whose blob differs. Repeat up to four passes; the run ends "final pending N of M".
- The scripts are push_rest.sh and pending_paths.py (session scratchpad of an agent, 15 Nov); copy them into agent_run if they are needed again.
- Never run two pushers on one clone; chain the second after the first's rc line.
- When the remote tip moves, push_paths falls back to the GitHub API, and that path skips the privacy scan (memory push_paths_api_fallback_skipped_public_privacy_scan_2026_11_15), so scan the folder before pushing.

What would change this: a faster machine, or push_paths learning to resume on its own.

