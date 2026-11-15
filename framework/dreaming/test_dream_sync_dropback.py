"""Controls for the 15 Nov 2026 fix: the dream's move must not delete a local copy, and a file rewritten while the
move is being prepared keeps its newest bytes.

    python -X utf8 test_dream_sync_dropback.py <dir holding dream_git_sync.ps1 and its helpers> <work dir> fixed|old

Builds a scratch origin, a checkout A one commit behind, and a script dir whose index helper refuses `stage` (the 02:55
sync of 15 Nov staged nothing in place) and whose facts helper rewrites two files after reading their hashes (a session
writing during the six minutes between the facts and the move). In A before the sync:
  same.txt    untracked, the incoming bytes          -> must be on disk afterwards (the old script deleted it)
  raced.txt   untracked, the incoming bytes at the facts, a third version after  -> must keep the third version
  tr.txt      tracked, edited to the incoming bytes at the facts, a third version after -> must keep the third version
  differ.txt  untracked, a third version             -> kept (was already kept)
  new.txt     never held                              -> stays absent, marked not held
expect = fixed: exit 0 only when every check holds. expect = old: exit 0 only when the old faults show (the control
that proves this test can see them).
"""
import os
import shutil
import subprocess
import sys

NW = 0x08000000
V1, V2, THIRD = b"one\n", b"two\n", b"third, local\n"
HOOKS = ""

SHIM_INDEX = (
    "import os, runpy, sys\n"
    "if len(sys.argv) > 1 and sys.argv[1] == 'stage':\n"
    "    sys.exit(1)\n"
    "real = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real_dream_sync_index.py')\n"
    "sys.argv[0] = real\n"
    "runpy.run_path(real, run_name='__main__')\n"
)
SHIM_FACTS = (
    "import os, runpy, sys\n"
    "real = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'real_dream_sync_facts.py')\n"
    "repo = sys.argv[1]\n"
    "argv0 = sys.argv[0]\n"
    "sys.argv[0] = real\n"
    "code = 0\n"
    "try:\n"
    "    runpy.run_path(real, run_name='__main__')\n"
    "except SystemExit as e:\n"
    "    code = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)\n"
    "for n in ('raced.txt', 'tr.txt'):\n"
    "    with open(os.path.join(repo, 'data', n), 'wb') as fh:\n"
    "        fh.write(b'third, local\\n')\n"
    "sys.exit(code)\n"
)


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
            d[path] = head.split()[0]
    return d


def main():
    global HOOKS
    src_dir, work, expect = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
    ps1_name = sys.argv[4] if len(sys.argv) > 4 else "dream_git_sync.ps1"
    if os.path.isdir(work):
        shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    HOOKS = os.path.join(work, "nohooks")
    os.makedirs(HOOKS)
    scripts = os.path.join(work, "scripts")
    os.makedirs(scripts)
    shutil.copyfile(os.path.join(src_dir, ps1_name), os.path.join(scripts, "dream_git_sync.ps1"))
    for n in os.listdir(src_dir):
        if n.startswith("dream_sync_") and n.endswith(".py"):
            shutil.copyfile(os.path.join(src_dir, n), os.path.join(scripts, "real_" + n if n in (
                "dream_sync_index.py", "dream_sync_facts.py") else n))
    with open(os.path.join(scripts, "dream_sync_index.py"), "w", encoding="ascii", newline="\n") as fh:
        fh.write(SHIM_INDEX)
    with open(os.path.join(scripts, "dream_sync_facts.py"), "w", encoding="ascii", newline="\n") as fh:
        fh.write(SHIM_FACTS)

    origin, a, b = (os.path.join(work, n) for n in ("origin.git", "A", "B"))
    run(["git", "init", "-q", "--bare", "-b", "main", origin])
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", origin, b])
    put(b, "data/base.txt", V1)
    put(b, "data/tr.txt", V1)
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "c0")
    git(b, "push", "-q", "origin", "HEAD:main")
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", origin, a])
    git(a, "config", "core.autocrlf", "false")
    c0 = git(a, "rev-parse", "HEAD").strip()
    for n in ("same", "raced", "differ", "new", "tr"):
        put(b, "data/%s.txt" % n, V2)
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "target")
    git(b, "push", "-q", "origin", "HEAD:main")
    t = git(b, "rev-parse", "HEAD").strip()
    put(a, "data/same.txt", V2)
    put(a, "data/raced.txt", V2)
    put(a, "data/tr.txt", V2)
    put(a, "data/differ.txt", THIRD)

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
                        scripts, a, origin, t, log], capture_output=True, creationflags=NW, timeout=900)
    text = open(log, encoding="utf-8-sig").read() if os.path.exists(log) else ""
    print(text.strip()[:1800])
    if r.stderr.strip():
        print("PS STDERR " + r.stderr.decode("utf-8", "replace")[:600])
    head = git(a, "rev-parse", "HEAD").strip()
    fl = flags(a)
    status = sorted(l for l in git(a, "status", "--porcelain").splitlines() if l.strip())
    tmp = os.environ.get("TEMP", "")
    left = [n for n in (os.listdir(tmp) if os.path.isdir(tmp) else []) if n.startswith("dream_sync_park_") and n.endswith("_drop")]
    obs = {
        "parse_errors_0": "PARSE_ERRORS 0" in text,
        "result_true": "RESULT True" in text,
        "head_is_target": head == t,
        "nothing_in_place": "0 files indexed in place" in text,
        "same_on_disk_v2": get(a, "data/same.txt") == V2,
        "same_gone": get(a, "data/same.txt") is None,
        "raced_keeps_third": get(a, "data/raced.txt") == THIRD,
        "raced_gone": get(a, "data/raced.txt") is None,
        "tr_keeps_third": get(a, "data/tr.txt") == THIRD,
        "tr_overwritten_v2": get(a, "data/tr.txt") == V2,
        "differ_keeps_third": get(a, "data/differ.txt") == THIRD,
        "base_untouched": get(a, "data/base.txt") == V1,
        "new_not_written": get(a, "data/new.txt") is None,
        "new_marked": fl.get("data/new.txt", "?") in ("S", "s"),
        "no_mark_on_present": all(fl.get("data/%s.txt" % n, "?") not in ("S", "s") for n in ("same", "raced", "tr", "differ")),
        "race_logged": "changed while the move was being prepared" in text,
        "stage_failure_logged": "the in-place index step failed (exit 1 on try 2" in text,
        "status_three_modified": status == [" M data/differ.txt", " M data/raced.txt", " M data/tr.txt"],
    }
    want = {
        "fixed": ["parse_errors_0", "result_true", "head_is_target", "nothing_in_place", "same_on_disk_v2",
                  "raced_keeps_third", "tr_keeps_third", "differ_keeps_third", "base_untouched", "new_not_written",
                  "new_marked", "no_mark_on_present", "race_logged", "stage_failure_logged", "status_three_modified"],
        "old": ["parse_errors_0", "result_true", "head_is_target", "nothing_in_place", "same_gone", "raced_gone",
                "tr_overwritten_v2", "differ_keeps_third", "base_untouched", "new_not_written"],
    }[expect]
    bad = [k for k in want if not obs[k]]
    for k in want:
        print("%-24s %s" % (k, "ok" if obs[k] else "FAIL"))
    print("status: %r" % status)
    print("drop dirs left in TEMP: %d" % len(left))
    print("%s: %d of %d checks pass" % (expect, len(want) - len(bad), len(want)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
