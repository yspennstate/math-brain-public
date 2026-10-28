"""Run the dream end to end with a stand-in agent, on a scratch copy of the starter, and check what it does.

make_agenda.py and run_dream.py are easy to read and hard to trust until they have run once: the agenda has to reach
the agent, a record the agent deletes has to come back, the log has to say what changed. A real agent costs money and
takes minutes, so this test uses a stand-in: a short Python script that reads the prompt on stdin the way an agent
CLI does, writes the rule a mistake is missing, deletes a record, and replies. The steps:

    prompt, stage file       the filing pass carries section 1 and not section 5
    prompt, stage connect    the connecting pass carries sections 5 and 6 and not section 1
    lock                     a second dream is refused (exit 3) while another holds dream/.dream.lock
    one dream                the agent's rule lands, the record it deleted is put back, the log says both,
                             the mistakes-without-a-rule count falls by one, a backup exists, the lock is gone
    timeout                  an agent that runs past --timeout is stopped and the log says so
    night                    dream_night.py takes the stages in turn and stops after two cycles that change nothing

Everything runs in a temporary copy of this folder, so the real memory/ is not touched. Exit 0 when every step
behaves, 1 otherwise.

    python3 dream/dream_test.py           # add -v to print what each step said
"""
import glob
import hashlib
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VERBOSE = "-v" in sys.argv[1:]

# The stand-in agent. It reads the prompt from stdin, as `claude -p` and `codex exec -` do, and works in the folder
# it is started in. MODE picks what it does: "work" fixes one mistake and deletes one record, "idle" writes nothing,
# "slow" sleeps past any short timeout, "once" works on its first call and idles after.
AGENT = r'''
import os, re, sys, time
mode = sys.argv[1]
prompt = sys.stdin.read()
if mode == "slow":
    time.sleep(60)
if mode == "once":
    flag = os.path.join("dream", ".agent_ran")
    if os.path.exists(flag):
        mode = "idle"
    else:
        open(flag, "w").close()
        mode = "work"
if mode == "idle":
    print("Read the agenda. Nothing to change.")
    sys.exit(0)
lines = prompt.splitlines()
slug = None
for i, line in enumerate(lines[:-1]):
    if "NO rule for next time" in lines[i + 1]:
        m = re.search(r"\[\[([a-z0-9_]+)\]\]", line)
        if m:
            slug = m.group(1)
            break
reply = []
if slug:
    with open(os.path.join("memory", slug + ".md"), "a", encoding="utf-8") as fh:
        fh.write("\n**How to apply:** before acting on a record, check whether it is superseded.\n")
    reply.append("memory/%s.md: added a How to apply line, the mistake had no rule" % slug)
else:
    m = re.search(r"`([a-z0-9_]+)`", prompt)
    if m:
        with open(os.path.join("memory", m.group(1) + ".md"), "a", encoding="utf-8") as fh:
            fh.write("\nChecked against the older records in a dream; no conflict found.\n")
        reply.append("memory/%s.md: noted the check" % m.group(1))
victim = os.environ.get("DREAM_TEST_DELETE")
if mode == "work" and victim:
    os.remove(os.path.join("memory", victim))
    reply.append("memory/%s: deleted" % victim)
print("\n".join(reply) or "nothing")
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
    real_before = tree_hash(os.path.join(ROOT, "memory"))
    work = tempfile.mkdtemp(prefix="brain_dream_")
    starter = os.path.join(work, "starter")
    shutil.copytree(ROOT, starter, ignore=shutil.ignore_patterns(
        "backups", "logs", ".state", "__pycache__", ".dream.lock", "STOP", "prompt.md", "requests.jsonl"))
    mem = os.path.join(starter, "memory")
    agent = os.path.join(work, "agent.py")
    with open(agent, "w", encoding="utf-8") as fh:
        fh.write(AGENT)
    py = shlex.quote(sys.executable.replace("\\", "/"))

    def agent_cmd(mode):
        return "%s %s %s" % (py, shlex.quote(agent.replace("\\", "/")), mode)

    def run(script, *args, env=None):
        res = subprocess.run([sys.executable, os.path.join(starter, "dream", script)] + list(args), cwd=starter,
                             capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=600,
                             env=env)
        return res.returncode, (res.stdout + res.stderr).strip()

    results = []

    def check(step, ok, said):
        results.append(ok)
        print("%s  %s" % ("ok  " if ok else "FAIL", step))
        if VERBOSE or not ok:
            for line in (said or "(nothing)").splitlines()[:10]:
                print("        " + line[:150])

    def read(path):
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()

    prompt_file = os.path.join(work, "prompt.md")
    rc, said = run("run_dream.py", "--write-prompt", prompt_file, "--stage", "file")
    text = read(prompt_file) if os.path.exists(prompt_file) else ""
    check("prompt, stage file: section 1 and not section 5", rc == 0 and "## 1." in text and "## 5." not in text,
          said)
    rc, said = run("run_dream.py", "--write-prompt", prompt_file, "--stage", "connect")
    text = read(prompt_file) if os.path.exists(prompt_file) else ""
    check("prompt, stage connect: sections 5 and 6, not section 1",
          rc == 0 and "## 5." in text and "## 6." in text and "## 1." not in text, said)

    lock = os.path.join(starter, "dream", ".dream.lock")
    open(lock, "w").close()
    before = tree_hash(mem)
    rc, said = run("run_dream.py", "--agent-cmd", agent_cmd("work"))
    check("lock: a second dream is refused and the store is unchanged", rc == 3 and tree_hash(mem) == before, said)
    os.remove(lock)

    records = sorted(f for f in os.listdir(mem) if f.endswith(".md") and f not in ("MEMORY.md", "MISTAKES.md"))
    victim = records[-1]
    victim_text = read(os.path.join(mem, victim))
    env = dict(os.environ, DREAM_TEST_DELETE=victim, PYTHONIOENCODING="utf-8")
    rc, said = run("run_dream.py", "--agent-cmd", agent_cmd("work"), env=env)
    logs = sorted(glob.glob(os.path.join(starter, "dream", "logs", "dream_*.md")))
    log = read(logs[-1]) if logs else ""
    check("one dream: exit 0 and a log", rc == 0 and bool(log), said)
    m = re.search(r"no rule for next time: (\d+) before, (\d+) after", log)
    ruled = [f for f in records if "superseded.\n" in read(os.path.join(mem, f))]
    check("one dream: the agent's rule landed and the no-rule count fell by one",
          bool(m) and int(m.group(2)) == int(m.group(1)) - 1 and len(ruled) == 1, m.group(0) if m else log)
    back = os.path.exists(os.path.join(mem, victim)) and read(os.path.join(mem, victim)) == victim_text
    check("one dream: the deleted record is back, word for word, and the log names it",
          back and "put back from the backup" in log and victim in log, log[-600:])
    backups = glob.glob(os.path.join(starter, "dream", "backups", "*"))
    check("one dream: a backup of memory/ exists and the lock is gone",
          len(backups) == 1 and os.path.exists(os.path.join(backups[0], victim)) and not os.path.exists(lock),
          "\n".join(backups))

    rc, said = run("run_dream.py", "--agent-cmd", agent_cmd("slow"), "--timeout", "3")
    logs = sorted(glob.glob(os.path.join(starter, "dream", "logs", "dream_*.md")), key=os.path.getmtime)
    check("timeout: the agent is stopped, the log says so, exit 1",
          rc == 1 and "ran past 3 s" in read(logs[-1]) and not os.path.exists(lock), said)

    rc, said = run("dream_night.py", "--agent-cmd", agent_cmd("once"), "--hours", "1", "--rest", "0",
                   "--min-cycle", "0", "--max-cycles", "5", "--idle-stop", "2", "--stages", "file,connect")
    nights = glob.glob(os.path.join(starter, "dream", "logs", "night_*.md"))
    night = read(nights[0]) if nights else ""
    rows = re.findall(r"^\| (\d+) \| (\w+) \|", night, re.M)
    check("night: stages alternate and it stops after two idle cycles",
          rc == 0 and [s for _, s in rows] == ["file", "connect", "file"]
          and "2 cycle(s) in a row changed nothing" in night, said)

    check("the real memory/ was not touched", tree_hash(os.path.join(ROOT, "memory")) == real_before, "")
    shutil.rmtree(work, ignore_errors=True)
    bad = results.count(False)
    print("%d of %d steps behave" % (len(results) - bad, len(results)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
