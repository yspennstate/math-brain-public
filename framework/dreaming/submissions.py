"""submissions.py - a private record of where each paper has been submitted, when, and where it stands.

One row per (paper, journal), so that a paper is never sent to two journals at once and never sent back to a
journal that has already decided on it. The record is SUBMISSIONS.jsonl in ~/.claude/paper_submissions/ (or the
file named by PW_SUBMISSIONS). Keep it out of paper repositories and public repositories.

  python submissions.py check "<title or a few words of it>"   exit 3 when the paper is in process somewhere
  python submissions.py add --title "..." --journal "..." --date 2026-01-15 [--id MS-123] [--status submitted]
                            [--account <which login>] [--agent <id>] [--note "..."]
  python submissions.py status <row id> <status> [--date ...] [--id MS-123] [--note "..."]
  python submissions.py looked <row id> [<row id> ...]          the journal's page was read today; nothing changed
  python submissions.py list [--open] [--paper "<words>"]
  python submissions.py render                                  rewrites SUBMISSIONS.md from the rows
  python submissions.py journal "<name or submission address>"  exit 3 for a journal on your own barred list

Statuses. In process (the paper may not go anywhere else): draft_started, submitted, under_review, revision.
Closed: accepted, declined, desk_returned, withdrawn, draft_deleted.
A journal with a closed row for a paper does not get that paper again.

Barred journals (optional): BARRED_JOURNALS.txt beside the record, one journal a line as
"<display name><TAB><regular expression>". add refuses an open row at a journal it matches; --force overrides.
"""
import datetime
import json
import os
import re
import sys

HOME = os.path.join(os.path.expanduser("~"), ".claude", "paper_submissions")
LEDGER = os.environ.get("PW_SUBMISSIONS") or os.path.join(HOME, "SUBMISSIONS.jsonl")
OPEN = ("draft_started", "submitted", "under_review", "revision")
CLOSED = ("accepted", "declined", "desk_returned", "withdrawn", "draft_deleted")
STOP = set("the a an of for and with on in to at by from its their is are every any all new some via over under into "
           "paper note case results result theory theorem problem problems model models version".split())


def toks(s):
    s = re.sub(r"\\[A-Za-z]+\*?|[{}$~]", " ", s or "").lower()
    return set(w for w in (re.sub(r"'s$", "", x) for x in re.findall(r"[a-z][a-z'-]{2,}", s)) if w not in STOP)


def same_paper(a, b):
    """Two titles name one paper when most of the distinctive words of the shorter one are in the other."""
    ta, tb = toks(a), toks(b)
    if not ta or not tb:
        return False
    hit = len(ta & tb)
    return hit >= 2 and hit >= 0.6 * min(len(ta), len(tb))


JSTOP = set("of the and its in on for".split())


def same_journal(a, b):
    """J. Appl. Probab. = Journal of Applied Probability = JAP; Adv. Appl. Probab. is another journal."""
    def tk(x):
        return [w for w in re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", x or "").lower()) if w not in JSTOP]
    ta, tb = tk(a), tk(b)
    if not ta or not tb:
        return False
    if ta == tb:
        return True
    for x, y in ((ta, tb), (tb, ta)):
        if len(x) == 1 and len(y) > 1 and x[0] == "".join(w[0] for w in y):
            return True
    return len(ta) == len(tb) and all(p.startswith(q) or q.startswith(p) for p, q in zip(ta, tb))


def barred_list():
    out = []
    try:
        with open(os.path.join(os.path.dirname(LEDGER), "BARRED_JOURNALS.txt"), encoding="utf-8") as f:
            for ln in f:
                if ln.strip() and not ln.startswith("#") and "\t" in ln:
                    name, pat = ln.rstrip("\n").split("\t", 1)
                    out.append((name.strip(), pat.strip()))
    except OSError:
        pass
    return out


def barred(journal):
    """The display name of the barred journal this names, or ''."""
    for name, pat in barred_list():
        try:
            if re.search(pat, journal or "", re.I):
                return name
        except re.error:
            pass
    return ""


def load(path=None):
    rows = []
    try:
        with open(path or LEDGER, encoding="utf-8") as f:
            for ln in f:
                ln = ln.strip()
                if ln:
                    try:
                        rows.append(json.loads(ln))
                    except ValueError:
                        pass
    except OSError:
        pass
    return rows


def save(rows, path=None):
    p = path or LEDGER
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    os.replace(tmp, p)


def find(rows, words):
    """Rows of the paper these words name: by title, by an alias, or by the paper key."""
    out = []
    few = toks(words) if len(toks(words)) < 2 else None      # one distinctive word: any title that contains it
    for r in rows:
        names = [r.get("title", "")] + list(r.get("aliases") or [])
        if few is not None:
            if few and any(all(w in n.lower() for w in few) for n in names):
                out.append(r)
            continue
        if toks(words) & set(w.lower() for w in (r.get("unlike") or [])):   # a look-alike title: another paper
            continue
        if words.strip().lower() == str(r.get("paper", "")).lower() or any(same_paper(words, n) for n in names):
            out.append(r)
    return out


def verdict(rows, words):
    """(open rows, closed rows) for the paper named by the words."""
    got = find(rows, words)
    return [r for r in got if r.get("status") in OPEN], [r for r in got if r.get("status") not in OPEN]


def line(r):
    return "%s | \"%s\" | %s%s | submitted %s | %s%s" % (
        r.get("rid", "?"), r.get("title", "?")[:80], r.get("journal", "?"), (" " + r["ms_id"]) if r.get("ms_id") else "", r.get("submitted") or "?",
        r.get("status", "?"), (" (" + r["status_note"] + ")") if r.get("status_note") else "")


def render(rows):
    def tab(rs):
        out = ["| Row | Paper | Journal | Number | Submitted | Status | Last looked |", "|---|---|---|---|---|---|---|"]
        for r in sorted(rs, key=lambda x: (x.get("title", "").lower(), x.get("submitted") or "")):
            out.append("| %s | %s | %s | %s | %s | %s | %s |" % (
                r.get("rid", ""), r.get("title", ""), r.get("journal", ""), r.get("ms_id", ""), r.get("submitted", ""),
                r.get("status", "") + ((": " + r["status_note"]) if r.get("status_note") else ""), r.get("checked", "")))
        return out
    op = [r for r in rows if r.get("status") in OPEN]
    cl = [r for r in rows if r.get("status") not in OPEN]
    txt = ["# Where each paper has been submitted", "",
           "Private. Rendered from SUBMISSIONS.jsonl by submissions.py on %s; edit the rows with the script, not this file."
           % datetime.date.today().isoformat(), "",
           "## In process: these papers go nowhere else (%d)" % len(op), ""] + tab(op) + [
           "", "## Closed: these journals do not get these papers again (%d)" % len(cl), ""] + tab(cl) + [""]
    os.makedirs(os.path.dirname(LEDGER) or ".", exist_ok=True)
    with open(os.path.join(os.path.dirname(LEDGER), "SUBMISSIONS.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(txt))


class Lock(object):
    """One writer at a time: several agents may record submissions, and a row lost here is a paper sent twice."""
    def __init__(self):
        self.p = LEDGER + ".lock"

    def __enter__(self):
        import time
        os.makedirs(os.path.dirname(self.p) or ".", exist_ok=True)
        for _ in range(240):
            try:
                fd = os.open(self.p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, str(os.getpid()).encode())
                os.close(fd)
                return self
            except FileExistsError:
                try:
                    if time.time() - os.path.getmtime(self.p) > 180:      # a writer that died
                        os.remove(self.p)
                        continue
                except OSError:
                    pass
                time.sleep(0.5)
        raise SystemExit("the record is locked by another writer (%s); nothing was written, run it again" % self.p)

    def __exit__(self, *a):
        try:
            os.remove(self.p)
        except OSError:
            pass


def _opt(argv, name, default=""):
    if name in argv:
        i = argv.index(name)
        if i + 1 < len(argv):
            return argv[i + 1]
    return default


def main(argv):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            pass
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 0
    cmd, today = argv[0], datetime.date.today().isoformat()
    if cmd in ("add", "status", "looked"):                  # read, change and write under one lock
        with Lock():
            return _run(cmd, argv, load(), today)
    return _run(cmd, argv, load(), today)


def _run(cmd, argv, rows, today):
    if cmd == "journal":
        name = " ".join(argv[1:]).strip()
        if not name:
            print("journal needs a journal's name or its submission address")
            return 2
        bj = barred(name)
        if bj:
            print("BARRED: %s is on your barred list (BARRED_JOURNALS.txt)." % bj)
            return 3
        print("Not on the barred list. Also check this record for the paper (check \"<title>\") before choosing it.")
        return 0
    if cmd == "check":
        words = " ".join(a for a in argv[1:] if not a.startswith("--"))
        if not toks(words):
            print("check needs the title, or a distinctive word of it")
            return 2
        op, cl = verdict(rows, words)
        if op:
            print("IN PROCESS - a row whose title matches these words is open; if it is this paper, it goes nowhere else:")
            for r in op:
                print("  " + line(r))
        if cl:
            print("Closed rows (do not send it to these journals again):")
            for r in cl:
                print("  " + line(r))
        if not op and not cl:
            print("No row names this paper. Read SUBMISSIONS.md once for a paper filed under another title "
                  "before the first submission.")
        elif not op:
            print("Not in process anywhere on this record.")
        return 3 if op else 0
    if cmd == "add":
        title, journal = _opt(argv, "--title"), _opt(argv, "--journal")
        if not title or not journal:
            print("add needs --title and --journal")
            return 2
        op, cl = verdict(rows, title)
        status = _opt(argv, "--status", "submitted")
        if status not in OPEN + CLOSED:
            print("status is one of: " + ", ".join(OPEN + CLOSED))
            return 2
        bj = barred(journal)
        if bj and status in OPEN and "--force" not in argv:
            print("REFUSED: %s is on your barred list (BARRED_JOURNALS.txt). Choose another journal, or pass --force." % bj)
            return 3
        same_j = [r for r in op + cl if same_journal(r.get("journal", ""), journal)]
        if same_j and "--force" not in argv:
            if same_j[0].get("status") in OPEN:
                print("A row for this paper at this journal exists; change it with: status %s <status>" % same_j[0].get("rid"))
            else:
                print("REFUSED: this journal already has a closed row for this paper; it does not get the paper again.")
            print("  " + line(same_j[0]))
            return 3
        if op and status in OPEN and "--force" not in argv:
            print("REFUSED: this paper is in process elsewhere. A paper is at one journal at a time.")
            for r in op:
                print("  " + line(r))
            print("If it was withdrawn or the journal decided, record that first (status <row> withdrawn|declined); "
                  "--force overrides.")
            return 3
        n = 1 + max([int(m.group(1)) for m in (re.match(r"S(\d+)$", str(r.get("rid", ""))) for r in rows) if m] or [0])
        key = (op + cl)[0].get("paper") if (op + cl) else re.sub(r"[^a-z0-9]+", "-", " ".join(sorted(toks(title), key=title.lower().find)[:5])).strip("-")
        row = {"rid": "S%04d" % n, "paper": key, "title": title, "journal": journal, "ms_id": _opt(argv, "--id"),
               "submitted": _opt(argv, "--date", today), "status": status, "status_date": _opt(argv, "--date", today),
               "status_note": _opt(argv, "--note"), "account": _opt(argv, "--account"), "agent": _opt(argv, "--agent"),
               "checked": today, "source": _opt(argv, "--source", "recorded at submission"), "history": []}
        rows.append(row)
        save(rows)
        render(rows)
        print("recorded " + line(row))
        return 0
    if cmd == "status":
        if len(argv) < 3 or argv[2] not in OPEN + CLOSED:
            print("status <row id> <%s>" % "|".join(OPEN + CLOSED))
            return 2
        for r in rows:
            if r.get("rid") == argv[1]:
                r.setdefault("history", []).append({"status": r.get("status"), "date": r.get("status_date"), "note": r.get("status_note")})
                r["status"], r["status_date"] = argv[2], _opt(argv, "--date", today)
                r["status_note"], r["checked"] = _opt(argv, "--note"), today
                if _opt(argv, "--id"):
                    r["ms_id"] = _opt(argv, "--id")
                save(rows)
                render(rows)
                print("now " + line(r))
                return 0
        print("no row " + argv[1])
        return 2
    if cmd == "looked":
        for r in rows:
            if r.get("rid") in argv[1:]:
                r["checked"] = today
        save(rows)
        render(rows)
        return 0
    if cmd == "list":
        words = _opt(argv, "--paper")
        rs = find(rows, words) if words else rows
        if "--open" in argv:
            rs = [r for r in rs if r.get("status") in OPEN]
        for r in sorted(rs, key=lambda x: x.get("title", "").lower()):
            print(line(r))
        print("%d rows" % len(rs))
        return 0
    if cmd == "render":
        render(rows)
        print("SUBMISSIONS.md written, %d rows" % len(rows))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
