# -*- coding: utf-8 -*-
"""Record today's breadth answers in the campaign's intake ledgers (claude-322bc92e, 10 Oct 2026; his 08:52 "record how
many open problems were solved, in the brain"). The ledgers' own convention: a problem re-recorded with its result is a
new row with a later recorded_at (prob_cover.py keeps the newest). One row per answered problem: the referee's verdict
and claim, the solver's evidence status; DROP answers are recorded as attempted, the problem stays open."""
import glob
import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGERS = "~/<private-repo>/06_math_research/probability_1000_intake_%s_*/problems.jsonl"
STAMP = "2026-10-10T11:00:00+03:00"


def parse(txt):
    m = re.search(r"\{.*\}", txt, re.S)
    if not m:
        return {}
    s = m.group(0)
    for end in range(len(s), 0, -1):
        if s[end - 1] == "}":
            try:
                return json.loads(s[:end])
            except ValueError:
                continue
    return {}


def main():
    q = {json.loads(l)["target_id"]: json.loads(l) for l in io.open(os.path.join(HERE, "QUEUE_ALL_OPEN.jsonl"),
                                                                      encoding="utf-8") if l.strip()}
    out, tally = {}, {}
    for f in sorted(glob.glob(os.path.join(HERE, "results", "*.txt"))):
        pid = os.path.basename(f)[:-4]
        j = parse(io.open(f, encoding="utf-8", errors="replace").read())
        ev = str(j.get("evidence_status") or "").lower()
        ref = os.path.join(HERE, "results", "%s.referee.md" % pid)
        rt = io.open(ref, encoding="utf-8").read() if os.path.exists(ref) else ""
        v = (re.findall(r"VERDICT:\s*(KEEP|FIX|DROP)", rt) or [None])[-1]
        claim = (re.findall(r"CLAIM:\s*(.+)", rt) or [""])[-1].strip()
        if "literature" in ev:
            status, result = "resolved_in_literature_2026_10_10", "solver reports it solved in the literature: %s" % (
                json.dumps(j.get("source_checks"), ensure_ascii=False)[:600])
        elif v == "KEEP":
            status = ("counterexample_2026_10_10" if "counterexample" in ev else
                      "answered_2026_10_10" if "proved" in ev else "partially_answered_2026_10_10")
            result = claim
        elif v in ("DROP", "FIX"):
            status, result = "attempted_2026_10_10", "answer %s by the Claude referee; problem stays open" % v
        else:
            continue
        r = q.get(pid, {})
        tag = re.match(r"([A-Z]+)", pid).group(1)
        row = {"schema": "prob1000-problem-v1", "problem_id": pid, "title": r.get("title"),
               "statement": r.get("problem_statement"), "source_id": (r.get("source") or {}).get("source_id"),
               "locator": (r.get("source") or {}).get("locator"), "current_status": status, "result_status": result,
               "verification": "Codex gpt-6.1-sol (max) solver; sealed Claude (claude-opus-5-5) referee verdict %s; not "
                               "refereed by a person; files in math-open-problems probability_campaigns/breadth_2026-10-10"
                               % (v or "n/a"),
               "recorded_at": STAMP, "intake": "breadth_2026_10_10", "admitted": True}
        out.setdefault(tag, []).append(row)
        tally[status] = tally.get(status, 0) + 1
    for tag, rows in out.items():
        files = glob.glob(LEDGERS % tag)
        if len(files) != 1:
            print("ledger for", tag, "not unique:", files)
            continue
        raw = open(files[0], "rb").read()
        nl = b"\r\n" if b"\r\n" in raw else b"\n"
        with open(files[0], "ab") as fh:
            if raw and not raw.endswith(b"\n"):
                fh.write(nl)
            for row in rows:
                fh.write(json.dumps(row, ensure_ascii=False).encode("utf-8") + nl)
        print("appended %d rows to %s" % (len(rows), files[0].replace("\\", "/").split("06_math_research/")[-1]))
    print(json.dumps(tally))


if __name__ == "__main__":
    main()
