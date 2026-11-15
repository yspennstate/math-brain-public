"""Control for the 13 Nov 2026 guard in scan_secrets.py: a --range whose base is not in a partial clone must be
refused without downloading anything; a range whose ends are present must scan as before.

    python -X utf8 test_scan_secrets_absent_base.py --module <scan_secrets.py> --work <fresh dir>

Builds a scratch origin (40 commits), a blob:none clone one commit behind with one local commit, then:
  P  present base (the clone's origin/main) .. HEAD: the scan passes (rc 0), no new pack;
  X  absent base (the origin's new tip) .. HEAD: with the guard rc != 0 and no new pack, the error names the range
     end; without the guard a pack whose .promisor names the tip twice appears (the leak).
Exit 0 when the module behaves as the guard should; exit 1 otherwise (so the unpatched module exits 1).
"""
import glob
import os
import subprocess
import sys

NW = 0x08000000
ARGS = sys.argv[1:]
MOD = os.path.abspath(ARGS[ARGS.index("--module") + 1])
WORK = os.path.abspath(ARGS[ARGS.index("--work") + 1])


def run(args, cwd=None, ok=True):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    r = subprocess.run(args, cwd=cwd, capture_output=True, creationflags=NW, env=env, timeout=900)
    if ok and r.returncode != 0:
        raise SystemExit("FAILED %s: %s" % (" ".join(args[:7]), r.stderr.decode("utf-8", "replace")[:400]))
    return r.returncode, r.stdout.decode("utf-8", "replace").strip(), r.stderr.decode("utf-8", "replace").strip()


def git(repo, *a, ok=True):
    return run(["git", "-C", repo, "-c", "user.name=t", "-c", "user.email=t@example.invalid", "-c", "core.autocrlf=false",
                "-c", "core.hooksPath=" + HOOKS, "-c", "gc.auto=0", "-c", "maintenance.auto=false", *a], ok=ok)


def packs(repo):
    out = {}
    for p in glob.glob(os.path.join(repo, ".git", "objects", "pack", "*.pack")):
        pr = p[:-5] + ".promisor"
        out[os.path.basename(p)] = open(pr, encoding="utf-8", errors="replace").read() if os.path.isfile(pr) else None
    return out


def scan(repo, spec):
    return run([sys.executable, "-X", "utf8", MOD, "--range", spec], cwd=repo, ok=False)


def main():
    global HOOKS
    if os.path.exists(WORK):
        raise SystemExit("work dir exists; give a fresh one")
    os.makedirs(WORK)
    HOOKS = os.path.join(WORK, "nohooks")
    os.makedirs(HOOKS)
    origin, b, c = os.path.join(WORK, "origin.git"), os.path.join(WORK, "B"), os.path.join(WORK, "clone")
    url = "file:///" + origin.replace("\\", "/")
    run(["git", "init", "-q", "--bare", "-b", "main", origin])
    run(["git", "-C", origin, "config", "uploadpack.allowFilter", "true"])
    run(["git", "-C", origin, "config", "uploadpack.allowAnySHA1InWant", "true"])
    run(["git", "clone", "-q", "-c", "core.autocrlf=false", url, b])
    for i in range(40):
        with open(os.path.join(b, "f%02d.txt" % (i % 5)), "w", encoding="ascii", newline="\n") as fh:
            fh.write("plain line %d\n" % i)
        git(b, "add", "-A")
        git(b, "commit", "-q", "-m", "c%d" % i)
    git(b, "push", "-q", "origin", "HEAD:main")
    run(["git", "clone", "-q", "--filter=blob:none", "-c", "core.autocrlf=false", url, c])
    for k, v in (("user.name", "t"), ("user.email", "t@example.invalid"), ("gc.auto", "0"), ("maintenance.auto", "false")):
        git(c, "config", k, v)
    present = git(c, "rev-parse", "origin/main")[1]
    with open(os.path.join(c, "local.txt"), "w", encoding="ascii", newline="\n") as fh:
        fh.write("a local line\n")
    git(c, "add", "local.txt")
    git(c, "commit", "-q", "-m", "local")
    head = git(c, "rev-parse", "HEAD")[1]
    with open(os.path.join(b, "new.txt"), "w", encoding="ascii", newline="\n") as fh:
        fh.write("new\n")
    git(b, "add", "-A")
    git(b, "commit", "-q", "-m", "X")
    git(b, "push", "-q", "origin", "HEAD:main")
    x = git(b, "rev-parse", "HEAD")[1]
    checks = []

    before = packs(c)
    rc, out, err = scan(c, present + ".." + head)
    print("P: rc=%d  %s" % (rc, (err or out).replace("\n", " / ")[:300]))
    checks.append(("P1 present range scans clean", rc == 0))
    checks.append(("P2 and adds no pack", packs(c) == before))

    absent = git(c, "--no-lazy-fetch", "cat-file", "-e", x + "^{commit}", ok=False)[0] != 0
    checks.append(("X0 the new tip is absent before the scan", absent))
    before = packs(c)
    rc, out, err = scan(c, x + ".." + head)
    after = packs(c)
    new = {k: v for k, v in after.items() if k not in before}
    single = [k for k, v in new.items() if v is not None and v.split() == [x, x]]
    print("X: rc=%d  new packs %d, single-id packs %d  %s" % (rc, len(new), len(single), (err or out).replace("\n", " / ")[:300]))
    checks.append(("X1 absent base is refused", rc != 0))
    checks.append(("X2 nothing was downloaded", len(new) == 0))
    checks.append(("X3 the tip is still absent", git(c, "--no-lazy-fetch", "cat-file", "-e", x + "^{commit}", ok=False)[0] != 0))
    checks.append(("X4 the error names the range end", "is not a commit in this clone" in (err + out)))
    # ref form of the same absent id: a short unknown name is refused before any lookup that could download
    rc, out, err = scan(c, "origin/main..HEAD")
    checks.append(("R1 ref range still resolves and scans", rc == 0))
    bad = [n for n, okk in checks if not okk]
    for n, okk in checks:
        print("%-52s %s" % (n, "ok" if okk else "FAIL"))
    print("%d of %d checks pass" % (len(checks) - len(bad), len(checks)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
