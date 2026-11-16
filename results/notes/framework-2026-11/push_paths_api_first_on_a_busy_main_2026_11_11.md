---
name: push_paths_api_first_on_a_busy_main_2026_11_11
description: "Push to the brain repo slow, a git push rejected on a moved tip before the API lane? Since 11 Nov push_paths.sh sends the scanned commit straight to the API lane when main took 5 or more commits in 600 s and starts again on the git lane if that fails; a real push 111 s -> 57 s (about 20 s of it the faster fetch); PUSH_PATHS_API_FIRST=0 switches it off"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T08:14:46+02:00
  status: verified
  evidence: "brain_improvement/agent_run/pusher_api_first/patch_api_first.py, test_api_first.py (16 checks, fails old-as-new); ledger_rows_20261111_p.jsonl; commit d2de7da95afd"
---

A push through push_paths.sh to a repository whose main moves several times a minute (the brain
repository took 248 commits in the hour to 07:08 on 11 Nov 2026) used to fetch, build, scan, then lose a git push to
a moved tip and only then go to the API lane, which landed the same scanned commit in seconds.

Timed on one real one-file push, 07:16, PUSH_PATHS_BUDGET=0 (one git attempt): 111 s = fetch 37 s, read-tree and
staging 5 s, tree and diff 4 s, secret scan 10 s, a git push that took 32 s to be rejected, 4 s sleep, API checks
4 s, landing through GraphQL 13 s. With the default budget of 150 s a caller paid a second fetch and a second
rejected push before the API lane.

Since 11 Nov the script decides after the scan: when the fetched history of main holds PUSH_PATHS_BUSY_COMMITS (5)
or more commits in the last PUSH_PATHS_BUSY_WINDOW (600) seconds, and the API lane may be used for this push
(PUSH_PATHS_API not 0, push_paths_gitdata.py beside the script, no push CI in the repository or [skip ci] in the
message), it prints "main is busy (N commits in the last 600 s): the scanned commit goes to the API lane without a
git push" and goes there. Nothing else changed: the same removal check and secret scan run first, the same disk
check runs before the API call, and the API lane still holds the remote to the tip it reads.

If the API lane then does not land the commit for any reason (no credential, a path changed on disk since the scan,
a refusal, exit 4), the script prints "...: starting again on the git lane" and runs itself again with
PUSH_PATHS_API_FIRST=0, which is the old order with the API lanes as fallback. So the new order cannot fail a push
the old order would have landed; it can cost one extra round.

Switch it off for one call with PUSH_PATHS_API_FIRST=0. A quiet repository (fewer than five commits in ten minutes)
pushes by git as before.

Controls: brain_improvement/agent_run/pusher_api_first/test_api_first.py <old> <new> <empty dir> builds bare
origins on disk with commits dated by hand, a stand-in for push_paths_gitdata.py and a stand-in credential in the
clone's own config (the secret scan refuses a run that inherits git settings from the environment, and every new
clone here carries the pre-push cost guard, so the CI cases set ALLOW_CI_PUSH=1). Sixteen checks; with the old file
given as new the busy case fails.

First real push after the landing, 08:06 on 11 Nov, default settings, five paths, 50 commits on main in the last
600 s: 57 s end to end, no git push attempted, landed through GraphQL on the second try (the tip moved once) as
d2de7da95afd. Not all of the 54 s is this change: the fetch had also dropped from 37 s to 11-20 s that hour when
the pack index was rebuilt. The part that is this change is the rejected git push (32 s) and the sleep (4 s).

Not covered: the Macs carry their own copies of push_paths.sh (told on the fleet board); callers that wrap the
script in `timeout` keep their own limits; the fetch itself is not shortened. A slow fetch in the brain checkout is
packs outside the multi-pack-index (see
[[process_ready_at_belownormal_is_starved_not_hung_brain_midx_hourly_2026_11_11]]); to see it, run the fetch with
GIT_TRACE2_PERF=<file> and compare the trace's `midx load/num_packs` with the count of .pack files.

Rollback: copy push_paths.sh.bak_apifirst_20261111 over push_paths.sh.

