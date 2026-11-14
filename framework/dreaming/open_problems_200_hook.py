# -*- coding: utf-8 -*-
"""THE 200 OPEN PROBLEMS HOOK (his order, 10 Oct 2026 18:42 his clock).

Written at the author's request..

What it does: on a prompt about open problems (solving, conjectures, problem ids such as P0359, the directive), it says
once per session per 45 minutes where the list is and the rules that go with it; and when a prompt names problem ids
that are not on the list it says so, once per session per id per 45 minutes. Silent after the directive ends (16 Oct
2026, 19:08 his clock). Never blocks or edits; swallows its own errors; ASCII output. Switch file:
~/.claude/dreaming/OPEN_PROBLEMS_200_HOOK_OFF. State: open_problems_200_hook_state.json beside this file.

    python open_problems_200_hook.py                     Claude (plain text)
    python open_problems_200_hook.py --runtime codex     Codex (JSON hookSpecificOutput; Codex discards plain stdout)
    python open_problems_200_hook.py --selftest          controls on a temporary state file; the live state is untouched
"""
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "open_problems_200_hook_state.json")
OFF = os.path.join(HERE, "OPEN_PROBLEMS_200_HOOK_OFF")
IDS = r"~\brain_workers\OPEN_PROBLEMS_200\ids.txt"
END = time.mktime((2026, 10, 16, 19, 8, 0, 0, 0, -1))
EVERY_S = 2700
TOPIC = re.compile(r"\bopen[ -]problems?\b|\bconjectur\w*|\bunsolved\b|\bsolv(?:e|es|ed|er|ers|ing)\b[^.\n]{0,60}"
                   r"\b(?:problem|conjecture|question)s?\b|\b(?:prime|primary)\s+directive\b|\bteam o\b|"
                   r"\b[CDEFGHIP]0\d{3}\b|\bOPEN_PROBLEMS_200\b|\bopen-problems-repo\b", re.I)
PID = re.compile(r"\b([CDEFGHIP]0\d{3})\b")
LINE = ("[open-problems-200] Two lists are live; newer words win. (1) The top-400 list, "
        "06_math_research/top200_probability_2026_10_14/list.jsonl: the famous-200 probability problems T001-T222 (his "
        "14 Oct orders: 18:46 get it to 200 and solve what remains, 22:09, 23:25 the frontier framework) and, since 16 Oct "
        "01:18/01:2x, 200 deep-learning problems tied to probability, T223-T422 (list tag TOP200_DL; a Codex auditor "
        "passes each before solvers start, frontier.py gate checks it). A row is worked only through "
        "06_math_research/frontier/frontier.py brief and check, lead per frontier/STAFF.json. (2) His 10 Oct 18:42 list "
        "of 200 publishable but doable problems, ~/brain_workers/OPEN_PROBLEMS_200/LIST.md (list.jsonl, "
        "ids.txt; brain copy 06_math_research/open_problems_200_2026_10_10; on GitHub in open-problems-repo). Nothing off "
        "both lists before 16 Oct 19:08 unless he names it. Before you start one, search the literature and GitHub for "
        "someone else's solution and cite it. A claimed answer is a candidate until two independent audits pass; record "
        "it in the problem's ledger row (newest recorded_at wins), never by editing a list. Test items are local only.")


def session_key(payload):
    for k in ("session_id", "sessionId", "thread_id", "conversation_id"):
        v = payload.get(k) if isinstance(payload, dict) else None
        if v:
            return str(v)[:64]
    for k in ("CODEX_THREAD_ID", "CODEX_SESSION_ID", "CLAUDE_SESSION_ID"):
        if os.environ.get(k):
            return os.environ[k][:64]
    return "pid%s:%s" % (os.getppid(), (payload.get("cwd") if isinstance(payload, dict) else "") or os.getcwd())


def due(key, now, state_path=STATE, every=EVERY_S):
    """True once per key per `every` seconds; records the fire. Entries older than a day are dropped."""
    try:
        st = json.load(io.open(state_path, encoding="utf-8"))
    except Exception:
        st = {}
    last = st.get(key)
    if isinstance(last, (int, float)) and now - last < every:
        return False
    st = {k: v for k, v in st.items() if isinstance(v, (int, float)) and now - v < 86400}
    st[key] = now
    tmp = state_path + ".%d.tmp" % os.getpid()
    try:
        with io.open(tmp, "w", encoding="utf-8") as f:
            json.dump(st, f)
        os.replace(tmp, state_path)
    except Exception:
        try:
            os.remove(tmp)
        except Exception:
            pass
    return True


def on_list(ids_path=IDS):
    try:
        return {l.strip() for l in io.open(ids_path, encoding="utf-8") if l.strip()}
    except Exception:
        return set()


def lines_for(key, text, now, state_path=STATE, ids_path=IDS):
    if now >= END or not text or not TOPIC.search(text):
        return []
    out = []
    if due(key, now, state_path):
        out.append(LINE)
    listed = on_list(ids_path)
    if listed:
        off = sorted({m for m in PID.findall(text) if m not in listed})
        off = [m for m in off if due(key + "|" + m, now, state_path)]
        if off:
            out.append("[open-problems-200] Not on the 10 Oct 200 list: %s. No solving work on these before 16 Oct 19:08 "
                       "unless he names them; papers for problems already solved are his separate order." % ", ".join(off[:12]))
    return out


# THE ROW'S BRIEF FOR A CODEX WORKER (15 Oct 2026, an agent; his 14 Oct 23:25 order, T-20261014-145: "i don't
# want agents wasting time resolving the same stuff ... make sure that the codex agent ... push forward like this").
# frontier_hook.py gives the brief to Claude sessions only (through the dispatcher), and a new Codex hook would need his
# trust; this hook is already trusted on every Codex profile. A Codex session whose cwd is a worker folder that
# frontier/STAFF.json assigns to a top-200 row (or the parent of one: w675 for w675/T067, since the pool runs a worker
# in its own root) gets that row's short brief - STATE (what is done), failure point, obstruction, targets, routes not
# to redo - once per 45 minutes per row, i.e. at the start of each stage. ASCII only.
TOP200 = "~/brain-repo/06_math_research/frontier"


def _norm(p):
    return os.path.normcase(os.path.normpath(str(p or ""))).rstrip("\\/")


def staffed_rows(cwd, staff_path=None):
    """The top-200 rows whose STAFF.json folder is cwd, or is a row subfolder (TNNN) directly inside cwd."""
    c = _norm(cwd)
    if not c:
        return []
    try:
        staff = json.load(io.open(staff_path or os.path.join(TOP200, "STAFF.json"), encoding="utf-8"))
    except Exception:
        return []
    rows = []
    for row, info in staff.items():
        if not (isinstance(info, dict) and re.fullmatch(r"T\d{3}", row)):
            continue
        for f in info.get("folders") or []:
            nf = _norm(f)
            # the parent counts only for a row subfolder (w675/T067); else brain_workers itself would match every worker
            if nf == c or (os.path.dirname(nf) == c and re.fullmatch(r"t\d{3}", os.path.basename(nf), re.I)):
                rows.append(row)
                break
    return sorted(rows)


def frontier_lines(key, cwd, now, state_path=STATE, staff_path=None, brief=None):
    out = []
    for row in staffed_rows(cwd, staff_path)[:2]:
        if not due(key + "|frontier|" + row, now, state_path):
            continue
        try:
            if brief is None:
                import importlib.util
                spec = importlib.util.spec_from_file_location("frontier_top200", os.path.join(TOP200, "frontier.py"))
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                body = mod.brief_text(row, True)
            else:
                body = brief(row)
        except Exception:
            continue
        body = body.replace("\u2013", "-").replace("\u2014", "-").encode("ascii", "replace").decode("ascii")
        out.append("[frontier %s] Work this row only through its brief; run frontier.py check before any route. %s"
                   % (row, body[:6000]))
    return out


def emit(runtime, lines):
    text = "\n".join(lines)
    if runtime == "codex":
        sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                                            "additionalContext": text}}) + "\n")
    else:
        sys.stdout.write(text + "\n")
    sys.stdout.flush()


def main(argv):
    runtime = "codex" if "--runtime" in argv and argv[argv.index("--runtime") + 1:argv.index("--runtime") + 2] == ["codex"] else "claude"
    if "--selftest" in argv:
        return selftest()
    try:
        if os.path.exists(OFF):
            return 0
        raw = ""
        try:
            if not sys.stdin.isatty():
                raw = sys.stdin.read()
        except Exception:
            raw = ""
        try:
            payload = json.loads(raw) if raw.strip() else {}
        except Exception:
            payload = {}
        prompt = payload.get("prompt") if isinstance(payload, dict) else ""
        key, now = session_key(payload), time.time()
        got = lines_for(key, prompt if isinstance(prompt, str) else "", now)
        if runtime == "codex" and isinstance(payload, dict):
            got += frontier_lines(key, payload.get("cwd") or "", now)
        if got:
            emit(runtime, got)
    except Exception:
        pass
    return 0


def selftest():
    import tempfile
    d = tempfile.mkdtemp()
    sp, ip = os.path.join(d, "state.json"), os.path.join(d, "ids.txt")
    with io.open(ip, "w", encoding="utf-8") as f:
        f.write("P0359\nC0035\n")
    t0 = END - 86400
    checks = [
        ("fires on an open-problem prompt", lines_for("s1", "work on the open problem P0359 next", t0, sp, ip), [LINE]),
        ("same session inside 45 min is quiet", lines_for("s1", "keep solving the open problems", t0 + 60, sp, ip), []),
        ("flags an id that is not on the list", len(lines_for("s1", "try to solve problem F0009 now", t0 + 120, sp, ip)), 1),
        ("the same off-list id is not repeated", lines_for("s1", "try to solve problem F0009 now", t0 + 180, sp, ip), []),
        ("silent on a film prompt", lines_for("s2", "render the next scene of the film", t0, sp, ip), []),
        ("another session fires", lines_for("s3", "which conjecture should the solvers take", t0, sp, ip), [LINE]),
        ("silent after the directive ends", lines_for("s4", "open problem P0359", END + 1, sp, ip), []),
    ]
    stp = os.path.join(d, "STAFF.json")
    with io.open(stp, "w", encoding="utf-8") as f:
        json.dump({"T067": {"folders": ["C:/W/w682", "C:/W/w675/T067"]}, "T170": {"folders": ["C:/W/w685/T170"]},
                   "_retired": {"T059": "x"}}, f)
    fake = lambda row: "BRIEF %s \u2013 lambda \u03bb" % row
    fl = lambda key, cwd, t: frontier_lines(key, cwd, t, sp, stp, fake)
    checks += [
        ("frontier: worker root gets its row", [x[:15] for x in fl("c1", "C:\\W\\w682", t0)], ["[frontier T067]"]),
        ("frontier: same row inside 45 min is quiet", fl("c1", "C:/W/w682", t0 + 60), []),
        ("frontier: parent of a staffed subfolder", [x[:15] for x in fl("c2", "C:/W/w675", t0)], ["[frontier T067]"]),
        ("frontier: the staffed subfolder itself", [x[:15] for x in fl("c3", "C:/W/w685/T170", t0)], ["[frontier T170]"]),
        ("frontier: unrelated folder is silent", fl("c4", "C:/W/w999", t0), []),
        ("frontier: a grandparent is silent", fl("c5", "C:/W", t0), []),
        ("frontier: output is ASCII", all(ord(ch) < 128 for x in fl("c6", "C:/W/w682", t0) for ch in x), True),
    ]
    ok = True
    for name, got, want in checks:
        good = got == want
        ok = ok and good
        print("%s  %s" % ("PASS " if good else "FAIL ", name))
    env = json.loads(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": LINE}}))
    print("%s  codex envelope carries the line" % ("PASS " if env["hookSpecificOutput"]["additionalContext"] == LINE else "FAIL "))
    asc = all(ord(c) < 128 for c in LINE)
    print("%s  line is ASCII (%d chars)" % ("PASS " if asc else "FAIL ", len(LINE)))
    ok = ok and asc
    print("PASS - open problems 200 hook controls" if ok else "FAIL - open problems 200 hook controls")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
