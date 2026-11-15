"""build_squash.py - one commit that carries a replayed backlog (10 Nov 2026).

    python build_squash.py <repo> <onto> <replayed head> <local tip> <out file>

After a long stall the dream's local main holds many commits that main never received as commits (86 on 10 Nov).
Replaying them one by one takes about an hour while main moves every few seconds, so the leased push cannot win.
This writes ONE commit whose tree is the replayed head's tree and whose parent is <onto>, with the local commits'
subjects in its body. It moves no ref and touches neither the index nor the working tree; the commit id is printed on
the last line and written to <out file>. Exit 0 ok, 3 refused.
"""
import os
import subprocess
import sys

NOWIN = 0x08000000 if os.name == "nt" else 0


def git(repo, args, inp=None):
    e = dict(os.environ)
    e["GIT_NO_LAZY_FETCH"] = "1"
    p = subprocess.run(["git", "-C", repo] + args, input=inp, capture_output=True, creationflags=NOWIN, env=e)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args[:3]), p.stderr.decode("utf-8", "replace")[:200]))
    return p.stdout.decode("utf-8", "replace")


def main():
    if len(sys.argv) != 6:
        print(__doc__.split("\n\n")[0], file=sys.stderr)
        return 2
    repo, onto, head, tip, out = sys.argv[1:]
    onto = git(repo, ["rev-parse", "--verify", onto + "^{commit}"]).strip()
    head = git(repo, ["rev-parse", "--verify", head + "^{commit}"]).strip()
    tip = git(repo, ["rev-parse", "--verify", tip + "^{commit}"]).strip()
    anc = subprocess.run(["git", "-C", repo, "merge-base", "--is-ancestor", onto, head], creationflags=NOWIN)
    if anc.returncode != 0:
        print("refused: the replayed head does not descend from onto")
        return 3
    n_replayed = int(git(repo, ["rev-list", "--count", onto + ".." + head]).strip())
    subjects = [l for l in git(repo, ["log", "--reverse", "--format=%h %ad %s", "--date=short",
                                      onto + ".." + tip]).splitlines() if l.strip()]
    # The replay drops a local commit whose change main already holds (cherry-pick equivalent, or empty once its
    # conflicts resolve to the live bytes), so it may carry fewer commits than the local side has - never more.
    if n_replayed < 1 or n_replayed > len(subjects):
        print("refused: %d replayed commits against %d local ones" % (n_replayed, len(subjects)))
        return 3
    tree = git(repo, ["rev-parse", "--verify", head + "^{tree}"]).strip()
    if tree == git(repo, ["rev-parse", "--verify", onto + "^{tree}"]).strip():
        print("refused: the replayed tree equals onto's tree; there is nothing to carry")
        return 3
    first = subjects[0].split(" ")[1] if subjects else "?"
    last = subjects[-1].split(" ")[1] if subjects else "?"
    msg = ("Nightly dream: catch-up of %d local commits (%s to %s)\n\n"
           "The dream's push was blocked from 21 Oct; these commits were replayed onto main and are carried here as\n"
           "one commit (%d of them held a change main did not already have). Where main already held a file's\n"
           "content, main's version stands; a local version main never had is under\n"
           "12_cognitive_architecture/sync_carried/<commit>/.\n\n%s\n\n"
           "Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>\n") % (len(subjects), first, last, n_replayed,
                                                                           "\n".join(subjects))
    commit = git(repo, ["commit-tree", tree, "-p", onto, "-F", "-"], msg.encode("utf-8")).strip()
    if len(commit) != 40:
        print("refused: commit-tree gave no id")
        return 3
    with open(out, "w", encoding="ascii", newline="\n") as fh:
        fh.write(commit + "\n")
    print("subjects %d, tree %s, parent %s" % (len(subjects), tree[:12], onto[:12]))
    print(commit)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("build_squash: " + str(exc)[:300], file=sys.stderr)
        sys.exit(3)
