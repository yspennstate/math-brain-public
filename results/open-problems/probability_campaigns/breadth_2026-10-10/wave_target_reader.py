# -*- coding: utf-8 -*-
"""Cross-family labels for the 300-worker probability wave (claude-322bc92e, 10 Oct 2026; his 10:38 goal "classify it,
put it in the brain, make nodes and edges, review it and audit it"; claude-4a88bc43's ask that every pushed result
carry proved / partial / counterexample / draft with its verdict file). One sealed Claude read per TARGET (25), not per
worker (228 hold a claimed proof): the packet is every claim its workers label proved, independently checked or
counterexample, with each worker's ATTEMPT.md. Sequential, windowless when launched with pythonw; STOP_TARGET_READER
beside this file ends it after the current target; it ends by itself at 13:40.

Writes claude_labels/<target>.md (+ .response.json, the served model) and claude_labels/LABELS.jsonl (one row per claim).
"""
import io
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
WAVE = "~/brain_workers/teams/PROBABILITY300_20261010/ASSIGNMENTS.json"
OUT = os.path.join(HERE, "claude_labels")
sys.path.insert(0, "~/pd_work/pilot_pair")
import claude_reader_s11 as R  # noqa: E402

STRONG = re.compile(r"proved|independently checked|counterexample", re.I)
ASK = """You are an independent referee from a different model family than the authors (a GPT prover, adversary and
referee per approach). Below are the claims that a group of workers on ONE open problem labelled as proved, independently
checked or counterexample, each with its worker's attempt record. For EACH claim decide what it actually establishes:
PROVED (a complete, correct proof of exactly the stated claim), PARTIAL (a correct proof of something weaker: a special
case, a conditional result, a reduction - say which), COUNTEREXAMPLE (a correct counterexample meeting every hypothesis),
DRAFT (not established: a gap, an unproved step, an error, or an input that is missing - name it). Never upgrade a claim;
a claim about the famous open problem itself is DRAFT unless the proof is complete and checkable here.

Answer with one JSON object only, keyed by claim id: {"<claim_id>": {"label": "PROVED|PARTIAL|COUNTEREXAMPLE|DRAFT",
"verdict": "KEEP|FIX|DROP", "line_checked": "<the step the label rests on>", "note": "<one sentence>"}, ...}"""


def packet(target, workers):
    parts, claims = [], []
    for w in workers:
        d = "~/brain_workers/%s" % w
        rows = []
        if os.path.exists(d + "/CLAIMS.jsonl"):
            for line in io.open(d + "/CLAIMS.jsonl", encoding="utf-8", errors="replace"):
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if STRONG.search(str(r.get("status") or r.get("evidence_status") or "")):
                    r["_worker"] = w
                    r.setdefault("claim_id", r.get("id") or "%s-%d" % (w, len(rows) + 1))
                    rows.append(r)
        if not rows:
            continue
        claims += rows
        att = io.open(d + "/ATTEMPT.md", encoding="utf-8", errors="replace").read()[:40000] if os.path.exists(
            d + "/ATTEMPT.md") else "(no ATTEMPT.md)"
        parts.append("=== WORKER %s: claims ===\n%s\n=== WORKER %s: ATTEMPT.md ===\n%s" % (
            w, "\n".join(json.dumps(r, ensure_ascii=False)[:6000] for r in rows), w, att))
    return claims, "\n\n".join(parts)[:400000]


def main():
    os.makedirs(OUT, exist_ok=True)
    by_t = {}
    for a in json.load(io.open(WAVE, encoding="utf-8")):
        by_t.setdefault(a["target_id"], []).append(a["worker"])
    # REVERSE=1: a second copy takes the targets from the other end, so two run without picking the same one until they meet
    for t, ws in sorted(by_t.items(), reverse=bool(os.environ.get("REVERSE"))):
        if time.strftime("%H:%M") >= "13:40" or os.path.exists(os.path.join(HERE, "STOP_TARGET_READER")):
            break
        md = os.path.join(OUT, "%s.md" % t)
        if os.path.exists(md):
            continue
        claims, text = packet(t, ws)
        if not claims:
            continue
        R.OUT = OUT
        j = R.call(ASK + "\n\nOPEN PROBLEM " + t + "\n\n" + text, timeout=3600)
        if j.get("is_error") or j.get("_rc"):
            # 10 Oct 12:1x: two reads killed in flight (rc 143) wrote an empty 'done' file and were never retried
            print("read of %s failed (rc %s); left for a retry" % (t, j.get("_rc")), flush=True)
            continue
        res = str(j.get("result") or "")
        io.open(os.path.join(OUT, "%s.response.json" % t), "w", encoding="utf-8").write(json.dumps(j, ensure_ascii=False))
        io.open(md, "w", encoding="utf-8", newline="\n").write(
            "# %s: cross-family labels (sealed Claude, %s; served %s; %d claims read)\n\n%s\n" % (
                t, time.strftime("%Y-%m-%d %H:%M"), sorted((j.get("modelUsage") or {}).keys()), len(claims), res))
        m = re.search(r"\{.*\}", res, re.S)
        try:
            lab = json.loads(m.group(0)) if m else {}
        except ValueError:
            lab = {}
        with io.open(os.path.join(OUT, "LABELS.jsonl"), "a", encoding="utf-8", newline="\n") as fh:
            for c in claims:
                v = lab.get(str(c["claim_id"])) or {}
                fh.write(json.dumps({"target": t, "worker": c["_worker"], "claim_id": c["claim_id"],
                                     "worker_label": c.get("status"), "claude_label": v.get("label") or "UNREAD",
                                     "verdict": v.get("verdict"), "line_checked": v.get("line_checked"),
                                     "note": v.get("note")}, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
