"""dream_sync_index.py - let the dream's checkout move keep local files in place instead of deleting or parking them.

    python dream_sync_index.py stage <repo> <old> <target> <paths_file> <staged_out> <undo_out>
    python dream_sync_index.py undo  <repo> <undo_file>
    python dream_sync_index.py absent <repo> <old> <target> <staged_out> <undo_out>
    python dream_sync_index.py present <repo> <out_file>

`git reset --keep <target>` refuses a path whose local file would be overwritten: an untracked copy of an incoming file,
or a tracked file edited here. dream_git_sync.ps1 used to delete the untracked copies (identical ones outright,
differing ones after copying them aside) and to revert edited files to HEAD, let the move write the incoming version,
and put the local bytes back. For those minutes the files were missing: on 25 Sep 05:3x a campaign's evals read three
bank files in that window and failed (memory the_dreams_git_sync_empties_pushed_campaign_files_for_minutes_2026_09_25).

`stage` sets the INDEX entry of each listed path to the target's own entry (mode and blob, from one
`git diff --raw -z old target`), with one `git update-index -z --index-info`, and never touches the working tree. git's
two-way merge (reset --keep) keeps an index entry that already equals the target's and leaves its file alone; after the
move the file is tracked at the incoming version, clean when its bytes match and shown as an edit when they differ -
the same end state as delete-and-restore, without the gap. Only paths the target adds or modifies as a regular file or
symlink are staged; everything else (a deletion, a submodule, a path not in the diff) is left to the caller's old
handling and simply not listed in <staged_out>. <undo_out> gets the index entries to put back if the move is refused:
the HEAD entry for a tracked path, mode 0 (remove) for an untracked one. `undo` feeds that file to --index-info.

Exit 0 on success (possibly staging nothing); anything else means nothing was changed and the caller keeps its old path.
"""
import os
import subprocess
import sys

NOWIN = 0x08000000 if os.name == "nt" else 0
ZERO = "0" * 40
MODES = ("100644", "100755", "120000")


def git(repo, args, inp=None):
    p = subprocess.run(["git", "-C", repo] + args, input=inp, capture_output=True, creationflags=NOWIN)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args[:3]), p.stderr.decode("utf-8", "replace")[:200]))
    return p.stdout


def raw_diff(repo, old, target):
    out = git(repo, ["-c", "core.quotepath=false", "diff", "--raw", "-z", "--no-renames", "--no-abbrev", old, target])
    parts = out.split(b"\0")
    entries = {}
    i = 0
    while i + 1 < len(parts) and parts[i].startswith(b":"):
        meta = parts[i][1:].decode("ascii").split()
        path = parts[i + 1].decode("utf-8", "surrogateescape")
        if len(meta) == 5:
            entries[path] = {"old_mode": meta[0], "new_mode": meta[1], "old_oid": meta[2], "new_oid": meta[3],
                             "status": meta[4]}
        i += 2
    return entries


def current_index(repo, paths):
    """{path: (mode, oid)} for stage-0 index entries of the given paths (absent = untracked)."""
    if not paths:
        return {}
    # a pathspec per path would overflow the command line on a long list; read the whole index once
    out = git(repo, ["-c", "core.quotepath=false", "ls-files", "-s", "-z"])
    want = set(paths)
    have = {}
    for rec in out.split(b"\0"):
        if not rec:
            continue
        head, _, path = rec.partition(b"\t")
        p = path.decode("utf-8", "surrogateescape")
        if p in want:
            mode, oid, stage = head.decode("ascii").split()
            if stage == "0":
                have[p] = (mode, oid)
            else:
                have[p] = ("conflict", oid)
    return have


def stage(repo, old, target, paths_file, staged_out, undo_out):
    paths = [l.rstrip("\r\n") for l in open(paths_file, encoding="utf-8-sig") if l.rstrip("\r\n")]
    raw = raw_diff(repo, old, target)
    idx = current_index(repo, paths)
    todo, undo = [], []
    for p in dict.fromkeys(paths):
        e = raw.get(p)
        if not e or e["status"] not in ("A", "M", "T") or e["new_mode"] not in MODES or e["new_oid"] == ZERO:
            continue
        cur = idx.get(p)
        if cur is not None and cur[0] == "conflict":
            continue
        todo.append((e["new_mode"], e["new_oid"], p))
        undo.append((cur[0], cur[1], p) if cur is not None else ("0", ZERO, p))
    # the undo file is written BEFORE the index changes, so a crash in between can still be undone
    tmp = undo_out + ".tmp"
    with open(tmp, "wb") as fh:
        for mode, oid, p in undo:
            fh.write(("%s %s\t" % (mode, oid)).encode("ascii") + p.encode("utf-8", "surrogateescape") + b"\0")
    os.replace(tmp, undo_out)
    if todo:
        data = b"".join(("%s %s\t" % (mode, oid)).encode("ascii") + p.encode("utf-8", "surrogateescape") + b"\0"
                        for mode, oid, p in todo)
        git(repo, ["update-index", "-z", "--index-info"], data)
    tmp = staged_out + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        for _mode, _oid, p in todo:
            fh.write(p + "\n")
    os.replace(tmp, staged_out)
    return 0


def undo(repo, undo_file):
    data = open(undo_file, "rb").read()
    if data:
        git(repo, ["update-index", "-z", "--index-info"], data)
    skip = undo_file + ".skip"
    if os.path.exists(skip):
        flagged = open(skip, "rb").read()
        if flagged:
            git(repo, ["update-index", "-z", "--skip-worktree", "--stdin"], flagged)
    return 0


# ABSENT (2026-11-10). The move used to write every file the target adds. Since the other computers push their own
# outputs to this repository, and since AI outputs are uploaded and then removed from this computer (owner, 9 Nov),
# most incoming files are ones this checkout never held: on 10 Nov a move from the stale local main would have
# downloaded and written 171,063 of them. `absent` sets the index entry of each such path to the target's entry and
# marks it skip-worktree, so `git reset --keep` keeps the entry and writes nothing; git then treats the path as
# unchanged. A path already marked that way is brought to the target's entry the same way on later nights. Paths under
# KEEP_PREFIXES (the trees the persist stages and rebuilds) and top-level files are left to the ordinary checkout, and
# so is any path that exists on disk.
KEEP_PREFIXES = ("01_ai_consciousness/",)


def index_flags(repo):
    """{path: (tag, mode, oid, stage)} for the whole index; tag S or s means skip-worktree."""
    out = git(repo, ["-c", "core.quotepath=false", "ls-files", "-v", "-s", "-z"])
    have = {}
    for rec in out.split(b"\0"):
        if not rec:
            continue
        head, _, path = rec.partition(b"\t")
        f = head.decode("ascii").split()
        if len(f) == 4:
            have[path.decode("utf-8", "surrogateescape")] = (f[0], f[1], f[2], f[3])
    return have


def absent(repo, old, target, staged_out, undo_out):
    raw = raw_diff(repo, old, target)
    idx = index_flags(repo)
    todo, undo_rows, reflag = [], [], []
    for p, e in raw.items():
        if e["status"] not in ("A", "M", "T") or e["new_mode"] not in MODES or e["new_oid"] == ZERO:
            continue
        if "/" not in p or p.startswith(KEEP_PREFIXES):
            continue
        cur = idx.get(p)
        if cur is not None and (cur[3] != "0" or cur[0] not in ("S", "s")):
            continue                                   # tracked here and not marked: the ordinary move handles it
        if cur is None and e["status"] != "A":
            continue
        if os.path.lexists(os.path.join(repo, p)):
            continue
        todo.append((e["new_mode"], e["new_oid"], p))
        if cur is None:
            undo_rows.append(("0", ZERO, p))
        else:
            undo_rows.append((cur[1], cur[2], p))
            reflag.append(p)
    tmp = undo_out + ".tmp"
    with open(tmp, "wb") as fh:
        for mode, oid, p in undo_rows:
            fh.write(("%s %s\t" % (mode, oid)).encode("ascii") + p.encode("utf-8", "surrogateescape") + b"\0")
    with open(undo_out + ".skip", "wb") as fh:
        fh.write(b"".join(p.encode("utf-8", "surrogateescape") + b"\0" for p in reflag))
    os.replace(tmp, undo_out)
    if todo:
        data = b"".join(("%s %s\t" % (mode, oid)).encode("ascii") + p.encode("utf-8", "surrogateescape") + b"\0"
                        for mode, oid, p in todo)
        git(repo, ["update-index", "-z", "--index-info"], data)
        git(repo, ["update-index", "-z", "--skip-worktree", "--stdin"],
            b"".join(p.encode("utf-8", "surrogateescape") + b"\0" for _m, _o, p in todo))
    tmp = staged_out + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n", errors="surrogateescape") as fh:
        for _mode, _oid, p in todo:
            fh.write(p + "\n")
    os.replace(tmp, staged_out)
    return 0


# PRESENT (2026-11-13). `absent` marks a path skip-worktree because no file was here. When a file appears later (a
# session writes it, a push lane leaves its copy, a restore puts it back) the mark stays and the entry's stat is zero.
# core.sparseCheckout is off in this clone, so `git reset --keep` compares such an entry with the file, finds them
# different and refuses the whole move ("Entry ... not uptodate. Cannot merge."); `git diff` and `git status` skip
# marked entries, so neither the facts helper nor the parking loop ever lists the file. From 10 to 13 Nov three such
# files (one tsv, two scripts, each holding exactly the incoming bytes) kept every night's commit local. `present`
# clears the mark on every marked entry whose file exists. An entry whose file holds the index's own bytes also gets
# its stat refreshed (the move does not refresh, and a zero stat reads as edited). After that the file is an ordinary
# tracked file: unchanged, or shown as edited and handled by the caller's rules for edited files.
def present(repo, out_file):
    idx = index_flags(repo)
    marked = [p for p, v in idx.items()
              if v[0] in ("S", "s") and v[3] == "0" and v[1] in MODES and "\n" not in p
              and os.path.isfile(os.path.join(repo, p))]
    rows = []
    if marked:
        out = git(repo, ["hash-object", "--stdin-paths"],
                  ("\n".join(marked) + "\n").encode("utf-8", "surrogateescape"))
        shas = out.decode("ascii").split()
        if len(shas) != len(marked):
            raise RuntimeError("hash-object returned %d ids for %d paths" % (len(shas), len(marked)))
        same = [p for p, s in zip(marked, shas) if s == idx[p][2]]
        git(repo, ["update-index", "-z", "--no-skip-worktree", "--stdin"],
            b"".join(p.encode("utf-8", "surrogateescape") + b"\0" for p in marked))
        if same:
            git(repo, ["update-index", "-z", "--info-only", "--stdin"],
                b"".join(p.encode("utf-8", "surrogateescape") + b"\0" for p in same))
        keep = set(same)
        rows = [(p, "same" if p in keep else "differs") for p in marked]
    tmp = out_file + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n", errors="surrogateescape") as fh:
        for p, kind in rows:
            fh.write("%s\t%s\n" % (p, kind))
    os.replace(tmp, out_file)
    return 0


def main():
    if len(sys.argv) >= 4 and sys.argv[1] == "present":
        return present(sys.argv[2], sys.argv[3])
    if len(sys.argv) >= 7 and sys.argv[1] == "absent":
        return absent(*sys.argv[2:7])
    if len(sys.argv) >= 8 and sys.argv[1] == "stage":
        return stage(*sys.argv[2:8])
    if len(sys.argv) >= 4 and sys.argv[1] == "undo":
        return undo(sys.argv[2], sys.argv[3])
    print(__doc__.split("\n\n")[0], file=sys.stderr)
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("dream_sync_index: " + str(exc)[:300], file=sys.stderr)
        sys.exit(3)
