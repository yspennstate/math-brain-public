"""Controls for the 13 Nov 2026 fix: a commit made in the shared checkout while the dream's sync runs must stay on main.

    python -X utf8 test_dream_sync_late_commits.py <dir holding dream_git_sync.ps1 and its helpers> <work dir> <case>

Builds a scratch origin, a checkout A with one local commit (L1) and one incoming commit (U), runs
Sync-LocalMainToAdvertised from the given script dir, and makes something happen in A in the middle of the sync:

  replay_window   a commit lands right after the replay finished (the 06:21 case of 13 Nov): it must be on main after
  prep_disjoint   a commit on a file that is not incoming lands just before the move: carried over, the move is made
  prep_clash      a commit on an incoming file lands just before the move: the move is not tried, nothing is lost
  prep_edit       an uncommitted edit to an incoming tracked file is made just before the move: refused, edit kept
  scene_0621      a commit lands after the replay and the same file is then edited again without a commit

Exit 0 only when every check of the case passes.
"""
import os
import shutil
import subprocess
import sys

NW = 0x08000000
V1, V2 = b"one\n", b"two\n"
LATE, EDIT = b"late, local\n", b"an edit nobody committed\n"


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


def blob(repo, rev, rel):
    r = subprocess.run(["git", "-C", repo, "cat-file", "blob", rev + ":" + rel], capture_output=True, creationflags=NW)
    return r.stdout if r.returncode == 0 else None


HARNESS = r'''param($ScriptDir, $Repo, $Url, $Oid, $LogFile, $Case, $Hooks)
$tok = $null; $err = $null
[void][System.Management.Automation.Language.Parser]::ParseFile((Join-Path $ScriptDir 'dream_git_sync.ps1'), [ref]$tok, [ref]$err)
Add-Content -LiteralPath $LogFile -Value ('PARSE_ERRORS ' + @($err).Count) -Encoding UTF8
. (Join-Path $ScriptDir 'dream_git_sync.ps1')
$script:injected = $false
function Write-Late([string] $rel, [string] $text, [bool] $commit) {
    $p = Join-Path $Repo $rel
    if ($commit) {
        [System.IO.File]::WriteAllText($p, $text)
        & git -C $Repo -c core.autocrlf=false -c core.hooksPath=$Hooks add -- $rel 2>&1 | Out-Null
        & git -C $Repo -c user.name=t -c user.email=t@example.invalid -c core.autocrlf=false -c core.hooksPath=$Hooks commit -q -m ("late " + $rel) -- $rel 2>&1 | Out-Null
        Add-Content -LiteralPath $LogFile -Value ('INJECT commit ' + $rel + ' rc ' + $LASTEXITCODE) -Encoding UTF8
    } else {
        [System.IO.File]::AppendAllText($p, $text)
        Add-Content -LiteralPath $LogFile -Value ('INJECT edit ' + $rel) -Encoding UTF8
    }
}
$origAbsent = ${function:Set-IndexAbsentToTarget}
function Set-IndexAbsentToTarget {
    param([string] $Repo, [string] $Old, [string] $Target)
    $r = & $origAbsent -Repo $Repo -Old $Old -Target $Target
    if (-not $script:injected) {
        if ($Case -eq 'prep_disjoint') { $script:injected = $true; Write-Late 'data/late.txt' "late, local`n" $true }
        elseif ($Case -eq 'prep_clash') { $script:injected = $true; Write-Late 'data/shared.txt' "late, local`n" $true }
        elseif ($Case -eq 'prep_edit') { $script:injected = $true; Write-Late 'data/x.txt' "an edit nobody committed`n" $false }
    }
    return $r
}
$log = {
    param($m)
    Add-Content -LiteralPath $LogFile -Value ('LOG ' + $m) -Encoding UTF8
    if (-not $script:injected -and "$m" -like '*replayed * local commit(s) onto the advertised main*') {
        if ($Case -eq 'replay_window') { $script:injected = $true; Write-Late 'data/late.txt' "late, local`n" $true }
        elseif ($Case -eq 'scene_0621') {
            $script:injected = $true
            Write-Late 'data/a.txt' "late, local`n" $true
            Write-Late 'data/a.txt' "an edit nobody committed`n" $false
        }
    }
}
$r = Sync-LocalMainToAdvertised -Repo $Repo -PushUrl $Url -Oid $Oid -Logger $log
Add-Content -LiteralPath $LogFile -Value ('RESULT ' + $r) -Encoding UTF8
'''


def main():
    global HOOKS
    script_dir, work, case = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2]), sys.argv[3]
    if os.path.isdir(work):
        shutil.rmtree(work, ignore_errors=True)
    os.makedirs(work)
    HOOKS = os.path.join(work, "nohooks")
    os.makedirs(HOOKS)
    origin, a, b = (os.path.join(work, n) for n in ("origin.git", "A", "B"))
    run(["git", "init", "-q", "--bare", "-b", "main", origin])
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", origin, b])
    for n in ("shared", "x", "a"):
        put(b, "data/%s.txt" % n, V1)
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "c0")
    git(b, "push", "-q", "origin", "HEAD:main")
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", origin, a])
    git(a, "config", "core.autocrlf", "false")
    git(a, "config", "user.name", "t")
    git(a, "config", "user.email", "t@example.invalid")
    put(a, "data/l1.txt", V1)
    git(a, "add", "--", "data/l1.txt")
    git(a, "commit", "-q", "-m", "L1", "--", "data/l1.txt")
    l1 = git(a, "rev-parse", "HEAD").strip()
    for n in ("shared", "x", "u"):
        put(b, "data/%s.txt" % n, V2)
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "U")
    git(b, "push", "-q", "origin", "HEAD:main")
    u = git(b, "rev-parse", "HEAD").strip()

    log = os.path.join(work, "sync.log")
    harness = os.path.join(work, "harness.ps1")
    with open(harness, "w", encoding="ascii", newline="\r\n") as fh:
        fh.write(HARNESS)
    r = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", harness,
                        script_dir, a, origin, u, log, case, HOOKS], capture_output=True, creationflags=NW, timeout=900)
    text = open(log, encoding="utf-8-sig").read() if os.path.exists(log) else ""
    print("\n".join(l[:330] for l in text.strip().splitlines())[:2600])
    if r.stderr.strip():
        print("PS STDERR " + r.stderr.decode("utf-8", "replace")[:600])
    head = git(a, "rev-parse", "HEAD").strip()
    over_u = git(a, "rev-list", "--count", u + "..HEAD", ok=False).strip()
    has_u = git(a, "merge-base", "--is-ancestor", u, "HEAD", ok=False) is not None and subprocess.run(
        ["git", "-C", a, "merge-base", "--is-ancestor", u, "HEAD"], creationflags=NW).returncode == 0
    subjects = git(a, "log", "--format=%s", "-n", "4").split("\n")
    status = sorted(l for l in git(a, "status", "--porcelain").splitlines() if l.strip())
    late_head = git(a, "rev-list", "-n", "1", "--grep=^late ", "--all", ok=False).strip()
    obs = {
        "parse_errors_0": "PARSE_ERRORS 0" in text,
        "injected": "INJECT " in text,
        "inject_commit_rc_0": "INJECT commit" in text and " rc 0" in text,
        "result_true": "RESULT True" in text,
        "result_false": "RESULT False" in text,
        "head_built_on_incoming": has_u,
        "two_commits_over_incoming": over_u == "2",
        "late_commit_on_main": any(s.startswith("late ") for s in subjects),
        "l1_on_main": blob(a, "HEAD", "data/l1.txt") == V1,
        "late_file_in_head": blob(a, "HEAD", "data/late.txt") == LATE,
        "late_file_on_disk": get(a, "data/late.txt") == LATE,
        # an incoming file this checkout never held (data/u.txt) is indexed without being written, by design
        "incoming_on_disk": get(a, "data/shared.txt") == V2 and get(a, "data/x.txt") == V2,
        "status_clean": status == [],
        "said_replaying": "were made here while the sync was replaying" in text,
        "said_preparing_carried": "were made here while the move was being prepared" in text and "none on an incoming file" in text,
        "said_not_tried": "so the move was not tried" in text or "nothing in the checkout was changed" in text,
        "refused_logged": "moving the checkout was refused" in text,
        "head_is_late_commit": late_head != "" and head == late_head,
        "head_is_l1": head == l1,
        "shared_keeps_late_bytes": get(a, "data/shared.txt") == LATE and blob(a, "HEAD", "data/shared.txt") == LATE,
        "x_keeps_the_edit": get(a, "data/x.txt") == V1 + EDIT,
        "a_in_head_is_late": blob(a, "HEAD", "data/a.txt") == LATE,
        "a_on_disk_keeps_the_edit": get(a, "data/a.txt") == LATE + EDIT,
        "status_only_a_modified": status == [" M data/a.txt"],
        "status_only_x_modified": status == [" M data/x.txt"],
    }
    moved = ["parse_errors_0", "inject_commit_rc_0", "result_true", "head_built_on_incoming", "two_commits_over_incoming",
             "late_commit_on_main", "l1_on_main", "incoming_on_disk"]
    want = {
        "replay_window": moved + ["late_file_in_head", "late_file_on_disk", "status_clean", "said_replaying"],
        "prep_disjoint": moved + ["late_file_in_head", "late_file_on_disk", "status_clean", "said_preparing_carried"],
        "prep_clash": ["parse_errors_0", "inject_commit_rc_0", "result_false", "said_not_tried", "head_is_late_commit",
                       "shared_keeps_late_bytes", "l1_on_main", "status_clean"],
        "prep_edit": ["parse_errors_0", "injected", "result_false", "refused_logged", "head_is_l1", "x_keeps_the_edit",
                      "status_only_x_modified"],
        "scene_0621": moved + ["a_in_head_is_late", "a_on_disk_keeps_the_edit", "status_only_a_modified", "said_replaying"],
    }[case]
    bad = [k for k in want if not obs[k]]
    for k in want:
        print("%-28s %s" % (k, "ok" if obs[k] else "FAIL"))
    print("head %s, %s commit(s) over incoming, subjects %r, status %r" % (head[:10], over_u, subjects[:3], status))
    print("%s: %d of %d checks pass" % (case, len(want) - len(bad), len(want)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
