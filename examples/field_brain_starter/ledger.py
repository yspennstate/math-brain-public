"""Read and write the request ledger without installing the package.

    python ledger.py list                                  # open requests, the ones asked most first
    python ledger.py list --all                            # every request, with its status
    python ledger.py ask "How long should the harbour film be?"
    python ledger.py link req_0060ef7a1d15 project_harbour_film_cut_to_twelve_minutes_2026_03_10 answered_by
    python ledger.py link req_0060ef7a1d15 method_one_test_shot_before_any_long_render_2026_03_19 produced
    python ledger.py drop req_0060ef7a1d15 --note "the festival was cancelled"
    python ledger.py list --repeats                        # asked on two or more days, the latest first
    python ledger.py list --unseen                         # answered or dropped, not yet read by the owner
    python ledger.py seen req_0060ef7a1d15                 # the owner's mark; `seen all` marks every unseen one

`seen` belongs to the person who asked. Done means the agent finished; seen means the owner has read the result, so
the unseen list is the owner's reading queue (docs/brain-building/task-checklist.md). An agent never runs `seen`.

The ledger is requests.jsonl beside this script, or --ledger, or $MATH_BRAIN_REQUESTS (see
docs/prompts-as-nodes.md). Every command appends one event in the format math_brain.requests writes, so the
library, recall.py, hooks/request_hook.py and dream/make_agenda.py all read the result. Nothing is rewritten or
removed: a mistaken link is answered by a later event, never by editing the file.

`link` is what the dream uses on section 7 of its agenda: `answered_by` when a record answers the request,
`produced` when a record is work toward it. It refuses a record that is not in memory/ and a request that is not in
the ledger; a request id may be shortened to any prefix that names one request. Standard library only.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "hooks"))
sys.path.insert(0, HERE)   # python -I leaves the script's own folder off the path
import recall  # noqa: E402
from request_hook import normalize, redact, request_id  # noqa: E402


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def append(ledger, event):
    os.makedirs(os.path.dirname(os.path.abspath(ledger)), exist_ok=True)
    with open(ledger, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def find(reqs, rid):
    hits = [k for k in reqs if k == rid] or [k for k in reqs if k.startswith(rid)]
    if len(hits) != 1:
        sys.exit("%s request matches %s" % ("no" if not hits else "more than one", rid))
    return hits[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ledger", default=os.environ.get("MATH_BRAIN_REQUESTS") or os.path.join(HERE, "requests.jsonl"))
    ap.add_argument("--dir", default=os.environ.get("BRAIN_MEM_DIR", os.path.join(HERE, "memory")))
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("list")
    p.add_argument("--all", action="store_true", help="answered and dropped requests too")
    p.add_argument("--unseen", action="store_true", help="answered or dropped, not yet seen by the owner")
    p.add_argument("--repeats", action="store_true",
                   help="asked on two or more days, the most recently asked first: what the owner keeps saying")
    p = sub.add_parser("ask")
    p.add_argument("text")
    p = sub.add_parser("link")
    p.add_argument("id")
    p.add_argument("record")
    p.add_argument("rel", choices=("answered_by", "produced"))
    p = sub.add_parser("drop")
    p.add_argument("id")
    p.add_argument("--note", default="")
    p = sub.add_parser("seen")
    p.add_argument("id", help="a request id or prefix, or 'all' for every unseen one")
    a = ap.parse_args()

    reqs = recall.load_requests(a.ledger) if os.path.exists(a.ledger) else {}
    unseen = [r for r in reqs.values() if r["status"] != "open" and not r["seen"]]
    if a.cmd == "list":
        if a.unseen:
            rows = unseen
        elif a.repeats:
            rows = [r for r in reqs.values() if len(r["days"]) >= 2]
        else:
            rows = [r for r in reqs.values() if a.all or r["status"] == "open"]
        if a.repeats:
            # a request repeated on another day usually means the first answer did not land: newest first, so the
            # agent reads what is being said now before what was said last month
            rows.sort(key=lambda r: r["last"], reverse=True)
        else:
            rows.sort(key=lambda r: (-r["times"], r["first"]))
        for r in rows:
            recall.show_request(r)
        print("%d of %d requests" % (len(rows), len(reqs)))
    elif a.cmd == "ask":
        text = redact(a.text).strip()
        if not normalize(text):
            sys.exit("an empty request")
        append(a.ledger, {"op": "ask", "id": request_id(text), "text": text, "role": "researcher", "at": now()})
        print(request_id(text))
    elif a.cmd == "link":
        rid = find(reqs, a.id)
        if a.record not in recall.load(a.dir):
            sys.exit("no record %s in %s" % (a.record, a.dir))
        append(a.ledger, {"op": "link", "id": rid, "node": a.record, "rel": a.rel, "at": now()})
        print("%s %s %s" % (rid, a.rel, a.record))
    elif a.cmd == "drop":
        rid = find(reqs, a.id)
        append(a.ledger, {"op": "status", "id": rid, "status": "dropped", "note": a.note, "at": now()})
        print("%s dropped" % rid)
    elif a.cmd == "seen":
        ids = [r["id"] for r in unseen] if a.id == "all" else [find(reqs, a.id)]
        if reqs.get(ids[0] if ids else "", {}).get("status") == "open":
            sys.exit("%s is still open: there is no result to have seen yet" % ids[0])
        for rid in ids:
            append(a.ledger, {"op": "seen", "id": rid, "at": now()})
            print("%s seen" % rid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
