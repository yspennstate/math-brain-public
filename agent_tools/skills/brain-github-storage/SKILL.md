---
name: brain-github-storage
description: Save brain memories and agent-made files to GitHub, check each copy, catalogue where it went, and only then free the local disk. Use when asked to back up the brain, push results, move big files off the computer, or keep pushes free of CI costs.
---

# Keeping the brain on GitHub

## Where things go

- Memories, indexes and the brain's code: a private git repository.
- Large files (pictures, audio, video, data): release assets on that repository, not git history.
  An asset can be up to 2 GB; GitHub reports its size and sha256 digest.
- Anything meant for other people: a separate public repository, only after a private-material
  scan.

## Upload, check, catalogue, delete

For each file or folder:

1. Upload it (commit and push, or attach to a release).
2. Check the copy on GitHub: for a commit, `git ls-remote` shows the remote head equals your
   commit; for an asset, the size and sha256 digest GitHub reports equal the local file's.
3. Write a catalogue line in the brain: local path, repository, commit or release, digest. Without
   it the file is safe but cannot be found.
4. Only now delete the local copy, and only if the person wants the disk freed. Never delete a file
   whose remote copy you have not checked. Keep files a running job is reading.

## Keeping pushes free

- Read `.github/workflows` before pushing. If workflows run on push, push once per finished piece,
  not per commit, and put `[skip ci]` in the head commit's message unless the change needs the
  tests.
- Do not add workflows, schedules, LFS tracking or large artifacts to a private repository unless
  the person has decided to pay for them.
- Commit by explicit path (`git add <paths>`, `git commit -- <paths>`), so files another agent left
  staged in the same clone do not ride along.

## Before a public push

Scan every file for home-folder paths, names, email addresses, account numbers, keys, tokens and
anything about the person's private projects. Show the person what the scan found when in doubt.
After the push, check it landed (`git ls-remote`) and report the commit.
