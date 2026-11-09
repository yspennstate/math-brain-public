# GitHub as the brain's storage

A brain that lives on one laptop is one disk failure away from gone, and it cannot be shared with
agents on another computer. Keeping it in a git repository on GitHub fixes both.

## What goes where

- The memories, the indexes and the brain's own code go in a private repository. Git keeps every
  version, so a memory that turns out wrong can be marked superseded and the old text is still in
  the history.
- Large files the agents make (pictures, audio, video, data dumps) do not belong in git history.
  Put them on a release of the same repository as release assets. A release asset can be up to
  2 GB, and GitHub reports its size and sha256 digest, so you can check the upload byte for byte.
- Anything you want other people to use (the framework, worked examples, papers) goes in a
  separate public repository, after a check for private material.

## Saving, checking, then deleting

The habit that keeps a laptop's disk free and nothing lost is: upload, check the copy on GitHub,
and only then delete the local file. Tell the agent exactly that:

```
upload <folder> to github: text files into <repository>, large files as release assets. for each
file check the copy on github (size and sha256 for assets, the remote commit for files). only
when the check passes, delete the local copy. keep a list of what went where so the brain can
find it again.
```

The list matters. A file that left the laptop is only useful if the agent can find it later, so
each uploaded file should get a line or a node in the brain saying where it is.

## Keeping it free

A push to GitHub costs nothing. What can cost money is a repository with workflows that run on
every push (GitHub Actions bills minutes past the free allowance, and macOS minutes count ten
times). If a repository has a `.github/workflows` folder:

- push once when a piece is finished, not after every commit;
- put `[skip ci]` in the commit message when the change does not need the tests;
- do not add workflows, scheduled jobs or Git LFS to a private repository without deciding to pay
  for them.

## Before anything goes public

Have the agent scan every file first: home-folder paths, names, email addresses, account numbers,
keys and tokens, and anything about your own projects you would not put on a website. The
framework has a checker (`scripts/check_no_private_labels.py` in the framework repository) and a
secret scanner; run both and read what they flag.

```
I want to publish <folder> in a public repository. scan every file for private material first
(paths, names, emails, keys, anything about my private work) and show me what you found before
you push anything.
```

## Recall that reaches GitHub

Once files have left the laptop, recall should still find them. The pattern is a small catalogue in
the brain (path, repository, release, digest) and a fetch step: recall finds the catalogue entry,
and the agent downloads the file only when it needs it. That keeps the laptop light and the brain
complete.
