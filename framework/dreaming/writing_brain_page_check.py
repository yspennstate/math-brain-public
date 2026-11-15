# -*- coding: utf-8 -*-
"""The page check that runs by itself after a Write or Edit (written by an agent, 14 Nov 2026, as a proposal;
taken into tools/ and wired as a PostToolUse hook by an agent the same night).

Why: in the 36 hours to 14 Nov 00:20, five Claude sessions were told about the writing brain by the hook and then
edited prose (main.tex 95, 92, 44 and 23 times); none of them ran after_page.py or writing_recall.py once
(wb_usage_audit.py beside this file). The hook's pattern cards see only the text of one Write or Edit, so a fault of
the whole file (I in one section and we in the next, a reference in the abstract, the missing funding line, headings
on one template) is never checked unless the agent chooses to run the page check. This makes the page check run by
itself.

What: decide_post(event) for PostToolUse of Write or Edit on a page of prose (the hook's own wing_of_path). It runs
every machine check of that wing over the WHOLE file as it now stands on disk, and prints at most MAX_CARDS cards
that fire, each with its count and first lines. A card is printed for a session and file only when it is new there
or its count has changed, and the file is checked again no sooner than COOL_S after the last check. It never blocks.

As a hook it reads the event from stdin (PostToolUse, Write or Edit), keeps its state beside itself, prints plain
text and never fails loudly. The live copy is ~/.claude/dreaming/writing_brain_page_check.py; this file is the source.

usage: python -I -X utf8 page_check_after_write.py --selftest
       python -I -X utf8 page_check_after_write.py FILE --wing mathematics     (one run, as the hook would print)
       (no arguments, an event on stdin: the hook)"""
import io, json, os, re, sys, tempfile, time

# As a hook: read the event and leave at once, before the heavier imports, unless it is a Write or Edit of a file
# that could be a page of prose. Most Write and Edit calls are code, and each one starts this process.
_EVENT = None
if __name__ == "__main__" and len(sys.argv) == 1:
    try:
        _EVENT = json.loads(sys.stdin.read() or "{}")
        _fp = str((_EVENT.get("tool_input") or {}).get("file_path") or "").lower()
        if _EVENT.get("tool_name") not in ("Write", "Edit") or not _fp.endswith((".tex", ".md", ".txt", ".fountain", ".json", ".jsonl")):
            sys.exit(0)
    except SystemExit:
        raise
    except Exception:  # noqa: BLE001
        sys.exit(0)

TOOLS ="~/brain-repo/12_cognitive_architecture/writing_brain/tools"
sys.path.insert(0, TOOLS)
import after_page as AP            # read-only use: load, MECH, C (wb_checks), headings
import writing_brain_hook as H     # read-only use: wing_of_path

ROOT = os.path.normpath(os.path.join(TOOLS, "..")).replace("\\", "/")
COOL_S = 20 * 60
MAX_CARDS = 3
MAX_BYTES = 1500000
STATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "writing_brain_page_check_state.json")
KEEP_S = 7 * 86400


def headings_same_first_word_v2(path, lines, text):
    """The heading check, which since 14 Nov leaves out an article or "Proof" as the shared first word."""
    return AP.MECH["headings_same_first_word"](path, lines, text)


def _load():
    try:
        with io.open(STATE, encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def _save(d, now=None):
    now = now or time.time()
    try:
        # a time is kept for a week; a count (said already) lives as long as the time of its file's last check
        times = dict((k, v) for k, v in d.items() if "|WB-" not in k and isinstance(v, (int, float)) and now - v < KEEP_S)
        keep = dict(times)
        for k, v in d.items():
            if "|WB-" in k and k.rsplit("|", 1)[0] in times:
                keep[k] = v
        tmp = "%s.%d.tmp" % (STATE, os.getpid())
        with io.open(tmp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(keep, f)
        os.replace(tmp, STATE)
    except Exception:  # noqa: BLE001
        pass


def hook_main():
    p = _EVENT
    if not isinstance(p, dict) or (p.get("hook_event_name") or "PostToolUse") != "PostToolUse":
        return
    try:
        st = _load()
        before = json.dumps(st, sort_keys=True)
        out = decide_post(p, st)
    except Exception:  # noqa: BLE001
        return
    if json.dumps(st, sort_keys=True) != before:
        _save(st)
    if out:
        try:
            sys.stdout.write(out.encode("ascii", "replace").decode("ascii") + "\n")
        except Exception:  # noqa: BLE001
            pass


def run_checks(path, wing, root=ROOT, mech=None):
    """[(card, hits)] for every machine check of the wing that fires on the whole file. Same loop as after_page.main."""
    mech = mech or AP.MECH
    raw = io.open(path, "r", encoding="utf-8", errors="replace").read()
    lines = [(n, l) for n, l in enumerate(raw.splitlines(), 1) if l.strip() and not l.lstrip().startswith("%")]
    text = "\n".join(l for _, l in lines)
    out = []
    for c in AP.load(root):
        if c["wing"] not in (wing, "all"):
            continue
        hits = []
        if c.get("pattern"):
            rx = re.compile(c["pattern"], re.I)
            hits += [(n, l.strip()) for n, l in lines if rx.search(l)]
        for name in [x.strip() for x in (c.get("mechanical") or "").split(";") if x.strip()]:
            if name in AP.C.NAMED:
                got = AP.C.run_named(name, raw)
                got = None if got is None else [(0, l) for l in got]
            else:
                f = mech.get(name)
                got = f(path, lines, text) if f else None
            if got:
                seen = set(n for n, _ in hits)
                hits += [(n, l) for n, l in got if n == 0 or n not in seen]
        if hits:
            out.append((c, hits))
    return out


def decide_post(p, state=None, now=None, root=ROOT, mech=None, max_cards=MAX_CARDS):
    """Text to print after a Write or Edit, or ''. state is mutated when a check runs."""
    state = state if state is not None else {}
    now = now or time.time()
    if p.get("tool_name") not in ("Write", "Edit"):
        return ""
    path = str((p.get("tool_input") or {}).get("file_path") or "").replace("\\", "/")
    wing = H.wing_of_path(path)
    if not wing or not os.path.isfile(path) or os.path.getsize(path) > MAX_BYTES:
        return ""
    sid = str(p.get("session_id") or "nosession")[:40]
    key = "%s|page|%s" % (sid, path.lower())
    if now - state.get(key, 0) < COOL_S:
        return ""
    state[key] = now
    out = []
    fired = run_checks(path, wing, root, mech)
    for c, hits in fired:
        ck = "%s|%s" % (key, c["id"])
        if state.get(ck) == len(hits):
            continue                      # said already, and nothing changed
        if len(out) >= max_cards:
            continue                      # not shown, so not marked as said: it comes up at the next check
        state[ck] = len(hits)
        n, l = hits[0]
        out.append("[writing-brain] whole page, %s  %s - %d place(s); first: %s%s\n   rule: %s"
                   % (c["id"], c["title"], len(hits), ("line %d: " % n) if n else "", l[:140], c["rule"]))
    if out:
        out.append("[writing-brain] %d machine check(s) fire on this file as it stands. All of them, with lines: "
                   "python -X utf8 %s/after_page.py \"%s\" --wing %s . Hints, not verdicts; fix or say why not before he reads it."
                   % (len(fired), TOOLS, path, wing))
    return "\n".join(out)


def selftest():
    bad = 0

    def check(name, ok):
        nonlocal bad
        bad += not ok
        print("%s %s" % ("ok  " if ok else "FAIL", name))
    d = tempfile.mkdtemp(prefix="wbpost_")
    tex = os.path.join(d, "paper_x.tex").replace("\\", "/")
    body = ("\\begin{abstract}\nWe extend the result of \\cite{L} to trees.\n\\end{abstract}\n\\section{Intro}\n"
            "We show the bound.\n\\section{Proof}\nHere I use the lemma.\n")
    io.open(tex, "w", encoding="utf-8").write(body)
    ev = {"session_id": "s1", "tool_name": "Edit", "tool_input": {"file_path": tex, "new_string": "Here I use the lemma."}}
    st = {}
    first = decide_post(ev, st, now=1000000.0, max_cards=50)
    check("an Edit of one clean line still gets the whole-file faults (I and we; a citation in the abstract)",
          "WB-M0057" in first and "WB-M0039" in first)
    if "--show" in sys.argv:
        print("\n".join(l[:110] for l in first.split("\n") if l.startswith("[writing-brain]")))
    check("quiet inside the cooldown", decide_post(ev, st, now=1000000.0 + 60, max_cards=50) == "")
    check("after the cooldown, unchanged faults are not said twice", decide_post(ev, st, now=1000000.0 + COOL_S + 1, max_cards=50) == "")
    io.open(tex, "w", encoding="utf-8").write(body + "Again I note it.\n")
    again = decide_post(ev, st, now=1000000.0 + 2 * COOL_S + 2, max_cards=50)
    check("a fault whose count changed is said again, the unchanged one is not", "WB-M0057" in again and "WB-M0039" not in again)
    check("another session is told", "WB-M0057" in decide_post(dict(ev, session_id="s2"), st, now=1000000.0 + 60, max_cards=50))
    st2 = {}
    one = decide_post(ev, st2, now=2000000.0, max_cards=1)
    two = decide_post(ev, st2, now=2000000.0 + COOL_S + 1, max_cards=1)
    check("a card cut by the cap is not marked as said: the next check shows a different card",
          one.count("whole page") == 1 and two.count("whole page") == 1 and one.split("\n")[0] != two.split("\n")[0])
    clean = os.path.join(d, "paper_clean.tex").replace("\\", "/")
    io.open(clean, "w", encoding="utf-8").write("\\section{Intro}\nLet $G$ be a tree. The bound holds.\n")
    got = decide_post({"session_id": "s3", "tool_name": "Write", "tool_input": {"file_path": clean}}, {}, now=3000000.0)
    check("a clean page of two lines: nothing about I, we or the abstract", "WB-M0057" not in got and "WB-M0039" not in got)
    notes = os.path.join(d, "notes.md").replace("\\", "/")
    io.open(notes, "w", encoding="utf-8").write(body)
    check("quiet on a file that is not a page of prose", decide_post({"session_id": "s4", "tool_name": "Write", "tool_input": {"file_path": notes}}, {}) == "")
    check("quiet on a Bash call", decide_post({"session_id": "s5", "tool_name": "Bash", "tool_input": {"command": "ls"}}, {}) == "")
    L = lambda hs: [(i + 1, "\\section{%s}" % h) for i, h in enumerate(hs)]
    check("v2 headings: three that open with What still fire",
          len(headings_same_first_word_v2("", L(["What we prove", "What is known", "What remains", "Setup"]), "")) == 3)
    check("v2 headings: A / The / Proof of are not a template",
          headings_same_first_word_v2("", L(["A finite criterion", "A combined criterion", "A third one", "The algebra", "The states",
                                              "The proof idea", "Proof of Theorem 1", "Proof of Theorem 2", "Proof of Lemma 3"]), "") == [])
    print("selftest: %d failed" % bad)
    return bad


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(1 if selftest() else 0)
    if len(a) == 3 and a[1] == "--wing":
        t = time.time()
        got = decide_post({"session_id": "cli", "tool_name": "Edit", "tool_input": {"file_path": a[0]}}, {}) or "(nothing to say)"
        print(got.encode("ascii", "replace").decode("ascii"))
        print("-- %.1f s" % (time.time() - t))
    elif a:
        print(__doc__)
    else:
        hook_main()
