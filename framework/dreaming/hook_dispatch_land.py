"""hook_dispatch_land.py - the one way to put an edited hook_dispatch.py live.

Why this exists. Every hook of every Claude session on this machine runs through hook_dispatch.py, and two things
have gone wrong when the file was replaced by hand:
  1. The edit raised in the dispatcher's own code and every hook was skipped at exit 0 (six times, 18 Sep - 10 Nov
     2026). Since 10 Nov a raise falls back to hook_dispatch.lkg.py, but a broken edit should not land at all.
  2. The replace changed the file's mtime, hook_dispatch_allow.json became older than the dispatcher, the in-process
     fast list emptied and every hook spawned its own process (17 Sep, 18 Sep, 21 Sep for 32 hours, 10 Nov for
     eleven minutes: PostToolUse 8.9 s against 0.14 s, some PreToolUse calls over 200 s).
This tool does both halves in one step and then reads the log, so neither can be forgotten.

usage (claim file:~/.claude/dreaming/hook_dispatch.py on the mesh first):
  python -s -X utf8 hook_dispatch_land.py <edited copy> --base-sha <sha256 of the live file the edit was made on>
         --resign touch --why "<why this diff cannot change what a hook does when run in-process>"
  python -s -X utf8 hook_dispatch_land.py <edited copy> --base-sha <sha> --resign none
         (the diff CAN change in-process behaviour: every hook spawns until hook_dispatch_control.py has been run)
  add --dry-run to run every check and change nothing.

What it does, in order; any failure before step 5 leaves the live file untouched:
  1. refuses unless the live file's sha256 starts with --base-sha (somebody else edited it since: rebuild the edit)
  2. compiles the edited copy
  3. runs the copy's --selftest in a scratch folder and requires exit 0 and the same output as the live file's
  4. breaks the copy the 10 Nov way (a NameError in main) and requires that the last-known-good fallback still runs
  5. backs the live file up, re-signs the fast list ahead of the replace (--resign touch), replaces the live file
     waiting out readers, and re-signs again at the real time, so the list is never older than the dispatcher
  6. waits, then reads what the log gained: any 'fatal:' naming the live file, any 'lkg: the last-known-good copy
     ran', any 'ALLOWLIST STALE' stamped with the new dispatcher time. Exit 0 only when there is none.
Exit codes: 0 landed clean; 2 refused, nothing changed; 3 landed with --resign none (hooks spawn until the control
run); 4 landed and the log shows trouble (the rollback command is printed).
"""
import argparse
import hashlib
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.join(HERE, "hook_dispatch.py")
ALLOW = os.path.join(HERE, "hook_dispatch_allow.json")
LOG = r"~\.claude\compute\hook_dispatch.log"
CREATE_NO_WINDOW = 0x08000000
BREAK_OLD = '    if not os.path.exists(ENABLED) and "--force" not in sys.argv:'
BREAK_NEW = '    _arm_deadline_gone_for_the_landing_test()\n' + BREAK_OLD
PAYLOAD = '{"hook_event_name": "PreToolUse", "tool_name": "Read", "session_id": "land-test", "note": "\u05e9\u05dc\u05d5\u05dd"}'


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def read(p):
    with open(p, "rb") as fh:
        return fh.read()


def replace_waiting(src, dst, wait_s=30.0):
    end = time.monotonic() + wait_s
    while True:
        try:
            os.replace(src, dst)
            return
        except PermissionError:
            if time.monotonic() >= end:
                raise
            time.sleep(0.05)


def log(line):
    try:
        with open(LOG, "a", encoding="utf-8") as fh:
            fh.write(time.strftime("%Y-%m-%d %H:%M:%S") + "  " + line + "\n")
    except OSError:
        pass


def run(script, args, scratch, lkg, stdin=b""):
    env = dict(os.environ)
    env.pop("HOOK_DISPATCH_IN_LKG", None)
    logp = os.path.join(scratch, "log_%d.txt" % time.time_ns())
    env.update({"HOOK_DISPATCH_LOG": logp, "HOOK_DISPATCH_LKG": lkg})
    p = subprocess.run([sys.executable, "-s", script] + list(args), input=stdin, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, env=env, timeout=900, creationflags=CREATE_NO_WINDOW)
    logged = ""
    if os.path.exists(logp):
        with open(logp, encoding="utf-8", errors="replace") as fh:
            logged = fh.read()
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace"), logged


def refuse(msg):
    print("REFUSED, nothing changed: " + msg)
    sys.exit(2)


def main():
    ap = argparse.ArgumentParser(description="land an edited hook_dispatch.py: test, replace, re-sign, read the log")
    ap.add_argument("new_copy")
    ap.add_argument("--base-sha", required=True, help="sha256 (16+ hex) of the live file the edit was made on")
    ap.add_argument("--resign", required=True, choices=["touch", "none"])
    ap.add_argument("--why", default="", help="with --resign touch: why the diff cannot change in-process behaviour")
    ap.add_argument("--settle", type=float, default=25.0, help="seconds to wait before reading the log")
    ap.add_argument("--skip-fallback-check", action="store_true",
                    help="only when main() no longer holds the line the check breaks; say so in --why")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    base = a.base_sha.strip().lower()
    if len(base) < 16:
        refuse("--base-sha needs at least 16 hex characters")
    if a.resign == "touch" and len(a.why.strip()) < 20:
        refuse("--resign touch needs --why: one sentence on why this diff cannot change what a hook does in-process")
    live_bytes, new_bytes = read(LIVE), read(a.new_copy)
    live_sha, new_sha = sha_bytes(live_bytes), sha_bytes(new_bytes)
    if not live_sha.startswith(base):
        refuse("the live dispatcher is %s, the edit was made on %s - rebuild the edit on the live file" % (live_sha[:16], base[:16]))
    if new_sha == live_sha:
        refuse("the edited copy is byte-identical to the live file")
    try:
        compile(new_bytes, LIVE, "exec")
    except SyntaxError as e:
        refuse("the edited copy does not compile: %s" % e)

    scratch = tempfile.mkdtemp(prefix="hook_dispatch_land_")
    cand_dir = os.path.join(scratch, "cand")
    os.makedirs(cand_dir)
    cand = os.path.join(cand_dir, "hook_dispatch.py")
    with open(cand, "wb") as fh:
        fh.write(new_bytes)
    none = os.path.join(scratch, "no_such_lkg.py")

    rc_new, out_new, err_new, _ = run(cand, ["--selftest"], scratch, none)
    if rc_new != 0:
        refuse("the edited copy's --selftest exits %d: %s" % (rc_new, (out_new + err_new)[-600:]))
    rc_old, out_old, _, _ = run(LIVE, ["--selftest"], scratch, none)
    same = (rc_old == rc_new and out_old == out_new)
    print("selftest: edited copy exit 0; %s" % ("same output as the live file" if same else
          "OUTPUT DIFFERS from the live file (expected only if the edit changes the selftest)"))
    if not same and a.resign == "touch":
        refuse("the selftest output changed, so the diff is not behaviour-neutral: land with --resign none and run"
               " hook_dispatch_control.py, or explain the selftest change and re-run after updating this check")

    text = new_bytes.decode("utf-8")
    if text.count(BREAK_OLD) == 1:
        eol = "\r\n" if "\r\n" in text else "\n"
        broken_dir = os.path.join(scratch, "broken")
        os.makedirs(broken_dir)
        broken = os.path.join(broken_dir, "hook_dispatch.py")
        with open(broken, "w", encoding="utf-8", newline="") as fh:
            fh.write(text.replace(BREAK_OLD, BREAK_NEW.replace("\n", eol)))
        stub = os.path.join(scratch, "stub_lkg.py")
        with open(stub, "w", encoding="utf-8") as fh:
            fh.write('import sys\ndata = sys.stdin.buffer.read()\n'
                     'sys.stdout.buffer.write(b"LKG-RAN|" + data + b"|" + " ".join(sys.argv[1:]).encode())\nsys.exit(2)\n')
        rc, out, _, logged = run(broken, ["--event", "PreToolUse", "--force"], scratch, stub, PAYLOAD.encode("utf-8"))
        want = "LKG-RAN|" + PAYLOAD + "|--event PreToolUse --force"
        if rc != 2 or out != want or "lkg: the last-known-good copy ran" not in logged:
            refuse("with this edit a raise in main() no longer reaches the last-known-good copy (exit %r, output %r)" % (rc, out[:160]))
        print("fallback: a raise in the edited copy's main() still runs the last-known-good copy, payload intact")
    elif a.skip_fallback_check:
        print("fallback: check SKIPPED on request (the line it breaks is not in main() any more)")
    else:
        refuse("cannot run the fallback check: main() no longer holds the line it breaks (%r). Update BREAK_OLD in"
               " this tool, or pass --skip-fallback-check and say why" % BREAK_OLD.strip())

    if a.dry_run:
        print("dry run: every check passed; the live file %s was not touched" % live_sha[:16])
        return 0

    # the live file may have moved while the checks ran (they take a minute on a slow box)
    if sha_bytes(read(LIVE)) != live_sha:
        refuse("the live dispatcher changed while the checks ran - start again on the new file")
    stamp = time.strftime("%Y%m%d_%H%M%S")
    bak = LIVE + ".bak_land_" + stamp
    with open(bak, "wb") as fh:
        fh.write(live_bytes)
    log_from = os.path.getsize(LOG) if os.path.exists(LOG) else 0
    tmp = LIVE + ".tmp.%d" % os.getpid()
    with open(tmp, "wb") as fh:
        fh.write(new_bytes)
    if a.resign == "touch":
        ahead = time.time() + 5.0
        os.utime(ALLOW, (ahead, ahead))          # signed ahead of the replace: never older than the dispatcher
    replace_waiting(tmp, LIVE)
    d_m = os.path.getmtime(LIVE)
    if a.resign == "touch":
        now = max(time.time(), d_m + 0.01)
        os.utime(ALLOW, (now, now))
        if os.path.getmtime(ALLOW) < d_m:
            os.utime(ALLOW, (d_m + 1.0, d_m + 1.0))
        log("land: hook_dispatch.py %s -> %s; fast list re-signed by touch: %s" % (live_sha[:16], new_sha[:16], a.why.strip()[:300]))
    else:
        log("land: hook_dispatch.py %s -> %s; fast list NOT re-signed: every hook spawns until hook_dispatch_control.py runs" % (live_sha[:16], new_sha[:16]))
    print("landed: %s -> %s; backup %s" % (live_sha[:16], sha_bytes(read(LIVE))[:16], os.path.basename(bak)))

    time.sleep(max(0.0, a.settle))
    gained = b""
    if os.path.exists(LOG):
        with open(LOG, "rb") as fh:
            fh.seek(log_from)
            gained = fh.read()
    lines = gained.split(b"\n")
    d_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(d_m)).encode()
    live_name = LIVE.encode("utf-8").lower()
    fatal = [l for l in lines if b" fatal: " in l and live_name in l.lower()]
    lkg_ran = [l for l in lines if b"lkg: the last-known-good copy ran" in l]
    stale = [l for l in lines if b"ALLOWLIST STALE" in l and b"dispatcher=" + d_stamp in l]
    done = [l for l in lines if b" hooks=" in l and b" exit=" in l]
    print("log since landing (%.0f s): %d dispatches completed, %d fatal, %d fallback runs, %d stale-list lines"
          % (a.settle, len(done), len(fatal), len(lkg_ran), len(stale)))
    rollback = ('python -s -X utf8 "%s" "%s" --base-sha %s --resign touch --why "rollback to the file that served before %s"'
                % (os.path.abspath(__file__), bak, new_sha[:16], stamp))
    trouble = bool(fatal or lkg_ran or (stale and a.resign == "touch"))
    if trouble:
        for l in (fatal + lkg_ran + stale)[:6]:
            print("   " + l[:300].decode("utf-8", "replace"))
        print("TROUBLE after landing. The last-known-good copy is serving every call that raises. Roll back with:\n  " + rollback)
        return 4
    if not done:
        print("note: no dispatch completed in the wait; read the log again before trusting this landing")
    if a.resign == "none":
        print("the fast list is stale by choice: every hook spawns its own process until\n"
              "  python -X utf8 %s\nhas been run and passes." % os.path.join(HERE, "hook_dispatch_control.py"))
        return 3
    print("clean. rollback, if ever needed:\n  " + rollback)
    return 0


if __name__ == "__main__":
    sys.exit(main())
