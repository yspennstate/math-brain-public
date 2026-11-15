"""build_parts.py - cut one catch-up commit into parts the secret scanner can certify (10 Nov 2026).

    python build_parts.py <repo> <onto> <squash> <out file> [--budget MB]

The scanner reads at most 256 MB of new objects in one scan (scan_secrets.py MAX_TOTAL_OBJECT_BYTES) and at most
64 MB in one object. The 10 Nov catch-up commit held 489.6 MB of new blobs, so one scan of it is refused. This writes
a chain onto -> part 1 -> ... -> part n in which each part adds at most --budget MB (default 170) of the squash's
changed paths, largest first, and the last part's tree is the squash's tree. The scanner is not loosened: every byte
is scanned, one part at a time. No ref, index or working-tree file is touched; the part ids are printed in order and
written to <out file>, one per line. Exit 0 ok, 3 refused.
"""
import os
import subprocess
import sys
import tempfile

NOWIN = 0x08000000 if os.name == "nt" else 0
ZERO = "0" * 40
MAX_OBJECT = 64 * 1024 * 1024


def git(repo, args, inp=None, env=None):
    e = dict(os.environ)
    e["GIT_NO_LAZY_FETCH"] = "1"
    if env:
        e.update(env)
    p = subprocess.run(["git", "-C", repo] + args, input=inp, capture_output=True, creationflags=NOWIN, env=e)
    if p.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args[:3]), p.stderr.decode("utf-8", "replace")[:300]))
    return p.stdout


def changed(repo, onto, squash):
    """[(new_mode, new_oid, path bytes)] for every path the squash changes; a deletion has mode 0 and the zero id."""
    raw = git(repo, ["diff-tree", "-r", "-z", "--raw", "--no-renames", onto, squash])
    parts = raw.split(b"\0")
    rows = []
    i = 0
    while i + 1 < len(parts):
        head = parts[i].decode("ascii")
        if not head.startswith(":"):
            i += 1
            continue
        f = head[1:].split()
        status = f[4][0]
        path = parts[i + 1]
        if status == "D":
            rows.append(("0", ZERO, path))
        elif status in ("A", "M", "T"):
            rows.append((f[1], f[3], path))
        else:
            raise RuntimeError("unexpected status %s" % status)
        i += 2
    return rows


def sizes(repo, oids):
    out = git(repo, ["cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)"],
              inp=("\n".join(oids) + "\n").encode("ascii"))
    got = {}
    for line in out.decode("ascii", "replace").splitlines():
        f = line.split()
        if len(f) == 3 and f[1] in ("blob", "commit"):
            got[f[0]] = int(f[2])
        else:
            raise RuntimeError("object not readable here: %s" % line[:80])
    return got


def main():
    args = [a for a in sys.argv[1:]]
    budget = 170.0
    if "--budget" in args:
        k = args.index("--budget")
        budget = float(args[k + 1])
        del args[k:k + 2]
    if len(args) != 4:
        print(__doc__.split("\n\n")[0], file=sys.stderr)
        return 2
    repo, onto, squash, out = args
    onto = git(repo, ["rev-parse", "--verify", onto + "^{commit}"]).decode().strip()
    squash = git(repo, ["rev-parse", "--verify", squash + "^{commit}"]).decode().strip()
    parent = git(repo, ["rev-parse", "--verify", squash + "^"]).decode().strip()
    if parent != onto:
        print("refused: the squash's parent is %s, not onto" % parent[:12])
        return 3
    rows = changed(repo, onto, squash)
    if not rows:
        print("refused: the squash changes nothing")
        return 3
    size = sizes(repo, sorted({oid for _m, oid, _p in rows if oid != ZERO}))
    big = [(size[oid], p) for _m, oid, p in rows if oid != ZERO and size[oid] > MAX_OBJECT]
    if big:
        print("refused: %d object(s) over the scanner's 64 MB object limit, largest %.1f MB" % (
            len(big), max(b[0] for b in big) / 2 ** 20))
        return 3
    cap = int(budget * 1024 * 1024)
    rows.sort(key=lambda r: -(size.get(r[1], 0)))
    bins, loads = [], []
    for r in rows:
        s = size.get(r[1], 0)
        for k in range(len(bins)):
            if loads[k] + s <= cap:
                bins[k].append(r)
                loads[k] += s
                break
        else:
            bins.append([r])
            loads.append(s)
    full_msg = git(repo, ["cat-file", "commit", squash]).split(b"\n\n", 1)[1]
    subject, _, body = full_msg.partition(b"\n")
    squash_tree = git(repo, ["rev-parse", "--verify", squash + "^{tree}"]).decode().strip()
    fd, idx = tempfile.mkstemp(prefix="build_parts_idx_")
    os.close(fd)
    os.remove(idx)
    env = {"GIT_INDEX_FILE": idx}
    made = []
    try:
        git(repo, ["read-tree", onto], env=env)
        prev = onto
        n = len(bins)
        for k, rows_k in enumerate(bins, 1):
            inp = b"".join(("%s %s\t" % (m, oid)).encode("ascii") + p + b"\0" for m, oid, p in rows_k)
            git(repo, ["update-index", "-z", "--index-info"], inp=inp, env=env)
            tree = git(repo, ["write-tree", "--missing-ok"], env=env).decode().strip()
            if k == n:
                if tree != squash_tree:
                    print("refused: the last part's tree %s is not the squash's tree %s" % (tree[:12], squash_tree[:12]))
                    return 3
                msg = subject + (" (part %d of %d)" % (k, n)).encode("ascii") + b"\n" + body
            else:
                msg = ("%s (part %d of %d)\n\n%d paths, %.1f MB; the last part carries the list of commits.\n\n"
                       "Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>\n" % (
                           subject.decode("utf-8", "replace"), k, n, len(rows_k), loads[k - 1] / 2 ** 20)).encode("utf-8")
            prev = git(repo, ["commit-tree", tree, "-p", prev, "-F", "-"], inp=msg).decode().strip()
            if len(prev) != 40:
                print("refused: commit-tree gave no id")
                return 3
            made.append(prev)
            print("part %d of %d: %s  %d paths  %.1f MB" % (k, n, prev, len(rows_k), loads[k - 1] / 2 ** 20))
    finally:
        for f in (idx, idx + ".lock"):
            try:
                os.remove(f)
            except OSError:
                pass
    with open(out, "w", encoding="ascii", newline="\n") as fh:
        fh.write("\n".join(made) + "\n")
    print("paths %d, largest object %.1f MB, parts %d, last tree equals the squash's tree" % (
        len(rows), max(size.values()) / 2 ** 20 if size else 0.0, len(made)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("build_parts: " + str(exc)[:300], file=sys.stderr)
        sys.exit(3)
