"""Controls for the 13 Nov 2026 fix: a commit GitHub advertised must reach a partial clone by an ordinary fetch, never
by a lazy fetch of that one id (which downloads the whole history again).

    python -X utf8 test_dream_confirm_commit.py <dir holding dream_git_sync.ps1> <fresh work dir>

Builds a scratch origin with HIST commits, three blob:none clones one commit behind, and checks:
  A  a plain `git rev-list --count X..HEAD` on the absent tip X downloads a pack whose .promisor names X twice
     (the leak, shown on this git version);
  B  the same command with --no-lazy-fetch refuses and downloads nothing;
  C  Confirm-CommitInClone brings X with an ordinary fetch (a small pack, no single-id .promisor), after which the
     plain command answers and downloads nothing more;
  D  Confirm-CommitInClone on an id that does not exist returns False and leaves the clone as it was.
Exit 0 only when every check holds. If the script dir has no Confirm-CommitInClone, C and D are reported as ABSENT.
"""
import glob
import os
import subprocess
import sys

NW = 0x08000000
HIST = 60


def run(args, cwd=None, ok=True, env=None):
    r = subprocess.run(args, cwd=cwd, capture_output=True, creationflags=NW, env=env)
    if ok and r.returncode != 0:
        raise SystemExit("FAILED %s: %s" % (" ".join(args[:7]), r.stderr.decode("utf-8", "replace")[:400]))
    return r.returncode, r.stdout.decode("utf-8", "replace").strip()


def git(repo, *a, ok=True):
    return run(["git", "-C", repo, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "-c", "core.autocrlf=false",
                "-c", "core.hooksPath=" + HOOKS, "-c", "gc.auto=0", "-c", "maintenance.auto=false", *a], ok=ok)


def packs(repo):
    """{pack base name: (pack bytes, .promisor text or None)}"""
    out = {}
    for p in glob.glob(os.path.join(repo, ".git", "objects", "pack", "*.pack")):
        pr = p[:-5] + ".promisor"
        out[os.path.basename(p)] = (os.path.getsize(p), open(pr, encoding="utf-8", errors="replace").read()
                                    if os.path.isfile(pr) else None)
    return out


def new_packs(before, after):
    return {k: v for k, v in after.items() if k not in before}


def single_id(new, oid):
    return [k for k, (_, prom) in new.items() if prom is not None and prom.split() == [oid, oid]]


def main():
    global HOOKS
    script_dir, work = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if os.path.exists(work):
        raise SystemExit("work dir exists; give a fresh one")
    os.makedirs(work)
    HOOKS = os.path.join(work, "nohooks")
    os.makedirs(HOOKS)
    origin, b = os.path.join(work, "origin.git"), os.path.join(work, "B")
    url = "file:///" + origin.replace("\\", "/")
    run(["git", "init", "-q", "--bare", "-b", "main", origin])
    run(["git", "-C", origin, "config", "uploadpack.allowFilter", "true"])
    run(["git", "-C", origin, "config", "uploadpack.allowAnySHA1InWant", "true"])
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", url, b])
    os.makedirs(os.path.join(b, "d"))
    for i in range(HIST):
        with open(os.path.join(b, "d", "f%02d.txt" % (i % 7)), "wb") as fh:
            fh.write(os.urandom(600) + b"\n%d\n" % i)
        git(b, "add", "-A")
        git(b, "commit", "-q", "-m", "c%d" % i)
    git(b, "push", "-q", "origin", "HEAD:main")
    clones = {}
    for n in ("A", "B2", "C", "D"):
        p = os.path.join(work, "clone_" + n)
        run(["git", "clone", "-q", "--filter=blob:none", "-c", "core.autocrlf=false", url, p])
        clones[n] = p
    # one local commit in each clone (so X..HEAD is a real range), then the origin moves: X is the new tip
    for p in clones.values():
        with open(os.path.join(p, "local.txt"), "wb") as fh:
            fh.write(b"local\n")
        git(p, "add", "local.txt")
        git(p, "commit", "-q", "-m", "local")
    with open(os.path.join(b, "d", "new.txt"), "wb") as fh:
        fh.write(b"new\n")
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "X")
    git(b, "push", "-q", "origin", "HEAD:main")
    x = git(b, "rev-parse", "HEAD")[1]
    full = max(v[0] for v in packs(clones["A"]).values())   # the commits-and-trees pack of the clone
    checks = []

    def have(repo, oid):
        return git(repo, "--no-lazy-fetch", "cat-file", "-e", oid + "^{commit}", ok=False)[0] == 0

    # A: the leak
    a = clones["A"]
    checks.append(("A0 tip X absent before", not have(a, x)))
    before = packs(a)
    rc, out = git(a, "rev-list", "--count", x + "..HEAD", ok=False)
    new = new_packs(before, packs(a))
    sid = single_id(new, x)
    size = sum(new[k][0] for k in sid)
    print("A: plain rev-list rc=%d out=%r; new packs %d, single-id packs %d, %d bytes (clone's first pack total %d)"
          % (rc, out, len(new), len(sid), size, full))
    checks.append(("A1 plain probe answered", rc == 0 and out == "1"))
    checks.append(("A2 plain probe wrote a single-id promisor pack", len(sid) == 1))
    checks.append(("A3 that pack repeats the history (at least 80 pct of the clone's packs)", size >= 0.8 * full))

    # B: the guard alone
    b2 = clones["B2"]
    before = packs(b2)
    rc, out = git(b2, "--no-lazy-fetch", "rev-list", "--count", x + "..HEAD", ok=False)
    new = new_packs(before, packs(b2))
    print("B: guarded rev-list rc=%d; new packs %d" % (rc, len(new)))
    checks.append(("B1 guarded probe refuses", rc != 0))
    checks.append(("B2 guarded probe downloads nothing", len(new) == 0 and not have(b2, x)))

    # C and D: the helper
    harness = os.path.join(work, "harness.ps1")
    with open(harness, "w", encoding="ascii", newline="\r\n") as fh:
        fh.write("param($ScriptDir, $Repo, $Url, $Oid, $LogFile)\n"
                 "$tok = $null; $err = $null\n"
                 "[void][System.Management.Automation.Language.Parser]::ParseFile((Join-Path $ScriptDir 'dream_git_sync.ps1'), [ref]$tok, [ref]$err)\n"
                 "Add-Content -LiteralPath $LogFile -Value ('PARSE_ERRORS ' + @($err).Count) -Encoding UTF8\n"
                 ". (Join-Path $ScriptDir 'dream_git_sync.ps1')\n"
                 "if (-not (Get-Command Confirm-CommitInClone -CommandType Function -ErrorAction SilentlyContinue)) { Add-Content -LiteralPath $LogFile -Value 'ABSENT' -Encoding UTF8; exit 0 }\n"
                 "$log = { param($m) Add-Content -LiteralPath $LogFile -Value ('LOG ' + $m) -Encoding UTF8 }\n"
                 "$r = Confirm-CommitInClone -Repo $Repo -PushUrl $Url -Oid $Oid -Logger $log\n"
                 "Add-Content -LiteralPath $LogFile -Value ('RESULT ' + $r) -Encoding UTF8\n")

    def helper(repo, oid, tag):
        log = os.path.join(work, "log_%s.txt" % tag)
        r = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", harness,
                            script_dir, repo, url, oid, log], capture_output=True, creationflags=NW, timeout=600)
        text = open(log, encoding="utf-8-sig").read() if os.path.exists(log) else ""
        if r.stderr.strip():
            text += "\nPS STDERR " + r.stderr.decode("utf-8", "replace")[:400]
        return text

    c = clones["C"]
    before = packs(c)
    text = helper(c, x, "C")
    print("C: " + " / ".join(text.split("\n"))[:500])
    if "ABSENT" in text:
        print("C, D: ABSENT (this script dir has no Confirm-CommitInClone)")
        checks.append(("C helper present", False))
    else:
        new = new_packs(before, packs(c))
        size = sum(v[0] for v in new.values())
        print("C: new packs %d, %d bytes, single-id packs %d" % (len(new), size, len(single_id(new, x))))
        checks.append(("C0 script parses", "PARSE_ERRORS 0" in text))
        checks.append(("C1 helper returns True", "RESULT True" in text))
        checks.append(("C2 helper logged the fetch", "fetched the advertised main" in text))
        checks.append(("C3 X is in the clone", have(c, x)))
        checks.append(("C4 no single-id promisor pack", len(single_id(new, x)) == 0))
        # a small fetch lands as loose objects (under fetch.unpackLimit), so 0 new pack bytes is the usual answer
        checks.append(("C5 the fetch is small (under 20 pct of the clone's packs)", size < 0.2 * full))
        before = packs(c)
        rc, out = git(c, "rev-list", "--count", x + "..HEAD", ok=False)
        checks.append(("C6 plain probe now answers 1", rc == 0 and out == "1"))
        checks.append(("C7 and downloads nothing", len(new_packs(before, packs(c))) == 0))
        text2 = helper(c, x, "C2")
        checks.append(("C8 second call returns True without a fetch", "RESULT True" in text2 and "fetched" not in text2))
        d = clones["D"]
        before = packs(d)
        text = helper(d, "0123456789abcdef0123456789abcdef01234567", "D")
        print("D: " + " / ".join(text.split("\n"))[:400])
        checks.append(("D1 unknown id returns False", "RESULT False" in text))
        checks.append(("D2 says so", "still not in this clone" in text))
        checks.append(("D3 no single-id pack for it", len(single_id(new_packs(before, packs(d)), "0123456789abcdef0123456789abcdef01234567")) == 0))
    bad = [n for n, okk in checks if not okk]
    for n, okk in checks:
        print("%-72s %s" % (n, "ok" if okk else "FAIL"))
    print("%d of %d checks pass" % (len(checks) - len(bad), len(checks)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
