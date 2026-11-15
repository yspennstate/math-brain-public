"""Controls for scan_secrets.py --range written as refs (origin/main..HEAD).

Builds a throwaway repository with a clean commit and a commit holding a fake
GitHub token, then checks both directions: ref and full-ID ranges over clean
history pass, the planted token is still caught through either form, and
malformed sides are refused.

  python test_scan_secrets_refrange.py [--module path/to/scan_secrets.py]
"""
import os
import random
import shutil
import string
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ARGS = sys.argv[1:]
MOD = os.path.abspath(ARGS[ARGS.index("--module") + 1]) if "--module" in ARGS else os.path.join(HERE, "scan_secrets.py")


def git(repo, *a):
    return subprocess.run(["git", *a], cwd=repo, capture_output=True, text=True, check=True).stdout.strip()


def main():
    repo = tempfile.mkdtemp(prefix="scan_refrange_")
    try:
        git(repo, "init", "-q", "-b", "main", ".")
        git(repo, "config", "user.email", "t@t")
        git(repo, "config", "user.name", "t")
        with open(os.path.join(repo, "a.txt"), "w") as f:
            f.write("a\n")
        git(repo, "add", "a.txt")
        git(repo, "commit", "-qm", "one")
        git(repo, "branch", "base")
        with open(os.path.join(repo, "a.txt"), "a") as f:
            f.write("b\n")
        git(repo, "commit", "-qam", "two")
        git(repo, "branch", "clean")
        r = random.Random(7)
        token = "ghp_" + "".join(r.choice(string.ascii_letters + string.digits) for _ in range(36))
        with open(os.path.join(repo, "cfg.txt"), "w") as f:
            f.write("token = %s\n" % token)
        git(repo, "add", "cfg.txt")
        git(repo, "commit", "-qm", "three")
        b, c, h = (git(repo, "rev-parse", x) for x in ("base", "clean", "HEAD"))
        cases = [
            ("refs, clean", "base..clean", 0),
            ("refs, planted token", "base..HEAD", 1),
            ("full ids, clean", "%s..%s" % (b, c), 0),
            ("full ids, planted token", "%s..%s" % (b, h), 1),
            ("unknown ref", "nosuch..HEAD", 2),
            ("three-dot", "base...HEAD", 2),
            ("option-like side", "--all..HEAD", 2),
            ("empty tip", "base..", 2),
            ("no dots", "HEAD", 2),
            ("tree, not a commit", "base..HEAD^{tree}", 2),
        ]
        failed = 0
        for name, spec, want in cases:
            p = subprocess.run([sys.executable, MOD, "--range", spec], cwd=repo, capture_output=True, text=True)
            ok = p.returncode == want
            failed += not ok
            print("%s %-26s rc=%d want=%d" % ("ok  " if ok else "FAIL", name, p.returncode, want))
        print("%s - %d controls, %d failed" % ("PASS" if not failed else "FAIL", len(cases), failed))
        return 1 if failed else 0
    finally:
        shutil.rmtree(repo, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
