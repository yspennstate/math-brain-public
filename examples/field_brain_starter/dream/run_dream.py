"""Run one dream over the starter brain with any agent command-line tool, on Linux, macOS or Windows.

    python dream/run_dream.py --write-prompt dream/prompt.md          # build the agenda and the prompt, run nothing
    python dream/run_dream.py --agent-cmd "claude -p --permission-mode acceptEdits"
    python dream/run_dream.py --agent-cmd "codex exec --full-auto -"

The agent command receives the prompt on stdin and runs with this folder as its working directory, so it can read
and edit memory/. Any tool that takes a prompt on stdin and can edit files works.

One run does five things:
1. builds dream/DREAM_AGENDA.md with make_agenda.py and counts the items in each section;
2. copies memory/ to dream/backups/<stamp>/ so a person can undo the night;
3. hands the agent the agenda and the three dream rules;
4. checks that no record was deleted (a deleted record is put back from the copy and the log says so);
5. rebuilds the agenda and writes dream/logs/dream_<stamp>.md: the agent's reply, the files it changed, and each
   section's count before and after.

A section whose count falls is work done. A section that comes back the same means the agent read but did not
write. Standard library only.
"""
import argparse
import datetime as dt
import filecmp
import os
import re
import shlex
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MEM = os.path.join(ROOT, "memory")
AGENDA = os.path.join(HERE, "DREAM_AGENDA.md")
LOCK = os.path.join(HERE, ".dream.lock")

RULES = """You are running tonight's dream for the brain in this folder. The records are in memory/, one fact per
file; memory/MEMORY.md is the index and memory/MISTAKES.md the dated corrections. The agenda below says what to work on.

1. Work through the agenda's sections in order. Do not invent work the agenda does not list.
2. Every change is a new line or a new record with a date and a reason. Never delete a record or an index line; mark a
   wrong record superseded_by: the record that corrects it. Use new_record.py to write a new record and its index line.
3. When a mistake has no rule for next time, write one: one sentence that names the situation and the check to run,
   on a "**How to apply:**" line in the record the mistake links.

Leave a record's status as it is unless you have the evidence in front of you. When you finish, reply with one line
per change: the file, what changed and why.

"""


def build_agenda():
    subprocess.run([sys.executable, os.path.join(HERE, "make_agenda.py")], cwd=ROOT, check=True,
                   capture_output=True, text=True)
    return open(AGENDA, encoding="utf-8").read()


def section_counts(agenda):
    counts, name = {}, None
    for line in agenda.splitlines():
        if line.startswith("## "):
            name = line[3:].strip()
            counts[name] = 0
        elif name and line.startswith("- "):
            counts[name] += 1
    return counts


def no_rule_count(agenda):
    return len(re.findall(r"NO rule for next time", agenda))


def changed_files(before, after):
    cmp = filecmp.dircmp(before, after)
    out = []

    def walk(c, rel):
        out.extend(("changed", os.path.join(rel, f)) for f in c.diff_files)
        out.extend(("added", os.path.join(rel, f)) for f in c.right_only)
        out.extend(("removed", os.path.join(rel, f)) for f in c.left_only)
        for d, sub in c.subdirs.items():
            walk(sub, os.path.join(rel, d))
    walk(cmp, "")
    return sorted(out, key=lambda t: t[1])


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--agent-cmd", help="agent CLI that reads the prompt on stdin, e.g. \"claude -p\"")
    ap.add_argument("--write-prompt", metavar="FILE", help="write the prompt to FILE and run nothing")
    ap.add_argument("--timeout", type=int, default=3600, help="seconds the agent may run (default 3600)")
    a = ap.parse_args()
    if not (a.agent_cmd or a.write_prompt):
        ap.error("give --agent-cmd CMD or --write-prompt FILE")

    agenda = build_agenda()
    prompt = RULES + agenda
    if a.write_prompt:
        open(a.write_prompt, "w", encoding="utf-8", newline="\n").write(prompt)
        print("wrote %s (%d characters); sections: %s" % (a.write_prompt, len(prompt), section_counts(agenda)))
        return 0

    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
    except FileExistsError:
        print("another dream holds %s; if no dream is running, delete the file and run again" % LOCK)
        return 3
    try:
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = os.path.join(HERE, "backups", stamp)
        shutil.copytree(MEM, backup)
        before = section_counts(agenda)
        try:
            res = subprocess.run(shlex.split(a.agent_cmd), input=prompt, cwd=ROOT, capture_output=True, text=True,
                                 encoding="utf-8", errors="replace", timeout=a.timeout)
            reply, rc = res.stdout.strip(), res.returncode
        except subprocess.TimeoutExpired:
            reply, rc = "(the agent ran past %d s and was stopped)" % a.timeout, None

        changes = changed_files(backup, MEM)
        restored = []
        for kind, rel in changes:
            if kind == "removed":
                src, dst = os.path.join(backup, rel), os.path.join(MEM, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, dst)
                restored.append(rel)

        agenda2 = build_agenda()
        after = section_counts(agenda2)
        log = ["# Dream %s" % stamp, "",
               "Agent: `%s` (exit %s). Backup of memory/: `dream/backups/%s/`." % (a.agent_cmd, rc, stamp), "",
               "| section | before | after |", "|---|---|---|"]
        log += ["| %s | %d | %d |" % (k, before.get(k, 0), after.get(k, 0)) for k in before]
        log += ["", "Mistakes with no rule for next time: %d before, %d after." % (no_rule_count(agenda),
                                                                                 no_rule_count(agenda2)), ""]
        log += ["## Files the agent changed", ""] + (["- %s %s" % c for c in changes] or ["- none"])
        if restored:
            log += ["", "## Records the agent deleted, put back from the backup", ""] + ["- " + r for r in restored]
        log += ["", "## The agent's reply", "", reply or "(empty)", ""]
        os.makedirs(os.path.join(HERE, "logs"), exist_ok=True)
        path = os.path.join(HERE, "logs", "dream_%s.md" % stamp)
        open(path, "w", encoding="utf-8", newline="\n").write("\n".join(log))
        print("dream done: %d file(s) changed, %d put back; log %s" % (len(changes), len(restored), path))
        return 0 if rc == 0 else 1
    finally:
        os.remove(LOCK)


if __name__ == "__main__":
    sys.exit(main())
