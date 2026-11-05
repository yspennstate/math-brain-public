"""Controls for mistake_graph.py reading the dated prose corrections (27 Sep 2026).

Parses a small corrections file with this folder's parser and with the version before the change (a path given as
the first argument, or the copy in this repository's git history), and checks that every old record keeps its id and
that the dated entries come out as records of their own. Reads no installed brain.

    python test_mistake_graph_dated.py [OLD_MISTAKE_GRAPH_PY]

Without git history and without an argument, control 1 checks only that the bold entries are still records.
"""
import importlib.util
import os
import subprocess
import sys
import tempfile

DR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DR)
FAILS = []
OLD_REV = "dec23649c417c478778105ad364eead9007cc71e"   # the last public commit before the dated parser

TEXT = """# Corrections

- **2026-08-12 morning (a bold family)** 'quote' -> wrong: an old mistake in the bold form. Lesson: do the check first.
- 2026-08-13 (evening, agentx): a dated entry right under a bold one with no blank line between them. Rule: split
  the population before naming it.

- 2026-09-27 05:2x-05:3x local (agent-a, note layer): notes.py read SESSION_NAME, which is
  never set. Every fetch has an empty session. Rule: grep every reader of a wrong name in the same hour.
  - 2026-09-26 an indented dated sub-item that belongs to the entry above
- 2026-09-27 06:39 local (agent-a, co-activation fold): a test wrote into the live table through default
  arguments, and nothing states a rule here.

- **2026-07-10 (old one)** -> wrong: a thing. Lesson: another thing.
- **2026-07-11 (old two)** -> wrong: something. Lesson: something else.
"""


def load(path, name):
    if not path.endswith(".py"):                 # a backup copy: the loader only takes a .py name
        import shutil
        dst = os.path.join(tempfile.mkdtemp(prefix="mg_old_"), name + ".py")
        shutil.copy(path, dst)
        path = dst
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


def old_parser_path(tmp):
    if len(sys.argv) > 1:
        return sys.argv[1]
    r = subprocess.run(["git", "-C", DR, "show", OLD_REV + ":framework/dreaming/mistake_graph.py"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 or "def parse_corrections" not in r.stdout:
        return None
    p = os.path.join(tmp, "mistake_graph_old.py")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(r.stdout)
    return p


def main():
    tmp = tempfile.mkdtemp(prefix="mg_test_")
    new = load(os.path.join(DR, "mistake_graph.py"), "mg_new")
    ids = {"a_fix_at_one_site_is_a_note"}
    rn, _ = new.parse_corrections(ids, raw=TEXT)
    oldp = old_parser_path(tmp)
    if oldp:
        old = load(oldp, "mg_old")
        ro, _ = old.parse_corrections(ids, raw=TEXT)
        so = {r["id"] for r in ro}
        check("1 every record the old parser made keeps its id", so <= {r["id"] for r in rn},
              "missing %d" % len(so - {r["id"] for r in rn}))
    else:
        print("SKIP 1 every record the old parser made keeps its id (no git history and no path given)")
        bold = ("2026-08-12 morning", "2026-07-10", "2026-07-11")   # the bold entries in TEXT
        so = {r["id"] for r in rn if r["header"].startswith(bold)}
        check("1b the three bold entries are still records", len(so) == 3, str([r["header"] for r in rn]))
    dated = [r for r in rn if r["id"] not in so]
    heads = [r["header"] for r in dated]
    check("2 the three column-0 dated entries become records", len(dated) == 3, str(heads))
    check("3 a clock like 05:2x stays in the header", any("05:2x-05:3x local" in h for h in heads), str(heads))
    e = [r for r in dated if r["wrong"].startswith("notes.py read")]      # headers are stored cut at 60 characters
    check("4 the rule becomes the lesson and the first sentence the wrong",
          bool(e) and e[0]["lesson"].startswith("grep every reader") and e[0]["wrong"].startswith("notes.py read"),
          str(e[0] if e else None))
    check("5 an indented dated sub-item does not start a record", not any(h.startswith("2026-09-26") for h in heads),
          str(heads))
    n = [r for r in dated if r["wrong"].startswith("a test wrote into the live table")]
    check("6 an entry without a rule is kept, with an empty lesson", bool(n) and n[0]["lesson"] == "", str(n))
    print("%d of 6 controls pass" % (6 - len(FAILS)))
    return 1 if FAILS else 0


if __name__ == "__main__":
    if "-h" in __import__("sys").argv[1:] or "--help" in __import__("sys").argv[1:]:
        print((__doc__ or "").strip() or "usage: python %s" % __import__("os").path.basename(__file__))
        raise SystemExit(0)
    sys.exit(main())
