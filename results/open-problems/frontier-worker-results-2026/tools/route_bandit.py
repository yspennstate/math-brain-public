"""Route choice on a frontier row as a bandit (research statement, section 6).

Each route r on a row has an unknown probability p_r of yielding a useful step. Its posterior is Beta(a_r, b_r):
  prior   - the base rate of finished routes across every row (done/settled against dead), worth PRIOR_MASS
            pseudo-attempts, plus half-weight evidence from terminal routes on OTHER rows whose words match r
            (the record shared across agents and days);
  data    - moves on this row attributed to r: a progress move (moved, narrowed, result, partial) is a success,
            a move recording a failed attempt (tried, failed, dead-end, obstruction, refuted) is a failure.
            A move written with `record` names its route exactly; an older move is attributed by word overlap
            (frontier.sim >= ATTR) to the single best-matching route, or to none.
Thompson sampling over these posteriors gives the order in which to try the live routes. A route is flagged DROP
when P(p_r > FLOOR) < LEVEL, i.e. the record is confident it rarely pays.

Commands
  order  TNNN [--seed N] [--json]      live routes in Thompson order with posterior mean and P(p>floor)
  record TNNN --route R --outcome useful|tried --by ID [--text T]   append a route-tagged move (no frontier.py change)
  report [--json]                      every row: live routes, how many have data, how many would be dropped
"""
import argparse
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier as F  # noqa: E402

PRIOR_MASS = 2.0      # pseudo-attempts carried by the cross-row base rate
TRANSFER_W = 0.5      # weight of one matching terminal route on another row
TRANSFER_CAP = 4.0    # at most this many pseudo-attempts from transfer, so a crowded family cannot drown the row's own data
ATTR = 0.34           # same threshold frontier.py check uses for "close to a known route"
FLOOR = 0.10
LEVEL = 0.05
SUCCESS_KINDS = set(F.PROGRESS) | {"result", "partial", "useful"}
FAIL_WORDS = ("tried", "fail", "dead", "obstruct", "refut", "no_progress", "stuck")
SUCCESS_STATUS = ("done", "settled")


def is_fail(kind):
    k = (kind or "").lower()
    return any(w in k for w in FAIL_WORDS)


def terminal_routes():
    """(row, route text, success?) for every finished or dead route on every row."""
    out = []
    for row in F.list_rows():
        for r in F.routes(row):
            st = (r.get("status") or "").lower()
            if st.startswith(SUCCESS_STATUS):
                out.append((row, r.get("route") or "", True))
            elif st.startswith("dead"):
                out.append((row, r.get("route") or "", False))
    return out


def base_rate(term):
    s = sum(1 for t in term if t[2])
    return (s + 1.0) / (len(term) + 2.0)


def posteriors(row, term=None):
    row = row.upper()
    term = terminal_routes() if term is None else term
    p0 = base_rate(term)
    live = [r for r in F.routes(row) if (r.get("status") or "").lower().startswith("live")]
    stats = {}
    for r in live:
        txt = r.get("route") or ""
        a, b = PRIOR_MASS * p0, PRIOR_MASS * (1 - p0)
        ta = tb = 0.0
        for orow, otxt, ok in term:
            if orow == row:
                continue
            if F.sim(txt, otxt) >= ATTR:
                if ok:
                    ta += TRANSFER_W
                else:
                    tb += TRANSFER_W
        tot = ta + tb
        if tot > TRANSFER_CAP:
            ta, tb = ta * TRANSFER_CAP / tot, tb * TRANSFER_CAP / tot
        stats[txt.strip().lower()] = {"route": txt, "by": r.get("by", "?"), "a": a + ta, "b": b + tb,
                                      "succ": 0, "fail": 0, "transfer": round(tot, 1)}
    keys = list(stats)
    for m in F.jsonl(os.path.join(F.rowdir(row), "moves.jsonl")):
        kind = (m.get("kind") or "").lower()
        ok = kind in SUCCESS_KINDS
        bad = is_fail(kind)
        if not (ok or bad):
            continue
        tag = (m.get("route") or "").strip().lower()
        key = tag if tag in stats else None
        if key is None and not tag:
            text = " ".join(str(m.get(k) or "") for k in ("text", "claim", "summary"))
            best = max(((F.sim(text, stats[k]["route"]), k) for k in keys), default=(0.0, None))
            if best[0] >= ATTR:
                key = best[1]
        if key is None:
            continue
        if ok:
            stats[key]["a"] += 1
            stats[key]["succ"] += 1
        else:
            stats[key]["b"] += 1
            stats[key]["fail"] += 1
    return p0, list(stats.values())


def prob_above(a, b, floor, n=4000, rng=None):
    rng = rng or random.Random(0)
    return sum(1 for _ in range(n) if rng.betavariate(a, b) > floor) / float(n)


def order(row, seed=None, term=None):
    p0, st = posteriors(row, term)
    rng = random.Random(seed)
    for s in st:
        s["draw"] = rng.betavariate(s["a"], s["b"])
        s["mean"] = s["a"] / (s["a"] + s["b"])
        s["p_above"] = prob_above(s["a"], s["b"], FLOOR)
        s["drop"] = s["p_above"] < LEVEL
    st.sort(key=lambda s: -s["draw"])
    return p0, st


def cmd_order(a):
    p0, st = order(a.row, a.seed)
    if a.json:
        print(json.dumps({"row": a.row.upper(), "base_rate": p0, "routes": st}, ensure_ascii=False, indent=1))
        return
    print("%s: %d live routes, cross-row base rate %.3f (try in this order)" % (a.row.upper(), len(st), p0))
    for i, s in enumerate(st, 1):
        print("%2d. draw %.3f mean %.3f P(p>%.2f)=%.2f  +%d/-%d transfer %.1f%s  %s (%s)" % (
            i, s["draw"], s["mean"], FLOOR, s["p_above"], s["succ"], s["fail"], s["transfer"],
            "  DROP" if s["drop"] else "", s["route"][:110], s["by"]))


def cmd_record(a):
    if a.outcome not in ("useful", "tried"):
        sys.exit("outcome must be useful or tried")
    rec = {"at": F.now(), "by": a.by, "kind": a.outcome, "route": a.route, "claim": "", "text": a.text or ""}
    F.append(os.path.join(F.rowdir(a.row), "moves.jsonl"), rec)
    print(json.dumps(rec, ensure_ascii=False))


def cmd_report(a):
    term = terminal_routes()
    rows, tot = [], {"rows": 0, "live": 0, "with_data": 0, "drop": 0}
    for row in F.list_rows():
        p0, st = order(row, 0, term)
        if not st:
            continue
        wd = sum(1 for s in st if s["succ"] + s["fail"])
        dr = sum(1 for s in st if s["drop"])
        rows.append({"row": row, "live": len(st), "with_data": wd, "drop": dr})
        tot["rows"] += 1
        tot["live"] += len(st)
        tot["with_data"] += wd
        tot["drop"] += dr
    tot["terminal_routes"] = len(term)
    tot["base_rate"] = round(base_rate(term), 4)
    if a.json:
        print(json.dumps({"total": tot, "rows": rows}, indent=1))
    else:
        print(json.dumps(tot))
        for r in sorted(rows, key=lambda r: -r["live"])[:25]:
            print("%s live %d with_data %d drop %d" % (r["row"], r["live"], r["with_data"], r["drop"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("order")
    p.add_argument("row")
    p.add_argument("--seed", type=int)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_order)
    p = sp.add_parser("record")
    p.add_argument("row")
    p.add_argument("--route", required=True)
    p.add_argument("--outcome", required=True)
    p.add_argument("--by", required=True)
    p.add_argument("--text")
    p.set_defaults(fn=cmd_record)
    p = sp.add_parser("report")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_report)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
