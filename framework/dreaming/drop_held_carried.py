"""drop_held_carried.py <repo> <head> <out file> - drop carried .jsonl snapshots whose every line stays held (10 Nov 2026).

The replay carries a local version main never had to 12_cognitive_architecture/sync_carried/<commit>/<path>. For a
line-record log that several local commits each snapshotted, that is one nested copy per commit (10 Nov: seven copies
of two monthly prompt logs, 195 MB). A carried .jsonl is dropped here only when every non-blank line of it is in a
file that stays in the tree: a same-stem sibling of the original path (PROMPTS_2026-10.p01.jsonl beside
PROMPTS_2026-10.jsonl) or a larger carried snapshot of the same path that is kept. Nothing else is touched. Writes a
commit on top of <head> (no ref, index or working-tree change), prints one line per carried .jsonl and the new id last.
Exit 0 ok (the id is <head> itself when nothing can be dropped), 3 refused.
"""
import hashlib
import os
import subprocess
import sys
import tempfile

NOWIN = 0x08000000 if os.name == "nt" else 0
CARRY = "12_cognitive_architecture/sync_carried/"
ZERO = "0" * 40


def git(repo, args, inp=None, env=None):
    e = dict(os.environ)
    e["GIT_NO_LAZY_FETCH"] = "1"
    if env:
        e.update(env)
    p = subprocess.run(["git", "-C", repo] + args, input=inp, capture_output=True, creationflags=NOWIN, env=e)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args[:3]), p.stderr.decode("utf-8", "replace")[:200]))
    return p.stdout


def line_set(repo, head, path):
    data = git(repo, ["cat-file", "blob", "%s:%s" % (head, path)])
    return {hashlib.blake2b(l.rstrip(b"\r"), digest_size=16).digest() for l in data.split(b"\n") if l.strip()}, len(data)


def main():
    repo, head, out = sys.argv[1:4]
    head = git(repo, ["rev-parse", "--verify", head + "^{commit}"]).decode().strip()
    names = [n for n in git(repo, ["ls-tree", "-r", "-z", "--name-only", head, "--", CARRY]).decode(
        "utf-8", "surrogateescape").split("\0") if n.endswith(".jsonl")]
    groups = {}
    for c in names:
        commit, _, orig = c[len(CARRY):].partition("/")
        if orig:
            groups.setdefault(orig, []).append(c)
    drops, saved = [], 0
    for orig, snaps in sorted(groups.items()):
        folder, _, base = orig.rpartition("/")
        stem = base.split(".")[0]
        spec = [head, "--", folder + "/"] if folder else [head]
        sib = [s for s in git(repo, ["ls-tree", "-z", "--name-only"] + spec).decode("utf-8", "surrogateescape").split("\0")
               if s and s.rpartition("/")[2].split(".")[0] == stem and s.endswith(".jsonl")]
        pool = set()
        for s in sib:
            pool |= line_set(repo, head, s)[0]
        loaded = sorted(((line_set(repo, head, c), c) for c in snaps), key=lambda t: -len(t[0][0]))
        for (lines, size), c in loaded:
            missing = len(lines - pool)
            keep = missing > 0
            print("%s  %6.1f MB  lines %7d  not held by what stays %6d  %s" % (
                "keep" if keep else "DROP", size / 2 ** 20, len(lines), missing, c[len(CARRY):][:90]))
            if keep:
                pool |= lines
            else:
                drops.append(c)
                saved += size
    if not drops:
        print("nothing to drop")
        new = head
    else:
        fd, idx = tempfile.mkstemp(prefix="drop_carried_idx_")
        os.close(fd)
        os.remove(idx)
        env = {"GIT_INDEX_FILE": idx}
        try:
            git(repo, ["read-tree", head], env=env)
            inp = b"".join(("0 %s\t" % ZERO).encode("ascii") + c.encode("utf-8", "surrogateescape") + b"\0" for c in drops)
            git(repo, ["update-index", "-z", "--index-info"], inp=inp, env=env)
            tree = git(repo, ["write-tree", "--missing-ok"], env=env).decode().strip()
        finally:
            for f in (idx, idx + ".lock"):
                try:
                    os.remove(f)
                except OSError:
                    pass
        left = [n for n in git(repo, ["ls-tree", "-r", "-z", "--name-only", tree, "--", CARRY]).decode(
            "utf-8", "surrogateescape").split("\0") if n]
        if any(d in left for d in drops):
            print("refused: a dropped path is still in the tree")
            return 3
        msg = ("sync: drop %d carried log snapshots whose every line is held by a file that stays (%.1f MB)\n\n"
               "Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>\n" % (len(drops), saved / 2 ** 20))
        new = git(repo, ["commit-tree", tree, "-p", head, "-F", "-"], inp=msg.encode("utf-8")).decode().strip()
        if len(new) != 40:
            print("refused: commit-tree gave no id")
            return 3
        print("dropped %d, %.1f MB" % (len(drops), saved / 2 ** 20))
    with open(out, "w", encoding="ascii", newline="\n") as fh:
        fh.write(new + "\n")
    print(new)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("drop_held_carried: " + str(exc)[:300], file=sys.stderr)
        sys.exit(3)
