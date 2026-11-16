---
name: dream_commit_pushed_through_side_branch_server_merge_2026_11_10
description: "Dream commit will not push because GitHub main moves several times a minute? Push it to a side branch and let GitHub merge it (POST /merges): no race, nothing forced. Done by hand 10 Nov (9 commits, merge b1c98f3c4e2f) and built into Push-WithResync as Publish-ViaBranchMerge; 11 fixture arms pass; no dream has used it yet"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T08:34:06+02:00
  status: provisional
  evidence: ""
---

Dream commit will not push because GitHub main keeps moving? Push it to a side branch and let GitHub merge it. Measured and done 10 Nov 2026 on the private brain repository.

**What happened.** The scheduled GPT tasks commit to main 3 to 15 times in almost every minute. The dream's push is a leased push (`--force-with-lease=refs/heads/main:<base>`), and on a rejection `Push-WithResync` re-syncs local main onto the new tip, re-certifies the range with the secret scan and tries again. One such pass takes about three minutes on this clone (376,882 index entries, about 7,400 packs). Three passes in a row by hand (07:4x to 08:07) each ended "main moved since the sync" (rc 6): a three-minute pass cannot win against a stream that moves several times a minute. Nine dream commits (71 paths under 01_ai_consciousness/claude/memory) stayed local.

**The route that has no race.** Push the commit to a side branch (a plain push; nothing else writes that ref), then ask GitHub to merge the branch into main with the merges endpoint (`POST /repos/<slug>/merges`, base main, head the branch). The server makes the merge commit in one step on whatever main is at that moment. Nothing is forced, no peer commit can be lost, and what the merge adds to main is exactly the scanned range as long as main still contains the range's base.

By hand, 10 Nov 08:10-08:21: each of the nine commits scanned against its parent (the nine-commit range is over the scanner's 256 MB bound; each commit alone passes in 40 to 70 s), branch `dream-sync-ahead-20261110` pushed at 62ca9370194c, merged as b1c98f3c4e2f (parents 78953bfd09f0 and 62ca9370194c). Checked as a separate step afterwards: fetch, then `git merge-base --is-ancestor` for both ids against origin/main, both 0; side branch deleted.

**In the dream.** `Push-WithResync` (dream_git_sync.ps1) now ends with `Publish-ViaBranchMerge` when every leased attempt lost and the last range was certified: it refuses unless the server's main contains the certified base (a rewound main is never merged into), pushes `dream-sync-<stamp>-<sha7>`, runs `merge_branch_api.py <slug> <branch> <head oid> <message file> <certified base oid>` (the tool asks the server's compare endpoint for the same containment before merging; exit 0 merged, 3 conflict, 4 anything else) and deletes the side branch either way. A conflict leaves the commit local for the next cycle. `DREAM_BRANCH_MERGE=0` switches it off. The log line to look for: "persist: main moved during every push attempt; <sha7> went out through side branch ... and the server merged it".

**Controls.** `test_push_with_resync_lease.py` (local bare remote, a stand-in merge tool with the same arguments and exit codes): 11 arms, 0 failed. The four new ones: BRANCH (peer pushed during the attempt: merged, one merge commit, nothing uncertified reachable, no side branch left), BRANCHREWIND (main rewound below the base: nothing pushed), BRANCHCONFLICT (peer wrote the same path: not pushed, main stays the peer's, no side branch left), BRANCHOFF (switch off: old behaviour).

**Not yet seen.** No dream has pushed through this route; the first that can is 10 Nov 10:30. The stand-in tool is not GitHub: the live proof is the by-hand merge above.

**Traps met on the way.** `origin/main` in this clone goes stale, because the sync fetches into `refs/remotes/dream-sync/main`; fetch `origin main` before using it as a merge base (a stale one made nine outgoing commits read as 58).

Related: [[dream_catchup_merged_in_scanned_parts_2026_11_10]], [[git_crash_leaves_index_lock_judged_by_age_and_open_handle_2026_11_10]], [[dream_takes_15h_capped_tail_steps_budget_now_in_runpy_2026_11_10]].

