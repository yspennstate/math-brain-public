"""Make an empty brain for a new field from this starter.

The starter ships with twenty records from an invented documentary studio. None of the scripts knows anything about
films, so a brain for another field is the same folder with the records taken out. This script does that in one step:

    python3 new_field.py ../bakery_brain --field "a chain of four bakeries"

It copies every script, hook and dream file into the new folder, writes an empty index and an empty mistakes file,
an empty questions.json, and a short README naming the field and the first things to do. It leaves out the studio's
records, its questions, its dream agenda (make_agenda.py builds a new one from your records), the two tests that check the
hooks and the dream against the studio's records, and anything a running brain writes for itself: claims, backups, locks, the request ledger, hook state. Then it runs check_store.py on the
new store and prints what to do next.

The new folder must not exist yet, or must be empty. This folder is only read.
"""
import argparse
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Written by a brain while it runs, or specific to the studio. Everything else is copied.
SKIP_NAMES = {"claims", "backups", ".state", "__pycache__", "requests.jsonl", "STOP", "prompt.md",
              ".dream.lock", ".index.lock", "new_field.py", "new_field_test.py"}
# session_test.py and dream_test.py check the hooks and the dream against the studio's own records (the delivery
# spec, the raw-footage rule), so they stay with the starter; agents_test.py works on any store and is copied.
SKIP_PATHS = {"memory", "questions.json", "README.md", os.path.join("dream", "DREAM_AGENDA.md"),
              os.path.join("hooks", "session_test.py"), os.path.join("dream", "dream_test.py")}

INDEX = "# Memory Index\n\n"

MISTAKES = ("# Mistakes\n\n"
            "Dated corrections, newest first. The dream cycle turns a mistake that recurs into a reflex.\n\n")

README = """# A brain for {field}

Made from the field brain starter. The store is empty; the scripts are the starter's, unchanged.

## First day

1. Write the first ten records with `new_record.py`, from what the team has already paid to learn: decisions and
   who made them, the policies agents keep getting wrong, the incidents that cost the most and the check that would
   have caught each, and where the documents that matter live. One fact a record, with its reason.

       python3 new_record.py feedback "Refunds over 200 need a manager's yes" --why "..." --apply "..."

2. Put ten questions the team really asks into `questions.json`, each with the phrases a right answer contains, and
   one question the store cannot answer, marked `"absent": true`:

       [{{"id": "q01", "question": "...", "any_of": [["phrase", "or this phrase"]]}},
        {{"id": "q10", "question": "...", "any_of": [["no record", "unknown"]], "absent": true}}]

3. Run `python3 check_store.py`, then `python3 three_arm.py --write-prompts prompts/` (or `--model-cmd`). If the
   brain arm does not beat the none arm on your own questions, fix the records before adding anything else.

4. Then the hooks (`hooks/`), the nightly dream (`dream/README.md`) and, when several agents work at once,
   `claims.py` (`python3 agents_test.py` checks it on a scratch copy of this store). The starter's README in the
   repository explains each one; its `hooks/session_test.py` and `dream/dream_test.py` test the scripts against
   the studio's records and stay there, so run them in the starter after changing a hook or the dream.
"""


def skipped(rel):
    parts = rel.split(os.sep)
    return rel in SKIP_PATHS or any(p in SKIP_NAMES for p in parts) or rel.endswith((".pyc", ".lock"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dest", help="the folder to create")
    ap.add_argument("--field", default="a new field", help="a few words naming the field, for the README")
    a = ap.parse_args()
    dest = os.path.abspath(a.dest)
    if os.path.commonpath([dest, HERE]) == HERE:
        sys.exit("the new brain cannot go inside the starter folder: %s" % dest)
    if os.path.exists(dest) and os.listdir(dest):
        sys.exit("%s exists and is not empty; choose a new folder" % dest)

    copied = 0
    for root, dirs, files in os.walk(HERE):
        rel_root = os.path.relpath(root, HERE)
        rel_root = "" if rel_root == "." else rel_root
        dirs[:] = sorted(d for d in dirs if not skipped(os.path.join(rel_root, d)))
        os.makedirs(os.path.join(dest, rel_root), exist_ok=True)
        for name in sorted(files):
            rel = os.path.join(rel_root, name)
            if not skipped(rel):
                shutil.copy2(os.path.join(HERE, rel), os.path.join(dest, rel))
                copied += 1

    mem = os.path.join(dest, "memory")
    os.makedirs(mem, exist_ok=True)
    for name, text in (("MEMORY.md", INDEX), ("MISTAKES.md", MISTAKES)):
        with open(os.path.join(mem, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
    with open(os.path.join(dest, "questions.json"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("[]\n")
    with open(os.path.join(dest, "README.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(README.format(field=a.field))

    res = subprocess.run([sys.executable, os.path.join(dest, "check_store.py"), "--dir", mem],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("made %s: %d files copied, an empty store, an empty questions.json" % (dest, copied))
    print("check_store.py: %s" % ("clean" if res.returncode == 0 else "exit %d" % res.returncode))
    if res.returncode:
        print((res.stdout + res.stderr).strip())
        return 1
    print("next: write ten records with new_record.py and ten questions in questions.json (README.md has the steps)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
