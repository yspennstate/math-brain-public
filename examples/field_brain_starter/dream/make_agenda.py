"""Build a dream agenda for the starter brain.

A dream is an offline pass over the store: an agent reads what changed, checks it against what was already known,
and writes back links, corrections and reflexes. The agent works best from a short agenda that says what to look
at. This script builds that agenda from memory/ alone, using only the standard library.

    python dream/make_agenda.py                 # write dream/DREAM_AGENDA.md
    python dream/make_agenda.py --today 2026-04-03 --fresh 7

The sections, in the order a dreaming agent should work through them:

1. Mistakes to sit with - each dated correction in MISTAKES.md, and whether its record already carries a
   "How to apply" line. A mistake with no rule for next time is the first thing to fix.
2. Fresh records - written in the last N days. Check each against older records: does it contradict one,
   refine one, or repeat one?
3. Superseded pairs - a record marked superseded_by, and the record that replaced it. Confirm that every record
   which links the old one also mentions the new one.
4. Provisional records - claims not yet checked. Either find the evidence or leave the status as it is.
5. Open questions - records that ask instead of state. Has anything newer answered one?
6. Unlinked records - nothing links to them and they link to nothing. Recall finds them only by their own words.
7. Requests still waiting (when a request ledger exists: --requests, $MATH_BRAIN_REQUESTS, or requests.jsonl
   beside memory/, the ledger math_brain.requests keeps) - the questions
   the researcher asked that no record answers yet, the ones asked more than once first. Was one answered by a
   record this dream should link to it?
"""
import argparse
import datetime as dt
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MEM = os.path.join(ROOT, "memory")
SKIP = {"MEMORY.md", "MISTAKES.md"}
LINK = re.compile(r"\[\[([a-z0-9_]+)\]\]")
DATE = re.compile(r"(\d{4})_(\d{2})_(\d{2})$")


def read_record(path):
    text = open(path, encoding="utf-8").read()
    head, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        for line in text[3:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                head[k.strip()] = v.strip()
        body = text[end + 4:]
    return head, body


def open_requests(path):
    """Fold a request ledger (append-only JSON lines) into its open requests, without importing math_brain.

    The fold follows math_brain.requests: an ask adds or counts a request, an answered_by link answers it, a
    status event sets its status, and asking again after an answer reopens it. Unreadable lines are skipped.
    """
    reqs = {}
    for line in open(path, encoding="utf-8"):
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        r = reqs.get(ev.get("id"))
        if ev.get("op") == "ask" and "text" in ev and "at" in ev:
            if r is None:
                r = reqs[ev["id"]] = dict(id=ev["id"], text=ev["text"], first=ev["at"], last=ev["at"], times=0,
                                          status="open", produced=set())
            r["times"] += 1
            r["first"], r["last"] = min(r["first"], ev["at"]), max(r["last"], ev["at"])
            if r["status"] == "answered" and ev.get("reopen", True):
                r["status"] = "open"
        elif r is not None and ev.get("op") == "link":
            r["last"] = max(r["last"], ev.get("at", ""))
            if ev.get("rel") == "produced":
                r["produced"].add(ev.get("node"))
            if ev.get("rel") == "answered_by" and r["status"] == "open":
                r["status"] = "answered"
        elif r is not None and ev.get("op") == "status":
            r["status"] = ev.get("status", r["status"])
    return sorted((r for r in reqs.values() if r["status"] == "open"), key=lambda r: (-r["times"], r["first"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", help="YYYY-MM-DD; defaults to the newest record's date")
    ap.add_argument("--fresh", type=int, default=7, help="days that count as fresh")
    ap.add_argument("--out", default=os.path.join(HERE, "DREAM_AGENDA.md"))
    ap.add_argument("--requests", default=os.environ.get("MATH_BRAIN_REQUESTS", os.path.join(ROOT, "requests.jsonl")),
                    help="a request ledger; adds section 7 when the file exists (default $MATH_BRAIN_REQUESTS,"
                         " else requests.jsonl beside memory/)")
    ap.add_argument("--max-requests", type=int, default=15)
    a = ap.parse_args()

    recs = {}
    for f in sorted(os.listdir(MEM)):
        if not f.endswith(".md") or f in SKIP:
            continue
        head, body = read_record(os.path.join(MEM, f))
        slug = head.get("name", f[:-3])
        m = DATE.search(slug)
        when = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
        recs[slug] = dict(head=head, body=body, when=when, links=set(LINK.findall(body)))

    today = dt.date.fromisoformat(a.today) if a.today else max(r["when"] for r in recs.values() if r["when"])
    inbound = {s: set() for s in recs}
    for s, r in recs.items():
        for t in r["links"]:
            if t in inbound:
                inbound[t].add(s)

    out = ["# Dream agenda", "", "Built %s from %d records. Work through the sections in order; write back what you"
           " change, with its date and reason." % (today.isoformat(), len(recs)), ""]

    out += ["## 1. Mistakes to sit with", ""]
    for line in open(os.path.join(MEM, "MISTAKES.md"), encoding="utf-8"):
        if not line.startswith("- "):
            continue
        targets = LINK.findall(line)
        ruled = any("How to apply" in recs[t]["body"] for t in targets if t in recs)
        out.append("%s  \n  -> %s" % (line.strip(), "has a rule for next time; check it is specific enough to act on"
                                     if ruled else "NO rule for next time yet: write one, with its reason"))
    out.append("")

    out += ["## 2. Fresh records (last %d days)" % a.fresh, ""]
    fresh = sorted((r["when"], s) for s, r in recs.items() if r["when"] and (today - r["when"]).days <= a.fresh)
    for when, s in reversed(fresh):
        out.append("- %s `%s` - %s" % (when.isoformat(), s, recs[s]["head"].get("description", "")))
    out += ["", "For each: does it contradict, refine or repeat an older record? Link it to the record it"
            " touches.", ""]

    out += ["## 3. Superseded pairs", ""]
    for s, r in sorted(recs.items()):
        new = r["head"].get("superseded_by")
        if not new:
            continue
        stale = sorted(t for t in inbound[s] if t != new and new not in recs.get(t, {}).get("links", ()))
        out.append("- `%s` -> `%s`" % (s, new))
        out.append("  - records that link the old one but not its replacement: %s" % (", ".join(stale) or "none"))
    out.append("")

    out += ["## 4. Provisional records", ""]
    for s, r in sorted(recs.items()):
        if r["head"].get("status") == "provisional":
            out.append("- `%s` - %s" % (s, r["head"].get("description", "")))
    out.append("")

    out += ["## 5. Open questions", ""]
    for s, r in sorted(recs.items()):
        if "open_question" in s or r["head"].get("description", "").lower().startswith("open"):
            newer = sorted(t for t, q in recs.items() if q["when"] and r["when"] and q["when"] > r["when"])
            out.append("- `%s` - newer records to read for an answer: %s" % (s, ", ".join(newer) or "none"))
    out.append("")

    out += ["## 6. Unlinked records", ""]
    for s, r in sorted(recs.items()):
        if not r["links"] and not inbound[s]:
            out.append("- `%s` - %s" % (s, r["head"].get("description", "")))
    out.append("")

    if a.requests and os.path.exists(a.requests):
        waiting = open_requests(a.requests)
        out += ["## 7. Requests still waiting", ""]
        for r in waiting[: a.max_requests]:
            work = "%d produced" % len(r["produced"]) if r["produced"] else "nothing produced"
            out.append("- `%s` asked %dx, first %s, last touched %s, %s: %s"
                       % (r["id"], r["times"], r["first"][:10], r["last"][:10], work, r["text"][:140]))
        if len(waiting) > a.max_requests:
            out += ["", "And %d more; `python -m math_brain.requests backlog` lists them all."
                    % (len(waiting) - a.max_requests)]
        out += ["", "For each: does a record answer it? If one does, link it (`requests link <id> <record>"
                " answered_by`); if a record is partial work toward it, link it as `produced`.", ""]

    open(a.out, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    print("wrote %s (%d records, %d fresh)" % (a.out, len(recs), len(fresh)))


if __name__ == "__main__":
    main()
