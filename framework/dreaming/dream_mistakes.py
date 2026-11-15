# dream_mistakes.py - how much of each dream journal is mistake-work, against the author's standing order
# ("30% of the dreaming should be about mistake", 2026-07-08; repeated in his dream prompts).
#
# PRODUCER   the dream writes its journal to memory\dreams\dream_<date>[_rem|_partial].md
# CONSUMER   dream.py puts agenda_lines() at the top of agenda section M, so the next dream reads how far
#            the last ones fell short; brain_status.py prints summary_line() under its DREAM line
# FRESHNESS  read from the journal files at call time; nothing is cached
# FAILURE    a journal with no mistake section and no MISTAKES: line counts as 0; three full dreams in a
#            row under FLOOR turn the agenda line into a SHORTFALL that tells the dream to start with M
# TEST       --selftest (fixture journals in a temp folder; the live folder is not touched)
#
#   python dream_mistakes.py            table of the last journals
#   python dream_mistakes.py --summary  one line
#   python dream_mistakes.py --agenda   the lines the agenda carries
#   python dream_mistakes.py --selftest
import os
import re
import sys

DREAMS = os.path.join(os.path.expanduser("~"), ".claude", "projects", os.environ.get("BRAIN_SLUG", "default"), "memory", "dreams")
TARGET = 0.30      # his order
FLOOR = 0.20       # under this a full dream is counted short
MIN_BYTES = 1500   # a stub or a died-early journal is not judged as a dream
HEAD = re.compile(r"^(#{2,4})\s+(.*)$")
MISTAKE_HEAD = re.compile(r"(?i)\bmistakes?\b|\bcorrections?\b|\bscars?\b|^m[\.,:]?\s|^m$|^section m\b")
LINE = re.compile(r"(?im)^MISTAKES:\s*(.*)$")
KIND = re.compile(r"(?i)\b(nap|sws|slow-wave|rem)\b")
DR = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(DR, "logs")
WATCH_STATUS = os.path.join(DR, ".mistake_graph_status.json")
# Both patterns are anchored to the start of a line: the runner also prints the child's last output joined on
# one "child said:" line, and that line can quote a correction that merely mentions these words.
WATCH_HEAD = re.compile(r"(?m)^ RECURRENCE WATCH  \(change since last snapshot\)[ \t]*$")
WATCH_FAIL = re.compile(r"(?m)^\s*\*\* (?:WATCH|CORRECTION|ARGUMENT|ARTIFACT) [A-Z ]*FAILED[^\n]*"
                        r"|^\d\d:\d\d:\d\d mistake graph watch failed[^\n]*")
WATCH_END = re.compile(r"^\d\d:\d\d:\d\d |^\[")       # the runner's next log line ends the block
WATCH_LOG_BYTES = 8 * 1024 * 1024
WATCH_BLOCK_LINES = 14
WATCH_LINE_CHARS = 420


def kind_of(name, text):
    first = text.split("\n", 1)[0]
    m = KIND.search(first)
    k = (m.group(1).lower() if m else "")
    if k == "slow-wave":
        k = "sws"
    if not k and name.endswith("_rem.md"):
        k = "rem"
    return k or "full"


def measure(text):
    """Share of the journal's characters that sit under a mistake heading (subsections included)."""
    total = 0
    inside = 0
    on = False
    on_level = 0
    for ln in text.split("\n"):
        m = HEAD.match(ln)
        if m:
            level = len(m.group(1))
            hit = bool(MISTAKE_HEAD.search(m.group(2).strip()))
            if hit:
                on, on_level = True, level
            elif on and level <= on_level:
                on = False
        n = len(ln) + 1
        total += n
        if on:
            inside += n
    lm = LINE.search(text)
    return {"chars": total, "mistake_chars": inside, "share": (inside / total) if total else 0.0,
            "line": (lm.group(1).strip()[:160] if lm else "")}


def rows(limit=10, folder=None):
    folder = folder or DREAMS
    out = []
    try:
        names = [n for n in os.listdir(folder) if n.startswith("dream_") and n.endswith(".md")]
    except OSError:
        return out
    names.sort(key=lambda n: os.path.getmtime(os.path.join(folder, n)), reverse=True)
    for n in names:
        if len(out) >= limit:
            break
        p = os.path.join(folder, n)
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        r = measure(text)
        r["name"] = n
        r["partial"] = "_partial" in n or "PARTIAL" in text[:300]
        r["judged"] = (not r["partial"]) and len(text.encode("utf-8", "replace")) >= MIN_BYTES
        r["kind"] = kind_of(n, text)
        out.append(r)
    return out


def full(rs):
    """The journals the 30% applies to: finished, not a stub, not a nap."""
    return [r for r in rs if r["judged"] and r["kind"] != "nap"]


def _median(xs):
    xs = sorted(xs)
    if not xs:
        return 0.0
    h = len(xs) // 2
    return xs[h] if len(xs) % 2 else (xs[h - 1] + xs[h]) / 2.0


def summary_line(rs=None):
    rs = rows() if rs is None else rs
    fs = full(rs)
    if not fs:
        return "  mistake work: no finished full dream journal among the last %d" % len(rs)
    med = _median([r["share"] for r in fs])
    return ("  mistake work: median %.0f%% of the journal text in the last %d full dreams (his order: about %.0f%%); "
            "a mistake section in %d, a MISTAKES: line in %d; %d of the last %d journals were stubs or died early"
            % (100 * med, len(fs), 100 * TARGET, sum(1 for r in fs if r["mistake_chars"]),
               sum(1 for r in fs if r["line"]), sum(1 for r in rs if not r["judged"]), len(rs)))


def watch_lines(logs=None, status_path=None, limit=40):
    """What the recurrence watch (mistake_graph.py --watch, a tail step of every dream) said last, for the agenda.

    PRODUCER   the watch prints its block into the dream log; its status file carries the counts
    CONSUMER   agenda_lines() below, so the NEXT dream is told which one-off became recurring
    FRESHNESS  read from the newest dream logs and the status file at call time
    FAILURE    a watch that failed is said so, with how many dream logs in a row and the watch's own reason
    Until 10 Nov 2026 the block reached the log and nothing else: the watch refused 35 dreams in a row and no
    dream was told.
    """
    logs = LOGS if logs is None else logs
    out = []
    try:
        names = sorted((n for n in os.listdir(logs) if n.startswith("dream_") and n.endswith(".log")), reverse=True)
    except OSError:
        names = []
    failed, reason, block, block_log, failed_at = 0, "", [], "", 0.0
    for n in names[:limit]:
        try:
            with open(os.path.join(logs, n), encoding="utf-8", errors="replace") as fh:
                text = fh.read(WATCH_LOG_BYTES)
        except OSError:
            continue
        m = WATCH_FAIL.search(text)
        heads = [h.start() for h in WATCH_HEAD.finditer(text)]
        i = heads[-1] if heads else -1
        if m:
            failed += 1
            if not reason:
                reason = " ".join(m.group(0).split()).lstrip("* ")[:260]
                try:
                    failed_at = os.path.getmtime(os.path.join(logs, n))
                except OSError:
                    failed_at = 0.0
            continue
        if i >= 0:
            for ln in text[i:].splitlines()[2:]:
                if not ln.strip() or ln.startswith("(report-only") or WATCH_END.match(ln):
                    break
                block.append(ln.rstrip()[:WATCH_LINE_CHARS])
            block, block_log = block[:WATCH_BLOCK_LINES], n[:-4]
            break
        # a log with neither (a skipped start, a dream that died before its tail) says nothing either way
    try:
        status_at = os.path.getmtime(status_path or WATCH_STATUS)
    except OSError:
        status_at = 0.0
    if failed and status_at > failed_at > 0:
        # a run outside a dream has published since: the status below is current, its verdict text is in no dream log
        out.append("The recurrence watch failed in the last %d dream log(s) (%s) and has published since, in a run "
                   "outside a dream. The status below is current; that run's verdict text is in no dream log."
                   % (failed, reason))
    elif failed:
        out.append("**The recurrence watch FAILED in the last %d dream log(s) in a row** (%s). Its status file is "
                   "older than those dreams; nothing below it is current. Find out why before any other mistake work."
                   % (failed, reason))
    try:
        import mistake_graph_status as _mgs
        s = _mgs.summarize_path(status_path or WATCH_STATUS)
        out.append("Recurrence watch status: %s" % s.line.replace("MISTAKES", "", 1).strip())
    except Exception as exc:
        out.append("Recurrence watch status: not readable (%s)" % " ".join(str(exc).split())[:120])
    if block and not failed:
        out.append("Its last verdict (%s):\n```\n%s\n```" % (block_log, "\n".join(block)))
        if any("BECAME RECURRING" in ln for ln in block):
            out.append("**The watch says a one-off became recurring.** Read the pair first: the watch links entries by "
                       "shared words, and two entries can share words without sharing a failure (10 Nov 2026: the pair "
                       "shared only 'file', 'memory', 'named'). If the two are one failure shape, write its reflex tonight "
                       "(append to `instincts_learned.json`) and name its key in the MISTAKES: line; if they are not, say "
                       "so there in one clause.")
    return out


def agenda_lines(rs=None, watch=None):
    rs = rows() if rs is None else rs
    fs = full(rs)[:3]
    out = []
    try:
        out.extend(watch_lines() if watch is None else watch)
    except Exception as exc:
        out.append("(the recurrence-watch reader did not run: %s)" % " ".join(str(exc).split())[:160])
    if fs:
        shares = ", ".join("%s %.0f%%" % (r["name"][6:-3], 100 * r["share"]) for r in fs)
        short = [r for r in fs if r["share"] < FLOOR]
        if len(short) == len(fs):
            out.append("**SHORTFALL: the last %d full dreams gave the corrections %s of their journal; his order is about "
                       "%.0f%%.** Tonight this section is worked FIRST, right after the safety gate and before any filing, "
                       "so a dream that runs out of clock has not skipped it." % (len(fs), shares, 100 * TARGET))
        else:
            out.append("Mistake share of the last full dreams' journals: %s (his order: about %.0f%%)."
                       % (shares, 100 * TARGET))
    else:
        out.append("No finished full dream journal to measure yet; his order is about %.0f%% of the dream on the corrections."
                   % (100 * TARGET))
    out.append("Write it in the journal under a heading `## M. Mistakes` and close that section with one line starting "
               "`MISTAKES:` - how many corrections you worked, how many reflexes you wrote or extended (their keys), "
               "which ones recur (their dates). The share is measured from that section.")
    return out


def table(rs):
    out = ["journal                      kind  bytes  mistake%  section  line"]
    for r in rs:
        out.append("%-28s %-5s %6d  %7s  %-7s  %s" % (
            r["name"][6:-3][:28], r["kind"], r["chars"],
            ("%.0f" % (100 * r["share"])) if r["judged"] else "stub",
            "yes" if r["mistake_chars"] else "no", "yes" if r["line"] else "no"))
    return out


def selftest():
    import tempfile
    d = tempfile.mkdtemp(prefix="dream_mistakes_")
    pad = "x" * 70 + "\n"

    def put(name, text, age):
        p = os.path.join(d, name)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        t = 1700000000 - age * 3600
        os.utime(p, (t, t))

    put("dream_2026_01_05.md", "# Dream 2026-01-05 (REM)\n\n## E. Replay\n" + pad * 35 +
        "## M. The corrections (the 30 percent)\n" + pad * 12 + "### Reflex draft\n" + pad * 3 +
        "MISTAKES: worked 4, reflexes 1 (ps1_hook_edit), recurring 2\n## H. Incubation\n" + pad * 4, 1)
    put("dream_2026_01_04.md", "# Dream 2026-01-04 (SWS / slow-wave filer)\n\n## A. Consolidated\n" + pad * 40 +
        "## Final reflection\n" + pad * 5, 2)
    put("dream_2026_01_03_partial.md", "# Dream 2026-01-03 (PARTIAL - mechanical stub)\n" + pad * 40, 3)
    put("dream_2026_01_02.md", "# Dream 2026-01-02 (midday NAP)\n\n## Mistakes, kept warm\n" + pad * 3 +
        "## Reflection\n" + pad * 30, 4)
    put("dream_2026_01_01.md", "# Dream 2026-01-01 (REM)\n\ntiny\n", 5)
    put("dream_2025_12_31.md", "# Dream 2025-12-31 (SWS)\n\n## C. Stale beliefs\n" + pad * 30 +
        "## Mistakes - the one error under the many\n" + pad * 2, 6)
    put("dream_2025_12_30.md", "# Dream 2025-12-30 (SWS)\n\n## A\n" + pad * 30, 7)
    rs = rows(folder=d)
    by = {r["name"]: r for r in rs}
    checks = []

    def ck(name, ok):
        checks.append((name, bool(ok)))

    ck("seven journals read, newest first", [r["name"] for r in rs][:2] == ["dream_2026_01_05.md", "dream_2026_01_04.md"] and len(rs) == 7)
    a = by["dream_2026_01_05.md"]
    ck("a journal with an M section measures between a quarter and a third", 0.25 < a["share"] < 0.34)
    ck("the subsection under M counts, the next ## section does not", a["mistake_chars"] > 15 * 71 and a["mistake_chars"] < 17 * 71 + 200)
    ck("the MISTAKES: line is read", a["line"].startswith("worked 4"))
    b = by["dream_2026_01_04.md"]
    ck("a journal with no mistake section measures 0 and has no line", b["share"] == 0.0 and b["line"] == "")
    ck("a partial stub is not judged", by["dream_2026_01_03_partial.md"]["judged"] is False)
    ck("a tiny journal is not judged", by["dream_2026_01_01.md"]["judged"] is False)
    ck("a nap is read as a nap and left out of the full dreams", by["dream_2026_01_02.md"]["kind"] == "nap" and by["dream_2026_01_02.md"] not in full(rs))
    ck("kinds: rem, sws", a["kind"] == "rem" and b["kind"] == "sws")
    fs = full(rs)
    ck("four full dreams", [r["name"] for r in fs] == ["dream_2026_01_05.md", "dream_2026_01_04.md", "dream_2025_12_31.md", "dream_2025_12_30.md"])
    ag = agenda_lines(rs, watch=[])
    ck("one good dream among the last three: no shortfall, shares named", "SHORTFALL" not in ag[0] and "2026_01_05" in ag[0])
    ck("the agenda always asks for the section and the line", "## M. Mistakes" in ag[-1] and "MISTAKES:" in ag[-1])
    ag2 = agenda_lines(rs[1:], watch=[])
    ck("three short dreams in a row: SHORTFALL, worked first", ag2[0].startswith("**SHORTFALL") and "FIRST" in ag2[0])
    ag3 = agenda_lines([], watch=[])
    ck("no journal at all: still two lines, no crash", len(ag3) == 2 and "No finished" in ag3[0])
    ck("the watch's lines lead the section", agenda_lines(rs, watch=["W1", "W2"])[:2] == ["W1", "W2"])

    # the recurrence watch, read from dream logs
    lg = os.path.join(d, "logs")
    os.mkdir(lg)
    rule = "=" * 74 + "\n"
    head = rule + " RECURRENCE WATCH  (change since last snapshot)\n" + rule
    said = ("2026-01-05 03:31:08 run_bounded: child said: a correction that says WATCH STATE FAILED in passing | "
            " RECURRENCE WATCH  (change since last snapshot) | mistake graph watch failed is quoted here\n")
    good = ("03:29:50 step: mistake_graph watch\n" + said + head +
            "  9 correction(s) were edited in place since the last snapshot.\n"
            "  ** A ONE-OFF BECAME RECURRING - author a reflex now (it is no longer a coincidence):\n"
            "     2026-09-14 ~16:4x named two leak sites from the shape of the code " + "y" * 600 + "\n"
            "  42 new correction(s) since last run: 2 still novel (no sibling), 40 fit an existing family.\n"
            "\n(report-only; run with --write to emit mistake_families.json as reflex content)\n"
            "03:31:09 step: next thing\n  this line is not part of the block\n")
    quiet = "03:29:50 step: mistake_graph watch\n" + said + head + "  No change since the last snapshot.\n\n(report-only)\n"
    bad = ("03:29:50 step: mistake_graph watch\n" + said +
           "  ** WATCH STATE FAILED - prior preserved; recurrence verdict suppressed: watch observation removes 9 "
           "correction id(s); rerun explicitly with --allow-removals after verifying the source\n\n"
           "03:31:09 mistake graph watch failed (nonfatal, exit=1)\n")
    none = "03:00:00 dream skipped: another dream holds the lock\n"

    def logs_of(*texts):
        for n in os.listdir(lg):
            os.remove(os.path.join(lg, n))
        for k, t in enumerate(texts):                   # first argument = newest log
            with open(os.path.join(lg, "dream_202601%02d_023000.log" % (20 - k)), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(t)

    st = os.path.join(d, "absent_status.json")
    logs_of(good, bad, bad)
    w = watch_lines(logs=lg, status_path=st)
    j = "\n".join(w)
    ck("a published verdict is quoted with its log's name", "Its last verdict (dream_20260120_023000)" in j and "edited in place" in j)
    ck("a one-off that became recurring asks for its reflex tonight", "write its reflex tonight" in j and "Read the pair first" in j)
    ck("older failed logs behind a published one are not reported", "FAILED" not in j)
    ck("the block stops at its blank line and long lines are cut", "not part of the block" not in j and "report-only" not in j
       and max(len(x) for x in j.splitlines()) <= WATCH_LINE_CHARS + 60)
    ck("the status line is always there, even with no status file", any(x.startswith("Recurrence watch status:") for x in w))
    logs_of(bad, bad, none, bad, good)
    w = watch_lines(logs=lg, status_path=st)
    j = "\n".join(w)
    ck("failures are counted in a row across a log that says nothing", w[0].startswith("**The recurrence watch FAILED in the last 3 dream log(s) in a row**"))
    ck("the watch's own reason is given", "watch observation removes 9 correction id(s)" in w[0])
    ck("an older verdict is not shown as current when the newest logs failed", "Its last verdict" not in j and "reflex tonight" not in j)
    st2 = os.path.join(d, "status_newer.json")
    with open(st2, "w", encoding="utf-8") as fh:
        fh.write("{}")
    for n in os.listdir(lg):
        os.utime(os.path.join(lg, n), (1700000000, 1700000000))
    os.utime(st2, (1700009000, 1700009000))
    w = watch_lines(logs=lg, status_path=st2)
    ck("a status file newer than the failed logs: said to have published since, not FAILED",
       "has published since" in w[0] and "FAILED" not in w[0].replace("WATCH STATE FAILED", ""))
    os.utime(st2, (1699990000, 1699990000))
    ck("a status file older than the failed logs: FAILED", watch_lines(logs=lg, status_path=st2)[0].startswith("**The recurrence watch FAILED"))
    logs_of(quiet)
    j = "\n".join(watch_lines(logs=lg, status_path=st))
    ck("a quiet verdict is quoted and asks for nothing", "No change since the last snapshot" in j and "reflex tonight" not in j and "FAILED" not in j)
    logs_of(said + none)
    w = watch_lines(logs=lg, status_path=st)
    ck("words quoted on the runner's child-said line are neither a failure nor a verdict", len(w) == 1 and w[0].startswith("Recurrence watch status:"))
    ck("a missing log folder gives the status line only", len(watch_lines(logs=os.path.join(d, "nologs"), status_path=st)) == 1)
    s = summary_line(rs)
    ck("summary names the median, the sections, the lines and the stubs", "median" in s and "a mistake section in 2" in s and "a MISTAKES: line in 1" in s and "2 of the last 7" in s)
    ck("summary with nothing to judge says so", "no finished full dream" in summary_line([by["dream_2026_01_03_partial.md"]]))
    ck("a heading that only contains the letter m inside a word does not count", measure("## Methods and memory\n" + pad * 5)["share"] == 0.0)
    ck("'## M, kept warm' and '## Section M' count", measure("## M, kept warm\n" + pad)["share"] > 0.9 and measure("## Section M glance\n" + pad)["share"] > 0.9)
    ck("a missing folder gives no rows", rows(folder=os.path.join(d, "absent")) == [])
    bad = [n for n, ok in checks if not ok]
    for n, ok in checks:
        print(("ok   " if ok else "FAIL ") + n)
    print("PASS - %d checks" % len(checks) if not bad else "FAIL - %d of %d checks failed" % (len(bad), len(checks)))
    return 0 if not bad else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    rs = rows()
    if "--agenda" in argv:
        print("\n".join(agenda_lines(rs)))
        return 0
    if "--summary" not in argv:
        print("\n".join(table(rs)))
    print(summary_line(rs))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
