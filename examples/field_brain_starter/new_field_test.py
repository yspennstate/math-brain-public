"""Check that new_field.py makes a clean, working, empty brain and leaves the starter alone.

    new brain           exit 0 and the store checks clean
    nothing of the studio's   no records, an index and a mistakes file with no entries, an empty questions.json,
                        no dream agenda, no hook or dream test that needs the studio's records
    scripts             every script copied byte for byte
    first record        new_record.py files a record, check_store.py is clean, recall.py finds it
    first lesson        the scar hook warns before a command that repeats that feedback record, and not otherwise
    refusals            a folder that is not empty, and a folder inside the starter, are refused
    the starter         not touched

Runs in a scratch folder. Exit 0 when every step behaves, 1 otherwise.

    python3 new_field_test.py
"""
import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = ["recall.py", "new_record.py", "check_store.py", "claims.py", "ledger.py", "three_arm.py",
           "agents_test.py", "dream/make_agenda.py", "dream/run_dream.py", "dream/dream_night.py",
           "hooks/wake_hook.py", "hooks/recall_hook.py", "hooks/scar_hook.py", "hooks/write_back_hook.py",
           "hooks/request_hook.py"]


def tree_hash(folder):
    h = hashlib.sha256()
    for path in sorted(glob.glob(os.path.join(folder, "**", "*"), recursive=True)):
        if os.path.isfile(path) and "__pycache__" not in path:
            h.update(os.path.relpath(path, folder).encode())
            with open(path, "rb") as fh:
                h.update(fh.read())
    return h.hexdigest()


def run(*args, cwd=None):
    res = subprocess.run([sys.executable] + list(args), capture_output=True, text=True, encoding="utf-8",
                         errors="replace", cwd=cwd, timeout=300, env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return res.returncode, (res.stdout + res.stderr).strip()


def same_bytes(a, b):
    with open(a, "rb") as fa, open(b, "rb") as fb:
        return fa.read() == fb.read()


def main():
    before = tree_hash(HERE)
    work = tempfile.mkdtemp(prefix="new_field_")
    dest = os.path.join(work, "bakery_brain")
    results = []

    def check(step, ok, said=""):
        results.append(ok)
        print("%s  %s" % ("ok  " if ok else "FAIL", step))
        if not ok:
            for line in (said or "(nothing)").splitlines()[:12]:
                print("        " + line[:150])

    rc, said = run(os.path.join(HERE, "new_field.py"), dest, "--field", "a chain of four bakeries")
    check("new brain: exit 0 and the store checks clean", rc == 0 and "check_store.py: clean" in said, said)

    mem = os.path.join(dest, "memory")
    files = sorted(os.listdir(mem)) if os.path.isdir(mem) else []
    index = open(os.path.join(mem, "MEMORY.md"), encoding="utf-8").read() if "MEMORY.md" in files else ""
    mistakes = open(os.path.join(mem, "MISTAKES.md"), encoding="utf-8").read() if "MISTAKES.md" in files else ""
    questions = json.load(open(os.path.join(dest, "questions.json"), encoding="utf-8"))
    left_out = ["dream/DREAM_AGENDA.md", "hooks/session_test.py", "dream/dream_test.py", "new_field.py"]
    check("nothing of the studio's: no records, empty index, mistakes and questions, no studio-bound tests",
          files == ["MEMORY.md", "MISTAKES.md"] and "\n- " not in index and "\n- " not in mistakes
          and questions == [] and not any(os.path.exists(os.path.join(dest, p)) for p in left_out)
          and "four bakeries" in open(os.path.join(dest, "README.md"), encoding="utf-8").read(),
          "memory/: %s\nquestions: %s" % (files, questions))

    missing = [s for s in SCRIPTS if not os.path.exists(os.path.join(dest, s))
               or not same_bytes(os.path.join(HERE, s), os.path.join(dest, s))]
    check("scripts: every script copied byte for byte", not missing, "missing or changed: %s" % missing)

    rc1, s1 = run("new_record.py", "feedback", "Refunds over two hundred need a manager's yes",
                  "--why", "A clerk refunded a delivered wedding cake in full.",
                  "--apply", "Ask a manager before any refund over two hundred.", "--date", "2026-05-01", cwd=dest)
    rc2, s2 = run("check_store.py", cwd=dest)
    rc3, s3 = run("recall.py", "refund manager approval", cwd=dest)
    check("first record: filed, the store checks clean, recall finds it",
          rc1 == 0 and rc2 == 0 and rc3 == 0 and "refunds_over_two_hundred" in s3, "\n".join([s1, s2, s3]))

    def scar(command):
        event = json.dumps({"session_id": "t", "tool_name": "Bash", "tool_input": {"command": command}})
        res = subprocess.run([sys.executable, os.path.join("hooks", "scar_hook.py")], input=event, capture_output=True,
                             text=True, encoding="utf-8", errors="replace", cwd=dest, timeout=120)
        return res.stdout
    warned = scar("python refund.py --order 4411 --amount 350 full refund, no manager")
    quiet = scar("ls -la invoices")
    check("first lesson: the scar hook warns on a command that repeats it, and stays quiet otherwise",
          "refunds_over_two_hundred" in warned and quiet.strip() == "", "warned: %r\nquiet: %r" % (warned, quiet))

    rc1, s1 = run(os.path.join(HERE, "new_field.py"), dest)
    rc2, s2 = run(os.path.join(HERE, "new_field.py"), os.path.join(HERE, "inside"))
    check("refusals: a folder that is not empty, and a folder inside the starter",
          rc1 != 0 and rc2 != 0 and not os.path.exists(os.path.join(HERE, "inside")), "\n".join([s1, s2]))

    check("the starter was not touched", tree_hash(HERE) == before)
    shutil.rmtree(work, ignore_errors=True)
    bad = results.count(False)
    print("%d of %d steps behave" % (len(results) - bad, len(results)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
