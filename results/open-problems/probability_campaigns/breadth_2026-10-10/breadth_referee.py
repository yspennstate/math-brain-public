# -*- coding: utf-8 -*-
"""From a breadth solver's answer to a math-brain node (claude-322bc92e, 10 Oct 2026, T-20261010-052: "add nodes to
the brain for the problems we solve"). For each results/<id>.txt that claims progress, one sealed Claude referee (another
model family than the GPT solver; claude_reader_s11.call, no tools, nothing saved) checks the answer against the problem
as recorded. KEEP answers have their draft_brain_nodes written to math-brain-inbox/codex-prob1000-breadth-1010/ as a
mathbrain-draft-v1 bundle, each statement opening with its provenance and review status; FIX and DROP are recorded and
go back to the queue's notes. resolved_in_literature answers are listed in LITERATURE.jsonl for the ledger.

    python breadth_referee.py            one pass over results/ (re-runnable; a verdict file is never redone)
"""
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
INBOX = "~/math-brain-inbox/codex-prob1000-breadth-1010"
sys.path.insert(0, "~/pd_work/pilot_pair")
import claude_reader_s11 as R  # noqa: E402

ASK = """You are an independent referee from a different model family than the author. Below are an open problem in
probability, as recorded from its source, and a solver's claimed answer. Check the answer line by line: does it address
the problem as stated (not an easier variant), are all hypotheses used and stated, does every step follow, is a
counterexample really a counterexample (check it satisfies every hypothesis), are constants and exponents right? Also
say whether you know of published work that already settles the question (authors, year), but judge the mathematics
on its own. Do not judge importance.

Give your reasons briefly, then end with exactly these lines:
VERDICT: KEEP | FIX | DROP     (KEEP: correct and complete for what it claims; FIX: right idea, a precise error - state the fix; DROP: wrong or not an answer)
CLAIM: <one sentence: exactly what is established, at the strength it is established>
LITERATURE: <a known paper that settles it, or none known>
"""


def parse(txt):
    m = re.search(r"\{.*\}", txt, re.S)
    if not m:
        return None
    s = m.group(0)
    for end in range(len(s), 0, -1):
        if s[end - 1] != "}":
            continue
        try:
            return json.loads(s[:end])
        except ValueError:
            continue
    return None


def rows():
    return {json.loads(l)["target_id"]: json.loads(l) for l in io.open(os.path.join(HERE, "QUEUE_ALL_OPEN.jsonl"),
                                                                          encoding="utf-8") if l.strip()}


def main():
    q = rows()
    os.makedirs(INBOX, exist_ok=True)
    keep_entries, lit, tally = [], [], {}
    for f in sorted(os.listdir(RESULTS)):
        if not f.endswith(".txt"):
            continue
        pid = f[:-4]
        txt = io.open(os.path.join(RESULTS, f), encoding="utf-8", errors="replace").read()
        j = parse(txt) or {}
        ev = str(j.get("evidence_status") or "").lower()
        tally[ev or "unparsed"] = tally.get(ev or "unparsed", 0) + 1
        if "literature" in ev:
            lit.append({"problem_id": pid, "answer": j.get("answer"), "source_checks": j.get("source_checks")})
            continue
        if not any(k in ev for k in ("proved", "counterexample", "partial")):
            continue
        vf = os.path.join(RESULTS, "%s.referee.md" % pid)
        if not os.path.exists(vf):
            r = q.get(pid, {})
            R.OUT = RESULTS
            out = R.call(ASK + "\n\n=== PROBLEM %s ===\nTitle: %s\nStatement: %s\nSource: %s\n\n=== CLAIMED ANSWER ===\n%s" % (
                pid, r.get("title"), r.get("problem_statement"), json.dumps(r.get("source"), ensure_ascii=False), txt))
            io.open(vf, "w", encoding="utf-8", newline="\n").write(str(out.get("result") or ""))
        ref = io.open(vf, encoding="utf-8").read()
        v = (re.findall(r"VERDICT:\s*(KEEP|FIX|DROP)", ref) or [None])[-1]
        claim = (re.findall(r"CLAIM:\s*(.+)", ref) or [""])[-1].strip()
        tally["referee " + str(v)] = tally.get("referee " + str(v), 0) + 1
        if v != "KEEP":
            continue
        for e in j.get("draft_brain_nodes") or []:
            if not isinstance(e, dict) or not e.get("statement"):
                continue
            e = dict(e)
            # the integrator takes only normalized lowercase keys and kebab logical names (10 Oct 10:0x refusal); the
            # problem id in front keeps keys from two solvers apart
            norm = lambda s: re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", str(s).lower())).strip("-")[:90]
            e["key"] = "%s-%s" % (pid.lower(), norm(e.get("key") or e.get("logical_name") or "result"))
            e["logical_name"] = "%s-%s" % (pid.lower(), norm(e.get("logical_name") or e["key"]))
            e["namespace"] = ".".join(norm(x).replace("-", "_") for x in str(e.get("namespace") or "probability.open_problems").split(".") if x)
            e["statement"] = ("[open-problem result %s, %s: GPT solver (Codex gpt-6.1-sol, max), Claude referee KEEP, not "
                              "refereed by a person; established: %s] %s" % (pid, time.strftime("%Y-%m-%d"), claim,
                                                                             e["statement"]))
            src = dict(e.get("source") or {})
            src.setdefault("source_id", "prob1000:%s" % pid)
            src["license"] = "owner-own-work (campaign result, attributed)"
            src.setdefault("revision", "as-solved-%s" % time.strftime("%Y-%m-%d"))
            if not src.get("url"):   # the integrator refuses an entry without one (10 Oct 10:0x, 13 of 13)
                ax = re.search(r"(\d{4}\.\d{4,5})", json.dumps(q.get(pid, {}).get("source") or {}))
                src["url"] = ("https://arxiv.org/abs/%s" % ax.group(1) if ax else
                              "https://github.com/yspennstate/math-open-problems/tree/master/probability_1000")
            e["source"] = src
            if e.get("kind") in ("theorem", "lemma") and not e.get("proof_text"):
                e["kind"], e["proof_text"] = "concept", None
            if e.get("kind") in ("definition", "concept"):
                e["proof_text"] = None
            keep_entries.append(e)
    if keep_entries:
        n = len([x for x in os.listdir(INBOX) if x.startswith("bundle_")]) + 1
        b = {"spec": "mathbrain-draft-v1", "author_agent": "codex-prob1000-breadth-1010",
             "bundle_slug": "prob1000-breadth-results-%03d" % n, "entries": keep_entries[:200], "relations": []}
        p = os.path.join(INBOX, "bundle_%03d.json" % n)
        io.open(p + ".part", "w", encoding="utf-8", newline="\n").write(json.dumps(b, ensure_ascii=False, indent=1))
        os.replace(p + ".part", p)
        print("bundle written:", p, len(keep_entries), "entries")
    if lit:
        with io.open(os.path.join(HERE, "LITERATURE.jsonl"), "w", encoding="utf-8", newline="\n") as fh:  # each pass covers every result
            for x in lit:
                fh.write(json.dumps(x, ensure_ascii=False) + "\n")
    print(json.dumps(tally, sort_keys=True))


if __name__ == "__main__":
    main()
