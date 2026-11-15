"""Controls for the 13 Nov 2026 fix: a skip-worktree index entry whose file is on disk must not refuse the dream's move.

    python -X utf8 test_dream_sync_present.py <dir holding dream_git_sync.ps1 and its helpers> <work dir> [expect]

Builds a scratch origin, a checkout A one commit behind, and in A three marked entries whose files are on disk
(f1 = the incoming bytes, f2 = the index's bytes, f3 = a third version), one marked entry with no file (gone) and one
incoming file A never held (new). Runs Sync-LocalMainToAdvertised from the given script dir and prints what happened.
expect = refused | moved: exit 0 only when the observed outcome matches every check for that case.
"""
import os
import shutil
import subprocess
import sys

NW = 0x08000000
V1, V2, THIRD = b"one\n", b"two\n", b"third, local\n"


def run(args, cwd=None, inp=None, ok=True):
    r = subprocess.run(args, cwd=cwd, input=inp, capture_output=True, creationflags=NW)
    if ok and r.returncode != 0:
        raise SystemExit("FAILED %s: %s" % (" ".join(args[:6]), r.stderr.decode("utf-8", "replace")[:400]))
    return r.stdout.decode("utf-8", "replace")


def git(repo, *a, inp=None, ok=True):
    return run(["git", "-C", repo, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "-c",
                "core.autocrlf=false", "-c", "core.hooksPath=" + HOOKS, *a], inp=inp, ok=ok)


def put(repo, rel, data):
    p = os.path.join(repo, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as fh:
        fh.write(data)


def get(repo, rel):
    p = os.path.join(repo, rel.replace("/", os.sep))
    return open(p, "rb").read() if os.path.isfile(p) else None


def flags(repo):
    d = {}
    for rec in git(repo, "ls-files", "-v", "-s", "-z").split("\0"):
        if rec:
            head, path = rec.split("\t", 1)
            f = head.split()
            d[path] = (f[0], f[2])
    return d


def main():
    global HOOKS
    script_dir, work, expect = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
    if os.path.isdir(work):
        shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    HOOKS = os.path.join(work, "nohooks")
    os.makedirs(HOOKS)
    origin, a, b = (os.path.join(work, n) for n in ("origin.git", "A", "B"))
    run(["git", "init", "-q", "--bare", "-b", "main", origin])
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", origin, b])
    for n in ("f1", "f2", "f3", "f4", "gone"):
        put(b, "data/%s.txt" % n, V1)
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "c0")
    git(b, "push", "-q", "origin", "HEAD:main")
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", origin, a])
    git(a, "config", "core.autocrlf", "false")
    c0 = git(a, "rev-parse", "HEAD").strip()
    v1 = git(a, "rev-parse", "HEAD:data/f1.txt").strip()
    marked = ["data/f1.txt", "data/f2.txt", "data/f3.txt", "data/gone.txt"]
    for p in marked:
        os.remove(os.path.join(a, p.replace("/", os.sep)))
    # as dream_sync_index.py absent leaves them: entry rewritten through --index-info (stat zero), then marked
    git(a, "update-index", "-z", "--index-info", inp=b"".join(("100644 %s\t%s" % (v1, p)).encode() + b"\0" for p in marked))
    git(a, "update-index", "-z", "--skip-worktree", "--stdin", inp=b"".join(p.encode() + b"\0" for p in marked))
    put(a, "data/f1.txt", V2)
    put(a, "data/f2.txt", V1)
    put(a, "data/f3.txt", THIRD)
    for n in ("f1", "f2", "f3", "gone", "new"):
        put(b, "data/%s.txt" % n, V2)
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "target")
    git(b, "push", "-q", "origin", "HEAD:main")
    t = git(b, "rev-parse", "HEAD").strip()
    v2 = git(b, "rev-parse", "HEAD:data/f1.txt").strip()

    before = git(a, "reset", "-q", "--keep", "--no-refresh", c0, ok=False)   # no-op move, proves the repo is usable
    log = os.path.join(work, "sync.log")
    harness = os.path.join(work, "harness.ps1")
    with open(harness, "w", encoding="ascii", newline="\r\n") as fh:
        fh.write("param($ScriptDir, $Repo, $Url, $Oid, $LogFile)\n"
                 "$tok = $null; $err = $null\n"
                 "[void][System.Management.Automation.Language.Parser]::ParseFile((Join-Path $ScriptDir 'dream_git_sync.ps1'), [ref]$tok, [ref]$err)\n"
                 "Add-Content -LiteralPath $LogFile -Value ('PARSE_ERRORS ' + @($err).Count) -Encoding UTF8\n"
                 ". (Join-Path $ScriptDir 'dream_git_sync.ps1')\n"
                 "$log = { param($m) Add-Content -LiteralPath $LogFile -Value ('LOG ' + $m) -Encoding UTF8 }\n"
                 "$r = Sync-LocalMainToAdvertised -Repo $Repo -PushUrl $Url -Oid $Oid -Logger $log\n"
                 "Add-Content -LiteralPath $LogFile -Value ('RESULT ' + $r) -Encoding UTF8\n")
    r = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", harness,
                        script_dir, a, origin, t, log], capture_output=True, creationflags=NW, timeout=900)
    text = open(log, encoding="utf-8-sig").read() if os.path.exists(log) else ""
    print(text.strip()[:1500])
    if r.stderr.strip():
        print("PS STDERR " + r.stderr.decode("utf-8", "replace")[:600])
    head = git(a, "rev-parse", "HEAD").strip()
    fl = flags(a)
    status = sorted(l for l in git(a, "status", "--porcelain").splitlines() if l.strip())
    obs = {
        "parse_errors_0": "PARSE_ERRORS 0" in text,
        "result_true": "RESULT True" in text,
        "refused_logged": "moving the checkout was refused" in text,
        "head_is_target": head == t,
        "head_is_old": head == c0,
        "f1_bytes_v2": get(a, "data/f1.txt") == V2,
        "f2_bytes_v2": get(a, "data/f2.txt") == V2,
        "f2_bytes_v1": get(a, "data/f2.txt") == V1,
        "f3_bytes_third": get(a, "data/f3.txt") == THIRD,
        "f4_bytes_v1": get(a, "data/f4.txt") == V1,
        "gone_still_absent": get(a, "data/gone.txt") is None,
        "new_not_written": get(a, "data/new.txt") is None,
        "marks_cleared_f1_f2_f3": all(fl.get("data/f%d.txt" % i, ("?",))[0] not in ("S", "s") for i in (1, 2, 3)),
        "marks_kept_f1_f2_f3": all(fl.get("data/f%d.txt" % i, ("?",))[0] in ("S", "s") for i in (1, 2, 3)),
        "gone_marked": fl.get("data/gone.txt", ("?",))[0] in ("S", "s"),
        "gone_entry_v2": fl.get("data/gone.txt", ("?", "?"))[1] == v2,
        "new_marked_v2": fl.get("data/new.txt", ("?", "?")) in (("S", v2), ("s", v2)),
        "status_only_f3_modified": status == [" M data/f3.txt"],
    }
    want = {
        "moved": ["parse_errors_0", "result_true", "head_is_target", "f1_bytes_v2", "f2_bytes_v2", "f3_bytes_third",
                  "f4_bytes_v1", "gone_still_absent", "new_not_written", "marks_cleared_f1_f2_f3", "gone_marked",
                  "gone_entry_v2", "new_marked_v2", "status_only_f3_modified"],
        "refused": ["parse_errors_0", "refused_logged", "head_is_old", "f1_bytes_v2", "f2_bytes_v1", "f3_bytes_third",
                    "f4_bytes_v1", "gone_still_absent", "new_not_written", "marks_kept_f1_f2_f3", "gone_marked"],
    }[expect]
    bad = [k for k in want if not obs[k]]
    for k in want:
        print("%-28s %s" % (k, "ok" if obs[k] else "FAIL"))
    print("status: %r" % status)
    print("%s: %d of %d checks pass" % (expect, len(want) - len(bad), len(want)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
