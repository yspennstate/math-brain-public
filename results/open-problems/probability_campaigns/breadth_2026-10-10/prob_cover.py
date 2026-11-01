# -*- coding: utf-8 -*-
"""Every probability open problem we hold, against the workers and the math brain (claude-322bc92e, 10 Oct 2026, his
07:3x ask T-20261010-052: "make sure they are working on solving open problems in probability theory, all of the ones
we have, and add nodes to the brain for the problems we solve").

Reads the seven intake ledgers of the 1,000-problem campaign (brain repo 06_math_research/probability_1000_intake_*),
the 300 wave's targets and the live math store (read only), and writes beside this file:
  COVERAGE.md              counts, and every result of ours with whether the store holds a node for it
  SOLVED_NEEDS_NODE.jsonl  our results with no node yet (the node step reads this)
  QUEUE_ALL_OPEN.jsonl     one self-contained solver brief per open problem the 300 wave does not cover, ranked,
                           in the KAGGLE_QUEUE.jsonl schema (gpt-6.1-sol, max reasoning, fast tier)
The ledgers hold public research problems from published sources; no test material is read or written.
"""
import collections
import glob
import io
import json
import os
import re
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGERS = "~/<private-repo>/06_math_research/probability_1000_intake_*/problems.jsonl"
STORE = "~/math-brain-build/local/population/brain.sqlite3"
WAVE = "~/brain_workers/teams/PROBABILITY300_20261010/ASSIGNMENTS.json"
OURS = ("answered", "refuted", "settled", "resolved_2026", "partially_solved", "reduced", "partially_refuted",
        "corrected_and_partially")
CLOSED = ("resolved_in_literature", "resolved_in_source", "closed_published", "duplicate", "not_well_posed",
          "no_resolution_found")          # the last: the source itself turned out not to pose it as open
# a remark or question in a recent paper has been the most tractable kind (the 13-14 Sep results came from H, I, F)
LEDGER_RANK = {"I": 0, "H": 1, "F": 2, "E": 3, "G": 4, "D": 5, "C": 6}


def ledger_rows():
    rows = []
    for f in sorted(glob.glob(LEDGERS)):
        tag = re.search(r"intake_([A-Za-z]+)_", f.replace("\\", "/")).group(1)
        tag = "C" if tag == "claude" else tag
        for line in io.open(f, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                r["_ledger"] = tag
                rows.append(r)
    return rows


def store_text():
    db = sqlite3.connect("file:%s?mode=ro" % STORE, uri=True, timeout=60)
    return [p for (p,) in db.execute("select payload_json from claims")]


def main():
    rows = ledger_rows()
    claims = store_text()
    blob = "\n".join(claims)
    wave = {a["target_id"] for a in json.load(io.open(WAVE, encoding="utf-8"))}
    # duplicate ids across a ledger's own rows (a problem re-recorded with its result) collapse to the newest row
    by_id = collections.OrderedDict()
    for r in rows:
        by_id[r["problem_id"]] = r if r["problem_id"] not in by_id else (
            r if str(r.get("recorded_at", "")) >= str(by_id[r["problem_id"]].get("recorded_at", "")) else by_id[r["problem_id"]])
    ours, closed, open_, cls = [], [], [], collections.Counter()
    for pid, r in by_id.items():
        st = str(r.get("current_status") or "")
        if any(st.startswith(s) for s in OURS):
            ours.append(r)
            cls["our result"] += 1
        elif any(st.startswith(s) for s in CLOSED):
            closed.append(r)
            cls["closed (literature, duplicate, not posed)"] += 1
        else:
            open_.append(r)
            cls["open"] += 1
    in_wave = [r for r in open_ if r["problem_id"] in wave]
    rest = [r for r in open_ if r["problem_id"] not in wave]
    # a node exists when the store names the problem id (the campaign's bundles write "(F0055)" into the statement)
    for r in ours:
        r["_node"] = bool(re.search(r"\b%s\b" % re.escape(r["problem_id"]), blob))
    rest.sort(key=lambda r: (LEDGER_RANK.get(r["_ledger"], 9),
                             0 if "partial" in str(r.get("current_status")) else 1, r["problem_id"]))
    with io.open(os.path.join(HERE, "SOLVED_NEEDS_NODE.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for r in ours:
            if not r["_node"]:
                fh.write(json.dumps({k: v for k, v in r.items() if not k.startswith("_") or k == "_ledger"},
                                    ensure_ascii=False) + "\n")
    with io.open(os.path.join(HERE, "QUEUE_ALL_OPEN.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        for k, r in enumerate(rest, 1):
            fh.write(json.dumps(brief(r, k), ensure_ascii=False) + "\n")
    lines = ["# Probability open problems: coverage (written by prob_cover.py)", "",
             "Rows in the seven intake ledgers: %d (distinct ids %d)." % (len(rows), len(by_id)), ""]
    lines += ["- %s: %d" % (k, v) for k, v in cls.most_common()]
    lines += ["- open and a 300-wave target: %d" % len(in_wave),
              "- open, not in the wave, queued in QUEUE_ALL_OPEN.jsonl: %d (by ledger %s)" % (
                  len(rest), dict(collections.Counter(r["_ledger"] for r in rest))),
              "- the P ledger (P0001..) survives only as recovered store nodes; its 10 wave targets are in the wave", "",
              "## Our results and their nodes", "", "| id | status | node in the math store | title |", "|---|---|---|---|"]
    for r in sorted(ours, key=lambda r: r["problem_id"]):
        lines.append("| %s | %s | %s | %s |" % (r["problem_id"], str(r.get("current_status"))[:32],
                                               "yes" if r["_node"] else "NO", str(r.get("title"))[:90].replace("|", "/")))
    io.open(os.path.join(HERE, "COVERAGE.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("\n".join(lines[:14]))
    print("our results %d, with a node %d, without %d" % (len(ours), sum(r["_node"] for r in ours),
                                                          sum(not r["_node"] for r in ours)))


def brief(r, k):
    src = {"source_id": r.get("source_id"), "locator": r.get("locator"),
           "historical_status": r.get("historical_status"), "current_status": r.get("current_status"),
           "status_search": str(r.get("status_search") or "")[:600]}
    prompt = (
        "Open problem %s (ledger %s, queue rank %d). Probability research; work yourself, no child agents.\n"
        "Title: %s\nStatement as recorded from the source: %s\nSource: %s, %s.\n"
        "Recorded status: %s. A recorded status is not a current-openness certificate.\n\n"
        "1. Status first (at most a fifth of your effort): find the papers that cite the source and search them for "
        "this problem; if it is solved, give the citation and stop with evidence_status=resolved_in_literature.\n"
        "2. Otherwise attack it: compute exact small cases or a numerical experiment, find the extremal or limiting "
        "family, then prove the claim or build a counterexample. A partial answer (a special case, a reduction, a "
        "corrected statement) is worth returning; say exactly what is proved.\n"
        "3. Return one self-contained JSON object: problem_id, source_checks, exact_statement, answer "
        "(yes/no/partial/open), proof_or_counterexample (complete, every step checkable), hardest_remaining_gap, "
        "evidence_status (proved / counterexample / partial / numerical / no progress / resolved_in_literature), "
        "draft_brain_nodes: a list of math-brain draft entries (key, namespace, logical_name, kind "
        "theorem|lemma|definition|concept, title, statement, proof_text for a theorem or lemma, assumptions, domain, "
        "source {source_id, url, revision, license 'owner-own-work (campaign result)' for our own proof}).\n"
        "Label conjecture, numerical evidence, sketch and proof separately. No solved claim without a complete "
        "proof; an independent reader of a different model family audits every result before it becomes a node."
    ) % (r["problem_id"], r["_ledger"], k, r.get("title"), r.get("statement"), r.get("source_id"), r.get("locator"),
         r.get("current_status"))
    return {"assignment_id": "open-%s" % r["problem_id"], "target_id": r["problem_id"], "queue_rank": k,
            "lane": "breadth-solve", "role": "solver", "model": "gpt-6.1-sol", "reasoning_effort": "max",
            "service_tier": "fast", "features": {"fast_mode": True}, "problem_statement": r.get("statement"),
            "title": r.get("title"), "source": src, "prompt": prompt}


if __name__ == "__main__":
    main()
