---
name: brain_clone_current_but_github_main_stale_2026_11_08
description: "Brain scripts on GitHub stale? 8 Nov: local clone's dreaming mirror matched live 576/577 but GitHub main had 22 stale + 47 absent (persist not committing 8 days); GraphQL oid compare finds it in a minute; landed 26 (b418ea89) with a head-moved retry"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T09:29:57+02:00
  status: verified
  evidence: "commit b418ea89e3e3ed0392157fefc908d9c7c4144fd2"
---

On 8 Nov the local brain clone's 12_cognitive_architecture/dreaming matched the live ~/.claude/dreaming scripts 576 of 577 by sha256, yet GitHub main held 22 of the recently changed ones at an old blob and lacked 47 (41 of those were other agents' dev copies such as brain_q*_68ce.py). The dream's persist step had copied the files into the clone but had not committed for about eight days, so "the mirror matches" on disk said nothing about GitHub.

How to check, cheaply: one GraphQL query of `object(expression: "main:<path>") { oid }` per file, 60 aliases per query, compared with the local git blob sha1 (gh_dry.py; 163 files in about a minute, no REST budget used). A null oid means absent, a different oid means stale.

Landing: 26 files went in as one createCommitOnBranch, commit b418ea89 (blob readback all matched, scan_secrets clean). The first two tries were refused because main moved between the head read and the mutation: other agents land every few seconds, and uploading 26 files takes long enough to lose the race. A bounded retry that re-reads the head on an "expected ... head" refusal (land_gql_retry.py, up to 6 tries) landed it on the second try.

brain.py was left out because another agent held its write claim; GitHub's copy stays behind the live one until that landing carries it.

How to apply: before saying the brain is on GitHub, compare against main's blobs, not against the local clone; land by API with a head-moved retry.


Related: [[github_graphql_create_commit_on_branch_lands_when_rest_quota_is_zero_2026_11_08]] [[the_brain_repo_outgrew_git_pushes_every_landing_goes_by_the_api_gist_2026_11_02]] [[the_dream_has_not_committed_since_08_27_and_its_reason_was_swallowed_2026_09_02]]
