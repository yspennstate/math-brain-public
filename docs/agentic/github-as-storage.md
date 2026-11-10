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

## Signing the agent in to GitHub

Everything on this page assumes the agent can push to your GitHub account. You need a free account
on github.com, and then one sign-in on each computer. The usual way is GitHub's own command-line
tool, `gh`: run `gh auth login`, choose GitHub.com and the browser option, and approve the code it
shows you in the browser. After that git on that computer can push without asking again.

Do the sign-in yourself, in the browser. Never paste a password or an access token into the chat
with the agent: whatever you type there is kept in the session's history, and the history may end
up in the very repository you are setting up. The agent can do everything around it:

```
install the GitHub command-line tool if it is missing, then start the sign-in and tell me what
to do in the browser. do not ask me for a password or a token. when I say it is done, create a
private repository called <name> and push one test file to check that it works.
```

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

## One brain on several computers

If you run agents on more than one computer, keep one brain for all of them in one private
repository rather than a separate brain on each machine. The rule is short: pull before work,
push after. An agent that starts on the second computer pulls first and sees what the first one
learned an hour ago; when it finishes, it pushes what it learned so the next agent anywhere sees
it too.

Memories are small text files, one fact each, so two computers rarely edit the same lines and
git merges them on its own. When it cannot, do not let the agent pick a side silently. Have it
keep both versions, mark which is newer and which computer wrote each, and fix it by reading
both.

```
before you start, pull the brain repository. when you finish, push what you saved. if the push
is refused because the other computer pushed first, pull again, merge, and push. if a memory
conflicts, keep both versions with the computer name and time on each, and tell me.
```

Give each computer a short name and have every saved memory say which computer wrote it. When
something goes wrong a week later, that one line tells you where to look.
