"""Start several agents at the same moment against one brain and check that they do not overwrite each other.

claims.py and new_record.py are written for agents that run at once, and their selftests call the functions one
after another in a single process. Races only show up between processes, so this test starts real ones: each agent
is its own Python process, they all wait on a start line, and they go together. The steps:

    one claim, eight agents     exactly one gets topic:pricing; the other seven exit 3 and each names the winner
    release                     after the winner releases, the next agent to ask gets it
    a crashed agent             a claim nobody renews runs out and the next agent takes it over
    eight records at once       eight agents file a record each through new_record.py: eight files, eight index
                                lines, no lock left behind, and check_store.py finds nothing wrong
    a crashed writer            an index lock left by a writer that died is cleared by the next one

Everything runs on a scratch copy of memory/ and a scratch claims folder, so the real store is not touched. Exit 0
when every step behaves, 1 otherwise.

    python3 agents_test.py           # add -v to print what each agent said
"""
import glob
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
VERBOSE = "-v" in sys.argv[1:]
AGENTS = 8

# Each agent process announces that it has started, waits for the start line, then runs its command. Python takes a
# moment to start, so without the wait the first agent would finish before the last one began and nothing would race.
WAIT_THEN_RUN = r'''
import os, subprocess, sys, time
ready, go = sys.argv[1], sys.argv[2]
open(ready, "w").close()
end = time.time() + 120
while not os.path.exists(go) and time.time() < end:
    time.sleep(0.005)
res = subprocess.run(sys.argv[3:], capture_output=True, text=True, encoding="utf-8", errors="replace")
sys.stdout.write(res.stdout + res.stderr)
sys.exit(res.returncode)
'''


def tree_hash(folder):
    h = hashlib.sha256()
    for path in sorted(glob.glob(os.path.join(folder, "**", "*"), recursive=True)):
        if os.path.isfile(path):
            h.update(os.path.relpath(path, folder).encode())
            with open(path, "rb") as fh:
                h.update(fh.read())
    return h.hexdigest()


def main():
    real_before = tree_hash(os.path.join(HERE, "memory"))
    work = tempfile.mkdtemp(prefix="brain_agents_")
    mem = os.path.join(work, "memory")
    shutil.copytree(os.path.join(HERE, "memory"), mem)
    claims_dir = os.path.join(work, "claims")
    runner = os.path.join(work, "wait_then_run.py")
    with open(runner, "w", encoding="utf-8") as fh:
        fh.write(WAIT_THEN_RUN)
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    results = []

    def check(step, ok, said):
        results.append(ok)
        print("%s  %s" % ("ok  " if ok else "FAIL", step))
        if VERBOSE or not ok:
            for line in (said or "(nothing)").splitlines()[:12]:
                print("        " + line[:150])

    def tool(script, *args):
        return [sys.executable, os.path.join(HERE, script)] + list(args)

    def together(commands):
        """Start every command as its own process, release them at once, and return [(exit code, output)]."""
        go = os.path.join(work, "go_%d" % time.time_ns())
        procs = []
        for i, cmd in enumerate(commands):
            ready = "%s_ready_%d" % (go, i)
            procs.append((ready, subprocess.Popen([sys.executable, runner, ready, go] + cmd, env=env,
                                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)))
        end = time.time() + 120
        while not all(os.path.exists(r) for r, _ in procs) and time.time() < end:
            time.sleep(0.01)
        open(go, "w").close()
        out = []
        for _, p in procs:
            text = p.communicate(timeout=300)[0].decode("utf-8", "replace").strip()
            out.append((p.returncode, text))
        return out

    def once(script, *args):
        res = subprocess.run(tool(script, *args), capture_output=True, text=True, encoding="utf-8",
                             errors="replace", env=env, timeout=120)
        return res.returncode, (res.stdout + res.stderr).strip()

    # One claim, eight agents.
    names = ["agent%d" % i for i in range(AGENTS)]
    got = together([tool("claims.py", "claim", "--dir", claims_dir, "--agent", n, "--resource", "topic:pricing",
                         "--purpose", "move the ship date") for n in names])
    winners = [n for n, (rc, _) in zip(names, got) if rc == 0]
    refused = [(n, text) for n, (rc, text) in zip(names, got) if rc == 3]
    said = "\n".join("%s exit %s: %s" % (n, rc, text) for n, (rc, text) in zip(names, got))
    check("one claim, %d agents: exactly one wins, the rest are refused and told who holds it" % AGENTS,
          len(winners) == 1 and len(refused) == AGENTS - 1
          and all(("held by %s" % winners[0]) in text for _, text in refused), said)

    # Release, and the next agent gets it.
    winner = winners[0] if winners else names[0]
    loser = next((n for n in names if n != winner), names[1])
    rc1, s1 = once("claims.py", "release", "--dir", claims_dir, "--agent", loser, "--resource", "topic:pricing")
    rc2, s2 = once("claims.py", "release", "--dir", claims_dir, "--agent", winner, "--resource", "topic:pricing")
    rc3, s3 = once("claims.py", "claim", "--dir", claims_dir, "--agent", loser, "--resource", "topic:pricing")
    check("release: only the holder can release, and then the next agent gets it",
          rc1 == 3 and rc2 == 0 and rc3 == 0, "\n".join([s1, s2, s3]))

    # A crashed agent: a claim of a few seconds that nobody renews.
    once("claims.py", "claim", "--dir", claims_dir, "--agent", "crashed", "--resource", "record:refund_rule",
         "--minutes", "0.03")
    rc1, s1 = once("claims.py", "claim", "--dir", claims_dir, "--agent", "next", "--resource", "record:refund_rule")
    time.sleep(2.5)
    rc2, s2 = once("claims.py", "claim", "--dir", claims_dir, "--agent", "next", "--resource", "record:refund_rule")
    check("a crashed agent: its claim holds until it runs out, then the next agent takes it over",
          rc1 == 3 and rc2 == 0, "\n".join([s1, s2]))

    # Eight records at once.
    index = os.path.join(mem, "MEMORY.md")
    lines_before = open(index, encoding="utf-8").read().count("\n- ")
    files_before = set(os.listdir(mem))
    got = together([tool("new_record.py", "feedback", "Agent %d found a cue with no licence at rough cut" % i,
                         "--why", "Agent %d hit it on the harbour film." % i,
                         "--apply", "List every cue and its licence before the edit locks.",
                         "--dir", mem, "--date", "2026-04-01") for i in range(AGENTS)])
    new_files = sorted(set(os.listdir(mem)) - files_before)
    text = open(index, encoding="utf-8").read()
    indexed = [f for f in new_files if "](%s)" % f in text]
    said = "\n".join("exit %s: %s" % (rc, t) for rc, t in got)
    check("%d records at once: every file written and every index line kept" % AGENTS,
          all(rc == 0 for rc, _ in got) and len(new_files) == AGENTS and len(indexed) == AGENTS
          and text.count("\n- ") == lines_before + AGENTS, said)
    rc, s = once("check_store.py", "--dir", mem)
    check("%d records at once: no index lock left and the store checks clean" % AGENTS,
          rc == 0 and not os.path.exists(os.path.join(mem, ".index.lock")), s)

    # A crashed writer: a lock two minutes old.
    lock = os.path.join(mem, ".index.lock")
    open(lock, "w").close()
    old = time.time() - 120
    os.utime(lock, (old, old))
    rc, s = once("new_record.py", "project", "The April interviews move to the lighthouse keeper's cottage",
                 "--dir", mem, "--date", "2026-04-02")
    check("a crashed writer: its stale index lock is cleared and the record is filed",
          rc == 0 and not os.path.exists(lock) and "lighthouse_keeper" in open(index, encoding="utf-8").read(), s)

    check("the real memory/ was not touched", tree_hash(os.path.join(HERE, "memory")) == real_before, "")
    shutil.rmtree(work, ignore_errors=True)
    bad = results.count(False)
    print("%d of %d steps behave" % (len(results) - bad, len(results)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
