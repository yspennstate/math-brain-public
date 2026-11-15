---
name: dream_push_merge_locally_first_partial_clone_missing_ok_2026_11_10
description: "Dream branch merge 500s, or write-tree hangs 14 min in the brain clone? Merge locally first (merge-tree, view conflicts take main's), push the merge; partial clone needs write-tree --missing-ok (14 min -> 34 s)"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T18:34:19+02:00
  status: verified
  evidence: "test_push_with_resync_lease.py 12/12 incl. BRANCHVIEWS, 10 Nov 18:3x; 77/80 sampled memory files equal live"
---

The dream commit that sat local since this morning (28b1488) did not reach GitHub because the side-branch route sent the dream commit itself, whose parent was far behind main. GitHub's merge API then had to merge a 6,000-path catch-up and returned 500.

The fix (10 Nov, dream_git_sync.ps1 Publish-ViaBranchMerge): merge locally first, then send the merge.
- `git merge-tree --write-tree --name-only --no-messages <main tip> <dream commit>` gives the merged tree.
- On a conflict (rc 1), if every conflicted path matches `^01_ai_consciousness/(brain|claude/memory)/[^/]+$`, those paths take main's blob. These are generated views and mirror files that the next sync rebuilds anyway. The rewrite goes through a temp GIT_INDEX_FILE: read-tree, then update-index --cacheinfo (or --force-remove).
- Any other conflict leaves the commit local and logged.
- Then run `commit-tree -p <tip> -p <dream>`, push that merge to `dream-sync-<stamp>-<sha7>`, and have merge_branch_api.py fast-forward main.

The trap: the brain clone is a PARTIAL clone (promisor packs). A plain `git write-tree` lazily fetched about 76,554 missing blobs and ran 14+ minutes. `write-tree --missing-ok` did the same job in 34 s. Use --missing-ok (or merge-tree --write-tree, which does not need the blobs) on any tree-building step in that clone.

Tests: test_push_with_resync_lease.py has 12 controls, including BRANCHVIEWS (dream and peer both rewrite the same view; main's view wins, nothing uncertified, no side branch left). It passed 12/12 on 10 Nov 18:3x. Acceptance is merge_is_honest: the merge's tree equals merge-tree(p1, p2), and every conflicted path holds p1's blob.

Spot check before publishing 28b1488: the resolved tree differed from main in 6,416 paths (3,760 added, 2,654 changed, almost all memory mirror files). 77 of 80 sampled files equal the live memory file, so the merge is catch-up, not damage.

Related: [[brain_push_six_minutes_pack_bloat_branch_route_2026_11_10]] [[dream_commit_pushed_through_side_branch_server_merge_2026_11_10]] [[dream_catchup_merged_in_scanned_parts_2026_11_10]]

